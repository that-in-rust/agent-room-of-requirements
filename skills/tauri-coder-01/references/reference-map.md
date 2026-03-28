# Reference Map

Use this file to route quickly before loading the full Tauri doctrine.

## Jump Points

- `Chosen Patterns`: fast triage of the scored Tauri-specific reliability surface
- `Non-Negotiables`: the defaults that should survive most refactors
- `Pattern 1` to `Pattern 3`: command shape, managed state, and serializable error flow
- `Pattern 4` to `Pattern 7` and `Pattern 20`: capabilities, filesystem scope, plugin safety, typed invoke contracts, and window-label security
- `Pattern 8`, `Pattern 9`, `Pattern 17`, and `Pattern 18`: channels, events, binary IPC, and raw request handling
- `Pattern 11`, `Pattern 19`, and `Pattern 25`: sidecars, permission scoping, and packaged external binaries
- `Pattern 14`, `Pattern 21`, and `Pattern 26` to `Pattern 29`: updater, tray, single-instance, deep-link, CLI, and window-state lifecycle
- `High-Confidence Anti-Patterns`: mistakes to reject before shipping
- `TDD-First Checks For Tauri`: final implementation and verification prompts

## Section Search

- `rg '^##|^###' references/doctrine.md`
- `rg 'Chosen Patterns|Non-Negotiables|High-Confidence Anti-Patterns|TDD-First Checks' references/doctrine.md`

## Use Order

1. Read `Chosen Patterns`.
2. Open the specific pattern sections that match the boundary you are touching.
3. Finish with `High-Confidence Anti-Patterns` and `TDD-First Checks For Tauri`.
