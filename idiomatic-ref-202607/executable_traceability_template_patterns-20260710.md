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

Use a **Traceability Change Record** when a behavior change must remain explainable across owners, tools, release stages, or delayed handoffs. The record is not a second specification. It is a revision-scoped decision object that identifies the authoritative claim, the evidence relevant to that claim revision, and the release disposition reached from that evidence.

The full record is justified for cross-team APIs, generated contracts, data migrations, security controls, operational limits, regulated approvals, and behavior whose failure is costly to reverse. For a local low-risk change, a compact record containing claim identity, authoritative location, evidence identity, disposition, and retrieval result is enough. Exploratory code that cannot ship need not acquire release governance prematurely.

**Minimum record contract**

| Record field | Completion rule | Failure the field prevents |
|---|---|---|
| `change_id` | Use one immutable identity for the proposed behavior change | Evidence from unrelated work being attached by proximity |
| `claim_revisions` | List each atomic claim identity and exact revision or content digest | An older passing result silently approving changed semantics |
| `decision_owner` | Name the accountable role and the authority under which it acts | A reviewer comment being mistaken for product or release acceptance |
| `behavior_cases` | Link positive, negative, boundary, and interaction cases required by the claims | Happy-path coverage standing in for the whole contract |
| `implementation_links` | Identify the code, configuration, schema, or operational mechanism that realizes each claim | Requirements and tests agreeing while production behavior is elsewhere |
| `evidence_requirements` | State the evidence type and why it fits each claim | A unit test being used to prove deployment, policy, or human-review behavior |
| `evidence_runs` | Bind artifact digest, environment, command or review question, result, and observed time | A green label with no reproducible artifact or execution boundary |
| `negative_probe` | Record a mutation, controlled fault, or counterexample that relevant evidence detects | An assertion that passes regardless of prohibited behavior |
| `exceptions` | Record scope, rationale, owner, compensating control, expiry, and review trigger | A temporary waiver becoming an invisible permanent policy |
| `decision` | Record accepted, rejected, conditional, or superseded state with rationale | Complete-looking data without an accountable conclusion |
| `release_links` | Identify the build, package, deployment, or approval to which the decision applies | Evidence for one artifact authorizing a different release candidate |
| `invalidation_triggers` | Name changes that make the decision or evidence stale | A once-correct record surviving claim, tool, dependency, or environment drift |

Validate lifecycle state as well as field presence:

| State | Required observation | Transition that must be rejected |
|---|---|---|
| `proposed` | Atomic claims and accountable owner exist | Direct transition to accepted with no evidence requirements |
| `evidence_pending` | Cases, links, and expected evidence are defined | Treating missing or inaccessible evidence as a pass |
| `reviewable` | Required current evidence is retrievable and exceptions are explicit | Review with a run bound to another claim revision |
| `accepted` | Authorized decision and matching release boundary are recorded | Acceptance by a role lacking the stated authority |
| `conditional` | Limitation, compensating control, owner, and expiry are present | Open-ended conditional state without a review trigger |
| `rejected` | Reason and observed counterevidence are retained | Deleting rejection history and later repeating the same proposal |
| `superseded` | Replacement revision and migration disposition are linked | Reusing superseded evidence as current approval |

**Worked record**

The following values are illustrative, not target policy. The example concerns a change that revokes all active sessions after a user resets a password.

```yaml
traceability_change_record:
  change_id: AUTH-CHANGE-042
  claim_revisions:
    - id: AUTH-SESSION-017
      revision: 3
      statement: A successful password reset invalidates every active session for that account.
  decision_owner:
    role: identity-service-owner
    authority: authentication-behavior-acceptance
  behavior_cases:
    - password-reset-invalidates-two-active-sessions
    - failed-reset-preserves-existing-sessions
    - concurrent-refresh-cannot-revive-revoked-session
    - unrelated-account-session-remains-valid
  implementation_links:
    - identity-service/reset-password-handler
    - session-store/account-revocation-generation
  evidence_requirements:
    - type: integration-behavior
      reason: The claim crosses credential and session-store boundaries.
    - type: controlled-concurrency-probe
      reason: A refresh racing with revocation is an interaction risk.
  evidence_runs:
    - artifact_digest: build-auth-20260711-042
      environment: isolated-integration
      result: passed
      evidence_key: run-auth-session-042
  negative_probe:
    mutation: Disable the account revocation-generation update.
    expected_observation: The two-session integration case fails.
    observed_result: detected
  exceptions: []
  decision:
    state: accepted
    rationale: Required cases pass, the negative probe is detected, and evidence matches revision 3.
  release_links:
    - identity-service-candidate-20260711-042
  invalidation_triggers:
    - claim revision changes
    - session-store protocol changes
    - evidence artifact becomes unavailable
    - release candidate digest changes
```

This record does not prove that password-reset revocation is the right product policy. That policy must already be accepted by the proper owner. It proves which accepted claim revision was evaluated, why integration and concurrency evidence fit, which implementation was exercised, and which release candidate may rely on the decision.

**Representation choices**

| Representation | Best fit | Main benefit | Main risk |
|---|---|---|---|
| Markdown matrix | Small, review-centered repositories | Easy human scanning and diff review | Weak state transitions and accidental manual drift |
| Code annotations | Stable claims close to implementation | High code proximity and searchable identity | Poor cross-repository and release visibility |
| Issue workflow | Approval-heavy organizational change | Ownership, discussion, and access controls | Evidence can become detached or links can decay |
| Append-only event ledger | Audited state transitions and long retention | Preserves rejected and superseded decisions | Higher query and migration complexity |
| Generated projection | Several audiences need different views | One write model can serve review, CI, and audit | Generator correctness and schema compatibility become dependencies |

Choose one authoritative write model. Generate secondary matrices, dashboards, release summaries, and audit views when possible. Two manually maintained authoritative copies create a reconciliation problem that the artifact was meant to prevent.

**Artifact verification ladder**

1. Parse the record and reject missing identities, unknown states, duplicate claim revisions, or invalid links.
2. Build the typed graph and reject required claims without cases, implementation, evidence requirements, or a decision path.
3. Review semantic fit: confirm that each case addresses the claim and each evidence type can observe the stated failure.
4. Run a negative probe and show that relevant evidence changes from passing to failing for the expected reason.
5. Verify that every cited run matches the claim revision, implementation artifact, environment, and release candidate under review.
6. Retrieve stored evidence from its durable identity after the authoring workspace is unavailable.
7. Reject expired exceptions, missing compensating controls, inaccessible evidence, unauthorized decisions, and stale invalidation conditions.
8. Reconcile the final release so accepted claims are current, rejected claims are not shipped, and superseded evidence grants no authority.

**Good:** the worked record binds revision 3 to a specific build, exercises cross-boundary and concurrency behavior, detects a disabling mutation, and records an authorized release decision. **Bad:** a row says only `AUTH-SESSION-017 -> test passed` and gives no revision, artifact, assertion sensitivity, owner, or release identity. **Borderline:** a current test run exists, but its artifact was produced before revision 3; preserve the run as historical evidence and execute the required evidence against the new candidate before acceptance.

The record is deliberately small at its write boundary and rich in reproducible projections. Downstream impact analysis, release automation, audit review, evidence retention, migration planning, and incident reconstruction can consume stable identities without turning the record into the owner of domain execution. When a claim, implementation, schema, runner, authority, dependency, or environment changes, invalidate affected projections and reopen only the decisions whose causal support has changed.

## Worked Example Set

Use this sequence for worked transformations:

1. State the accepted need and its authority.
2. Separate atomic claims while preserving interaction claims.
3. Derive positive, negative, boundary, and interaction cases.
4. Select evidence that can observe each claim's failure mechanism.
5. Demonstrate an expected failing probe before relying on a passing result.
6. Bind current evidence to a revision, artifact, owner, and disposition.

The examples below teach that sequence. Their identifiers, values, technologies, and organizational roles are illustrative; they do not establish policy for an unseen target repository.

**Example A: split a bundled cancellation request without losing the transaction**

**Raw request:** "When a customer cancels a paid order, cancel fulfillment and issue a refund."

A weak rewrite creates one broad claim, one test called `cancellation_works`, and one link from that test to the requirement. It cannot say which obligation failed, and it can pass while fulfillment is cancelled but no refund is recorded.

A stronger decomposition is:

| Claim | Atomic behavior | Required case | Evidence fit |
|---|---|---|---|
| `ORDER-CANCEL-001` revision 1 | An eligible paid order enters cancelled state | Eligible paid order is cancelled | Domain behavior test |
| `ORDER-CANCEL-002` revision 1 | Cancellation prevents a new fulfillment handoff | Handoff attempted after cancellation is rejected | Integration test at fulfillment boundary |
| `ORDER-CANCEL-003` revision 1 | Cancellation records one refund instruction for captured payment | Captured payment produces one instruction | Persistence and payment-adapter integration test |
| `ORDER-CANCEL-004` revision 1 | Cancellation is all-or-recoverable across state, handoff, and refund effects | Refund adapter fails after cancellation starts | Controlled fault plus recovery-state assertion |

The fourth claim matters. Splitting the request into three atomic outcomes without an interaction claim could approve a partially applied cancellation. The exact transaction or compensation policy still requires product and architecture authority; the example only makes that decision visible.

**Expected negative probe:** disable refund-instruction persistence. Evidence for `ORDER-CANCEL-003` and the interaction claim must fail, while the isolated cancellation-state case may still pass. If every case stays green, the evidence graph is structurally linked but semantically insensitive.

**Good:** each claim has a separate result, and the fault probe exposes partial application. **Bad:** one passing end-state assertion checks only `order.status`. **Borderline:** all four cases pass, but the run belongs to a build produced before revision 1; retain it as history and rerun against the candidate.

**Example B: turn "make search fast" into an accepted quality contract**

Do not begin by copying a latency number from a template. First capture the workload and decision authority:

| Contract dimension | Concrete question | Required evidence |
|---|---|---|
| Population | How many indexed records and tenants represent the supported boundary? | Reproducible dataset manifest and distribution summary |
| Request mix | Which query forms, cache states, and result sizes matter? | Versioned workload profile |
| Metric | Which latency statistic and error handling define success? | Measurement method and aggregation rule |
| Environment | Which hardware, concurrency, dependency, and warm-up state apply? | Environment manifest and calibration record |
| Objective | Which value has the product or service owner accepted? | Decision record with owner and revision |
| Regression policy | What comparison, tolerance, and repeated-run rule blocks release? | Statistical gate with raw result retention |

Suppose a target owner accepts a hypothetical objective for a named workload. The resulting traceability record must link that accepted value to a benchmark that actually generates the workload, retains raw samples, reports the chosen statistic, and identifies the tested artifact. A unit test that sleeps for a fixed duration is not evidence of search latency, and a single local run does not establish a stable service objective.

**Expected negative probe:** add a controlled delay to the measured search path, not to unrelated setup. The quality gate should cross its accepted boundary while correctness cases remain interpretable. **Borderline:** the benchmark detects the delay but uses a dataset smaller than the supported population; record the run as partial evidence rather than changing the workload claim after seeing the result.

**Example C: match evidence to a cross-boundary security behavior**

**Accepted claim:** a successful password reset invalidates all active sessions for the affected account and does not invalidate another account's sessions.

| Candidate evidence | What it can show | What it cannot establish alone | Disposition |
|---|---|---|---|
| Handler unit test with mocked session store | The reset handler requests revocation | Stored sessions and refresh races actually obey it | Useful but insufficient |
| Session-store component test | Revocation generation blocks older tokens | Password-reset workflow invokes the mechanism | Useful but insufficient |
| Integration test across reset and session boundaries | End-to-end account-scoped behavior | Production deployment and telemetry state | Required behavior evidence |
| Controlled concurrency probe | Refresh racing with reset cannot revive an old session | All operational environments behave identically | Required interaction evidence where race is in scope |
| Deployment verification | Candidate configuration enables the expected protocol | Assertion sensitivity in source tests | Separate release evidence |

**Bad:** link the claim only to the mocked unit test because it is fast. **Good:** retain fast unit evidence for handler intent and add the integration and concurrency observations required by the claim. **Borderline:** integration evidence passes but another account is never exercised; the account-isolation clause remains missing rather than implicitly accepted.

**Example D: reconcile a temporary evidence exception with release**

A migration changes a data format, but one platform-specific compatibility suite is unavailable. "Known issue" is not an executable exception. A reviewable exception records:

```yaml
exception_id: MIGRATION-EXCEPTION-006
affected_claim: DATA-COMPAT-009 revision 2
missing_evidence: platform-z-compatibility-suite
reason: isolated runner is unavailable
compensating_control: block platform-z rollout and verify read-only export against retained fixtures
owner: migration-release-owner
expiry: release-candidate-3
review_trigger: runner restored or candidate digest changes
release_scope: platforms-a-and-b-only
```

At release reconciliation, platforms A and B may proceed only if their required current evidence passes and the release mechanism enforces the stated scope. Platform Z remains blocked. The exception expires at the named boundary; copying it into the next candidate without a new decision is a failure.

**Good:** missing evidence is explicit, the rollout cannot exceed the compensating scope, and expiry is enforced. **Bad:** mark the missing suite as skipped and count the job green. **Borderline:** the exception is approved and scoped, but the deployment configuration has not been checked; the governance record is complete while release enforcement remains unproved.

**Verification and reuse rules**

For each worked example, a target adaptation should answer:

- Which facts came from an accepted target need rather than this illustration?
- Which first draft was rejected, and what ambiguity or failure did it hide?
- Which traceability edges are required, optional, missing, stale, or superseded?
- Which probe makes relevant evidence fail for the expected reason?
- Which artifact, environment, run, reviewer role, and release boundary produced the observation?
- Which values, APIs, identities, and authority roles must be replaced locally?
- What change invalidates the result or reopens the decision?

Promote stable adaptations into conformance fixtures for parsers, graph validators, generators, review checks, and release reconciliation. Include bad and borderline fixtures as well as valid ones. Then add novel incident-derived mutations over time: a fixture suite that recognizes only its teaching examples can pass while production invents a failure it was never asked to detect.

## Outcome Metrics and Feedback Loops

Measure whether traceability improves decisions, not how many identifiers were created. Structural links are prerequisites; semantic fit, assertion sensitivity, current evidence, authorized disposition, and recoverability determine whether those links deserve trust.

Every metric needs a contract:

```text
Metric name and decision it informs
Population and observation boundary
Numerator, denominator, and missing-state rule
Event-time or version-time definition
Raw sources and join identities
Deduplication and exclusion rules
Accountable owner and permitted response
Countermetric and known blind spot
Target objective, if locally accepted
Definition version and refresh trigger
```

Do not assign a target merely because a metric can be calculated. Establish a baseline, inspect failures, estimate collection and response cost, then let the accountable target owner choose an objective. Sparse repositories should review counts and cases; percentages over a tiny denominator look precise without being stable.

**Balanced metric portfolio**

| Measure | Reproducible definition | Decision use | Blind spot or countermetric |
|---|---|---|---|
| Claim population closure | Shippable claim revisions with an explicit accepted, rejected, conditional, or superseded disposition divided by all claim revisions in the candidate boundary | Detect unreviewed behavior before release | A disposition can be wrong; pair with semantic audit findings |
| Required-edge completeness | Claim revisions whose required typed links exist divided by claims for which those link types are required | Detect missing cases, implementation, evidence, or release paths | Presence says nothing about fit; sample link meaning |
| Semantic audit yield | Sampled links judged incorrect, irrelevant, bundled, or misleading divided by sampled links reviewed | Estimate structural false confidence and target review | Reviewer variation; calibrate questions and retain rationales |
| Negative-probe sensitivity | Required sampled probes that make the intended evidence fail for the expected reason divided by probes executed | Detect assertions that cannot observe prohibited behavior | Samples may miss other weak assertions; rotate mutations and use incidents |
| Current-evidence coverage | Claim revisions with all required evidence valid for the exact candidate and current invalidation state divided by claim revisions requiring executable or review evidence | Decide which claims can enter release reconciliation | Freshness policy can be wrong; inspect invalidation rules and artifact joins |
| Evidence retrieval success | Referenced evidence artifacts retrievable with identity and integrity intact divided by retrieval attempts in the sample | Detect links that work only in the author's workspace | Retrieval does not prove semantics; pair with evidence-fit audit |
| Exception health | Active exceptions with owner, scope, compensating control, enforced boundary, expiry, and current review divided by all active exceptions | Find invisible or permanent waivers | Complete metadata may hide weak compensation; review consequence and enforcement |
| Release reconciliation closure | Candidate releases for which every in-scope claim, evidence set, exception, and decision matches the released artifact divided by releases inspected | Detect approval of the wrong build or revision | Release correctness beyond traced claims needs its own controls |
| Decision reconstruction success | Sampled historical release decisions that an independent reviewer can reconstruct from retained identities and evidence divided by attempts | Test whether the record survives handoff and time | Reviewer familiarity and retention policy affect results |
| Traceability-caused rework | Changes requiring claim, link, evidence, or disposition repair after review, classified by root cause | Find authoring ambiguity and workflow friction | Classification is judgment; do not infer total engineering quality |
| Escaped traceability defect | Incidents where a missing, wrong, stale, or ignored traceability relationship materially contributed to release or recovery failure | Prioritize schema, gate, fixture, and ownership improvements | Rare events and multiple causes prevent simple rate attribution |
| False-block burden | Release blocks or review escalations caused by incorrect traceability data or a faulty gate | Balance strictness against delivery reliability | A reversed block is not always waste; inspect avoided risk and repair cause |

Count `unknown`, `missing`, `inaccessible`, `not-applicable`, `excepted`, `stale`, and `superseded` separately. Never remove unjoinable records from a denominator silently. Deduplicate retries by the decision unit being measured: ten reruns of one claim revision do not create ten independently evidenced claims.

Evidence freshness is primarily event-bound:

- A claim revision invalidates evidence for an older semantic revision unless compatibility is proved.
- A rebuilt or reconfigured candidate invalidates run binding when the relevant artifact identity changes.
- A runner, dependency, environment, schema, or protocol change may invalidate only affected evidence classes.
- An expired exception invalidates conditional acceptance even if tests remain green.
- Evidence loss changes a retrievable result to inaccessible; a remembered pass is not a retained observation.
- Calendar age matters only when target policy or the failure mechanism makes time itself relevant.

A one-minute-old run against the wrong build is stale. An older immutable proof may remain current when its claim, artifact, environment assumptions, and retention integrity are unchanged.

**Interpretation examples**

**Good metric card:** current-evidence coverage names the release candidate population, counts stale and inaccessible evidence as non-current, identifies the graph and run store as sources, and routes failures to rerun, repair, exception, or release-block actions. Its countermetric samples evidence fit so authors cannot improve the rate with irrelevant passing jobs.

**Bad metric card:** "traceability is complete because every test name contains an ID." It has no claim denominator, permits duplicate and stale IDs, excludes non-test evidence, and cannot show whether any assertion notices prohibited behavior.

**Borderline metric card:** median review time decreases after a generator rollout. This may indicate lower friction, but it could also reflect smaller changes, skipped review, or reviewer adaptation. Segment by consequence and change size, then inspect rework, semantic audit yield, and escaped defects before attributing improvement to the generator.

No portfolio score should average these measures into release authority. A high structural rate must not cancel an expired security exception or a failed behavior probe. Inspect disagreements directly: high edge completeness with poor negative-probe sensitivity suggests decorative links; high evidence coverage with low retrieval success suggests transient storage; low review time with increased rework suggests rushed decisions.

**Verification of the measurement system**

1. Unit-test each numerator, denominator, state classification, deduplication rule, and definition version.
2. Feed synthetic records containing missing links, duplicate runs, stale revisions, inaccessible evidence, skipped checks, expired exceptions, and mismatched release digests.
3. Recompute sampled metrics independently from raw graph, run, exception, and release records.
4. Audit a stratified sample of links and decisions for semantic fit rather than checking presence alone.
5. Trace an unfavorable metric to the action taken, owner, result, and follow-up observation.
6. Compare dashboard totals with release candidates and incident records to detect silently absent populations.
7. Preserve the old definition when a metric changes so trend breaks are explicit rather than rewritten.

These checks verify computation and workflow response. They do not prove that traceability alone caused a change in defect rate, lead time, or incident severity. Report observed association, plausible mechanism, confounders, and remaining uncertainty.

**Feedback loops and cadence**

| Trigger | Review action | Durable output |
|---|---|---|
| Claim or implementation revision | Recompute affected links and invalidate dependent evidence | Updated impact set and evidence state |
| New release candidate | Reconcile claims, artifacts, runs, exceptions, authority, and release scope | Candidate decision record |
| Every generated-reference edit | Run the focused verifier and inspect changed guidance semantically | Verifier evidence plus review note |
| Exception creation or approaching expiry | Confirm necessity, compensation, enforcement, owner, and next decision | Renewed, narrowed, resolved, or blocked disposition |
| Tool, schema, runner, or storage migration | Run compatibility fixtures and evidence retrieval checks | Migration result and affected-version boundary |
| Public source or API refresh | Compare current source, applicability, and local adaptation without overwriting local evidence | Source-delta record and accepted or rejected changes |
| Incident or escaped misunderstanding | Reconstruct the decision chain and identify the weakest causal edge | Root-cause class, new fixture, and bounded process change |
| Periodic sampled review | Inspect semantics, evidence sensitivity, retrieval, and reviewer comprehension | Calibrated findings and prioritized repair |

Close the loop as: observe, diagnose, choose the smallest causal intervention, update a schema, gate, example, owner, or workflow, add a regression fixture, roll out by version, and measure again. Removal is a valid intervention. A field or gate that costs authors time but never changes a decision, catches a failure, supports recovery, or satisfies accepted governance should be simplified or retired rather than preserved as ceremony.

## Completeness Checklist

Completeness is relative to lifecycle state. A proposed claim needs authority, atomic semantics, and planned evidence; a release candidate additionally needs current observed evidence, an accountable disposition, enforced exceptions, and artifact reconciliation. Do not mark an item complete merely because text exists.

Use these states:

| State | Meaning | Permitted effect |
|---|---|---|
| `passed` | Required observation exists and satisfies the gate for the evaluated revision | May support the scoped decision |
| `failed` | The observation contradicts the required condition | Blocks acceptance unless an authorized bounded exception applies |
| `missing` | Required evidence or relationship was not supplied | Blocks the dependent decision and routes to an owner |
| `unknown` | The system cannot determine the state reliably | Never silently treated as passed |
| `conditional` | A scoped exception with compensation, authority, and expiry applies | Supports only the recorded boundary |
| `not-applicable` | The gate does not fit this claim, with a recorded semantic reason | Excluded explicitly, never by omission |
| `superseded` | A newer claim, artifact, run, decision, or gate definition replaced it | Preserved as history without current authority |

**Gate A: source, need, and claim**

- [ ] The user or operational need is concrete enough to identify affected behavior and decision consequence.
- [ ] The authority that accepted the behavior is named; an example or historical source is not mistaken for authority.
- [ ] Every claim has a stable identity and exact revision or digest.
- [ ] Each claim states one independently decidable obligation, or its coupling is an intentional interaction contract.
- [ ] Preconditions, trigger, observable outcome, boundary, failure behavior, and defaults are explicit where relevant.
- [ ] Qualitative properties use accepted units, workload, environment, statistic, and objective rather than copied sample values.
- [ ] Assumptions, exclusions, unresolved conflicts, and source currentness are visible.
- [ ] A changed claim supersedes rather than silently mutates prior meaning.

**Completion decision:** the change may enter evidence design when semantics are reviewable. Product acceptance is not manufactured by this checklist.

**Gate B: traceability graph**

- [ ] Claims link to required positive, negative, boundary, and interaction cases by typed relationships.
- [ ] Claims link to the implementation, configuration, schema, policy, or operational mechanism that realizes them.
- [ ] Evidence requirements name what must be observed and why the evidence class can observe that failure.
- [ ] Many-to-many relationships are represented directly; names and file proximity are not the sole link mechanism.
- [ ] Duplicate identities, dangling links, forbidden cycles, conflicting active revisions, and ambiguous supersession fail validation.
- [ ] Optional and not-applicable edges include a semantic reason rather than disappearing from the graph.
- [ ] Generated projections identify their authoritative input and can be reproduced.

**Completion decision:** the graph is structurally closed for the selected profile, but structural closure is not yet semantic or runtime proof.

**Gate C: evidence design and expected failure**

- [ ] Each test or review case states which claim behavior it can distinguish.
- [ ] Assertion depth matches the claim: output shape, side effect, error type, interaction, quality measure, or deployment state as required.
- [ ] A negative probe, mutation, controlled fault, or counterexample is selected for consequential assertions.
- [ ] The expected initial failure is named, including why it demonstrates a missing behavior rather than broken setup.
- [ ] Unit, integration, system, quality, policy, and human-review evidence are used only within their observation boundaries.
- [ ] Test data and environments expose relevant boundaries instead of making the desired result inevitable.
- [ ] Non-determinism, retries, isolation, and cleanup behavior are planned where they can alter interpretation.

**Completion decision:** implementation may proceed when the expected evidence can fail for a relevant reason. If the change existed before the evidence, create a controlled counterexample rather than inventing an earlier history.

**Gate D: observed execution and retained evidence**

- [ ] The expected negative observation occurred and its cause was inspected.
- [ ] The minimum implementation changed relevant evidence to passing without masking unrelated failures.
- [ ] Broader regression evidence appropriate to the impact set was run.
- [ ] Each result binds claim revision, source revision, built artifact, environment, command or review question, and observed time.
- [ ] Skips, cancellations, retries, flakes, missing results, and infrastructure failures retain their own states.
- [ ] Repeated runs do not inflate independently evidenced claim counts.
- [ ] Required artifacts are durably retrievable by identity with integrity checks.
- [ ] Performance or reliability claims retain raw measurements and method metadata, not only a summarized green label.

**Completion decision:** evidence is reviewable only for the artifact and boundary it actually observed.

**Gate E: review, exceptions, and disposition**

- [ ] A reviewer checks semantic fit between need, claims, cases, implementation, assertions, and evidence.
- [ ] The reviewer role has authority for the decision being recorded.
- [ ] Counterarguments, known limitations, rejected alternatives, and residual risk are visible.
- [ ] Every exception identifies affected claims, missing or failed evidence, rationale, compensating control, enforcement, owner, scope, expiry, and review trigger.
- [ ] Expired, ownerless, unenforced, or overbroad exceptions fail closed for their dependent decision.
- [ ] The disposition is explicit: accepted, rejected, conditional, or superseded.
- [ ] The rationale cites the evidence and uncertainty that actually changed the decision.

**Completion decision:** a visible failure with an authorized rejection is more complete than an unexplained all-green record.

**Gate F: release reconciliation**

- [ ] The exact release candidate digest matches the artifacts exercised by required evidence.
- [ ] Every in-scope active claim has a current disposition for this candidate.
- [ ] Accepted claims have all required evidence; rejected claims are absent or blocked.
- [ ] Conditional claims remain inside enforced exception scope.
- [ ] Superseded claims and evidence grant no authority to the candidate.
- [ ] Generated documentation and matrices reflect the authoritative graph version.
- [ ] Release logs retain the candidate, claim set, evidence set, exceptions, owner, and final decision.
- [ ] Rollback, migration, or compatibility obligations are linked where the change requires them.

**Completion decision:** the candidate may ship only within the reconciled decision boundary. A previous release's green evidence cannot authorize a rebuilt artifact by label similarity.

**Gate G: maintenance and recovery**

- [ ] Invalidation triggers cover claim, implementation, dependency, runner, schema, environment, authority, and retention changes that matter.
- [ ] Evidence and decisions can be reconstructed after the author's workspace and short-lived CI logs are gone.
- [ ] Tool, schema, and checklist versions needed to interpret historical results are retained.
- [ ] Public or ecosystem claims have a refresh trigger and do not overwrite local observed evidence automatically.
- [ ] Incidents and review reversals produce bounded fixture, gate, ownership, or guidance changes.
- [ ] Duplicate views are generated or reconciled; no unexplained second authority drifts independently.
- [ ] Retired identifiers, profiles, and mechanisms have migration and consumer disposition.
- [ ] Costly checks that never inform decisions are reviewed for simplification or removal.

**Profile selection**

| Profile | Use when | Required depth beyond core identity and disposition |
|---|---|---|
| Compact | Local, reversible, low-consequence behavior with one owner and no release gate | Direct behavior case, relevant assertion, current result, retrieval, and change invalidation |
| Shared | Behavior crosses modules, owners, generated artifacts, or delayed handoffs | Typed graph, impact review, broader evidence, explicit ownership, and release reconciliation |
| Consequential | Security, data integrity, external compatibility, operational objective, regulated approval, or expensive reversal is involved | Negative probes, independent review, durable evidence, exceptions, recovery, and stronger retention |
| Migration | Identity, schema, runner, generator, or evidence store changes | Dual-version compatibility fixtures, consumer inventory, conversion audit, and retirement evidence |

Core identity, revision binding, missing-state semantics, evidence fit, current disposition, and release scope are never waived by choosing a lighter profile. The profile changes depth, not the meaning of a pass.

**Final reconstruction question**

An independent reviewer should be able to answer, from retained records:

> Which accepted claim revision does this candidate implement, which evidence could have disproved it, what was actually observed against this artifact, who had authority to decide, which limitations remain, and what event reopens the decision?

If any part cannot be answered, record `missing` or `unknown`, route the gap to its owner, and limit the decision accordingly. Preserve the checklist definition and version that evaluated each historical release so later reviews do not apply new state semantics retroactively.

## Adjacent Reference Routing

Stay in this reference when the unresolved decision is how accepted claim revisions connect to cases, implementation, evidence, exceptions, release artifacts, and an accountable disposition. Route elsewhere when another concern must be resolved before those links can be made honestly.

Relevant filenames below were observed in the July reference directory on 2026-07-11. Their path existence supports navigation only. Their evolved completeness, current authority, and compatibility with a target project were not evaluated here; read a selected reference before consequential adoption.

**Decision-state router**

| Unresolved decision | Candidate adjacent reference | Expected return artifact | Reentry condition |
|---|---|---|---|
| The request is vague, bundled, or lacks testable semantics | `executable_specification_skill_patterns-20260710.md` | Atomic claim revisions, boundaries, accepted measures, and authority | Return when claims are stable enough to design typed links and evidence |
| The claims are clear but the test-first development loop is unclear | `tdd_cycle_skill_patterns-20260710.md` | Expected failure, minimum passing change, refactoring evidence, and observed results | Return when runs can be bound to claim and artifact identities |
| The implementation appears done but completion or release confidence is disputed | `completion_verification_gate_patterns-20260710.md` | Current verification observations and completion disposition | Return for claim-level evidence fit and release reconciliation |
| Work spans interruptions or ownership handoffs | `tdd_progress_journal_schema-20260710.md`, `tdd_checkpoint_cadence_playbook-20260710.md`, or `tdd_resume_handoff_prompts-20260710.md` | Durable phase, exact evidence state, files in motion, blocker, and next action | Return when handoff records need to join to claim and evidence revisions |
| A broad executable-practice orientation is needed before choosing a narrow workflow | `executable_metapattern_reference_digest-20260710.md` | A bounded practice choice and reasons rejected alternatives do not fit | Return before creating traceability artifacts; a digest is not release evidence |
| A Rust-specific executable template is needed after semantics are accepted | `rust_executable_template_patterns-20260710.md` | Target-language artifact that preserves claim identities and evidence meaning | Return to validate cross-language links and release state |
| The problem is Rust build or convention enforcement rather than behavior traceability | `rust_conventions_quality_gates-20260710.md` or `rust_quality_gate_patterns-20260710.md` | Observed target gate result with artifact identity | Return only if the gate contributes evidence required by a claim |
| The problem is Kotlin backend test data or integration setup | `kotlin_backend_testing_fixtures-20260710.md` | A fixture strategy and observed target tests | Return when fixtures can be evaluated for semantic fit and isolation |
| The deliverable is an interactive learning or experimentation surface | `interactive_playground_template_patterns-20260710.md` | A runnable demonstration with stated educational boundary | Return if demonstration behavior becomes a supported product claim |

Do not route by keyword alone. Ask:

1. What exact decision cannot be made with the current artifact?
2. Which reference appears to own that decision?
3. What stable identity, evidence, or disposition must come back?
4. What target version and authority make the returned guidance applicable?
5. Which original claim-graph state should change if the route succeeds?

If no state changes, the route was orientation rather than resolution. That may still be useful, but it must not be reported as evidence.

**Route contract**

Before leaving, record:

```text
Original claim or change identity
Current lifecycle state
Unresolved decision and consequence
Selected adjacent path and observed version
Reason this reference does not own the decision
Expected return artifact and owner
Compatibility assumptions
Reentry gate and stop condition
```

On return, verify that the artifact can join to the original claim revision. A test result without the same build identity, a requirement rewrite without acceptance authority, or a checklist with incompatible state semantics is not a completed handoff.

**Good, bad, and borderline routes**

**Good:** a bundled request is routed to executable specification guidance. It returns three atomic claims plus one interaction claim, each accepted by the product owner. This reference then builds cases, implementation links, evidence requirements, and release decisions around those revisions.

**Bad:** missing runtime evidence is routed to a language style guide. The result improves naming but provides no observed behavior, artifact identity, or evidence state. The original release uncertainty remains unchanged.

**Borderline:** an older workflow playbook provides a useful expected-failure responsibility but names obsolete runner syntax. Preserve the responsibility, discover the target command, and verify its observed states; do not copy the stale mechanism or treat the route as current authority.

**Route verification**

Use inexpensive checks continuously:

```bash
test -f idiomatic-ref-202607/executable_specification_skill_patterns-20260710.md
test -f idiomatic-ref-202607/tdd_cycle_skill_patterns-20260710.md
test -f idiomatic-ref-202607/completion_verification_gate_patterns-20260710.md
test -f idiomatic-ref-202607/tdd_progress_journal_schema-20260710.md
test -f idiomatic-ref-202607/executable_metapattern_reference_digest-20260710.md
```

For a selected consequential route, additionally verify:

- The referenced heading and decision boundary exist, not just the file.
- Its source, target, version, and evidence assumptions fit the current project.
- Vocabulary and lifecycle states can be translated without losing meaning.
- Returned identifiers are unique and joinable to the original artifact.
- Required evidence remains observable after the handoff.
- Contradictory guidance is recorded and resolved by an accountable owner.
- The route does not enter a cycle that only adds documents and never changes a decision.

If a path is missing or stale, keep the unresolved state visible and use the smallest inline rule needed to continue safely. Do not invent the absent reference's contents. Broken optional navigation is a documentation defect; a broken route that owns required release evidence is a control failure and should block the dependent decision.

Consequential routes form a dependency graph among schemas, identities, workflow phases, and artifact versions. Track compatibility and retirement for those edges. A renamed file is inexpensive to repair; a changed meaning for `passed`, `conditional`, or `superseded` can reinterpret historical releases and requires migration evidence.

## Workload Model

Treat executable traceability as a change-and-evidence workload, not a document-size workload. A packet with many independent low-risk claims may be easier than three tightly coupled claims crossing services, owners, environments, and release authorities. No source evidence supports a universal claim-count ceiling.

Start with one coherent **change unit**: claims that share a behavior boundary, accountable decision, release fate, and evidence lifecycle. Measure pressure before selecting local limits.

**Workload vector**

| Dimension | Observation | Pressure signal | Possible response |
|---|---|---|---|
| Active claim revisions | Count of current claim versions in the decision boundary | Reviewers cannot state each obligation or distinguish superseded meaning | Narrow the change, generate concise views, or add domain partitions |
| Relationship density | Required typed edges among claims, cases, implementation, evidence, decisions, and releases | Missing interactions, graph query growth, or unreadable matrices | Preserve graph authority; project task-specific views and index common traversals |
| Fan-out and fan-in | Dependents invalidated by one revision and inputs supporting one decision | A small edit triggers broad rerun or one decision depends on opaque evidence volume | Classify impact, cache immutable results, and isolate stable subgraphs |
| Claim change rate | Revisions and supersessions per observation window | Evidence and reviews become stale before release | Shorten decision windows, automate invalidation, or separate volatile claims |
| Evidence run volume | Unique artifacts, environments, retries, shards, and review observations | Current state is buried in retry history or storage cost grows unexpectedly | Deduplicate by decision identity and tier historical retention |
| Evidence size | Logs, reports, samples, screenshots, attestations, and human records retained | Retrieval slows or authors link summaries with no raw support | Store content by digest, retain reproducible summaries, and apply policy-based tiers |
| Environment cardinality | Supported platforms, deployments, configurations, and dependency combinations | Matrix explosion or untested combinations are hidden | Define support classes, risk-based combinations, and explicit uncovered states |
| Owner count | Product, engineering, security, operations, compliance, and release roles involved | Approval ambiguity and handoff delay | Separate authority types and record one accountable disposition per decision |
| Repository or service span | Code and evidence boundaries crossed by a claim | Broken links, version mismatch, and partial candidate identity | Use global stable identities and explicit cross-boundary contracts |
| Release concurrency | Candidates, branches, versions, and deployments evaluated simultaneously | Evidence for one candidate authorizes another | Bind every result and decision to immutable candidate identities |
| Access segmentation | Evidence subject to restricted, external, or tenant-specific controls | Reviewers cannot retrieve required artifacts or copied data violates policy | Preserve verifiable authority links and least-privilege projections |
| Consequence | Security, data, compatibility, availability, financial, or regulatory impact | Lightweight evidence cannot support reversal cost | Increase independent review, probe depth, retention, and release enforcement |
| Retention horizon | Time decisions must remain reconstructable | Schema and tools change before records expire | Preserve interpretation versions and test migrations with historical fixtures |
| Generated projection count | Matrices, reports, docs, dashboards, and manifests derived from the graph | Duplicate truth drifts or regeneration dominates authoring | Keep one write model, incremental generation, and projection integrity checks |

Record `current` and `historical` workloads separately. Superseded claims and retry runs belong in retained history but should not inflate the current release denominator or slow its common queries unnecessarily.

**Coherent-unit test**

Keep work in one traceability unit when most answers are yes:

- Do the claims serve one accepted user or operational outcome?
- Can one accountable owner decide the behavior, with named specialist reviews where required?
- Do the claims share a release candidate or coordinated release boundary?
- Are their evidence environments and retention rules compatible?
- Can a reviewer understand the interaction graph without unrelated context?
- Will a revision invalidate a bounded, predictable evidence set?
- Can access rules expose enough evidence to every required decision maker?

Partition when semantics, authority, release fate, access policy, or evidence lifecycle diverges. Do not split a transaction merely to satisfy a row count. If decomposition is unavoidable, preserve an explicit parent interaction claim and aggregate release view.

**Partition strategies**

| Partition axis | Prefer when | Benefit | Cost to control |
|---|---|---|---|
| Bounded behavior | Domain outcomes change independently | High semantic coherence | Cross-domain interactions need explicit contracts |
| Accountable owner | Decisions have distinct authorities | Clear review and escalation | Organization changes can destabilize partitions |
| Release unit | Components ship independently | Evidence aligns with immutable artifacts | Coordinated behavior needs aggregate reconciliation |
| Evidence environment | Test or review systems have distinct lifecycle and access | Isolates operational pressure | One claim may require joins across evidence stores |
| Repository or service | Tooling and source ownership are naturally separate | Local automation stays practical | Global identity and version joins become essential |
| Access boundary | Restricted evidence cannot share one store or view | Supports least privilege | Missing visibility can be mistaken for missing evidence |
| Volatility tier | Rapidly changing claims invalidate evidence frequently | Stable subgraphs remain cacheable | Cross-tier changes need impact analysis |

Choose the axis that best aligns authoritative change with evidence lifecycle. Count the resulting cross-partition edges and sample their review and reconciliation cost. A partition is not successful if local packets shrink while release assembly becomes an undocumented manual process.

**Workload scenarios**

**Small and coherent:** one session-revocation change has four claims, two implementation components, integration and concurrency evidence, one product owner, and one release candidate. Keep one unit; the low count and shared lifecycle make the interactions reviewable.

**Small but consequential:** three data-deletion claims cross application storage, backups, and audit retention under separate authorities. Do not select the compact profile because the count is low. Preserve one outcome view while partitioning evidence and approvals by authority and access boundary.

**Large but regular:** many generated API compatibility claims share one schema revision, generator version, consumer inventory, and release. Keep a normalized source graph, generate consumer-specific projections, and test the generator and compatibility model. Hand-editing one large matrix will drift.

**High churn:** a volatile experiment revises claims faster than broad environment suites can finish. Separate non-shippable exploration from accepted behavior, run targeted evidence during discovery, and trigger the full accepted profile only for a stabilized candidate. Never let exploratory passes authorize release.

**Borderline transaction:** one order-cancellation transaction spans order, fulfillment, and payment owners. Partition implementation evidence by service but retain a parent interaction claim, controlled partial-failure probes, and aggregate release reconciliation. Measure whether reviewers can reconstruct the transaction after the split.

**Calibration and verification**

Collect target evidence before setting limits:

1. Count current claims, typed edges, revisions, artifacts, runs, retries, environments, owners, exceptions, and release candidates.
2. Measure degree distributions and identify claims whose revisions invalidate unusually broad evidence sets.
3. Sample time and error for common queries: claim-to-release, change impact, missing evidence, exception expiry, and decision reconstruction.
4. Generate representative dense, high-churn, multi-environment, and long-history fixtures; include missing and stale states.
5. Ask independent reviewers to reconstruct sampled decisions and record ambiguity, omitted interactions, and unavailable evidence.
6. Replay a release and a schema or store migration using retained identities and historical interpretation versions.
7. Test partition candidates by comparing cross-unit edge count, duplicated authority, invalidation scope, retrieval, and final reconciliation effort.
8. Establish provisional objectives only after the accountable owner sees baseline distributions and consequence.

Synthetic scale can expose storage, query, generation, and invalidation behavior. It cannot reproduce every semantic misunderstanding or organizational handoff, so pair it with sampled real decisions, review reversals, and incidents.

**Pressure responses**

- If graph reads slow but semantic coherence remains good, index or project before partitioning behavior.
- If reviewers cannot understand claims despite fast queries, narrow the decision boundary or improve task-specific views.
- If revisions invalidate excessive unrelated evidence, separate volatile domains and correct overbroad links.
- If evidence retention dominates cost, tier history while preserving claim, artifact, decision, and integrity lineage.
- If restricted evidence blocks reviewers, create least-privilege attestations or routed review rather than copying protected content.
- If generated views drift, stop manual edits and verify generation from one authoritative model.
- If release reconciliation is the bottleneck, align partitions with release identity or automate the aggregate query.

The relevant capacity boundary is where an accepted decision-quality, release, retrieval, or recovery objective degrades. Calibrate that boundary from observed behavior and revise it when workload shape, tools, support commitments, or consequence changes. Compacting or partitioning must preserve enough causal lineage to explain why a candidate was accepted; deleting that lineage trades visible performance for hidden recovery cost.

## Reliability Target

Reliability has two layers:

1. **Decision-integrity invariants** describe states the traceability process must never treat as valid authority.
2. **Operational objectives** describe availability, latency, retrieval, recovery, and review behavior whose targets require a measured local baseline and accountable owner.

The historical values in the seed are not measured target results. Do not inherit a perfect percentage or a small sample threshold as policy.

**Decision-integrity invariants**

| Invariant | Forbidden state | Detection | Required response |
|---|---|---|---|
| Identity uniqueness | Two active artifacts claim the same identity and revision with different meaning | Parser, content digest, and graph uniqueness check | Quarantine conflict; do not select one by timestamp alone |
| Revision isolation | Evidence for an older claim revision authorizes changed semantics | Claim-to-run revision join and invalidation query | Mark evidence stale and rerun or review the current revision |
| Artifact binding | A result or decision for one build authorizes another candidate | Immutable source, build, environment, and release digest comparison | Block reconciliation until matching evidence exists |
| State fidelity | Missing, unknown, skipped, cancelled, inaccessible, failed, or superseded becomes passed | State-machine validation and synthetic transition fixtures | Reject transition and repair affected decisions |
| Semantic evidence fit | A linked artifact cannot observe the claim's prohibited behavior | Reviewer audit plus negative probe or mutation | Remove false authority and add fitting evidence |
| Decision authority | A role accepts, waives, or releases behavior outside its authority | Role and policy validation with recorded scope | Escalate to an accountable owner; preserve prior observation without authority |
| Exception containment | A waiver exceeds scope, lacks enforcement, or survives expiry | Exception query and release-boundary check | Fail closed for affected claim unless emergency policy explicitly applies |
| Source boundary | Historical text, external guidance, inference, and target evidence are presented as interchangeable | Provenance labels, source retrieval, and semantic review | Correct claim status before reuse or generation |
| Release closure | A candidate ships with unresolved required claims or unreconciled evidence | Claim-to-candidate release query | Block or narrow release according to authorized policy |
| Historical integrity | A current schema or checklist silently reinterprets an older decision | Versioned decoder and migration fixtures | Use the historical interpretation or record an explicit migration |

These are safety intentions, not claims that an implementation has achieved perfection. Observe violations, retain incidents, and test recovery. An aggregate success rate must never create an allowed quota for a wrong high-consequence release authorization.

**Operational objective contract**

Define each local objective with:

```text
Decision served and accountable owner
Population and consequence class
Service indicator and exact calculation
Observation window and missing-data rule
Accepted objective and error-budget response
Measurement source and independent check
Known confounders and countermetric
Degraded-mode behavior
Recovery objective and reconciliation step
Review and retirement trigger
```

Candidate indicators include:

| Operational concern | Indicator candidate | Objective-setting evidence | Countermeasure against false confidence |
|---|---|---|---|
| Evidence retrieval | Successful identity-and-integrity retrievals divided by required retrieval attempts | Baseline by store, age, and access class; support commitment | Sample semantic fit and permission-denied classification |
| Current-state query | Duration and correctness of claim-to-release and missing-evidence queries | Representative graph size, density, and concurrency | Compare query result with independent raw-record reconstruction |
| Invalidation propagation | Delay from relevant change event to affected evidence becoming non-current | Change replay and observed production events | Audit false invalidations and missed dependents |
| Projection consistency | Generated views matching the authoritative graph version | Regeneration fixtures and sampled repository checks | Reject manual edits and verify content digest |
| Decision reconstruction | Independent reviews that recover the original claim, evidence, authority, and release scope | Historical samples across retained versions | Include older schema, restricted evidence, and rejected decisions |
| Backup recovery | Restored records supporting integrity checks and decision replay | Isolated restore drill | Verify artifact retrieval and historical decoder, not file count alone |
| Gate false-block burden | Incorrect blocks attributable to traceability data or control faults | Release incident classification | Pair with escaped-invalid-decision review |
| Degraded operation | Decisions handled according to declared outage policy | Fault injection and emergency drill | Reconcile every bypass after service recovery |

Set no objective until the population, consequence, indicator, and response are understood. Initial launch criteria may be conservative and provisional, but must state owner, expiry, and calibration plan.

**Reliability across failure modes**

| Failure condition | Preserve | Do not infer | Degraded action |
|---|---|---|---|
| Evidence store unavailable | Known identity, last verified state, and outage observation | That a remembered pass remains current | Hold dependent release or invoke authorized scoped emergency policy |
| Permission denied | Artifact identity, required reviewer role, and access failure | That evidence is absent or failed | Route least-privilege review or obtain a verifiable attestation |
| Generator failure | Authoritative source graph and last projection version | That an old projection represents current state | Repair generation or use direct graph review with recorded version |
| Partial schema migration | Old and new version identities plus conversion status | That migrated and unmigrated records share semantics | Use version-aware readers and block ambiguous joins |
| Conflicting active revisions | Both records and their provenance | That latest timestamp implies authority | Quarantine and resolve with owner and accepted supersession |
| Clock skew | Immutable event identities and causal sequence where available | That wall-clock order proves currentness | Prefer revision and artifact causality; flag ambiguous time rules |
| Retry storm | Each attempt state and one decision unit | That retries are independent evidence | Deduplicate metrics and inspect infrastructure cause |
| Cache lag | Authoritative version and cache observation | That a fast response is current | Reject stale authority and refresh or bypass cache safely |
| Corrupted evidence | Identity, expected digest, and corruption observation | That partial readable content is valid | Isolate artifact, restore from verified copy, and re-evaluate decisions |

Availability and truth are orthogonal. A highly available cache can return stale authority; an unavailable store can contain correct evidence that cannot presently support a decision. Preserve those distinctions.

**Control-plane policy**

If traceability gates release automatically, choose outage behavior by consequence:

- **Fail closed:** default for missing required high-consequence evidence, expired exceptions, identity conflicts, or mismatched candidates.
- **Narrow release:** permit only claims and environments with current evidence and enforced separation from blocked scope.
- **Degraded manual review:** use independently retrievable evidence and an authorized reviewer, retaining the exact outage and decision record.
- **Emergency bypass:** require explicit break-glass authority, bounded scope, compensating controls, expiry, immutable audit record, and post-recovery reconciliation.
- **Fail open:** acceptable only where an authorized policy explicitly judges traceability unavailability less harmful than delay; never make this the accidental result of unknown being treated as pass.

An emergency action does not erase missing evidence. After recovery, reconstruct the candidate, rerun or retrieve required observations, review the bypass outcome, resolve exceptions, and add a regression fixture for the failure mechanism.

**Verification program**

| Reliability question | Verification method | Expected evidence |
|---|---|---|
| Can invalid states grant authority? | State-machine and property tests over all transitions | Rejected transition with preserved original state |
| Can weak evidence look valid? | Mutation and controlled-fault suites | Relevant evidence fails for the intended reason |
| Can concurrent revisions split authority? | Concurrency tests around create, supersede, and decide operations | One valid active lineage or explicit quarantined conflict |
| Can stale caches authorize release? | Delay and partition injection between source and projection | Stale version rejected at reconciliation |
| Can retained data survive tool change? | Versioned migration fixtures and dual-reader comparison | Equivalent meaning or explicit incompatible record |
| Can evidence be recovered? | Isolated backup restore plus digest verification | Historical decision reconstructed from restored artifacts |
| Can least privilege preserve review? | Access-role tests and restricted artifact routing | Authorized reviewer obtains sufficient evidence without data copying |
| Can outage policy be followed? | Staged service failure and emergency drill | Correct block, narrowing, or authorized bypass plus reconciliation |
| Can false blocks be diagnosed? | Release-control incident replay | Root cause, corrected state, and regression fixture |

Manual source review and downstream samples remain useful, but they cannot cover corruption, concurrency, state conversion, migration, restore, or outage behavior. Conversely, automated fault tests cannot determine whether a product claim or reviewer judgment is wise. Keep the layers independent enough to disagree.

Report reliability with two evidence classes: **control design** states what should prevent or contain failure; **observed exercise** states what actually happened under representative use or injected faults. Current target values, recovery objectives, and accepted error budgets remain unresolved until a target owner adopts them from measured evidence.

## Failure Mode Table

Contain incorrect authority first; diagnose exact cause second. A detector has not contained a failure if stale or unsupported evidence can still authorize the candidate.

| Failure mode | Trigger or detection signal | Unsafe inference to prevent | Immediate containment | Recovery and recurrence control |
|---|---|---|---|---|
| Source drift | Local policy, public guidance, tool behavior, or support boundary changes | Historical guidance remains current automatically | Mark affected adaptations unresolved or stale; stop regeneration that grants authority | Retrieve current source, compare applicability, record owner decision, and add a refresh trigger |
| Unsupported synthesis | Plausible recommendation has no source boundary, accepted target need, or verification path | Fluent prose is production evidence | Remove decision authority from the claim and label it as a hypothesis | Obtain target evidence or narrow the guidance; add a review fixture for unsupported claims |
| Identity collision | Same active identity and revision resolves to different content | Timestamp or file order selects the correct meaning | Quarantine both lineages and block dependent joins | Resolve ownership, assign unambiguous revisions, migrate consumers, and enforce uniqueness |
| Bundled claim | One claim contains independently decidable outcomes | One passing case proves every embedded obligation | Prevent acceptance and split obligations while retaining needed interaction semantics | Add atomicity review and fixtures containing conjunction, quality, and failure clauses |
| Lost interaction | Atomic claims pass independently but transactional or concurrent behavior is absent | Decomposition guarantees combined behavior | Block the combined release decision where coupling is consequential | Add an interaction claim, controlled partial-failure case, and aggregate reconciliation |
| Wrong or dangling edge | Link target is absent, wrong type, wrong revision, or semantically irrelevant | Graph completeness equals evidence fit | Remove invalid authority and mark dependent claims missing | Repair typed link, rerun graph checks, and sample semantic fit |
| Insensitive assertion | Test remains green after prohibited behavior is introduced | A linked passing test observes the claim | Downgrade evidence and hold dependent disposition | Add a mutation or controlled fault, deepen assertion, and preserve the negative observation |
| Unobserved expected failure | Passing evidence exists with no relevant negative baseline or probe | The test could have detected absence of behavior | Treat assertion sensitivity as unknown | Run a safe counterexample or mutation and record expected versus observed failure |
| Evidence-class mismatch | Unit, review, benchmark, deployment, or attestation evidence is used outside its observation boundary | Any artifact labeled evidence proves any claim | Remove the mismatched link from required evidence | Select a fitting evidence class and retain the weaker artifact only for what it actually shows |
| Stale claim run | Claim, implementation, dependency, environment, or runner changes after observation | Recent timestamp alone means current | Mark affected run non-current and reopen decision | Execute or review the current revision; test invalidation propagation |
| Candidate mismatch | Run artifact digest differs from release candidate | Similar branch, version, or job name proves identity | Block release reconciliation | Rebuild or rerun against exact candidate and enforce immutable joins |
| State collapse | Missing, unknown, skipped, cancelled, denied, failed, or superseded appears as passed | Absence of a red result is success | Reject conversion and identify every decision that consumed it | Repair state model, backfill affected records, and add transition fixtures |
| Duplicate-run inflation | Retries or shards count as separately evidenced claims | More green rows mean broader coverage | Deduplicate the decision population | Retain attempts for diagnostics while aggregating by claim, artifact, environment, and evidence requirement |
| Unsupported quality target | Latency, reliability, capacity, security, or accuracy value lacks accepted method and authority | A concrete number copied from a template is an objective | Remove release authority from the value | Define workload, unit, statistic, environment, owner, baseline, and measurement evidence |
| Exception escape | Waiver is ownerless, unenforced, overbroad, copied, or expired | A prior approval permanently changes policy | Block affected scope or invoke explicit emergency policy | Re-decide, narrow, compensate, enforce, expire, and test release boundaries |
| Unauthorized disposition | Reviewer role lacks authority for acceptance, rejection, exception, or release | Participation implies decision rights | Preserve observation but remove authoritative status | Route to accountable owner and validate role scope at transition time |
| Evidence inaccessible | Artifact exists but required reviewer or gate cannot retrieve it | Claimed existence supports the decision | Classify inaccessible separately from missing or failed; hold dependent decision | Restore access, use approved routed review, or reproduce evidence with matching identity |
| Evidence corruption | Digest mismatch, incomplete object, undecodable record, or lost metadata | Readable fragments are trustworthy | Quarantine artifact and invalidate dependent current state | Restore verified copy or regenerate, then replay affected decisions |
| Projection drift | Matrix, documentation, dashboard, or manifest differs from authoritative graph version | A polished generated view is current | Stop consuming the projection for authority | Regenerate deterministically, reject manual edits, and verify source-version digest |
| Partial migration | Old and new schemas, identities, or state meanings coexist without compatibility rules | All records can be joined under one interpretation | Use version-aware readers and quarantine ambiguous conversions | Run dual-version fixtures, audit conversion, migrate consumers, and record retirement |
| Release open set | Candidate has active claims with no disposition or unexamined evidence dependencies | A green build closes product behavior automatically | Block or narrow release boundary | Run claim-to-candidate closure query and record final accountable reconciliation |
| Recovery without reconciliation | Tool or evidence is repaired but prior decisions remain based on bad state | Restoring service restores decision validity | Keep affected decisions reopened | Recompute impact, rerun evidence, reaffirm or withdraw decisions, and annotate historical incident |

Not every requirement needs a test. It needs evidence appropriate to its semantics: automated behavior, benchmark, static rule, deployment observation, policy review, human judgment, or a combination. Conversely, one test name containing an ID does not establish a useful relationship.

**Triage sequence**

1. Identify the claim revision, candidate, decision, and consequence that may be affected.
2. Preserve raw states, conflicting records, logs, identities, and access observations before repair.
3. Prevent new authority from flowing through the suspect artifact or transition.
4. Classify what is known as missing, stale, failed, denied, corrupt, conflicting, or unknown.
5. Trace upstream causes and downstream consumers; compound failures rarely stop at the first visible symptom.
6. Repair the smallest causal mechanism without rewriting historical evidence.
7. Re-execute relevant probes and verify the detector, containment, and recovery path.
8. Reconcile every dependent decision: reaffirm with current evidence, narrow, reject, or supersede.
9. Add a regression fixture and update schema, gate, guidance, ownership, or observability where justified.

**Response examples**

**Good:** release reconciliation detects that a passing integration run belongs to an older artifact digest. The gate blocks the candidate, preserves the historical run, executes current evidence, records the new disposition, and adds a mismatch fixture.

**Bad:** a flaky job is rerun until green, the successful attempt replaces all prior states, and the release proceeds. This destroys evidence about instability and does not establish that the final pass observed the intended behavior.

**Borderline:** a graph migration repairs every current link, but old evidence objects cannot be retrieved. Current release may proceed if all required evidence is reproduced and accepted; historical reconstruction remains degraded and needs an explicit retention incident, not a silent green status.

**Verification probes by family**

- Introduce conflicting active revisions and confirm the graph quarantines rather than selects one.
- Remove an interaction edge and confirm the aggregate release query reports a missing obligation.
- Mutate behavior behind a linked assertion and confirm the expected case fails.
- Feed skipped, denied, corrupt, cancelled, and superseded states through every projection and confirm none becomes passed.
- Attach a valid run to a different candidate digest and confirm release reconciliation rejects it.
- Expire an exception and confirm its dependent scope is blocked or routed through explicit emergency policy.
- Break evidence retrieval after authoring and confirm the decision state changes to inaccessible.
- Migrate historical fixtures through versioned readers and compare meaning, not only parse success.
- Repair an injected fault and confirm all downstream decisions remain reopened until current evidence reconciles them.

The table is a reference hazard catalog, not observed frequency data. Rank target work using local incidents, consequence, propagation breadth, detectability, and recovery cost. No recorded incidents may reflect strong controls, low exposure, or weak detection; it does not prove the failure is absent.

## Retry Backpressure Guidance

Retry only when another attempt can produce new valid information without hiding prior state, changing the decision unit silently, or repeating unsafe side effects. A semantic contradiction is not an infrastructure transient.

**Retry eligibility**

| Failure class | Retry? | Required precondition | Escalation or alternative |
|---|---|---|---|
| Network timeout retrieving immutable evidence | Usually bounded | Operation is idempotent, digest is known, deadline remains, and prior timeout is retained | Circuit-break dependency and classify evidence inaccessible |
| Isolated runner startup failure | Usually bounded | No test behavior executed, candidate identity is unchanged, and infrastructure cause is observable | Move to healthy isolated runner or mark infrastructure failure |
| Eventually consistent projection lag | Bounded polling or event wait | Authoritative source version is fixed and projection exposes its applied version | Read authority directly or classify projection stale |
| Rate limit or dependency overload | Delayed and coordinated | Retry guidance is current, global budget exists, jitter or queueing is available, and work remains relevant | Apply backpressure and circuit breaking |
| Corrupted retrieved object | No blind retry | Expected digest exists and alternate verified replica may be selected | Quarantine object, restore or regenerate, then re-evaluate |
| Permission denied | No time-based retry | Access policy or reviewer route must change explicitly | Request authorized access or routed attestation |
| Invalid schema or parse error | No unchanged retry | Input, schema version, or decoder must be corrected | Quarantine record and run compatibility repair |
| Duplicate or conflicting identity | No | Accountable lineage resolution is required | Block dependent decisions and resolve conflict |
| Deterministic assertion failure | No retry for authority | Code, claim, test, or fixture must change through a new recorded attempt | Diagnose behavior and preserve failure as evidence |
| Flaky assertion or non-deterministic result | Diagnostic repetitions only | Attempts are retained, isolation is controlled, and no pass replaces failure history | Quarantine test from release authority until reliability is resolved or excepted |
| Missing context or source | No repetition without input | New source, artifact, or owner decision must become available | Route to source owner or mark unresolved |
| Stale claim or candidate | Restart, not retry | New job binds the current claim and candidate identities | Cancel superseded work and recompute impact |
| Expired exception | No | New authorized decision and current compensation are required | Block affected scope or invoke explicit emergency policy |
| Policy or reviewer contradiction | No mechanical retry | Authorities and decision boundary must be reconciled | Preserve both positions and escalate |

"Retryable" never means "ignore the earlier attempt." Preserve each state and distinguish final behavior evidence from operability evidence. A test that passes after several infrastructure attempts may still support behavior for the exact artifact, while the attempt history creates a separate runner-reliability signal. A test that alternates pass and fail under unchanged controlled inputs is not made authoritative by choosing the last result.

**Retry contract**

Before enabling retries, define:

```text
Operation and idempotency key
Decision unit: claim, artifact, environment, evidence requirement
Retryable error classes
Non-retryable and quarantine classes
Attempt-count and elapsed-deadline budgets
Delay, jitter, queue, and concurrency behavior
Side-effect deduplication or compensation
Artifact and source-version stability checks
Cancellation and supersession conditions
Attempt retention and metric aggregation
Escalation owner and degraded-mode decision
```

Numeric limits, delay curves, and concurrency caps require target measurements: dependency contract, typical and tail duration, cost per attempt, side effects, shared-client load, release deadline, and consequence. A provisional policy should be conservative, visible, and reviewed after representative failures. A dependency library's default is only a candidate; nested clients can multiply attempts and exceed the caller's deadline.

Where delayed retries are appropriate, increase delay between attempts and add jitter so independent workers do not synchronize. Stop on the earliest of success, non-retryable classification, elapsed deadline, attempt budget, candidate supersession, cancellation, or circuit-break condition. Do not sleep inside a scarce worker when durable queueing can release capacity safely.

**Evidence-preserving attempt model**

| Attempt state | Meaning | Decision effect |
|---|---|---|
| `scheduled` | Work is accepted for a current decision unit | No evidence yet |
| `running` | One worker owns the attempt lease | No pass implied |
| `transient-failed` | Retryable operation failed and details were retained | Evidence remains missing; budget may allow another attempt |
| `semantic-failed` | Relevant behavior contradicted the claim | Blocks dependent acceptance until a new artifact or decision is evaluated |
| `infrastructure-failed` | Environment prevented a valid observation | Does not prove behavior pass or fail |
| `cancelled` | Work was intentionally stopped | Remains non-evidence with cause |
| `superseded` | Claim, artifact, source, or job revision changed | Result cannot authorize the replacement unit |
| `passed` | Required observation succeeded for the bound unit | Supports only its stated claim and boundary |
| `quarantined` | Result is unreliable, conflicting, corrupt, or under investigation | Grants no authority until resolved |

Aggregate metrics by the decision unit, not attempt rows. Retain attempts for diagnosis. A hundred retries of one claim do not create broader claim coverage.

**Backpressure controls**

Apply backpressure before repeated low-information work consumes all capacity:

| Pressure signal | Local response | Shared-system response | Decision response |
|---|---|---|---|
| Dependency timeouts rise | Pause new optional retrieval and honor deadlines | Reduce concurrency, open circuit, and stagger probes | Mark required evidence inaccessible when deadline expires |
| Runner queue grows | Cancel superseded and duplicate jobs | Prioritize current high-consequence candidates and reserve recovery capacity | Narrow release scope or move decision deadline explicitly |
| Source or schema conflict appears | Stop generation from ambiguous input | Quarantine version and notify owner | Reopen dependent claims and projections |
| Verification gate is red | Stop downstream work that assumes acceptance | Continue independent diagnosis and unaffected units | Reject, repair, or authorize a bounded exception |
| Review backlog grows | Reduce batch size and unrelated context | Allocate owners by decision unit and expose age and consequence | Defer or narrow candidate rather than silently skipping review |
| Evidence store reaches retention pressure | Avoid duplicate uploads and compact diagnostics safely | Tier immutable history while preserving lineage and integrity | Do not delete artifacts supporting active or retained decisions |
| Many agents target one file or theme | Respect exclusive ownership and durable checkpoints | Queue ownership transfers and verify exact scope | Prevent competing revisions from becoming parallel authority |

Backpressure protects reviewer attention as well as compute. Repeated generation against unresolved source boundaries creates more prose without increasing evidence.

**Long-running and distributed workflows**

- Assign one owner to each mutable reference, packet, graph partition, or evidence decision unit.
- Save complete atomic work before transferring ownership; never hand off an unrecorded in-memory state.
- Checkpoint exact paths, revisions, states, tests, blockers, and next action at bounded intervals.
- Re-read the controlling specification and current artifact before broad edits or phase transitions.
- Cancel queued work when its claim or source revision is superseded.
- Use leases or equivalent ownership for shared attempts, with expiry and idempotency protection.
- Verify headings, paths, evidence boundaries, and current revisions when independent outputs reunite.
- Preserve rejected and failed work so another worker does not rediscover the same contradiction as new.

**Timelines**

**Good retry:** attempt A times out retrieving immutable artifact digest `run-auth-session-042`. The timeout is retained. A delayed attempt uses the same identity, succeeds before the decision deadline, verifies the digest, and supplies retrieval evidence. The timeout remains an operability signal.

**Bad retry:** an integration assertion fails, so the job repeats until one pass occurs. The system reports only green. No source, artifact, environment, or behavior changed, and the discarded failures may indicate a race. Quarantine the result rather than authorizing release.

**Borderline restart:** a generated matrix job fails transiently, but the source graph changes before the retry. The worker must cancel the old decision unit and start a new job bound to the new graph version. Attaching the successful projection to the old job would misstate lineage.

**Verification**

1. Inject each retryable and non-retryable error class and assert the intended transition.
2. Run concurrent duplicate attempts and verify side effects deduplicate by the declared key.
3. Supersede the claim or artifact while work is queued and confirm cancellation prevents old authority.
4. Simulate dependency overload and confirm concurrency falls, delay spreads attempts, and the circuit opens before capacity is exhausted.
5. Exhaust count and elapsed budgets independently and verify escalation retains every attempt.
6. Alternate pass and fail under unchanged conditions and confirm the result is quarantined rather than last-write-wins.
7. Restore the dependency and verify recovery does not auto-accept decisions left missing or stale during outage.
8. Recompute claim coverage and confirm retries do not inflate the denominator or numerator.
9. Inspect fairness so low-volume high-consequence reconciliation is not starved by bulk optional work.

A growing backlog can indicate insufficient capacity, but it can also reveal overbroad release scope, unstable claims, excessive evidence requirements, or unresolved ownership. Diagnose which decision load should exist before making the queue drain faster.

## Observability Checklist

Observe enough to reconstruct a decision and diagnose a failure without retaining every transcript or sensitive payload. An independent reviewer should be able to answer:

- Which claim revision and accepted need were evaluated?
- Which source, implementation, built artifact, and environment were in scope?
- Which evidence was required, attempted, skipped, denied, failed, passed, or superseded?
- Which exception and compensating control changed the decision boundary?
- Who made the disposition under which authority?
- Which release candidate consumed that disposition?
- Which later event invalidated, renewed, or superseded it?

**Minimal event envelope**

| Field | Purpose | Constraint |
|---|---|---|
| `event_id` | Deduplicate and retrieve one immutable observation | Globally unique within the retention boundary |
| `event_type` | Distinguish proposal, execution, decision, exception, release, and invalidation | Versioned controlled vocabulary |
| `schema_version` | Decode historical meaning | Never infer current semantics for an older event |
| `recorded_at` | Support operations and retention | Do not use wall-clock order as sole causality |
| `caused_by` | Connect the event to prior events or state changes | Preserve multiple causes where needed |
| `claim_id` and `claim_revision` | Bind semantic behavior | Required for claim-dependent authority |
| `change_id` | Group one proposed change across artifacts | Immutable after creation |
| `source_revision` | Identify the evaluated source state | Use digest or version, not branch label alone |
| `artifact_digest` | Identify the executable or review artifact | Required for run and release joins |
| `environment_id` | Bound the observation context | Version configuration relevant to the claim |
| `evidence_requirement_id` | State what this observation was intended to show | Separate intent from actual result |
| `attempt_id` | Preserve retries, shards, and cancellations | Never overwrite earlier attempt state |
| `state` | Record passed, failed, missing, unknown, denied, inaccessible, cancelled, conditional, or superseded | Validate transitions and projections |
| `actor_role` and `authority_scope` | Distinguish observation from decision rights | Required for dispositions and exceptions |
| `evidence_key` | Retrieve detailed retained evidence | Include integrity identity and access classification |
| `release_candidate_id` | Bind release reconciliation | Immutable candidate identity |
| `reason_code` | Support consistent routing and metrics | Keep free-form explanation separately |
| `correlation_id` | Connect distributed work for diagnosis | Must not replace semantic identities |

Human review is evidence too. Record the question asked, artifact revision shown, reviewer role, observed conclusion, limitations, and time boundary. Do not record private reasoning transcripts when the decision and rationale can be captured directly.

**Choose the signal for the question**

| Signal | Best use | Required link | Common misuse |
|---|---|---|---|
| Lifecycle event | Authoritative state transition and audit reconstruction | Claim, artifact, actor, and prior state | Logging a state without validating authority |
| Metric | Population health, capacity, and trend | Definition version plus drill-down event or exemplar | Treating an aggregate as claim-level release authority |
| Trace | Latency and dependency path for one distributed operation | Correlation plus decision-unit identities | Assuming sampled success proves every claim run |
| Diagnostic log | Error detail and local investigation | Attempt and artifact identity | Using mutable text as the only audit record |
| Evidence artifact | Full test, benchmark, review, or attestation support | Content digest, schema, access, and retention | Linking a transient workspace path |
| Generated projection | Reviewer-specific matrix, report, or dashboard | Authoritative source version | Hand-editing the projection into a second truth |
| Journal checkpoint | Human handoff, phase, blocker, and next action | Exact paths, revisions, and current test evidence | Replacing artifact evidence with progress prose |

Do not duplicate one fact manually across all signals. Emit one authoritative transition, derive metrics and projections, and link detailed diagnostics by immutable identity.

**Illustrative event timeline**

```json
{"event_id":"evt-101","event_type":"claim-revised","schema_version":1,"claim_id":"AUTH-SESSION-017","claim_revision":3,"change_id":"AUTH-CHANGE-042","state":"proposed"}
{"event_id":"evt-102","event_type":"evidence-required","schema_version":1,"claim_id":"AUTH-SESSION-017","claim_revision":3,"evidence_requirement_id":"auth-session-integration","state":"missing","caused_by":["evt-101"]}
{"event_id":"evt-103","event_type":"evidence-attempted","schema_version":1,"claim_id":"AUTH-SESSION-017","claim_revision":3,"artifact_digest":"build-auth-20260711-042-mutation-disable-revocation","environment_id":"isolated-integration","evidence_requirement_id":"auth-session-integration","attempt_id":"attempt-1","state":"failed","reason_code":"mutation-detected","caused_by":["evt-102"]}
{"event_id":"evt-104","event_type":"evidence-attempted","schema_version":1,"claim_id":"AUTH-SESSION-017","claim_revision":3,"artifact_digest":"build-auth-20260711-042","environment_id":"isolated-integration","evidence_requirement_id":"auth-session-integration","attempt_id":"attempt-2","state":"passed","evidence_key":"run-auth-session-042","caused_by":["evt-102","evt-103"]}
{"event_id":"evt-105","event_type":"claim-decided","schema_version":1,"claim_id":"AUTH-SESSION-017","claim_revision":3,"artifact_digest":"build-auth-20260711-042","actor_role":"identity-service-owner","authority_scope":"authentication-behavior-acceptance","state":"accepted","caused_by":["evt-103","evt-104"]}
{"event_id":"evt-106","event_type":"release-reconciled","schema_version":1,"claim_id":"AUTH-SESSION-017","claim_revision":3,"artifact_digest":"build-auth-20260711-042","release_candidate_id":"identity-service-candidate-20260711-042","state":"accepted","caused_by":["evt-105"]}
```

The failed event is not erased by the pass. Here it records that a distinct controlled-mutation artifact was detected in the same isolated environment, while the normal candidate passed. A real behavior failure in the normal candidate would require a new artifact or explicit disposition before a later pass could grant authority. Event meaning comes from type, reason, identity, and causal relationship, not color alone.

**Capture checklist**

**Source and semantics**

- Record archive, local policy, external guidance, and inference roles separately.
- Record which candidate sources were not retrieved and why.
- Bind every claim revision to its accepted authority and supersession lineage.
- Capture unresolved disagreement without choosing a winner by write order.

**Evidence execution**

- Record exact command or reviewer question, tool version, relevant configuration, artifact digest, environment, and attempt state.
- Preserve expected negative observations and distinguish them from infrastructure failure.
- Retain skipped, cancelled, denied, inaccessible, flaky, and superseded states.
- Summarize output for review, but link to durable raw evidence where the decision needs it.

**Decision and release**

- Record accepted, rejected, conditional, and superseded dispositions with actor authority and rationale.
- Capture exception scope, compensating control, enforcement result, owner, and expiry events.
- Record the exact candidate and claim population considered by release reconciliation.
- Emit invalidation events when claim, artifact, environment, runner, dependency, authority, or evidence availability changes.

**Privacy, integrity, and access**

- Avoid secrets, credentials, personal data, source payloads, and restricted evidence in labels or general logs.
- Use stable opaque identities for high-cardinality claim, run, and artifact values; keep them out of uncontrolled metric labels.
- Classify evidence access and record denial without exposing protected content.
- Protect decision and audit events from silent mutation; retain integrity digests and authorized correction events.
- Define retention by decision consequence and recovery need, then test deletion and legal-hold behavior where applicable.
- Record telemetry delivery loss, exporter backlog, sampling, and dropped-event counts.

**Measurement conditions**

Record latency percentiles only when a real question, comparable population, and method exist. Define start and end events, success and failure inclusion, concurrency, warm-up, sampling, aggregation, and observation window. Reviewer time and runtime latency are different populations. With sparse observations, report cases and ranges rather than implying stable tail behavior.

Metrics should include definition version and link to event exemplars. High-cardinality identities belong in events, traces, or indexed logs rather than unbounded metric dimensions.

**Verification**

1. Contract-test every producer and consumer against versioned event fixtures.
2. Inject duplicate, reordered, delayed, denied, corrupt, stale, missing, and superseded events.
3. Deliberately drop one required transition and verify closure detects the absence.
4. Replay a claim from proposal through release and compare the derived state with raw records.
5. Restore retained events and evidence in an isolated environment and reconstruct an older decision.
6. Test redaction and access roles with representative sensitive payloads outside production.
7. Generate load with representative cardinality and verify exporters report loss before buffers overflow.
8. Recompute dashboard measures independently and compare them with source events.
9. Sample a green release and prove that claim, artifact, evidence, authority, exception, and candidate identities all join.
10. Change an event schema and verify old and new readers preserve or explicitly reject meaning.

For a file-only workflow, version control, structured records, CI artifacts, and a progress journal can satisfy these semantics. A distributed platform may use event storage, metrics, traces, and protected evidence services. The architecture differs; the reconstruction questions and state fidelity do not.

Observability itself becomes part of the delivery control plane when missing or distorted telemetry can authorize, block, or reconstruct a release. Trace only the telemetry components whose failure can alter consequential decision state: producer version, exporter delivery, schema interpretation, derived metric, evidence retention, and required review access.

## Performance Verification Method

Separate two performance questions:

1. **Domain quality claim:** does the software under test meet an accepted latency, throughput, capacity, resource, or reliability objective for a defined workload?
2. **Traceability workflow performance:** can authors, reviewers, gates, and release systems build and query the evidence graph within acceptable cost while preserving decision integrity?

A requirement-to-test mapping percentage answers neither question. Claims may require benchmarks, deployment observations, policy review, or human evidence, and a link can exist without semantic fit.

**Domain quality-claim contract**

Before measuring a domain claim, record:

| Dimension | Required decision |
|---|---|
| Accepted objective | Value, unit, statistic, comparison rule, owner, and consequence |
| Workload | Population, request or operation mix, data distribution, result sizes, and error cases |
| Boundary | Exact start and end events plus included setup, queue, retry, and dependency time |
| Environment | Hardware, operating system, runtime, dependencies, network, configuration, and concurrency |
| Artifact | Immutable source and build identities |
| State | Cold, warm, cache policy, initialization, and background load |
| Method | Harness, timer, profiler, sampling, run order, repetition, and outlier policy |
| Correctness | Behavior and result-set checks that must remain unchanged during measurement |
| Evidence | Raw samples, summaries, logs, profiles, environment manifest, and integrity identity |
| Decision | Baseline, candidate comparison, uncertainty, owner, disposition, and invalidation trigger |

Do not invent a target to complete the form. If no owner has accepted an objective, measure a baseline or remove the quantitative claim.

**Traceability workload fixtures**

| Fixture | Shape | Operations to exercise | Failure it reveals |
|---|---|---|---|
| Compact change | Few claims, sparse edges, short history, one candidate | Parse, validate, generate review view, reconcile | Fixed startup and authoring overhead |
| Dense interaction | Many claim-to-case and cross-claim edges | Impact traversal, missing-link query, semantic projection | Relationship-density and fan-out cost |
| Long history | Many superseded revisions, attempts, decisions, and schema versions | Current-state query, historical replay, retention retrieval | History pollution and decoder cost |
| High churn | Frequent claim and artifact revisions | Invalidation propagation, cancellation, regeneration | Stale-work amplification |
| Multi-environment | Evidence across platforms and configurations | Coverage, missing-state, exception, and release queries | Combination growth and hidden unknowns |
| Concurrent release | Several candidates and workers share dependencies | Identity isolation, queue fairness, reconciliation | Cross-candidate contamination and contention |
| Restricted evidence | Mixed access classes and routed reviews | Retrieval, authorization, attestation, audit | Permission latency and accidental data copying |
| Migration | Old and new schemas plus generated projections | Convert, dual-read, compare, regenerate, restore | Compatibility and partial-conversion cost |

Build fixtures from observed target distributions where possible. Synthetic data should preserve degree distribution, version history, state mix, artifact sizes, and access behavior relevant to the claim. State clearly where it differs from production.

**Method selection**

| Method | Use for | Strength | Blind spot |
|---|---|---|---|
| Microbenchmark | Parser rule, graph operation, serializer, digest, or projection kernel | Isolates mechanism and supports profiling | Omits coordination, storage, network, and reviewer behavior |
| Component benchmark | Graph service, evidence store, generator, or validator | Includes realistic local dependencies | May not represent end-to-end release flow |
| End-to-end benchmark | Author-to-decision or change-to-release workflow | Measures coordination and integration | Harder to diagnose and control |
| Load and saturation test | Concurrent queries, runs, writes, or generation | Reveals queueing, limits, and degraded behavior | Synthetic arrival patterns can mislead |
| Production replay | Representative recorded workload against isolated candidate | High shape realism | Privacy, drift, and side-effect control require care |
| Profile | CPU, allocation, I/O, lock, queue, and network cost | Locates optimization opportunity | Does not establish user or decision impact alone |
| Reviewer study | Navigation, comprehension, decision time, and error | Measures human workflow | Task equivalence, learning, and small samples limit inference |

Choose the least expensive method capable of observing the stated claim. Use profiles to select changes, then verify the outcome at the decision boundary.

**Benchmark protocol**

1. **Accept the question.** Name the decision, objective or comparison, owner, and consequence.
2. **Freeze identities.** Record claim revision, source revision, built artifact, harness, fixture, environment, and configuration digests.
3. **Validate fixture answers.** Run structural and semantic checks so the benchmark cannot become faster by dropping claims, edges, evidence states, or release obligations.
4. **Calibrate measurement.** Measure timer and instrumentation overhead, resolution, clock behavior, and resource collector effects.
5. **Separate states.** Measure cold and warm behavior intentionally; report cache population and startup rather than mixing them silently.
6. **Control order.** Interleave baseline and candidate where feasible, randomize run order, and monitor background load and thermal or resource drift.
7. **Exercise failure.** Inject a known delay, graph expansion, evidence loss, or queue pressure and confirm the measured boundary changes as expected.
8. **Retain raw data.** Store per-operation samples, failures, retries, environment observations, and profiles by integrity identity.
9. **Compare with uncertainty.** Report distributions and effect size appropriate to the population; avoid a pass from one favorable run.
10. **Recheck correctness.** Compare result sets, missing states, transition validity, and release decisions before accepting a speedup.
11. **Review tradeoff.** Include resource use, false blocks, stale results, operational complexity, and recovery cost.
12. **Bind disposition.** Record which artifact and workload the result supports and what change invalidates it.

**Validity checks**

- Include queue and retry time if users or releases experience it; excluding it can create coordinated omission.
- Count errors, timeouts, cancellations, and unavailable evidence in the population rather than timing only successes.
- Ensure load generators continue issuing work according to the intended arrival model when the system slows.
- Report throughput and latency together near saturation; either alone can conceal overload.
- Track CPU, memory, allocation, storage, network, lock, queue, and evidence-retention cost relevant to the mechanism.
- Use representative skew. Uniform claims and edges may hide high-fan-out invalidation and hot owners.
- Keep warm-up explicit and do not compare a warm candidate with a cold baseline.
- Treat retries as attempts within one decision operation; do not report the fastest successful attempt as end-to-end latency.
- Investigate multimodal results instead of compressing them into one average.
- Use tail percentiles only with a defined population and enough observations for the estimate to be meaningful; otherwise report raw cases, ranges, or ordered samples.
- For reviewer studies, hold task consequence and complexity as comparable as possible, capture decision correctness and rework, and report learning or ordering effects.
- Distinguish exploratory local timing from release evidence.

**Correctness-under-load gates**

Performance evidence is invalid if the optimized system:

- omits active claims, required edges, missing states, or exceptions;
- serves a projection from the wrong graph version;
- allows one candidate's evidence to authorize another;
- collapses denied, inaccessible, failed, or superseded states into success;
- drops audit events without an observable loss signal;
- evicts evidence still required for active or retained decisions;
- changes decision results relative to the validated baseline without an accepted semantic revision;
- starves high-consequence reconciliation behind optional bulk work;
- produces output that cannot be reconstructed after restore.

These gates keep caching, compaction, denormalization, sampling, and partitioning from buying speed by weakening traceability meaning.

**Worked benchmark interpretations**

**Good:** a candidate index is tested on compact, dense, and long-history graphs. Claim-to-release result sets match the baseline, stale projections are rejected, raw samples and profiles are retained, and the accountable owner accepts the observed improvement for the defined environment.

**Bad:** an empty graph is queried repeatedly after cache warm-up. The fastest result is reported as tail latency, no errors are included, and the optimized query silently excludes superseded-state validation. This does not support a target objective.

**Borderline:** a representative dense fixture shows a large consistent slowdown on shared CI while correctness remains intact. Background noise prevents a narrow threshold decision, but the evidence is sufficient to trigger profiling and a controlled benchmark. Preserve it as diagnostic evidence, not final release authority.

No latency, throughput, memory, capacity, or reviewer-time result is asserted by this reference. Establish local objectives from representative baselines and consequence. The total performance budget includes false blocks, stale authority, retry amplification, evidence retention, reviewer rework, and recovery effort as well as CPU time and query latency.

## Scale Boundary Statement

This reference defines semantics and decision controls; it is not a universal storage, governance, or distributed-systems blueprint. Multiple owners or services do not automatically make it inapplicable. The boundary is crossed when the chosen implementation can no longer preserve identity, state, evidence, authority, access, release closure, or recovery at the required workload and consequence.

**Three applicability zones**

| Zone | Conditions | Use of this reference | Additional action |
|---|---|---|---|
| Direct | One coherent behavior boundary; reviewable graph; compatible evidence lifecycle; bounded source discovery; one release decision | Apply the artifact, graph, evidence, and decision guidance directly | Use repository-native files, CI, and durable evidence if they satisfy invariants |
| Coordinated | Several services, repositories, owners, environments, or access classes share a change or release | Keep these semantics, partition authoring and evidence collection, and preserve global identities and typed contracts | Add federation, aggregate release reconciliation, compatibility, access routing, and recovery tests |
| Specialist | Legal interpretation, safety case, regulated records, enterprise identity, high-scale platform design, or operational objectives exceed this reference's authority | Use this reference as an input vocabulary and traceability responsibility map | Route architecture and policy to accountable domain, security, compliance, reliability, data, or platform owners |

Unaccepted product semantics also stop progress, regardless of scale. Traceability cannot manufacture authority for the behavior it links.

**Direct-use coherence test**

Direct use remains suitable when:

- claims serve one accepted user or operational outcome;
- interactions are comprehensible in one review view;
- authoritative owners and specialist reviewers are named;
- the claims share or explicitly coordinate release fate;
- evidence stores and access rules support required reviewers;
- invalidation can identify affected evidence and decisions predictably;
- historical records can be interpreted for the required retention period;
- verification and recovery fit the current repository or workflow mechanisms.

Physical colocation is neither necessary nor sufficient. A multi-service password-reset transaction can remain one coherent decision model while each service owns local evidence. One monorepo can contain unrelated domains, incompatible authorities, and restricted evidence that should be separated.

**Scale pressure and transition signals**

| Signal | Why the current mechanism is insufficient | Next design question |
|---|---|---|
| Local identity collisions or ambiguous revisions | Independent producers cannot join artifacts safely | Which global namespace and supersession contract are shared? |
| Schema versions drift across producers | The same field or state no longer has one meaning | How are compatibility, migration, and historical readers governed? |
| Cross-unit interactions disappear from review | Partitioning hides transaction or concurrency behavior | Which parent claims and aggregate cases preserve coupling? |
| Manual release reconciliation becomes error-prone | Local green states do not close one candidate decision | What generated global view and accountable release authority are required? |
| Evidence access blocks required reviewers | Centralization or copying violates least privilege | Which routed reviews or attestations preserve proof without payload exposure? |
| Change fan-out causes broad stale evidence | Invalidation and rerun scope exceed delivery window | How should volatile domains, caches, and impact indexing be partitioned? |
| Current queries are fast but historical recovery fails | Optimization removed interpretation or lineage | Which retention tier and versioned decoder restore reconstruction? |
| Gate or evidence service outage blocks unrelated work | Shared control-plane dependency is too broad | Which capabilities can degrade, isolate, or fail independently? |
| Reviewers repeatedly miss obligations | Human comprehension, not storage, is saturated | Which decision boundaries and generated views should narrow scope? |
| Unbounded source discovery continues during delivery | Authority and currentness cannot close | Which source owner and retrieval budget define a stop condition? |
| Specialized policy determines acceptance | Engineering guidance lacks decision authority | Which domain owner and formal process must lead? |

No universal system count, owner count, graph size, traffic level, or latency threshold is supported here. Calibrate transitions from observed errors, delay, query and generation behavior, review reconstruction, incident recovery, and accepted objectives.

**Architecture choices beyond direct use**

| Model | Strength | Main tradeoff | Required invariant |
|---|---|---|---|
| Repository-native records | Low infrastructure and strong code proximity | Cross-repository joins, access, and retention are manual or generated | Immutable global identities and candidate binding |
| Central graph and evidence index | Simple global traversal and release closure | Shared availability, access, governance, and migration dependency | Domain authority remains explicit; central storage does not imply decision rights |
| Federated graphs with shared contracts | Local autonomy and evidence ownership | Compatibility, discovery, and partial availability become complex | Versioned identity, state, link, and reconciliation protocol |
| Append-only event model | Strong transition history and replay | Projection correctness and event migration require discipline | Idempotent events, causal identity, and versioned interpretation |
| Hybrid index with local evidence | Global metadata and closure without centralizing protected payloads | Retrieval and attestation paths can fail independently | Integrity-bound references and permission-aware state |

The durable default at organizational scale is often **federated evidence with narrowly shared identity, state, and reconciliation contracts**. Centralize only what requires global agreement. Keep domain execution, detailed evidence, and specialist authority with their owners where possible.

**Cross-boundary contract**

Every independently owned unit should publish or expose:

```text
Namespace and claim revision rules
Supported event and graph schema versions
Typed outgoing and incoming relationships
Artifact and evidence integrity identities
State vocabulary and invalid transition behavior
Authority and exception boundaries
Access and attestation behavior
Invalidation and supersession events
Release-candidate participation
Retention and historical interpretation support
Degraded-mode and recovery contract
```

One aggregate release owner or explicitly coordinated decision protocol must reconcile cross-unit claims. Local acceptance cannot silently grant global transaction acceptance.

**Multi-agent and long-running execution**

- Assign exclusive mutable ownership by exact file, packet, graph partition, or evidence unit.
- Complete and save atomic work before another owner consumes it.
- Preserve the governing specification, source identities, exact heading order, tests, blockers, and next action in durable checkpoints.
- Re-read current artifacts at phase transitions and after interruption; context summaries do not override filesystem state.
- Prevent parallel agents from creating competing active revisions for the same identity.
- Merge through semantic and evidence checks, not text concatenation alone.
- Keep one accountable verifier for each aggregate release or reference, while allowing independent evidence owners.
- Cancel work when the source or claim revision it serves is superseded.

Exclusive file ownership prevents write collision. It does not prevent semantic split brain: two files can be internally valid while assigning different meaning to one state or requirement. Shared compatibility fixtures must cover those contracts.

**Scale verification**

1. Generate independent units with deliberate identity collisions and confirm quarantine.
2. Run old and new schema producers concurrently and verify compatible joins or explicit rejection.
3. Change one cross-unit interaction claim and confirm invalidation reaches every dependent evidence and release view.
4. Partition one service or evidence store and verify the declared block, narrow-release, or degraded-review behavior.
5. Exercise access denial and routed attestation without copying restricted evidence into a global log.
6. Reconcile several concurrent candidates and prove no run or exception crosses artifact identity.
7. Restore historical units under versioned readers and reconstruct an aggregate decision.
8. Compare direct and partitioned models for graph correctness, reviewer comprehension, reconciliation effort, and recovery.
9. Sample real cross-owner decisions to expose authority delay and vocabulary mismatch that synthetic load cannot model.
10. Migrate one unit and retire its old protocol only after consumer and historical-read evidence closes.

**Zone examples**

**Direct:** one repository owns a local parser change, its claims, focused tests, current run, and one package release. Repository-native traceability is sufficient if evidence is durable and identities are exact.

**Coordinated:** order cancellation crosses order, fulfillment, and payment services. Each service owns implementation evidence; a shared transaction claim, stable IDs, partial-failure probes, and aggregate release reconciliation preserve the end-to-end decision.

**Bad split:** each repository invents its own claim IDs and reports a local green release. The transaction has no parent interaction claim, shared candidate identity, or accountable aggregate decision. More files reduced local context while removing global meaning.

**Borderline:** stable federated IDs and schemas exist, but aggregate release is assembled manually. Low frequency and consequence may make that acceptable temporarily. Instrument errors and delay, rehearse recovery, and define the trigger for generated reconciliation rather than centralizing automatically.

Scaling the mechanism creates organizational infrastructure. Identity, state, and schema contracts affect team autonomy; a central gate can become a delivery bottleneck and outage dependency. Prefer the smallest shared control surface that preserves global decision integrity, and retain local ownership everywhere global agreement is unnecessary.

## Future Refresh Search Queries

No web search was performed during this evolution. Every external query and URL below is an **unexecuted retrieval target**, not current evidence or a paraphrase of present external guidance.

Refresh in this order:

1. Inspect target repository policy, schemas, code, tests, workflows, and observed behavior.
2. Verify frozen local source identity and compare repository history for changed adaptations.
3. Retrieve a known primary external URL for the exact unresolved mechanism.
4. Search an official domain when the authoritative path or vocabulary is unknown.
5. Use issue reports or examples to generate failure hypotheses, then reproduce them locally.
6. Let an accountable target owner accept, adapt, reject, or defer the external change.

Search ranking, repository popularity, and repeated mirrors do not establish authority.

**Refresh triggers**

| Trigger | Question to resolve | Consumer impact to inspect |
|---|---|---|
| Local policy or schema revision | Which identity, state, link, exception, or release semantics changed? | Parsers, graphs, generators, historical readers, gates, and decisions |
| CI or evidence tool release | Did run identity, permissions, status, artifact, retention, cancellation, or cache behavior change? | Evidence collection, retrieval, retry, and release reconciliation |
| Broken or redirected source URL | Where is current primary authority, and was content superseded? | External claim status and refresh schedule |
| Contradiction between reference and observed target behavior | Is the reference stale, target misconfigured, or boundary different? | Current guidance, tests, examples, and failure modes |
| Incident or review reversal | Which assumption or control failed, and is there current official guidance? | Regression fixtures, priorities, exception rules, and recovery |
| New language, runner, or release surface | Which mechanisms are target-specific while semantics remain stable? | Templates, adapters, commands, and compatibility |
| Approaching retention or deprecation boundary | What history and consumers still require the mechanism? | Evidence recovery, migration, and retirement |
| Scheduled high-consequence review | Have quiet upstream changes invalidated a consequential dependency? | Security, compliance, release, and operational controls |

**Targeted query catalog**

| Query intent | Future query text | Preferred source | Evidence expected before adoption |
|---|---|---|---|
| Codex instruction discovery | `site:developers.openai.com/codex AGENTS.md discovery scope precedence nested instructions` | Current OpenAI Codex documentation | Direct page, retrieval date, applicable product version, bounded paraphrase, and target repository behavior |
| Codex instruction conflict | `site:developers.openai.com/codex AGENTS.md conflicting instructions precedence repository` | Current OpenAI Codex documentation | Explicit current rule plus a target fixture for nested and conflicting instructions |
| GitHub Actions run states | `site:docs.github.com/actions workflow run conclusions skipped cancelled failure success permissions` | Current GitHub Actions documentation | Exact state semantics and observed known-pass, known-fail, skip, cancellation, and permission cases |
| GitHub Actions artifact identity | `site:docs.github.com/actions artifact retention digest attestation workflow run identity` | Current GitHub Actions documentation | Current feature pages, retention and integrity boundary, and target retrieval test |
| GitHub Actions cache boundary | `site:docs.github.com/actions cache key restore stale workflow evidence` | Current GitHub Actions documentation | Current cache semantics and a target stale-cache rejection probe |
| Agent instruction format | `site:agents.md specification scope precedence version` | Current primary format site | Versioned format claims and observed compatibility with selected tools |
| Repository release change | `site:github.com release notes traceability schema migration evidence graph` | Maintainer-owned repository and release records after a product is selected | Tagged release, migration notes, affected target version, and local compatibility result |
| Assertion sensitivity | `mutation testing assertion sensitivity equivalent mutants official documentation` | Primary documentation for a tool discovered through the query and then adopted locally | Current mechanism and a local mutation that changes the expected assertion |
| Evidence retention | `CI artifact retention integrity access deletion restore official documentation` | Product-owned documentation discovered for the target CI and evidence store | Retention, access, integrity, deletion behavior, and target restore evidence |
| Traceability interoperability | `requirements traceability identity revision evidence schema official standard` | Current standard or product authority retrieved and accepted by the target owner | Version, normative scope, compatibility mapping, and rejected differences |

The final three are broad authority-discovery queries because no target mutation tool, evidence store, or interoperability standard was selected. Treat every result as a candidate locator until its primary owner, version, scope, and local applicability are verified.

**Local refresh queries**

Use repository evidence before broad external search:

```bash
shasum -a 256 agents-used-monthly-archive/idiomatic-references-202606/generated-references/executable_traceability_template_patterns.md
git log -- idiomatic-ref-202607/executable_traceability_template_patterns-20260710.md
git log -S 'Traceability Change Record' -- idiomatic-ref-202607
rg -n 'claim_revision|artifact_digest|evidence_requirement|release_candidate' .
rg -n 'skipped|cancelled|inaccessible|superseded|exception' .github tests docs
```

Adapt paths to the target repository. A search hit is a candidate observation; inspect context, ownership, current version, and executed behavior before promoting it.

**Refresh evidence record**

```text
Refresh trigger and affected claim
Query or direct locator used
Source owner and authority class
Retrieval date, version, and content digest where permitted
Exact supported point and bounded paraphrase
Unsupported or ambiguous point
Duplicate, mirror, redirect, or deprecation status
Target policy and behavior inspected
Compatibility or contradiction result
Accepted, adapted, rejected, deferred, or no-change disposition
Accountable owner and rationale
Affected references, generators, gates, evidence, and decisions
Next trigger and review boundary
```

**Result validation and disposition**

1. Open the primary page rather than relying on a search snippet.
2. Confirm owner, publication or version boundary, and whether the page is normative, explanatory, or an example.
3. Record only the claim the source directly supports; do not extend it to requirement semantics or release authority.
4. Compare with previous captured source and explain meaningful differences.
5. Test the selected mechanism in the target repository, including negative, skipped, cancellation, permission, stale, and migration cases as applicable.
6. Preserve conflicts between external guidance, local policy, and observed behavior.
7. Have the correct target owner decide applicability.
8. Invalidate or migrate generated references and decisions that consumed a changed claim.
9. Record `no-change` when the source and target comparison support retaining current guidance.

**Good:** a CI artifact-retention concern triggers retrieval of the exact current product page, a target expiry and restore fixture, and a local decision about evidence retention. **Bad:** a broad "best practices" result is copied into a release gate because several blogs repeat it. **Borderline:** a maintainer issue reports an integrity failure without a reproducible case; retain it as a test hypothesis and do not claim the failure applies locally until reproduced or confirmed by authority.

Version query intents as concerns and terminology evolve. Monitor known high-consequence locators, but avoid continuous broad searches that generate noise without a decision consumer. Retire a query when its mechanism is removed, its source is superseded, or no maintained local guidance depends on it.

## Evidence Boundary Notes

Evidence role determines what a statement may authorize. Provenance alone does not establish current applicability, and repeated generation does not promote a synthesis into target policy.

**Controlled evidence roles**

| Role | Assignment test | Permitted use | Required caution |
|---|---|---|---|
| Historical local fact | Directly observable in a frozen local source with identity | Describe what the source contains or omitted at capture time | Does not establish current target policy or outcome |
| Current target fact | Directly observed in the target code, schema, workflow, run, or environment | Describe bounded current behavior | Bind revision, artifact, environment, and observation time |
| Accepted target policy | Explicitly adopted by an accountable target owner under current authority | Control behavior, evidence, or release inside stated scope | Record version, exceptions, and invalidation trigger |
| Current external source | Retrieved from a primary owner-controlled source and reviewed for applicable version | Support claims about that external mechanism | Record date, locator, bounded support, and target compatibility |
| Synthesis | Reasoned guidance combining observations, failure analysis, and engineering judgment | Propose a default, alternative, test, or design question | Label assumptions and verify before consequential adoption |
| Illustration | Concrete invented example used to teach artifact shape or reasoning | Demonstrate how a record or gate could work | Values, identities, roles, and technologies are not target facts |
| Hypothesis | Plausible claim awaiting evidence | Drive discovery, experiment, or review | Grants no release or policy authority |
| Conflict | Sources, target observations, or authorities disagree | Preserve uncertainty and route a decision | Do not select by recency or rank without applicability review |
| Unknown | Required fact was not retrieved, observed, or interpretable | Keep a decision open or bounded | Never convert to passed or absent silently |
| Negative evidence | A failure, omission, contradiction, or mutation demonstrates a limitation | Reject an overclaim and create a regression fixture | Omission alone does not prove the proposed replacement is correct |

**Evidence ledger for this evolution**

| Claim group | Evidence available | Confidence and boundary |
|---|---|---|
| Archive seed identity | The working seed and archive seed were byte-identical at baseline with SHA-256 `2a0876253a67e3317cbcaca095c6fc3d16bc5f52a3700293a2b113add4a74454` | High confidence local fact for the baseline only |
| Historical template source | Three local 118-line template paths were byte-identical with SHA-256 `c7e44220936452079080a46fb23725ec5b3332fb8b1a8a082eaeed76b2bd2812` | One source with three locators, not three independent authorities |
| Historical content | The source contains a requirement shape, traceability matrix, development sequence, Rust, TypeScript, and Go skeletons, vague-to-measurable rewrites, and a quality gate | High confidence description of local historical content; no target adoption implied |
| Source limitations | The local template includes unresolved authoring syntax, illustrative quality values, and a checklist whose test-link language does not cover every evidence class | Direct source observation plus bounded critique; replacement guidance remains synthesis |
| Public URLs | Codex instruction guidance, the GitHub Actions documentation root, and the agents.md format location were inherited as future source families | Path strings are local facts; present external contents, versions, and recommendations are unknown because no browsing occurred |
| Local adjacent filenames | Candidate reference paths in the July directory were observed by filename | Path existence supports navigation only; content completeness and compatibility were not reviewed here |
| Traceability Change Record | Revision, claim, case, implementation, run, exception, release, and invalidation fields are synthesized from identified lifecycle failure modes | Reasoned reference model, not a discovered standard or adopted target schema |
| State and graph invariants | Identity collision, stale revision, state collapse, evidence mismatch, and candidate mismatch are plausible failure mechanisms with proposed probes | Strong engineering synthesis; target frequency and control effectiveness are unmeasured |
| Worked records | Session revocation, cancellation, performance, and migration examples use invented identities and values | Illustrations only; replace every domain decision with accepted target facts |
| Reliability, performance, and scale | The reference defines methods, dimensions, hazards, and objective contracts | No target latency, throughput, availability, capacity, retry, retention, or reviewer-time result was measured |
| External refresh queries | Query intents and direct source paths are specified for future work | Unexecuted retrieval plans, not external evidence |
| Evolved artifact checks | Structure, uniqueness, heading, expansion, hygiene, table, fence, and test verifiers can establish properties of these files | They do not prove that the guidance improves an unseen production system |

**Claim-record profile**

For consequential guidance, retain:

```text
Claim identity and exact text
Evidence role and confidence
Source owner, locator, revision, and content digest
Bounded observation or paraphrase
Target boundary and authority
Assumptions and counterevidence sought
Verification performed and observed result
Accepted, adapted, rejected, unresolved, or superseded disposition
Consumers: templates, gates, generators, decisions, and releases
Invalidation, refresh, and retirement trigger
```

Orientation-only prose can use a compact role label and source map. Increase record depth when a claim is generated, shared, audited, release-blocking, costly to reverse, or retained across tool and schema versions.

**Boundary rules**

1. A local source fact supports only what the identified span or paraphrase actually says.
2. A historical source does not become current policy because several duplicate paths contain it.
3. A public URL does not support a current claim until its content is retrieved and reviewed.
4. A primary external source can explain its mechanism but cannot decide a target product requirement.
5. A test pass supports only the claim, artifact, environment, and assertion boundary it observed.
6. A release decision requires target authority; documentation and generated matrices do not grant it.
7. A source omission may expose a risk but does not prove one proposed architecture is the solution.
8. A concrete sample value remains illustrative until accepted and measured locally.
9. Mixed-role paragraphs should be split when confidence, consequence, or refresh behavior differs.
10. Unknown, denied, inaccessible, stale, and conflicting evidence remain explicit states.

**Examples of boundary handling**

**Good historical fact:** "The archived template contains a traceability matrix with one sample requirement linked to several evidence levels." This is directly inspectable and does not claim the matrix is sufficient.

**Bad extension:** "Therefore every target project must use that exact matrix and every requirement must map to a test." The source cannot establish target policy, and some claims require other evidence classes.

**Bounded synthesis:** "A typed evidence graph may prevent lifecycle links from disappearing when one matrix becomes dense." This identifies a plausible design response and still requires target workload and verification.

**Promoted target rule:** a target owner adopts stable claim revisions after parser, graph, migration, and release checks. Record the adoption as target policy while preserving that its original inspiration was historical. Later demotion changes target status without rewriting source provenance.

**Conflict:** current target behavior disagrees with retrieved external guidance. Preserve both observations, inspect version and configuration, and let the accountable target owner resolve applicability. Do not hide the conflict by changing the evidence label.

**Verification and lifecycle**

- Hash frozen local sources and compare expected identities before reuse.
- Map consequential claims to bounded source support or explicit synthesis records.
- Retrieve primary external pages directly, respecting permitted quotation and archival limits.
- Compare external version and target behavior; do not stop at source retrieval.
- Search for counterexamples and contradictory policy before promotion.
- Run target parser, graph, mutation, evidence, exception, and release checks appropriate to the claim.
- Detect when cited support no longer matches claim text after edits.
- On source or target change, traverse consumers and reopen only affected decisions.
- Preserve historical evidence roles and record promotion, demotion, supersession, and retirement as events.
- Generate reader-friendly provenance tables from one authoritative claim record where tooling exists.

Confidence in this evolved reference comes from explicit assumptions, counterarguments, verification design, and local structural checks. It is not empirical proof that every recommendation improves a target system. The operational value of provenance is its ability to answer both "why is this guidance here" and "which consumers must reopen if its evidence is wrong."
