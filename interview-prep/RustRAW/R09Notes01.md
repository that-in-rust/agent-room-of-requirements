# 🦀 Rust Exercise #1: Welcome — MCU Edition

> **Exercise:** `exercises/01_intro/00_welcome`  
> **Goal:** Complete the `greeting()` function to return `"I'm ready to learn Rust!"`

---

## 🎬 The Big Picture: Your First Rust File

```mermaid
flowchart TB
    subgraph STARK["🏢 STARK INDUSTRIES (lib.rs)"]
        direction TB
        
        subgraph JARVIS["🤖 JARVIS (Comments)"]
            C1["// Explains what's happening"]
            C2["// Ignored by compiler"]
        end
        
        subgraph SUIT["🦾 IRON MAN SUIT (Function)"]
            FN["fn greeting()"]
            ARROW["-> &'static str"]
            BODY["Returns a message"]
        end
        
        subgraph SHIELD["🛡️ S.H.I.E.L.D. (Tests)"]
            CFG["#[cfg(test)]"]
            ASSERT["assert_eq!()"]
        end
    end
    
    JARVIS --> SUIT
    SUIT --> SHIELD
```

### 🎮 ELI10 (Explain Like I'm 10)
Imagine you're Tony Stark building your first Iron Man suit! **Comments** are like JARVIS giving you hints. The **function** is the actual suit that DOES something. The **tests** are S.H.I.E.L.D. checking if your suit works!

### 💻 ELI15 (Explain Like I'm 15)
A `.rs` file is your workshop. Comments (`//`) are documentation the compiler ignores. Functions define reusable behavior with explicit return types. The test module (`#[cfg(test)]`) only compiles during `cargo test`, verifying your implementation.

---

## 🦾 Function Anatomy: Building the Suit

```mermaid
flowchart LR
    A["<b>fn</b><br/>🔧 Keyword"]
    B["<b>greeting</b><br/>🏷️ Name"]
    C["<b>()</b><br/>📭 No Params"]
    D["<b>-></b><br/>➡️ Returns..."]
    E["<b>&'static str</b><br/>📜 String slice"]
    F["<b>{ body }</b><br/>⚙️ The code"]
    
    A --> B --> C --> D --> E --> F
```

### The Code

```rust
fn greeting() -> &'static str {
    // TODO: fix me 👇
    "I'm ready to learn Rust!"  // ← THE SOLUTION!
}
```

### 🎮 ELI10
A function is like a vending machine! Press the button (`greeting()`), get something back (the string). The `->` is the chute where your snack comes out!

### 💻 ELI15
`&'static str` means we return a **reference** to a string slice with a **'static lifetime**—it lives for the entire program. Rust guarantees memory safety at compile time.

---

## 🛡️ Test Flow: S.H.I.E.L.D. Verification

```mermaid
flowchart TB
    A["🚀 cargo test"]
    B["📦 #[cfg(test)]<br/>Only compile for tests"]
    C["🧪 #[test]<br/>Mark as test"]
    D["⚖️ assert_eq!<br/>Compare values"]
    
    A --> B --> C --> D
    
    D -->|"✅ Match"| E["🎉 PASSED"]
    D -->|"❌ No Match"| F["💥 FAILED"]
```

### The Test Code

```rust
#[cfg(test)]
mod tests {
    use crate::greeting;

    #[test]
    fn test_welcome() {
        assert_eq!(greeting(), "I'm ready to learn Rust!");
    }
}
```

### 🎮 ELI10
Tests are like getting a report card! Nick Fury checks if your answer matches the expected answer. Say it wrong? Back to training! Say it right? Welcome to the Avengers!

### 💻 ELI15
`#[cfg(test)]` is **conditional compilation**—the test module only exists in test builds. `assert_eq!` panics if values don't match, causing the test to fail.

---

## ⚡ Complete Mission Flow

```mermaid
sequenceDiagram
    participant You as 🧑‍💻 You
    participant Code as 📄 lib.rs
    participant Rust as 🔧 Compiler
    participant Test as 🛡️ Tests
    
    You->>Code: Write solution
    You->>Rust: cargo test
    Rust->>Rust: Compile with tests
    Rust->>Test: Run test_welcome()
    Test->>Code: Call greeting()
    Code-->>Test: "I'm ready to learn Rust!"
    Test->>Test: assert_eq! check
    
    alt Match ✅
        Test-->>You: 🎉 PASSED!
    else No Match ❌
        Test-->>You: 💥 FAILED
    end
```

---

## 🎯 The Solution

```mermaid
flowchart LR
    BEFORE["❌ BEFORE<br/>'I'm ready to __!'"]
    AFTER["✅ AFTER<br/>'I'm ready to learn Rust!'"]
    
    BEFORE -->|"Fix TODO"| AFTER
```

### Complete Working Code

```rust
fn greeting() -> &'static str {
    "I'm ready to learn Rust!"
}

#[cfg(test)]
mod tests {
    use crate::greeting;

    #[test]
    fn test_welcome() {
        assert_eq!(greeting(), "I'm ready to learn Rust!");
    }
}
```

---

## 📚 Key Concepts Mind Map

```mermaid
mindmap
    root((🦀 Exercise 1))
        Comments
            // single line
            Ignored by compiler
        Functions
            fn keyword
            Parameters in ()
            Return type after ->
        Types
            &'static str
            String slice reference
            Lives forever
        Testing
            #[cfg(test)]
            #[test]
            assert_eq!
```

---

> *"I am Iron Man."* — And now, YOU are ready to learn Rust! 🦀
