---
name: tir-polyglot-idioms
description: >-
  Cross-language idiomatic patterns (TypeScript, Go, Java, Kafka, Kubernetes, Terraform, ASP.NET Core + Angular) and extracting idioms from reference codebases. Use when implementing or reviewing multi-language stacks.
---

# TIR Polyglot Idioms

Focused skill for polyglot engineering idioms, ASP.NET Core + Angular full-stack changes, and extracting idioms from reference repos. Companion reference: [reference.md](../tir-system-design/reference.md). Related: [tir-system-design](../tir-system-design/SKILL.md).

## 1. Purpose

Use this skill to make or review an architecture decision whose consequences cross a process, service, language or team boundary, and to write code in each stack the way that stack's own practitioners would. It gives you a decision method (estimate, position, select, verify), a conditional pattern catalogue, per-stack idiom rules for TypeScript/JavaScript, Java/Spring, Go, C#/.NET, Angular, Kafka and infrastructure-as-code, a vertical-slice discipline for ASP.NET Core plus Angular, and a method for extracting new idioms from high-quality codebases.

The detailed catalogue, numbers, extended examples and evidence limits live in [reference.md](../tir-system-design/reference.md). Everything needed to act is in this file.
## 2. When to use, when not to use

Use it when:

1. "Design a notification service for 10 million daily users. Do we need Kafka?"
2. "Review this pull request: it adds a retry around the payment call and a new Redis cache."
3. "We have a Go service publishing events consumed by a Spring Boot service. What should the contract and the consumer look like?"
4. "Add a profile-edit endpoint in ASP.NET Core and wire the Angular form to it, including the conflict case."
5. "Here are text dumps of tokio, axum and serde. Build me an idiom archive I can inject into coding prompts."

Do not use it when:

1. The work is a single-stack implementation in a stack with its own skill. A TypeScript/Express/Mongoose service belongs to `typescript-backend`; a React screen to `react-frontend`; Kotlin to `kotlin-backend`; Python to `python`. Rust has no skill in this library, so label Rust implementation answers as external research. Return here only for the cross-service or cross-language part.
2. The task is to write requirements, acceptance criteria or a test plan with no architecture question. Use `executable-specs`.
3. The task is to find why one test or one request fails. Use `review-verify-debug`, and come back if the root cause turns out to be a boundary or topology decision.

Route by who owns the acceptance test, not by file extension. A `.ts` file can be an Angular consumer of a .NET contract (here), a Node service (elsewhere) or a React component (elsewhere).
## 3. Operating modes

Declare one mode before reading the catalogue. Browsing without a mode turns into pattern shopping: picking a pattern because it is impressive, then looking for a problem.

| Mode | You are doing | Start with | Output |
|---|---|---|---|
| Estimator | Sizing load, storage, cache, servers, bandwidth | Section 7.1 formulas | Numbers with assumptions |
| Designer | Choosing patterns | Estimates, then section 7.2 and 7.3 | Decision worksheet (section 11.1) |
| Reviewer | Checking an existing design or diff, or a reference others will design from | Anti-pattern screens (section 15); section 6.7 for a reference | Findings with failing condition and gate |
| Explainer | Teaching or comparing options | Trade-off script (section 7.2) | Comparison with what is lost |
| Idiom implementer | Writing code in one or more covered stacks | Section 8 for the stack | Code plus its compile/test/lint gate |
| Slice builder | One behavior across ASP.NET Core and Angular | Section 9 | Behavior ledger (section 11.3) plus cross-layer test |
| Idiom extractor | Mining patterns from codebases | Section 10 | Idiom records in the schema of section 11.5 |

Estimator normally precedes designer. Estimate 5,800 QPS before discussing sharding; ask about data volume before recommending a single replayable stream pipeline. If a task mixes modes (for example interview practice and a production change), do them as separate steps with separate outputs.
## 4. Workflow

1. **State the reader and the decision.** Name who will act on the answer, what state they start from (a design choice, a failure symptom, a dependency map, an unclear boundary), which decision is being made, and when it will be used. If you cannot name the decision, ask.
2. **Pick the mode** (section 3) and say so.
3. **Discover the project.** List the stacks present and their real gates before proposing anything. For a .NET/Angular workspace run the discovery command in section 14.1; for others read the build files, lint config, CI workflow and three neighboring source files to learn the local dialect.
4. **Estimate.** Compute QPS, peak, storage, cache size, server count and bandwidth from stated or assumed inputs (section 7.1). Write the assumptions down. A result of 115 QPS can justify a single database; do not skip this because the system "sounds big".
5. **Position.** For each trade-off axis that matters (section 7.2), write the business fact that selects a side. Do not prefill positions from a previous design; a prefilled worksheet is a rubber stamp.
6. **Select.** Choose patterns from section 7.3 or the reference catalogue. Copy each pattern's use-when, avoid-when and anti-pattern into the worksheet, and record at least one rejected alternative and why.
7. **Classify the decision as Adopt, Adapt or Avoid** (section 6.2) and name the cost of being wrong: what would have to be undone or inspected.
8. **Write the failure path.** For every effect, name its bound: timeout, retry cap, idempotency identity, compensation, dead-letter route or acknowledgment condition (section 6.4). Advice lacking one of these is rejected.
9. **Translate into each stack's idiom.** Apply the four cross-stack families (section 6.3) using the stack's own form from section 8 or 9. Translate the idea, not the syntax.
10. **Attach a gate to every recommendation**: a command, a metric with a threshold, a checklist item or a review question (section 14). A configuration with no matching gate is unverified.
11. **Label evidence.** Mark each claim as a project observation, a catalogue fact, a refreshed external fact, an inference, an illustration or a measured result (section 6.1). Date product-specific numbers.
12. **Record the decision** using the worksheet or ledger templates in section 11, including the reversal trigger and migration sequence.
13. **Run the gates you named** and report results with their limits (section 13). Run the closing self-check (section 17).

For implementation work inside one stack, steps 4 to 7 shrink to a sentence each, and the stub, red, green, refactor cycle of section 8.1 takes over.
## 5. Scope boundaries

- Covered stacks: TypeScript and JavaScript, Java and Spring Boot, Go, C# and ASP.NET Core with EF Core, Angular, Kafka, Docker, Kubernetes, Terraform, GitHub Actions. A thin MERN layer (MongoDB, Express, React) is included only for cross-stack comparison; attach a confidence warning when leaning on it.
- Python and Rust have no idiom catalogue here. For Rust the extraction method of section 10 applies, but its prompts are a method, not a finished set of Rust idioms. For an unmapped stack either route to that stack's skill, extract a new idiom record, or label the answer as external research.
- Cross-stack seams (for example a Go producer publishing Avro to a Java consumer) need explicit contract work; neither stack's idioms settle the wire format.
- The guidance stops being sufficient when the work spans several independent systems, more than one ownership boundary, production traffic with no stated service-level objective, unbounded source discovery, or a large codebase with no dependency graph to narrow it. In those cases assign one verification owner, add merge checkpoints, and narrow the graph first (`codebase-navigation`).
## 6. Core rules

### 6.1 Evidence and conditions

1. No pattern is universally correct. Every recommendation carries three parts: **Use when**, **Avoid when**, **Anti-pattern**. Matching conditions to the situation is the skill; reciting solutions is not.
2. Summaries drop conditions first. Before reusing any pattern statement, check that its conditions survived. "Use cache-aside" without "set a TTL; tolerate stale reads" is a stripped claim.
3. Keep three labels apart in every answer: what the project or the catalogue says, what a retrieved current source says, and what you inferred from combining them. An unretrieved URL is a lead, not evidence.
4. Use two-hop wording for upstream attribution: "the catalogue attributes hybrid feed fan-out to Twitter", not "Twitter engineering says". Second-hand latency figures stay second-hand.
5. Conceptual claims (quorum overlap, CAP reasoning, consensus, availability arithmetic) age slowly. Product numbers (queue throughput limits, default concurrency, API versions, required auth flows, memory sizes) age at release cadence. Date them and re-check before relying on them.
6. Do not average conflicting thresholds. A 1 to 5 percent canary and a 10 percent canary are answers to different contexts. Check context equivalence first, prefer the more specific source for configuration and the better-corroborated one for principles, and cite both when the conflict remains.
7. Worked numbers are assumptions, not constants: a 7-character Base62 key, a 10,000-follower hybrid threshold, 4 MB chunks, a 50 percent circuit-breaker threshold all change with the workload.
8. Never state a performance result without its harness, workload, environment, population and guardrails. Figures quoted from older material without a harness are illustrations. Do not claim speed from a pattern alone.
9. Compilation proves local static consistency. A test proves its own scope. A generated-client diff proves drift only when generation is reproducible and the diff reviewed. One end-to-end test proves one deployed behavior in one environment. `terraform plan` shows a diff, not behavior. A green CI badge alone proves nothing about fit.
10. Interview-scoped designs and illustrative code need hardening before production reuse. Interview time boxes are interview facts, not delivery schedules.

### 6.2 Deciding: Adopt, Adapt, Avoid

| Decision | Choose when | Cost | Check |
|---|---|---|---|
| Adopt | Greenfield code, or project convention and current evidence agree | Fast; may copy a stale assumption | Is the pattern present in both the project and a current source? |
| Adapt | Brownfield code with a discoverable, uniform local dialect; or the responsibility fits but the example conflicts with local convention or changed guidance | Needs an explicit inference note | Are observation, external fact and inference labelled separately? |
| Avoid | Evidence is thin or conflicting, the stack is unmapped, the mechanism is duplicate or ownerless | Needs deeper research | Is there a confidence warning and a named next route? |
| Escalate | The change persists in schema, security policy, generator ownership or release order | Slower | Is there an owner and a rollback trigger? |

- Sample three neighboring files and record which branch you took and why.
- Local consistency beats catalogue fidelity until a migration is declared. Two `Result` dialects in one service (hand-rolled and a library) is worse than either.
- Safety outranks consistency. Never preserve ignored errors, missing authorization or unbounded retries for the sake of matching the surroundings.
- A harmful local convention is fixed by a bounded migration: one module per cycle, behind gates, with a stated end.
- Every Avoid names a rollback, an escalation or the next reference to consult.
- Override the default ordering at the earliest observed failing boundary. An authorization escape, a malformed payload, a duplicate write or a stale client outranks everything downstream of it; fix it, keep the reason, and rerun dependent gates.

### 6.3 The four cross-stack families

Apply these before any single-stack nicety whenever a codebase spans two or more stacks. A rule earns cross-stack status only when it appears in at least three stacks.

| Family | TypeScript / Angular | Java / Spring | Go | C# / .NET | Kafka / infrastructure |
|---|---|---|---|---|---|
| Explicit types at boundaries | Branded IDs, runtime schema parse of `unknown`, discriminated unions | Records with validating compact constructors, sealed interfaces | Small interfaces, concrete return structs, typed sentinel errors | Records, `required`/`init` DTOs, closed outcome hierarchies | Schema Registry with Avro or Protobuf; typed, validated Terraform variables |
| Contextual error values | `Result<T, E>` or typed error unions for expected failures | Sealed `Result`, `Optional` as return type only, domain exception hierarchy | `fmt.Errorf("op: %w", err)`, `errors.Is` / `errors.As` | Typed outcomes mapped once at transport; faults stay faults | Dead-letter records carrying original topic and error headers |
| Constructor-injected dependencies | Interface parameters in constructors; Angular `inject()` | Constructor injection, never field injection | Accept interfaces, functional options | Constructor or primary-constructor injection | Modules with typed inputs instead of hardcoded values |
| Idempotent effects | Idempotency key on writes; cancellation with `AbortController` | Explicit `@Transactional` boundaries, optimistic `@Version` | Context deadlines, safe retry of idempotent calls | Cancellation token propagation, version checks on update | `enable.idempotence=true` with `acks=all`; consumers deduplicate; temp-file-plus-rename for storage |

The shared move behind all four is making illegal states unrepresentable and hidden dependencies visible. Boolean flags hide state machines, service locators hide dependencies, anemic models hide invariants.

Translate idioms, not syntax. Go-style `(value, err)` tuples pasted into TypeScript are an accent; use a `Result` union. Java `Optional` discipline becomes strict null checks and unions in TypeScript. Do not paste a TypeScript `Result` into Java where a sealed `Result` already exists. A retry-with-jitter helper ports only after its sleep primitive and error taxonomy are adapted.

### 6.4 Failure paths, retries and backpressure

1. Reject failure-path advice that lacks a bound. Each effect needs at least one of: timeout, retry cap, compensation, dead-letter route, acknowledgment condition.
2. Retry only with an idempotence story: an idempotency key, an idempotent producer, or a naturally idempotent operation. Disabling a button is not idempotency. Client debounce is not idempotency. A successful retry does not prove there was no duplicate.
3. Classify before retrying.

| Outcome | Automatic retry? |
|---|---|
| Accepted, validation rejected, authentication or authorization failure, malformed or unsupported payload, cancelled, obsolete | Never |
| Not found, conflict | No; refresh or reconcile instead |
| Rate limited (429), known-transient with known no effect, 5xx, timeout on a read | Yes, bounded |
| Timeout or connection loss on a write with unknown effect | Only after an operation identity lookup or reconciliation |
| Partial failure across dependencies | Only with defined compensation or repeatability |

4. Implement these together, never one alone: exponential backoff (`base × 2^attempt`), full jitter (`random(0, min(cap, base × 2^attempt))`), a retry budget shared across the fleet and across layers (browser, gateway, service, SDK, database, message consumer) per logical operation, retryable-error discrimination, and a stop condition. An open circuit or an exhausted budget stops retries.
5. Derive attempt counts, factors, caps, queue sizes and circuit thresholds from the dependency's contract, its latency and recovery behavior, the consequence of a duplicate, capacity and the user's deadline. The catalogue's numbers (section 12, item 8) are starting examples.
6. Inner timeouts are shorter than outer ones, so inner layers finish before callers give up. Example ladder: edge 60 s, gateway 55 s, service 50 s, database 30 s. Propagate the remaining deadline (for example an `X-Request-Deadline` header, a Go `context`, a .NET `CancellationToken`).
7. Bound concurrency at the constrained resource. Every queue declares capacity, ordering, fairness, expiry, cancellation, restart behavior and what happens when full. Shed optional work first; pair client retries with server-side load shedding or admission control.
8. Circuit breakers go around external dependencies, not local operations. Define the failure class, the half-open probe and what the user sees while open.
9. Sagas need a compensation for every step. Choreography suits roughly two to four services; beyond that, or when the workflow needs visibility, orchestrate. Do not use a saga where immediate consistency is mandatory.
10. Reconnect is not replay. A realtime stream needs a snapshot, an order or cursor, gap detection, deduplication, resync and auth renewal, unless the UI states that messages are ephemeral and can resync.
11. Cancellation must be honest: propagate the token to every effect and define the commit boundary. A durable accepted job may outlive the request only by contract.
12. For work on documents and plans, keep retries separate from runtime retries: classify the failed check (transient, stale evidence, missing context, contradiction), allow one bounded refresh of stale evidence, then escalate. Stop implementation when sources, critique or gates are red.

### 6.5 Observability

1. Establish the join key first: propagate W3C Trace Context (`traceparent`, `tracestate`) across every hop, including into message headers.
2. Emit structured JSON logs carrying `timestamp`, `level`, `service`, `trace_id`, `message`. Log identifiers and counts, never full payloads or personal data.
3. Use RED for services (rate, errors, duration), USE for resources (utilization, saturation, errors), and the four golden signals (latency, traffic, errors, saturation) overall.
4. Bound metric cardinality. Never use user IDs, request IDs, emails, raw routes, validation input, stack traces or SQL as labels. A working ceiling from the catalogue: under 100 values per label and under 10 million series in total. Per-user labels can make monitoring the outage.
5. Tail-sample every error and slow trace; head sampling is cheaper but misses rare failures.
6. Alert on user-visible symptoms and error-budget burn; keep cause alerts as tickets. Example multi-window policy: page at 14.4× burn over 1 hour, ticket at 6× over 6 hours. Every alert has an owner and an action.
7. Pair every pattern with its proof series: circuit breaker with an error-rate series, cache with hit ratio and origin load, retry with attempts and duplicates, SLO with an error-budget policy.
8. Missing telemetry is unknown, not zero. Verify one incident or one synthetic operation end to end across traces, logs and metrics.

### 6.6 Performance and scale

1. Budget from the latency ladder before designing: memory in nanoseconds, SSD in microseconds, disk seeks and same-region network in milliseconds, cross-region in hundreds of milliseconds. Two cross-region hops make a 100 ms goal impossible; redesign regionally instead of tuning cache lookups.
2. Inspect structural idioms first (N+1 queries, missing pagination, unbounded payloads, absent pooling). Demand percentiles only on latency- or throughput-critical paths with an owner-supplied target.
3. P99, not the mean, gates acceptance. Verify with staged load and a histogram quantile (section 14.4).
4. Every pattern has an envelope and a successor: vertical scaling ends at the hardware ceiling, single-leader replication at write saturation, push fan-out at the celebrity threshold, offset pagination at large tables, a monolith at team and deploy contention. Instrument the distance to the boundary and plan the migration before reaching it.
5. Avoid both premature graduation (shards at startup load) and overdue graduation (a saturated envelope causing an outage). Cheap insurance, such as including a shard key in a single-database schema, is defensible. Volume alone does not force a new architecture.
6. Never copy example bounds (worker counts, concurrency limits, replica counts, resource limits). Derive or measure them locally.
7. When a scale mechanism's pressure disappears and the simpler option passes the gates, remove the mechanism. Managed infrastructure does not own your semantics, policy, failure handling, budgets or recovery.

### 6.7 When the thing under review is a reference

Sometimes the artifact to review is not a design or a diff but a reference, a skill or a pattern catalogue that others will design from. Hold it to these requirements. To write or restructure one, use `authoring-skills-and-references`; this section says what the result must contain.

Every reference, whatever its subject:

1. Names the primary reader, starting state, decision and moment of use, and shows the user journey with happy and failure paths.
2. Gives Adopt, Adapt or Avoid guidance with trade-offs and the cost of being wrong, not generic pattern rows. Headings that only list what a source mentions become ordered guidance.
3. States the source hierarchy: canonical, supporting, legacy or duplicate; primary, secondary, merely historical.
4. Has one good, one bad and one borderline example, and review questions that discriminate between them.
5. Has success criteria, leading indicators, failure signals, telemetry and a revision feedback loop.
6. Is completed in this order: role-based opening scenario; the subject's own artifact; a worked before/after or end-to-end trace; subject-specific failure modes; a use, do-not-use and adjacent-reference decision table; a completeness checklist usable without rereading the sources.
7. Where agent work is involved, shows prompt and context selection, tool calls, checkpoints, verification and the learning captured for the next run, and defines completion by user outcome with negative tests, measurable gates, traceability and handoff or resume behavior.

Evidence obligation: a reference built on one mapped source is thin and owes adjacent-source discovery plus a confidence warning before it is treated as canonical. Two to six sources is usable and owes an opinionated hierarchy of primary, secondary and merely historical sources. Eight or more is broad and owes prioritization and duplicate collapse. (These bands are the ones the critique applied: 1, 2 to 6, and 8 to 16 sources. It saw no reference with seven and states no cut-off between usable and broad, so place seven by judgement.) External sources owe recency, version and authority notes; four or more external sources must be compared, not listed.

Each family of reference owes its own depth, its own worked example and subject-specific artifacts:

| Family | Depth it must add | Worked example it must add | Subject-specific artifacts |
|---|---|---|---|
| Agent context and orchestration | Agent user journey, context budget policy, delegation failure modes, escalation rules, observability, success and failure telemetry | A before/after task trace: prompt, context selection, tool calls, checkpoints, verification, learning captured for the next run | Context budget policy stating what belongs in the prompt, in a file, in memory or in a sub-agent handoff; agent charter (owner, user, trigger, tool budget, escalation path, retirement rule); debate-quality rubric (convergence criteria, dissent handling, evidence thresholds); prioritization model (now/next/later cuts, opportunity sizing, kill criteria) |
| Method, explanation and skill references | Audience definition, prioritization logic, worked examples, edge cases, decision criteria, explicit non-goals | A role-based usage guide with examples, trade-offs, common mistakes and concrete completion checks | Canonical-source policy, freshness workflow and a safe-update example (polyglot idioms); input/output contracts, evaluation prompts and bad-prompt rewrites; activation criteria, progressive-disclosure boundaries, good invocations and misuse cases (skills) |
| Creative and generative work | Creative brief template, taste criteria, iteration loops, artifact-specific verification, weak versus strong outputs | A creative cycle from prompt to draft to critique to final artifact, with acceptance criteria and regeneration triggers | Creative constraints, deterministic seed strategy, iteration scoring, export QA; control design, saved states, inspectability and exploratory learning outcomes (interactive playgrounds); scenario assumptions, leading indicators, reversal triggers, decision checkpoints (timeline simulations) |
| Writing, documentation and visual explanation | Reader segmentation, narrative sequence, examples, scannability standards, before/after rewrites, comprehension checks | A reader journey map plus one polished exemplar section | Reader promise, outline logic, before/after rewrite, plain-language acceptance test; layout constraints and terminal width rules; information architecture, responsive QA, visual regression checks; diagram grammar and a visual QA rubric |
| Branch and worktree delivery | Branch risk matrix, dirty-worktree handling, remote failure handling, PR and issue workflow, recovery when verification fails | A maintainer playbook with exact commands, decision points, expected outputs and rollback or no-rollback boundaries | Dirty-worktree matrix, commit scope rules, push and PR decision criteria, recovery commands |
| Plugins and integrations | Capability boundaries, install and update lifecycle, permissions, failure recovery, marketplace readiness, support-burden analysis | A decision tree plus an end-to-end plugin example covering manifest, invocation, tests, docs, versioning and rollback behavior | Manifest schema, compatibility matrix, validation gates, install-failure examples; command anatomy and argument handling; hook lifecycle, safety constraints, bypass policy; resource and tool boundary rules with a permission model; configuration schema with migration behavior; for payment integration: payment state machine, webhook idempotency, reconciliation, fraud handling, support escalation flow |
| Executable specifications, verification and test-first | Definition of done by user outcome, negative tests, sample failing output, traceability from requirement to test to artifact, refactor debt policy | A complete miniature feature: WHEN/THEN/SHALL requirement, RED output, GREEN output, final audit checklist | Claim-to-evidence matrix with a freshness requirement and examples of insufficient verification; requirements-to-tests trace with measurable acceptance gates; RED and GREEN evidence, refactor policy, resume-ready checkpoints |
| Architecture, dependency mapping and debugging | Decision records, trade-off matrices, dependency maps, failure taxonomy, blast-radius analysis, measurable validation signals | A diagnostic or design worksheet: symptoms, hypotheses, probes, architecture options, rejected alternatives, verification gates | Boundary options, rejected alternatives, decision records, migration sequencing (system design); graph-building assumptions, false-positive handling, ownership map; symptom-to-hypothesis loop, repro minimization, probe ordering, confidence scoring |
| Front end and TypeScript reliability | User workflow states, component ownership, server/client boundaries, accessibility gates, performance budgets, empty, error and loading states | A real screen-level example: state model, component contract, interaction map, tests, visual checks, accessibility review | Request lifecycle diagrams, persistence boundaries, observability hooks, failure-mode tables (back-end reliability); component ownership, data-fetching boundary, rendering budget; quality-bar examples, lint and test gates, review rubrics, release-blocker definitions (quality and anti-pattern gates) |
| Kotlin back end and language | Framework trade-offs between Spring Boot, Ktor and coroutine-first design, Gradle conventions, transaction boundaries, operational runbooks | A thin-slice service walkthrough: request model, validation, coroutine scope, database boundary, tests, failure-mode handling, release gate | Request lifecycle diagrams, persistence boundaries, observability hooks, failure-mode tables (playbook and entry point); runbooks for deploy, rollback, SLO breach, logging, tracing and incident review (runtime operations); threat models, abuse cases, permission boundaries, supply-chain review gates (security); fixture strategy, test pyramid, red/green transcript, flaky-test policy (testing); quality-bar examples, lint and test gates, review rubrics, release-blocker definitions (quality gates); routing rules for canonical source selection and for stale or conflicting sources; canonical-source policy and freshness workflow; activation criteria and misuse cases (language entry point) |
| Python | pyproject decisions, typing strictness, pytest fixture strategy, runtime validation, dependency hygiene, a gradual adoption path | An adoption ladder from loose scripts to a typed package, with mypy, ruff and pytest gates and examples of agent-safe refactors | Activation criteria, progressive-disclosure boundaries, good invocations and misuse cases (entry point); quality-bar examples, lint and test gates, review rubrics, release-blocker definitions (quality gates); routing rules for canonical source selection and for stale or conflicting sources; canonical-source policy, freshness workflow and safe-update examples (reliability reference) |
| Rust | Ownership, error and async design trade-offs, crate-level boundaries, benchmark expectations, rejected non-idiomatic alternatives | A worked example from requirement to API shape, Result and Error type, tests, benchmarks and refactor checks | Request lifecycle diagrams, persistence boundaries, observability hooks, failure-mode tables; runbooks for deploy, rollback, SLO breach, logging, tracing and incident review (runtime operations); threat models, abuse cases, permission boundaries, supply-chain review gates; fixture strategy, test pyramid, red/green transcript, flaky-test policy; quality-bar examples, lint and test gates, review rubrics, release-blocker definitions; requirements-to-tests trace, negative examples, measurable acceptance gates, audit checklist (executable references); routing rules; activation criteria (idiomatic skill) |
| Tauri desktop | Command boundary design, IPC risk, platform permissions, asset bundling, update strategy, end-to-end desktop verification | A feature slice: front-end call, Rust command, permission surface, test harness, packaging gate, failure recovery | Quality-bar examples, lint and test gates, review rubrics, release-blocker definitions (conventions); requirements-to-tests trace, negative examples, measurable acceptance gates, audit checklist (executable playbooks, maps and skills) |

Where a subject has no artifact of its own listed, it owes at least one concrete example with user goal, decision point, failure mode and verification gate. The subject-by-subject list is in reference.md under "Completeness Checklist".
## 8. Polyglot idioms

### 8.1 Workflow shared by every stack

Drive implementation as **STUB → RED → GREEN → REFACTOR**:

1. **STUB.** Declare interfaces, DTOs or value objects, and the error union before any implementation.
2. **RED.** Write a behavior test that fails. Include the negative case first (for an order service: insufficient stock returns a typed error, reserves nothing and publishes nothing).
3. **GREEN.** Implement the minimum path. On failure return the typed error and perform no save and no publish.
4. **REFACTOR.** Keep tests green while adding boundary validation, structured logs, metrics, correlation and error context, compensation and documentation.

Smallest complete instance of the cycle, the same in TypeScript, Java and Go. STUB a `UserService` with `createUser`, `findById` and `updateUser` and the error union `'EMAIL_EXISTS' | 'INVALID_DATA' | 'NOT_FOUND'` (absence is `User | null` in TypeScript, `Optional<User>` in Java, `(*User, error)` in Go; the Java `UserId` record rejects null and blank). RED: build the service from a mocked repository and a mocked event publisher, stub `existsByEmail` to false and `save` to succeed, call `createUser` with `test@example.com`, assert success and the email; it fails because the implementation does not exist. GREEN: if `existsByEmail(email)` is true return the typed error (`Result.err('EMAIL_EXISTS')`; `Result.failure(UserError.EMAIL_EXISTS)` inside a `@Transactional` method; `ErrEmailExists` in Go); otherwise create the user, save it, publish `UserCreatedEvent`, return success. Go wraps infrastructure errors with context: `fmt.Errorf("checking email existence: %w", err)` and `fmt.Errorf("saving user: %w", err)`. REFACTOR adds input validation, structured logging, metrics, error context and documentation. The code for all three stacks is in reference.md.

Never quote GREEN-phase code as final, never copy a refactored service without its tests, and keep `SHALL NOT` assertions when porting a behavior to another stack. Infrastructure is different: Terraform validation blocks and Kubernetes probes are declarative gates, not red-green cycles. Whether tests-first pays off for throwaway exploration is untested; say so if asked.

Specify behavior as `WHEN … THEN … SHALL` with preconditions, postconditions and error conditions. Example: an absent email plus a valid password creates the account, sends verification and returns 201 with the user ID; an existing email returns 409 and creates nothing. For the full specification method use `executable-specs`.

Layering, in every stack: presentation (controllers, handlers, resolvers, CLI) → application (use cases, commands, queries, DTOs) → domain (entities, value objects, events, aggregates) ← infrastructure (repositories, external APIs, queues, caches). Dependencies point inward. The domain has zero external dependencies; infrastructure implements interfaces owned by the domain or application layer. Separate bounded contexts, connect them with events, and do not span one transaction across aggregates.

Test shape: static checks first, mostly integration tests, unit tests for complex pure logic, end-to-end only for critical user paths. Arrange-act-assert; behavioral names such as `should_[expected]_when_[condition]`; mock only at boundaries; assert behavior, not private calls. Working targets: unit tests under 100 ms, integration tests under 5 s, no flakiness in CI.

Error category map, shared across stacks:

| Category | Status | Retry | Log level |
|---|---|---|---|
| Validation | 400 | No | WARN |
| Authentication | 401 | No | WARN |
| Authorization | 403 | No | WARN |
| Not found | 404 | No | DEBUG |
| Conflict | 409 | No | INFO |
| Rate limited | 429 | Backoff | WARN |
| Server error | 500 | Limited | ERROR |
| Unavailable | 503 | Backoff | ERROR |

Diagrams in repository documents use Mermaid so they render on the hosting platform.

### 8.2 TypeScript and JavaScript

- Compiler: `strict`, `noUncheckedIndexedAccess`, `noImplicitReturns`, `noFallthroughCasesInSwitch`, `noImplicitOverride`, `exactOptionalPropertyTypes`, `noPropertyAccessFromIndexSignature`. Prefer `unknown` to `any`. Use path aliases instead of `../../../` chains.
- Layers: language primitives first, runtime built-ins second, ecosystem packages third. Reach for a package only when the lower layer cannot do the job.
- Branded IDs: `type UserId = string & { readonly brand: unique symbol }`, created by a validating factory. The compiler must reject passing an `OrderId` where a `UserId` is expected; prove it with `// @ts-expect-error`. Brands vanish at runtime, so they complement parsing, never replace it.
- State: discriminated unions (`idle | loading | success(data) | error(error)`) switched exhaustively with a `never` default. Boolean flags permit impossible combinations.
- Expected failures: `Result<T, E> = { ok: true; value: T } | { ok: false; error: E }` or a library equivalent with `map` and `flatMap`. A domain error class carries code, status, timestamp and context; unknown throws are normalized to `Error` and mapped to a generic 500.
- Boundaries: parse all external data with a runtime schema and infer the static type from it. Never write `json as User`.
- Literal precision: `as const`, `satisfies` (checks without widening), type predicates (`x is Admin`) for guards, `K extends keyof T` constraints, template literal types for routes and event names, mapped and conditional types with `infer`, overloads when the input shape selects the return type.
- Async: `Promise.allSettled` for independent work that may partially fail; `AbortController` for cancellation and timeouts with `clearTimeout` in `finally`; a bounded queue or limiter for concurrency; no unhandled rejections.
- Retry helper (defensive form): retry only network errors and 5xx by default; `shouldRetry` and `onRetry` hooks; exponential delay with jitter and a cap. Do not retry schema validation errors.
- Dependency injection: pass interfaces into constructors and test with typed mocks. Do not instantiate hard dependencies inside services.
- Browser background work: bound it with a worker pool, not one worker per task. A pool holds a queue of work and a register of workers and takes a worker factory (`createWorker`) and a maximum size (`maxPoolSize`, default 15 in the Neo4j Browser `WorkPool`). Finding a worker: reuse one whose state is free; else create and register one only while the pool is below the maximum; else return nothing and leave the work queued. Treat it as a small scheduler with queue, registry, worker state and completion hooks. Use it for expensive, cancelable tasks that can be serialized through worker messages; not for latency-sensitive UI updates that should stay synchronous, nor for tasks that need shared mutable worker state across jobs. Lifecycle bugs leave work stuck in the busy state, and cancellation must cover both queued and in-flight work. When adding work types keep ID-based lookup, finish hooks and `next()` scheduling, and test queued cancellation and pool saturation.
- Builders over a schema: a fluent `add(resource, lifecycle, options?)` records `{config, lifecycle, dependencies: []}` (plus `remoteAccess: true` when `options.remoteAccess` is set) in an internal `Partial<StackConfig>` keyed by resource ID and returns `this`; `build()` returns `StackSchema.parse(this._config)` and is the only place a deployable configuration is produced. Builders accumulate intent; one schema-backed boundary turns intent into a validated artifact, so invalid partial state never leaks. Use it for SDKs that assemble infrastructure, workflow or policy objects across many small calls; skip it when construction is trivial and parsing directly is clearer. Builder methods must preserve invariants until `build()`. For a new resource type: schema fields first, builder affordances second, then tests that call `build()` and do not inspect private builder state.
- Plain JavaScript: `const` by default, strict mode, `Object.freeze` for configuration, `#private` fields or `WeakMap` for private data, `at(-1)`, `Object.fromEntries`, `Object.groupBy`, `pipe`/`compose`, async generators for pagination, `Promise.withResolvers`. Benchmark critical paths instead of assuming.

### 8.3 Java and Spring Boot

- Records for DTOs, value objects and projections; validate and normalize in the compact constructor. Money rejects negative amounts, fixes scale and refuses mixed currencies.
- Sealed interfaces for domain events and for `Result` (`Success`, `Failure`) with exhaustive `switch` and no `default`.
- `Optional` is a return type only. Never an `Optional` parameter or field; collections return empty, not `Optional`; never call `.get()` unchecked.
- Constructor injection exclusively (a generated required-args constructor is fine). Field injection hides dependencies and forces a Spring context in tests. Segregate reader and writer interfaces.
- Typed, validated configuration with `@ConfigurationProperties` and `@Validated`; secrets from the environment; profile- and property-conditional beans with a fallback bean when missing.
- Explicit transaction policy on service operations (`propagation`, `isolation`, `rollbackFor`).
- JPA: UUID IDs, `@Version` optimistic locking, enum strings, equality on ID, protected no-arg constructor plus a factory. Kill N+1 with fetch joins or an entity graph. Dynamic predicates through `Specification`.
- Web: versioned request mapping, `@Valid` bodies, 201 with `Location` on create, a `@ControllerAdvice` mapping not-found to 404 and validation to 400. Stateless JWT security with every endpoint covered.
- Remote calls: circuit breaker plus retry plus time limiter with a fallback that returns a typed failure.
- Concurrency: virtual threads for I/O-bound blocking work, with bounded waits; they are not a CPU speedup. Parallel streams only when the workload justifies them; no side effects in `forEach`.
- Reactive: `Mono` for zero or one, `Flux` for many; keep the chain non-blocking end to end.
- Tests: Mockito without a context for units; `@WebMvcTest` with MockMvc for the web slice; `@SpringBootTest` with Testcontainers for persistence.

### 8.4 Go

- Errors are values. Wrap with operation and context while preserving identity: `fmt.Errorf("get user %d: %w", id, err)`. Define sentinel errors (`ErrNotFound`, `ErrUnauthorized`, `ErrInvalidInput`, `ErrConflict`); inspect with `errors.Is` and `errors.As`; aggregate validation with `errors.Join`. Never discard an error (`user, _ := GetUser(id)`); never panic for a recoverable failure. Panic during initialization is idiomatic.
- `context.Context` is the first parameter. Derive timeouts, always `defer cancel()`, pass the context to every database and client call, and never replace the caller's context with `context.Background()`.
- Accept interfaces, return structs. Keep interfaces small; one-method interfaces take the `-er` suffix. Split a five-method data store into focused interfaces.
- Concurrency: worker pools and fan-in must select on `ctx.Done()`, make channel-closing ownership explicit, and close results only after the `WaitGroup` completes. Use `errgroup.WithContext` to cancel siblings on first error. A send to an unread unbuffered channel leaks the goroutine.
- Configuration through functional options (`NewServer(addr, WithTimeout(5*time.Second))`).
- `sync.Once` for one-time initialization; `sync.Pool` only with reset before reuse. Generic constraints use underlying types (`~int | ~int64 | ~float64`).
- HTTP handlers: decode and validate, set content type and status, map sentinel and deadline errors to 404, 401, 504, map unknown errors to 500 without leaking details; middleware adds a request ID, logs method, path, status and duration, and recovers panics.
- Tests are table-driven with named subtests covering normal, boundary, zero and error cases.
- Make zero values useful; a little copying beats a little dependency; clear beats clever.

### 8.5 Kafka

- Producer: `enable.idempotence=true`, `acks=all`, retries effectively unlimited, at most five in-flight requests per connection, explicit delivery and request timeouts. Always handle the send callback or future. Fire-and-forget sends are forbidden.
- Consumer: auto-commit off, `isolation.level=read_committed` when producers are transactional, commit only after successful processing, deduplicate (by message ID or topic-partition-offset), bounded retries with backoff, then a dead-letter topic. Dead-letter records keep the original key and value and add `original-topic` and `error-message` headers.
- Events are immutable facts. Design for replay. Govern schemas from day one with a registry (Avro or Protobuf).
- Use exactly-once processing only where required; the default is at-least-once delivery with idempotent consumers.
- Ordering exists per partition only. Consumers beyond the partition count sit idle. Adding partitions breaks existing key-to-partition ordering.
- Use transactions to group related records atomically; use the outbox pattern with change data capture when a database write and a publish must agree.
- Monitor consumer lag and partition distribution. Batching, linger and compression trade throughput against latency.

### 8.6 Docker, Kubernetes, Terraform, GitHub Actions

- Everything is versioned code; Git is the source of truth; replace instead of modifying in place; least privilege by default; every deployment can roll back.
- Docker: multi-stage builds, dependency layers cached before source, a slim or distroless runtime image, non-root user, health check. Never `latest` base tags and never dev dependencies in the runtime image.
- Kubernetes: resource requests and limits on every container; distinct liveness, readiness and (where needed) startup probes; `runAsNonRoot`, `allowPrivilegeEscalation: false`, `readOnlyRootFilesystem: true`, `capabilities.drop: [ALL]`; secrets by reference; rolling update with `maxSurge: 1`, `maxUnavailable: 0`; a PodDisruptionBudget; default-deny NetworkPolicy for ingress and egress, then explicit allows; anti-affinity or topology spread for replicas. CPU-based autoscaling can be the wrong signal for a latency-sensitive service.
- Terraform: typed, documented, validated inputs; outputs marked sensitive where needed; pinned provider and tool versions; remote state with encryption and locking; common tags merged in; no hardcoded values.
- GitHub Actions: matrix builds, dependency caching, cancellation of superseded runs, pinned action major versions, OIDC federation in place of stored cloud secrets (`id-token: write`, `contents: read`), deployment from the main branch only.

### 8.7 Naming

| Stack | Rule |
|---|---|
| TypeScript / JavaScript | Functions camelCase and verb-first; types, classes, components PascalCase; constants SCREAMING_SNAKE_CASE; component files PascalCase, utility files kebab-case; tests `*.test.ts` or `*.spec.ts` |
| Java | Classes PascalCase; methods camelCase verb-first; lowercase reverse-domain packages; tests `*Test` and `*IT`; Spring beans camelCase; properties `lowercase.with.dots` |
| Go | MixedCaps, never underscores; exported PascalCase; lowercase single-word packages; files `snake_case.go`; initialisms upper case (`HTTPClient`, `ID`) |
| C# | Public members PascalCase; private camelCase; interfaces prefixed `I`; async methods suffixed `Async` |
| Infrastructure | Terraform snake_case; Kubernetes and Helm resources kebab-case; images lowercase with a version tag; environment variables SCREAMING_SNAKE_CASE |
| Kafka | Consumer groups name their purpose (`order-processor-group`); schemas PascalCase; topic form per section 12, item 3 |

Where sources disagree on naming (interface prefixes, name length, topic form) see section 12.

### 8.8 Python: a sentinel for "argument omitted"

Python work belongs to the `python` skill. One idiom is kept here because the omitted-versus-null question appears at every API boundary. When `None` is a valid value and omission must mean something else, represent omission with an identity-stable sentinel, not with a value from the domain. The pandas form:

```python
class _NoDefault(Enum):
    no_default = ...

no_default: Final = _NoDefault.no_default
NoDefault: TypeAlias = Literal[_NoDefault.no_default]

# at the call site of the public function
if allow_fill is no_default:
    if fill_value is None:
        warnings.warn(..., Pandas4Warning, stacklevel=find_stack_level())
        allow_fill = False
    else:
        allow_fill = fill_value is not no_default
```

- Purpose: tell "argument omitted" from "argument explicitly passed as `None`" during a long deprecation window, warn on omission and derive the value.
- Compare with `is no_default`. Identity, not equality.
- Translate the sentinel before calling lower-level code that does not understand it. Sentinels leak into downstream helpers.
- Avoid it in new APIs, where keyword-only parameters and explicit enums are cleaner.
## 9. ASP.NET Core plus Angular: one behavior across the stack

Use this section when one user-visible behavior crosses a C# back end and an Angular/TypeScript front end. The slice is:

`user action → request → validation and authorization → domain and effects → typed response → owned client state → accessible outcome`

Back-end and front-end types need not mirror each other class for class. They must agree on data, outcomes, effects and recovery at the transport.

### 9.1 Pick a profile

| Profile | Use when | Minimum work |
|---|---|---|
| Primary vertical slice | Back-end behavior or effects and an Angular consumer both change | Outcome contract, parser, transport mapping, one state owner, recovery, cross-layer test, release envelope |
| Back-end boundary | Back end changes, no Angular edits | Identify transport consumers; cancellation; side effects; integration test |
| Front-end consumer | Back-end contract is stable | Parse the deployed payload; state and async model; accessible states; component and browser evidence |
| Contract evolution | Schema, generated client, outcomes or version change with independent consumers | Schema owner; deterministic generation; old/new tests; staged migration; rollback |
| Realtime companion | Server push changes Angular state | Snapshot, order, duplicates, gaps, resync, auth renewal, reconnect and offline semantics |
| Not primary | Pure syntax, CSS, database tuning, Node/MongoDB, infrastructure, security architecture, multi-service operations | Use the narrower guide; attach only the affected contract check |

Stop production work when the stack, the user outcome or its authorization, the schema owner, the current behavior of a volatile API, the cross-boundary test or the supported versions are unknown. An isolated spike is allowed if it names its convergence gate. Re-route when an endpoint becomes public, a write gains a retry, a payload becomes generated, a second component consumes the state, ownership changes or deployments separate.

### 9.2 Order of work

1. **Behavior and authorization.** Name the action, every outcome the user can see, who may do it, what work the user keeps on failure.
2. **Transport before DTO generation.** Fields, stable outcome discriminants, version data, compatibility. Characterize deployed behavior first. Freeze outcome semantics before generating anything.
3. **Back-end outcomes and cancellation.** Expected domain failures are data; unexpected infrastructure faults stay faults and go to telemetry. Map outcomes to HTTP once, at the transport. Propagate the `CancellationToken` into every database and outbound call.
4. **Effects.** Decide duplicate policy (ignore, join, idempotent processing) and concurrency policy (a version check where a real invariant exists).
5. **Reproducible generation.** Regenerate clients only with an owned generator, frozen input, command and version; review the diff; never hand-edit generated output.
6. **Runtime parsing.** Parse payloads that are external, independently produced, cached or proxied. Static declarations alone are enough only under documented atomic same-build deployment.
7. **One Angular state owner** per remote resource, exposing read-only derived state.
8. **Accessible states.** Idle, submitting, success, each rejection, cancelled, retryable; keyboard operation, focus placement, status announcement, retained input.
9. **Layer tests, then one cross-layer test** including a negative browser path.
10. **Compatibility and rollback.** Supported version orderings, telemetry by contract version, rollback trigger.

### 9.3 Rules

**Back end**

- Use the project's existing endpoint style (controllers or Minimal APIs). Add shared filters or base policy only when repeated behavior needs an owner.
- Keep the transport thin. The server owns authorization, invariants and effects; the client mirrors only stable, helpful checks.
- Use explicit outcomes when validation, not-found, conflict, forbidden or duplicate change what the transport or UI does. Do not wrap infallible local code in a result type.
- A closed outcome hierarchy for an update could be `Accepted(dto, version)`, `ValidationRejected(fieldErrors)`, `Forbidden`, `Missing`, `Conflict(current, version)`, `Unavailable(effectKnownAbsent)`.
- Direct EF Core access is fine for one store-specific use case. Add a repository or service when there are multiple stores, an external dependency, a transaction policy or a query that varies independently. A repository that only renames `DbSet` methods is harmful; direct access is harmful when policy, isolation or test needs go unmet. See section 12, item 4 for the stricter layering position.
- Complex query criteria, includes, ordering and paging can live in a specification object evaluated in one place.
- Read paths: `AsNoTracking()`, project to the DTO in the query, page with a total count, eager-load to avoid N+1. Bulk deletes use a set-based `ExecuteDeleteAsync`.
- Caches are scoped by security context and version, invalidated deterministically on write, and covered by a stale-read test.
- C# language features (primary constructors, collection expressions, `required` and `init` members, records) depend on the project's language version, analyzers and serializer. Read the configuration and test binding and serialization before adopting them.

**Front end**

- Signals for owned synchronous state: a private writable signal, `asReadonly()` exposure, `computed` for derived values, `effect` for side effects such as persistence. Update immutably with `update` or `set`; mutating the array inside a signal does not notify.
- RxJS for temporal, multi-value and cancellable work. Operator choice is a concurrency policy: `switchMap` for latest-wins (search), `exhaustMap` to ignore overlapping submits, `concatMap` for ordered bounded commands, `mergeMap` for independent bounded reads.
- One async model per public API. If a service returns an `Observable`, components subscribe with teardown (`async` pipe, `takeUntilDestroyed`) or adapt once to a Promise in one named, tested place. Never `await` a stream; never use a Promise test double for an Observable service.
- Model view state as a discriminated union (for an editor: `editing | saved | conflict | retryable`) so the draft survives conflict and unavailability. Independent booleans can represent impossible states.
- A failure is not an empty success. `catchError(() => of([]))` is allowed only where the product explicitly treats failure as optional absence.
- Feature-local state is the default. Introduce a global store only for observed cross-view coordination, invalidation or navigation recovery.
- Lists: track by a stable identity in `@for`; OnPush change detection; virtual scrolling for long lists, justified by a local measurement.
- Bind every subscription and effect to a lifetime; keep browser-only effects out of server rendering.

**Contract**

- A TypeScript parser accepts `unknown`, checks record shape, discriminant and field types, returns `{ ok: true, value } | { ok: false, reason }`, and maps unsupported or malformed variants to a protocol failure. `payload as UpdateProfileResult` is not validation.
- Co-deploy a breaking contract change only when atomic deployment is enforced. Otherwise evolve additively with tolerant readers, explicit versions and a retirement point; test each supported ordering of old and new.
- Realtime (for example SignalR): automatic reconnect restores the connection, not the missed messages. Token source, renewal, ordering and resync are design decisions.

### 9.4 Reliability stance

Distinguish an invariant (a stale version never silently overwrites), a measured objective (a project-owned distribution) and a recovery objective (tolerable interruption, data loss or manual work). This skill supplies the categories, never universal percentages, latencies or recovery times. Fail closed for authorization, tenancy and invariants; optional features may degrade. The working invariant for an edit flow: a stale update produces no write, a conflict outcome, a retained draft and a tested accessible way to reconcile.
## 10. Extracting idioms from reference codebases

Use this when asked to build or extend an idiom archive from high-quality repositories. The method was written for Rust (text dumps of anyhow, axum, bevy, clippy, embassy, embedded-hal, heapless, hyper, quote, rayon, RTIC, serde, syn, thiserror, tokio, tonic and tower) and transfers to any language by renaming the layers. It is a method; its output is only as good as the code it is run on, and nothing it produces is a verified idiom until the snippet compiles.

### 10.1 Layers

| Layer | Rust meaning | What to look for | Equivalent elsewhere |
|---|---|---|---|
| L1 core | Language features independent of an OS (`no_std`) | Ownership and borrowing, lifetimes, trait usage, generics, `Result`/`Option` | Language primitives and type system |
| L2 standard library | Patterns using `std` | Collections, iterators, concurrency primitives, API design, module organization | Runtime built-ins |
| L3 ecosystem | Framework and library patterns | Async/await, web framework idioms, embedded patterns, macros, testing strategies | Third-party packages and frameworks |

Classify every idiom by stack and layer. Prefer a lower layer unless the higher one supplies needed function.

### 10.2 Two roles, three pillars

- **Discovery agent**: researches and extracts (prompts 1, 2, 3 and 5).
- **Implementation agent**: writes code constrained by the archive (prompt 4).
- **Pillar I, extraction and curation**: triage a repository, then deep-dive its hotspots; whole repositories exceed context limits, so never skip triage.
- **Pillar II, application**: retrieve relevant idioms and inject them as constraints into a test-first implementation prompt.
- **Pillar III, evolution**: after a compiler error, failed test, lint warning or needless complexity in your own work, run a retrospective and add what was learned to the archive.

### 10.3 Broad extraction prompt

Use this when the whole set of repositories is available and you want a first sweep.

```text
# CONTEXT
You are a Senior Rust Language Analyst specializing in identifying idiomatic patterns and
anti-patterns. I have downloaded these high-quality Rust repositories:
- {{REPOSITORY_LIST}}

# MISSION
Analyze these codebases to extract comprehensive idiomatic patterns organized by Rust's
architectural layers (L1-core, L2-std, L3-ecosystem).

# ANALYSIS FRAMEWORK
L1 (Core/no_std): ownership/borrowing, lifetime management, trait system usage,
  generic programming, error handling (Result/Option)
L2 (Standard Library): collections, iterators, concurrency primitives, API design,
  module organization
L3 (Ecosystem): async/await, web framework idioms, embedded patterns, macro usage,
  testing strategies

# EXTRACTION INSTRUCTIONS
For each repository, identify:
1. IDIOMATIC PATTERNS: Pattern Name; Layer (L1/L2/L3); Code Example (3-5 lines);
   Context (when / when not to use); Benefits (safety, performance, readability);
   Source File
2. ANTI-PATTERNS: Problem; Common Mistake; Idiomatic Alternative; Rationale
3. ARCHITECTURAL PATTERNS: Project Structure (module organization); Error Handling
   Strategy (library vs application); Testing Approach (unit vs integration);
   Dependency Management (crate usage)

# OUTPUT FORMAT
## [Repository Name] - [Pattern Category]
### Pattern: [Name]
**Layer:** L1/L2/L3
**Context:** [When this pattern applies]
**Example:** [fenced code snippet]
**Benefits:** [Compile-time safety, performance, etc.]
**Source:** [File path or module]
### Anti-Pattern: [Name]
**Problem:** [What to avoid]
**Better Approach:** [fenced improved code]
**Rationale:** [Why this is better]

# SPECIFIC ANALYSIS FOCUS AREAS
1. Error Handling: compare anyhow vs thiserror usage
2. Async Patterns: Tokio vs embassy approaches
3. API Design: serde's trait system vs axum's extractors
4. Memory Management: heapless vs std collections
5. Testing Strategies: property-based vs unit test patterns

# QUALITY CRITERIA
Focus on patterns that improve compile-time safety, reduce runtime errors, enhance
performance, increase readability, and are widely used across multiple repositories.
Provide at least 3-5 high-quality patterns per repository, prioritizing those that
appear consistently across multiple codebases.
```

Follow with three passes, in this order:

```text
[Cross-repository correlation]
Now analyze the patterns you extracted and identify:
1. Universal Patterns: idioms that appear in 3+ repositories
2. Context-Specific Patterns: unique to certain domains (async, embedded, web)
3. Evolution Patterns: how idioms differ between established vs newer crates
4. Contradictory Patterns: cases where different repos use conflicting approaches
Create a matrix showing pattern prevalence across repositories.
```

```text
[Compile-time safety]
Focus specifically on patterns that enable compile-time bug prevention:
1. Type System Patterns: newtype, phantom types, zero-sized types
2. Ownership Patterns: borrow checker-friendly APIs
3. Trait Bound Patterns: generic constraints that prevent misuse
4. API Design Patterns: compile-time enforced invariants
For each, explain how it catches errors during compilation rather than runtime.
```

```text
[Anti-pattern identification]
Analyze common mistakes and their idiomatic corrections:
1. Fighting the Borrow Checker: cloning vs borrowing solutions
2. Error Handling Anti-Patterns: unwrap abuse vs proper propagation
3. Async Misuse: blocking in async contexts
4. Unsafe Misuse: when unsafe is unnecessary
Provide before/after examples showing the transformation from problematic to idiomatic code.
```

Order of use: broad extraction, then correlation (universal versus context-specific), then compile-time safety, then anti-patterns to build the "what to avoid" half.

### 10.4 Staged prompts for large repositories

**Prompt 1, codebase triage.** Feed the full or truncated text dump of one repository.

```text
# ROLE
You are an expert Rust code analyst (The Discovery Agent).
# OBJECTIVE
Perform an initial triage of the ingested codebase: {{REPOSITORY_NAME}}.
# INPUT
<CODEBASE_TEXT>
[Ingested text; directory structure and Cargo.toml must be visible]
</CODEBASE_TEXT>
# INSTRUCTIONS
1. Layer Classification: based on dependencies (Cargo.toml) and usage of `std` vs `no_std`,
   classify this codebase primarily as L1, L2, or L3. Explain your reasoning.
2. Architectural Overview: describe the high-level architecture and the purpose of the
   key modules.
3. Idiom Hotspots: identify the 3-5 most critical files or modules where advanced or
   interesting idiomatic patterns relevant to its primary domain are most likely. These
   will be used for deep-dive analysis.
```

**Prompt 2, forensic idiom extraction.** Run on each hotspot file. Insert exactly one focus block and the full schema from section 11.5.

```text
# ROLE
You are a Forensic Rust Code Analyst (The Discovery Agent).
# OBJECTIVE
Analyze the provided code from {{REPOSITORY_NAME}} and extract idiomatic patterns
according to the Standardized Idiom Schema (SIS).
# CONTEXT
Codebase Domain: {{DOMAIN}} (e.g., Async Runtime, Serialization Framework)
# ANALYSIS FOCUS
[ONE FOCUS BLOCK]
# INPUT
<CODE_SNIPPET>
[Target file identified in triage]
</CODE_SNIPPET>
# INSTRUCTIONS
1. Analyze the code for unique uses of traits, ownership management, safety invariants,
   or performance optimizations within the Analysis Focus areas.
2. Hypothesize the Rationale: why did the author choose this approach? How does it
   contribute to compile-first success, safety, or efficiency?
3. Document each distinct, high-quality pattern strictly according to the SIS JSON format.
# SIS FORMAT
[FULL SIS JSON STRUCTURE]
# OUTPUT FORMAT
A list of JSON objects adhering to the SIS.
```

Focus blocks:

```text
--- [L1 Focus: no-std/Core] ---   (e.g. heapless, embassy, RTIC)
Focus on how the code achieves its goals WITHOUT `std`.
1. Memory Management: static allocation, stack-based collections, fixed buffers, or
   careful use of `core::alloc`.
2. Error Handling: efficient enum usage, `Result` propagation without `Box<dyn Error>`.
3. Hardware Interaction and Concurrency: synchronization (critical sections, atomics) and
   hardware abstraction (traits) without an OS.
4. Type-State Programming: using the type system to enforce correct sequences of
   operations at compile time.

--- [L2 Focus: Standard Library] ---   (e.g. rayon, clap, regex)
Focus on the effective and ergonomic use of the standard library.
1. Ownership Mastery: smart pointers (Arc, Box, Rc), interior mutability (Mutex, RefCell),
   minimizing allocations and clones.
2. Iterators and Collections: efficient, functional use of iterators and closures over
   manual loops.
3. Concurrency Primitives: idiomatic `std::sync` (channels, Mutexes) or data parallelism.
4. API Design: Builder, Newtype, RAII, and common traits (Deref, AsRef, From/Into).

--- [L3 Focus: Ecosystem/Frameworks] ---   (e.g. tokio, axum, serde)
Focus on patterns specific to the architecture of major frameworks and runtimes.
1. Asynchronous Patterns: task management, async synchronization, streams, `Send`/`Sync`
   safety, avoiding executor blocking.
2. Framework Architecture: core patterns (Middleware/Service, data model).
3. Macros and Metaprogramming: procedural or declarative macros for ergonomics.
4. Advanced Trait Systems: complex trait use for abstraction and extensibility.
```

**Prompt 3, architectural template synthesis.** Provide the directory listing, manifest and entry-point files.

```text
# ROLE
You are a Chief Software Architect specializing in Rust (The Discovery Agent).
# OBJECTIVE
Analyze the provided codebase structure from {{REPOSITORY_NAME}} and synthesize an
idiomatic architectural template.
# DOMAIN FOCUS
{{DOMAIN_TYPE}} (e.g., Network Service (L3), Embedded Firmware (L1), CLI Utility (L2))
# INPUT
<CODEBASE_STRUCTURE>
[Directory listing, Cargo.toml, main.rs / lib.rs]
</CODEBASE_STRUCTURE>
# ANALYSIS REQUIREMENTS
1. Module Structure & Hierarchy: `src/` organization, workspace usage, and visibility.
2. Data Flow & State Management: how is state shared (e.g., Arc<Mutex<T>>, channels)?
3. Concurrency Model: async tasks, thread pools, message passing?
4. Error Handling Strategy: overall approach to definition and propagation.
# OUTPUT FORMAT
A detailed report including Overview, Core Components, a component interaction diagram
(MermaidJS syntax), and a high-level code skeleton illustrating the template.
```

**Prompt 4, constraint-guided implementation.** Retrieve idioms from the archive (by hand or by retrieval) and inject them as numbered constraints.

```text
# ROLE
You are a Senior Rust Developer (The Implementation Agent).
# OBJECTIVE
Implement the specified component using a Test-Driven Development approach, strictly
adhering to the Idiomatic Guidelines.
# REQUIREMENT
[Component requirement, e.g. "Implement the User Authentication service"]
# IDIOMATIC GUIDELINES (Constraints)
1. RUST-L2-ITERATOR-COMBINATORS: Prefer iterators (`map`, `filter`) over manual `for` loops.
2. RUST-L3-ASYNC-MUTEX: Use `tokio::sync::Mutex` in async code, NOT `std::sync::Mutex`.
   Rationale: avoid blocking the executor.
3. RUST-L2-ERROR-THISERROR: Use `thiserror` for defining custom error enums in libraries.
# INSTRUCTIONS
1. TDD Red Phase (Tests First): generate a comprehensive suite of unit tests
   (`#[cfg(test)] mod tests { ... }`) covering happy paths, edge cases, and error
   conditions. The implementation should initially be `unimplemented!()`.
2. TDD Green Phase (Implementation): implement the code required to make the tests pass.
3. Rigorously follow the Idiomatic Guidelines provided.
# OUTPUT FORMAT
The complete Rust module, including the tests and the implementation.
```

**Prompt 5, retrospective analysis and idiom discovery.**

```text
# ROLE
You are a Rust Code Reviewer and Mentor (The Discovery Agent).
# OBJECTIVE
Analyze an implementation attempt from our own work, identify issues, and extract new
idiomatic patterns.
# INPUT CODE
[Code generated by a model or written by a developer]
# SITUATION REPORT
[Compiler error message, failed test output, lint warning, or general complexity]
# ANALYSIS TASKS
1. Identify the root cause of the issue.
2. Determine if the issue stems from non-idiomatic implementation (e.g., fighting the
   borrow checker, excessive cloning).
3. Propose a refactored, idiomatic solution.
4. Extract New Insights: if this revealed a new pattern or anti-pattern, document it
   according to the SIS.
# OUTPUT FORMAT
1. Root Cause Analysis.
2. Refactored Solution (Code).
3. New Idiom Discovery (JSON object in SIS format, if any).
```

To use the prompts for another language, replace the role's language, the manifest name, the layer definitions and the ID prefix, and keep everything else.

### 10.5 Admission rules for the archive

- A record is admitted only with every schema field present. A record with no anti-pattern or no provenance is an unreviewable snippet.
- The snippet is minimal and verified: it compiles in the target toolchain. Ten lines is good; a hundred lines defeats review.
- "Universal" means observed in three or more repositories. One codebase proves what that codebase did, not ecosystem consensus.
- Record contradictory patterns as contradictions with the context that selects each; do not pick a winner silently.
- Provenance must resolve to something readable (file in the ingested dump, or a retrieved URL with date). An unretrieved URL is candidate provenance only.
- After each task that used an archive entry, record whether it shipped, was adapted or was rejected, and why.

### 10.6 Feeding code to a model under a budget

Hotspots given to the forensic prompt, and code handed to a sub-agent, must fit a token or line budget without losing their structural anchors. Use outline-aware excerpt assembly, the pattern Zed uses to build edit-prediction context (`assemble_excerpt_ranges(buffer, input_ranges: Vec<(Range<Point>, usize)>)`):

1. Clip each target range to whole lines and merge overlapping ranges.
2. Collect the outline items (functions, types, modules) that contain each target, and add their header and tail ranges, not their full bodies, carrying the target's order value.
3. Extend the list with those outline ranges, merge again, and return the ranges in deterministic order.

Rules: expand context with structure-aware ranges and prefer that to arbitrary line padding. If the outline is wrong or missing (it depends on parser or language-server accuracy), the fallback must still include the direct input range. Do not use excerpts for an exact refactor, where an omitted body could hide a required dependency; send the full bodies.
## 11. Templates

### 11.1 Design decision worksheet (file it as the decision record)

```text
Reader, starting state, decision, moment of use:
Mode: estimator | designer | reviewer | explainer

ESTIMATE
  Inputs and assumptions (users, actions, sizes, ratios):
  Average / peak QPS:            Storage (daily, total):
  Cache size:                    Servers:            Bandwidth:
POSITION (one business fact per axis that matters)
  Consistency vs availability:
  Latency vs consistency:
  Latency vs throughput:
  Monolith vs services:
  Read vs write optimization:
  Push vs pull:
SELECT
  Pattern:
    Use when (and the fact that satisfies it):
    Avoid when (and why it does not apply):
    Anti-pattern to screen for:
  Boundary options considered and rejected alternatives (with reason):
  Dependencies touched and blast radius if this fails:
  Decision: adopt | adapt | avoid | escalate          Cost of being wrong:
VERIFY
  Gate (command, metric + threshold, checklist item or review question):
  Failure path bound (timeout / retry cap / idempotency / compensation / dead letter / ack):
  Evidence role of each claim (project observation, catalogue fact, refreshed fact,
    inference, illustration, measurement) and dates of product numbers:
  Uncertainty:
  Migration sequence and envelope successor:
  Rollback or escalation, and the signal that triggers it:
  Reopen this decision when:
```

For a diagnosis instead of a new design, prepend: symptoms, hypotheses, probes run and their results.

### 11.2 Decision ledger (one entry per choice inside a slice)

```text
Behavior held constant:
Project evidence and mandatory policy:
Selected option and responsibility owned:
Simpler candidate rejected because:
Focused gate and observed result:
Known uncertainty or untested combination:
Owner, rollout impact, and rollback trigger:
Reopen this decision when:
```

### 11.3 Cross-stack behavior ledger

Link the authoritative schema, client, decision record and tests; do not duplicate them. One block per behavior, one row per outcome.

```text
Behavior identity (stable name):
User promise and retained work:
Links: schema | generator config | parser | state owner
Owners: back end | front end | schema | generation | telemetry | rollback
Deployment atomicity: atomic same-build | independent
Conditional concerns (mark "not applicable: <reason>" or give owner and date):
  concurrency | duplicates | cancellation | retry | realtime | offline | migration
Project revision, last gate run, assumptions not refreshed:

| Outcome | Server precondition and effect | Transport discriminant | Parser result | Client state and recovery | Proof (back end / consumer) | Retry, duplicate, cancel policy | Rollout and operational evidence |
|---|---|---|---|---|---|---|---|
| accepted | one authorized commit, new version | | | | | | |
| validation rejected | no write, field errors | | | draft retained | | never retry | |
| forbidden | no write, safe disclosure | | | | | never retry | |
| missing | no write; not an empty success | | | | | refresh, do not retry | |
| conflict | no silent overwrite | | | draft kept separate from current | | reconcile | |
| unavailable | effect known absent or unknown | | | retryable | | bounded retry or reconcile | |
| malformed | adapter failure | | protocol failure | no partially trusted render | | never retry | |
| cancelled | honest effect semantics | | | late results ignored | | | |
```

A row that says only "error → show message" is invalid. Include the conflict row only when a real version invariant exists. Refresh the ledger whenever schema, generator, parser, state owner, outcomes, deployment or rollback change.

### 11.4 Claim extraction record (for reusing older or external guidance)

```text
Source and heading:
Exact observation (in historical tense, with version and date):
Role: candidate | supporting | project policy | legacy | conflicting | negative | duplicate
Target boundary and user consequence:
Project evidence inspected:
Executable gate and result:
Unresolved currency or applicability:
Disposition: promote | adapt | retain as warning | reject
Owner and refresh trigger:
```

Promote only after target fit and an executable gate. Demote on a counterexample. Keep negative evidence while the mistake stays plausible.

### 11.5 Idiom record

Standardized Idiom Schema, for machine-readable archives and retrieval:

```json
{
  "id": "RUST-L[1|2|3]-[DOMAIN]-[PATTERN_NAME]",
  "layer": "L1 (Core/no_std) | L2 (Std) | L3 (Ecosystem)",
  "name": "Descriptive Pattern Name (e.g., Typestate Programming, Scoped Threads)",
  "domain_keywords": ["Error Handling", "Concurrency", "Memory Management"],
  "context_problem": "What specific problem does this solve? In what context is it applicable?",
  "solution_snippet": "A minimal, verified, compilable code example.",
  "rationale": "Why is this superior? (Safety, Efficiency, Maintainability, Compile-First Success)",
  "anti_patterns": {
    "description": "What should be avoided?",
    "example": "A brief counter-example."
  },
  "relevant_crates": [],
  "provenance": "Where was this discovered? (file name from ingested data, URL)"
}
```

`relevant_crates` is filled for L3 records (for example `["Tokio", "Serde"]`). For other languages replace the ID prefix with the stack key (`TS`, `JAVA`, `GO`, `CS`, `NG`, `KAFKA`, `INFRA`) and `relevant_crates` with the packages involved.

The same content as a prose card has eight fields: pattern name; stack and layer; context or problem; minimal verified snippet; rationale; anti-pattern; relevant packages; provenance. A card also states the user's goal, the decision boundary and the verification command or question when it is used in an answer.
## 12. Where the source material disagrees

Both positions are kept. The selector says which applies.

1. **Name length.** One position: every function, method and class gets a four-word name in the form entity-purpose-type-qualifier or verb-constraint-target-qualifier (`UserAccountRepositoryAsync`, `CreateOrderWithValidation`, `UserProfileCardComponent`), and short names like `UserRepo` or `GetUser()` are underspecified. The other: use project casing and the shortest unambiguous domain name; word counting obscures domain clarity. *Selector:* follow four-word naming where repository policy or an analyzer requires it; otherwise shortest unambiguous. Never mix both in one module.
2. **TypeScript interface prefix.** One catalogue writes `IDatabase`; the other says interfaces carry no `I` prefix. *Selector:* the existing repository convention; without one, no prefix in TypeScript and Java. C# interfaces always take `I`.
3. **Kafka topic names.** `com.company.domain.event` (reverse-domain, dot-separated) versus `orders.created.v1` (domain, event, version). *Selector:* the existing cluster convention; choose the versioned form when the schema version must be visible in the topic name.
4. **.NET layering.** Strict `controller → service → repository → EF Core`, with direct `DbContext` access from controllers forbidden and build-failing, versus thin transport with a repository or service added only for real policy, variation, isolation, transaction or test need. *Selector:* an existing architecture rule or dependency check enforces the strict form; without one, apply the need test in section 9.3. The strict position names Parseltongue as the dependency-graph tool that verifies it, for the back-end graph and for the front-end graph (pages → features → UI components → primitives; features → services → HttpClient; pages → primitives and UI components → services forbidden). Its two specifications: WHEN a controller imports EF Core directly THEN the build SHALL fail AND the architectural violation SHALL be reported; WHEN the codebase is analysed with Parseltongue THEN forbidden dependencies SHALL be detected AND the report SHALL list violations with suggested fixes. If the project adopts the strict form, wire both: a build-failing rule and a graph query whose empty result is the pass condition (the dependency-graph workflow is in `codebase-navigation`).
5. **Angular async.** An older component example awaits a service call while the service is written with `Observable`. The later review classifies that mix as a defect. *Selector:* what the service actually returns. Keep one model or adapt once.
6. **Generated DTOs.** "Generating TypeScript types from C# prevents shape drift" versus "generated types do not parse JSON and give no confidence about deployed payloads". *Selector:* atomic same-build deployment lets generation stand alone; independent consumers, proxies, caches or old clients require runtime parsing and compatibility tests as well.
7. **Realtime reconnect.** "Lost connections reconnect and resume messages" versus "reconnect does not prove replay, order, deduplication or auth renewal". *Selector:* resumption is true only if the protocol you built replays; otherwise treat reconnect as a fresh subscription needing resync.
8. **Retry numbers.** Basic helper: `baseDelayMs × 2^attempt`, no jitter, no predicate. Defensive helper: 3 attempts, base 1,000 ms, cap 30,000 ms, up to 10 percent jitter, `shouldRetry` for network and 5xx. System-design form: 5 attempts, full jitter, cap 60 s. Kafka consumer form: 3 fixed 1 s backoffs, then dead letter. And the later review: do not copy universal counts at all. *Selector:* never the basic helper for remote calls; otherwise derive from the dependency, starting from the form that matches its kind. Do not blend variants.
9. **Canary weight.** "Commonly 1 to 5 percent" versus a 10 percent example versus stepped 20 percent then 40 percent with pauses. *Selector:* traffic volume needed for a statistically useful signal and tolerable blast radius.
10. **Kubernetes probe and limit examples.** `/health` after 30 s every 10 s with a 256 Mi limit, versus `/healthz` with 15 s initial delay, 20 s period, 5 s timeout, 3 failures and a 512 Mi limit, versus liveness at 15 s initial and 10 s period. *Selector:* the application's real endpoints, start-up time and measured memory.
11. **Coverage.** "Business-logic coverage above 80 percent" as a checklist gate versus "80 percent is a starting point, not a retroactive merge blocker for legacy code". *Selector:* enforce on new and changed code; ratchet on legacy.
12. **Front-end performance figures.** An older reference states that 10,000 DOM nodes take about 3 seconds to render and virtual scrolling cuts this to about 20 nodes and 50 ms, with a 60 fps target. The later review finds no harness behind those figures. *Selector:* treat them as an illustration of direction; measure locally before quoting any number.
13. **L2 cache latency.** 7 ns in one guide, about 4 ns in another. *Selector:* neither matters for design; use the order of magnitude.

Also note three scoped rules that look like disagreements but are not: panic is wrong for recoverable Go errors but idiomatic at initialization; a boolean parameter is acceptable when the choice is genuinely binary; anemic DTOs are correct at serialization boundaries.
## 13. Output contract

An answer produced with this skill contains, in this order:

1. **Mode and decision**: one line naming the mode, the reader and the decision.
2. **Estimates and assumptions** (designer, estimator, reviewer modes), with arithmetic shown.
3. **Recommendation**: each pattern with its use-when fact, avoid-when check and screened anti-pattern; Adopt, Adapt, Avoid or Escalate; rejected alternatives.
4. **Failure path**: the bound for each effect.
5. **Per-stack form**: code or configuration in each affected stack's idiom, with the section key from reference.md when a catalogue idiom is borrowed (for example TS.7, J.3, G.1, K.2, D.3).
6. **Gates**: exact commands or review questions, and for those already run, the evidence packet: working directory, candidate identity (commit or build), exact command, selected projects, result summary, what the result does and does not cover. "All tests passed" alone is insufficient.
7. **Evidence labels and uncertainty**: which statements are project observations, catalogue facts, refreshed facts, inferences, illustrations or measurements; which product numbers are undated.
8. **Reversal**: rollback or escalation path, the triggering signal, and when to reopen.

For a .NET/Angular slice add the behavior ledger. For an extraction task the output is a list of idiom records plus the prevalence matrix. For a review, each finding names the violated condition, the consequence, the smallest repair and the gate that would have caught it.

Completion states: **Ready** (all applicable gates pass), **Conditional handoff** (named unresolved items with owner and consequence), **Repair required** (a gate fails), **Orientation complete** (explanation only, nothing verified). Mark each checklist item PASS, FAIL, NOT APPLICABLE with a causal reason, or UNRESOLVED with owner and consequence. A status with no observation behind it is not evidence.
## 14. Quality gates

Discover what exists before naming a gate. Do not claim a gate the project does not have.

### 14.1 Discovery

```bash
# .NET + Angular workspace
rg --files -g '*.sln' -g '*.slnx' -g '*.csproj' -g 'global.json' \
  -g 'Directory.Build.*' -g 'package.json' -g 'angular.json' \
  -g 'tsconfig*.json' -g 'playwright.config.*' -g '*openapi*' -g '*swagger*'

# Other stacks
rg --files -g 'go.mod' -g 'pom.xml' -g 'build.gradle*' -g 'Dockerfile*' -g '*.tf' \
  -g 'Chart.yaml' -g 'kustomization.yaml' -g '.golangci.*' -g 'vitest.config.*' \
  -g '.github/workflows/*.yml'
```

### 14.2 Per-stack gates

```bash
# TypeScript
npx tsc --noEmit && npx eslint . && npx vitest run --coverage

# Java / Spring (pick the project's build tool)
./gradlew check            # or: ./mvnw verify   (JUnit 5, Testcontainers)

# Go
go vet ./... && golangci-lint run --timeout 5m && go test -race -coverprofile=coverage.out ./...

# C# / ASP.NET Core
dotnet build && dotnet test

# Angular (use the scripts defined in package.json / angular.json)
npx ng build && npx ng test --watch=false && npx playwright test

# Terraform
terraform fmt -check && terraform validate && terraform plan

# Kubernetes manifests
kubectl apply --dry-run=server -f k8s/

# Container image
docker build -t candidate:local .
```

Kafka has no single command: the gates are consumer lag, partition distribution, a test that a malformed event yields exactly one dead-letter record, and a duplicate-delivery test asserting one effect.

Gate limits to state with results: a build says nothing about authorization, persistence or transport; a mocked service says nothing about real routing, binding or serialization; clean generation says nothing about deployed payloads or old clients; static TypeScript is not runtime trust; a unit double is not the server; one browser path needs lower-layer breadth behind it. Stop downstream testing on an unexplained generated diff or a failed contract test.

### 14.3 Resilience and contract gates

```bash
# Consumer-driven contract check before deploy
pact-broker can-i-deploy --pacticipant <service> --version <git-sha> --to-environment production
```

- Circuit breaker: a test that drives CLOSED → OPEN → HALF-OPEN → CLOSED.
- Timeouts: an injected-delay test proving the inner timeout fires before the outer one.
- Retry: a lost-response-after-commit test asserting one effect.
- Chaos: a network-partition, resource-stress or pod-kill experiment run against a written steady-state hypothesis.
- Probes: liveness, readiness and startup endpoints respond as the manifest expects.
- Layering, when the strict .NET/Angular rule is adopted (section 12, item 4): a build that fails when a controller imports EF Core, and a dependency-graph analysis that lists every forbidden edge with a suggested fix. No forbidden edge is the pass condition.

### 14.4 Load and latency

```javascript
// k6 staged profile: adapt targets to the estimate, keep the shape
export const options = {
  stages: [
    { duration: '1m', target: 50 },   // ramp
    { duration: '5m', target: 50 },   // steady
    { duration: '1m', target: 100 },  // spike
    { duration: '2m', target: 100 },  // sustain
    { duration: '1m', target: 0 },    // ramp down
  ],
  thresholds: { http_req_duration: ['p(99)<500'], errors: ['rate<0.01'] },
};
```

```promql
# error ratio
sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))
# P99 latency
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))
# fast-burn page at a 99.9% SLO
error_rate > (14.4 * 0.001)
```

The thresholds above are examples from an order-service contract; replace them with the owner's target. Record the measurement packet: decision, baseline and candidate revisions, workload and outcome mix, environment, cold or warm, exact command, units, population and statistics, guardrails (correctness, duplicates, retries, accessibility, memory, cost), uncertainty. If noise overlaps the difference, report inconclusive and prefer the simpler, reversible option.

### 14.5 Pre-commit checklist

- Types: no implicit `any`; null safety; exhaustive matching on unions and sealed types.
- Errors: no silent failures; domain-specific error types; global handler or error boundary.
- Tests: unit tests for business logic; API integration tests; performance test on critical paths.
- Security: every input boundary validated; authentication and authorization before business operations; no hardcoded secrets; parameterized queries; output encoding; restricted CORS; rate limits; dependency scanning.
- Performance: indexes for common queries; connection pools configured; read-heavy data cached; lists paginated; async I/O.
- Observability: structured logs with correlation IDs; metrics; health and readiness endpoints; tracing where applicable.
- Infrastructure: resource limits; liveness and readiness probes; graceful shutdown; retry and circuit breaker on external calls.
## 15. Anti-patterns

**Architecture**

- Distributed monolith: services that must deploy together.
- Shared tables across services with no end date.
- Synchronous everything: long call chains with no async decoupling.
- Big-bang migration; a strangler migration never finished.
- Microservices, CQRS or event sourcing adopted before the problem that needs them exists.
- Pure push fan-out with celebrity-scale followers.
- Pattern chosen before the problem shape is proven; technology chosen because a larger company uses it.
- Building for maximum scale with no demand.

**Omissions to screen for mechanically**

- No TTL on a cache; no stampede protection.
- No jitter, no cap, no budget on a retry; retry without idempotency.
- No compensation in a saga; no conflict resolution in multi-writer replication.
- No snapshots in an event-sourced aggregate.
- Reading a replica immediately after writing the leader.
- No backpressure on a queue or stream.
- No distinction between liveness and readiness.
- N+1 queries.
- High-cardinality metric labels.

**Code, across stacks**

- Ignored errors (Go `_`), swallowed exceptions, catch-to-empty.
- `any`, unvalidated casts (`json as User`), boolean state flags, primitive IDs.
- Field injection, service locators, hard-instantiated dependencies.
- Mutable setter POJOs; `Optional` parameters or fields; unchecked `.get()`.
- God services; anemic domain models (except DTOs at serialization boundaries).
- Temporal coupling: APIs that only work when called in a hidden order.
- Leaky abstractions: persistence annotations or query details in domain interfaces.
- Boolean parameters where named options are clearer.
- Shotgun surgery: one field change touching ten unrelated files.
- Tests that assert private internals.
- Fire-and-forget Kafka sends; auto-commit with non-idempotent consumers.
- Replacing a caller's context or dropping a cancellation token.
- Goroutine leaks on unread channels.
- `latest` image tags; root containers; hardcoded secrets or infrastructure values.

**.NET and Angular slice**

- Collapsing validation, absence, conflict, forbidden and cancelled into a generic error.
- Treating generated interfaces as runtime validation.
- Mixing Promise and Observable for one operation.
- Two owners for one remote resource; independent loading and error booleans.
- Mutating a signal's value in place.
- Subscriptions or effects with no lifetime.
- Async states that keyboard or assistive-technology users cannot perceive or recover from.
- Reconnect treated as delivery.
- Cache keys that ignore user or version scope.
- Confidence from mocks only, with no real boundary test.
- Forwarding layers that add no policy.
- A performance target with no workload behind it.
- Ignoring the order in which old and new clients and servers are deployed.

**Guidance itself**

- Stripping conditions from a pattern.
- Hardening a catalogue claim into "per Netflix" or "per the book".
- Presenting archived product numbers as live limits.
- Blending two variants of a helper into one that neither source wrote.
- Answering one stack's question from another stack's idioms.
- Citing an unretrieved URL.
- Advice with no gate.
## 16. Bundled scripts

This skill bundles no scripts or assets. All commands are inline in section 14 and use the project's own toolchain.
## 17. Closing self-check

Before delivering, confirm each line or mark it not applicable with a reason:

- [ ] The mode, reader and decision are named.
- [ ] Estimates precede pattern choices, with assumptions written down.
- [ ] Every axis position cites a business fact.
- [ ] Every recommended pattern carries use-when, avoid-when and anti-pattern, and none lost its conditions.
- [ ] At least one rejected alternative is recorded.
- [ ] Each decision is Adopt, Adapt, Avoid or Escalate, with the cost of being wrong.
- [ ] Every effect has a bound; every retry has an idempotence story and a stop condition.
- [ ] Idioms are in each stack's own form; no syntax was transplanted; variants were not blended.
- [ ] Local dialect was sampled (three neighboring files) before deviating from it.
- [ ] Every recommendation has a gate; gates that were run have an evidence packet with stated limits.
- [ ] Observability names the join key, log shape, metrics and bounded labels.
- [ ] No number is presented as measured without its harness; product numbers are dated.
- [ ] Claims are labelled by evidence role; upstream attributions use two-hop wording.
- [ ] For a .NET/Angular slice: outcomes are distinct end to end, one state owner, one async model, runtime parse or documented atomic trust, a negative browser path, compatibility and rollback.
- [ ] For extraction: every record has all schema fields, a compiling snippet and resolvable provenance.
- [ ] For a review of a reference, skill or catalogue: the seven general requirements, the evidence obligation and the family's depth, worked example and artifact were checked (section 6.7).
- [ ] Rollback or escalation and the reopening condition are stated.
- [ ] Anything outside scope was routed to a named skill instead of answered from the wrong altitude.
