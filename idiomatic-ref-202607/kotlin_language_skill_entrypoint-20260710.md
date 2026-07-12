# Kotlin Language Skill Entrypoint

Use this reference to decide how a Kotlin request should be approached before
loading broad language guidance or changing code. It is a routing and
reliability entrypoint, not a Kotlin tutorial and not a substitute for target
repository evidence.

`entrypoint_default`: Name the accepted outcome, classify the Kotlin surface,
identify the strongest plausible failure, select one lead work mode, preserve
the target toolchain, open only the relevant frozen reference regions, and
choose the smallest gate capable of disproving the proposed change.

The frozen `kotlin-coder-01` skill defines seven composable modes:
`Core Kotlin Mode`, `Nullability Mode`, `Type Boundary Mode`, `Coroutine Mode`,
`Interop Mode`, `Testing Mode`, and `Review Mode`. Mode names organize the
investigation; they do not prove that a mechanism fits a future target.

| initial_surface | likely_lead_mode | first_risk_question | route_change_trigger |
| --- | --- | --- | --- |
| pure function, collection transform, extension, package, or visibility change | Core Kotlin Mode | Does the design keep ownership, receiver, return value, and mutation obvious? | raw input, Java uncertainty, asynchronous ownership, or public compatibility becomes material |
| nullable input, Java return, generated API, reflection, or deserialized value | Nullability Mode | Where can uncertainty be converted once into an explicit Kotlin state? | the issue is really wire compatibility, framework binding, or domain outcome design |
| identifier, unit, parser, DTO, state machine, result, or public domain API | Type Boundary Mode | Which invalid or distinct states are currently representable by accident? | Java consumers, serialization shape, persistence identity, or framework proxy rules dominate |
| suspend function, `Flow`, parallel child work, timeout, retry, or blocking adapter | Coroutine Mode | Who owns lifetime, cancellation, failure, dispatcher use, and cleanup? | application lifecycle, queue semantics, deployment shutdown, or provider retry policy leads |
| Kotlin API called by Java or Java library consumed by Kotlin | Interop Mode | Which nullability, naming, overload, exception, generic, and binary contracts cross the boundary? | the target is primarily Java or a framework-generated contract outside Kotlin ownership |
| behavior is unclear or a high-risk boundary needs executable evidence | Testing Mode | What is the lightest faithful test that fails for the suspected Kotlin defect? | only a real framework, database, broker, package, or platform can represent the behavior |
| existing Kotlin change needs risk-focused evaluation | Review Mode | Which boundary can compile while remaining unsafe, ambiguous, or incompatible? | implementation or incident response is authorized and a more specific route must lead |

Select one lead mode so the task has a clear decision owner. Add another mode
only for a named interface. For example, `Coroutine Mode` can lead a suspend
API change while `Interop Mode` checks a Java callback boundary and `Testing
Mode` supplies cancellation evidence. Three labels without distinct questions
are context expansion, not routing.

**Activation test**

Activate this entrypoint as the lead when all of the following are true:

- Kotlin language semantics or Kotlin/JVM API design owns the main accepted
  outcome.
- The consequential uncertainty concerns types, nullability, Java interop,
  cancellation, blocking isolation, collections, scope-function clarity,
  public API evolution, or behavior-first tests.
- Applicable repository instructions, build files, Kotlin and JVM targets,
  compiler plugins, and configured quality gates can be inspected before a
  change.
- A focused language-level or boundary-level gate can provide meaningful
  evidence.

Use the entrypoint in support mode when a backend, framework, persistence,
security, runtime, deployment, or incident route owns the overall outcome but
needs a bounded Kotlin question answered. Route away when the request is
primarily Spring Boot or Ktor lifecycle, database behavior, migration, auth,
service operations, production traffic, or platform recovery. The frozen
skill explicitly assigns those concerns to `kotlin-backend-delivery-01`.

A `.kt` extension is not sufficient evidence. A database migration written in
Kotlin remains a data and rollout decision. Conversely, a Java platform type
escaping from a framework adapter may still require language support even
though backend delivery leads.

**Preservation stance**

Unless a migration is requested, preserve the repository's wrapper, Kotlin
version, JVM target, compiler settings, build style, test stack, static-analysis
tools, package conventions, and framework stance. Suggested commands such as
`./gradlew test`, `./gradlew build`, `./gradlew ktlintCheck`, `./gradlew detekt`,
`./mvnw test`, and `./mvnw verify` are candidate gate families from the frozen
source. Run only commands that target discovery shows are configured and
applicable. A globally installed tool or a newly introduced plugin is not an
equivalent substitute.

**Minimal activation record**

```text
accepted_outcome:
target_repository_revision:
kotlin_surface:
lead_mode:
supporting_modes_and_interface_questions:
dominant_failure_consequence:
applicable_instructions_and_owners:
effective_kotlin_jvm_build_state:
boundary_inputs_callers_and_consumers:
preserved_choices:
candidate_reference_regions:
first_falsifying_gate:
negative_or_boundary_case:
route_away_or_escalation_trigger:
known_evidence_and_uncertainty:
```

This record can be a brief working note for a small change. It should become a
durable decision record when the API is public, Java consumers exist, state is
persisted or serialized, concurrency is consequential, or another owner must
reuse the reasoning.

**Good, bad, and borderline activation**

Good language lead: a Java library returns an unannotated value that enters a
non-null domain field. Select `Nullability Mode` with `Interop Mode` support,
inspect the actual signature and callers, normalize the platform type in one
adapter, model absence explicitly, and test null plus non-null behavior. A
successful compilation alone is not the gate.

Good coroutine lead: a suspend operation catches `Exception` and converts all
failures into one result. Select `Coroutine Mode`, trace scope and cancellation
ownership, determine whether blocking work is hidden, preserve
`CancellationException`, and use a cancellation scenario that observes child
termination and cleanup. The backend operations route joins only if process shutdown or
durable work ownership is part of the outcome.

Support mode: a Ktor route introduces a sealed domain result. Backend delivery
leads routing, serialization, status mapping, lifecycle, and integration.
`Type Boundary Mode` answers whether the result space is closed and exhaustive.
The language result returns to the lead route for framework-level evidence.

Route away: a service needs a production database migration and staged
rollback decision. Kotlin syntax may implement an adapter, but data
compatibility, old and new application versions, deployment order, and recovery
own the consequence. Use the backend and data route first.

Direct answer: a developer asks what `val` means in an isolated snippet. No
multi-mode plan is needed unless target behavior or a code change expands the
question.

Borderline case: a data class is used by Kotlin domain code, Java callers,
serialization, and an ORM. Do not declare a mode from the class syntax. Inspect
equality, copy semantics, generated methods, Java call sites, serialized shape,
and persistence identity. The first boundary that can invalidate the change
selects the lead or triggers a composed route.

**Evidence boundary**

This evolved reference is grounded in frozen local files dated by their
archive context. The canonical skill and its four companion references were
read locally at recorded hashes. No public URL was retrieved during this
evolution, and no future target repository was inspected. Therefore:

- frozen content can establish what the historical skill says;
- systems synthesis can recommend conservative discovery and routing;
- target inspection establishes what a repository actually uses;
- qualified tests and scenarios establish only their recorded outcomes;
- current external behavior requires an authorized, version-bounded refresh;
- production or compatibility acceptance belongs to accountable target owners.

Treat route selection as revisable. Reroute when target discovery reveals a
different framework owner, a Java or binary compatibility surface, generated
code, a blocking dependency, persistent state, a security boundary, or an
environment that the chosen gate cannot represent. A useful entrypoint reduces
wrong work while leaving uncertainty visible; it does not maximize the number
of Kotlin patterns applied.

## Source Evidence Mapping Table

Use sources by bounded claim. A path, domain, or official label does not carry a
single confidence value across every question. Identity, source ownership,
currentness, target applicability, and observed outcome are separate evidence
dimensions.

**Frozen local sources read for this evolution**

Paths are under
`agents-used-monthly-archive/codex-skills-202606/kotlin-coder-01/`.

| local_source | sha256 | source_role_for_this_reference | strongest_supported_claim | prohibited_transfer |
| --- | --- | --- | --- | --- |
| `SKILL.md` | `e7e1606b917312f104e9ab337154bd88836dd292af82b64f6df359fb6d8889de` | canonical historical entrypoint contract | archived description, activation surfaces, seven work modes, workflow, output order, guardrails, and companion links | cannot prove a future target's build, versions, framework, behavior, or adoption |
| `references/reference-map.md` | `53cff6b483ef56f72ff6e78914963539891e81970827e8ffc8e3f63be99fa944` | progressive-disclosure router | archived jump points, section-search commands, and read order | cannot decide which region is relevant before target risk classification |
| `references/kotlin-reliability-reference.md` | `9a9fe3255daed3376ed035de5baacf12de09edc9d3e1b5c3314f4a43a03f101f` | language reliability doctrine | archived rationale and examples for type design, nullability, Java interop, coroutines, testing, and build gates | cannot establish framework, database, provider, binary, or target-runtime results by itself |
| `references/kotlin-quality-gates-and-anti-patterns.md` | `1b393027a06d8a4ca7790822c9c29485bd3e8d59d77d7dfc310a8a761cb44400` | final risk and gate checklist | archived anti-pattern causes, preferred alternatives, reliability stack, candidate wrapper commands, and review pass | cannot make an absent task, plugin, test, or tool applicable to a target |
| `references/sources-and-research-brief.md` | `b0fe8c64510af0025187f60d03440d286492342787a8e2a8e4b48e2a0bb05028` | dated provenance and future discovery map | what the local corpus says was researched on 2026-06-23, listed primary locations, repo-local influences, and synthesis boundaries | cannot establish that any public page, release, advisory, or default remains current on 2026-07-11 |

All five local artifacts were read completely for this evolution. Hashes prove
the bytes read; they do not prove that the archived recommendations are correct
for every Kotlin version or target.

**Inherited public mappings not refreshed in this evolution**

| historical_location | archived_usage_description | future_claim_owner | required_before_factual_reuse | current_status |
| --- | --- | --- | --- | --- |
| `https://kotlinlang.org/docs/home.html` | Kotlin language, style, type-system, interop, and coroutine-documentation discovery | version-applicable official Kotlin documentation and API | resolve target Kotlin and JVM versions, navigate to the exact owning page, read prerequisites and exceptions, record retrieval time, and reconcile with target code | unrefreshed historical mapping; no current page content claimed |
| `https://github.com/Kotlin/kotlinx.coroutines` | official coroutine library source, releases, tests, and implementation evidence | released coroutine repository material for the exact target version | resolve dependency version and execution mode, select tag or release, distinguish implementation from contract, then reproduce the target boundary | unrefreshed historical mapping; no repository state claimed |
| `https://github.com/spring-guides/tut-spring-boot-kotlin` | Spring-maintained Kotlin application example and integration vocabulary | applicable Spring documentation plus target project policy | confirm Spring is the chosen target, resolve versions, treat sample code as orientation, and verify proxy, serialization, lifecycle, and build behavior locally | unrefreshed representative-example mapping; not backend authority by itself |
| `https://ktor.io/docs/welcome.html` | Ktor server and client framework discovery | version-applicable Ktor documentation and target engine or plugin behavior | confirm Ktor and engine mode, resolve versions, open exact feature guidance, and run target integration and lifecycle scenarios | unrefreshed framework mapping; no target adoption inferred |

The local research brief additionally names Kotlin pages for coding
conventions, scope functions, sealed classes and interfaces, Java interop,
Java-to-Kotlin nullability, coroutine exception handling, and cancellation and
timeouts. Those are dated discovery leads from the frozen source. They are not
silently promoted to `refreshed_external_fact` here.

**Target evidence classes**

| target_evidence | use_for | minimum_record | important_limit |
| --- | --- | --- | --- |
| applicable instructions | edit boundaries, required workflow, ownership, and repository-specific constraints | path, scope, revision, precedence, and conflict | instructions do not prove successful runtime behavior |
| build and dependency resolution | effective Kotlin, Java, plugins, libraries, targets, tasks, and generated-code inputs | wrapper, build files, resolved values, module, and revision | configuration presence does not prove compatibility or correct behavior |
| implementation and caller inspection | actual types, scopes, adapters, visibility, Java consumers, serialization, and ownership | symbols, call paths, generated surfaces, and affected artifact | source inspection does not establish every runtime or binary consumer |
| target policy or owner decision | accepted support, compatibility, security, risk, and release constraints | accountable role, policy version, scope, exception, and expiry | authority cannot make technically incompatible behavior succeed |
| focused executable gate | deterministic language or boundary behavior | command or scenario, artifact, input, result, negative control, and skipped scope | a local unit gate cannot prove framework, provider, package, or production behavior |
| real-boundary or compatibility gate | Java, serialization, framework, dependency, ABI, or package interaction | actual versions, environment, fixture, result, and failure interpretation | one environment and population do not establish universal behavior |
| observed incident or production result | behavior of a recorded artifact under a recorded event | time, artifact, config, workload, state, signals, action, and final outcome | observation may not reveal cause or predict future conditions |

**Source-selection protocol**

1. State one decision-sensitive claim and the consequence if it is wrong.
2. Inspect applicable repository instructions and effective target state before
   assuming the frozen skill applies unchanged.
3. Use `SKILL.md` to choose the route and mode, then use `reference-map.md` to
   open only the reliability regions that own the named risk.
4. Finish with the anti-pattern and quality-gate reference for the activated
   boundaries. Do not import every checklist item into a small task.
5. Use source code and tests for implementation facts, target owners for policy,
   and current primary authority for version-sensitive support claims when
   retrieval is authorized.
6. Run a gate capable of exposing the suspected defect. Preserve negative,
   inconclusive, and conflicting evidence instead of selecting only a pass.
7. Record the stronger neighboring claim not supported, such as distinguishing
   `compiles locally` from `compatible for Java callers`.
8. Stop loading sources when the decision is bounded and additional material
   cannot change the route, implementation, or gate.

**Evidence ledger**

```text
claim_id_and_scope:
failure_consequence:
source_role:
source_or_target_locator:
hash_version_revision_environment:
read_region_and_date:
extracted_fact_or_observation:
prerequisites_exceptions_and_conflicts:
target_applicability:
verification_action_and_result:
stronger_claim_not_supported:
consumer_and_decision_owner:
refresh_or_invalidation_event:
```

When two sources conflict, first compare version, artifact, execution mode,
target configuration, and ownership layer. Applicable target policy constrains
the accepted choice, official authority constrains supported behavior, and a
qualified target failure blocks adoption under its observed conditions. Keep
the conflict visible until a discriminating scenario or accountable decision
resolves it.

Refresh selectively. A Kotlin compiler upgrade may invalidate language and
plugin claims without invalidating a pure parser invariant. A changed Java
consumer can invalidate interop evidence without requiring new coroutine
research. A framework migration should reroute backend integration claims even
when the core value type remains sound. Claim-level lineage keeps progressive
disclosure both small and maintainable.

## Pattern Scoreboard Ranking Table

The seed's values are preserved as historical editorial provenance. No sample,
scale, weighting method, or outcome calibration was recorded, so `95`, `91`,
and `88` are not percentages, probabilities, reliability levels, or measured
performance. They must not become adoption thresholds.

| inherited_pattern | seed_value | useful_historical_intent | limitation_that_changes_current_use |
| --- | ---: | --- | --- |
| `source_map_first_synthesis` | 95 | consult local Kotlin material before generalizing from ecosystem examples | begin with applicable instructions and effective target state; open only the mapped regions that own the risk |
| `evidence_boundary_split_pattern` | 91 | distinguish local content, public material, and synthesis | add target facts, policy, observed results, negative evidence, conditional claims, and currentness rather than relying on three coarse labels |
| `verification_gate_coupling` | 88 | connect recommendations to a command, checklist, or review gate | require a gate capable of failing for the named defect; an exact but irrelevant command does not qualify |

The frozen reliability reference contains fifteen additional `KC1` editorial
scores for platform types, non-null domains, value classes, sealed outcomes,
data classes, immutability, parsing, scope functions, structured concurrency,
cancellation, blocking isolation, Java interop, extensions, compatibility, and
tests. Those values likewise record emphasis, not universal risk magnitude.

**Current priority rule**

Prioritize an entrypoint pattern from observed target risk, not inherited rank:

| priority_pattern | activate_when | failure_prevented | minimum_gate | demote_or_reject_when |
| --- | --- | --- | --- | --- |
| `target_state_before_advice` | wrapper, versions, callers, generated code, configured gates, or ownership are not yet known | implementing against an imagined repository or toolchain | inspect applicable instructions, build roots, effective dependencies, consumers, and existing tests | the question is isolated explanation with no target mutation or compatibility claim |
| `mode_before_detail` | several Kotlin concerns could lead and broad reference loading would blur the decision | mixing language, backend, framework, and operational ownership | state one lead mode, supporting interface questions, and a reroute condition | one obvious bounded language question can be answered directly |
| `platform_type_containment` | Java, generated, reflection, or annotation-uncertain values enter Kotlin code | invisible nullability uncertainty crossing into non-null state | adapter test with null and non-null values plus caller inspection | target signature is fully Kotlin and nullability is proven end to end |
| `explicit_absence_and_outcomes` | nullable values, booleans, sentinel strings, or generic exceptions conflate distinct states | callers silently mishandling absent, invalid, forbidden, not-found, or review states | behavior tests for every accepted outcome and caller exhaustiveness where applicable | the state space is genuinely open or a target protocol requires another representation |
| `parse_raw_inputs_once` | strings, maps, JSON, CLI arguments, environment values, or Java objects reach domain logic | repeated validation, partial invariants, and distant failure | valid, malformed, absent, boundary, and round-trip cases at the actual adapter | the value is already a trusted domain type inside the bounded core |
| `value_type_semantics` | primitives carry identifiers, units, offsets, keys, or validated-string meaning | mixing semantically distinct values or bypassing invariants | construction, invalid input, equality, serialization, and interop checks as activated | wrapping adds no invariant or creates unsupported Java, framework, or binary behavior |
| `structured_concurrency_ownership` | suspend work, child tasks, `Flow`, timeout, or lifecycle scopes are touched | work outliving its owner, hidden failure, and incomplete cleanup | cancellation and child-failure scenarios observing final state and resource release | the operation is purely synchronous and no asynchronous ownership boundary exists |
| `cancellation_preservation` | broad catches, retry, logging, result normalization, or cleanup surround suspend calls | converting cooperative cancellation into business failure or continued work | cancel at each relevant phase and assert propagation without unwanted side effects | no suspend or cancellable boundary is in the execution path |
| `blocking_boundary_honesty` | JDBC, filesystem, legacy SDK, native, DNS, or CPU-heavy work appears under a suspend API | dispatcher starvation and misleading caller expectations | representative concurrency, cancellation, thread or dispatcher, and cleanup observation | target evidence proves the call is nonblocking or an intentionally blocking API owns it |
| `java_contract_explicitness` | Java callers or libraries cross public Kotlin APIs | platform leaks, unusable defaults, unexpected names, overload ambiguity, or binary breakage | compile or run representative Java callers and inspect signatures or compatibility reports | Java is not a supported consumer and no Java-origin value crosses the boundary |
| `data_class_semantic_fit` | a data class carries identity, lifecycle, lazy state, persistence behavior, or unsafe copy semantics | equality, copying, destructuring, or generated methods violating domain expectations | equality, copy, lifecycle, serialization, and framework scenarios relevant to the class | the type is immutable value data and generated semantics match the contract |
| `scope_function_clarity` | nested `let`, `also`, `apply`, `run`, or `with` obscures receiver or return value | reviewing or modifying the wrong object through visually compact code | behavior test plus reviewer check that ownership and returned value remain explicit | a short conventional scope function clearly expresses one receiver and result |
| `public_compatibility_preservation` | visibility, signatures, defaults, overloads, generics, annotations, sealed members, or serialized forms change | source, binary, Java, serialization, or downstream consumer breakage | repository-compatible API, ABI, caller, or contract gates selected from actual consumers | the API is private and target evidence confirms no persistent or generated consumer |
| `claim_to_falsifying_gate` | a recommendation could pass compilation while its risk remains untested | confident completion based on a no-op or shallow green gate | deliberate negative control and the smallest faithful boundary scenario | no code or behavior claim is being made |
| `backend_route_transfer` | Spring, Ktor, persistence, migration, auth, runtime, deployment, or production recovery owns the outcome | language guidance omitting the lifecycle that determines safety | precise handoff with target state, Kotlin interface question, owner, and return evidence | the concern remains a generic language-level library or module decision |

Categorical safety and correctness gates do not trade against an aggregate
score. A known platform-type crash, swallowed cancellation, unauthorized data
state, or incompatible public signature blocks the dependent claim even if
many lower-risk style checks pass.

**Priority selection record**

```text
task_and_accepted_outcome:
observed_target_surface:
candidate_patterns:
activated_failure_for_each:
earliest_ambiguity_hiding_boundary:
consequence_and_reversibility:
dependency_order_constraints:
verification_cost_and_fidelity:
selected_priority_order:
deferred_or_rejected_patterns:
reordering_evidence:
owner_and_review_event:
```

**Examples**

Good ordering: a Java API returns an unannotated identifier that is immediately
wrapped in a Kotlin value class. Contain and test the platform type first,
because the wrapper would otherwise make unverified non-nullness look trusted.
Then validate value-class invariants and Java call behavior.

Bad ordering: apply the historically high-scored source-map pattern by loading
all Kotlin documents, then refactor scope functions, introduce sealed results,
and add a lint plugin before checking that the task is a framework-managed
database migration. The sequence is busy but misrouted.

Interaction ordering: a retry wrapper around suspend work catches
`Exception`. Cancellation preservation precedes retry tuning because a swallowed
cancellation can keep attempts alive after the owner has stopped waiting.

Borderline ordering: a public data class may be value data or a persistence
entity. Inspect equality consumers, copying, serialization, ORM behavior, and
Java callers before prioritizing a class-form change. Record which observation
settles the route.

**Qualification and evolution**

For repeated use, evaluate priorities on representative task classes. Seed a
known boundary defect where safe, compare the route selected, record the first
causal issue found, reviewer disagreement, wrong work avoided, rework, and any
escaped consumer. Do not report an accuracy percentage without a defined
population and adequate evidence.

Promote a priority after recurring consequential escapes or a new target
boundary. Demote a manual priority when compiler, type, static-analysis, or CI
automation reliably enforces it and preserves diagnosis. Retire rows when the
mechanism or supported consumer disappears. Version durable policy changes so
incident recency does not silently reorder every future Kotlin task.

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The frozen skill defines a generic Kotlin
reliability baseline organized around explicit work modes, progressive
references, typed boundaries, null-safety, structured concurrency, Java
interop, behavior-first tests, repository wrappers, and a route to backend
delivery when framework or operational concerns lead.

`combined_evidence_inference_note`: Reliable Kotlin work contains ambiguity at
the earliest owned boundary, represents meaningful states and lifetimes
explicitly, preserves the target's supported toolchain and consumers, and
matches every consequential claim to evidence capable of disproving it.
Kotlin syntax serves that contract; syntax is not the contract.

No public source was refreshed for this evolution. Current language, coroutine,
framework, plugin, or provider behavior remains a version-bounded future fact,
not an `external_research_sourced_fact` already established here.

**Causal model**

Raw or externally owned values enter through boundaries. If nullability,
validation, identity, units, caller expectations, lifetime, blocking behavior,
or effect state remains implicit, that ambiguity spreads through otherwise
concise Kotlin code. Each downstream function must remember an unwritten rule,
tests cover only selected interpretations, and failures occur farther from the
cause.

The conservative response is:

1. identify the accepted outcome and the boundary that can make it invalid;
2. convert uncertainty once into an explicit Kotlin type, state, error, scope,
   or handoff where the target contract supports that representation;
3. keep the core non-null, immutable, ownership-aware, and small enough that
   ordinary language and compiler checks remain useful;
4. preserve uncertainty when the evidence cannot resolve it rather than using
   `!!`, generic exceptions, detached work, or an invented default;
5. verify the boundary and its failure, cancellation, compatibility, or
   recovery behavior at the lightest faithful tier.

This does not mean wrapping every primitive, replacing every exception with a
sealed hierarchy, marking every function `suspend`, or applying scope functions
for visual Kotlin style. Added structure is justified when it prevents a real
invalid state, reduces repeated boundary checks, clarifies caller obligations,
or makes a consequential transition testable.

**Default entrypoint loop**

| step | decision | evidence_to_collect | stop_or_reroute_condition |
| --- | --- | --- | --- |
| outcome | define normal, absent, invalid, failed, canceled, compatibility, and final states that matter | request, current behavior, affected users and callers, owner policy | objective or authority is unresolved enough that implementation would guess |
| target preflight | discover instructions, module, wrapper, Kotlin and JVM versions, plugins, execution mode, callers, generated code, and configured gates | repository files, dependency resolution, source and test locators | target is not Kotlin-led or another framework, data, security, or runtime owner controls the outcome |
| mode selection | choose one lead mode and named support questions | activated failure classes and ownership boundaries | several modes compete because the accepted outcome is still too broad |
| progressive retrieval | read the reference map, relevant reliability regions, then matching anti-pattern and gate material | frozen source regions and target-specific sources | additional prose cannot change the decision or target evidence is now the limiting uncertainty |
| boundary design | compare preservation and candidate representations with caller and compatibility costs | types, APIs, scopes, effects, consumers, serialization, binary and framework mechanisms | no safe intermediate state exists or migration authority is absent |
| falsifying gate | select a focused test or real-boundary scenario that can expose the causal defect | configured commands, negative case, actual artifact and environment | gate is absent, no-op, unrealistic, or unable to represent the boundary |
| reconciliation | interpret pass, fail, conditional, or inconclusive evidence and update route, code, tests, and limits | results, stronger claim not proved, residual risk, owner decision | new evidence changes the lead owner, support range, or accepted representation |

The loop is deliberately reversible. A failed Java caller compile may reveal an
interop route. A cancellation test may expose hidden blocking and require a
real adapter investigation. Framework proxy behavior may transfer leadership to
backend delivery. Rerouting is evidence of improved understanding, not failure
to follow the entrypoint.

**Ambiguity checklist**

| ambiguity | Kotlin question | common misleading shortcut | evidence that resolves it |
| --- | --- | --- | --- |
| value | Is this primitive an identifier, unit, validated string, offset, or opaque external value? | pass raw `String`, `Int`, or `Long` everywhere | construction, invalid input, round trip, caller, serialization, and interop behavior |
| absence | Does null mean missing, unknown, forbidden, invalid, not loaded, or not found? | propagate `T?` or assert with `!!` | accepted state model plus null, absent, and error boundary tests |
| outcome | Is the result space closed, extensible, exceptional, or protocol-owned? | boolean, sentinel text, or generic `Exception` | caller handling, exhaustiveness, evolution, wire, and Java behavior |
| identity and lifecycle | Is value equality and copying valid, or does the object have identity and transitions? | use a data class by default | equality, copy, persistence, framework, and state-transition scenarios |
| ownership | Who owns mutable state, a coroutine scope, child failure, or cleanup? | global singleton, `GlobalScope`, or detached launch | cancellation, child failure, concurrency, lifetime, and resource-release tests |
| execution | Does `suspend` actually suspend, or does it hide blocking or CPU-heavy work? | add `suspend` without tracing the call | dispatcher or thread observation under representative concurrency and cancellation |
| caller | Are Kotlin, Java, reflection, generated, or serialized consumers supported? | optimize only the visible Kotlin call site | signature inspection and representative caller or compatibility gates |
| evolution | Can visibility, defaults, overloads, sealed members, generics, annotations, or data shape change safely? | trust compilation of the edited module | downstream source, binary, Java, serialization, and contract evidence as applicable |
| proof | Can the selected test fail for this defect and does it execute the intended artifact? | accept a green build, filter, lint, or mocked happy path | negative control, task selection, boundary fidelity, artifact identity, and final state |

**Principle and mechanism tradeoffs**

| principle | useful_candidate | alternative_that_can_be_better | selection_boundary |
| --- | --- | --- | --- |
| contain uncertainty | parse once into a typed value or outcome | preserve a nullable or raw value at an adapter when the external state is genuinely open | choose from domain meaning, protocol evolution, caller cost, and target support |
| make meaning explicit | value class, enum, sealed interface, data class, or plain class | existing primitive or exception contract | add a type only when it removes meaningful confusion or repeated validation |
| preserve lifetime | caller-owned scope, `coroutineScope`, or deliberate lifecycle scope | synchronous or explicitly blocking API | choose from ownership, cancellation, work duration, and resource semantics |
| keep failure visible | typed outcome, typed exception, explicit nullable state, or propagated cancellation | framework or Java exception contract at an owned boundary | choose from expectedness, caller obligations, interoperability, and wire behavior |
| keep code readable | named locals and small functions | a conventional scope function | choose whichever makes receiver, side effect, and return value immediately clear |
| verify behavior | pure unit, compile, coroutine, interop, contract, or real-boundary test | owner review or conditional handoff when execution is inaccessible | use the lowest tier that still represents the causal failure |
| preserve target stance | retain versions, wrappers, plugins, analysis, and architecture | explicit migration with compatibility and rollback or roll-forward plan | migration must be accepted scope, not a side effect of idiomatic cleanup |

**Evidence ladder**

- A pure deterministic test can establish parsing, value invariants, state
  transitions, and collection behavior for controlled inputs.
- A Kotlin compile gate can establish source typing for the selected module and
  compiler configuration, but not Java usability, binary compatibility, or
  runtime semantics.
- A Java compile or adapter test can exercise names, nullability, overloads,
  exceptions, generics, and representative platform types.
- A coroutine test can establish cancellation and structured ownership only if
  its scheduler, dispatcher, blocking behavior, and final-state assertions
  represent the claim.
- A serialization or contract test can establish selected wire shapes and
  evolution cases, not every external consumer.
- A real framework, dependency, package, or platform scenario is required when
  proxying, generated code, persistence, networking, process lifecycle, or
  deployment behavior decides the outcome.
- Accountable owners decide support, risk, and policy; tests establish observed
  behavior within their scope.

An inaccessible stronger tier creates a conditional claim. It does not grant a
pass and does not make the lower-tier evidence worthless.

**Counterexamples**

An apparently idiomatic sealed result can be the wrong choice when a public
protocol is open to unknown future outcomes or Java consumers cannot use the
generated shape safely. Preserve an extensible representation until the
consumer contract is known.

A `suspend` wrapper around JDBC or a legacy SDK can be less honest than a named
blocking function if it merely hides execution cost. Inspect the actual call,
dispatcher policy, cancellation behavior, and resource bounds before choosing
the API.

A compact chain of `let`, `also`, and `apply` can preserve behavior yet make
receiver and return semantics harder to review. Named locals are more
idiomatic when they make ownership visible.

A backend route can require a non-null value object while still rejecting this
language reference as lead because migration, authorization, transaction,
traffic, or recovery state determines the accepted outcome.

**Second-order result**

When ambiguity is contained deliberately, tests become smaller, reviews can ask
which boundary owns each invariant, Java and framework handoffs become
explicit, and future changes can invalidate only dependent evidence. When the
distinction no longer matters, retire the wrapper, route, or manual check rather
than preserving abstraction for its own sake.

The thesis therefore optimizes for visible contracts and reversible evidence,
not maximum Kotlin cleverness, minimum line count, or automatic use of every
archived pattern.

## Local Corpus Source Map

The local corpus uses progressive disclosure: a compact skill selects a mode,
a reference map locates the relevant region, a deeper reliability reference
explains the mechanism, and a final anti-pattern pass challenges the result.
Apply that structure after target preflight rather than loading every file
because the request contains the word Kotlin.

All paths below are relative to
`agents-used-monthly-archive/codex-skills-202606/kotlin-coder-01/`.

| source_and_region | open_when | question_owned | important_caveat | stop_or_widen_event |
| --- | --- | --- | --- | --- |
| `SKILL.md` frontmatter and `Overview` | deciding whether the generic language skill should lead | Is this primarily reliable Kotlin library, CLI, JVM module, domain, coroutine, interop, or review work? | description is archived activation guidance, not target adoption evidence | route to backend delivery when framework, persistence, runtime, auth, migration, or operations owns the outcome |
| `SKILL.md` `When To Use` | the surface is Kotlin but the route remains ambiguous | Which concrete Kotlin surfaces and correctness concerns fit? | file extension alone does not determine ownership | inspect callers, lifecycle, data, and target policy if several surface classes overlap |
| `SKILL.md` `Mode Selection` | one or more language risks are known | Which mode leads, and which modes answer bounded support questions? | mode labels do not prescribe implementation | stop after one lead and named interfaces; reframe if all modes appear necessary |
| `SKILL.md` `Workflow` | planning or executing a consequential change | What order connects classification, requirements, references, design, coroutines, and gates? | examples such as Gradle commands are conditional on target configuration | widen to target build, consumer, or real-boundary evidence as soon as a step depends on it |
| `SKILL.md` `Output Expectations` | a plan or review needs traceable presentation | Which decision artifacts should be returned, and in what order? | output headings are a communication default, not a required code architecture | adapt to the user's requested artifact while preserving requirements, boundaries, evidence, and open questions |
| `SKILL.md` `Guardrails` | finishing a plan, implementation, refactor, or review | Which broad language mistakes must be challenged before handoff? | each guardrail activates only when its mechanism can occur | route backend concerns and retain justified exceptions with tests |
| `SKILL.md` `References` | deeper guidance is needed | Which local companions are intended by the archived skill? | link presence proves navigation, not independent corroboration | use `reference-map.md` to select exact regions |
| `references/reference-map.md` `Jump Points` | the lead mode and failure class are known | Which reliability or quality region is likely relevant? | labels are navigation summaries and omit target-specific exceptions | open the complete matching region and adjacent premise when interpretation depends on it |
| `references/reference-map.md` `Section Search` | a local copy has a compatible layout and exact headings need discovery | Which commands locate the archived regions? | commands are examples against that skill directory, not universal repository tasks | fall back to focused file and heading discovery if paths or layout differ |
| `references/reference-map.md` `Use Order` | context must remain bounded | What historical sequence did the corpus intend? | `Pattern Scoreboard` is editorial prioritization, not empirical authority | stop after the activated regions and final anti-pattern check answer the decision |
| `references/kotlin-reliability-reference.md` `Premise` and `Pattern Scoreboard` | establishing the reliability model or candidate patterns | Which ambiguity and ownership failures did the frozen corpus emphasize? | scores are uncalibrated historical values | move to the exact mechanism region and target evidence rather than applying the full list |
| `references/kotlin-reliability-reference.md` `1. Kotlin API And Type Design` | meaningful primitives, closed outcomes, value data, or raw inputs are touched | Should value classes, sealed outcomes, data classes, or parse-once boundaries represent the contract? | framework, Java, serialization, persistence, and binary consumers can constrain representation | widen to those owners and tests when generated shape or lifecycle matters |
| `references/kotlin-reliability-reference.md` `2. Nullability And Java Interop` | Java or uncertain values cross into Kotlin, or Java consumes Kotlin APIs | Where should platform types, absence, names, overloads, defaults, and compatibility become explicit? | target annotations, generated signatures, and supported consumers must be inspected | stop after adapter and caller evidence covers the accepted contract; widen for public ABI or framework generation |
| `references/kotlin-reliability-reference.md` `3. Coroutines And Flow Reliability` | suspend functions, `Flow`, scopes, cancellation, timeouts, blocking, or child failure are consequential | Who owns lifetime, failure, dispatcher use, and cleanup? | library-level guidance cannot decide application shutdown, queue ownership, or provider policy | route those lifecycle questions to backend or runtime owners and return a bounded Kotlin contract |
| `references/kotlin-reliability-reference.md` `4. Testing And Fixtures` | a Kotlin risk needs an executable specification | Which behavior-focused test and fixture expose the failure without hiding required state? | test library and fixture capabilities are target-discovered | widen to real boundary, compatibility, or package tests when unit fidelity is insufficient |
| `references/kotlin-reliability-reference.md` `5. Tooling And Build Gates` | selecting compile, test, build, format, lint, or static checks | Which repository-native gates could support the claim? | listed Gradle and Maven commands apply only if the wrapper and tasks exist | inspect build files and effective task selection; preserve skipped or absent gate limits |
| `references/kotlin-reliability-reference.md` `Kotlin Review Questions` | conducting a focused final review | Which platform, nullability, outcome, cancellation, scope-function, and test risks remain? | compact questions supplement rather than replace code, caller, and gate evidence | stop when every activated question has evidence or a named conditional boundary |
| `references/kotlin-quality-gates-and-anti-patterns.md` `High-Value Anti-Patterns` | challenging a proposed implementation or reviewing existing code | Which concise Kotlin forms can hide nullability, lifetime, receiver, state, or mutation defects? | a matched text pattern is a lead, not proof of unsafe behavior | inspect semantics and accept narrow justified exceptions with relevant tests |
| `references/kotlin-quality-gates-and-anti-patterns.md` `Default Reliability Stack` | preparing handoff or completion | Did the change preserve typed boundaries, non-null domains, cancellation, blocking honesty, tests, and configured gates? | inactive rows may be excluded only with a reason tied to absent state | widen when an exclusion depends on an uninspected caller or generated mechanism |
| `references/kotlin-quality-gates-and-anti-patterns.md` `Quality Gate Commands` | discovering target verification | Which wrapper families and search terms can orient task selection? | do not install or invent a tool because it appears in the frozen list | execute only discovered tasks and verify they select the intended tests and artifact |
| `references/kotlin-quality-gates-and-anti-patterns.md` `Review Pass` | a concise risk-based handoff is needed | Can another reviewer see nullability, interop, type, coroutine, test, and gate status? | six labels do not prove the underlying behavior | link each activated label to evidence or an explicit unresolved owner |
| `references/sources-and-research-brief.md` `Primary Sources` | reconstructing historical provenance or planning authorized refresh | Where did the archived authors report consulting Kotlin guidance? | dated source list is not a current retrieval | use exact target version and claim to select a current owning page when needed |
| `references/sources-and-research-brief.md` `Repo-Local Sources` and `Synthesis Notes` | understanding design lineage and scope separation | Which prior skill patterns influenced structure, and which backend concerns were intentionally excluded? | influence is not independent evidence for Kotlin behavior | route to the actual backend source or target owner when excluded concerns activate |

**Recommended retrieval sequence**

1. Inspect applicable target instructions, module boundaries, build roots,
   effective versions, callers, and configured tests.
2. Read the compact `SKILL.md` completely. Choose one lead mode and list any
   support-mode interface questions.
3. Read `reference-map.md` completely. Use its jump points to select only the
   relevant deeper regions.
4. Read each selected region completely, including rationale, examples, and
   caveats. Do not lift an isolated code block or bullet.
5. Read the matching anti-pattern rows and the relevant final reliability-stack
   items as a skeptical pass.
6. Return to target code, consumers, and executable gates. Archived prose is
   orientation; target evidence decides adoption.
7. Record what was intentionally not opened and the observation that would
   widen the route.

The archived map offers these navigation commands:

```bash
rg '^##|^###' references/kotlin-reliability-reference.md
rg '^##|^###' references/kotlin-quality-gates-and-anti-patterns.md
rg 'Pattern Scoreboard|High-Value Anti-Patterns|Default Reliability Stack' references/*.md
```

Use them only from a directory with that layout. In another repository, first
discover actual files with repository-native tools. Heading-like text inside a
fence must not be treated as structure.

**Retrieval examples**

Platform type: target inspection finds an unannotated Java SDK return flowing
into a non-null `UserId`. Lead with `Nullability Mode`, read `2. Nullability And
Java Interop`, then the platform-type and `!!` anti-patterns. Skip coroutine
material unless the call is suspend or cancellation-sensitive. Verify the
adapter and representative Java behavior.

Cancellation: a broad catch wraps a suspend client call. Lead with `Coroutine
Mode`, read `3. Coroutines And Flow Reliability`, then cancellation and hidden
blocking anti-patterns. Inspect the actual client and dispatcher. Widen to
backend runtime only if process shutdown, retries, or durable work ownership is
part of the accepted outcome.

Public result type: a sealed outcome is proposed for a shared JVM API. Lead
with `Type Boundary Mode`, add `Interop Mode`, read the type-design and interop
regions, then inspect Java and serialized consumers. A compile-only gate is
insufficient if binary or wire compatibility matters.

Review: a small internal collection refactor touches no raw boundary, Java
consumer, or coroutine. Read the core premise, applicable scope-function row,
and compact review pass. Do not load framework or backend references merely for
completeness.

**Map maintenance**

Verify path existence, hashes, and heading names before relying on a frozen
route. If a region moves, update navigation deliberately while preserving its
claim role. If repeated tasks require the same pair of regions, consider a
small interface checklist. If a compiler or CI gate fully enforces a stable
invariant, shorten the manual route but retain enough evidence for diagnosis.
Retire paths that no longer influence a supported decision rather than
accumulating dead context.

## External Research Source Map

`external_mapping_unrefreshed_note`: No public location was opened during this
evolution. The rows below preserve historical discovery routes and define what
a future authorized research task must establish. They do not report current
page content, releases, defaults, compatibility, maintenance, or target
behavior.

| inherited_location | future_authority_role | use_only_after | can_support_after_refresh | cannot_support_alone |
| --- | --- | --- | --- | --- |
| `https://kotlinlang.org/docs/home.html` | entry point to official Kotlin language and tool documentation | target Kotlin, JVM, platform, compiler mode, and exact claim are known | version-applicable language syntax, type, interop, convention, or API guidance from the exact owning page | target adoption, build configuration, plugin behavior, Java consumer success, or runtime outcome |
| `https://github.com/Kotlin/kotlinx.coroutines` | official coroutine library repository, tags, releases, source, and tests | effective coroutine version, target execution model, symbol, and failure question are resolved | released implementation evidence, change history, and repository-owned examples for the selected version | public API promise beyond applicable docs, target dispatcher policy, hidden blocking behavior, or packaged lifecycle |
| `https://github.com/spring-guides/tut-spring-boot-kotlin` | Spring-maintained representative application example | Spring is target-confirmed and a bounded integration vocabulary question remains | orientation to sample project shape and Kotlin-facing entry points at the inspected revision | current Spring support policy, target proxy or serialization behavior, security, persistence, release, or production readiness |
| `https://ktor.io/docs/welcome.html` | entry point to official Ktor documentation | Ktor, engine or client mode, framework version, plugin set, and exact mechanism are known | version-applicable framework semantics from the complete relevant page | target configuration, deployment lifecycle, provider policy, or observed integration behavior |

The frozen research brief also reports prior use of official Kotlin pages for
coding conventions, scope functions, sealed classes and interfaces, Java
interop, Java-to-Kotlin nullability, coroutine exception handling, and
cancellation and timeouts. A future task should navigate directly to the exact
owning page and version context when one of those claims is consequential.

**Future authority classes**

| uncertainty | preferred_external_authority | target_preflight | adoption_evidence |
| --- | --- | --- | --- |
| language rule or standard-library API | applicable official Kotlin documentation or API reference | Kotlin version, platform, compiler mode, symbol, and supported targets | compile and behavior evidence in the target module plus affected callers |
| compiler, language, or tooling change | official release notes, compatibility guide, issue, or released source where needed | current and candidate compiler versions, flags, plugins, warnings, and build tool | clean target build, generated-code checks, focused behavior, and compatibility gates |
| Java interop behavior | official Kotlin Java-interop guidance plus applicable Java or library contract | Java version, annotations, signatures, callers, overloads, exceptions, and binary consumers | representative Java compile or run, adapter tests, and API or ABI analysis where configured |
| coroutine API or semantic change | official coroutine documentation, API, release notes, and released repository evidence | coroutine version, dispatcher and scope ownership, blocking calls, timeout, retry, and failure state | cancellation, child-failure, flow, resource, and real-client scenarios in the target |
| Gradle or Maven integration | official build-tool and Kotlin plugin documentation for resolved versions | wrapper, plugin coordinates, modules, tasks, generated sources, and target JVM | repository-wrapper task selection, clean build, artifact, and negative control |
| serialization or code generation | maintainer documentation and release material for the exact plugin or library | compiler plugin, format, schema, generated API, consumers, and compatibility policy | round-trip, malformed, unknown-field, old/new, Java, and target-framework scenarios |
| binary or source compatibility | applicable Kotlin compatibility guidance plus target-approved analysis tooling | public surface, supported consumers, baselines, artifacts, and release policy | configured ABI or API report and representative downstream compilation |
| Spring Kotlin integration | versioned Spring documentation owning the precise framework mechanism | Boot or Framework versions, plugins, proxying, serialization, web mode, persistence, and lifecycle | target framework tests, packaged behavior, and backend-owner acceptance |
| Ktor Kotlin integration | versioned Ktor documentation owning the precise plugin, engine, or client mechanism | Ktor version, engine, installed plugins, configuration, client or server mode, and lifecycle | target integration, failure, package, and lifecycle scenarios |
| vulnerability or support status | maintainer advisory and target-approved security authority | exact component, transitive path, version, exposure, and sensitive-handling policy | dependency evidence, target reachability, remediation test, and accountable risk decision |

Framework authority answers framework questions. It does not replace the
generic Kotlin route for platform types or cancellation, and the Kotlin route
does not replace backend ownership for transactions, auth, migrations,
configuration, health, deployment, or recovery.

**External evidence path**

1. Write the exact target decision and the strongest currentness-dependent
   uncertainty in one sentence.
2. Resolve effective coordinates from target build and runtime evidence. Include
   platform and mode, not only a product name.
3. Identify the authority that owns the claim. Prefer a direct versioned manual,
   API, release note, compatibility guide, or advisory over open search when it
   is already known.
4. Remove private service names, customer or tenant data, credentials, internal
   URLs, incident payloads, and unreleased security details from any public
   query.
5. Retrieve the narrowest applicable source under explicit authorization.
   Record URL or revision, retrieval time, version selector, and rejected
   near-matches.
6. Read the complete relevant region, including prerequisites, defaults,
   experimental status, exceptions, deprecations, and platform restrictions.
7. Extract one bounded fact. Distinguish supported contract, example,
   implementation detail, migration advice, and historical behavior.
8. Compare it with effective target state and owner policy. Preserve conflicts
   instead of selecting the convenient source.
9. Run the target gate or scenario that can disprove the practical consequence.
10. Update only dependent guidance, tests, decisions, and runbooks. Leave
    unrelated evidence frozen.

**Reject or downgrade a result when**

- it silently redirects to latest while the target uses another release;
- it describes another platform, compiler frontend, JVM target, framework,
  engine, plugin mode, product edition, or multiplatform target;
- it is a search snippet, generated summary, forum answer, tutorial, sample,
  fork, or default-branch file used as normative compatibility evidence;
- it omits an experimental marker, opt-in requirement, prerequisite, exception,
  deprecation, migration, failure state, or Java behavior that changes the
  decision;
- it exposes implementation detail but the question concerns a supported
  contract;
- it is official for the wrong ownership layer;
- target code, configured versions, owner policy, or qualified execution
  contradict it and the conflict remains unresolved.

**Examples of correct evidence use**

Language rule: target build resolves a specific Kotlin version and a public
sealed hierarchy change is proposed. A future authorized task reads the
version-applicable official sealed-class guidance, records scope and
restrictions, then compiles Kotlin and Java consumers and runs serialization or
compatibility gates. The page does not itself prove safe evolution.

Coroutine change: target resolution identifies the coroutine version and a
retry wrapper catches broad exceptions. The future researcher uses released
docs and tag-specific repository evidence for cancellation semantics, then
executes target cancellation and client-failure scenarios. Default-branch tests
are not substituted for the released dependency.

Example orientation: a target-confirmed Spring service needs vocabulary for a
small Kotlin configuration shape. The Spring guide can orient project structure
after its revision is inspected. Versioned Spring authority and the target's
actual plugin, proxy, serialization, and lifecycle behavior still govern the
change.

Stop research when the source has bounded the supported mechanism and only
target execution or owner policy remains; when the evidence cannot resolve the
conflict; or when the answer cannot change the accepted decision. Preserve a
conditional claim instead of widening searches indefinitely.

**Future research record**

```text
research_decision_id:
target_revision_and_coordinates:
platform_execution_and_consumer_mode:
bounded_claim_and_consequence:
authority_and_lookup_path:
sensitive_context_excluded:
retrieved_at_and_version_selector:
complete_region_read:
extracted_fact_and_source_role:
prerequisites_exceptions_and_deprecations:
rejected_results_and_conflicts:
target_locator_and_owner_policy:
target_scenario_and_result:
stronger_claim_not_supported:
dependent_consumers_updated:
refresh_or_retirement_event:
```

Retain consequential research by claim, not by query volume. Revisit it when
the target coordinate, platform, compiler plugin, consumer, public contract,
maintainer ownership, advisory, or observed behavior changes. Retire public
routes whose mechanism no longer exists or whose result drives no supported
decision.

## Anti Pattern Registry Table

Registry rows are diagnostic hypotheses. A matched token or shape is not enough
for a finding. Trace the target boundary, callers, generated code, execution,
and consequence; then choose the smallest compatible repair and a gate capable
of exposing both the original defect and a regression introduced by the
repair.

| anti_pattern | causal_failure | discriminating_evidence | safer_default | exception_or_limit | verification_shape |
| --- | --- | --- | --- | --- | --- |
| keyword_only_skill_activation | `.kt` or a Kotlin phrase activates broad language guidance while another owner controls data, framework, security, runtime, or release state | accepted outcome, changed state, target owners, and lifecycle path | select one lead route from the consequential boundary and keep Kotlin as a named support interface | isolated Kotlin explanation or pure internal language change may need no adjacent route | reviewer can state why this route leads and what evidence reroutes it |
| context_free_summary_output | generic advice is produced without instructions, target versions, callers, or configured gates | compare recommendations with actual build, source, tests, consumers, and ownership | target preflight followed by progressive local regions | low-consequence conceptual explanation can remain target-neutral if it makes no adoption claim | every applied recommendation links to a target locator and bounded evidence |
| whole_corpus_context_dump | all Kotlin references are loaded regardless of risk, displacing target evidence and counterexamples | context inventory shows unrelated type, coroutine, interop, and backend material | read the compact route, one lead region, named support regions, then final activated gates | complete-file reading is warranted for source evolution or cross-cutting review | skipped regions have explicit absence reasons and widening triggers |
| source_label_as_authority | local, official, or external labels are treated as universal proof | claim lacks version, role, prerequisites, target scope, or observed result | claim-level evidence roles and stronger-claim boundary | broad orientation can use coarse labels without implementation consequence | sampled claims are entailed by their sources and target adoption is independently established |
| unverified_agent_instruction | an exact command or checklist is supplied without proving it exists, selects work, or represents the defect | wrapper, task discovery, test count, negative control, and artifact differ from prose | discover repository-native gate and qualify selection | illustrative command families may orient when clearly conditional | deliberate defect fails the intended gate and clean target passes |
| platform_type_escape | Java or generated nullability uncertainty enters non-null domain code as if proven | inspect source signature, annotations, generated stubs, adapter, and null behavior | normalize to explicit nullable, non-null, or typed failure at one adapter | trusted generated contract may be non-null after version-applicable evidence and tests | null and non-null Java boundary cases cannot leak invalid state |
| non_null_assertion_as_migration | `!!` converts unresolved input uncertainty into a distant crash | trace possible null sources, old data, Java calls, reflection, and deserialization | parse or check once, model meaningful absence, and return a bounded failure | narrow test-only fixture or proven impossible invariant may justify an assertion with rationale | malformed, absent, historical, and valid values reach accepted outcomes |
| nullable_everything_model | `T?` represents invalid, forbidden, missing, unknown, not loaded, and not found identically | callers branch inconsistently or cannot explain null semantics | non-null domain core plus sealed, enum, result, or named absence where distinctions matter | genuine optional data can remain nullable | every accepted absence state and caller obligation is tested |
| primitive_wrapper_cargo_cult | value classes wrap primitives without invariant or confusion reduction | wrapper has no distinct domain meaning and complicates Java, serialization, boxing, or framework behavior | use value classes for meaningful IDs, units, keys, offsets, or validated values after consumer review | raw primitives are appropriate for local unambiguous values | construction, equality, round trip, Java, and generated behavior match the contract |
| boolean_or_sentinel_outcome | callers must remember undocumented meanings for `true`, `false`, empty text, or magic values | call sites map the same result differently or lose new states | named enum or sealed outcome for a genuinely closed set; typed exception or extensible result otherwise | binary predicates remain clear when names make both states obvious | tests cover all states and evolution behavior at supported consumers |
| generic_exception_business_flow | expected decline, invalid, absent, conflict, or review states are hidden in broad exceptions | callers catch by message, overcatch infrastructure failures, or cannot exhaust outcomes | typed outcome or typed error at the owned boundary | protocol or Java APIs may require exceptions; adapt explicitly at the edge | expected and unexpected failures remain distinguishable across callers |
| data_class_by_default | identity-heavy, lifecycle-managed, lazy, persistent, or mutable objects receive value equality and copy semantics | equality, `copy`, destructuring, ORM, proxy, or state transition violates intent | data class for immutable value data; plain or framework-specific class for identity and lifecycle | some framework entities safely define value semantics under explicit policy | equality, copy, serialization, persistence, and lifecycle cases match expectations |
| mutable_alias_escape | a nominally immutable API exposes mutable collections or shared state through aliases | caller mutation changes internal state or races across threads | immutable snapshots, owned mutation, constructor injection, and explicit state scope | performance-sensitive ownership transfer may use mutable structures behind a strict boundary | mutation and concurrency tests show no unauthorized alias effects |
| scope_function_obscurity | nested `let`, `also`, `apply`, `run`, or `with` hides receiver, side effect, or returned object | reviewers cannot identify which value is changed or returned without simulation | named locals, small functions, or one conventional scope function | a short single-receiver expression can remain clearer than extra names | behavior is preserved and a reviewer can state receiver and result immediately |
| detached_coroutine_work | `GlobalScope` or an unowned scope lets request, command, or user-visible work outlive its owner | cancellation or parent failure leaves work running, effects ambiguous, or resources held | caller-owned scope, `coroutineScope`, deliberate lifecycle scope, or durable work handoff | process-lifetime work can use an application-owned scope with explicit shutdown | parent cancellation and failure produce accepted child and resource states |
| cancellation_swallowed_as_failure | broad catch, retry, logging, or result conversion consumes `CancellationException` | canceled work continues, retries, emits misleading errors, or commits effects | rethrow cancellation before handling ordinary exceptions and preserve cleanup | truly noncancellable cleanup must be narrow, bounded, and justified | cancel before, during, and after consequential phases and inspect final effects |
| supervisor_scope_without_independence | `supervisorScope` is used to suppress child failure without an accepted partial-success model | sibling work continues even though outcome requires atomic or coordinated failure | use ordinary structured failure or explicitly model independent child outcomes | independent best-effort children may justify supervision with result collection | one child failure demonstrates intended sibling, parent, and final outcome behavior |
| hidden_blocking_inside_suspend | a `suspend` signature wraps JDBC, filesystem, legacy SDK, native, DNS, or CPU-heavy work without isolation | dispatcher starvation, poor cancellation, timeout mismatch, and misleading callers | expose blocking honestly or isolate it through target-owned dispatcher or adapter policy | a target library may prove nonblocking behavior despite an unfamiliar API | representative concurrency and cancellation observe threads, resources, and completion |
| hardcoded_dispatcher_everywhere | implementation selects dispatchers locally without ownership or test policy | caller control, testing, fairness, and resource management fragment | inject or centralize execution policy at the appropriate application boundary | leaf adapters may use an established target convention for known blocking work | dispatcher choice and saturation behavior are exercised under target workload |
| flow_lifetime_leak | cold or hot `Flow` collection, sharing, buffer, or callback ownership outlives intended consumer | producers continue, buffers grow, callbacks leak, or cancellation does not propagate | define producer, collector, sharing, buffer, completion, and cleanup ownership | application-wide streams can be long-lived under explicit lifecycle management | collect, cancel, fail, and restart scenarios release producers and resources |
| kotlin_only_public_api_design | a public API is optimized for default parameters, extension functions, value classes, or sealed shapes without supported Java callers | Java names, overloads, nullability, exceptions, generics, boxing, or evolution become unsafe | inspect supported consumers and add explicit facade, annotations, or overloads only when justified | internal Kotlin-only APIs need not pay Java ergonomics costs | representative Java and Kotlin callers compile and observe equivalent contracts |
| generated_surface_blindness | review covers handwritten Kotlin but ignores compiler plugins, serialization, framework proxies, annotation processing, or generated stubs | executed signatures and lifecycle differ from source intuition | inspect effective plugins and generated or transformed artifact surfaces | generated internals need not be read exhaustively when stable target gates cover them | clean generated build and relevant caller or framework tests detect drift |
| public_change_without_compatibility | visibility, signature, default, overload, generic, sealed member, annotation, or serialized shape changes without consumer inventory | downstream source, binary, Java, or wire clients break after local tests pass | preserve surface or run an explicit versioned migration with compatibility evidence | private APIs with proven local consumers can use ordinary refactor gates | configured API or ABI checks and representative consumers pass or break deliberately |
| style_refactor_with_behavioral_blast | nullability, class form, coroutine shape, collection type, or exception contract changes under a cleanup label | hidden semantic and compatibility migration escapes review | split formatting from behavior and state the executable requirement for each semantic change | mechanically equivalent target-proven cleanup can remain narrow | diff classification and behavior tests show no unintended contract change |
| backend_guidance_bleed | generic Kotlin advice decides Spring, Ktor, persistence, auth, migration, health, deployment, or recovery | language-level proof omits framework and operational state | route backend delivery as lead and return only the bounded Kotlin interface | core domain or library work remains language-led even inside a service repository | framework, data, security, and lifecycle owners accept their interfaces and gates |
| test_filter_no_op | a focused test command succeeds after selecting no tests, stale output, wrong module, or mocked-away boundary | green evidence cannot detect the stated defect | qualify task, filter, fixture, negative control, and artifact identity | cached results may be valid only when all relevant inputs are part of the key | seeded failure makes the gate red and clean rerun executes expected cases |
| public_currency_overclaim | archived source or inherited URL is described as current support or best practice | version-sensitive guidance becomes authoritative without retrieval | label historical mapping, refresh exact claim when authorized, and reproduce target behavior | stable language principles may remain useful as synthesis without current-release claims | retrieval ledger and target scenario bound any current external fact |
| finding_count_as_quality | review success is measured by number of anti-pattern matches or rewritten constructs | reviewers optimize volume, raise false positives, and miss causal boundaries | prioritize severity, reachability, ownership, and evidence; allow no-finding outcomes | broad exploratory scans can enumerate leads if clearly non-verdict | sampled findings reproduce the risk and rejected matches retain reasons |

**Review protocol**

1. State the accepted behavior, supported consumers, and strongest consequence.
2. Find a registry match, but describe the target occurrence without declaring a
   defect yet.
3. Trace inputs, callers, generated surfaces, coroutine ownership, effects,
   compatibility, and framework boundaries that can make the risk reachable.
4. Identify the earliest causal boundary and the target convention that owns
   repair.
5. Compare preservation, local adaptation, compatibility migration, and route
   transfer. Avoid unrelated cleanup.
6. Write or select a negative case that fails for the causal defect. Add a
   regression guard for behavior the repair might break.
7. Classify the result as confirmed, rejected, conditional, inconclusive, or
   accepted exception with owner and expiry.
8. Promote recurring high-signal defects into type design, configured static
   analysis, compiler policy, or reusable tests where target ownership permits.

**Compact examples**

Good platform repair: an unannotated Java call returns a nullable value. The
adapter converts it into `LookupResult.Found`, `LookupResult.Missing`, or a
typed boundary error according to the accepted contract. Domain code receives
no platform type. Java null and non-null scenarios plus callers verify the
repair.

Bad null repair: replace a platform value with `value!!` because current test
data is non-null. The uncertainty is hidden until a future SDK response or old
record causes a distant crash.

Good cancellation repair: catch `CancellationException` first and rethrow it,
then classify ordinary failures. A cancellation scenario verifies that retries
stop, children end, cleanup runs, and no post-cancel effect occurs.

Borderline data class: a class appears value-like but is also serialized and
loaded by an ORM. Preserve it while inspecting copy, equality, generated
constructors, persistence identity, and wire consumers. Choose the class form
only after those observations.

**Finding record**

```text
finding_id:
target_revision_and_symbol:
registry_hypothesis:
accepted_behavior_and_consumers:
causal_path_and_reachability:
generated_framework_or_runtime_surface:
consequence_and_severity_reason:
preserve_adapt_migrate_or_route_options:
selected_repair_and_owner:
original_failure_gate:
repair_regression_gate:
result_and_remaining_uncertainty:
exception_expiry_or_invalidation:
```

Retire a manual row when its mechanism disappears or stronger target-native
prevention and diagnosis cover it. Keep enough incident or design provenance to
explain why the replacement control exists. Add a new row only for a distinct
causal state or repair interface, not another name for the same symptom.

## Verification Gate Command Set

`verification_gate_command_set`: Verify the reference artifact and the target
Kotlin claim independently. A reference pass proves document conformance. It
does not prove that a future Kotlin design compiles, preserves Java callers,
propagates cancellation, or fits a backend lifecycle.

**Exact gates for this evolved reference**

```bash
python3 tests/verify_idiomatic_reference_file.py --path idiomatic-ref-202607/kotlin_language_skill_entrypoint-20260710.md
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

The focused verifier is the assignment-specific acceptance gate. The archived
final-stage verifier is a broader frozen-corpus gate where present. Current
test evidence must report corpus-wide unfinished state separately from a clean
focused assignment; it must not edit shared queue state to manufacture green.

For a target Kotlin repository, discover the build and configured tools before
running or suggesting mutation:

```bash
rg --files -g 'build.gradle*' -g 'settings.gradle*' -g 'gradle.properties' -g 'gradlew' -g 'pom.xml' -g 'mvnw'
rg 'kotlin|jvmToolchain|languageVersion|apiVersion|ktlint|detekt|kotest|junit|mockk|turbine|kotlinx-coroutines-test' .
```

Limit the search to relevant build and configuration roots in a large
repository. Generated output and dependency caches should not be treated as
source configuration.

The frozen skill lists these candidate repository-native gate families:

| candidate_command_family | use_only_when_discovered | strongest_bounded_claim | does_not_prove |
| --- | --- | --- | --- |
| `./gradlew test` | the wrapper and applicable test task exist for the affected build | selected Gradle tests pass under resolved target configuration | Java consumer compatibility, unselected source sets, package behavior, or production lifecycle |
| `./gradlew build` | target instructions use the wrapper and build task covers intended modules | compilation, configured checks, tests, and artifacts included by that build succeed | that a particular risk was exercised or every downstream consumer was included |
| `./gradlew ktlintCheck` | the target configures that task and style is part of acceptance | configured formatting or style policy passes | type, nullability, cancellation, interop, or runtime correctness |
| `./gradlew detekt` | the target configures Detekt and applicable rules | configured static rules find no reported violation in selected sources | absence of semantic defects outside rule coverage or justified false positives |
| `./mvnw test` | Maven wrapper and target test lifecycle are authoritative | selected Maven tests pass for the resolved project and profiles | package verification, integration phases, or unsupported consumers |
| `./mvnw verify` | target policy maps verification to Maven's verify lifecycle | configured checks through the selected verify lifecycle pass | that external systems, deployment, or every compatibility surface was represented |

Do not substitute a globally installed Gradle, Maven, linter, or analyzer for a
repository wrapper and configuration without explicit target approval. Do not
add a plugin merely to make a frozen command available.

**Claim-to-gate matrix**

| claim | minimum_faithful_gate | negative_or_boundary_case | wider_gate_when_activated |
| --- | --- | --- | --- |
| raw input becomes a valid domain value or typed failure | pure parser or factory behavior test | absent, malformed, boundary, Unicode or encoding, and invariant-breaking values as applicable | serialization, CLI, environment, or Java adapter test using the actual boundary |
| platform type cannot escape | Kotlin adapter plus representative Java fake or real signature test | Java returns null despite Kotlin caller expecting a value | generated-signature, library-version, and downstream caller build when public |
| absence states remain distinct | behavior tests for every accepted state and caller branch | missing, forbidden, invalid, not found, unknown, and future state where applicable | wire, Java, or persistence compatibility tests if state crosses those boundaries |
| value-class or data-class semantics fit | construction, equality, copy, and round-trip tests | wrong identifier type, invalid value, unsafe copy, boxing or generated edge | Java caller, serialization, framework, API or ABI, and persistence tests as activated |
| sealed outcome evolution is safe | exhaustive Kotlin caller tests and compilation | new or unknown outcome reaches each supported consumer | Java, serialization, binary, protocol, and framework compatibility gates |
| cancellation propagates | coroutine test that cancels at relevant phases and observes final child state | cancel during delay, child work, catch, retry, and cleanup | real client, dispatcher, resource, worker, or package shutdown scenario |
| blocking is isolated honestly | representative concurrency and cancellation observation around the actual adapter | slow or stuck blocking call under constrained execution capacity | backend workload, pool, health, shutdown, and recovery evidence when service-owned |
| `Flow` ownership is correct | collect, cancel, fail, complete, and cleanup scenarios | collector ends while producer, callback, buffer, or sharing scope remains active | application lifecycle and resource tests for long-lived or shared flows |
| Java API is usable | representative Java source compiles and executes expected calls | null, default, overload, generic, checked exception, name, and annotation edges | configured API or ABI baseline and downstream consumer matrix |
| public API remains compatible | target-approved source or binary compatibility analysis plus consumers | deliberate incompatible change must fail the gate | release, migration, serialization, and deprecation policy evidence |
| configured style or static policy passes | actual repository task with intended source selection | known violating fixture or reversible local mutation is detected | behavior gates for the underlying risk because static success is not semantic proof |
| backend integration is safe | target framework, data, security, or runtime scenario owned by the backend route | framework proxy, binding, persistence, auth, cancellation, shutdown, or migration failure | packaged, staged, and recovery evidence as required by the accepted outcome |

**Gate selection protocol**

1. Convert the requirement into an observable failure. A phrase such as
   `make it idiomatic` is not a test contract.
2. Discover applicable instructions, wrapper, modules, source sets, tasks,
   compiler and plugin configuration, generated code, and consumers.
3. Choose the lowest-cost gate that still crosses the causal boundary.
4. Confirm task and filter selection. Record expected test count or identifiers
   where stable enough to detect an empty pass.
5. Qualify the gate with a reversible negative control, known failing fixture,
   or retained prior failure. Avoid unsafe mutation of shared baselines.
6. Run the focused gate, preserve the earliest causal failure, and do not retry
   flaky or inconclusive evidence until it happens to pass.
7. Run wider build, compatibility, or real-boundary gates only for affected
   consumers and artifacts.
8. Inspect asynchronous final state: child work, resources, callbacks, queues,
   and effects must not outlive a test unnoticed.
9. Report pass, fail, conditional, skipped, or inconclusive with the strongest
   claim not proved.
10. Re-run selectively when implementation, version, consumer, fixture,
    compiler, plugin, task selection, or environment changes.

**Kotlin/JVM caveats**

- Virtual time can prove logical delay and timeout behavior but is not
  wall-clock performance evidence and cannot make real blocking cooperative.
- A coroutine test must not finish while detached children or callbacks remain
  active. Assert completion, cancellation, cleanup, and final effects.
- Mixed Java and Kotlin compilation order, generated sources, annotation
  processing, compiler plugins, and framework transformations may change the
  public or executed surface.
- A Kotlin compilation does not prove binary compatibility with a previously
  published artifact or usability from Java.
- A serialization happy path does not prove unknown-field, historical-data,
  malformed-input, or old/new compatibility.
- A lint or static-analysis pass is limited to configured rules, sources,
  baselines, and suppressions. Inspect those inputs before interpreting green.
- A broad build can bury the first causal error; run the focused gate first and
  retain the wider regression result separately.

**Result semantics**

| result | interpretation |
| --- | --- |
| pass | qualified gate selected the intended behavior and observed the accepted result for the recorded target state |
| fail | gate produced interpretable evidence that contradicts a requirement or hard boundary |
| conditional | available gate proves a narrower layer while a material consumer, environment, or owner remains unavailable |
| skipped | gate was deliberately omitted with an absent-boundary or authority reason and an event that reopens it |
| inconclusive | flakiness, no-op selection, cache uncertainty, contamination, environment failure, or asynchronous leakage prevents interpretation |

Do not average these states. A failed cancellation or compatibility gate is not
canceled by passing style checks.

**Verification evidence record**

```text
requirement_and_failure:
target_revision_module_and_artifact:
wrapper_versions_plugins_and_source_sets:
gate_command_or_scenario:
selection_and_cache_state:
fixture_and_environment:
negative_control:
observed_result_and_exit_status:
async_resource_and_effect_final_state:
result_classification:
stronger_claim_not_proved:
skipped_or_inaccessible_boundary:
evidence_locator:
owner_and_invalidation_event:
```

Keep evidence summaries concise and access-safe. Store detailed logs only where
target policy permits, and never paste credentials, private payloads, or broad
incident output into a generic record.

Review gate health from escaped defects, false positives, flakiness, runtime,
selection failures, and consumer coverage. Promote stable invariants into
compiler, type, or configured static controls where feasible. Quarantine or
repair unreliable gates. Consolidate duplicates only after proving that the
remaining gate preserves failure detection and diagnosis.

## Agent Usage Decision Guide

`agent_usage_decision_guide`: Use this reference when Kotlin language
reliability owns the requested decision or when another route asks a precise
Kotlin interface question. Do not activate it solely from a keyword, file
extension, or nearby framework.

**Fast route**

1. What action did the user request: explain, plan, implement, refactor, review,
   debug, migrate, or assess compatibility?
2. What target surface changes: value, API, Java boundary, coroutine lifetime,
   flow, build, test, generated code, framework, data, or runtime lifecycle?
3. Which failure has the strongest consequence, and who owns it?
4. Can a Kotlin language gate represent that failure? If not, route the overall
   outcome elsewhere and keep only a bounded language question.
5. Which one of the seven frozen modes leads, which sources are relevant, and
   what evidence will stop or reroute work?

**Usage profiles**

| profile | choose_when | required_context | expected_output | completion_boundary |
| --- | --- | --- | --- | --- |
| direct_explanation | user needs a bounded concept or existing snippet explained and no target mutation is implied | provided code, terms, and any explicit version context | concise explanation, caveat, and example appropriate to the question | user question is answered without claiming uninspected target behavior |
| core_language_implementation | pure or mostly internal Kotlin logic, collections, extensions, visibility, or package design leads | instructions, module, callers, existing conventions, types, and focused tests | executable requirement, smallest design, implementation, focused tests, configured regression gates | behavior passes and no raw, Java, coroutine, public, or backend boundary was missed |
| nullability_boundary | nullable, Java, reflection, generated, serialized, or old-data uncertainty enters Kotlin | exact origin signature, annotations, adapter, consumers, domain semantics, malformed and absent cases | explicit boundary conversion with non-null core or meaningful absence model | platform uncertainty does not escape and representative callers observe accepted states |
| type_and_api_design | identifiers, units, parsed values, DTOs, states, outcomes, or public APIs change | invariant, state space, equality, copy, serialization, Java, binary, and framework consumers | preserve or introduce a representation with migration and compatibility reasoning | invalid states and caller obligations are explicit at all activated boundaries |
| coroutine_and_flow | suspend, `Flow`, child work, timeout, dispatcher, retry, blocking, or cleanup changes | owner scope, call tree, execution resources, cancellation, effects, lifecycle, and tests | structured lifetime design, blocking policy, failure model, and phase-based tests | cancellation, failure, completion, resources, and effects reach accepted final states |
| java_interop_and_compatibility | Java calls Kotlin, Kotlin calls Java, or a public JVM surface evolves | Java version, signatures, annotations, defaults, overloads, names, exceptions, generics, artifacts, and support policy | explicit interop facade or preserved surface plus caller and compatibility evidence | representative supported consumers pass or a versioned breaking change is accepted |
| testing_design | behavior is ambiguous or a boundary lacks a faithful gate | requirement, failure class, target test stack, fixtures, clock, dispatcher, dependency, and artifact | verification matrix, negative control, fixtures, and smallest faithful tests | the gate detects the defect, passes clean behavior, and states stronger tiers not proved |
| risk_focused_review | existing change needs findings rather than implementation | diff, target context, callers, build, generated code, tests, and accepted contract | findings ordered by consequence with file locators, evidence, uncertainty, and missing tests | every finding is reachable and actionable; no-issue result states residual risk honestly |
| exploratory_discovery | legacy or greenfield surface lacks enough facts to select a design | instructions, architecture and dependency map, representative symbols, consumers, constraints, and owners | bounded hypotheses, preserved options, discriminating observations, and stop point | one route becomes evidence-backed or the unresolved decision is handed to its owner |
| language_support_for_backend | backend delivery owns framework, persistence, security, runtime, or release while Kotlin semantics form one interface | lead route outcome, exact Kotlin boundary question, target versions, mechanism, and required return evidence | bounded language decision and tests returned to the integration owner | backend route reconciles the result through framework, data, package, and lifecycle evidence |
| stop_and_clarify | outcome, target, authority, supported consumers, or irreversible migration state is missing | known evidence, conflict, consequence, and person or artifact that can resolve it | explicit blocker or conditional decision with smallest next question | missing authority or evidence arrives; no speculative implementation proceeds |
| no_change | proposed Kotlin abstraction or cleanup lacks a meaningful invariant, safety gain, or compatible migration | current behavior, consumer burden, alternatives, test evidence, and maintenance cost | preservation decision plus any targeted test or documentation improvement | rejected change remains unnecessary unless an invalidation event occurs |

Several profiles may contribute, but one must lead. For a public suspend API
used from Java, `java_interop_and_compatibility` may lead if consumer breakage is
the dominant consequence, while `coroutine_and_flow` answers lifetime and
cancellation. Do not create two independent plans for the same API.

**Preflight before mutation**

- Read applicable workspace, repository, and directory instructions.
- Inspect working-tree state and preserve user or collaborator changes. Do not
  revert or broadly reformat unrelated files.
- Identify the owned files and decision record. Shared work requires one writer
  per artifact or an explicit merge owner.
- Discover build roots, wrappers, effective versions, source sets, generated
  code, tests, public consumers, and configured static gates.
- State changed and deliberately unchanged behavior. Separate Kotlin language
  scope from framework, data, security, runtime, and release scope.
- Select a negative or boundary case before implementation when behavior is
  being changed.
- Confirm that commands, external research, destructive actions, commits,
  pushes, and production mutations are authorized before performing them.
- Keep credentials, private payloads, customer data, and sensitive incident
  material out of prompts, public queries, logs, and generic evidence records.

**Profile-specific source loading**

| profile | local_regions | target_evidence_that_must_dominate |
| --- | --- | --- |
| nullability_boundary | `Nullability Mode`, `2. Nullability And Java Interop`, platform-type and non-null assertion rows | actual signatures, annotations, generated surfaces, callers, domain absence, and null behavior |
| type_and_api_design | `Type Boundary Mode`, `1. Kotlin API And Type Design`, type-related anti-patterns | state space, invariants, equality, copy, wire, Java, binary, framework, and migration policy |
| coroutine_and_flow | `Coroutine Mode`, `3. Coroutines And Flow Reliability`, cancellation and blocking rows | scope ownership, actual client behavior, dispatcher policy, effects, lifecycle, resources, and cancellation evidence |
| java_interop_and_compatibility | `Interop Mode`, interop region, public-compatibility rows | supported Java consumers, signatures, artifacts, baselines, release policy, and caller gates |
| testing_design | `Testing Mode`, `4. Testing And Fixtures`, quality-gate regions | configured test libraries, real failure, fixture fidelity, task selection, artifact, and result |
| risk_focused_review | `Review Mode`, activated reliability regions, final review pass | diff, callers, generated code, execution, configured gates, and accepted exceptions |
| language_support_for_backend | only regions needed for the interface question | lead route's framework, data, security, package, operational, and recovery evidence |

**Handoff contract**

When another route must lead, transfer the smallest sufficient state:

```text
accepted_outcome_and_lead_owner:
target_revision_module_and_artifact:
kotlin_interface_question:
observed_types_callers_scopes_and_effects:
effective_versions_and_generated_mechanisms:
language_options_and_rejected_alternatives:
focused_gate_and_result:
remaining_framework_data_or_runtime_uncertainty:
decision_or_evidence_requested:
return_recipient_and_invalidation_event:
```

Do not pass an unbounded transcript or private logs. A specialist returns a
decision, evidence, limits, and reroute condition; the integration owner
reconciles it with the full outcome.

**Examples**

Review profile: a diff changes a nullable Java SDK response to `value!!` and
adds a value class. Inspect the exact Java signature and adapter, identify the
reachable null state, review value semantics and consumers, and report the
crash risk plus missing null case before discussing style. If no null is
possible under an applicable contract, record that evidence instead of forcing
a rewrite.

Implementation profile: a CLI parser currently returns raw strings throughout
domain logic. Write behavior requirements for valid, absent, malformed, and
boundary arguments; parse once into target-compatible types; keep errors at the
CLI boundary; run focused parser tests and the discovered build gate. Do not
load backend runtime guidance.

Coroutine profile: a `Flow` adapter registers a callback and never unregisters
it after collection cancellation. Trace producer and collector ownership,
implement bounded cleanup using the target library contract, and test cancel,
failure, normal completion, and callback release. Widen only if an application
lifecycle scope owns sharing.

Backend support profile: a Spring service exposes a sealed domain outcome.
Language guidance evaluates whether states are closed and Kotlin or Java
callers are exhaustive. Backend delivery remains lead for proxying,
serialization, status mapping, auth, transactions, package, and operation.

Bad keyword activation: a task says `Kotlin service migration`, so the agent
loads every language reference and redesigns types before inspecting schema,
old and new artifacts, data state, deployment order, or recovery. The route is
wrong even if the new types compile.

Borderline profile: a shared data class might be internal value data or a
published serialized and Java-consumed contract. Enter exploratory discovery,
inspect consumers and artifact policy, and preserve the class until evidence
selects type design or compatibility work.

**Usage acceptance**

A route is acceptable when it names the outcome, lead owner, target facts,
activated failure, focused sources, changed and unchanged scope, falsifying
gate, evidence result, stronger claim not proved, and next stop or handoff. It
is not acceptable merely because the final code looks idiomatic or many local
sources were quoted.

For repeated agent use, review wrong routes, needless source loading, skipped
consumers, handoff loops, rework, and escaped defects across representative task
classes. Optimize context and tool count only while holding decision quality
and verification fidelity constant. Retire profile outputs that no consumer
uses, and sharpen triggers when the same ownership mistake recurs.

## User Journey Scenario

This illustrative journey shows how to route a mixed Java/Kotlin boundary. It is
not evidence that the interfaces, task names, annotations, or result type exist
in a future repository.

**Opening request**

A maintainer asks: "Remove a non-null assertion from our shared JVM directory
adapter, make the Kotlin API safer, and keep existing Java callers working. The
lookup is used from a coroutine flow."

The request appears small, but it activates four distinct questions:

- `Nullability Mode` leads because an unannotated Java return becomes trusted
  Kotlin state.
- `Interop Mode` owns Java caller shape and compatibility.
- `Coroutine Mode` owns lifetime, blocking isolation, and cancellation at the
  Kotlin call site.
- `Testing Mode` selects the failure and consumer evidence.

Backend delivery does not lead yet. It joins if the gateway is remote and the
accepted outcome includes authentication, retry, rate limits, service health,
process shutdown, or deployment recovery.

**Target preflight**

Before editing, inspect:

1. applicable instructions and the working tree;
2. the actual Java signature, nullability annotations, documented not-found and
   failure behavior, and whether the call blocks;
3. every Kotlin and Java caller, including generated or reflective access;
4. current Kotlin, JVM, coroutine, compiler-plugin, and build-wrapper state;
5. public artifact and compatibility policy;
6. existing tests, Java fixtures, dispatchers, API baselines, and task
   selection;
7. whether `null`, exception, empty text, or another provider result currently
   represents not found.

Suppose target inspection establishes this bounded current surface:

```java
public interface DirectoryGateway {
    String findDisplayName(String userId);
}
```

The return has no applicable nullability annotation. Kotlin therefore sees a
platform type. The current adapter contains a pattern equivalent to:

```kotlin
suspend fun loadDisplayName(userId: String): String =
    withContext(directoryDispatcher) {
        gateway.findDisplayName(userId)!!
    }
```

Do not infer from this sketch that `directoryDispatcher` is correctly owned,
that the Java call is interruptible, or that null means not found. Those are
target facts to establish.

**Executable requirements**

Use target identifiers and revision them under the repository's convention.
The scenario's requirements are:

```text
REQ-KOTLIN-101.0
WHEN the Java gateway returns a non-null display name
THEN the adapter SHALL return the validated found state
AND SHALL NOT expose a platform type beyond the adapter.

REQ-KOTLIN-102.0
WHEN the Java gateway returns null under the documented not-found condition
THEN the adapter SHALL return the explicit missing state
AND SHALL NOT throw a non-null assertion failure.

REQ-KOTLIN-103.0
WHEN directory work is canceled
THEN the Kotlin coroutine boundary SHALL preserve cancellation
AND SHALL NOT normalize cancellation into missing or provider failure.

REQ-KOTLIN-104.0
WHEN a supported Java caller uses the public facade
THEN its source and runtime contract SHALL remain compatible
UNLESS an approved versioned migration explicitly changes that contract.

REQ-KOTLIN-105.0
WHEN the provider reports an ordinary failure
THEN the adapter SHALL preserve a distinguishable failure path
AND SHALL NOT collapse it into the missing state.
```

The null requirement is conditional on target evidence that null really means
not found. If that meaning is unknown, stop and obtain provider or owner
authority rather than inventing it.

**Representation options**

| option | benefit | cost_or_risk | choose_when |
| --- | --- | --- | --- |
| preserve current `String` and replace assertion with local failure | smallest public change | may retain ambiguous missing and failure semantics | current contract intentionally promises a value and null represents a contract breach |
| return `String?` | simple representation of one meaningful absence | callers can conflate missing, unknown, forbidden, and provider failure; public surface may break | exactly one absence state exists and consumers can migrate safely |
| throw a typed not-found exception | fits exception-oriented Java or framework contracts | expected state becomes control flow and cancellation or provider failures can be overcaught | target policy and supported callers use typed exceptions consistently |
| return a standard result wrapper | separates success and failure | nested null or ad hoc error types can remain ambiguous; Java ergonomics vary | target conventions define error and absence semantics clearly |
| introduce a sealed lookup outcome | exhaustive closed states and explicit caller handling | public, Java, serialization, and future-state evolution may become more complex | state space is owned and closed, or the type remains internal behind a compatible facade |
| keep an internal sealed outcome and preserve a public facade | contains uncertainty while allowing staged consumer migration | two surfaces and mapping logic must remain coherent | public consumers cannot change atomically and the internal distinctions are valuable |

Assume target evidence establishes three internal outcomes: found, missing, and
provider failure. A target-adapted internal design could be:

```kotlin
sealed interface DirectoryLookup {
    data class Found(val displayName: String) : DirectoryLookup
    data object Missing : DirectoryLookup
    data class Failed(val cause: DirectoryFailure) : DirectoryLookup
}

sealed interface DirectoryFailure {
    data class ProviderRejected(val message: String) : DirectoryFailure
    data class Unexpected(val cause: Throwable) : DirectoryFailure
}
```

Do not automatically expose `Throwable` across a public or serialized boundary.
The example keeps it internal; a real target decides error redaction,
classification, and public contract.

An adapter sketch can contain the platform type immediately:

```kotlin
class JavaDirectoryAdapter(
    private val gateway: DirectoryGateway,
) {
    fun lookupBlocking(userId: String): DirectoryLookup =
        try {
            gateway.findDisplayName(userId)
                ?.let { displayName -> DirectoryLookup.Found(displayName) }
                ?: DirectoryLookup.Missing
        } catch (error: DirectoryProviderException) {
            DirectoryLookup.Failed(
                DirectoryFailure.ProviderRejected(error.message.orEmpty()),
            )
        }
}
```

This sketch is intentionally blocking and contains no coroutine catch. The
application or owning adapter layer can isolate it according to target
execution policy:

```kotlin
class SuspendingDirectoryLookup(
    private val adapter: JavaDirectoryAdapter,
    private val blockingContext: CoroutineContext,
) {
    suspend fun lookup(userId: String): DirectoryLookup =
        withContext(blockingContext) {
            adapter.lookupBlocking(userId)
        }
}
```

`withContext` preserves coroutine cancellation at its boundary, but it does not
magically make a noncooperative Java call interruptible. The target must decide
dispatcher capacity, client timeout, resource release, and what happens when
the caller stops waiting. If those decisions affect a service, route them to
backend delivery.

If additional exception normalization is needed around suspend work, preserve
cancellation explicitly:

```kotlin
try {
    performSuspendLookup()
} catch (error: CancellationException) {
    throw error
} catch (error: DirectoryProviderException) {
    recordProviderFailure(error)
}
```

Do not copy that catch structure when the target exception hierarchy differs.
Catch only failures the boundary actually owns.

**Compatibility facade**

If an existing Java API returns nullable `String`, an internal sealed state can
be introduced without changing it immediately:

```kotlin
class DirectoryFacade(
    private val lookup: JavaDirectoryAdapter,
) {
    fun findDisplayName(userId: String): String? =
        when (val result = lookup.lookupBlocking(userId)) {
            is DirectoryLookup.Found -> result.displayName
            DirectoryLookup.Missing -> null
            is DirectoryLookup.Failed -> throw mapFailure(result.cause)
        }
}
```

This mapping is valid only if it exactly preserves the accepted Java contract.
If errors were historically returned as null, changing them to exceptions is a
behavioral migration and needs explicit approval and consumer evidence.

**Test-first evidence**

Begin with the failure that motivated the change. A representative test matrix
is:

| test | failure_it_must_detect | accepted_observation |
| --- | --- | --- |
| Java gateway returns a name | adapter accidentally rejects or transforms valid data | found state contains the expected value and no platform type escapes |
| Java gateway returns null | assertion or implicit assignment crashes | explicit missing state is returned under the target-owned null contract |
| Java gateway throws known provider failure | implementation collapses failure into missing | provider failure remains distinguishable and redacted as required |
| caller cancels before lookup | work starts despite canceled ownership | suspend boundary does not begin unwanted work and cancellation remains cancellation |
| caller cancels during controlled wait | broad catch converts cancellation or retries | cancellation propagates and final resource or effect state is accepted |
| Java facade caller compiles and runs | Kotlin-only shape breaks names, nullability, overloads, or exceptions | supported Java call observes preserved contract |
| compatibility baseline compares public artifact | local source compiles while published surface drifts | no unapproved source or binary break is reported |
| configured build and regression tasks run | focused fixture passes while another affected module fails | intended modules, tests, generated sources, and artifacts are covered |

The Java test double should originate from Java or an equivalent generated
signature. Replacing it with a safe Kotlin `String?` interface can hide platform
uncertainty and weaken the gate.

Use a negative control. Temporarily restore the non-null assertion or inject a
platform null in an isolated test and confirm the focused gate fails for the
expected reason. Then restore the repair and rerun. Do not mutate a shared
published compatibility baseline without authorization.

**Result and handoff**

A strong local result can establish that:

- the platform type is contained in one adapter;
- found, missing, and owned provider failure remain distinct for tested inputs;
- selected cancellation paths preserve cancellation;
- representative Java callers retain the approved facade contract;
- configured target tasks and selected regressions pass.

It cannot establish untested provider semantics, noncooperative blocking
termination, all downstream binaries, production capacity, or service shutdown.
Those remain conditional and are handed to the provider, artifact, or backend
owner with exact target state and evidence.

**Bad journey**

Search for a Kotlin best practice, replace the assertion with a sealed class,
mark the method `suspend`, catch `Exception` into `Missing`, and run a Kotlin
unit test. This appears idiomatic but can break Java callers, swallow
cancellation, hide provider failures, and leave blocking work unchanged.

**Feedback after adoption**

Track new provider states, recurring adapter failures, Java migration burden,
cancellation escapes, and duplicated mappings. If the provider outcome set
becomes open, reconsider a sealed public contract. If all consumers migrate to
the explicit outcome, retire the compatibility facade after evidence. If the
adapter no longer crosses Java or blocking boundaries, simplify the route and
tests rather than preserving accidental complexity.

## Decision Tradeoff Guide

Use this guide after target preflight. Agreement among archived sources is not
enough to adopt a pattern, and disagreement does not automatically require a
rewrite. The decision must account for the target contract, consumers,
execution, migration, evidence, and reversibility.

**Decision forms**

| decision | choose_when | principal_benefit | principal_cost_or_risk | required_evidence |
| --- | --- | --- | --- | --- |
| preserve | current representation satisfies accepted behavior and the proposed pattern removes no meaningful ambiguity | smallest blast radius and no migration burden | can retain a latent defect if the assessment misses a boundary | target callers, failure cases, and configured gates support current contract |
| contain_locally | one adapter, parser, scope, or private type owns the defect and a safe intermediate state exists | fixes the earliest cause without changing broad consumers | mapping layer and local complexity must remain maintained | focused failure plus affected local callers and regression gate |
| adapt_pattern | frozen guidance is useful but target conventions, versions, consumers, or framework mechanisms require another shape | keeps the principle while respecting repository support | adaptation may weaken the original guarantee or introduce custom behavior | explicit principle, target constraint, rejected direct adoption, and target gate |
| compose_modes | one accepted outcome crosses distinct language risks with one lead owner | preserves specialist depth without duplicating the full plan | interface mismatch and context growth | lead mode, support questions, returned evidence, and integration scenario |
| compatibility_facade | internal contract should improve while public Kotlin, Java, binary, or wire consumers cannot change atomically | enables staged migration and local clarity | duplicate surfaces, translation defects, and delayed removal | consumer inventory, mapping tests, version policy, and retirement gate |
| breaking_migration | current public contract is unsafe or cannot support the accepted outcome and owners accept coordinated change | removes structural debt and can simplify the final design | downstream breakage, release coordination, data or wire incompatibility | versioned requirements, migration path, consumer evidence, stop and recovery plan |
| defer | decisive consumer, provider, version, policy, or execution evidence is temporarily unavailable | prevents speculative irreversible design | leaves current risk or blocks delivery | bounded missing fact, consequence, owner, containment, and next gate |
| route_away | framework, persistence, security, build migration, runtime, or production lifecycle owns the outcome | puts authority and evidence with the correct specialist | handoff cost and possible route loops | exact interface question, target state, lead owner, and required return evidence |
| reject | candidate adds no invariant, safety, clarity, or maintainability sufficient to justify its burden | avoids abstraction cargo cult and needless churn | may miss a future need if assumptions change | comparison with preservation, target evidence, and reopening event |
| temporary_containment | immediate harm must be bounded before durable design or migration is available | reduces current consequence quickly | workaround can hide cause and become permanent | owner, duration condition, monitoring, durable correction, and removal proof |

Preservation is the starting stance for toolchain, versions, plugins,
architecture, public surfaces, and unrelated code. It is not permission to
preserve a confirmed crash, cancellation leak, data violation, or unsupported
consumer break. Contain confirmed harm while keeping unrelated choices stable.

**Representation tradeoffs**

| decision_surface | candidate | works_well_when | becomes_wrong_when | verify |
| --- | --- | --- | --- | --- |
| meaningful primitive | value class | identifier, unit, key, offset, or validated value has a stable invariant and target consumers support the generated form | wrapper adds no semantic protection or conflicts with Java, serialization, framework, reflection, boxing, or ABI constraints | construction, invalid input, equality, round trip, Java, generated, and compatibility behavior as activated |
| optional value | nullable type | exactly one meaningful absence exists and callers can handle it without losing cause | null conflates missing, invalid, forbidden, unknown, not loaded, or provider failure | every absence and caller branch, including raw boundary conversion |
| closed state space | sealed interface or class | owner controls all variants and exhaustive handling is valuable | protocol is open, unknown future states must pass through, Java or wire consumers cannot evolve safely | Kotlin exhaustiveness plus Java, serialization, binary, and unknown-state behavior where relevant |
| small fixed category | enum | states carry little variant data and stable names or codes are defined | variants need distinct payloads or external numeric and text codes evolve independently | mapping, unknown input, serialization, and consumer compatibility |
| value data | data class | immutable properties fully define equality, copy, and destructuring semantics | identity, lifecycle, lazy loading, proxying, persistence, or mutable transitions matter | equality, copy, destructuring, serialization, persistence, and framework behavior |
| identity or lifecycle object | plain or framework-specific class | state transitions and identity need controlled methods and equality | class ceremony adds no protection to simple immutable data | lifecycle, identity, state-transition, and framework tests |
| expected domain outcome | typed result or sealed outcome | callers should handle explicit accepted states | state set is open or target contract requires exception, null, or protocol-specific representation | all outcomes, caller handling, evolution, and boundary mapping |
| exceptional failure | typed exception | target Java or framework contract is exception-oriented and failure is not ordinary domain flow | callers must parse messages or broad catches hide cancellation and infrastructure faults | exception type, cause, Java behavior, cancellation, and mapping tests |
| execution API | synchronous or explicitly blocking function | work is inherently blocking and caller or application owns isolation | callers are misled about latency or block constrained execution without policy | representative execution, resource, timeout, and caller behavior |
| suspend API | suspend function with structured ownership | operation cooperates with cancellation or deliberately isolates blocking work | signature merely hides blocking, detached work, or an unowned scope | cancellation at phases, child failure, threads or dispatchers, resources, and effects |
| concise receiver logic | one scope function | receiver, side effect, and return value remain immediately obvious | nesting or mixed functions obscures object identity and result | behavior test and reviewer readback |
| explicit local flow | named locals and small functions | multiple values, side effects, branches, or return semantics need names | fragmentation obscures one simple transformation | behavior and readability review under target conventions |

**Compatibility and migration dimensions**

Before changing a non-private surface, inspect:

- Kotlin source callers and default or named argument use;
- Java names, overloads, defaults, nullability annotations, exceptions, generics,
  value-class representation, and static access;
- binary consumers and published artifact policy;
- reflection, dependency injection, framework proxies, compiler plugins, and
  generated code;
- serialization, unknown states, schema, persistence, and historical data;
- coroutine, callback, thread, dispatcher, and lifecycle ownership;
- test fixtures, documentation, scripts, and downstream examples;
- deprecation, coexistence, migration, rollback or roll-forward, and retirement.

A private declaration is not automatically isolated: reflection, generated
code, serialization, tests, and framework access can create effective
consumers. Conversely, not every internal change needs public compatibility
machinery. Trace actual reachability.

**Decision procedure**

1. State the accepted outcome, current contract, and strongest consequence.
2. Inventory consumers and ownership at value, caller, artifact, wire, runtime,
   and backend boundaries.
3. Name preservation and at least one feasible alternative. Include no-change
   rather than comparing only favored rewrites.
4. Eliminate candidates that violate a hard correctness, security, data,
   cancellation, compatibility, or authority gate.
5. For remaining options, compare ambiguity removed, caller burden,
   extensibility, migration, target convention, testability, runtime cost,
   operational effect, and reversibility.
6. Identify safe intermediate states. If none exist, route to a coordinated
   migration rather than pretending the refactor is local.
7. Use the least expensive evidence able to discriminate the options. A small
   prototype or signature analysis can remain exploratory.
8. Record the selected option, rejected alternatives, uncertainty, owner, and
   event that reopens the decision.
9. After adoption, compare predicted and observed caller, defect, performance,
   and maintenance effects. Retire temporary compatibility layers when their
   exit gates pass.

**Worked tradeoffs**

Platform null: an unannotated Java value can be absent. `value!!` is eliminated
by a local adapter. If null means one normal absence, `T?` may be enough. If
null, forbidden, and provider failure differ, use a target-compatible explicit
state internally. Preserve the public facade until consumers can migrate.

Primitive identifier: a raw string is passed among two internal functions and
cannot be confused with another value. A value class adds no current invariant;
reject it. If the identifier crosses many call sites alongside other strings
and has validation rules, reconsider with Java and serialization evidence.

Public sealed result: exhaustive Kotlin handling is attractive, but a public
protocol can introduce unknown future outcomes and Java callers require stable
interop. Keep an extensible wire representation, parse known states internally,
and preserve an unknown state if the protocol owns extension.

Coroutine wrapper: a legacy client blocks. Simply adding `suspend` is rejected.
Either keep an explicit blocking port and let the application own isolation or
adapt through an approved bounded execution context. If service capacity and
shutdown matter, backend delivery leads those decisions.

Scope-function cleanup: replacing clear named locals with nested `let` and
`also` reduces lines but obscures receiver and return value. Preserve the named
flow. Idiomatic Kotlin favors clarity over visual density.

**Decision record**

```text
decision_id_and_owner:
accepted_outcome_and_current_contract:
target_revision_versions_and_consumers:
activated_modes_and_failure:
preservation_option:
candidate_options:
hard_gates:
tradeoff_dimensions_and_evidence:
safe_intermediate_states:
selected_option_and_rationale:
rejected_options_and_reopening_events:
focused_and_compatibility_results:
forecasted_caller_migration_and_runtime_cost:
observed_followup:
temporary_mechanism_retirement:
```

**Cost of being wrong**

Wrong language guidance can create crashes from platform values, lost
cancellation, continued effects after caller exit, ambiguous domain states,
Java or binary breaks, wire incompatibility, framework failures, unbounded
adapter layers, or tests that protect the wrong contract. It can also waste a
development loop by sending an agent to unrelated files and tools.

Assess both directions: harm from leaving the current design and harm created
by the proposed repair. A reviewer should know what to revert, which consumers
to inspect, what state cannot be recovered automatically, and which owner must
decide next.

Review durable decisions when target versions, consumers, state ownership,
frameworks, generated mechanisms, incident evidence, or support policy changes.
Remove temporary facades and compatibility gates only after consumer evidence
shows they are no longer needed.

## Local Corpus Hierarchy

Use hierarchy to route a claim, not to grant one file universal precedence. The
frozen corpus is a designed stack whose members own different questions.

| frozen_source | integrating_role | leads_for | supports_but_does_not_lead | evidence_limit |
| --- | --- | --- | --- | --- |
| `SKILL.md` | entrypoint and scope integrator | activation, seven work modes, workflow order, output expectations, guardrails, backend route, and companion links | mechanism rationale and examples summarized from deeper files | archived prompt contract; cannot establish current target or external behavior |
| `references/reference-map.md` | progressive-disclosure navigator | jump points, heading search, and historical read order | subject-matter decisions after the region is opened | navigation metadata; cannot prove the selected pattern applies |
| `references/kotlin-reliability-reference.md` | generic Kotlin mechanism explainer | frozen rationale and examples for API and type design, nullability, Java interop, coroutines, testing, and build gates | entrypoint selection and final target adoption | generic historical guidance; omits many framework, consumer, and version specifics |
| `references/kotlin-quality-gates-and-anti-patterns.md` | skeptical completion challenger | frozen anti-pattern causes, safer candidates, reliability stack, gate families, and compact review | detailed mechanism design and source provenance | pattern matches and command suggestions require target qualification |
| `references/sources-and-research-brief.md` | dated provenance and refresh planner | what the local corpus reports researching on 2026-06-23 and which scope was deliberately generic | current source discovery and synthesis history | reports past research; does not refresh public facts |

The roles above are direct where the source states them and synthesis where this
reference names their integrating relationship. None is target policy.

**Authority layers by claim**

| claim_class | first_local_route | decisive_target_or_external_authority | final_evidence_owner |
| --- | --- | --- | --- |
| should this skill activate? | `SKILL.md` description, use cases, modes, and guardrails | applicable instructions, user outcome, target ownership, and changed state | integration owner accepting the route |
| where is local guidance? | `reference-map.md` | exact frozen or live source layout and complete relevant region | reader or agent documenting selected and skipped regions |
| what generic Kotlin risk should be considered? | relevant reliability and anti-pattern regions | version-applicable language or library authority when semantics are currentness-sensitive | target implementation and review evidence |
| what does the target use? | local sources only suggest discovery questions | build resolution, source, generated artifacts, tests, configuration, and callers | target repository evidence at a named revision |
| what is supported publicly? | research brief supplies historical starting points | applicable current primary documentation, release, advisory, or maintained source | future authorized research record |
| what behavior occurred? | local doctrine selects a scenario | qualified target test, compatibility gate, real boundary, or incident observation | recorded result with artifact, environment, input, and final state |
| what risk is acceptable? | guardrails frame concerns | accountable service, library, security, data, platform, or release owner | owner decision under applicable policy |
| how does a backend concern work? | `SKILL.md` says to combine with backend delivery | target framework, persistence, security, runtime, and operational sources and owners | backend integration evidence and owner |

No layer universally wins. Applicable owner policy can constrain a choice but
cannot make incompatible behavior succeed. Official documentation can establish
supported behavior but not target adoption. A qualified target failure can
block adoption under its observed conditions without proving the general source
wrong.

**Precedence protocol**

1. Name the atomic claim. Split paragraphs whose source role, version, target
   scope, or confidence differs.
2. Identify the ownership layer: route, navigation, language semantics, target
   implementation, public support, observed behavior, or risk acceptance.
3. Select the source that owns that layer and record its scope. Do not choose by
   length, detail, or a global canonical label.
4. Check identity, read depth, version, target applicability, and derivation.
   Repeated wording from a shared origin is not independent corroboration.
5. Preserve conflicts. Compare artifact, version, platform, execution mode,
   defaults versus effective configuration, and observation quality.
6. Run a discriminating target scenario where safe. Escalate policy or
   irreversible migration conflict to the accountable owner.
7. Record the stronger claim not established and the event that reopens the
   hierarchy decision.

**Source role vocabulary**

Use these roles at claim level:

- `entrypoint_router`: selects task mode and adjacent ownership;
- `navigation_index`: locates focused source regions;
- `mechanism_guidance`: explains a candidate principle, failure, or example;
- `skeptical_gate_guidance`: challenges implementation and selects evidence
  families;
- `dated_provenance`: records historical research and synthesis lineage;
- `target_instruction`: constrains repository scope and workflow;
- `target_implementation`: establishes effective code, build, consumer, and
  artifact state;
- `target_policy`: states accountable support and risk requirements;
- `refreshed_primary_authority`: bounds a current version-sensitive fact after
  authorized retrieval;
- `observed_result`: reports a qualified test, compatibility, runtime, or
  incident outcome;
- `combined_inference`: joins premises into bounded engineering guidance;
- `conditional_or_conflicting`: preserves a missing owner, inaccessible
  environment, or unresolved contradiction;
- `superseded`: records why a prior route or claim no longer applies and which
  consumers must migrate.

Whole files can have default routing roles, but a particular sentence still
needs the role appropriate to its claim.

**Conflict examples**

Platform type: the reliability reference recommends immediate normalization.
Target inspection shows a generated Java signature whose current annotation
claims non-null, while a target test produces null. The observed contradiction
blocks trusting the generated contract for that case. Investigate version,
generation, and fixture fidelity; do not discard the generic boundary principle
or silently ignore the result.

Coroutine exception: frozen guidance says cancellation must propagate. A target
framework wrapper catches all exceptions under a lifecycle policy. The
framework source owns its intended mechanism, but a cancellation scenario owns
the observed result. If cancellation becomes ordinary failure, preserve the
conflict and route to the framework or backend owner.

Value class: local guidance recommends meaningful wrappers. Java consumer and
serialization evidence shows an unsupported generated surface. Target
compatibility outranks direct adoption; preserve the principle by containing
the value internally or choose another representation.

Backend route: a language source explains `Flow`, while production work
ownership, acknowledgment, shutdown, and recovery are controlled by a queue and
platform. The Kotlin reference answers cancellation at the adapter interface;
backend delivery integrates the full lifecycle.

**Hierarchy verification**

- Confirm every frozen path exists and each recorded hash still matches.
- Confirm links and heading names resolve without interpreting fenced examples
  as structure.
- Sample consequential claims and verify the cited region entails them with its
  prerequisites and caveats.
- Check whether a target fact, owner policy, current primary source, or observed
  result has been incorrectly downgraded beneath archived prose.
- Detect circular routing and duplicated conclusions. A route that repeatedly
  returns without new evidence signals a badly framed decision boundary.
- Track missing guidance, wrong-region reads, unnecessary context, conflicts,
  and post-handoff escapes.

**Hierarchy decision record**

```text
claim_and_consequence:
ownership_layer:
selected_source_role_and_locator:
hash_version_target_revision:
complete_region_read:
derivation_or_duplicate_sources:
supporting_and_conflicting_evidence:
target_authority_and_observed_result:
precedence_decision_and_reason:
stronger_claim_not_supported:
consumer_and_invalidation_event:
```

Evolve the hierarchy conservatively. Add a new durable source role only when a
repeated consequential question has independent ownership and maintenance
value. Merge or retire routes that duplicate decisions or no longer affect a
supported consumer. Keep `SKILL.md` compact by linking stable deep guidance
rather than absorbing it, while ensuring handoffs remain few enough that a user
can still identify one integration owner.

## Theme Specific Artifact

The reusable artifact is a **Kotlin Skill Activation Contract**. It records why
the language route activated, what it owns, which context was disclosed, which
choices remain preserved, and what evidence permits the next state. It can be a
short working note for a local change or a durable record for public,
concurrent, cross-owner, or long-lived work.

**Contract states**

| state | entry_condition | permitted_action | exit_condition |
| --- | --- | --- | --- |
| unclassified | request exists but outcome, target, or risk is not yet bounded | inspect instructions, target, callers, owners, and current behavior | one accepted outcome and dominant failure class are stated |
| routed | lead mode and any support interfaces are selected | open focused sources and gather target evidence | selected route has enough context to compare safe options |
| design_ready | requirements, preserved choices, alternatives, and hard gates are explicit | implement or review only the bounded change | focused negative and accepted cases are specified |
| evidence_active | implementation or review is being exercised | run qualified focused and affected wider gates; preserve failures | evidence is interpretable as pass, fail, conditional, skipped, or inconclusive |
| conditional | a narrower claim is supported while a material owner, consumer, or environment remains unavailable | hand off exact missing boundary or proceed only within the supported subset | missing evidence arrives or stronger claim is withdrawn |
| rerouted | new evidence shows another mode or owner leads | transfer minimal state and stop conflicting work | receiving route accepts ownership and return interface |
| accepted | bounded outcome, consumers, and required gates satisfy target authority | hand off implementation or findings with limits | invalidation event reopens the contract |
| rejected | candidate violates a hard gate or offers insufficient benefit | preserve or select another option | new evidence or changed requirement reopens comparison |
| superseded | target revision, consumer, source, policy, or mechanism invalidates the record | use the replacement record and migrate consumers | historical consumers and temporary controls are retired |

Do not calculate a completion percentage. A single unresolved public consumer,
swallowed cancellation path, or wrong artifact can block the dependent claim
even when many descriptive fields are filled.

**Required core fields**

| field | completion_rule | evidence_or_question |
| --- | --- | --- |
| contract_id_and_version | stable identifier plus schema or decision revision | Can later consumers distinguish an amendment from a new decision? |
| requested_action | explain, plan, implement, refactor, review, debug, migrate, or assess | What did the user authorize, and what remains outside scope? |
| accepted_outcome | observable normal, absent, invalid, failed, canceled, compatibility, and final states as applicable | What must be true for users and callers, not merely for the source diff? |
| target_identity | repository, revision, module, artifact, environment, and supported branch where known | Which exact system can the evidence describe? |
| applicable_instructions_and_owners | scoped rules and accountable decision owners | Who can constrain edits, compatibility, security, migration, and risk? |
| current_contract | existing types, callers, scopes, effects, errors, build, tests, and behavior relevant to the change | What is being preserved or deliberately changed? |
| lead_mode | one of the frozen seven modes or route-away state | Which failure class owns the plan? |
| support_interfaces | additional modes or adjacent routes with one precise question each | What must each specialist return, and who integrates it? |
| dominant_failure_and_consequence | earliest causal defect plus affected caller or state | Why is this work worth doing now? |
| preserved_choices | versions, wrapper, plugins, architecture, public surface, and unrelated code not in scope | What must not drift during the change? |
| progressive_source_selection | local regions opened, skipped regions, target evidence, and future authority used | Why was each context item necessary, and what would widen retrieval? |
| alternatives_and_hard_gates | preservation plus feasible candidates, categorical rejection rules, and safe intermediate states | Which options remain possible after consequence and authority checks? |
| selected_design_and_boundaries | chosen representation, ownership, adapters, callers, and mappings | Where is ambiguity contained and who now owns it? |
| executable_requirements | target identifiers and observable behavior | Can tests distinguish accepted, rejected, canceled, and compatibility states? |
| verification_matrix | focused failure, negative control, broader consumers, task selection, and artifact identity | Which gate can disprove each claim? |
| evidence_status | pass, fail, conditional, skipped, or inconclusive per claim | What did the evidence actually establish? |
| uncertainty_and_stronger_claim | missing version, consumer, environment, owner, or behavior plus the claim it blocks | What must not be inferred from the current record? |
| route_stop_and_handoff | stop, reroute, escalation, return recipient, and required evidence | What is the next safe action if the route cannot continue? |
| invalidation_and_retirement | source, version, consumer, policy, incident, or mechanism change that reopens the record | When must evidence be rerun and temporary controls removed? |

Use explicit values such as `not_applicable because no Java consumer exists at
revision X`, `conditional pending managed-platform cancellation evidence`, or
`unknown; blocks public API migration`. An empty field cannot distinguish an
intentional exclusion from a missed question.

**Conditional mode fields**

| activated_boundary | additional_fields |
| --- | --- |
| nullability or raw input | origin signature, annotation status, semantic meanings of absence, normalization point, malformed and historical cases |
| type or state design | invariant, state openness, equality, copy, serialization, persistence, Java, and binary consumers |
| coroutine or flow | owner scope, child relation, dispatcher, blocking behavior, cancellation phases, buffer or sharing, effects, cleanup, final state |
| Java interop | Java version, signatures, names, defaults, overloads, exceptions, generics, annotations, facades, and representative callers |
| public API compatibility | current and candidate artifacts, supported consumers, baseline, deprecation, coexistence, versioning, and migration |
| generated or framework surface | compiler plugins, generated sources, proxy or reflection rules, target framework mode, and real-boundary gate |
| backend handoff | framework, persistence, auth, config, runtime, package, data, operational, and recovery owner interfaces |
| shared workspace | exclusive file ownership, concurrent changes, merge owner, persisted checkpoints, and authorized actions |

**Artifact profiles**

Lightweight: for a direct explanation or private pure function, retain requested
action, outcome, target assumptions, lead mode, one source region, one gate or
caveat, and stronger claim not made.

Standard: for implementation, refactor, or review, complete the full required
core and activated conditional rows.

Consequential: for public API, Java or binary consumers, serialization,
concurrency, persistent state, security, framework integration, or cross-owner
work, persist target identities, owner decisions, migration states, all evidence
tiers, and retirement conditions in the target's durable decision system.

**Filled illustrative activation contract**

| field | scenario_value |
| --- | --- |
| contract_id_and_version | `directory-platform-null-activation-v1` |
| requested_action | refactor one shared JVM adapter and preserve supported Java callers; no backend deployment change authorized |
| accepted_outcome | Java non-null result becomes found, documented null becomes missing, provider failure remains distinct, cancellation remains cancellation, public facade remains compatible |
| target_identity | illustrative shared JVM module at a frozen review revision; no real repository result claimed |
| applicable_instructions_and_owners | module owner decides public contract; backend owner joins only if remote-client lifecycle becomes in scope |
| current_contract | unannotated Java return enters Kotlin through a non-null assertion; a suspend wrapper and Java facade consume it |
| lead_mode | Nullability Mode |
| support_interfaces | Interop Mode checks Java shape; Coroutine Mode checks cancellation and blocking; Testing Mode qualifies fixtures and gates |
| dominant_failure_and_consequence | platform null can crash far from the boundary and broad error handling can erase cancellation |
| preserved_choices | Kotlin and JVM versions, wrappers, compiler plugins, public Java facade, provider library, and unrelated architecture |
| progressive_source_selection | read nullability and interop, coroutine, testing, and matching anti-pattern regions; skip core collection and backend operation regions unless discovery activates them |
| alternatives_and_hard_gates | preserve with typed contract failure, nullable return, internal sealed state, typed exception, or compatibility facade; reject any option that conflates cancellation or breaks unapproved callers |
| selected_design_and_boundaries | illustrative internal found, missing, or failed state behind a compatibility-preserving facade; platform value contained in Java adapter |
| executable_requirements | scenario requirements `REQ-KOTLIN-101.0` through `REQ-KOTLIN-105.0` from the worked journey |
| verification_matrix | Java null and value cases, known provider failure, cancellation phases, Java caller build, compatibility baseline if configured, and affected regression tasks |
| evidence_status | design-ready illustration only; no target command or external provider evidence executed |
| uncertainty_and_stronger_claim | provider null semantics, interruptibility, dispatcher capacity, all downstream binaries, and service lifecycle remain unknown |
| route_stop_and_handoff | stop state-model adoption if null meaning or consumer policy is unresolved; hand remote lifecycle to backend owner |
| invalidation_and_retirement | provider signature, annotations, Kotlin or coroutine version, public consumers, facade policy, or observed cancellation behavior changes |

This example is good because it exposes both what the language route can decide
and what it cannot. A bad record would say `Use sealed types because Kotlin
recommends them`, list a unit test, and claim the adapter production-safe
without signatures, consumers, cancellation, provider behavior, or target
results.

**Acceptance gates**

- Required and activated fields have classified values, not omissions.
- One lead mode and one integration owner exist.
- Sources and target locators support their bounded claims at recorded identity.
- Preservation and a rejected option are visible.
- Every hard gate can realistically fail under the current scenario.
- Verification results identify task selection, artifact, input, environment,
  final state, and stronger claim not proved.
- Conditional boundaries name an owner and next evidence action.
- Sensitive values and unbounded logs are absent.
- Another reviewer can reconstruct the route and next safe action without the
  original conversation.

**Lifecycle**

Update the contract when the target revision, source identity, version,
consumer, execution model, owner policy, result, or incident changes materially.
Create a new version when the accepted outcome or public migration changes.
Supersede rather than silently rewrite records that have durable consumers.
Retire temporary facades, suppressions, dispatchers, or test gates only after
their exit evidence passes and dependent documentation or automation migrates.

Aggregate only access-safe categories from repeated contracts: wrong routes,
missing consumers, common failure classes, inconclusive gates, and stale source
regions. Use those trends to improve the entrypoint, not to rank individual
engineers or reward shorter context at the expense of correctness.

## Worked Example Set

These examples are decision fixtures, not verified target implementations. Each
states the evidence that would select or reverse the route. Adapt names,
versions, frameworks, and tests to the repository before using code.

**Example A: meaningful identifier**

Context: two raw strings represent `UserId` and `InvoiceId` across many domain
calls, and both have validated nonblank formats. Target inspection finds Kotlin
callers, one serializer, and no supported Java or framework-generated consumer.

Good route: select `Type Boundary Mode`; compare preservation with value
classes; validate at construction; keep raw parsing at the adapter; test wrong
type prevention through compilation, invalid values, equality, and serializer
round trip. Preserve the serializer configuration and Kotlin version.

Illustrative shape:

```kotlin
@JvmInline
value class UserId private constructor(val value: String) {
    companion object {
        fun parse(raw: String): UserId? =
            raw.trim().takeIf(String::isNotEmpty)?.let(::UserId)
    }
}
```

Bad route: wrap every `String` in a value class because wrappers have a high
historical score, leave public construction unrestricted, and skip serializer
and consumer checks. More types exist, but the invariant and migration remain
unclear.

Borderline route: Java callers or framework binding are discovered after the
design. Keep the type internal or preserve raw public signatures while
investigating generated representation, annotations, boxing, reflection, and
compatibility. Do not claim the final public wrapper safe yet.

Evidence: parser tests for empty, whitespace, valid, and round-trip values;
compile checks preventing identifier interchange; target serializer and
generated-surface tests; Java and API or ABI gates only if consumers exist.

**Example B: platform nullability**

Context: an unannotated Java library returns a platform type that is assigned to
a non-null Kotlin property.

Good route: select `Nullability Mode` with `Interop Mode` support; inspect the
actual Java signature and documented semantics; convert the value at one
adapter into a nullable or typed state; keep platform uncertainty out of the
domain; exercise representative Java null and non-null cases.

Bad route:

```kotlin
val displayName: String = javaClient.findDisplayName(userId)!!
```

The assertion converts incomplete evidence into a runtime crash and hides the
origin after the value crosses the boundary.

Borderline route: current annotations say non-null, but old target logs or a
test show null. Preserve both claims, check library version and generated
signature, validate fixture fidelity, and keep the adapter defensive until the
conflict is resolved. A source label cannot erase observed contradictory state.

Evidence: Java-origin fixture, null and value scenarios, actual adapter and
callers, generated build, and target dependency version. A Kotlin-only fake
whose return is already `String?` does not fully reproduce platform inference.

**Example C: closed outcome versus open protocol**

Context: Kotlin code handles `approved`, `declined`, and `review` states from an
external protocol that may add states independently.

Good route: preserve an extensible raw or wire representation at the boundary;
parse recognized states into explicit internal outcomes; retain `Unknown` with
the original safe code or metadata according to policy; keep domain `when`
handling exhaustive for the internal state.

```kotlin
sealed interface Decision {
    data object Approved : Decision
    data class Declined(val reason: String) : Decision
    data object RequiresReview : Decision
    data class Unknown(val code: String) : Decision
}
```

Bad route: model only today's three states as a public sealed hierarchy and
throw on any future code because sealed outcomes are described as idiomatic.
The representation converts protocol evolution into an outage.

Borderline route: the organization owns both producer and consumers and has a
versioned closed contract. A sealed public type may be appropriate, but verify
old and new artifacts, Java callers, serialization, unknown-state policy, and
release ordering before removing extensibility.

Evidence: every known state, unknown input, malformed input, round trip, old and
new consumer behavior, and explicit owner policy. A compiler exhaustiveness
check alone cannot prove wire compatibility.

**Example D: data class or identity object**

Context: a `Customer` type has a database identity, mutable lifecycle status,
lazy relations, and framework proxying.

Good route: select `Type Boundary Mode` but route persistence and framework
semantics to backend delivery. Use a plain or target-framework-compatible class
if value equality, `copy`, and destructuring do not match identity and lifecycle.
Keep immutable snapshots or DTOs as data classes where their full value defines
equality.

Bad route: convert the entity to a data class to obtain generated methods, then
use `copy` to change status outside domain transitions. Equality and persistence
identity diverge while local tests compare only field values.

Borderline route: the type is called an entity but is actually an immutable
event snapshot. Inspect construction, equality consumers, persistence mapping,
proxy requirements, serialization, and mutation before changing class form.

Evidence: equality and hash behavior, copy or transition semantics, persistence
round trip, proxy or generated behavior, and historical data. A naming
convention is not evidence of identity.

**Example E: cancellation and blocking**

Context: a suspend function catches all exceptions around a legacy blocking
client and returns a generic failure.

Good route: select `Coroutine Mode`; identify caller-owned scope; preserve
`CancellationException`; keep the client explicitly blocking or isolate it
through target-owned execution policy; test cancel before call, during a
controlled wait, after result, and during cleanup; inspect resources and effects.

```kotlin
suspend fun loadRecord(): RecordResult =
    try {
        executeOwnedLookup()
    } catch (error: CancellationException) {
        throw error
    } catch (error: ClientFailure) {
        RecordResult.Failed(error.kind)
    }
```

Bad route: mark the legacy call `suspend`, catch `Exception`, retry it, and
assume `withContext` makes the underlying operation interruptible. Cancellation
can become failure while blocked work and external effects continue.

Borderline route: the library documentation claims cooperative cancellation,
but the target version and provider mode are not established. Keep the claim
conditional, inspect released authority when authorized, and run a real-client
scenario before relying on prompt cancellation for resource or shutdown safety.

Evidence: scope and child tree, actual client and dispatcher, cancellation at
phases, attempt count, resource release, effect state, and backend lifecycle if
the call belongs to a service. Virtual time is not blocking or performance
proof.

**Example F: Kotlin API used from Java**

Context: a public Kotlin function with default arguments and a value-class
parameter is published to Java consumers.

Good route: select `Interop Mode`; inspect generated JVM signatures; decide
whether an explicit facade, `@JvmName`, `@JvmOverloads`, or another target-
compatible surface improves safety; preserve binary and exception policy; run
representative Java calls and configured compatibility gates.

Bad route: optimize the Kotlin call site and assume Java receives the same
defaults, names, nullability, and value-class ergonomics. The Kotlin module
compiles while supported Java source or binaries break.

Borderline route: no Java consumer is found in the repository, but the artifact
is public. Treat external consumer status as unresolved. Preserve the surface
or obtain release authority before a breaking change rather than inferring
privacy from local search.

Evidence: published artifact identity, Java source fixture, bytecode or API
surface inspection, baseline comparison, supported consumer inventory, and
version policy. Do not add annotations mechanically without observing their
generated effect.

**Example G: scope-function cleanup**

Context: a review proposes replacing explicit locals with nested `let`, `also`,
and `apply` blocks.

Good route: use `Core Kotlin Mode` and ask whether receiver, mutation, and
return value remain obvious. Keep one conventional scope function when it
clarifies a small operation; retain named locals when several objects or effects
interact.

Bad route: equate density with idiomatic Kotlin and accept a chain whose final
value differs from the object most recently mutated. The code passes behavior
tests today but becomes difficult to modify safely.

Borderline route: team conventions prefer a familiar pattern and reviewers can
read it reliably. Preserve it unless an actual defect or maintenance burden is
shown. Style preference alone is not a reliability migration.

Evidence: existing behavior tests, receiver and return readback during review,
diff scope, and target style gates. No performance claim follows from fewer
lines.

**Example H: backend handoff**

Context: a Ktor worker consumes queue items with a `Flow`, writes a database,
and must shut down without losing effects.

Good route: backend delivery leads queue ownership, transaction, acknowledgment,
health, shutdown, restart, and recovery. The language route answers only
structured coroutine ownership, cancellation propagation, and type boundaries
at the interface. Testing guidance supplies phase interruption; the backend
owner integrates final evidence.

Bad route: use `Flow` and `coroutineScope` because they are language defaults,
run a coroutine unit test, and claim graceful production behavior without
broker, database, package, platform, or recovery state.

Borderline route: the worker is an in-memory library component with no durable
source or external effects. Language mode may lead after target discovery
confirms the operational boundaries are absent.

Evidence: the language-level gate plus real queue, data, process termination,
restart, and final-effect evidence owned by backend delivery. A clean coroutine
completion is not durable-work proof.

**Example maintenance rules**

- Keep the context, bad path, borderline discriminator, and evidence boundary
  synchronized with each example's mechanism.
- Avoid exact version or library claims unless the example has a recorded
  execution and source scope.
- Add a fixture only for a distinct causal failure; consolidate examples that
  differ only in naming.
- Re-run executable fixtures when compiler, library, generated mechanism, or
  target consumer changes.
- Remove an example when the bad path no longer fails, the mechanism is no
  longer supported, or the lesson is fully enforced by a stronger control.

The best example changes the next decision. It does not ask readers to imitate
surface syntax without understanding ownership and evidence.

## Outcome Metrics and Feedback Loops

The seed's `one focused implementation session` target has no baseline,
population, consequence model, or evidence and is not retained as policy. Session
length is also an unstable unit across tasks, agents, repositories, and
interruptions.

Use feedback to answer a decision. Start with categorical integrity and safety
invariants, characterize repeated work, and set target-owned objectives only
after definitions, baselines, consumers, and collection quality are known.

**Metric hierarchy**

| layer | question | candidate_measure_shape | guardrail |
| --- | --- | --- | --- |
| artifact integrity | Did the entrypoint record, reference, and evidence satisfy deterministic structure? | required fields, exact source identities, gate results, and invalidation state | structural completeness cannot certify target Kotlin behavior |
| route integrity | Did the selected lead mode and owner match the consequential boundary? | representative tasks by actual versus selected route, reroutes, unowned interfaces, and reviewer disagreement | do not force one correct label when several routes legitimately compose |
| boundary safety | Did ambiguity remain contained at the intended adapter, type, scope, or facade? | platform leaks, assertion crashes, conflated states, detached work, swallowed cancellation, and escaped mutable aliases | aggregate success cannot offset a categorical correctness or consumer violation |
| verification quality | Could the selected gate expose the named defect and did it run the intended target? | negative-control yield, empty selections, wrong artifacts, flaky or inconclusive results, and escaped defects | more commands and longer builds do not imply stronger evidence |
| consumer compatibility | Did supported Kotlin, Java, binary, wire, generated, and framework consumers remain accepted? | affected consumers checked, unapproved breaks, migration status, and delayed downstream failures | local repository search may not cover external public consumers |
| flow and rework | How long and how many transitions were needed to reach an accepted decision? | time from accepted requirement to interpretable evidence, reroute delay, review cycles, and causal rework | segment by task class and hold quality plus consequence constant |
| context yield | Did each source or tool materially change the route, design, gate, or uncertainty? | selected and skipped regions, irrelevant context, repeated reads, and missing-source escapes | fewer files or tokens is not success if a consequential boundary is omitted |
| maintenance outcome | Did the change reduce repeated checks and remain understandable? | duplicated adapters, caller branches, test burden, stale exceptions, temporary facade age, and review findings | added types and tests can become debt if their distinctions no longer matter |
| learning outcome | Did recurring evidence improve code, gates, source routes, or ownership? | promoted compiler or static controls, new fixtures, trigger changes, retired manual rows, and unresolved recurrence | avoid process churn from one recent or weakly classified event |

**Hard invariants**

When activated by the target, treat these as non-compensable:

- platform uncertainty does not silently enter a non-null domain invariant;
- expected distinct states are not collapsed into an indistinguishable boolean,
  null, sentinel, or generic failure without an accepted contract;
- cancellation remains cancellation across owned coroutine, logging, retry, and
  error-normalization boundaries;
- caller-owned work does not detach without an explicit lifecycle or durable
  owner;
- blocking behavior is not hidden by a suspend signature without target-owned
  isolation and evidence;
- public Kotlin, Java, binary, wire, generated, and framework consumers do not
  break outside an approved migration;
- a green gate selects the intended work and artifact and can detect its named
  defect;
- language guidance does not grant backend, security, data, deployment, or
  production-readiness claims outside its evidence.

An invariant can be not applicable only when the underlying state or consumer
cannot exist in the accepted scope and that absence is evidenced.

**Operational definitions**

Define a route attempt from the moment an accepted outcome and target scope are
available, not from the first vague request. Define a reroute as a lead-owner
change caused by new evidence; do not count a planned support-mode handoff as a
route failure. Define rework as discarded or materially redone implementation,
tests, or design caused by a wrong assumption that could have been discovered
earlier. Separate necessary iterative refinement from avoidable causal rework.

For defect and compatibility measures, define:

- population: tasks, changes, APIs, consumers, coroutine flows, or incidents;
- unit: route decision, boundary, consumer, gate, artifact, or final outcome;
- inclusion and exclusion: abandoned requests, exploratory spikes, generated
  code, external consumers, and delayed reports;
- severity and consequence: crash, data or effect error, resource leak,
  cancellation defect, source or binary break, review burden, or style-only
  issue;
- detection stage: type or compiler, focused test, wider build, review,
  downstream consumer, release, or production;
- missing data: unknown rather than silently excluded;
- ownership: who acts when the measure changes.

**Feedback methods**

| method | useful_for | limitation |
| --- | --- | --- |
| seeded route fixtures | checking whether activation distinguishes language, backend, interop, coroutine, and no-change tasks | synthetic prompts may not represent legacy context or real ownership |
| reversible negative controls | qualifying that a gate detects platform null, cancellation loss, compatibility drift, or empty selection | unsafe for some shared baselines or external systems |
| post-review finding audit | identifying boundary defects missed before handoff | reviewer quality and taxonomy vary |
| escaped-defect causal review | finding the earliest route, type, adapter, scope, or gate that could have prevented harm | incidents are sparse and hindsight can overstate predictability |
| consumer migration record | observing Java, binary, wire, or framework burden and compatibility escapes | external consumers may report late or remain invisible |
| context and tool trace summary | finding irrelevant source loading, repeated searches, route loops, and inconclusive gates | detailed traces create privacy and measurement overhead |
| before-and-after cohort | estimating whether a route or gate change altered flow and defect discovery | task, model, team, and repository differences confound attribution |
| second-reader reconstruction | testing whether a durable activation contract supports handoff and resume | does not prove implementation behavior |

Do not retain raw conversations, source payloads, private code, credentials, or
customer data merely to improve measurement. Use access-safe categories and
locators under target policy.

**Good interpretations**

Route feedback: several public Java API tasks are initially classified as
`Core Kotlin Mode`, then compatibility issues appear late. Review task fixtures
and real findings, sharpen the interop trigger to include published artifacts,
add Java caller discovery, and measure whether late compatibility reroutes
decline without increasing false activation on private code.

Gate feedback: cancellation tests pass, but incident evidence shows work
continues after caller exit. The review finds tests used virtual delay while the
real adapter blocked. Add a real adapter or controlled blocking fixture, update
the coroutine route to inspect execution mode, and classify prior tests as
narrow rather than false universally.

Context feedback: agents load all five local files for simple collection
refactors. Reduce retrieval to the compact skill, core section, and final
activated review rows. Validate that boundary escapes and reviewer rework do not
increase. Fewer reads alone are not the outcome.

Consumer feedback: an internal sealed outcome reduces nullable branches, but a
compatibility facade remains long after Java consumers migrate. Track remaining
callers and gate evidence; remove the facade and its duplicate mapping only
when the owner-approved retirement condition passes.

Bad interpretation: tool calls and elapsed time decrease after removing Java
fixtures and wider builds, so the route is declared more efficient. A delayed
consumer break shows the apparent gain shifted work and risk downstream.

Borderline interpretation: a small fixture set suggests mode selection improved,
but tasks changed and reviewers disagree. Report the observed cases, retain the
new trigger as provisional, and gather representative use before claiming a
general improvement.

**Metric record**

```text
metric_id_and_decision_consumer:
question_and_action_threshold_source:
population_unit_and_task_classes:
baseline_and_comparison:
inclusions_exclusions_and_missing_data:
data_source_access_and_privacy:
hard_guardrails:
observed_distribution_or_cases:
reviewer_disagreement_and_confounders:
interpretation_and_confidence:
action_owner:
expected_change_and_rollback:
followup_result:
retirement_or_recalibration_event:
```

No universal numeric threshold is supplied here. A target team may define
objectives for repeated route delay, escape rate, migration age, or gate
reliability after establishing its population and consequence. Rare severe
failures still require categorical prevention and direct scenarios even when a
rate cannot be estimated reliably.

**Feedback loop**

1. Observe a route, boundary, gate, consumer, or maintenance outcome.
2. Validate collection and classification; preserve missing and contradictory
   evidence.
3. Identify the earliest causal control, not merely the final failing symptom.
4. Propose the smallest change to an activation trigger, type boundary, source
   map, gate, handoff, or owner interface.
5. State expected benefit, possible regression, hard guardrails, and rollback.
6. Apply under target ownership and compare a representative future cohort or
   scenario.
7. Retain, revise, or revert the intervention from evidence.
8. Retire the metric when it drives no decision or stronger prevention makes it
   obsolete.

Review cadence follows change and consequence. Re-run deterministic artifact
gates after every relevant edit. Requalify source and compatibility evidence
when versions, consumers, or public contracts change. Review route and outcome
trends after enough representative work or a consequential escape, not merely
on a calendar that produces no action.

## Completeness Checklist

Use this checklist at a route, design, implementation, review, migration, or
handoff boundary. Activate target rows from the actual Kotlin surface and
plausible consequence. Deterministic requirements for this evolved reference
remain mandatory regardless of target profile.

**Status semantics**

| status | meaning | required_record | effect_on_claim |
| --- | --- | --- | --- |
| pass | evidence at the required fidelity supports the bounded claim | target identity, action, result, final state, evidence locator, and reviewer or owner | claim may proceed only within recorded scope |
| fail | interpretable evidence contradicts a requirement or hard gate | earliest causal failure, affected consumers, preserved state, containment, and owner | stop dependent action until corrected or explicitly rejected by authority |
| conditional | a narrower layer passes while a material consumer, version, owner, or environment is unavailable | passed subset, missing boundary, stronger claim blocked, next gate, and owner | proceed only with the supported subset |
| skipped | a gate is deliberately omitted because its state or consumer cannot occur in scope | target fact proving absence, consequence if scope changes, and reviewer | row reopens when the absent boundary appears |
| inconclusive | selection, cache, flakiness, contamination, environment, or asynchronous leakage prevents interpretation | uncertainty source, affected claim, isolation action, and owner | no dependent readiness is granted |

Do not compute an overall percentage. Passing formatting, compilation, and unit
tests cannot offset a failed cancellation, platform-type, compatibility,
security, data, or wrong-artifact gate.

**Reference artifact conformance**

| gate | required_state | verification |
| --- | --- | --- |
| original structure | exactly the 26 original Markdown heading texts in original order with no added reference headings | parse heading sections outside fences and compare with the archive seed |
| section expansion | every evolved section is strictly longer than its matching seed and adds decision-relevant depth | per-section character comparison plus skeptical semantic review |
| packet grammar | 26 packet sections contain ten exact questions and six required fields in order | structural parser reports 26 sections, 260 questions, and 1,560 values |
| packet uniqueness | all mandatory values are unique before and after Section and Question context prefixes are stripped | exact and normalized uniqueness counts both equal 1,560 |
| frozen source integrity | archive seed, queue spans, canonical skill, and companion source hashes match recorded bytes | SHA-256 and LF-normalized span checks |
| evidence accuracy | complete-read depth, dated public mappings, no-browse status, and target unknowns are stated without overreach | claim-level provenance review |
| Markdown integrity | tables have consistent columns and code fences close without creating accidental headings | deterministic structure scan and parser review |
| text hygiene | ASCII, final newline, no trailing whitespace, unresolved markers, malformed tables, or copied generic filler | focused and independent static audits |
| complete reread | all packet and reference sections receive skeptical reread with persisted checkpoints no more than five sections apart | lane journal evidence through Section 026 |
| focused verification | repository file verifier accepts the exact reference and matching packet | retained command, exit status, counts, and output hash |

These gates prove only the reference artifact contract. They do not establish a
future Kotlin target's correctness, compatibility, or operational readiness.

**Activation and route completeness**

- The requested action and accepted outcome are explicit. Explanation,
  implementation, review, debugging, migration, and backend support are not
  treated as interchangeable.
- Applicable instructions, target revision, module, wrapper, Kotlin and JVM
  versions, plugins, generated mechanisms, callers, and owners are inspected to
  the depth required by the claim.
- One lead mode owns the plan. Supporting modes and adjacent routes receive one
  bounded interface question each.
- The dominant failure and cost of being wrong identify users, callers, data,
  effects, resources, or maintenance state affected.
- Backend framework, persistence, auth, migration, runtime, package, and
  production concerns are routed rather than absorbed into generic Kotlin
  advice.
- Stop, reroute, and invalidation events are stated. A keyword match is not an
  activation proof.

**Source and context completeness**

- `SKILL.md` was used for route and scope, `reference-map.md` for navigation,
  relevant reliability regions for mechanisms, and matching quality-gate rows
  for skeptical review.
- Only activated regions were loaded; skipped regions have an absent-boundary
  reason and widening trigger.
- Frozen local content, target facts, refreshed future authority, observed
  results, inference, judgment, and conditional claims remain distinguishable.
- Public mappings are labeled unrefreshed unless a future authorized retrieval
  records version, date, complete region, extracted fact, conflict, and target
  reproduction.
- No source's whole-file role is transferred to an unrelated claim. Duplicate
  derivation is not counted as independent corroboration.
- Sensitive source, customer, credential, and incident material remains outside
  generic records and public queries.

**Requirement and design completeness**

- Ambiguous terms such as safe, clean, idiomatic, fast, simple, or compatible
  are replaced by observable behavior or an explicit review criterion.
- Executable requirements cover normal, absent, malformed, boundary, failed,
  canceled, compatibility, and final states activated by the change.
- Preservation is an option. Versions, wrapper, plugins, architecture, public
  surfaces, and unrelated code remain stable unless migration is accepted.
- Alternatives include local containment, adaptation, compatibility facade,
  breaking migration, defer, route away, and reject where feasible.
- Hard gates eliminate options that violate correctness, cancellation,
  compatibility, security, data, or authority.
- The selected design names the point where raw or platform uncertainty becomes
  a domain value, state, error, scope, or explicit handoff.
- Safe intermediate states, caller migration, rollback or roll-forward, and
  temporary mechanism retirement are visible when the surface cannot change
  atomically.

**Kotlin boundary completeness**

| boundary | completion_questions |
| --- | --- |
| nullability | What does absence mean, where do platform types originate, and can uncertainty escape the adapter or become an assertion crash? |
| values and invariants | Does a value class, primitive, enum, sealed type, data class, or plain class match meaning, equality, copy, extension, and construction rules? |
| raw input | Are strings, maps, JSON, CLI args, environment values, old data, and Java objects parsed once before domain logic? |
| errors and outcomes | Are expected states distinguishable from infrastructure failure and cancellation, and can callers handle evolution safely? |
| immutability and ownership | Can mutable aliases, globals, or lifecycle state escape their owner or leak across tests and threads? |
| scope functions and extensions | Are receiver, return, side effect, visibility, ownership, and discoverability clear? |
| coroutines | Who owns scope, children, failure, cancellation, timeout, dispatcher, effects, cleanup, and final state? |
| blocking | Is blocking named or target-isolated, and do capacity plus cancellation claims match actual client behavior? |
| flow | Who owns producer, collector, sharing, buffer, callback, completion, failure, cancellation, and resource release? |
| Java interop | Are platform types, names, defaults, overloads, annotations, generics, exceptions, SAM use, boxing, and representative callers explicit? |
| public compatibility | Are source, binary, wire, generated, reflection, framework, and downstream consumers inventoried and gated? |
| build and plugins | Are effective compiler, JVM target, plugins, generated sources, task selection, and configured static analysis preserved or deliberately migrated? |

Exclude a row only when the state cannot occur in the bounded target. For
example, private pure Kotlin logic with no suspend or Java edge can skip
coroutine and interop gates, but the evidence for that privacy and reachability
must be credible.

**Verification completeness**

- Each requirement maps to the smallest gate that can expose its causal defect.
- Test and build tasks are discovered through repository wrappers; global tools
  and newly introduced plugins are not substitutes.
- Task and filter selection, source sets, generated code, cache inputs, artifact
  identity, environment, and expected cases are known.
- A reversible negative control or retained known failure qualifies new or
  changed gates.
- Pure, compile, Java, coroutine, serialization, API or ABI, real-boundary,
  package, and backend tiers are selected only as activated.
- Asynchronous tests assert child, callback, resource, effect, and cleanup final
  state rather than ending while work continues.
- Results are classified per claim. Lower-tier passes do not grant inaccessible
  compatibility, provider, package, or production evidence.
- Skipped and inconclusive gates remain visible with owners and next actions.

**Consumer and migration completeness**

- Supported Kotlin and Java source callers are inspected or explicitly outside
  scope under owner policy.
- Published artifact, binary baseline, serialized shape, generated APIs,
  reflection, framework proxies, persistence, and historical data are activated
  where the change can reach them.
- Deprecation, coexistence, facade mapping, old and new versions, release order,
  and support window are defined for non-atomic changes.
- Breaking decisions have accountable authority and a recoverable intermediate
  state or explicit maintenance transition.
- Temporary facades, suppressions, adapters, dispatchers, feature contracts,
  and compatibility gates have exit evidence and owners.

**Review and handoff completeness**

- Findings distinguish observed defect, causal path, consequence, uncertainty,
  repair option, and missing test; finding count is not a success metric.
- A no-finding review still states target regions inspected, gates run, and
  residual risk such as external consumers or inaccessible runtime behavior.
- A support route transfers target identity, Kotlin interface question,
  options, focused evidence, remaining uncertainty, and required return result.
- One integration owner reconciles language output with framework, data,
  security, package, runtime, and recovery state.
- Another reviewer can identify the next safe action without the original
  conversation or access to secret-bearing raw logs.

**Completion profiles**

Direct explanation: route, source scope, caveat, and stronger target claim not
made are enough.

Design handoff: add target preflight, executable requirements, modes,
alternatives, hard gates, selected boundaries, consumer inventory, planned
evidence, and conditional owners.

Implementation completion: add focused failure and accepted-case results,
configured build and affected regression evidence, generated and consumer
checks, clean artifact identity, and final asynchronous state.

Public migration: add source and binary policy, Java and wire consumers,
deprecation, coexistence, old and new artifact matrix, release authority,
rollback or roll-forward, and temporary mechanism retirement.

Code review: add risk-ranked findings, reachability, file locators, evidence,
counterargument, missing gates, and residual risk. Do not rewrite unrelated
code merely to satisfy the checklist.

Backend handoff: add framework, persistence, security, runtime, package,
shutdown, and recovery interfaces owned elsewhere, plus the exact Kotlin result
to integrate.

**Skeptical completion questions**

1. Which claim was hardest to prove, and was it narrowed instead of being
   upgraded by confident prose?
2. Which green gate could select no tests, use the wrong artifact, mock away the
   boundary, or finish before asynchronous work ends?
3. Which platform type, generated signature, Java caller, binary, serialized
   state, or framework mechanism remains outside local source inspection?
4. What target observation would make the chosen type, scope, or error model
   wrong?
5. Does a compatibility facade preserve every old behavior intentionally, or
   has it changed failure semantics while keeping the same signature?
6. Can cancellation or timeout leave blocking work, callbacks, resources, or
   effects active after the caller exits?
7. Did local Kotlin elegance move burden into every caller, backend owner, or
   future migration?
8. Is any not-applicable row based only on a name, visibility modifier, or local
   repository search rather than consumer evidence?
9. Is a public mapping or historical score being used as current or empirical
   authority?
10. Can another owner reproduce the evidence, understand what not to change,
    and retire temporary mechanisms safely?

Qualify this checklist through seeded defects, evidence sampling, second-reader
reconstruction, and escaped-state review. Promote stable invariant checks into
types, compiler policy, configured static analysis, or CI. Retire manual rows
only when stronger prevention preserves both coverage and diagnosis.

## Adjacent Reference Routing

`adjacent_reference_guidance`: Keep one accepted outcome and integration owner.
Route one named uncertainty to the smallest source or owner that controls it,
then reconcile the returned contract with the target code, consumers, artifact,
and lifecycle. Do not open another reference merely because its filename shares
a keyword.

**Frozen `kotlin-coder-01` routes read for this evolution**

| destination | route_when | question_to_answer | return_with |
| --- | --- | --- | --- |
| `agents-used-monthly-archive/codex-skills-202606/kotlin-coder-01/SKILL.md` | activation, work mode, output shape, or generic-versus-backend boundary is unclear | Should the generic Kotlin language route lead, support, or leave the task? | lead mode, support interfaces, preserved scope, and first gate |
| `agents-used-monthly-archive/codex-skills-202606/kotlin-coder-01/references/reference-map.md` | a local mechanism region must be found with minimal context | Which frozen reliability and final-check regions own this risk? | selected regions, skipped regions, and widening event |
| `agents-used-monthly-archive/codex-skills-202606/kotlin-coder-01/references/kotlin-reliability-reference.md` | type, nullability, interop, coroutine, test, or build rationale is needed | Which generic Kotlin candidate, failure boundary, and caveat apply? | candidate mechanisms, counterexample, and target questions |
| `agents-used-monthly-archive/codex-skills-202606/kotlin-coder-01/references/kotlin-quality-gates-and-anti-patterns.md` | implementation or review needs a skeptical closing pass | Which recurring failure and target-native gate must be challenged? | confirmed or rejected findings, gate family, and exception boundary |
| `agents-used-monthly-archive/codex-skills-202606/kotlin-coder-01/references/sources-and-research-brief.md` | historical provenance or a future refresh route matters | What prior source lineage was recorded and which current claim remains unverified? | dated provenance, candidate primary authority, and no-currentness limit |

**Observed working-corpus routes**

The following paths exist under `idiomatic-ref-202607/`. Path existence is a
navigation fact. Except where read and completed by this Beta lane, it does not
establish current contents, completeness, or authority. Read the selected
destination before applying it.

| working_reference | observed_or_read_status_here | route_when | interface_question |
| --- | --- | --- | --- |
| `kotlin_reliability_reference_patterns-20260710.md` | path observed only | deeper generic Kotlin reliability patterns lead | Which type, nullability, coroutine, interop, or test pattern owns the defect? |
| `kotlin_quality_antipattern_gates-20260710.md` | path observed only | a Kotlin-specific anti-pattern or gate catalog is the needed artifact | Which finding is reachable and which configured gate can expose it? |
| `kotlin_reference_routing_sources-20260710.md` | path observed only | source routing and research provenance are the primary uncertainty | Which source role and currentness boundary supports the claim? |
| `kotlin_backend_skill_entrypoint-20260710.md` | path observed only | a backend Kotlin delivery route may need activation | Should framework, persistence, security, runtime, or delivery own the outcome? |
| `kotlin_backend_reference_routing-20260710.md` | Beta-evolved and completely reread before this assignment | several backend specialist references or owners must be composed | Which backend mode, local source, target owner, and evidence sequence should lead? |
| `kotlin_backend_playbook_reference-20260710.md` | path observed only | service anatomy, contracts, errors, transactions, clients, workers, or architecture leads | What application and state boundary must the Kotlin design preserve? |
| `kotlin_spring_ktor_idioms-20260710.md` | path observed only | Spring or Ktor mechanism, plugin, proxy, route, serialization, or framework lifecycle is uncertain | Which version-bounded extension point implements the contract? |
| `kotlin_backend_testing_fixtures-20260710.md` | path observed only | backend fixture fidelity, framework test type, database, client, worker, or contract testing leads | What is the lightest backend test that can expose this defect? |
| `kotlin_backend_security_resilience-20260710.md` | path observed only | trust, validation, auth, secrets, retry, idempotency, abuse, or external effects lead | Which security or repeated-effect contract constrains the Kotlin boundary? |
| `kotlin_backend_runtime_operations-20260710.md` | Beta-evolved and completely reread before this assignment | config, secrets, migrations, telemetry, package, CI, rollout, health, shutdown, or recovery leads | Which runtime lifecycle and operational evidence must the language result integrate with? |

The corresponding frozen `kotlin-backend-delivery-01` skill and its reference
set were read completely during the prior Beta routing assignment. They remain
historical sources. The working references above can have other owners and must
not be edited or treated as complete from this path inventory.

**Target and authority routes**

| receiving_role | route_when | minimum_language_handoff | required_return |
| --- | --- | --- | --- |
| repository or library owner | accepted behavior, public scope, support range, deprecation, or ownership is unclear | target revision, API or symbol, current consumers, proposed invariant, and evidence | approved contract, support policy, owner, and constraints |
| Java consumer owner | names, nullability, overloads, exceptions, generics, defaults, value classes, or binary behavior affect Java | generated or published JVM surface, representative calls, change options, and focused result | supported caller matrix, compatibility decision, and consumer gate |
| serialization or schema owner | sealed members, enums, data classes, value classes, defaults, unknown values, or wire shape change | current and candidate schemas, artifacts, consumers, and failure cases | evolution policy, old/new compatibility, migration, and contract tests |
| build or artifact owner | wrapper, Kotlin or Java version, plugins, generated code, API baseline, packaging, or publication changes | effective build state, intended artifact, requested change, and gate gap | applicable task and policy, artifact identity, negative control, and release evidence |
| framework owner | Spring, Ktor, dependency injection, proxy, reflection, binding, routing, or lifecycle decides behavior | Kotlin-side contract, target framework and version, current integration, and unresolved mechanism | version-bounded extension point, integration constraints, and real framework gate |
| data or persistence owner | identity, equality, transactions, schema, migration, historical rows, or recovery is consequential | type and invariant proposal, persistence mechanism, consumers, and compatibility concern | data contract, migration states, dialect evidence, and recovery authority |
| security owner | authorization, secret, private data, validation, audit, unsafe deserialization, or exposure is involved | Kotlin boundary, identities, data, failure states, and proposed output | applicable policy, abuse cases, effective authority, and acceptance |
| runtime or platform owner | dispatcher capacity, blocking isolation, health, traffic, termination, process scope, resource, or recovery is platform-controlled | coroutine and blocking contract, package state, signals, and final-state uncertainty | platform policy, staged lifecycle evidence, limits, and stop authority |
| external library or provider owner | nullability, error, retry, cancellation, effect, quota, ordering, or compatibility semantics are unresolved | exact coordinate, mode, operation, observed behavior, and bounded question | supported contract, version, exceptions, and target reproduction requirement |
| current primary documentation | a version-sensitive language, coroutine, tool, or framework fact remains unresolved and browsing is authorized | exact target coordinate, symbol or mechanism, claim, and consequence | source URL or revision, retrieval date, version, fact, caveats, and conflict |
| incident command | active shared harm crosses services, dependencies, or owners | artifact, current state, Kotlin failure path, containment constraints, and evidence | common authority, timeline, containment, service actions, and closure criteria |

**Routing protocol**

1. State the accepted outcome and current lead. If neither is clear, route first
   to requirements or ownership, not another technology document.
2. Name one unresolved interface question. Examples: `Can this Java return be
   null in the resolved version?` or `Who owns cancellation after process
   termination begins?`
3. Identify the behavior owner. Use frozen local material for orientation,
   target state for what is used, accountable policy for what is accepted,
   current primary authority for supported version behavior, and execution for
   observed outcome.
4. Send the smallest access-safe handoff: revision, artifact, mode, symbol,
   callers, current state, observed failure, alternatives, evidence already
   run, and exact decision requested.
5. Require a return containing decision, evidence, limits, unresolved conflict,
   owner, and event that changes the answer.
6. Reconcile the return with Kotlin values, callers, scopes, artifacts, wire
   forms, framework state, and backend lifecycle as activated.
7. Run or update the affected target gate. A handoff answer is not
   implementation evidence.
8. Stop when the decision has sufficient authority and evidence. More routing
   is not completion.

**Minimal handoff record**

```text
handoff_id:
accepted_outcome_and_lead:
target_revision_module_artifact:
kotlin_interface_question:
current_types_callers_scopes_and_effects:
effective_versions_plugins_and_generated_surface:
observed_failure_and_evidence:
alternatives_and_hard_gates:
why_receiving_role_owns_it:
sensitive_or_access_boundaries:
decision_or_action_requested:
required_return_evidence:
return_recipient:
reroute_or_invalidation_event:
```

**Routing examples**

Platform type: language route leads conversion of an unannotated Java value.
External-library authority answers whether null is supported for the resolved
version; target tests reproduce null and non-null; Java owner confirms consumer
shape. No backend route is needed unless remote-client lifecycle matters.

Public sealed outcome: type mode proposes a closed state, while serialization
and Java owners establish extension and compatibility. One integration owner
decides whether the type stays internal, gains an unknown state, or requires a
versioned public migration.

Coroutine worker: backend playbook owns durable work and effects; security and
resilience owns idempotency and retry; runtime operations owns package shutdown
and restart; language mode owns structured coroutine and cancellation at the
adapter. All results reconcile in a phase-interruption scenario.

Spring or Ktor endpoint: framework route owns binding, proxy, serialization,
status, and lifecycle. Language mode can support nullability and domain outcome
design. A Kotlin unit test cannot replace framework integration evidence.

Pure syntax question: answer directly from known language context or future
versioned authority when needed. Do not create a backend or multi-agent route.

Shared incident: incident command leads containment and common state. Language
guidance can identify cancellation or platform-type hypotheses but does not
independently mutate provider, traffic, credential, or deployment policy.

Borderline performance defect: latency may come from hidden blocking,
dispatcher saturation, database pool, serialization, telemetry, or platform
resources. Gather call-path and resource evidence first; route to the owner
selected by the first discriminating observation rather than broadcasting the
problem to every reference.

**Anti-loop and ownership rules**

- Two routes cannot independently lead the same decision. Split interfaces or
  name one integration owner.
- Return to a prior route only when new evidence invalidates an earlier
  assumption; record the delta.
- Do not ask another owner to `review everything`. State the exact transition,
  consumer, or mechanism.
- A reference route grants no authority to edit another owner's files, install
  tools, mutate shared baselines, run destructive commands, or change
  production systems.
- If no owner accepts a consequential boundary, stop and escalate instead of
  routing indefinitely.
- If several routes repeatedly travel together, consider a stable interface
  checklist or test rather than copying their full prose into this entrypoint.
- Retire destinations when paths, architecture, ownership, or mechanisms change.

Review routing quality from resolved questions, reroutes, handoff rework,
context needed, unowned boundaries, and post-integration escapes. Keep durable
route names based on state ownership such as language contract, artifact, data,
identity, work, runtime, and recovery rather than transient team names.

## Workload Model

`combined_evidence_inference_note`: Treat Kotlin Language Skill Entrypoint as an
agent workflow and language-boundary reference, not a prose summary. The seed's
limits of one task, ten sources, and three delegated subtasks have no measured
basis in the frozen corpus and are not general capacity rules.

Workload is the set of independently failing decisions, consumers, execution
states, and evidence tiers that must be reconciled for one accepted outcome.

**Workload dimensions**

| dimension | low_pressure_shape | pressure_that_requires_widening_or_split | evidence_to_collect |
| --- | --- | --- | --- |
| requested action | one explanation, local implementation, or bounded review | mixed design, migration, incident, and release authority in one request | user authorization, accepted deliverable, changed and unchanged scope |
| Kotlin surface | one pure or internal language boundary | types, Java, coroutines, flow, generated code, serialization, and build interact | symbols, call paths, modes, and causal failure map |
| state space | small owned normal and failure model | open protocol, historical data, partial transition, unknown states, or external effects | state machine, owner, intermediate states, and reconciliation |
| consumer breadth | proven local Kotlin callers | Java, binary, wire, reflection, framework, generated, public, or external consumers | inventory, support policy, artifact identities, and compatibility gates |
| execution ownership | synchronous or one caller-owned coroutine | multiple scopes, callbacks, hot flows, blocking clients, durable work, or process lifecycle | scope tree, dispatcher, resources, effects, cancellation, shutdown, final state |
| generated mechanisms | none or a stable qualified local plugin path | compiler plugins, proxies, annotation processing, serialization, reflection, or code generation change surface semantics | effective versions, generated signatures, clean build, real-boundary tests |
| build topology | one module and wrapper with known tasks | multi-module, composite, multiplatform, mixed Java/Kotlin, custom source sets, publication, or several artifacts | build graph, toolchain, task selection, artifacts, cache inputs, and owners |
| compatibility transition | private implementation with atomic update | public deprecation, coexistence, facades, old and new artifacts, wire or data migration | migration sequence, supported combinations, rollback or roll-forward, retirement |
| source uncertainty | one frozen region and target facts settle the question | conflicting local, target, current authority, and observed evidence | claim ledger, version, conflicts, discriminating scenario, and decision owner |
| verification fidelity | pure or compile gate represents the failure | Java, coroutine, serialization, API, real dependency, framework, package, platform, or incident evidence is needed | requirement-to-gate map, negative control, environment, result, stronger claim |
| ownership | one reachable module owner | independent language, library, framework, data, security, artifact, runtime, or incident authorities | decision interfaces, recipients, escalation, and integration owner |
| irreversibility | local reversible code and test change | published break, persistent data, external effect, security exposure, or destructive operation | hard gates, authority, safe intermediate state, containment, and recovery |
| context and coordination | relevant code and sources remain reviewable together | target evidence is displaced, multiple agents redefine one contract, or resume state is fragile | ranked context map, exclusive ownership, checkpoints, and merge protocol |

File count and line count can predict reading effort, but they do not define
semantic workload. One public generic signature can have more coordination
pressure than a large private implementation refactor.

**Workload profiles**

| profile | choose_when | execution_shape | completion_gate |
| --- | --- | --- | --- |
| direct_language_answer | no target mutation or compatibility claim and one concept is bounded | answer from supplied context or applicable authority with caveat | question answered and stronger target claim excluded |
| focused_language_change | one owned Kotlin boundary and local consumers dominate | one lead mode, selected source region, focused tests, affected build | behavior and activated regression gates pass; no hidden adjacent owner |
| composed_language_change | several language modes share one API or artifact outcome | one lead mode, bounded specialist interfaces, one activation contract | every interface plus integrated caller and artifact scenario passes |
| compatibility_migration | public Kotlin, Java, binary, wire, or generated consumers transition | versioned current and candidate surfaces, coexistence, consumer waves, retirement | every supported intermediate combination is usable and recoverable |
| backend_support | framework, data, security, runtime, or release route owns the outcome | language workstream returns type, nullability, coroutine, or interop contract | backend integration owner validates full lifecycle and final state |
| exploratory_discovery | target or consumer state is insufficient to choose representation | ranked hypotheses, focused traces, small reversible probes, explicit stop | a bounded route is selected or missing authority receives a precise handoff |
| distributed_independent_work | workstreams own different artifacts and stable interfaces | exclusive writes, frozen contracts, local gates, frequent integration | local, interface, and end-to-end gates pass before acceptance |
| coordinated_transition | no safe independent rollout exists across consumers or owners | one program or migration authority sequences states and controls stop or recovery | every intermediate state, artifact, consumer, and owner decision is explicit |
| incident_support | active harm makes common state and containment primary | incident command leads; language specialists supply bounded causal evidence | accepted system state and residual owner closure, not local code green alone |

**Split and composition rules**

Keep one route when one owner can state the complete outcome, the target surface
fits in context, all consequential transitions share a coherent artifact and
evidence plan, and recovery or rollback remains understandable.

Split or compose when:

- public API and internal implementation have independently versioned owners;
- Java, binary, wire, persistence, or framework consumers require distinct
  migration and evidence;
- coroutine lifetime and backend durable-work lifecycle cannot be tested in one
  language-level gate;
- multiple artifacts promote independently or support mixed versions;
- a security, data, platform, or incident owner must accept consequential state;
- context required for one boundary displaces the evidence needed for another;
- independent work can proceed behind a stable interface and intermediate state.

Do not split when both workstreams would redefine the same sealed state,
nullability contract, public signature, dispatcher ownership, compatibility
baseline, or requirement. Resolve that shared decision first.

**Parallel execution contract**

- Assign exclusive write ownership per file, module, schema, baseline, or
  decision record.
- Freeze interface inputs and outputs: type shape, nullability, errors,
  cancellation, Java surface, version, artifact, and evidence required.
- Persist packet, design, and implementation units at the required cadence.
- Run a local sanity gate after each atomic save and stop on structure,
  compilation, consumer, or evidence failure.
- Integrate before every workstream has optimized independently around stale
  assumptions.
- Record changes to shared interfaces and reroute dependent work immediately.
- Preserve user changes and never use parallelism as authority for conflicting
  edits, destructive operations, or production mutation.

**Context selection**

1. Start with applicable instructions and the accepted outcome.
2. Locate the edited API or execution entry point and trace direct callers,
   consumers, generated surfaces, and tests.
3. Rank context by causal relevance: boundary implementation, failing case,
   caller contracts, build and generated mechanisms, then broader architecture.
4. Read compact local routing sources completely and deeper regions selectively.
5. Reserve context for a counterexample, rejected option, and strongest missing
   evidence rather than filling it with repeated summaries.
6. Persist a locator and decision map before interruption or delegation.
7. Widen only when a discovered edge changes consequence, ownership,
   compatibility, or verification fidelity.

Repository-native dependency or graph tools can accelerate narrowing when they
are available and qualified. Text search remains appropriate for build config,
annotations, task names, error strings, and non-code artifacts. A large
unranked file list is not a workload model.

**Examples**

Small code, large workload: a one-line change adds a sealed variant to a
published library used by Kotlin, Java, and serialized consumers. The diff is
small, but compatibility, unknown-state, artifact, migration, and owner
dimensions require a coordinated route.

Large code, focused workload: an internal parser refactor touches many lines but
keeps one module, one raw boundary, no Java or public consumers, and robust
property plus regression tests. One language route can remain coherent.

Safe composition: a suspend Java adapter change separates nullability,
interop, and cancellation questions. One API owner integrates them; each mode
returns a bounded contract; Java and coroutine tests exercise the combined
surface.

Unsafe parallel work: one agent introduces a sealed result while another changes
Java overloads and exception mapping without a frozen public contract. Both can
pass local tests yet publish incompatible meanings. Sequence the shared API
decision first.

Backend support: language work contains a platform type and preserves
cancellation at a worker adapter. Backend owners separately decide transaction,
acknowledgment, retry, shutdown, and recovery. A phase-interruption integration
gate reconciles the interface.

Conditional discovery: local search finds no Java caller, but the artifact is
public and consumer policy is unavailable. Internal implementation review can
proceed; public compatibility remains conditional and blocks a breaking API
change.

**Workload record**

```text
accepted_outcome_and_action:
kotlin_surfaces_and_state_spaces:
callers_consumers_and_artifacts:
execution_scopes_blocking_and_effects:
generated_framework_and_build_topology:
compatibility_and_intermediate_states:
source_and_target_uncertainty:
verification_tiers_and_environments:
owners_and_authorities:
irreversible_or_sensitive_boundaries:
context_map_and_omissions:
selected_workload_profile:
split_or_compose_interfaces:
integration_owner_and_gates:
conditional_boundaries:
invalidation_and_coordination_retirement:
```

**Qualification and feedback**

After completion, compare the model with actual source loading, reroutes,
rework, consumer discoveries, gate failures, merge conflicts, and escaped
states. Distinguish errors in workload classification from ordinary
implementation difficulty. Do not infer universal agent capacity from one
duration or task count.

Promote recurring independent boundaries into dedicated source routes, test
fixtures, compatibility policies, or owner interfaces only when their
maintenance value exceeds added discovery cost. Retire temporary coordination
after migration and consumer evidence close. The goal is coherent accountability,
not maximum decomposition or minimum context at any cost.

## Reliability Target

The seed's perfect percentage, fixed eighteen-of-twenty sample, zero-rate claim,
and universal recovery wording lack a population, baseline, measurement system,
or accountable owner. They are not empirical targets.

Reliability has two layers:

1. Reference conformance is deterministic because the complete reference,
   packet, seed, and frozen sources are inspectable.
2. Target Kotlin reliability concerns language boundaries, consumers, lifetime,
   artifacts, and evidence. Values and risk acceptance come from target owners
   and qualified observations.

**Deterministic reference invariants**

| invariant | required_state |
| --- | --- |
| headings | exactly 26 original texts in original order and no added reference headings |
| section depth | every evolved section strictly exceeds its seed and contains useful reasoning rather than repeated filler |
| packet structure | 26 sections, 260 exact questions, and 1,560 mandatory values in the required order |
| packet substance | all 1,560 values remain exact-unique and prefix-stripped normalized-unique |
| frozen identity | archive seed, 115 queue spans, canonical skill, and four companion hashes remain unchanged |
| hygiene | ASCII, final newline, no trailing whitespace, unresolved markers, malformed tables, unclosed fences, or duplicated generic blocks |
| review | complete packet and reference rereads are checkpointed through all 26 sections |
| focused status | repository verifier reports pass for this exact path and packet |

Failure of one reference invariant makes the artifact nonconforming. These rows
are not a service objective and must not be averaged.

**Target reliability hierarchy**

| layer | purpose | contract_shape | authority |
| --- | --- | --- | --- |
| user_and_consumer_outcome | state what Kotlin, Java, framework, or downstream consumers must experience | accepted value, explicit absence or failure, cancellation, compatibility, and migration outcome | product, library, API, and consuming owners |
| hard_invariant | identify states that aggregate success cannot trade away | no platform uncertainty past adapter; no swallowed cancellation; no unapproved public break | accepted requirement and applicable policy |
| scenario_contract | exercise rare or high-consequence state directly | null, unknown state, child failure, cancellation phase, Java call, old and new artifact | implementation and test owners with consumer review |
| measured_objective | bound recurring target behavior over a defined population | locally owned route delay, gate reliability, defect discovery, or migration objective | accountable owner using qualified data |
| diagnostic_indicator | help explain boundary and gate health | assertion occurrence, platform leak, detached work, test selection, compatibility drift | mechanism and tooling owners |
| degraded_or_conditional_state | describe unavailable consumer, version, environment, or evidence | narrower layer passes while stronger claim is blocked | integration owner and missing-boundary owner |
| recovery_or_migration_contract | return APIs, callers, artifacts, and temporary mechanisms to accepted state | rollback, roll-forward, facade retirement, consumer migration, or evidence repair | release, artifact, consumer, and integration owners |

A diagnostic indicator is not a reliability objective merely because it is easy
to count. A clean compile can coexist with a Java binary break or work that
continues after cancellation.

**Language and consumer dimensions**

| dimension | hard_questions | degraded_or_failure_states | evidence |
| --- | --- | --- | --- |
| target identity | Are source, versions, plugins, generated code, tests, and artifact coherent? | wrong module, stale cache, different compiler, substituted artifact | wrapper resolution, clean build, artifact and generated-surface checks |
| raw and platform input | Does uncertainty become explicit once before domain use? | assertion crash, implicit non-null assignment, repeated inconsistent validation | Java or raw boundary fixtures, malformed and historical inputs, adapter tests |
| domain states | Are absence, invalidity, failure, cancellation, and unknown states distinguishable where consequential? | booleans, sentinel values, nullable conflation, lost future state | state behavior, caller exhaustiveness, unknown input, mapping and round-trip tests |
| value and object semantics | Do construction, equality, copy, identity, mutation, and lifecycle match the contract? | wrong identifier accepted, unsafe copy, identity collapse, mutable alias | invariant, equality, copy, persistence, serialization, and framework scenarios |
| coroutine lifetime | Is all work owned, cancellable as promised, and finalized safely? | detached child, swallowed cancellation, continued effect, resource leak | cancellation and failure injection at phases, child and final-state observation |
| blocking and capacity | Is blocking explicit or isolated under target policy? | dispatcher starvation, timeout mismatch, uninterruptible work, shutdown delay | real adapter concurrency, thread or dispatcher, resource, and cancellation evidence |
| flow semantics | Are producer, collector, sharing, buffer, callback, completion, and cleanup owned? | producer leak, stale callback, buffer growth, lost terminal state | collect, cancel, fail, complete, restart, and resource scenarios |
| Java interoperability | Are generated names, nullability, defaults, overloads, generics, exceptions, annotations, and boxing usable? | source compile break, ambiguous overload, unusable value class, wrong exception | representative Java callers and signature or artifact analysis |
| public compatibility | Do supported source, binary, wire, reflection, and framework consumers remain accepted? | unapproved break, unknown variant failure, old/new incompatibility | baseline comparison, downstream builds, contract and migration matrix |
| gate reliability | Does evidence select intended cases and causal boundary? | empty pass, flaky result, wrong artifact, mocked-away defect, async leakage | negative control, task selection, environment, result, final-state audit |
| route reliability | Does language work lead only its owned outcome and hand off adjacent state? | wrong mode, context dump, route loop, unowned backend claim | representative route fixtures, handoff replay, reviewer and escape evidence |

Activate only dimensions whose states can occur. Record the target fact that
supports every exclusion.

**Reliability contract record**

```text
contract_id_and_owner:
accepted_user_and_consumer_outcomes:
population_or_direct_scenario:
target_revision_artifact_and_versions:
normal_absent_failed_canceled_and_recovered_states:
hard_invariants:
target_owned_objective_if_any:
measurement_or_scenario_definition:
inclusions_exclusions_and_missing_data:
supported_consumers_and_compatibility:
signals_gates_and_coverage:
degraded_or_conditional_behavior:
decision_actions_and_authority:
verification_tiers_completed:
residual_risk_and_stronger_claim_not_proved:
recalibration_invalidation_and_retirement:
```

Do not fill this record with plausible percentages or latency values. If no
owner objective exists, retain a direct invariant or comparative hypothesis and
state which stronger decision remains unavailable.

**Objective selection**

1. Start with the user or consumer outcome and consequence of failure.
2. Define hard invariants that cannot be traded for aggregate success.
3. Identify the population: route decisions, APIs, calls, work items, consumers,
   artifacts, migrations, or scenarios actually represented.
4. Define normal, absent, invalid, failed, canceled, incompatible, and recovered
   states as applicable.
5. Use measured objectives only where events, definitions, and data quality
   support them. Use direct scenarios for rare and severe states.
6. Map every indicator to a decision. Remove metrics with no consumer or action.
7. Qualify missing consumers, flaky tests, retries, generated code, delayed
   reports, external artifacts, and evidence-system failure.
8. Add target-appropriate failure and compatibility scenarios.
9. Review whether the objective can be improved by hiding failure, excluding
   hard tasks, weakening tests, or shifting migration burden elsewhere.

**Evidence tiers**

| tier | establishes | does_not_establish |
| --- | --- | --- |
| deterministic_logic | controlled parsing, invariant, state transition, equality, and selection behavior | Java platform inference, coroutine runtime, generated code, public consumers, or framework behavior |
| compile_and_static | source typing and configured static policy for selected modules | runtime state, Java ergonomics, binary compatibility, or failure timing |
| language_boundary | actual Java adapter, coroutine, flow, serialization, or generated surface in a controlled target | all downstream artifacts, production scheduling, or backend lifecycle |
| compatibility | selected source, binary, wire, or downstream consumer combinations | every external consumer or future release |
| framework_or_package | target framework integration or packaged artifact under recorded configuration | universal platform, workload, provider, or production behavior |
| downstream_or_incident | actual observed consumer or production state for a recorded event | complete causal certainty or future outcomes |

Confidence increases per bounded claim. It does not become a universal
percentage.

**Good and bad contracts**

Good platform invariant: every target path from an unannotated Java return to
domain code passes through one adapter that classifies null and value according
to the owner-approved contract. Java-origin null and value tests plus caller
inspection qualify the boundary. The claim does not extend to another library
version automatically.

Bad nullability target: `zero null failures`. It lacks a population, detection
coverage, platform sources, historical data, generated paths, and distinction
between meaningful absence and invalid null.

Good cancellation contract: every request-owned child ends or transfers to an
explicit durable owner when the caller cancels; cancellation is not converted
to ordinary failure; resources and effects reach accepted final states. Phase
injection exercises the actual adapter.

Bad coroutine target: `all suspend functions are nonblocking`. A suspend
modifier neither proves cooperation nor reveals legacy client, filesystem,
JDBC, native, or CPU-heavy work.

Good compatibility contract: all owner-supported Kotlin and Java source
callers, configured binary baseline, serialized states, and old/new artifact
combinations activated by the change pass or follow an approved migration.

Conditional compatibility: local Kotlin and Java fixtures pass, but public
external consumer inventory is unavailable. Internal behavior can pass;
breaking publication remains blocked pending release-owner authority.

Good route contract: representative fixtures distinguish language lead,
backend lead, support mode, direct answer, and stop state; wrong routes and
reviewer disagreements are retained. No universal accuracy rate is claimed
from a small set.

**Reliability decision loop**

At implementation or review, verify the activated hard invariants and evidence
tiers. On violation, preserve target and artifact state, classify the earliest
broken boundary, contain only under authority, and correct the owning design or
gate. After migration or recovery, confirm callers, artifacts, state, children,
resources, and temporary mechanisms reached accepted conditions.

Recalibrate when Kotlin, Java, coroutine, plugin, framework, consumer, artifact,
wire, workload, ownership, test, or incident evidence changes materially.
Retire indicators with no decision. Preserve direct scenarios for rare severe
states even when aggregate builds and review flow look healthy.

Reliable guidance makes absence, failure, cancellation, incompatibility, and
conditional evidence visible. Concealing those states to protect a success
number is itself a reliability failure.

## Failure Mode Table

Treat each row as a causal hypothesis. Before action, preserve target revision,
artifact, effective versions, generated surface, failing input, caller, scope,
task selection, timestamps, and access-safe diagnostics. Target owners govern
public migrations, destructive changes, security decisions, backend lifecycle,
and production response.

| failure_mode | discriminating_evidence | likely_consequence | immediate_containment_question | durable_correction | recovery_proof | escalation_or_limit |
| --- | --- | --- | --- | --- | --- | --- |
| wrong_skill_or_mode | accepted outcome and strongest consequence are owned by another route despite a Kotlin keyword | irrelevant sources, wrong files, and locally elegant but incomplete design | Can implementation pause while the lead owner and changed state are clarified? | reroute by outcome, keep one Kotlin interface question, and preserve gathered target facts | receiving owner accepts handoff and integrated gate covers the full outcome | stop if no owner accepts framework, data, security, runtime, or migration state |
| frozen_or_public_source_drift | local hash, source date, target version, or future current authority conflicts with reused guidance | stale semantics or compatibility assumptions guide implementation | Can the dependent claim remain conditional while exact provenance is checked? | refresh only the bounded claim when authorized and update dependent decisions selectively | target scenario passes under applicable source and version | unresolved authority conflict belongs to source and target owners |
| target_toolchain_drift | local, CI, generated, published, or deployed Kotlin, JVM, plugin, or dependency state differs | compile, ABI, serialization, proxy, bytecode, or runtime behavior diverges | Can build and publication stop until effective versions and artifacts are identified? | restore repository-owned alignment or run an explicit version migration | clean generated build, affected gates, artifact identity, and consumers agree | artifact and build owners decide shared toolchain or release changes |
| platform_type_null_escape | Java or generated value reaches non-null Kotlin state without validation | distant non-null failure, corrupted invariant, or inconsistent caller handling | Can the raw boundary be isolated while null semantics and affected callers are established? | normalize once into explicit value, absence, or typed failure at the adapter | Java-origin null and value cases plus downstream invariants pass | provider or generated-contract conflict requires owning authority |
| absence_state_conflation | null, boolean, empty value, or generic result represents missing, invalid, forbidden, unknown, and failure | callers make unsafe or inconsistent decisions and future states disappear | Which consumers and effects depend on each meaning, and can ambiguous operations pause? | model only consequential distinctions using target-compatible states and mappings | all accepted states, unknown input, and callers reach intended outcomes | open protocols and public wire forms require schema or provider ownership |
| non_null_assertion_crash | `!!` is reachable from malformed input, old data, Java, reflection, or deserialization | runtime crash far from cause and incomplete diagnostics | Can invalid input be rejected or quarantined at the boundary without changing unrelated behavior? | parse or validate once and preserve meaningful absence or contract breach explicitly | representative valid, absent, malformed, and historical inputs pass | data or public contract repair may require backend or migration owner |
| value_or_class_semantic_mismatch | value class, data class, enum, sealed type, or plain class generated semantics differ from domain and consumer needs | wrong equality, copy, identity, serialization, Java shape, or framework behavior | Can public or persistent migration pause while current semantics are inventoried? | choose representation from invariants and consumers; stage facade or migration if needed | equality, copy, construction, wire, Java, persistence, and compatibility gates as activated | public, data, and framework owners accept breaking or persistent changes |
| mutable_alias_or_global_state_leak | callers mutate shared collections or singleton state outside ownership | cross-test contamination, race, hidden lifecycle, and nondeterministic behavior | Can mutation be isolated and concurrent access stopped without losing required state? | constructor-injected or scoped ownership, immutable views or snapshots, and explicit mutation API | concurrency, isolation, lifecycle, and cleanup tests pass | framework-managed state requires target lifecycle ownership |
| swallowed_cancellation | broad catch, retry, logging, or result normalization consumes cancellation | work continues after owner exit, retries, false failure, or unwanted effect | Can new work and retries stop while active child and effect state are observed? | preserve cancellation before ordinary errors and make cleanup narrow and bounded | phase cancellation ends children, releases resources, and leaves accepted effects | backend owner joins for process, queue, or external-effect lifecycle |
| detached_coroutine_or_flow | unowned scope, hot flow, callback, buffer, or producer outlives intended consumer | memory or resource leak, stale updates, invisible failure, and shutdown delay | Can collection or admission stop while ownership and active producers are inventoried? | caller or lifecycle scope, explicit sharing and buffer policy, callback cleanup, and terminal state | cancel, fail, complete, restart, and cleanup scenarios show no orphaned work | application or platform lifecycle owner controls long-lived scope |
| hidden_blocking_or_dispatcher_saturation | suspend path uses JDBC, filesystem, native, legacy SDK, DNS, or CPU work without honest isolation | latency, starvation, cancellation delay, health churn, and test mismatch | Can concurrency or admission be bounded while actual threads, pools, and calls are observed? | explicit blocking port or target-owned bounded execution and capacity policy | representative concurrency, cancellation, resource recovery, and final work state pass | service capacity, health, and shutdown belong to backend runtime owners |
| Java_surface_break | Kotlin signature, default, overload, value class, annotation, generic, exception, or name changes generated JVM use | supported Java source or runtime consumer fails after Kotlin build passes | Can publication hold while current artifact and Java consumers are identified? | preserve facade or run approved versioned interop migration with explicit generated surface | representative Java compile and run plus API or ABI evidence pass | unknown public consumers require release-owner risk decision |
| binary_or_wire_compatibility_break | published API, sealed or enum state, serialized shape, default, or generated signature drifts | old consumers fail to link, parse, or handle new state | Can promotion stop and old plus new artifacts remain available for diagnosis? | compatible evolution, coexistence, deprecation, facade, or coordinated breaking release | supported artifact and consumer matrix plus unknown-state and rollback or roll-forward evidence | artifact, schema, and consumer owners control support policy |
| generated_surface_mismatch | compiler plugin, proxy, serializer, annotation processor, or reflection produces behavior unlike source assumption | runtime construction, binding, interception, serialization, or API fails | Can generated output and effective plugin versions be captured before another build? | preserve or explicitly migrate plugin configuration and design against actual generated contract | clean generation, framework or serializer integration, and artifact inspection pass | framework and build owners resolve unsupported combinations |
| test_gate_no_op | task or filter selects no tests, wrong source set, stale cache, mocked boundary, or different artifact | green evidence fails to protect the intended defect | Can release or handoff pause while task selection and negative control are qualified? | fix selection, fixture fidelity, cache inputs, and artifact lineage | known defect fails; clean target executes expected cases and broader affected gates | build owner controls shared task and CI changes |
| coroutine_test_false_confidence | virtual time or test completion hides real blocking, detached children, callbacks, or effects | lifetime or performance defect survives despite green unit tests | Can the actual adapter and unfinished work be observed in a controlled environment? | add faithful execution fixture and final-state assertions; retain virtual tests for logical behavior only | real cancellation and cleanup path matches accepted contract | inaccessible provider or platform behavior remains conditional |
| compatibility_facade_semantic_drift | facade preserves signature but changes null, exception, default, mapping, or cancellation meaning | old callers compile yet observe different behavior | Can consumer rollout stop while old behavior and mappings are compared? | explicit mapping contract, old and new tests, versioning, and retirement criteria | representative old callers, new internal state, and failure mappings agree | owner decides whether behavioral break requires version migration |
| generic_advice_overreach | agent applies value, sealed, coroutine, or style patterns without target invariants or consumers | abstraction burden, broken integration, and unrelated churn | Which proposed changes lack a named defect or target gate and can be dropped? | preserve target stance and retain only patterns that remove demonstrated ambiguity | focused change passes while unrelated diff and toolchain remain stable | route unresolved framework or public policy questions to owners |
| context_or_progress_loss | interruption, stale summary, or unsaved work causes repeated or contradictory edits | duplicated packet content, wrong scope, lost user constraints, and overwritten collaborator state | Can work stop at the last durable atomic boundary and current instructions be reread? | immediate section saves, exact journals, immutable ownership, and resume from verified state | counts, hashes, headings, unique values, and current focus match durable record | do not guess shared state or revert another owner's work |
| parallel_decision_collision | multiple agents change one API, schema, baseline, route, or state model concurrently | locally passing but incompatible artifacts and meanings | Can conflicting writes pause and one decision owner reconcile the interface? | exclusive ownership, frozen contracts, frequent integration, and one verifier per invariant | local plus interface plus whole-artifact gates pass | coordinator or accountable owner resolves shared decision authority |
| backend_lifecycle_omission | language design claims safety while framework, data, auth, package, shutdown, or recovery state is untested | production behavior, effects, or recovery diverge from Kotlin unit evidence | Can adoption remain local or conditional while backend owner inspects lifecycle? | route full outcome to backend delivery and integrate bounded language contract | framework, data, package, shutdown, and recovery scenarios satisfy accepted state | language reference cannot accept backend operational risk |

**Response protocol**

1. Establish authority and preserve revision, artifact, consumer, scope, failure,
   and evidence state. Protect sensitive values and external effects.
2. Name the earliest observed contract violation, not the loudest exception or
   final failing build.
3. Keep competing hypotheses when platform, generated, version, fixture, or
   consumer state is uncertain.
4. Use an independent confirmation source when the suspected boundary includes
   a broken test, generated artifact, or asynchronous signal.
5. Identify possible amplification through retries, detached work, blocking,
   publication, migration, broad refactors, or parallel edits.
6. Apply the smallest reversible authorized containment. A source revert may be
   unsafe if public artifacts, wire forms, or consumer migration already changed.
7. Reassess after containment. A changed symptom can invalidate the original
   causal model.
8. Correct the owning boundary and add the earliest faithful gate that would
   have detected the failure.
9. Verify callers, artifacts, children, callbacks, resources, compatibility,
   and temporary controls reached accepted final state.
10. Convert repeated causal failures into type prevention, source routing,
    configured gates, or owner interfaces only after checking side effects.

**Failure interactions**

- A platform type can be hidden by a value class, serialized into persistent
  state, and exposed through a Java facade. Repair and evidence must follow the
  whole activated path.
- A broad catch can swallow cancellation, trigger retry, keep blocking work
  alive, and make a facade report an ordinary failure while an effect continues.
- Compiler or plugin drift can alter generated signatures, make compatibility
  baselines incomparable, and cause tests to run against a different artifact.
- A no-op gate can make a wrong route look complete. Verify task selection
  before interpreting source guidance or adding more tests.
- Context loss and parallel decisions can create two internally coherent but
  incompatible state models. Preserve one source of truth and integration owner.
- Backend lifecycle omission can make clean coroutine completion irrelevant to
  durable work, process termination, or recovery.

**Response examples**

Good platform response: a null failure appears after a Java library upgrade.
Confirm the deployed or tested dependency and generated signature, preserve the
failing input, contain at the adapter, classify null semantics with provider and
owner evidence, test Java-origin null and value cases, and rerun affected
callers. Do not scatter assertions or nullable fields through the domain.

Bad coroutine response: a timeout occurs, so the agent adds retries and a
larger dispatcher without checking whether cancellation was swallowed or the
client call blocks. Work amplification and resource pressure worsen.

Good compatibility response: a Java consumer fails after a Kotlin default-
argument change. Hold publication, compare artifacts and generated signatures,
preserve or restore the facade, add the representative Java fixture and target
compatibility gate, then choose a versioned migration if the change is still
required.

Conditional generated response: source and unit tests pass, but framework proxy
behavior cannot be reproduced. Mark language behavior passed, keep framework
adoption conditional, and hand exact versions, generated surface, and expected
scenario to the framework owner.

**Failure qualification record**

```text
failure_id_and_target_revision:
violated_contract_and_consumers:
artifact_versions_and_generated_surface:
input_scope_execution_and_timeline:
primary_symptom:
independent_confirmation:
competing_hypotheses:
amplification_paths:
containment_and_authority:
containment_result:
durable_correction:
focused_and_regression_evidence:
caller_artifact_async_and_effect_final_state:
residual_uncertainty_and_owner:
route_gate_or_source_change:
invalidation_or_control_retirement:
```

Prioritize target failures by consequence, reachability, irreversibility,
detection coverage, recurrence, and recovery difficulty. Do not assign universal
likelihood or severity numbers. Retire a row when its mechanism disappears or
stronger prevention and diagnosis subsume it; preserve enough provenance to
explain why the replacement control exists.

## Retry Backpressure Guidance

`retry_backpressure_default`: Do not repeat an operation until the failure,
effect boundary, remaining deadline, cancellation, capacity, target policy, and
terminal state are known. Fail without automatic retry for deterministic or
unauthorized states. Reconcile ambiguous effects before replay. Admit only work
that has a bounded owner-visible wait, drop, failure, or durable handoff.

This section defines language and agent-workflow safety. Backend owners select
provider-specific attempts, delays, queue capacity, traffic policy, and
production controls.

**Failure classification**

| failure_class | default_disposition | repeat_can_be_valid_when | primary_risk |
| --- | --- | --- | --- |
| invalid_input_or_invariant | return explicit failure without automatic repeat | caller changes input or relevant domain state | repeated CPU, logs, and confusing delayed failure |
| platform_null_or_contract_breach | preserve failing value and classify boundary contract | dependency, annotation, adapter, or fixture state is corrected | recurring crash and propagation of false non-null trust |
| deterministic_implementation_defect | fail, preserve reproduction, and repair code | implementation or relevant target state changes | retry hides cause and multiplies work |
| unsupported_version_or_generated_surface | stop and select compatible target or explicit migration | aligned artifact, plugin, compiler, or consumer becomes effective | repeated incompatible builds and misleading partial green |
| denied_permission_or_owner_authority | stop dependent action and route to accountable owner | authority, credential, or policy is deliberately changed | unsafe workaround, lockout, audit noise, or shared-state harm |
| cancellation | propagate immediately, release owned resources, and preserve durable state | a durable owner deliberately resumes a known work identity | abandoned work continues or cancellation becomes ordinary failure |
| transient_pre_effect_failure | fail or repeat inside one target-owned total budget | no effect crossed, condition can recover, capacity exists, and operation is repeat-safe | synchronized attempts and deadline exhaustion |
| optimistic_conflict | refresh current state and recompute rather than replay stale mutation | operation is safe to derive again and attempts remain bounded | starvation, lost update, and hot-key pressure |
| capacity_or_dispatcher_saturation | reduce admission, concurrency, or workload and allow recovery | capacity becomes available and a new wave will not recreate saturation | positive feedback, memory growth, and long recovery |
| timeout_before_proven_effect | classify phase before deciding | target semantics establish no effect occurred and remaining budget exists | misclassifying an ambiguous commit as safe retry |
| ambiguous_external_effect | enter explicit unresolved state and reconcile | stable effect identity or provider-supported idempotency proves repeat safety | duplicate or missing irreversible effect |
| flow_or_callback_overflow | apply target-owned drop, conflate, buffer, suspend, or fail policy | lost or delayed elements are acceptable and observable | silent data loss, stale updates, memory growth, and producer leak |
| flaky_or_inconclusive_gate | isolate evidence system rather than retry until green | clean task selection and controlled environment can produce a discriminating result | ceremonial passing and hidden defect |
| stale_external_evidence | keep currentness-dependent claim conditional | one bounded authorized refresh can change the decision | browsing loops and context displacement |
| missing_context_or_owner | pause only the dependent claim | target fact or owner decision is returned | speculative design and repeated broad source loading |

An exception class or HTTP-style label is not enough to classify phase or
effect. A timeout can occur before call, during blocking work, after an external
commit, or after the caller canceled while work continued.

**Retry contract**

Before enabling retry around Kotlin or Java work, record:

- the logical caller operation and stable identity;
- eligible and ineligible failure classes;
- the point at which data, message, file, or external effect can occur;
- whether repeat safety comes from purity, idempotency, deduplication,
  transaction, stable key, lookup, or reconciliation;
- the outer accepted deadline, cancellation owner, and remaining-budget rule;
- the single layer that owns attempts across gateway, client, coroutine, flow,
  worker, proxy, and caller;
- target-owned stop rule, delay or provider signal, dispersion, and fairness;
- dispatcher, thread, pool, semaphore, buffer, queue, and downstream capacity;
- per-logical-operation and per-attempt evidence;
- final failure, ambiguous state, durable handoff, quarantine, or owner action;
- shutdown, restart, and temporary-policy retirement semantics.

Count effective attempts across all layers. A client, proxy, caller loop, and
worker can each repeat while appearing locally bounded.

**Backpressure choices**

| choice | use_when | state_created | key_tradeoff_to_verify |
| --- | --- | --- | --- |
| fail_fast | invalid, unsupported, unauthorized, deadline-exhausted, or saturated work cannot succeed safely now | explicit rejection | caller retry, user impact, and error classification |
| bounded_concurrency | a scarce client, thread, CPU, memory, or effect boundary needs a cap | limited active set plus bounded wait or rejection | fairness, cancellation while waiting, and long-task head-of-line blocking |
| explicit_blocking_port | legacy or inherently blocking work must remain honest | synchronous caller responsibility | application isolation, timeout, and resource ownership |
| target_owned_dispatcher_isolation | blocking work is allowed under a configured execution boundary | bounded executor or dispatcher work | capacity, noncooperative cancellation, shutdown, and queue growth |
| suspending_buffer | producer can pause until consumer capacity returns | bounded delayed elements | deadlock, cancellation, fairness, and producer ownership |
| bounded_buffer_with_overflow | a target policy accepts drop or replacement under pressure | explicit loss or replacement state | which element is lost, user semantics, metrics, and recovery |
| conflation | only the latest state matters and intermediate values are intentionally obsolete | replacement of pending state | invalid use for events, commands, payments, or required transitions |
| sampling | representative observation is sufficient | intentional partial telemetry or processing | bias, rare-event loss, privacy, and decision validity |
| durable_handoff | work must outlive caller or process and an owned source exists | durable identity, status, and backlog | acknowledgment, duplicate, retention, cancellation, poison work, and recovery |
| reconciliation | effect outcome is unknown across systems | explicit unresolved record | lookup authority, final decision, privacy, and operational burden |
| operator_hold | high-consequence migration or publication needs human authority | paused change or work | response time, evidence freshness, and retirement of stale holds |

A buffer does not remove pressure. It stores delayed work and needs item-size,
age, capacity, overflow, cancellation, shutdown, and drain contracts. No
universal buffer or concurrency value is supplied here.

**Coroutine and Flow rules**

- Tie child work to caller or explicit lifecycle scopes. Do not use detached
  scopes as an overflow strategy.
- Preserve cancellation through catches, retry wrappers, logging, and result
  conversion. Cleanup must not restart canceled business work.
- Derive inner timeouts and attempts from one outer outcome budget where the
  target uses deadlines.
- Bound parallel child creation before launching work; a bounded downstream
  client does not make an unlimited coroutine launch harmless.
- Identify whether `Flow` carries states or events. Conflation may fit state and
  corrupt event semantics.
- Define cold versus shared collection, producer scope, callback registration,
  buffer, overflow, terminal event, and cleanup.
- Observe waiting and active work separately. Cancellation while waiting must
  remove ownership cleanly.
- A blocking Java call inside `withContext` may continue after coroutine
  cancellation if the call is noncooperative. Make residual work and effects
  visible and route service capacity or shutdown to backend operations.

**Testing and build retries**

Do not rerun a failing test without classifying deterministic failure, flaky
environment, task-selection error, stale generated output, cache issue, or real
race. Preserve the first failure and control one suspected source of variance.
A retry-until-pass policy hides evidence.

When a build or gate fails because a target artifact, version, or generated
surface is wrong, correct that state before repetition. Do not generate many
candidate artifacts while the evidence contract is red.

**Agent workflow backpressure**

- Save one complete packet section before its matching reference section, then
  run immediate sanity before starting another section.
- Stop generation when heading, packet grammar, uniqueness, source identity,
  test, or ownership gates fail. Repair the earliest incomplete boundary.
- Persist journal checkpoints no later than each required batch and phase;
  reread checkpoints prevent a complete review from living only in transient
  context.
- Re-read current instructions after interruption, ownership change, spec
  change, or contradictory user direction.
- Assign one writer per file or shared decision. Parallel agents may analyze
  independent surfaces but cannot redefine the same contract concurrently.
- Bound external research to one exact claim and authorized source route. Stop
  when execution or owner policy is the remaining uncertainty.
- Do not repeat destructive commands, compatibility baseline changes, commits,
  pushes, releases, or production actions without explicit authority.

These workflow controls protect artifacts and context. They do not prove a
Kotlin runtime retry policy.

**Verification scenarios**

| scenario | observe | accepted_shape | hidden_failure |
| --- | --- | --- | --- |
| invalid input | logical calls, attempts, CPU, logs, final state | one bounded explicit failure | caller or proxy silently repeats |
| transient pre-effect failure | per-layer attempts, deadline, resources, downstream load | bounded work fits policy and recovers | synchronized attempt wave after recovery |
| cancellation during retry | children, attempts, delay, resources, effects | attempts stop and cancellation propagates | broad catch returns ordinary failure |
| blocking call cancellation | coroutine state, thread, client, resource, effect | residual behavior matches explicit target contract | test ends while blocking work continues |
| flow overflow | producer, buffer, dropped or replaced elements, consumer, memory | target-owned loss or suspension semantics remain visible | silent event loss or unbounded callback queue |
| ambiguous write | operation identity, provider state, local result, repeat | reconciliation reaches one accepted final outcome | duplicate effect hidden by final success |
| recovery wave | pending work, attempts, resources, latency, final state | work subsides without a delayed second overload | buffered and retried work surges only after recovery |
| flaky test | task selection, environment, seed, scheduler, repeats | controlled evidence identifies cause or remains inconclusive | retries select the one convenient green run |
| source refresh | target coordinate, exact claim, result, decision delta | one bounded lookup resolves or preserves uncertainty | broad repeated search displaces target evidence |

**Examples**

Good transient retry: a target client proves a connection failed before request
acceptance; the logical operation is read-only; one layer owns attempts; the
outer deadline has budget; fault tests show cancellation stops attempts and
resources recover. Attempts and delays come from target policy, not this file.

Bad timeout retry: a Java client times out after an external write may have
committed. The Kotlin wrapper catches the timeout and retries without effect
identity. The final call succeeds while two effects exist.

Good flow backpressure: a UI-style state flow explicitly retains only the
latest state, and tests show intermediate values have no semantic obligation.
The same conflation policy would be rejected for audit events or commands.

Bad coroutine backpressure: launch one child per input without a bound and rely
on a limited dispatcher. Memory and queued continuations grow before the
dispatcher protects the external dependency.

Good evidence backpressure: a normalized duplicate appears after one packet
section. Work stops, that section is repaired, cumulative uniqueness passes,
the matching reference is saved, and the journal records the durable boundary.

Conditional provider case: local fake and released docs support cancellation,
but the managed provider and target client mode are unavailable. Language
behavior passes locally; resource and effect guarantees remain conditional.

**Policy record**

```text
operation_and_owner:
logical_identity_and_effect_boundary:
eligible_and_ineligible_failures:
repeat_safety_and_reconciliation:
outer_deadline_and_cancellation:
retry_owning_layer:
attempt_stop_and_delay_policy_source:
concurrency_dispatcher_pool_buffer_bounds:
overflow_fairness_and_priority:
flow_or_callback_semantics:
shutdown_restart_and_terminal_state:
attempt_resource_effect_and_recovery_evidence:
conditional_provider_behavior:
invalidation_disable_and_retirement:
```

Review the policy when workload, client, provider, effect, version, dispatcher,
buffer, caller, lifecycle, gate, or incident evidence changes. Remove duplicate
retry layers and temporary limits when stronger ownership and capacity controls
replace them. Stable behavior remains bounded and diagnosable under pressure and
does not release a hidden wave of work after recovery.

## Observability Checklist

`observability_default`: Begin with a failure, compatibility, cancellation, or
route decision. Record the smallest access-safe evidence that distinguishes the
state, names its target and consumer, and leads an accountable owner to an
action. Percentiles, tool counts, traces, and persistent telemetry are not
mandatory categories.

**Evidence contract**

| field | requirement |
| --- | --- |
| decision_question | state what ambiguity the evidence must resolve and which action depends on it |
| target_identity | source revision, module, Kotlin and JVM versions, plugins, generated surface, artifact, and environment as relevant |
| state_or_event | define value, absence, failure, cancellation, attempt, consumer, artifact, migration, or final outcome being observed |
| source_and_owner | identify the component, gate, caller, provider, or person that knows the state and who maintains its semantics |
| bounded_dimensions | use controlled mode, operation, result, failure, version, consumer class, or work phase values needed for diagnosis |
| sensitive_boundary | exclude credentials, raw private payloads, customer data, unbounded exception text, and confidential source according to policy |
| temporal_semantics | define event versus collection time, scheduler or clock assumptions, ordering, and freshness where interpretation depends on them |
| logical_operation_semantics | distinguish original operation, retry attempt, child work, callback, flow element, final result, and reconciliation |
| evidence_path | identify source, compiler or test, collector or file, query or review, consumer, and action actually used |
| loss_and_inconclusive_state | define how empty selection, cache uncertainty, dropped events, stale report, detached work, or inaccessible consumers become visible |
| independent_confirmation | name a direct caller, artifact, resource, provider, or final-state source for consequential decisions |
| verification_scenario | inject or reproduce normal, failure, cancellation, incompatibility, evidence-loss, and resolution states as activated |
| retention_and_consumers | record access, retention, automation, reviews, runbooks, and downstream tools that depend on the evidence |
| invalidation_and_retirement | name version, schema, target, consumer, gate, or mechanism changes that force requalification or removal |

If no consumer or action exists, question whether persistent collection is
needed. A local assertion or compatibility report may be better than runtime
telemetry for a deterministic language contract.

**Evidence source selection**

| source | strongest_use | important_limit |
| --- | --- | --- |
| compiler diagnostic | source typing, exhaustiveness, visibility, overload, and configured warning state | only selected compiler, source set, plugins, and current consumers |
| static analysis | configured syntactic and data-flow rules such as target-approved null, coroutine, or style checks | baselines, suppressions, false positives, and no semantic runtime proof |
| deterministic test | parsing, invariant, state, equality, mapping, and controlled caller behavior | mocks and Kotlin-safe fakes can hide Java, generated, provider, or lifecycle state |
| Java caller fixture | generated JVM signature, nullability, names, defaults, overloads, exceptions, and generics | representative callers do not cover every external binary |
| coroutine or flow test | logical lifetime, cancellation, child failure, buffering, completion, and cleanup | virtual time and cooperative fakes do not prove real blocking or platform behavior |
| API or ABI report | selected public source and binary surface compared with baseline | baseline and tool configuration define coverage; behavior and wire state remain separate |
| serialization or contract report | selected wire shape, unknown states, malformed input, and old/new compatibility | does not prove all consumers or persistent historical data without representative fixtures |
| generated artifact inspection | plugin, proxy, serializer, annotation, and emitted JVM surface | source shape alone does not prove runtime framework behavior |
| structured runtime signal | repeated operation, error, resource, cancellation, and lifecycle state in an operated target | volume, privacy, dimensions, collection loss, and owner action must be qualified |
| thread, coroutine, or profile diagnostic | where blocking, suspended, allocated, locked, or active work exists during a reproduced state | sampling and overhead; not an outcome or compatibility contract alone |
| decision or handoff record | route, authority, alternatives, evidence, uncertainty, and next action | human consistency and stale ownership; no behavioral proof by itself |
| downstream or incident report | actual consumer and production impact for a recorded artifact and event | late, incomplete, confounded, and not universally predictive |

Use complementary sources only when they resolve different uncertainty. Three
views of the same unqualified test result are not independent evidence.

**Kotlin boundary checklist**

| boundary | observe | failure_or_negative_case | action_supported |
| --- | --- | --- | --- |
| route and mode | accepted outcome, lead mode, support questions, skipped regions, reroute cause | keyword activation or unresolved owner | continue, narrow, reroute, or stop |
| toolchain and artifact | wrapper, compiler, JVM target, plugins, generated sources, source sets, tests, artifact identity | local and CI drift, stale cache, wrong module, substituted artifact | repair build state or hold compatibility decision |
| raw and platform input | origin signature, annotation, parse result, absence meaning, boundary error | Java null, malformed or old input, conflicting annotation | contain uncertainty, reject, or revise state model |
| types and objects | construction, equality, copy, identity, unknown state, serialization, generated form | invalid value, wrong ID, unsafe copy, future state, framework proxy | preserve, adapt, migrate, or route to owner |
| errors and outcomes | expected state, infrastructure failure, cancellation, exception mapping, caller handling | generic catch, sentinel, lost cause, cancellation conversion | correct mapping or public contract |
| coroutine scope | parent, children, supervisor policy, active work, cancellation, completion, cleanup | cancel before and during work, child failure, detached launch | contain lifetime and verify final state |
| blocking and resources | actual thread or dispatcher, queue, pool, duration, timeout, resource release | slow or stuck call under constrained capacity | expose or isolate blocking and route capacity decisions |
| flow and callback | producer, collector, sharing, buffer, attempts, elements lost or replaced, callback registration and release | overflow, collector cancellation, producer failure, restart | select buffer policy, cleanup, or lifecycle owner |
| Java consumer | generated signatures, compile and runtime calls, nullability, overloads, exceptions, boxing | null, default, generic, overload, annotation, and artifact change | preserve facade or approve migration |
| public compatibility | current and candidate artifacts, baseline, consumer matrix, wire and unknown states | deliberate breaking mutation and old/new mismatch | hold, version, coexist, migrate, or retire |
| gate health | task and filter selection, expected cases, cache, artifact, negative control, async final state | empty selection, flaky environment, test finishes early | accept, fail, isolate, or classify inconclusive |
| backend handoff | language contract, framework or provider state, returned owner decision, integration evidence | local unit green with missing lifecycle | keep claim conditional or transfer lead |

**Privacy and bounded dimensions**

- Use controlled names for mode, boundary, result, failure class, version,
  consumer class, test phase, and evidence status.
- Do not place raw source, URLs with private paths, exception messages, user IDs,
  payloads, SQL, tokens, credentials, account values, or arbitrary strings into
  high-cardinality labels or generic workflow logs.
- Keep detailed diagnostics in an access-controlled target system with
  redaction, retention, and owner policy.
- Correlation identifiers must not encode private content and should have a
  target-defined lifetime.
- Test high-variety inputs where persistent signals exist; inspect series,
  index, file, buffer, and exporter growth.
- Exercise redaction on success, failure, cancellation, build errors, generated
  reports, and handoff summaries.

**Temporal and counting correctness**

- Separate logical operation, retry attempt, coroutine child, flow element,
  callback, and final consumer outcome.
- Record whether a timeout precedes effect, follows ambiguous effect, or simply
  reflects caller abandonment.
- Do not count request acceptance as asynchronous work completion.
- State virtual versus wall-clock time and scheduler behavior. Virtual delay is
  not runtime latency.
- Observe work after test completion or cancellation; a green assertion can
  precede detached failure.
- Preserve artifact and version boundaries in comparisons.
- State sampling, missing observations, external consumer delay, and stale
  report behavior.

**Evidence-system health**

Observe or otherwise detect:

- empty test or source selection;
- cache keys that omit source, version, plugin, generated, or fixture inputs;
- test retries and flaky result selection;
- background children or callbacks active after the test returns;
- generated reports from another artifact or baseline;
- compiler, linter, or API tool configuration drift;
- trace or signal sampling and propagation gaps;
- dashboard, report, or compatibility baseline freshness;
- missing downstream consumer and owner acknowledgment;
- discrepancy between summary evidence and direct caller, artifact, resource,
  or final state.

When the evidence path is degraded, classify the claim inconclusive. Use an
independent state source for high-consequence containment and do not declare
recovery from silence.

**Qualification protocol**

1. State the failure question and action owner.
2. Freeze target revision, artifact, versions, consumer, and environment.
3. Produce a safe known normal or failure state using non-sensitive data.
4. Observe source, gate selection, output, evidence storage, reviewer or alert,
   and owner action.
5. Confirm dimensions, attempts, timestamps, cancellation, artifact, redaction,
   and correlation agree with direct state.
6. Inject evidence loss or an empty/no-op path and verify it becomes
   inconclusive rather than green.
7. Correct or recover the target state and confirm observations resolve,
   children and resources end, and temporary controls retire.
8. Retain concise locators, result, limits, and invalidation event.

**Agent-workflow evidence**

- Record complete local source regions read and intentionally skipped regions
  with their widening triggers.
- Record target files, symbols, consumers, build roots, versions, and ownership
  that established applicability.
- Record exact focused and wider commands or review methods, selection, exit
  status, result summary, and stronger claim not proved.
- Record changed paths, ownership, checkpoints, unresolved risks, conditional
  environments, and next actions.
- Prefer concise summaries and locators over raw command transcripts or
  complete conversation dumps.
- Do not use tool-call, file-count, or context size as quality without a
  decision-yield and boundary-safety guardrail.

**Examples**

Good platform evidence: a Java-origin fixture records resolved dependency and
signature, injects null and non-null returns, observes adapter classification
and downstream invariant, and keeps raw values out of logs. The evidence leads
to containment at one boundary.

Bad workflow evidence: a journal records many files and commands but omits the
target symbol, selected tests, public consumers, and result. Volume cannot
reconstruct the decision.

Good cancellation evidence: a controlled scenario correlates parent, child,
attempt, resource, and effect identity; cancels at a consequential phase; and
observes termination plus cleanup after the test assertion. Cancellation
remains distinguishable from ordinary failure.

Conditional compatibility evidence: local Kotlin and Java callers plus the
configured API baseline pass, but external public consumers are unknown.
Internal evidence passes; publication authority remains conditional.

Temporary diagnostic: a protected coroutine diagnostic is enabled for a
reproduced leak with bounded duration and access. It contains no private
payload, records overhead, and has a removal event after the causal gate exists.

**Evidence inventory record**

```text
evidence_id_and_schema_version:
decision_question_and_action:
target_revision_artifact_versions:
source_component_gate_and_owner:
state_event_and_population:
bounded_dimensions_and_sensitive_boundary:
time_attempt_async_and_final_state_semantics:
evidence_path_consumers_and_access:
loss_inconclusive_and_independent_state:
qualification_scenario_and_result:
retention_cost_and_compatibility:
stronger_claim_not_proved:
invalidation_and_retirement:
```

Treat durable evidence schemas as operational APIs. Inventory consumers,
version material semantic changes, requalify automation and reviews, and remove
records or signals with no decision consumer after confirming no hidden
compatibility, audit, or incident dependency remains.

## Performance Verification Method

The seed's one-session target and universal percentile packet have no target
objective, baseline, workload, artifact, environment, or measurement evidence.
They are not retained as defaults.

`performance_verification_default`: Define one bounded performance hypothesis,
preserve functional and compatibility invariants, use a representative target
artifact and workload, qualify the harness, compare like conditions, identify
the first limiting mechanism, and observe final state after pressure.

If no target-owned objective exists, characterize behavior or compare a
candidate with a baseline. Do not claim objective compliance.

**Performance claim types**

| claim | outcome_to_define | material_inputs | hard_guardrails |
| --- | --- | --- | --- |
| pure algorithm or parser | operation cost across specified input distribution and size | input shape, validation, collections, compiler, runtime, allocations | correctness, malformed and boundary behavior, no changed invariant |
| value and object representation | allocation, boxing, equality, copying, serialization, or memory behavior | value class or primitive use sites, generics, nullability, reflection, Java and serializer mode | semantic equality, Java and wire compatibility, no invalid construction |
| coroutine operation | end-to-end, wait, service, dependency, cancellation, and cleanup behavior | dispatcher, scope, concurrency, client, blocking, timeout, retries, workload | structured ownership, bounded attempts, no lost cancellation or effects |
| flow processing | element or state processing, lag, buffer, backpressure, completion, and resource behavior | cold or shared mode, producer, collectors, buffer, overflow, transformations, workload | event or state semantics, no hidden loss, cleanup, and final state |
| Java interop | adapter and caller cost plus generated representation where performance matters | Java version, signatures, boxing, annotations, overloads, reflection, calls | source, binary, exception, and nullability contract preserved |
| serialization or generation | encode, decode, generated build, startup, or artifact impact | plugin, schema, payload distribution, unknown fields, historical data, compiler | wire compatibility, malformed handling, artifact identity, no data loss |
| build feedback | clean and incremental compile, test, static, generation, or package duration | wrapper, daemon, cache, modules, source sets, plugins, hardware, runner | same checks, sources, artifacts, and cache correctness |
| packaged JVM behavior | startup, class loading, readiness, resource, request, or shutdown outcome | artifact, JVM, architecture, config, topology, dependencies, warm state | correct startup, traffic or work state, cancellation, resources, recovery |
| compatibility migration | consumer build and test burden across old and new artifacts | consumer matrix, baselines, deprecation, facades, release order | all supported intermediate states and rollback or roll-forward remain valid |
| entrypoint workflow | time and work needed to reach the correct route, design, gate, or stop | task class, target access, source state, interruptions, reviewer experience | route correctness, consumer coverage, evidence fidelity, rework, and handoff quality |

Do not combine these into one score. A faster adapter can allocate more, lose
cancellation, or break Java callers. A faster workflow can omit a public
consumer or real-boundary gate.

**Method selection**

| method | strongest_use | controls_needed | cannot_prove_alone |
| --- | --- | --- | --- |
| deterministic timing or complexity test | algorithmic regression or explicit timeout logic under controlled inputs | stable or virtual clock where semantically valid, input distribution, correctness | JVM throughput, JIT, real dependency, platform, or production behavior |
| target-configured microbenchmark | comparative hot-path operation, allocation, or representation cost | repository benchmark harness, warmup, dead-code resistance, forks or repetitions, stable environment | end-to-end caller, dependency, compatibility, or recovery outcome |
| profiler or allocation diagnostic | locating CPU, allocation, lock, thread, blocking, or garbage-collection mechanism | representative workload, bounded overhead, artifact and warm state | user outcome or objective compliance without separate measurement |
| component concurrency test | coroutine, flow, dispatcher, buffer, or adapter behavior under controlled pressure | actual implementation, scheduler, blocking fake or real adapter, resource observation | managed platform, full downstream system, and production distribution |
| Java or serialization harness | generated JVM or wire cost and compatibility for representative consumers | actual versions, signatures, payloads, artifacts, warm state | all external consumers and future schema evolution |
| clean and incremental build study | compiler, plugin, source-set, test, and generation feedback cost | identical checks, daemon and cache state, runner, modules, artifacts, repetitions | runtime performance or developer outcome beyond measured cohort |
| packaged-process measurement | startup, JVM, resources, config, and local lifecycle | intended artifact, JVM, architecture, resources, dependencies, cold or warm state | managed identity, traffic, autoscaling, provider, and production topology |
| synthetic workload or stress | controlled mix, concurrency, payload, failure, and first limiting resource | qualified generator and collector, representative model, stop conditions | unmodeled production traffic or owner objective |
| staged target observation | scoped real platform, consumer, dependency, artifact, and lifecycle behavior | owner, baseline, immutable artifact, stop and recovery conditions | universal future behavior |
| workflow task fixture | route and decision quality under controlled requests | representative task classes, hidden boundaries, reviewer rubric, source access | all repositories, agents, teams, and real migration complexity |

Use the least costly method that can falsify the claim. Profiling explains an
observed difference; it does not replace outcome measurement.

**Preconditions**

1. State the target-owned objective or a comparative hypothesis. If neither
   exists, explain what characterization will decide.
2. Freeze correctness, cancellation, security, data, public compatibility, and
   artifact invariants. Performance cannot silently trade them away.
3. Record revision, wrapper, Kotlin and Java versions, compiler and plugins,
   dependency set, artifact, JVM, architecture, configuration, and resources.
4. Define inputs and workload: operation mix, sizes, distributions, malformed
   cases, concurrency, payloads, consumers, dependencies, warm state, and
   failure or lifecycle phases.
5. Define the measured boundary: queue wait, execution, dependency,
   serialization, compile, end to end, acceptance, or final completion.
6. Establish a comparable baseline when making improvement or regression claims.
7. Qualify generator, collector, benchmark harness, clock, caches, daemon,
   fixture cleanup, and final-state assertions.
8. Define stop conditions for resource, external system, data, cost, and
   environment harm.

**Kotlin and JVM controls**

- Separate cold startup, early warmup, and steady warmed execution. Class
  loading, JIT compilation, caches, reflection, serializers, and connections
  can dominate different phases.
- Record JVM options and container or runner resources when they can affect
  memory, garbage collection, threads, CPU, and diagnostics.
- Observe allocation and garbage collection when comparing value classes, data
  representations, collection pipelines, or serialization. Value classes can
  box in generic, nullable, interface, reflection, or Java contexts.
- Distinguish coroutine suspension from blocking. A suspend signature can call
  JDBC, filesystem, native, DNS, or legacy Java work.
- Record dispatcher, executor, thread, connection, semaphore, buffer, and worker
  limits that shape queueing and throughput.
- Do not use virtual-time coroutine tests as wall-clock performance evidence.
- Include compiler plugins, generated code, proxying, reflection, serialization,
  and mixed Java/Kotlin paths used by the target artifact.
- For incremental build claims, record changed files, daemon and cache state,
  invalidated tasks, generated inputs, and whether the output artifact is
  equivalent.

**Execution protocol**

1. Run a smoke and negative control to confirm the intended code path and
   evidence distinction.
2. Establish cold or warm state explicitly. Reset or record caches, JIT state,
   daemons, generated output, data, connections, and buffers as needed.
3. Run baseline and candidate with comparable target, artifact, resources,
   inputs, dependencies, and measurement overhead.
4. Alternate or randomize order when environment drift can bias one side.
5. Use enough observations and repetitions for the claimed statistic. Do not
   report tail percentiles from a population too small or censored to support
   them.
6. Observe accepted and completed work, errors, cancellation, attempts, queue
   wait, execution, dependencies, allocation, resources, and final state.
7. Increase pressure only in an isolated or owner-approved environment and
   identify the first limiting mechanism.
8. Remove pressure or restore dependencies. Observe buffers, children, retries,
   resources, latency, build state, and accepted outcomes until recovery or an
   explicit residual state.
9. Mark a run inconclusive when harness saturation, collector loss, wrong
   artifact, stale generated code, noisy runner, or incomparable cache state
   prevents interpretation.
10. Reproduce material differences before claiming improvement, unless one run
    reveals a deterministic hard failure that already blocks adoption.

**Interpretation rules**

- Use a statistic appropriate to the decision. Median, tail, maximum, mean,
  throughput, allocation, compile duration, and reviewer time answer different
  questions.
- Report population, count, inclusion, missing results, retries, canceled work,
  and asynchronous completion semantics.
- Preserve enough bounded raw or distribution evidence for review without
  retaining private payloads.
- Compare an authoritative target objective and baseline change separately.
  Passing one does not imply the other.
- Report run-to-run variation and uncertainty; avoid decimal precision beyond
  measurement quality.
- Segment incompatible operations, input sizes, consumers, artifacts, warm
  states, and dependency modes.
- Treat timeouts and abandoned calls carefully because censored slow work can
  make remaining results look faster.
- Count original operations and attempts separately.
- Record profiling and detailed-observability overhead when it changes results.

No universal percentile names are required. When a target uses a percentile,
record its population, window, estimator, sample sufficiency, missing-data rule,
and owner threshold.

**Guardrails**

A performance improvement fails if it:

- changes accepted values, state, ordering, equality, validation, error, or
  cancellation behavior;
- loses or duplicates effects beyond the accepted contract;
- breaks Kotlin, Java, binary, wire, generated, reflection, framework, or
  historical consumers;
- hides errors or disables evidence needed for diagnosis;
- shifts latency into buffers, retries, detached work, callers, or recovery;
- depends on a different artifact, compiler, plugin, fixture, check set, or
  weaker test;
- consumes resources or cost beyond target policy;
- harms fairness or starves a population hidden by aggregate throughput.

**Examples**

Parser comparison: compare a new typed parser with the baseline across target-
derived valid, absent, malformed, boundary, and representative-size inputs.
Assert identical or deliberately revised semantics, observe allocation only if
it matters, and report characterization if no target objective exists.

Value-class comparison: inspect actual call sites where a wrapper may box,
including generics, nullable use, interface calls, Java, reflection, and
serialization. A microbenchmark of one unboxed local call cannot justify a
public representation decision.

Coroutine comparison: measure end-to-end and queueing under representative
concurrency while observing cancellation, blocking, attempts, dispatcher
capacity, resources, and final effects. Faster completion with swallowed
cancellation fails.

Build regression: compare clean and incremental builds under the same wrapper,
compiler, plugins, checks, modules, runner, daemon, and cache policy. Confirm
both produce the intended equivalent artifact. One warm incremental command is
not a general developer-feedback objective.

Workflow comparison: representative tasks use old and evolved routing. Measure
time to an interpretable decision only alongside wrong routes, source omissions,
rework, consumer escapes, and reviewer agreement. Fewer files or one session is
not automatically better.

Conditional package result: local JVM startup and resource behavior improve,
but target platform identity, traffic, and lifecycle are inaccessible. Report
the packaged local improvement and leave deployment performance conditional.

**Result classes**

| result | meaning |
| --- | --- |
| objective_pass | qualified target population meets an authoritative objective and all hard guardrails at the tested envelope |
| comparative_improvement | candidate reproducibly improves against comparable baseline while preserving guardrails; objective status may remain unknown |
| characterization | behavior, variability, limiting resource, and recovery are observed without a pass threshold |
| failure | objective or hard guardrail is violated with interpretable evidence |
| conditional | narrower environment or consumer evidence passes while material target scope remains unavailable |
| inconclusive | harness, artifact, environment, data, dependency, cache, or variability prevents the claimed interpretation |

**Performance record**

```text
claim_id_owner_and_objective_or_hypothesis:
population_and_measurement_boundary:
baseline_and_candidate_artifacts:
kotlin_java_compiler_plugins_jvm_architecture:
config_resources_and_environment:
input_workload_consumer_and_dependency_profile:
cold_warm_cache_daemon_and_generated_state:
method_generator_collector_and_negative_control:
trial_order_repetitions_and_variability:
time_throughput_allocation_resource_or_build_results:
errors_attempts_cancellation_and_final_state:
first_limiting_mechanism:
correctness_compatibility_fairness_cost_guardrails:
post_pressure_or_post_build_recovery:
confounders_missing_data_and_uncertainty:
result_classification_and_invalidation:
```

Requalify when target inputs, Kotlin or Java version, compiler, plugin, JVM,
artifact, consumer, dispatcher, dependency, resource, cache, workload, gate, or
objective changes materially. Retire benchmarks that no longer represent a
supported path or drive a decision.

Sustainable performance preserves meaning and diagnosis at the boundary,
fails or degrades visibly outside the tested envelope, and returns children,
buffers, resources, artifacts, and consumer state to an accepted condition.

## Scale Boundary Statement

`scale_boundary_default`: This reference is sufficient as the lead when one
accepted Kotlin language outcome has discoverable target state, bounded changed
transitions, known consumers, one integration owner, feasible evidence, and a
safe completion or migration path. It remains useful in support mode when
another route owns the broader outcome.

No universal system, owner, source, file, endpoint, traffic, or task count
defines this boundary.

**Scale dimensions**

| dimension | language_entrypoint_can_lead_when | compose_split_or_transfer_when | invariant_to_preserve |
| --- | --- | --- | --- |
| accepted outcome | value, API, caller, coroutine, or test outcome forms one coherent contract | several outcomes can fail or recover independently under different authorities | user and consumer states plus one integration owner |
| repositories and modules | changed dependency path and consumers are discoverable and share compatible release policy | independent repositories or modules publish and migrate on separate schedules | versioned interface, artifact identity, and consumer compatibility |
| language targets | one Kotlin/JVM stance and compiler mode governs behavior | JVM, multiplatform, native, Java-only, or several compiler and plugin modes differ materially | source intent, generated form, platform behavior, and support matrix |
| public artifacts | one private or coherently versioned artifact contains change | libraries, plugins, services, and clients publish independently or coexist | source, binary, wire, generated, and deprecation contract |
| state ownership | types and outcomes are owned by one domain or adapter | protocol, persistence, external provider, or data owner controls state evolution | unknown states, mapping, migration, and final business meaning |
| execution ownership | caller or one lifecycle scope owns coroutine and resources | callbacks, hot flows, workers, processes, queues, and platforms have separate lifetime | cancellation, effect, cleanup, shutdown, and recovery contract |
| consumers | supported Kotlin and Java callers are known and update coherently | external, binary, serialized, reflective, generated, framework, or historical consumers need separate evidence | compatibility and safe intermediate states |
| build and generation | one wrapper, toolchain, plugin set, and artifact path is authoritative | composite builds, custom source sets, generated systems, shared baselines, or artifact platforms have independent owners | effective versions, task selection, generated surface, and immutable artifact |
| framework and backend | framework is incidental or the language question is isolated behind an interface | Spring, Ktor, persistence, auth, migration, runtime, package, traffic, or recovery decides success | Kotlin contract plus backend lifecycle integration |
| security and data | no separate trust, regulated data, persistent mutation, or external effect boundary changes | authorization, secrets, audit, schema, historical data, or irreversible effects activate specialist authority | least authority, data invariants, audit, and recovery |
| verification | one target environment and gate set represents all consequential states | consumers, providers, frameworks, artifacts, or platforms require distinct fixtures and owners | requirement traceability and honest conditional scope |
| context | target and source evidence fit a ranked route without displacing counterexamples | discovery remains unbounded or one boundary crowds out another's evidence | persisted locator map, omissions, and decision record |
| authority | one reachable owner can accept the language outcome and integration | risk or migration decisions are fragmented or no owner can accept the combined state | explicit decision interfaces, escalation, and final acceptance |

One repository can still require Java, serialization, data, framework, and
artifact owners. Several repositories can remain one bounded change if a stable
interface, release policy, and integration owner genuinely unify them.

**Sufficiency test**

Keep this reference as lead only when all are true:

- the requested action, accepted states, and strongest consequence are clear;
- applicable instructions, build, versions, plugins, generated mechanisms,
  callers, consumers, and existing gates can be discovered;
- Kotlin language semantics own the principal design decision;
- every changed value, state, caller, lifetime, compatibility, and artifact
  transition has one owner;
- preservation and feasible alternatives fit one decision record;
- focused and affected consumer evidence can be assigned without contradictory
  target assumptions;
- public or persistent migration has safe intermediate states or an accepted
  coordinated transition;
- source and target context can be narrowed enough to preserve counterexamples,
  uncertainty, and actual evidence.

When a condition fails, this reference can remain language support while a
backend, framework, data, security, artifact, platform, migration, or incident
route leads.

**Scale route modes**

| route_mode | choose_when | coordination | completion |
| --- | --- | --- | --- |
| direct_language | one private or bounded language contract and local consumers dominate | one owner and focused modes | activated behavior and regression gates pass |
| composed_language | nullability, type, coroutine, interop, and testing interfaces share one API outcome | one lead mode, bounded support returns, one activation contract | each interface and integrated consumer scenario pass |
| compatibility_program | public source, binary, Java, wire, or generated consumers migrate across versions | artifact and consumer owners, coexistence, versioning, staged retirement | every supported combination and intermediate state is usable |
| backend_integration | Kotlin contract serves a service, framework, data, security, runtime, or worker outcome | backend route leads and language owner returns a tested interface | backend lifecycle, package, and recovery evidence integrate language result |
| parallel_independent | workstreams edit disjoint artifacts behind stable contracts | exclusive writes, frozen interfaces, frequent integration, one verifier per invariant | local, interface, and final artifact gates pass |
| sequential_shared_decision | several tasks depend on one evolving public type, schema, scope, or compatibility baseline | one owner resolves shared contract before dependent work | shared state accepted and versioned before parallelism resumes |
| exploratory_narrowing | target consumers, generated behavior, or authority are incomplete | ranked hypotheses, dependency tracing, reversible probes, and stop condition | one bounded route or precise owner handoff is reached |
| platform_or_provider_transfer | runtime capacity, cancellation, artifact, traffic, effect, or external contract is owned elsewhere | target authority plus language interface | provider or platform evidence and integrated target scenario pass |
| incident_support | active harm spans artifacts, consumers, or services | incident command owns common state and containment | accepted system state and residual owner closure |
| stop_and_reframe | no accepted outcome, owner, safe intermediate state, or faithful gate exists | preserve evidence and resolve the missing decision | bounded objective and accountable route are accepted |

**Split protocol**

1. Map the whole outcome from raw input through Kotlin type, callers, coroutine
   or flow lifetime, generated artifact, consumers, backend state, and recovery.
2. Identify transitions that can fail or recover independently and the owner of
   each decision.
3. Define safe intermediate states. If no state allows independent progress,
   use a coordinated migration or maintenance transition.
4. Split by decision and artifact, not arbitrary theme or file count.
5. Freeze interfaces: value and state shape, nullability, errors, cancellation,
   Java surface, wire form, version, artifact, and returned evidence.
6. Assign one integration owner and one source of truth for shared decisions.
7. Select local and interface gates before implementation, including one
   boundary failure per interface.
8. Integrate early enough to expose target and assumption drift.
9. Exercise coexistence, old and new artifacts, failure, stop, and recovery as
   applicable.
10. Retire temporary facades, adapters, dual representations, suppressions,
    compatibility gates, and coordination structures after exit evidence.

**Interface contract**

Every split activated by language work should specify:

- producer and consumer artifacts plus supported versions;
- Kotlin and Java source signatures, generated JVM form, nullability,
  exceptions, generics, defaults, and annotations;
- wire or persistent schema, unknown states, historical values, and mapping;
- coroutine scope, cancellation, dispatcher, blocking, effects, and cleanup;
- framework, reflection, proxy, serialization, and plugin assumptions;
- build, generated inputs, task selection, baselines, publication, and promotion;
- local, interface, compatibility, and backend integration gates;
- stop, defer, rollback, roll-forward, reconciliation, and retirement authority.

**Distributed agent and shared-workspace controls**

- Assign exclusive ownership per reference, packet, module, public API, baseline,
  or decision record.
- Do not allow parallel workers to choose the same state model or migration
  independently.
- Save each complete atomic unit immediately and run its local gate before
  beginning another.
- Persist counts, paths, results, blockers, and nonempty next steps at required
  cadence.
- Freeze shared inputs and recheck hashes or revisions before final integration.
- Preserve unrelated user and collaborator changes; do not revert or broadly
  reformat another workstream.
- Reconcile changed interfaces with every dependent owner before claiming
  completion.
- Keep destructive commands, baseline changes, commits, pushes, releases, and
  production actions within explicit authority.
- Resume from durable state after interruption and reread governing constraints
  before editing.

Parallelism is unsafe when two agents edit one public signature, state
hierarchy, serialized form, coroutine ownership boundary, compatibility
baseline, or requirement. Run that decision sequentially through one owner.

**Large-codebase narrowing**

1. Find applicable instructions, build roots, modules, wrappers, source sets,
   compiler and plugin configuration, publication, and generated outputs.
2. Identify the edited API or execution entry point.
3. Trace direct callers, Java consumers, serializers, frameworks, coroutine
   scopes, tests, and artifacts before broad architecture reading.
4. Rank input boundary, implementation, failure path, consumers, gates, and
   owner policy by decision relevance.
5. Persist a locator and dependency map. Expand only when a discovered edge
   changes consequence, authority, or compatibility.
6. Use repository-native graph tooling when available and qualified; use focused
   text and build search for non-code state.

A source list without ranked relevance, consumer reachability, and owner state
is not scale evidence.

**Examples**

Coherent large repository: a monorepo contains many services, but one internal
Kotlin module changes a parser with local callers and configured property plus
regression tests. Dependency narrowing keeps one language route sufficient.

Small but scaled API: one declaration in a published library changes nullability
and a sealed result used by Java and serialized consumers. The work requires a
compatibility program despite one file and one team.

Safe split: language owner defines an internal explicit state; Java owner
preserves facade and callers; artifact owner manages version and baseline; one
integration owner controls coexistence and retirement. Interface and old/new
artifact tests run throughout.

Unsafe parallel split: one worker adds a sealed state while another changes
exception mapping and Java overloads without a frozen consumer contract. Both
pass local Kotlin tests but publish incompatible meanings.

Backend support: a queue worker's type and cancellation design is bounded in
the language route. Backend owners lead acknowledgment, transaction, retry,
shutdown, restart, and effect reconciliation. Phase-interruption evidence joins
both.

Conditional public scope: repository search finds no external Java caller, but
the artifact is public and release ownership is unavailable. Internal
implementation can be reviewed; a breaking public change remains conditional.

**Scale record**

```text
accepted_outcome_and_consequence:
repositories_modules_targets_and_artifacts:
kotlin_java_wire_and_generated_consumers:
state_owners_and_compatibility:
coroutine_flow_blocking_and_backend_lifecycle:
build_release_and_platform_authority:
security_data_and_irreversible_effects:
context_dependency_and_source_map:
sufficiency_result:
route_modes_and_split_decisions:
frozen_interface_contracts:
local_interface_and_integration_gates:
safe_intermediate_states:
integration_owner_and_escalation:
conditional_boundaries:
temporary_coordination_and_retirement:
```

Review scale decisions from route loops, merge conflicts, stale interfaces,
late consumer discovery, incompatible artifacts, integration defects, and
incidents. Promote recurring independently evolving boundaries into dedicated
gates, artifacts, or references only when their maintenance benefit exceeds
the added discovery and coordination cost.

Healthy scaling preserves one accountable consumer outcome while allowing
specialists to own truly independent decisions. It does not pretend one
language checklist can understand or operate every surrounding system.

## Future Refresh Search Queries

`future_research_only_note`: No query in this section was executed during this
evolution. No current page, release, default, compatibility, advisory,
repository state, or search result is asserted.

Future public research must be explicitly authorized. Do not place private
service names, customer or tenant details, internal URLs, credentials, raw
incident payloads, account identifiers, private source, or unreleased security
information in a public query.

**Target preflight before query construction**

| fact_to_resolve | target_source | why_it_changes_the_query |
| --- | --- | --- |
| Kotlin language and compiler version | wrapper, plugins, dependency resolution, and compiler settings | selects applicable language rules, flags, releases, and compatibility guidance |
| Java and JVM target | toolchain, bytecode target, packaged runtime, and supported consumers | changes interop, generated form, libraries, and runtime behavior |
| platform and compiler mode | JVM, multiplatform, native, frontend, experimental or opt-in configuration | prevents another target or compiler mode from answering the question |
| coroutine library version | resolved dependency and lock state | scopes API, cancellation, flow, dispatcher, and release behavior |
| compiler and code-generation plugins | target build and generated sources | scopes serialization, no-arg, proxy, reflection, and generated signature behavior |
| framework and execution mode | target dependencies, engine, web style, plugins, and lifecycle | distinguishes language questions from Spring or Ktor ownership |
| public and generated consumers | source, Java, binary, wire, reflection, framework, and downstream artifacts | determines which compatibility authority and scenarios matter |
| exact symbol or mechanism | target code, compiler output, error, and call path | prevents theme-level browsing from replacing a bounded claim |
| consequence and owner | requirement, failure, migration, and policy | determines evidence depth and when research may stop |

If these facts cannot be resolved, return to target discovery. For greenfield
selection, list candidate coordinates separately and label the work option
research rather than installed-state evidence.

**Future query construction catalog**

The `construction` column describes how to build the future query from resolved
target facts. It intentionally contains no fill-in token that could be mistaken
for an already executable target query.

| query_family | use_when | construction | preferred_source | stop_or_reject |
| --- | --- | --- | --- | --- |
| official_language_rule | syntax, type, visibility, sealed, value, scope-function, or convention semantics are version-sensitive | combine `site:kotlinlang.org`, the resolved Kotlin version, exact feature name, target platform, and bounded behavior phrase | official version-applicable Kotlin documentation or API | result is overview-only, wrong platform, latest-only, or target execution remains the real uncertainty |
| language_release_change | current and candidate compiler versions have an explicit behavior or compatibility question | combine official Kotlin domain, both version identifiers, feature or diagnostic, and `release notes` or `compatibility` | official release, compatibility, migration, or issue material | source does not cover the selected compiler mode or plugin interaction |
| Java_interop_contract | names, nullability, defaults, overloads, generics, exceptions, annotations, or JVM representation are uncertain | combine official Kotlin domain, `Java interop`, exact mechanism, target Java version, and generated-surface concern | official Kotlin interop documentation plus applicable Java or library authority | query is used instead of compiling representative Java callers |
| platform_nullability | Java annotation, platform type, enhancement, or generated nullability semantics decide safety | combine official Kotlin domain, exact annotation or library mechanism, resolved versions, and `nullability` | owning Kotlin and library documentation | result cannot establish provider behavior or target-generated signature |
| coroutine_api_semantics | cancellation, exceptions, scope, flow, dispatcher, timeout, or sharing semantics are unresolved | combine official Kotlin or coroutine authority, resolved coroutine version, exact API, execution mode, and failure phrase | official coroutine docs or API at applicable release | generic coroutine tutorial or target blocking behavior remains unknown |
| coroutine_release_change | behavior differs or may differ between resolved releases | combine official coroutine repository, exact old and new versions, symbol, and `release notes` or `changelog` | maintainer release, tag, source, issue, or test at the released version | default branch replaces release evidence or implementation is mistaken for contract |
| compiler_plugin_behavior | serialization, proxy, no-arg, all-open, compiler, or generated code changes target surface | combine owning maintainer domain, resolved Kotlin and plugin versions, plugin name, generated mechanism, and compatibility phrase | official plugin documentation and release material | target generated output and clean build are not inspected |
| Gradle_Kotlin_integration | Kotlin plugin, toolchain, task, source set, or incremental build behavior is uncertain | combine official Gradle and Kotlin authorities, wrapper version, plugin version, task or feature, and exact failure | official build-tool and plugin documentation | global tool or unrelated build version is returned |
| Maven_Kotlin_integration | Maven plugin, lifecycle, source order, compiler, or generated code is uncertain | combine official Kotlin and Maven plugin authority, resolved plugin and Maven versions, lifecycle, and failure | official plugin and build documentation | query substitutes for target effective model and wrapper execution |
| API_or_binary_compatibility | public Kotlin or Java artifact evolution requires tool or policy authority | combine official Kotlin or target-approved tool domain, exact versions, artifact type, changed surface, and compatibility concern | official compatibility guidance and target-approved tool docs | result is used without baseline, artifact, supported consumer, or release policy |
| Spring_Kotlin_integration | target-confirmed Spring behavior depends on Kotlin classes, proxies, nullability, serialization, or coroutines | combine `site:docs.spring.io`, resolved Spring version, Kotlin, exact mechanism, and target web or data mode | versioned Spring reference owning the mechanism | tutorial or sample is treated as support policy or target proof |
| Ktor_Kotlin_integration | target-confirmed Ktor engine, plugin, route, client, or lifecycle behavior is uncertain | combine `site:ktor.io`, resolved Ktor version, engine or client mode, exact plugin, and behavior phrase | version-applicable Ktor documentation or API | welcome content omits version, engine, plugin order, or target evidence |
| serialization_evolution | wire shape, default, unknown field or state, value class, sealed type, or generated serializer changes | combine owning serializer authority, resolved versions, exact Kotlin construct, schema behavior, and compatibility phrase | official serializer documentation, release, and migration guidance | source is used without old and new target contract tests |
| maintainer_advisory | exact component and version have a security or support-status question | combine verified maintainer advisory domain, public component coordinate, version, and advisory term | maintainer advisory or target-approved vulnerability source | query would expose private vulnerability context or decide risk acceptance |
| official_source_test | applicable docs are ambiguous and released source implementation matters | combine official repository, released tag, exact symbol, behavior, and `test` | maintainer source or tests at the released revision | source detail is promoted to public promise or a fork outranks maintainer source |
| official_example_discovery | primary semantics are known and a target-confirmed framework needs orientation | combine official organization, resolved version, framework, Kotlin, sample, and exact mechanism | official example or guide used for vocabulary | sample becomes architecture, security, compatibility, or production evidence |

**Safe generic discovery phrases**

These phrases are future vocabulary searches only and contain no result claim:

```text
site:kotlinlang.org Kotlin Java interop nullability annotations
site:kotlinlang.org Kotlin cancellation exception handling coroutines
site:kotlinlang.org Kotlin sealed classes Java interoperability
site:github.com/Kotlin kotlinx.coroutines release notes cancellation
site:docs.spring.io Kotlin proxy final classes coroutines
site:ktor.io Kotlin engine plugins shutdown
```

Do not run them unchanged for an adoption decision. Add resolved target version,
mode, and exact consequence first. Prefer direct navigation when the owning
manual or release page is already known.

**Future research protocol**

1. State one target decision and one currentness-dependent uncertainty.
2. Record target revision, artifact, effective coordinates, platform, execution
   mode, consumers, and owner policy.
3. Select the authority that owns the behavior. Distinguish language,
   coroutine, build, plugin, framework, serializer, consumer, and provider
   layers.
4. Sanitize the query and record sensitive context deliberately excluded.
5. Use the narrowest direct lookup or query. Record exact text, retrieval time,
   selected result, version selector, and rejected near-matches.
6. Open and read the complete relevant region. Ignore result snippets and
   generated summaries as evidence.
7. Extract one bounded fact with prerequisites, defaults, experimental status,
   exceptions, deprecations, platform, and version.
8. Compare it with effective target mechanism and policy. Preserve conflicts.
9. Design and run the target gate capable of disproving the practical
   consequence.
10. Update only dependent route, design, test, compatibility, and handoff
    records. Keep stronger claims conditional.

**Result rejection rules**

Reject or downgrade a source when it:

- silently uses latest while the target uses another release;
- covers another platform, frontend, JVM target, framework, engine, plugin,
  source set, product edition, or execution mode;
- is a tutorial, sample, forum, search snippet, generated summary, fork, or
  default-branch source used as normative compatibility evidence;
- omits opt-in, experimental, prerequisite, exception, deprecation, migration,
  failure, or recovery information that changes the decision;
- is official for the wrong ownership layer;
- redirects, is archived, or lacks a verifiable maintainer and version;
- conflicts with target policy, generated artifacts, callers, or observed
  behavior and the conflict is unresolved;
- cannot be connected to a target scenario and still claims operational effect.

Official provenance does not guarantee target applicability. Several secondary
pages repeating one claim do not create independent evidence.

**Future research ledger**

```text
research_id_and_decision:
target_revision_artifact_and_coordinates:
platform_mode_consumers_and_consequence:
authority_and_query_or_direct_lookup:
sensitive_context_excluded:
retrieved_at_and_version_selector:
selected_source_and_complete_region:
source_role_and_bounded_fact:
prerequisites_defaults_exceptions_deprecations:
rejected_results_and_conflicts:
target_mechanism_and_owner_policy:
target_gate_and_observed_result:
stronger_claim_not_supported:
dependent_artifacts_and_consumers_updated:
refresh_supersession_or_retirement_event:
```

Stop research when the bounded mechanism is sufficiently supported for the
accepted risk, when target execution or owner policy is the remaining
uncertainty, or when available authority cannot resolve conflict. Preserve a
conditional decision rather than widening queries indefinitely.

Curate only searches that repeatedly reach the right authority and change a
decision. Revise constructions that return wrong versions or ownership layers.
Retire them when the component, terminology, mechanism, or supported consumer
no longer exists. Selective refresh should make future research smaller, not
create a permanent broad browsing ritual.

## Evidence Boundary Notes

Evidence status belongs to an individual claim, not to a document, paragraph, or source name. A path can prove what a frozen local file says without proving that the guidance fits a later target. A public URL can identify a future research route without proving what the page says today. A successful command can establish an observed result for one checkout and environment without establishing a universal Kotlin rule. Use the narrowest truthful label and retain enough coordinates for another agent to reproduce or challenge the claim.

**Claim-level evidence taxonomy**

| Label | Use it when | Minimum supporting record | It does not establish |
|---|---|---|---|
| `local_corpus_sourced_fact` | A statement is directly entailed by a frozen local source read during this evolution. | Repository path, snapshot hash, and the exact region or named rule used. | Current public behavior or applicability to an uninspected target. |
| `local_corpus_hierarchy_note` | A statement explains ownership or routing among the skill and its companion references. | All relevant local owners and the precedence or delegation relation between them. | That a delegated technology currently behaves as expected. |
| `external_mapping_unrefreshed_note` | A domain or URL is retained only as a future discovery route. | Inherited coordinate, intended research question, and explicit no-retrieval status. | Page contents, current version, maintenance status, defaults, or compatibility. |
| `refreshed_external_fact` | A public source was actually retrieved and directly supports a time-sensitive claim. | Exact URL, retrieval date, product or library version, bounded excerpt location, and applicability. | Target configuration or behavior that was not inspected or executed. |
| `target_instruction_fact` | A target repository instruction governs how work must be performed there. | Instruction path, applicable directory scope, revision, and any higher-priority constraint. | Runtime behavior or public language semantics. |
| `target_policy_fact` | A target configuration declares an enforced project choice. | Configuration path, relevant key or task, effective scope, and resolution evidence where needed. | That every execution path complies with the declared policy. |
| `target_implementation_fact` | Source inspection establishes how the current target is implemented. | File and symbol coordinates, revision, reachable context, and relevant generated-code boundary. | Actual runtime outcome under conditions that were not exercised. |
| `observed_result` | A command, test, build, benchmark, or reproduction was run and its result retained. | Exact command, checkout, environment facts, inputs, exit status, and material output. | Behavior outside the exercised matrix or a causal explanation by itself. |
| `negative_or_contradictory_evidence` | A source or observation conflicts with, narrows, or fails to confirm a claim. | Search or test scope, contradiction, coverage limit, and the claim affected. | Universal absence unless the examined space was demonstrably exhaustive. |
| `combined_evidence_inference_note` | Multiple identified facts support a conclusion that no single source states. | Premises with separate labels, inference rule, target scope, and plausible alternative explanation. | Direct source authority for the synthesized conclusion. |
| `engineering_judgment` | A recommendation chooses among valid options using explicit tradeoffs. | Decision context, alternatives, governing values, reversibility, and review trigger. | Objective superiority outside those assumptions. |
| `forecast_or_hypothesis` | A proposed outcome or explanation remains to be tested. | Causal rationale, disconfirming observation, test plan, and expiration condition. | Present behavior or promised future performance. |
| `conditional_claim` | A statement is valid only when named preconditions hold. | Preconditions, postcondition, excluded cases, and verification route. | The presence of those preconditions in an unseen repository. |
| `superseded_or_rejected_claim` | Earlier guidance is retained because its failure or replacement informs later work. | Former claim, rejection evidence, replacement decision, date, and affected consumers. | Permission to keep using the former recommendation. |

The older label `external_research_sourced_fact` is unsafe for this snapshot because no public page was retrieved during the evolution. Existing URLs and domains in the external source map therefore remain `external_mapping_unrefreshed_note` entries until a future task performs the retrieval, checks ownership and version, and records what the source actually entails. Renaming the boundary prevents an inherited link from acquiring borrowed authority merely by surviving into a newer reference.

**Precedence and conflict handling**

Evidence classes answer different questions, so precedence is based on ownership and applicability rather than a universal ranking. Apply these rules:

1. Obey explicit task constraints and applicable target instructions for the work procedure. Record a conflict instead of silently substituting a generic skill preference.
2. Use target policy and resolved build configuration to describe what the project selects. Use implementation inspection and observed results to describe what the project does.
3. Use the frozen Kotlin skill corpus to describe this skill's routing, language-level reliability defaults, and quality-gate doctrine.
4. Use refreshed official sources for current public language, library, or tool behavior. A maintainer source can update an external fact but cannot rewrite a target's local policy without a target change.
5. Keep inference and judgment visibly downstream from their premises. They may guide action, but they do not overwrite contradictory facts.
6. When sources disagree, preserve both coordinates, narrow each claim to its applicable scope, identify the owner of the disputed contract, and state what observation would resolve the conflict.

This model permits two apparently opposing facts to coexist. For example, an official coroutine API may support cancellation while a target wrapper suppresses or delays it. The public contract and target implementation describe different layers. The engineering decision must address the gap rather than discard whichever source is less convenient.

**Minimum record for a consequential claim**

Use a compact record for guidance that affects public APIs, nullability boundaries, concurrency, Java compatibility, generated interfaces, releases, or mandatory checks. The field names are stable; the values below illustrate a fully populated local-corpus claim rather than an empty template.

```text
claim_id: KLS-EVIDENCE-001
claim: Start Kotlin reliability routing from the canonical skill and its reference map.
label: local_corpus_hierarchy_note
source_coordinates: SKILL.md and references/reference-map.md in the kotlin-coder-01 skill
snapshot_skill: e7e1606b917312f104e9ab337154bd88836dd292af82b64f6df359fb6d8889de
snapshot_reference_map: 53cff6b483ef56f72ff6e78914963539891e81970827e8ffc8e3f63be99fa944
target_scope: Generic Kotlin language implementation and review work
verification: Read both local sources completely and compare the requested task with their routing boundaries.
limit: Backend delivery concerns require the backend-focused owner after target inspection.
invalidation_trigger: The canonical skill or reference map changes its routing contract.
consumers: Entry routing, adjacent-reference selection, and final quality-gate review
```

For an observed result, replace source interpretation with exact execution evidence. Include the command, checkout revision, runtime and tool versions that affect the result, relevant inputs, exit status, and bounded output. Do not convert a proposed command from this reference into an `observed_result` until it has actually run in the intended target.

**Examples that expose the boundary**

- Good local claim: "The frozen Kotlin skill separates generic language reliability from backend delivery" can be labeled `local_corpus_hierarchy_note` when the canonical skill and reference map are cited. Its limit is that the active target still needs classification.
- Good target observation: "The configured verification task passed for checkout X under JDK Y" can be labeled `observed_result` only with the exact command and result. It does not show that an omitted source set, platform, or runtime path is healthy.
- Good synthesis: "This target should wrap the Java platform type before it reaches domain code" can be a `combined_evidence_inference_note` when source inspection identifies the platform boundary and the local nullability doctrine supplies the containment principle. The wrapper design itself remains engineering judgment.
- Borderline claim: "A data class is appropriate here" remains `engineering_judgment` until the author demonstrates value semantics, equality expectations, copy behavior, and mutability boundaries in the target. Merely having several properties does not promote it to fact.
- Unsound claim: "The linked documentation confirms the current compiler default" is not permitted when only an inherited URL is available. Keep the route unrefreshed and retrieve the authoritative versioned page when the decision depends on it.
- Unsound absence claim: "No blocking call exists" is not established by a narrow text search. Record the searched scope and terms as `negative_or_contradictory_evidence`, then inspect wrappers, Java interop, generated code, and indirect I/O paths before broadening the conclusion.

**Verification protocol**

1. Split compound prose into independently testable claims. A sentence containing a local rule, a target assertion, and a forecast needs three labels.
2. Select the narrowest evidence class and record source coordinates, snapshot or version, scope, limitation, and invalidation trigger.
3. Read the cited region in context. Check semantic entailment: the evidence must support every material clause, not merely share Kotlin vocabulary.
4. Reproduce observable claims in the intended target. Preserve the exact command and conditions, and distinguish a passing check from the explanation for why it passed.
5. Search for contradictory and negative evidence across the relevant boundary. Report incomplete coverage instead of turning an unsuccessful search into universal absence.
6. Map downstream consumers and register the event that requires review. Recheck affected claims when a source, target policy, implementation, dependency, toolchain, or requirement changes.

Mechanical integrity and semantic support are separate gates. A hash proves that a local snapshot has not changed; it does not prove that the prose interprets the snapshot correctly. A command exit status proves the recorded execution outcome; it does not prove that the command exercised every contract named in the recommendation. A skeptical review must pass both gates.

**Known evidence for this evolution**

The following inventory is intentionally bounded to work actually performed on 2026-07-11:

- The complete archive seed and initial working reference were read. They were initially byte-identical at SHA-256 `e9fd0593e882398b2aec13963f838afb1584d8d716223512ddc22f69dcc312e3`.
- The governing evolution specification, evolution tests, and Beta progress journal were read completely for process and acceptance constraints.
- The canonical Kotlin skill was read at SHA-256 `e7e1606b917312f104e9ab337154bd88836dd292af82b64f6df359fb6d8889de`.
- The local reference map was read at SHA-256 `53cff6b483ef56f72ff6e78914963539891e81970827e8ffc8e3f63be99fa944`.
- The Kotlin reliability reference was read at SHA-256 `9a9fe3255daed3376ed035de5baacf12de09edc9d3e1b5c3314f4a43a03f101f`.
- The quality-gates and anti-patterns reference was read at SHA-256 `1b393027a06d8a4ca7790822c9c29485bd3e8d59d77d7dfc310a8a761cb44400`.
- The sources and research brief was read at SHA-256 `b0fe8c64510af0025187f60d03440d286492342787a8e2a8e4b48e2a0bb05028`.
- No public page was retrieved, no public claim was refreshed, and no future consumer repository was inspected. Current external releases, defaults, advisories, compatibility, and target-specific outcomes therefore remain unknown until a relevant task supplies evidence.

Earlier completed Kotlin Beta references can support consistency checks inside this local corpus. They do not automatically prove a claim about another repository, a new toolchain, or a later dependency version. Likewise, a filename observed in the working reference directory is not evidence that its contents were read unless the relevant evidence record says so.

**Negative evidence and uncertainty discipline**

Record what was searched or tested, why the scope was expected to reveal the condition, and which blind spots remain. A failing test is evidence against the exercised behavior. A passing test is evidence for that behavior under the exercised conditions. No matching text may mean the construct is absent, generated, aliased, indirect, or expressed with different vocabulary. These outcomes must not share one conclusion.

When support is incomplete, use uncertainty to guide the next action:

- Missing current public semantics calls for a bounded refresh of the authoritative source.
- Missing target applicability calls for repository instruction, build, source, and test inspection.
- Conflicting local owners call for scope and precedence resolution.
- An unexplained runtime result calls for reproduction and instrumentation.
- A reversible design choice with complete facts may proceed as labeled engineering judgment.
- An irreversible or high-impact choice should remain blocked until the decisive evidence is obtained.

**Evidence lifecycle and second-order effects**

Evidence is maintained only while a live claim or consumer depends on it. A source update should invalidate the claims that cite that source, not every Kotlin recommendation. A target configuration change should trigger review of target-policy and observed-result records, not stable language semantics. A contradicted claim should remain linked to its replacement long enough for downstream consumers to migrate and for reviewers to understand why the old guidance disappeared.

This selective invalidation reduces both stale certainty and needless rereading. It also exposes evidence debt: the risk created when an important recommendation has no reproducible premise, limitation, or refresh trigger. Resolve the highest-impact debt before adding more prose. The resulting entrypoint stays compact in active context because agents can retrieve decisive claims and known limits without replaying the entire research history.
