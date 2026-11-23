---
name: rust-unsafe-ffi
description: Self-contained guide for unsafe Rust and foreign-function interfaces. Use when the change writes or reviews an `unsafe` block, raw pointers, `MaybeUninit`, `transmute`, `repr(C)` or packed layouts, `extern "C"` functions, C or C++ bindings (`bindgen`, `cbindgen`, `cxx`), exported C ABIs, Python or Node bindings, dynamic plugins, signal handlers, atomics and lock-free structures, or a hand-written `Future` with `Pin`. Not for ordinary application or library code, which should contain no unsafe at all.
---

# Unsafe Rust and FFI

Unsafe code is where the compiler stops checking and you start. A mistake here is not a
wrong answer but undefined behaviour: it can corrupt memory far from the bug, pass every
test, and appear only under optimisation or on another platform. The work is to keep the
unsafe part small, write down the invariant each block rests on, wrap it in an interface
that safe code cannot misuse, and check it with tools that can see what tests cannot.

## When to use this skill

- **Use it when** a change adds, edits or reviews `unsafe`, crosses a language boundary, exports an ABI, or builds a concurrency primitive from atomics.
- **Signals:** `unsafe`, `extern "C"`, `#[repr(C)]`, `#[unsafe(no_mangle)]` or `#[no_mangle]`, `*const` and `*mut`, `MaybeUninit`, `transmute`, `bindgen`, `cbindgen`, `cxx`, `pyo3`, `napi`, `libloading`, `Pin`, `Ordering::`.
- **Skip it when** a safe form exists. That is most of the time, and reaching for this skill should itself prompt the question.
- **It is complete on its own.** The Rust essentials, the gate commands and the definition of done are at the end.

## The defaults, in priority order

If unsure what matters most, work down the list.

1. **Look for the safe form first:** slices and iterators in place of pointer arithmetic, `bytemuck` or `zerocopy` in place of transmutes, `std` atomics and locks in place of hand-written ones.
2. **Every `unsafe` block has a `// SAFETY:` comment** naming the invariant and who upholds it. Every `unsafe fn` and unsafe trait has a `# Safety` section stating what the caller must guarantee.
3. **The unsafe part is small, private and behind a safe interface that is sound for every safe caller.** If safe code can cause undefined behaviour through your safe function, the function is unsound.
4. **Everything arriving over FFI is untrusted:** null pointers, lengths, enum discriminants, strings, alignment. Check before use.
5. **No panic crosses an FFI boundary.** Every exported function catches unwinding and returns an error code.
6. **One side allocates and the same side frees.** Ownership across the boundary is written in the signature's documentation.
7. **Unsafe for speed needs a measurement,** and is deleted when the gain is not there.
8. **Run the tools:** Miri for unsafe Rust, sanitizers where FFI is involved, `loom` for hand-written synchronisation, a fuzz target for anything parsing foreign bytes.

**How this kind of Rust differs from application Rust.** In a service, "it works and the
tests pass" is strong evidence. Here it is weak evidence: undefined behaviour can pass
every test. A claim of soundness rests on a written argument plus tool runs, and a review
reads each `SAFETY` comment against the code it covers.

**Defaults.**

- **Most code needs no `unsafe`.** Before writing it, look for a safe form: slices and iterators in place of pointer arithmetic, `bytemuck` or `zerocopy` in place of transmutes, `std` atomics and locks, a maintained `-sys` crate with a safe wrapper.
- **`unsafe` does not switch off the rules; it makes you the one who checks them.** Each block rests on an invariant the compiler cannot see. Write it down.
- **Keep it small, private and behind a safe API** whose every use is sound. If safe callers can cause undefined behaviour through your safe function, the function is unsound, however unlikely the call.
- **Unsafe as an optimisation needs a measurement.** `get_unchecked` to skip a bounds check is rarely worth it; restructuring into iterators usually removes the check safely.
- Application crates can set `#![forbid(unsafe_code)]`. Crates that need unsafe set `#![deny(unsafe_op_in_unsafe_fn)]` and `clippy::undocumented_unsafe_blocks`.

## Writing an unsafe block

```rust
/// Returns the element at `index` without a bounds check.
///
/// # Safety
///
/// `index` must be less than `self.len()`.
pub unsafe fn get_unchecked(&self, index: usize) -> &T {
    // SAFETY: the caller guarantees `index < self.len`, and `self.ptr` points to
    // `self.len` initialised elements for as long as `self` is borrowed.
    unsafe { &*self.ptr.as_ptr().add(index) }
}
```

- **An `unsafe fn` has a `# Safety` section** stating what the caller must guarantee. **Every `unsafe` block has a `// SAFETY:` comment** stating why those guarantees hold here. "This is safe" is not a reason; name the invariant and where it is established.
- **One unsafe operation per block where practical,** so each comment covers one claim.
- **The invariant lives in a type.** Fields that the unsafe code relies on are private, and every safe method preserves the invariant. The whole module is the trust boundary: any code that can touch those fields can break the unsafe block, even though it contains no `unsafe` itself.
- **An `unsafe trait`** is for a property that unsafe code elsewhere relies on (`Send`, `Sync`, "this layout is plain bytes"). The `unsafe impl` carries its own `SAFETY` comment.
- **Hand-written `unsafe impl Send` or `Sync` is a strong claim.** State why access from several threads is sound: the type owns its pointee exclusively, or every access is synchronised.

## What must always hold

| Rule | The usual violation |
|---|---|
| `&mut T` is unique; `&T` is not mutated (outside `UnsafeCell`) | two `&mut` made from one raw pointer; writing through a pointer while a `&` is live |
| A reference is non-null, aligned and points to a valid, initialised `T` | `&*ptr` on a null or dangling pointer; a reference to a `repr(packed)` field |
| Every value is valid for its type | a `bool` other than 0 or 1, an enum with an unknown discriminant, a `char` that is a surrogate, uninitialised integers |
| Pointer arithmetic stays within one allocation | `ptr.add(n)` past the end plus one |
| Memory is freed once, by the allocator that made it, with the same layout | `Box::from_raw` on a pointer from C's `malloc`; a `Vec` rebuilt with the wrong capacity |
| No data races | a `static mut` touched from two threads |

- **Breaking these is undefined behaviour even when the program appears to work.** The optimiser assumes they hold, so the failure can appear later, elsewhere, or only at another optimisation level.
- **Creating an invalid reference is already undefined behaviour,** used or not. Stay with raw pointers (`&raw const`, `&raw mut`, `ptr::read`, `ptr::write`) until a valid reference can be made.
- **`MaybeUninit<T>` for memory not yet initialised.** Write through `as_mut_ptr()` or `write()`, and call `assume_init` only after every part is written. Never make a `&mut T` or `&T` to it earlier. `mem::uninitialized` and `mem::zeroed` on a type with invalid zero bytes are always wrong.

```rust
let mut buffer = [const { MaybeUninit::<u8>::uninit() }; 4];
for (index, slot) in buffer.iter_mut().enumerate() {
    slot.write(index as u8);
}
// SAFETY: the loop above initialised all four elements.
let bytes: [u8; 4] = unsafe { mem::transmute(buffer) };
```

- **Panic safety.** If code between two unsafe steps can panic (a user closure, `clone`, an allocation), the unwind runs destructors over the half-finished state. Keep the structure valid at every panic point, or use a guard whose `Drop` repairs it. Setting a length before the elements are written is the classic mistake.
- **`static mut` is almost never right.** Use an atomic, a `Mutex`, `OnceLock`, or an `UnsafeCell` wrapper with a documented `Sync` argument.
- **`transmute` is the last resort.** Prefer `to_ne_bytes`/`from_ne_bytes`, pointer `cast`, `bytemuck`, or a `union`. Never transmute between types whose layout is unspecified, and never to extend a lifetime.

## The FFI boundary

**Only C-shaped types cross.** `&str`, `&[T]`, `String`, `Vec`, `&dyn Trait`, tuples and
default-layout structs have no stable ABI. Pass a pointer and a length; pass structs marked
`repr(C)`.

```rust
#[repr(C)]
pub struct ByteSlice {
    pub ptr: *const u8,
    pub len: usize,
}

/// # Safety
///
/// `input.ptr` must point to `input.len` readable bytes that are not modified during
/// the call. `out` must be valid for one write.
#[unsafe(no_mangle)] // `#[no_mangle]` before edition 2024
pub unsafe extern "C" fn lib_checksum(input: ByteSlice, out: *mut u64) -> i32 {
    let outcome = std::panic::catch_unwind(|| {
        if input.ptr.is_null() || out.is_null() {
            return Err(Status::NullPointer);
        }
        // SAFETY: non-null was checked; the caller guarantees the length and validity.
        let bytes = unsafe { std::slice::from_raw_parts(input.ptr, input.len) };
        let value = checksum(bytes).map_err(Status::from)?;
        // SAFETY: `out` is non-null and valid for one write by the caller's contract.
        unsafe { out.write(value) };
        Ok(())
    });
    match outcome {
        Ok(Ok(())) => 0,
        Ok(Err(status)) => status as i32,
        Err(_panic) => Status::Panic as i32,
    }
}
```

- **A panic never unwinds into foreign code.** Catch it at every exported function and every callback handed to C, and turn it into an error code. Since Rust 1.81 an uncaught panic leaving `extern "C"` aborts the process; before that it was undefined behaviour. `extern "C-unwind"` is only for a boundary where both sides have agreed to unwinding. With `panic = "abort"`, `catch_unwind` catches nothing, so know which profile ships.
- **Check every incoming pointer for null,** and treat every length, index and enum value from the other side as untrusted input.
- **Results go out through out-parameters and a status code.** Error detail comes from a "last error" function or an error out-parameter, never from a Rust type.
- **Nullable things are `Option<NonNull<T>>`, `Option<&T>` or `Option<extern "C" fn(...)>`.** These have the same representation as a nullable C pointer, and the type forces the check. No magic sentinel integers.
- **An integer from C is not yet a Rust enum.** An unknown discriminant is undefined behaviour the moment the enum value exists. Receive the integer and convert it with `TryFrom`. Give C-facing enums an explicit `#[repr(u8)]` or `#[repr(C)]` and explicit values.

**Layout.**

| Attribute | Use |
|---|---|
| `#[repr(C)]` | any struct, union or enum the other side reads or writes |
| `#[repr(transparent)]` | a newtype that must be passed exactly like its one field (`struct Fd(i32)`) |
| `#[repr(u8)]`, `#[repr(i32)]` | a field-less enum with a fixed integer size |
| `#[repr(align(N))]` | raise alignment, for example to a cache line to stop false sharing |
| `#[repr(packed)]` | match a packed C or wire layout; only when you must |

- The default layout is unspecified and may change between compiler versions; that freedom is why it packs best. Never rely on field order or size without a `repr`.
- **A reference to a packed field is undefined behaviour** because it may be unaligned. Copy the field out by value, or use `&raw const` and `read_unaligned`.
- Check layout assumptions at compile time: `const _: () = assert!(size_of::<Header>() == 16);`.
- For reading wire formats, parsing bytes into fields is usually simpler and safer than a packed struct overlay; `zerocopy` does the overlay safely when the speed matters.

**Ownership across the boundary.**

- **Memory is freed by the side that allocated it,** with that side's function. A string from the C library is copied and then released with the library's free; a Rust allocation handed to C comes back to Rust to be dropped.
- **An opaque handle** is `Box::into_raw(Box::new(value))` going out and `Box::from_raw` exactly once coming back, in an exported `destroy` function that accepts null.
- **Strings:** `CStr::from_ptr` borrows a NUL-terminated string from C; it is not necessarily UTF-8, so convert with `to_str()` and handle the error, or use `to_string_lossy()` knowingly. `CString::new` fails on an interior NUL. A `CString` given away with `into_raw` is reclaimed with `CString::from_raw`, never with C's `free`.
- **Never take `.as_ptr()` from a temporary.** `CString::new(name)?.as_ptr()` dangles at the end of the statement. Bind the owner to a variable that outlives the call. The same holds for a `Cow` or any buffer normalised for the call.
- **Callbacks** are an `extern "C" fn` plus a `*mut c_void` for user data. State who owns the user data, how long the callback may be called, and from which thread; that decides whether the data must be `Send`.

**A child handle borrows its parent.** The wrapper owns the raw pointer, keeps alive anything
the C side still points into, and carries the parent's lifetime in `PhantomData`.

```rust
pub struct RawIterator<'db> {
    inner: NonNull<ffi::iterator_t>,
    _options: ReadOptions,              // the C iterator points into this
    _database: PhantomData<&'db Database>, // cannot outlive the database
}

impl Drop for RawIterator<'_> {
    fn drop(&mut self) {
        // SAFETY: `inner` came from `iterator_create` and is destroyed only here.
        unsafe { ffi::iterator_destroy(self.inner.as_ptr()) }
    }
}
```

- A raw pointer field makes the type `!Send` and `!Sync`, which is the safe default. Add `unsafe impl Send` only after reading what the C library promises about threads.

**One helper for a C error out-parameter.** Copy the message, free it with the library's own
function, and convert to `Err`, in one place.

```rust
/// # Safety
///
/// `message` must be a NUL-terminated string allocated by the library.
pub(crate) unsafe fn take_error(message: *mut c_char) -> Error {
    // SAFETY: guaranteed by the caller.
    let text = unsafe { CStr::from_ptr(message) }.to_string_lossy().into_owned();
    // SAFETY: allocated by the library, so released by the library. Never Rust's allocator.
    unsafe { ffi::lib_free(message.cast()) };
    Error::new(text)
}

macro_rules! ffi_try {
    ($function:path, $($argument:expr),* $(,)?) => {{
        let mut error: *mut ::std::ffi::c_char = ::std::ptr::null_mut();
        let result = $function($($argument,)* &mut error);
        if !error.is_null() {
            return Err(unsafe { $crate::take_error(error) });
        }
        result
    }};
}
```

**Crate layout.** Raw bindings live in a `foo-sys` crate with `links = "foo"` in its manifest
and a build script that finds or builds the library; it contains declarations and nothing
else. A separate `foo` crate depends on it and exposes the safe API. Generate bindings with
`bindgen` (and headers for a Rust library with `cbindgen`) so that declarations cannot drift
from the header; a hand-written signature that disagrees with the C one is undefined
behaviour that no tool reports.

- **Keep the public API's constraints in safe types and the unchecked path private.** The implementation takes a fast path (`get_unchecked`, a flat loop over contiguous storage) only after it has established the shape that makes it valid, and falls back to the checked path otherwise.

## Containing unsafe in larger designs

**Checked constructor first; an unchecked twin only after profiling.**

```rust
impl SortedIds {
    pub fn try_new(ids: Vec<u32>) -> Result<Self, NotSorted> {
        if ids.is_sorted() { Ok(Self { ids }) } else { Err(NotSorted) }
    }

    /// # Safety
    ///
    /// `ids` must be sorted ascending: exactly what `try_new` checks.
    pub unsafe fn new_unchecked(ids: Vec<u32>) -> Self {
        debug_assert!(ids.is_sorted());
        Self { ids }
    }
}
```

- Add the unchecked form only when a profile shows validation repeated on data already proven valid. Its preconditions are exactly the checks of the safe one, and each call site says why they hold.
- A `debug_assert!` of the precondition inside the unchecked function catches wrong callers in tests at no release cost.
- **It needs `unsafe` only if breaking the invariant can cause undefined behaviour** (other code skips bounds checks on the strength of it). If a broken invariant merely gives wrong answers, name it `new_unchecked` without `unsafe`, or better, drop it.
- Never call the unchecked form to make an error go away.

**Smaller rules.**

- **A trait whose answers unsafe code trusts is an `unsafe trait`.** If a fast path believes `is_contiguous()` or `len()` and skips checks, a wrong implementation is undefined behaviour, so implementing it must be an explicit promise.
- **One narrow type owns raw allocation.** If raw buffers are needed at all, one small struct holds the pointer, length and `Layout`, and is the only code that calls the allocator and frees in `Drop`. Prefer `Vec`, `Box<[T]>` or an established buffer crate; zero-size and overflowing layouts are easy to get wrong.
- **At an exported entry point, in order:** set out-parameters to null or zero, convert opaque pointers to references once, validate every size and relation between the arguments, then work. A failed call then leaves nothing uninitialised for the caller to read.
- **Low-level copy and bit-packing routines** keep their separate fast paths (tiny, byte-aligned, unaligned). Do not simplify one without benchmarks and tests for zero, tiny, aligned, unaligned and boundary-spanning ranges.
- **Owned or borrowed, for every function of a C API.** Write the owning wrapper, whose `Drop` calls the matching release function, before any logic. An owning wrapper around a borrowed handle is a double free. RAII settles lifetime, not thread safety.
- **Unsafe wrapping in one place.** When a typed wrapper is only valid for raw values produced by a particular object (a match from *this* query, an index into *this* arena), one `unsafe fn wrap` does the pairing and the public iterator always supplies the right pair, so callers stay safe.

**Bindings for another language over a Rust core.**

- **The binding layer is thin:** convert inputs, call the core, wrap the result. It has no behaviour of its own, so the core is tested without the host language.
- **Errors cross through one pair of conversions,** core error to host exception and back, not an ad hoc `map_err` per function. A host exception that passes through Rust comes out as the original exception. Interrupts and cancellation keep their identity; they are not wrapped as generic failures.
- **Host control signals become a typed value at the boundary;** every other exception propagates unchanged.

```rust
match callback_result {
    Ok(_) => Ok(Control::Continue),
    Err(error) if error.is_instance_of::<PruneSearch>(py) => Ok(Control::Prune),
    Err(error) if error.is_instance_of::<StopSearch>(py) => Ok(Control::Stop),
    Err(error) => Err(error), // never swallow an unknown exception as control flow
}
```

- **Cross the boundary once, before going parallel.** Call every host callback and validate every value (NaN, negative weights) up front on the calling thread, into a plain table. The parallel section touches only native data and never calls back into the host runtime, which avoids its global lock and its exceptions inside worker threads. *Not when* the callback depends on traversal state or must be lazy.
- **Model the host's scope protocol as states.** For a context manager or similar: `Pending`, `Entered`, `Finalized`. Re-entry and use after finalisation return an error; they never touch released state.
- **Field order is drop order.** When a wrapper holds a resource and the owner it depends on, the dependent field comes first, with a comment saying the order is load-bearing.

```rust
struct ActiveWrite {
    transaction: WriteTransaction, // must drop before `database`: declared first on purpose
    database: Py<Database>,
}
```

**Dynamic-library plugins.** Rust has no stable ABI. A plugin exposing Rust types is valid
only when built by the same compiler version, for the same target, against the same API
version.

```rust
fn check_compatible(plugin: &BuildInfo, host: &BuildInfo) -> Result<(), PluginError> {
    if plugin.api_version != host.api_version {
        return Err(PluginError::ApiMismatch);
    }
    if plugin.rustc != host.rustc {
        return Err(PluginError::CompilerMismatch);
    }
    if plugin.target != host.target {
        return Err(PluginError::TargetMismatch);
    }
    Ok(())
}
```

- **The build-info query is itself a C-ABI function returning plain data,** and it is the first thing called. Nothing else in the library runs until it passes.
- Both sides must allocate and free with the same allocator; the host passes its own, or ownership never crosses.
- **Unloading is not safe in general:** any vtable, `'static` string or thread from the plugin dangles afterwards. Leak the library deliberately and accept that "reload" keeps the old code mapped.
- **Prefer alternatives.** A C-ABI interface (`abi_stable` or hand-written), WebAssembly, or a separate process over IPC all give versioning and isolation that a Rust-ABI `dylib` cannot. Untrusted plugins always run sandboxed or out of process; a loaded library has the host's full privileges.
- **A binding mirrors the C library's supported ABI version range** and checks a loaded artefact against it before use.

## Fixed layouts, exported ABIs and handlers

**A fixed binary header is checked at compile time and validated after the cast.** For a
fixed-width network, disk or shared-memory record read by reinterpreting bytes:

```rust
pub const HEADER_SIZE: usize = 256;

#[repr(C)]
#[derive(Debug, Clone, Copy, CheckedBitPattern, NoUninit)]
pub struct Header {
    pub magic: [u8; 4],
    pub version: u32,
    pub kind: RecordKind, // #[repr(u8)], also CheckedBitPattern
    _reserved: [u8; 247],
}

const _: () = {
    assert!(size_of::<Header>() == HEADER_SIZE);
    assert!(offset_of!(Header, kind) == 8);
};

let header: &Header = bytemuck::checked::try_from_bytes(&buffer[..HEADER_SIZE])?;
header.validate()?; // magic, version range, lengths within the file
```

- `NoUninit` refuses a struct with padding, so no uninitialised byte is ever written out. `CheckedBitPattern` rejects bytes that are not a valid `bool` or enum value, where a plain cast would be undefined behaviour.
- **The cast proves only that the bytes are a valid `Header`.** A `validate()` step checks meaning before any field is used: magic, version, and every length and offset against the real buffer size.
- **Decide endianness.** A byte cast reads native-endian integers. Store explicitly little-endian fields (`zerocopy`'s byte-order types, or `from_le_bytes` on read) if the data crosses machines. The cast also needs the buffer aligned for the struct; `try_from_bytes` fails otherwise, and `pod_read_unaligned` copies instead.
- Changing the header changes the assertions and the invalid-byte tests in the same commit.
- *Not for* formats that must grow. Those want a length-prefixed or tagged encoding, parsed field by field.

**A C ABI exported from Rust** publishes opaque handles and status codes, never a Rust struct
layout.

- Every handle has a `create` and a `destroy`. Every function returns a status enum with fixed values: zero for success, negative for errors, stable across releases.
- Callers never see inside a handle; the header declares `typedef struct lib_session lib_session;` and nothing more. In the other direction, never reach into a C library's private struct.
- For overload-like convenience, generate one real typed symbol per type with a macro, and put any generic facade on the Rust side.
- The header is generated (`cbindgen`) and checked in CI for freshness.

**Generated bindings and files.**

- A generated file begins with a header naming its generator and the command that regenerates it. Nobody edits it by hand. CI regenerates and fails on a difference.
- Review the generator and one representative output, not thousands of generated lines; generated code hides a bad abstraction well.
- **One core, many languages:** a single interface definition generates every language's package around the same opaque core type (`uniffi`, or per-language tools such as `pyo3` and `napi-rs` driven from one definition). A new method goes into the definition and into each language's end-to-end tests, never by hand into one package.
- **A blocking host method that drives an async Rust future** releases the interpreter lock while it waits, checks for interrupts so Ctrl-C works, and says in its documentation that it blocks.
- **Bulk data crosses in a columnar or batch format** (Arrow's C data interface, a byte buffer), not as one host object per record. Per-record crossings dominate the run time.

**Untrusted extension code runs in a sandbox behind a byte protocol.** With WebAssembly, the
host owns a small protocol: serialised input in, bytes out, explicit registration of what
may be called.

- Every call is fallible I/O: it can trap, time out or return nonsense. Give it fuel or a deadline and a memory limit, and validate the output like any external input.
- Each host function or WASI capability you grant widens the sandbox. Do not call it a security boundary without reviewing what is exposed.
- Trusted first-party extensions are plain Rust; the sandbox is a cost paid only for code you do not control.

**A crash signal handler reports once and re-raises.**

```rust
extern "C" fn on_fatal_signal(signal: i32) {
    static ENTERED: AtomicBool = AtomicBool::new(false);
    if !ENTERED.swap(true, Ordering::SeqCst) {
        // One minimal write(2) to stderr. Nothing else.
    }
    restore_default_and_reraise(signal); // sigaction(SIG_DFL), then raise
}
```

- Re-raising with the default disposition lets the shell and core-dump tooling see the real termination. The atomic guard stops recursion if the handler itself faults.
- **Almost nothing is safe inside a signal handler:** no allocation, no locks, no logging framework, no `println!`. A backtrace allocates; printing one is a knowing compromise. No recovery logic belongs there.
- **For ordinary shutdown signals, do not write a handler.** Use `tokio::signal` or `signal-hook`, which only set a flag or wake a task; the real work runs in normal code.

**Typed arena handles with a niche.**

```rust
pub struct Handle<T> {
    index: NonZeroU32,
    _marker: PhantomData<fn() -> T>,
}

impl<T> Clone for Handle<T> {
    fn clone(&self) -> Self {
        *self
    }
}
impl<T> Copy for Handle<T> {}
```

- `NonZeroU32` makes `Option<Handle<T>>` four bytes. Store `index + 1`, or reserve slot zero, so that zero never names an element.
- The type parameter stops a `Handle<Expr>` being used where a `Handle<Type>` is expected. It does not stop a handle from one arena being used with another arena of the same type; that needs a generation or arena id, checked in debug builds.
- **Implement `Clone`, `Copy`, `PartialEq`, `Eq` and `Hash` by hand.** A derive would add `T: Clone` and the rest, which the handle does not need.
- `PhantomData<fn() -> T>` keeps the handle `Send` and `Sync` whatever `T` is, and tells the compiler the handle does not own a `T`.
- This is entirely safe code. Indices plus an arena are the usual way to avoid unsafe pointer graphs.

## Wrappers around native handles

**Early close is idempotent.** Normally the owning wrapper frees its native peer once, in
`Drop`. Where a handle must also be closable early, as in bindings for a garbage-collected
language, hold it as an `Option` and let exactly one function free it.

```rust
pub struct Parser {
    raw: Option<NonNull<ffi::Parser>>,
}

impl Parser {
    pub fn close(&mut self) {
        if let Some(raw) = self.raw.take() {
            // SAFETY: `raw` came from `ffi::parser_new`, and `take()` means it is freed once.
            unsafe { ffi::parser_free(raw.as_ptr()) }
        }
    }

    fn handle(&self) -> Result<NonNull<ffi::Parser>, Error> {
        self.raw.ok_or(Error::Closed)
    }
}

impl Drop for Parser {
    fn drop(&mut self) {
        self.close();
    }
}
```

- Every public method goes through `handle()` and returns a "closed" error; none touches a freed peer.
- A wrapper that may hold either an owned or a borrowed handle records which, and never frees a borrowed one.
- An atomic pointer makes reading the pointer atomic. It does not make the native object thread-safe.
- In plain Rust code, prefer consuming `self` in `close(self)`: use after close then fails to compile and no closed state exists.

**One gateway for foreign status codes.** Every call into a C library that returns an integer
status passes through one function that turns the code into a typed status and then a domain
error. The library's detailed message is fetched lazily, on failure only.

```rust
fn check(code: ffi::Status, detail: impl FnOnce() -> String) -> Result<(), NativeError> {
    match Status::try_from(code) {
        Ok(Status::Success) => Ok(()),
        Ok(status) => Err(NativeError::new(status, detail())),
        Err(_) => Err(NativeError::unknown_code(code)),
    }
}
```

- Call sites never compare raw integers, and a code the binding does not know is an error of its own, not a success and not a panic.

**One closed enum owns a set of native bindings.** When a fixed set of native components is
linked in (grammars, codecs, drivers), one enum is the only code that calls their `extern`
constructors, and it also drives listing, parsing of names and display.

```rust
impl Language {
    pub fn grammar(self) -> tree_sitter::Language {
        // SAFETY: each function returns a pointer to a static grammar linked into this binary.
        unsafe {
            match self {
                Language::Go => tree_sitter_go(),
                Language::Rust => tree_sitter_rust(),
                Language::TypeScript => tree_sitter_typescript(),
            }
        }
    }
}
```

- No wildcard arm, so a new variant does not compile until it is wired. Components loaded at run time need a registry instead.

**Smaller rules.**

- **One native artefact, thin loaders.** A native library used from several runtimes is one core product with a minimal loader per runtime. Each loader has the same smallest test, "the library loads here", written before any behaviour test. It catches packaging and link failures and says nothing about correctness, which is tested once, in the core.
- **A native binding must pay for itself.** It is justified when the hot operation's cost outweighs the build, packaging and safety burden of the binding.
- **Raw-pointer containers** (intrusive lists, linked nodes) sit behind a narrow set of typed operations written once, as a generic or a macro. The raw form never leaks out of its module. Try an arena with indices first.
- **Arena handles do not survive a rebuild of the arena.** Either the arena never moves or reuses slots, or handles carry a generation that is checked.

## More handle and callback rules

**A typed wrapper keeps its library context alive.** The wrapper holds the raw handle, an
`Arc` of the context the handle belongs to, and the element type as `PhantomData<T>`. `Drop`
frees the handle; the `Arc` guarantees the context is still there when it does.

```rust
pub struct SparseMatrix<T: ValueType> {
    context: Arc<Context>,
    raw: ffi::Matrix,
    _element: PhantomData<T>,
}

impl<T: ValueType> SparseMatrix<T> {
    /// Gives up ownership. The caller must free the handle while the context lives.
    pub fn into_raw(self) -> (ffi::Matrix, Arc<Context>) {
        let this = ManuallyDrop::new(self);
        // SAFETY: `this` is never dropped, so the `Arc` is moved out exactly once.
        (this.raw, unsafe { ptr::read(&this.context) })
    }
}
```

- Handing ownership out is safe, like `Box::into_raw`; taking a raw handle back in (`from_raw`) is the `unsafe` direction, because the caller vouches for where it came from.
- A handle borrowed from another owner gets a separate borrowed wrapper with a lifetime, and no `Drop`.
- Review drop, clone, extraction and the context's lifetime together, and re-justify each `unsafe impl Send` or `Sync` when any of them changes.

**One opaque Rust type per kind of foreign object,** so two handle types cannot be passed for
each other.

```rust
#[repr(C)]
pub struct Store {
    _data: [u8; 0],
    _marker: PhantomData<(*mut u8, PhantomPinned)>,
}

pub type StoreRef = *const Store;
```

- The marker makes the type `!Send`, `!Sync` and `!Unpin`, and it can never be constructed or read in Rust. Take integer and boolean widths from the `-sys` crate's typedefs (`c_int`, `c_long`), never from a guess: `long` is 32 bits on Windows.

**A closure handed to a C library** that takes a function pointer and a user-data pointer:

- Box a context struct holding the closure and anything it must keep alive. Pass `Box::into_raw` as the user data, and register an `extern "C"` trampoline that casts the pointer back and calls the closure inside `catch_unwind`.
- **Reclaim the box with `Box::from_raw` in exactly one place,** reached both when the callback is replaced and when the owner is dropped. Clear the registration in the C library first, so it never holds a dangling pointer.
- If the library may call from another thread, the closure must be `Send`; say so in the bound.
- **State for a single-threaded host** (an editor's scripting engine, a UI thread) can be `Rc<RefCell<T>>`. The wrapper is then `!Send`, which is the correct statement of the host's rule. Do not reach for `Arc<Mutex<T>>` to quiet the compiler.
- Positions crossing such a boundary are newtypes converted at the edge; the two sides often count in different units (bytes, UTF-16 units, characters).

**A synchronous foreign surface shares one runtime.** When the host cannot await a Rust
future, the FFI library holds one process-wide runtime and each exported method calls
`block_on` on it. No exported method builds its own.

```rust
static RUNTIME: LazyLock<tokio::runtime::Runtime> = LazyLock::new(|| {
    tokio::runtime::Builder::new_multi_thread()
        .enable_all()
        .build()
        .expect("tokio runtime for the FFI layer")
});

impl Client {
    pub fn connect(&self) -> Result<(), ClientError> {
        RUNTIME.block_on(self.inner.connect())
    }
}
```

- This belongs at the FFI edge only. Calling `block_on` from inside async code panics or deadlocks; a callback that re-enters an exported method from a runtime thread hits exactly that.

**Smaller rules.**

- **Resources in a managed runtime** (a JVM object behind a global reference) are owned by a Rust wrapper. Scope-bound local references never leave it. `Drop` closes the resource and logs a failure; it never panics.
- **`Drop` does not run on abort, `SIGKILL` or power loss.** A type that creates a temporary system resource (a mount, a keychain, a lock file) also offers explicit clean-up, and start-up removes leftovers from a previous crashed run.
- **Generated C is not held to your warning policy.** When a build script compiles generated code with `cc`, turn warnings off for that unit.
- **A binding crate tests every public member on every target it claims.** A binding that passes on the host can fail under another ABI. Tests that share one native object do not depend on order.
- **A binding generator evaluates C constants in a wide type** (`i128`) and narrows at the end, with a fixture per expression form. A macro it cannot evaluate is skipped with a diagnostic, never emitted as a wrong constant.
- **The core `run` function takes its arguments as parameters,** not from `std::env::args()`, so a binding and the command-line binary share one implementation.

**Verification for unsafe code.**

| Tool | Finds |
|---|---|
| `cargo +nightly miri test` | aliasing violations, use of uninitialised memory, out-of-bounds and use-after-free, in what the tests execute. Cannot run foreign code. |
| AddressSanitizer, ThreadSanitizer | memory errors and data races across the FFI boundary |
| `cargo fuzz` | inputs that reach a bad state in parsers and decoders |
| `loom` | interleavings of small concurrent models |
| `cargo geiger`, `cargo-careful` | where unsafe is; extra standard-library checks |

- Miri and sanitizers only judge the paths the tests take, so the tests must cover empty, one-element, boundary and error cases. A clean run is evidence, not proof.

## Atomics and lock-free code

**A read followed by a write is not atomic, whatever the orderings.**

```rust
// Lost update: two threads can both read 5 and both store 6.
let current = counter.load(Ordering::Acquire);
counter.store(current + 1, Ordering::Release);

// One atomic operation.
counter.fetch_add(1, Ordering::Relaxed);

// A conditional update: retry until no one else changed it in between.
let mut current = high_water.load(Ordering::Relaxed);
while candidate > current {
    match high_water.compare_exchange_weak(
        current,
        candidate,
        Ordering::Relaxed,
        Ordering::Relaxed,
    ) {
        Ok(_) => break,
        Err(actual) => current = actual,
    }
}
```

- Use the single-operation forms: `fetch_add`, `fetch_max`, `fetch_update`, `swap`, `compare_exchange`. Orderings govern what other memory becomes visible; they do not join two operations into one.
- `compare_exchange_weak` may fail spuriously and belongs in a loop; the strong form is for a single attempt.
- **A fence or an atomic store does not make plain data shareable.** Non-atomic mutable state reached from two threads needs a lock or an atomic of its own, or it is a data race and undefined behaviour.
- **Do not hand-roll a spin lock, a lock-free queue or memory reclamation.** Use `Mutex`, `crossbeam`'s queues and deques, `crossbeam-epoch` for deferred reclamation, and `AtomicCell` for a small `Copy` slot. Freeing a node another thread may still be reading is the classic lock-free bug, and it passes most tests.
- **Lock-free is not automatically faster.** An uncontended mutex costs a few nanoseconds. Go lock-free only when a profile shows contention on that lock, and after trying to shrink the critical section, shard the data, or give each thread its own copy.
- A `loom` test joins its threads and asserts the invariant; without the assertion it checks nothing. No timers, randomness or I/O inside the model.
- `std::sync::OnceLock` and `LazyLock` replace `lazy_static!` and most of `once_cell`; reach for the crates only to support an older toolchain.

### Lock order

**Lock ranks, checked in debug builds.** When a component has more than a handful of locks,
"one documented order" stops being checkable by reading. Give each lock a rank and assert on
every acquisition that it is higher than every rank the thread already holds.

```rust
#[cfg(debug_assertions)]
thread_local! {
    static HELD: RefCell<Vec<LockRank>> = const { RefCell::new(Vec::new()) };
}

pub struct RankedMutex<T> {
    rank: LockRank,
    inner: Mutex<T>,
}

pub struct RankedGuard<'a, T> {
    guard: MutexGuard<'a, T>,
    rank: LockRank,
}

impl<T> RankedMutex<T> {
    pub fn lock(&self) -> RankedGuard<'_, T> {
        // Checked before blocking, so a violation panics instead of deadlocking.
        #[cfg(debug_assertions)]
        HELD.with(|held| {
            let mut held = held.borrow_mut();
            assert!(
                held.iter().all(|other| *other < self.rank),
                "lock order violation: {:?} taken while holding {:?}",
                self.rank,
                held
            );
            held.push(self.rank);
        });
        RankedGuard {
            guard: self.inner.lock().unwrap_or_else(PoisonError::into_inner),
            rank: self.rank,
        }
    }
}

impl<T> Drop for RankedGuard<'_, T> {
    fn drop(&mut self) {
        #[cfg(debug_assertions)]
        HELD.with(|held| {
            let mut held = held.borrow_mut();
            if let Some(position) = held.iter().rposition(|other| *other == self.rank) {
                held.remove(position);
            }
        });
    }
}
```

- The check fires on the first run that takes locks in a bad order, even when no deadlock happens that time. That is its whole value: a deadlock needs an unlucky interleaving, a rank violation does not.
- Every lock gets a rank when it is added. One unranked lock makes the check meaningless.
- It is per-thread, so it does not see a guard held across `.await` on another thread; that case is already forbidden.
- For two or three locks, a comment stating the order is enough.

## Pin and hand-written futures

Most code never needs this. `async fn`, `tokio::pin!` and `Box::pin` cover nearly everything.

- **Project pinned fields with `pin-project-lite`,** never by hand and never with `Pin::new_unchecked` without a written proof.

```rust
pin_project_lite::pin_project! {
    pub struct Timed<F> {
        #[pin]
        inner: F,
        started: Instant,
    }
}

impl<F: Future> Future for Timed<F> {
    type Output = (F::Output, Duration);

    fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output> {
        let this = self.project();
        let output = std::task::ready!(this.inner.poll(cx));
        Poll::Ready((output, this.started.elapsed()))
    }
}
```

- **The `Pending` contract:** return `Poll::Pending` only after something has been arranged to wake the task (usually by polling an inner future that registered the waker). Returning `Pending` without that hangs forever; calling `wake` immediately and returning `Pending` is a busy loop.
- Do not poll a future again after it returned `Ready` unless it is documented as fused.
- *Prefer* an `async` block or a combinator. Write a manual `Future` only for a leaf primitive or when the state machine must be named and stored.

## Tests and tools

A stress test that passes has only failed to find a problem. Use the tool that can see
the class of defect:

| Risk | Tool | What it cannot see |
|---|---|---|
| Aliasing, uninitialised memory, out-of-bounds, use after free in Rust code | `cargo +nightly miri test` | Paths the tests do not run; most FFI calls |
| Memory errors across the FFI boundary | AddressSanitizer on both sides | Errors on paths not exercised |
| Data races | ThreadSanitizer; `loom` for a small state machine on atomics and locks | Async I/O; anything outside the modelled code |
| Malformed foreign bytes | `cargo fuzz` | Semantic errors with no crash or assertion |
| Layout assumptions | `const` assertions on `size_of` and `align_of`; binding tests on each target ABI | Behaviour |

**Concurrency: a stress run is a smoke check, a model is a proof.**

```rust
#[tokio::test(flavor = "multi_thread", worker_threads = 4)]
async fn req_005_no_lost_updates_under_load() -> anyhow::Result<()> {
    let counter = Arc::new(Counter::default());

    let tasks: Vec<_> = (0..100)
        .map(|_| {
            let counter = Arc::clone(&counter);
            tokio::spawn(async move { counter.increment().await })
        })
        .collect();
    for task in tasks {
        task.await??;
    }

    assert_eq!(counter.get().await, 100);
    Ok(())
}
```

- Assert the final state, not only that every task returned `Ok`. One hundred successful tasks and a lost update is exactly the bug.
- The default `#[tokio::test]` runtime is single-threaded; real parallelism needs `flavor = "multi_thread"`.
- This sees only the schedules the runtime happened to choose. Where the order of operations on shared state matters, model it:

```rust
#[cfg(loom)]
#[test]
fn req_005_two_writers_never_lose_an_update() {
    loom::model(|| {
        let counter = loom::sync::Arc::new(Counter::default());
        let other = counter.clone();
        let handle = loom::thread::spawn(move || other.increment());
        counter.increment();
        handle.join().unwrap();
        assert_eq!(counter.get(), 2);
    });
}
```

- `loom` explores every interleaving, so the model must be tiny: two or three threads and a few operations. The code under test must use `loom`'s `sync` and `atomic` types behind a `cfg`, and it runs with `RUSTFLAGS="--cfg loom"`.
- `loom` does not fit code that does real I/O or uses an async runtime. A stress test is the legitimate fallback there; write down that it is a substitute and why.
- A limit stated in a requirement (retries, concurrency, queue depth) has a test that reaches it.
- **Test that nothing is left running.** After shutdown, every spawned task has been joined or aborted. No detached task survives its owner.

**Layout claims as tests.** When a size or an identity is part of the design (a cache-line
budget, an interning guarantee, a niche-optimised `Option`), pin it.

```rust
#[test]
fn node_layout_stays_within_budget() {
    assert!(std::mem::size_of::<Node>() <= 64, "Node must fit one cache line");
    assert_eq!(std::mem::size_of::<Option<NodeId>>(), std::mem::size_of::<NodeId>());
}

#[test]
fn interning_returns_the_same_allocation() {
    let a = Interned::new("common_name");
    let b = Interned::new("common_name");
    assert!(std::ptr::eq(a.as_str(), b.as_str()));
}
```

- Prefer an upper bound (`<=`) to an exact size unless the exact size is the contract (FFI, an on-disk format). Exact sizes differ between 32-bit and 64-bit targets and may change with the compiler for `repr(Rust)` types.
- For a hard guarantee, check at compile time: `const _: () = assert!(std::mem::size_of::<Node>() <= 64);`.
- *Skip* for types whose size nobody depends on; the test then only blocks harmless refactors.

**Fuzzing, for anything that takes bytes from outside.**

```rust
#![no_main]
use libfuzzer_sys::fuzz_target;

fuzz_target!(|data: &[u8]| {
    if let Ok(value) = my_crate::parse(data) {
        // Not only "does not panic": what parsed must survive a round trip.
        let again = my_crate::parse(&value.to_bytes()).expect("re-parse of own output");
        assert_eq!(value, again);
    }
});
```

- A target that only ignores the result finds panics, overflows (in debug) and hangs. Add an assertion and it finds logic errors: a round trip, agreement with a reference implementation, an invariant on the output.
- Seed the corpus with real inputs, and keep it. Every crash becomes a checked-in regression test with the minimised input.
- For structured input derive `arbitrary::Arbitrary` instead of hand-decoding bytes.
- Run it with a time limit on a schedule, not on every push. Set a per-input timeout and a memory limit so a hang or an allocation bomb is reported as a finding.
- *Use for* parsers, decoders, decompressors, protocol state machines, and unsafe code reachable from input. *Skip for* code whose input is already a validated domain type.

## Review

- Does every `unsafe` block have a `SAFETY` comment that names an invariant, and does the code around it uphold that invariant on every path, including panics and early returns?
- Can any safe caller, however odd, reach undefined behaviour through a safe function?
- Is every pointer, length and discriminant from the foreign side checked before use?
- Does every exported function catch unwinding?
- Is it written down which side allocates and which side frees each value?
- Are `Send` and `Sync` implemented by hand anywhere, and is the argument for each written beside it?
- Which tool runs cover the change (Miri, sanitizers, `loom`, fuzzing), and which were skipped and why?
- If the unsafe code is an optimisation, where is the measurement?

**Reject by default:** `unsafe` to get round the borrow checker; `transmute` where a cast or
a `bytemuck` call works; a reference to a packed field; a `static mut`; a foreign integer
cast straight to a Rust enum; a callback that can unwind into C; memory freed by a
different allocator from the one that allocated it; anything but async-signal-safe work in
a signal handler.

## Out of scope

- **Compiler internals, kernel-grade lock-free algorithms and deeply embedded firmware.** They need specialist material beyond this skill.
- **The safe code around the unsafe core.** Write it with the skill for its kind of Rust (library, service, infra).
- **The foreign library's own correctness.** This skill covers the boundary, not what lies beyond it.

<!-- essentials:begin -->
## Rust essentials shared by every writer skill

This block is the same in every Rust writer skill. It holds the language-level rules that
decide whether Rust code is correct whatever it is for: ownership, types at boundaries,
errors, async, tests and the anti-patterns to reject. Where the skill above states a rule
for its own kind of Rust more firmly, that statement wins.

### Ownership and borrowing

**Defaults.**

- Borrow to read, take ownership to keep, `&mut` to change in place. The signature tells the caller which.
- Clone when the design calls for a second owner, not to make an error go away. A clone of a small value on a cold path is fine and often the clearest code; a clone in a loop over large data is worth a second look.
- `Arc` for shared ownership across threads, `Rc` within one. Neither is a substitute for deciding who owns the data.
- Hold locks and `RefCell` borrows for the shortest scope that is correct, and never across an `.await`.

**The error usually describes a real overlap.** Find which borrow is still alive and why,
then shorten it, instead of reaching for `clone` or `Rc<RefCell<_>>`.

```rust
// Rejected: first borrows items while push needs it mutably.
let first = &items[0];
items.push(first.clone());

// End the shared borrow before the mutation.
let first = items[0].clone();
items.push(first);
```

- **A method borrows all of `self`.** Calling `self.helper()` while a field is borrowed fails even if the helper touches other fields. Borrow the fields separately, which the compiler tracks, or make the helper take the fields it needs.

```rust
let Self { index, scratch, .. } = self;
for id in index.keys() {
    scratch.push(*id); // index is borrowed shared, scratch mutably: disjoint fields
}
```

- **Collect, then mutate.** Gather the keys or indices to change in one pass and apply them in a second. Often clearer as well as accepted.
- **Use indices or IDs instead of long-lived references** into a collection that also needs mutation. This is the normal shape for graphs and trees with parent links.
- **Move out through `&mut` with `std::mem::take`, `replace` or `Option::take`,** instead of cloning a field in order to consume it.
- **The `entry` API** does "look up, then insert or update" with one borrow and one hash.

```rust
*counts.entry(word).or_insert(0) += 1;
```

- **Separate the read phase from the write phase in an API.** A method that returns a reference into `self` keeps `self` borrowed for as long as the caller holds it; returning a small owned value or an ID frees the caller.
- `vec.push(vec.len())` compiles through two-phase borrows. Do not design an API that only works because of that rule; write the temporary.
- **Stop and reconsider the design** when a structure wants references to itself, or when lifetimes spread through many signatures. Owned data plus indices, or an arena, is nearly always the answer; `unsafe` is not.

### Interior mutability

| Need | Use | Watch for |
|---|---|---|
| A `Copy` value, one thread | `Cell<T>` | nothing; it cannot fail |
| Any value, one thread | `RefCell<T>` | a second overlapping `borrow_mut` panics at run time |
| Shared across threads | `Mutex<T>` | poisoning, lock order, holding it across `.await` |
| Read-mostly across threads | `RwLock<T>` | writer starvation; often no faster than `Mutex`, so measure |
| A counter or flag | `AtomicUsize`, `AtomicBool` | choosing an ordering; `SeqCst` unless you can argue for less |
| Set once, read often | `OnceLock<T>`, `LazyLock<T>` | initialisation that can fail |

- `RefCell` moves a compile-time rule to run time. Keep each borrow to one statement where possible, and prefer `try_borrow_mut` where re-entrancy is conceivable (callbacks, observers).
- Do not use a `Mutex` in single-threaded code to quiet the borrow checker, and do not make a type `Sync` by wrapping it in one without deciding what the lock protects.
- Interior mutability behind `&self` is part of the API's contract. Say so in the docs when a `&self` method changes observable state.

### Choosing a pointer

| Need | One thread | Across threads |
|---|---|---|
| One owner on the heap (recursive type, large value, trait object) | `Box<T>` | `Box<T>` |
| Several owners, read-only | `Rc<T>` | `Arc<T>` |
| Several owners, mutation | `Rc<RefCell<T>>` | `Arc<Mutex<T>>` or `Arc<RwLock<T>>` |
| A reference back to an owner | `rc::Weak<T>` | `sync::Weak<T>` |

- **Shared and immutable is the cheap case.** Prefer `Arc<T>` of immutable data, replaced whole, over `Arc<Mutex<T>>` mutated in place. `Arc::make_mut` gives copy-on-write when a private change is needed.
- **`Rc<RefCell<T>>` throughout a design is a sign** that ownership was never decided. It suits a few shared nodes (a GUI tree, an observer list), not a whole data model. Indices into an owning `Vec` are usually simpler and faster.
- **Parent-to-child strong, child-to-parent `Weak`,** or the cycle never frees.
- `Arc::clone(&x)` rather than `x.clone()` makes it visible that only the count is bumped.
- Before `Arc<Mutex<T>>` across tasks, ask whether one task could own the state and receive messages on a channel.

### Iterators and collections

- **A fallible pipeline short-circuits.** An iterator of `Result<T, E>` collects into `Result<Vec<T>, E>` and stops at the first error. `try_for_each` and `try_fold` do the same without collecting. Never `unwrap` inside a chain.

```rust
let ports: Vec<u16> = fields
    .iter()
    .map(|field| field.parse::<u16>())
    .collect::<Result<_, _>>()?;
```

- **Iterator promises are contracts.** `size_hint` must bracket the true length; implement `ExactSizeIterator` only when the length is exact. Unsafe code must not rely on either for memory safety, since safe code can implement them wrongly.
- Offer `iter()`, `iter_mut()` and `IntoIterator` for `&T`, `&mut T` and `T` on a collection type, so `for x in &collection` works.
- Iterators are lazy. A `map` with side effects that is never consumed does nothing; use `for` when the point is the effect.

| Need | Collection |
|---|---|
| A sequence; the default | `Vec` |
| Push and pop at both ends | `VecDeque` |
| Lookup by key, order irrelevant | `HashMap`, `HashSet` |
| Sorted order, range queries, deterministic iteration | `BTreeMap`, `BTreeSet` |
| Insertion order with lookup | `IndexMap` |
| Repeatedly take the largest | `BinaryHeap` (wrap in `Reverse` for the smallest) |
| A handful of items | a `Vec` and a linear scan, or `SmallVec` if measured |

- **`HashMap` iteration order is arbitrary and differs between runs.** Anything that reaches output, a hash, a snapshot or a test goes through a sort or an ordered map.
- `LinkedList` is almost never right: a `Vec` or `VecDeque` is faster for nearly every workload.
- The default hasher resists collision attacks and is slower for it. A faster hasher (`FxHashMap`, `ahash`) is for keys an attacker does not control, after a profile says hashing matters.
- `Vec::with_capacity` when the size is known; it is free and removes reallocations.

### Types and API basics

Each with when it pays and when it does not.

- **Accept borrowed inputs.** `&str`, `&[T]` and `&Path`, not `&String`, `&Vec<T>` and `&PathBuf`. The API then commits to meaning, not to a container. *When the function stores the value,* take it owned (`String`, or `impl Into<String>`) so the caller who already owns one does not pay for a clone. `impl AsRef<Path>` is right for path arguments; `impl AsRef<str>` everywhere is noise and bloats code through monomorphisation.
- **Newtypes, and parse instead of validating.** Turn raw data plus repeated checks into a type that can only hold a valid value. IDs, units, offsets, validated strings and handles stop being interchangeable primitives. *Skip when* the wrapper carries no invariant and no distinction anyone could confuse; a newtype around every `String` is ceremony.

```rust
#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub struct Email(String);

impl Email {
    pub fn parse(raw: &str) -> Result<Self, EmailError> {
        let trimmed = raw.trim();
        if trimmed.is_empty() {
            return Err(EmailError::Empty);
        }
        if !trimmed.contains('@') {
            return Err(EmailError::MissingAt);
        }
        Ok(Self(trimmed.to_owned()))
    }
    pub fn as_str(&self) -> &str { &self.0 }
}
```

  Keep the field private and offer no constructor that skips the check, or the guarantee is gone. That includes `Deserialize`: derive it through `#[serde(try_from = "String")]`, not on the raw field. Do not implement `DerefMut` or hand out `&mut` to the inner value.
- **`From` for conversions that cannot fail, `TryFrom` for those that can.** *Use a named constructor instead* when the operation does real work, loses information or has more than one sensible meaning. `From` must be cheap and unsurprising, because `?` and `.into()` call it invisibly.
- **Combinators for straight-line flows, `match` for branching.** `map`, `and_then`, `ok_or_else` and `transpose` keep a linear transformation linear. When there are several arms with different work, or a chain of four closures, a `match` or `let ... else` reads better.
- **Generics or `dyn`, chosen on purpose.** Generics for hot paths and when the caller knows the type. `dyn Trait` for heterogeneous collections, plugin points, and to keep compile time and code size down. For a call that does I/O, the virtual call is immeasurable; do not make a service generic over five type parameters to avoid it.
- **Return `impl Iterator` to stay lazy** and hide adapter types. Use `Box<dyn Iterator>` when branches return different iterator types or the type must be stored in a struct field without a generic parameter. Return a `Vec` when the caller always needs all of it and the size is bounded.
- **A named enum over a boolean or a sentinel.** A `bool` says something happened; an enum says what the caller must do next. `enum Inserted { New, Replaced(Old) }` beats `true`; `Option<usize>` beats `-1`. *A `bool` is fine* for a real yes-or-no question (`is_empty`).
- **A flat public facade with `pub use`.** Internal file layout and public paths are separate decisions; re-exports let internals move without breaking callers. Re-export deliberately, item by item. Do not re-export a dependency's types unless they are part of your contract, because then its version is too.
- **Blanket impls for `&T`, `&mut T` and `Box<T>`** make a trait usable through references and boxes without wrappers. Add them when the trait is naturally delegating and its methods take `&self`.
- **Omitted is not the same as explicitly empty.** For a partial update, "not provided" and "set to nothing" are different inputs:

```rust
pub enum Patch<T> {
    Keep,
    Clear,
    Set(T),
}
```

  `Option<Option<T>>` works with serde but is hard to read; the enum is clearer in domain code. Never use a magic value from the domain (an empty string, zero) to mean either.
- **Name the unit of an offset.** Bytes, `char`s and UTF-16 code units are different numbers for the same position. Put the unit in the type (`ByteOffset`, `Utf16Offset`) wherever offsets cross a boundary, and test on multi-byte text.
- **Strategies are named for the guarantee they give.** An operational choice is a named type behind a small trait, not a hidden boolean, and its documentation says what it does *not* preserve:

```rust
pub trait Sharding: Send + Sync {
    fn pick_shard(&self, shard_count: usize, key: &Key) -> usize;
}
pub struct Balanced { next: AtomicUsize } // spreads load; does not keep per-key order
pub struct Ordered;                       // keeps per-key order; load may skew
```

  Offer no alternatives where correctness needs one behaviour.

### Core idioms

- **Expressions over statements.** `if`, `match` and blocks are expressions; bind their value instead of declaring a `mut` and assigning in each branch. Use an iterator chain where it reads as a description of the result; use a loop where there are side effects, early exits or several accumulators.

```rust
let label = match status {
    Status::Active => "active",
    Status::Suspended { .. } => "suspended",
    Status::Closed => "closed",
};
```

- **`Cow<'_, str>` when the value is usually borrowed and sometimes changed:** normalisation, escaping, lossy decoding.

```rust
pub fn normalise(input: &str) -> Cow<'_, str> {
    if input.contains('\t') {
        Cow::Owned(input.replace('\t', "    "))
    } else {
        Cow::Borrowed(input)
    }
}
```

  *Skip it* when the value is always owned or always borrowed, and in struct fields unless profiling asks for it: the lifetime spreads to every holder. Calling `.into_owned()` on every result means it should have returned `String`.
- **A `type` alias is not a new type.** `type UserId = u64;` documents and checks nothing. Use a newtype for distinction; use an alias to shorten a long generic type.
- **`#[repr(transparent)]` on a newtype** is needed only when its layout is relied on: across FFI, or for a reference cast between the wrapper and its field. Elsewhere it is harmless and unnecessary.
- **The orphan rule:** to implement a foreign trait for a foreign type, wrap the type in a local newtype.
- **Do not return `Result` from something that cannot fail,** and do not return `Option` where an error would explain why.
- **`impl Fn` for callbacks, `fn` pointers for tables.** `impl Fn(T) -> U` accepts closures and inlines. A plain `fn(T) -> U` pointer rejects capturing closures; use it in static dispatch tables, in `const` contexts and across FFI, where a nameable, `Copy` type is the point. `&dyn Fn` or `Box<dyn Fn>` when the callback is stored or code size matters more than the call.
- **Keep generic bounds as simple as the use.** `fn f(s: &str)` beats `fn f<S: AsRef<str>>(s: S)` unless callers really pass several types; over-generic signatures hurt inference and error messages. When a generic wrapper is wanted, make it thin and delegate at once to a non-generic inner function, so the body is compiled once.

```rust
pub fn read_config(path: impl AsRef<Path>) -> Result<Config, ConfigError> {
    fn inner(path: &Path) -> Result<Config, ConfigError> { /* the real body */ }
    inner(path.as_ref())
}
```

- **Visibility is the narrowest that works.** Start private; widen to `pub(crate)`, then `pub` when something outside needs it. Every `pub` item in a library is a promise.
- **Do not clone to quiet the borrow checker.** The error is usually pointing at an ownership question: who should own this, and for how long. Answer that. `Rc` or `Arc` is for when several owners really exist.
- **Monomorphisation has a cost.** If generics inflate compile time or binary size, use `dyn Trait` at boundaries and on cold paths, and measure the effect (`cargo llvm-lines`, `cargo bloat`).
- **Name the collection type where it reads best:** `let v: Vec<_> = iter.collect();` or `iter.collect::<Vec<_>>()`. Collect into `Result<Vec<_>, _>` to stop at the first error.
- **Pick the pattern form by the number of cases.** `match` when every case matters; `if let` for one case where the rest is nothing; `let ... else` to unwrap or leave early and keep the happy path unindented; `while let` to drain; `matches!` for a boolean test.

```rust
let Some(user) = users.get(&id) else {
    return Err(Error::UnknownUser(id));
};
```

- **`#[non_exhaustive]` keeps room to grow.** On a public enum, other crates must write a wildcard arm, so adding a variant is not a breaking change; on a struct, they cannot construct it literally, so adding a field is not either. *Use on* public error enums and option structs expected to grow. *Do not use on* an enum callers are meant to match exhaustively (a closed set of states), because it takes the compiler's check away from them. It has no effect inside the defining crate.
- **Avoid a wildcard arm on your own enums.** `_ =>` silences the compiler exactly when a new variant arrives. List the variants, or group them explicitly.

### Destructors, guards and temporaries

- `Drop` cannot fail, must not block and should have almost no side effects. If teardown can fail, block or needs `.await`, expose `close`, `flush` or `shutdown` returning `Result`, and let `Drop` release only local state as a fallback.
- If correctness needs teardown to happen before later work, show it in control flow (an explicit `drop(guard)` or an inner block) and test it.
- `let _ = mutex.lock();` drops the guard at once; `let _guard = mutex.lock();` holds it to the end of the scope. Choose on purpose.
- A temporary created in a `match` or `if let` scrutinee lives to the end of the whole statement:

```rust
// Bad: the guard lives for the whole match, so the second lock deadlocks.
match cache.lock().unwrap().get(&key).cloned() {
    Some(v) => v,
    None => compute_and_insert(&cache, key), // locks the cache again
}

// Good: the guard is dropped at the end of the let statement.
let hit = cache.lock().unwrap().get(&key).cloned();
match hit {
    Some(v) => v,
    None => compute_and_insert(&cache, key),
}
```

- A task that can outlive its caller documents how it is cancelled and how it shuts down.

### Errors

**Defaults.**

- A function that can fail returns `Result`; `?` propagates. Panics are for bugs: a broken invariant that no caller could handle.
- **Libraries return typed errors** (an enum or struct, usually via `thiserror`) that callers can match on. **Applications use `anyhow` or `eyre`** at the top, where errors are reported, not matched. Never export `anyhow::Error` from a library: it tells callers nothing and takes away their ability to react.
- No `unwrap` or `expect` on a path that input, I/O or another system can make fail. Where an invariant truly guarantees success, `expect("why this cannot fail")` states it.
- Never swallow an error. Handle it, return it, or log it with a reason for going on.

### Designing an error type

```rust
#[derive(Debug, thiserror::Error)]
pub enum StoreError {
    #[error("record {id} not found")]
    NotFound { id: RecordId },

    #[error("query timed out after {elapsed:?} (limit {limit:?})")]
    Timeout { elapsed: Duration, limit: Duration },

    #[error("reading {}", .path.display())]
    Read {
        path: PathBuf,
        #[source]
        source: io::Error,
    },

    #[error(transparent)]
    Database(#[from] DatabaseError),
}
```

- **One variant per thing a caller might do differently** (retry, report to the user, treat as absent), not one per call site and not one per underlying library.
- **A variant carries the data needed to act or to explain:** the ID, the path, the limit. A variant holding only a `String` is a message, not a type.
- **Keep the cause as `#[source]`, and do not repeat its text in your message.** Reporters print the chain; a message that embeds the source prints it twice. `cause: String` throws the chain away.
- Messages are lower case, without a trailing full stop, and say what was being attempted.
- **`#[from]` only where the conversion needs no context.** A blanket `From<io::Error>` makes every `?` on a file operation produce an error that does not say which file.
- Errors are `Send + Sync + 'static` so they can cross threads and be boxed. Keep them small; box a large payload, since the size of `E` is paid by every `Result<T, E>`.
- **`#[non_exhaustive]` on a public error enum that will grow,** so adding a variant is not a breaking change.

**An opaque error with a kind, when the error space will evolve.** A public enum freezes its
variants and their fields. A struct with a private representation and a public `kind()` keeps
room to change.

```rust
#[derive(Debug)]
pub struct Error {
    kind: ErrorKind,
    source: Option<Box<dyn std::error::Error + Send + Sync>>,
}

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
#[non_exhaustive]
pub enum ErrorKind {
    NotFound,
    Timeout,
    InvalidInput,
}

impl Error {
    pub fn kind(&self) -> ErrorKind {
        self.kind
    }

    pub fn is_retryable(&self) -> bool {
        matches!(self.kind, ErrorKind::Timeout)
    }
}
```

- Callers cannot construct it, so only your crate decides which states exist. Predicates such as `is_retryable()` answer the question callers actually have.
- *Use a plain enum* when the set is small, stable and callers benefit from matching on fields. Most internal crates are in that case.

### Context and reporting

**Add context where the operation is still meaningful.** `?` alone says what failed, not what
was being done.

```rust
pub fn load_config(path: &Path) -> anyhow::Result<Config> {
    let text = fs::read_to_string(path)
        .with_context(|| format!("reading config {}", path.display()))?;
    let config = toml::from_str(&text)
        .with_context(|| format!("parsing config {}", path.display()))?;
    Ok(config)
}
```

- Context belongs at I/O and orchestration boundaries: opening a file, sending a request, decoding a payload, calling another service. Adding it at every helper repeats the same sentence down the chain.
- `with_context` takes a closure, so the message is formatted only on failure.
- In a library, the equivalent is a variant that carries the context plus the `#[source]`, built with `map_err`.

**A diagnostic for a person says where and what to do.** For user-facing input (configuration,
flags, patterns, file formats): the file, line and column or byte offset, what was found, what
was expected, and a hint when there is an obvious repair. An abstract variant name helps
nobody.

- Rich reports with source snippets and labelled spans (`miette`, `ariadne`, `color-eyre`) belong in the binary. Do not put their types in a library's public API; expose spans and messages as plain data and let the binary render them.
- **Diagnostics must survive non-UTF-8 data.** Paths, command output and protocol bytes are not always valid UTF-8. Print paths with `.display()`, bytes with an escaping formatter, and do not convert to `String` early with `unwrap` or lose data with a silent lossy conversion.
- Never put secrets, tokens or whole payloads in an error message. Errors travel to logs and to users.

**The binary owns the exit code.**

```rust
fn main() -> ExitCode {
    match run() {
        Ok(()) => ExitCode::SUCCESS,
        Err(error) if is_broken_pipe(&error) => ExitCode::SUCCESS,
        Err(error) => {
            eprintln!("error: {error:#}");
            ExitCode::from(2)
        }
    }
}
```

- Returning `ExitCode` from `main` lets destructors run; `std::process::exit` does not, so buffered output and temporary files can be lost.
- A closed pipe (`tool | head`) is not a failure. Look for `io::ErrorKind::BrokenPipe` in the chain and exit quietly.
- `{error:#}` prints an `anyhow` error with its causes on one line; `{error:?}` prints the multi-line report with a backtrace if one was captured.
- Distinct exit codes for distinct classes (usage error, runtime failure) are part of a CLI's interface; document them. Errors go to stderr, results to stdout.
- **A library never exits the process,** prints to stdout or stderr, or installs global handlers.

### Panics

- **Audit production paths before a release:** `unwrap`, `expect`, `panic!`, `unreachable!`, `todo!`, slice indexing and arithmetic on external input. Each becomes a `Result` or gets a comment stating the invariant.

```sh
cargo clippy -- -W clippy::unwrap_used -W clippy::expect_used \
  -W clippy::indexing_slicing -W clippy::panic
```

- Compiling and passing unit tests does not show that a panic is unreachable. For each boundary, one test feeds the bad input and asserts the returned error.
- These lints are noisy in tests; allow them there (`#![cfg_attr(test, allow(clippy::unwrap_used))]`) instead of weakening them everywhere.
- **A panic must not cross an FFI boundary.** Catch it with `catch_unwind` at every exported `extern "C"` function and turn it into an error code.

### Recovery by error class

| Class | Where it arises | Recovery | Represent as |
|---|---|---|---|
| Validation | parsing, input edge | reject with the reason | typed parse or validation error |
| Business rule | domain workflow | reject with a precise outcome | named domain error or outcome enum |
| Transient external | network, storage, subprocess | retry with bounds, degrade, reschedule | retryable variant or flag |
| Permanent external | auth, contract or schema mismatch | fail fast, name the repair | typed permanent error |
| Timeout | async orchestration | fail, retry or cancel, explicitly | timeout error carrying the limit |
| Cancellation | task or workflow boundary | stop cooperatively, clean up | its own path, not a failure |
| Overload | queue, pool, stream | reject, shed or wait with a bound | explicit "saturated" result |
| Invariant breach | core logic | make impossible by construction, else fail fast | a narrow panic or an internal error |
| Clean-up failure | close, shutdown | explicit `close`, best-effort `Drop` | close error or shutdown report |
| FFI boundary | ABI, foreign ownership | convert, isolate or abort | the safe wrapper's error |

- **A message answers three questions:** what failed, where, and what the reader should do next.
- **If callers branch on it, give them structure; if they only pass it up, give them context.** Most errors are the second kind.
- Cancellation and overload are not failures of the operation and should not be logged or counted as such.
- A dependency's error type in your public signature makes its version part of your API. Wrap it or re-export it deliberately.

**Smaller rules.**

- **An undo log for in-memory mutations that need rollback.** Record each mutation's inverse as data (`enum UndoOp { CreateNode(NodeId), UpdateAttr { id, old } }`) and replay it backwards on failure. A new mutation kind adds its undo record in the same change; an exhaustive `match` enforces it. Use real transactions when the storage engine has them.
- **`no_std` errors:** implement `core::fmt::Display` by hand and `core::error::Error` directly (stable since Rust 1.81), or put `std::error::Error` behind a `std` feature on older toolchains.
- **Tests assert the variant or code, not message text,** so wording can improve. Retry tests assert behaviour (a permanent error is attempted once; the deadline stops the loop), not exact jittered delays.

### Async and concurrency

**Defaults.**

- **Never block the executor.** No blocking I/O, `std::thread::sleep`, long CPU work or blocking lock inside an async function. Blocking work goes to `spawn_blocking`; CPU-heavy work to a thread pool such as `rayon`.
- **Never hold a lock guard across `.await`.**
- **Everything is bounded:** channels, concurrency, retries, timeouts, buffers.
- **Every task has an owner** that can cancel it and learns how it ended.
- **Every long-running operation can be cancelled** and has a deadline.
- First ask whether you need async at all. A CLI, a build tool or a CPU-bound pipeline is usually simpler and as fast with threads. Async earns its place with many concurrent I/O waits.

### Blocking and locks

**How long is too long without an `.await`?** As a rule of thumb, more than about 100
microseconds of work between yield points starts to hurt other tasks' latency.

| Work | Where it runs |
|---|---|
| Short CPU work, non-blocking calls | inline in the task |
| Blocking I/O, a synchronous client, file-system calls | `tokio::task::spawn_blocking` |
| Heavy CPU work, parallel across cores | `rayon`, with the result sent back over a `oneshot` |
| A long-lived blocking loop | a dedicated `std::thread` |

- `spawn_blocking` tasks cannot be cancelled once started, and the pool is large but finite. Do not park an endless loop there.
- `tokio::fs` uses the blocking pool underneath. For many small file operations, one `spawn_blocking` around the whole batch is faster.

**Locks.**

```rust
// Wrong: the guard lives across the await.
let mut state = shared.lock().unwrap();
state.total += fetch_amount().await?;

// Right: await first, then lock briefly.
let amount = fetch_amount().await?;
shared.lock().unwrap().total += amount;
```

- **Use `std::sync::Mutex` (or `parking_lot`) for short critical sections, even in async code.** It is faster than an async mutex, and its guard is not `Send`, so the compiler rejects holding it across an `.await` in a spawned task.
- **Use `tokio::sync::Mutex` only when the guard must be held across an `.await`,** such as serialising access to a connection. Then ask whether a single owning task with a channel would be clearer.
- A guard in a temporary lives to the end of the statement, and in `if let` or `match` on editions before 2024 to the end of the block. When in doubt, bind the value you need and `drop(guard)` explicitly.
- The same rule holds for a `RefCell` borrow and for anything else that must be released: a pooled connection, a permit, a transaction.
- **Lock order:** when two locks are ever held together, one documented order, everywhere. Better, restructure so that no code holds two.

### Cancellation

**In async Rust, any `.await` is a point where the future may be dropped and never resumed.**
That happens on `select!`, on a timeout, when a `JoinHandle` is aborted, and when a client
disconnects.

- **A future is cancel-safe if dropping it between polls loses nothing.** `recv()` on a Tokio channel is. Reading "exactly n bytes" into a local buffer is not: the bytes already read vanish with the future.
- **In `select!`, keep state outside the branch futures.** A half-filled buffer or a half-advanced parser lives in a variable that survives the loop iteration; the branch only awaits the next piece.

```rust
let mut buffer = BytesMut::new(); // outlives each select! iteration
loop {
    tokio::select! {
        _ = shutdown.cancelled() => break,
        read = socket.read_buf(&mut buffer) => {
            if read? == 0 { break; }
            while let Some(frame) = try_parse(&mut buffer)? {
                handle(frame).await?;
            }
        }
    }
}
```

- **A multi-step change that must not be half-done** is either made atomic (one transaction, one message to an owning task) or run in a spawned task the caller waits on, so that dropping the caller does not stop it midway.
- **Clean-up after cancellation runs in `Drop`, which cannot `.await`.** Hand async clean-up to an owner task, or offer an explicit async `shutdown()` and treat `Drop` as the fallback.
- **Use a `CancellationToken` for cooperative shutdown.** Pass it down, check it in loops and `select!`, and give children `child_token()` so a subtree can be cancelled alone.
- Document, for every public async function, whether it is cancel-safe.

### Tasks and their owners

**A spawned task belongs to something that waits for it.** A detached `tokio::spawn` whose
handle is dropped keeps running, its panic goes unnoticed, and shutdown cannot wait for it.

```rust
let mut tasks = JoinSet::new();
for job in jobs {
    tasks.spawn(process(job));
}
while let Some(joined) = tasks.join_next().await {
    match joined {
        Ok(Ok(report)) => reports.push(report),
        Ok(Err(error)) => return Err(error), // dropping the set aborts the rest
        Err(join_error) => return Err(Error::TaskPanicked(join_error)),
    }
}
```

- `JoinSet` aborts its remaining tasks when dropped, so an early return does not leak work. A `JoinError` is a panic or an abort; handle it, do not `unwrap` it.
- **Bound the fan-out.** A `Semaphore` permit per task, or `futures::stream::iter(jobs).map(f).buffer_unordered(limit)` when the futures need not be spawned.
- **`join!` and `try_join!` for a fixed, small set** of futures on the current task: no spawn, no `'static` bound, borrowing allowed. `tokio::spawn` when the work should run in parallel on other threads or outlive the caller.
- **A background task for the life of the service** is held by the component that starts it: store the `JoinHandle` and the cancellation token, and have `shutdown()` cancel and then await it with a time limit.
- **Carry trace context across the spawn.** Do it in the project's one spawn helper, so tasks inherit the caller's span by default.

```rust
tokio::spawn(work().instrument(tracing::Span::current()));

let span = tracing::Span::current();
tokio::task::spawn_blocking(move || span.in_scope(blocking_work));
```

- **Threads:** name them (`thread::Builder::new().name(...)`), join them, and prefer `std::thread::scope` when they only need to borrow local data for a bounded time.

**A supervisor fails in-flight jobs before it restarts the worker.** A worker that can crash
(a thread, a child process, a WASM instance) has a supervisor holding a registry of pending
replies.

```rust
struct Supervisor {
    in_flight: HashMap<JobId, oneshot::Sender<Result<Output, WorkerError>>>,
    consecutive_restarts: u32,
}

impl Supervisor {
    fn on_worker_exit(&mut self) -> Result<(), WorkerError> {
        for (_, reply) in self.in_flight.drain() {
            let _ = reply.send(Err(WorkerError::Crashed)); // the caller may have gone away
        }
        self.consecutive_restarts += 1;
        if self.consecutive_restarts > MAX_RESTARTS {
            return Err(WorkerError::GaveUp);
        }
        self.spawn_worker()
    }

    fn on_worker_ready(&mut self) {
        self.consecutive_restarts = 0; // only a successful start resets the count
    }
}
```

- **A clean error beats a future that never completes.** Jobs are failed, not replayed: only the caller knows whether a retry is safe.
- Restart with backoff and a cap. A worker that dies at start-up must not be restarted in a tight loop.
- Per-job resources are freed by an owning guard's `Drop`, so the crash path releases them too.

**A timeout does not mean the work stopped.** Dropping a timed-out future stops async work at
its next `.await`, but a `spawn_blocking` closure, a thread or a child process carries on.

```rust
match self.running.get(&job) {
    Some(handle) if !handle.is_finished() => return Tick::StillRunning, // skip this tick
    Some(_) => {
        self.running.remove(&job);
    }
    None => {}
}
let handle = tokio::task::spawn_blocking({
    let job = job.clone();
    move || run(job)
});
self.running.insert(job, handle);
```

- For a periodic job, skip the tick while the previous run is alive, or runs pile up on the same data.
- For work that must stop, give it a flag or token it checks, or run it in a child process that can be killed.
- Report "timed out, still running" differently from "failed".

### Tests and evidence

| Evidence | Choose it when | It does not show |
|---|---|---|
| Unit test | Behaviour is local and deterministic | That the parts work together |
| Integration test | Behaviour crosses a module, process or adapter boundary | Every edge case; too slow for that |
| Doctest | A public example is part of the contract | Anything about error paths, unless written |
| Compile-fail test (`trybuild`) | Misuse must not compile: typestate, `Send` bounds, lifetimes | Run-time behaviour |
| Property test (`proptest`) | An invariant or a round trip matters more than examples | That the stated property is the right one |
| Fuzzing (`cargo-fuzz`) | A parser, decoder or other frontier takes untrusted bytes | Semantic correctness; it finds panics, hangs and whatever you assert |
| `loom` | A small concurrent state machine built on atomics or locks | Anything about async I/O or large systems; the model must be tiny |
| Miri | Unsafe code, aliasing, uninitialised memory | Paths the tests do not execute; no FFI |
| Benchmark | A latency or memory threshold was stated | Production behaviour, unless the input is representative |
| Snapshot test (`insta`) | Output is large and structured: rendered text, plans, diagnostics | Correctness of the first snapshot; a person must read it |

- **Pick the rows at the start and record which ones the change triggers.** A matrix filled in after the code only justifies the evidence that already exists. Formatting, lints, tests and a build can all pass over a parser that was never fuzzed and a lock whose interleavings were never explored.
- **No threshold, no performance claim.** The benchmark row is owed only when a number was stated; without one, do not write "fast" in the report either.
- **Choose the smallest set that covers the risk,** not the largest that can be listed.
- **A missing test is written as missing.** An empty row marked "not covered" is honest; an invented test name is not.
- Coverage is a tool for finding untested code. It is not evidence that the tested code is right, and it is a poor target.

**The test-first loop.**

```text
STUB -> RED -> GREEN -> REFACTOR -> VERIFY
```

- **STUB.** Write the signature with a `todo!()` body, and the tests against it. At least one test per requirement.
- **RED.** Run it and *read the failure*. The first failure should be the missing behaviour. An unrelated compile error or a panic in the set-up means the test is not yet testing the thing. A test that has never failed has not been shown to test anything.
- **GREEN.** The least code that passes. Resist generalising here.
- **REFACTOR.** Improve names, decomposition and ownership with the tests green. No behaviour change in this step.
- **VERIFY.** Formatting, lints, the full test suite and a build, plus whichever rows from the table the change triggered.

For each requirement, cover three paths: the normal one, the error one, and an edge (empty,
one, maximum, boundary). State the empty case in the requirement itself: no matches is an empty
`Vec`, not an error and not `None`.

**When to apply it strictly, and when not.**

- *Strictly* for a bug fix (the failing test is the reproduction and stays as the regression test), for logic with a clear input-to-output contract, and for anything behind a public API.
- *Loosely* for exploratory work where the interface is not known yet: spike without tests, learn the shape, then throw the spike away or write the tests before it is merged. Do not let a spike become the implementation untested.
- *Not test-first* for pure wiring, generated code and thin adapters; an integration test afterwards covers them better than unit tests written in advance.
- Anti-pattern: writing the implementation, then writing tests that assert whatever it does. Those tests pin the bugs.
- Anti-pattern: changing the assertion to make a failing test pass, without first deciding whether the code or the test was wrong.

**Cheap checks before commit.** Search the added lines of the diff for `TODO`, `FIXME`,
`todo!`, `unimplemented!` and `dbg!`, and the added non-test lines for `.unwrap()` and
`.expect(`. Each hit is either removed or justified.

### Names

**A name says what the thing is or does at the call site,** in the vocabulary of the domain.
Length follows scope: a loop index may be `i`; a public function may not be `process`.

- **Follow the Rust API naming conventions:** `as_`, `to_`, `into_` by cost; `iter`, `iter_mut`, `into_iter`; `new` and `with_` constructors; `try_` for the fallible twin; `is_` and `has_` for predicates; getters without a `get_` prefix; `_mut` and `_unchecked` suffixes.
- **Casing:** `UpperCamelCase` types and traits, `snake_case` functions and modules, `SCREAMING_SNAKE_CASE` constants. Acronyms are words: `HttpClient`, `parse_url`. Crate names avoid `-rs` and `rust-`.
- **A name carries its unit when the type does not:** `timeout_ms`, `size_bytes`. Better, let the type carry it (`Duration`, a newtype).
- **Do not repeat the module in the item:** `cache::Config`, not `cache::CacheConfig`, unless items are usually imported bare.
- **One concept, one word.** If the code says `fetch`, `load` and `get` for the same operation, the reader assumes three operations.
- **Avoid names that say nothing:** `data`, `info`, `manager`, `helper`, `util`, `handle_it`, `do_work`.
- **Booleans read as assertions,** positively: `is_enabled`, not `not_disabled` or `flag`.
- **Follow the repository's own scheme where it has one.** Some codebases adopt a fixed pattern such as four-word `verb_constraint_target_qualifier` names (`filter_implementation_entities_only`). That is a local convention: apply it there, and nowhere else by default. Never count words where the result is a worse name.
- **A risky rename of a public item is done in two steps:** add the new name, deprecate the old with `#[deprecated(note = "use `new_name`")]`, and remove it in the next major version.

### Anti-patterns

This is the list to scan before handing work over. Each
has an exception, because the opposite mistake exists too.

### Reject by default

| Smell | Do instead | Legitimate exception |
|---|---|---|
| A requirement with nothing measurable ("make it faster") | A testable statement: input, expected result, threshold | Exploratory spikes, labelled as such and thrown away |
| A performance claim with no measurement | A benchmark, or a contract test that enforces the number | None; say "not measured" |
| `&Vec<T>`, `&String`, `&Box<T>` parameters | `&[T]`, `&str`, `&T` | You need `capacity()` or another method of the container itself |
| `anyhow::Error` or `Box<dyn Error>` in a library's public API | A typed error enum | Applications and binaries, where nobody matches on the error |
| `unwrap()` or `expect()` on a path input can reach | `?` and a typed error | A proven invariant, stated in the `expect` message; tests |
| Blocking work on an async executor | `spawn_blocking`, a dedicated thread, or an async API | Work bounded well under a millisecond |
| A lock guard or `RefCell` borrow held across `.await` | Copy out and drop the guard; or an async mutex where the await is the point | An async mutex guarding an I/O resource that must be used serially |
| An unbounded channel or queue | A bound, plus a stated policy when full | A provably bounded producer, with the proof in a comment |
| A spawned task with no owner | `JoinSet` or a supervisor; a cancellation path; observed failures | None in a long-running service |
| Concurrency never exercised under contention | Stress tests, `loom` for small lock-free cores, TSan | Code that is trivially confined to one thread |
| Text handling that assumes UTF-8, or one byte per character | `&[u8]`, `OsStr`, `Path`; `char_indices` for boundaries | Input already validated as `str` |
| I/O, runtime or framework types in the core domain | Pure core; adapters at the edge | Small programs where the split would be the bulk of the code |
| A struct holding the concrete database or HTTP client it uses | Depend on a narrow trait or pass a function; construct at the edge | The adapter itself |
| A "manager" struct with twenty fields | Split by responsibility and by what changes together | A plain configuration record |
| A domain model that ignores real cases | Model the cases the input actually has, or reject them explicitly | A stated, enforced subset |
| A public enum that will grow, without `#[non_exhaustive]` | Add it before the first release | Enums that are closed by definition |
| A diagnostic that drops the location | Carry file, line, column or byte span through to the message | None |
| Tests that only replay examples | Add the invariant: a property test, a round trip, a boundary table | Glue code with no invariant to state |
| Generic "so we can swap it later" | One concrete implementation; abstract at the second real use | A boundary you must fake in tests today |

A note on resource leaks: Rust closes files, sockets and locks when their owner is dropped,
so "forgot to close" is rare. The leaks that do happen are tasks and threads nobody joins,
child processes nobody waits for, temporary files, `Rc` or `Arc` cycles, entries never
removed from a long-lived map, and anything whose clean-up is async and so cannot run in
`Drop`.

### Subtler ones

- **Borrowing by habit.** Lifetimes threaded through a design, or clones hidden inside, only to avoid taking ownership of data the callee keeps anyway. If it is stored, moved to a task or outlives the call, take it owned.
- **Recovery logic keyed on message text.** Retry or fallback chosen by a substring of an error message breaks silently when the wording or a wrapper changes. Match typed variants or a retryability method.
- **The kitchen-sink error enum.** One public enum with a variant per dependency and a catch-all string. Callers cannot tell what is actionable, and every internal change is an API change. Use errors local to each boundary, expressed in that boundary's terms.
- **Dependency types in a public API.** A dependency upgrade becomes your breaking change. Wrap them. *Exception:* crates whose purpose is to extend that dependency, and vocabulary crates such as `bytes`, `http` or `serde`.
- **Trait and module sprawl.** Tiny traits and wrappers that exist to look abstract. A seam belongs at a real external or semantic boundary.
- **Accumulator soup.** Nested loops with pushes, flags and branch-specific state. Use an iterator chain or small named helpers. Keep the loop when control flow is heavy (early exits, `?`, several outputs) and the chain would be harder to read.
- **A mutable configuration blob,** patched by many call sites before use, so validity depends on timing. Validate once and hand out a frozen value.
- **A build that works only by folklore:** undocumented features, a remembered toolchain, commands that work only from one directory. Pin the toolchain, keep features additive, and run the gates from the workspace root.
- **Transport types used as domain types.** When handlers, services and storage share one DTO, every layer re-decides what is valid. Convert at the edge.
- **Speculative `unsafe` or lock-free code.** Build the safe version, measure, and only then narrow `unsafe` to the proven hot spot, with a proof plan.
- **"It compiles" offered as proof of behaviour.** The compiler proves memory and thread safety, not logic, liveness, ordering or performance. Each of those needs its own evidence.
- **Hand-edited generated code.** Regeneration discards the edit. Change the schema, the generator configuration or a wrapper module.
- **Broad desktop privilege:** wide filesystem grants, generic shell access, sidecar processes with no owner or health check. Running on the user's own machine is not an exception.
- **Hazards a signature does not show:** a guard kept alive by an iterator or a temporary in a `match` scrutinee; an `Arc` cycle; a new trait method that breaks object safety; a new auto-trait-breaking field (`Rc`, a raw pointer) that silently removes `Send` from a public type.

### Mistakes in applying this list

- **Over-correcting.** Removing every clone, making every `&str` parameter `impl AsRef<str>`, giving every function its own error enum, adding a trait to mock one call. A clone is right when it makes ownership clear and the cost is unmeasured or small. Fix the instance that hurts.
- **Fixing the symptom.** Similar symptoms need opposite fixes: a borrow error may want a clone, a restructured scope, or a different owner. Reproduce the failure in the smallest case, confirm the mechanism, then change the code. Adding a clone, a retry, a lock or a trait before that is guessing.
- **Moving a cost instead of removing it.** A convenience in one function often transfers a panic, an allocation, a queue or a compatibility burden to callers and operators. Ask who pays now.
- **The unnamed shortcut.** A design that deliberately avoids a tempting default (a clone per call, `Arc<Mutex<_>>` around everything, `Box<dyn Error>` in a public API) says so at the boundary. Otherwise the next change puts it back.
<!-- essentials:end -->

<!-- core:begin -->
## Working rules shared by every Rust skill

This block is the same in every Rust skill. It covers how to work, the gates, and what
"done" means. Where the repository you are in has its own convention or gate, that wins.

**If nothing else is in reach:**

1. **Say what "correct" means before writing code,** in terms something can check.
2. **Put invariants in types** where that is cheap, and in tests where it is not.
3. **Make ownership, errors, cancellation and shutdown deliberate.** Each should be a decision someone can point to.
4. **Bound everything that can grow:** queues, buffers, retries, recursion, waits, output.
5. **Treat everything from outside the process as untrusted** until it has been parsed into a type that cannot hold the invalid form.
6. **Measure before optimising, and state the method with the number.**
7. **Follow the repository you are in** over any general convention, this skill included.
8. **Report what you ran and what you saw.** Unverified is a legitimate status; passing it off as verified is not.

### Size the process to the task

| Task | Process that fits |
|---|---|
| Rename, comment, one-line fix covered by an existing test | Read the code and its callers, change it, run the gates |
| Bug fix | Reproduce it with a failing test, fix, run the gates |
| Feature inside one module | A short list of checkable requirements, tests first, implement |
| New public API, a change that crosses a boundary, concurrency, unsafe | Requirements, design of types and boundaries, a chosen test mix, then code |

Process heavier than the task buries the change the reviewer has to check. Process lighter
than the task is how a "small" change to an error type or a lock ships a regression.

### Working with the compiler and the ecosystem

- **Fix the first error first.** Later errors are often cascades. Read the whole message, including the `help:` and `note:` lines. Run `cargo check` after each small edit, not after three hundred lines.
- **A borrow-checker error is design information.** Before adding `.clone()`, `Rc<RefCell<_>>`, `Arc<Mutex<_>>` or `'static` to make it compile, say who owns the value and how long the borrow must live. A clone is fine when the value is small or the path is cold; it is wrong when it silently forks state that was meant to be shared.
- **Never guess an API.** Find the version in `Cargo.lock`, then read the documentation for that version or the source under `~/.cargo/registry/src`. Widely used crates change shape between major versions, and code remembered from one version fails on another.
- **Check the edition and the minimum Rust version** (`edition` and `rust-version` in `Cargo.toml`) before using a newer language feature.
- **Match the codebase.** Use its error crate, runtime, logging, naming and module layout. A second way of doing the same thing is a cost every later reader pays.
- **Keep the diff to the task.** No drive-by reformatting, renames or dependency upgrades. Report what you noticed; do not fix it uninvited.
- **Add a dependency deliberately.** Check that std or an existing dependency does not already do it, look at maintenance and licence, enable only the features needed, and say in the handover that you added it.
- **Read before you write.** Read the function you change, its callers and its tests.
- **A red test must be red for the right reason:** it fails on the assertion, not on a compile error or a set-up mistake.
- **Debug in a loop with a stop condition.** Reduce to the smallest reproduction, test one hypothesis per probe, and stop when a regression test fails for the confirmed cause. A plausible story is not a diagnosis.

### What the compiler does not prove

- It proves memory and type properties. It proves nothing about domain correctness, performance, cancellation behaviour or compatibility.
- Code that compiles with clones everywhere has not shown the clones are right.
- No data race does not mean no logical race: check-then-act across two lock acquisitions, dropped work and stale reads all compile.

### The required gates

Cheapest first, so the fastest check fails first:

```bash
cargo fmt --all -- --check
cargo clippy --workspace --all-targets --all-features -- -D warnings
cargo test --workspace --all-targets --all-features
cargo test --workspace --doc --all-features
```

- **Use the repository's own gate if it has one** (a `just` or `make` target, a CI script). These commands are the default when there is none.
- **`--all-targets` does not run doc tests.** They need the separate `--doc` run.
- **Clippy without `-D warnings` is not the gate.** It prints and passes.
- **`--all-features` is wrong for crates with mutually exclusive features.** Test the supported combinations explicitly.
- Run from the workspace root you mean. A command run in one member checks that member only.
- **A zero exit code can hide tests that did not run.** Read the count: how many ran, how many were ignored or filtered out.

Run a heavier gate when the change touches its risk, and say so when you skip one:

| Gate | Run it when |
|---|---|
| `cargo test --release` | Behaviour could differ with optimisation: overflow checks, `debug_assert`, timing, unsafe code |
| `cargo +nightly miri test` | Unsafe code changed |
| `RUSTDOCFLAGS="-D warnings" cargo doc --no-deps` | Public items or documentation changed |
| `cargo deny check` or `cargo audit` | Dependencies changed |
| `cargo semver-checks` | A published library's public interface changed |
| Benchmarks against a baseline | A performance claim is made, or a hot path changed |

### Before claiming done

1. Identify the command that would prove the claim.
2. Run it fresh and in full, after the last edit.
3. Read the output and the exit status.
4. Report what happened, and only then say done or not done.

- **"It compiles" is not done.** Done is: the required gates green on the final code, and the claimed behaviour covered by tests.
- **If you could not run a command, say so and list it for a human.** Never report an unrun command as passed, and never describe output you did not see. "Skipped" is not "passed".
- **Do not weaken a check to make it pass:** no deleted or `#[ignore]`d test, no loosened assertion, no blanket `#[allow]`, no special case for the test's input. If a test is wrong, say so and fix the test as its own visible change.
- **Before handoff, search your own diff** for `todo!()`, `unimplemented!()`, `dbg!`, stray `println!`, commented-out code and placeholder `TODO` markers.
- **Never invent an identifier, a number or a citation** to satisfy a checklist. If an item does not apply, say why.
- **No secret reaches a log, an error message or a `Debug` output.** No compiler checks this; look at debug, error and crash paths.

**The record at handoff:** the commands run, their results and the toolchain version;
which heavier gates ran or were skipped, with the reason; what was verified by test, what
by reading, and what not at all; known limitations and anything left for a human.
<!-- core:end -->
