# Executable Traceability Template Patterns

Use this reference to make consequential software claims reviewable from intent through current evidence. The primary question is not whether every document contains an identifier. It is whether a reviewer can determine what behavior is promised, which verifier can disprove it, which implementation owns it, what was actually observed, which environment produced that observation, and whether the current release decision is justified.

The three mapped local paths are byte-identical copies of one historical 118-line template source. That source demonstrates requirement contracts, a traceability matrix, a TDD plan, language-specific test skeletons, vague-to-executable rewrites, and a pre-commit checklist. It is useful evidence for artifact shapes and authoring questions. Its example identifiers, numeric thresholds, test names, phase labels, and unresolved template tokens are illustrations rather than measured target-project facts. The inherited public mappings were not browsed during this evolution.

**Core traceability chain**

```text
User need or risk
        |
        v
Atomic accepted claim -----> owner and lifecycle state
        |
        +-----> verification case -----> executable assertion
        |                                  |
        |                                  v
        +-----> implementation owner ---> observed run evidence
                                           |
                                           v
                                  release or exception decision
                                           |
                                           v
                                  change invalidation and rerun
```

A link is executable when it can change work or status. A changed requirement should invalidate affected verification and evidence. A failed verifier should block, narrow, or explicitly except the affected claim. A passing run should record enough identity and environment to show what passed. A superseded claim should route implementations, tests, and consumers to its replacement. A matrix that cannot drive any of those decisions is an index, not a control.

**Minimum traceability objects**

| Object | Required meaning | Useful fields | Failure if omitted |
|---|---|---|---|
| Need, risk, or decision | Why the claim exists and whose outcome changes | Source, actor, consequence, scope owner | Requirements become detached from user value or risk |
| Requirement | One observable behavior or bounded quality under stated conditions | Stable ID, title, trigger, outcome, boundaries, priority, owner, state | Broad prose cannot be disproved or changed safely |
| Verification case | A scenario or analysis capable of revealing a requirement defect | Stable case ID, requirement links, level, fixture, expected observation, limitation | Coverage exists by name but not by detection power |
| Executable assertion | The concrete check inside a test, analyzer, review, or drill | Assertion location, failure signal, controlled input, negative case | A test can pass while checking an incidental detail |
| Implementation link | The code, configuration, migration, document, or service boundary that owns the behavior | Target path or symbol, owning module, change reference | Impact analysis misses affected production artifacts |
| Evidence record | What verifier ran against which artifact and environment, with what result | Artifact hash or version, command, environment, time, result, retained output | A green claim outlives the run that once supported it |
| Decision record | Whether the claim may ship, is excepted, is blocked, or is retired | Status, approver role, evidence set, exception, expiry, replacement | Passing tests are mistaken for product acceptance automatically |
| Invalidation edge | Which changes make prior evidence stale | Trigger, affected links, required rerun, owner | Semantically obsolete evidence remains green |

**Recommended default workflow**

1. **Discover the decision.** Name the user need, risk, compatibility promise, or policy whose outcome matters. Keep exploratory questions separate from accepted obligations.
2. **Write atomic claims.** Give each accepted claim a stable identity and state one trigger or precondition, one primary observable outcome, applicable boundaries, and explicit quality units only when a real target and method exist.
3. **Challenge the claim.** Add normal, negative, boundary, failure, and interaction cases in proportion to consequence. Confirm that each case could reveal a meaningful violation.
4. **Choose the verifier.** Use unit, integration, contract, end-to-end, static, review, performance, security, migration, or operational evidence according to the claim. Do not force qualitative or governance claims into an unrelated unit test.
5. **Link implementation ownership.** Identify the modules, interfaces, configurations, migrations, or documents that realize the claim and the owner who reconciles changes.
6. **Observe an initial failure.** Before implementation, confirm the new verifier fails or is absent for the expected reason. A passing test that predates the behavior may not establish that the new requirement is protected.
7. **Implement minimally and refactor.** Satisfy the accepted claim without broadening scope, then improve structure while preserving all relevant evidence.
8. **Capture run evidence.** Record the exact artifact, environment, command or review method, result, failure or skip classes, and limitations. A test definition is not a test run.
9. **Reconcile release status.** Block missing evidence, approve supported claims, or record a bounded exception with owner, consequence, expiry, and compensating evidence.
10. **Propagate change.** When need, claim, implementation, verifier, fixture, environment, or support range changes, invalidate dependent evidence and rerun the smallest complete affected set.

**Mapping semantics**

Traceability is many-to-many. One requirement can need several evidence types because unit behavior, integration boundaries, migration, performance, and denial fail differently. One scenario can cover several requirements when their interaction is the behavior under test. Preserve the assertion-level relationship in either direction; do not duplicate tests merely to create one row per identifier.

Not every accepted claim maps to an automated test. A dependency-license policy may map to an analyzer and review. A disaster-recovery claim may map to a controlled drill. A user-facing wording claim may map to an accessibility or product review. A performance claim maps to a versioned workload and measurement method. Each alternative still needs an owner, expected observation, evidence record, expiry, and limitation.

**Concrete bounded example**

Suppose a product requires a revoked session to lose protected access promptly. A useful requirement record could be:

| Field | Accepted value |
|---|---|
| Requirement ID | `REQ-AUTH-014` |
| Trigger | A previously active session has been revoked successfully |
| Primary outcome | The next protected request using that session is denied with the service's typed unauthenticated result |
| Boundary | No protected handler may use cached authorization after revocation is visible to that handler's consistency model |
| Security observation | Audit evidence identifies the correlation and denial class without recording the session secret |
| Excluded claim | This requirement does not define a universal propagation duration; a measured target requires the selected architecture and workload |

Its traceability may include a session-store unit case, an HTTP integration case, a cache-invalidation interaction case, a secret-redaction assertion, and a measured propagation case only when a supported timing objective exists. A shallow test that merely calls the revoke function and checks success does not prove protected access is denied afterward.

**Good, bad, and borderline use**

Good traceability links `REQ-AUTH-014` to assertions that would fail if cached authorization remained usable, captures evidence from the current service artifact, and invalidates that evidence when cache semantics change.

Bad traceability adds the identifier to a test name while the assertion checks only that a response object exists. The matrix is complete syntactically but cannot reveal the requirement defect.

Borderline traceability records an exploratory spike against a candidate cache design. Keep its result as experiment evidence, not accepted release evidence, until architecture, consistency boundary, workload, and requirement owner stabilize.

**Use this reference directly when:**

- ambiguous intent must become testable behavioral or quality claims;
- several modules, teams, releases, or compatibility promises share a change;
- a regression needs requirement-level prevention and impact analysis;
- performance, reliability, security, migration, or operational language needs a real method;
- reviewers must distinguish test definition, observed run, accepted exception, and current release status; or
- a template, generator, or agent will propagate requirement and verification conventions.

Use a lightweight profile for a small reversible change: state the behavior in the test, link the issue or decision, run the focused evidence, and retain the result. Route product discovery, architecture selection, test implementation details, performance experimentation, regulatory interpretation, or release governance to their specialist owners while keeping the relevant claim and evidence edges here.

This reference stops being sufficient when it is asked to invent the product outcome, choose architecture without evidence, guarantee production behavior from a template, or replace domain approval. It coordinates traceability; it does not make every linked claim true. The durable result is a trustworthy answer to what changed, what proves it, what evidence is current, and what must happen before shipment.

## Source Evidence Mapping Table

Treat each source as evidence for a bounded claim rather than authority for the whole traceability lifecycle. The three local paths contain exactly the same 118-line file with SHA-256 `c7e44220936452079080a46fb23725ec5b3332fb8b1a8a082eaeed76b2bd2812`. Preserve all locations for lineage and discovery, but count the technical content once.

| Source | Inspection and identity state | Permitted use | Material limit | First applicability gate |
|---|---|---|---|---|
| `agents-used-monthly-archive/codex-skills-202602/executable-specs-01/references/executable-specs-templates.md` | Complete local read; earliest frozen copy; shared content hash | Primary historical evidence for requirement-contract, matrix, development-plan, language-skeleton, rewrite, and quality-gate artifact shapes | Its identifier forms, test names, threshold examples, and checklist terms are illustrative; it contains no target repository or run evidence | Adapt one real claim, connect it to a disconfirming verifier, and exercise the target workflow |
| `agents-used-monthly-archive/codex-skills-202603/executable-specs-01/references/executable-specs-templates.md` | Complete local read; byte-identical later archive locator | Shows the template persisted into a later archived corpus and helps locate dependent material | Duplicate bytes add no independent corroboration or currentness | Compare hash and lineage; treat divergence as new evidence only after independent review |
| `unclassified-yet/Executable Specifications Templates.md` | Complete local read; byte-identical unclassified locator | Helps discover current repository references to the same content | Location does not make the template current policy or prove active use | Identify owner and consumers before treating the path as maintained guidance |
| `https://developers.openai.com/codex/guides/agents-md` | Inherited public URL; not browsed in this evolution | Future target for deciding how repository-level agent instructions expose traceability conventions | Cannot establish requirement semantics, test correctness, evidence freshness, or release approval here | Select a Codex instruction-placement decision, inspect the current direct source, and validate target behavior |
| `https://docs.github.com/actions` | Inherited public documentation root; not browsed in this evolution | Future target for CI workflow syntax, event, permission, artifact, and result-retention questions after a GitHub Actions gate is selected | A CI platform cannot decide product requirements or prove that assertions cover them | Inspect the exact current feature and run known-pass, known-fail, skip, cancellation, and permission cases in the target repository |
| `https://agents.md/` | Inherited public format location; not browsed in this evolution | Future context for instruction-file scope and interoperability when that format is selected | Does not define a project's claim identity, traceability graph, test harness, or release policy | Confirm format applicability, precedence, supported tooling, and repository behavior before reuse |
| Target project evidence | Not available in this generic reference | Current authority for accepted needs, local identifiers, code ownership, verifiers, environments, exceptions, and release decisions | Local artifacts can be stale, generated, bypassed, or inconsistent with deployed state | Reconcile declarations with executable observations and accountable approval |

The local source directly demonstrates these historical patterns:

- a requirement contract with a stable-looking identifier, trigger, primary outcome, secondary behavior, and edge or default behavior;
- an explicit rule favoring one behavior per obligation line, measurable units for quality claims, and independent testability;
- a many-row traceability matrix linking one sample requirement to unit, integration, and performance cases;
- a development sequence that creates test shape, observes failure, implements minimally, refactors, and verifies the broader suite;
- language-specific test skeletons for Rust, TypeScript, and Go around one filtering scenario;
- vague-to-executable rewrites for speed, reliability, and malformed input; and
- a pre-commit checklist linking requirement identity, tests, build, and measurable claims.

These observations establish source content, not current best practice or measured outcomes. In particular, the sample latency and success-rate values are not targets for this reference. The template's unresolved authoring tokens are not copied into the evolved output. Exact identifier syntax, quality thresholds, language naming, phase vocabulary, and gate commands remain project-owned decisions.

**Target-project evidence map**

| Evidence class | Questions it can answer | Required identity | Common overreach |
|---|---|---|---|
| Product need or risk record | Why a behavior matters, who is affected, and what consequence drives priority | Decision or issue identity, owner, accepted scope, date | Treating an unapproved request as a committed requirement |
| Requirement authority | Which claim text and lifecycle state the project accepts | Stable claim ID, revision or history, owner, status | Assuming an ID makes ambiguous prose testable |
| Architecture or interface decision | Which boundaries and tradeoffs constrain implementation and verification | Decision ID, affected interfaces, alternatives, supersession | Treating architecture rationale as observed runtime behavior |
| Verifier definition | What defect a test, analyzer, review, benchmark, migration, or drill can expose | Case ID, assertion location, fixture, requirement links | Counting a test name without reading its assertions |
| Implementation ownership | Which code, configuration, schema, migration, or document realizes the claim | Artifact version, path or symbol, module owner | Assuming file proximity proves complete implementation |
| Run evidence | What executed against which artifact and environment, with what outcome | Artifact hash or version, verifier version, command, environment, time, result | Reusing a stale green result after relevant change |
| Exception record | Which missing or failing evidence is temporarily accepted and why | Affected claim, consequence, compensating control, owner, expiry | Turning a temporary waiver into silent permanent status |
| Release decision | Which claim set is approved, blocked, rolled back, superseded, or retired | Release identity, evidence set, decision owner, unresolved risk | Equating test success with product or governance approval |
| Operational observation | Whether production behavior supports, contradicts, or narrows a claim | Deployment identity, window, workload, signal health, limitation | Using absence of incidents as proof of correctness |

**Source disposition record**

For every consequential extraction, retain:

```text
Source path or direct location and content identity
Exact bounded observation and source version
Evidence role and permitted claim scope
Target requirement, verifier, implementation, or decision affected
Adapted choice and rejected alternative
Gate executed and observed result
Conflict, residual uncertainty, owner, and invalidation trigger
```

A content hash answers whether bytes match; it does not answer who owns the guidance, whether a claim is current, whether an assertion is meaningful, or whether a run passed. A public page can be authoritative for instruction placement or CI syntax while remaining irrelevant to product behavior. A target test can pass locally while the public support boundary or release decision remains unresolved.

Good use extracts the atomic-behavior question, writes a real target requirement, creates positive and negative assertions, and records a current run. Bad use copies the historical sample latency into a product contract and cites the template as measurement evidence. Borderline use adopts its identifier style after confirming repository policy, generators, links, migration cost, and ownership; the style remains local policy rather than a universal rule.

No current public-page fact is established here. A future authorized refresh must record publisher, direct source, checked date, exact release or revision, bounded finding, applicability, conflict, changed action, and target retest. Traceability truth emerges from accepted claim, meaningful verifier, implementation ownership, current run evidence, and release decision together; no source row proves that chain alone.

## Pattern Scoreboard Ranking Table

The inherited values are editorial ordering from the seed. Their derivation, scale, sample, and predictive validity are unavailable. They are not probabilities, confidence, coverage, adoption, or effectiveness. Preserve them for provenance, but do not average them, compare their spacing, or use them as release thresholds.

| Pattern | Inherited score or priority | Apply when | Failure prevented | Direct falsifier |
|---|---|---|---|---|
| Source Map First (`executable_traceability_template_patterns`) | 95; historical default tier | Before reusing syntax, identifiers, thresholds, phases, or gates from the duplicated template source | Illustrative historical content becomes target policy without review | Every promoted source claim has a disposition, applicability boundary, and target result |
| Evidence Boundary Split (`executable_traceability_template_patterns`) | 91; historical default tier | When historical facts, public mappings, target observations, examples, and recommendations mix | A copied file or reputable link gains authority it has not earned | Claims distinguish frozen source, duplicate locator, unrefreshed mapping, local policy, observation, and judgment |
| Verification Gate Coupling (`executable_traceability_template_patterns`) | 88; historical default tier | Before a requirement, quality claim, exception, or release state is described as supported | Plausible prose or a test name substitutes for disconfirming evidence | The affected claim names a verifier, expected failure signal, current run evidence, and decision response |
| Decision Anchor First | First construction decision | A request, risk, issue, or policy is becoming an accepted obligation | Traceability optimizes a misunderstood or unapproved problem | Actor, desired outcome, consequence, scope owner, and acceptance state are explicit |
| Atomic Observable Claim | Hard requirement-authoring gate | One sentence combines several triggers, outcomes, defaults, or quality dimensions | A verifier can pass one part while the requirement appears fully covered | The claim can fail for one clear reason and split claims retain explicit interactions |
| Boundary and Negative Design | Leads before happy-path-only implementation | Invalid, denied, absent, duplicate, retry, compatibility, or edge behavior changes the promise | Green happy paths conceal noninterference and recovery defects | Representative negative and boundary cases produce explicit expected observations |
| Verifier Semantic Fit | Hard evidence-design gate | A test, analyzer, review, benchmark, migration, or drill is linked to a claim | Coverage counts a verifier that cannot reveal the relevant violation | Deliberate claim-breaking mutation causes the expected assertion or audit failure |
| Initial Failure Observation | Hard change-protection gate | New or changed behavior is being implemented | A pre-existing green test is credited with protecting behavior it never challenged | New evidence fails or is absent for the expected pre-implementation reason |
| Many-to-Many Link Integrity | Structural traceability gate | Claims need multiple evidence types or one scenario observes an interaction | Forced one-to-one rows duplicate tests or hide missing assertion relationships | Orphan, duplicate, contradictory, and unsupported edges are detected without flattening valid interaction |
| Implementation Ownership Link | Change-impact gate | Code, configuration, schema, migration, document, or service realizes the claim | Requirement changes do not reach the artifacts that must be reviewed | A requirement mutation identifies all accountable implementation boundaries and owners |
| Current Run Binding | Hard evidence-freshness gate | A test definition or review is used to support release status | Old, wrong-environment, skipped, or flaky evidence remains green | Run record binds artifact, verifier, environment, result, time, and limitation |
| Exception Expiry Contract | Hard deviation gate | Required evidence is missing, failing, or intentionally deferred | Temporary waiver becomes silent permanent support | Affected claim, consequence, compensating control, owner, expiry, and recovery evidence are visible |
| Change Invalidation Propagation | Hard maintenance gate | Need, claim, implementation, verifier, fixture, environment, or support range changes | Stale downstream evidence survives semantic change | The changed node produces the smallest complete review and rerun set |
| Release Reconciliation | Final decision gate | Claim evidence, failures, skips, exceptions, and ownership are ready for shipment review | Test success is mistaken for product approval automatically | Release status accounts for every in-scope claim and unresolved deviation |
| Template Promotion Review | Propagation gate | A convention, generator, dashboard, or agent will copy traceability structure | Illustrative shortcuts and arbitrary samples become organizational defaults | Independent use preserves semantics, graph integrity, current evidence, ownership, migration, and retirement |

**Default construction order:** establish decision and scope; author atomic claims; add negative and quality boundaries; select semantically matched verifiers; observe the expected initial failure; link many-to-many assertions and implementation ownership; capture current run identity; reconcile exceptions and release status; then define invalidation, promotion, and retirement.

**Repair override:** begin at the earliest observed broken relationship and rerun its dependents. An incident starts with reproducible failure and state preservation before requirement cleanup. A stale green release elevates run binding and invalidation. An ambiguous product request returns to decision ownership. A test that survives a deliberate defect elevates assertion semantics. An expired exception blocks the affected claim regardless of the inherited editorial rows.

Use three qualitative profiles:

- **Lightweight:** one bounded reversible change, a clear behavior assertion, implementation link, focused run result, and concise decision record.
- **Standard:** several claims or modules, explicit negative cases, many-to-many matrix, current evidence, owners, exceptions, and change-impact checks.
- **High assurance:** consequential security, safety, compliance, compatibility, migration, or operational claims with independent evidence types, stronger provenance, controlled fault cases, and accountable release review.

Good prioritization follows the missing edge that changes the next action. Bad prioritization completes every identifier and table row while a mapped assertion checks the wrong behavior. Borderline exploratory work can retain provisional links, but it must not become release evidence until claim, environment, verifier, and ownership stabilize.

Numeric rank cannot rescue invalid evidence. Keep override reasons and review repeated failures: recurring orphan links may justify better generation, repeated stale results may require stronger invalidation, and copied threshold mistakes may require template demotion. Change the order only when evidence shows which relationship repeatedly fails first or when one severe escape exposes an unacceptable consequence.

## Idiomatic Thesis Synthesis Statement

`historical_local_observation`: The three mapped local paths contain one byte-identical template. It demonstrates atomic obligation lines, explicit units for quality claims, a many-row requirement matrix, a failure-first development plan, language-specific test skeletons, vague-to-executable rewrites, and a final gate checklist. It does not establish a target project's accepted requirements, test semantics, run results, identifier policy, thresholds, CI, or release authority.

`external_mapping_unrefreshed_note`: The Codex instruction guide, GitHub Actions documentation root, and AGENTS.md format location were inherited and not opened. They provide no current instruction, automation, or traceability fact in this evolution.

`systems_synthesis_or_judgment`: Idiomatic executable traceability is a typed evidence graph and change protocol. It connects an accepted need to atomic claims, discriminating verification cases, implementation ownership, immutable run observations, explicit exceptions, and release status. Each edge has an owner and an invalidation rule, so a change can identify what must be reviewed, rerun, blocked, migrated, or retired.

Use this reversible loop:

1. **Frame the decision.** Name actor, need or risk, desired outcome, consequence, scope owner, and whether the item is exploratory, proposed, or accepted.
2. **Define claim identity.** Assign a stable local ID after acceptance. Keep title and revision history readable without recycling identity for a different behavior.
3. **Write observable semantics.** State trigger or precondition, primary outcome, relevant boundaries, failure behavior, and quality units only when a real method and target exist.
4. **Design disconfirming evidence.** Add positive, negative, boundary, interaction, denial, migration, performance, review, or operational cases according to consequence.
5. **Choose the evidence mechanism.** Bind each claim to a test, analyzer, benchmark, review, drill, or combination whose observation can reveal the violation.
6. **Observe the initial gap.** Confirm the new or changed evidence fails, is absent, or exposes the expected mismatch before implementation. Preserve the cause rather than treating any red output as sufficient.
7. **Implement and refactor.** Change the smallest accountable artifact set, make the expected evidence pass, and improve design while relevant checks remain green.
8. **Capture immutable observation.** Record artifact and verifier identity, environment, command or review method, result, skips, failures, time, retained evidence, and limitations.
9. **Reconcile decision state.** Approve, block, narrow, except, supersede, or retire each in-scope claim. A passing run informs but does not replace product or governance approval.
10. **Propagate change.** When intent, claim, implementation, verifier, fixture, environment, compatibility range, or policy changes, invalidate affected observations and rerun the smallest complete evidence set.

**Core principles**

- **Identity is stable; meaning has history.** Do not recycle a requirement ID for unrelated behavior. Record revisions or supersession while preserving links to released evidence.
- **Claims are atomic but systems interact.** Split independently failing outcomes, then preserve explicit interaction requirements where behavior emerges across them.
- **Traceability is many-to-many.** A quality claim can need several evidence types; one end-to-end scenario can exercise several claims. Record assertion-level links rather than manufacturing duplicate tests.
- **Definitions are not observations.** A test file proves that a verifier exists. A run record proves what happened against a named artifact and environment. Neither alone proves product acceptance.
- **Evidence has scope and freshness.** Environment, fixture, dependency, verifier, and artifact changes can invalidate a result even when the test name remains unchanged.
- **Missing evidence is a state.** Failed, skipped, unavailable, flaky, excepted, and out-of-scope outcomes remain visible. They are never silently folded into green.
- **Exceptions are bounded contracts.** Name affected claim, consequence, compensating evidence, owner, expiry, and the observation required to restore ordinary status.
- **Generated views are derived.** Keep authoritative requirement and assertion data close to their owners; generate matrices and dashboards when possible, then test generation for missing and contradictory edges.
- **Release is reconciliation.** Review the entire in-scope claim set, current evidence, skips, failures, exceptions, ownership, and compatibility boundary before deciding.
- **Traceability is proportional.** A reversible local fix can use a concise link and focused evidence. Shared, long-lived, privileged, compatibility-sensitive, or audited behavior needs stronger lineage and invalidation.

**Lifecycle states**

| Claim state | Meaning | Evidence consequence |
|---|---|---|
| Exploratory | A question or experiment informs scope but is not a release obligation | Preserve experiment conditions; do not count it as accepted coverage |
| Proposed | Claim awaits owner and acceptance | Verification may be designed, but release cannot depend on unaccepted meaning |
| Accepted | Owner commits to the behavior within a boundary | Required evidence and implementation ownership become active |
| Implementing | Work is underway and initial failure has been observed | Prior green evidence cannot satisfy the changed claim automatically |
| Verified | Current required evidence supports the accepted scope | Status remains bounded by artifact, environment, method, and freshness |
| Blocked | Required evidence fails or ownership is unresolved | Affected release scope cannot be called supported |
| Excepted | A bounded deviation is approved temporarily | Exception record and compensating evidence remain active until expiry |
| Superseded | A replacement claim governs new work | Consumers, implementations, and verifiers route through migration edges |
| Retired | Claim no longer applies to supported behavior | Active gates stop after dependents and retained evidence are reconciled |

Do not force every claim through every state; use the smallest lifecycle that preserves the project's decisions. State transitions must still be explicit when they alter required evidence or release status.

**Evidence fits the claim**

| Claim kind | Strong candidate evidence | Frequent mistake |
|---|---|---|
| Pure transformation | Unit and property cases with boundary inputs | Testing only one example and calling the function covered |
| Interface collaboration | Contract and integration cases | Mocking both sides so the real boundary never executes |
| User workflow | End-to-end or behavior scenario plus lower-level diagnostics | Asserting page or response presence without the promised outcome |
| Static policy | Analyzer, schema check, and focused review | Linking an unrelated runtime test to satisfy a row |
| Performance or capacity | Versioned workload, environment, method, distribution, and correctness guard | Copying a sample threshold or reporting a percentile from an unsuitable sample |
| Reliability or recovery | Fault case, state transition, resource inventory, and operational drill | Inferring recovery from happy-path success |
| Security or privacy | Threat-linked negative cases, permission denial, secret-safety checks, and review | Counting authentication success while denial and leakage remain untested |
| Migration or compatibility | Versioned fixture matrix, upgrade and rollback evidence, and supported-range decision | Testing a clean install and claiming upgrade safety |
| Human judgment | Named reviewer role, rubric, decision, disagreement, and expiry | Pretending a qualitative approval is an automated invariant |

**Complete and misleading examples**

Complete: an accepted session-revocation requirement links to unit, API integration, cache-interaction, and secret-redaction assertions. Current run evidence binds the service artifact and environment. A cache design change invalidates the interaction evidence and blocks the claim until rerun.

Misleading: the same requirement ID appears in a test name whose only assertion checks that a response object exists. A matrix row and green command are present, but the verifier cannot reveal continued protected access after revocation.

Conditional: an exploratory benchmark suggests a propagation objective. Preserve workload and observation as experiment evidence. Do not promote its number into an accepted claim until product need, architecture boundary, environment, variability, and measurement owner are agreed.

This thesis is not a universal identifier standard, testing framework, CI recipe, product specification, or approval policy. Target authority owns those mechanisms. It stops being sufficient when the team needs domain discovery, architecture selection, test implementation, statistical design, legal interpretation, or production operations without the relevant specialist. Bring back the accepted constraints and evidence links afterward.

The durable unit is an accepted claim plus evidence capable of disproving it, a current observation, and rules for invalidation and decision. A permanently green row is not the goal. A trustworthy system makes stale, missing, contradictory, skipped, and superseded evidence as visible as success.

## Local Corpus Source Map

Use the February archive as frozen provenance and the March archive plus unclassified path as byte-identical locators:

- `agents-used-monthly-archive/codex-skills-202602/executable-specs-01/references/executable-specs-templates.md`
- `agents-used-monthly-archive/codex-skills-202603/executable-specs-01/references/executable-specs-templates.md`
- `unclassified-yet/Executable Specifications Templates.md`

All three were read completely and have SHA-256 `c7e44220936452079080a46fb23725ec5b3332fb8b1a8a082eaeed76b2bd2812`. They are one 118-line historical source. Do not load each copy for confidence or count their rows as corroboration.

| Source region | Retrieve when | Durable candidate or question | Caveat | Target gate |
|---|---|---|---|---|
| Title and opening purpose | Deciding whether the source applies at all | Is the task converting a request into a testable contract? | The source assumes a specification task and does not perform product discovery or acceptance | Confirm an accountable decision and accepted scope before assigning requirement identity |
| Requirement contract shape | Authoring a behavior or quality claim | Does the claim state a trigger, primary outcome, secondary behavior, and edge or default behavior? | The shown domain, sequence, revision, and title tokens are unresolved teaching syntax, not a finished record | Use concrete target IDs and reject unresolved authoring tokens before publication |
| Requirement authoring rules | Reviewing atomicity and measurability | Does each obligation line own one behavior, and do quality claims use explicit units and independent verification? | One line can still hide preconditions, ambiguous terms, or interactions; units do not create a justified target | Perform semantic review and bind every quality value to product need and method |
| Traceability matrix | Designing links among requirement, test, assertion, target, and evidence type | Does each row explain what violation the verifier can reveal? | The sample suggests many-to-many evidence but does not define run identity, implementation links, exceptions, or release state | Validate orphan, duplicate, contradictory, superseded, and stale relationships in the target graph |
| Test-driven plan | Planning evidence before implementation | Are test shape, expected initial failure, minimal implementation, refactoring, and broader verification recorded distinctly? | Phase names alone do not prove the failure was relevant or the final evidence current | Capture expected and observed failure reason, then bind passing evidence to the current artifact |
| Rust test skeleton | Adapting a narrow Rust behavior case | Which input, call, and assertion express the requirement in Rust? | The sample filtering names and assertion are illustrative and may be too shallow for another domain | Use repository naming and assert the target requirement's observable outcome and boundaries |
| TypeScript test skeleton | Adapting a narrow TypeScript behavior case | Which fixture and assertion fit the project's runner and type boundary? | The shown API shape does not establish strictness, async behavior, integration, or failure semantics | Run under target configuration and add negative or async cases where the claim requires them |
| Go test skeleton | Adapting a narrow Go behavior case | How should failure output identify the violated behavior inside the project's test style? | The loop and fatal assertion are one example, not a universal table or subtest structure | Follow target package conventions and prove boundaries plus failure diagnostics |
| Vague-to-executable rewrites | Challenging speed, reliability, and bad-input language | What workload, window, unit, error type, or safety boundary is missing? | The concrete latency, entity count, success rate, and observation window are sample values without target evidence | Obtain product and architecture objectives, define method, establish baseline, then test the accepted value |
| Pre-commit quality gate | Building a local completion check | Are IDs, links, test results, build status, unresolved markers, and performance methods checked? | The historical marker vocabulary and universal test-link wording need adaptation; a green command does not prove semantics | Bind exact repository commands, include non-test evidence types, and inspect skipped or stale results |

**Progressive retrieval profiles**

- **Full traceability workflow:** read every region and reconcile claim shape, matrix semantics, development evidence, language adaptation, vague rewrites, and final gates before promoting a template.
- **Requirement authoring:** read the purpose, contract, rules, and rewrite regions, then confirm target identifier and acceptance policy.
- **Matrix or graph design:** read requirement rules, matrix, development plan, and quality gate, then add implementation, run, exception, release, and invalidation fields absent from the source.
- **Language test adaptation:** read requirement and development regions plus only the relevant language skeleton; use target framework and project conventions rather than translating every sample.
- **Quality objective:** read contract rules and vague rewrites, then route to product, architecture, and measurement owners before accepting a number.
- **Template promotion:** read the entire source and add current governance, generator behavior, graph validation, run evidence, exception lifecycle, migration, and retirement absent from the corpus.

**Region-specific traps**

- A single obligation line can still combine several independently failing outcomes through vague conjunctions.
- A matrix can show every requirement ID while assertions test incidental implementation details.
- One test per requirement can duplicate scenarios and hide many-to-many interaction evidence.
- An observed initial failure can be irrelevant if caused by malformed setup rather than missing behavior.
- Language skeletons can encourage copy-pasted names and fixtures that do not match target boundaries.
- An explicit unit can make an arbitrary threshold look measured.
- A pre-commit gate can pass while evidence comes from the wrong artifact, environment, or stale run.
- A checked box can hide a skip, unavailable dependency, expired exception, or unaccepted claim.

**Extraction record**

For consequential reuse, capture:

```text
Archive path, source region, and content hash
Exact historical observation and durable review question
Illustrative detail deliberately not copied
Target requirement or workflow decision
Adapted artifact and authoritative owner
Graph, behavior, run, and release evidence
Rejected alternative, residual uncertainty, and invalidation trigger
```

Good retrieval combines the requirement rules, matrix relationships, and development evidence before creating a shared template. Bad retrieval copies all three paths, unresolved authoring syntax, sample thresholds, and language names into a generator. Borderline reuse adopts the historical identifier family: it becomes acceptable after local ownership, uniqueness, migration, parsing, linking, and supersession behavior are verified.

The source bytes and content are known. Current requirement policy, test framework, CI, measurement targets, evidence retention, release governance, and workflow effectiveness remain unproved. When a reused region changes, invalidate dependents deliberately: claim-shape changes reopen parser and semantic review; matrix changes reopen graph generation; test-plan changes reopen evidence workflow; quality-gate changes reopen CI and release reconciliation.

## External Research Source Map

No browsing occurred in this evolution. These inherited locations are `external_mapping_unrefreshed_note` records, not current facts, recommendations, or proof that the selected target uses the associated mechanism.

| Inherited location | Historical mapped role | Permitted future use after inspection | Current disposition | Target applicability gate |
|---|---|---|---|---|
| `https://developers.openai.com/codex/guides/agents-md` | Codex repository-instruction context | Clarify current instruction scope, discovery, precedence, and project behavior only when traceability conventions must be exposed through that mechanism | Retain as a plausible product-owned retrieval target; content, version, and relevance are unverified | Select an instruction-placement decision, inspect current direct guidance, and test discovery, precedence, conflict, and refresh in the target repository |
| `https://docs.github.com/actions` | GitHub automation platform root | Resolve current workflow syntax, events, permissions, artifacts, cache, retention, status, and cancellation after GitHub Actions is selected for a traceability gate | Retain as a broad documentation root, not a direct claim about one workflow or evidence policy | Identify exact feature and repository context, inspect its current page, then run known-pass, known-fail, skip, cancellation, fork, and permission cases |
| `https://agents.md/` | General instruction-file format location | Clarify file scope and cross-tool format expectations when that instruction mechanism is deliberately adopted | Retain as a possible format authority; no current content or target compatibility is established | Confirm applicable tools, precedence, nested scope, conflict behavior, and repository observation before reuse |

These sources cannot decide the project's accepted need, requirement identity, atomicity, test assertion, measurement target, implementation owner, evidence freshness, exception approval, or release status. A CI system can execute a weak test reliably. An instruction file can propagate an ambiguous convention perfectly. Current external mechanics and local semantic correctness are distinct evidence.

**Missing authority categories**

A future authorized refresh should select only the categories activated by the target decision:

| Decision | Preferred authority | Local reproduction required |
|---|---|---|
| Requirement or issue schema | Product or requirements-tool documentation plus repository policy | Create, revise, supersede, query, and reject invalid records |
| Test annotations and discovery | Current test-framework and build-tool documentation | Discover linked cases and prove missing or malformed links fail visibly |
| Static-analysis or schema gate | Analyzer, compiler, or schema owner documentation | Exercise accepted, rejected, warning, suppression, and version cases |
| CI workflow and status | Exact provider feature documentation and repository workflow | Run success, assertion failure, setup failure, skip, cancellation, permission denial, artifact absence, and branch-policy cases |
| Coverage semantics | Coverage-tool documentation and local policy | Show what counts, what is excluded, and why percentage cannot establish requirement meaning alone |
| Performance method | Benchmark framework and domain measurement authority | Reproduce workload, environment, correctness guard, baseline, variability, and result |
| Security or privacy evidence | Current product, platform, and organizational security authority | Exercise threat-linked denial, secret safety, permission, audit, and recovery |
| Release and exception workflow | Current repository and organizational governance | Reconcile missing evidence, expiry, approval, rollback, and supersession |
| Evidence storage and retention | Artifact store and audit policy | Bind immutable identity, access, retention, deletion, and retrieval behavior |

Do not invent direct URLs when the target technology is unknown. Record the authority class and frozen question first. Add a location only after an authorized retrieval establishes publisher, version, and applicability.

**Refresh triggers**

Refresh a public contract when a current fact can alter a material decision: instruction discovery changes; CI runner or event behavior changes; permission or token scope changes; artifact retention changes; test framework upgrades; requirement-tool schema migrates; benchmark tooling changes; a security advisory affects evidence; release policy changes; or a previously working target gate disagrees with recorded guidance.

Local success can depend on deprecated or undocumented behavior. Conversely, current public guidance can be irrelevant to a pinned supported environment. Record both and reconcile rather than selecting whichever is convenient.

**Future refresh record**

```text
Frozen traceability question and implementation decision
Target repository, tool, feature, and exact version
Direct source, publisher, release or commit, and checked date
Relevant section and bounded paraphrased finding
Evidence role: format, product behavior, automation, security, or governance
Applicability, conflict, changed action, and migration consequence
Target configuration, focused run, and observed result
Disposition, residual uncertainty, owner, and next refresh trigger
```

Classify a result as `inspected`, `applicable`, `reproduced`, `reconciled`, `rejected`, `superseded`, or `no_material_impact`. Reading a page does not reproduce a workflow. Running a workflow does not make its assertion semantically sufficient. A product-owned source can define support while a target run still exposes an implementation defect.

**Examples**

Good future use selects GitHub Actions artifact retention as the evidence mechanism, finds the exact current product page, configures a disposable repository fixture, and tests artifact creation, absence on failure, permissions, expiry, and retrieval before relying on it for audit evidence.

Bad use cites the AGENTS.md format location to claim that every product requirement must use one identifier syntax. File-format authority cannot create product acceptance or release governance.

Borderline use consults the Codex instruction guide to propagate traceability guidance. It becomes applicable only after target instruction discovery, nested precedence, conflict, update behavior, and actual agent adherence are observed. The underlying requirement and verifier semantics remain owned elsewhere.

Prefer event-driven refresh over bibliography growth. Retire a repeatedly irrelevant mapping while preserving why it was rejected and which selected mechanism would reopen it. External evidence is complete only after the affected local edge is retested; publisher prestige and link presence never establish traceability quality by themselves.

## Anti Pattern Registry Table

Classify an anti-pattern only after naming the violated intent, claim, verifier, evidence, exception, release, or lifecycle relationship. Similar structure is not enough. Contain false support, unsafe behavior, secret exposure, and expired deviations before repairing graph shape or presentation.

| Anti-pattern | Cause and consequence | Detection signal | Safer response | Valid boundary or exception |
|---|---|---|---|---|
| `context_free_summary_output` | Generic specification advice replaces the completely read template source and target repository evidence | No source disposition or local artifact changes the recommendation | Trace each adopted responsibility through historical content, target policy, and one disconfirming gate | Skip an irrelevant source region when its inability to change the decision is recorded |
| `unsourced_authority_language` | Identifier, metric, CI, security, or release language sounds mandatory without an owner or evidence role | Claim has no authority, applicability result, or uncertainty | Separate frozen observation, unrefreshed mapping, local policy, target run, and judgment | A preference is valid when clearly scoped and owned |
| `duplicate_source_confidence` | Three byte-identical paths are counted as independent agreement | Different locations share the same hash and technical claims | Preserve lineage while counting content once | Independently observed target outcomes can corroborate a copied proposal |
| `unaccepted_request_as_requirement` | An idea or issue becomes release scope before product or risk ownership accepts it | Requirement state and decision owner are absent | Keep it exploratory or proposed until acceptance and scope are recorded | A time-boxed experiment can proceed without release commitment when labeled |
| `identifier_theater` | Stable-looking IDs are added without atomic meaning, ownership, or evidence | Search finds IDs but reviewers cannot state the behavior each controls | Define observable semantics and lifecycle before counting identifiers | A temporary local label can aid discussion if it is not treated as accepted coverage |
| `recycled_requirement_identity` | An old ID is reused for materially different behavior | Historical evidence appears linked to a new claim | Create a new identity and use supersession or migration edges | Editorial clarification can retain identity when accepted behavior does not change |
| `bundled_obligation_contract` | One requirement combines independently failing triggers, outcomes, defaults, and qualities | Different assertions cover different fragments while the row appears fully green | Split atomic claims and add explicit interaction requirements | Keep inseparable transactional behavior together when one observation truly defines success |
| `vague_or_unbounded_outcome` | Words such as fast, reliable, secure, graceful, or supported lack workload, units, boundaries, or failure semantics | Reviewers cannot construct a discriminating case | Name observable outcome, environment, method, and accepted scope | Exploratory goals may remain qualitative until a commitment is proposed |
| `hidden_precondition_or_nongoal` | Fixtures or implementation assume state not present in the requirement | Tests pass only under author knowledge and unrelated behavior is captured | State preconditions, defaults, exclusions, and route-away behavior | Internal setup detail may remain in the fixture when it cannot change user-observable meaning |
| `implementation_locked_requirement` | Claim prescribes a current class, function, storage engine, or algorithm without a mandated reason | Refactoring breaks the requirement despite unchanged behavior | State outcome and constraints; move design choice to architecture evidence | Legal, interoperability, or platform mandates can require an implementation constraint with authority |
| `forced_one_to_one_mapping` | Every requirement is forced into one test and every test into one requirement | Duplicate scenarios appear while interactions and quality evidence disappear | Preserve many-to-many case and assertion links | A genuinely atomic local behavior can have one primary focused verifier |
| `test_name_only_trace` | Requirement ID appears in a test name or comment but assertions check another behavior | Removing the meaningful assertion leaves the trace link intact | Link assertion intent and mutation sensitivity, not only names | Name links remain useful navigation after semantic evidence exists |
| `shallow_assertion_coverage` | Test checks existence, status, or call count rather than promised outcome | Deliberate requirement violation still passes | Assert observable result, forbidden effect, and relevant boundary | A smoke test can intentionally prove only availability when scoped as such |
| `test_definition_equals_evidence` | Presence of test code is reported as a successful observation | No artifact, environment, command, time, or result accompanies the claim | Store immutable run evidence separately from verifier definition | Static inspection may establish only that a verifier exists |
| `green_without_initial_gap` | Pre-existing passing evidence is credited with protecting changed behavior without demonstrating sensitivity | New requirement never produced the expected failure or absence | Add or alter the verifier and observe the relevant initial gap | Pure refactoring can rely on characterization evidence when behavior is explicitly unchanged |
| `coverage_percentage_equals_traceability` | Aggregate line or branch coverage is treated as requirement completeness | High coverage coexists with orphan claims or weak assertions | Use coverage as diagnostic context and audit claim-to-assertion semantics | Coverage can be a local quality signal when its limitation is explicit |
| `wrong_artifact_run` | Evidence comes from another binary, package, branch, configuration, or generated output | Run record lacks immutable artifact identity | Bind result to exact artifact and verifier versions | A reproducible source revision may be sufficient when build determinism is established |
| `wrong_environment_generalization` | One local environment is used to claim broad platform, dependency, or compatibility support | Environment matrix and exclusions are absent | Narrow claim or run representative supported combinations | Platform-neutral static claims may need no runtime matrix |
| `stale_green_result` | Requirement, code, verifier, fixture, dependency, or policy changes without invalidating old evidence | Result predates a change on its dependency path | Compute affected reruns and mark status unknown until current evidence exists | Unaffected evidence can remain current when dependency analysis is trustworthy |
| `hidden_skip_or_unavailable_case` | Skipped, filtered, quarantined, unavailable, or cancelled verification disappears from the release summary | Expected case count differs or skip cause has no owner | Record missing-evidence state, consequence, owner, and recovery | An explicitly out-of-scope case can be excluded with rationale and support boundary |
| `flaky_pass_as_support` | A passing retry or selected run hides unstable behavior | Repeated controlled runs disagree and failure is not classified | Block or narrow claim, diagnose variance, and preserve all outcomes | Measured probabilistic behavior can be valid with an accepted distribution and method |
| `metric_without_method` | Numeric quality language lacks workload, environment, baseline, sample, correctness guard, or owner | Number cannot be reproduced or linked to product consequence | Replace with a bounded measurement contract or remove the number | A regulatory or interface limit may be externally mandated but still needs verification |
| `manual_matrix_drift` | Hand-maintained rows diverge from requirement, code, tests, or run evidence | Orphans and mismatched revisions appear after changes | Generate stable mechanical edges and review semantic edges | A small short-lived matrix can remain manual with focused validation |
| `generated_graph_as_truth` | Automation creates links from names or annotations and is assumed semantically complete | Generator passes despite a deliberately wrong assertion or missing claim | Test generator mutations and require semantic review at consequential edges | Mechanical graph integrity can be fully automated within its declared scope |
| `exception_without_expiry` | Missing or failing evidence is waived without consequence, owner, compensating control, or end condition | Deviation remains open across releases silently | Bound exception, surface it in release reconciliation, and verify recovery | A permanent product limitation should become explicit supported scope rather than a recurring waiver |
| `supersession_without_migration` | A new claim replaces an old one while consumers, tests, and evidence still point to both ambiguously | Contradictory requirements remain active | Mark replacement, migrate dependents, preserve historical release evidence, then retire old gates | Parallel versioned behavior can coexist with explicit compatibility scope |
| `green_ci_equals_release_approval` | Workflow success is treated as product, security, or governance acceptance | No claim-set reconciliation or decision owner exists | Review in-scope claims, current evidence, missing cases, exceptions, and ownership | CI can be one delegated approval signal when policy defines its exact authority |
| `secret_or_private_evidence` | Fixtures, logs, artifacts, or matrix links retain credentials or private user content | Evidence store exposes reusable secrets or unnecessary data | Use synthetic fixtures, redaction, least access, bounded retention, and incident response | Approved nonsecret identifiers can remain when needed for correlation |
| `ownerless_traceability_template` | A copied convention, generator, or dashboard has no maintainer or migration path | Repositories diverge and no one can decide which form is current | Assign ownership, version support, feedback, demotion, and retirement | A disposable personal note can remain unsupported when propagation is prevented |

**Repair order**

1. Stop shipment or propagation of a claim falsely presented as supported.
2. Contain unsafe effects, sensitive evidence, and expired or ownerless deviations.
3. Preserve failing artifact, environment, result, and decision state.
4. Repair accepted claim meaning and boundaries before editing matrix presentation.
5. Strengthen the verifier so a deliberate violation produces the expected failure.
6. Correct graph links, implementation ownership, and current run identity.
7. Reconcile release status, supersession, exceptions, and affected consumers.
8. Add regression and mutation cases, then restore status deliberately.

**Controlled probes**

- Remove a requirement link and confirm orphan detection.
- Duplicate an ID with different meaning and confirm identity validation fails.
- Combine two independently failing outcomes and confirm semantic review requests a split.
- Leave an ID in a test name while weakening its assertion and confirm mutation review catches it.
- Run against a different artifact or environment and confirm evidence identity prevents reuse.
- Disable, skip, or quarantine a required case and confirm release status becomes missing or blocked.
- Expire an exception and confirm the affected claim cannot remain silently supported.
- Supersede a claim and confirm dependent tests, implementations, and consumers receive migration actions.
- Break the evidence collector and confirm absence is reported as unknown, never green.

Good traceability fails visibly when the promised behavior is mutated and identifies the affected release claim. Bad traceability has complete IDs, high coverage, and green CI while assertions cannot reveal the violation. Borderline traceability uses one scenario for several requirements: it is acceptable when each assertion and interaction edge is explicit and removing a link would let a real defect escape.

Cascades matter. An ambiguous product request can produce a bundled claim, shallow tests, complete-looking generated coverage, stale evidence, and confident release approval across every repository that copied the template. Repair the earliest supported cause and invalidate downstream artifacts. Repeated matrix repairs usually indicate a granularity, authority, or evidence-lifecycle problem upstream.

## Verification Gate Command Set

Run the focused assignment verifier from the repository root after changing this reference and packet:

```bash
python3 tests/verify_idiomatic_reference_file.py --path idiomatic-ref-202607/executable_traceability_template_patterns-20260710.md
```

Then run the shared generation contract:

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

These commands verify reference-evolution structure. They do not parse a target requirement system, inspect assertions, execute target tests, validate CI evidence, expire exceptions, or approve a release.

Discover actual target artifacts and commands before binding traceability gates:

```bash
rg --files | rg '(^|/)(requirements?|specs?|tests?|features?|contracts?|benchmarks?|migrations?|workflows?|decisions?|releases?|evidence)(/|\.|$)'
```

Inspect project instructions, package or build scripts, test discovery, CI workflows, requirement generators, coverage configuration, benchmark harnesses, artifact storage, release policy, and existing evidence records. A filename match is discovery only.

| Claim | Required gate | Passing observation | Limit |
|---|---|---|---|
| Frozen source was interpreted accurately | Reopen the mapped region, compare content hash, exact observation, and caveat | One-source/three-location identity and bounded extraction agree | Historical accuracy does not establish target policy |
| Requirement record is structurally valid | Run the target parser or schema against accepted and malformed records | Valid concrete claims pass and unresolved or invalid records fail clearly | Parsing does not prove atomicity, acceptance, or product value |
| IDs are unique and lifecycle-safe | Query active, superseded, retired, and historical identities, including attempted reuse | Duplicate or recycled identities fail; valid supersession preserves history | Unique IDs can still name ambiguous behavior |
| Claims are semantically testable | Review trigger, outcome, boundaries, units, non-goals, and owner | Reviewer can construct a discriminating observation and identify one failure reason | Human intent confirmation remains judgment |
| Traceability graph is coherent | Validate required node types and edges, many-to-many links, orphans, duplicates, contradictions, and dangling replacements | Every in-scope claim has permitted evidence and ownership paths without flattening valid interactions | Graph completeness cannot prove assertion strength |
| Verifier protects the intended behavior | Introduce a safe deliberate requirement violation or use mutation tooling | Expected assertion or review gate fails for the relevant reason | Mutation selection and equivalence require judgment |
| Initial evidence gap is real | Run new or changed verifier before implementation or preserve characterization mismatch | Evidence fails or is absent because promised behavior is missing, not because setup is broken | Pure behavior-preserving refactoring can use existing characterization evidence |
| Target cases are actually selected | Run discovery or list mode under the same configuration used for evidence | Required cases appear; filters, tags, quarantine, and exclusions are visible | Discovery does not establish pass or semantic value |
| Current artifact satisfies the claim | Execute the selected verifier against an immutable artifact and declared environment | Result, assertion outcomes, artifact identity, verifier version, environment, and time are retained | One environment cannot establish untested compatibility |
| Missing evidence is visible | Exercise failure, skip, unavailable dependency, cancellation, and collector-loss paths | Each becomes an explicit state with cause, consequence, and owner, never silent green | Policy determines whether a particular missing state blocks release |
| Quality claim has a method | Run a versioned workload or review protocol with correctness guard, baseline, environment, and uncertainty | Observation can be reproduced and supports only the accepted scope | A measured result does not create the product target that it evaluates |
| Exception is bounded | Advance time or release state through the exception's expiry and recovery conditions | Expired exception blocks or narrows the claim until required evidence returns | Governance owner decides whether the original exception was acceptable |
| Supersession migrates dependents | Replace one claim in an isolated graph and inspect implementation, verifier, consumer, and release links | New work routes to the replacement; historical evidence stays attributable; old active gates retire deliberately | Parallel supported versions require explicit compatibility scope |
| Release reconciliation is complete | Evaluate in-scope claims, current evidence, failures, skips, exceptions, ownership, and compatibility | Decision record states approved, blocked, narrowed, rolled back, or retired scope with rationale | Automated checks cannot substitute for every product or governance owner |
| Copied template remains honest | Apply the template in a clean fixture without author state | Concrete records contain no unresolved authoring syntax, arbitrary inherited targets, or hidden adapters | One fixture cannot prove all repository cultures or tools |

**Gate profiles**

- **Lightweight change:** semantic behavior review, focused verifier, implementation link, current run identity, and concise decision note.
- **Standard feature:** requirement schema, graph integrity, positive and negative assertions, initial gap, focused and broader suites, missing-evidence visibility, owner, and release reconciliation.
- **High assurance:** standard gates plus independent evidence types, fault or mutation cases, quality method, permission and privacy review, immutable artifact evidence, exception expiry, compatibility, rollback, and accountable approval.

Use fast source, parser, and graph checks during authoring. At candidate state, run assertion mutations, selected target cases, current artifact evidence, missing-signal controls, and relevant quality methods. Before release, reconcile exceptions, skips, supersession, compatibility, ownership, and rollback. Stop downstream dashboard or release work on ambiguous claim meaning, a verifier that survives the relevant mutation, or evidence bound to the wrong artifact.

**Evidence packet**

A useful record includes working context, claim and verifier identities, artifact hash or immutable version, target environment, exact command or review method, discovery and filter state, fixture version, expected observation, actual result, skipped and unavailable cases, retained output, decision supported, limitation, owner, and invalidation trigger. "Tests passed" without this identity cannot support a durable release claim.

Keep representative negative, boundary, stale-result, missing-case, expired-exception, and supersession fixtures when those risks apply. Rerun only affected evidence when the dependency graph is trustworthy, but always retain structural invariants and validate the impact algorithm with deliberate changed edges.

## Agent Usage Decision Guide

Use the decision and missing evidence edge rather than keywords to route the task.

| Usage profile | Choose when | Minimum action | Boundary and handoff |
|---|---|---|---|
| Requirement authoring | An accepted need or risk must become atomic observable claims | Confirm authority, state trigger, outcome, boundaries, quality method, owner, and lifecycle state | Product or domain owner supplies accepted meaning; return concrete claims and unresolved questions |
| Implementation change | Existing or new claims must drive code, configuration, schema, migration, or documentation changes | Map affected artifacts, design discriminating cases, observe initial gap, implement, capture current evidence | Architecture and code owners choose design; return implementation links and results |
| Incident regression | A failure needs reproduction, requirement reconstruction, repair, and prevention | Preserve failing artifact and environment, classify violated claim, add regression evidence, invalidate dependents | Incident and operations owners govern containment; return causal claim and protected repair |
| Quality objective | Performance, reliability, security, privacy, capacity, or usability language needs a method | Establish product consequence, workload or rubric, baseline, environment, correctness guard, owner, and decision threshold | Product, architecture, security, or measurement specialist owns the target and method |
| Migration or compatibility | Supported versions or stored states must transition safely | Define source and target states, compatibility range, migration, rollback, retained evidence, and supersession | Release and data owners govern rollout; return versioned fixtures and support decision |
| Release reconciliation | Shipment depends on current claim set, evidence, skips, failures, exceptions, and ownership | Verify artifact identity, evidence freshness, missing states, exception expiry, compatibility, and rollback | Accountable release roles approve or block; return immutable decision record |
| Audit or assurance | A reviewer must reconstruct why a consequential claim was accepted | Preserve authority, requirement history, verifier semantics, run identity, deviations, and release lineage | Security, legal, compliance, or assurance owner defines required evidence and retention |
| Template or generator promotion | A convention will be copied across repositories or agents | Validate clean application, semantic graph, current adapters, migration, feedback, ownership, and retirement | Maintainer owns compatibility; return versioned template and deprecation route |
| Orientation only | User is comparing traceability mechanisms or reading the historical source | Produce decision options and unknowns without claiming target execution | Implementation, evidence, and release status remain unrun |
| Avoid as primary | The unresolved work is product strategy, architecture selection, legal interpretation, statistical design, test-framework coding, CI incident repair, or governance approval | Open the specialist workflow and attach only relevant claim and evidence edges | Do not let a historical template substitute for domain or tool authority |

**Preflight before assigning IDs or editing tests**

Record:

- actor, accepted need or risk, desired outcome, consequence, non-goals, and decision owner;
- whether the item is exploratory, proposed, accepted, implementing, verified, blocked, excepted, superseded, or retired;
- existing requirement identity, history, duplicate and supersession policy, and affected consumers;
- target modules, interfaces, configurations, migrations, documents, environments, and owners;
- candidate verifier types, actual assertion locations, expected failure signal, negative cases, and discovery or filter state;
- artifact and verifier identity, evidence store, run environment, skip or unavailable behavior, and retention;
- product, architecture, security, privacy, measurement, legal, compliance, and release authorities that must contribute;
- exception, compatibility, migration, rollback, release, and retirement boundaries activated by the change.

A reduced preflight is appropriate for a small behavior-preserving test correction: confirm existing claim meaning, assertion intent, affected artifact, focused runner, current result, and changed-edge invalidation. Do not omit authority or evidence identity merely because the diff is small.

**Start blockers**

Keep the work exploratory or route it when:

- no one can accept or reject the user outcome;
- a requirement ID is being assigned to ambiguous or bundled behavior;
- the target repository's identity and supersession rules are unknown for a shared convention;
- a quality number has no product consequence, workload, method, or owner;
- proposed verifier cannot reveal the named violation;
- the current test selection, artifact identity, or environment cannot be established;
- missing, skipped, flaky, or unavailable evidence would be hidden from the release decision;
- an exception has no consequence, owner, expiry, or recovery gate; or
- release approval is being inferred solely from a command's color.

An exploratory experiment may proceed with a distinct identity and explicit non-release status. Preserve its environment and result, then define what must converge before it becomes an accepted requirement or evidence source.

**Route transitions**

Re-run routing when an exploratory question gains an owner; a behavioral claim becomes a quality objective; a unit change crosses an interface; a mock becomes live; a migration or compatibility promise appears; evidence becomes privileged or regulated; an exception crosses a release; a template gains another consumer; or support ownership changes.

Good routing uses the implementation profile for a cross-module session-revocation claim, then asks security and architecture owners to define consistency and secret-safety boundaries. Bad routing uses this reference to decide whether users value session revocation at all. A proposed latency target is borderline: it enters traceability only after product need, architecture, workload, measurement, and decision ownership make the value an accepted claim.

**Routing evidence record**

Retain decision, claim state, consequence, target artifacts, chosen profile, authoritative companions, rejected profiles, initial probe, verifier type, expected failure, current evidence gap, release implication, return artifact, owner, and reversal condition. The route remains provisional until authority and first disconfirming observation confirm it.

Correct routing minimizes duplicated specifications. Domain specialists return accepted meaning or constraints; test and platform specialists return executable verifiers; CI and evidence owners return trustworthy observations; release owners return decisions. This reference keeps those outputs connected without pretending one artifact owns them all.

## User Journey Scenario

Use this hypothetical journey to hold one outcome constant: a product owner says, "When a session is revoked, it must stop granting protected access." The team must turn that request into accepted claims, evidence that can reveal continued access or secret leakage, and a release decision. The example does not select an authentication architecture, consistency model, identity provider, universal response type, or propagation duration.

**Starting state**

- A protected API and session revocation operation already exist, but current semantics and test sensitivity are uncertain.
- Product ownership can accept the user outcome; security ownership can define credential and audit boundaries; architecture ownership can define the consistency model.
- Target requirement policy, test framework, build commands, CI, artifact identity, and release workflow must be discovered in the actual repository.
- A disposable session fixture can create, use, revoke, and retry access without touching real credentials.

| Phase | Action | Evidence to retain | Rework, block, or route condition |
|---|---|---|---|
| Discover | Inspect current product decision, authentication boundaries, existing requirement IDs, code ownership, tests, runner filters, CI, artifacts, exceptions, and release policy | Direct target artifacts, owners, and observed current behavior | Keep the journey conceptual when authority, protected boundary, or runner cannot be identified |
| Accept the need | Product owner accepts loss of protected access after successful revocation within the architecture's declared visibility model | Decision identity, actor, consequence, scope, non-goals, owner, and state | Do not assign release status to an exploratory preference |
| Separate concerns | Split access denial, typed failure behavior, audit redaction, and any measurable propagation objective when they can fail independently | Atomic claims and explicit interaction or dependency edges | Split bundled prose; route timing to architecture and measurement ownership |
| Assign identity | Use available repository policy to create stable nonrecycled IDs and history | Identity validation and duplicate or supersession check | Stop shared convention work when ID lifecycle is unknown |
| Design cases | Define active access, successful revocation, protected denial, repeated denial, stale cache, malformed session, audit redaction, and excluded provider scenarios | Case IDs, fixtures, expected observations, limitations, and claim links | Route unsupported threats or provider behavior to specialist evidence |
| Map implementation | Identify revocation service, session store, cache or authorization layer, protected handler, error mapping, and audit sink | Artifact and owner links plus architecture boundary | Reopen architecture when no component can observe the accepted consistency contract |
| Observe the gap | Run or inspect proposed cases before behavior change and preserve the relevant failure or missing evidence | Artifact, environment, command, discovery state, result, and cause | Repair setup when failure does not represent continued access or missing redaction |
| Implement | Change the smallest accountable artifacts, make focused evidence pass, and refactor while affected checks remain green | Code and configuration changes, review, focused results, and broader regression selection | Narrow or split when implementation broadens the accepted outcome |
| Challenge evidence | Mutate or disable cache invalidation and secret redaction in an isolated fixture | Expected integration and secret-safety failures | Strengthen assertions when the deliberate violation survives |
| Capture current run | Execute selected evidence against an immutable candidate and declared environment | Verifier and artifact versions, filters, results, skips, failures, time, retained output, and limitations | Mark unknown or blocked when required cases are missing, flaky, stale, or bound to another artifact |
| Reconcile release | Review accepted claims, current evidence, architecture limits, missing scenarios, exceptions, compatibility, rollback, and owners | Approved, blocked, narrowed, or excepted decision with rationale | Passing tests cannot bypass unaccepted timing, threat, or governance scope |
| Propagate change | On cache redesign, provider upgrade, handler change, error mapping change, or support-range change, invalidate affected evidence | Impact set, required reruns, migration or supersession, and restored decision | Stop relying on prior runs when dependency edges are uncertain |

**Accepted conceptual claims**

These records are semantic examples; adapt exact types and identity format to the target repository.

| Requirement ID | Accepted behavior | Boundary and non-goal |
|---|---|---|
| `REQ-AUTH-014` | After successful revocation is visible under the accepted consistency model, the next protected request using that session is denied with the service's typed unauthenticated outcome | Does not define a universal propagation duration or identity-provider behavior |
| `REQ-AUTH-015` | Audit evidence for the denied request identifies correlation and denial class without retaining the session secret | Does not mandate one logging product or unrestricted evidence retention |
| `REQ-AUTH-016` | Repeated protected requests with the revoked session remain denied and create no new authenticated state | Does not define unrelated malformed-token or account-lock policy |

An architecture decision must define what "visible" means for local store, distributed cache, or provider-backed revocation. If product needs a duration, create a separate quality claim only after target workload, environment, measurement method, baseline, consequence, and owner exist.

**Traceability slice**

| Verification case | Requirement links | Assertion capable of revealing defect | Evidence limitation |
|---|---|---|---|
| `CASE-AUTH-031` | `REQ-AUTH-014` | A session accepted before revocation receives the typed denial on a protected request after revocation becomes visible | Local service fixture does not prove external provider propagation |
| `CASE-AUTH-032` | `REQ-AUTH-014`, `REQ-AUTH-016` | Repeated protected requests never regain authenticated access or create replacement state | Does not cover every concurrency interleaving |
| `CASE-AUTH-033` | `REQ-AUTH-015` | Captured audit fields contain correlation and denial class while secret-shaped session material is absent | Redaction fixture must represent target encoding and sinks |
| `CASE-AUTH-034` | `REQ-AUTH-014` | Disabling cache invalidation in an isolated mutation causes the protected-access assertion to fail | Mutation equivalence and architecture applicability require review |
| `CASE-AUTH-035` | `REQ-AUTH-014`, `REQ-AUTH-015` | Revocation failure leaves prior state explicit and does not produce a false successful-revocation audit event | Exact failure contract depends on target transaction semantics |

A revocation-service unit case that checks a successful return can remain useful, but it does not replace `CASE-AUTH-031`; the user requirement concerns subsequent protected access. Likewise, an HTTP status check alone may be shallow if the service contract requires a typed body, no protected side effect, or audit evidence.

**Evidence state example**

Before implementation, record that `CASE-AUTH-031` fails because cached authorization remains usable, while `CASE-AUTH-033` is absent. After repair, record the exact candidate artifact and target runner observations. Do not write fictional commands into this generic reference. In a real project, the evidence packet includes discovered command, working directory, filters, fixture identity, environment, artifact hash, assertion results, skipped cases, retained output, and limitation.

**Change-impact example**

Months later, the authorization cache is replaced. The implementation edge from `REQ-AUTH-014` to cache visibility changes. That event invalidates `CASE-AUTH-031`, `CASE-AUTH-032`, and the mutation assumption in `CASE-AUTH-034`; it may not invalidate an unrelated audit-format unit case. The release claim returns to unknown until the affected set passes against the new artifact. This is executable traceability: the graph changes work and status.

Good outcome: accepted claims are split by independent failure, assertions detect continued access and secret leakage, run evidence binds the candidate, and the cache replacement triggers focused reruns.

Bad outcome: one broad "revocation works" requirement maps to a test that checks the revoke call returned success. The matrix is green while protected access remains possible.

Borderline outcome: a live provider experiment measures propagation in one environment. Preserve it as scoped experiment evidence; do not promote its observation into supported timing until product, architecture, workload, variability, compatibility, and measurement ownership are accepted.

The durable handoff contains accepted claim records, rejected timing proposal, architecture visibility decision, implementation ownership, case and assertion links, initial-gap evidence, current candidate run, missing scenarios, release decision, invalidation rules, and next refresh triggers. Its product is a retestable decision chain, not a completed matrix alone.

## Decision Tradeoff Guide

Make each choice against a fixed accepted decision and current repository workflow. Add identity, metadata, central infrastructure, or durable storage only when it protects an observed relationship or required handoff that a simpler candidate cannot.

| Decision boundary | Lightweight default | Choose the stronger alternative when | Cost if misapplied | Verification and reversal signal |
|---|---|---|---|---|
| Stable ID or prose-only behavior | Keep a clear behavior assertion close to a tiny reversible change | Add a stable requirement ID when several artifacts, owners, releases, or consumers must refer to the same accepted claim | No ID impairs impact and history; premature ID makes exploration look committed | Search dependents and simulate a semantic change; add identity when prose reference becomes ambiguous |
| Revision encoded in ID or separate history | Keep identity stable and store revision or change history separately | Encode revision when an external contract or established local policy requires version-qualified references | Encoded revisions cause link churn; hidden history obscures released meaning | Change wording and behavior independently, then verify links and historical evidence resolve correctly |
| Structured trigger-outcome syntax or ordinary declarative prose | Use the clearest atomic local form | Use a structured form when repeated ambiguity, generation, or review benefits from explicit trigger and outcome fields | Rigid syntax creates awkward claims; loose prose hides preconditions and boundaries | Ask independent reviewers to derive the same discriminating cases; simplify if structure adds no agreement |
| Split atomic claims or retain interaction contract | Split outcomes that can fail and change independently | Keep an interaction claim when the transaction or cross-component outcome is itself indivisible | Over-splitting loses system meaning; bundling creates partial green coverage | Remove or fail one assertion and verify requirement status changes accurately |
| Colocated requirements or central specification | Keep authoritative behavior near code, interface, schema, or tests when ownership is local | Centralize when cross-system review, audit, product ownership, or shared release needs one reconciled authority | Colocation fragments shared contracts; central documents drift from implementation | Trace a real change across owners and measure where duplicate edits or missed reviews occur |
| Manual matrix or generated graph | Use a small validated manual view for short-lived local work | Generate stable edges when identifiers, annotations, and consumers are numerous or frequently changing | Manual rows drift; generators can automate incorrect semantics | Inject missing, duplicate, wrong, superseded, and stale links; retain the simpler method if generation catches no additional defect |
| Test annotation or separate traceability row | Keep claim identity next to a meaningful assertion | Add a separate row when one scenario covers several claims, non-test evidence exists, or run and release metadata must be joined | Annotations become name-only theater; separate rows duplicate truth | Read the assertion and remove either link; every retained representation must change navigation or decision |
| One verifier or multiple evidence types | Use one focused verifier for a truly local deterministic behavior | Add integration, quality, security, migration, review, or operational evidence when distinct failures matter | Excess evidence slows change; one test hides cross-boundary defects | Mutate each relevant boundary and keep only evidence that detects a distinct accepted violation |
| Automated check or human review | Automate deterministic syntax, graph, behavior, and measurement assertions | Use accountable review for product meaning, usability, threat judgment, legal interpretation, or exception approval | Automation gives false objectivity; review can be inconsistent and stale | Define rubric, reviewer role, disagreement, evidence, expiry, and a repeatable sample |
| New failure-first test or characterization evidence | Observe a relevant initial failure for changed behavior | Use existing characterization when refactoring explicitly preserves behavior or when an incident already supplies the failing observation | Artificial failure adds noise; skipping sensitivity lets unrelated green tests claim coverage | Show how evidence distinguishes changed behavior from setup or unrelated failures |
| Ephemeral CI result or durable evidence store | Keep local result details sufficient for a reversible unshipped change | Persist immutable evidence when releases, audits, compatibility, or later reconstruction depend on it | Durable storage adds access and retention cost; ephemeral logs expire before review | Reconstruct a prior decision after ordinary log expiry and assess whether artifact, run, and result remain provable |
| Strict required gate or bounded exception | Fail closed when required evidence is absent or contradictory | Permit a temporary exception only when consequence, compensating control, owner, expiry, and recovery are acceptable | Absolute gates can halt harmless work; loose waivers become permanent unsupported scope | Advance through expiry and verify claim status blocks or recovers predictably |
| One universal template or risk-based profiles | Start with one minimal semantic core | Add profiles when lightweight, standard, and high-assurance work have materially different evidence obligations | One template overburdens small work or underspecifies severe risk | Apply profiles to representative changes and inspect missing controls plus unused fields |
| Inline run metadata or linked immutable record | Keep concise current result beside a local short-lived claim | Link a durable record when output is large, access-controlled, retained, or shared across releases | Inline data becomes noisy and stale; links can rot or lose access | Resolve evidence from a clean reviewer context and verify identity, permissions, retention, and fallback summary |
| Shared threshold template or locally accepted objective | Provide measurement fields without a default number | Add a concrete target only after product consequence, workload, environment, method, baseline, and owner are established | Sample values become arbitrary commitments or gaming targets | Reproduce the measurement and show which release action follows breach |

**Adopt, adapt, avoid, or escalate**

- **Adopt** a mechanism when an observed target relationship needs it, local policy accepts it, and a focused gate demonstrates value.
- **Adapt** historical claim, matrix, development, or gate shapes when their responsibility fits but syntax, tooling, authority, evidence storage, or lifecycle differs.
- **Avoid** fields, links, IDs, dashboards, or evidence that have no consumer, owner, invalidation rule, or decision effect.
- **Escalate** when the choice defines product scope, architecture, statistical method, security or privacy policy, legal meaning, regulated retention, production operations, or release authority.

**Worked choices**

Good lightweight choice: a local parser fix cites the existing accepted requirement in a meaningful test assertion, runs the focused suite against the candidate artifact, and retains a concise current result. A central graph adds no useful edge.

Bad heavyweight choice: the same fix creates a new requirement ID, central row, generated dashboard, durable artifact, and approval step while none changes review or release. Maintenance grows without detection power.

Borderline generated graph: annotations already have stable semantics and many consumers. Generation becomes worthwhile after mutation tests prove missing, wrong, duplicate, skipped, and superseded edges are exposed and a human still reviews claim meaning.

**Decision ledger**

For consequential choices, retain:

```text
Accepted claim and decision held constant
Target policy and mandatory control
Selected option and relationship protected
Simpler candidate rejected because
Focused gate and observed result
Authority, evidence, exception, and migration impact
Known uncertainty or untested environment
Owner and reopen condition
```

This guide does not establish current repository APIs, requirement schemas, test commands, evidence stores, or approval roles. Uncertainty should keep choices reversible and claims narrow. A heavier mechanism earns its place only when it detects, communicates, or governs a relationship the lighter option cannot preserve safely.

## Local Corpus Hierarchy

The February archive is **primary historical provenance**. The March archive and unclassified copies are **byte-identical duplicate locators**, not independent supporting sources. None becomes current project policy merely because it appears in several corpus locations.

| Hierarchy role | Assignment test | Permitted use | Promotion, demotion, or retirement trigger |
|---|---|---|---|
| Historical observation | Exact content can be located in the frozen archive | Describe what the template taught and illustrated at capture time | Never promote from archive presence alone; attach target authority and evidence |
| Duplicate locator | Another path contains identical bytes or repeats a claim without independent observation | Find consumers, lineage, and migration exposure | Reclassify only after material divergence, ownership, and independent evidence |
| Candidate traceability responsibility | The source asks a still-relevant question without contradicting the bounded target claim | Seed requirement, matrix, evidence, or quality review | Promote after local semantic and workflow gates; demote after counterexample |
| Illustrative syntax or value | Concrete text teaches shape but has no target acceptance | Inspire a sanitized concrete target record | Never use as policy or objective without independent owner and evidence |
| Target project policy | Current schema, instructions, governance, code, or tooling explicitly owns the rule | Treat as local default inside its repository and version boundary | Reopen after owner, tool, schema, workflow, or support change |
| Legacy mechanism | Identity, syntax, annotation, runner, or gate belongs to an older supported environment | Explain existing artifacts and migration constraints | Retire for new work after dependent releases and consumers migrate |
| Conflicting evidence | Historical guidance disagrees with target policy, observed behavior, or another authority | Drive comparison and preserve disagreement | Resolve only with accountable decision and reproducible observation |
| Negative evidence | Omission or sample-copying risk demonstrates a failure worth preventing | Populate anti-patterns, mutations, and promotion review | Retain while the inference remains plausible; revise when boundary changes |
| Promoted template rule | Repeated current use, ownership, migration, and evidence justify propagation | Generate or scaffold the bounded convention with limits | Demote after tool breakage, stale evidence, copied failure, or owner loss |

Apply roles by source region:

| Source theme | Role here | Useful contribution | Limitation and required gate |
|---|---|---|---|
| Purpose statement | Historical observation plus candidate | Frames the job as converting requests into testable contracts | Product acceptance and release authority remain absent; confirm the real decision owner |
| Requirement shape | Candidate with sanitized syntax | Encourages trigger, outcome, additional behavior, and edge or default semantics | Historical authoring tokens are unresolved; use concrete target IDs and parser checks |
| Atomicity and units rules | Strong candidate questions | Challenges bundled obligations and qualitative claims without units | Atomic lines can still hide preconditions and arbitrary values; run semantic and measurement review |
| Matrix columns and rows | Candidate relationship shape | Shows one sample claim linked to several evidence levels and assertions | Omits implementation, run, exception, release, and invalidation nodes; validate a richer target graph |
| Development-plan sequence | Candidate workflow | Separates test design, expected failure, minimal implementation, refactoring, and broader verification | Phase labels do not prove relevant failure or current evidence; capture observations explicitly |
| Rust test skeleton | Conditional illustration | Shows input, invocation, and assertion arrangement in Rust | Names and assertion depth belong to one example; follow target crate and requirement semantics |
| TypeScript test skeleton | Conditional illustration | Shows a concise behavior assertion in TypeScript | Does not establish async, strictness, integration, or error handling; use target runner and boundaries |
| Go test skeleton | Conditional illustration | Shows loop-based assertion and diagnostic in Go | Does not establish target package style or interaction coverage; adapt and exercise target behavior |
| Vague rewrite table | Candidate question plus illustrative values | Makes workload, unit, window, and typed failure visible | Every concrete number is unaccepted sample data; obtain product objective and measurement evidence |
| Pre-commit gate | Candidate plus negative evidence | Connects IDs, evidence, build, hygiene, and measurable claims | Historical link wording excludes non-test evidence and lacks run identity, skips, exceptions, and release reconciliation |
| Missing evidence lifecycle | Negative evidence | Shows why the source is not a complete modern release contract | Add artifact identity, current run, missing states, exception expiry, supersession, and decision ownership |

**Claim promotion tests**

- Does the source region directly support the paraphrased responsibility?
- Is the detail durable, or is it a sample identifier, value, API, or workflow term?
- Which target owner can accept or reject the adapted rule?
- What parser, graph, mutation, run, exception, or release gate can disprove it?
- Which generated artifacts and consumers will depend on the promoted claim?
- What event demotes, supersedes, or retires it?

**Extraction record**

```text
Archive path, source heading, and content hash
Exact historical observation
Role: candidate, illustration, legacy, conflict, negative, or duplicate
Target decision and accountable owner
Current repository evidence inspected
Gate executed and observed result
Rejected sample or alternative
Residual risk, disposition, and refresh trigger
```

Good reuse extracts the one-behavior question, adapts it to a real accepted claim, and proves assertion sensitivity plus current evidence. Bad reuse turns the source's sample latency into an organizational service objective. Borderline reuse adopts its identifier family: promote only after uniqueness, parser, linking, revision, supersession, migration, and ownership behavior pass in the target repository.

Promotion is reversible. Target evidence can demote a historically useful mechanism without altering the archive, and legacy syntax can remain available for migration after it stops guiding new work. Rules affecting generated templates, shared IDs, quality targets, evidence retention, exceptions, or release status need an owner and invalidation trigger; disposable orientation notes can use a lighter record.

## Theme Specific Artifact

Theme specific artifact: worked executable traceability template patterns example with user goal, decision point, failure mode, and verification gate.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Executable Traceability Template Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

Good example: Use Executable Traceability Template Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Executable Traceability Template Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Executable Traceability Template Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

Leading indicator: every shipped claim has a requirement ID and fresh verification evidence.
Failure signal: the reference describes TDD or specs without showing failing and passing evidence.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

- The role scenario names the user, starting state, decision, and trigger for Executable Traceability Template Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

Adjacent reference guidance: Use TDD, traceability, or completion verification references when the work is already scoped.
Adjacent reference 1: consider the executable adjacent reference when the current task pivots away from executable traceability template patterns.
Adjacent reference 2: consider the traceability adjacent reference when the current task pivots away from executable traceability template patterns.
Adjacent reference 3: consider the template adjacent reference when the current task pivots away from executable traceability template patterns.

## Workload Model

`combined_evidence_inference_note`: Treat Executable Traceability Template Patterns as a quality gate operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | specification, test, review, and verification work where the artifact must turn ambiguous intent into executable evidence | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one requirement packet, 20 requirement IDs or fewer, one traceability matrix, and one final gate command set | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Executable Specs Templates; 1) Requirement Contract Template; REQ-<DOMAIN>-<NNN>.<REV>: <Short title>; 2) Traceability Matrix Template; 3) TDD Plan Te | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is worked executable traceability template patterns example with user goal, decision point, failure mode, and verification gate | require the artifact before claiming the reference is operationally usable |

## Reliability Target

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| green check misses requirement | test command passes while a requirement lacks traceability | audit every REQ ID against at least one test or review assertion |
| metric claim has no method | performance or reliability language appears without measurement | replace claim with threshold, fixture, command, and owner |

## Retry Backpressure Guidance

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture reviewer decision, unresolved uncertainty, and next refresh trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

Performance method: require 100 percent REQ-to-test mapping and fail closed when any claim lacks a verification command or review assertion.
Leading indicator to measure: every shipped claim has a requirement ID and fresh verification evidence.
Failure signal to watch: the reference describes TDD or specs without showing failing and passing evidence.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

Executable Traceability Template Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | executable traceability template patterns official documentation best practices |
| `github_repository_query_phrase` | executable traceability template patterns GitHub repository examples |
| `release_notes_query_phrase` | executable traceability template patterns changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
