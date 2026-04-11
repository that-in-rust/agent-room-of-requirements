# Executable Specs Templates

Use these templates to convert requests into testable contracts.

## 1) Requirement Contract Template

```markdown
### REQ-<DOMAIN>-<NNN>.<REV>: <Short title>

**WHEN** <trigger or input condition>
**THEN** the system SHALL <primary outcome>
**AND** SHALL <secondary measurable behavior>
**SHALL** <edge-case or default behavior>
```

Authoring rules:
- Use one behavior per SHALL line.
- Use explicit units for performance or capacity claims.
- Keep each requirement independently testable.

## 2) Traceability Matrix Template

```markdown
| req_id | test_id | test_type | assertion | target |
| --- | --- | --- | --- | --- |
| REQ-API-001.0 | TEST-UNIT-001 | unit | returns only implementation entries | correctness |
| REQ-API-001.0 | TEST-INTEG-003 | integration | preserves order across parser + filter pipeline | integration |
| REQ-API-001.0 | TEST-PERF-002 | performance | p99 latency < 500us for 10k entities | latency |
```

## 3) TDD Plan Template

```markdown
### TDD Plan

1. STUB
- Write test stubs for each `REQ-*` ID.
- Define fixtures and expected outputs.

2. RED
- Run tests and confirm expected failures.
- Record failure reason and missing interface/function.

3. GREEN
- Implement minimal code to satisfy each failing test.
- Avoid optimization before behavior is correct.

4. REFACTOR
- Remove duplication.
- Improve naming and decomposition.
- Keep all tests green.

5. VERIFY
- Run full test suite.
- Run build and lint checks.
- Confirm every `REQ-*` has test coverage.
```

## 4) Language-Specific Test Skeletons

### Rust

```rust
#[test]
fn test_req_api_001_filter_implementation_entities_only() {
    // Arrange
    let input = create_test_entities_mixed_list();
    // Act
    let output = filter_implementation_entities_only(&input);
    // Assert
    assert!(output.iter().all(Entity::is_implementation));
}
```

### TypeScript

```ts
it("TEST-UNIT-001 filters implementation entities only", () => {
  const input = createTestEntitiesMixedList();
  const output = filterImplementationEntitiesOnly(input);
  expect(output.every((e) => e.isImplementation)).toBe(true);
});
```

### Go

```go
func TestReqAPI001FilterImplementationEntitiesOnly(t *testing.T) {
    input := createTestEntitiesMixedList()
    output := FilterImplementationEntitiesOnly(input)
    for _, entity := range output {
        if !entity.IsImplementation {
            t.Fatalf("expected implementation entity, got %+v", entity)
        }
    }
}
```

## 5) Vague-to-Executable Rewrite Patterns

| Vague statement | Executable rewrite |
| --- | --- |
| "Make it faster." | "Reduce p99 latency from 5ms to less than 1ms for 10k entities." |
| "Improve reliability." | "Keep successful processing rate at or above 99.9% over 24h." |
| "Handle bad input gracefully." | "Return typed validation errors for malformed input without panics." |

## 6) Quality Gate Template

```markdown
### Pre-Commit Quality Gates

- [ ] Every requirement has a stable `REQ-*` ID.
- [ ] Every `REQ-*` ID has at least one linked test.
- [ ] Tests pass.
- [ ] Build passes.
- [ ] No TODO/STUB/FIXME introduced.
- [ ] Performance claims include explicit metrics and test method.
```
