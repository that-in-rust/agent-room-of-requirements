# Dotnet Angular Typescript Patterns

Use this reference when one behavior crosses an ASP.NET Core backend and an Angular
TypeScript frontend: a user action becomes a request, validated domain work,
persistence or integration effects, a typed response, explicit client state, and an
accessible visible outcome. It is a vertical-slice boundary guide, not a universal C#,
Angular, or TypeScript style manual.

The conservative default is:

1. State the user-visible behavior, authorization rule, failure states, and rollback
   or recovery expectation.
2. Define the HTTP request, success response, problem response, cancellation behavior,
   compatibility boundary, and any concurrency or idempotency requirement.
3. Implement the thinnest backend entrypoint that validates transport input, invokes
   domain behavior, propagates cancellation, and maps typed outcomes deliberately.
4. Keep persistence and external effects behind boundaries that match real variation
   or test needs; do not add a repository or service layer only because an example has
   one.
5. Generate TypeScript contracts or clients when the project supports reproducible
   generation, but still validate untrusted runtime data at the trust boundary when a
   malformed or stale server response would matter.
6. Give one Angular owner responsibility for remote state and expose explicit idle,
   loading, success, empty, error, cancelled, conflict, and retry states that the
   workflow actually needs.
7. Verify backend behavior, generated-contract drift, TypeScript compilation, Angular
   state and accessibility, and at least one browser-visible cross-layer path.

Prefer the repository's established controllers or Minimal APIs, direct EF Core or
repository boundaries, signals or RxJS, and test runners unless a failed contract or
measured maintenance problem justifies change. Those choices are not interchangeable:
they alter indirection, cancellation, multicasting, runtime validation, and test
scope. Compare the smallest vertical slice under the same behavior before introducing
a new project-wide abstraction.

A good slice traces one user edit through validation, authorization, persistence,
typed success or conflict, and visible recovery. A bad slice pastes a backend endpoint
beside an Angular component while their error, cancellation, and data contracts
disagree. A borderline slice generates TypeScript interfaces from the backend but
assumes that generation validates deployed JSON; it reduces transcription drift while
leaving runtime compatibility unproved.

Route elsewhere for backend-only internals, frontend-only visual design, Node or
MongoDB implementation, broad platform migrations, live operations, or multi-service
choreography. A cross-ecosystem example may supply an explicitly labeled analogy, but
it cannot override the actual .NET and Angular project. This reference's one local
corpus is historical, and its public URLs were not browsed in this pass; current
framework defaults and version-specific APIs require project evidence or a future
primary-source refresh.

Discover solution files, package scripts, generators, and CI gates before naming exact
commands. Compilation proves only local type consistency; backend and frontend tests
prove their scoped behaviors; a generated-client diff proves drift only when the
workflow fails or records approval; and an end-to-end test proves one deployed
behavior under its environment. Treat the durable product as a versioned behavior
contract with recovery semantics, not merely classes with similar names in two
languages.

## Source Evidence Mapping Table

Treat sources as inputs to a project decision, not substitutes for the target
repository. The historical corpus can propose questions and candidate structures;
solution and package manifests, compiler settings, generated contracts, migrations,
builds, tests, and representative traces decide whether those candidates apply.

| source | inspected state | permitted use now | material limit | first applicability gate |
| --- | --- | --- | --- | --- |
| `agents-used-monthly-archive/idiomatic-references-202602/Idiom-DotNet-CSharp-Angular-TypeScript-Patterns.md` | Complete local read; historical version 1.0.0 dated 2026-01-30 | Candidate patterns for naming, ASP.NET entrypoints, EF queries, explicit results, cancellation, Angular state, TypeScript unions and brands, generated clients, SignalR, tests, anti-patterns, performance questions, and dependency rules | Its title asserts specific framework versions and idiomatic status that were not refreshed. Several examples disagree internally or make unverified behavioral claims. | Confirm project stack and conventions, compile the relevant slice, and test the complete caller-to-consumer contract. |
| `https://www.typescriptlang.org/docs/handbook/intro.html` | Inherited URL; not browsed in this pass | Future primary-source check for current TypeScript language semantics when a precise language claim is material | It cannot establish Angular APIs, ASP.NET behavior, generated-client runtime safety, or this project's compiler settings. | Inspect the current direct page, record version or section, then run the target project's typecheck and behavior tests. |
| `https://expressjs.com/en/` | Inherited out-of-stack mapping; not browsed in this pass | At most a future analogy about HTTP middleware or boundary questions | Express is a Node.js framework and supplies no present ASP.NET Core or Angular implementation authority here. | Restate the invariant in .NET terms and verify it with the actual endpoint pipeline; otherwise reject the analogy. |
| `https://www.mongodb.com/resources/products/compatibilities/using-typescript-with-mongodb-tutorial` | Inherited out-of-stack mapping; not browsed in this pass | Future evidence only if a confirmed TypeScript-owned MongoDB boundary enters the workload | It does not support EF Core, SQL persistence, Angular state, or an ordinary ASP.NET-to-Angular contract. | Prove that MongoDB and TypeScript data access are in scope, then verify their independent trust and deployment boundaries. |

The local source is useful but not self-validating. Its Angular service returns an
`Observable` where a component and tests treat the same operation as a `Promise`; its
Minimal API examples and later `Result<T>` service shape are not reconciled; generated
TypeScript interfaces are described as type safe without runtime payload validation;
automatic SignalR reconnect is treated as if message delivery simply resumes; a
four-word naming rule is presented as universal; rigid controller-service-repository
layers are treated as defaults; and frontend benchmark figures have no retained
protocol. These are claim-level defects, not reasons to discard unrelated guidance.

Use a disposition record for every material extraction:
`(source, question, exact claim, historical scope, project observation, decision,
verification, residual uncertainty)`. Good use extracts cancellation propagation,
then proves request abort reaches the endpoint and database operation. Bad use copies
an Express pattern into ASP.NET because both handle HTTP. Borderline use generates a
TypeScript client and treats the generated compile-time shape as drift protection,
while explicitly withholding runtime compatibility confidence until a contract or
browser test exercises deployed payloads.

No current public-page claim is established here. A future refresh must record the
direct URL, checked date, relevant section, supported wording, conflict, and changed
action. Link presence is not semantic support, and one compiling fragment does not
prove that its caller, transport, and consumer agree on async, error, cancellation,
or serialization behavior.

## Pattern Scoreboard Ranking Table

The inherited values are editorial ordering, not probabilities, confidence, benchmark
results, or universal architecture scores. Their calibration is unavailable. Retain
them for traceability, but do not average them, interpret their spacing, or let them
waive a failed compiler, security, compatibility, or user-behavior gate.

| pattern | inherited score or priority | apply when | failure prevented | direct falsifier |
| --- | --- | --- | --- | --- |
| Source Map First (`dotnet_angular_typescript_patterns`) | 95; historical default tier | Before reusing a recommendation from the dated corpus | Historical syntax or examples become current project policy without inspection. | A material recommendation has a source disposition and project applicability result. |
| Evidence Boundary Split (`dotnet_angular_typescript_patterns`) | 91; historical default tier | When historical facts, public mappings, project observations, and synthesis mix | An analogy or stale version claim acquires authority it has not earned. | Every decision-governing claim has the correct evidence state and scope. |
| Verification Gate Coupling (`dotnet_angular_typescript_patterns`) | 88; historical default tier | Before a pattern becomes implementation or release guidance | Plausible architecture has no falsifiable behavioral evidence. | The pattern names the boundary, exact expected behavior, and project-discovered gate. |
| User Behavior Contract First | First construction decision | A feature crosses backend and frontend ownership | Endpoint, generated client, UI, and tests encode different success or failure semantics. | One acceptance example traces request, outcome, visible state, and recovery. |
| Runtime Trust Boundary Validation | Hard external-data gate | Deployed JSON, identity, configuration, storage, or messages can violate static assumptions | Generated or declared types are mistaken for runtime validation. | A malformed, missing, or incompatible payload is rejected or mapped to a safe explicit state. |
| Explicit Backend Outcome Mapping | Before endpoint return shapes stabilize | Validation, absence, conflict, authorization, cancellation, and unexpected failure differ | Exceptions, status codes, and frontend states collapse into generic error handling. | Integration tests assert each material domain outcome and transport representation. |
| One Remote State Owner | Frontend ownership default | Several components consume or mutate one server-backed workflow | Duplicate subscriptions, stale caches, and contradictory loading or error flags appear. | State transitions have one owner and components render derived read-only state. |
| Cancellation Retry Idempotency | Leads for costly or repeated effects | Requests can be abandoned, retried, duplicated, or partially applied | Cancelled work continues, retries duplicate writes, or transient policy hides permanent faults. | Cancellation reaches cancellable work and duplicate delivery has a tested safe outcome. |
| Generated Contract Drift Gate | Leads when code generation is used | Backend schema and TypeScript artifacts can change independently | Stale generated clients compile while deployed behavior diverges. | Reproducible generation produces no unexplained diff and compatibility tests exercise the payload. |
| Accessible State Completeness | Hard presentation gate | A remote operation drives visible user workflow | Loading, empty, error, conflict, or disabled behavior is unavailable to keyboard or assistive users. | Component tests and browser review cover all declared states and accessible names or focus behavior. |
| Cross Layer Behavior Test | Hard completion gate | Independently verified layers must operate together | Backend and frontend suites pass while serialization, auth, timing, or deployment assumptions disagree. | At least one realistic browser path proves the contract and its most consequential failure. |

**Default order for a new slice:** user behavior and authorization, versioned transport
contract, backend outcomes and cancellation, persistence or integration effects,
reproducible client generation, runtime trust validation, one Angular state owner,
accessible rendered states, layer tests, cross-layer behavior, and compatibility or
rollback evidence. Freeze outcome semantics before generation; automation should not
encode an unresolved error model.

**Override rule:** begin repair at the earliest observed failing boundary and rerun
everything that depends on it. An authorization escape outranks all editorial rows; a
malformed deployed payload makes runtime validation lead; a duplicate write makes
idempotency lead; a stale client makes compatibility and generation drift lead. Keep
the override reason. Repeated relevant failures or one high-consequence escape may
justify changing the default order, while one isolated preference does not.

A bounded conflict-returning update is a good default example: the backend maps a
typed conflict, the client validates the response, and Angular renders a recoverable
state. Blindly trusting a generated interface is a bad example. Supporting an old and
new payload shape is borderline and requires explicit deployment assumptions plus
tests for both clients; numeric rank cannot make that migration safe.

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: This theme has one fully inspected historical source. It
explicitly proposes .NET entrypoints, EF persistence, Result-style outcomes,
cancellation, C# language features, Angular standalone components and signals, RxJS,
TypeScript unions and branded identifiers, generated clients, SignalR, layered tests,
anti-patterns, performance ideas, and dependency rules. Its examples are evidence of
what that document proposed, not proof that every snippet compiles together or remains
current and idiomatic.

`external_mapping_unrefreshed_note`: The TypeScript, Express, and MongoDB URLs were
inherited and not opened. They establish no current public-content claim. Express and
MongoDB are also outside the ordinary ASP.NET Core and Angular slice unless a concrete
workload proves their relevance.

`combined_evidence_inference_note`: An idiomatic full-stack slice is the smallest
project-consistent structure that makes user behavior, trust boundaries, side effects,
failure states, compatibility, and verification explicit. Backend and frontend types
need not mirror implementation classes, but they must agree semantically at the
transport boundary.

Use this default loop:

1. Define the user action, read outcome, authorization rule, validation boundary,
   material failure states, and recovery behavior.
2. Define transport semantics before DTO generation: request, success, absence,
   validation problem, conflict, forbidden outcome, cancellation, unexpected failure,
   and any idempotency or concurrency requirement.
3. Implement a thin backend transport boundary and keep domain, persistence, and
   external effects separate only where policy, transaction, isolation, or alternate
   implementation makes that separation useful.
4. Propagate cancellation to cancellable work. Bound retries to classified transient
   operations and make repeated side effects safe before enabling retry.
5. Generate client contracts reproducibly when available. Treat generated TypeScript
   as compile-time drift reduction, then validate untrusted runtime payloads when
   malformed or incompatible data could cause unsafe or misleading behavior.
6. Give remote state one Angular owner. Represent only applicable idle, loading,
   success, empty, error, cancelled, conflict, stale, and retry states; derive view
   state rather than maintaining several contradictory booleans.
7. Choose signals for owned synchronous state and RxJS for multi-value, temporal, or
   cancellable composition only when those roles match the target project. Convert
   between async models deliberately rather than naming an `Observable` method
   `Async` and awaiting it as if it were a `Promise`.
8. Render every material outcome accessibly, with stable focus, usable controls, and
   no silent empty-data fallback for authorization, transport, or parse failure.
9. Run project-discovered compile, unit, integration, contract-generation, component,
   accessibility, and browser gates. Include the most consequential failure path.
10. Verify deployment ordering, backward compatibility, telemetry correlation, and
    rollback when backend and frontend releases or consumers can diverge.

This loop is reversible. A contract test may expose an unresolved error model; a
component test may reveal missing backend state; a browser flow may reveal that a
nominal success is unusable. Return to the earliest responsible boundary and rerun its
dependents rather than patching a generic frontend error or transport exception.

Do not mandate a repository, service, cache, signal, observable, or naming pattern
because the historical source contains it. Keep an existing project convention when
it communicates ownership and passes the behavior contract. Introduce or remove a
layer when real variation, transaction scope, isolation, policy, or testability makes
the change pay for itself. Cross-language symmetry is optional; agreement about data,
outcomes, side effects, and recovery is not.

A conflict-aware update is a good slice: authorization and concurrency are checked,
the backend returns a deliberate outcome, the client validates and maps it, and the
view preserves the user's work with an accessible recovery action. An endpoint beside
a component with incompatible `Promise` and `Observable` assumptions is a bad slice.
A generated client without deployed-payload or stale-client evidence is borderline:
generation helps, but runtime and rollout confidence remain open.

The thesis fits bounded commands, queries, forms, and realtime views. It stops being
sufficient for offline merge policy, distributed transactions, multi-service delivery,
or operational SLO design without narrower guidance. The durable unit is a versioned
behavior contract plus owned generation, telemetry, migration, and rollback semantics,
not a set of similarly named classes.

## Local Corpus Source Map

The sole local corpus is
`agents-used-monthly-archive/idiomatic-references-202602/Idiom-DotNet-CSharp-Angular-TypeScript-Patterns.md`.
It was read completely. Treat it as a historical candidate library and defect ledger,
not current canonical policy. Its first-retrieval status comes from being the only
frozen local source for this theme; final authority comes from the target project's
contracts and executable behavior.

| source region | retrieve when | useful candidate or question | caveat | project gate |
| --- | --- | --- | --- | --- |
| Metadata, contents, and Section 1 naming | Establishing claimed stack, historical intent, or symbol style | Public/private casing, recognizable domain names, and cross-language vocabulary | The file mandates four-word names for every symbol; word count is not established here as an idiomatic C#, Angular, or TypeScript rule. | Inspect project analyzers and naming conventions; judge clarity at call sites and APIs rather than count alone. |
| Section 2 .NET backend patterns | Designing endpoint, persistence, service, result, cache, validation, or cancellation boundaries | Thin transport handling, explicit outcomes, specifications, cancellation propagation, and cache invalidation questions | Minimal API handlers and the later `Result<T>` service contract are not reconciled; generic repositories and services may duplicate EF Core or domain behavior. | Compile one slice; run endpoint and persistence integration tests for every material outcome and side effect. |
| Section 3 C# language features | Considering primary constructors, collection expressions, required members, records, or initialization | Concision and compile-time initialization candidates | Feature availability and style depend on the target language version, analyzers, serialization, and framework conventions. | Read the project language configuration, build all consumers, and test serialization or binding behavior where relevant. |
| Section 4 Angular frontend patterns | Choosing component shape, remote state, signals, RxJS, caching, or subscription lifetime | Standalone composition, derived state, immutable updates, explicit loading and error states, and teardown questions | One service returns `Observable<User>` while a component awaits it and tests return a `Promise`; automatic retries and manual subscriptions lack complete lifecycle policy. | Typecheck and run component tests with the real async contract, cancellation path, error state, teardown, and target rendering. |
| Section 5 TypeScript patterns | Modeling finite states, literal inference, or domain identifiers | Discriminated unions, exhaustive handling, and prevention of accidental ID mixing | Brands and generated interfaces disappear at runtime; assertions and casts can bypass safety; exception-throwing factories may not match boundary error policy. | Run strict typechecking plus malformed-input and boundary parsing tests; prove exhaustive behavior rather than relying on a cast. |
| Section 6 full-stack integration | Generating clients or adding SignalR-style realtime behavior | Reproducible DTO generation, one transport client, authenticated connection, reconnect, and state update questions | Generated types do not parse JSON; reconnect does not prove ordering, deduplication, replay, authorization renewal, or message recovery. | Diff reproducible generation, test deployed payload compatibility, and exercise disconnect, reconnect, missed-message, duplicate, and stale-auth behavior. |
| Section 7 testing patterns | Selecting backend, frontend, or browser evidence | Unit seams, validation examples, component state assertions, and user-flow coverage | Historical runner choices and mocks may not match the project; some tests assume the `Promise` contract that contradicts source service code; selectors and shared data can be brittle. | Discover current test projects and scripts, then add integration and contract tests where mocks would hide cross-layer disagreement. |
| Section 8 anti-patterns | Reviewing controller logic, cancellation, N+1 queries, subscriptions, signal mutation, or fallback errors | Durable failure mechanisms and safer questions | "Always" layering and empty-array error fallback can hide legitimate simple designs or convert failure into misleading success. | Reproduce the failure, verify the chosen correction under project ownership, and preserve visible error semantics. |
| Section 9 performance | A measured latency, query, rendering, or list-density problem exists | No-tracking queries, projection, paging, bulk operations, caching, virtual scrolling, stable identity, and change-detection hypotheses | The 10,000-item, 3-second, 50-millisecond, and 60-fps figures have no retained protocol and cannot be reused as targets. Caching also changes freshness and authorization behavior. | Establish workload and baseline, inspect database plans or browser traces, benchmark the exact candidate, and verify correctness under cache invalidation. |
| Sections 10-11 dependency rules and quick card | Auditing architecture direction or orienting before deeper retrieval | Explicit allowed and forbidden dependencies plus a compact candidate index | The fixed controller-service-repository and page-feature-UI layers may not match a vertical slice; the nested Markdown fence is malformed; quick-card tools are historical. | Derive the actual dependency graph, prohibit cycles and trust-boundary violations, and validate architecture rules against intentional project modules. |

Use progressive profiles. A full vertical slice usually reads metadata, the relevant
backend, Angular, TypeScript, integration, testing, anti-pattern, and dependency
regions. A backend-only task can omit Angular after recording why no consumer contract
changes. A frontend-only task still checks the transport and runtime payload boundary.
A language-feature question can remain narrow unless serialization, generation, or
public contract behavior makes it cross-layer.

Record `(region, unresolved question, extracted proposal, observed defect, project
evidence, selected or rejected decision, verification result)`. Good retrieval pairs
the Result proposal with endpoint mapping, generated-client, component-state, and
integration-test regions for one profile update. Bad retrieval copies the source's
four-word names and architecture graph wholesale. A SignalR proposal is borderline
until the target defines missed-message, replay, duplicate, ordering, and stale-auth
semantics and tests the ones that matter.

The source's path, headings, prose, examples, and contradictions are known. Current
idiomatic status, compile success in a complete project, benchmark results, and public
framework guidance remain unproved. Preserve cross-region contradictions as regression
fixtures: a future refresh should reconcile the async and outcome models rather than
merely replacing their syntax.

## External Research Source Map

No browsing occurred in this pass. These URLs are retained as
`external_mapping_unrefreshed_note`, not current facts.

| inherited URL | historical role | permitted future scope after inspection | current disposition | local applicability gate |
| --- | --- | --- | --- | --- |
| `https://www.typescriptlang.org/docs/handbook/intro.html` | TypeScript handbook entrypoint | Current language semantics for a precise TypeScript question | Retain as a plausible primary-source target; contents and currency unverified here. | Compare with the project's compiler configuration, then typecheck and test the behavior that depends on the rule. |
| `https://expressjs.com/en/` | Express documentation | HTTP middleware or routing only when a confirmed Node.js component is part of the workload | Reject for ordinary ASP.NET Core and Angular implementation decisions; at most retain a labeled analogy. | Reframe the invariant in ASP.NET terms and test the actual endpoint pipeline, or discard the analogy. |
| `https://www.mongodb.com/resources/products/compatibilities/using-typescript-with-mongodb-tutorial` | MongoDB and TypeScript tutorial | A confirmed TypeScript-owned MongoDB access boundary | Reject for EF Core, SQL persistence, Angular state, and normal ASP.NET-to-Angular contracts. | Prove the MongoDB component, data owner, runtime parser, and deployment boundary exist before inspecting or applying it. |

The inherited map is insufficient for current version-sensitive .NET and Angular
claims. A future pass may need direct primary documentation, release notes, migration
guidance, and security or compatibility material for the exact framework and package
versions discovered in the target project. This reference does not invent those URLs
or contents. Local lockfiles, compiler settings, generated artifacts, and executable
tests remain necessary even after official guidance is refreshed.

Refresh only when an external fact can change a material implementation, migration,
security, compatibility, or completion decision. Use this record:

`(trigger, direct_url, source_owner, checked_date, version_or_section,
paraphrased_claim, project_version, applicability, conflict, decision,
local_retest, residual_uncertainty)`

Classify the result as `inspected`, `applicable`, `reproduced`, `reconciled`,
`rejected`, or `no_material_impact`. An official page can be current yet inapplicable
to the deployed version; a project can compile while relying on behavior that a
future upgrade removes. Currency and applicability are separate.

Good use refreshes a TypeScript language rule after a real compiler question, then
runs the target typecheck and behavior test. Bad use cites Express to choose ASP.NET
middleware because both process requests. Borderline use extracts a validation
question from the MongoDB tutorial for a confirmed Mongo-backed TypeScript worker,
then derives implementation and verification from that worker's own stack rather
than transferring tutorial code.

Prefer event triggers such as a failed gate, package upgrade, migration, deprecation,
or new integration. Schedule periodic checks only for external contracts the product
actively depends on. Retire a mapping after repeated irrelevance, preserving why it
was rejected and which new workload condition would justify reopening it. A larger
bibliography is not a stronger evidence boundary.

## Anti Pattern Registry Table

Classify a failure only after naming the violated behavior, trust, ownership,
compatibility, or maintenance contract. Architectural resemblance is not enough. Fix
authorization and untrusted input first, then duplicate or partial side effects,
transport semantics and cancellation, runtime parsing, frontend state and
accessibility, performance, and finally naming or style.

| anti-pattern | cause and consequence | detection signal | safer response | valid boundary or exception |
| --- | --- | --- | --- | --- |
| `context_free_summary_output` | Historical examples become generic current advice without target-project inspection. | No source disposition or discovered project contract changes the recommendation. | Trace the proposal through project evidence and one behavior gate. | A source region may be skipped when its nonimpact is recorded. |
| `unsourced_recommendation_claims` | Version, security, compatibility, or performance language sounds authoritative without inspected support. | The claim has no evidence state, project result, or uncertainty. | Separate historical fact, unrefreshed mapping, synthesis, and observation. | A preference is valid when clearly scoped and owned. |
| `universal_word_count_naming` | A fixed four-word rule inflates symbols and substitutes counting for domain clarity. | Names satisfy word count but obscure the call-site behavior or local convention. | Follow language and project casing; use the shortest unambiguous domain name. | A project can enforce a deliberate naming schema with analyzer and review evidence. |
| `reflexive_layer_abstraction` | Controllers, services, and repositories are added even when they only forward calls, creating translation and test drift. | Each layer repeats the same method and outcome with no policy, isolation, transaction, or alternate implementation. | Keep the direct boundary or extract only the behavior that varies. | A layer is justified by real policy, ownership, transaction, or replacement needs. |
| `transport_domain_outcome_collapse` | Validation, absence, conflict, forbidden, cancellation, and unexpected failure become null, exception, or one generic error. | Status mapping and UI recovery cannot be derived deterministically. | Define typed domain outcomes and deliberate transport and view mappings. | A truly impossible distinction may remain internal when no consumer behavior changes. |
| `static_type_runtime_trust` | Generated interfaces or TypeScript annotations are treated as runtime payload validation. | Malformed JSON reaches components as if it satisfied the declared type. | Parse at the external trust boundary and map failure to an explicit state. | Closed-process values may rely on static types when runtime corruption is outside the threat model. |
| `async_model_identity_mismatch` | An `Observable` is awaited or a `Promise` is consumed as a stream because naming hides the actual contract. | Components, services, and tests use incompatible completion, cancellation, or multiplicity semantics. | Choose one public async model and convert explicitly at a named boundary. | A deliberate adapter is valid when lifetime and error semantics are tested. |
| `duplicate_remote_state_ownership` | Components and services maintain separate loading, data, error, and cache state for one workflow. | Races produce stale views or contradictory booleans after refresh and retry. | Give the workflow one owner and expose derived read-only state. | Independent views may own separate projections when synchronization is unnecessary. |
| `retry_without_idempotency` | Automatic retry repeats a write or hides a permanent authorization, validation, or conflict failure. | Duplicate records, charges, messages, or confusing delayed errors appear under transient faults. | Classify failures, bound retry, and make repeated side effects safe first. | Idempotent reads may retry under an explicit policy and cancellation budget. |
| `cancellation_token_sink` | Request cancellation stops at the endpoint while database, network, or background work continues. | Aborted requests retain resources or complete effects the caller believes abandoned. | Propagate cancellation to cancellable operations and define commit boundaries. | Durable accepted background work may outlive the request when acknowledgement semantics say so. |
| `cache_scope_or_freshness_leak` | A cache ignores user, tenant, authorization, mutation, or staleness boundaries. | One caller sees another's data or updates remain invisible after success. | Include security and version scope, invalidate deterministically, and test stale behavior. | Immutable public data can use a simpler cache with a declared freshness contract. |
| `reconnect_equals_delivery` | A re-established realtime connection is assumed to restore missed, ordered, unique, authorized messages. | Gaps, duplicates, reordering, or expired identity silently corrupt client state. | Define replay, cursor, deduplication, resync, and auth-renewal behavior as needed. | Ephemeral best-effort notifications may accept loss when the UI says so and can resync. |
| `stale_generated_contract` | Generated output is edited manually or not reproduced when the backend schema changes. | A clean frontend build uses old shapes or unexplained generated diffs recur. | Regenerate deterministically, review the diff, and test deployed compatibility. | Hand-written adapters are valid when explicitly owned and contract-tested. |
| `failure_as_empty_success` | HTTP, parse, or authorization failure is converted to an empty array or absent value. | The UI presents "no data" while the operation actually failed. | Preserve failure as a distinct state with useful recovery. | A fallback is acceptable when product semantics explicitly equate failure with optional absence. |
| `subscription_or_effect_lifetime_leak` | Long-lived subscriptions, browser effects, timers, or storage writes outlive their owner or run in unsupported environments. | Duplicate requests, memory growth, server-render errors, or repeated side effects follow navigation. | Bind lifecycle, use project-supported teardown, and isolate browser-only effects. | Application-lifetime services may be long-lived when their ownership is deliberate. |
| `inaccessible_async_state` | Loading, error, conflict, disabled, or retry behavior is visible only through color, timing, or pointer interaction. | Keyboard or assistive users cannot discover status or recover focus. | Give states semantic text, accessible names, predictable focus, and operable controls. | Purely decorative status can remain hidden when it communicates no action or meaning. |
| `mock_only_boundary_confidence` | Unit mocks reproduce assumptions shared by both sides and never exercise serialization, auth, database behavior, or browser rendering. | All units pass while the vertical slice fails in integration. | Keep focused units and add the smallest real boundary test for the claim. | Pure computations with no external contract can remain unit-tested. |
| `protocol_free_performance_target` | Historical latency, render, node-count, or frame-rate numbers become acceptance targets without workload evidence. | Teams optimize a synthetic number while correctness or real bottlenecks remain unknown. | Define workload, baseline, environment, correctness invariant, and reproducible measurement. | A contractual SLO is valid when its owner, population, and collection method are explicit. |
| `deployment_compatibility_blindness` | Backend, generated client, and frontend are treated as one atomic release despite independent deployment or stale consumers. | New payloads or outcomes break old clients with no safe rollback. | Test supported version combinations and stage additive change before removal. | Co-deployed internal prototypes can use a narrower compatibility envelope when documented. |

A good profile update maps a typed conflict through endpoint, runtime parser, one state
owner, accessible recovery, and a browser test. A bad update retries a non-idempotent
write and converts the final failure to empty data. A direct EF query is borderline but
often acceptable when it is bounded, testable, and contains no domain policy; record
the trigger that would justify extraction rather than adding a forwarding repository.

Use controlled probes: malformed and missing fields, forbidden identity, duplicate
delivery, cancellation at each side-effect boundary, stale generated output, old and
new client versions, disconnect and resync, cache mutation, keyboard recovery, query
count, and measured load. A detector earns only the scope it demonstrates. Preserve
the failing request, payload, state transition, and deployment combination so the
repair can be compared under unchanged inputs.

Cascades matter. An ambiguous backend result can create a stale generated client,
generic frontend error, misleading telemetry, and unsafe retry loop. Repeated frontend
compensation is evidence that the upstream outcome or runtime parser may be
underspecified. Repair the earliest supported cause and rerun every invalidated
downstream gate instead of polishing symptoms.

## Verification Gate Command Set

Run the focused assignment verifier from the repository root after editing this
reference and packet:

```bash
python3 tests/verify_idiomatic_reference_file.py --path idiomatic-ref-202607/dotnet_angular_typescript_patterns-20260710.md
```

Then run the shared reference-generation contract:

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

Those commands verify this documentation workflow. They do not compile the historical
snippets, discover a target application, inspect a database, render Angular, or prove
runtime compatibility.

For application work, discover the actual gates before invoking them:

```bash
rg --files -g '*.sln' -g '*.slnx' -g '*.csproj' -g 'global.json' \
  -g 'Directory.Build.*' -g 'package.json' -g 'angular.json' \
  -g 'tsconfig*.json' -g 'playwright.config.*' -g '*openapi*' -g '*swagger*'
```

Inspect the discovered solution, project references, package manager lockfile,
`package.json` scripts, generator configuration, test projects, and CI before choosing
commands. Typical command families include `dotnet build`, `dotnet test`, the
project's TypeScript or Angular build, its component tests, its accessibility checks,
its browser tests, and its contract-generation script. Replace placeholders with
discovered paths and scripts; do not report a gate as run when it does not exist.

| claim | required gate | pass evidence | limit |
| --- | --- | --- | --- |
| Backend code compiles under the selected project configuration | Build the discovered solution or affected project, including analyzers and generated code used by CI. | Exact command, configuration, candidate revision, and clean exit. | Compilation does not prove authorization, persistence, or transport behavior. |
| Domain outcomes map correctly to HTTP | Run endpoint integration tests against real routing, validation, authorization policy, serialization, and representative persistence or integration boundaries. | Each material outcome has an asserted transport representation and side-effect result. | A mocked service can conceal middleware, binding, database, and serialization disagreement. |
| Cancellation and idempotency are safe | Abort operations at relevant boundaries and deliver duplicate requests or messages under the declared policy. | Cancellable work stops where promised and repeated effects have the expected single, rejected, or reconciled outcome. | Synthetic interleavings do not establish every production race. |
| Generated client is reproducible | Run the discovered generator from its canonical schema, then inspect version-control status and the generated diff. | No unexplained generated change, or an explicitly reviewed compatibility change. | A clean diff does not validate deployed payloads or old clients. |
| Runtime payload is trustworthy | Exercise malformed, missing, extra, and version-skewed data at the external parser or adapter. | Unsafe data is rejected or mapped to an explicit recoverable state. | Static TypeScript success is not runtime evidence. |
| Angular state behavior is complete | Run project component or state tests for every declared idle, loading, success, empty, error, conflict, cancelled, stale, and retry transition that applies. | One state owner produces deterministic derived view state without leaked lifetime. | Unit doubles may still mirror the same incorrect server assumption. |
| UI is accessible and recoverable | Use the project's semantic, keyboard, focus, and automated accessibility checks on material states. | Status, controls, names, focus movement, and recovery are usable under the declared audience contract. | Automated scans cannot establish every assistive-technology experience. |
| Full-stack behavior agrees | Run the smallest realistic browser or consumer path through real serialization, auth, backend outcomes, and rendered recovery. | The happy path and most consequential failure match the behavior contract. | One end-to-end path is intentionally narrow and needs lower-layer breadth. |
| Independent deployment is compatible | Exercise every supported backend and frontend version ordering, migration step, feature flag, and rollback path. | Old and new consumers fail safely or continue according to the declared envelope. | Predeployment tests need staged telemetry when environment behavior remains material. |

Use fast build, type, and focused unit gates during construction. At candidate state,
run boundary integration, generation, component, accessibility, and browser evidence
that the change invalidates. Before release, add supported-version, migration,
observability, and rollback gates. Stop downstream testing on an unexplained generated
diff or failed contract; fix the earliest boundary and rerun its dependents.

A useful evidence packet records working directory, candidate identity, exact command,
configuration, dependency state, selected projects or scripts, result summary,
retained output, coverage claim, and limit. "All tests passed" without those details is
not enough. Keep at least one malformed-payload, conflict, cancellation, duplicate, or
stale-client failure as a regression fixture when that risk is material.

## Agent Usage Decision Guide

Use behavior and ownership, not keywords, to route the task.

| usage mode | choose when | minimum action | boundary |
| --- | --- | --- | --- |
| Primary vertical slice | One user behavior crosses ASP.NET Core transport or effects and an Angular TypeScript consumer. | Define outcome contract, trust parsing, backend mapping, one remote-state owner, visible recovery, cross-layer test, and release envelope. | This reference coordinates the complete behavior. |
| Backend boundary profile | Backend behavior changes but no Angular implementation is edited. | Verify transport compatibility, generated or hand-written consumers, cancellation, side effects, and integration tests. | Route backend internals to a .NET-specific method; retain this profile for consumer impact. |
| Frontend consumer profile | Angular consumes a stable backend contract. | Confirm deployed payload and runtime parsing, choose state ownership and async model, render accessible states, and run component plus browser evidence. | Route visual composition or product design elsewhere when remote behavior is unchanged. |
| Contract evolution profile | Schema, generated client, outcome, or supported version changes across independently built consumers. | Identify schema owner, regenerate deterministically, test old and new combinations, stage migration, and define rollback. | Compatibility and generation are primary even if application code changes are small. |
| Realtime companion profile | A push connection affects Angular state. | Define initial snapshot, ordering, duplicate, gap, resync, auth renewal, reconnect, and offline behavior before choosing client code. | Route broker operations and distributed delivery guarantees to specialized guidance. |
| Avoid as primary | The decisive work is pure language syntax, CSS or visual UI quality, database tuning, Node or MongoDB implementation, infrastructure, security architecture, or multi-service operations. | Open the narrower reference and attach only the affected full-stack contract check. | Do not load this historical corpus as generic technology authority. |

Before implementation, record:

- the user-visible action or query and every material success, empty, validation,
  conflict, forbidden, cancelled, stale, and unexpected-failure outcome;
- discovered solution and project files, frontend package scripts, compiler settings,
  generated artifacts, schema owner, affected consumers, and deployment ownership;
- the trust boundaries for request, identity, payload, storage, realtime messages, and
  browser persistence;
- the selected backend outcome model, public async model, Angular remote-state owner,
  compatibility envelope, and rollback or recovery owner;
- the exact project-discovered build, integration, generation, type, component,
  accessibility, browser, and deployment gates that the change can invalidate.

A reduced local helper profile may inherit all cross-stack contracts unchanged, but
the record must say why. Re-run routing when an endpoint becomes public, a write gains
retry, a payload is generated, another component consumes state, ownership changes,
or backend and frontend deployments separate.

Stop before production implementation when the actual stack has not been inspected,
the user outcome or authorization rule is unknown, schema or generated-client
ownership is missing, current volatile API behavior is decision-critical but
unverified, no test can cross the changed boundary, or supported consumer versions are
undefined. An exploratory spike may proceed as an isolated study with a convergence
gate; it cannot claim production fitness.

Good routing uses the primary profile for a profile-edit form whose backend can return
validation, forbidden, conflict, and success outcomes. Bad routing opens this reference
for a CSS-only card refinement. A backend schema change with an unknown Angular
consumer is borderline: pause implementation, discover consumers and generation
ownership, then choose backend-boundary or contract-evolution scope. File extension
does not settle the route.

Retain a routing record containing user behavior, affected boundaries, project
evidence, chosen profile, companion concerns, rejected profiles, first probe, gate set,
and reversal condition. The route remains provisional until the project probe and
consumer map confirm it. A correct route minimizes duplicated truth while ensuring
schema, runtime parsing, state, telemetry, compatibility, and rollback each have an
owner.

## User Journey Scenario

Use this hypothetical journey to hold one behavior constant while comparing implementation choices. An authenticated user edits a profile, submits once, and receives one distinguishable outcome: success, validation rejection, forbidden access, missing record, version conflict, or unavailable service. On every recoverable failure, the interface preserves the user's input and presents a deterministic next action. Conflict handling is optional unless the target persistence model exposes a real version invariant; do not invent a conflict state solely to make the example look complete.

| Phase | Action | Evidence to retain | Rework or stop condition |
|---|---|---|---|
| Discover | Locate the solution, Angular workspace, endpoint, schema or client generator, authentication boundary, tests, and deployment owners. | Paths, commands, owners, and the current observable behavior. | Stop contract work if schema ownership or the actual consumer cannot be identified. |
| Specify behavior | Write examples for accepted input and each applicable rejection. State whether duplicate submission is ignored, joined, or processed idempotently. | Named examples tied to user-visible effects and persistence effects. | Remove outcomes that the backend cannot distinguish; add missing consequential outcomes before coding. |
| Shape the contract | Define transport fields, stable outcome semantics, version data when required, and compatibility expectations. | A candidate contract plus one informative rejected alternative. | Characterize existing behavior first when a deployed consumer constrains the change. |
| Implement the backend | Apply authorization, validation, cancellation, persistence, and outcome mapping at explicit boundaries. Choose Minimal API or controller and direct persistence or repository from project variation, not fashion. | Compile results, focused endpoint tests, persistence assertions, and cancellation observations. | Return to the contract if different failures collapse into an empty or generic success response. |
| Cross the runtime boundary | Regenerate the client when generation is owned, inspect the diff, and validate untrusted response data where static types cannot establish runtime shape. | Frozen schema input, generator command and version, generated diff, and malformed-payload test. | Do not hand-edit generated output or treat an unknown generator as a harmless convenience. |
| Own frontend state | Put durable view state in one owner. Use a signal for local synchronous state and an Observable pipeline for cancellable or multi-event work; adapt between models once at a named boundary. | State-transition tests for idle, submitting, success, each rejection, cancellation, and retry. | Rework when template flags can form impossible combinations or the component awaits an Observable as though it were a Promise. |
| Verify the experience | Exercise keyboard order, focus after failure, accessible status, retained input, duplicate clicks, malformed data, and at least one negative browser path. | Component and browser results correlated with the expected backend outcome. | A visually correct success path is insufficient when error mapping or recovery is untested. |
| Release and hand off | Check old-client compatibility when deploys are independent, define rollback, and record telemetry that links a user-visible category to a backend outcome without sensitive data. | Compatibility result, rollout sequence, rollback trigger, correlation convention, and unresolved risks. | Narrow or stage the release if the server and client cannot be changed atomically and compatibility is unknown. |

A good result is a conflict-aware or rejection-aware form that retains input, announces the outcome accessibly, and offers a verified next step. A bad result maps every failure to an empty success state or duplicates truth across generated code, hand-written interfaces, and component booleans. A generated client with no stale-version test is borderline: it can be acceptable for atomic deployment, but becomes a compatibility risk when consumers roll independently.

This journey is a worked decision model, not evidence that a particular architecture or framework version is correct for a project. Its durable output is the accepted behavior contract, the gate evidence, the deployment assumption, one useful rejected candidate, and the conditions that require the decision to be revisited.

## Decision Tradeoff Guide

Make each choice against a fixed behavior contract. First record success, rejection, cancellation, retry, and compatibility outcomes that the workflow actually needs. Then inspect project convention and run the simplest project-native candidate. Add an abstraction only when it owns demonstrated variation, isolates a consequential dependency, or enables a gate that the baseline cannot support. An organizational mandate may override that default, but it should be labeled as policy rather than inferred technical necessity.

| Decision boundary | Lightweight default | Choose the stronger alternative when | Cost or failure if misapplied | Verification and reversal signal |
|---|---|---|---|---|
| Endpoint organization | Use the repository's existing Minimal API or controller convention and keep transport mapping near the HTTP boundary. | Filters, conventions, authorization policy, versioning, or repeated endpoint behavior needs a shared owner. | Adding a controller layer to a single trivial route creates navigation and tests without new behavior; forcing a compact handler to own many policies hides responsibilities. | Characterize status and body outcomes. Reopen when mapping or policy logic repeats and cannot be tested independently. |
| Application outcome | Return an explicit outcome where expected domain failures must remain distinguishable from infrastructure faults. | Validation, not-found, conflict, forbidden, or duplicate effects drive different transport and UI behavior. | Exception-only control flow can erase expected branches; a universal result wrapper can add ceremony to infallible local operations. | Tests must distinguish every consequential outcome and preserve unexpected-fault telemetry. |
| Persistence boundary | Call the existing persistence abstraction directly for one store-specific use case. | Multiple stores, a consequential external dependency, transaction policy, or reusable query behavior varies independently. | A repository that merely renames ORM calls duplicates an API; direct access becomes harmful when tests or policy require isolation the caller cannot provide. | Run use-case tests against the real persistence semantics that matter. Reopen after repeated mocking pain, policy duplication, or a planned store boundary. |
| Backend validation | Make the server authoritative for security, invariants, and persistent effects. Mirror only stable, user-helpful checks in the client. | Immediate feedback improves correction without pretending to authorize or establish persistence. | Client-only validation is bypassable; duplicating every server rule creates drift and conflicting messages. | Send invalid requests outside the UI and verify server rejection, then test that mirrored client feedback agrees for shared cases. |
| Client construction | Hand-write a narrow adapter when the API is tiny, stable, and generation has no established owner. | A maintained schema, reproducible generator, multiple operations, or several consumers make drift more costly than generated output. | Hand-written interfaces can diverge silently; generated files without frozen input and commands become opaque, unreviewable state. | Regenerate from a clean tree, inspect the diff, compile both sides, and fail CI on unexpected generated changes when generation is adopted. |
| Runtime payload trust | Rely on the generated or declared shape only under an explicit same-build, atomic-deployment trust model, and keep transport conversion in one adapter. | Parse and validate when the producer is external, independently deployed, cached, proxied, or otherwise able to drift or return malformed data. | Static TypeScript types do not validate bytes; parsing every value already established inside one trusted process adds noise without reducing a real risk. | Exercise malformed, missing, extra, and stale-version payloads at the adapter boundary, or prove and retain the narrower atomic trust model. |
| Local Angular state | Use one signal owner for synchronous, local view state with direct derivations. | Work is cancellable, time-based, multi-event, shared as a stream, or composed with other asynchronous sources; use an Observable pipeline. | Duplicating the same truth in signals, subscriptions, and booleans permits impossible states; forcing one-shot local state through broad streams obscures simple transitions. | State-transition tests cover idle, pending, success, rejection, cancellation, and teardown. Reopen when a second owner or temporal operator appears. |
| Shared frontend state | Keep state in the nearest feature or service that owns its lifetime. | Several independent views coordinate writes, caching, invalidation, or navigation recovery against the same source. | A global store for one form adds indirection; scattered feature-local caches can show contradictory data. | Map readers and writers, test invalidation across views, and remove the global layer if no cross-view invariant remains. |
| Async model bridge | Keep the source model through the service boundary and adapt once at a named consumer boundary. | An existing Promise API must join an Observable pipeline, or an Observable must feed signal-owned presentation state. | Awaiting an Observable, nesting subscriptions, or converting repeatedly loses cancellation and obscures lifetime. | Compile against the real return type and test cancellation, late completion, teardown, and duplicate subscription behavior. |
| Deployment compatibility | Co-deploy a breaking contract only when server and all consumers are demonstrably atomic. | Clients, services, caches, or generated consumers roll independently; use additive evolution, version tolerance, or staged migration. | Assuming atomicity can strand an older client; maintaining compatibility forever accumulates dead fields and branches. | Test supported old/new combinations, document the retirement point, and rehearse rollback before removing the compatibility path. |

**Adopt, Adapt, or Avoid**

- **Adopt** a candidate when the target project already uses it, the responsibility exists in this workflow, and a focused gate demonstrates its value.
- **Adapt** it when the responsibility is valid but the historical example conflicts with the project's async model, contract shape, ownership, or deployment topology. Record which local fact changed the implementation.
- **Avoid** it when it exists only in the historical corpus, relies on an unverified current-version claim, duplicates an existing owner, or cannot name a failure it prevents.
- **Escalate** the decision when it changes persistent data, public schema, security policy, generator ownership, or independent release order. These choices are harder to reverse than component structure or local syntax.

Good: a co-deployed profile form uses one endpoint handler, direct project-native persistence, a narrow client adapter, runtime parsing at the transport boundary, and a signal-owned state machine because no independent variation has been observed. Bad: the same form receives a repository, global store, multiple DTO copies, and exception-to-empty fallback without any distinct responsibility or failure test. Borderline: generated TypeScript types are reasonable when schema and regeneration are reproducible, but they are insufficient runtime evidence when responses cross an untrusted or independently deployed boundary.

For a consequential choice, retain this compact ledger:

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

This guide does not establish current .NET, Angular, or TypeScript API recommendations. Framework-version-sensitive syntax still requires target-project compilation and refreshed official evidence. Uncertainty should narrow the change, make it reversible, and strengthen the gate rather than automatically selecting either the most familiar or the most elaborate design.

## Local Corpus Hierarchy

The only mapped local corpus source is:

`agents-used-monthly-archive/idiomatic-references-202602/Idiom-DotNet-CSharp-Angular-TypeScript-Patterns.md`

It is **primary historical evidence**, meaning it is the first local source to inspect for this theme. That status does not make every claim canonical, current, or applicable. The file contains useful cross-stack candidates, dated version labels, internally inconsistent examples, strong claims without retained measurement evidence, and implementation choices that depend on a target project's topology. Classify claims rather than assigning one authority level to the whole file.

| Hierarchy role | Assignment test | Permitted use | Promotion, demotion, or retirement trigger |
|---|---|---|---|
| Historical observation | Exact content can be located in the immutable archive. | Describe what the corpus recommended or demonstrated at that time. | Never promote merely because it appears in the archive; attach project and current evidence. |
| Candidate guidance | The responsibility remains relevant and the claim is not contradicted by its own example. | Seed a behavior contract, decision comparison, or focused test. | Promote after target-project fit and executable gates; demote when the project exposes a counterexample. |
| Supporting evidence | Another local source or project artifact independently reinforces the same bounded claim. | Increase confidence while preserving separate provenance. | Reclassify if the support is duplicate prose rather than independent evidence. |
| Project policy | Current project code, tests, architecture records, or governance explicitly require the choice. | Treat as the local default within the documented boundary. | Reopen when ownership, deployment, contract, or policy changes. |
| Legacy guidance | The claim targets an older framework surface or a superseded local convention. | Explain existing code and migration constraints. | Retire from new-work recommendations after supported legacy consumers are gone. |
| Conflicting evidence | Source sections disagree with each other or with observed project behavior. | Drive a comparison test and preserve the disagreement. | Resolve only with a named contract, project fact, or reproducible result. |
| Negative evidence | The example demonstrates a failure mode worth preventing. | Populate anti-patterns, regression tests, and review prompts. | Keep while the same mistake remains plausible; update the example when the boundary changes. |
| Duplicate evidence | Another item restates the same claim without a distinct source or consequence. | Link to the stronger item rather than increasing confidence. | Remove duplication from the evolved reference while retaining original provenance. |

Apply that vocabulary to the mapped corpus as follows:

| Source theme | Current role in this reference | Useful contribution | Limitation and required gate |
|---|---|---|---|
| Version and technology labels | Historical observation | Identifies the ecosystem the source intended to discuss. | This evolution did not browse; do not treat the stated versions or recommendations as current. Compile against the target manifests and refresh official sources before making a current-version claim. |
| Four-word naming and dependency rules | Candidate plus conflicting evidence | Encourages semantic names and explicit dependency direction. | A universal word count and rigid layer rule can damage framework conventions or add empty indirection. Review names for clarity and dependencies for owned responsibilities instead. |
| C# and API boundary examples | Candidate guidance | Supplies ideas for typed outcomes, validation, cancellation, and narrow transport mapping. | The examples do not establish the target endpoint style, persistence boundary, or error protocol. Characterization and focused endpoint tests decide fit. |
| Angular component and state material | Candidate plus negative evidence | Highlights standalone composition, signals, Observable workflows, loading, failure, and empty states. | One historical flow returns an Observable while a component awaits it and its test mocks a Promise. Compile the real types and test cancellation and teardown before reuse. |
| TypeScript contracts and generated clients | Conditional candidate | Reduces hand-maintained transport duplication when schema generation is owned and reproducible. | Generated declarations do not validate runtime bytes. Freeze schema input, generator command, diff, compatibility expectations, and parser policy. |
| Realtime delivery and reconnect | Conditional candidate plus warning | Introduces connection lifecycle and push-update concerns. | Automatic reconnection does not prove missed messages are replayed or state is reconciled. Test gap detection, duplicate delivery, resynchronization, and backoff. |
| Testing and anti-pattern material | Strong candidate | Provides a broad inventory of compile, unit, integration, contract, component, and browser failure surfaces. | Some examples are illustrative rather than executable. Convert only the behavior relied upon into target-project tests. |
| Performance guidance | Historical observation with unsupported precision | Names allocation, rendering, payload, and latency questions worth measuring. | Retained benchmark harnesses and environments do not support the source's exact figures. Establish a local baseline and report distributions and conditions. |

Good reuse extracts the stable responsibility, records the source theme, and proves the adapted behavior in the target project. For example, preserving validation, forbidden, missing, conflict, and infrastructure outcomes is a useful candidate principle even when the project uses a different endpoint API. Bad reuse copies a universal naming constraint or a benchmark threshold because the prose sounds precise. Borderline reuse includes generated clients: promote them when schema ownership and regeneration are reproducible; retain caution when runtime trust or independent consumer rollout is unresolved.

Use this compact extraction record for consequential claims:

```text
Archive path and heading signal:
Exact historical observation:
Role: candidate | legacy | conflicting | negative | duplicate
Target boundary and user consequence:
Project evidence inspected:
Executable gate and result:
Unresolved currentness or applicability:
Disposition: promote | adapt | retain warning | reject
Owner and refresh trigger:
```

Promotion is reversible. New project evidence can demote a pattern without altering the archive, and a legacy pattern can remain valuable for migration even after it stops guiding new work. Guidance that affects a shared schema, persistent data, production operation, or repeated agent choice should retain an owner and refresh trigger; exploratory orientation can use a lighter record.

## Theme Specific Artifact

Use a **cross-stack behavior ledger** when one workflow must retain the same meaning across .NET application outcomes, HTTP transport, TypeScript runtime trust, Angular state, user recovery, tests, telemetry, and deployment. It is a reconciliation view, not a replacement for an OpenAPI document, generated client, architecture decision record, sequence diagram, or executable test. Link those authorities rather than copying their full schemas or implementations.

| Artifact scope field | Completion rule | Why it matters |
|---|---|---|
| Behavior identity | Give the workflow and contract candidate a stable local name. | Tests and telemetry can coordinate without using transport codes as domain vocabulary. |
| User promise | State the visible success and the user work that must survive recoverable failure. | Prevents backend and frontend teams from optimizing different outcomes. |
| Authoritative declarations | Link the server contract or schema, generator input and command when present, runtime parser, and state owner. | Keeps the ledger from becoming another source of truth. |
| Ownership and deployment | Name backend, frontend, schema, generation, telemetry, and rollback owners; state whether releases are atomic. | Exposes compatibility responsibilities that code layout cannot prove. |
| Conditional concerns | Record whether concurrency, duplicate submission, cancellation, retry, realtime gaps, offline behavior, and persistent migration apply. | Avoids both silent omissions and irrelevant ceremony. |
| Evidence freshness | Record the target project revision, last gate run, and any unrefreshed ecosystem assumption. | Separates retained evidence from current-version authority. |

Complete one row for every outcome that changes a user action, persistent effect, retry rule, or operational consequence:

| Outcome | .NET precondition and effect | Transport discriminant | TypeScript runtime boundary | Angular state and accessible recovery |
|---|---|---|---|---|
| Accepted | Authorized, valid update commits once and returns the resulting version. | Typed success response; exact status follows the project's protocol. | Validate external data when producer drift is possible, then promote to trusted profile state. | Replace displayed profile, announce success without stealing focus, and clear pending state. |
| Validation rejected | Input violates an authoritative server rule; no write occurs. | Structured field or form errors with a stable category. | Parse the rejection before mapping known fields; retain an unknown-form fallback. | Preserve edits, associate messages with controls, focus or summarize the first actionable error, and permit correction. |
| Forbidden | Identity lacks permission; no write occurs and sensitive details remain undisclosed. | Distinct authorization outcome, not validation or missing data by accident. | Map only the safe category and correlation information. | Preserve non-sensitive work when appropriate, explain that the action is unavailable, and provide a safe navigation path. |
| Missing | Target no longer exists or is not visible under the chosen disclosure policy; no write occurs. | The protocol's stable missing or concealed-resource outcome. | Do not coerce an absent entity into an empty successful profile. | Retain useful draft data if policy permits and offer refresh or navigation rather than a retry loop. |
| Version conflict | Supplied version is stale under a real persistence invariant; no silent overwrite occurs. | Conflict category plus only the version or reconciliation data the contract intentionally exposes. | Reject malformed conflict data and keep the submitted draft separate from server state. | Preserve edits, explain that newer data exists, and offer tested reload, compare, or resubmit behavior. |
| Unavailable | Infrastructure cannot establish the effect; commit status is known or explicitly uncertain. | Stable unavailable or ambiguous-effect category with bounded retry guidance. | Preserve the failure distinction instead of returning an empty success object. | Keep input, stop duplicate clicks, announce failure, and offer retry only when the operation and effect policy permit it. |
| Malformed response | Bytes do not satisfy the trusted client contract. | Adapter-local protocol failure; do not pretend it is a domain rejection. | Runtime parser returns a typed failure and captures safe diagnostic context. | Retain work, present a generic recoverable failure, and avoid rendering partially trusted fields. |
| Cancelled | Caller abandons work and the backend observes cancellation where supported; effect semantics remain explicit. | No invented success response after local cancellation. | Unsubscribe or abort through the owned async boundary and ignore late results according to policy. | Leave a coherent idle or retained-draft state without announcing a failure the user did not experience. |

Pair the semantic row with its proof and operational policy:

| Outcome | Backend or contract evidence | Consumer-observable evidence | Retry, duplicate, and cancellation policy | Operational and rollout evidence |
|---|---|---|---|---|
| Accepted | Endpoint and persistence test proves one authorized write and returned version. | Component or browser test proves rendered data, success announcement, and pending-state exit. | Duplicate submission is prevented or made idempotent; cancellation timing is characterized. | Bounded success category, supported client/server combinations, and rollback check. |
| Validation rejected | Contract test proves no write and stable error mapping. | Browser test proves retained input, associated messages, keyboard order, and correction. | Automatic retry is prohibited because user correction is required. | Rejection category excludes raw personal input and remains bounded. |
| Version conflict | Concurrent-update test proves stale input cannot overwrite newer state. | Browser test proves draft preservation and deterministic reconciliation. | Blind automatic retry is prohibited; any resubmit uses an explicit fresh version. | Conflict rate and rollout compatibility are observed without high-cardinality payload labels. |
| Unavailable or ambiguous effect | Fault-injection test distinguishes known no-effect from unknown effect where the system can do so. | Negative-path test proves retry controls cannot create accidental duplicate work. | Retry budget, backoff, idempotency key, and cancellation ownership are explicit. | Correlation, alert threshold, staged release, and rollback trigger are retained. |
| Malformed response | Adapter test feeds missing, extra, invalid, and stale-version payloads. | UI test proves untrusted partial data is not rendered and user work remains intact. | Retry follows transport policy only after classifying whether a fresh response can help. | Safe diagnostic event identifies contract boundary and consumer version. |

The profile-update conflict row is a good completed example because it links a backend invariant, no-write effect, transport category, runtime parse, preserved draft, accessible recovery, telemetry, compatibility, and two-sided tests. A row that says only `error -> show message` is invalid because it cannot tell correction from retry or no-effect from ambiguous effect. A success row with no duplicate-submit policy is borderline: it is complete for an idempotent read, but incomplete for a write that can be submitted twice.

Reject or repair the artifact when it copies DTO definitions, leaves an unowned consequential cell, cites a gate that cannot distinguish listed outcomes, or labels uncertainty as success. Use `not applicable` with a reason for a concern that cannot occur and `unresolved` with an owner and decision date for one that still can. The ledger is complete only when every consequential row has one backend or contract observation and one consumer-observable observation; add compatibility and operational observations when releases or ownership are independent.

Refresh the ledger when an authoritative schema, generator, runtime parser, state owner, outcome vocabulary, deployment sequence, or rollback policy changes. Retire it when no shared contract, migration, incident pattern, or repeated decision depends on the reconciliation view. Its executable gates and authoritative declarations remain after retirement because the ledger coordinates evidence rather than owning production behavior.

## Worked Example Set

These examples hold one command-response behavior constant: an authenticated user submits a profile draft, and the system preserves distinct accepted, validation, forbidden, missing, conflict, unavailable, malformed-response, and cancellation effects when they apply. They are semantic sketches, not current-version API prescriptions. Adapt endpoint mapping, Angular integration, validation libraries, and compiler syntax to the target manifests, then retain the behavior vectors and gates.

**Good example: model expected backend effects explicitly.** Expected domain outcomes are data; unexpected infrastructure faults remain faults with separate telemetry. A C# representation can use a closed record hierarchy:

```csharp
public abstract record UpdateProfileOutcome
{
    private UpdateProfileOutcome() { }

    public sealed record Accepted(ProfileDto Profile, string Version)
        : UpdateProfileOutcome;

    public sealed record ValidationRejected(
        IReadOnlyDictionary<string, string[]> Errors)
        : UpdateProfileOutcome;

    public sealed record Forbidden : UpdateProfileOutcome;
    public sealed record Missing : UpdateProfileOutcome;

    public sealed record Conflict(ProfileDto Current, string Version)
        : UpdateProfileOutcome;

    public sealed record Unavailable(bool EffectKnownAbsent)
        : UpdateProfileOutcome;
}
```

Map this hierarchy to the project's HTTP protocol once, at the transport boundary. Do not let controllers, handlers, middleware, and frontend adapters each invent a different mapping.

| Domain outcome | Required transport meaning | Persistent effect | Consumer recovery |
|---|---|---|---|
| `Accepted` | Typed success with resulting profile and version. | Exactly the intended committed update. | Replace trusted state and announce completion. |
| `ValidationRejected` | Structured correction data, distinct from authorization and availability. | No write. | Preserve draft and associate errors with controls. |
| `Forbidden` | Safe authorization rejection under the project's disclosure policy. | No write. | Preserve permitted local work and offer safe navigation. |
| `Missing` | Stable absent or concealed-resource result. | No write. | Refresh or leave the workflow; do not render empty success. |
| `Conflict` | Stale-version result with only intentional reconciliation data. | No silent overwrite. | Keep draft separate from current server state and offer a tested next action. |
| `Unavailable` | Known-no-effect or explicitly ambiguous-effect failure. | Captured by `EffectKnownAbsent` or a stronger project type. | Retry only under the operation's duplicate-effect policy. |

An acceptable alternative uses a language or library result type rather than nested records. It is equivalent only when expected branches remain exhaustive, unexpected faults stay observable, and transport mapping is tested once. Exception-only flow is a poor fit when validation, conflict, and absence are ordinary outcomes that drive different UI recovery.

**Good example: establish runtime trust before state ownership.** Static declarations describe what TypeScript code expects; they do not inspect response bytes. To keep the parser sketch bounded, the code below models only accepted, conflict, and unavailable responses. A project whose wire contract includes validation, forbidden, or missing outcomes must add each one to both the union and parser and test its distinct recovery; this is not a complete client contract for the full outcome table. A narrow adapter can accept `unknown`, validate the selected wire vocabulary, and produce a trusted discriminated result:

```typescript
type Profile = Readonly<{
  displayName: string;
  version: string;
}>;

type UpdateProfileResult =
  | Readonly<{ kind: "accepted"; profile: Profile }>
  | Readonly<{ kind: "conflict"; current: Profile }>
  | Readonly<{ kind: "unavailable"; effectKnownAbsent: boolean }>;

type ParseResult<T> =
  | Readonly<{ ok: true; value: T }>
  | Readonly<{ ok: false; reason: string }>;

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function parseProfile(value: unknown): ParseResult<Profile> {
  if (!isRecord(value) ||
      typeof value["displayName"] !== "string" ||
      typeof value["version"] !== "string") {
    return { ok: false, reason: "invalid profile payload" };
  }
  return {
    ok: true,
    value: {
      displayName: value["displayName"],
      version: value["version"],
    },
  };
}

function parseUpdateProfileResult(value: unknown): ParseResult<UpdateProfileResult> {
  if (!isRecord(value) || typeof value["kind"] !== "string") {
    return { ok: false, reason: "missing result discriminant" };
  }

  if (value["kind"] === "unavailable") {
    return typeof value["effectKnownAbsent"] === "boolean"
      ? { ok: true, value: {
          kind: "unavailable",
          effectKnownAbsent: value["effectKnownAbsent"],
        } }
      : { ok: false, reason: "invalid unavailable payload" };
  }

  const field = value["kind"] === "accepted" ? "profile" :
    value["kind"] === "conflict" ? "current" : undefined;
  if (field === undefined) {
    return { ok: false, reason: "unsupported result discriminant" };
  }

  const parsed = parseProfile(value[field]);
  if (!parsed.ok) {
    return parsed;
  }
  return value["kind"] === "accepted"
    ? { ok: true, value: { kind: "accepted", profile: parsed.value } }
    : { ok: true, value: { kind: "conflict", current: parsed.value } };
}
```

A generated validator or schema library is an acceptable alternative when its input and command are owned and reproducible. A type assertion such as `payload as UpdateProfileResult` is not validation. If backend and frontend are built and deployed atomically from one generated schema, omitting a second parser can be a documented trust decision; it becomes borderline when a proxy, independent service, cached response, old client, or untrusted producer can drift.

**Good example: make impossible presentation combinations unrepresentable.** Once the adapter returns a trusted result, a pure reducer can retain the draft through conflict and availability failures:

```typescript
type ProfileDraft = Readonly<{ displayName: string; version: string }>;

type EditState =
  | Readonly<{ kind: "editing"; draft: ProfileDraft }>
  | Readonly<{ kind: "saved"; profile: Profile }>
  | Readonly<{ kind: "conflict"; draft: ProfileDraft; current: Profile }>
  | Readonly<{ kind: "retryable"; draft: ProfileDraft; retryAllowed: boolean }>;

function applyUpdateResult(
  draft: ProfileDraft,
  result: UpdateProfileResult,
): EditState {
  switch (result.kind) {
    case "accepted":
      return { kind: "saved", profile: result.profile };
    case "conflict":
      return { kind: "conflict", draft, current: result.current };
    case "unavailable":
      return {
        kind: "retryable",
        draft,
        retryAllowed: result.effectKnownAbsent,
      };
  }
}
```

An Angular owner can expose this state through project-supported signals or derive it from an Observable pipeline. The semantic requirement is one state owner and one explicit bridge. Independent `loading`, `error`, `empty`, `conflict`, and `profile` variables are a bad alternative when they can simultaneously describe impossible states.

**Bad example: mock a different async program.** The historical corpus contains the shape of this contradiction:

```typescript
// Production service contract
loadProfile(): Observable<Profile>;

// Component treats the Observable as a Promise-like value
const profile = await service.loadProfile();

// Test double silently changes the contract again
loadProfile: () => Promise.resolve(profileFixture);
```

The test can appear coherent while production has different typing, cancellation, scheduling, and lifetime behavior. Repair it in one of two ways: keep `Observable<Profile>` through the service and consume it with one owned pipeline and teardown policy, or adapt once to `Promise<Profile>` at a named boundary and expose that Promise consistently. In both cases, the test double must implement the production return type exactly and a late-result or cancellation test must observe the chosen policy.

**Bad and borderline outcomes.** Catching every request failure and returning an empty profile makes unavailable, forbidden, missing, and malformed data indistinguishable; the user sees absence instead of a recovery action. A generated client with reproducible schema input is useful, but remains borderline until independent rollout and runtime trust are classified. A repository or global frontend store is similarly conditional: it is justified by observed variation or coordination, not by the fact that the example crosses two frameworks.

| Claim protected by the example | Minimum adapted gate | Expected disconfirming failure |
|---|---|---|
| Backend outcomes remain distinct. | Table-driven application and endpoint tests for every applicable branch and persistent effect. | Removing or merging one mapping fails the corresponding outcome assertion. |
| Unknown bytes do not enter trusted state. | Adapter cases for missing fields, wrong types, unsupported discriminants, and valid variants. | A malformed payload returns a typed parse failure and no partial profile. |
| Conflict preserves user work. | Pure reducer test plus a negative component or browser path. | Replacing conflict with generic failure loses the retained-draft assertion. |
| Async lifetime is coherent. | Compile against the real service type and test unsubscribe, abort, late completion, and teardown as applicable. | A Promise-shaped mock cannot satisfy the Observable contract or the lifetime assertion. |
| Accessibility follows the outcome. | Keyboard, focus, associated error, and live-status checks for at least one corrective and one retryable path. | A visually rendered message without association or announcement fails the accessibility gate. |
| Compatibility assumptions hold. | Supported old/new client-server combinations or documented atomic-deployment proof. | An unsupported discriminant reaches the tolerant external parser and follows the deliberate fallback path. |

These examples demonstrate information preservation, not that the shown syntax compiles under every target. Compile the adapted forms under the repository's actual C# and TypeScript configurations. When the wire vocabulary evolves, internal switches may remain exhaustive after normalization while the external parser deliberately handles a bounded unknown variant; that combination supports strict internal reasoning without crashing older consumers on every additive server change.

## Outcome Metrics and Feedback Loops

Measure whether a full-stack decision improves a named workflow without transferring cost into recovery, compatibility, accessibility, duplicate effects, or operations. Do not use reference length, abstraction count, test count, lines changed, or framework adoption as quality outcomes. Every retained metric must identify the decision it can change, its denominator or pass condition, its owner, and its blind spot.

Begin with a target-project baseline. If none exists, record that absence and collect the first comparable observation; do not invent a percentage or latency target. Invariant gates such as "a stale version never overwrites newer data" can be pass/fail. Distributional claims such as latency or failure incidence require a defined workload, population, window, and comparison.

| Outcome or guardrail | Operational definition | Evidence source | Decision it can trigger | Important blind spot |
|---|---|---|---|---|
| Contract outcome preservation | Every applicable domain outcome maps to one intended transport category and one tested consumer transition. | Table-driven application, endpoint, adapter, and state tests. | Repair a collapsed mapping or remove a distinction that has no different effect. | Passing fixtures can still encode the wrong product contract. |
| Successful workflow completion | Eligible attempts that reach the accepted user outcome, segmented by client and server contract version where relevant. | Bounded product event plus backend effect confirmation. | Continue rollout, investigate a drop, or compare a staged variant. | Completion alone can rise when failures are mislabeled as empty success. |
| Recoverable-input retention | Corrective or retryable failures after which the tested or observed draft remains available. | Reducer, component, browser, and sampled user-report evidence. | Block release or repair state ownership and navigation recovery. | Retention does not prove the recovery instructions are understandable. |
| Correction effectiveness | Validation or conflict recoveries that proceed to an accepted outcome without an unrelated abandonment, using a project-defined window. | Privacy-safe event sequence or usability observation. | Improve error association, conflict choices, or server error shape. | Event sequence cannot explain user intent and should not capture raw input. |
| Duplicate-effect incidence | Repeated persistent effects attributable to one logical operation, not merely repeated HTTP attempts. | Idempotency records, persistence assertions, and incident classification. | Disable automatic retry, add idempotency, or change duplicate-submit handling. | Missing operation identity can make duplicates invisible. |
| Malformed-payload containment | Invalid external payload cases rejected before trusted state or partial rendering. | Adapter tests, safe protocol-failure events, and negative browser paths. | Repair parser coverage, generator drift, or producer compatibility. | No event can mean no malformed payloads or broken instrumentation. |
| Async lifetime integrity | Cancelled or destroyed consumers that do not accept forbidden late results, leak subscriptions, or leave pending state. | Teardown tests, cancellation probes, and bounded runtime diagnostics. | Move the adaptation boundary or fix ownership and cancellation propagation. | Some backend effects cannot be undone after client cancellation. |
| Accessibility recovery gate | Keyboard order, focus, programmatic error association, and status announcement pass for accepted and selected negative paths. | Automated accessibility checks plus targeted manual or assistive-technology review. | Block release or repair template and state-transition behavior. | Automated checks do not establish usability for every user. |
| Compatibility matrix | Supported old/new client-server combinations preserve documented outcomes during the rollout window. | Contract fixtures, deployment simulation, or staged traffic by version. | Stage, adapt, rollback, or postpone contract removal. | Rare cached clients or intermediaries may not appear in the sample. |
| Retry amplification | Downstream attempts per logical operation, segmented by outcome and policy. | Client, gateway, and backend correlation with bounded labels. | Reduce retry budget, add backoff or jitter, or stop retrying a non-transient result. | Aggregation can hide one tenant or operation that is amplifying disproportionately. |
| Diagnostic resolution interval | Time from a detected consequential failure to a classified boundary and owned corrective action. | Incident timeline and correlation coverage. | Add missing outcome telemetry, ownership, or runbook routing. | Faster classification does not prove the fix is correct. |
| Performance distribution | Latency, allocation, payload, or render distribution under a named workload and environment. | Reproducible benchmark or production histogram with version dimensions. | Investigate regression or revise a locally established budget. | Cross-environment numbers are not directly comparable without normalization. |

Use counter-metrics for plausible reclassification. Pair workflow completion with classified rejection and empty-success checks. Pair lower request failures with duplicate-effect incidence and retry amplification. Pair faster rendering with accessibility and state-correctness gates. Pair fewer protocol errors with a synthetic malformed-payload event so silent instrumentation failure cannot masquerade as health.

| Feedback point | Required action | Evidence retained | Response when the signal disagrees |
|---|---|---|---|
| Before design | Characterize current contract, supported versions, workflow outcomes, and known incidents. | Baseline definition, source revision, missing data, and one primary risk. | Narrow the claim or add instrumentation before choosing an irreversible design. |
| During implementation | Run compile, focused outcome, parser, state, and generation gates after the boundary they protect changes. | Command, result, relevant fixture, and changed contract candidate. | Repair locally; do not defer a semantic mismatch to browser testing. |
| Integration and browser | Exercise at least one accepted, one corrective, and one retryable or protocol-failure path with real adapters. | Correlated backend effect and consumer-observable result. | Return to the earliest layer where meanings diverge. |
| Staging or deployment simulation | Exercise supported client/server versions, cancellation timing, retries, migration, and rollback where applicable. | Compatibility matrix, rollout sequence, and unresolved interleaving. | Stage more narrowly, retain compatibility, or postpone removal. |
| Controlled rollout | Compare the project-owned primary outcome and guardrails by contract version or cohort without sensitive labels. | Window, denominator, sampling, config revision, and rollback threshold. | Pause or roll back when a guardrail breaches its locally established threshold. |
| Incident review | Classify the first boundary that lost information and the gate that should have observed it. | Timeline, causal evidence, rejected hypotheses, owner, and regression test. | Update code, test, telemetry, ledger, and routing guidance together. |
| Periodic reference review | Recheck patterns after framework, schema, generator, ownership, deployment, or recurring failure changes. | Freshness record and retained/demoted guidance. | Refresh official evidence when allowed, or keep currentness explicitly unresolved. |

Good metric: the conflict-recovery gate proves no stale write, retained draft, accessible next action, and a bounded conflict category, then a staged rollout watches completion and conflict recurrence by supported contract version. Bad metric: "tests increased by 20" or "requests failed less" with no denominator, outcome semantics, or check for catch-to-empty behavior. Borderline metric: reduced endpoint latency is useful under a stable workload, but does not justify the change if cancellation leaks, payload size, or browser responsiveness worsened.

Metric plumbing needs its own verification. Unit-test event construction and bounded labels, inject one synthetic event to prove the ingestion path, verify the absence path so missing data is not interpreted as zero, and sample incidents against dashboard categories. Correlation identifiers may join frontend and backend observations, but user content, raw validation input, stack traces, and unrestricted identifiers must not become labels.

Observed association is not automatically causality. Record concurrent schema, traffic, deployment, and configuration changes; use a controlled or staged comparison when the decision requires a causal claim. Low-traffic workflows may never produce stable rates, so combine scenario gates, sparse incidents, and structured user evidence without manufacturing statistical certainty.

Feedback must update durable controls. A newly observed failure should produce, when applicable, a clarified outcome contract, a focused regression gate, an owned telemetry category, and a routing or anti-pattern update. Version metric definitions when their semantics change and overlap old and new events during migration so trend continuity is interpretable. Retire a metric when it no longer changes a decision, its boundary disappears, or a stronger direct gate replaces it.

## Completeness Checklist

Choose a completion profile before applying this checklist:

- **Reference integrity** applies when evolving or reviewing this document and its question packet.
- **Implementation handoff** applies when using the reference to change a target .NET and Angular project.
- **Orientation only** applies when the reader is selecting guidance and has not changed code; implementation rows remain outside scope.

For each applicable item, retain `PASS`, `FAIL`, `NOT APPLICABLE` with a causal reason, or `UNRESOLVED` with an owner and bounded consequence. A status without an observation is not completion evidence. A command result belongs to the revision, working directory, configuration, and environment in which it ran.

| Reference integrity item | Completion evidence | Stop or repair condition |
|---|---|---|
| Original structure | Exactly 26 original Markdown headings remain text-identical and ordered against the archive seed. | Any inserted, removed, renamed, or reordered heading requires repair. |
| Per-section expansion | Every evolved section is strictly longer than its matching seed section and adds causal detail rather than repeated filler. | A shorter, equal, duplicated, or inflated-but-empty section fails. |
| Decision packet shape | Exactly 26 packet sections contain the ten spec questions in exact text and order, with all six mandatory fields populated per question. | Missing, renamed, reordered, or malformed packet material fails. |
| Rationale uniqueness | All 1,560 values are exact-text unique and remain unique after the permitted Section/Question context prefix is stripped, whitespace collapsed, and case folded. | Any exact or normalized collision requires rewriting the duplicate values in their specific contexts. |
| Evidence fidelity | Historical observations, local paths, scores, and source limitations remain accurate; no current source is implied when none was refreshed. | Invented provenance, unsupported precision, or current-version authority fails. |
| Source hierarchy | Candidate, legacy, conflicting, negative, and project-policy roles are claim-specific; the sole archive file is not promoted wholesale to canon. | File-level authority that bypasses project and executable evidence requires repair. |
| Decision quality | Defaults include fit conditions, reversal signals, alternatives, counterexamples, uncertainty, and verification proportional to consequence. | Generic confidence language or unexplained prescription fails skeptical review. |
| Artifact coherence | Behavior ledger, examples, metrics, routing, workload, reliability, retry, observability, performance, scale, and evidence boundaries use compatible outcome vocabulary. | Two sections assigning different meanings or recovery to the same outcome require reconciliation. |
| Markdown and text hygiene | Tables have consistent rows, fences close, text is ASCII, trailing whitespace is absent, and forbidden placeholders do not occur. | Any malformed structure, non-ASCII byte, trailing whitespace, or placeholder fails. |
| Verification evidence | Focused verifier, repository verifier, field counts, heading comparison, per-section length comparison, and hygiene scans have current captured results. | A remembered or stale result cannot support final completion. |
| Reread evidence | Complete packet and reference rereads are journaled at least every five sections, including corrections or explicit no-change observations. | A partial scan or unrecorded whole-file claim is insufficient. |
| Scope integrity | Only authorized reference, packet, and Beta journal paths changed; shared specifications, tests, CSVs, archives, and other lanes remain untouched. | Unexpected owned-path drift must be investigated without reverting another agent's work. |

For an applied change, discover the repository before selecting exact commands. Link authoritative code and test output; do not duplicate full schemas or paste detached logs into the checklist.

| Implementation handoff item | Minimum evidence | A valid exclusion requires |
|---|---|---|
| User and system behavior | Accepted and applicable negative outcomes, persistent effects, preserved user work, and recovery actions are named. | Proof that the change is internal and cannot alter observable or boundary behavior. |
| Project fit | Solution, workspace, manifests, endpoint, state owner, schema or client generator, tests, and deploy owners were inspected. | Orientation-only profile with no implementation claim. |
| Backend semantics | Authorization, validation, expected outcomes, unexpected faults, persistence invariants, and cancellation are mapped at owned boundaries. | A named concern that the operation cannot exercise, with the architectural reason. |
| Transport contract | Domain outcomes map once to stable protocol meanings, and sensitive disclosure follows policy. | No transport boundary exists in the changed behavior. |
| Runtime trust | External or independently deployed payloads are parsed before trusted state, or the atomic trust assumption is documented and enforced. | Evidence that producer and consumer are generated, built, and deployed atomically under the accepted threat model. |
| Generated artifacts | Schema owner, frozen input, generator command and version, clean regeneration diff, and drift gate are retained when generation is used. | No generated artifact participates in the change. |
| Frontend state | One owner represents all reachable states; impossible flag combinations, error collapsing, and duplicate truth are absent. | No frontend state or rendered behavior changes. |
| Async lifetime | Observable, Promise, signal, subscription, abort, cancellation, teardown, and late-result policies agree across production and test doubles. | The operation is synchronous and has no cancellable or deferred work. |
| Negative-path experience | At least one corrective and one retryable or protocol-failure path is tested when applicable, with draft retention and deterministic next action. | Threat and consequence analysis shows the category cannot occur. |
| Accessibility | Keyboard order, focus, status announcement, programmatic error association, and contrast or layout are checked for changed states. | No user interface or accessibility tree changes. |
| Duplicate and retry effects | Duplicate submission, idempotency, retry budget, backoff, ambiguous effect, and cancellation interaction are decided. | The operation is effect-free and repeated attempts cannot create load or user-visible inconsistency. |
| Compatibility and rollout | Supported client/server combinations, additive migration, retirement point, staged release, rollback, and persistent-data implications are covered. | A demonstrably atomic deploy with no stored or cached old representation. |
| Observability and privacy | Bounded outcome categories, correlation, safe diagnostics, alert or review action, and absence-path instrumentation checks exist. | A local-only experiment with no production or shared-environment claim. |
| Performance claim | Baseline, workload, environment, distribution, guardrails, and reproducible command support any stated improvement or budget. | No performance claim or changed scale-sensitive path exists. |
| Final evidence | Target build, focused tests, integration or browser gates, generation, compatibility, and operational checks actually run are listed with outcomes. | Only commands outside the selected profile may be excluded. |

Good completion evidence says: the stale-version endpoint test proves no write, the reducer test proves draft retention, the browser path proves accessible reconciliation, and the supported old client handles the response during staged rollout. Bad evidence says only "error handling checked." Borderline evidence says deployment is atomic without naming the owner or control that enforces atomicity.

Exit with one explicit decision:

- **Ready:** all selected items pass and no unresolved risk can invalidate the supported behavior.
- **Conditional handoff:** bounded unresolved work has an owner, consequence, and decision point, and the current claim is narrowed accordingly.
- **Repair required:** a failed item contradicts the behavior, evidence, or authorized structure.
- **Orientation complete:** routing and assumptions are recorded, but no implementation readiness is claimed.

Completion expires selectively. A schema, outcome, generator, state owner, framework surface, deployment topology, workload, or operating policy change reopens the gates that depend on it plus structural invariants. This dependency-based reopening is preferable to carrying old checkmarks forward or rerunning every expensive gate after an unrelated edit.

## Adjacent Reference Routing

Keep this reference primary when one user behavior crosses a .NET backend, an Angular frontend, and TypeScript contracts or state. Route by the responsibility that owns the acceptance test, not by the extension of the first edited file. A companion reference contributes a specialized gate or constraint; it does not create a second behavior contract.

The current local inventory contains no dedicated dotnet-only or angular-only reference. Do not cite an unnamed adjacent file or substitute React lifecycle guidance for Angular. When a specialist reference is absent, inspect the target project, use its tests and conventions, and refresh official framework evidence when the workflow permits browsing.

| Local reference path | Make it primary when | Use it as a companion when | Avoid or return condition |
|---|---|---|---|
| `idiomatic-ref-202607/typescript_language_reliability_patterns-20260710.md` | The change is TypeScript-only and primarily concerns unknown input, discriminated types, async contracts, library boundaries, or compiler reliability. | A full-stack slice needs deeper TypeScript trust, exhaustiveness, or cancellation gates. | Return here when the parser or type decision changes a .NET contract, Angular recovery state, or rollout promise. |
| `idiomatic-ref-202607/frontend_design_quality_patterns-20260710.md` | The behavior contract is stable and the primary work is layout, visual hierarchy, responsive behavior, interaction polish, or accessibility quality. | The Angular workflow needs richer visual and accessibility acceptance checks. | Return here if presentation work changes loading, rejection, retry, empty, conflict, or data semantics. |
| `idiomatic-ref-202607/react_typescript_reliability_patterns-20260710.md` | The actual target is React plus TypeScript rather than Angular. | Only a clearly framework-neutral reliability principle is being compared and will be verified in Angular. | Do not copy React hooks, lifecycle, query, or state APIs into an Angular design; route back when Angular remains the target. |
| `idiomatic-ref-202607/threejs_react_visualization_patterns-20260710.md` | The target truly pivots to a React and Three.js visualization with scene lifecycle and performance concerns. | A separate visualization surface needs a bounded rendering or interaction gate. | Canvas presence alone is insufficient; ordinary Angular UI and non-Three.js rendering remain outside this route. |
| `idiomatic-ref-202607/typescript_backend_reliability_patterns-20260710.md` | The backend is actually Node, Bun, Deno, or a TypeScript worker rather than .NET. | A TypeScript service is an independent consumer or producer in the same contract. | Do not transfer TypeScript backend runtime patterns to C# by analogy; reconcile only the shared protocol here. |
| `idiomatic-ref-202607/mern_typescript_stack_patterns-20260710.md` | The application has pivoted to the MongoDB, Express, React, and Node stack. | A separate MERN consumer participates in a shared contract and needs its own stack gates. | Express or MongoDB source mappings are out of stack for the ordinary .NET and Angular workflow. |
| `idiomatic-ref-202607/system_design_architecture_patterns-20260710.md` | The primary decision is service topology, consistency, messaging, data ownership, or cross-system architecture. | A full-stack feature crosses independently operated services or requires a consequential migration. | Return with the chosen ownership and failure model before defining endpoint and UI mappings here. |
| `idiomatic-ref-202607/executable_specification_skill_patterns-20260710.md` | The main task is turning ambiguous requirements into executable contracts across a broader system. | Outcome vocabulary, traceability, or acceptance criteria need a stronger specification method. | Return after the shared behavior and verification obligations are stable enough to implement. |
| `idiomatic-ref-202607/completion_verification_gate_patterns-20260710.md` | The primary work is designing or auditing a reusable completion gate. | The full-stack change needs stronger evidence-before-completion discipline. | It cannot replace target builds, contract tests, browser checks, or rollout evidence. |
| `idiomatic-ref-202607/systematic_debugging_method_patterns-20260710.md` | An active defect must be reproduced, minimized, hypothesized, and instrumented before architecture changes are justified. | A cross-stack symptom has not yet been localized to backend, transport, runtime adapter, or UI state. | Return with a reproduction and responsible boundary; do not let diagnosis prematurely harden into a design rewrite. |
| `idiomatic-ref-202607/dependency_map_cli_patterns-20260710.md` | The immediate problem is repository orientation and dependency impact rather than pattern selection. | Endpoint, schema, generated artifacts, consumers, and test surfaces must be discovered. | Return once the affected graph and bounded context are known. |

**Routing examples**

- A profile update changes C# outcomes, wire mapping, a generated TypeScript client, Angular state, and independent rollout: keep this reference primary; use TypeScript language and completion-gate references only as companions.
- A stable Angular profile form needs keyboard flow, error placement, responsive layout, and visual polish with no contract change: make frontend design quality primary; return if state semantics change.
- A TypeScript decoder library receives `unknown` and has no .NET or Angular integration change: make TypeScript language reliability primary.
- An Angular component bug is routed to React because both use components: reject the route. Framework-neutral goals can transfer, but lifecycle and state APIs cannot.
- A parser change begins as TypeScript-only but adds an unknown outcome that changes server compatibility and UI recovery: return here and reconcile the behavior ledger.

Before routing, record the user behavior, changed boundary, project evidence, current primary reference, selected companion, expected gate, and reason another plausible route was rejected. After discovery, confirm that the chosen reference can name both the responsibility and a disconfirming test. If it cannot, reroute without discarding useful diagnostic evidence.

For work that crosses owners, pass this minimal handoff:

```text
Behavior identity and outcomes held constant
Authoritative schema, code, and generated-artifact locations
Boundary delegated and responsibility expected back
Evidence already run and observed result
Known failure, compatibility, privacy, and rollout constraints
Open uncertainty with owner and consequence
Return condition and integration gate
```

The companion returns a tested constraint, implementation artifact, or explicit route-away result. The primary owner then integrates it into the shared ledger, tests, telemetry, and rollout assumptions. Close the route when that evidence is reconciled or when project discovery proves the concern independent. Consulting more references is not success by itself; fewer contradictory artifacts and faster localization of the responsible boundary are better routing outcomes.

## Workload Model

The workload model describes the conditions under which a full-stack behavior must remain correct and responsive. It is not endpoint count, lines of code, or one arbitrary number of representative requests. Record observed distributions where available, owner-approved estimates where necessary, and the evidence source for each. Estimates support reversible planning, not production guarantees.

At minimum, characterize these dimensions before making a reliability, performance, retry, or scale claim:

| Workload dimension | Questions to answer | Pattern pressure if the value grows or changes | Evidence candidate |
|---|---|---|---|
| Interaction shape | Is this a foreground read, command, upload, long-running job, poll, subscription, or realtime stream? Does completion outlive the request or browser view? | Changes cancellation, progress, duplicate effects, state lifetime, reconciliation, and whether queueing or push is appropriate. | User-journey trace, route map, job lifecycle, or connection lifecycle. |
| Offered load and concurrency | What are request and logical-operation distributions, burst shape, concurrent users, and concurrent writes to the same key? | Pressures pools, locks, database contention, backpressure, and conflict behavior. | Sanitized production histogram or controlled synthetic schedule. |
| Outcome mix | What proportions are accepted, validation rejected, forbidden, missing, conflict, unavailable, cancelled, and malformed? | Different branches use persistence, serialization, rendering, and retry resources differently. | Bounded outcome events plus endpoint and browser test vectors. |
| Payload and response shape | What are body-size distributions, collection cardinality, field variability, compression, and generated-schema versions? | Pressures parsing, allocation, network transfer, browser memory, rendering, pagination, and compatibility. | Sanitized size histogram, schema fixtures, and browser profile. |
| Persistent effect | Is the operation read-only, idempotent, conditionally idempotent, or non-repeatable? Can commit status be ambiguous? | Determines duplicate-submit controls, idempotency keys, retry safety, and audit requirements. | Persistence invariant, operation identity, and fault-injection result. |
| Contention and consistency | Can two users or processes update the same entity? What version or ordering invariant applies? | Requires conflict detection, compare-and-set semantics, merge, serialization, or an explicit last-write policy. | Concurrent-update test and product-owned conflict rule. |
| Dependency path | Which identity, database, cache, queue, file, or external services participate? What are fan-out, quota, pool, and timeout constraints? | One slow or throttled dependency can dominate latency and trigger retry amplification or partial effects. | Dependency map, configured limits, traces, and failure injection. |
| Deadline and cancellation | Who owns the deadline? When can the user leave? Which work can be cancelled, and which committed effect cannot? | Requires propagation, teardown, late-result policy, and honest UI semantics after cancellation. | Cancellation tests at client, API, application, and dependency boundaries. |
| Client conditions | Which browsers, devices, network qualities, tabs, locales, and assistive technologies are supported? | Changes payload tolerance, rendering budget, offline behavior, focus, and reconnect assumptions. | Support matrix, browser tests, accessibility review, and network simulation. |
| State lifetime | Is state local to one component, shared across views, cached across navigation, persisted offline, or pushed by the server? | Pressures ownership, invalidation, memory, stale data, reconciliation, and global coordination. | Reader/writer map and state-transition tests. |
| Deployment overlap | Are backend, frontend, generated clients, proxies, and caches released atomically? How long can old representations remain? | Requires tolerant parsing, additive schema evolution, migration, version segmentation, and rollback. | Release topology, supported compatibility matrix, and cache lifetime. |
| Data consequence | Is data public, personal, tenant-scoped, regulated, financial, or destructive? What disclosure is permitted? | Raises authorization, validation, audit, privacy, rollback, and test-data requirements even at low traffic. | Threat model, data classification, policy, and security tests. |
| Failure and recovery burst | What happens when a dependency slows, returns, or partially recovers? Do clients synchronize retries? | Reduced capacity plus retries can exceed normal peak demand and duplicate effects. | Fault injection with offered-load, attempt, completion, and queue-depth observations. |
| Growth and seasonality | Which dimensions are expected to change, by what evidence, and at what review trigger? | Determines headroom, staged thresholds, partitioning, and when a local design must be reopened. | Product forecast labeled as estimate plus periodic observed comparison. |

**Baseline interaction profiles**

| Profile | Fits when | Required additions before using this reference's command example | Route or redesign signal |
|---|---|---|---|
| Bounded foreground command | One user action expects one bounded response, payload is constrained, dependencies are few, and the draft can be retained locally. | Explicit outcomes, effect semantics, cancellation timing, duplicate policy, runtime trust, and negative-path UI tests. | Completion outlives the request, payload is large, or the operation cannot expose honest progress. |
| Contention-sensitive command | Several actors can update the same authoritative state. | Version invariant, no-silent-overwrite test, deterministic conflict recovery, and conflict telemetry. | Domain needs merge, ordering, reservation, or serial workflow rather than simple retry. |
| Large collection or transfer | Response or upload size, item count, or render work is material. | Pagination, streaming or chunk policy, cancellation, bounded parsing, partial-failure behavior, and browser memory/render evidence. | A single request cannot meet the locally measured resource or experience budget. |
| Long-running operation | Work continues beyond the useful request deadline. | Durable operation identity, accepted-versus-completed semantics, progress, cancellation limits, idempotency, polling or push, and cleanup. | In-process fire-and-forget work can be lost or duplicated across restart and deployment. |
| Realtime or subscription | Multiple events update client state over a connection. | Ordering, duplicate delivery, gap detection, resynchronization, reconnect backoff, lifetime, and bounded buffering. | Automatic reconnect is the only recovery mechanism or missed events cannot be reconciled. |
| Offline or multi-writer client | Work may be created from stale local state and synchronized later. | Conflict and merge model, durable draft, operation identity, replay safety, schema compatibility, and user-visible reconciliation. | Product semantics cannot define conflict ownership or data-loss policy. |

**Worked workload card: profile update**

This is a hypothetical baseline, not a measured target. The interaction is one foreground command with a server-bounded draft. Identity and one persistence boundary participate. Traffic can be modest while same-record contention remains consequential, so a version conflict is included only if the store and product define a version invariant. The browser preserves the draft on corrective and retryable failures. No automatic retry is allowed until known-no-effect or idempotency is established. Client and server deployment atomicity is unknown, so compatibility remains unresolved rather than assumed. Payload size, concurrency distribution, dependency latency, supported clients, and outcome mix must be measured or owner-estimated before quantitative targets are set.

Good workload evidence says which operations were offered, which completed, which outcomes occurred, which client or server version participated, and what distribution and environment were measured. Bad evidence says "1,000 representative requests" without outcome mix, concurrency schedule, payload distribution, offered load, or generator bottleneck. Average latency alone is borderline because it can hide tails, conflict-heavy paths, cold state, or client rendering cost.

| Workload claim | Verification method | Required record | Disconfirming observation |
|---|---|---|---|
| Concurrent writes preserve the invariant. | Deterministic interleaving or controlled concurrency test against representative persistence semantics. | Initial versions, operation order, effects, and returned outcomes. | Both stale writes commit or the UI cannot reconcile the authoritative result. |
| Retry policy remains bounded during failure. | Fault injection with dependency degradation and recovery. | Logical operations, downstream attempts, backoff, queue or pool pressure, and duplicate effects. | Attempts grow faster than useful completions or recovery creates a synchronized surge. |
| Payload remains within the chosen interaction profile. | Size-distribution fixtures plus parser, network, and browser render profile. | Uncompressed and transferred size, cardinality, parse cost, memory, render responsiveness, and device class. | Tail payload violates a local budget or blocks recovery and cancellation behavior. |
| Client-server overlap is supported. | Compatibility matrix across retained schema and generated-client fixtures. | Version pair, contract outcome, tolerant-parser behavior, and retirement point. | A supported old client collapses or rejects a new outcome without deliberate fallback. |
| Cancellation is honest. | Timed cancellation at each owned boundary. | Whether work stopped, whether an effect committed, late-result handling, and final UI state. | UI says cancelled while an untracked effect commits or a destroyed consumer accepts a late result. |
| Load generator is trustworthy. | Compare offered load, client resource use, server receipt, completion, and error counts. | Generator configuration and its own CPU, memory, connection, and timeout limits. | The client harness saturates before the system and produces a false capacity boundary. |

Sanitize production-derived distributions and build synthetic fixtures; do not replay personal payloads. Report warm and steady state separately when startup, caches, connection pools, compilation, or browser initialization matter. Measure backend service time and client network, parse, state, and render contributions separately while retaining the end-to-end user interval.

Refresh this workload card when interaction shape, schema, dependency path, retry policy, supported clients, deployment overlap, data classification, or a leading distribution changes. Monitor the dimensions tied to credible failure modes rather than remeasuring everything continuously. The first violated assumption that changes correctness or ownership is the meaningful scale boundary; a past maximum throughput number is not.

## Reliability Target

Reliability means the workflow preserves authorization, effect, outcome, runtime trust, recoverability, compatibility, and diagnosability under its declared workload and failure model. Availability and speed are important, but they cannot compensate for silent overwrite, duplicate effects, unauthorized access, malformed data entering trusted state, or a UI that reports success when the effect is unknown.

Separate three kinds of target:

- **Invariant:** a scoped behavior that must hold for every tested operation under a named model, such as no stale write silently overwrites a newer version.
- **Measured objective:** a project-owned distributional target such as task completion, availability, or latency over a defined population and window.
- **Recovery objective:** a maximum tolerable interruption, data loss, compatibility window, or manual intervention for a named consequence.

This reference supplies target categories and evidence methods, not universal percentages, latency budgets, recovery times, or error budgets. Product and operations owners set those values from consequence, support commitments, baseline distributions, dependency limits, and cost.

| Reliability target | Scoped contract | Evidence that can disconfirm it | Breach or degradation response |
|---|---|---|---|
| Authorization integrity | An identity cannot cause or observe an effect outside the project's policy, including through retries, alternate routes, or stale clients. | Direct endpoint probes, policy tests, tenant-boundary cases, and safe disclosure checks. | Fail closed for the protected operation, preserve safe user state, alert the owner, and avoid leaking existence or details. |
| Validation authority | Invalid input cannot commit merely because client validation was bypassed; mirrored client checks remain advisory. | Submit invalid requests outside the UI and assert no effect plus stable correction semantics. | Reject with actionable safe data, retain the draft, and repair any client/server rule drift. |
| Persistence integrity | Accepted means the intended effect committed under the declared consistency model; stale data does not overwrite silently when a version invariant exists. | Transaction, concurrency, and post-effect tests against representative persistence semantics. | Stop or reconcile the write path, surface conflict honestly, and investigate affected records. |
| Duplicate-effect control | One logical operation cannot create unintended repeated effects under duplicate click, timeout, retry, or replay. | Idempotency, duplicate-submission, ambiguous-commit, and retry fault-injection tests. | Disable unsafe automatic retry, reconcile operation identity, and repair or compensate according to domain policy. |
| Outcome integrity | Validation, forbidden, missing, conflict, unavailable, malformed, cancelled, and accepted states remain distinguishable wherever recovery or effect differs. | Exhaustive domain-to-transport mapping and consumer state-transition tests. | Return to the first collapsed boundary; never hide the breach by mapping it to empty or accepted. |
| Runtime trust | Data from an untrusted or independently deployed producer cannot enter trusted TypeScript state until its supported wire shape is validated. | Missing, wrong-type, extra, stale-version, and unknown-discriminant adapter cases. | Contain partial data, preserve user work, emit safe diagnostics, and follow the deliberate compatibility fallback. |
| Draft recoverability | Corrective and retryable failures retain user input unless a documented security or product rule forbids it. | Reducer, component, navigation, refresh, and negative browser-path tests. | Prevent destructive transition, offer a deterministic next action, and investigate state ownership. |
| Async lifetime integrity | Cancellation, teardown, deadline, and late completion follow one declared policy across service, component, backend, and test double. | Real return-type compilation, abort or unsubscribe tests, timed cancellation, and destroyed-view cases. | Ignore or reconcile forbidden late results, stop leaks, and communicate honestly when a backend effect cannot be cancelled. |
| Accessibility recovery | Changed accepted and failure states remain keyboard reachable, programmatically associated, focus coherent, and announced when needed. | Automated checks plus targeted manual or assistive-technology paths for selected outcomes. | Block or roll back the affected experience when the user cannot perceive or act on a consequential state. |
| Compatibility integrity | Every supported client-server-schema combination preserves documented outcome semantics during the rollout window. | Contract fixtures, generated-client regeneration, version-pair matrix, cache and proxy cases, and rollback simulation. | Stage more narrowly, retain additive compatibility, roll back, or delay removal until the retirement condition holds. |
| Availability objective | Eligible logical operations receive a truthful accepted or actionable non-success outcome within the project-owned objective. | End-to-end observations segmented by logical operation and contract version, with instrumentation absence checks. | Degrade optional work, shed load deliberately, stop retry amplification, or roll back under the owned threshold. |
| Responsiveness objective | Backend, network, parse, state, and render intervals stay within locally established distributions for the declared workload. | Reproducible benchmark, production histogram, and browser profile with guardrails. | Localize the budget breach before optimizing and preserve correctness, accessibility, and resource bounds. |
| Diagnosability | A consequential user-visible failure can be correlated to a bounded backend outcome and owning boundary without sensitive payload labels. | Synthetic event, incident sampling, trace or correlation checks, dashboard absence test, and runbook exercise. | Restore signal integrity, narrow unsafe logging, and update ownership and regression evidence. |
| Rollback and reconciliation | A release can be stopped or reversed without violating stored data, schema compatibility, generated clients, or user work; irreversible effects have a forward-repair plan. | Deployment simulation, migration check, old/new matrix, rollback rehearsal, and data reconciliation test. | Halt expansion, invoke the owned rollback or forward repair, and retain evidence of affected versions and data. |

**How to set measured objectives**

1. Name the user promise and the logical-operation denominator; do not count retries as independent successes.
2. State the workload, outcome mix, supported clients, data consequence, dependency path, and deployment overlap.
3. Establish a baseline distribution and its collection quality. Mark missing or sparse evidence rather than filling it with a guess.
4. Choose a project-owned objective and guardrails based on consequence and operating cost. Record the owner and review window.
5. Define alert, degradation, stage, rollback, and escalation actions before the threshold is breached.
6. Test instrumentation with a synthetic event and an absence case so silent collection failure is distinguishable from a healthy zero.
7. Review after an incident, dependency or topology change, compatibility-window change, or workload-boundary violation.

**Worked target for the profile-update behavior**

The invariant is that stale input never silently overwrites a newer version when the target store uses optimistic concurrency. A deterministic concurrent-update test establishes the server effect, a contract test establishes the conflict mapping, and a browser test establishes retained draft plus accessible reconciliation. The measured objective for completion and the acceptable conflict incidence remain project-owned because this reference has no traffic or product baseline. During an availability breach, the interface may disable optional refresh or present an unavailable state, but it must not claim acceptance or blind-retry an operation with uncertain effect.

Good: "Under the declared version model, a stale update produces no write, returns the supported conflict outcome, retains the draft, and offers a tested reconciliation action; these four gates block release." Bad: "The profile service is highly available and resilient." Borderline: "Retries eventually succeed" without logical-operation identity, known effect semantics, bounded attempts, and duplicate-write evidence.

Fail-open versus fail-closed is policy and consequence dependent. Authorization, tenant isolation, and persistent invariants normally require failure that preserves protection; an optional recommendation panel may disappear while the core edit remains available. Queueing can improve request availability for long work but introduces durable operation identity, progress, duplicate, cancellation, cleanup, and delayed-failure obligations. Compatibility can be shortened to accelerate cleanup only when supported consumers and caches have crossed a documented retirement point.

Exercise declared degradation before relying on it. Induce unavailable dependencies, slow responses, malformed payloads, cancellation races, version skew, and rollback in proportion to consequence. Confirm the backend effect, transport result, frontend state, accessible message, telemetry category, and recovery action together. Pre-release tests establish scoped invariants; staged and production observations establish distributional objectives under real traffic.

Reference reliability remains a separate editorial gate: historical, external, project, and inferred claims must remain distinguishable, unsupported precision must be removed, and routing must name a next action. Those qualities help engineers choose reliable behavior, but they are not evidence that a deployed workflow meets an SLO.

## Failure Mode Table

Treat each row as a testable incident hypothesis, not a diagnosis. Start from the user-visible symptom and persistent effect, then find the earliest boundary at which intended meaning diverged from observed meaning. Immediate containment may reduce availability; durable correction must restore the contract and add evidence that would have failed before the fix.

| Failure mode and trigger | User or data consequence | Earliest useful signal | Immediate containment | Durable correction | Regression evidence |
|---|---|---|---|---|---|
| Authorization bypass or unsafe disclosure: policy is absent, applied after data access, or differs across routes. | Unauthorized effect, cross-tenant exposure, or leaked resource existence. | Identity, policy decision, route, tenant, and effect audit disagree. | Disable or fail closed for the affected operation under incident policy; preserve evidence without exposing payloads. | Centralize the owned policy boundary, minimize disclosure, and review alternate routes and retries. | Direct endpoint abuse cases, tenant isolation, forbidden mapping, and safe UI recovery. |
| Client/server validation drift: duplicated rule changes in one layer only. | UI accepts a request the server rejects, blocks a valid request, or gives conflicting correction. | Same fixture produces different decisions at client and server. | Keep server authority; show a safe form-level fallback and retain input. | Share schema where appropriate or deliberately map the stable mirrored subset with ownership. | Submit fixtures both through and around the UI; assert no invalid write. |
| Expected outcomes collapse: exceptions, generic errors, or mapping defaults erase validation, missing, conflict, or unavailable distinctions. | User receives the wrong next action; telemetry and retry policy misclassify the effect. | Backend outcome differs while transport or UI state remains identical. | Disable unsafe retry and present a conservative recoverable state. | Restore explicit domain outcomes and one exhaustive transport and adapter mapping. | Table-driven outcome, endpoint, parser, reducer, and negative browser cases. |
| Stale overwrite: concurrent writes lack a version invariant or the version is ignored. | Newer data is silently lost and a false success is displayed. | Persistence history shows a stale write committed after a newer version. | Pause the write path or require refresh for the affected operation. | Implement the product-owned ordering, compare-and-set, merge, or last-write policy explicitly. | Deterministic concurrent interleaving and conflict-recovery browser test. |
| Duplicate effect: duplicate click, timeout, replay, or retry repeats a non-repeatable write. | Repeated charge, message, record, or side effect despite one logical user action. | Multiple effects share one correlation or can be linked to the same logical intent. | Stop retries and reconcile by operation identity; repair or compensate under domain policy. | Add idempotency or a durable duplicate policy at the authoritative effect boundary. | Fault injection around commit and response loss, plus repeated-request persistence assertions. |
| Ambiguous commit is treated as known failure: response is lost after an effect may have committed. | Blind retry can duplicate work; UI can claim failure after success. | Dependency or server evidence cannot determine effect from request result alone. | Present an honest pending or reconciliation state and prevent blind replay. | Add operation lookup, idempotency, transactional outbox, or domain-specific reconciliation as justified. | Cut connection at commit boundaries and assert final effect and recovery behavior. |
| Generated contract drift: schema input, command, or generated output differs across owners. | Compile break, silent field mismatch, or old consumer misinterpretation. | Clean regeneration changes checked-in output or source schema cannot be identified. | Freeze rollout and restore the last compatible artifact set. | Own schema and generator versions, regenerate reproducibly, and gate drift. | Clean-tree generation diff, compile, contract fixtures, and supported version matrix. |
| Type assertion bypasses runtime trust: external bytes are cast to a TypeScript interface. | Partial or hostile data enters trusted state and can render incorrectly or break recovery. | Malformed fixture passes the adapter or failure appears deep in a component. | Contain untrusted data, retain user work, and show a safe protocol-failure state. | Parse at the external boundary and normalize supported wire variants before domain use. | Missing, wrong-type, extra, stale, and unknown-discriminant parser cases. |
| Unsupported new outcome reaches an old consumer. | Client crashes, loops, or maps a new server state to generic success or empty. | Version-segmented protocol failures rise after server rollout. | Stage or roll back; use the deliberate unknown fallback where supported. | Evolve additively, preserve tolerant external parsing, and define retirement. | Old/new client-server fixtures, cache cases, and unknown-variant browser behavior. |

| Failure mode and trigger | User or data consequence | Earliest useful signal | Immediate containment | Durable correction | Regression evidence |
|---|---|---|---|---|---|
| Observable/Promise contract mismatch: production returns a stream, component awaits it, and test double returns a Promise. | Scheduling, cancellation, typing, and lifetime differ between test and production. | Real service type and mock type disagree or a value is still an Observable after `await`. | Disable the broken path or adapt once at the integration boundary. | Choose one exposed async model, preserve its lifetime semantics, and make doubles exact. | Compile with real types; cancellation, teardown, late-result, and mock-contract tests. |
| Subscription or listener leak: teardown ownership is absent or repeated navigation adds consumers. | Duplicate requests, repeated updates, memory growth, and stale views. | Subscriber, listener, or request count increases after create-destroy cycles. | Stop or isolate the leaking feature and cap harmful fan-out if needed. | Give one owner the lifetime and use project-supported teardown mechanisms. | Repeated mount-destroy test with subscriber, request, and late-update assertions. |
| Late result overwrites newer state: requests race and completion order differs from intent order. | User sees data from an older selection or draft after choosing a newer one. | Request identity and state-transition chronology show stale completion accepted. | Ignore results not owned by the current intent; preserve current draft. | Cancel, switch, sequence, or compare request identity at one state boundary. | Controlled out-of-order completion test. |
| Split state creates impossible combinations: several booleans and caches represent one workflow. | Loading, error, empty, success, and conflict can appear together or flicker. | State snapshot violates the reachable transition graph. | Render a conservative state and stop duplicate writers. | Use one discriminated state owner and derived values. | Pure transition tests including invalid-order events. |
| Catch-to-empty hides failure: adapter or service converts any error to an empty profile or collection. | Unavailable, forbidden, malformed, and genuinely empty become indistinguishable. | Backend failure coincides with an empty-success UI and no failure category. | Stop destructive empty-state actions and expose a recoverable failure. | Preserve typed outcomes through adapter and presentation mapping. | Fault each backend category and assert it never reaches empty success. |
| Cancellation is dishonest: UI says cancelled while work continues or committed effect is unknown. | User retries or leaves under a false belief, causing duplicate or surprising effects. | Client cancellation and backend effect timeline disagree. | Prevent replay, show reconciliation where effect is uncertain, and preserve operation identity. | Propagate cancellation where possible and document the irreversible boundary. | Timed cancellation before, during, and after commit. |
| Error recovery is inaccessible: visual message lacks focus, association, announcement, or keyboard action. | Some users cannot perceive or correct a consequential failure. | Automated or manual accessibility path cannot locate or act on the state. | Block affected release or provide an accessible fallback path. | Tie presentation semantics to state transitions and verify selected negative outcomes. | Keyboard, focus, label, description, status, and assistive-technology checks. |
| Reconnect assumes replay: connection returns but missed or duplicate events are not reconciled. | Client state silently diverges from server state. | Sequence gap, stale version, or duplicate event appears after reconnect. | Force a snapshot refresh or mark state stale until reconciled. | Add cursor, sequence, idempotent event handling, gap detection, and bounded backoff. | Disconnect during updates, reconnect, and compare final authoritative state. |
| Cache invalidation misses a write or contract version. | Views disagree, stale schema persists, or rollback serves incompatible data. | Cache version and authoritative state differ after update or deployment. | Bypass or purge the affected cache under owned controls. | Define keys, versions, invalidation owner, lifetime, and compatibility policy. | Write-read, multi-view, old/new schema, expiry, and rollback tests. |
| Payload or render tail is unbounded. | Browser freezes, memory spikes, request times out, or cancellation cannot recover. | Tail item count, size, parse, memory, or render interval exceeds local envelope. | Limit result, disable expensive rendering, or fall back to bounded pagination. | Enforce server bounds, stream or paginate deliberately, virtualize where justified, and test cancellation. | Tail-distribution fixtures and browser profiles on supported device classes. |

| Failure mode and trigger | User or data consequence | Earliest useful signal | Immediate containment | Durable correction | Regression evidence |
|---|---|---|---|---|---|
| Retry amplification during dependency degradation. | Reduced capacity receives more attempts, latency rises, queues grow, and effects may duplicate. | Attempts per logical operation and pool or queue pressure rise while useful completion falls. | Stop or sharply bound retries, shed optional load, and protect the dependency. | Classify transient outcomes, budget attempts, add backoff and jitter, honor retry hints, and use idempotency. | Fault injection through degradation and recovery with offered-load and completion observations. |
| Pool or dependency saturation: concurrency exceeds database, HTTP, thread, or browser resource bounds. | Requests stall, time out, cascade, or leave UI pending. | Queue time and pool occupancy dominate service time before CPU or business work. | Bound admission, cancel abandoned work, and degrade optional fan-out. | Align concurrency with measured capacity, shorten held resources, and add backpressure. | Controlled concurrency ramp with queue, pool, timeout, and cancellation data. |
| Partial dependency failure is mapped as complete success. | Missing fields or side effects are accepted without product-approved degradation. | Downstream failure exists while response lacks partial or unavailable semantics. | Disable the misleading composite result and surface bounded degradation. | Define atomicity or partial-success contract and compensation ownership. | Fault each dependency and assert effect, response, and UI agree. |
| Migration and rollback are incompatible. | Old code reads new data incorrectly, rollback fails, or generated clients strand users. | Version-pair or rollback rehearsal fails before or during rollout. | Halt expansion and choose the owned forward-repair or rollback path. | Use compatible staged migration, expand-contract sequencing, and explicit retirement. | Old/new application-data-client matrix and rollback simulation. |
| Telemetry is absent, high cardinality, or sensitive. | Incidents cannot be localized, cost grows, or user data leaks through labels and logs. | Synthetic event is missing, labels grow without bound, or payload content appears. | Disable unsafe fields, restore bounded signal, and preserve minimum incident evidence. | Define outcome vocabulary, privacy review, sampling, correlation, and cardinality budgets. | Event-schema tests, synthetic ingestion, absence check, and label scan. |
| Test double implements a different contract. | Suite passes a Promise, status, payload, timing, or error shape production never provides. | Interface comparison or integration test exposes divergent behavior. | Stop relying on the misleading test result for release. | Share contract fixtures, enforce interfaces, and include a real-adapter test. | Mutation or contract test that fails when production and double return shapes diverge. |
| Source or framework guidance drifts. | Agent copies obsolete APIs, version claims, or conventions into a current project. | Target compilation or official refresh contradicts historical prose. | Narrow the claim, mark currentness unresolved, and follow project evidence. | Refresh authoritative sources when allowed and retain version-sensitive boundaries. | Manifest-specific compile and evidence review with a freshness trigger. |
| Generic best practice escapes review. | Extra layers, stores, retries, or naming rules appear without a responsibility or failure case. | Simpler candidate passes the same gates and the abstraction has no owner. | Stop expansion and preserve the working baseline. | Require behavior, alternative, consequence, and disconfirming gate in the decision ledger. | Reviewer can remove the mechanism and observe whether any relevant test fails. |
| Unsupported performance precision drives design. | Team optimizes for a threshold with no baseline, harness, environment, or workload. | Claimed number cannot be reproduced or changes with the generator or setup. | Withdraw the claim and avoid irreversible optimization. | Establish local distribution, guardrails, provenance, and repeatable measurement. | Independent rerun under recorded conditions plus correctness and accessibility guardrails. |

**Triage and learning sequence**

1. Protect identities, data, and irreversible effects; apply incident policy and label temporary containment.
2. Identify the logical operation, client and server versions, intended outcomes, and whether the effect committed, did not commit, or is unknown.
3. Correlate backend outcome, transport response, runtime adapter result, frontend transition, and user symptom without copying sensitive payloads.
4. Find the earliest divergence and write competing hypotheses, especially when retries, dependencies, caches, or deployments interact.
5. Reproduce or instrument the smallest consequential path; do not select architecture from the surface symptom alone.
6. Correct the owning boundary, run a gate that fails on the old behavior, and verify containment can be removed.
7. Update only the disproved assumptions in the behavior ledger, workload, reliability targets, retry policy, observability, routing, and reference guidance.

A button disable is useful experience protection but is not system-wide duplicate-effect prevention. Automatic reconnect restores a connection but not necessarily missed state. A successful retry proves neither no duplicate effect nor healthy backpressure. These borderline mitigations become sufficient only when the operation and workload model rule out the omitted consequence.

Retire a failure row from an applied checklist when its triggering architecture no longer exists or policy makes it impossible, and retain the reason. When several incidents show different surface symptoms but share one collapsed discriminant or missing identity, repair that shared boundary instead of accumulating local catches.

## Retry Backpressure Guidance

Retry only when another attempt is semantically safe, has a credible chance of success, fits the remaining deadline, and does not violate capacity policy. Safety is about repeated effects; usefulness is about failure classification and capacity. Both must hold. Count budgets per logical operation across the browser, gateway, service, SDK, database, and message infrastructure so independent defaults cannot multiply invisibly.

**Outcome classification**

| Observed outcome | Automatic retry default | Required reasoning before another attempt | User-facing and operational behavior |
|---|---|---|---|
| Accepted | Never. | Confirm the effect once and stop the operation. | Exit pending state and suppress late duplicate responses. |
| Validation rejected | No. | User or caller must provide corrected input; server rules remain authoritative. | Preserve draft, associate correction, and do not consume retry capacity. |
| Forbidden | No. | Identity or policy must change through an authorized path. | Present safe denial or navigation; avoid probing and sensitive detail. |
| Missing | No blind retry. | A later attempt is a new decision only when creation, replication, or refresh semantics make appearance plausible. | Offer refresh or navigation under product policy, not a tight loop. |
| Version conflict | No blind retry. | Refresh or reconcile intent and use a fresh version; the resubmission is deliberate. | Preserve the draft and expose the tested conflict action. |
| Malformed or unsupported payload | No. | Repair producer, schema, generation, compatibility, or parser policy. | Contain untrusted data and emit bounded protocol diagnostics. |
| Cancelled or obsolete intent | No. | A new user intent creates a new logical operation. | Stop pending state and ignore forbidden late results. |
| Rate limited or server-directed wait | Conditional. | Operation must be safe, a retry hint must be valid, time must remain, and the shared budget must permit it. | Explain delay when visible; honor cancellation and avoid synchronized wake-up. |
| Known transient unavailable with no effect | Conditional. | Idempotent or effect-free operation, classified transient cause, capacity headroom, and remaining deadline are required. | Use bounded delayed retry or let the user retry according to workflow consequence. |
| Timeout or connection loss with unknown effect | No blind replay. | Resolve by operation identity, idempotency lookup, or domain reconciliation first. | Show honest pending or unknown state and prevent accidental duplicate work. |
| Dependency partial failure | Contract dependent. | Retry only the safely repeatable missing work when partial effects and compensation are defined. | Do not represent partial completion as whole success. |

A corrected validation submission, refreshed conflict resubmission, or new post-cancellation intent is not merely another transport attempt. It is a new logical decision and should receive a new operation identity or explicit relationship to the prior one.

**One retry envelope per logical operation**

| Envelope field | Completion rule | Failure prevented |
|---|---|---|
| Logical identity | Correlate all attempts and effects without using user content as an identifier. | Duplicate effects and misleading per-request success metrics. |
| Classification owner | Name the boundary that decides transient, semantic, throttled, malformed, cancelled, or unknown-effect. | Different layers retrying the same failure for conflicting reasons. |
| Attempt budget | Bound total downstream attempts across all layers and state whether hedging or failover consumes the same budget. | Multiplicative retries and hidden load. |
| Time budget | Derive each attempt and delay from the remaining end-to-end deadline, including cleanup and UI usefulness. | Work that continues after the result can no longer help. |
| Effect safety | Establish read-only, idempotency, operation lookup, known-no-effect, or explicit reconciliation. | Repeated irreversible work after timeout or replay. |
| Delay policy | Prefer valid server hints; otherwise use a bounded project-owned backoff with jitter and a cap. | Synchronized retries and unbounded recovery delay. |
| Cancellation | Make delay and attempt cancellable, propagate where supported, and define the irreversible effect boundary. | Abandoned work, leaks, and dishonest cancelled state. |
| Capacity gate | Refuse or defer another attempt when queues, pools, circuit state, tenant policy, or dependency health say it would worsen overload. | Retry storms during reduced capacity. |
| Observability | Record logical operations, attempts, outcome, delay reason, budget exhaustion, and duplicate effect with bounded dimensions. | Inability to distinguish useful retry from amplification. |
| Ownership and configuration | Name the policy owner, configuration source, rollout, rollback, and review trigger. | Stale magic values and conflicting library defaults. |

Do not copy a universal attempt count, exponential factor, delay cap, queue size, timeout, or circuit threshold from this reference. Derive parameters from dependency contracts, observed latency and recovery, logical-operation consequence, capacity, and user deadline. Start conservatively, expose configuration safely, stage changes, and tune from measured attempts per useful completion rather than raw request success.

**Angular concurrency semantics**

Common RxJS operators express different product policies; compile and test the target project's supported APIs rather than selecting one by habit.

| Interaction intent | Semantic policy | Common operator shape | Failure if chosen incorrectly |
|---|---|---|---|
| Latest search or selection wins | Cancel or ignore obsolete inner work when a newer intent arrives. | Switching to the latest stream, commonly `switchMap`. | Older completion can overwrite newer state if cancellation or identity is absent. |
| Ignore duplicate submit while one is active | Admit the first and reject overlapping intents until completion. | Exhausting concurrent submissions, commonly `exhaustMap`. | Legitimate replacement intent may be ignored if the workflow actually needs latest-wins. |
| Preserve ordered commands | Queue bounded work and process in order. | Concatenating operations, commonly `concatMap`. | Unbounded input creates a growing queue and stale work. |
| Run independent reads concurrently | Permit bounded concurrency and reconcile results independently. | Merging operations, commonly `mergeMap` with an owned concurrency policy. | Shared-state writes race or capacity is exceeded. |

Client-side suppression improves experience but is not authoritative idempotency. Other callers, browser retries, proxies, gateways, and response loss can still repeat a write. Likewise, debouncing reduces offered interactions but does not classify failures or establish effect safety.

**Backpressure choices**

- Bound concurrent work at the boundary that owns the constrained resource. Align admission with database, HTTP, thread, queue, and downstream quotas rather than allowing every request to wait indefinitely.
- Use bounded queues only for work that can wait. Define capacity, ordering, fairness, expiry, cancellation, persistence, restart, and full-queue behavior. Queueing moves latency and ownership; it does not create capacity.
- Shed optional or low-priority work before weakening authorization, persistence truth, or critical recovery. Make priority and tenant fairness explicit where callers compete.
- Use circuit breaking only around a dependency and failure class for which fast failure protects capacity. Define half-open probes and user semantics; an open circuit is not a successful response.
- Honor server or provider retry hints when trustworthy, but still apply local deadline, budget, jitter, and cancellation. Reject hints that exceed useful time or policy.
- For polling, increase intervals or stop when the operation reaches a terminal state, the view is destroyed, the deadline expires, or visibility policy says work is no longer useful.
- For realtime reconnect, use bounded delay and jitter plus gap detection, duplicate handling, and snapshot reconciliation. Re-establishing a socket does not recover missed state.

**Verification under degradation and recovery**

| Scenario | Observe together | Unsafe result |
|---|---|---|
| Dependency slows then recovers. | Offered logical operations, downstream attempts, queue or pool pressure, completion, delay, and cancellation. | Attempts rise while useful completion falls, or recovery creates a synchronized surge. |
| Response is lost after commit. | Operation identity, effect count, client state, reconciliation, and subsequent attempt. | Blind replay duplicates the effect or UI reports a known failure without checking. |
| User changes selection rapidly. | Request identity, cancellation, completion order, state transition, and teardown. | Obsolete result replaces current state or abandoned work leaks. |
| Many users submit concurrently. | Admission, fairness, conflict outcomes, pool occupancy, latency distribution, and duplicate effects. | Unbounded waiting, tenant starvation, silent overwrite, or retry multiplication. |
| Queue reaches capacity. | Rejection or deferral semantics, expiry, memory, producer rate, consumer rate, and user feedback. | Queue grows without bound or accepted work is later discarded invisibly. |
| Realtime connection flaps. | Reconnect attempts, jitter, sequence gaps, duplicate events, snapshot reconciliation, and final state. | Connected status is green while client data remains stale. |

Run these tests in isolated or approved capacity with explicit stop conditions; a load generator can become the incident. Validate the generator by comparing offered work, server receipt, completed logical operations, errors, and the generator's own CPU, memory, connections, and timeout behavior.

The original workflow safeguards still apply when evolving this reference: classify a failed evidence signal before retrying source retrieval, stop new section work while structural or uniqueness gates are red, checkpoint durable progress, preserve one owner per file, and never use retries to overwrite another lane or bypass an authorization boundary. Those process controls are analogous to application backpressure, but they are not evidence that a deployed retry policy is safe.

## Observability Checklist

Build observability around the logical user operation and the bounded outcome vocabulary used by the contract. A browser event, transport attempt, backend outcome, dependency span, and persistent effect should be correlatable without copying user content. Tool selection is project-owned; this checklist defines semantics and verification that logs, metrics, traces, audits, and frontend events must preserve.

**Minimum cross-stack signal model**

| Signal concept | Required meaning | Safe bounded dimensions | Do not use as an ordinary dimension |
|---|---|---|---|
| Logical operation | One user or system intent across all retries, redirects, and participating services. | Operation kind, bounded outcome, client and contract version, retry class. | Email, name, raw route with identifiers, request body, validation input, or stack trace. |
| Attempt | One transport or dependency attempt belonging to the logical operation. | Attempt ordinal, layer, result class, delay reason, budget exhausted, cancellation. | Unbounded URL, SQL text, serialized exception, or third-party response body. |
| Contract outcome | Accepted, validation rejected, forbidden, missing, conflict, unavailable, malformed, cancelled, or a project-owned extension. | Stable outcome name, effect-known status, protocol version, endpoint template. | Free-form message or user-facing copy as a metric label. |
| Persistent effect | Whether the intended effect committed, did not commit, is partial, or remains unknown under the operation model. | Effect class, idempotency result, conflict class, storage boundary. | Entity contents, raw keys, or tenant-identifying values without approved protection. |
| Runtime trust result | Whether external payload normalization accepted, rejected, or used a deliberate compatibility fallback. | Parser or schema version, bounded failure category, producer class. | Entire malformed payload or arbitrary field path with unbounded values. |
| Frontend recovery | Which trusted state and next-action category the user received. | Saved, correction, denial, refresh, reconcile, retry, protocol failure, cancellation. | Draft contents, field values, or raw accessibility-tree text. |
| Dependency pressure | Time, result, pool or queue pressure, retry, and circuit state for a named dependency class. | Dependency role, operation class, result class, bounded saturation bucket. | Hostnames or tenant identifiers when they create high cardinality or disclosure. |
| Deployment context | The code and contract representations participating in the operation. | Service version, client build, schema or generated-client version, rollout cohort. | Full commit metadata or arbitrary feature-flag maps on every event. |

Use an opaque, scoped operation identifier to join evidence. It should not encode personal data, resource identifiers, or secrets, and it should have retention appropriate to diagnosis. Attempt identity is separate so repeated calls can be counted without treating retries as new user demand. When the effect is unknown, emit that state explicitly rather than inferring failure from a missing response.

**Choose the signal for the question**

| Question | Primary mechanism | Supporting mechanism | Limitation to record |
|---|---|---|---|
| How often does each logical outcome occur? | Counter or product event per logical operation with a defined denominator. | Sampled backend log for classification detail. | Client events may be blocked or offline; backend events may not know the final user recovery. |
| Where is latency spent? | Trace or separately measured backend, network, parse, state, and render intervals. | Histograms for stable distributions. | Sampling, clock alignment, and missing client spans affect attribution. |
| Did a write duplicate or conflict? | Authoritative persistence or audit evidence keyed by operation identity. | Backend outcome metric and incident trace. | Request count alone cannot establish effect count. |
| Are retries helping or amplifying? | Logical operations, attempts, useful completions, duplicate effects, queue or pool pressure, and delay distributions. | Dependency traces and circuit state. | Per-request success can improve while user completion and capacity worsen. |
| Did a malformed payload reach trusted state? | Adapter failure event plus parser and state regression tests. | Safe trace link to producer and contract version. | No event may mean no malformed input or broken instrumentation. |
| Can a user recover from a failure? | Bounded frontend recovery event plus browser and accessibility evidence. | Backend outcome correlation. | Telemetry cannot establish comprehension or assistive-technology usability alone. |
| Is a rollout compatible? | Outcome and parser failures segmented by supported client, server, and contract versions. | Compatibility test matrix and rollback rehearsal. | Rare cached or offline clients can be absent from the observed cohort. |
| What should an operator do? | Alert or review rule tied to a runbook decision and owner. | Dashboard showing primary outcome and guardrails. | A threshold without an action creates noise rather than operability. |

**Metric definition gate**

Before using a count, rate, percentile, or histogram, record:

- the logical event and whether it is per operation, attempt, user, effect, or time interval;
- population, eligibility, exclusions, denominator, unit, aggregation window, and timezone;
- source, instrumentation version, sampling, expected delay, and missing-data semantics;
- bounded dimensions and their cardinality budget;
- baseline, locally owned objective or review threshold, and guardrail;
- dashboard or query owner, consumer, action, rollback or escalation path, and retirement trigger.

Record p50, p95, p99, or another quantile only when the sample count, distribution, unit, window, workload, and collection path make that statistic useful. A percentile copied without these conditions is decoration. For sparse high-consequence failures, deterministic invariant tests and incident classification may be more informative than a tail estimate.

**Logging and trace checks**

- Use structured fields with stable meanings; free-form messages support reading but should not be the only query surface.
- Log boundary decisions and safe categories, not full request or response bodies. Redact before emission rather than relying only on downstream cleanup.
- Preserve unexpected fault identity and stack detail in approved restricted channels; do not expose it to users or metric labels.
- Propagate trace and operation context across supported async and dependency boundaries, but validate incoming context and prevent unbounded baggage.
- Mark retries and fallbacks as events on the original logical operation. A fallback success should not erase the degraded dependency signal.
- Record cancellation source and whether the effect could still commit. Client abandonment and server failure are different outcomes.
- Include schema or generated-client version when independent deployment can change interpretation.
- Bound span and event volume for loops, streams, and large collections; aggregate repeated low-value details while preserving error exemplars.

**Frontend and accessibility checks**

- Emit after the trusted state transition, not before, so the event describes what the user actually received.
- Avoid one event per keystroke or raw validation field. Use bounded correction and recovery categories when product analysis justifies them.
- Treat blocked, offline, sampled, and consent-limited client telemetry as missing evidence, not a healthy zero.
- Correlate accepted and selected negative paths to backend outcome without making a frontend event the authority for persistence.
- Keep accessibility proof in automated and manual test evidence. Telemetry can show that a recovery action was exposed or selected, but not that every user could perceive it.
- Verify navigation, refresh, multi-tab, and destroyed-view behavior so late events do not claim a state that was never displayed.

**Operational checks**

- Dashboards pair a primary user outcome with semantic failure, duplicate-effect, retry-amplification, compatibility, parser-failure, saturation, and instrumentation-health guardrails appropriate to the workflow.
- Alerts page or create work only when an owner has a specific response. Lower-urgency trends belong in review queues with cadence and threshold rationale.
- Rollout views segment by code and contract versions and preserve comparison long enough to decide stage, pause, rollback, or continue.
- Runbooks identify the first evidence to inspect, effect uncertainty, safe containment, retry controls, compatibility state, and rollback or forward-repair owner.
- Retention, access, redaction, and deletion follow project privacy and regulatory policy; observability data is another protected data system.
- Costs and cardinality are reviewed before and after rollout. Sampling changes are versioned so trend discontinuities are explainable.

**Verification ladder**

| Gate | What to induce or inspect | Passing observation |
|---|---|---|
| Event schema test | Construct accepted, conflict, unavailable, malformed, cancelled, and retry events as applicable. | Required fields, units, bounded values, and redaction rules hold; invalid events fail locally. |
| Cardinality and privacy scan | Feed varied users, resources, errors, routes, and payloads. | Dimensions remain bounded and no protected content appears in normal logs or metrics. |
| Synthetic cross-stack flow | Run a labeled non-user operation through browser or client, API, dependency, and persistence. | One logical chain joins attempts, outcome, effect, frontend recovery, and versions. |
| Fault and retry test | Slow or fail a dependency, lose a response, cancel, and recover. | Attempts, effect certainty, capacity pressure, and recovery remain visible without duplicate logical demand. |
| Missing-signal test | Suppress one expected source or break a test ingestion path. | Instrumentation health reports unknown or missing rather than displaying a healthy zero. |
| Dashboard query review | Recalculate a panel from raw approved events and inspect units, window, and denominator. | Query meaning matches the documented metric and version segmentation. |
| Alert or drill | Trigger a test route or announced controlled condition. | Correct owner receives actionable context, follows the runbook, and can suppress or close safely. |
| Incident sample | Trace a real or staged user symptom to the first divergent boundary. | Evidence supports or rejects hypotheses without requiring sensitive transcript dumps. |

Good instrumentation records `conflict` as a bounded outcome, joins it to an opaque operation, identifies client and contract version, proves no write in authoritative evidence, and correlates a retained-draft recovery. Bad instrumentation labels events with email, raw URL, exception message, or payload. Borderline instrumentation counts generic errors: it is useful during containment, but cannot guide durable correction until outcome, denominator, and action are defined.

Signal schemas have consumers and need lifecycle management. Version semantic changes, overlap old and new definitions during migration, document dashboard discontinuities, and retire obsolete fields after consumers move. An incident should update the relevant contract, focused gate, runbook, and reference assumption; adding another dashboard without a changed decision does not close the loop.

For reference-evolution auditability, also record local sources loaded or skipped, exact verification commands and observed summaries, changed paths, section and field counts, unresolved risks, and journal checkpoints. Keep that evidence concise and reviewable rather than preserving raw reasoning transcripts. Reference audit signals support trustworthy guidance but remain separate from deployed application telemetry.

## Performance Verification Method

Do not use a universal latency threshold. Define a project-owned objective from the user promise, workload, supported clients, dependency limits, and measured baseline. Performance evidence compares named revisions under recorded conditions; it does not turn one fast run or one handler percentile into a general capacity claim.

Measure one primary end-to-end interval and decompose it enough to locate change. For an interactive profile update, the primary interval might begin at accepted user intent and end when the resulting trusted state or actionable rejection is rendered. Decomposition can include browser scheduling, request queue, server application time, dependency time, serialization, transfer, runtime parsing, state reduction, rendering, and accessibility-related update. The target project defines the exact boundaries.

| Claim scope | First useful method | Escalate when | What it cannot establish alone |
|---|---|---|---|
| Pure algorithm or parser mechanism | Microbenchmark with representative size and shape distributions. | Allocation, runtime, or output affects integration behavior. | Network, framework, browser, dependency, and user-visible cost. |
| Endpoint or application use case | Focused integration benchmark against representative persistence and dependencies. | Pools, concurrency, external services, or client behavior influence the result. | Browser parse and render, rollout skew, and full production contention. |
| Contract and payload change | Serialization, transfer-size, parser, and compatibility fixture measurements. | Tail payloads, network quality, or old clients are consequential. | End-user responsiveness and server saturation by themselves. |
| Angular component or state change | Component timing, change or render count, memory, and deterministic interaction profile. | Data, network, routing, or device class changes the experience. | Backend service time and real browser scheduling across the supported matrix. |
| Full user journey | Browser-driven end-to-end profile with correlated backend and client timings. | Capacity, rare tails, or production topology matter. | Maximum sustainable load and every real client condition. |
| Capacity and backpressure | Controlled concurrency or arrival-rate test with offered load, logical completions, queue or pool pressure, attempts, and resource use. | Real dependencies, quotas, or recovery behavior differ from the environment. | Production safety unless load, data, and dependency behavior are representative. |
| Rollout impact | Staged or controlled production comparison segmented by code and contract version. | Traffic mix, configuration, or concurrent changes confound interpretation. | Strict causality without credible comparison and instrumentation quality. |
| Reference-review efficiency | Timed reviewer tasks with decision accuracy, files opened, unresolved questions, and gate selection. | The claim concerns deployed runtime behavior. | Application latency, reliability, or user success. |

**Required measurement packet**

| Packet field | Required content | Invalid or misleading state |
|---|---|---|
| Decision and primary claim | The exact user or resource outcome being compared and why it changes a decision. | "Faster" with no boundary or action. |
| Baseline and candidate | Immutable revisions, configuration, feature flags, generated artifacts, and dependency versions. | Different schema, output semantics, or hidden configuration. |
| Workload | Interaction shape, offered logical operations, concurrency or arrival schedule, outcome mix, input and payload distributions, state lifetime, and duration. | "Representative" with no provenance or distribution. |
| Data provenance | Synthetic or sanitized fixture generation, cardinality, tails, and privacy constraints. | Production personal payload copied into a benchmark. |
| Environment | Hardware, operating system, runtime mode, browser and device class, network shaping, database, dependency topology, and competing load. | Comparing local debug and production-optimized builds as implementations. |
| Setup state | Cold or warm runtime, JIT or compilation, caches, pools, database state, browser profile, and preconditioning. | Candidate always runs second and benefits from warmed shared state. |
| Command and harness | Exact command, working directory, harness revision, load generator settings, stop conditions, and instrumentation. | Manual steps or defaults that cannot be reconstructed. |
| Primary and decomposed measures | Units, start and end boundaries, end-to-end interval, server, dependency, payload, parse, state, render, memory, allocation, and resource measures that matter. | Mixing clock domains or reporting a component as end to end. |
| Population and statistics | Eligibility, exclusions, sample count, failed and cancelled operations, quantiles or distribution summaries, run-to-run variation, and missing data. | Dropping errors or timeouts from latency without reporting them. |
| Guardrails | Contract outcomes, persistent effects, duplicate count, retry amplification, accessibility, compatibility, memory, and cost checks. | Speed improves because work, validation, rendering, or error handling disappeared. |
| Result and uncertainty | Absolute baseline and candidate distributions, relative change when useful, noise, confounders, and unsupported extrapolations. | One ratio without absolute values or uncertainty. |
| Reproduction and retention | Independent rerun status, artifact location, expiry trigger, owner, and commands needed to compare later. | Screenshot or copied number with no executable provenance. |

**Procedure**

1. State the behavior and locally owned objective. If no objective exists, measure a baseline and describe the decision the observation can support; do not invent a pass threshold.
2. Freeze correctness fixtures and guardrails before optimizing. Ensure accepted and applicable negative outcomes remain the same.
3. Choose the least expensive method that can disconfirm the claim. Use a narrow benchmark for mechanism diagnosis and an integration or browser method for user impact.
4. Validate the harness. Confirm offered load, server receipt, completed logical operations, errors, cancellations, and generator resource use agree within explained boundaries.
5. Record cold and warm behavior separately when startup, JIT, caches, pools, browser initialization, or connection reuse matters.
6. Alternate or randomize baseline and candidate run order when thermal, cache, background, or time drift could bias a fixed sequence. Reset state that must be comparable.
7. Include the full outcome mix and tail fixtures that exercise validation, conflict, unavailable, malformed, and accepted paths where applicable.
8. Report absolute distributions and resource measures, not only a percentage. Include failed, timed-out, and cancelled operations in a separate accounting rather than deleting them.
9. Repeat enough to observe run-to-run variation under the decision's consequence. Classify a one-run clue as exploratory, not final evidence.
10. Run correctness, duplicate-effect, retry, compatibility, accessibility, memory, and cost guardrails after the candidate. Reject a faster implementation that changes the supported behavior without an approved contract change.
11. Confirm the relevant result at the next realistic boundary: parser to endpoint, endpoint to browser, local capacity to staging, or staging to controlled rollout.
12. Retain the packet with owner and invalidation triggers, then remove temporary high-overhead instrumentation that would distort production.

**Measurement pitfalls and controls**

- **Coordinated omission:** A closed-loop generator can stop offering work while the system stalls and understate user waiting. Record offered arrival behavior and choose a generator model appropriate to real demand.
- **Client bottleneck:** The load generator, test runner, browser, or network emulator can saturate first. Monitor its CPU, memory, connections, timers, and errors separately.
- **Cache and order bias:** A candidate run after the baseline may inherit warm data or compiled code. Alternate order, isolate state, or report the bias.
- **Outcome drift:** A faster variant may reject more work, skip parsing, collapse failures, serve stale cache, or render less. Compare outcome and effect counts before timing conclusions.
- **Tail exclusion:** Timeouts, cancellations, and errors cannot simply vanish from a latency histogram. Report their incidence and user semantics.
- **Sampling overhead:** Tracing, allocation profiling, browser tooling, and debug logging can alter the path. Measure overhead or use consistent instrumentation across variants.
- **Environment mismatch:** Local loopback hides network and deployment behavior; production comparison adds confounders. State which inference each environment supports.
- **Percentile decoration:** p50, p95, p99, or any quantile needs population, sample count, window, units, and method. Sparse data may not support a stable tail conclusion.
- **Sensitive data:** Build synthetic or sanitized distributions; do not export production bodies, identities, or raw validation values into fixtures.
- **Bundle and client transfer:** Server improvement can be offset by larger generated clients, JavaScript, payloads, or parsing. Track transferred bytes and client work when changed.

Good claim: "Under the recorded accepted/conflict workload, candidate and baseline preserve identical effects and recovery. Across alternating runs on the same release configuration, the candidate reduces the measured server application distribution and allocation while end-to-end browser responsiveness also improves; payload, retries, memory, accessibility, and error incidence remain within the project's guardrails. Results and variation are attached to the packet." Bad claim: "The handler is twice as fast" after one warm local run. Borderline claim: a clear server gain with no browser measurement; it supports a server-mechanism decision but not an end-user speed claim.

Pass when the locally established objective or comparison decision is supported under the declared workload, uncertainty is acceptable for the consequence, and all selected guardrails hold. Fail when conditions are not comparable, the harness saturates, errors are excluded, outcome semantics change unintentionally, or the result cannot be reproduced. When differences overlap measurement noise, report inconclusive evidence and prefer the simpler or more reversible candidate unless another verified benefit decides the choice.

Optimization can shift cost into cache invalidation, memory, bundle size, compatibility, operational complexity, or maintenance. Record those second-order changes when they exist. Removing unnecessary calls, conversions, duplicate state, or payload fields is often attractive because it reduces latency and the number of failure boundaries together, but it still requires contract and user-state verification.

## Scale Boundary Statement

This reference is sufficient as the primary guide while one bounded .NET and Angular behavior can be reasoned about through explicit outcomes, a known effect boundary, owned TypeScript trust, one coherent frontend state, a declared workload, and a testable deployment model. Traffic volume alone does not force a new architecture. A low-volume cross-region write can exceed the model because ordering and ownership change, while many independent bounded reads can remain within it at much higher traffic.

When an assumption breaks, transition only the affected responsibility. This reference can remain the edge guide for transport and UI reconciliation while system architecture, background processing, realtime delivery, offline synchronization, security, or data topology receives a specialist owner.

| Boundary signal | Evidence that the baseline assumption failed | Candidate transition | New obligations created | Premature or wrong response |
|---|---|---|---|---|
| Tail payload or collection no longer fits one response and render. | Size, cardinality, transfer, parse, memory, or render distributions breach a local user or resource objective. | Server bounds, pagination, incremental fetch, streaming, chunking, or bounded virtualization according to interaction semantics. | Ordering, continuation identity, cancellation, partial failure, duplicate items, accessibility, and compatibility. | Splitting arbitrarily without stable ordering or measuring only server time. |
| Work outlives the useful request deadline. | Requests time out or browsers leave while work must continue, and in-process completion is not durable. | Durable operation identity with queued or scheduled work, progress, poll or push, cancellation limits, and cleanup. | Accepted-versus-completed contract, idempotency, persistence, restart, poison work, expiry, observability, and reconciliation. | Fire-and-forget task inside the request process or infinite timeout. |
| Read demand repeats expensive stable work. | Measured dependency or computation pressure is dominated by repeated equivalent reads and freshness tolerance is explicit. | Request coalescing, precomputation, or bounded cache with owned keys and invalidation. | Freshness, versioning, stampede control, memory, privacy, eviction, rollback, and stale-result UI. | Cache before identifying repeated work or without an invalidation invariant. |
| Dependency or pool saturates under concurrency. | Queue time, occupancy, throttling, or timeout dominates useful work and offered load is verified. | Admission control, bounded concurrency, load shedding, batching, dependency-specific circuit, or capacity change. | Fairness, priority, rejected-work semantics, retry interaction, tuning, and recovery-phase tests. | Unbounded queue or retries that increase demand during reduced capacity. |
| Writes contend on the same authority. | Concurrent-update tests or incidents show conflicts, lock pressure, or lost updates beyond the accepted policy. | Optimistic versioning, explicit serialization, sharding by safe key, reservation, merge, or workflow redesign. | Hot-key detection, ordering, conflict UX, rebalance, idempotency, and migration. | Partitioning by a convenient key that does not match contention or consistency. |
| Client requires continuous or multi-event updates. | Polling misses freshness objectives, wastes capacity, or cannot represent event progression. | Realtime subscription or event stream with snapshot reconciliation. | Ordering, duplicate delivery, gap detection, reconnect backoff, bounded buffering, authorization changes, and lifecycle ownership. | Treating connection success as state correctness or assuming automatic replay. |
| Client works offline or from stale local state. | Product requires edits without current server state or later synchronization across writers. | Durable local operations plus explicit sync, merge, conflict, and replay model. | Schema evolution, operation identity, data protection, user reconciliation, storage limits, and cleanup. | Reusing online retry and last-write behavior without product-owned conflict semantics. |
| Consumers or deploys evolve independently. | Supported old and new clients, services, proxies, caches, or generated artifacts overlap in production. | Additive contract evolution, tolerant external parsing, versioning where necessary, staged migration, and retirement windows. | Compatibility matrix, schema ownership, generated drift gates, observability by version, rollback, and deprecation. | Breaking server-first rollout under assumed atomic deployment. |
| Several independently operated services share the behavior. | Ownership, release, data authority, failure policy, and rollback cannot be coordinated as one slice. | System-level contract, workflow, consistency, and failure architecture with one owner per authority. | Partial failure, distributed tracing, compensation, idempotency, schema governance, service objectives, and incident coordination. | Copying the same domain and retry rules into each service without an authority. |
| Data spans regions, residency zones, or legal boundaries. | Latency, availability, data-placement policy, or write ordering cannot be satisfied by one location model. | Explicit regional routing, replication, locality, failover, and conflict policy. | Residency proof, replication lag, split-brain behavior, failover drills, key management, and regional compatibility. | Multi-region writes before defining authority, loss tolerance, and reconciliation. |
| Team autonomy becomes the primary driver. | Teams need independent change and operation around a stable business responsibility, not merely fewer files. | Owned module or service boundary with explicit protocol and operating contract. | On-call, deployment, compatibility, telemetry, data ownership, and cost accountability. | Service extraction based on endpoint count or organization chart alone. |
| Security or data consequence exceeds the general guide. | Threat model, policy, regulated data, destructive effect, or abuse cases demand specialist review. | Security, privacy, identity, audit, and resilience guidance with accountable owners. | Threat modeling, policy enforcement, restricted evidence, incident response, and compliance proof. | Treating generic validation or authentication examples as sufficient assurance. |

**Transition test**

1. Name the first violated assumption: resource envelope, temporal lifetime, consistency, trust, deployment, ownership, or policy.
2. Establish baseline evidence and confirm the bottleneck or semantic gap at the owning boundary. An endpoint count or forecast alone is not enough unless policy mandates the topology.
3. Compare the simplest bounded remedy with the proposed new architecture under the same behavior, workload, and reliability targets.
4. List every new identity, queue, cache, protocol, store, service, region, owner, compatibility window, and operational path introduced.
5. Add gates for the transition's characteristic failures, including overload, restart, partial effect, retry, migration, rollback, and user recovery.
6. Stage the change with observable continue, pause, rollback, or forward-repair criteria.
7. Define when the mechanism can be removed, contracted, or returned to a simpler design if the pressure disappears.

Good transition: measured payload and browser render tails violate the local interaction objective, so the team adds stable server pagination, bounded client state, cancellation, keyboard-safe navigation, continuation tests, and an old-client compatibility path. Bad transition: twenty-six endpoints are split into services because the count feels large, while ownership, data, deployment, and failures remain shared. Borderline transition: repeated reads justify a cache, but without an invalidation owner and stale-state UX the candidate moves cost rather than resolving it.

**Companion versus route-away**

- Keep this reference primary and add a companion when the .NET/Angular contract remains one bounded behavior but needs deeper performance, security, visual, TypeScript, or verification guidance.
- Make system design primary when topology, distributed consistency, messaging, data authority, or cross-service recovery is the decision; return here with the resulting protocol and failure model.
- Make a background or realtime model primary when completion or updates no longer fit one response; return with durable identity, ordering, gap, cancellation, and reconciliation rules.
- Route away entirely when the target stack is no longer .NET and Angular, then preserve only the shared protocol obligations that actually cross into this stack.

After transition, verify the candidate improves the pressure that justified it and does not violate correctness, compatibility, accessibility, privacy, cost, or operability guardrails. Managed infrastructure may reduce implementation work, but it does not own product semantics, data policy, failure behavior, budget, or user recovery.

The same discipline applies to large codebases and distributed agent work. Narrow discovery with dependency or source graphs before loading broad context; rank evidence rather than treating a file list as authority. Keep one writer and one verification owner per reference, checkpoint durable progress, reread the governing specification after context transitions, and merge only through exact path, heading, evidence, uniqueness, and hygiene gates. Parallelism is useful across independent files, not as concurrent rewriting of one semantic authority.

Architecture may contract. Remove an unused cache, queue, compatibility branch, service hop, or global store when its pressure and consumers disappear and the simpler candidate passes the retained gates. Scale mechanisms are means for protecting a measured behavior, not permanent evidence of engineering maturity.

## Future Refresh Search Queries

No internet search was performed during this evolution. The historical corpus version labels and every external mapping remain unrefreshed. The rows below are a future authorized refresh queue, not evidence that a source was opened or a claim was confirmed.

Before executing a query, inspect the target solution, Angular workspace, package manifests, lockfiles, schema, generator configuration, and deployment topology. Append the exact discovered framework or package version to the query. Search to answer one decision or uncertainty, not for generic "best practices."

| Query ID | Decision or uncertainty | Future query text | Preferred authority and acceptance condition |
|---|---|---|---|
| `DOTNET-SUPPORT` | Which target .NET release is supported, and what migration or compatibility constraints apply? | `site:learn.microsoft.com dotnet support policy release lifecycle migration official` | Microsoft lifecycle and target-release documentation; record release, support state, date, and target manifest match. |
| `ASPNET-ENDPOINT` | Which endpoint organization and result-mapping APIs are supported for the target ASP.NET Core release? | `site:learn.microsoft.com asp.net core minimal APIs controllers typed results official` | Microsoft ASP.NET Core documentation for the exact release; accept bounded API semantics, not a global architecture ranking. |
| `ASPNET-ERROR` | What official error, validation, and problem-response conventions apply to the target release? | `site:learn.microsoft.com asp.net core error handling validation problem details official` | Microsoft documentation linked to the target protocol and tested mapping. |
| `ASPNET-CANCEL` | How does request cancellation propagate and where can work become irreversible? | `site:learn.microsoft.com asp.net core request cancellation RequestAborted official` | Microsoft API and ASP.NET Core guidance plus a target-project timed cancellation test. |
| `EF-CONCURRENCY` | What optimistic concurrency mechanisms and conflict behavior are supported by the target persistence stack? | `site:learn.microsoft.com ef core optimistic concurrency conflict official` | Microsoft EF Core documentation for the discovered provider and release; verify representative persistence semantics. |
| `EF-RESILIENCY` | Which execution retry mechanisms exist and what transaction or idempotency constraints accompany them? | `site:learn.microsoft.com ef core connection resiliency execution strategy transaction official` | Microsoft provider-relevant guidance; reconcile with the one logical-operation retry budget. |
| `ANGULAR-SUPPORT` | Which Angular release and migration path does the workspace target? | `site:angular.dev update guide version compatibility official Angular` | Angular official update and compatibility material matched to workspace manifests. |
| `ANGULAR-SIGNALS` | What are the target release's supported signal semantics, derived-state patterns, and lifetime constraints? | `site:angular.dev guide signals computed effect official` | Angular official guide for the target release; accept only claims compiled and tested in the workspace. |
| `ANGULAR-RXJS-INTEROP` | How should Observable and signal boundaries, subscriptions, and teardown be expressed in the target release? | `site:angular.dev rxjs interop signals teardown official` | Angular official interoperability and lifecycle guidance plus cancellation and destruction tests. |
| `ANGULAR-HTTP-TEST` | What HTTP client and testing APIs are supported, including cancellation and error responses? | `site:angular.dev http client testing requests official` | Angular official HTTP and test documentation matched to project providers and configuration. |
| `ANGULAR-FORMS-A11Y` | Which official forms, validation, and accessibility guidance applies to changed states? | `site:angular.dev forms validation accessibility official` | Angular guidance plus applicable W3C standards and target browser or assistive-technology checks. |
| `TYPESCRIPT-RELEASE` | Which compiler behavior, strictness options, and breaking changes apply to the target TypeScript release? | `site:typescriptlang.org docs release notes breaking changes strict official` | TypeScript handbook, configuration reference, and release notes for the manifest version. |
| `TYPESCRIPT-NARROWING` | What supported narrowing and discriminated-union behavior protects exhaustive internal state? | `site:typescriptlang.org handbook narrowing discriminated unions never official` | TypeScript official handbook and target compiler result; distinguish static exhaustiveness from runtime validation. |
| `RXJS-CONCURRENCY` | What are the exact concurrency, cancellation, and retry semantics of operators used by the project? | `site:rxjs.dev switchMap exhaustMap concatMap mergeMap retry official` | RxJS official API material for the installed major version plus marble or timed project tests. |
| `OPENAPI-SCHEMA` | Which OpenAPI semantics affect nullable, required, discriminator, and compatibility behavior? | `site:spec.openapis.org discriminator required nullable schema official` | OpenAPI specification version used by the discovered toolchain; reconcile with generator behavior. |
| `GENERATOR-OWNER` | Is the discovered client generator supported, reproducible, and compatible with target C# and TypeScript versions? | Use the exact package name, publisher, release, and the words `official documentation changelog breaking changes deterministic generation`. | Official publisher documentation and release notes plus clean regeneration, diff, compile, and old/new fixture gates. |
| `OTEL-SEMANTICS` | Which current semantic conventions apply to HTTP, exceptions, retries, and frontend correlation? | `site:opentelemetry.io docs specifications semantic conventions http exception official` | OpenTelemetry official specification matched to the project's instrumentation packages; preserve local outcome vocabulary. |
| `WEB-ACCESSIBILITY` | Which standards govern errors, status messages, focus, and keyboard recovery? | `site:w3.org WAI WCAG error identification status messages focus order official` | W3C WAI normative or technique material, interpreted with target user and assistive-technology tests. |
| `SECURITY-BOUNDARY` | Which current guidance affects authorization, validation, logging, and API abuse for this workflow? | `site:owasp.org API security authorization input validation logging official` | OWASP primary project material plus project policy and direct abuse-case tests; route high-consequence decisions to security owners. |

The generic source categories have distinct roles:

- Official documentation defines supported public behavior for a version.
- Release and migration notes identify changes and deprecations.
- Specifications define protocol semantics but may not describe one tool's implementation.
- Official sample repositories can demonstrate integration when publisher, tag, target release, and linked documentation are verified.
- Issue trackers and source code can explain defects or implementation details, but do not become the default recommendation without support and applicability evidence.
- Third-party tutorials can supply search vocabulary or a counterexample; they do not outrank primary sources.

**Refresh procedure**

1. Freeze the historical claim, target behavior, and implementation decision before searching.
2. Discover exact target versions and ownership. Stop if the relevant project or generator cannot be identified.
3. Run the narrow official-domain query and open the complete page, not only a search snippet. Verify publisher, target release, publication or update date, and page context.
4. Paraphrase the bounded finding. Avoid long quotations and do not generalize beyond the documented API or release.
5. Record whether the source confirms, narrows, contradicts, supersedes, or does not address the historical claim.
6. Reconcile with target project convention and compile or test the consequential behavior. Current official support does not by itself prove local fit.
7. When primary sources conflict or lag implementation, retain the conflict, narrow the recommendation, and add a disconfirming gate; do not average them into certainty.
8. Update this reference only when evidence changes applicability, implementation, risk, routing, or verification. Link churn alone is not a reason to rewrite stable guidance.

| Refresh record field | Completion rule |
|---|---|
| Query and frozen decision | Preserve the exact query, uncertain claim, and choice it may change. |
| Target context | Record solution or workspace revision, framework and package versions, generator, schema, and deployment assumptions. |
| Source identity | Record title, official publisher, direct location, publication or update date, accessed date, and applicable release. |
| Bounded finding | Paraphrase the supported behavior and its stated limit without importing unrelated recommendations. |
| Evidence role | Classify documentation, release note, specification, official sample, implementation, issue, or secondary discovery. |
| Conflict and uncertainty | Record disagreement with archive, project, another source, or untested behavior. |
| Project gate | Name the compile, contract, runtime parse, state, browser, compatibility, security, performance, or operational observation that decides applicability. |
| Disposition | Promote, adapt, retain as legacy, retain as negative evidence, reject, or leave unresolved with reason. |
| Ownership and freshness | Name the owner, next invalidation trigger, superseded record, and consumers affected by an update. |

Accept a future refresh only when the source is authoritative for the target release, the finding answers the frozen question, conflicts are visible, and a project gate supports the adopted implication. Reject or leave unresolved an undated summary, an incompatible version, a search snippet, an unofficial mirror, an unowned sample, or a source that never addresses the decision.

Newer evidence is not automatically applicable to a maintained older target. Conversely, failure to find official support is not permission to promote a popular tutorial. It is an explicit uncertainty that should narrow the change, preserve reversibility, and raise the value of target compilation and behavior tests.

## Evidence Boundary Notes

Confidence attaches to one claim under one scope and evidence condition. It does not transfer automatically from a polished source, official publisher, passing compile, or measured number to every recommendation around it. Use the smallest practical claim group and one of these seven classes:

| Evidence class | What it can support | What it cannot support alone | Verification and freshness rule |
|---|---|---|---|
| `historical_local_observation` | Exact statements, examples, scores, contradictions, and version labels found in the mapped archive source. | Current framework guidance, target-project fit, reproduced performance, or project policy. | Locate the immutable archive path and heading signal; retain historical tense and original limitation. |
| `target_project_observation` | Checked-in manifests, code, schemas, generator configuration, tests, deployment records, and current local policy for the project being changed. | General ecosystem recommendation or production outcome beyond what was observed. | Record revision, path, configuration, and observation; reopen when the project boundary changes. |
| `refreshed_external_evidence` | Current supported API, specification, release, migration, or security guidance from an authoritative source for a named version. | Local applicability, successful integration, or behavior under the target workload. | Verify publisher, complete page, date, target release, and bounded finding; attach a project gate and refresh trigger. |
| `systems_synthesis_or_judgment` | A reasoned default, alternative, causal mechanism, or risk derived from evidence and systems principles. | Fact that a target project uses the pattern or that the recommendation is universally optimal. | State fit, counterexample, uncertainty, reversal signal, and disconfirming observation. |
| `hypothetical_or_illustrative_example` | A worked model that makes semantics, tradeoffs, and tests concrete. | Compilation, current API support, production safety, measured improvement, or actual user behavior. | Label the example, adapt it to target manifests, and preserve its test obligations. |
| `executable_or_measured_result` | Behavior or distribution observed under a named revision, command, fixture, workload, environment, and time. | Universal behavior, causality beyond the comparison, or future performance after invalidating change. | Retain command, conditions, failures, guardrails, uncertainty, and expiry trigger; rerun after affected changes. |
| `unresolved_or_queued_claim` | A known uncertainty, conflict, missing owner, or future refresh question that can guide the next investigation. | Positive implementation authority or evidence that a risk is absent. | Name consequence, owner, next observation, stop condition, and why current evidence is insufficient. |

No internet browsing occurred during this evolution. Therefore:

- the public URL mappings in `External Research Source Map` are retrieval candidates, not `refreshed_external_evidence`;
- the future search queries are unanswered and do not support current-version claims;
- the historical framework and language version labels remain archive facts rather than statements about current releases;
- the worked C# and TypeScript snippets are semantic illustrations and were not compiled against a target project;
- no target production workload, SLO, latency distribution, capacity limit, browser population, or outcome metric was measured here;
- no target solution, workspace, generator, deployment ownership, security policy, or compatibility window is established by this reference alone.

**Directly observed local evidence**

The complete mapped February archive file was available locally and supplies a broad historical candidate corpus across .NET, C#, Angular, TypeScript, integration, testing, anti-patterns, performance, and dependency guidance. Direct inspection also reveals important limits: a universal four-word naming rule, framework choices presented too rigidly, an Observable-returning service consumed as though it were a Promise while the test double returns a Promise, generated static types without an inherent runtime validation guarantee, reconnect guidance without proof of message replay, exact performance claims without retained harness evidence, and version-sensitive statements that were not refreshed. These observations justify warnings and test prompts; they do not prove how often the failures occur in a target project.

The inherited scoreboard values are historical source observations only. They are not current benchmarks, confidence percentages, or quantified evidence that one pattern improves a target system. Similarly, the exact 26 headings and the archive seed are structural evidence for this evolution, not application reliability evidence.

**Claim-writing rules**

1. State the bounded claim before naming its source. Split a sentence when one half is historical fact and the other half is synthesis.
2. Use historical tense for archive recommendations and present tense only for directly observed project behavior, stable logical definitions, or properly refreshed external evidence.
3. Name the target release and source date for changing APIs. If either is absent, keep currentness unresolved and require target compilation.
4. Do not promote a URL, search snippet, repository example, filename, table of contents, or confident prose to authority by appearance.
5. Do not let several weak or duplicate sources create artificial certainty. Independent evidence strengthens a claim only when it observes a relevant boundary separately.
6. Preserve contradictions. Narrow scope and add a test instead of selecting whichever source supports the preferred implementation.
7. Treat a compile as evidence of syntax and static contracts for that configuration, not runtime payload validity, product correctness, accessibility, security, or production capacity.
8. Treat a passing mock as evidence only when the double implements the production contract and an integration boundary is also represented where consequential.
9. Treat a measurement as conditional on workload, environment, harness, population, guardrails, and uncertainty. Remove exact numbers whose method cannot be reproduced.
10. Label policy as policy and product choice as product choice. Neither becomes a universal technical principle through repetition.
11. Attach a disconfirming gate to guidance that changes implementation, persistent effect, compatibility, security, retry, performance, or operations.
12. During skeptical reread, search for absolute, current, quantitative, guaranteed, secure, fast, resilient, and best language; either support, bound, or remove it.

**Good, bad, and borderline evidence statements**

- Good: "The historical corpus contains an async contract contradiction: its service surface is Observable-shaped while the component and test use Promise-shaped behavior. Treat this as negative evidence; compile the real target types and test cancellation and teardown before selecting an adapter."
- Bad: "Angular currently requires signals for local state and Observables for every asynchronous operation." This overstates current API authority and converts a contextual design default into a universal rule.
- Good: "Runtime parsing is recommended at untrusted or independently deployed boundaries because TypeScript declarations do not inspect response bytes; an atomic generated deployment can document a narrower trust model."
- Borderline: "The generated client is type safe." Static generation can support compile-time agreement, but the statement must distinguish schema reproducibility, runtime trust, and version skew.
- Bad: "The endpoint must meet p99 under 500 ms." No target workload, objective, environment, or measurement supports that number here.
- Good: "Set a local responsiveness objective from the user promise and baseline, then report end-to-end and decomposed distributions with correctness and accessibility guardrails."

**Evidence precedence and conflict**

Project observation determines what the target currently does; it does not automatically prove what it should do. Refreshed official evidence determines supported ecosystem behavior for a named release; it does not automatically override a deliberate compatible project policy. Executable results determine behavior under their conditions; they do not erase product or security constraints. Systems synthesis connects these inputs and must retain the counterargument and uncertainty.

When evidence conflicts, first check version, configuration, scope, source role, and test fidelity. Preserve unresolved disagreement when no observation decides it. Prefer a reversible implementation, narrow the supported claim, and assign the next disconfirming gate. Never average contradictory claims into a medium-confidence recommendation.

**Verification by class**

| Claim class | Minimum verification action | Promotion condition | Demotion or expiry trigger |
|---|---|---|---|
| Historical local | Reopen the archive heading and confirm exact context. | Becomes candidate guidance only after bounded synthesis and target gate. | Source was misread, duplicate, or superseded for the intended use. |
| Target project | Inspect the authoritative path and run the relevant compile or behavior probe. | Becomes project policy only with current ownership or governance. | Revision, architecture, ownership, or behavior changes. |
| Refreshed external | Open the official complete source and verify target release, date, and applicability. | Supports current guidance after project reconciliation. | Release, documentation, support status, or target manifest changes. |
| Synthesis | Review fit, alternatives, failure mechanism, and disconfirming test. | Becomes local default after repeated project evidence or explicit decision. | Counterexample, incident, or simpler candidate passes the same gates. |
| Illustration | Adapt to project types and execute the listed obligations. | Becomes project example after compile and focused tests. | API, schema, contract, or state model changes. |
| Executable or measured | Rerun exact command under retained conditions and inspect failures and guardrails. | Supports the scoped behavior or comparison for that revision. | Code, data, workload, environment, instrumentation, or objective invalidates comparison. |
| Unresolved | Confirm owner, consequence, next action, and stop condition. | Moves to another class only after the named evidence arrives. | Becomes irrelevant because scope or architecture removes the concern. |

Evidence evolves. A hypothesis can become a tested project default; a current external recommendation can become legacy; a measured result can expire; a rejected claim can remain useful negative evidence. Reclassify when implementation, risk, routing, or supported behavior changes, not for cosmetic link churn. Preserve consequential rejection and supersession reasons so later agents do not rediscover the same unsupported claim and mistake novelty for evidence.

This reference is decisive about method: discover the project, preserve behavior, distinguish outcomes, validate runtime trust, own state and async lifetime, test negative paths, measure under declared conditions, and keep rollback and uncertainty visible. The exact framework APIs, quantitative targets, topology, policy, and project-specific pattern choices remain conditional until the corresponding evidence class and gate exist.
