# Iggy CI/CD Patterns

## Overview

Iggy uses comprehensive CI/CD with strict quality gates and multi-platform testing, and automated artifact publishing.

---

## 1. Pre-commit Hooks (prek)

### Installation
```bash
cargo install prek
prek install
```

### Configuration
Runs automatically on commit, covering:
- `cargo fmt --check`
- `cargo clippy -D warnings`
- `cargo sort --check`
- `taplo` (TOML formatting)
- Typos checking
- Binary artifact detection

---

## 2. Quality Gates

### Rust Quality Checks
```yaml
# .github/workflows/rust.yml
- name: Format
  run: cargo fmt --all -- --check

- name: Clippy
  run: cargo clippy --all-targets --all-features -- -D warnings

- name: Build
  run: cargo build --all-targets

- name: Test
  run: cargo test --workspace

- name: Unused dependencies
  run: cargo machete

- name: Dependency sorting
  run: cargo sort --workspace --check
```

### Additional Checks
```bash
# Typos
typos

# TOML formatting
taplo fmt --check
```

---

## 3. Multi-Platform Testing

### Platform Matrix
```yaml
strategy:
  matrix:
    os: [ubuntu-latest, macos-latest, windows-latest]
    rust: [stable, nightly]
```

### Linux-Specific Features
```yaml
- name: io_uring tests
  run: |
    cargo test --features io-uring
```

---

## 4. Coverage Reporting

### cargo-llvm-cov
```bash
cargo llvm-cov --workspace --branch --fail-under-lines 75
```

### Codecov Integration
```yaml
- name: Upload coverage
  uses: codecov/codecov-action@v3
  with:
    file: ./coverage/codecov.json
    flags: rust
```

---

## 5. Release Automation

### Version Management
```bash
# Automated version bump
cargo release $VERSION --workspace
```

### Crate Publishing
```yaml
- name: Publish to crates.io
  run: cargo publish --token ${{ secrets.CRATES_TOKEN }}
```

### Docker Images
```yaml
- name: Build Docker image
  uses: docker/build-push-action@v4
  with:
    context: .
    push: true
    tags: apache/iggy:${{ steps.version }}
```

---

## 6. Binary Artifacts

### Multi-Target Builds
```yaml
matrix:
  target:
    - x86_64-unknown-linux-gnu
    - x86_64-unknown-linux-musl
    - aarch64-unknown-linux-gnu
    - x86_64-apple-darwin
    - aarch64-apple-darwin
```

### Artifact Upload
```yaml
- name: Upload binary
  uses: actions/upload-artifact@v3
  with:
    name: iggy-${{ matrix.target }}
    path: target/${{ matrix.target }}/release/iggy-server
```

---

## 7. Pre-release Checks

### Binary Detection
```yaml
- name: Check for binaries
  run: |
    if find . -type f -executable -not -path './target/*' -not -path './.git/*' | grep -q .; then
      echo "Binary files detected"
      exit 1
    fi
```

### Security Audit
```bash
cargo audit
```

### Dependency Check
```bash
cargo deny check
```

---

## 8. Performance Benchmarking

### Automated Benchmarks
```yaml
- name: Run benchmarks
  run: |
    cargo bench --workspace --output-format bencher
```

### Regression Detection
```yaml
- name: Compare with baseline
  uses: bencherdev/bencher@v0
```

---

## 9. Documentation Generation

### API Docs
```bash
cargo doc --no-deps
```

### README Updates
```yaml
- name: Update README
  run: |
    cargo readme > README.md
```

---

## Summary: CI/CD Checklist

- [ ] Install pre-commit hooks (prek)
- [ ] Run format check (cargo fmt)
- [ ] Run clippy with -D warnings
- [ ] Run tests with coverage
- [ ] Check for unused dependencies (cargo machete)
- [ ] Sort dependencies (cargo sort)
- [ ] Check for typos
- [ ] Run security audit (cargo audit)
- [ ] Build for multiple targets
- [ ] Upload coverage to Codecov
- [ ] Publish to crates.io
- [ ] Build Docker images
