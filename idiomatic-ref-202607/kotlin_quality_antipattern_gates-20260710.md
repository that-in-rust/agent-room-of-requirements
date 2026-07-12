# Kotlin Quality Antipattern Gates

Use this reference to decide whether a Kotlin implementation or review preserves the semantic distinctions and ownership contracts that its callers depend on. It is not a style catalog and it does not select Spring, Ktor, Android, Gradle, Maven, a persistence framework, or a coroutine dispatcher on the reader's behalf. Its purpose is narrower and more operational: identify the smallest applicable quality controls, apply them at the boundary where uncertainty enters, and attach evidence strong enough for the claim being made.

`local_corpus_sourced_fact`: The mapped local source names ten high-value Kotlin anti-patterns, an eight-item reliability stack, repository-native Gradle and Maven gate commands, command-discovery steps, and a six-axis review pass covering nullability, Java interop, types, coroutines, tests, and gates.

`external_pointer_unrefreshed`: No public page was opened during this evolution. The Kotlin documentation, `kotlinx.coroutines`, Spring Boot Kotlin guide, and Ktor documentation rows later in this file are retained as unrefreshed pointers. They provide no current-version fact until an authorized refresh records the retrieved artifact, date, version, relevant span, and target applicability.

`combined_evidence_inference_note`: Reliable Kotlin code preserves information and ownership from the first uncertain boundary to the final observable outcome. Nullability, platform types, domain states, equality, coroutine lifetime, cancellation, blocking, and mutable state are therefore connected concerns rather than independent lint preferences.

**Primary decision**

Use the gates here when a change involves one or more of these questions:

- Where does an external, Java, serialized, database, configuration, or user-supplied value become trusted Kotlin data?
- Does `null` represent one real state, or is it hiding absent, invalid, forbidden, unknown, not-yet-loaded, or failed states?
- Who owns a coroutine's lifetime, cancellation, failure, and cleanup?
- Can a call block a constrained thread while presenting itself as suspending or nonblocking?
- Do equality, `copy`, and destructuring match the lifecycle of the modeled object?
- Can a caller distinguish success, rejection, absence, conflict, retryable failure, and terminal failure without guessing what `true`, `false`, or `null` means?
- Which project-native tests, builds, linters, and static analyzers provide evidence for the changed behavior?

The reference is sufficient only while those questions remain within a bounded code and ownership surface. Route away when the missing decision belongs to domain policy, framework lifecycle configuration, Java API ownership, persistence identity, security/privacy policy, or production capacity. A Kotlin syntax choice must not silently decide one of those matters.

**Recommended default sequence**

1. Inspect the repository's language, framework, dependency, test, formatting, lint, and static-analysis conventions before proposing a new mechanism.
2. Locate every uncertain ingress used by the changed path. Normalize platform types and malformed input in an adapter or boundary function before domain logic.
3. Model meaningful closed states with value objects, enums, or sealed outcomes. Keep `T?` only when one undifferentiated absence state is genuinely the contract.
4. Keep concurrency structured: use caller-owned scopes, `coroutineScope`, `supervisorScope` where sibling-failure isolation is intended, or an actual lifecycle scope. Preserve `CancellationException` and cleanup behavior.
5. Make blocking explicit. Prefer a named blocking API when callers must supply the execution policy; otherwise isolate a known blocking dependency on an appropriate dispatcher and test the boundary.
6. Prefer named locals and functions when nested scope functions obscure receiver, return value, side effect, or failure ownership.
7. Write or update tests for the highest-consequence distinction, including malformed, absent, cancelled, duplicate, blocking, equality, or boundary behavior as applicable.
8. Run the repository's own wrapper commands. Add no toolchain merely because this reference mentions `ktlint` or `detekt`; first prove the target project configures it.

This order matters. A formatter can standardize an unsafe `!!`, and a static analyzer can report a detached coroutine, but neither recovers the domain state or ownership information that the implementation already discarded. Boundary and ownership corrections have greater causal leverage than cosmetic cleanup.

**Constructs are signals, not context-free bans**

`!!`, `lateinit`, data classes, nullable properties, scope functions, broad catches, and dispatcher switches are not uniformly wrong. Their burden of proof changes with exposure and consequence:

| construct_or_choice | default_review_concern | bounded_exception_evidence |
| --- | --- | --- |
| `value!!` | moves uncertain input into a distant crash | invariant is established immediately beside the assertion and an impossible-state test or framework contract supports it |
| broad `lateinit` | creates temporal initialization state outside the type | lifecycle or test fixture owns initialization, access cannot race it, and teardown cannot expose stale state |
| Java platform type in domain code | hides nullability uncertainty | adapter conversion cannot occur earlier and every use remains within one reviewed interop boundary |
| `GlobalScope` | detaches lifetime, cancellation, and failure ownership | process-lifetime work has explicit supervision, shutdown, durable state, and failure reporting; most application work will not satisfy this |
| broad `catch (Exception)` in suspend work | can swallow cooperative cancellation | cancellation is rethrown first and the remaining exception set is translated deliberately |
| data class for an identity-heavy entity | generated equality, `copy`, and destructuring can violate lifecycle semantics | value semantics are the intended identity and every generated operation is valid for the framework and persistence model |
| dispatcher switch around blocking work | can conceal an unbounded or uninterruptible dependency | dependency is known blocking, pool ownership and saturation are measured, cancellation semantics are documented, and the boundary is tested |

**Good, unsafe, and conditional cases**

Good: a Java adapter converts a platform value into `EmailAddress` or a typed parse failure; domain code never sees the platform type. A suspend use case runs in a caller-owned scope, rethrows cancellation, and returns a sealed outcome that forces the caller to handle rejection and dependency failure separately. Tests cover malformed input and cancellation, followed by the repository's existing build and static checks.

Unsafe: a controller uses `request.email!!`, launches `GlobalScope.async`, catches `Exception`, calls a blocking client from the default dispatcher, and returns `true` for every non-crashing path. The code may compile and pass a successful-request test while losing five independent contracts: input validity, lifetime, cancellation, execution policy, and outcome meaning.

Conditional: a migration adapter temporarily receives a platform type and catches a broad library exception. It can be acceptable when the uncertainty is normalized before leaving the adapter, cancellation is not in the caught hierarchy or is rethrown, a removal or compatibility condition is explicit, and focused tests prove both conversion and failure translation. Calling it "idiomatic" is unnecessary; proving its containment is what matters.

**Evidence and completion boundary**

A quality claim is complete only to the extent that its evidence matches its scope:

- Source inspection can establish that a platform type is contained or a cancellation exception is rethrown on the inspected path.
- Unit and boundary tests can establish selected input, state, equality, cancellation, and translation behavior under their fixtures.
- Compilation and project builds can establish type and integration compatibility for the configured target.
- Configured lint and static analysis can establish the absence of their modeled findings in the scanned population.
- Runtime probes and load experiments are needed for dispatcher saturation, blocking impact, latency, memory, and production-capacity claims.

At least one negative or interrupted path should accompany a consequential Kotlin change. A successful request alone cannot prove that absent input, cancellation, Java nullability, blocking, or typed failure semantics are safe.

**Known and unknown at this evolution boundary**

Known from local evidence: the inherited anti-pattern list, reliability stack, command examples, discovery commands, and review dimensions. Known from the frozen seed: the 26-section structure and retained public pointers. Reasoned here: how those controls form a dependency-ordered operating model. Unknown until target inspection: which tools are configured, which framework contracts apply, whether a nullable state is legitimate, whether a dependency blocks, and which operational thresholds are acceptable. No defect-reduction percentage, latency target, universal dispatcher size, or productivity result is claimed.

## Source Evidence Mapping Table

The source map answers two separate questions: where guidance can be retrieved and what a specific artifact is allowed to prove. A path or URL is not self-promoting evidence. Each claim needs an observed source span, a target-applicability decision, and evidence that closes the behavior under review.

| source_location_path_key | observed_state_in_this_evolution | claim_authority_and_limits | promotion_or_invalidation_rule |
| --- | --- | --- | --- |
| `agents-used-monthly-archive/codex-skills-202606/kotlin-coder-01/references/kotlin-quality-gates-and-anti-patterns.md` | Read completely; SHA-256 `1b393027a06d8a4ca7790822c9c29485bd3e8d59d77d7dfc310a8a761cb44400` | Canonical local source for the inherited anti-pattern list, reliability stack, command examples, command discovery, and compact review pass. It is not target runtime evidence. | Re-read and re-hash if the file changes. Adapt its recommendations to target build files, dependency versions, code paths, and tests before claiming target compliance. |
| `https://kotlinlang.org/docs/home.html` | `unrefreshed_no_browse`; retained from the frozen seed | Potential primary documentation root for Kotlin language and type-system questions. No current page, version, or supporting span was observed here. | Promote a specific claim only after authorized retrieval records page, retrieval date, relevant Kotlin version, supporting span, and target reproduction. |
| `https://github.com/Kotlin/kotlinx.coroutines` | `unrefreshed_no_browse`; retained from the frozen seed | Potential official repository evidence for coroutine APIs and implementation. A repository root does not by itself prove cancellation or dispatcher behavior in the target version. | Freeze the target dependency version and retrieve the relevant source, docs, tests, or release note; invalidate version-sensitive claims when the dependency changes. |
| `https://github.com/spring-guides/tut-spring-boot-kotlin` | `unrefreshed_no_browse`; retained from the frozen seed | Potential Spring-maintained example. An example demonstrates one designed composition and is neither a universal Spring contract nor evidence for the target application. | Use only after matching the target Spring/Kotlin versions and configuration; promote behavior through target tests or authoritative framework contracts. |
| `https://ktor.io/docs/welcome.html` | `unrefreshed_no_browse`; retained from the frozen seed | Potential primary Ktor documentation root. No current plugin, engine, lifecycle, or version behavior was inspected. | Retrieve the precise topic and version when a Ktor-specific uncertainty exists, then reproduce the relevant behavior in the target configuration. |

**Claim-specific evidence classes**

| evidence_class | can_support | cannot_support_alone | typical_capture |
| --- | --- | --- | --- |
| `local_guidance_observed` | What the mapped local reference explicitly recommends | That an unspecified target repository follows the recommendation or that the advice is current for every dependency version | Path, hash, heading/span, concise claim |
| `target_source_observed` | What the inspected Kotlin, Java, build, or configuration path contains | Unexecuted branch behavior, runtime frequency, or production impact | Commit/worktree identity, path/span, dependency/config context |
| `target_test_observed` | Behavior under named fixtures and execution environment | Behavior outside fixture population or production capacity | Command, test ID, fixture, pass/fail output summary |
| `compiler_or_analyzer_observed` | Findings modeled by the configured compiler, linter, or analyzer in the scanned population | Absence of defects outside its rule model or scan scope | Tool/version, configuration path, command, file population, result |
| `official_external_observed` | The precise versioned contract or implementation statement in the retrieved official artifact | Target applicability without version/configuration matching and reproduction | URL/revision, retrieval date, source span, version scope |
| `runtime_observed` | Dynamic timing, blocking, saturation, cancellation, memory, or failure behavior under the captured workload | Unmeasured workloads, causal generalization, or future release behavior | Build identity, environment, workload, sample design, raw result, uncertainty |
| `owner_policy_accepted` | A domain, lifecycle, security, or operational choice accepted by its accountable owner | Technical correctness of an implementation that has not been inspected or tested | Decision, owner role, scope, date, review trigger |
| `combined_evidence_inference_note` | A bounded recommendation connecting multiple observed classes | A newly observed fact or universal Kotlin rule | Premises, reasoning, alternatives, uncertainty, invalidation trigger |

**Default retrieval and promotion sequence**

1. Read the mapped local source and identify the exact inherited recommendation.
2. Inspect the target repository's wrappers, build files, dependency locks/catalogs, compiler options, analyzer configuration, and changed code path.
3. State the uncertainty as a falsifiable claim, such as "cancellation is swallowed by this catch" or "this Java return value reaches domain code as a platform type."
4. Use the least expensive evidence capable of falsifying that claim. Source may close a structural question; behavior requires a test or runtime probe.
5. Retrieve an external source only when a versioned language or framework uncertainty remains and browsing is authorized.
6. Record conflicts and choose authority by claim type. Repository policy can be intentionally stricter than upstream guidance, while target execution outranks prose for observed target behavior.
7. Attach an invalidation trigger. A coroutine dependency upgrade should reopen version-sensitive coroutine claims, not unrelated domain equality tests.

**Evidence hazards**

- `authority_by_brand`: treating an official root URL as if its relevant content had been retrieved and applied.
- `example_to_contract_promotion`: converting a Spring or Ktor tutorial design into a framework-wide or target-specific guarantee.
- `source_to_runtime_promotion`: inferring dispatcher saturation, latency, or production incidence from code inspection alone.
- `duplicate_lineage_counting`: presenting copies or derivative summaries as independent confirmation.
- `version_scope_erasure`: citing current-looking guidance without matching the target Kotlin, coroutine, framework, JVM, or build-tool version.
- `tool_green_overreach`: claiming general quality because configured checks pass even though their rule and file populations are narrower.
- `policy_behavior_conflation`: treating an owner-approved rule as proof that the implementation enforces it, or a passing test as authority to invent policy.

**Contrastive evidence cards**

Good: local guidance identifies swallowed cancellation as a hazard; target source shows `catch (Exception)` around a suspending call; a focused test cancels the parent and observes that the child terminates after `CancellationException` is rethrown. The claim is target-scoped and reproducible.

Bad: the `kotlinx.coroutines` repository URL is listed, so the review states that the service uses structured concurrency correctly. No dependency version, scope owner, code path, or cancellation evidence is recorded.

Borderline: official Kotlin documentation confirms a nullability rule, and target source contains a Java platform type, but no representative nullable return can be produced locally. The structural risk is observed; target behavior remains proposed or blocked until a fixture, contract test, or upstream Java annotation contract closes it.

The map is intentionally selective. A hash proves source identity, not correctness. A test proves behavior under its fixtures, not production frequency. An official source can establish a versioned contract, not target configuration. Keeping those limits visible is what makes later recommendations auditable instead of merely well cited.

## Pattern Scoreboard Ranking Table

The inherited numbers are preserved as historical editorial priorities. Their derivation, calibration population, and outcome data are not present in the seed, so `95`, `91`, and `88` are not percentages, confidence levels, defect-reduction measurements, or universal ordering weights. Current adoption is selected by target uncertainty and consequence.

| pattern_identifier_stable_key | inherited_editorial_value | current_qualitative_status | trigger_and_failure_prevention_target | override_or_stop_condition |
| --- | ---: | --- | --- | --- |
| `source_map_first_synthesis` | 95 | default when authority or repository convention is unclear | Load the mapped local Kotlin quality source and target repository evidence before synthesizing recommendations; prevents context-free generic advice. | A reproduced consequential failure may be contained first, but source and target evidence must be reconstructed before broader reuse. |
| `evidence_boundary_split_pattern` | 91 | default for every promoted claim | Separate observed local facts, observed target facts, unrefreshed external pointers, inference, proposals, and results; prevents source-brand authority and invented certainty. | No override for claim status; incident notes may be terse but must still distinguish observation from inference. |
| `verification_gate_coupling` | 88 | default before completion | Attach each consequential recommendation to a focused behavior check, project command, analyzer gate, review assertion, or explicitly blocked evidence need. | Documentation-only orientation may end with a review assertion, but implementation or runtime claims require stronger target evidence. |
| `boundary_uncertainty_normalization` | not scored | default when uncertain input crosses into domain logic | Parse or normalize serialized, Java, database, configuration, and user input once; prevents distant null crashes and repeated defensive branching. | Preserve `T?` when one absence state is genuinely the domain contract; route disputed state meaning to the domain owner. |
| `closed_domain_state_modeling` | not scored | default when callers need different actions | Use value objects, enums, sealed outcomes, or typed exceptions for closed distinctions; prevents boolean, null, or stringly failure ambiguity. | Open extension protocols or framework serialization constraints may justify a different representation with exhaustive boundary translation. |
| `caller_owned_coroutine_lifetime` | not scored | default for suspend and asynchronous work | Use structured scopes or actual lifecycle scopes, propagate cancellation, and keep failure ownership visible; prevents detached work and leaked cleanup. | Process-lifetime work needs explicit supervision, shutdown, durable state, and failure reporting rather than an accidental global scope. |
| `explicit_blocking_execution_boundary` | not scored | default when a dependency can block | Keep blocking APIs named or isolate known blocking work under an owned execution policy; prevents starvation hidden behind `suspend`. | Do not add dispatcher switches to genuinely nonblocking APIs or assume that switching makes an uninterruptible call cancellable. |
| `scoped_state_injection` | not scored | default for mutable collaborators and caches | Use constructor injection or lifecycle-scoped state; prevents test leakage, hidden coupling, and concurrency races from global singletons. | Immutable process constants are not mutable services; generated framework registries require framework-specific lifecycle evidence. |

**Adoption lifecycle**

| status | meaning | required evidence to enter | exit_or_invalidation |
| --- | --- | --- | --- |
| `candidate` | Pattern may address an observed uncertainty but target fit is not established. | Named failure or decision plus plausible target boundary. | Inspect target and promote, reject for scope, or route away. |
| `default_for_scope` | Pattern is the recommended starting action for the stated target and claim. | Applicable local guidance, target-path fit, and a planned falsification gate. | Target conflict, framework contract, or stronger local abstraction can adapt or supersede it. |
| `conditional_for_scope` | Pattern is useful only under explicit prerequisites or accepted costs. | Preconditions, owner, tradeoff, and verification method. | Promote when prerequisites are proven; reject when they fail. |
| `superseded_for_scope` | A repository-native or framework-owned mechanism closes the same risk more directly. | Replacement identity and equivalent or stronger evidence. | Reopen if the replacement is removed, upgraded incompatibly, or fails its contract. |
| `rejected_for_scope` | Applying the pattern would not reduce the target uncertainty or would violate a stronger contract. | Concrete mismatch and safer route. | Reconsider only when the target premise changes. |

**Consequence-based override rule**

The next gate is chosen by the highest unresolved consequence, not the largest inherited number. For example, a known `catch (Exception)` that swallows cancellation should be contained and regression-tested before polishing source-map prose. Conversely, an unfamiliar repository with no reproduced defect should establish source and target authority before introducing a new result abstraction, analyzer, or dispatcher policy.

**Application signatures**

- Source-map-first is applied when every recommendation can point to a local source, target artifact, explicit inference, or unresolved evidence need.
- Evidence-boundary split is applied when unvisited URLs are not described as observed facts and test scope is not generalized beyond its fixtures.
- Verification coupling is applied when a reviewer can name the command, test, analyzer, inspection, owner decision, or blocked condition for each consequential claim.
- Boundary normalization is applied when domain code receives validated Kotlin types or typed failures rather than platform or transport uncertainty.
- Structured coroutine ownership is applied when parentage, cancellation, failure propagation, and cleanup can be traced for the changed work.
- Blocking isolation is applied when the actual dependency behavior, execution owner, saturation boundary, and cancellation limits are explicit.

**Anti-gaming rules**

Do not count mentions, table rows, passing commands, or pattern adoption frequency as quality outcomes. A pattern is useful only when it changes a code, test, review, routing, or stop decision. A green analyzer cannot promote behavior it does not model. A frequently selected pattern is not necessarily sufficient. A lower-frequency pattern can be decisive for a high-consequence boundary.

**Feedback without false precision**

Record deterministic facts first: the pattern selected, uncertainty addressed, evidence run, finding, decision, and invalidation trigger. Over time, a repository may track repeated finding categories, review reversals, escaped defects, or rework, but those trends need stable classification and comparable cohorts. Until such data exists, the register remains a qualitative retrieval index and decision history rather than a scored effectiveness model.

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: One mapped local file was read completely. It supplies concrete guidance about `!!`, Java platform types, `GlobalScope`, cancellation handling, scope-function nesting, nullable domain fields, data-class identity, hidden blocking, boolean results, mutable global state, boundary normalization, typed failures, risk-focused tests, and repository-native commands.

`external_pointer_unrefreshed`: No external source was retrieved during this evolution. Public rows are possible future authorities for precise language or framework questions, not evidence that a current external contract was checked.

`combined_evidence_inference_note`: Kotlin quality is the preservation of information and ownership as data and work cross boundaries. An idiom is preferred when it makes the caller's obligations, lifecycle, failure states, execution policy, and verification surface more explicit. Familiar syntax without those properties is not sufficient.

The thesis is implemented as a causal pipeline:

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

**1. Uncertain ingress**

Uncertainty enters through transport payloads, configuration, environment variables, databases, serialization, Java APIs, reflection, framework injection, user input, and external dependencies. First identify what is actually uncertain: presence, format, authorization, version, lifecycle, thread behavior, or failure class. A generic null check cannot preserve distinctions that were never named.

**2. Boundary normalization**

Convert uncertainty once at the narrowest owned edge. A Java platform value should become `T`, `T?`, or a typed parse/contract failure before domain logic. A raw identifier should become a validated value object when validity changes caller behavior. Boundary normalization is not an instruction to remove all nullable types; it is an instruction to make each nullable type mean one deliberate absence state.

**3. Explicit domain states and identity**

Use the least complex representation that keeps consequential states distinct. An enum can represent a closed label set. A sealed hierarchy can require exhaustive handling of success, rejection, absence, conflict, dependency failure, or another closed outcome family. A plain class can protect identity and lifecycle when generated data-class equality, `copy`, or destructuring would be invalid. Typed exceptions may fit framework boundaries when the exception taxonomy and translation owner are explicit.

The representation is wrong when two states requiring different caller actions collapse into `null`, `false`, an empty string, or one broad exception. It is also wrong when elaborate type machinery distinguishes states that no caller, test, operation, or policy treats differently.

**4. Owned execution and state lifetime**

Every asynchronous task needs a lifetime owner, cancellation path, failure destination, and cleanup rule. Prefer structured scopes or actual framework lifecycle scopes over detached work. `supervisorScope` is not a generic resilience switch; use it only when one child failure should not cancel siblings and the parent still accounts for each outcome. Catch cancellation separately and rethrow it unless the API contract explicitly translates cancellation at a boundary that owns that translation.

Mutable state likewise needs an owner. Constructor-injected or lifecycle-scoped state exposes dependencies and test reset semantics. A mutable global singleton hides both. Immutable constants and framework-managed registries are separate cases and should be judged by their actual mutation and lifecycle contracts.

**5. Explicit blocking and failure policy**

The `suspend` modifier does not make a call nonblocking. Inspect the dependency. If callers must choose execution policy, expose a named blocking API. If an adapter owns a known blocking dependency, isolate it on an appropriate owned dispatcher, bound concurrency where needed, and document whether cancellation interrupts the underlying operation or merely stops waiting for its result. Do not add a dispatcher switch to a genuinely nonblocking API, and do not present a thread switch as proof of capacity.

Expected failures should be distinguishable from programmer defects and cancellation. A sealed result, enum, value object, or typed exception is useful when it forces the required handling. A boolean flag is adequate only when its two meanings are obvious, exhaustive, and require no different diagnostic or recovery information.

**6. Caller-visible outcome**

Trace each modeled state to a caller decision. If every branch is immediately mapped to one generic response, the new distinction may belong at another layer or may be unnecessary. If callers currently infer retry, denial, or absence from message text or null, the contract is underspecified. The final representation should make illegal or forgotten handling harder without imposing ceremony unrelated to behavior.

**7. Claim-matched verification**

Choose evidence by the claim:

| claim | minimum useful evidence | stronger evidence when needed |
| --- | --- | --- |
| Platform type is contained | Target source trace and boundary conversion test | Java contract fixture or versioned upstream contract |
| Closed states are handled | Compilation plus focused branch tests | Property or integration tests across serialization/persistence boundaries |
| Cancellation propagates | Deterministic coroutine cancellation test | Framework lifecycle integration test and cleanup observation |
| Blocking is isolated | Dependency inspection and execution-boundary test | Thread/dispatcher instrumentation and representative load experiment |
| Identity semantics are correct | Equality, copy/lifecycle, persistence, or collection behavior tests as applicable | Framework integration and migration evidence |
| Project gates pass | Actual repository wrapper commands with tool/config population | CI reproduction on the supported matrix |
| Production impact is acceptable | Not established by source or unit tests | Controlled runtime measurement with workload, environment, samples, and uncertainty |

A gate can be explicitly not applicable, unavailable, or blocked. It cannot be silently assumed green. At least one negative, absent, cancelled, malformed, equality-sensitive, or blocking branch should accompany a consequential claim.

**8. Selective learning and invalidation**

When a gate exposes a recurring mechanism, move the guarantee earlier: strengthen an adapter, introduce a shared value object, provide a structured coroutine helper, clarify a framework boundary, or configure an existing analyzer rule. Do not generalize from one occurrence merely to create more process. Shared controls need a shared causal mechanism, ownership, migration path, and regression evidence.

Invalidate only what changed. A Java library annotation update reopens platform-type assumptions. A coroutine dependency upgrade reopens version-sensitive cancellation or dispatcher claims. A domain policy change reopens state modeling. A formatter change does not invalidate a boundary parse test. This keeps evidence current without turning every change into a full re-audit.

**Scope and refusal**

This thesis does not decide domain meaning, framework lifecycle policy, security/privacy requirements, persistence identity, or production capacity without the appropriate owner and target evidence. When those are missing, the correct output is a named uncertainty, the owner or source needed, a safe containment boundary, and the condition for resuming. Locating an unresolved decision before it leaks into `null`, `lateinit`, dispatcher choice, equality, or default retry behavior is itself a successful Kotlin quality result.

## Local Corpus Source Map

The local corpus for this theme contains one mapped reference, not several independent confirmations. It was read completely because its brevity and internal progression matter: named hazards lead to a reliability sequence, executable gate discovery, and a handoff review pass.

| local_source_filepath_value | identity_and_role | stable_guidance_contribution | prohibited_inference |
| --- | --- | --- | --- |
| `agents-used-monthly-archive/codex-skills-202606/kotlin-coder-01/references/kotlin-quality-gates-and-anti-patterns.md` | Read-only archive reference; SHA-256 `1b393027a06d8a4ca7790822c9c29485bd3e8d59d77d7dfc310a8a761cb44400`; canonical source for inherited theme content in this assignment | Ten named Kotlin hazards, eight reliability checks, Gradle/Maven command examples, build/tool discovery commands, and six review dimensions | Does not prove target tool configuration, framework/version behavior, production capacity, organizational policy acceptance, or that every listed construct is unconditionally forbidden |

**Heading-level semantic map**

| source_heading | contribution_to_decision | target_closure_needed | invalidation_trigger |
| --- | --- | --- | --- |
| `High-Value Anti-Patterns` | Supplies causal review signals for `!!`, platform types, detached coroutine work, cancellation swallowing, scope-function opacity, nullable state collapse, data-class identity mismatch, hidden blocking, boolean ambiguity, and mutable global state. | Inspect whether the construct occurs on the changed path, whether its hazardous interpretation applies, and whether a bounded exception has an owner and test. | Target refactor, framework contract change, new legitimate exception, or repeated escaped failure. |
| `Default Reliability Stack` | Orders boundary parsing, non-null domain modeling, hazard review, typed failure, structured concurrency, blocking treatment, risk-focused tests, and existing gates. | Map each applicable item to a target path and mark non-applicable items with a reason. | Domain state, concurrency model, dependency behavior, or repository gate changes. |
| `Quality Gate Commands` | Gives representative wrapper commands and commands for discovering build/configuration before introducing tools. | Inspect actual wrappers, modules, task names, profiles, and analyzer configuration; run only commands that exist for the target. | Build-system or CI configuration changes. |
| `Review Pass` | Supplies compact handoff prompts for nullability, interop, types, coroutines, tests, and gates. | Attach findings and evidence to the changed path rather than returning six context-free green labels. | Change scope expands or a new boundary/failure class is discovered. |

**Complete local facts preserved from the source**

The anti-pattern table recommends:

- parse once, return typed failure, or retain explicit `T?` instead of using `!!` in production paths;
- normalize Java platform types in adapters instead of allowing nullability uncertainty into domain code;
- use caller-owned, structured, or lifecycle scopes instead of `GlobalScope` for real work;
- catch and rethrow `CancellationException` before translating broader suspend-work failures;
- replace unclear nested `let`/`also`/`apply` chains with named locals or a simpler function;
- use sealed outcomes or typed value objects when nullable fields conflate several domain states;
- prefer plain or framework-specific classes when data-class equality, `copy`, or destructuring conflicts with identity/lifecycle;
- isolate known blocking work or keep the blocking contract explicit instead of hiding it in `suspend`;
- replace ambiguous boolean result flags with named closed outcomes when callers need distinct meaning;
- replace mutable global singletons with constructor-injected or lifecycle-scoped state.

The reliability stack then asks whether boundaries are normalized, domain absence is meaningful, new assertion and interop hazards are contained, expected failures are typed, structured cancellation is preserved, blocking is deliberate, high-risk behavior is tested, and existing repository gates were run or explicitly skipped with a reason.

The command section intentionally says to use repository-native commands and wrappers. Its examples are possibilities, not requirements:

```bash
./gradlew test
./gradlew build
./gradlew ktlintCheck
./gradlew detekt
./mvnw test
./mvnw verify
```

Before choosing among them, inspect the target:

```bash
rg --files -g 'build.gradle*' -g 'settings.gradle*' -g 'pom.xml'
rg 'ktlint|detekt|kotest|junit|mockk|turbine|kotlinx-coroutines-test' .
```

The examples do not authorize adding a formatter, analyzer, or test library. They establish a discovery discipline: prefer wrappers, prove configuration, use actual task/module/profile names, and explain a skipped applicable gate.

**Flexible-entry control loop**

The source need not be applied from its first heading on every task. Enter at the observed failure, then close adjacent dependencies:

1. Diagnose the concrete hazard and its causal path.
2. Check whether boundary or domain-state ambiguity created it.
3. Repair ownership, cancellation, blocking, identity, or state scope as applicable.
4. Add the smallest behavior evidence that could fail if the repair regresses.
5. Run configured project gates for the affected population.
6. Use the six review dimensions to confirm that the fix did not move uncertainty elsewhere.

For example, a broad catch around a suspending client call enters at coroutine cancellation. The review must still ask what outcome the caller receives, whether cleanup runs, and which focused test proves parent cancellation. It need not redesign unrelated identifiers or add an analyzer.

**Reuse and conflict protocol**

Reuse this reading while the hash, task scope, and interpretation remain unchanged. Re-read when the source changes or when a new task depends on a different heading interaction. If target code, configured compiler/analyzer behavior, current official version evidence, or accountable owner policy conflicts with the archive guidance, record the conflict by claim. A target can be intentionally stricter than upstream guidance; an archive example cannot override an observed target contract silently.

The local source is canonical for what this assignment inherited, not exhaustive for Kotlin or authoritative over every platform. Its strongest safeguard is self-limiting: inspect the project before inventing a toolchain, and adapt every recommendation to the actual boundary it is meant to protect.

## External Research Source Map

No external page was opened. Every row below is a queued retrieval surface with `unrefreshed_no_browse` status. The seed's `external_research_sourced_fact` category is retained as historical source-role metadata, but it must not be read as a statement that current content was observed.

| external_source_url_value | current_status | decision_trigger | required_retrieval_and_target_closure |
| --- | --- | --- | --- |
| `https://kotlinlang.org/docs/home.html` | `unrefreshed_no_browse` | A precise Kotlin language or type-system question remains unresolved, such as nullability, Java interop, equality generation, sealed exhaustiveness, or exception behavior. | Retrieve the specific official topic, record date and relevant Kotlin version/span, freeze target compiler settings, and compile or test the target case. |
| `https://github.com/Kotlin/kotlinx.coroutines` | `unrefreshed_no_browse` | A version-sensitive coroutine API, cancellation, structured-concurrency, dispatcher, testing, or implementation question remains after target inspection. | Record target artifact version, retrieve the relevant docs/source/tests/release material at a revision, and reproduce parent/child/cancellation behavior in the target. |
| `https://github.com/spring-guides/tut-spring-boot-kotlin` | `unrefreshed_no_browse` | A Spring Boot Kotlin composition example is needed for project structure, binding, testing, or framework integration. | Match Spring/Kotlin/JVM versions and plugins, classify the artifact as an example, adapt to target configuration, and verify through target tests or stronger framework contracts. |
| `https://ktor.io/docs/welcome.html` | `unrefreshed_no_browse` | A Ktor-specific server/client plugin, engine, lifecycle, testing, or integration question remains. | Retrieve the precise versioned topic, match target engine/plugins, and reproduce behavior in the configured application or test host. |

**Research entry contract**

External retrieval begins only after a small decision packet exists:

| field | required content |
| --- | --- |
| `unresolved_claim` | One falsifiable question that local source and target inspection did not close. |
| `target_identity` | Repository revision/worktree, Kotlin/JVM and relevant dependency versions, module, framework/plugins, and build configuration. |
| `why_external_is_needed` | The missing language, API, lifecycle, migration, or implementation contract. |
| `preferred_authority` | Official language docs, official project docs, implementation/tests, release notes, or maintained guide, selected for the claim type. |
| `stop_condition` | The source span and target evidence that would accept, adapt, reject, or keep the claim blocked. |
| `allowed_action` | Read-only orientation, implementation guidance, migration decision, or completion evidence. |

If local code and tests already close the claim, skip external research. Avoiding a broad browse is not a knowledge failure; it preserves attention and prevents unrelated authoritative-looking material from changing a bounded decision.

**Promoted external evidence packet**

When browsing is authorized and an external source affects implementation, capture:

- exact URL and, where available, immutable revision, tag, release, or commit;
- retrieval date and source type;
- product/library and version scope;
- concise supporting span or faithful paraphrase;
- intended claim and explicit non-claims;
- target dependency/configuration match;
- target reproduction command, test, or source trace;
- conflicts with local policy or target behavior;
- adoption outcome: accept, adapt, reject for scope, informative only, or blocked;
- invalidation trigger and refresh owner.

An official root page without a supporting topic is discovery metadata. A mutable default branch without a commit is weak identity. A guide is an example unless it links to a normative contract. Implementation internals can explain behavior but may not be a stable API promise. These distinctions should survive into the final review note.

**Authority by question type**

| question_type | preferred external evidence | target evidence still required |
| --- | --- | --- |
| Kotlin language/nullability semantics | Specific official Kotlin documentation and, when necessary, compiler behavior for the target version | Compile/test fixture using target compiler options and Java annotations |
| Coroutine contract/API | Versioned official coroutine documentation, source, tests, or release notes | Target dependency version plus deterministic coroutine test |
| Spring composition | Version-matched Spring reference material or maintained guide, with guide status visible | Target application configuration and integration test |
| Ktor composition | Version-matched Ktor topic and relevant engine/plugin contract | Target plugin/engine configuration and application/test-host behavior |
| Runtime throughput or saturation | External material may suggest mechanisms or experiment design | Controlled target measurement; external numbers do not substitute |
| Domain or organizational policy | External examples can reveal alternatives | Accountable local owner decision and enforcement evidence |

**Conflict and mismatch handling**

If external guidance differs from the local source, classify the disagreement. A newer API may supersede an implementation example while leaving the local principle intact. A repository may intentionally require a stricter rule. A target test may expose configuration-specific behavior that a general guide does not cover. Record the claim, both scopes, and the chosen authority; do not resolve a conflict merely by preferring whichever source looks newer.

If versions do not match, external evidence can remain informative for test design but cannot be promoted directly. For example, a Spring guide on a different major version may suggest how to structure a binding test, yet every API call and lifecycle assumption must be adapted and verified. If an official example cannot be reproduced, the mismatch is evidence to investigate, not a reason to claim success or silently abandon the discrepancy.

**Current no-results ledger**

| source | observed_current_content | target_reproduction | current_allowed_use |
| --- | --- | --- | --- |
| Kotlin documentation root | none | none | Future retrieval routing only |
| `kotlinx.coroutines` repository root | none | none | Future retrieval routing only |
| Spring Boot Kotlin guide repository | none | none | Future retrieval routing only |
| Ktor documentation root | none | none | Future retrieval routing only |

This no-results state is deliberate. It prevents public source names from being used as synthetic support while preserving a precise route for future versioned questions. If a later authorized refresh adopts one claim, invalidate and update only the affected nullability, coroutine, Spring, or Ktor guidance rather than treating all four rows as a single freshness switch.

## Anti Pattern Registry Table

An anti-pattern entry is a review hypothesis, not a token ban. Confirm that the hazardous interpretation occurs on an owned path, identify the contract lost, and then choose the smallest replacement that restores caller-visible meaning or ownership.

| anti_pattern_failure_name | lost_contract_and_likely_failure | safer_default_or_containment | legitimate_exception_boundary | detection_and_verification |
| --- | --- | --- | --- | --- |
| `non_null_assertion_on_uncertain_path` | `!!` converts unresolved presence into a distant `NullPointerException`, often after boundary context is lost. | Parse/normalize once, return typed failure, or preserve deliberate `T?` and force handling. | A proven invariant immediately adjacent to the assertion, with framework or test evidence and no asynchronous/state gap. | Search owned production paths for `!!`; trace origin; exercise null/malformed input and assert boundary outcome. |
| `broad_lateinit_temporal_state` | Access order becomes an implicit runtime state, creating uninitialized crashes, races, or stale test/lifecycle values. | Constructor injection, explicit nullable lifecycle state, delegated validation, or framework-owned binding with narrow scope. | Test fixture or framework lifecycle establishes initialization-before-access and teardown/reset semantics. | Search `lateinit`; map writer/readers, threads, lifecycle transitions, and negative access tests. |
| `platform_type_domain_leakage` | Java nullability uncertainty becomes invisible and spreads assertion or defensive branching into domain code. | Normalize in a Java/Kotlin adapter into `T`, `T?`, or typed failure. | A single reviewed interop shim may retain the platform type while converting before export. | Inspect Java signatures/annotations and Kotlin inferred types; fixture nullable returns; prove no platform value crosses the adapter. |
| `detached_global_coroutine_work` | `GlobalScope` work outlives caller/lifecycle, loses cancellation and failure ownership, and complicates shutdown/testing. | Caller-owned scope, `coroutineScope`, deliberate `supervisorScope`, or actual framework lifecycle scope. | True process-lifetime work has explicit supervisor, durable state, shutdown, failure telemetry, and owner. | Search scope creation/launch; trace job parent; cancel caller/lifecycle; assert child termination and cleanup. |
| `cancellation_swallowed_by_broad_catch` | `catch (Exception)` around suspend work can translate cooperative cancellation into failure, fallback, or retry. | Catch `CancellationException` first and rethrow; then translate only expected failures. | A boundary that owns cancellation translation defines and tests the caller-visible contract explicitly. | Search broad catches in suspend paths; deterministic parent cancellation test; observe cleanup and no fallback/retry side effect. |
| `opaque_scope_function_nesting` | Nested `let`/`also`/`apply`/`run` chains obscure receiver, return value, mutation, null branch, and exception location. | Named locals, guard clauses, extraction, or one scope function whose semantics remain obvious. | A short local chain has one unambiguous receiver and no mixed mutation/return/failure effects. | Review receiver aliases and returned expression; mutate one branch in a test or extract until ownership is readable. |
| `nullable_field_state_collapse` | One `null` conflates absent, invalid, forbidden, unknown, not loaded, or failed states that require different actions. | Value object, enum, sealed state/outcome, or separate optional value plus explicit status. | `null` genuinely means one absence state and all callers treat it identically. | Enumerate caller actions for each state; compile for exhaustiveness; test serialization/persistence and every consequential branch. |
| `data_class_identity_mismatch` | Generated structural equality, `copy`, `componentN`, and hash behavior conflict with entity identity, persistence lifecycle, proxying, or invariants. | Plain class, explicit equality, immutable value type, or framework-specific model. | The object is a true value and all generated operations are valid and invariant-preserving. | Test equality before/after identity assignment, set/map membership, copy invariants, persistence/framework integration, and destructuring exposure. |
| `hidden_blocking_inside_suspend` | A blocking dependency occupies constrained threads while the API implies cooperative suspension; cancellation may only stop waiting. | Keep a named blocking API or isolate known blocking work on an owned dispatcher with bounded concurrency. | No isolation is needed for a genuinely nonblocking API; a tiny controlled blocking call still needs an explicit contract. | Inspect dependency implementation/docs; capture thread/dispatcher; cancel during call; instrument queue/saturation under representative load before capacity claims. |
| `boolean_outcome_semantic_erasure` | `true`/`false` cannot carry whether work was rejected, absent, conflicting, retryable, or terminal; callers guess recovery. | Named enum, sealed outcome, value object, or typed exception taxonomy. | A private predicate with obvious yes/no semantics and no diagnostic or recovery distinction. | Inspect all callers; list actions per value; introduce exhaustive handling test or compile-time branch coverage. |
| `mutable_global_singleton_state` | Tests leak state, concurrent callers race, dependencies hide, and lifecycle/reset ownership is unclear. | Constructor injection, immutable shared value, request/session/application scope, or explicitly synchronized owned cache. | Immutable process constants or framework registries with documented lifecycle are separate from mutable service state. | Search object/static mutable fields; run order-randomized or concurrent tests; verify reset, shutdown, and owner. |
| `result_wrapper_without_error_taxonomy` | A generic wrapper or `Result<Any>` can move ambiguity rather than modeling expected failures, and `runCatching` can capture cancellation or programmer defects indiscriminately. | Closed domain outcome or narrow typed exception translation; keep cancellation and defects distinct. | Local transformation of a known exception set can use `Result` when callers preserve distinctions and cancellation is not swallowed. | Inspect producer and every fold/getOrElse; cancel suspend path; assert error classification and no accidental retry. |
| `dispatcher_switch_as_nonblocking_proof` | `withContext(Dispatchers.IO)` is treated as proof of scalability or cancellability even when work is unbounded or uninterruptible. | Document the dependency, execution owner, concurrency bound, interruption semantics, and measurement plan. | A repository-owned dispatcher policy may encapsulate these controls and evidence. | Inspect actual call and dispatcher config; measure active/queued work and thread use; test cancellation separately from interruption. |
| `context_free_summary_output` | An agent skips local and target evidence, producing generic Kotlin advice disconnected from build, framework, and changed path. | Source-map-first plus target-path inspection and an explicit no-claim boundary. | Pure orientation may remain generic if it is labeled and does not direct implementation or completion. | Verify mapped source identity, target files/config read, and claim-to-evidence links. |
| `unsourced_recommendation_claims` | Guidance sounds authoritative while observed local facts, external facts, target evidence, and inference are blended. | Evidence-boundary split with claim status and invalidation trigger. | Stable reasoning may be stated as inference without a citation when its premises and limits are explicit. | Audit promoted claims for source class, target closure, version scope, and prohibited inference. |
| `unverified_agent_instruction` | A recommendation cannot be falsified by a test, command, review assertion, owner decision, or explicit blocked condition. | Verification-gate coupling selected from the claim. | Documentation-only orientation can end with a precise review check rather than execution. | Require a gate signature and population for every consequential completion claim. |

**Finding disposition**

Each observed candidate ends in one of these states:

- `confirmed_defect`: the contract loss and target consequence are observed; repair and regression evidence are required.
- `conditional_hazard`: the dangerous interpretation is plausible, and a named invariant or behavior test is still needed.
- `bounded_exception`: invariant, owner, scope, and verification make the construct acceptable on this path.
- `accepted_risk`: an accountable owner accepts a stated consequence and review trigger; this is not the same as safe.
- `not_applicable`: generated/framework-owned/nonproduction context or absent mechanism makes the hazard irrelevant, with reason recorded.
- `blocked`: domain, framework, dependency, security, or operational authority is missing; do not manufacture a replacement.

**Common compound failure chains**

| initial_contract_loss | downstream_chain | root-first correction |
| --- | --- | --- |
| Platform type enters domain | repeated safe calls -> one `!!` -> distant crash -> generic retry | Normalize at interop adapter and model failure before retry policy. |
| Detached coroutine owns blocking call | caller completes -> work persists -> pool saturates -> failure has no destination | Restore lifecycle parent, then make blocking/concurrency policy explicit. |
| Broad catch swallows cancellation | timeout/cancel -> translated failure -> fallback or retry -> duplicate side effect | Rethrow cancellation before classifying retry and side effects. |
| Nullable field hides load/failure state | UI/service treats unknown as absent -> overwrites or suppresses recovery | Separate lifecycle state from optional value and test caller actions. |
| Boolean result hides conflict | caller interprets `false` as retryable -> repeats non-idempotent operation | Introduce closed outcomes and couple each to an explicit recovery action. |
| Mutable singleton contaminates tests | earlier test leaves state -> later test passes/fails by order -> false confidence in fix | Scope/inject state, reset ownership, and randomize or isolate tests. |

Prioritize the earliest loss of information or ownership. Removing a downstream `!!` while retaining platform-type spread may move the crash. Adding `Dispatchers.IO` while retaining detached work may hide saturation. Adding a sealed outcome while every caller maps it back to boolean may add ceremony without preserving meaning.

**Contrastive Kotlin examples**

Good: an adapter calls a Java API, explicitly checks its nullable contract, returns `CustomerLookup.Found`, `.Missing`, or `.DependencyFailure`, and a caller-owned suspend use case handles each outcome. Tests cover Java null, cancellation, and dependency failure.

Unsafe: domain code accepts a platform `String!`, asserts it with `!!`, starts detached work, catches `Exception`, executes a blocking client, writes a mutable singleton cache, and returns `false` on every failure. Each construct erases a different obligation.

Conditional: a framework-injected test property uses `lateinit`, but the test extension establishes initialization before each test, teardown cannot race access, and no production code reads it. Record it as a bounded fixture exception rather than redesigning production dependency injection.

**Population-aware detection**

Search is a candidate generator. Record included roots, exclusions, generated code policy, and baseline so "no findings" has a denominator. Then inspect semantics and run behavior evidence. A clean `rg '!!'` scan cannot prove Java nullability containment, and a cancellation test cannot prove every broad catch is safe. Completion requires the gates relevant to the confirmed failure mechanism.

## Verification Gate Command Set

`verification_gate_command_set`: Select gates from the claim and target repository. Discover wrappers, modules, tasks, profiles, and analyzer configuration before running or recommending a command. A green command proves only its modeled assertions over its actual population.

**Gate dependency order**

```text
G0 target and tool discovery
  -> G1 focused behavior reproduction
  -> G2 compile and build integration
  -> G3 configured lint/static-analysis population
  -> G4 semantic Kotlin review checks
  -> G5 broader regression and supported matrix
  -> G6 runtime experiment for runtime claims
  -> G7 reference artifact verification when this document changes
```

Later gates do not repair missing earlier evidence. A successful build does not prove cancellation. A clean analyzer does not prove domain-state meaning. A focused behavior test does not prove production saturation.

**G0: discover the target before choosing commands**

Use repository-native wrappers and inspect build/configuration first. The mapped local source provides these representative discovery commands:

```bash
rg --files -g 'build.gradle*' -g 'settings.gradle*' -g 'pom.xml'
rg 'ktlint|detekt|kotest|junit|mockk|turbine|kotlinx-coroutines-test' .
```

Also inspect wrapper presence, modules, version catalogs, compiler options, CI workflows, and custom scripts. On Gradle targets, task discovery can be useful when allowed by the project, but the exact invocation depends on wrapper and project configuration. Do not infer that `ktlintCheck` or `detekt` exists merely because it appears below.

**G1: run the narrowest behavior gate**

Choose a test that fails if the target semantic distinction regresses:

- Nullability/interoperability: nullable Java return, malformed input, missing field, and adapter export type.
- Closed states: every caller-relevant branch, serialization/persistence round-trip where applicable, and exhaustive handling.
- Cancellation: cancel the parent or lifecycle, observe child termination, cleanup, and absence of fallback/retry side effects.
- Blocking: observe execution context, cancellation semantics, and concurrency behavior for the actual dependency.
- Identity: equality/hash, collection membership, copy/lifecycle invariants, persistence/proxy behavior as applicable.
- State scope: repeated, reordered, parallel, teardown, restart, and reset behavior.

Example Gradle syntax, only after target task/module discovery:

```bash
./gradlew :module:test --tests 'package.ClassName.testName'
```

Example Maven syntax, only after target module/profile discovery:

```bash
./mvnw -pl module -Dtest=ClassName#testName test
```

Record the expected pre-fix failure mechanism when doing test-first work. A test that fails because the environment is missing is not evidence for the intended Kotlin defect.

**G2: compile and build integration**

Representative inherited commands are:

```bash
./gradlew test
./gradlew build
./mvnw test
./mvnw verify
```

Use the repository's actual aggregate or module commands. Compilation is especially useful for exhaustive sealed handling, type changes, Java/Kotlin interop, visibility, and API compatibility. Build success remains narrower than runtime or semantic correctness.

**G3: configured lint and static analysis**

Representative inherited Gradle tasks are:

```bash
./gradlew ktlintCheck
./gradlew detekt
```

Run them only when target configuration proves they exist. Capture tool/plugin version, configuration/baseline path, included modules/source sets, exclusions, and result. A baseline can suppress known findings; generated or test code may be excluded. State the population before claiming no findings.

**G4: semantic Kotlin review checks**

Search creates candidate sets and requires manual path review. Adjust roots/exclusions to the target:

```bash
rg -n '!!|lateinit|GlobalScope|catch\s*\(\s*(?:[A-Za-z_][A-Za-z0-9_]*\s*:\s*)?Exception' src
rg -n 'withContext\s*\(\s*Dispatchers\.IO|runCatching|object\s+[A-Za-z_][A-Za-z0-9_]*' src
rg -n '\.let\s*\{|\.also\s*\{|\.apply\s*\{|\.run\s*\{' src
```

These patterns are intentionally incomplete. They can miss aliases, fully qualified names, custom dispatchers, Java catches, generated code, and semantic equivalents. They can also report legitimate fixtures and bounded exceptions. Record candidate population, inspect the path, and attach behavior evidence before classifying a defect.

Manual review should answer:

1. Where does uncertainty enter, and where is it normalized?
2. Do nullable or boolean states collapse caller actions?
3. Do equality and generated data-class operations match lifecycle identity?
4. Who owns every coroutine, mutable state object, cancellation, failure, and cleanup path?
5. Which calls actually block, and who owns execution policy and concurrency bounds?
6. Which expected failures are translated, and can cancellation or defects be captured accidentally?

**G5: broader regression and supported matrix**

After the focused mechanism is understood, run the repository's broader unit, integration, build, and supported-target gates. Attribute unrelated failures rather than hiding or reclassifying them. A local change can have valid focused evidence while a shared suite remains red for another owner; completion must report both states and the boundary between them.

**G6: runtime claims require runtime evidence**

Source, tests, and static checks cannot establish production latency, dispatcher saturation, thread use, memory, throughput, or capacity. A runtime gate needs build identity, environment, dependency behavior, warmup, workload distribution, concurrency, samples, percentiles only when statistically meaningful, raw results, counter-metrics, and uncertainty. Compare equivalent outputs and correctness before comparing speed.

**G7: verify this evolved reference**

The current focused verifier for one 202607 reference is:

```bash
python3 tests/verify_idiomatic_reference_file.py --path idiomatic-ref-202607/kotlin_quality_antipattern_gates-20260710.md
```

It checks the archive/working section contract and matching packet shape, including raw and prefix-stripped normalized uniqueness. It does not prove that every Kotlin recommendation is correct for a target application, so editorial and source-boundary review still apply.

The frozen seed's historical 202606 command remains preserved for provenance:

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

Treat it as a legacy archive verifier unless its current scope is inspected and deliberately selected. It is not a substitute for the 202607 focused verifier or target Kotlin behavior gates.

**Gate result schema**

| field | required content |
| --- | --- |
| `gate_id_and_claim` | What the gate is intended to falsify. |
| `command_or_review_assertion` | Exact command or deterministic inspection. |
| `cwd_module_target` | Repository identity, working directory, module/profile/source set, and supported target. |
| `tool_and_configuration` | Wrapper/tool/plugin version, config/baseline, relevant environment. |
| `population_or_fixture` | Files, tests, inputs, schedules, or workload included and excluded. |
| `result_state` | `pass`, `fail`, `blocked`, `unavailable`, `not_applicable`, or `expected_external_red`. |
| `evidence_summary` | Exit status, key assertion/finding, concise diagnostic; avoid unneeded raw logs and secrets. |
| `owner_and_next_transition` | Repair, changed-premise retry, route, accepted risk, or completion owner. |

Retry a gate only when a premise changes: code, fixture, configuration, dependency, environment, or command selection. Repeating the same flaky or failing command without classification creates volume, not confidence.

## Agent Usage Decision Guide

`agent_usage_decision_guide`: Use this reference when a Kotlin task requires a decision about boundary uncertainty, nullability, Java interop, domain-state representation, identity semantics, coroutine ownership, cancellation, blocking, mutable state, expected failures, or quality-gate evidence. A keyword or mapped path opens the reference; it does not authorize edits, dependency additions, broad migration, network research, commits, or releases.

**Default state machine**

| state | entry condition | allowed action | exit evidence |
| --- | --- | --- | --- |
| `orient` | Task intent, target, write boundary, or supported environment is unclear. | Read instructions, build files, dependency/configuration context, mapped source, and relevant target path. | Concrete scope, owner, permissions, and candidate claim. |
| `inspect` | A candidate anti-pattern or quality claim is named but not confirmed. | Trace data/work ownership, callers, generated/framework boundaries, and existing tests/gates. | Confirmed defect, bounded exception, not-applicable result, or unresolved evidence need. |
| `reproduce` | Behavior is consequential and a deterministic fixture is feasible. | Add or run the smallest test/probe that exercises the lost distinction. | Intended failure mechanism observed, or hypothesis rejected/reframed. |
| `design` | Contract loss is understood and alternatives affect callers or lifecycle. | Compare bounded options, state tradeoffs, choose authority, and define verification before editing. | Chosen route with prerequisites and rollback/containment. |
| `implement` | User intent permits edits and target contract is sufficiently explicit. | Make the smallest coherent change, including boundary and caller updates required for correctness. | Focused behavior passes and no known contract remains half-migrated. |
| `verify` | Implementation or completion claim is ready. | Run claim-matched focused, build, analyzer, broader, and runtime gates as applicable. | Results classified with populations and unresolved risks. |
| `route` | Domain, framework, Java dependency, persistence, security/privacy, or operations authority is missing. | Preserve evidence, identify owner/source, offer safe containment or test sketch. | Owner decision or authoritative artifact arrives. |
| `blocked` | Required permission, input, environment, or consequential decision is unavailable. | Stop affected action, persist exact condition and non-destructive next step. | Blocking condition changes. |
| `handoff` | Work is complete for current scope or crosses ownership. | Summarize changed paths, behavior, commands/results, skipped gates, risks, invalidation, and next owner. | Reviewer accepts or returns a specific gap. |

States can be skipped when evidence already exists, but their obligations cannot be silently assumed. A pure explanation request can move from `orient` to `handoff` without edits. A reproduced cancellation defect may move quickly from `inspect` to `implement`, yet still needs a target contract and focused gate.

**Intent and permission checks**

Before acting, answer:

1. Is the user asking for explanation, review, diagnosis, implementation, migration, or verification?
2. Which files and repositories may be read or written?
3. Are network access, dependency changes, generated-code changes, build execution, commit, push, or deployment authorized?
4. Is the target production code, tests, generated code, example code, build logic, or documentation?
5. Which owner decides domain meaning, lifecycle, persistence identity, security/privacy, and operational limits?

When the user requests analysis only, return evidence and decisions rather than editing. When write scope is narrow, do not create helper files or change shared configuration merely to simplify the agent's workflow. When a task is explicitly broad, expand scope through an inventory and staged plan rather than an implicit search-and-replace.

**Operational modes**

| mode | choose_when | required_output | not_allowed_without_transition |
| --- | --- | --- | --- |
| `review_only` | User asks for findings or code cannot be changed. | Ordered findings with path/line, consequence, evidence, and suggested gate. | Editing or claiming the fix is complete. |
| `focused_repair` | One confirmed mechanism has bounded callers and tests. | Minimal coherent patch plus focused and relevant broad evidence. | Opportunistic repository cleanup. |
| `characterization_first` | Existing semantics are ambiguous or legacy behavior must be preserved before redesign. | Tests labeled as observed behavior, discrepancy ledger, and owner decision needed for desired contract. | Presenting current behavior as correct policy. |
| `adapter_containment` | Interop or framework uncertainty cannot yet be removed globally. | Narrow adapter, explicit exported contract, tests, and remaining boundary. | Allowing uncertainty to spread beyond the adapter. |
| `staged_migration` | Shared type, global state, coroutine architecture, or identity model has broad blast radius. | Inventory, compatibility strategy, stages, rollback, ownership, and per-stage gates. | One-shot mechanical replacement without characterization. |
| `specialist_route` | Missing decision belongs to another discipline or owner. | Exact question, evidence gathered, consequence, safe interim state, and return contract. | Inventing policy or production thresholds. |

**Good trajectory**

An agent reviewing a Kotlin service sees a Java client return value used as a platform type. It reads the adapter and callers, confirms that `null` currently becomes `!!`, adds a fixture returning null, observes the boundary crash, proposes `CustomerLookup.Missing` versus `.DependencyFailure`, updates the adapter and exhaustive callers, runs the focused test and repository-native gates, and reports external docs as unnecessary for this target-scoped fix.

**Unsafe trajectory**

An agent searches the repository for `!!`, `lateinit`, and `data class`, replaces every match, adds Detekt because the local source mentions it, wraps all blocking-looking calls in `Dispatchers.IO`, and reports success after compilation. It has not established semantics, ownership, tool permission, dependency behavior, or tests.

**Conditional trajectory**

An agent finds a framework-owned persistence entity implemented as a data class. Generated equality may conflict with identity, but the framework version, proxy behavior, and migration blast radius are unclear. The agent records the finding, writes a focused identity/equality characterization test if permitted, routes the framework contract question, and does not convert the class until evidence chooses the model.

**Overreach and underreach controls**

Overreach signals include repository-wide lexical edits, unrequested tool or dependency installation, framework replacement, invented domain states, guessed dispatcher limits, external research without permission, or claiming broad completion from narrow gates.

Underreach signals include repeating generic caveats after target evidence is available, refusing a bounded adapter fix because broader architecture is imperfect, or routing the entire task when only one policy decision needs another owner. Continue useful source tracing, fixture design, containment, and option analysis within authority.

**Minimal action and handoff ledger**

Record high-level decision rationale rather than hidden thought:

| ledger_field | content |
| --- | --- |
| `intent_and_scope` | User goal, allowed paths/actions, target behavior. |
| `evidence_loaded` | Material local source, target paths/config, and any authorized external artifact. |
| `claim_or_failure` | Lost distinction or ownership, consequence, and current evidence state. |
| `decision` | Keep, repair, adapt, route, block, or accept risk, with reason and alternatives. |
| `changes` | Exact changed paths and contract surface. |
| `verification` | Commands/review assertions, populations, results, and external reds. |
| `uncertainty` | Missing owner/evidence, no-claim boundary, and invalidation trigger. |
| `next_condition` | Specific evidence or decision that unlocks the next action. |

For long-running work, persist at meaningful boundaries and resume from the latest evidence rather than memory. For small work, one concise handoff can satisfy the same contract. The purpose is not ceremony; it is preventing context loss, scope drift, fabricated gate status, and duplicate work.

## User Journey Scenario

This scenario is illustrative. It describes no inspected repository, measured workload, or achieved outcome. Its purpose is to show how the gates change decisions when a Kotlin service wraps a blocking Java fraud client whose return is a platform type.

**Role and starting state**

A Kotlin service maintainer is asked to stop sporadic request failures in a checkout-risk path. The existing adapter calls a Java method that may return null, launches the call in detached work, catches broad exceptions, writes a process-global cache, and returns a boolean. The happy-path test passes. It is unknown whether null means "no match," dependency failure, stale result, or a Java contract violation. The Java call is suspected to block, but no target measurement exists.

Illustrative unsafe shape:

```kotlin
suspend fun checkRisk(orderId: String): Boolean {
    return try {
        GlobalScope.async {
            cache[orderId] = javaRiskClient.lookup(orderId)!!.score
            true
        }.await()
    } catch (error: Exception) {
        false
    }
}
```

This snippet intentionally combines several hazards. A real review must confirm each one rather than assuming the example matches a target.

**Journey phase 1: freeze intent and authority**

The maintainer records:

- Goal: preserve a meaningful risk outcome and request cancellation without a platform-type crash.
- Allowed scope: adapter, use case, callers, and tests; no dependency upgrade or global cache redesign without approval.
- Domain question: what should Java null mean to checkout policy?
- Operational question: does the Java call block, and what execution/concurrency policy owns it?
- Completion split: semantic correctness can be verified locally; production capacity remains unclaimed until measured.

If the domain owner cannot distinguish null states, implementation stops short of a public outcome name. The adapter can still preserve `JavaNull`, `ClientFailure`, and `Value` internally so information is not destroyed while policy is pending.

**Journey phase 2: inspect target and dependency**

The maintainer discovers actual wrappers, modules, Kotlin/JVM and dependency versions, existing test libraries, coroutine utilities, static-analysis configuration, and client implementation or contract. They trace all `checkRisk` callers and cache ownership. They do not run or add `detekt` merely because the local source mentions it.

Evidence questions:

| question | evidence sought | possible transition |
| --- | --- | --- |
| Can Java return null? | Java annotations/source, existing mocks, integration behavior | Confirm platform-type uncertainty or reject the null hypothesis. |
| What does null mean? | Domain owner decision and existing caller behavior | Name a domain state, preserve provisional technical state, or block public translation. |
| Does the call block? | Client implementation/docs and controlled thread observation | Keep blocking explicit, isolate on owned dispatcher, or retain nonblocking path. |
| Who owns coroutine lifetime? | Job parent, request/lifecycle scope, shutdown path | Use existing structured scope or design a bounded owner. |
| What does `false` mean? | Every caller branch and recovery action | Keep predicate only if truly binary; otherwise introduce closed outcome. |
| Who owns cache lifetime? | Scope, synchronization, reset, stale-data policy | Inject/scoped cache, retain immutable/no-op state, or route broader redesign. |

**Journey phase 3: write discriminating tests**

Before choosing final representation, the maintainer creates the smallest feasible fixtures:

1. Java client returns null. The current implementation should fail for the expected assertion path, not because the fixture cannot start.
2. Java client throws a known dependency exception. The test records current translation separately from desired policy.
3. Parent request/test scope is cancelled after the client boundary is entered. Synchronization proves the child has started before cancellation; cleanup and absence of fallback/cache mutation are asserted.
4. Two callers require different actions for missing versus dependency failure. This demonstrates why boolean is insufficient.
5. Repeated or parallel tests expose whether the global cache leaks state or races.

If deterministic cancellation cannot reach or interrupt the opaque blocking client, the test must observe whether cancellation returns promptly or is delayed until the call completes; it must not assume either behavior. It can separately assert that no forbidden post-cancellation side effect is committed. It cannot claim the underlying native or Java operation stopped.

**Journey phase 4: choose bounded contracts**

Assume, for illustration, that the domain owner decides null means no score was available, while dependency exceptions are operational failures. A possible internal contract is:

```kotlin
sealed interface RiskLookup {
    data class Found(val score: RiskScore) : RiskLookup
    object Missing : RiskLookup
    data class DependencyFailure(val cause: RiskClientFailure) : RiskLookup
}
```

This is not universally preferable to typed exceptions or `RiskScore?`. It is justified only because callers take different actions for missing and failure. If every caller treats both identically and no observability/recovery distinction exists, a simpler contract may be better.

For the blocking boundary, choose among:

| observed premise | route | boundary that remains |
| --- | --- | --- |
| Client is genuinely nonblocking/suspending | Call in structured scope without an unnecessary dispatcher switch. | Verify cancellation and failure contract. |
| Client blocks and adapter owns execution policy | Isolate on a repository-owned blocking dispatcher or policy with explicit concurrency limits. | Underlying call may remain uninterruptible; measure saturation before capacity claims. |
| Client blocks and callers must choose execution policy | Expose a named blocking adapter API. | Callers own dispatcher/thread and must preserve lifecycle. |
| Work must survive request/process lifecycle | Route to durable job architecture with idempotency, persistence, and operations ownership. | This reference alone is insufficient for queue/durability design. |

Detached `GlobalScope` is removed because request work does not meet the process-lifetime exception contract. Cancellation is rethrown before translating expected dependency failures. Cache mutation is either removed from the focused repair or moved behind an injected owner with explicit policy and tests.

**Journey phase 5: implement as one coherent boundary**

The adapter translates Java uncertainty. The use case owns structured execution. Callers handle every outcome. Tests and framework mapping change in the same coherent patch where required. Avoid a half-migration in which the adapter returns `RiskLookup` but callers immediately convert it back to `Boolean` and recreate ambiguity.

A conceptual shape is:

```kotlin
suspend fun lookupRisk(orderId: OrderId): RiskLookup =
    withContext(blockingClientDispatcher) {
        try {
            javaRiskClient.lookup(orderId.value)
                ?.let { raw -> RiskLookup.Found(RiskScore.parse(raw.score)) }
                ?: RiskLookup.Missing
        } catch (cancelled: CancellationException) {
            throw cancelled
        } catch (failure: KnownRiskClientException) {
            RiskLookup.DependencyFailure(RiskClientFailure.from(failure))
        }
    }
```

The example assumes the adapter owns dispatcher policy and that parsing cannot silently throw an unmodeled exception. A target implementation must decide those premises explicitly. If the Java call is uninterruptible, cancellation of the Kotlin continuation does not prove interruption of the call.

**Journey phase 6: layered verification**

The maintainer runs:

- null, known-failure, caller-branch, cancellation, and cache/state-isolation tests;
- the actual module's compile/test/build commands;
- configured lint/static-analysis tasks, with population and baseline recorded;
- broader repository gates, attributing unrelated failures;
- a thread/concurrency experiment only if making blocking-impact or capacity claims.

The handoff separates states:

| claim | illustrative completion state |
| --- | --- |
| Platform type no longer leaves adapter | Verified by target source trace and null fixture. |
| Missing and dependency failure remain distinguishable | Verified by closed outcome and caller tests. |
| Parent cancellation is not translated into failure/fallback | Verified by synchronized cancellation test. |
| Underlying Java call is interrupted | Unverified unless dependency contract or probe observes interruption. |
| Dispatcher capacity is acceptable in production | Unmeasured; requires operations-owned experiment and SLO. |
| Global cache semantics are safe | Verified only if included in the repair; otherwise separately routed. |

**Journey phase 7: rollback and selective follow-up**

If caller migration or framework mapping fails, retain the adapter normalization and use a compatibility translation at one boundary rather than reverting to platform-type leakage. If runtime probing shows unacceptable blocking saturation, route to client replacement, bounded pool/concurrency design, or durable asynchronous architecture. Do not respond by adding more detached coroutines.

The local fix creates a hypothesis for sibling Java adapters: search and inspect them only with explicit scope. One verified occurrence is not proof that every adapter shares the same contract. Promote shared helpers or analyzer rules after recurring semantics, ownership, and migration value are established.

## Decision Tradeoff Guide

Use a tradeoff table only when alternatives change a consequential caller, lifecycle, failure, persistence, or operational contract. For a private predicate with obvious binary meaning, direct code and a focused test are enough.

**State representation**

| option | choose_when | principal_cost_or_risk | verification_signature |
| --- | --- | --- | --- |
| `T?` | Exactly one absence state exists and every caller takes the same action for absence. | Cannot distinguish invalid, forbidden, unknown, failed, or not-loaded states later. | Inventory callers; null branch test; serialization/persistence behavior where applicable. |
| Enum | Closed named states carry no distinct payload and expansion is controlled. | Adding states can break consumers; cannot encode state-specific data without another structure. | Exhaustive `when`; compatibility and serialization tests. |
| Sealed state/outcome | Closed states require different payloads or caller actions and exhaustive handling is valuable. | More types and migration work; framework serialization/mapping may need adapters. | Compile-time exhaustiveness, every consequential branch, boundary round-trip. |
| Typed exception | Framework or API naturally propagates failures and stack/context are useful. | Hidden control flow, accidental broad catch, cross-boundary taxonomy leakage. | Exact catch/translation tests, cancellation separation, framework mapping. |
| `Result<T>` | A narrow API has one understood failure channel and callers preserve its meaning. | Generic failure wrappers can capture defects/cancellation or erase taxonomy. | Inspect producer/callers, failure classification, cancellation test for suspend paths. |

Default: use the simplest option that preserves every state requiring a different caller action. A sealed hierarchy is not automatically superior to `T?`; it becomes justified when null would erase a decision.

**Value versus lifecycle identity**

| option | choose_when | principal_cost_or_risk | verification_signature |
| --- | --- | --- | --- |
| Data class | The object is an immutable value and generated equality, hash, `copy`, and destructuring are all valid. | Generated operations can violate entity identity, invariants, proxies, or lifecycle. | Equality/hash law tests, copy invariant tests, collection and framework behavior. |
| Plain class with explicit identity | Lifecycle or stable identity differs from all-field structural value. | More code and deliberate equality decisions; fewer convenience operations. | Identity before/after persistence, collection membership, proxy/framework integration. |
| Framework-specific model | Framework contract governs construction, proxying, serialization, or lifecycle. | Couples domain representation to framework and may weaken portability. | Versioned framework contract and target integration tests. |
| Separate persistence/transport and domain models | Boundaries have incompatible identity or nullability contracts. | Mapping code and potential drift. | Mapper round-trips, invariant tests, version/migration coverage. |

Default: data classes for values, deliberate classes for identity-heavy lifecycle objects, and boundary mapping when one representation cannot honestly satisfy both contracts.

**Coroutine failure ownership**

| option | choose_when | principal_cost_or_risk | verification_signature |
| --- | --- | --- | --- |
| `coroutineScope` | Child failure should cancel sibling work and the parent owns all results. | One child failure stops the group, which may be inappropriate for independent work. | Parent/child failure and cancellation tests; cleanup observation. |
| `supervisorScope` | Child failures are independent and the parent explicitly accounts for each result. | Can hide failures when results are launched and ignored; not a generic resilience wrapper. | One-child-fails fixture, sibling behavior, result accounting, parent cancellation. |
| Framework lifecycle scope | UI/request/application lifecycle is authoritative. | Incorrect lifecycle choice can leak work or cancel too early. | Lifecycle transition integration tests and shutdown/cleanup evidence. |
| Durable queue/job | Work must survive caller or process lifetime and be recovered operationally. | Persistence, idempotency, retries, monitoring, and operations complexity. | Durable state, duplicate/restart tests, operational ownership. |
| Process-lifetime supervised scope | Work genuinely exists for the entire process. | Shutdown, failure, and lost state risks if supervision is incomplete. | Explicit owner, supervisor, shutdown, telemetry, and durability policy. |

Default: structured caller or lifecycle ownership. Choose supervision only when failure independence is a stated requirement. Route survival requirements to durable architecture rather than detached coroutine work.

**Blocking execution boundary**

| option | choose_when | principal_cost_or_risk | verification_signature |
| --- | --- | --- | --- |
| Named blocking API | Caller has the information and authority to choose thread/execution policy. | Less convenient for suspend callers and may spread execution decisions. | API naming/review, caller execution tests, blocking behavior documented. |
| Adapter-owned dispatcher isolation | Adapter owns a known blocking dependency and repository policy supplies a suitable dispatcher/concurrency bound. | Thread switch can hide saturation; cancellation may not interrupt work. | Dependency inspection, execution-context test, cancellation versus interruption, queue/thread measurement for capacity claims. |
| Nonblocking suspend call | Dependency is genuinely asynchronous/cooperative. | Unnecessary dispatcher switching adds overhead and obscures execution. | Versioned dependency contract and target cancellation test. |
| Durable asynchronous job | Work is long-running, retryable, or must outlive the request/process. | Architectural and operational complexity. | Persistence/idempotency/recovery/monitoring contract. |

Default: do not infer nonblocking behavior from `suspend`. Inspect the dependency and place execution policy with the owner best able to bound it.

**State ownership**

| option | choose_when | principal_cost_or_risk | verification_signature |
| --- | --- | --- | --- |
| Constructor injection | Collaborator or mutable state has object/request/application ownership visible to callers. | Wiring overhead and potentially wider constructor changes. | Construction graph, isolated tests, lifecycle teardown. |
| Explicit lifecycle scope | Framework owns creation and disposal. | Scope mismatch can leak or stale state. | Framework lifecycle integration and reset/shutdown test. |
| Owned synchronized cache | Shared cache is required with explicit consistency, eviction, and concurrency policy. | Race, staleness, memory, and operational complexity. | Concurrent tests, eviction/staleness behavior, metrics, owner. |
| Mutable global singleton | Almost never the default for service state. | Hidden dependency, test contamination, races, unclear reset/shutdown. | Requires exceptional process-wide contract and equivalent evidence to an owned cache. |

**Repair scope**

| route | choose_when | cost | stop_or_rollback |
| --- | --- | --- | --- |
| Focused local repair | Confirmed defect has bounded callers and regression fixture. | May leave sibling hazards untouched. | Stop at coherent boundary; record sibling hypothesis without claiming inventory. |
| Adapter containment | External/framework uncertainty cannot yet be removed globally. | Mapping layer and temporary dual models. | Keep uncertainty from exporting; add owner and review trigger. |
| Compatibility shim | Public/persistence contract cannot migrate atomically. | Duplicate semantics can become permanent. | Equivalence tests, one owner, deprecation/review condition, rollback path. |
| Staged migration | Shared model, global state, or concurrency ownership spans modules. | Inventory, sequencing, temporary compatibility, and coordination cost. | Per-stage gates and rollback; do not begin without ownership. |
| Route or block | Domain, framework, security, persistence, or operations decision is missing. | Slower implementation but avoids invented policy. | Resume on named owner decision or evidence artifact. |

**Adopt, adapt, avoid**

- Adopt a local pattern when target semantics, ownership, compatibility, and verification align.
- Adapt when the principle is sound but framework, public API, persistence, or migration constraints require a boundary translator or staged path.
- Avoid when the option erases a caller distinction, hides lifetime/execution ownership, relies on unverified framework behavior, or lacks authority for a consequential policy.
- Route when evidence is strong about the technical risk but authority is missing for the desired domain or operational contract.

**Cost of being wrong**

Wrong state modeling causes callers to retry, deny, overwrite, or ignore incorrectly. Wrong identity semantics corrupt equality, collections, persistence, or lifecycle. Wrong coroutine ownership leaks work or loses failure. Wrong blocking policy starves threads or creates misleading cancellation. Wrong migration scope breaks public/persistence compatibility. These costs grow with API visibility, persisted data, shared callers, concurrency, irreversibility, and operational coupling.

Every durable decision should record the rejected alternatives and the premise that made them lose. Reopen the decision only when that premise changes: a new caller needs another state, framework version changes identity behavior, work must outlive its lifecycle, the dependency becomes nonblocking, or runtime evidence invalidates the execution policy.

## Local Corpus Hierarchy

Classification vocabulary includes `canonical_for_claim`, `supporting`, `legacy`, `duplicate_lineage`, `conflicting`, `target_descriptive`, `target_behavioral`, and `owner_normative` roles. These roles form a partial order by claim; they are not one universal ranking.

Confidence warning: only one local corpus source is mapped. It is canonical for the inherited content of this assignment, but no adjacent-source inventory or current organizational policy designation was performed. Do not convert archive path placement into a claim of enterprise-wide authority.

| local_source_filepath_value | role_for_this_assignment | claim_scope | target_closure |
| --- | --- | --- | --- |
| `agents-used-monthly-archive/codex-skills-202606/kotlin-coder-01/references/kotlin-quality-gates-and-anti-patterns.md` | `canonical_for_inherited_guidance` | Exact ten anti-patterns, reliability stack, representative command/discovery guidance, and review dimensions. | Inspect target code/configuration, run relevant tests/gates, and obtain owners for domain/lifecycle/operations choices. |

**Role definitions**

| role | meaning | authority limit |
| --- | --- | --- |
| `canonical_for_claim` | Preferred source for a specific definition, policy, or inherited guidance statement. | Does not automatically prove target implementation or runtime behavior. |
| `supporting` | Adds an independent explanation, example, test, or narrower detail consistent with the claim. | Contribution and lineage must be named; source count alone adds no confidence. |
| `legacy` | Preserves history or applies to an older tool/version/workflow. | Use for migration or rationale, not current behavior without revalidation. |
| `duplicate_lineage` | Same or derivative content under another path/name. | One evidence family; useful for drift detection, not independent corroboration. |
| `conflicting` | Makes a materially different recommendation or reports different behavior for the same scope. | Keep both visible until claim scopes and authority resolve the disagreement. |
| `target_descriptive` | Target code/configuration establishes what currently exists. | Existing behavior may be defective and is not desired-policy authority. |
| `target_behavioral` | Tests or runtime evidence establish behavior under a named population. | Does not generalize beyond fixtures/environment or invent desired semantics. |
| `owner_normative` | Accountable domain/framework/security/operations owner chooses desired policy or accepted risk. | Does not prove implementation enforces the choice. |

**Authority by claim**

| claim | primary authority | required corroboration or closure |
| --- | --- | --- |
| What anti-pattern guidance was inherited? | Mapped archive reference and hash. | Faithful section mapping and evidence-boundary review. |
| What build/analyzer tasks exist? | Target wrappers, build files, plugins, CI configuration. | Actual command/task discovery and result population. |
| What code currently does? | Target source and generated/framework configuration. | Caller trace and behavior test where consequential. |
| What code should mean? | Domain/API/lifecycle owner plus relevant local policy. | Desired-contract tests and migration/compatibility plan. |
| How Kotlin/compiler/library version behaves? | Versioned official contract or implementation plus target configuration. | Target compile/test reproduction. |
| What happens under selected fixtures? | Target test output. | Fixture validity, population, and limits. |
| What happens under runtime load? | Controlled target runtime observation. | Environment/workload identity, correctness equivalence, samples, uncertainty, operations review. |
| Whether risk is acceptable? | Accountable owner for domain, security/privacy, framework, or operations surface. | Evidence summary, consequence, alternatives, and review trigger. |

**Conflict resolution procedure**

1. Split the disagreement into descriptive, normative, behavioral, versioned-contract, and operational claims.
2. Confirm source identity and scope. Two differently named files may share one lineage; two tests may use different fixtures.
3. State the material consequence. If choosing either side changes no caller, behavior, gate, operation, or accepted risk, resolve it as local presentation.
4. Assign authority by claim. Target code describes current implementation; it does not prove correctness. Owner policy defines desired meaning; it does not prove enforcement. Tests observe fixtures; they do not choose policy.
5. Preserve characterization and desired-contract evidence separately when migrating legacy behavior.
6. Choose accept, adapt, stage, reject for scope, or block, and record the premise and invalidation trigger.

**Conflict examples**

Good: the archive source prefers typed outcomes to boolean flags. Target callers take three different recovery actions, and the domain owner confirms those distinctions. Target tests establish current boolean behavior; new desired-contract tests drive a staged sealed-outcome migration. Each artifact has a different authority role.

Bad: target code uses `GlobalScope`, so a review declares detached work canonical because "the code is the source of truth." The code proves current use only; lifecycle and failure ownership remain unverified.

Borderline: target tests pass for a data-class persistence entity, but they characterize structural equality that the owner intends to replace with database identity. Preserve the passing characterization tests, add desired identity tests, and stage migration; do not call either test set universally correct without its contract label.

**Adjacent local discovery trigger**

Search for another local source only when a named gap remains, for example:

- framework lifecycle or persistence-model behavior absent from the mapped source;
- repository-specific compiler, lint, baseline, or wrapper policy;
- organizational policy for nullable APIs, result types, or accepted assertions;
- shared coroutine/dispatcher/state helpers whose contract could supersede direct application;
- migration history explaining a current exception.

Record candidate identity, heading contribution, lineage, version/freshness, claim role, conflict, and target closure. More files are not the goal. The goal is the minimum diverse evidence needed to make the next consequential decision.

**Selective invalidation**

The mapped source changing invalidates claims about inherited guidance. Build changes invalidate task/tool availability. Dependency upgrades invalidate related version behavior. Domain policy changes invalidate state meaning. New runtime evidence invalidates operational assumptions. None of those changes automatically invalidates unrelated, deterministic boundary tests.

This claim-specific hierarchy keeps the single-source warning honest without making progress impossible. One source is sufficient to establish what it says. It is insufficient to establish everything a target Kotlin system does, should do, or can sustain.

## Theme Specific Artifact

Theme-specific artifact: **Kotlin Quality Evidence Packet (KQEP)**, a claim-oriented quality bar with review blockers, configured gate results, bounded exceptions, release criteria, and explicit no-claim states. The schema is proposed by this reference; no target organization adoption or efficiency result is asserted.

**Profile selection**

| profile | choose_when | minimum burden |
| --- | --- | --- |
| `compact` | One private or module-local distinction changes, with bounded callers and no persistence/concurrency/public API effect. | Goal, target, one claim/finding, decision, focused evidence, relevant project gate, uncertainty. |
| `standard` | Boundary, domain state, interop, coroutine, blocking, identity, or shared state changes with multiple callers or integration effects. | Full core schema, finding dispositions, claim-to-gate matrix, rollback, and handoff. |
| `migration` | Public API, persisted model, shared global state, framework entity, or concurrency architecture changes across modules/owners. | Full schema plus inventory, compatibility, stages, per-stage gates, rollback, ownership, and completion split. |

Profiles change evidence volume, not honesty. A compact packet still cannot report a skipped applicable test as green.

**Core schema**

| artifact_field_name | completion_rule | example_evidence_source |
| --- | --- | --- |
| `packet_identity` | Stable packet/change ID and current state. | Review or work item identifier. |
| `user_goal_and_non_goals` | Concrete behavioral goal plus explicitly excluded cleanup, tooling, migration, and operational claims. | User request and scope confirmation. |
| `target_identity` | Repository/worktree revision, module/source set, Kotlin/JVM, framework/dependency, and build profile relevant to the claim. | Build files, version catalog/lock, wrapper, CI. |
| `write_and_action_boundary` | Allowed files/actions and network/dependency/commit/release permissions. | User/owner instruction. |
| `boundary_and_caller_map` | Where uncertainty/work enters, exported contract, callers, lifecycle owner, side effects, and generated/framework edges. | Target source trace and dependency map. |
| `claim_inventory` | Stable claim IDs with local fact, target fact, inference, desired contract, and no-claim labels. | Source map, code, tests, owner decisions. |
| `finding_dispositions` | Every candidate is confirmed, conditional, bounded exception, accepted risk, not applicable, or blocked. | Anti-pattern registry plus target inspection. |
| `state_and_identity_contract` | Meaning of null/closed states, equality, copy, persistence, and caller actions as applicable. | Domain/API decision and tests. |
| `execution_and_state_ownership` | Coroutine parent/lifecycle, cancellation/failure/cleanup, blocking owner, concurrency bound, mutable-state scope. | Code trace, framework contract, tests/probes. |
| `decision_and_alternatives` | Adopt/adapt/route/block choice, rejected alternatives, tradeoffs, and invalidation premise. | Decision Tradeoff Guide. |
| `change_surface` | Exact changed paths/symbols/contracts and compatibility impact. | Diff and caller inventory. |
| `gate_matrix` | Claim -> command/review assertion -> population -> result -> owner. | Verification Gate Command Set. |
| `exceptions_and_accepted_risk` | Invariant, scope, evidence, accountable owner, consequence, and review trigger. | Exception test and owner decision. |
| `blockers_and_completion_split` | Semantic, integration, operational, release, and external-owner states remain distinct. | Gate outcomes and route records. |
| `rollback_or_containment` | Reversible action, compatibility boundary, data/state considerations, and trigger. | Migration or incident plan. |
| `observability_and_privacy` | Evidence needed after change without logging secrets or high-cardinality sensitive data. | Runtime/operations contract. |
| `handoff_and_invalidation` | Changed paths, evidence, skipped gates, unresolved risks, next owner, and source/code/version changes that reopen claims. | Journal or review summary. |

**Claim record**

Each consequential claim uses a small record:

| claim_field | meaning |
| --- | --- |
| `claim_id` | Stable local identifier such as `KQ-NULL-001`. |
| `claim_text` | Falsifiable target-scoped statement. |
| `claim_class` | Boundary, state, identity, coroutine, blocking, failure, mutable state, gate, or runtime. |
| `evidence_state` | Observed local, observed target source, observed test, observed runtime, inference, proposal, owner policy, blocked, or no claim. |
| `support_and_limit` | Evidence that supports it and the population/non-claim boundary. |
| `verification` | Focused assertion and broader applicable gates. |
| `decision` | Accept, adapt, repair, route, block, or accepted risk. |
| `invalidation` | Specific change that requires re-review. |

**Review blockers**

| blocker_level | condition | release_effect |
| --- | --- | --- |
| `B0_integrity` | Packet/target identity is unknown, required source cannot be read, or evidence is attributed to the wrong artifact. | Stop; no reliable decision can be made. |
| `B1_semantic` | Null/state/identity/failure meaning is unresolved for a changed consequential contract. | Block public/production promotion; containment may proceed without collapsing states. |
| `B2_ownership` | Coroutine, cancellation, blocking, mutable state, cleanup, or side-effect owner is absent. | Block implementation completion for the affected path. |
| `B3_behavior` | Focused negative/cancellation/equality/boundary test is missing or fails for the intended mechanism. | Block behavior claim. |
| `B4_integration` | Compile/build/configured analyzer or supported matrix fails due to the change. | Block integration/release according to repository policy. |
| `B5_operational` | Runtime capacity, saturation, or resilience claim lacks measurement/operations acceptance. | Semantic change may complete, but operational promotion claim remains blocked. |
| `B6_external` | Another owner/lane/shared suite remains red outside this change. | Report and route; local completion is possible only when repository policy permits and scope is explicit. |

Passing a lower-numbered blocker does not imply later gates. A `B5` no-capacity-claim is not a semantic defect. A `B6` external red must not be hidden or "fixed" through unauthorized files.

**Exception contract**

A bounded exception to a default records:

1. Exact construct and path.
2. Dangerous interpretation being excluded.
3. Invariant that makes use acceptable.
4. Owner and lifetime/scope.
5. Test, framework contract, or analyzer evidence.
6. Consequence if the invariant fails.
7. Review or removal trigger.

"Framework needs it" or "tests pass" is not enough without the precise lifecycle or behavior being relied on.

**Illustrative compact packet**

| field | illustrative value |
| --- | --- |
| `goal` | Convert a Java client's nullable risk response before domain code and preserve parent cancellation. |
| `non_goals` | No global cache migration and no production throughput claim. |
| `claim KQ-NULL-001` | Platform type does not leave `RiskClientAdapter`. |
| `claim KQ-CANCEL-002` | Parent cancellation is rethrown and causes no fallback/cache mutation. |
| `finding` | Existing `!!` and broad catch are confirmed on the adapter path; dispatcher capacity is conditional/unmeasured. |
| `decision` | Introduce closed adapter outcome, caller-owned scope, cancellation-first catch; retain blocking isolation only under existing dispatcher policy. |
| `focused evidence` | Java-null fixture and synchronized parent-cancellation test. |
| `project gates` | Actual target module test/build and configured analyzer tasks; command names discovered from target. |
| `completion split` | Null/cancellation semantics verified; underlying Java interruption and production capacity remain no-claim. |
| `rollback` | Keep adapter normalization and restore compatibility mapping at one caller boundary if public migration fails. |

All values above are illustrative. They demonstrate schema semantics, not a completed change.

**Artifact acceptance**

Structural acceptance confirms required fields, stable claim IDs, evidence links, result states, populations, nonempty blockers, and explicit next conditions. Semantic acceptance confirms that states correspond to caller actions, owners are real, exception invariants are credible, and the evidence can falsify each claim. Automation can help with the first group; it cannot replace the second.

The KQEP is complete only relative to its declared claims. Adding generic prose to every field is failure. Marking a field `not_applicable` with a reason is valid. Marking it green without evidence is not.

## Worked Example Set

All fixtures below are illustrative. They express causal contracts and test designs, not observed target code, framework-version guarantees, measured performance, or copy-ready APIs.

**Fixture A: Java platform nullability**

Unsafe:

```kotlin
fun loadName(id: String): CustomerName =
    CustomerName(javaDirectory.find(id).name!!)
```

The Java result and property can be platform types. `!!` converts uncertainty into a crash after the adapter has already lost whether the customer, name, or dependency was absent.

Safer primary route: inspect the Java contract and normalize in the adapter into a closed result such as found, missing, malformed, or dependency failure only when callers need those distinctions. Domain code receives `CustomerName` or a typed outcome, never `String!`.

Conditional route: use `CustomerName?` when exactly one absence state exists and every caller takes the same action. A sealed hierarchy would be needless ceremony in that contract.

Evidence: Java-null and malformed fixtures; source trace showing no platform type leaves the adapter; exhaustive caller tests. Remaining uncertainty: upstream version contract until directly inspected or retrieved.

**Fixture B: cancellation and broad catch**

Unsafe:

```kotlin
suspend fun refresh(): RefreshOutcome = try {
    remote.refresh()
    RefreshOutcome.Updated
} catch (error: Exception) {
    RefreshOutcome.Failed(error.message.orEmpty())
}
```

If cancellation is an `Exception` on this path, the function can turn caller cancellation into ordinary failure, telemetry, fallback, or retry.

Safer primary route:

```kotlin
suspend fun refresh(): RefreshOutcome = try {
    remote.refresh()
    RefreshOutcome.Updated
} catch (cancelled: CancellationException) {
    throw cancelled
} catch (failure: KnownRemoteFailure) {
    RefreshOutcome.DependencyFailure(RemoteFailure.from(failure))
}
```

Conditional route: a framework boundary may intentionally translate cancellation into its own response or state, but that boundary must own the contract and prove cleanup and absence of unintended side effects.

Evidence: synchronize until `remote.refresh()` is entered, cancel the parent, assert child termination/cleanup, and assert no failure fallback or retry. Remaining uncertainty: whether an opaque underlying blocking call is actually interrupted.

**Fixture C: value versus lifecycle identity**

Unsafe premise:

```kotlin
data class AccountEntity(
    val id: Long?,
    val email: String,
    val status: String,
)
```

The syntax is not automatically unsafe. Risk appears when generated all-field equality, `hashCode`, `copy`, or destructuring conflicts with persistence identity, proxies, status transitions, or invariants.

Good value case: `Money(currency, minorUnits)` is immutable, all fields define value, and copy/equality are intended. A data class is a strong fit.

Safer identity route: use a plain/framework-specific entity with deliberate identity semantics and map to immutable value/DTO types at boundaries.

Borderline route: retain a framework-required data class during migration, characterize equality before/after identity assignment, and prevent use as a mutable set/map key until the owner chooses the model.

Evidence: equality/hash laws, collection membership, copy invariant, persistence/proxy integration, and serialization tests as applicable. Remaining uncertainty: framework/version behavior without target integration.

**Fixture D: hidden blocking in suspend work**

Unsafe:

```kotlin
suspend fun readInvoice(id: InvoiceId): Invoice =
    legacyJdbcClient.read(id.value)
```

The `suspend` modifier does not change the client's blocking behavior. A caller can reasonably but incorrectly assume cooperative suspension.

Safer adapter-owned route:

```kotlin
suspend fun readInvoice(id: InvoiceId): Invoice =
    withContext(blockingDispatcher) {
        legacyJdbcClient.read(id.value)
    }
```

This route is only safer when the dependency is confirmed blocking, the adapter owns execution policy, the dispatcher/concurrency policy is bounded, and cancellation limitations are explicit. The code does not prove interruption or production capacity.

Alternative: expose `fun readInvoiceBlocking(...)` when callers have better execution-policy context. Route long-lived or process-surviving work to durable jobs rather than detached coroutines.

Evidence: dependency inspection, thread/dispatcher observation, cancellation-versus-interruption test, and representative concurrency experiment before saturation claims. Borderline state: semantic behavior verified, operational promotion withheld.

**Fixture E: mutable global state**

Unsafe:

```kotlin
object SessionRegistry {
    val sessions = mutableMapOf<String, Session>()
}
```

Mutation, synchronization, lifecycle, reset, eviction, and ownership are hidden. Tests may pass or fail by order.

Safer primary route: inject a `SessionStore` whose implementation has explicit application/request/test lifecycle, synchronization, and reset/shutdown behavior.

Conditional route: an immutable process constant or framework-owned registry is not equivalent to a mutable service singleton. An owned application cache can be valid with consistency, eviction, concurrency, privacy, observability, and operations contracts.

Evidence: repeat/reorder/parallel tests, isolation between fixtures, race-focused tests, reset/shutdown behavior, and cache policy tests. Remaining uncertainty: production contention and memory until measured.

**Fixture F: opaque scope functions and boolean outcome**

Unsafe:

```kotlin
fun register(input: Registration?): Boolean =
    input?.let { normalize(it) }
        ?.also { audit(it) }
        ?.let { repository.save(it) }
        ?.also { notifier.notify(it) }
        ?.let { true }
        ?: false
```

The chain collapses absent input, normalization rejection, persistence conflict/failure, and notification failure into `false`. Receiver and side-effect boundaries are difficult to audit.

Safer route: guard absent input, use named locals/functions, model the states that require distinct caller recovery, and define transaction/notification semantics. A private predicate can remain boolean if it is genuinely a side-effect-free yes/no question.

Conditional route: a short one-receiver `let` or `also` remains clear and need not be replaced to satisfy a token rule.

Evidence: enumerate caller actions; test every consequential result and side effect; verify transaction/notification behavior; review receiver and return semantics. Remaining uncertainty: domain choice about partial success until an owner decides it.

**Cross-fixture comparison**

| fixture | earliest contract loss | tempting incomplete fix | root-first action |
| --- | --- | --- | --- |
| Platform nullability | Interop uncertainty leaves adapter. | Replace `!!` with `?: return null`. | Decide and encode boundary states before domain export. |
| Cancellation | Parent control becomes ordinary failure. | Add another fallback or retry. | Preserve cancellation before translating known failures. |
| Identity | Value syntax is applied to lifecycle object. | Customize one equality test without defining identity. | Name identity and framework/persistence contract first. |
| Blocking | Execution behavior is hidden by suspend signature. | Add `Dispatchers.IO` and claim scalability. | Identify dependency behavior and execution owner, then measure capacity separately. |
| Global state | Mutable lifetime and synchronization are implicit. | Clear singleton in one test teardown. | Scope/inject state and define lifecycle/concurrency policy. |
| Scope/boolean | Multiple failure states collapse into null/false. | Add comments to the chain. | Separate steps and model caller-relevant outcomes. |

**Promotion rule for borderline cases**

A conditional case becomes a bounded exception only when it records the exact path, invariant, owner, failure consequence, test or framework evidence, and review trigger. Without that evidence it remains a finding, not a stylistic disagreement.

These examples share a mental model, not one helper library: locate the earliest information or ownership loss, preserve the distinctions that change behavior, and prove the dangerous branch. Reuse code abstractions only when multiple targets share semantics and lifecycle, not merely similar syntax.

## Outcome Metrics and Feedback Loops

No target workflow was measured during this evolution. The seed's "under one focused implementation session" statement has no baseline, task definition, cohort, or collection method and is therefore not retained as a target. The metric cards below are proposed measurement contracts, not observed results.

**Metric layers**

| layer | purpose | examples | interpretation limit |
| --- | --- | --- | --- |
| `deterministic_gate_data` | Confirm packet and gate mechanics for a named population. | Claims linked, blockers open, applicable gates run, findings disposed, exceptions evidenced. | Completeness does not prove semantic correctness or improvement. |
| `sampled_workflow_outcomes` | Assess whether reviewers and implementers make correct, efficient decisions. | Review reversal, blocker precision, time in blocked state, rework, evidence reconstruction. | Task mix and reviewer differences require bounded cohorts. |
| `downstream_quality_outcomes` | Observe recurrence or escaped mechanisms after adoption. | Platform-type boundary escape, cancellation defect recurrence, state leakage, identity regression, blocking incident. | Correlation does not establish that one gate caused the change. |

**Proposed metric menu**

| metric_name | definition_and_denominator | decision_use | required_counter_metric |
| --- | --- | --- | --- |
| `claim_evidence_coverage` | Consequential packet claims with at least one matching evidence record / all consequential packet claims. | Detect unverified completion and unclear no-claim boundaries. | Review reversal: evidence can exist yet not support the claim. |
| `boundary_escape_findings` | Confirmed uncertain values that cross their intended adapter boundary / inspected interop boundaries in the named population. | Target adapter reviews or shared normalization controls. | False-positive/conditional rate and scan population changes. |
| `cancellation_path_coverage` | Changed consequential suspend paths with deterministic parent/lifecycle cancellation evidence / changed consequential suspend paths where cancellation applies. | Identify missing interrupted-path tests. | Test determinism/flakiness and cleanup assertions; a count alone does not prove production behavior. |
| `blocking_contract_coverage` | Changed calls with classified blocking behavior and named execution owner / changed calls whose behavior can occupy threads. | Find hidden blocking and unowned dispatcher policy. | Runtime overhead and investigation cost; source classification may remain uncertain. |
| `finding_disposition_latency` | Time from confirmed/conditional finding to repair, bounded exception, accepted risk, not-applicable decision, route, or block resolution. | Identify owner or evidence bottlenecks. | Consequence/severity and task complexity; speed must not reward premature closure. |
| `blocker_precision_sample` | Sampled blockers reviewers agree would permit a material defect or unsupported claim / sampled blockers reviewed. | Calibrate blocker wording and targeting. | Missed-defect sample or escaped mechanisms; high precision can coexist with low coverage. |
| `review_reversal_rate` | Material claim/status decisions reversed after new evidence / reviewed decisions in a stable cohort. | Detect weak evidence or unclear authority. | Beneficial early reversals and task novelty; not every reversal is failure. |
| `gate_signal_yield` | Actionable, confirmed findings from a gate / findings emitted by that gate for the captured population. | Narrow noisy searches/rules or improve exception handling. | Defect escape and scan coverage; optimizing precision alone can miss hazards. |
| `rework_due_to_contract_ambiguity` | Changes reopened because null/state/identity/cancellation/blocking semantics were unresolved / completed changes in a comparable cohort. | Decide whether earlier decision artifacts or tests are valuable. | Overall scope and evolving requirements. |
| `escaped_mechanism_recurrence` | Post-handoff incidents/bugs sharing a previously classified causal mechanism / comparable changes or exposure period. | Promote shared controls or revise gates after case review. | Exposure, detection changes, severity, and independent causes. |
| `review_effort` | Reviewer/implementer time attributable to the quality process for a defined change class. | Keep gates sustainable; select compact versus standard profile. | Rework avoided and defect consequence; lower effort alone is not better. |
| `operational_regression` | Correctness-equivalent before/after runtime measures crossing an owner-defined threshold. | Validate dispatcher, blocking, allocation, or latency effects. | Workload/environment equivalence, uncertainty, and semantic correctness. |

No universal target is supplied. Owners establish thresholds only after baseline collection, task grouping, and consequence review.

**Metric card requirements**

Every metric used for a decision records:

1. Name, owner, and decision it is allowed to influence.
2. Numerator, denominator, inclusion/exclusion, and unit.
3. Cohort or population identity, including module, task type, and time/version boundary.
4. Data source and collection/recomputation procedure.
5. Baseline and comparison state, if any.
6. Counter-metric and known gaming pressure.
7. Privacy/redaction constraints.
8. Uncertainty and prohibited causal interpretation.
9. Review cadence, invalidation, and retirement condition.

**Good metric card**

`cancellation_path_coverage` is collected for changed request-owned suspend paths in two named service modules. The denominator excludes pure CPU leaf functions and framework-generated code with separate lifecycle tests. A path counts only when parent cancellation is synchronized after entry and cleanup/no-side-effect assertions pass. The paired counter-metric is test flakiness and review effort. The metric can trigger missing-test review; it cannot claim fewer production incidents without incident evidence.

**Bad metric**

"Count `!!` and drive it to zero." This has no semantic denominator, treats generated/tests/proven invariants like uncertain production paths, encourages cosmetic replacement, and says nothing about platform-type containment or nullable state modeling.

**Borderline metric**

Detekt findings decline after a baseline or configuration change. The observation is real for the new analyzer population but not comparable to the prior series. Create a series boundary, report rule/population changes, and do not describe the decline as code improvement without re-running an equivalent configuration or reviewing changed findings.

**Validity and anti-gaming checks**

- Do not render missing observations as a healthy zero.
- Deduplicate one causal finding reported by multiple gates while retaining each detector's contribution.
- Separate severity and consequence; ten private style findings are not equivalent to one swallowed-cancellation defect.
- Freeze metric definitions during comparisons or mark a series boundary.
- Keep generated-code, source-set, baseline, and module exclusions visible.
- Pair speed with rework, reversal, blocker quality, and escaped mechanisms.
- Treat increasing findings after better detection as ambiguous until exposure and outcome are reviewed.
- Do not rank individual people or agents from quality metrics; evaluate mechanisms and controls.

**Feedback loop**

```text
capture deterministic evidence
    -> sample decision quality and burden
    -> inspect downstream cases
    -> propose one control change
    -> trial on a bounded cohort
    -> compare with counter-metrics
    -> adopt, adapt, narrow, remove, or roll back
```

Examples of valid responses include strengthening one Java adapter contract after repeated boundary escapes, adding a reusable cancellation fixture after repeated missing tests, narrowing a noisy lexical scan, documenting a framework-owned exception, removing a duplicate gate, or splitting one broad blocker into semantic and operational states.

**Current evidence state**

This reference defines metrics but reports no baseline, observed value, comparison, quality improvement, reviewer-time change, or defect reduction. Deterministic Assignment 9 artifact counts belong to the evolution workflow and should not be generalized into Kotlin engineering outcomes. Measurement readiness is not evidence of positive performance.

## Completeness Checklist

Completion has two layers: the artifact must be internally valid, and each target claim must be closed or honestly left blocked/no-claim. Passing one layer cannot promote the other.

**Layer A: evidence-packet integrity**

- [ ] User goal, non-goals, target identity, supported environment, and allowed actions are explicit.
- [ ] Mapped local source identity and complete-reading status are recorded.
- [ ] External rows are marked observed, unrefreshed, or not used; no root URL is promoted as evidence.
- [ ] Every consequential claim has a stable ID, class, scope, evidence state, and invalidation trigger.
- [ ] Observed source facts, observed target facts, desired owner policy, inference, proposal, result, blocked state, and no-claim state are not blended.
- [ ] Every anti-pattern candidate has a disposition: confirmed, conditional, bounded exception, accepted risk, not applicable, or blocked.
- [ ] Every exception names the excluded danger, invariant, owner, evidence, consequence, and review trigger.
- [ ] Every gate records command/assertion, target population, result, and owner; no command is implied to exist.
- [ ] Every skipped applicable gate has a reason and next owner/condition.
- [ ] Contradictory statuses are reconciled; for example, a claim cannot be both verified and blocked for the same scope.
- [ ] Changed paths/contracts, compatibility effect, rollback/containment, unresolved risk, and handoff are explicit.

**Layer B: target semantic and behavioral closure**

- [ ] The exact uncertainty ingress and normalization boundary are identified.
- [ ] Nullable, absent, invalid, forbidden, unknown, failed, and not-loaded states are distinguished when callers act differently.
- [ ] Java platform types do not escape their intended adapter unless a bounded exception proves containment.
- [ ] Boolean, null, string, generic wrapper, or broad exception outcomes do not force callers to guess recovery.
- [ ] Data/value/identity representation matches equality, hash, copy, destructuring, persistence, proxy, and lifecycle semantics as applicable.
- [ ] Every coroutine has an owner, parent/lifecycle, cancellation path, failure destination, cleanup rule, and result accounting.
- [ ] `CancellationException` is preserved or translated only by a boundary that owns and tests that translation.
- [ ] Every blocking dependency is classified; execution policy, concurrency ownership, and cancellation-versus-interruption limits are explicit.
- [ ] Mutable state has lifecycle, synchronization, reset/shutdown, consistency, and observability ownership.
- [ ] Focused tests exercise the highest-consequence negative, absent, cancellation, equality, blocking, or isolation branch.
- [ ] Compile/build and configured lint/static gates run for the actual module/source-set population or have a recorded unavailable/not-applicable state.
- [ ] Broader regression/support-matrix results are reported, including attributed external failures.
- [ ] Runtime latency, throughput, saturation, memory, or capacity is claimed only with a controlled target experiment and operations acceptance.

**Conditional profile gates**

| condition | additional completion requirements |
| --- | --- |
| Public API changes | Caller/consumer inventory, compatibility/versioning, migration path, contract tests, rollback. |
| Persisted representation changes | Data migration, old/new read/write compatibility, identity/equality effects, rollback/data recovery. |
| Framework entity/lifecycle changes | Versioned framework contract, integration fixture, lifecycle transitions, generated/proxy behavior. |
| Shared coroutine or dispatcher change | Caller/lifecycle inventory, failure/cancellation matrix, queue/thread/runtime evidence, operations owner. |
| Global/shared mutable state change | Usage inventory, concurrency/consistency policy, staged replacement, test isolation, shutdown and rollback. |
| New/changed analyzer or baseline | Rule/config/version, population, existing-finding treatment, rollout/noise plan, CI parity, ownership. |
| Production performance claim | Correctness-equivalent outputs, environment/workload identity, samples, uncertainty, counter-metrics, SLO owner. |
| Cross-owner or multi-module migration | Stage graph, compatibility boundary, per-stage gates, rollback, merge/coordination owner. |

**Completion states**

| state | meaning | allowed claim |
| --- | --- | --- |
| `orientation_complete` | Sources and target are mapped; no implementation claim is made. | "Relevant risks, options, and next evidence are identified." |
| `containment_complete` | Immediate consequence is bounded; root redesign or policy remains open. | "The named path is contained under these invariants; full resolution remains open." |
| `semantic_complete` | Target states, ownership, and focused behavior are verified. | "The named semantic contract is verified for the tested target population." |
| `integration_complete` | Relevant build/analyzer/broader gates pass or permitted external reds are attributed. | "The change integrates for this configured target and matrix." |
| `operationally_promoted` | Runtime-sensitive claims have target measurement and owner acceptance. | "The measured operational contract is accepted for this environment/workload." |
| `blocked` | Required evidence, authority, permission, or environment is absent. | "Work is blocked on this exact condition; no completion claim is made." |
| `no_claim` | A dimension is deliberately outside scope and no downstream decision relies on it. | "This work makes no claim about the named dimension." |

One summary can derive from the matrix, but it must retain split states. For example: semantic and integration complete for null/cancellation behavior; operational blocking capacity remains no-claim; shared suite has one attributed external red. That is clearer than either "done" or "failed."

**Good completion**

`KQ-NULL-001` links a Java adapter path, nullable fixture, typed exported outcome, caller branch tests, target module build, configured analyzer population, and dependency-version invalidation. Runtime latency is irrelevant and marked not applicable.

**Bad completion**

"Build, tests, and lint pass; null safety improved." The target population, null contract, negative fixture, analyzer configuration, callers, and exception status are absent.

**Borderline but honest completion**

Null and cancellation semantics are verified, but the legacy client may block longer than the dispatcher policy permits. The change can be semantically complete while operational promotion remains blocked or no-claim, depending on whether release relies on a capacity assertion.

**Exclusion and anti-filler review**

`not_applicable` needs a claim-specific reason. Repeated exclusions should be reviewed: they may reveal that a gate is mis-targeted, a common profile is missing, or a risk is being systematically ignored. Generic phrases such as "covered by tests" do not satisfy a row without the test and behavior. A fully populated packet with unsupported content fails integrity.

**Selective re-open**

Completion is versioned. Reopen related claims when source identity, dependency/compiler/framework version, target code, caller set, state policy, execution configuration, analyzer population, or runtime workload changes materially. Rerun affected focused gates and relevant integration checks; do not discard unrelated valid evidence.

## Adjacent Reference Routing

Keep this reference primary for Kotlin information preservation, ownership, anti-pattern classification, and gate sufficiency. Route only the smallest consequential claim that requires deeper framework, runtime, security, testing, reliability, language, or navigation authority.

The candidate files below were confirmed to exist by filename. Their content, freshness, and completion status were not opened or asserted for this section, except that `kotlin_backend_security_resilience-20260710.md` was the immediately preceding Delta-owned assignment and has its own recorded verification. Validate every destination at selection time.

| unresolved_claim_or_task | candidate_adjacent_reference | handoff_entry_evidence | result_required_back |
| --- | --- | --- | --- |
| Which Kotlin reference should own a broad or mixed question? | `idiomatic-ref-202607/kotlin_backend_reference_routing-20260710.md` or `idiomatic-ref-202607/kotlin_reference_routing_sources-20260710.md` | Claim, target, current primary reference, and why ownership is ambiguous. | Primary destination, alternatives, evidence scope, and return owner. |
| What is the general Kotlin language/coding entrypoint beyond this quality focus? | `idiomatic-ref-202607/kotlin_language_skill_entrypoint-20260710.md` | Language-level question, target versions/config, and local evidence gap. | Applicable language contract or route, with target verification need. |
| What is the backend workflow or integrated playbook? | `idiomatic-ref-202607/kotlin_backend_skill_entrypoint-20260710.md` or `idiomatic-ref-202607/kotlin_backend_playbook_reference-20260710.md` | Backend goal, phase, affected layers, current quality finding. | Workflow ownership, required artifacts/gates, and how quality claim re-enters. |
| How should Spring or Ktor-specific idioms/lifecycle be applied? | `idiomatic-ref-202607/kotlin_spring_ktor_idioms-20260710.md` | Framework and version, plugin/engine/config, exact lifecycle or mapping question, target test gap. | Version-scoped mechanism, tradeoff, target integration gate, and non-claims. |
| How should tests, coroutine fixtures, or integration harnesses be designed? | `idiomatic-ref-202607/kotlin_backend_testing_fixtures-20260710.md` | Claim ID, failure mechanism, deterministic event/input needed, current test stack. | Fixture design, synchronization/population, expected assertion, and limit. |
| How should runtime operation, blocking saturation, observability, or day-two recovery be handled? | `idiomatic-ref-202607/kotlin_backend_runtime_operations-20260710.md` | Build/dependency identity, execution model, workload or failure observation, semantic correctness state. | Runtime experiment/operating contract, SLO owner, measurement, rollback, and promotion state. |
| How should abuse, trust, authorization, secrets, retries/idempotency, or resilience be handled? | `idiomatic-ref-202607/kotlin_backend_security_resilience-20260710.md` | Actor/asset/trust boundary, side effect, failure/retry semantics, current quality finding. | Protected-transition contract, negative evidence, owner, and integration implications. |
| How should broader Kotlin reliability patterns be selected? | `idiomatic-ref-202607/kotlin_reliability_reference_patterns-20260710.md` | Failure class, ownership boundaries, current local evidence, missing reliability depth. | Pattern choice, limits, verification, and how it composes with the KQEP. |

**Route modes**

| route_mode | ownership effect | use_when | completion rule |
| --- | --- | --- | --- |
| `consult` | Current quality owner remains primary; destination answers one narrow contract question. | Version, lifecycle, fixture, or operational detail is missing. | Returned result is reconciled into the original claim and gate. |
| `compose` | Different references own different claim IDs under one integration owner. | A change spans quality plus security, runtime, testing, or framework behavior. | Every claim has one primary owner; conflicts and integration gates are resolved. |
| `transfer` | Destination becomes primary for the whole task or work item. | Original task was misclassified and adjacent capability dominates. | Handoff is accepted and final integration/review owner is named. |
| `block_and_route` | Affected claim stops; safe evidence gathering/containment may continue. | Consequential policy, environment, permission, or owner is absent. | Exact missing decision/evidence arrives and resume point is explicit. |

**Handoff packet**

Every material route carries:

1. Stable claim ID and one-sentence unresolved question.
2. User goal, target identity, write/action boundaries, and current phase.
3. Evidence already loaded and hashes/versions where material.
4. Confirmed finding, rejected hypotheses, and current evidence state.
5. Consequence of choosing incorrectly.
6. What this reference continues to own.
7. Exact result requested from the destination.
8. Return, verification, and invalidation conditions.

This prevents the destination from repeating discovery or broadening scope unintentionally.

**Good routes**

- A source trace proves a Java call blocks, but acceptable dispatcher saturation is unknown. Keep semantic adapter work here; consult runtime operations with dependency, workload, thread observations, and no-capacity-claim state.
- A data-class entity may conflict with Spring persistence proxies. Keep identity finding and caller impact here; consult Spring/Ktor idioms for the versioned framework contract and required integration fixture.
- A broad catch can swallow cancellation and also retry a privileged side effect. Compose this quality claim with the security/resilience protected-transition claim; one owner integrates cancellation, idempotency, and negative tests.

**Bad routes**

- Send every `!!` finding to security because null could theoretically be security-related.
- Send a missing unit fixture to runtime operations before checking the testing reference or target test stack.
- Route to several references without assigning claim ownership, then combine whichever recommendations are easiest.
- Transfer the task because domain semantics are difficult while discarding the adapter trace and characterization evidence already gathered.

**Borderline route**

A framework-owned data class has uncertain equality semantics. A consult is appropriate if framework behavior is the only missing premise. A transfer is excessive if the change remains a bounded Kotlin identity repair. If the entity is public, persisted, and shared across modules, composition or staged migration ownership may be justified.

**Route-loop and conflict controls**

- Reject circular routing with unchanged claim and evidence; return a concrete missing-input request instead.
- Check destination path/ownership/status before relying on it.
- Preserve one primary owner per claim even when references compose.
- Record disagreements by claim scope and authority rather than averaging recommendations.
- Do not promote a specialist result beyond the population it observed.
- Reconcile returned results into callers, tests, gates, and completion state; a route is not complete merely because advice came back.

The route boundary is the smallest unanswered consequential claim. Continue useful local inspection, characterization, and safe containment within authority while that claim is routed. Routing should preserve information and ownership at the process level just as Kotlin quality controls preserve them in code.

## Workload Model

`combined_evidence_inference_note`: Treat Kotlin Quality Antipattern Gates as a quality operating reference. Workload is the unresolved decision surface, not the number of requirement IDs or pages in the packet.

The seed's boundary of one packet, twenty or fewer requirement IDs, one matrix, and one command set is uncalibrated historical guidance. This reference preserves no universal requirement-count capacity. A target team may adopt measured budgets with an owner and review method.

**Workload dimensions**

| workload_dimension_name | observation_to_capture | pressure_signal | implication |
| --- | --- | --- | --- |
| `uncertainty_ingress_count` | Distinct transport, Java, database, configuration, reflection, framework, or user-input boundaries on the claim path. | Different contracts and normalization owners. | Narrow by boundary or create adapter-specific claims. |
| `state_action_complexity` | Distinct states that cause different caller, recovery, authorization, or side-effect actions. | Null/boolean/string cannot preserve actions; policy disputed. | Obtain owner taxonomy and use closed modeling or route. |
| `caller_and_api_breadth` | Direct/transitive callers, public consumers, modules, source sets, generated clients. | Compatibility and coordinated migration grow. | Inventory and stage; keep one integration owner. |
| `identity_and_persistence_coupling` | Equality, hash, copy, schema, proxy, cache, and serialized representation dependencies. | Irreversible or data-sensitive migration. | Require migration profile, compatibility, and rollback. |
| `lifecycle_and_coroutine_edges` | Parent/child jobs, scopes, lifecycle events, cleanup, supervision, shutdown. | Ownership crosses framework/process boundaries. | Model failure/cancellation matrix; route framework/durable concerns. |
| `blocking_and_concurrency_edges` | Blocking dependencies, dispatchers/executors, queueing, concurrency limits, shared state. | Production behavior cannot be inferred locally. | Separate semantic repair from runtime promotion and operations measurement. |
| `framework_and_generated_surface` | Framework-owned models/lifecycle, code generation, proxies, plugins, engines. | Direct edits may be unsafe; version contract dominates mechanism. | Contain in owned adapter and consult versioned framework evidence. |
| `owner_count` | Domain, API, persistence, framework, security/privacy, runtime/operations, release owners. | Decision authority fragments or conflicts. | Assign claim owners, route narrowly, and establish integration owner. |
| `evidence_availability` | Source visibility, deterministic fixtures, supported local environment, telemetry, external authorization. | Claims remain conditional/blocked; reproduction cost rises. | Characterize, probe, route, or keep no-claim state. |
| `gate_cost_and_duration` | Focused/broad command time, environment setup, flakiness, analyzer noise, supported matrix. | Feedback slows and retries consume context. | Narrow-first, parallelize independent read-only gates, or defer with owner. |
| `reversibility` | Ease of reverting code, API, schema, state, concurrency, or deployment change. | Irreversible/high-blast changes need stronger evidence. | Stage, add compatibility, migration, rollback, and review gates. |
| `shared_write_and_coordination` | Files/areas with multiple workers, branches, or release trains. | Collision, contradictory edits, lost state. | Single owner per file/claim, durable checkpoints, merge-time integration gate. |

Counts describe the target; they do not automatically determine a threshold. One hidden blocking call on a shared dispatcher can dominate dozens of isolated nullable DTO fields.

**Work modes**

| mode | entry shape | primary action | exit condition |
| --- | --- | --- | --- |
| `compact_path` | One boundary, bounded callers, no shared persistence/lifecycle, deterministic fixture. | Focused KQEP, coherent repair, focused plus configured gates. | Semantic/integration closure or one named route. |
| `standard_path` | Several related states/callers or coroutine/blocking/identity concern in one owned service/module. | Full claim map, caller trace, standard packet and layered gates. | All applicable claims closed or split by owner. |
| `characterization_path` | Existing behavior or desired semantics unclear. | Preserve current observations, identify discrepancy, seek owner contract. | Desired contract selected or containment accepted. |
| `migration_path` | Public/persisted/shared model, global state, or concurrency architecture spans boundaries. | Inventory, compatibility, stages, rollback, per-stage evidence. | Each stage integrates and final compatibility debt is resolved/owned. |
| `incident_containment` | Active consequence requires immediate reversible action. | Capture symptom, bound blast radius, apply smallest containment, verify immediate effect. | Incident stabilized; follow-up semantic/runtime work explicitly owned. |
| `routed_path` | Missing authority/evidence belongs to specialist or external owner. | Preserve packet, route smallest claim, continue safe local work. | Return contract resolves claim or transfer accepted. |

**Safe narrowing strategies**

| strategy | preserves | can_lose | safeguard |
| --- | --- | --- | --- |
| Narrow by one ingress-to-caller path | End-to-end semantics for one behavior. | Sibling boundary variants. | Record sibling hypothesis and avoid broad claims. |
| Adapter containment | External/framework uncertainty and stable internal contract. | Duplicate mappings or long-lived compatibility layer. | One owner, equivalence tests, invalidation/removal trigger. |
| Characterization first | Current behavior before risky redesign. | Confusing observed behavior with desired policy. | Label tests and obtain owner contract. |
| Shard by disjoint adapter/module owner | Parallel implementation throughput. | Shared model/caller conflicts. | Freeze shared contract and use one integration owner/gate. |
| Stratified sample of repeated findings | Early estimate of semantic variants. | Rare high-consequence outliers. | Sample by framework, lifecycle, caller action, side effect, and inspect outliers. |
| Automated candidate scan | Fast population discovery. | Semantic false positives/negatives. | Manual classification and behavior evidence. |
| Route one specialist claim | Preserves local progress and correct authority. | Context/decision fragmentation. | Stable claim ID, handoff/return contract, final reconciliation. |

**Hard stop or route signals**

Stop production/public promotion for the affected claim when:

- domain state meaning, identity, authorization, or accepted risk is disputed and no owner can decide;
- required source/hash/target identity is missing or stale;
- generated/framework behavior is consequential and version contract cannot be inspected or reproduced;
- work must survive lifecycle/process but durability/idempotency/operations architecture is absent;
- persisted/public migration lacks compatibility and rollback;
- blocking/capacity claim is required for release but representative measurement and SLO owner are absent;
- multiple workers would edit the same reference or shared contract without one owner/merge gate;
- a focused test cannot distinguish the proposed fix from an unrelated environment failure.

Continue read-only evidence capture, safe characterization, or reversible containment within authority. A hard stop applies to the unsupported claim, not necessarily every task action.

**Parallelism rule**

Parallelize independent source reads, disjoint candidate inventories, or disjoint adapter implementations only after the shared contract, ownership, and integration gates are stable. Do not parallelize competing edits to one file or one unresolved domain taxonomy. Parallelism before semantic decomposition increases merge volume and inconsistent decisions rather than throughput.

**Post-split equivalence gate**

A split is successful when:

1. Every original claim and caller/owner edge is assigned once.
2. Shared states, identity, error taxonomy, and lifecycle contracts are versioned and consistent.
3. Each shard has focused evidence and declared exclusions.
4. Compatibility boundaries and temporary translations are tested.
5. Integrated behavior matches the intended end-to-end contract.
6. No worker claims global completion from a local shard.
7. Rollback and final ownership remain clear.

**Dynamic reassessment**

Recalculate workload only on material evidence: a failing test narrows the mechanism, a caller trace expands compatibility surface, a framework contract removes uncertainty, a runtime probe reveals saturation, or an owner changes policy. Avoid constant replanning during stable implementation. Track unresolved dimensions, not only accumulated tasks; good evidence can shrink the workload by eliminating hypotheses.

**Current capacity evidence**

No target workload, gate duration, reviewer capacity, caller graph, migration size, or production limit was measured for this reference. The model supplies routing variables and completion logic, not universal thresholds.

## Reliability Target

Reliability means bounded prevention, detection, containment, recovery, and learning for a named population. It is not one score. No target application, production workload, review cohort, or achieved reliability result was measured during this evolution.

**Reliability profile schema**

| profile_field | required content |
| --- | --- |
| `profile_id_and_scope` | Repository/module/path, claim classes, supported environment, time/version window. |
| `consequence_model` | What happens if state, identity, ownership, blocking, or evidence is wrong. |
| `hard_invariants` | Mechanically decidable conditions that must hold for the declared population. |
| `sampled_indicators` | Review or outcome signals requiring a sample and uncertainty. |
| `sentinel_events` | High-consequence events that trigger review regardless of aggregate rate. |
| `prevention_detection_containment_recovery` | Controls at type, test, analyzer, runtime, and operational layers. |
| `evidence_and_population` | Commands/tests/reviews/measurements and exact denominator. |
| `owner_and_response` | Who acts on violation and how. |
| `accepted_risk_and_no_claims` | Deliberate residual uncertainty and claims not made. |
| `review_and_invalidation` | Definition version, cadence, trigger, and retirement condition. |

**Hard invariants for a declared change population**

| invariant | bounded threshold | evidence | violation_response |
| --- | --- | --- | --- |
| `claim_evidence_state_present` | Every consequential KQEP claim has support/limit, verification or explicit blocked/no-claim state. | Structural packet audit plus semantic review. | Block completion of the affected claim. |
| `evidence_boundary_preserved` | Every reused recommendation distinguishes observed local/target evidence, inference/proposal, external status, and result as applicable. | Claim audit over the declared packet/reference population. | Correct status and re-review dependent decisions. |
| `unsupported_claims_absent` | No production, security, latency, capacity, or reliability result is promoted without matching evidence and owner scope. | Editorial audit and claim-to-evidence trace. | Remove/narrow claim or obtain evidence; do not round uncertainty up. |
| `confirmed_findings_disposed` | Every confirmed finding is repaired, bounded by proven exception, accepted by owner, routed, or explicitly blocked. | Finding registry reconciliation. | Keep affected completion state open. |
| `cancellation_preserved_on_changed_paths` | Every changed applicable suspend path preserves or owner-translates cancellation under its named fixture. | Deterministic cancellation tests for the declared paths. | Block semantic completion; inspect catch/scope/cleanup. |
| `platform_uncertainty_contained` | Every changed applicable Java platform boundary exports explicit Kotlin types/outcomes or a bounded exception. | Source trace and nullable/malformed boundary fixtures. | Block boundary claim; normalize or document exception. |
| `recovery_route_named` | Every blocked/failed/avoid state names containment/rollback, owner/route, and resume condition. | Packet/handoff audit. | Treat recovery claim as incomplete. |

These exact thresholds apply only because the population is finite and declared. "Every changed applicable suspend path" is auditable; "all Kotlin coroutine code is reliable" is not.

**Sampled indicators**

The seed's "at least 18 of 20" route-decision value is retained only as an inherited illustrative regression sample. It is not a production probability, universal acceptance threshold, or measured result. If a team uses such a suite, it must freeze the twenty fixtures, their expected routes, severity, and version. One wrong sentinel route can fail the suite even if nineteen benign cases pass.

| indicator | interpretation | required counter-evidence |
| --- | --- | --- |
| Sampled route agreement | Reviewers agree that adopt/adapt/avoid/route decisions fit a frozen fixture set. | Disagreement reasons, sentinel misses, fixture representativeness, and version changes. |
| Blocker precision | Sampled blockers correspond to material risk or unsupported claims. | Escaped defects and missed-blocker sample. |
| Review reversal | Later evidence changes an earlier material decision. | Whether reversal occurred early and prevented rework; novelty of task. |
| Finding recurrence | Same causal mechanism appears after an accepted control. | Exposure, detector/configuration change, and independent causes. |
| Gate burden | Time/noise/flakiness attributable to a control. | Rework or consequence avoided; do not optimize speed alone. |

No sampled indicator has a value in this reference.

**Sentinel events**

Regardless of aggregate metrics, review and potentially block the affected profile when any of these occurs:

- a platform type or unvalidated boundary value escapes into consequential domain logic and causes incorrect behavior;
- parent/lifecycle cancellation is swallowed, translated accidentally, or followed by an unintended side effect;
- hidden blocking exhausts or materially degrades a constrained execution resource;
- data-class or mutable identity behavior corrupts persistence, collections, cache keys, or lifecycle invariants;
- shared mutable state causes cross-request/test leakage, race, stale value, or unsafe shutdown;
- a configured gate is reported green for a population it did not scan;
- a production/security/performance outcome is claimed without matching evidence;
- recovery documentation names no owner or executable/observable route.

**Layered control strategy**

| reliability_goal | prevention | detection | containment_and_recovery | learning |
| --- | --- | --- | --- | --- |
| Preserve boundary meaning | Adapter normalization and typed exports. | Null/malformed fixtures and source trace. | Keep uncertainty in adapter; fail/return typed state. | Standardize shared adapter only after recurring semantics. |
| Preserve coroutine ownership | Structured/lifecycle scopes and cancellation-first translation. | Parent/child cancellation and cleanup tests. | Cancel owned work, prevent side effects, route durable needs. | Improve shared test helpers or scope APIs after repeated gaps. |
| Keep blocking explicit | Named blocking contract or owned bounded isolation. | Dependency/thread inspection and runtime experiment. | Backpressure, concurrency limit, degradation/route. | Revisit client/architecture from measured saturation. |
| Preserve identity/state | Value versus entity modeling and scoped state. | Equality/persistence/concurrency/isolation tests. | Compatibility shim, state reset, rollback/migration. | Promote domain types or lifecycle controls when shared. |
| Preserve evidence integrity | Claim states, populations, configured commands, no-claim boundaries. | Packet/verifier/editorial audit. | Block/narrow unsupported claims and route missing authority. | Calibrate or remove noisy/redundant gates. |

**Reliability target lifecycle**

`proposed` means definition only. `baselined` means population and initial observations exist. `accepted` means the accountable owner adopts the target. `observed_pass` or `observed_violation` records one evidence window. `superseded` changes definition and creates a series boundary. `retired` means the target no longer changes decisions or a stronger control replaces it.

Do not rewrite prior values after a definition change. Preserve version and explain the series boundary.

**Good target**

For changed request-owned suspend functions in module X, every function that catches broad failures has a deterministic parent-cancellation test proving rethrow/cleanup and no fallback side effect. The population and exceptions are enumerated. Violation blocks semantic completion. This is a finite invariant, not a production failure-rate claim.

**Bad target**

"Achieve 99 percent coroutine reliability." It lacks population, event definition, measurement, owner, response, and distinction among prevention, runtime incidence, and recovery.

**Borderline target**

A frozen twenty-case routing suite requires eighteen correct decisions. It is useful as a regression signal only if the two allowed misses are non-sentinel, the fixture set remains representative, and results are not generalized. Until the suite and outcome exist, the value remains illustrative historical guidance.

Reliability targets should be removed or narrowed when they produce noise without changing behavior, duplicate a stronger type/test control, or encourage cosmetic compliance. More gates are not inherently more reliable.

## Failure Mode Table

Classify the failure layer before editing. Contain harmful side effects, preserve evidence, repair the earliest demonstrated contract loss, verify return to a defined state, and then decide whether a shared prevention control is justified.

| failure_mode_name | trigger_and_causal_chain | detection_signal | immediate_containment | durable_repair_and_recovery |
| --- | --- | --- | --- | --- |
| `source_drift_hides_truth` | Local/external/build guidance changes -> stale claim remains promoted -> wrong mechanism or command reused. | Hash/version/config mismatch or target contradiction. | Mark dependent claims stale; stop promotion. | Refresh precise source, reproduce target, update only affected claims/invalidation. |
| `generic_advice_escapes_review` | Agent skips local/target context -> plausible Kotlin slogan directs broad edits. | No target paths, evidence states, caller trace, or gate population. | Block implementation claim and restore scope. | Source-map and target inspection; bounded decision and verification. |
| `platform_null_crash` | Java platform value escapes adapter -> caller assumes non-null -> `!!` or dereference crashes. | Nullable fixture, stack/source trace, platform inferred type. | Prevent boundary export; return typed/provisional state. | Normalize adapter, define state meaning, update callers, null/contract tests. |
| `null_state_policy_collapse` | Absent/invalid/forbidden/failed/not-loaded all become null -> caller takes wrong recovery action. | Different desired caller actions mapped to same branch. | Preserve raw distinctions; avoid overwrite/retry/deny decision. | Owner taxonomy, closed state/outcome, exhaustive and boundary tests. |
| `lateinit_lifecycle_race` | Access precedes initialization or follows teardown -> runtime crash/stale value. | Lifecycle/order/concurrency fixture and writer/reader trace. | Guard affected lifecycle; prevent concurrent access. | Constructor/lifecycle ownership or explicit state; teardown/reset tests. |
| `data_class_identity_corruption` | Structural equality/hash/copy conflicts with entity lifecycle -> collection/persistence/proxy errors. | Equality changes after ID/status mutation, set lookup failure, framework mismatch. | Avoid mutable entity as key/copy path; preserve data. | Deliberate class/model mapping, identity tests, migration/compatibility. |
| `boolean_recovery_ambiguity` | Rejection/conflict/missing/failure collapse into false -> caller retries or suppresses incorrectly. | Caller branches infer meaning from false/message. | Disable unsafe retry/fallback and expose diagnostic state. | Closed outcome or typed exception; exhaustive caller tests. |
| `detached_work_outlives_owner` | Global/unowned coroutine survives request/lifecycle -> stale side effect, leak, lost failure. | Job has no parent/owner; shutdown/cancellation test leaves work active. | Cancel/disable detached path; prevent late side effects. | Structured/lifecycle/durable ownership; cleanup and failure reporting tests. |
| `cancellation_translated_as_failure` | Broad catch captures cancellation -> fallback/log/retry/side effect runs. | Parent cancellation yields domain failure or downstream action. | Rethrow cancellation and stop recovery path. | Narrow failure translation, synchronized cancellation/cleanup/no-side-effect tests. |
| `supervision_hides_child_failure` | `supervisorScope` or launched children used without result accounting -> child fails silently. | Missing await/result/handler; partial success not represented. | Stop dependent commit; surface child result. | Explicit sibling-independence contract and aggregate outcome tests. |
| `blocking_starves_dispatcher` | Hidden blocking in suspend path -> constrained threads occupy -> queue/latency/cancellation degrade. | Thread/queue observation, dependency inspection, concurrent slowdown. | Bound incoming work, isolate/degrade, stop unbounded launches. | Explicit execution owner/concurrency, client change or durable architecture, measured promotion. |
| `dispatcher_switch_false_confidence` | `Dispatchers.IO` added -> scalability/cancellability assumed -> uninterruptible/unbounded work persists. | No dependency or saturation evidence; cancellation leaves call running. | Narrow claim to thread isolation only. | Document interruption/queue behavior, bound concurrency, target experiment. |
| `mutable_global_state_leak` | Singleton mutation crosses tests/requests/lifecycles -> order dependence, race, stale state. | Reordered/parallel tests, cross-request contamination, unsafe shutdown. | Clear/isolate affected state under owner; avoid concurrent mutation. | Inject/scope state; synchronization/consistency/reset/shutdown evidence. |
| `scope_chain_hides_partial_side_effect` | Nested scope functions combine validation/save/notify -> failure point and transaction unclear. | Null/exception path leaves partial audit/save/notify. | Stop further side effect and reconcile current state. | Named steps, transaction/outbox/compensation decision, branch/side-effect tests. |
| `generic_result_captures_wrong_failure` | Broad `runCatching`/generic result captures cancellation or defect -> ordinary recovery follows. | Cancellation/bug appears as expected result. | Re-throw/reclassify and disable inappropriate retry. | Narrow taxonomy and caller handling; cancellation/defect tests. |
| `fixture_misses_dangerous_branch` | Fake never returns null/blocks/enters call -> test green without exercising mechanism. | Coverage/synchronization shows branch not reached. | Withdraw behavior claim. | Contract-faithful fixture, entry synchronization, integration evidence where needed. |
| `green_gate_population_gap` | Analyzer/test excludes module/source/generated path -> clean result generalized. | Config/baseline/population differs from claim. | Narrow result and reopen uncovered claim. | Record population, run correct gate or manual/alternative evidence. |
| `nonexistent_toolchain_invented` | Example command treated as required -> dependency/config churn or failed build. | Build files/wrappers lack tool/task. | Revert unauthorized tool addition; use current gates. | Discover repo-native commands; propose tooling only as separate owned decision. |
| `broad_suite_external_red_hidden` | Shared/other-owner failures filtered or mislabeled -> misleading completion. | Full suite red but handoff reports pass. | Report both local and external states; preserve logs/owner. | Route external failure; follow repository release policy; do not edit unauthorized scope. |
| `migration_half_translates_contract` | Producer adopts typed outcome but callers map back to boolean/null -> ambiguity persists across compatibility layer. | Caller inventory finds lossy translation. | Keep one explicit compatibility boundary; block global completion. | Stage callers, equivalence tests, remove/deprecate shim under owner. |
| `persistence_rollback_incompatible` | Model/schema/equality change deploys without old/new compatibility -> unreadable/corrupt state. | Migration/round-trip/rollback test fails. | Halt rollout; protect backups/writes. | Forward/backward compatibility, staged migration, data recovery, owner approval. |
| `metric_no_data_rendered_zero` | Missing observations displayed as healthy zero -> risk appears absent. | Collection gap or denominator missing. | Mark unknown and stop comparison. | Fix instrumentation/provenance; recompute with explicit population. |
| `runtime_claim_from_local_test` | Unit/build result promoted to capacity/latency claim -> unsafe release assumption. | No workload/environment/sample evidence. | Remove/narrow claim; keep semantic evidence. | Controlled correctness-equivalent experiment and operations acceptance. |
| `recovery_route_has_no_owner` | Failure text says retry/escalate/rollback without owner or executable condition -> stalled or repeated action. | Same failure recurs with no state change. | Stop blind retries; persist evidence and blocker. | Assign owner, changed-premise transition, drill or observable recovery proof. |
| `parallel_workers_collide` | Multiple agents edit shared file/contract -> overwritten rationale, inconsistent states. | Concurrent diffs, heading/packet mismatch, lost checkpoint. | Stop affected writes; preserve both evidence sets. | Single file/claim owner, disjoint work, merge/integration gate, durable journal. |

**Failure handling state machine**

```text
signal
  -> preserve target/build/config/evidence identity
  -> classify layer and side-effect risk
  -> contain harmful action
  -> test discriminating hypothesis
  -> repair earliest confirmed contract loss
  -> verify focused recovery
  -> verify integration and applicable operation
  -> update finding, reliability, source, and prevention records
```

If the hypothesis fails, return to classification; do not stack unrelated fixes. If reproduction is impossible, keep incident evidence, narrow causal certainty, and design the safest discriminating probe or owner route.

**Compound trajectories**

Good: parent cancellation is observed entering a broad catch. The system prevents fallback/cache mutation, rethrows cancellation, verifies cleanup, runs integration gates, and records that the opaque blocking call's interruption remains unverified.

Bad: a timeout occurs, the catch returns `false`, the caller retries, and global state records two writes. The response adds `Dispatchers.IO` and another retry without classifying cancellation, blocking, or idempotency.

Borderline: a blocking Java call is correctly isolated and semantic tests pass, but no representative saturation measurement exists. Mark semantic/integration completion separately and keep operational promotion no-claim or blocked; do not describe the local fix as production capacity evidence.

**Recovery proof**

A mitigation is not complete merely because the original exception disappears. Verify the defined post-recovery state: caller outcome, side effects, parent/child jobs, persisted data, shared state, resource queues, telemetry, and ability to resume. Use representative nonproduction drills for destructive rollback or restart paths and retain residual uncertainty.

**Learning rule**

Promote a shared adapter, test helper, analyzer rule, or review blocker when a mechanism recurs, is shared by architecture, or is a high-consequence sentinel. Avoid overfitting one occurrence. Also remove or narrow controls that repeatedly emit noise, duplicate stronger guarantees, or obscure root causes.

## Retry Backpressure Guidance

Retry is not one policy. Application calls, build/test commands, external retrieval, and agent work have different side effects and owners. This section defines classification and stop rules; target production attempt counts, delays, deadlines, idempotency, rate limits, and concurrency budgets require their owning service/security/resilience/operations contract.

**Default rule**

Do not repeat automatically. First classify the result, preserve caller cancellation/deadline, identify side effects, inspect retry topology, and require a changed premise or an already-owned transient policy. Consume one end-to-end budget rather than allowing every layer to believe it has an independent allowance.

**Failure classification**

| class | default_retry_decision | premise_needed_for_another_attempt |
| --- | --- | --- |
| `caller_cancellation_or_deadline` | Never retry beneath the caller; propagate/stop and clean up. | A new explicit caller request creates new work under a new budget. |
| `validation_or_domain_rejection` | Do not retry unchanged input/policy. | Input or authoritative policy changes. |
| `deterministic_code_or_test_failure` | Do not rerun to seek green. | Code, fixture, hypothesis, configuration, or environment changes. |
| `permission_or_authority_missing` | Stop affected action and route. | Permission/owner decision arrives. |
| `stale_or_missing_evidence` | Refresh only when authorized and source/target can close the claim. | New artifact/version/span or target reproduction becomes available. |
| `transient_idempotent_dependency_failure` | Use existing owned bounded policy if deadline/load permit. | Policy classifies failure as transient and attempt budget remains. |
| `unknown_dependency_failure` | Do not assume transient. | Classification evidence or owner policy. |
| `unsafe_or_non_idempotent_side_effect` | Do not retry without idempotency/deduplication/transaction contract. | Side-effect safety is established and tested. |
| `resource_saturation_or_backpressure` | Stop or slow admission; blind retry amplifies load. | Capacity recovers under observable policy and deadline remains. |
| `flaky_or_nondeterministic_test` | Retain all attempts; do not select a passing run as proof. | Root nondeterminism is diagnosed/fixed or an approved quarantine policy applies. |
| `shared_external_failure` | Attribute and route; do not edit outside ownership merely to turn suite green. | External owner changes state or integration policy permits scoped completion. |

**Application retry contract**

Before adding or accepting an application retry, identify:

1. Exact operation and side effects.
2. Failure classes that are retryable and terminal.
3. Idempotency key, deduplication, transaction, or compensation semantics.
4. Caller cancellation and total deadline.
5. End-to-end attempt budget including client, framework, proxy, broker, and worker retries.
6. Delay/backoff/jitter and rate-limit handling owned by target policy.
7. Concurrency/admission backpressure and queue bounds.
8. Attempt observability without sensitive payloads.
9. Final caller outcome, recovery, and operations owner.

Do not catch `CancellationException` as a retryable dependency failure. Do not retry a boolean `false` when its meaning is unknown. Do not infer idempotency because a method name sounds read-like. Route distributed retry/idempotency design to the security/resilience or operations reference when it exceeds a local typed-failure correction.

**Verification and tool retries**

A command can be rerun after code, fixture, command selection, configuration, dependency, or environment changed. Record the change. If the same command and environment alternate pass/fail, classify flakiness; preserve attempt outputs and withdraw deterministic completion.

Good: a focused test fails because a fixture lacks a required test dependency. The dependency/configuration is corrected within scope, then the test runs again. The changed premise is explicit.

Bad: a cancellation test fails intermittently, so it is run until green and only the passing output is reported. The evidence now hides the exact nondeterminism the gate should reveal.

Diagnostic reruns can be useful when they vary one controlled factor or collect additional instrumentation. They are experiments, not retries-to-completion.

**External research retries**

The seed's one bounded retry for stale external evidence is a workflow example, not a universal network constant. Under authorized research, one may correct a URL, revision, or query after classifying a retrieval failure. Repeating an unavailable or contradictory source without new scope does not improve evidence. Route to a narrower official artifact, target source/test, cached approved artifact, or owner decision.

Keep network/transient policy distinct from semantic disagreement. A successfully retrieved page can still fail to support the claim.

**Agent and long-running workflow backpressure**

Apply backpressure when:

- source or target identity is unresolved;
- packet/review coverage is incomplete for the next edit;
- normalized uniqueness or structural gates are red;
- an owner decision blocks the next semantic transition;
- multiple workers would touch one file or shared contract;
- focused verification exposes a new root hypothesis;
- context drift risks losing the current evidence boundary;
- a shared gate is red outside current ownership and attribution is incomplete.

Backpressure actions:

1. Stop opening new sections/files or accepting new work for the affected stream.
2. Finish and persist the current atomic unit if it is coherent and safe.
3. Record current phase, exact evidence/results, changed paths, blocker, and nonempty next condition.
4. Bound in-flight work and keep one owner per file/claim.
5. Resume from the journal and revalidate changed dependencies, not from memory.
6. Re-run the relevant focused gate after a changed premise; do not restart valid completed units.

**Attempt record**

| attempt_field | content |
| --- | --- |
| `attempt_id_and_domain` | Application, tool/test, research, or agent-work attempt. |
| `operation_and_owner` | What runs and who owns policy. |
| `failure_class` | One classified state above, with evidence. |
| `premise_change` | Code/input/config/environment/source/permission change since prior attempt. |
| `deadline_and_budget_state` | Caller deadline and end-to-end attempts remaining when applicable. |
| `side_effect_safety` | Idempotency/deduplication/transaction/no-side-effect evidence. |
| `delay_and_admission` | Policy-selected delay/backpressure, not a guessed constant. |
| `result_and_observation` | Outcome, key signal, side effects, and uncertainty. |
| `next_transition` | Stop, repair, route, retry under policy, quarantine, or complete. |

**Verification fixtures**

- Cancellation sequence: cancel parent after call entry; assert no retry and no post-cancel side effect.
- Deterministic failure sequence: return validation/denial repeatedly; assert one attempt for unchanged input.
- Transient sequence: fail with classified transient outcomes then succeed; assert budget/deadline/delay and attempt metadata under target policy.
- Duplicate sequence: repeat unsafe write; assert deduplication or verify retry remains prohibited.
- Saturation sequence: constrain owned resource; assert admission/backpressure rather than retry storm.
- Flaky test sequence: retain alternating outcomes and ensure completion remains blocked until nondeterminism is handled.

**Nested retry topology**

Inventory retries in HTTP/client libraries, framework filters, database drivers, brokers, workers, proxies, and callers. Multiplication can exceed intended load and deadlines even when each layer is locally bounded. Choose one authoritative layer for each failure class or ensure budgets propagate end to end.

**No universal values**

This reference specifies no universal attempt count, timeout, delay, jitter, queue size, concurrency, or stale-evidence refresh count. Those values depend on target side effects, SLOs, rate limits, resource cost, and operations ownership. The universal quality rule is narrower: classification, cancellation, side-effect safety, changed premise, bounded ownership, observability, and stop behavior must be explicit.

## Observability Checklist

Observability should let another reviewer reconstruct the claim, target, decision, gate, and next owner without exposing sensitive payloads or relying on raw transcript volume. Runtime telemetry is conditional: do not collect or report percentiles merely because the seed mentioned them.

**Common evidence envelope**

| field | meaning |
| --- | --- |
| `event_schema_version` | Version of the event definition and series boundary. |
| `event_type` | Claim, finding, gate, exception, retry, cancellation, blocking, migration, route, or collection-health event. |
| `claim_finding_gate_id` | Stable bounded identifier that links packet, code, and evidence. |
| `target_identity` | Repository/build/module/source-set/environment identity appropriate to the event. |
| `source_or_configuration_identity` | Hash/version/config/baseline relevant to interpretation. |
| `state_and_classification` | Observed, proposed, pass, fail, blocked, no-claim, retry class, or finding disposition. |
| `population_or_fixture` | Files, paths, inputs, tests, workload, or sample included and excluded. |
| `result_and_limit` | Concise outcome plus what it cannot establish. |
| `owner_and_next_transition` | Accountable role and repair/route/retry/rollback/review action. |
| `correlation_token` | Non-sensitive token linking related evidence when needed. |
| `recorded_at_and_retention` | Time window and retention/privacy policy, not necessarily high-resolution per-event time. |

Do not put request payloads, secrets, credentials, tokens, full personal identifiers, raw exception messages containing sensitive data, or unbounded user/order IDs into quality telemetry. Prefer typed categories such as `platform_null`, `cancelled_by_parent`, `known_dependency_failure`, or `blocking_queue_saturated`.

**Artifact and workflow events**

| event_type | minimum fields | reconstruction question |
| --- | --- | --- |
| `source_loaded` | Path/URL, hash/revision, observed status, relevant heading/span, skipped reason. | Which guidance was actually available? |
| `claim_state_changed` | Claim ID, old/new state, support/limit, invalidation. | Why was a claim promoted, narrowed, blocked, or reopened? |
| `finding_disposed` | Finding ID/class, path, consequence, disposition, exception/owner. | Was the hazard repaired, bounded, accepted, routed, or dismissed correctly? |
| `gate_result` | Gate ID, command/assertion, target/population, tool/config, result, key diagnostic. | What exactly passed or failed? |
| `route_handoff` | Claim, from/to owner/reference, evidence, requested result, return condition. | Where did authority move and what came back? |
| `exception_reviewed` | Construct, invariant, evidence, owner, consequence, review trigger. | Why is a default exception safe for this scope? |
| `completion_state` | Semantic/integration/operational/external states, blockers, no-claims. | What can downstream users rely on now? |

Persist concise decision evidence, not hidden thought or every tool call. A useful gate event contains the exact command and result summary; it does not need an entire successful build log. Keep enough failure context to diagnose without exposing unrelated or sensitive output.

**Kotlin runtime quality events**

Runtime telemetry is appropriate only when the change makes or depends on a runtime claim.

| event_or_metric | safe dimensions | unsafe_or_misleading_dimensions | use |
| --- | --- | --- | --- |
| Cancellation outcome | Scope/lifecycle class, operation class, cancellation source, cleanup/side-effect status. | Raw request/user data, exception message as taxonomy. | Detect cancellation translated as failure or followed by side effects. |
| Blocking execution | Dependency/operation class, dispatcher/executor class, active/queued counts, duration distribution under defined workload. | High-cardinality operation IDs, percentiles without sample/workload. | Observe saturation and policy fit. |
| Typed outcome | Outcome category, caller path class, retry/fallback action. | Payload values or personal identifiers. | Detect unexpected collapse or unsafe recovery. |
| State isolation | Scope class, reset/shutdown event, conflict/race category. | Dumping mutable state contents. | Observe lifecycle leakage and cleanup. |
| Retry/backpressure | Failure class, attempt ordinal within owned budget, delay class, deadline state, dedupe result, stop reason. | Payload, globally unique business key as metric label. | Detect amplification, duplicate effects, and ignored cancellation. |
| Migration compatibility | Old/new contract version, read/write path class, conversion/rollback result. | Persisted content. | Detect half-migration or rollback incompatibility. |

**Logs, metrics, traces, and records**

Use packet/gate records for deterministic audit, logs for bounded diagnostic narratives, metrics for low-cardinality aggregates, and traces for sampled causal paths. Assign one canonical source for each fact and link derived views to it. A dashboard value without metric-definition/version and collection-health links is not durable evidence.

**Missing versus zero**

Every aggregate must distinguish:

- `observed_zero`: collection was healthy for the stated population and no events occurred;
- `not_applicable`: mechanism was absent by inspected contract;
- `not_instrumented`: no collection exists;
- `collection_degraded`: data may be incomplete;
- `unknown_population`: denominator cannot be reconstructed;
- `no_claim`: this change intentionally makes no statement about the metric.

Never render the last four states as a healthy zero. Collection health is a prerequisite for interpreting absence.

**Runtime distribution requirements**

Report p50/p95/p99 only when runtime applies and sample design can support those summaries. Capture build, environment, workload distribution, concurrency, warmup, sample count, collection interval, correctness equivalence, and uncertainty. For small samples, raw observations or ranges may be more honest than tail percentiles. Reviewer-time measurement likewise needs a task cohort and counter-metrics before any efficiency conclusion.

**Privacy and cardinality checklist**

- [ ] No secrets, credentials, tokens, raw payloads, or unnecessary personal data.
- [ ] No unbounded business/user/request identifier used as a metric dimension.
- [ ] Exception/failure categories are typed and stable rather than raw message strings.
- [ ] Correlation token is scoped, non-sensitive, access-controlled, and retained only as needed.
- [ ] Sampling, aggregation, and retention match consequence and diagnostic need.
- [ ] Diagnostic mode is approved, time-bounded, redacted, access-controlled, and has a removal trigger.
- [ ] Metric/cardinality budgets and collection cost have owners where runtime telemetry is added.

**Observability verification**

| gate | assertion |
| --- | --- |
| Schema test | Required fields and state enums are valid for each emitted event type. |
| Redaction test | Representative sensitive values never appear in logs/events. |
| Deterministic fixture event | Null/cancellation/blocking/retry fixture emits the expected typed category and correlation. |
| Collection-health test | Dropped/unavailable pipeline produces degraded/unknown state, not zero. |
| Cardinality review | Dimension values remain bounded under representative input. |
| Integration/synthetic check | Event reaches intended sink/view with target build/config identity. |
| Response drill | Owner can move from alert/evidence to containment, route, or recovery and record the result. |

Local tests cannot prove production delivery, retention, dashboard correctness, or operator response. Those require target integration and operations ownership.

**Contrastive events**

Good: `KQ-CANCEL-002` records parent-request cancellation, adapter operation class, cleanup complete, cache mutation absent, test fixture ID, target build, and no claim about underlying Java interruption.

Bad: a log prints request payload, user ID, token fragment, and stack trace, then reports `error=false` because no parser consumed the message. It leaks data and provides no stable category or collection health.

Borderline: a dashboard shows zero cancellation failures during a telemetry outage. The correct state is `collection_degraded`; no reliability conclusion is permitted.

**Feedback linkage**

Use observed recurrence, gate noise, retry amplification, collection gaps, and route delay to propose one bounded control change. Review causality and counter-metrics before adopting it. Observability can justify narrowing or removing a gate as well as adding one.

No target runtime event, latency distribution, reviewer-time measurement, cardinality result, or operations drill was observed for this reference. The schemas above are proposed contracts.

## Performance Verification Method

Run a performance experiment only when a decision or release claim depends on cost, latency, throughput, resource use, blocking saturation, gate duration, or workflow effort. Most nullability, state-modeling, cancellation, and ownership repairs need semantic and integration evidence but no performance claim.

No target benchmark, load test, gate-duration study, reviewer-time study, or performance improvement was produced during this reference evolution.

**Performance claim classes**

| claim_class | examples | appropriate method | common invalid shortcut |
| --- | --- | --- | --- |
| `runtime_latency_throughput` | Blocking-client isolation, coroutine concurrency, request/worker throughput. | Correctness-equivalent integration/load experiment in representative environment. | Unit timing or `Dispatchers.IO` presence. |
| `resource_and_saturation` | Threads, dispatcher queue, memory, allocations, connection/resource use. | Instrumented controlled workload with resource counters and failure/cancellation paths. | Source inspection alone. |
| `local_algorithm_allocation` | Value/outcome representation or mapping hot path. | Profiling then appropriate benchmark with realistic data and JIT/GC controls. | One wall-clock run. |
| `build_and_gate_cost` | Analyzer, test suite, compilation, baseline change. | Pinned tool/config/population and repeated CI-like runs. | Comparing different file/rule populations. |
| `review_workflow_effort` | KQEP profile or gate process changes reviewer/implementation time. | Comparable task cohorts, stable definitions, outcome and rework counter-metrics. | One "focused session" anecdote. |
| `no_performance_claim` | Semantic correction where performance does not govern acceptance. | Record not applicable/no claim; run normal regression gates. | Inventing a benchmark to appear complete. |

**Experiment sequence**

1. State a falsifiable target-scoped claim and why the result changes a decision.
2. Name the accountable threshold/SLO or decision owner before inspecting results when practical.
3. Freeze baseline and candidate build, dependency, configuration, environment, and workload identity.
4. Prove correctness equivalence, including expected failure, absence, cancellation, and side effects relevant to the change.
5. Choose the least expensive valid method: profiler, benchmark, integration load, runtime observation, gate timing, or workflow cohort.
6. Define warmup, order/randomization, repetition, sample capture, counter-metrics, and abort conditions.
7. Execute without changing multiple variables; retain raw observations and failures.
8. Analyze distribution and uncertainty at a level supported by samples.
9. Decide retain, narrow, optimize, route, rollback, or no action; report non-claims.
10. Attach invalidation trigger for environment, workload, tool, dependency, or semantic change.

**Correctness equivalence gate**

Before comparing performance, verify both candidates:

- accept and reject the same valid/invalid boundary inputs under the desired contract;
- preserve the same caller-visible state taxonomy;
- preserve parent/lifecycle cancellation and cleanup;
- produce equivalent side effects, transactions, cache/state outcomes, and ordering where required;
- classify failures and retries equivalently;
- preserve identity/equality/persistence behavior;
- pass relevant focused and integration gates.

If behavior differs intentionally, performance results answer a different product question and must be reported with that tradeoff. A faster path that drops validation, error detail, cancellation, synchronization, or durability is not an optimization of the same contract.

**Runtime experiment packet**

| field | required content |
| --- | --- |
| `claim_and_decision` | Metric, target scope, decision enabled, owner. |
| `baseline_candidate_identity` | Commits/builds, Kotlin/JVM, dependencies, flags, framework/config. |
| `environment` | Hardware/container/runtime, OS/JVM, resource limits, co-tenancy/noise controls. |
| `workload` | Input distributions, size, concurrency, arrival pattern, state/cache setup, success/failure/cancellation mix. |
| `correctness_oracle` | Output/state/side-effect equivalence checks. |
| `method` | Warmup, order, repetitions, measurement interval, profiler/instrumentation overhead. |
| `metrics` | Wall/CPU time, latency distribution, throughput, active/queued threads/tasks, memory/allocations, errors/cancellations as applicable. |
| `counter_metrics` | Correctness, failures, retries, queue growth, GC, resource consumption, operational complexity. |
| `raw_and_summary` | Raw observations or durable location plus summaries supported by sample size. |
| `uncertainty_and_confounds` | Noise, cache/JIT/GC, environment mismatch, unmodeled workload. |
| `acceptance_and_result` | Predefined threshold/owner and final decision, including no comparison. |

Percentiles are conditional. Report p50/p95/p99 only when the population and sample method make them meaningful. For small runs, show raw observations/range and avoid tail precision. Never omit errors, timeouts, cancellations, or dropped work from the denominator to make latency look better.

**Blocking and dispatcher profile**

For hidden-blocking corrections, capture actual dependency behavior, execution context, active/queued work, concurrency/admission policy, caller deadline, cancellation versus interruption, and downstream resource use. Exercise steady and burst patterns plus failure/cancellation. A thread switch can reduce event-loop blocking yet still create an unbounded IO queue; report both.

**Build and analyzer cost profile**

Pin wrapper, tool/plugin, configuration, baseline, modules/source sets, daemon/cache state, and CI-like environment. Compare equivalent populations and rule sets. A new baseline or excluded module creates a series boundary. Pair timing with actionable finding yield, flakiness, and escaped-mechanism review so speed does not reward weaker coverage.

**Workflow effort profile**

Define task cohort by risk/visibility/mechanism, packet profile, reviewer role, and completion quality. Measure effort alongside review reversals, rework, blocker precision, and escaped defects. Do not infer process improvement from one task or rank individuals. If cohort comparability is weak, report qualitative cases instead of a percentage.

**Validity checklist**

- [ ] Only one intended mechanism changed between baseline and candidate, or confounds are named.
- [ ] Correctness-equivalent outputs and failure/cancellation behavior are checked.
- [ ] Environment and workload represent the decision being made.
- [ ] Warmup/JIT/cache/GC/order effects are controlled or reported.
- [ ] Sample and percentile claims are supportable.
- [ ] Failures, retries, dropped work, and saturation remain in evidence.
- [ ] Instrumentation overhead and collection health are understood.
- [ ] Threshold and owner were not invented after seeing results.
- [ ] Counter-metrics prevent obvious gaming.
- [ ] Result is not generalized beyond target/version/environment/workload.

Abort or report `no_comparison` when correctness differs unexpectedly, collection is degraded, environment identity is unknown, sample capture is incomplete, or a confounding configuration change cannot be separated.

**Contrastive experiment records**

Good: compare the same blocking Java-client behavior before and after adapter-owned dispatcher isolation under a controlled workload. Verify identical typed outcomes and cancellation semantics, capture active/queued work and resource use, and leave production capacity unclaimed if the environment is not representative.

Bad: time one happy-path unit call before and after replacing a sealed outcome with boolean, report lower nanoseconds, and ignore lost failure states and JIT variation.

Borderline: target module build becomes faster after narrowing analyzer scope. The observation is valid for the new population but cannot be called a tool optimization until equivalent rule/file coverage is compared. Treat it as a policy tradeoff with a series boundary.

**Decision outcomes**

- `retain`: candidate meets semantic and owner performance criteria.
- `narrow`: benefit exists only for a bounded path/workload.
- `optimize`: measured relevant cost justifies another controlled change.
- `route`: specialist/runtime/operations evidence is required.
- `rollback`: semantic, operational, or complexity cost exceeds accepted benefit.
- `no_action`: difference is immaterial or evidence cannot support a change.
- `no_claim`: performance is outside scope and no downstream decision relies on it.

The best outcome can be rejecting an optimization whose complexity exceeds measured value. Performance discipline protects semantic quality from being traded away under precise-looking but invalid numbers.

## Scale Boundary Statement

Kotlin Quality Antipattern Gates remains sufficient while one integration owner can trace and verify the affected uncertainty, state, identity, lifecycle, blocking, mutable-state, and gate contracts. It becomes insufficient for a claim when the next invariant requires authority, durability, compatibility, runtime capacity, or coordination that the local path cannot own.

No target repository size, file count, caller count, traffic, dispatcher capacity, owner count, or SLO was measured. The boundaries below are qualitative and evidence-triggered, not universal numeric limits.

**Local sufficiency test**

This reference can remain primary when:

- the affected ingress-to-caller path and side effects are bounded and inspectable;
- state/identity meaning is decided by an available owner;
- coroutine/lifecycle/state ownership is local or governed by a current platform contract;
- blocking behavior can be classified and no production-capacity claim is required, or target measurement is available;
- public/persisted compatibility is absent or has a bounded adapter/migration;
- focused and relevant integration gates can be run or honestly attributed;
- one owner can reconcile the final contract and handoff.

If one condition fails, route the affected claim; do not automatically transfer the entire task.

**Pressure indicators versus hard boundaries**

| dimension | pressure_indicator | hard_boundary_for_this_reference_alone | evidence_that_can_resolve_or_route |
| --- | --- | --- | --- |
| Caller/API breadth | Many callers/modules or repeated translations. | Public contract migration across independently versioned consumers. | Consumer inventory, compatibility/version plan, integration owner. |
| Persistence/identity | Entity used in caches/collections or several repositories. | Schema/data/identity migration with irreversible or cross-release effects. | Migration/rollback/data recovery and persistence owner. |
| Coroutine/lifecycle | Multiple scopes, supervision, or shared dispatcher. | Work must survive caller/process or spans durable distributed execution. | Lifecycle/platform contract or durable job architecture and operations owner. |
| Blocking/concurrency | Shared dispatcher or growing queue/resource contention. | Release requires production capacity/SLO without representative evidence. | Controlled runtime experiment, resource model, SLO acceptance. |
| Security/side effects | Failures affect privileged or non-idempotent action. | Cross-system retries/idempotency/authorization cannot be owned locally. | Protected-transition design, security/resilience ownership, negative/replay evidence. |
| Framework/generated code | Adapter touches generated/proxied/lifecycle-managed type. | Correct behavior depends on opaque/version-specific framework contract. | Versioned framework source/docs and target integration fixture. |
| Source discovery | Candidate guidance expands across many files. | Canonical authority or relevant target path cannot be bounded. | Ranked claim-specific source map and dependency/caller narrowing. |
| Ownership | Several reviewers or teams contribute. | No owner can decide shared contract, risk, or integration. | Claim owner map and explicit final integration authority. |
| Distributed agent execution | Disjoint references/adapters can be processed separately. | Multiple workers would rewrite one file or unresolved shared contract. | Exclusive file/claim ownership, durable checkpoints, merge/equivalence gate. |
| Production traffic | Local tests show semantics. | Runtime claim is required but SLO/workload/environment/operations owner is absent. | Measured target profile and owner acceptance; otherwise no claim. |

**Route ladder**

| route | choose_when | preserved_invariant | added_cost_and_risk |
| --- | --- | --- | --- |
| `keep_local` | One owner/path/test surface can close claim. | Fast causal feedback and minimal translation. | Can miss hidden callers without initial inventory. |
| `narrow_by_boundary` | Large repository but one ingress-to-caller path is consequential. | End-to-end semantics for selected claim. | Sibling variants remain unreviewed; no broad claim. |
| `adapter_containment` | External/framework/public uncertainty needs stable internal contract. | Uncertainty localized and testable. | Mapping/compatibility layer can drift. |
| `shard_disjoint_implementation` | Several adapters/modules share a frozen contract and disjoint writes. | Parallel throughput with local tests. | Integration/contract drift; needs one merge owner. |
| `federate_versioned_contract` | Independent domains/services need interoperability without identical internals. | Shared wire/API semantics with domain autonomy. | Versioning, compatibility, governance, cross-system tests. |
| `persistent_or_durable_architecture` | Work/state must survive lifecycle/process/restart. | Recovery and ownership beyond coroutine lifetime. | Persistence, idempotency, retries, operations, monitoring. |
| `platform_specialist_route` | Framework, security, testing, runtime, or persistence authority dominates. | Correct claim ownership. | Coordination and return reconciliation. |
| `stop_and_block` | Required policy, permission, source identity, rollback, or SLO owner is absent. | Prevents unsupported promotion. | Delays change; requires explicit resume condition. |

Creating a service, queue, shared library, or central dispatcher is not inherently a scaling solution. It is justified only when it owns a missing invariant more clearly and its operational/coordination cost is accepted.

**Distributed execution contract**

1. Freeze shared claim IDs, state taxonomy, identity semantics, lifecycle/side-effect contract, and gate signatures before parallel implementation.
2. Assign one exclusive owner per file and one primary owner per claim.
3. Give each shard disjoint writes, source/target identity, exclusions, and focused tests.
4. Persist progress at atomic boundaries; do not hold several completed units only in transient context.
5. Prevent workers from editing shared queue/spec/test/other-owner artifacts without explicit authority.
6. Integrate through contract/version compatibility and end-to-end equivalence tests, not merely clean merges.
7. Report local green and external/shared reds separately.
8. Retain rollback and final integration owner.

Parallelism is useful after semantic decomposition. Before that, it multiplies inconsistent assumptions and merge conflicts.

**Large-codebase narrowing**

Use repository-native search, dependency/caller maps, build/module metadata, generated-source boundaries, and ownership data to select the relevant population. Record source/time/tool limits. Validate critical edges manually because static maps can miss reflection, dependency injection, generated bindings, runtime registration, and external calls.

A source list without claim-specific authority is insufficient. A graph without semantic state or runtime behavior is navigation evidence, not correctness proof.

**Scale examples**

Good: eight independent Java adapters share a versioned internal outcome contract. Each owner migrates a disjoint adapter with null/cancellation fixtures; one integration owner verifies caller compatibility and removes temporary shims.

Bad: a global search replaces every `!!` and data class across the monorepo under several agents, without shared state semantics, framework exceptions, or file ownership.

Borderline: a platform team centralizes blocking calls on one dispatcher. This can be sound when dependency classes, concurrency/admission, cancellation limits, observability, capacity measurement, and operations ownership are explicit. A larger pool constant alone does not cross the promotion gate.

**Scale-in and rollback**

Shared controls should be narrowed, removed, or decentralized when they add coordination latency, duplicate stronger type/test guarantees, emit persistent noise, become a resource bottleneck, or erase legitimate domain differences. Versioned contracts and adapters should permit rollback without reintroducing platform types, detached work, or ambiguous outcomes.

Scalable Kotlin quality is the ability to localize decisions, ownership, evidence, and failures while preserving integration semantics. It is not the ability to enforce one syntax or one process everywhere.

## Future Refresh Search Queries

The exact seed query strings are preserved below. None was executed. They are queued discovery prompts with `unexecuted_no_browse` status and contribute no external facts to this reference.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | kotlin quality antipattern gates official documentation best practices |
| `github_repository_query_phrase` | kotlin quality antipattern gates GitHub repository examples |
| `release_notes_query_phrase` | kotlin quality antipattern gates changelog release notes migration |

**Decision-triggered query plan**

| query_label | use_only_when | likely_first_filter | stop_or_promotion_condition |
| --- | --- | --- | --- |
| `official_docs_query_phrase` | A precise Kotlin language, coroutine, framework, or tool contract remains unresolved after local/target inspection. | Prefer official Kotlin, coroutine, Spring, Ktor, Gradle/Maven, or analyzer domains relevant to the claim. | Stop when a precise versioned primary artifact plus target reproduction closes the claim; broad result pages remain discovery only. |
| `github_repository_query_phrase` | Implementation, tests, examples, issue history, or release provenance is needed for a versioned behavior. | Prefer official organization repositories and immutable tags/commits. | Capture exact repository/revision/path; do not treat example or issue discussion as target behavior without reproduction. |
| `release_notes_query_phrase` | A compiler, coroutine, framework, plugin, analyzer, or build-tool upgrade may invalidate current guidance. | Prefer official release notes/changelog/migration guide for the installed-to-target versions. | Map each relevant change to target config/code/tests; unrelated release content does not reopen all claims. |

The query wording may not match canonical terminology and has not been evaluated. During authorized research, refine it around a falsifiable claim, such as:

- Kotlin/Java platform type behavior for the target compiler and Java annotations;
- cancellation behavior for the exact `kotlinx-coroutines` version and API;
- Spring or Ktor lifecycle/model behavior for installed versions/plugins;
- Detekt or ktlint rule/configuration migration for configured plugin versions;
- Gradle/Maven/Kotlin compiler change affecting target gates.

Do not search the public web for domain state meaning, accepted risk, release approval, or production SLO ownership. Those are local authority questions.

**Research ladder**

1. State unresolved claim, consequence, target identity, and why local source/code/tests are insufficient.
2. Check direct known official roots and versioned artifacts before broad search.
3. Use broad query only to discover precise primary material or terminology.
4. Select the minimum relevant primary artifacts; secondary material may guide discovery but remains unpromoted.
5. Record artifact identity, date, version scope, concise support/limits, and conflicts.
6. Reproduce or validate against target code/configuration/tests.
7. Decide accept, adapt, reject for scope, informative only, contradictory, or blocked.
8. Update affected claims and invalidation triggers; leave unrelated guidance unchanged.

**Research record**

| field | required content |
| --- | --- |
| `authorization_and_time` | Who authorized network retrieval and when. |
| `claim_and_target` | Falsifiable claim plus target versions/configuration. |
| `query_and_filters` | Exact query, refinements, domains/repositories, and why selected. |
| `selected_artifact_identity` | URL, title, source type, retrieval date, tag/commit/release/version where available. |
| `support_and_limit` | Concise relevant span/paraphrase, claim supported, and non-claims. |
| `authority_and_lineage` | Official/primary/example/secondary status and duplicate relationships. |
| `target_match_and_reproduction` | Version/config comparison and target test/source evidence. |
| `conflict` | Local policy, target behavior, or another source disagreement. |
| `outcome` | Accept, adapt, reject, informative only, contradictory, blocked, or no result. |
| `invalidation_and_owner` | Change that reopens claim and who refreshes it. |

**Good research outcome**

An authorized query locates official versioned coroutine cancellation documentation and tests at the target dependency revision. The target fixture reproduces parent cancellation and cleanup. The source supports the contract; the target test supports applicability. The claim is promoted with both limits.

**Bad research outcome**

A search-result snippet says `GlobalScope` is discouraged, so all asynchronous code in the repository is rewritten. No source is opened, target lifecycle is not mapped, and process-lifetime work is not distinguished.

**Borderline research outcome**

A Spring Kotlin guide demonstrates a useful binding/test pattern on a different major version. Keep it `informative_only`, derive a target experiment, and promote only after APIs and lifecycle are adapted and verified. Finding the guide is not failure; adopting it directly would be.

**Research integrity controls**

- Cite/open the selected artifact, not a search-result page or snippet.
- Record mutable-page date/version or immutable revision when available.
- Do not count reposts or derivative copies as independent evidence.
- Quote minimally and preserve source meaning; prefer concise paraphrase with direct support.
- Do not infer current target behavior from an official example.
- Keep search-result absence distinct from evidence that no guidance exists.
- Stop when claim closure is reached; result volume is not completeness.
- Retire queries that repeatedly add no decision-relevant evidence or replace them with stable direct sources.

**Current no-results ledger**

| query_label | execution_state | selected_results | current_external_claims |
| --- | --- | ---: | ---: |
| `official_docs_query_phrase` | `unexecuted_no_browse` | 0 | 0 |
| `github_repository_query_phrase` | `unexecuted_no_browse` | 0 | 0 |
| `release_notes_query_phrase` | `unexecuted_no_browse` | 0 | 0 |

The zeroes above count deliberately selected results in this pass, not the existence or quality of external information. No query was sent, so search coverage and query usefulness remain unknown.

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.

These seed labels are retained, with one critical correction in use: the public URLs were not opened, so this file contains no currently observed `external_research_sourced_fact`. Their rows are `unrefreshed_no_browse` pointers. Synthesis in this file combines observed local material with coding/systems reasoning and explicitly identified target needs, not with newly retrieved public content.

**Evidence families and states**

| evidence_family_or_state | establishes | does_not_establish |
| --- | --- | --- |
| `local_corpus_sourced_fact` | Exact content and identity of a mapped local source. | Target applicability, current public freshness, or achieved outcome. |
| `target_source_observed` | What inspected Kotlin/Java/build/config code currently contains. | Desired policy, unexecuted behavior, or production frequency. |
| `target_test_observed` | Behavior under named fixtures/environment. | Untested inputs/schedules, production capacity, or domain authority. |
| `target_runtime_observed` | Dynamic behavior under captured build/environment/workload. | Other environments/workloads or causal generalization without controls. |
| `owner_policy_accepted` | Desired domain/lifecycle/security/operations decision or accepted risk for a scope. | That code enforces it or runtime meets it. |
| `external_research_sourced_fact` | Content of a directly retrieved external artifact under recorded date/version/span. | Target applicability without matching and reproduction. |
| `external_pointer_unrefreshed` | Where authorized future research may begin. | Any current external factual claim. |
| `combined_evidence_inference_note` | Bounded reasoning from stated premises, alternatives, and limits. | A newly observed fact or universal result. |
| `proposed_contract_or_method` | A design, schema, test, metric, experiment, or workflow awaiting target use. | Implementation, acceptance, or effectiveness. |
| `characterization_observed` | Current behavior preserved by a test/trace. | That current behavior is desired or safe. |
| `verified_for_scope` | Named claim passed named evidence for a declared population. | Broader correctness or future validity. |
| `accepted_risk` | Accountable owner accepts a consequence under conditions. | Absence of defect or risk. |
| `contradictory_evidence` | Material sources/evidence disagree for overlapping scope. | Which side wins until authority and target closure are resolved. |
| `blocked` | Exact missing authority, evidence, permission, environment, or dependency prevents promotion. | Failure of every unrelated action. |
| `no_claim` | Dimension is outside scope and downstream decisions must not rely on it. | A pass, fail, or healthy zero. |

**Claim card**

Use a full card for consequential, shared, public, persisted, concurrent, runtime-sensitive, or reusable guidance:

| claim_card_field | content |
| --- | --- |
| `claim_id_and_text` | Stable ID and one falsifiable statement. |
| `scope_and_population` | Target, versions/config, paths/callers, fixtures/workload, inclusions/exclusions. |
| `evidence_state` | One or more states above, kept distinct. |
| `support` | Source/path/test/runtime/owner record that actually supports the statement. |
| `counterevidence_and_limit` | Conflict, non-claims, uncertainty, population boundary. |
| `inference_or_decision` | Reasoning, alternatives, authority, and chosen action. |
| `verification_and_result` | Gate, result, population, and failure response. |
| `owner_and_risk` | Accountable implementation/policy/operations owner and accepted residual risk. |
| `invalidation` | Source/code/version/config/caller/workload/policy change that reopens it. |
| `reuse_status` | Local only, reusable with adaptation, superseded, retired, or blocked. |

For low-risk orientation, inline labels and a direct source link may suffice. Escalate to a card when the claim begins directing implementation, release, migration, or shared policy.

**Promotion lifecycle**

```text
pointer or local observation
    -> target inspection
    -> bounded inference or proposed contract
    -> focused verification
    -> verified_for_scope and/or owner acceptance
    -> integration/operational promotion as applicable
    -> selective invalidation, supersession, or retirement
```

Promotion is claim-specific. A test result can promote target behavior for its fixture but cannot promote domain policy. Owner policy can promote desired semantics but cannot promote implementation enforcement. Runtime observation can promote behavior for an environment/workload but cannot retroactively prove source intent.

**Precedence by claim type**

| question | primary authority | reconciliation requirement |
| --- | --- | --- |
| What did the inherited reference say? | Local source identity and text. | Faithful paraphrase and scope. |
| What exists now? | Target source/config/build. | Caller/dependency trace and generated/framework context. |
| What happens under fixture? | Target test observation. | Fixture validity and population limits. |
| What should state/identity mean? | Accountable domain/API/lifecycle owner. | Desired-contract tests and migration implications. |
| What does a version promise? | Versioned official external artifact. | Target version/config match and reproduction. |
| What happens under load? | Controlled target runtime evidence. | Correctness equivalence, workload/environment, uncertainty, operations owner. |
| Is residual risk acceptable? | Accountable risk owner. | Consequence, alternatives, evidence, and review trigger. |

No source globally outranks all others. Split conflicts into descriptive, normative, behavioral, versioned, and operational claims before choosing authority.

**Prohibited inference patterns**

| observed evidence | prohibited promotion |
| --- | --- |
| Official root URL listed | "Current official guidance confirms this recommendation." |
| Local archive source says prefer X | "Target repository implements X correctly." |
| Target code uses X | "X is desired policy or safe." |
| Unit test passes | "All inputs, schedules, or production behavior are correct." |
| Analyzer is green | "No Kotlin quality defect exists." |
| Build succeeds | "Cancellation, blocking, identity, and state semantics are verified." |
| Owner accepts risk | "The implementation enforces the contract." |
| Runtime sample meets threshold | "All environments/workloads or future releases meet it." |
| No event observed while collection is degraded | "Failure rate is zero." |
| Guidance is detailed and internally coherent | "The workflow is effective in real use." |

**Contrastive claim cards**

Good: `local_corpus_sourced_fact` identifies swallowed cancellation as a hazard. `target_source_observed` finds a broad catch around a suspending client. `proposed_contract_or_method` rethrows cancellation. `target_test_observed` verifies parent cancellation, cleanup, and no fallback side effect for one fixture. The claim becomes `verified_for_scope`; underlying blocking-call interruption remains `no_claim`.

Bad: the `kotlinx.coroutines` repository URL is listed, therefore all service coroutines are declared structured and reliable. No page, version, target scope, or test exists.

Borderline: characterization tests show structural equality for a data-class entity, while the domain owner wants persistence identity. Current behavior is observed and desired policy is accepted, but migration remains proposed/blocked until compatibility and integration evidence exist. Both records are useful without calling either complete enforcement.

**Known ledger for this Assignment 9 evolution**

Known and observed locally:

- The working seed and archive seed began byte-identical at SHA-256 `2d5de11b9ddf670d8a3328864fdb8dfb5a68aca630c06138cce486c84c636c8f`.
- The mapped local Kotlin quality source was read completely at SHA-256 `1b393027a06d8a4ca7790822c9c29485bd3e8d59d77d7dfc310a8a761cb44400`.
- The local source contains ten anti-patterns, an eight-item reliability stack, representative Gradle/Maven commands and discovery queries, and a six-axis review pass.
- The frozen queue assigned 115 contiguous semantic blocks and 26 headings to Delta file order 9 before edits.
- This evolved reference preserves the exact 26 original headings in order; its matching packet contains ten exact questions and six populated fields per question.

Reasoned synthesis, requiring target adaptation:

- Information and ownership preservation unify the local anti-patterns.
- Claim-specific evidence, tradeoffs, reliability profiles, failure handling, retry/backpressure, observability, performance, and scale methods in this file.
- The proposed KQEP schema, event model, metric cards, and workload routes.

Unknown or explicitly unobserved:

- Current content of the four public source URLs and results of the three future search queries.
- Any target Kotlin repository's tool configuration, framework behavior, domain state meaning, code findings, tests, runtime, security, or operations policy.
- Effectiveness, review cost, defect reduction, latency, capacity, reliability, or adoption of this guidance.
- Whether candidate adjacent references are semantically sufficient at a future selection time.

**Final evidence audit**

- [ ] Every promoted claim has a source/evidence class capable of establishing it.
- [ ] Mixed sentences do not hide facts, inference, proposal, and result under one label.
- [ ] Local and external identity/freshness are explicit.
- [ ] Target scope, version/config, population, and non-claims are visible.
- [ ] Characterization and desired behavior are distinct.
- [ ] Owner policy and implementation enforcement are distinct.
- [ ] Tests/analyzers/build/runtime are not generalized beyond their populations.
- [ ] Contradictions are preserved and resolved by claim authority.
- [ ] Missing data is not represented as zero or pass.
- [ ] Invalidation and reuse conditions accompany durable guidance.
- [ ] Structural verifier success is not described as Kotlin target effectiveness.

**Reuse and derivation protocol**

When copying guidance into a prompt, review, new reference, or policy, carry at least: source/target identity, claim scope, evidence state, support, limit/no-claim, target adaptation requirement, and invalidation trigger. A direct link to this claim card can replace repeated prose when durable. Revalidate target code/configuration/tests; do not inherit a prior target result automatically.

Provenance compression is safe only when authority, scope, limits, and reopening conditions survive. Otherwise bounded guidance becomes an unsupported universal rule.
