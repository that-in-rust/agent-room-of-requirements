# Why Rust Backends Need Their Own Playbook

## Big Idea

We first made a general Rust planning skill, and then we realized backend work keeps dragging around extra real-world baggage, so it deserved its own smaller, sharper playbook.

## Why It Matters

A general Rust skill is like a good toolbox. It helps you think about types, boundaries, tests, errors, and reliability.

But backend work is not just "Rust, but on a server." It is more like running a small restaurant kitchen. You are not only cooking one dish. You are also handling tickets, ingredients, timing, storage, handoffs, cleanup, and what happens when something goes wrong in the middle of service.

That is why the split happened.

The general Rust skill is still useful. It is the broad architect.

The backend skill exists because HTTP services keep repeating the same extra problems:

- request handlers and app state
- database writes and migrations
- configuration and secrets
- tracing and request IDs
- auth, sessions, cookies, and password flows
- external API clients and mocking
- retries, idempotency, and timeouts
- background workers and rollout safety

Those are not side quests. For backend work, they are the job.

## Core Ideas Made Simple

### 1. The first Rust skill was broad on purpose

The earlier Rust executable specs skill was built to cover a lot of ground:

- libraries
- CLIs
- async services
- backends
- parsers and protocol code
- contained FFI work

That made it a good "big map" skill.

But big maps are not always the best hiking guide.

### 2. Backend work has a different failure pattern

A library bug often lives inside code you control.

A backend bug often lives in the seams:

- the request parses but the domain rules are wrong
- the code works but the migration order is dangerous
- the API client is fine but retries duplicate work
- the login flow works but leaks useful failure clues
- the endpoint passes unit tests but fails when the app, database, and HTTP client are wired together

That is why backend work benefits from **integration-first thinking**.

The important question becomes:

> "Does the whole machine behave correctly when all the pieces touch?"

Not just:

> "Does this Rust function look clean?"

### 3. The backend skill is a field kit, not a replacement

`rust-executable-specs-01` is still the general-purpose Rust planner.

`rust-web-backend-delivery-01` is the field kit for Rust services and APIs.

Think of it like this:

- general Rust skill = architect + structural engineer
- backend Rust skill = architect + site supervisor + operations checklist

The backend skill does not replace the Rust fundamentals.

It narrows the attention onto the things that backend work repeatedly gets wrong:

- transport vs domain validation
- persistence and migration safety
- secrets and configuration layering
- tracing and operator visibility
- auth failure shaping
- idempotency and durable retries
- deciding when a request should become background work

### 4. This split makes triggering better

A skill is most useful when it wakes up for the right problem.

If one Rust skill tries to own everything, its instructions get fatter and its trigger gets fuzzier.

Then the model has to sift through library advice, backend advice, and operations advice all at once.

That is like packing a camping bag, a toolbox, and a kitchen sink for a one-day walk.

By splitting the backend patterns into their own skill:

- the generic Rust skill stays cleaner
- the backend skill becomes more precise
- the references become easier to load in the right order
- the user gets advice that matches the actual job faster

### 5. The real lesson from the follow-up work

The last Rust-skill commit gave us a strong general Rust planning layer.

The follow-up discussion exposed the missing piece:

Rust web backends are not special because they use a server framework.

They are special because they sit at the intersection of:

- code correctness
- system wiring
- operator visibility
- security behavior
- deployment sequencing

That combination is what justified a sibling skill instead of a few extra paragraphs in the older one.

## Tiny Example

Imagine the request is:

`Build a Rust newsletter signup API with persistence and email confirmation.`

The general Rust executable specs skill is good at saying:

- write `REQ-*` contracts
- pick verification strategy
- design boundaries carefully
- keep types and errors honest

That is helpful, but incomplete.

The backend delivery skill adds the missing backend questions:

- How do we spin up the app for integration tests?
- How do we isolate the database and apply migrations in tests?
- How do we mock the email API cleanly?
- Where do config and secrets live?
- What do we trace for request correlation?
- What happens if the email provider times out?
- Which part must happen in the request, and which part should move to a durable worker later?

Same project. Same language. Different level of real-world mess.

That is why the backend skill exists.

## What To Remember

The general Rust skill teaches you how to build a strong machine. The backend Rust skill teaches you how to run that machine safely in the messy outside world.
