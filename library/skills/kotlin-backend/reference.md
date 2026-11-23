# Kotlin Backend Reference

Depth behind [SKILL.md](SKILL.md). The skill file carries the workflow, rules, templates and commands. This file carries the reasoning, the ranked patterns, the tradeoffs, the worked cases, the failure tables and the evidence rules.

## Idiomatic Thesis Synthesis Statement

Reliable Kotlin makes ambiguity visible at boundaries and keeps the core small, non-null, typed and cancellation-aware. Any paraphrase has to keep the cancellation clause; "boundary-visible, core-typed" alone is incomplete.

A Kotlin backend is reliable when coherence is controlled across trust, authority, validation, execution, side effects, dependency failure, durability and operations. The order of controls is fixed by cause, not by taste:

1. Inspect the stack.
2. Specify behavior.
3. Map the six boundaries.
4. Model types, errors and transactions.
5. Implement the smallest change.
6. Verify functional and operational claims.

A generic verifier cannot rescue a wrong framework, a wrong transaction scope or a wrong blocking model. Verification cannot repair a wrong starting assumption, and a correct starting assumption does not make an untested one safe.

The causal pipeline for the Kotlin inside the service:

```text
uncertain ingress
  -> boundary normalization
  -> explicit domain states and identity
  -> owned execution and state lifetime
  -> explicit blocking and failure policy
  -> caller-visible outcome
  -> claim-matched verification
  -> selective learning and invalidation
```

Boundary and ownership fixes have more leverage than formatting or analyzers, because neither of those can recover a discarded state or a lost owner. Identify what kind of uncertainty enters: presence, format, authorization, version, lifecycle, thread behavior or failure class. A generic null check cannot preserve distinctions nobody named. Choose the least complex representation that keeps the consequential states.

Framework idioms are dependency-topology decisions. Scheduler, transaction, serializer, proxy and lifecycle assumptions matter more than concise syntax. Choose blocking or non-blocking end to end. Local consistency is safer than novelty.

Runtime principles:

1. Lifecycle outcome before tool.
2. Target before ecosystem preference.
3. Preserve artifact lineage.
4. Configuration is an input contract.
5. Secrets are both data and authority.
6. Signals answer decisions.
7. Health controls automation, so it must describe real traffic semantics.
8. Migrations are deployed behavior.
9. CI gates claims, not checkbox volume.
10. Shutdown is correctness.
11. Recovery is observed, not promised.
12. Every mechanism creates lifecycle cost: owners, consumers, compatibility, tests and retirement.

This synthesis combines the owner's doctrine with public ecosystem practice. Label it as a combined inference; do not present it as universal Kotlin consensus.

## Pattern Scoreboard Ranking Table

All scores in this section are the author's emphasis. None is a measured defect rate, probability, coverage figure or service objective. The order is a review priority, not an implementation order and not a team's defect distribution.

### Kotlin reliability patterns

| Rank | ID | Score | Pattern | Area |
| ---: | --- | ---: | --- | --- |
| 1 | `KC1-01` | 98 | Contain platform types at Java boundaries | Nullability and interop |
| 2 | `KC1-02` | 96 | Prefer non-null domain types and explicit absence | Nullability and interop |
| 3 | `KC1-09` | 95 | Preserve structured concurrency and cancellation propagation | Coroutines and Flow |
| 4 | `KC1-03` | 94 | Use value classes for meaningful primitive identifiers | API and type design |
| 4 | `KC1-10` | 94 | Do not swallow `CancellationException` | Coroutines and Flow |
| 6 | `KC1-04` | 93 | Use sealed outcomes for closed result and state spaces | API and type design |
| 7 | `KC1-05` | 91 | Keep data classes for value data, not lifecycle-heavy entities | API and type design |
| 7 | `KC1-11` | 91 | Isolate blocking calls from coroutine dispatchers | Coroutines and Flow |
| 9 | `KC1-06` | 90 | Prefer immutable collections and constructor-injected state | API and type design |
| 9 | `KC1-07` | 90 | Parse raw inputs once before domain logic | API and type design |
| 11 | `KC1-08` | 89 | Use scope functions only when receiver and return semantics stay obvious | API and type design |
| 12 | `KC1-12` | 88 | Make Java interop contracts explicit with annotations and overload choices | Nullability and interop |
| 13 | `KC1-13` | 87 | Use focused extension functions at stable ownership boundaries | API and type design |
| 14 | `KC1-14` | 86 | Keep public API growth binary- and source-compatible where possible | API and type design |
| 15 | `KC1-15` | 85 | Test cancellation, nullability, and serialization boundaries directly | Testing |

The five doctrine areas are API and type design, nullability and Java interop, coroutines and Flow, testing and fixtures, and tooling and build gates. `KC1-06`, `KC1-08` and `KC1-13` to `KC1-15` have thinner written guidance than their scores suggest; treat them as prompts for judgment. `KC1-09` to `KC1-11` are the most perishable, because they depend on the coroutine library's behavior; date any claim about them to the library version in the build.

Review boundary work before style. For a trivial diff, use the top five rows or the six review questions.

### Evidence hygiene patterns

| Score | Pattern | Prevents |
| ---: | --- | --- |
| 95 | Start from the target and the owner's doctrine before synthesizing | Generic advice that ignores the repository. A reproduced consequential defect may be contained first, with evidence reconstructed after |
| 91 | Split evidence by kind: owner doctrine, retrieved external fact, inference | Hidden authority boundaries |
| 88 | Couple every consequential claim to a test, command, analyzer, review assertion, owner decision or explicit blocked need | Instructions nobody can check |

The chain is ordered: target first, then evidence labels, then a gate. In an outage, stop event-loop blocking or transaction hazards first, then finish the evidence before making the mitigation permanent.

### Named design patterns

| Pattern | Note |
| --- | --- |
| Boundary uncertainty normalization | Convert once, in an adapter |
| Closed domain state modeling | Open extension or serialization constraints may require translation at the boundary |
| Caller-owned coroutine lifetime | Parent owns children |
| Explicit blocking execution boundary | Do not dispatcher-switch genuinely non-blocking APIs, and do not claim that a switch gives scalability or cancellability |
| Scoped state injection | Immutable constants and framework registries are separate cases |

A pattern's status in a given target is one of: candidate, default for scope, conditional for scope, superseded for scope, rejected for scope.

### Security and resilience adoption order

Adopt in this causal order; each depends on the ones before it:

1. Protected transition boundary.
2. Trust and authority boundary split.
3. Typed failure and response contract.
4. Structured execution lifecycle.
5. Transactional side-effect integrity.
6. Bounded dependency recovery.
7. Durable worker execution.
8. Negative and failure gate coupling.
9. Operational recovery and invalidation.

### Hard gates for backend delivery

| Gate | Kind |
| --- | --- |
| Surface before mode | Blocking |
| Preserve framework and versions | Blocking |
| Executable outcome | Blocking |
| Service boundary map | Blocking |
| Framework lane | Blocking |
| Boundary-first testing | Blocking |
| Cancellation and blocking truth | Blocking |
| Transaction and migration truth | Blocking |
| Security negative paths | Blocking |
| Runtime and rollout | Promotion gate |
| Route reassessment | Learning gate |

### Runtime gates

| Gate | Direct falsifier |
| --- | --- |
| Runtime outcome before tool | The mechanism has no stated normal, failure, shutdown or recovery outcome |
| Preserve target stance | A wrapper, version or tool changed without an accepted gap |
| Immutable artifact identity | The promoted artifact differs from the tested one |
| Typed startup contract | Valid, absent, malformed, conflicting and redacted states do not produce the accepted startup behavior |
| Secret boundary | A synthetic secret appears in a response, log, trace, label or error report |
| Compatibility before migration | Old and new application versions cannot both run against a schema state |
| Signal to action | A signal has no operator decision |
| Health and traffic truth | Automation sends traffic too early or restarts a recoverable service repeatedly |
| Package and least privilege | The container runs with more privilege or ports than needed |
| Gate placement and coverage (promotion) | A deliberate defect does not fail the intended stage |
| Staged rollout control (production) | Nobody is authorized and able to stop the rollout |
| Graceful termination | Accepted work is lost, duplicated or left unrecoverable |
| Recovery rehearsal (promotion) | The recovery path has never been exercised |
| Route reassessment (learning) | New evidence did not change the plan when it should have |

Build and static gates run early for fast feedback, but they do not outrank data integrity, secret exposure, traffic safety or recovery. Hard gates are never averaged into an aggregate score. One dangerous scheduler or transaction error must not be averaged away by many trivial passes.

## Agent Usage Decision Guide

### When to open which part

| Situation | Lead | Support |
| --- | --- | --- |
| Vague backend request | Spec Mode, then the service anatomy | Testing once the failure boundary is known |
| Known Spring or Ktor wiring defect | Framework rules first | Service anatomy only if ownership is unclear |
| Storage change | Persistence | Real-dialect tests and runtime migration rules |
| Auth or account flow | Security | Framework configuration and denied-path tests |
| External write with retry | Spec, framework, Coroutine, Resilience, Operations and Testing as one correctness chain | None omitted without a reason |
| Sync read endpoint over an existing service | Spec, framework, Testing | Not Coroutine or Persistence |
| Worker refactor | Review plus Coroutine | Resilience |
| Pure Kotlin type or domain change | Language rules | Operations only if serialization, config, artifact or lifecycle changes |
| Agent-written Kotlin about to merge | The fifteen patterns and the six questions | Gates |

Select modes by changed behavior and consequence, not by keywords. Mode selection is additive but behavioral. Every omitted mode needs a reopen condition. A novel shape needs an explicit mode composition, and repeated novel compositions signal a missing mode. A greenfield service has no stack to preserve: Spec Mode drives, and stance conflicts go to the user. Spring is not a universal preference; a Ktor-first repository stays Ktor.

### Operating sequence

1. State the goal, the target and the write boundary.
2. Discover the target: framework, versions, wrapper, modules, tests, static analysis, CI, consumers.
3. Name the surface and the main risk.
4. Choose one lead mode and the support modes, each with a named interface question.
5. Write the requirements and the first negative case.
6. Trace one real request or job through the six boundaries. Layer count is not mandatory; the trace is.
7. Run the narrowest gate that is expected to fail before the repair, and confirm the failure cause.
8. Make the smallest correction.
9. Rerun the focused gate, then the affected wiring, infrastructure, migration, security and rollout gates.
10. Record result, limitation, skipped gates and owner decisions.
11. Reassess the plan when evidence changes it.

### Work states and modes

Kotlin work moves through: orient, inspect, reproduce, design, implement, verify, route, blocked, handoff. Working modes:

| Mode | Rule |
| --- | --- |
| Review only | No edits and no completion claims |
| Focused repair | One bounded fix; do not route it away merely because the wider architecture is imperfect |
| Characterization first | Preserve ambiguous behavior with tests without calling it policy |
| Adapter containment | Normalize at one adapter and leave the rest |
| Staged migration | Inventory, compatibility, stages, rollback |
| Specialist route | Hand one claim to its owner |

Security and resilience work moves through: orienting, policy or threat blocked, contract specified, implemented, negative verified, fault verified, operationally ready, invalidated. Readiness is non-monotonic: a change in identity, permission, schema, runtime, transaction or deployment reopens the matching stage. Urgency can reorder stages. It cannot turn missing evidence into proof.

### Start blockers

Do not start implementation while any of these is unknown:

- Target, framework, version or wrapper.
- The owner of a policy the change depends on.
- The identity of an effect that can repeat.
- The blocking and cancellation model.
- Schema, dialect or rollout plan for a storage change.
- A fixture that can show the failure.
- What "secure", "fast" or "resilient" means in observable terms.
- Whether independently releasable outcomes have been bundled.

Stop and escalate when the request is ambiguous, no owner exists, backend architecture is being decided from generic advice, or a critical version-sensitive fact cannot be established. Never run repository-wide lexical replacement, install unrequested tools, replace frameworks, invent domain states, guess dispatcher limits or claim broad completion from narrow gates.

### Handoff

A handoff carries: requirement identifiers, boundaries, code paths, tests, dependency versions, risks, rollback, owner, expected output, stop condition and return path. It must be reconstructable without the conversation. A handoff cannot authorize a migration or relax scope.

Routing to another owner takes one of four forms:

| Form | Meaning |
| --- | --- |
| Consult | The current owner stays primary |
| Compose | Claims are split under one integration owner |
| Transfer | The destination owns the whole misclassified task |
| Block and route | The affected claim stops while safe work continues |

Good: prove a Java call blocks locally, then consult the runtime owner about saturation. Bad: send every `!!` to security. Reject circular routing. A handoff succeeds only when it returns reduced uncertainty and a concrete decision.

## Decision Tradeoff Guide

### Framework and execution model

| Choice | Choose when | Cost of being wrong |
| --- | --- | --- |
| Spring MVC with blocking JPA or JDBC | Conventional CRUD; dependencies block; the repository is Spring | Low; an isolated, timeout-bound client covers outbound calls |
| Spring WebFlux or coroutines | The repository and every dependency are non-blocking, or the team accepts the complexity | Blocking on the event loop |
| Ktor, coroutine-first | The repository is Ktor-first and its dependencies support the model | Blocking on the event loop; uncontrolled plugin composition |
| Deliberately blocking service with a bounded pool | Dependencies block | Safer than unnamed blocking on an event loop |
| New isolated Ktor prototype | Only as a reversible evaluation | Provisional until workload, ownership, deployment and integration evidence support it |

Avoid fashionable R2DBC, JPA on an event loop, hybrid stacks and ceremony without invariants. Introducing Ktor and R2DBC together is the bad case. The cost of an error here is a thread-pool, proxy, transaction or public-contract mismatch, not syntax. Compare options on workload, stack, dependency blocking, team operations experience, public-contract impact, tests, observability, migration cost and rollback. Excellent framework code can still be wrong in stance.

### State and outcome

| Choice | Choose when |
| --- | --- |
| `T?` | One absence, and every caller takes the same action |
| Enum | Closed labels with no payload |
| Sealed type | Distinct payloads or actions |
| Typed exception | Framework or API propagation, with an explicit taxonomy |
| `Result<T>` | One understood failure channel |

### Identity

| Choice | Choose when |
| --- | --- |
| Data class | Immutable true values |
| Plain class with explicit identity | Lifecycle entities |
| Framework model | The framework's contract governs |
| Separate persistence, transport and domain models | The boundary contracts conflict |
| One shape for everything | Explicit, tested, tiny CRUD with an exit trigger: a new invariant, scale or a new boundary |

A data-class entity that a framework requires may stay temporarily, with characterization tests.

### Coroutine scope

| Choice | Choose when |
| --- | --- |
| `coroutineScope` | A child failure should cancel its siblings |
| `supervisorScope` | Children are independent and every result is accounted for |
| Lifecycle scope | The application owns the lifetime |
| Durable queue | The work must survive and recover |
| Process scope | The work is genuinely process-lifetime |

Flow and callback bridges need the same ownership answers. Define whether collection is cold (the producer runs per collector) or shared, the producer scope, when the callback is registered and unregistered, the buffer, the overflow policy, the terminal event and the cleanup. Identify whether the Flow carries state or events: conflation may fit state and corrupts event semantics. Bound parallel child creation before launching work; a bounded downstream client does not make an unlimited launch harmless, and a detached scope is not an overflow strategy. Observe waiting and active work separately: cancellation while waiting must remove ownership cleanly, and a blocking Java call inside `withContext` may continue after cancellation when it is noncooperative, so make the residual work and effects visible and route capacity or shutdown questions to runtime operations. Cleanup must not restart cancelled business work.

### Consistency across systems

Prefer a local transaction that couples the idempotency record with the state change. When systems cannot share a transaction, use an outbox, saga, compensation or reconciliation, and expose the partial or unknown state. Never claim atomic exactly-once. Deliberately allow loss only for owner-approved, low-consequence telemetry.

### Test realism

Compare on semantic fidelity, feedback time, isolation, reproducibility, diagnostic precision, lifecycle cost and the consequence of a false negative. Prefer a hybrid portfolio: cheap unit and slice tests for invariants, plus a small realistic set for dialects, transactions and wiring. Escalate when a test failure could authorize destructive migration, security, money or concurrency behavior.

### Runtime decision modes

| Mode | Choose when |
| --- | --- |
| Preserve | The established mechanism satisfies the accepted outcome |
| Adapt in place | One boundary needs a bounded change |
| Compose | Two owners each hold part of the outcome |
| Coexist temporarily | A staged move needs both paths; each temporary path needs an owner, a signal, a deadline and removal evidence |
| Replace | Demonstrated unfitness, not tutorial appeal |
| Split outcome | Independent outcomes were bundled |
| Defer with evidence | The evidence is not yet available and the risk is bounded |
| Stop and contain | A hard gate fails |
| Retire | The mechanism no longer has consumers |

Hard gates come before any scoring. An option is out if policy or authority rejects it; the artifact cannot be built, identified, promoted or started reproducibly; configuration or secret behavior leaks or bypasses validation; data and migration states cannot preserve invariants and consumers; health or rollout automation sends unsafe traffic or amplifies failure; shutdown, retry or recovery can silently lose or repeat an unacceptable effect; it depends on an inaccessible owner or environment while claiming production readiness; or there is no feasible containment for a partial transition.

Tradeoff dimensions and their usual blind spots:

| Dimension | Blind spot |
| --- | --- |
| Target fit | Choosing by generic Kotlin popularity |
| Correctness | Testing only steady-state success |
| Compatibility | Treating build compatibility as runtime compatibility |
| Reversibility | Saying "rollback" when data or effects are irreversible |
| Operational burden | Counting implementation effort but not on-call work |
| Failure amplification | Evaluating components in isolation |
| Security and authority | Assuming a managed service means secure defaults |
| Delivery evidence | Relying on stage count or green status |
| Performance and capacity | Unsupported percentages or average-only comparison |
| Complexity | Fewer source lines is not lower system complexity |
| Evidence cost | Selecting the option that is easiest to demonstrate |
| Future option value | Speculative abstraction |

Decision protocol: name one decision; state the accepted outcomes and hard gates; record the target baseline; list feasible alternatives, always including preservation and the smallest adaptation; reject non-starters explicitly; map the transition states (entering, operating, failing, recovering, retiring); pick the cheap scenario that can eliminate an option first.

Examples. Good preservation: keep the existing migration tool, add a nullable column by expansion, remove the old one in a later contract step. Familiarity is not the reason; demonstrated fit is. Justified adaptation: add one bounded drain-deadline signal, not new exporters, collectors and dashboards. Unjustified replacement: answer a shutdown defect by moving framework and broker because tutorials advertise structured concurrency.

A broader mechanism earns its place only when it protects an accepted boundary that the simple route cannot.

## Theme Specific Artifact

### Request-lifecycle dossier

For a non-trivial endpoint or worker:

```text
HTTP request
  -> Transport    (parse / auth / map)
  -> Application  (use case / idempotency / transaction choreography)
  -> Domain       (typed invariants / state / outcome)
  -> Persistence  (query / migration / transaction)
  -> Integration  (timeout / retry / dedup or outbox)
  -> Runtime      (logs / metrics / health / rollout / rollback)
  -> HTTP response or durable worker outcome
```

The dossier lists request and response contracts, domain types and outcomes, the transaction, persistence and migration, external timeout, retry and idempotency, the dispatcher and blocking model, logs, metrics and health, tests, rollout and rollback, and a failure table. Every boundary needs an owner, an observable failure and a recovery. Use a compact checklist for small endpoints, a state-transition table for domain-only work, and a sequence or deployment diagram for distributed workflows. Signs of false readiness: decorative happy-path arrows, retries inside transactions, missing cancellation, metrics with no owner.

The dossier is an attachment to the `Service Design` section of the eight-section work packet. It does not replace the packet. The reviewable instance is one filled packet for a representative endpoint in which every requirement row has a test row and the `Open Questions` section is filled, not skipped.

| Packet | Verdict |
| --- | --- |
| Every requirement row has a test row; gate output and open questions are attached | Good |
| A lifecycle diagram with no requirements behind it | Bad: not a sufficient packet |
| A journey or packet that stops at the framework choice | Bad: the pivotal step, the requirements, is missing |
| A review-mode packet with findings in place of an implementation plan, noted as review-shaped | Borderline: acceptable with the note |
| A hotfix recorded as a two-line requirement and a test, with the compression noted | Borderline: acceptable with the note |

A full packet is ceremony for a trivial fix. A review pass, a trivial fix or a hotfix may compress it only when the compression, the provenance and the resulting limitation are stated. Provenance matters because a packet written after implementation looks identical to a spec-first one. Record requirements as the literal delivered text; paraphrases drift from what was agreed. Whether compressed packets for tiny fixes are retained in full or sampled is a provisional rule for the repository owner to set.

### Route record

```yaml
status: orientation-only | planning | implementation-ready | verified
surface: <Spring MVC API | Ktor service | worker | ...>
framework_and_versions: <as found in the build>
primary_mode: <one mode>
companion_modes: [<mode>, ...]
omitted_modes:
  - mode: <mode>
    reason: <why it does not apply>
    reopen_when: <condition>
required_artifacts: [<requirement list>, <verification matrix>, ...]
first_negative_case: <the first failure to prove>
stop_condition: <what ends the work>
```

### Protected transition review packet

Each field is in one state: verified, approved, inherited and checked, provisional, blocked, or not applicable.

1. Identity, owners and mode.
2. Goal and non-goals.
3. Trigger, bounds and untrusted data.
4. Actor, authentication, mapping and revocation.
5. Resource and tenant authorization, and the denial behavior.
6. Inputs, invariants and errors.
7. Effect, severity and reversibility.
8. Commit, acknowledgement and ambiguity.
9. Replay key: scope, uniqueness, order and retention.
10. Deadline and cancellation.
11. Blocking and capacity.
12. Typed failures, retry and backpressure.
13. Durable work.
14. External dependencies.
15. Abuse and fault cases.
16. Redacted observability and operations.
17. Evidence ledger.
18. Invalidation map.
19. Handoff and rollback.

### Kotlin quality evidence packet

A proposed format, not evidence that any team has adopted it. Use the compact profile for one private distinction with bounded callers and no persistence, concurrency or public API effect; the standard profile for several callers or an integration; the migration profile for a public API, a persisted model, a shared global or framework entity, or cross-owner concurrency. More burden changes volume, not honesty.

Core fields: packet identity; user goal and non-goals; target identity; write and action boundary; boundary and caller map; claim inventory; finding dispositions; state and identity contract; execution and state ownership; decision and alternatives; change surface; gate matrix; exceptions and accepted risk; blockers and completion split; rollback or containment; observability and privacy; handoff and invalidation.

Finding dispositions. Classify each construct (`!!`, `lateinit`, `GlobalScope`, a broad `catch (Exception)`, a data class, `Dispatchers.IO`) by the contract it can erase. Every observed candidate then ends in exactly one state:

| Disposition | Meaning | Required before closing |
| --- | --- | --- |
| `confirmed_defect` | The contract loss and the consequence in the target are observed | Repair and regression evidence |
| `conditional_hazard` | The dangerous interpretation is plausible | The named invariant or behavior test that is still needed |
| `bounded_exception` | Invariant, owner, scope and verification make the construct acceptable on this path | The exception record: exact path, invariant, owner, failure consequence, test or framework evidence, review trigger |
| `accepted_risk` | An accountable owner accepts a stated consequence and a review trigger | The owner decision. This is not the same as safe, and it is not evidence that no defect exists |
| `not_applicable` | Generated, framework-owned or non-production context, or an absent mechanism, makes the hazard irrelevant | The reason, recorded |
| `blocked` | Domain, framework, dependency, security or operational authority is missing | Routing to that authority. Do not manufacture a replacement |

Promotion rule for borderline cases: a conditional case becomes a bounded exception only when it records the exact path, invariant, owner, failure consequence, test or framework evidence and review trigger. Without that evidence it remains a finding, not a stylistic disagreement.

Each claim has a stable identifier such as `KQ-NULL-001`, falsifiable text, a class (boundary, state, identity, coroutine, blocking, failure, mutable state, gate or runtime), an evidence state, its support and limit, its verification, the decision and an invalidation condition.

Blockers, lowest first. Passing a lower one does not imply the later ones:

| Blocker | Meaning |
| --- | --- |
| `B0_integrity` | The target or source cannot be identified reproducibly |
| `B1_semantic` | The meaning of a state or outcome is undecided |
| `B2_ownership` | A state, lifetime or decision has no owner |
| `B3_behavior` | The behavior is not shown by a test |
| `B4_integration` | The change is not proven with its callers |
| `B5_operational` | No runtime or capacity evidence |
| `B6_external` | A red gate belongs to someone else |

Semantic completion can coexist with a `B5` no-capacity-claim or an attributed `B6` red. Acceptance is both structural and semantic; automation cannot replace semantic review.

### Fixture plan

One row per claim: requirement identifier, boundary, test type, subject, dependencies, real-or-fake rationale, data builder, lifecycle owner, isolation key, clock and dispatcher control, injected failure, assertion, cleanup, command, flake response and unresolved risk.

When one plan stops being reviewable. Keep one fixture plan for one owned service capability. Split it by independently deployable system, data store, external contract, security boundary or verification environment when ownership, lifecycle or failure semantics diverge. Shared fixture abstractions across independent systems create hidden coupling. Fully isolated plans leave cross-system contracts untested unless a deliberate integration owner remains.

Each split keeps:

- an owner, and one verification owner for that split;
- a requirement subset;
- a fixture namespace;
- a gate;
- a dependency contract;
- an evidence handoff;
- one higher-level, cross-split test that proves the interactions the split cannot, held by a named integration owner.

| Case | Verdict |
| --- | --- |
| Separate producer and consumer fixture plans with a versioned contract test and one integration owner | Good |
| Two agents rewriting one global fixture file at the same time | Bad |
| A shared Testcontainers utility whose lifecycle and schema isolation stay owned by each service suite | Borderline: acceptable |

Failure boundary: parallel agents edit the same artifact; every module invents incompatible fixtures; a monolithic environment serializes all work; or the split removes responsibility for migration order and cross-service idempotency. Bounded alternatives: contract tests between services, a dedicated end-to-end environment, shared low-level builders with locally owned lifecycle, CI sharding, dependency-graph narrowing, or a staged migration plan. Watch for shared databases that cross ownership, port and namespace collisions, version skew in contract simulators, duplicated cleanup, secret distribution, test-data sovereignty and evidence labels lost at merge time.

Verify a split by auditing ownership and path exclusivity, running contract compatibility in both directions, exercising independent and integrated cleanup, checking CI shard determinism and tracing one requirement across every split gate. The right partition and shared-infrastructure strategy depend on deployment topology, data ownership, CI capacity and team boundaries. Fixture architecture often reveals organizational architecture: cleanup, credentials and contract ownership make hidden service coupling visible before production deployment.

### Runtime operations runbook

A runbook is complete only when an authorized responder can identify the intended artifact and state, choose the next action from observed evidence, execute or escalate, and verify the recovered condition. A collection of commands without decision boundaries is not complete. Unknown values stay explicitly unknown, with an owner.

Tiers: bounded handoff, release runbook, incident-capable runbook.

| Field | Reject when |
| --- | --- |
| Purpose and scope | Missing |
| Target identity | Ambiguous environment |
| Release identity | A mutable tag |
| Supported states | Only the happy state |
| Prerequisites | Assumed |
| Secret and access boundary | Secrets printed to verify access |
| Baseline | None captured |
| Stage plan | Progression only because time elapsed |
| Decision signals | "Watch logs" |
| Service objective breach | A threshold with no source, applicability or action |
| Health and traffic | Process liveness only |
| Data and migration | No mixed-version statement |
| Worker and shutdown | No statement of work ownership |
| External dependencies | Unlisted |
| Stop conditions | Nobody can stop |
| Recovery options | "Rollback" with no compatibility check |
| Action procedures | Commands with no decision |
| Verification after action | Process health only |
| Escalation and communications | Dependence on one person's memory |
| Evidence preservation | None |
| Known limits | None stated |
| Rehearsal evidence | None |
| Invalidation events | Calendar review alone |
| Retirement | No end condition |

Lifecycle: candidate, qualified, staged, active, degraded, incident, contained, recovered, under review, retired. Qualification levels: reviewed, tabletop, isolated drill, staged rehearsal, incident validated (valid for that incident only). A rehearsal measures whether the responder recognizes the state and chooses correctly, not how fast commands are typed. A bad entry reads: "deploy latest, watch logs for a few minutes, roll back if errors rise".

The runbook must not invent a service objective. A breach signal is a hypothesis until it is correlated with service and business state.

### Framework idiom decision packet

Use it to record a Spring or Ktor idiom decision so a reviewer can reproduce the decision and its stop condition.

Fields:

- user-visible contract;
- current framework and execution model;
- dependency and lifecycle map;
- chosen Spring or Ktor pattern;
- cross-framework type rules;
- rejected alternatives;
- failure and rollback boundaries;
- test matrix;
- evidence labels;
- expected results and observed results, kept apart;
- ownership.

Rules:

- Every field holds a repository observation or an explicitly labelled uncertainty.
- Write one packet per service capability or coherent change. Split independent framework or ownership decisions into separate packets.
- Replace an expected result with an observed one only after the listed tests have run.
- A rollback names its trigger and its owner.
- Keep the bad-path fixture.
- Scale the depth with the blast radius.

Lighter alternatives: a short architecture decision for a migration; a test plan for a narrow bug fix; a route contract sheet for a transport-only change; a risk register when several unresolved owners block the choice.

| Case | Example |
| --- | --- |
| Good | A Spring MVC endpoint over JPA, documented with its transactional service, stable error mapper, integration fixture and rollback flag |
| Bad | "Use idiomatic coroutines", with no dependency trace |
| Borderline | A Ktor plugin plan written before implementation. Acceptable only if every result stays marked expected until `testApplication` evidence exists |

## Worked Example Set

Do not transfer paths, commands, status codes or time budgets from these examples to a target. Check each example by mutation: swap Ktor and Spring, read and write, request-scoped and durable, mock and real, planned and executed. The plan must change when one of those flips.

### Create account (Spring or Ktor)

- **Good:** parse and authenticate, map to a command, return a sealed duplicate outcome, commit once, ship a safe migration, prove HTTP 409 with an integration test against the production dialect, and carry operations and rollback evidence.
- **Bad:** bind JSON directly to a JPA data class and catch `Exception`.
- **Borderline:** one shape for request, entity and response in a tiny CRUD service. Acceptable only when the tradeoff is explicit, tested and has an exit trigger.

### Spring domain interval

An interval requires `end >= start`. Enforce it at the domain boundary so that HTTP, worker and internal entry points all get it. A Bean Validation annotation alone is the bad version. Whether equal bounds are allowed is a product question; stop and ask. Test valid, equal and reversed input through the alternate entry points as well.

### Ktor provider read

An existing Ktor read-only price route calls a provider. Do not invent a database, cache, queue or idempotency. Owners define freshness, provider mapping, total deadline and degraded behavior; a stale fallback is an owner decision. The first negative case is a provider call that exceeds the deadline or completes after cancellation. If the SDK blocks, choose an intentionally blocking design or a bounded executor with capacity evidence. A cache adds freshness, key, invalidation and storage decisions. A durable refresh adds a worker, broker, idempotency and restart. A principal change activates Security.

Required tests: success; invalid input rejected without a provider call; provider 4xx, 5xx, connection failure and malformed body; timeout inside the total budget; caller cancellation with cleanup; a stale completion that mutates no shared state; missing configuration that fails safely at startup; bounded, non-sensitive observability.

The bad answer recommends Spring WebClient, a generic retry, a suspend-wrapped blocking SDK and a guessed test pass.

### Spring idempotent write

Put a unique external key inside the authoritative transaction. Prove it against the production dialect with a concurrent duplicate fixture, plus the migration and rolling compatibility. An in-memory precheck, a mock or H2 cannot prove atomicity. Historical duplicate rows need a remediation owner before the constraint lands.

### Ktor durable export

Split acceptance from the worker. Give each export a durable identity, a lease, delivery semantics, and restart, shutdown and idempotency behavior. An untracked coroutine loses the work. Future scale alone does not justify a queue.

### Payment-style transition

Sealed outcome, typed identifier, service-level transaction, timeout-bound client and stable error envelope. Manual mapping is enough until complexity justifies mappers. The provider commits a charge, the response is lost, and the retry uses another key or none: stop the blind retry, reconcile by the stable key, and add a test for response failure after provider commit. "Payment API error; add retries" is the bad answer.

### Framework trio

- **Good:** a Spring MVC controller calls a transactional blocking-JPA service, with centralized mapping of sealed outcomes to errors, typed configuration and a stable error test.
- **Bad:** a suspend WebFlux handler invokes JPA directly and holds a transaction across an HTTP call.
- **Borderline:** a Ktor service isolates one blocking client on bounded capacity and propagates cancellation where it can. It stays provisional until load and timeout tests pass.

Each framework example should state the context, the selected idiom, the causal reason, the observable consequence, the evidence, the public response and the recovery.

### Testing trio

- **Good:** Ktor `testApplication` proves that invalid JSON maps to a stable error body, and a production-dialect database test proves that duplicate insertion is atomic.
- **Bad:** a mocked route verifies that the repository was invoked and claims both are covered.
- **Borderline:** a Spring `@WebMvcTest` proves security and serialization only with the filters included; transaction semantics remain outside it.

### Kotlin construct cases

| Case | Unsafe | Coherent |
| --- | --- | --- |
| Meaningful identifier | Raw strings for `UserId` and `InvoiceId` drift across many domain calls; or every `String` is wrapped because wrappers score high, with public construction unrestricted and serializer and consumer checks skipped | `@JvmInline value class UserId private constructor(val value: String)` with `parse(raw): UserId?` in the companion, parsed once at the adapter. Evidence: parser tests for empty, whitespace, valid and round-trip values; compile checks that the two identifiers cannot be interchanged; target serializer and generated-surface tests; Java and API or ABI gates only when such consumers exist. If Java callers or framework binding appear after the design, keep the type internal or keep the raw public signature while generated representation, annotations, boxing, reflection and compatibility are investigated, and do not call the public wrapper safe yet |
| Platform nullability | `CustomerName(javaDirectory.find(id).name!!)` loses whether the customer, the name or the dependency was absent | Normalize to found, missing, malformed or dependency failure only when callers need the distinction; use `CustomerName?` for one common absence |
| Cancellation | A broad catch around `remote.refresh()` | Catch and rethrow `CancellationException`, then translate the known remote failure. A boundary may translate cancellation only if it owns and tests cleanup and there are no side effects |
| Identity | A data class for an entity | `Money(currency, minorUnits)` is a good immutable value. For an entity, test equality before and after the identifier is assigned, collection membership, copy invariants, and persistence, proxy and serialization |
| Blocking | `suspend fun readInvoice(...) = legacyJdbcClient.read(...)` still blocks | `withContext(blockingDispatcher)` helps only for confirmed blocking with an owned bounded policy and stated cancellation limits; or expose `readInvoiceBlocking`. A saturation claim needs a load measurement |
| Global state | A mutable singleton store | Inject a `SessionStore` with an application, request or test lifecycle, synchronization, reset and shutdown |
| Scope functions and booleans | One chain that normalizes, audits, saves and notifies and returns `false` for absent input, rejection, conflict and failure alike | Named steps and caller-relevant outcomes. A short one-receiver chain or a private pure predicate may stay |
| `lateinit` | A required dependency outside any managed lifecycle | Acceptable for a framework-injected dependency when it is lifecycle-managed and the justification is recorded |
| Retry helper | A helper catches all throwables, logs or maps them and does not rethrow cancellation | Rethrow first. Defensive-looking code can silently leak cancellation |

A sealed outcome can still be undermined by a payload where every field is nullable. Grade an example by whether ambiguity stops at the boundary and cancellation survives every wrapper.

### Unsafe to coherent, security and resilience

| Unsafe | Coherent |
| --- | --- |
| Global lookup after authentication | Tenant- and resource-scoped lookup |
| `catch (Throwable)` | Preserve cancellation |
| Retry every exception | Typed transient policy |
| Detached critical coroutine | Durable accepted work |
| Raw provider error | Normalized bounded response |

A simpler model is allowed for a read-only internal health detail only if exposure, identity, sensitivity, blocking and the absence of writes are explicit and tested.

### Runtime cases

- **Typed outbound-client configuration.** Bind raw values once at the composition boundary. Separate sensitive handles from printable configuration. Inject only the settings each adapter needs. Derive the timeout from the end-to-end budget. Test valid, absent, malformed, minimum, maximum, unknown-key, denied-secret and restart. The misleading path reads the environment deep in the client on each call, turns a parse failure into a default, prints the full configuration object in an error, takes a timeout from a tutorial and adds a new configuration library.
- **Signal and health.** Distinguish downstream saturation from validation, application, network and telemetry failure. Add only the missing classification. Do not fail liveness because a dependency is unavailable. Trace the signal from SDK to exporter, collector, backend, query, alert, consumer and runbook. Inject telemetry loss so that absence is not mistaken for recovery. The misleading path adds a new stack, uses paths and exception messages as labels, raises an alert on a threshold nobody owns, and puts every downstream into liveness.
- **Schema and rolling change.** Inventory prior schema states, application versions, consumers and historical data shapes. Express the invariant independently of migration syntax. Find violating rows and decide on remediation or quarantine. Expand, deploy tolerant code, backfill, observe, switch, and contract after old consumers are gone. The misleading path adds validation and a required constraint in one release, verifies on an empty database and calls the change reversible because the previous image exists.
- **CI gate and immutable promotion.** Stage count is irrelevant. Each gate names a failure class. Run a negative control. Confirm that a green stage does not hide a skipped or empty test selection.
- **One required timeout setting.** Good: use the existing binder, typed validation, and valid, missing and malformed production-like startup; add telemetry only if operators need a new failure distinction. Bad: a pure parser change triggers a new linter, a metrics stack, a container base, a readiness endpoint and an arbitrary latency objective. Conditional: a schema migration is valid locally but the rolling-deploy policy and production data shape are unavailable; the result is planning-level and must not be called rollback-safe or rollout-ready.
- **Incident trace.** Failures rise after a schema and image change. The poor response rolls the image back immediately. The disciplined response preserves state, then asks whether old code is compatible with current data, whether the promoted digest matches CI, and whether this is application failure, false readiness or telemetry loss, and only then chooses. If data changed irreversibly, do not restore old code merely because it is available.

## User Journey Scenario

### Journey 1: account creation endpoint

1. State the observable contract: 201 with the public id, 409 for a duplicate email, no leak about inactive accounts.
2. Find the framework entry point and the execution model.
3. Map transport input to an application command.
4. Put the business decision in the application and domain layers.
5. Wire configuration and error mapping.
6. Test one end-to-end success and the principal failure.

Map 201, malformed body, duplicate email, rollback and idempotent retry onto a route slice plus a production-dialect integration test. Coverage percentage, copied fixtures, production-like secrets, controller mocks and startup alone are not proof. A read-only route may omit a write transaction, but it still needs validation, ordering and deterministic pagination. For a vague endpoint request, write at least three executable requirements and record whether each was confirmed by the user or drafted by the agent. Pause for missing constraints.

### Journey 2: Java-backed payment decision

Convert raw Java-client values once at the boundary into typed non-null values. Return a sealed `PaymentDecision`. Preserve cancellation through suspend and retry wrappers. Add risk tests and pass the native gates. The parse-once step stops ambiguity from traveling and simplifies every later rule. A version that skips the adapter can assign a platform type to a non-null field; compilation alone is not completion. The fraud-client version of this journey, with code, is in [SKILL.md](SKILL.md).

### Journey 3: signed provider callback for an invoice

1. The provider account authenticates a bounded callback.
2. The provider identity maps to exactly one local tenant. Tenant text in the payload grants no authority.
3. The invoice lookup is tenant-scoped.
4. One transaction reserves the replay identity and transitions the invoice state.
5. Remote follow-up work is recorded as an outbox intent in the same transaction.
6. The service acknowledges only after the local commit or durable acceptance.
7. The event key is provider-scoped, the database enforces concurrency, a duplicate gets a stable outcome, and retention and late-replay policy are defined.
8. Cancellation before commit rolls back and propagates.
9. A response lost after commit is recovered by replay lookup.

Adverse cases: oversized body, stale or invalid signature, malformed command, unknown provider account, foreign invoice, sequential and concurrent duplicate, timeout, restart, retry exhaustion, and redaction of a synthetic secret. The bad version trusts the token's tenant, launches global work, catches every throwable, logs the auth header and retries a timeout until it succeeds.

### Journey 4: a worker loses work during termination

1. **Preserve evidence.** Revision, image identity, effective non-secret configuration, termination signal and deadline, work identifiers, broker and store state, database rows, external effect identifiers, timestamps. State the strongest supported symptom, such as "in two observed termination windows the application stopped after an external request but before a durable completion record, and one item was later redelivered", not "coroutines lose jobs".
2. **Inspect the target.** Worker entry point, application scope, child scope and supervisor policy, dispatchers, blocking adapters, timeout and retry composition; acquisition, lease, visibility, acknowledgement, retry, dead-letter and redelivery semantics; transaction boundaries, durable work and effect identifiers, completion records; configuration; signals; image, resources, readiness, liveness, termination deadline and restart policy; CI. A shutdown defect is not permission to migrate the framework, broker, telemetry, build system or platform.
3. **Split ownership.** Operations leads lifecycle, configuration, signals, health, drain and restart. Resilience leads idempotency, retry, timeout and effect safety. Service design leads worker and transaction boundaries. Record disagreements: a coroutine may be cancellable while a blocking driver call is not; an application may stop intake while a broker lease continues; a process may exit cleanly while an external effect stays ambiguous.
4. **Write outcome contracts.**

   | Contract | Statement |
   | --- | --- |
   | Admission | Stop acquiring new work before reporting drain complete |
   | Ownership | One durable identity and a discoverable owner per admitted item |
   | Cancellation | Reaches owned coroutine work and bounded blocking adapters within the deadline |
   | Effect safety | A retry after timeout or restart cannot silently repeat an effect; ambiguous effects enter reconciliation |
   | Acknowledgement | Source completion only after the required durable state |
   | Drain | A bounded budget; remaining work reaches an explicit retry, release, handoff or reconciliation state |
   | Resource release | Connections, leases, locks, executors, files, telemetry flush |
   | Restart | Expired, pending, duplicate and partial attempts are detected and resolved without manual guesswork |
   | Signals | Distinguish normal drain, deadline expiry, cancellation failure, duplicate suppression, unresolved ambiguity and recovery |
   | Recovery | A named owner determines the final business state |

   Derive deadlines, throughput and duplicate tolerance from the workload, platform limits, product consequence and a measured baseline. Do not write arbitrary latency or success percentages.
5. **Compare options.** Finish synchronously before the response or acknowledgement; a bounded in-process drain (a forced kill stays ambiguous without durable identity); broker or durable-store ownership (duplicates, leases and backlog become first-class); a transactional intent or outbox (adds a relay, schema, cleanup and lag ownership); idempotency plus reconciliation; temporary operational containment with an owner, a bounded duration and an exit condition. Options can combine. Do not select a complex pattern because it is recognizable; prove the actual gap.
6. **Verify failure first.** Send the same termination signal the target uses at each interruption point:

   | Interruption point | Unacceptable result |
   | --- | --- |
   | Before acquisition | New work is acquired after drain began |
   | After acquisition, before processing | The item disappears on exit |
   | During cancellable processing | Detached work continues with no owner |
   | During a blocking call | Shutdown hangs indefinitely |
   | Immediately before the external effect | The effect happens after the process reported completion |
   | Response lost after the effect committed | A blind retry duplicates an irreversible effect |
   | After the completion record, before acknowledgement | The item is processed again with a second effect |
   | During the drain deadline | The process reports graceful completion while state is unknown |
   | After restart | The backlog looks healthy while business state is partial |

7. **Correct narrowly.** Move worker children under the framework-owned application scope; stop intake before drain; give each item and effect a stable durable identity; order completion and acknowledgement per the target's semantics; use one total deadline; classify failures as retriable, permanent, ambiguous or reconciliation-required; persist restart state without sensitive payloads; emit bounded signals for acquired, active, completed, retried, duplicate-suppressed, ambiguous, drain-expired and recovered; add startup reconciliation or an owner repair path only where the evidence requires it. Do not apply every mechanism at once. If the failure is solely a detached scope with no external effect, structured lifecycle suffices. If external commit ambiguity exists, a graceful delay alone is not enough.
8. **Qualify the artifact and pipeline.** Package once. Readiness stays false until the accepted traffic behavior is possible.
9. **Stage termination and restart.** Capture a baseline; admit known test work with non-sensitive identifiers; terminate at each phase; observe; restart the same artifact; exercise the stop authority; retain the evidence.
10. **Close.** The bad close is a fixed sleep in the shutdown hook, one clean local exit and a "production-safe" label.

The work-item lifecycle used to reason about this journey:

| Phase | Question |
| --- | --- |
| available | Who may take it |
| acquired | Who holds the lease or claim |
| admitted | Has the process accepted responsibility |
| processing | Which scope owns the work |
| effect_prepared | Is the effect identity recorded |
| effect_committed | Did the external or durable effect happen |
| completion_recorded | Is completion durable |
| acknowledged | Has the source been told |
| draining | Is intake stopped and what remains |
| terminated | What state was left behind |
| restarted | What does the new process find |
| recovered | Is the business state final |

The critical question is where ownership or externally visible state changes, not how many coroutine functions exist.

## Anti Pattern Registry Table

Registry rows generate hypotheses, not conclusions. Check the exception column: a target convention is not unsafe merely because it resembles a label. Apply the replacement at the narrowest owned boundary, and do not replace one unverified fashion with another. Each finding needs a code or test signal, a containment, an owner and a gate to rerun. Record a counterexample where the detector should stay silent. Severity follows false-negative risk, not aesthetics.

### Kotlin constructs

| Hazard | Lost contract | Safer default and bounded exception | Detection and proof |
| --- | --- | --- | --- |
| `!!` on an uncertain path | A distant null failure after boundary context is lost | Parse once; typed failure or deliberate `T?`. An adjacent proven invariant may justify the assertion | Trace the origin; null and malformed fixtures; boundary outcome |
| Broad `lateinit` | Temporal state, races, uninitialized or stale values at teardown | Constructor injection, explicit lifecycle nullable state, delegated validation, narrow framework binding | Map writers, readers, threads and lifecycle; negative access tests |
| Java platform type in the domain | Hidden nullability spreads assertions and defensive branches | Adapter exports `T`, `T?` or a typed failure; one reviewed shim may keep it temporarily | Inspect annotations and inferred types; nullable fixture; prove no leakage |
| `GlobalScope` or detached work | Lifetime, cancellation, failure, cleanup and shutdown ownership | Caller, structured or lifecycle scope. A process-lifetime exception needs a supervisor, shutdown, durable state, telemetry and an owner | Trace the job parent; cancel the owner; assert termination and cleanup |
| Broad `catch (Exception)` in suspend work | Cancellation becomes failure, fallback or retry | Catch and rethrow `CancellationException`, then translate known failures | Deterministic parent cancellation; cleanup; no fallback |
| Opaque nested `let`/`also`/`apply`/`run` | Receiver, return, mutation, null branch and exception point are hidden | Named locals, guards, extraction, or one clear scope function | Review receiver, return and side effects |
| Nullable field state collapse | Null merges absent, invalid, forbidden, unknown, not-loaded and failed | Value object, enum, sealed state, or value plus explicit status; null only if all callers act identically | Enumerate caller actions; exhaustive, serialization, persistence and branch tests |
| Data class for an identity-heavy entity | Generated equality, hash, copy and `componentN` conflict with identity, proxy, lifecycle and invariants | Plain class, explicit equality, immutable value, or framework model | Equality before and after the identifier, collections, copy, persistence, proxy and destructuring tests |
| Hidden blocking in `suspend` | Constrained threads starve; cancellation may only stop waiting | Named blocking API or owned dispatcher with bounded concurrency; no switch for a genuinely non-blocking API | Dependency inspection, execution context, cancel versus interrupt, load and saturation measurement |
| Boolean outcome erasure | True and false hide rejection, absence, conflict, retryable and terminal failure | Named enum, sealed outcome, value or typed exceptions; boolean only for an obvious private predicate | Inspect all callers and recovery actions |
| Mutable global singleton | Hidden dependencies, test leakage, races, unclear reset and shutdown | Constructor, lifecycle, request or session injection, or an owned synchronized cache | Reordered, parallel, race, reset and shutdown tests; cache policy |
| Generic `Result<Any>` or broad `runCatching` | Expected failures, cancellation and defects become one channel | Narrow taxonomy and typed translation; preserve cancellation and defects | Cancellation and defect classification tests |
| Nullable-everything fields | The source's uncertainty becomes the domain's | Keep domain state non-null; contain uncertainty at the boundary (`KC1-02`) | Compare DTO and domain nullability |
| Catch-all that logs and continues | A cancellation leak | Rethrow-first shape (`KC1-10`) | Read each hit; a naive search overcounts valid rethrow-first catches |

Every row ends in one finding disposition: `confirmed_defect`, `conditional_hazard`, `bounded_exception`, `accepted_risk`, `not_applicable` or `blocked`. The states and the promotion rule are defined under the Kotlin quality evidence packet.

Root first. Prioritize the earliest loss of information or ownership, because a downstream fix alone is incomplete. Removing a downstream `!!` while platform types still spread only moves the crash. Adding `Dispatchers.IO` while the work is still detached hides saturation. Adding a sealed outcome while every caller maps it back to a boolean adds ceremony without preserving meaning.

Common compound chains, each corrected at its first link:

| Initial contract loss | Downstream chain | Root-first correction |
| --- | --- | --- |
| A platform type enters the domain | Repeated safe calls, then one `!!`, then a distant crash, then a generic retry | Normalize at the interop adapter and model the failure before any retry policy |
| A detached coroutine owns a blocking call | The caller completes, the work persists, the pool saturates, the failure has no destination | Restore the lifecycle parent, then make the blocking and concurrency policy explicit |
| A broad catch swallows cancellation | Timeout or cancel becomes a translated failure, then a fallback or retry, then a duplicate side effect | Rethrow cancellation before classifying retry and side effects |
| A nullable field hides load or failure state | The caller treats unknown as absent and overwrites data or suppresses recovery | Separate lifecycle state from the optional value and test the caller actions |
| A boolean result hides conflict | The caller reads `false` as retryable and repeats a non-idempotent operation | Introduce closed outcomes and tie each to an explicit recovery action |
| A mutable singleton contaminates tests | An earlier test leaves state, a later test passes or fails by order, the fix earns false confidence | Scope or inject the state, reset ownership, and randomize or isolate tests |

Tempting incomplete fixes, by area:

| Area | Earliest contract loss | Tempting incomplete fix | Root-first action |
| --- | --- | --- | --- |
| Platform nullability | Interop uncertainty leaves the adapter | Replace `!!` with `?: return null` | Decide and encode the boundary states before the value is exported to the domain |
| Cancellation | Parent control becomes an ordinary failure | Add another fallback or retry | Preserve cancellation before translating known failures |
| Identity | Value syntax is applied to a lifecycle object | Customize one equality test without defining identity | Name the identity and the framework or persistence contract first |
| Blocking | The suspend signature hides execution behavior | Add `Dispatchers.IO` and claim scalability | Identify the dependency's behavior and the execution owner, then measure capacity separately |
| Global state | Mutable lifetime and synchronization are implicit | Clear the singleton in one test teardown | Scope or inject the state and define its lifecycle and concurrency policy |
| Scope functions and booleans | Several failure states collapse into null or false | Add comments to the chain | Separate the steps and model the outcomes callers act on |

These cases share a mental model, not a helper library: locate the earliest loss of information or ownership, preserve the distinctions that change behavior, and prove the dangerous branch. Reuse a code abstraction only when several targets share semantics and lifecycle, not merely similar syntax.

### Framework and service design

| Anti-pattern | Signal | Safer default |
| --- | --- | --- |
| Execution-model mismatch | Blocking JDBC or JPA on a reactive or Ktor path | Keep MVC, or isolate the work with measured capacity |
| Hidden Spring proxy or constructor requirements | Final classes, self-invocation bypassing a proxy | Compiler plugins aligned with the Kotlin version; call through the proxy |
| Transport-only validation | Invariants only in annotations | Domain and application checks as well |
| Unstable error mapping | Exception names in responses; scattered mapping | One mapper, stable envelope |
| Long transaction | Remote I/O inside a transaction; locks and connections span slow I/O | Transaction around the service workflow only |
| Transaction in transport | A controller or route opens the transaction | Application service owns it |
| Uncontrolled Ktor plugin composition | Plugins installed by habit, order unexamined | Deliberate installation; plugin order is target-specific |
| Untested serialization or persistence of Kotlin types | Value or sealed types meet reflection, ORM or Java | Compatibility fixtures |
| Data-class entity | Equality or identity defects | Acceptable only after identity, proxy, lazy-loading and equality tests pass |
| Kotlin idiom over framework reality | Compiles, then reflection, ORM, serialization or proxy fails | Compatibility fixtures before broad use |
| Dispatcher magic | A dispatcher switch changes transaction behavior | One explicit adapter |
| Package-name architecture | Layers inferred from package names | Trace an actual request or job |
| Keyword mode selection | Every mode loaded because a word appeared | Select by changed behavior |
| Plan without target discovery | Remembered commands and versions | Inspect first |
| Migration as a file | A script with no compatibility plan | Treat as deployed behavior |
| Test by habit | Full startup or mocks everywhere | Boundary-first test selection |
| Arbitrary performance threshold | A number with no owner | Owner objective or no claim |
| Planned command reported as passed | No exit status | Report the real state |

Traps worth memorizing: constructor injection does not establish layer ownership; a suspend controller can block the event loop; Bean Validation is not stateful domain authorization; a slice is not full production wiring or security; the Ktor test host is not a container, proxy or live network; H2 is not dialect or migration proof; a retry without idempotency duplicates; readiness is not traffic capacity; a formatter and static analysis are not architecture; a dated summary of official guidance is not current compatibility.

### Testing

Block overbroad startup, excessive mocking, production-dialect substitution, real sleeps, shared mutable fixtures, happy-path-only contracts and nondeterministic data. Each finding needs an observable signal, the causal risk, a safer replacement, and a mutation or failure injection proving that the replacement catches the defect. Legitimate exceptions: a mock at a narrow provider boundary; full startup for wiring; an embedded dependency for portable semantics; a quarantined legacy fixture with a focused characterization test. Detect by scanning annotations and sleeps, shuffling or parallelizing tests, injecting duplicate and timeout failures, comparing critical SQL with the production dialect, and requiring each suppression to say why it is safe.

### Security and resilience

Security: payload-derived identity or tenant; a coarse role instead of resource policy; an authentication-chain bypass; unstable error or enumeration details; CSRF disabled under ambient cookies; raw credentials, signatures, tokens, sessions or provider errors in diagnostics; inconsistent validation; swallowed cancellation; detached request work; blocking starvation; mismatched pools; nested deadlines that exceed the parent; supervision without outcome ownership.

Resilience: deterministic retry; synchronized retry storm; check-then-insert replay race; a separately reserved idempotency key that strands work; a response lost after commit; a remote effect inside an uncertain local transaction; expired replay retention with no late policy; applying events in arrival order; acknowledging in-memory work; unrecoverable claims; aggressive reclaim without fencing; a poison-message hot loop; unsafe stale or write degradation; telemetry overload or silence; incompatible rollout state; recovery starved by live traffic; partial credential rotation.

Reject a change when: a valid principal reaches another tenant; a token appears in an exception log; a broad catch consumes cancellation; a blocking call occupies a constrained event loop; a timeout duplicates a write; a raw provider exception leaks; the process dies after reporting success and before anything owns the work; or a faster candidate omits authorization or error handling.

### Runtime operations

| Anti-pattern | Safer default | Gate | Exception |
| --- | --- | --- | --- |
| `secret_bearing_diagnostics` | Model sensitive values separately, redact by construction, test failure rendering | Inject recognizable non-production canary values and scan every emitted surface | None |
| `telemetry_without_decision` | The smallest bounded signal that distinguishes a consequential state and maps to an owner action | Name the decision and the consumer | Temporary exploratory instrumentation with an expiry |
| `unbounded_signal_dimensions` | Bounded dimensions, sampled detail, correlation identifiers | Review labels for request values, identifiers, stack text and user-controlled data | Bounded tenant or operation dimensions when scale, privacy and backend limits are measured |
| `process_alive_as_readiness` | Define readiness from traffic semantics and only the dependencies needed to serve | Delay or fail each critical startup condition and observe readiness and real request behavior | A dependency-free service |
| `dependency_failure_as_liveness` | Reserve liveness for local unrecoverable states; report dependency degradation through readiness, status and signals | Slow a downstream and confirm no restart storm | A locally wedged client when restart is the proven recovery |
| `empty_database_migration_confidence` | Migrate from supported prior states with representative data, production dialect, invalid legacy rows, mixed versions and partial failure | Run the migration against those states | An initial unreleased schema |
| `single_step_breaking_schema_change` | Expand, migrate or backfill, observe, switch, contract | Run old and new versions against each intermediate state | A coordinated offline migration with exclusivity, bounded downtime, backup and recovery authority |
| `startup_coupled_unbounded_migration` | A single-owner migration mechanism with ordering, timeout and observability | Start several instances against a pending change | A small idempotent initialization |
| `green_pipeline_wrong_claim` | Map each requirement to the earliest reliable gate | Break the changed behavior on purpose and confirm the intended stage fails on the same artifact | A later scheduled gate owns expensive evidence when policy contains the risk |
| `rebuild_per_environment_promotion` | Build once; promote an immutable identity with validated environment-specific configuration | Compare digest and provenance | None |
| `permissive_container_by_default` | Minimal runtime contents; only the required user, files, ports, capabilities and network | Test read-only and restricted execution and the required write paths | None |
| `rollout_without_stop_authority` | Define stage, observation window, decision signals, stop conditions, authority and recovery before traffic changes | Exercise the stop | None |
| `shutdown_as_process_exit` | Stop admission, propagate cancellation, drain bounded in-flight work, release resources, persist durable identity, reconcile on restart | Send termination during each work phase | Stateless handlers with no external effects |
| `detached_background_coroutine` | Explicit scope, supervisor policy, durable identity when needed, observable completion | Cancel the owner and assert termination | Process-lifetime maintenance work in an application scope with an explicit lifecycle and failure policy |
| `retry_without_effect_identity` | Classify, bound under the total deadline, and use a stable effect identity or a compensating workflow | Inject a timeout before and after the external commit, retry, and verify final state and duplicates | Read-only or provably idempotent operations need only bounded backoff and cancellation |
| `stacked_timeout_budget` | Derive nested deadlines from the accepted request or job budget | Slow DNS, connection, response, processing and shutdown phases | None |
| `rollback_word_as_recovery` | Choose rollback, roll-forward, repair, replay or containment from the actual state transition; rehearse after partial progress | Rehearse | Code-only stateless releases with immutable prior artifacts |
| `checklist_without_scenario` | Convert high-consequence answers into target locators, executable scenarios, stop conditions and runbook actions | Run one scenario | None |

Good use of the registry: a worker loses jobs at termination, so detached coroutine, retry without effect identity and shutdown as process exit become three hypotheses to test. Bad use: a reviewer rejects one raw configuration read inside an adapter that validates once and injects a typed object.

## Verification Gate Command Set

A gate is evidence for one bounded claim only when these are known: the requirement and the failure it guards; the revision, configuration, dependencies and artifact; the task definition including filters and exclusions; the environment, fixture and data state; the expected negative observation; the actual action, exit status and output; the stronger claim it does not establish; and the owner and invalidation condition. Command familiarity is not evidence. A broad build can omit integration, migration, image and deploy checks. A focused test can use the wrong engine or fixture.

### Discovery

```bash
rg --files -g 'build.gradle*' -g 'settings.gradle*' -g 'gradle.properties' -g 'gradlew' -g 'pom.xml' -g 'mvnw'
rg 'kotlin|jvmToolchain|languageVersion|apiVersion|ktlint|detekt|kotest|junit|mockk|turbine|kotlinx-coroutines-test' .
```

### Repository-native gates

```bash
./gradlew test
./gradlew build
./gradlew detekt
./gradlew ktlintCheck
./mvnw test
./mvnw verify
```

### Focused gates

```bash
./gradlew :module:test --tests 'package.ClassName.testName'
./mvnw -pl module -Dtest=ClassName#testName test
```

### Candidate scans

```bash
rg -n '!!|lateinit|GlobalScope|catch\s*\(\s*(?:[A-Za-z_][A-Za-z0-9_]*\s*:\s*)?Exception' src
rg -n 'withContext\s*\(\s*Dispatchers\.IO|runCatching|object\s+[A-Za-z_][A-Za-z0-9_]*' src
rg -n '\.let\s*\{|\.also\s*\{|\.apply\s*\{|\.run\s*\{' src
```

### Gate profiles

| Change | Gates |
| --- | --- |
| Pure Kotlin | Compile, unit, static analysis if configured, traceability |
| Configuration syntax | Build only |
| Spring endpoint | Slice first; full context only if wiring, configuration or filters matter |
| Ktor route | `testApplication`, plus real dependencies and a smoke check when the change crosses them |
| Persistence or migration | Production dialect, transactions, supported schema states, rolling compatibility, recovery |
| Client or worker | Cancellation, deadlines, retries, idempotency, restart, metrics, bounded concurrency |
| Auth | Allowed, unauthenticated, denied, malformed, expired, enumeration, CSRF, secrets |
| Hardening | Only the gates the target makes relevant |

Gate families for security and resilience: parser and domain property tests; real security-chain route tests; persistence, transaction, uniqueness and concurrency tests; coroutine fake-time and cancellation tests; provider fault fixtures; worker restart and redelivery tests; load, saturation and recovery; a redaction audit of logs, metrics and traces.

Falsifying fixtures: a cross-tenant request discloses nothing and causes no effect; the parent is cancelled during every suspension and transaction phase; concurrent duplicates race against real persistence behind a barrier; the worker is killed at each claim phase; a mixed-version rollback preserves replay and state semantics.

### Rules

- A test should fail for the expected reason before implementation and pass afterward.
- Record command, working directory, exit status, test identifiers, exclusions, dependency availability and unavailable gates.
- Outcomes are pass, fail, blocked, unavailable, not applicable or expected external red. Evidence states for a plan are planned, running, passed, failed, skipped, blocked and not applicable. A planned gate is never reported as passed.
- Verification crosses the same six boundaries as the request. Unit tests suffice for a pure value object, not for its adapters. Mocks can hide serialization and transaction behavior. Test profiles, virtual time, rollback semantics and migration ordering matter.
- Minimum evidence by claim: source plus a boundary test for platform types; compile plus branch tests for closed states; a deterministic cancellation test; dependency inspection plus a boundary test for blocking; identity and persistence tests for entities; the real wrapper gates; a controlled runtime measurement for any production-impact claim.
- Evidence is insufficient when the framework or version is unknown, requirements are unobservable, blocking or cancellation is unresolved, a write can duplicate, denied paths are absent, migration compatibility is unknown, or release stop and recovery have no owner. Stop and repair the earliest contract.
- Beware relative-path drift, shell globbing and a global Gradle or Maven standing in for the wrapper.
- Never run destructive fault injection against shared or production systems without authorization, isolation, monitoring and a recovery path.

## Failure Mode Table

Classify a failure by its earliest causal boundary and contain it there. Name the earliest observed contract violation, not the loudest symptom. No likelihood or severity numbers are assigned here: without calibrated data, prioritize by consequence, irreversibility, recurrence, exposure, detectability and recovery cost.

### Kotlin code

| Failure | Signal | Correction |
| --- | --- | --- |
| Platform null crash | Null failure far from the Java call | Normalize in the adapter; nullable fixture |
| Null-policy collapse | Callers branch on one null for different reasons | Explicit states |
| `lateinit` race | Access before initialization or after teardown | Constructor or lifecycle ownership |
| Data-class identity corruption | Entity vanishes from a set after its identifier is assigned | Explicit identity; equality tests |
| Boolean ambiguity | Callers cannot tell rejection from failure | Typed outcome |
| Detached work | Work continues after the caller is cancelled | Structured scope |
| Swallowed cancellation | Fallback or retry runs after cancellation | Rethrow first |
| Unaccounted supervision | A child fails and nobody observes it | Own every result |
| Flow lifetime leak | A cold or shared collection, a buffer or a callback outlives its consumer: producers continue, buffers grow, callbacks leak, cancellation does not propagate | Define producer, collector, sharing, buffer, completion and cleanup ownership; prove release with collect, cancel, fail and restart scenarios. An application-wide stream may be long-lived under explicit lifecycle management |
| Dispatcher starvation | Latency rises with blocked threads | Bounded owned dispatcher or blocking design |
| False confidence from `Dispatchers.IO` | A switch is cited as capacity | Measure; bound the queue |
| Mutable-global leakage | Tests pass alone, fail together | Scoped injection, reset |
| Opaque partial side effects | A chain half-completes | Named steps and outcomes |
| Generic result capturing defects | Cancellation or a bug is returned as a value | Narrow taxonomy |
| Fixture missing the dangerous branch | Green tests, defect remains | Test the consequential distinction |
| Gate population gap | The analyzer did not cover the changed files | Record the population |
| Invented toolchain | A task was assumed to exist | Discover first |
| Hidden external red | Someone else's failure is not reported | Attribute and report it |
| Half-translated migration | Old and new shapes coexist with no shim | One compatibility translation |
| Incompatible persistence rollback | Old code cannot read new rows | Staged compatibility |
| Missing data rendered as zero | Dashboard shows healthy | Explicit unknown state |
| Runtime claim from a local test | "Fast" from a unit timing | Controlled experiment or no claim |
| Ownerless recovery | Nobody can resume | Name the owner and resume condition |
| Colliding workers | Two editors change one contract | One owner per shared file |

Recovery sequence: signal, preserve identity, classify and contain, test the hypothesis, repair the earliest loss, run focused recovery, verify integration and operation, update records. A mitigation is incomplete until the caller outcome, side effects, jobs, persisted and shared state, resource queues, telemetry and the ability to resume are verified. Promote a shared helper or analyzer rule only for a recurring, shared or high-consequence mechanism, and remove noisy or redundant controls.

### Review process

| Failure | Signal | Mitigation |
| --- | --- | --- |
| Rows skimmed on a large diff | A boundary diff has no findings | Split the review; audit zero-finding records. Zero findings often means an unread diff |
| Exception drift | A finding contradicts a stated exception such as the `lateinit` lifecycle allowance | Cite the clause. Over-strict review blocks legitimate code and erodes trust |
| Search trusted without reading | Unresolved scan hits | Read each hit; separate rethrow-first catches and fixtures |
| Score treated as measurement | A score quoted as a defect rate | Label it author emphasis |
| Modes never chosen | Work starts with no mode | Surface before mode |
| Vague requirements | "Production-ready" with no criteria | Reject and rewrite |
| Silent migration | Dependency or plugin diff changes the stack | Audit build diffs, not only source diffs |
| Coroutine safety assumed | "It is a suspend function" | Cancellation and blocking tests |
| Guidance drift | Advice no longer matches the installed versions | Refresh, rerun local gates, mark stale claims |
| Generic advice | No command, reviewer question or metric attached | Block completion until one is |

### Framework and service

| Failure | Signal | Correction |
| --- | --- | --- |
| Spring self-invocation bypasses a proxy | `@Transactional` or security has no effect | Call through the proxy; integration test |
| Blocking on a reactive or Ktor path | Event-loop latency | Keep MVC or isolate |
| Remote I/O inside a long transaction | Connection pool exhaustion | Narrow the transaction |
| Incomplete Ktor status-page mapping | Raw exception in a response | Central mapper; negative tests |
| Java platform null | Null failure in a controller | Adapter |
| Mutable entity equality | Collection anomalies | Explicit identity |
| Request surge | Queues grow, timeouts rise | Rate limits, queue bounds, cancellation, rollback playbook |
| Security boundary fails silently | No denial tests | Abuse-case tests; deny by default |

Do not merely retry every timeout or raise the coroutine count. Reproduce the trigger, contain it, prove recovery, and set an expiry on temporary controls. A bad surge response raises the pool size, adds retries and rolls forward with no total deadline and no evidence of downstream capacity.

### Security and resilience

| Failure | Correction |
| --- | --- |
| Authentication bypass or misordered path | Test direct entry and filter order |
| Payload-derived tenant or role (confused deputy) | Resolve authority server-side |
| Coarse role | Resource policy |
| Error enumeration | Stable, non-revealing errors |
| Misclassified browser integrity | Decide CSRF from the real client context |
| Sensitive diagnostics | Redact by construction |
| Split validation | One owner for each layer's checks |
| Swallowed cancellation or detached work | Structured scope, rethrow |
| Blocking and pool mismatch | Match dispatcher bounds to the backing pool |
| Nested deadline | Derive from the parent |
| Unobserved supervised child | Own results |
| Deterministic retry | Classify |
| Retry storm | Jitter, budget, one retry owner |
| Check-then-insert race | Atomic uniqueness, lock or state machine |
| Stranded reservation | Transactional coupling, or an in-progress lease with recovery |
| Lost response after commit | Replay lookup |
| Remote effect inside an uncertain transaction | Outbox or reconciliation |
| Replay retention expiry | Late-replay policy |
| Out-of-order event | Sequence, version or state-machine checks |
| In-memory acknowledgement | Durable acceptance first |
| Abandoned or aggressively reclaimed claim | Lease with fencing |
| Poison hot loop | Parking or dead-letter |
| Unsafe degradation | Fail safe unless policy approves the fallback |
| Telemetry overload | Bounded signals |
| Mixed rollout or configuration rotation | Compatibility across versions |
| Recovery starved by live traffic | Reserved or fair capacity; monitor the oldest work |

### Runtime operations

Each row is a hypothesis to test, with evidence, a containment question, a durable correction and a recovery proof.

| Failure | First question |
| --- | --- |
| `wrapper_or_version_drift` | Did the build tool or a plugin version change |
| `missing_or_malformed_config` | Does startup stop safely before traffic |
| `secret_exposure` | Which sinks received it; rotate and investigate |
| `secret_or_identity_denial` | Is the workload identity correct |
| `authorization_or_input_boundary_failure` | Which boundary accepted it |
| `dependency_latency_or_outage` | What is the accepted degraded behavior |
| `retry_amplification` | How many attempts per logical operation |
| `pool_or_resource_exhaustion` | What holds the resource |
| `telemetry_blindness_or_corruption` | Is there an independent state source |
| `unbounded_or_sensitive_telemetry` | Which label is unbounded |
| `readiness_false_positive` | Was traffic sent before the service could serve |
| `liveness_restart_amplification` | Is a healthy instance being restarted |
| `historical_data_incompatibility` | Which rows violate the new invariant |
| `partial_or_contended_migration` | What is the actual schema state |
| `wrong_or_mutable_artifact` | Does the running digest match the tested one |
| `package_permission_or_runtime_mismatch` | Which path, user or port is missing |
| `CI_gate_no_op_or_wrong_scope` | Did the gate run any tests |
| `staged_rollout_regression` | Who can stop it |
| `lost_or_duplicate_worker_effect` | Where did ownership change |
| `shutdown_deadline_or_drain_failure` | What was in flight |
| `ambiguous_external_commit` | Can it be reconciled by identity |
| `recovery_action_incompatible` | Is prior code compatible with current data |
| `correlated_platform_or_provider_failure` | Is this incident command's call |

Failures interact. A dependency slowdown can consume pools, trigger retries, fail readiness, induce liveness restarts, overload telemetry and create shutdown ambiguity. Raising a timeout or a resource limit may only move the bottleneck. Migration contention can delay startup, fail readiness, cause replacement loops and make rollback incompatible. Telemetry loss can make a stopped alert look like recovery. A wrong artifact plus configuration drift can mimic a code defect. Other correlated sets: cancellation plus late commit plus client retry gives a duplicate; backlog plus shutdown plus redelivery; stale guidance plus green tests.

Incident response: establish authority and protect people, data, credentials and evidence; record current and prior states; classify the earliest supported break; if telemetry or health automation is the suspect, confirm from an independent source; contain only under authorization; choose recovery from the actual partial state; verify recovered business invariants, not merely process health; hand off residual risk.

Recovery decisions:

| State | Decision |
| --- | --- |
| Code regression with unchanged, compatible data | Rollback may be viable |
| Compatible schema expansion, new code fails | Roll back the code, keep the expansion |
| Partially applied data transformation | Evaluate roll-forward, repair or containment before rollback; reject rollback if the inverse is lossy |
| External effect may have committed after a timeout | Reconcile before replay |
| Wrong artifact promoted | Stop and restore the intended artifact path |
| False readiness routes unsafe traffic | Remove or hold traffic and correct the health contract; do not restart if that would amplify |
| Worker drain deadline expires | Stop intake, preserve unfinished identities, use source recovery or reconciliation |

## Workload Model

Workload is the unresolved decision surface, not a count of requirements, pages or lines. Requirements are the splitting currency: split when the requirement list cannot be verified by one owner in one coherent pass.

### Units

- One work packet per classified surface, with one fixed mode set.
- One service boundary and one release objective per batch. Batch only when contracts, persistence, execution model, owner and rollback are shared.
- One diff per review record, with applicable rows fixed at scoping and one verification owner. Boundary-touch count, not line count, is the size signal. A short adapter can carry more risk than a long rename. Split when a diff touches more than a handful of distinct boundaries.
- One protected transition with one accountable owner for security and resilience work.

### Inherited planning heuristics and what selects each position

Two positions exist and both are kept:

| Position | Statement | Applies when |
| --- | --- | --- |
| Numeric prompt | One service boundary, up to 25 endpoints or workers, 1,000 representative requests and one deploy rollback path per review batch; one packet with at most 20 requirement identifiers, one matrix and one command set | As a prompt to ask "should this be split?" when nothing better is known. These figures are unmeasured and uncalibrated. They are not throughput, capacity or completeness guarantees |
| Coherence test | No endpoint, file, request, service or owner count is universal | Always, as the deciding test. Split by independent outcomes, ownership, artifacts, state, evidence fidelity and recovery decisions |

Five routes that share one command and one transaction can fit in a batch; twenty-five unrelated workers cannot. A thousand happy requests do not cover invalid, duplicate or cancellation paths. Split when ownership differs, when the sample lacks concurrency or tail representativeness, when rollback requires data repair, or when event-loop and blocking workloads mix.

### Dimensions

Ingress count; state and action complexity; caller and API breadth; identity and persistence coupling; lifecycle and coroutine edges; blocking and concurrency edges; framework and generated surface; owner count; evidence availability; gate cost and duration; reversibility; shared writes. One hidden blocking call can dominate many isolated nullable fields.

### Paths

| Path | Exit |
| --- | --- |
| Compact | Semantic closure of one private distinction |
| Standard | Integration closure across callers |
| Characterization | A selected contract after behavior is pinned |
| Migration | Staged integration |
| Incident containment | Stabilization |
| Routed | Returned authority |

Narrow a large task by one ingress path, adapter containment, characterization, disjoint owner shards, stratified samples, automated candidate scans with manual classification, or one specialist claim.

### Runtime and test workloads

For a runtime claim, define logical operations separately from physical attempts; the mix of valid, invalid and duplicate work; and keys, tenants and skew. The correctness oracle counts offered, admitted, rejected, cancelled and queued work, terminal outcomes, durable effects, duplicates, unknowns, unfinished work, claims and leases, and telemetry gaps.

For tests, model case count, state cardinality, parallel workers, real dependency instances, setup and teardown, virtual-time needs, cleanup and resource saturation. Split by transport, persistence, coroutine and adapter. Shard integration tests, serialize scarce infrastructure, and use property tests to reduce combinations.

Runtime work profiles: focused configuration change; signal change; schema and data rollout; container and platform change; worker lifecycle; CI and release change; production hardening, which inspects every region and then prioritizes by consequence and causal dependency.

## Reliability Target

Reliability is bounded prevention, detection, containment, recovery and learning for a named population. This skill sets no service objective. Do not fill a target with plausible percentages or deadlines. If the owner has not set a value, keep it unresolved and state which claim it blocks.

### Hierarchy

1. User or operator outcome.
2. Hard invariant.
3. Measured objective.
4. Degraded contract.
5. Component indicator.
6. Recovery contract.
7. Evidence and coverage.

### Hard controls for delivery

Traceability, stable error mapping, explicit transaction scope, named blocking, bounded calls, retry classification, idempotent writes, migration compatibility, deny-by-default security, observability and rollback. Zero uninvited framework migrations: audit dependency and plugin diffs, not only source diffs.

### Hard invariants for Kotlin changes

- Every consequential claim has support, a limit and a verification, or is marked blocked or no-claim.
- Evidence boundaries are preserved.
- No unsupported production, security, latency or capacity claim.
- Confirmed findings are disposed.
- Every changed suspend path preserves or owns cancellation.
- Platform uncertainty is contained.
- Every blocked, failed or avoided state names a recovery route, owner and resume condition.

"Every changed applicable suspend path" is auditable. "All Kotlin coroutine code is reliable" is not. "99 percent coroutine reliability" is a bad target: it has no population, event, measurement, owner or response. "Startup succeeds almost always" is a bad configuration target: it has no artifact, profile, attempt definition, missing-secret treatment, restart-loop guardrail or output-safety invariant.

### Sentinel events

Each of these is a defect regardless of any aggregate: platform escape; swallowed cancellation or a side effect after cancellation; hidden blocking degradation; identity corruption; mutable leakage or race; gate population mismatch; an unsupported production, security or performance claim; ownerless recovery.

### Inherited audit targets

These are acceptance targets for the guidance itself. None has been measured or achieved, and none is a statistical guarantee:

- 100 percent of recommendations keep the owner-doctrine, external and inference boundaries visible.
- At least 18 of 20 sampled uses reach the correct adopt, adapt, avoid or hand-off decision. The 18 of 20 figure is an illustrative sample, not a probability or an acceptance threshold for services.
- Zero unsupported production, security, latency or reliability claims.
- Every avoid or failure case names a rollback, escalation or next route.
- Per merge window: 100 percent of boundary-touching diffs have a review record, and zero merged broad catches around suspend work fail to rethrow cancellation. These are unbaselined binary targets; the first window only establishes feasibility. Syntax-aware review is required, because a naive search overcounts valid rethrow-first catches.

### Objective qualification

Define attempt, success, failure, duplicate, cancelled, maintenance and recovered. Preserve retries and partial attempts instead of counting only final successful responses. Segment. Missing telemetry is unknown or failure by policy, never silently excluded. Include recovery work done after the service returned. Examine correlated failures; independence assumptions mislead. A target moves through proposed, baselined, accepted, observed pass or observed violation, and superseded or retired.

### Evidence tiers

| Tier | Establishes | Does not establish |
| --- | --- | --- |
| `deterministic` | Logic under controlled inputs | I/O, framework and distributed failure |
| `real_boundary` | Behavior against a real dependency or dialect | Packaged and platform behavior |
| `packaged` | The built artifact starts and behaves | Platform traffic and rollout |
| `staged_platform` | Behavior under platform automation | Every environment; it is stronger but noisy |
| `incident_or_production_observation` | What happened in that case | Other cases; it is real but confounded |

Use the lowest tier that can falsify the claim. Confidence rises per bounded claim and environment, never as a universal percentage. Do not combine tiers into one number.

Acknowledgement semantics have to be precise: completed effect, durable acceptance or volatile scheduling. A performance change fails if the speed weakens authorization, durability, cancellation, observability or effect integrity.

## Retry Backpressure Guidance

Default: no automatic retry until the operation, failure class, total deadline, repeat-effect semantics, capacity, cancellation and owner are known. Retry changes when work happens. Backpressure changes whether and where work waits, fails, sheds or transfers ownership. They share one capacity budget.

An error label alone is not classification. The same timeout can occur before connection, during processing, after an external commit, or while telemetry is delayed.

### Failure classification

| Class | Default | Retry valid when | Main risk |
| --- | --- | --- | --- |
| `invalid_request_or_domain_state` | Fail | Never unchanged | Wasted load |
| `missing_or_malformed_config` | Stop startup | Never | Restart loop |
| `denied_permission_or_identity` | Stop; route to security or platform | Never | Lockout, noise |
| `unsupported_version_or_contract` | Stop; select a compatible artifact | Never | Corruption |
| `deterministic_implementation_defect` | Fail and fix | Never | Hidden defect |
| `optimistic_concurrency_conflict` | Refresh state and reconsider | Safe to recompute, bounded, deadline remains | Starvation, lost update, hot-key contention |
| `transient_connection_setup` | Retry within the total budget | Budget remains | Synchronized connection storm |
| `explicit_rate_or_quota_limit` | Respect provider policy; reduce admission; defer or fail | Per provider policy | Starving tenants |
| `dependency_unavailable` | Bound or shed; accepted degradation or durable handoff | Per degraded contract | Amplified outage |
| `timeout_before_known_effect` | Retry may be considered | Effect provably did not start | Misclassified ambiguous commit |
| `timeout_with_ambiguous_effect` | Ambiguous state; reconcile before replay | After reconciliation | Duplicate effect |
| `cancellation_or_shutdown` | Propagate, preserve durable state, release resources | Never in the cancelled scope | Work after abandonment |
| `capacity_or_pool_exhaustion` | Reduce admission and concurrency | Capacity is available and the retry does not recreate the wave | Overload wave |
| `data_or_migration_failure` | Stop mutation; route to the data owner | Only through a verified resumable or idempotent step | Partial state |
| `stale_external_evidence` | Refresh once | One bounded refresh | Retrying toward a preferred answer |
| `missing_context_or_owner` | Pause with a precise handoff | After the owner answers | Guessing |
| `telemetry_or_gate_inconclusive` | Repair the evidence system | After the premise changes | Rerunning tests until one passes |

### Retry contract

Define before enabling:

1. The operation and its stable identity.
2. Eligible and ineligible failure classes.
3. The effect boundary, and whether it is idempotent, deduplicated, transactional or reconcilable.
4. The outer deadline, the cancellation source and the remaining budget.
5. Which layer owns the retry, so nested libraries, proxies, queues and workers do not multiply attempts invisibly.
6. The attempt limit, from target policy and measured workload, not copied.
7. Delay and dispersion.
8. Admission, concurrency, pool, queue and downstream limits.
9. Per-attempt and total-work signals.

Count total work across gateway, client, message source and worker. Measure attempts separately from operations and preserve the original failure. If a retry lacks idempotency, a timeout budget or classification, redesign: queue and drain for non-idempotent work, or a circuit breaker where downstream health is observable. Backoff utilities are an option only after coroutine semantics are verified. Redesign when retries mask non-idempotent work.

### Backpressure options

| Option | Obligation it adds |
| --- | --- |
| `fail_fast` | A clear caller contract |
| `admission_limit` | A rejection response |
| `concurrency_limit` | Sizing against real downstream capacity |
| `bounded_memory_queue` | It is volatile and lost at exit |
| `durable_queue_or_store` | Durability, age, shutdown and poison handling |
| `load_shedding` | A fairness policy |
| `degraded_response` | An accepted correctness, security and freshness contract |
| `circuit_or_dependency_guard` | Probe policy, shared state, false opening, synchronized recovery |
| `durable_handoff` | An owner on the other side |
| `reconciliation` | A stable identity to reconcile by |
| `operator_hold` | Someone authorized to release it |

A queue does not remove load; it moves load into the future. Bound backlog, age, item size, attempts, retention, poison work and drain rate. State the overflow behavior and how recovery avoids a second surge. A fallback is not automatically safer than failure: a stale or partial response needs an accepted contract, and a fallback that calls another shared dependency can move or amplify the outage.

### By plane

- **Request and client.** Derive inner connect, read, processing and retry budgets from the end-to-end deadline. Classify connect failure, explicit refusal, partial response, rate limit, timeout, cancellation and ambiguous commit separately. After recovery, verify that attempt rate and queued work subside.
- **Worker and broker.** Stable identity. Bound active workers against real resource and downstream capacity. Avoid an unbounded coroutine launch behind a bounded source poll. Treat retry, redelivery and restart as one attempt model. Do not acknowledge before the required durable state. Do not hold ownership beyond a useful deadline. Poison work goes to a terminal, quarantined or owner-review state with sensitive-data controls.
- **Persistence.** Retry only a known rollback-safe class with no external effect inside the transaction.
- **Migration.** Not an ordinary retry. Confirm whether the step is transactional, idempotent, resumable, partially applied, lock-holding and compatible with old and new artifacts. Inspect the actual state before repeating a failed data mutation.
- **Release.** Pause progression when a mapped gate, signal, identity or compatibility condition fails, and restart from the earliest invalidated gate.
- **Tests and tools.** Rerun only after a premise changes. A diagnostic rerun varies one controlled factor. Never retry toward a preferred answer.
- **The work itself.** Stop starting new work when a gate is red and repair the earliest incomplete boundary. Stop-work triggers: unresolved identity, a red structural gate, an owner block, a shared-edit collision, a new root hypothesis, context drift, an unattributed external red. On long tasks, re-read the requirements before a broad rewrite or a destructive action. One owner per shared file.

### Verification scenarios

| Scenario | Hidden failure to look for |
| --- | --- |
| Invalid input | The caller or gateway silently retries |
| Transient connect failure | A synchronized attempt wave after recovery |
| Timeout with ambiguous effect | A duplicate effect masked by a final success |
| Dependency outage | Liveness restarts, or a fallback overloads another system |
| Rate or quota limit | Queued work expires, or one tenant starves others |
| Worker termination | Lost or repeated work |
| Poison work | Infinite redelivery, or a sensitive payload in diagnostics |
| Recovery wave | The retry surge begins only after the dependency returns |

Fixtures for the code: cancel after call entry and assert no retry and no side effect; repeat a deterministic rejection and assert exactly one attempt; a classified transient sequence with a budget and deadline; a duplicate unsafe write; a constrained resource with admission; alternating flaky outcomes.

The bad case in one line: a write times out after the provider may have committed, the client repeats without an effect identity, the final call succeeds, and the metrics look healthy while two external effects exist.

## Observability Checklist

Begin with a failure or recovery decision. Pick the smallest bounded signal set that distinguishes the state and leads a consumer to an action. Percentiles, counts, dashboards and alerts are not mandatory by category. A tiny service may omit tracing, but it keeps structured outcomes and saturation. If a signal has no consumer or action, question whether it should persist.

### Signal contract

For each signal, record: the decision question; the state and event; source and owner; artifact and configuration identity; dimensions; the sensitive-data boundary; temporal semantics; retry and work semantics; emission path; delivery path; retention and cost; consumer and query; action and authority; behavior when telemetry is missing or degraded; an independent confirmation; a verification scenario; compatibility and consumers; invalidation and retirement. Treat signals as operational APIs: version them, inventory consumers, keep compatibility.

### Choosing a signal type

| Type | Choose when |
| --- | --- |
| Structured event or log | A bounded narrative of one operation is needed |
| Metric | A low-cardinality aggregate drives an alert or a trend |
| Trace | A sampled path across boundaries explains latency or failure, and the platform supports propagation |
| Audit event | Someone must later prove who did what |
| Health state | Automation makes a traffic or restart decision |
| Work or effect ledger | Each item's ownership and effect must be reconstructable |
| Direct database or broker state | An independent source is needed to confirm telemetry |
| Profile or sample | A measurement needs explaining |
| Synthetic or direct probe | The user-visible path must be checked from outside |
| Runbook decision log | Operator actions need to be reviewable |

Duplicating the same unqualified state across logs, metrics and traces does not create independent evidence.

### By boundary

| Boundary | What the signals must answer |
| --- | --- |
| Build and artifact | Which revision and digest is running |
| Configuration | Which validated profile is effective, without printing secrets |
| Secrets and identity | Was access denied, expired or rotated |
| Requests and routes | Outcome code, error class, latency by bounded route name |
| External calls | Dependency, attempt, timeout, retry, final result |
| Persistence | Transaction result, pool wait and saturation, conflict |
| Migration | Version, phase, duration, partial state |
| Queues and workers | Depth, age, lag, attempts, terminal and parked outcomes, abandoned-claim recovery |
| Resource and capacity | Dispatcher and pool active and queued counts |
| Health and traffic | Why readiness changed |
| Rollout | Cohort, stage, stop trigger |
| Shutdown | Drain start, in-flight count, deadline expiry |
| Recovery | What was reconciled and what remains unknown |

### Fields for the service

Controlled-cardinality requirement or operation identifiers; route or worker; outcome code; latency; error class; transaction result; dispatcher or pool; dependency timeout and retry; queue depth; saturation; migration version; health; rollout cohort; rollback trigger.

Security signals: denied-operation effect violations; bounded authentication outcome mix; cross-tenant denial evidence; throttle outcomes on sensitive flows; a synthetic secret absent from responses, logs, traces, labels and error reports; drift in the external error contract.

Resilience signals: retry amplification (dependency attempts per logical operation); deadline consumption; unknown-commit count; duplicate decision mix; duplicate-effect violations; cancellation cleanup; blocking saturation; durable work age and lag; worker attempts and terminal outcomes; abandoned-claim recovery; dependency concurrency pressure.

Kotlin-level categories worth typing: platform null, cancelled by parent, known dependency failure, blocked, unknown population. Runtime dimensions: for cancellation, the scope, operation, source and cleanup; for blocking, the dependency, dispatcher, active and queued counts and duration under workload; for outcomes, the type, category and action; for state, the scope, reset and conflict; for retry, the class, ordinal, deadline, deduplication and stop reason; for migration, the old and new version, conversion and rollback.

### Privacy and cardinality

Use a controlled vocabulary for route, operation, result, dependency, artifact, version, work phase and recovery state. Never use raw URLs, request bodies, SQL, exception text, user or customer identifiers, credentials, tokens, arbitrary tenant strings, queue payloads, attempt identifiers or stack traces as metric dimensions. Redact passwords, authorization headers, tokens, sessions, reset material, signatures, raw bodies and sensitive payment or provider data. On a secret exposure, rotate or revoke and investigate every sink. On a denied-effect violation, contain and reopen the authorization and idempotency gates.

### Counting and time

Distinguish event time from collection time. Count original operations, individual attempts, final results, cancelled work, duplicates and reconciliation separately. Define whether a timeout is a failed attempt, an ambiguous effect or a final user failure. A request accepted for durable work is not the same as work completed. Keep artifact and configuration boundaries so a rollout mix does not look like one population. Report p50, p95 or p99 only with an adequate sample design; small samples may need raw ranges.

### Missing data

Distinguish observed zero, not applicable, not instrumented, collection degraded, unknown population and no claim. Never render missing data as a healthy zero. No alert or a zero count may mean healthy, low traffic, telemetry loss, sampling, a broken query or an unobserved attack. When telemetry is degraded, enter an explicit unknown state and never declare recovery from silence.

Watch the telemetry itself: emission failures and drops; exporter queue saturation; collector availability; trace propagation gaps and sampling changes; series and index growth; dashboard freshness; alert evaluation and delivery failures; paging gaps; discrepancies against independent state.

### Verifying signals

Emit synthetic success, denial, duplicate, transient, terminal, cancel, saturation and recovery cases. Verify the fields and the exclusion of secrets. Reconcile counts to durable effects. Interrupt telemetry and confirm that missing data is visible. Verify that success does not alarm, trigger each outcome, exercise the runbook, and observe cardinality and cost. Local tests cannot prove production delivery, retention, dashboard correctness or operator response.

A bad dependency signal: one `error_count` rises, exception text is a label, retries are counted as independent requests, and there is no artifact or dependency identity.

### Observability of the work

Keep the delivered packet, the modes, the traceability table, gate results and open questions with the change; a pull request description can carry them. For a review, keep the applicable rows, findings, scoped-out reasons, gate results, the proof command, the decision and the uncertainty next to the diff. Keep it small: a command-output summary, the changed-file list and unresolved-risk notes, not raw transcripts. Scoped-out rows matter, because they show what was not examined and may predict escaped defects.

## Performance Verification Method

Most semantic repairs need no performance claim. Record no claim. There is no universal Kotlin latency target.

### The latency fallback: two positions

| Position | Statement | Applies when |
| --- | --- | --- |
| Provisional diagnostic | With no owner objective, p95 under 200 ms and p99 under 500 ms may serve as a local diagnostic | Latency matters, the owner has set nothing, and the figures are labeled as unmeasured placeholders. They are never a service objective and never published as compliance. Replace them before deployment |
| No fallback | Those figures are unsupported and must not be used | No owner objective and no meaningful mechanism change: mark the claim not applicable with a reopen condition |

When the owner has an objective, use it and ignore both rows. Calling 200 ms a service objective is the bad case under either position.

### Preconditions

A target-owned objective, or a comparative hypothesis stated with "no objective pass will be claimed". Confirm the hard gates first. Record revision, wrapper, versions, artifact digest, JVM, architecture, configuration, topology and limits.

### Claim types

Request or operation latency; throughput and capacity; startup and readiness; dependency client; database and query; migration; worker and queue; resource efficiency; shutdown and drain; recovery; local allocation; build and gate cost; workflow effort. Do not collapse these into one score.

### Methods

Select the least costly method able to falsify the claim. Isolation diagnoses; integration accepts.

| Method | Supports | Cannot prove alone |
| --- | --- | --- |
| Static analysis | A hypothesis | Any runtime behavior |
| Deterministic timing test | A regression guard on logic | Production latency |
| Microbenchmark (harness, warm-up, dead-code resistance) | A local code-path comparison | I/O, framework, distributed behavior |
| Profiler or diagnostic sample | An explanation of a measurement | The measurement itself |
| Framework or component load | One component under load | End-to-end behavior |
| Database or broker integration | Real dialect, locking, delivery | Production data shape |
| Packaged process test | Startup and behavior of the real artifact | Platform behavior |
| Synthetic load or stress | Behavior under a modeled workload | Production capacity, unless distribution, environment and limiting resources are representative |
| Sanitized trace replay | Realistic mix | Future mixes |
| Sustained stability run | Leaks and drift | Peak behavior |
| Staged platform observation or canary | Behavior under real automation | Other environments |
| Analytical capacity model | A planning estimate | Anything, until measured |

### Kotlin and JVM controls

- State whether the measurement is cold startup, early warm-up or steady warmed. Class loading, JIT, caches and connection establishment differ.
- Record JVM options: memory, garbage collector, threads, container resource awareness.
- Observe garbage collection and allocation. Do not infer a cause from a pause or heap summary alone.
- Distinguish suspension from blocking. A coroutine-friendly API can still call blocking JDBC, filesystem, DNS, native or client work beneath it. Trace coroutine threads and align backing pools.
- Count cancelled work and released permits. Distinguish an asynchronous acknowledgement from a completed effect. Count every retry layer.
- Document clocks, histograms and instrumentation overhead.
- A thread switch may reduce event-loop blocking while creating an unbounded I/O queue.

### Execution

Freeze the workload hash, seed and data. Define a correctness oracle. Run a smoke test and a negative control. Make cold and warm explicit. Compare like artifacts, and randomize or alternate the order when drift could bias. Inject failures, overload and recovery. Repeat. Collect enough observations for the claimed statistic; do not report tail percentiles from a population too small or too censored to support them. Pace arrivals according to the model. Reconcile the aftermath. Observe recovery after pressure.

Measure end-to-end and boundary latency, throughput and errors, allocations, dispatcher and connection-pool saturation, dependency budgets, cancellation, and correctness under load. Record input size, concurrency, environment and versions, warm-up, sample, the statistics the owner requires, errors, saturation, retries, exclusions and the regression action.

### Interpretation

The median is typical behavior. A tail percentile is a qualified upper part of the distribution. The maximum depends on the sample. Averages hide multimodal behavior. Report counts, inclusion rules, missing observations, retries and cancelled operations. No particular percentile names are required. If the target requires p50, p95 or p99, record the population, window, estimator, sample sufficiency, missing-data behavior and the owner's threshold.

Misleading evidence: one-run percentiles, mocked dependencies, tiny data, cold caches, JIT and garbage collection effects, coroutine scheduling, coordinated omission, hidden retries, average-only or completed-only figures, uniform keys, closed-loop demand, disabled security, unit timing, `Dispatchers.IO` cited as capacity, unequal populations, one anecdote.

A performance improvement fails if it changes results, ordering, invariants, authorization or secret handling; loses or repeats work or effects; hides errors or disables signals; shifts latency into queues, retries, background work or another service; increases restart churn, migration risk or shutdown ambiguity; depends on a different artifact, a lower-fidelity fixture or a weaker gate; exceeds the cost budget; or harms fairness.

Correctness equivalence between baseline and candidate covers valid and invalid inputs, the state taxonomy, cancellation and cleanup, side effects, transactions, cache and order, failure and retry classes, and identity and persistence.

### Result states

| State | Meaning |
| --- | --- |
| Pass against objective | An owner objective was met under the recorded method |
| Comparative improvement | Better than baseline; no objective claimed |
| Characterization | A description, no judgment |
| Failure | Objective missed or a guardrail broken |
| Inconclusive | Degraded collection, unknown environment, incomplete samples or an inseparable confound |
| Conditional | Holds only under stated assumptions |

Abort a comparison on a correctness difference. Decisions after a result: retain, narrow, optimize, route, roll back, no action, no claim.

### Measurement record

Claim and owner; outcome and effect oracle; harness, version and tier; workload and faults; environment; sampling and analysis; results; guardrails; uncertainty; decision, rollback and invalidation.

### Review cost

Measure review minutes per record, applicable-row count, findings caught before merge, escaped defects attributed to skipped rows, and the direction of scan-hit counts. Record the duration at review time; reconstructed records inflate it. Handler latency is not proof that a checklist has value. An inherited sampling target says a reviewer should find the next action, the gate and the stop condition within ten minutes without reading unrelated files. That target is unmeasured and is not a service objective. A cost ratio from a sample of three is provisional.

## Scale Boundary Statement

Do not use endpoint count, request count, file count, service count or owner count as a universal threshold. Scale is the interaction among state independence, consequence, context, evidence fidelity and coordination. No size threshold has been measured.

### What this guidance covers

One bounded Kotlin backend outcome: one service boundary, one protected transition with one accountable owner, one integration owner who can trace and verify ingress, state, identity, lifecycle, blocking, mutable state and gate contracts. Kotlin on the JVM.

### Where it stops

- Multiple independent systems or more than one ownership boundary.
- Unbounded discovery.
- Production traffic with no owner objective.
- A public multi-consumer migration.
- Irreversible schema or identity changes.
- Durable or distributed lifecycle design.
- Release capacity or a service objective with no measurement.
- Cross-system authorization or idempotency.
- Opaque, version-specific framework behavior.
- A shared contract with no owner; colliding edits.
- A runtime claim with no workload, objective or operations owner.
- Non-JVM targets, where the Java-interop rows are meaningless. Scope explicitly to JVM modules or split out a multiplatform variant.

Framework rules assume one explicit execution model. Mixed MVC and WebFlux, blocking JPA on a coroutine path, multiple transaction resources, and Android or multiplatform lifecycles need separate decisions.

### Control scope

Name the scope of each control: coroutine or request, process or instance, partition or shard, service, region or zone, organization or global. A local mutex is not cross-replica idempotency. An instance counter is not tenant-wide rate limiting. Regional uniqueness is not global. One service's success is not an end-to-end terminal outcome.

### Splitting

1. Map the whole outcome.
2. Identify the transitions that fail and recover independently, and their owners.
3. Define safe intermediate states. If there are none, use a coordinated atomic or maintenance transition, not parallel implementation.
4. Split by decision and owned artifact, not by file count.
5. Freeze interfaces before parallel work.

A natural split by authority and commit: ingress, authentication and durable acceptance; then worker and domain effect; then provider and reconciliation; then the terminal outcome. Split delivery by independent service, schema migration, external workflow or runtime failure domain once requirements, contracts, owners, rollout order and rollback are explicit, with one integrator. Split large refactors into adapter and domain reviews, and time-box reviews with a handoff of unfinished rows. Fixture plans split on their own criteria (deployable system, data store, external contract, security boundary, verification environment), and every split keeps a named integration owner and a cross-split contract test; the full rule is under Fixture plan in Theme Specific Artifact.

Interface contract between split parts: versions and supported combinations; schema and unknown-field behavior; authentication, identity, secret and audit ownership; timeout, cancellation, retry, idempotency, ordering and duplicates; transaction, migration, freshness, cache and reconciliation; artifact, configuration and release ordering; readiness, liveness, degradation and termination; signals and correlation.

### Parallel work

Parallelize disjoint adapters and read-only investigation. Do not parallelize shared entities, work inside one transaction, coupled schemas, mixed blocking and reactive decisions, or shared contracts. Parallelism is unsafe when two workers choose the same architecture, edit the same schema, mutate shared state or depend on an interface still under negotiation. Give each module or artifact one writer, and each decision record one final owner. Topologies: one integrated owner, specialist composition, sequential phases, parallel evidence gathering.

### Narrowing in a large codebase

1. Find the target's instructions and build roots.
2. Find the runtime entry point, composition root, workers, migrations, pipeline, package and deployment artifacts.
3. Trace inbound and outbound dependencies at the changed boundary.
4. Rank by decision relevance.
5. Spend context on the failure path and the counterexample before broad architecture prose.
6. Keep a locator map and expand only when a discovered edge changes the blast radius.

A long unranked file list is not context evidence.

### Review at volume

Manual row walks suffice while volume permits. As diff volume grows, mechanize the searchable rows, adopting existing detekt rules before writing custom ones. A naive `!!` lint flags fixtures; keep known false positives with triage. Boundary judgment, receiver clarity and API compatibility stay human. Recheck the coroutine rows after a major `kotlinx.coroutines` release and the stance assumptions after a major framework release.

## Outcome Metrics and Feedback Loops

No metric here has a measured baseline or an effect size. A metric is complete only with a decision question, population, unit, event source, inclusion and exclusion rules, data quality, segmentation, interpretation, a guardrail, an owner action and an invalidation condition. A dashboard value without an action path is telemetry, not a feedback loop. Select the few metrics that change current decisions.

### Delivery

Requirement-to-test coverage; boundary defects found before rollout; escaped contract errors; migration rehearsal; timeout and cancellation coverage; duplicate-write prevention; rollback readiness; saturation; review effort; lead time by comparable feature class. Packet section completeness; fill rate of the requirement-to-test table; unchanged-stack rate; vague requirements rejected; near-misses on uninvited migration; wrapper-gate pass rate.

Leading indicator: lead time from requirement to verified endpoint, within one focused implementation session. Failure signal: framework or coroutine behavior that was guessed. Requiring every endpoint or worker change to finish in one sitting is a bad measure; it produces artificial splitting and skipped gates. One sitting is not a baseline.

### Kotlin quality

Proposed and unmeasured: claim-evidence coverage; boundary-escape findings; cancellation-path coverage; blocking-contract coverage; finding disposition latency; blocker precision on a sample; review reversal rate. Each needs a denominator, a decision use and a counter-metric against gaming.

Per review record: applicable rows, identifier-keyed findings, severity, whether each boundary diff has risk tests, scoped-out rows, gate results. Track findings per identifier, scan hits per diff for `!!`, `lateinit` and `GlobalScope`, and the fraction of suspend-path diffs with cancellation tests.

### Testing

By boundary and test type: requirement-to-red time; focused and full duration; first-run failure rate; repeatability; quarantine count; seeded-fault detection; escaped defects; setup cost; a reviewer's ability to identify the proof. Quarantines get an owner and an expiry. Convert every escaped defect or diagnosed flake into a fixture-boundary update. A production-dialect suite that costs extra time but catches locking mutations should be isolated and kept, not deleted.

### Security and resilience

Verified or approved field closure; claim-to-gate traceability; negative-path closure; fault-path closure; age of selectively invalidated evidence; whether the gate detects the unsafe form; recurring findings.

### Runtime

Accepted-outcome coverage; first discriminating feedback; gate qualification; deterministic gate health; artifact continuity; configuration safety; migration compatibility; signal actionability; health automation truth; staged release control; worker and shutdown reconciliation; recovery effectiveness; runbook usability; temporary control burden; operational toil and cost; evidence freshness; learning closure.

### Reading the numbers

- Faster delivery, more types and no incident do not prove quality.
- Counting packets rewards ceremony. Counting findings rewards nitpicking.
- A falling finding count may mean cleaner code or lazier review. Zero findings with rising scan hits is not success.
- Faster requirement-to-pass is not improvement if the first discriminating gate moved later.
- More tests are not better if they repeat one failure model. Coverage percentage, retries and deleting realistic tests are not outcomes.
- Fewer incidents may be lower exposure or changed reporting. Shorter recovery may hide premature closure. Fewer alerts may be broken routing.
- Deployment frequency is not a safety result. Lower cost can shift risk.
- Completion percentage is not safety proof, and packet completeness is not semantic correctness.
- Correlation with downstream quality is not causation.
- A metric pipeline's failure must be visible: an empty alert stream or a falling incident count is not improvement if collection stopped.

### Loops

Cadence follows events: contract formation, pre-merge, staged rollout, steady operation, a dependency or policy change, an incident or near miss, and a review of metric definitions. Calendar review is only a backstop. Actions are proceed, hold, roll back, scale, contain, repair or revise. Close a loop only after both the intended outcome and its guardrail are checked. Three layers of evidence feed the loop: deterministic gate data, sampled workflow outcomes and downstream quality outcomes.

## Completeness Checklist

Status for each item is pass, conditional (blocks only the stronger claim), not applicable (needs a target fact proving absence; reopen on scope change), fail or inconclusive. Do not compute an overall percentage: one failed secret, data, artifact, traffic, effect or recovery invariant is not cancelled by many passing checks. A waiver names the authority, the reason and the compensating evidence. Two reviewers should be able to locate the same evidence for each item.

### Delivery

- [ ] Framework and versions evidenced from the build.
- [ ] Versioned requirements with identifiers.
- [ ] Six-boundary map, or a compact checklist with a reason.
- [ ] Request and response contracts.
- [ ] Domain invariants and errors.
- [ ] Transaction boundary.
- [ ] Persistence and migration.
- [ ] Blocking model named.
- [ ] Deadlines.
- [ ] Retry and idempotency.
- [ ] Validation at transport and domain.
- [ ] Authorization and validation ownership.
- [ ] Stable error mapping.
- [ ] Compiler-plugin and serializer implications.
- [ ] Observability.
- [ ] Success and failure tests.
- [ ] Rollout and rollback.
- [ ] Evidence for each non-functional claim.
- [ ] Coroutines not marked safe merely because a handler is `suspend`.

Review twice: first validate each item against an artifact, command or code path; then trace one success and one failure journey through all boundaries. Watch for checkbox theater, tests that skip installed plugins, no invalid-input case, a missing Java platform-type review and implicit transactions.

### Kotlin semantics

- [ ] Exact ingress normalized.
- [ ] Nullable, absent, invalid, forbidden, unknown, failed and not-loaded distinguished where callers differ.
- [ ] Platform types contained.
- [ ] No ambiguous boolean, null, string, generic or broad-exception outcomes.
- [ ] Identity, equality, copy and persistence aligned.
- [ ] Coroutine cancellation, failure and cleanup owned.
- [ ] Blocking classified and bounded.
- [ ] Mutable state has a lifecycle, synchronization, reset and shutdown.
- [ ] The dangerous branch is tested.
- [ ] Actual gates and external reds reported.
- [ ] Runtime claims come only from controlled experiments.

When this guidance is summarized or restated, check that all fifteen `KC1` identifiers and scores, the five doctrine areas, the six review questions and every exception clause survive. A rule can be inverted while its identifier remains.

Extra gates by condition:

| Condition | Extra evidence |
| --- | --- |
| Public API | Consumer inventory, versioning, rollback |
| Persisted model | Migration, read and write compatibility, data recovery |
| Framework entity | Versioned contract, integration test, proxy behavior |
| Shared dispatcher | Lifecycle, failure matrix, queue evidence, operations owner |
| Global state | Usage, consistency, staged replacement, shutdown |
| Analyzer change | Rule, configuration, population, baseline, CI |
| Performance claim | Equivalent behavior, workload, samples, objective owner |

### Testing

- [ ] Each test maps to a requirement and a boundary.
- [ ] The test tool matches the framework.
- [ ] Fixture ownership and cleanup.
- [ ] Deterministic clock and dispatcher control.
- [ ] Negative cases.
- [ ] Production dialect where SQL or locking matters.
- [ ] Concurrency where a race is the risk.
- [ ] Red evidence before the fix.
- [ ] The full command and its result.
- [ ] Unresolved risks routed.

Files existing or coverage rising is not completion.

### Security and resilience

- [ ] A bounded transition with policy owners.
- [ ] Classified evidence, non-goals and scale.
- [ ] Bounded untrusted inputs.
- [ ] Authentication and resource authorization.
- [ ] Enumeration and error contract.
- [ ] Browser integrity decision.
- [ ] Abuse controls on sensitive flows.
- [ ] Proofs for coroutine, blocking, transaction, retry, idempotency, client and durable work.
- [ ] Overload behavior.
- [ ] Telemetry.
- [ ] Rollback.
- [ ] Invalidation.

### Runtime

- [ ] **Build and artifact.** Wrapper and configured tasks; effective versions including transitive ones; version changes are explicit upgrades; a clean package produces an identified artifact; CI deliberately fails for a representative defect when a gate is new or changed. Style success is not runtime evidence.
- [ ] **Configuration, secrets and profiles.** Raw configuration is bound at an owned boundary; valid, absent, malformed, boundary, unknown and restart cases run through the actual binding and packaged startup; environment differences are declared capabilities, not hidden branches on environment names; non-production canary values verify no disclosure; denied or missing secret access gives the intended state without restart amplification or unsafe fallback.
- [ ] **Data and migration.** Supported prior states, mixed versions, partial failure.
- [ ] **Signals, health and objectives.** Each signal answers a failure question; bounded dimensions; telemetry loss exercised; objectives come from the target's owners; dependency failure does not automatically fail liveness.
- [ ] **Package, CI, release and platform.**
- [ ] **Worker, shutdown and recovery.** Termination injected before and after each ownership and effect transition, not only when idle.
- [ ] **Runbook and handoff.**

Use a subset by phase: design handoff, implementation completion, release review, incident closure, or the minimal set for an active incident.

### Skeptical questions before closing

- Which row was hardest to prove, and was the claim weakened honestly?
- Which passing gate could be a no-op, the wrong artifact, an unrealistic fixture or a telemetry illusion?
- Which state exists only in production or on another owner's platform?
- What counterexample would reverse the choice of mechanism?
- Can a not-applicable row occur through a transitive dependency, a worker, an old consumer or a platform override?
- Does a green process hide wrong data, work, traffic, effect or customer state?
- Does any temporary path lack an owner or a retirement event?

Hard stops: a reported pass that cannot be traced to a run; a changed production boundary with no owner-authorized stop and recovery.

## Adjacent Reference Routing

One accepted outcome has one lead owner. Route a named uncertainty to the smallest source or authority that owns it.

### Other skills in this library

| Question | Go to |
| --- | --- |
| Writing the requirement before the code | [../executable-specs/SKILL.md](../executable-specs/SKILL.md) |
| Red-green-refactor discipline and resuming interrupted work | [../tdd-progress-and-resume/SKILL.md](../tdd-progress-and-resume/SKILL.md) |
| Reviewing, verifying or debugging a change in general | [../review-verify-debug/SKILL.md](../review-verify-debug/SKILL.md) |
| Finding the affected boundaries in a large codebase | [../codebase-navigation/SKILL.md](../codebase-navigation/SKILL.md) |
| Cross-service architecture and choices that span languages | [../system-design-and-polyglot/SKILL.md](../system-design-and-polyglot/SKILL.md) |
| Branches, commits and pull requests | [../git-delivery-flow/SKILL.md](../git-delivery-flow/SKILL.md) |
| TypeScript or Python services | [../typescript-backend/SKILL.md](../typescript-backend/SKILL.md), [../python/SKILL.md](../python/SKILL.md) |
| Android UI, Kotlin Multiplatform clients, Kotlin/JS | Not covered. Say so |

### Inside this skill

| Question | Lead |
| --- | --- |
| Code shape, interop, domain modeling, coroutine doctrine | Kotlin reliability rules |
| Workflow, mode and framework stance | Mode selection and workflow |
| Framework composition, execution-model alignment, transport and application boundaries | Spring and Ktor rules |
| Boundary, harness, data, determinism and failure injection in tests | Testing and fixtures |
| Trust boundaries, retries, idempotency | Security and resilience |
| Build, configuration, signals, migration, package, CI, health, rollout, shutdown, recovery | Runtime operations |

Testing is a seam: gate selection is shared, but the choice of risk tests belongs to the Kotlin rules. A coroutine cancellation question with a known contract stays in testing; an undecided production execution model goes to runtime. Generic cancellation stays generic until request lifecycle or dispatcher ownership makes backend guidance necessary; a Ktor Flow cancellation issue needs both, as separate claims. Do not use generic Kotlin guidance to decide Spring, Ktor, persistence, authentication, migration or production-runtime policy. Do not let operations guidance redefine product semantics. A shared word such as build, config or deploy is not enough to activate runtime guidance. Do not use an adjacent source to avoid an in-scope decision.

When runtime is not the lead: for pure Kotlin types, language guidance leads and operations supports only if serialization, configuration, artifact or lifecycle changes; for an endpoint or domain change, service design leads and runtime constraints attach to its acceptance criteria; for an incident, preserve evidence, contain under authority and start at the earliest observed break.

### Outside owners

| Owner | Send | Get back |
| --- | --- | --- |
| Security and identity | The transition, the actor, the proposed policy | The authorization decision and threat model. Threat and abuse analysis owns attacker goals and broad data flows |
| Database and data | The invariant, the migration, the historical data shapes | Compatibility and remediation decisions. Data-governance records own legal classification and retention |
| Broker or external system | "When is this item durably acknowledged?" | Delivery and acknowledgement semantics |
| CI and artifact platform | The gate and the artifact identity | Provenance and promotion rules |
| Runtime and deployment platform | "Which platform state removes traffic before drain?" | Health, traffic and termination behavior |
| Telemetry and incident tooling | The signal contract | Delivery, retention, alert routing |
| Incident command | A provider outage or organization-wide incident | Coordination; stop local changes |
| Current primary documentation | One versioned claim | Mechanism behavior only |
| Architecture decisions | A cross-service choice | The decision record |

An external authority explains supported mechanism behavior. It does not replace target policy or an observed outcome. Product semantics, migration, threat model, provider and data policy, objectives and rollout go to their owners.

A handoff carries origin, trigger, destination, the question, the evidence, the expected return artifact, the owner and the stop condition.

Anti-loop rules: return to a prior owner only when new evidence invalidates an assumption. Two sources cannot both lead the same decision; two are justified only for distinct roles, such as language semantics plus framework lifecycle. Avoid "review everything" handoffs. The receiving side must not change unrelated mechanisms. A document handoff grants no production authority. If no owner accepts a consequential boundary, stop and escalate. Organize durable routes around state ownership (artifact, data, identity, traffic, work, recovery), not personal names. Missing the owner is worse than carrying extra context. End when the reader can stop reading and act.

## Source Evidence Mapping Table

| Claim area | Basis | Status |
| --- | --- | --- |
| Fifteen `KC1` patterns, their scores, the five doctrine areas, the six review questions | The owner's Kotlin reliability doctrine | Authored doctrine. Scores are assertions |
| Twelve Kotlin hazards, the gate ladder, candidate scans, the evidence packet and blockers | The owner's Kotlin quality-gate doctrine | Authored doctrine; the packet is a proposed format |
| Nine modes, eight workflow steps, the output contract, framework stance | The owner's Kotlin backend delivery doctrine | Authored doctrine |
| Six service boundaries, transaction, DTO, client and worker rules, API defaults | The owner's backend playbook | Authored doctrine |
| Spring and Ktor rules | The owner's framework idiom notes | Authored doctrine. Framework facts are not re-checked against current releases |
| Test selection, fixtures, coroutine and database tests | The owner's testing notes | Authored doctrine |
| Security, retry, idempotency, durable work | The owner's security and resilience notes | Authored doctrine |
| Build, configuration, observability, migration, container, CI, rollout, shutdown | The owner's runtime operations notes | Authored doctrine |
| Failure tables, workload, reliability targets, metrics, scale boundaries | Expanded study notes over the doctrine above | Reasoned synthesis; no figure is measured |
| Evidence hygiene scores 95, 91 and 88 | Inherited from the same study notes | Assertions |
| Review-batch sizes, the 18 of 20 sample, the ten-minute review target, the p95 and p99 placeholders | Proposed in the study notes | Unmeasured |

Public sources the doctrine cites. The doctrine's research is dated 2026-06-23. None of these pages was re-fetched for this file; treat each as a routing lead until it is retrieved and matched to the target's versions.

Entry points:

| Topic | URL | Owns |
| --- | --- | --- |
| Kotlin documentation | <https://kotlinlang.org/docs/home.html> | Syntax, types, conventions, nullability, interop, sealed types |
| `kotlinx.coroutines` | <https://github.com/Kotlin/kotlinx.coroutines> | Scheduling, cancellation, exceptions. Repository state is not necessarily released dependency behavior |
| Spring Boot with Kotlin tutorial | <https://github.com/spring-guides/tut-spring-boot-kotlin>, <https://spring.io/guides/tutorials/spring-boot-kotlin/> | Spring and Kotlin integration examples |
| Ktor documentation | <https://ktor.io/docs/welcome.html>, <https://ktor.io/> | Ktor as a framework for asynchronous servers and clients |

Kotlin language and server side:

| What the doctrine takes from it | URL |
| --- | --- |
| Kotlin suits server-side work and stays compatible with Java stacks | <https://kotlinlang.org/docs/server-overview.html> |
| Style and organization | <https://kotlinlang.org/docs/coding-conventions.html> |
| Scope functions | <https://kotlinlang.org/docs/scope-functions.html> |
| Sealed classes and interfaces | <https://kotlinlang.org/docs/sealed-classes.html> |
| Java interop | <https://kotlinlang.org/docs/java-interop.html> |
| Java-to-Kotlin nullability | <https://kotlinlang.org/docs/java-to-kotlin-nullability-guide.html> |
| Structured concurrency | <https://kotlinlang.org/docs/coroutines-basics.html> |
| Cancellation and timeouts | <https://kotlinlang.org/docs/cancellation-and-timeouts.html> |
| Coroutine context and dispatchers | <https://kotlinlang.org/docs/coroutine-context-and-dispatchers.html> |
| Coroutine exception handling | <https://kotlinlang.org/docs/exception-handling.html> |
| Data classes as value carriers | <https://kotlinlang.org/docs/data-classes.html> |
| Serialization | <https://kotlinlang.org/docs/serialization.html>, <https://github.com/Kotlin/kotlinx.serialization> |
| Why Spring AOP needs open classes | <https://kotlinlang.org/docs/all-open-plugin.html> |
| Why JPA needs no-arg construction | <https://kotlinlang.org/docs/no-arg-plugin.html> |

Spring:

| What the doctrine takes from it | URL |
| --- | --- |
| Kotlin as a first-class Spring path | <https://docs.spring.io/spring-boot/reference/features/kotlin.html>, <https://docs.spring.io/spring-framework/reference/languages/kotlin.html> |
| Coroutine integration points | <https://docs.spring.io/spring-framework/reference/languages/kotlin/coroutines.html> |
| Test slices and full application tests | <https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html> |
| Kotlin DSL for security configuration | <https://docs.spring.io/spring-security/reference/servlet/configuration/kotlin.html> |
| Actuator health | <https://docs.spring.io/spring-boot/api/rest/actuator/health.html> |
| Micrometer-backed metrics | <https://docs.spring.io/spring-boot/reference/actuator/metrics.html> |
| Testcontainers integration | <https://docs.spring.io/spring-boot/reference/testing/testcontainers.html> |
| Flyway endpoint for migration visibility | <https://docs.spring.io/spring-boot/api/rest/actuator/flyway.html> |

Ktor:

| What the doctrine takes from it | URL |
| --- | --- |
| Routing | <https://ktor.io/docs/routing.html> |
| Type-safe routing | <https://ktor.io/docs/type-safe-routing.html> |
| Server serialization | <https://ktor.io/docs/server-serialization.html> |
| Server testing | <https://ktor.io/docs/server-testing.html> |
| Database integration with Exposed and repository injection | <https://ktor.io/docs/server-integrate-database.html> |

Persistence:

| What the doctrine takes from it | URL |
| --- | --- |
| Exposed: DSL and DAO APIs; database work happens inside transactions | <https://www.jetbrains.com/help/exposed/home.html>, <https://www.jetbrains.com/help/exposed/transactions.html>, <https://github.com/JetBrains/Exposed> |
| jOOQ: type-safe SQL and Kotlin usage | <https://www.jooq.org/>, <https://www.jooq.org/doc/latest/manual/getting-started/jooq-and-kotlin/>, <https://www.jooq.org/doc/latest/manual/sql-building/kotlin-sql-building/> |
| Flyway: versioned migrations | <https://documentation.red-gate.com/fd> |

Testing and static analysis:

| What the doctrine takes from it | URL |
| --- | --- |
| Kotest and property testing | <https://kotest.io/>, <https://kotest.io/docs/proptest/property-based-testing.html>, <https://github.com/kotest/kotest> |
| MockK: Kotlin-native mocking, coroutine-aware | <https://mockk.io/>, <https://github.com/mockk/mockk> |
| Testcontainers: disposable real infrastructure | <https://java.testcontainers.org/> |
| ktlint | <https://github.com/pinterest/ktlint> |
| detekt | <https://detekt.dev/>, <https://github.com/detekt/detekt> |

Representative repositories, useful as precedents and not as rules:

| Repository | URL |
| --- | --- |
| Spring Kotlin demo | <https://github.com/sdeleuze/spring-boot-kotlin-demo> |
| Ktor official samples | <https://github.com/ktorio/ktor-samples> |
| RealWorld, Kotlin and Spring | <https://github.com/gothinkster/kotlin-spring-realworld-example-app> |
| RealWorld, Kotlin and Ktor | <https://github.com/Rudge/kotlin-ktor-realworld-example-app> |

Three findings from that research shape the whole skill:

- Kotlin backend risk is not language syntax. It clusters around Spring or Ktor integration, nullability, coroutines, persistence, testing and JVM operations.
- No single source states universal Kotlin backend practice. The guidance is a synthesis from primary documentation and representative repositories, and it preserves local framework choices.
- Spring and Ktor share language concerns, but their ergonomics differ enough to need separate modes. One framework rule does not cover both.

Four lenses to read a design through, each with what it presses on:

| Lens | Presses on |
| --- | --- |
| Kotlin and JVM language specialist | Nullability, platform types, value classes, data classes, sealed outcomes, compiler plugins, coroutine semantics |
| Backend operator | Migrations, configuration, secrets, observability, health checks, timeouts, retries, deployment safety |
| Spring or Ktor implementer | Test slices, plugins, typed configuration, dependency injection, transaction scope, route and controller boundaries |
| Skeptical reviewer | Over-broad claims, fake non-blocking designs, all-purpose data classes, full-stack rewrites disguised as feature work |

Authority is role-specific. Official Kotlin documentation answers language questions; `kotlinx.coroutines` answers scheduling and cancellation; Spring or Ktor documentation answers only for the matching framework; the target repository answers local applicability; the owner answers policy. Citing the Kotlin home page to choose a Spring test slice is the bad case.

## Evidence Boundary Notes

### Kinds of claim

Keep these apart, and attach the strongest accurate role, not the most prestigious source:

| Kind | What it cannot support alone |
| --- | --- |
| Owner doctrine (this skill) | A fact about the target or about current framework behavior |
| External fact, not refreshed | Current behavior |
| External fact, refreshed and versioned | Target applicability; official status establishes provenance, not fit |
| Target instruction or policy | That the code follows it |
| Target implementation | Desired policy or correctness |
| Observed result (test, command, runtime) | Other inputs, other environments |
| Negative or contradictory evidence | Absence, unless the observation path was qualified |
| Combined inference | Being quoted as a fact |
| Engineering judgment | Being quoted as a requirement |
| Forecast or hypothesis | Any completion claim |
| Conditional claim | Anything outside its condition |
| Accountable owner decision or accepted risk | Enforcement |
| Illustrative scenario | Any target |
| Unknown or unresolved | Anything; name the owner |

Examples: transaction placement is a doctrine rule; annotation behavior is a tested Spring fact; latency is a local benchmark. A rethrow-first rule can be cited as doctrine under `KC1-10`; a score of 98 cannot be presented as measured.

### Authority by claim type

Meaning of a rule comes from this doctrine. Current existence comes from target source and configuration. Fixture behavior comes from target tests. Desired state and identity come from the owner. Version promises come from a versioned official artifact plus reproduction in the target. Load behavior comes from a controlled runtime measurement. Residual risk comes from an accountable owner.

### Prohibited inferences

- An official root URL means current guidance.
- Target code means desired policy.
- A passing unit test means all inputs or production.
- A green analyzer or build means no defects, or verified cancellation, blocking or identity.
- Accepted risk means enforcement.
- A runtime sample means all environments.
- Degraded collection or no event means zero.
- `suspend` means non-blocking.
- A sealed outcome covers infrastructure exceptions.
- Green unit tests cover proxies and transactions.
- A hash proves truth; it proves artifact identity.
- Documentation proves adoption; it proves a mechanism exists.
- Happy-path tests prove denial or recovery.

Absence is meaningful only when the observation path was expected and qualified. No alert may mean no failure, broken emission, delayed collection, a wrong query, changed routing or missing access. A test pass may mean correct behavior, an empty selection, a skipped task, a stale cache, an unrealistic fixture or the wrong artifact.

### Evidence chain

Discovery lead, reviewed claim, policy or authority, target representation, executable result, staged observation, maintained claim with invalidation triggers. Confidence has several dimensions (integrity, authority, relevance, freshness, target adoption, execution coverage, operational coverage, independence, uncertainty) and is not one number.

### Rules

- Break a statement into separate claims when role, version or scope differ.
- A claim names its boundary, the dependency and version, the source role, the retrieval date and local applicability. Evidence detached from scope decays into folklore.
- Date coroutine-semantics claims to the library version in the build.
- Do not copy Spring examples into Ktor. Do not infer a Spring annotation from a framework-neutral rule.
- Never call a link current without retrieving it.
- Keep recommendation and requirement distinct.

### What this file does not establish

Which framework, build tool, database or tool a future repository uses. Any current public release, default or advisory. Any universal latency, throughput, capacity, reliability, retry, service-objective or recovery value. Production readiness of anything.

### Known disagreements inside the doctrine

| Topic | Positions | What selects |
| --- | --- | --- |
| Spring or Ktor | Spring by default for enterprise JVM stacks; Ktor for coroutine-first services | The target repository's existing stack. Greenfield goes to the user |
| Latency fallback figures | A provisional local diagnostic; or not to be used at all | Whether an owner objective exists and whether latency is in scope (see Performance Verification Method) |
| Review-batch size | A numeric prompt (25 endpoints, 1,000 requests, 20 requirement identifiers); or no universal count | Coherence decides; the numbers only prompt the question |
| Moving blocking work to another dispatcher | The patterns say to isolate blocking calls on a named dispatcher; the failure tables list a dispatcher switch as false confidence | Both hold. The switch isolates when the adapter owns a bounded policy; it never proves capacity or cancellability |
| Full fifteen-row review record | Required for boundary-touching diffs; ceremony for trivial ones | Whether the diff touches a boundary |
| Value and sealed types | Preferred for identifiers and outcomes; can conflict with reflection, serialization, ORM and Java | Verified framework and persistence support in the target |

## Future Refresh Search Queries

Refresh only when an external claim can change the plan: a version difference, an advisory, a provider change, a deprecation or an unexplained failure. Stop when the claim is supported enough, when target execution or owner policy is the remaining uncertainty, or when sources cannot resolve the conflict. Query text is not evidence. Sanitize credentials, personal data and internal hosts before any external search.

### Fill these from the target first

Resolved Kotlin and Java versions; framework name and version; coroutine library version; compiler plugins; database engine and version; migration tool; telemetry component; platform or provider and its mode; CI and artifact system; the claim phrase; the observed failure class. If these cannot be established, go back to target discovery, not to another broad search.

### Query catalog

```text
site:kotlinlang.org {resolved_kotlin_version} {resolved_java_version} {claim_phrase}
site:kotlinlang.org {coroutine_version} cancellation timeout dispatcher exception {claim_phrase}
site:docs.spring.io {framework_name} {framework_version} Kotlin {claim_phrase}
site:docs.spring.io {framework_version} health readiness liveness graceful shutdown {claim_phrase}
site:ktor.io {framework_version} {platform_mode} configuration health shutdown {claim_phrase}
```

Further families, built the same way from the target's fields: Kotlin compiler-plugin compatibility; database engine semantics; migration tool behavior and compatibility changes; telemetry integration, failure and limits; JVM container runtime; platform health, traffic and termination; secret provider integration; CI artifact provenance; provider incidents and deprecations; maintainer security advisories; release notes for the exact component; current official samples.

Topic queries from the language doctrine:

```text
kotlin coding conventions updates
kotlinx.coroutines changelog
cancellation and structured concurrency guidance
Kotlin binary-compatibility tooling
```

### How each family is confirmed locally

| Family | Local confirmation |
| --- | --- |
| Kotlin compatibility | Compile the target feature |
| Coroutines | Exercise the scope in a test |
| Spring or Ktor mechanism | Run the target context or test host |
| Build or plugin | Resolve through the wrapper |
| Serialization | Malformed wire fixtures |
| Database, driver, ORM, migration | Production dialect, isolation, rehearsal |
| Broker | Duplicate, restart and drain tests |
| Advisory | Exposure check and gates on the fixed release |
| Provider effect | The actual request identity |
| Deployment | Startup, traffic, disconnect, health, shutdown |

### Quality rules

- Claim first, versioned. Include the dependency version, the execution model and the disputed API.
- Avoid "Kotlin backend best practices", unversioned snippets and cross-framework samples. Prefer ecosystem vocabulary.
- Kotlin search results skew toward Android. Grade backend relevance and rewrite queries that return mostly Android lifecycle material.
- Release notes have the highest yield for compiler-plugin, framework-version and coroutine-API assumptions. The coroutine rows (`KC1-09` to `KC1-11`) are the most perishable, so changelog and cancellation searches come first.
- Open the selected artifact, not the snippet. Do not count reposts as independent sources. Distinguish no search result from no guidance.
- Reject a result that defaults to the latest release while the target uses another; describes a different engine, mode or edition; is a tutorial, forum post or snippet used as a rule; omits prerequisites; or is official for the wrong ownership layer.
- Record each result as accept, adapt, reject, informative only, contradictory, blocked or no result, with the retrieval date and the claim it changes.
- Mark superseded claims stale instead of deleting them by date alone. A broken link does not necessarily mean obsolete guidance.
