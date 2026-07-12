# Executable Metapattern Reference Digest

This digest helps an implementation agent or technical lead decide **how to turn an ambiguous but actionable engineering request into source-bound obligations, executable checks, and a recoverable handoff**. It is not a product-discovery substitute, a universal architecture method, a debugging diagnosis, or evidence that a proposed performance target is achievable. Its job begins when the user goal and decision owner can be stated; unresolved choices remain explicit rather than being guessed into a formal-looking contract.

The governing question is:

> What must be true, under which conditions, how could it fail, who can accept it, and what observation would prove or refute it before implementation is called complete?

**Default evidence-to-decision pipeline**

| stage | required input | output | rejection or route signal |
| --- | --- | --- | --- |
| Clarify | User outcome, actors, system boundary, non-goals, and owner. | One bounded decision plus open questions. | Product value, authority, or desired behavior is still undecided. |
| Classify evidence | Local instructions, source, tests, current templates, retained external pointers, and explicit inference. | Typed evidence ledger with freshness and scope. | A claim depends on an unread, stale, unavailable, or unsuitable source. |
| Decompose behavior | Triggers, inputs, outcomes, invariants, failures, concurrency or timing where relevant. | Small falsifiable behavior claims. | Compound behavior cannot be tested or assigned independently. |
| Author contracts | Stable requirement identifiers and condition/outcome/constraint clauses. | Executable requirements with empty, invalid, boundary, and recovery cases. | A clause uses qualitative aspiration where an observable result is needed. |
| Design verification | Project test surfaces, fixtures, negative cases, measurement method, and review questions. | Bidirectional requirement/test matrix and expected initial failures. | A requirement has no capable check, or a check merely repeats implementation internals. |
| Implement | A reviewed contract, owned change boundary, and Red evidence. | Minimal Green behavior followed by structure-preserving refactoring. | Code expands beyond the contract, hides a contradiction, or relies on an invented threshold. |
| Verify and hand off | Full relevant checks, source state, diff, reviewer evidence, and residual uncertainty. | Proceed, proceed within scope, revise contract, reject, or escalate. | The reviewer cannot reconstruct why the evidence authorizes the action. |

This order is a default, not a ceremony. A repository may already have an authoritative contract and regression test for a narrow reversible change; in that case, reuse them and record why the omitted authoring work is unnecessary. Compression is valid only when the same behavior, counterexample, traceability, and rejection semantics remain visible.

**Minimum inputs**

- A concrete user or system outcome, including who observes it.
- The repository, service, artifact, or policy boundary affected by the decision.
- Current local instructions and the strongest available behavior authority.
- Material failure cases, including invalid input and unavailable dependencies where applicable.
- The action consequence and an owner who can resolve remaining product or risk choices.
- A verification surface capable of observing the promised behavior.

**Required outputs for durable work**

| output | minimum content | what it must not imply |
| --- | --- | --- |
| Decision statement | Outcome, actor, boundary, consequence, non-goals, and unresolved choices. | That the chosen behavior was discovered automatically. |
| Evidence ledger | Source identity, evidence class, scope, freshness, conflicts, and inference. | That local prose or a public pointer proves target behavior. |
| Requirement set | Stable IDs, triggering conditions, observable outcomes, constraints, edge cases, and failure behavior. | That an identifier makes a vague clause testable. |
| Test matrix | Requirement-to-test and test-to-requirement links, test type, assertion, fixture, and expected initial failure. | That line coverage or a green suite proves the requirement is complete. |
| TDD record | Test-skeleton intent, Red reason, minimal Green change, refactoring, and final verification. | That phase labels alone demonstrate disciplined execution. |
| Quality gate | Exact commands or review checks, expected result, failure response, and limitations. | That one command is authoritative for every language, configuration, or runtime path. |
| Handoff state | Proceed state, residual uncertainty, owner, recovery, invalidation trigger, and next action. | That current acceptance remains valid after its premises change. |

**Fit and route-away guide**

| task state | use this digest? | next evidence route |
| --- | --- | --- |
| Bounded feature or defect prevention with known desired behavior | Yes; compile intent into contracts and checks. | Repository-specific implementation and tests. |
| Existing behavior must be explained before changing it | Partly; use the digest after source and runtime evidence establish the current contract. | Code navigation, build/configuration analysis, or runtime observation first. |
| Failure cause is unknown | Not as the primary method. | Systematic reproduction, hypothesis testing, instrumentation, and causal diagnosis. |
| Architecture alternatives are still being chosen | Use only to define evaluation criteria and acceptance boundaries. | Architecture decision and dependency-impact analysis. |
| Security, compliance, or authorization claim is consequential | Use for traceability, never as sole assurance. | Threat model, domain checks, negative tests, runtime/configuration evidence, and authorized owner. |
| Latency, memory, throughput, or capacity target has no baseline | Use to define a measurement contract, not a value. | Benchmark, profiling, load, or production telemetry under a frozen workload. |
| Large evolving artifact cannot be read safely in one pass | Use the current skill's measured context protocol and explicit global-review phase. | Deterministic index, complete selected sections, atomic save, and fresh hash checks. |
| Product intent or owner authority is unresolved | Stop contract promotion. | Stakeholder clarification, product discovery, policy decision, or explicit owner escalation. |

**Evidence and claim states**

Use precise states instead of one confidence score:

- `source_observed`: exact local bytes, command output, test result, or runtime fact was captured under stated identity.
- `inferred_for_design`: a recommendation follows from named premises but has not been validated as target behavior.
- `specified`: a falsifiable obligation has an owner, scope, and proposed verification route.
- `verified_for_scope`: claim-appropriate checks support the bounded action under the recorded state.
- `refuted`: a counterexample or authoritative conflict disproves the claim as written.
- `unresolved`: evidence or authority is insufficient; the next capable route is named.
- `invalidated`: a source, requirement, implementation, environment, workload, or policy premise changed.

Good use: a request to reject duplicate idempotency keys becomes a condition/outcome contract, includes concurrent and replay cases, maps to unit and integration checks, records the expected Red failure, and stops if the storage authority cannot define duplicate scope.

Bad use: a document assigns requirement IDs, repeats inherited productivity percentages, invents a latency threshold, and calls the plan executable without a workload, measurement method, negative case, or project command.

Conditional use: a one-line parser correction can reuse an existing requirement and regression fixture when both describe the exact boundary. If the change later broadens to compatibility, performance, or migration, the lightweight evidence must be promoted through the missing gates.

The digest is complete for a decision only when another reviewer can identify the intended behavior, locate its authority, falsify each material claim, reproduce the relevant checks, see what remains unknown, and know what to reopen when a premise changes. A missing input is a useful diagnostic. It must produce clarification, route-away, or explicit uncertainty, never invented certainty.

## Source Evidence Mapping Table

The map is a claim router, not a citation counter. Local byte identity establishes what a file contains; current skill text establishes present local workflow guidance; target source and tests establish program behavior; a retained URL establishes only that future research was suggested. No public page was opened while evolving this file.

**Mapped local corpus and current operational context**

| source_location_path_key | observed_identity | evidence_class | strongest legitimate use | important limit or invalidation |
| --- | --- | --- | --- | --- |
| `agents-used-monthly-archive/codex-skills-202602/executable-specs-01/references/meta-patterns-reference.md` | SHA-256 `78ead044feb402432f104e37f82578f3fad5f161a4df4bec809120cd2eea7882` | Dated archive snapshot; member of one duplicate content family. | Establish exactly what the 202602 path contains and orient the metapattern vocabulary. | It does not prove measured outcomes, current workflow mechanics, or target applicability. |
| `agents-used-monthly-archive/codex-skills-202603/executable-specs-01/references/meta-patterns-reference.md` | Same observed SHA-256 as the 202602 copy. | Dated archive snapshot and duplicate content. | Establish persistence of identical bytes at the 202603 path. | It is not an independent empirical confirmation and cannot rewrite the earlier snapshot's identity. |
| `unclassified-yet/Executable Specifications Meta Patterns Reference.md` | Same observed SHA-256 as both archive copies. | Local unclassified duplicate. | Provide a repository-local locator for the same digest content. | Its creation history, intended owner, and classification rationale are not recorded in this reference. |
| `/Users/amuldotexe/.codex/skills/executable-specs-01/references/meta-patterns-reference.md` | Same observed SHA-256 as all three mapped copies. | Current installed duplicate. | Show that the installed skill currently carries the same rationale digest. | Installation presence does not establish that a particular agent loaded it or that its outcome figures are calibrated. |
| `/Users/amuldotexe/.codex/skills/executable-specs-01/SKILL.md` | SHA-256 `0647bbf3d63f2b3ad5097017fb888203d4b9125ae58457a61472140477d04066` | Current executable workflow guidance. | Establish current local rules for contract IDs, test mapping, measured thresholds, context selection, deterministic indexing, and explicit global review. | It is process guidance, not target behavior or a guarantee that every recommendation fits every repository. |
| `/Users/amuldotexe/.codex/skills/executable-specs-01/references/executable-specs-templates.md` | SHA-256 `3562fbbdb7506edca27761ac246f75f6d173c18dd96054793e7c0be8d2d59629` | Current template family. | Supply requirement, traceability, TDD, quality-gate, and large-artifact contract shapes. | Example values and skeletons are illustrative; copying them does not establish a real threshold or passing result. |
| `/Users/amuldotexe/.codex/skills/executable-specs-01/agents/openai.yaml` | SHA-256 `ac7a1cc858b8d126cecb74ab5e4e1a1495d235583c084cbce85859b20a4d36cf` | Current interface metadata. | Establish display text and default invocation intent for the installed skill. | Metadata does not govern specification semantics or supersede the skill body. |
| `agents-used-monthly-archive/idiomatic-references-202606/generated-references/executable_metapattern_reference_digest.md` | SHA-256 `fac50f5eeb78e0a2a27033297d78721f5203cc23597c957b4cf0ba2f67249b5a` before evolution. | Frozen reference seed. | Establish all 26 original headings and the exact baseline each evolved section must exceed. | It is the structural and historical baseline, not current evidence that its recommendations are correct. |
| `idiomatic-reference-evolution-spec-202607.md` and `tests/test_idiomatic_reference_evolution.py` | Current shared process controls, read but not edited by this lane. | Assignment specification and executable structural verifier. | Define packet shape, exact questions, persistence cadence, heading preservation, expansion, uniqueness, and placeholder gates. | Passing these checks establishes evolution integrity, not theme-level empirical truth. |

The first four metapattern paths are one semantic source family. Read one representative copy completely for meaning, retain every path for temporal and packaging provenance, and never multiply evidentiary weight because identical bytes appear four times. Hash equality does not show that each copy had the same surrounding bundle, activation context, or assigned authority.

**Retained public research pointers**

| external_source_url_value | locally retained description | current evidence state | promotion gate |
| --- | --- | --- | --- |
| `https://developers.openai.com/codex/guides/agents-md` | OpenAI Codex agent-instruction context guidance. | `unrefreshed_pointer`; current content, path, version, and applicability were not checked. | With browsing authorization, open the official source, record retrieval identity, compare with active local instructions, and reproduce any behavior claim. |
| `https://docs.github.com/actions` | GitHub Actions verification and automation documentation. | `unrefreshed_pointer`; no workflow behavior is asserted from it here. | Retrieve the version-relevant primary documentation, then validate permissions, runner, shell, concurrency, and artifact behavior in a safe workflow. |
| `https://agents.md/` | General agent-instruction format pointer. | `unrefreshed_pointer`; current format and authority remain unknown. | Retrieve and version the source, compare with the active harness, and retain only claim-relevant guidance. |

The descriptions above are facts about what the seed says those links are for. They are not refreshed external facts. Search snippets, memory, or a familiar URL cannot promote them.

**Claim-specific authority routing**

| question | first authority | corroboration | source that must not overrule it |
| --- | --- | --- | --- |
| What did a dated digest path contain? | Exact archive bytes at the recorded hash. | Duplicate-family comparison and surrounding archive metadata. | Current skill prose cannot rewrite historical content. |
| What workflow is currently recommended locally? | Current installed `SKILL.md` and its linked current templates. | Current agent metadata for invocation intent and repository instructions for scope. | An older digest cannot override newer explicit guardrails. |
| What contract shape is available? | Current template bytes. | Skill output contract and target repository conventions. | An example row cannot choose a real target value. |
| What behavior should the target system have? | User or domain authority plus target source, configuration, tests, and runtime evidence. | Executable requirement packet and owner review. | Metapattern guidance cannot invent product intent. |
| Did an implementation satisfy a requirement? | Claim-capable project checks under a recorded state. | Direct source review, negative cases, integration evidence, and owner acceptance where needed. | Structural packet tests alone cannot prove product behavior. |
| Does a performance or reliability claim hold? | A controlled measurement under a defined workload and environment. | Representative samples, raw evidence, uncertainty, and operational telemetry as appropriate. | Inherited directional figures or template thresholds cannot serve as current results. |
| What does a public platform currently support? | Refreshed versioned official source followed by local reproduction. | Installed capability and target-specific test. | The retained URL row cannot establish current behavior. |

**Default source route**

1. Read the complete user request, repository instructions, and target context.
2. Read one representative metapattern digest to understand inherited rationale and terminology.
3. Read the current skill and only the template sections needed for the active artifact.
4. Separate direct local facts, historical observations, current guidance, examples, inference, unknowns, and owner choices.
5. Use target source, configuration, tests, build, and runtime evidence to settle implementation claims.
6. Refresh a public source only when authorization exists and the external fact can change the decision.
7. Record which source and premise invalidates each durable claim.

**Conflict and drift handling**

| conflict | required response |
| --- | --- |
| Historical digest and current skill disagree | Preserve the digest as historical rationale; use the current skill for current local workflow unless repository instructions override it. |
| Current template and repository convention disagree | Preserve template intent, adapt to repository-native IDs and test surfaces, and record why the local convention is stronger. |
| Requirement and existing behavior disagree | Decide whether the contract describes a bug fix, migration, compatibility requirement, or mistaken assumption before changing code. |
| Two hash-equal paths have different role labels | Preserve both labels as metadata, report the unexplained distinction, and avoid using it as independent technical evidence. |
| Public guidance and installed behavior disagree after an authorized refresh | Version both, reproduce the installed result, narrow applicability, and avoid averaging incompatible evidence. |
| A measurement contradicts an inherited outcome figure | Keep the inherited number as a source observation, use the controlled target measurement for the bounded decision, and document cohort differences. |

Good source use says, "The four local digest copies contain identical guidance; the current skill adds explicit guards against invented context budgets; this target requirement is verified by the named repository checks." Bad source use says, "Four local files and three links prove the metapattern improves productivity." A concise answer may cite one representative digest path, but the durable ledger must preserve the duplicate family, current operational sources, and unrefreshed status.

The map is causal and versioned. Guidance informs templates; templates help compile a decision packet; target evidence supports or refutes its claims; failures feed a later skill or template revision. A later improvement must not rewrite what an earlier source said or retroactively strengthen a decision made under weaker evidence.

## Pattern Scoreboard Ranking Table

The seed's numbers are preserved as **inherited editorial scores**. No local source gives their formula, sample, denominator, reviewer rubric, uncertainty, or outcome study. They rank emphasis inside the historical digest; they do not establish percentage effectiveness, comparative accuracy, or universal priority.

**Preserved inherited scoreboard**

| pattern_identifier_stable_key | inherited_score_value | inherited_tier | protected_failure | present interpretation |
| --- | ---: | --- | --- | --- |
| `source_map_first_synthesis` | 95 | `default_adoption_pattern_tier` | Context-free advice created without loading theme-specific authority. | Start new durable work by identifying claim-capable local sources and recording what each can prove. |
| `evidence_boundary_split_pattern` | 91 | `default_adoption_pattern_tier` | Local guidance, public pointers, examples, and inference blended into one authoritative voice. | Give every material claim a source type, scope, uncertainty state, and promotion gate. |
| `verification_gate_coupling` | 88 | `default_adoption_pattern_tier` | Recommendation cannot be falsified by a command, test, review question, measurement, or owner decision. | Attach a capable check and explicit failure response before the claim authorizes implementation or handoff. |

The repeated seed identifier `executable_metapattern_reference_digest` names the theme rather than three distinct patterns. The evolved stable keys above make the protected behavior independently addressable while retaining the original values as historical metadata.

**Causal adoption order**

1. `source_map_first_synthesis`: identify the strongest source for each pending question.
2. `evidence_boundary_split_pattern`: state whether the resulting claim is observed, inherited, inferred, illustrative, unresolved, or owner-selected.
3. `verification_gate_coupling`: choose a mechanism capable of rejecting that exact claim.
4. `requirement_behavior_decomposition`: split compound obligations until each has one observable outcome and failure boundary.
5. `bidirectional_traceability_audit`: map every material requirement to checks and every retained check to a requirement or documented invariant.
6. `expected_failure_reason_confirmation`: demonstrate that the pre-implementation check fails because behavior is missing or wrong, not because the harness is broken.
7. `minimal_behavior_then_refactor`: implement only the behavior needed for Green evidence, then improve structure without widening the contract silently.
8. `claim_invalidation_route`: name the source, implementation, configuration, workload, or policy change that reopens the accepted result.

The order is causal, not mandatory ceremony. An existing repository contract may already satisfy the first five controls. Reuse is valid when its authority, current state, negative cases, and traceability are checked. Mentioning all pattern names without performing their rejection behavior is not adoption.

**Current qualitative register**

| pattern | default posture | apply when | adapt or avoid when | verification gate | counter-signal |
| --- | --- | --- | --- | --- | --- |
| Source map first | Default for new durable packets. | Several sources, versions, owners, or evidence classes can affect the decision. | A narrow direct source and authoritative existing test already settle a reversible lookup. | Another reviewer can locate each material source and explain its authority. | Source inventory grows while no decision or conflict changes. |
| Evidence boundary split | Required for material claims. | Guidance, observations, external research, measurements, or inference are mixed. | Use concise labels for low-risk navigation, but do not erase scope. | Claim-to-source audit rejects unsupported promotion. | Labels exist but do not change wording, action, or uncertainty. |
| Verification gate coupling | Required before implementation completion. | A recommendation promises behavior, quality, compatibility, or a constraint. | Route to owner judgment when no technical mechanism can decide the policy choice. | Positive, negative, and failure-path evidence under the target state. | Gate passes regardless of whether the requirement is satisfied. |
| Behavior decomposition | Default for compound requests. | One sentence contains several actors, outcomes, constraints, or error cases. | Keep an atomic contract intact when splitting would hide one transaction invariant. | Every clause can fail independently or its coupling is explicit. | A requirement needs many unrelated fixtures and owners. |
| Bidirectional traceability | Default for durable changes. | Requirements and checks may drift across implementation and review. | A tiny existing contract may use a concise link rather than a large matrix. | No orphan material requirement and no unexplained behavior-defining check. | Row count increases while important assertions remain tautological. |
| Expected failure confirmation | Default for changed behavior. | A new or corrected behavior needs evidence that the check can detect absence. | Existing regression reproduction may serve as Red evidence if identity is retained. | The failure reason matches the missing or incorrect behavior. | Failure is caused by syntax, setup, permissions, or unrelated state. |
| Measured constraint gate | Required for quantitative claims. | Latency, memory, throughput, capacity, error rate, or reviewer-time language affects acceptance. | Keep the value unresolved until baseline, workload, and owner exist. | Reproducible measurement packet with units, environment, sample, and uncertainty. | A template or inherited percentage supplies the target without local evidence. |
| Deterministic context index | Conditional for large evolving artifacts. | Repeated complete reads materially waste context and exact section selection is possible. | Small artifacts should be read completely; global review must remain explicit. | Same canonical bytes yield the same complete index and stale hashes reject edits. | Index summaries replace required canonical content or omit matches. |
| Claim invalidation route | Default for handoff. | Evidence will outlive the current session or depends on mutable state. | A transient navigation observation may state only its revision and stop point. | A changed premise identifies all dependent claims and checks to reopen. | Accepted claims survive source or policy changes without review. |

**Adoption profiles**

| profile | minimum visible controls | prohibited promotion |
| --- | --- | --- |
| Navigation | Current source identity, bounded question, direct observation, and stop reason. | Cannot become a behavior, consumer-completeness, safety, or performance claim without additional gates. |
| Standard implementation | Source map, evidence classification, decomposed requirements, negative cases, bidirectional traceability, Red/Green/Refactor record, and project verification. | Cannot invent product choices, quantitative targets, or high-assurance absence. |
| High assurance | Standard controls plus domain authority, configuration and variant coverage, independent checks, recovery, owner acceptance, and residual-risk record. | A green structural verifier or one integration path cannot substitute for the domain evidence floor. |

**Pattern admission and lifecycle rules**

A new metapattern enters the register only when it:

- prevents a distinct recurring failure rather than renaming an existing control;
- states prerequisites and the task profiles where it fits;
- names a concrete pass, fail, unresolved, and route-away state;
- can be verified without checking merely for its own label;
- records implementation and review cost plus a counter-signal;
- identifies what change invalidates its adoption evidence.

Promote a candidate pattern after controlled fixtures or repeated target observations show that it catches the named failure without unacceptable side effects. Adapt it when repository conventions preserve the control through another mechanism. Retire or narrow it when it produces paperwork without affecting detection, decision quality, recovery, or downstream outcomes.

Good scoreboard use: a reviewer sees conflicting local requirements, applies source mapping first, preserves the unresolved conflict through evidence typing, and blocks code until an owner-approved contract has a failing behavioral check. Bad scoreboard use: an agent says score 95 proves source mapping is 95 percent effective. Conditional reuse: a current repository test and requirement may satisfy the chain implicitly, but their identity and rejection behavior must be demonstrated before the shortcut is accepted.

Future outcome calibration must keep process conformance separate from effectiveness. A pattern-presence audit asks whether the control was executed. An outcome study asks whether comparable decisions had fewer reversals, missed requirements, or escaped defects. Only the latter could justify a new empirical ranking, and it would remain bounded by its task cohort and consequence.

## Idiomatic Thesis Synthesis Statement

**Governing thesis:** An executable metapattern is a typed conversion from intent and evidence into a falsifiable obligation, a capable rejection mechanism, a bounded implementation action, and a recoverable decision record. Formal syntax, identifiers, or a green command are insufficient when the source, desired behavior, negative cases, or claim-to-check fit is wrong.

The thesis preserves three seed evidence umbrellas while narrowing their meaning:

- `local_corpus_sourced_fact`: the mapped three local paths, plus the current installed reference, are one hash-equal digest family. They establish exact inherited guidance and numbers, not the provenance or reproducibility of the claimed outcomes.
- `external_research_sourced_fact`: no refreshed fact of this type was created here. The seed's public URLs remain unrefreshed research pointers because browsing was prohibited.
- `combined_evidence_inference_note`: local guidance and systems reasoning support the pipeline below, but target applicability and outcome improvement still require target evidence.

**Evidence conversion pipeline**

| conversion | required input | emitted artifact | gate before promotion | failure state |
| --- | --- | --- | --- | --- |
| Request -> decision | User goal, actor, boundary, consequence, non-goals, owner. | Bounded decision and open-question set. | Owner confirms desired outcome and authority. | Clarification or product route required. |
| Source -> claim | Exact source identity, scope, version, and observation. | Typed factual, inferred, illustrative, or unresolved claim. | Claim wording does not exceed source authority. | Narrow, relabel, or reject claim. |
| Claim -> requirement | Trigger, observable result, invariant, failure, and applicable constraint. | Stable behavior contract. | Each obligation is falsifiable and independently owned or explicitly coupled. | Decompose or return to authority. |
| Requirement -> verification | Target test surface, fixture, assertion, negative case, measurement, or review authority. | Bidirectional test and review matrix. | Mechanism can reject the promised failure class. | Route to a stronger mechanism or leave unresolved. |
| Verification -> implementation | Confirmed expected failure and authorized change boundary. | Minimal behavior needed for Green evidence. | Failure reason matches missing or incorrect behavior. | Repair harness or premise before coding. |
| Green -> refactored design | Passing behavior evidence plus source and architecture context. | Clearer implementation with unchanged contract. | Relevant checks remain green and diff stays in scope. | Revert or revise design, not the evidence. |
| Implementation -> accepted decision | Full relevant checks, counterevidence, configuration, review, and recovery. | Proceed, scoped proceed, revise, reject, or escalate. | Evidence profile matches consequence and owner authority. | Block handoff or narrow action. |

The pipeline is deliberately fail-fast. Precision added after an unsupported conversion does not repair the premise. A meticulously formatted test matrix still fails when the product outcome was invented; a benchmark still fails when workload identity changed; a reviewer approval still fails outside the reviewer's authority.

**Operational principles synthesized from the local digest and current skill**

1. Use specific retrieval cues and semantic names. Names should expose behavior and scope to humans and tools. The four-word convention is a default for new symbols where feasible, not a reason to break public compatibility, framework idioms, or clarity.
2. Iterate through explicit evidence states. Explore alternatives, constrain with authority, refine the contract, and verify the result. Iteration should change a premise or artifact, not repeat the same prompt until a preferred answer appears.
3. Persist canonical state across context loss. Save exact contracts, source identities, tests, decisions, and next actions. Summaries may orient a resumed agent but cannot replace canonical inputs required by the active phase.
4. Expose decision rationale and challenge assumptions. Record premises, counterarguments, and falsification routes. Do not confuse useful high-level rationale with a demand to preserve private hidden reasoning traces.
5. Keep anti-patterns causal. Record the failure, mechanism, detection signal, safer route, and regression evidence so future agents avoid the same class rather than memorizing a slogan.
6. Make tests and checks executable contracts. Confirm the expected failure, implement the smallest behavior change, refactor under Green evidence, and run final claim-capable verification.
7. Evolve guidance from outcomes. Version source and templates, retain reversals and defects, and change defaults only when evidence shows a recurring mismatch or better route.

**Verification modes and tradeoffs**

| mode | strongest use | blind spot | combine with |
| --- | --- | --- | --- |
| Example-based unit test | Concrete input/output and local edge behavior. | Unenumerated state space and integration semantics. | Boundary, property, and integration checks. |
| Property or model check | Invariants across generated cases or state transitions. | Model assumptions and environment integration. | Representative examples and production constraints. |
| Type or schema constraint | Prevent impossible shapes before runtime. | Dynamic policy, external state, and semantic intent. | Behavioral tests and migration checks. |
| Integration or contract test | Boundary behavior among real components. | Unselected variants, external instability, and production scale. | Unit diagnostics, configuration matrix, and operational evidence. |
| Build or static analysis | Compilation, compatibility, dependency, and policy properties. | Exercised runtime behavior and business outcome. | Runtime or test evidence where behavior is dynamic. |
| Benchmark or load test | Quantitative behavior under a frozen workload. | Other workloads, machines, and long-term production effects. | Baseline, profiler, uncertainty, and production telemetry. |
| Reviewer or owner gate | Semantics, tradeoffs, policy, and risk acceptance. | Reviewer blind spots and unverifiable implementation detail. | Reproducible technical evidence and dissent record. |

Choose the least costly bundle capable of falsifying the pending consequential claim. More methods do not automatically mean stronger evidence when they share the same blind spot.

**False-executability checks**

Reject or revise a packet when:

- a requirement uses aspiration such as "better," "robust," or "fast" without an observable definition;
- a quantitative value comes from a template, inherited percentage, or intuition rather than workload and authority;
- a test asserts private implementation shape while the promised external behavior could still be wrong;
- requirement identifiers exist but material requirements or tests are orphaned;
- only happy-path evidence exists for a failure-sensitive feature;
- compatibility exceptions are hidden to satisfy a naming convention;
- a passing check was never shown capable of detecting the missing behavior;
- one environment or configuration result is generalized to all variants;
- a summary substitutes for current canonical source after context compaction;
- the packet has no invalidation, recovery, or route-away state.

Good program example: a repository's authoritative retry policy and storage semantics become idempotency requirements for first attempt, replay, concurrent duplicate, expiry, and backend failure. Each maps to a capable check, the missing behavior produces the expected failure, and final evidence records configuration scope and recovery.

Bad example: "Improve reliability" becomes a numbered requirement with a copied success percentage and one test that calls the same helper the implementation uses. The appearance of structure does not define reliability or create independent evidence.

Conditional documentation example: a runbook change cannot always be programmatically tested, but it can still be executable when an unfamiliar reviewer follows the steps against a safe fixture, reaches the expected state, and rejects an injected stale or unauthorized input. The gate is behavioral even though it is partly human-executed.

**Second-order consequences**

Requirements are an intermediate representation between human intent and several consumers: code, tests, types, review, observability, rollout, and future agents. That makes requirement quality a systems boundary. A vague contract multiplies ambiguity downstream; a source-bound falsifiable contract lets each consumer specialize without losing the original decision.

The resulting packet is also an invalidation graph. A source change reopens derived claims; a requirement change reopens linked tests and implementation; a workload change reopens measured constraints; a policy change reopens authorization. Unrelated verified facts remain intact. This selective retraction is the thesis's reliability mechanism: not universal certainty, but controlled promotion, contradiction, and recovery.

## Local Corpus Source Map

The local corpus has one duplicate rationale family and three distinct current operational artifacts. The map below routes complete semantic sections; it does not copy their bodies or allow a heading match to substitute for reading the selected section.

**Content-family inventory**

| family | local paths | observed SHA-256 | read strategy | authority boundary |
| --- | ---: | --- | --- | --- |
| AI-Native Meta-Patterns Digest | 202602 archive, 202603 archive, unclassified local file, current installed reference. | `78ead044feb402432f104e37f82578f3fad5f161a4df4bec809120cd2eea7882` | Read one copy completely for meaning; retain all four identities and surrounding context for provenance questions. | Historical and current rationale; no independent outcome replication from duplicate bytes. |
| Current executable-spec workflow | Current installed `SKILL.md`. | `0647bbf3d63f2b3ad5097017fb888203d4b9125ae58457a61472140477d04066` | Read completely for a new workflow; select complete relevant sections on later bounded reuse. | Present local process guidance, not target behavior. |
| Current executable-spec templates | Current installed template reference. | `3562fbbdb7506edca27761ac246f75f6d173c18dd96054793e7c0be8d2d59629` | Load only the complete template needed after reading the skill contract. | Artifact shapes and illustrative examples, not achieved results or mandatory target values. |
| Current agent interface metadata | Current installed `agents/openai.yaml`. | `ac7a1cc858b8d126cecb74ab5e4e1a1495d235583c084cbce85859b20a4d36cf` | Read when invocation or display behavior matters. | Interface intent only; no authority over requirements or evidence. |

The digest names `/Users/amuldotexe/Downloads/notes01-agent (1).md` as its source reference. That origin was not part of the required mapped corpus and was not inspected. The statement that the digest names it is locally observed; the origin's content, generation process, and study lineage remain unknown.

**AI-Native Meta-Patterns Digest routing**

| complete source section | load when the pending question is | useful contribution | required caution |
| --- | --- | --- | --- |
| `1) Measured Outcomes to Preserve` | What directional benefits motivated the practices? | Preserves the inherited before/after figures and their local "directional targets" caveat. | No study design, corpus, sampling, attribution, or reproducibility packet is present; do not treat values as target results. |
| `2) Seven Core Principles (Operational Form)` | Which broad behaviors should guide agent work? | Specific retrieval cues, iteration, checkpoints, assumption review, anti-pattern memory, TDD, and cumulative learning. | Each principle needs repository fit, a failure boundary, and observable adoption evidence. |
| `3) Four-Word Naming Convention (4WNC)` | How should new generated symbols expose semantic intent? | A memorable `verb_constraint_target_qualifier` default and compatibility caveat. | Four words are not universally idiomatic; preserve public APIs, framework contracts, established vocabulary, and clarity. |
| `4) TDD-First Loop` | How should a behavior change move through test and implementation states? | Test skeleton, Red, Green, Refactor, and final verification sequence. | Phase names do not prove the failure reason, test independence, minimality, or full-suite evidence. |
| `5) Executable Requirement Pattern` | How should a behavior clause state condition, outcome, constraint, and edge case? | Condition/outcome/constraint syntax and a warning against vague aspiration. | Not every clause needs all keywords; atomicity, authority, and verification fit matter more than ritual shape. |
| `6) Context Budget Guidance` | What historical context-selection heuristics were suggested? | Discovery-before-analysis order and illustrative task budgets. | The current skill explicitly forbids inventing budgets, packet sizes, and schedules; measure the active artifact and model constraints. |
| `7) 2026 Agent Patterns to Reuse` | How should agents use computers, tools, files, isolation, caching, and trajectories? | Filesystem persistence, small action space, progressive disclosure, context offload, isolation, and learning. | Apply only when tool availability, ownership, security, and coordination contracts are known. |
| `8) Anti-Patterns Checklist` | Which broad failures should a spec workflow reject? | First-pass perfection assumptions, narrative-only contracts, partial feature packaging, placeholder residue, and unsupported performance claims. | Convert each slogan into a local detection and recovery rule before enforcement. |

**Current skill routing**

| complete skill section | decision served | current guardrail or contract | route away when |
| --- | --- | --- | --- |
| `Workflow` | How to turn a request into contracts and verification. | Parse outcome, actors, failures, limits, and runtime constraints; choose context shape; assign stable IDs; map checks; execute TDD; emit quality gates. | Product outcome or domain authority is still unresolved. |
| `Output Contract` | What order and shape should a specification packet use? | Executable requirements, test matrix, TDD plan, quality gates, and open questions. | Repository-native format is stronger; adapt while preserving semantic fields. |
| `Guardrails` | What practices are prohibited or conditional? | Reject vague/unmeasured claims, invented context numbers, unsafe input splitting, unjustified periodic rereads, and deterministic editorial decisions. | A project policy imposes a stricter measurable rule; record the authority. |
| `Large Evolving Artifacts` | How should repeated work on one large canonical artifact preserve context and integrity? | Self-describing headings, deterministic indexes, complete selected sections, stale-hash rejection, atomic rebuild, and explicit global review. | The artifact is small enough for complete reads or every section is required now. |
| `Context Strategy` | What should be loaded first and how should context expand? | Skill first, templates on demand, rationale when needed, complete small artifacts, measured search-first protocol for expensive repeated reads. | Search cannot guarantee complete candidates or a global phase is active. |

**Current template routing**

| template section | use | verify before reuse |
| --- | --- | --- |
| Requirement Contract | Create an atomic condition/outcome/constraint clause. | Desired behavior authority, independently observable result, and edge/failure coverage. |
| Traceability Matrix | Link requirement IDs to test identities, types, assertions, and targets. | Both directions are complete and assertions observe behavior rather than labels. |
| TDD Plan | Record expected failure, minimal behavior, refactoring, and final checks. | Red reason is correct, Green is scoped, and relevant full checks are known. |
| Language-Specific Test Skeletons | Bootstrap Rust, TypeScript, or Go test shape. | Repository framework, naming, fixtures, error semantics, async model, and style. |
| Vague-to-Executable Rewrite Patterns | Demonstrate measurable wording. | Example quantities are replaced by owner-approved, workload-defined values. |
| Quality Gate Template | Assemble pre-handoff structural and behavioral checks. | Each check has a real command or reviewer mechanism plus a failure response. |
| Large Evolving-Artifact Template | Specify deterministic headings, indexes, selected reads, and edit guards. | Artifact size/churn justifies indexing and the canonical source remains authoritative. |

**Observed evolution and tension points**

| earlier digest guidance | current skill refinement | synthesis decision |
| --- | --- | --- |
| Suggested fixed token budgets by task type. | Do not invent token budgets, packet sizes, segment sizes, or review schedules; derive them from measured inputs and constraints. | Preserve historical suggestions as rationale only; measure before setting a current budget. |
| Use four words for new function names where feasible. | Keep generated names at four words, preserve existing public API names, and use wrappers when useful. | Apply as a semantic-density default with explicit compatibility and idiom exceptions. |
| Write short summaries after milestones. | Checkpoints aid orientation but cannot replace canonical content required by the phase. | Persist summaries plus exact canonical locators, hashes, and required complete sections. |
| Keep action space small and offload context. | Deterministic tools may index and validate but must not make editorial decisions. | Use automation for mechanical completeness and agents or owners for semantic selection. |
| Directional outcome figures motivate adoption. | Reject performance claims without measurable thresholds and method. | Keep figures as inherited observations; collect target evidence before any outcome claim. |

**Retrieval profiles**

| profile | required local reads | safe stopping point |
| --- | --- | --- |
| Narrow reuse | Current repository instructions, existing authoritative contract, relevant skill rule, and complete selected template section. | Existing source and check settle a reversible bounded change. |
| Standard new packet | Complete current skill, complete request and repository context, one representative digest, and every selected template section. | Requirements, tests, gates, and open questions are reviewable and source-bound. |
| Historical comparison | Every relevant archive path plus surrounding metadata, current counterpart, and byte diff. | Temporal claim is bounded and duplicate evidence is not overcounted. |
| Global artifact review | Complete canonical artifact, complete fresh index if used, all required source sections, and explicit global-review contract. | Whole-artifact consistency and final gates pass with durable checkpoints. |

**Map integrity rules**

1. Verify each path exists and capture a content identity before relying on it.
2. Read each distinct content family completely at least once for this evolution.
3. Preserve duplicate path and date identities without rereading identical bodies for semantic weight.
4. Search headings for routing, then read the complete selected semantic section.
5. Reconcile current skill guardrails with historical digest heuristics.
6. Treat template examples as shapes until target values and checks replace them.
7. Rebuild or re-review the map after source hash or heading changes.
8. Escalate to a complete global read when all sections or cross-section invariants matter.

Good retrieval: an agent designing a large-artifact workflow reads the complete current `Large Evolving Artifacts` section and template, measures the canonical artifact, and tests deterministic index behavior. Bad retrieval: the agent copies the digest's `8k` refactoring suggestion and truncates required context to fit it. Conditional policy: a team may adopt a fixed local budget after a measured study and owner decision, but the resulting policy is new target evidence, not validation of the inherited number.

## External Research Source Map

No external query or page retrieval was performed. Each URL is preserved exactly from the seed with state `unrefreshed_no_browse`. The locally observed fact is that the seed associates a URL with a role; current page content, authority, version, and applicability are unknown until a future authorized refresh.

**Decision-bound external queue**

| external_source_url_value | seed_description | trigger to refresh | question the primary source must answer | required local closure | current state |
| --- | --- | --- | --- | --- | --- |
| `https://developers.openai.com/codex/guides/agents-md` | OpenAI Codex agent-instruction context model. | Active instruction scope, precedence, discovery, or supported behavior changes in a way that affects a live agent contract. | For the active product and date, how are instruction files discovered, scoped, combined, and applied, and what boundaries remain tool- or repository-specific? | Compare official guidance with the active harness and complete local instruction chain; reproduce the exact scope behavior needed by the decision. | `unrefreshed_no_browse` |
| `https://docs.github.com/actions` | GitHub Actions verification and automation model. | An executable gate is being moved to hosted automation or a workflow failure depends on permissions, runner, shell, artifacts, concurrency, cancellation, or environment semantics. | Which version-relevant platform contract governs the exact workflow feature, and what permissions and failure states must the specification encode? | Test a least-privilege safe fixture under the selected workflow and runner, retain logs and configuration identity, and verify the intended rejection path. | `unrefreshed_no_browse` |
| `https://agents.md/` | General agent-instruction format. | Cross-tool instruction portability or format compatibility becomes a real deliverable. | Which syntax, scope, interoperability, and extension behavior is currently specified, and which behavior belongs to individual agent products? | Compare the exact candidate document with every target harness, preserve unsupported differences, and run tool-specific behavior checks. | `unrefreshed_no_browse` |

These rows are hypotheses about where primary evidence may live. They do not assert that the paths are stable, that a named feature exists, or that one format controls every agent implementation.

**Local-first and external-first routes**

| situation | first move | external move | stop condition |
| --- | --- | --- | --- |
| Existing local instruction behavior is clear | Read complete active instructions and observe the harness. | Do not browse unless a current product contract would change the decision. | Local evidence settles the bounded claim and no portability assertion is made. |
| Known platform upgrade or deprecation caused a mismatch | Capture installed/deployed identity and exact failure. | Retrieve official migration and version documentation first, then reproduce locally. | Applicable change is confirmed or the result is escalated as version-ambiguous. |
| CI gate design is new | Define the repository acceptance and security boundary locally. | Retrieve only feature-specific official workflow documentation needed by that design. | A safe fixture demonstrates both success and rejection behavior. |
| Cross-agent portability is exploratory | Inventory target tools and local constraints. | Time-box a format survey and retain candidates only. | No production guidance changes until at least one target comparison exists. |
| Required access or hosted environment is unavailable | Preserve the blocked claim and owner. | Do not infer behavior from a page alone. | Access changes, an authorized owner accepts narrower scope, or the feature is rejected. |

**Source-quality ladder**

| source class | strongest use | limitation |
| --- | --- | --- |
| Versioned official specification or product manual | Establish the publisher's stated contract for a named version or retrieval date. | Does not prove installed packaging, configuration, or repository behavior. |
| Official release notes, migration guide, or issue/source history | Explain changes, regressions, and compatibility boundaries. | Unreleased or unresolved material may not apply to the deployed version. |
| Installed help, local source, active harness, or runner output | Establish actual local capability and behavior for observed cases. | Can omit conceptual limits and does not generalize to other installations. |
| Controlled positive and negative fixture | Establish causal behavior for selected inputs and configuration. | Does not prove broad platform reliability or all target variants. |
| Representative target workflow | Establish bounded applicability to the repository decision. | Remains scoped to the selected runner, permissions, workload, and time. |
| Community article or discussion | Generate vocabulary, edge-case hypotheses, or candidate alternatives. | Not decision authority; verify through primary and local evidence. |

**External evidence promotion protocol**

1. State the blocked local claim and why existing sources cannot settle it.
2. Confirm browsing authorization, data-handling boundaries, and acceptable source classes.
3. Record the exact query, retrieval date, product/version scope, direct URL, publisher, title, and relevant section.
4. Paraphrase the smallest claim needed, including preconditions and explicit limitations; avoid copying large passages.
5. Match the active installed, deployed, or target version and configuration.
6. Reproduce a positive and a negative case or record why reproduction requires unavailable authority.
7. Compare the result with local instructions, repository conventions, and existing tests.
8. Update the decision as adopt, adapt, reject, no change, or escalation required.
9. Name the external release, local version, configuration, or policy change that invalidates the result.

Finding a plausible page completes only retrieval, not the refresh. The refresh completes when the external claim has a bounded applicability decision and a local evidence effect.

**Refresh result card**

| field | required content |
| --- | --- |
| `research_identifier` | Stable link to the original requirement or unresolved claim. |
| `trigger_and_consequence` | Why current external behavior matters and what false guidance could cause. |
| `retrieval_identity` | Query, direct source, publisher, date, version, section, and source class. |
| `narrow_claim` | Paraphrased contract with conditions, exclusions, and uncertainty. |
| `local_identity` | Active product, harness, runner, repository, configuration, and working state. |
| `reproduction` | Positive, negative, conflict, unavailable, or not-applicable result with exact mechanism. |
| `decision_effect` | Requirement, test, route, implementation, or explicit no-change outcome. |
| `counterevidence` | Local behavior, conflicting source, packaging difference, or owner constraint. |
| `invalidation` | Upstream, local, repository, or policy change that reopens the result. |
| `owner_and_next_action` | Accountable reviewer, implementation or fixture work, and stop condition. |

**Research failure states**

| failure | response |
| --- | --- |
| URL unavailable or moved | Search only within the official publisher under authorization, record the old pointer as historical, and do not invent continuity. |
| Current page has no version identity | Record retrieval date and narrow the claim to that observed page; rely on local reproduction for applicability. |
| Official statement conflicts with installed behavior | Verify versions and packaging, retain both observations, and use the target behavior for the bounded implementation while escalating compatibility. |
| Search snippet appears sufficient | Open the primary source or discard the claim; snippets lack full scope and authority. |
| Community guidance is the only source | Keep it as a hypothesis and require a local fixture plus owner review before adoption. |
| Hosted test cannot run safely | Preserve the blocked state, define the required authorized environment, and avoid substituting simulated confidence. |
| External result does not change a decision | Close or retire the item rather than adding a ceremonial citation. |

Good research use: a hosted workflow rejects an expected permission. The operator captures the exact runner and configuration, retrieves the relevant official permission contract, reproduces a least-privilege positive and negative fixture, and changes the requirement and gate accordingly.

Bad research use: "GitHub Actions documentation proves this pipeline is secure." A broad documentation root cannot establish a repository's permissions, secret handling, third-party actions, or runtime behavior.

Conditional exploration: a team may survey instruction formats before selecting target agents. The result is a candidate compatibility matrix, not an adopted contract, until each target harness is versioned and tested.

**Queue lifecycle**

- Prioritize a consequential blocker before a recurring mismatch, planned upgrade, performance hypothesis, or exploratory horizon item.
- Assign an owner and a decision effect to every active research question.
- Close an item when local source and fixtures settle it more directly.
- Retire a pointer when the product or trigger no longer applies, preserving the historical reason.
- Refresh event-driven claims after relevant upstream or installed-version changes; do not invent periodic schedules without evidence.
- Keep prior retrieval identity when guidance changes so old decisions remain interpretable.

The external map is therefore a queue of falsifiable research questions, not a bibliography and not current source attribution. Its success is measured by a safer local decision, including the decision not to browse or not to adopt.

## Anti Pattern Registry Table

Use the registry to classify the earliest failed premise and change workflow state. Do not use it as a vocabulary for post hoc blame. A matched entry should identify what becomes unsafe, what remains usable, and what evidence releases the block.

**Common containment and recovery protocol**

1. Stop promotion of every claim that depends on the suspected defect.
2. Preserve the exact source, requirement, check, output, and contradiction needed for diagnosis.
3. Identify the earliest observable stage: intent, source, claim, requirement, verification design, implementation, measurement, handoff, or reuse.
4. Select the smallest control capable of distinguishing the leading mechanism from alternatives.
5. Correct the premise or route the claim to a stronger authority; do not patch only the final wording.
6. Replay the affected negative and positive gates, then reopen only dependent decisions.
7. Add or revise a regression fixture when the mechanism is recurring, severe, deterministic, and safe to represent.

**Cross-cutting anti-pattern registry**

| anti_pattern_failure_name | stage and mechanism | observable signal | unsafe consequence | safer default and containment | release evidence |
| --- | --- | --- | --- | --- | --- |
| `context_free_summary_output` | Source selection: agent produces generic guidance without reading mapped local authority. | Recommendations cannot be traced to exact local source or target context. | Advice may contradict current repository rules while sounding polished. | Stop durable handoff; apply source-map-first synthesis and retain skipped-source reasons. | Complete selected source reads plus claim-to-source audit. |
| `duplicate_source_vote_inflation` | Evidence weighting: byte-identical copies are counted as independent agreement. | Several citations share one hash or copied text but are described as corroboration. | Confidence increases without any new observation model. | Collapse substantive weight into one content family and retain paths only for provenance. | Hash ledger and corrected evidence rationale. |
| `unrefreshed_pointer_promotion` | External evidence: retained URL is described as current fact. | No retrieval date, version, direct page observation, or applicability check exists. | Stale or unavailable guidance can drive current implementation. | Relabel as an unrefreshed pointer; browse only under authorization and decision need. | Versioned primary source plus local reproduction. |
| `inherited_metric_result_promotion` | Measurement: historical or template number becomes a current outcome. | Figure lacks target workload, sample, environment, method, and raw evidence. | False performance, productivity, accuracy, or reliability claim. | Preserve as inherited observation; define a target measurement packet before adoption. | Controlled target result with uncertainty and owner interpretation. |
| `fixed_context_budget_without_measurement` | Context planning: suggested token or segment count becomes a hard cap. | Required source is truncated or skipped solely to satisfy an inherited number. | Missing evidence is hidden as efficiency. | Measure artifact and phase inputs; change phase or method rather than silently truncating. | Complete input accounting and no-missing-candidate gate. |
| `semantic_naming_rule_overreach` | Design: four-word default overrides public compatibility, framework contract, or clear domain vocabulary. | Rename breaks callers or produces awkward, misleading terms. | API regression and lower clarity under nominal compliance. | Apply semantic-density intent; preserve external names and use wrappers only when useful. | Compatibility checks, call-site review, and naming rationale. |
| `requirement_identifier_without_behavior` | Contract authoring: stable ID is attached to aspiration or compound prose. | Trigger, observable result, edge behavior, or owner is absent. | Traceability matrix gives a vague promise formal authority. | Decompose and rewrite into falsifiable behavior before implementation. | Reviewer can construct a failing case from the clause. |
| `owner_choice_disguised_as_requirement` | Authority: agent invents product policy, target, or tradeoff. | No user, domain, or policy source supports the selected value. | Code implements an unauthorized decision. | Mark an open question or bounded hypothesis and route to the decision owner. | Recorded owner decision and updated contract. |
| `one_way_traceability_claim` | Verification mapping: requirements list tests, but tests are not audited back to behavior. | Orphan tests encode undocumented invariants or linked tests assert unrelated behavior. | Green suite appears complete while contracts drift. | Run bidirectional requirement/check mapping with semantic assertion review. | No unexplained behavior-defining checks and no unverified material requirements. |
| `tautological_test_oracle` | Test design: assertion derives expected output through the implementation under test or checks private shape only. | Wrong external behavior can pass because test and code share the same premise. | False Green evidence and fragile refactors. | Use independent expected values, model, fixture, boundary observation, or differential oracle. | Injected wrong behavior causes the check to fail for the intended reason. |
| `green_without_expected_failure` | TDD execution: implementation exists before the check demonstrates detection. | No retained Red result, or failure came from syntax/setup rather than missing behavior. | Passing test may never have been capable of catching the defect. | Reproduce the pre-fix behavior or use a regression fixture with a verified failure reason. | Expected failure identity followed by Green under only the intended change. |
| `happy_path_only_contract` | Requirement and test design: errors, empty inputs, boundaries, cancellation, concurrency, or recovery are omitted where material. | Every example succeeds and failure semantics are undefined. | Production failure behavior becomes accidental. | Add consequence-relevant negative cases and explicit error or fallback contracts. | Negative checks reject unsafe behavior and preserve recovery. |
| `implementation_before_authority` | Workflow: code starts while desired behavior or owner choice is unresolved. | Diff grows while requirement questions remain open or contradictory. | Rework and accidental policy selection. | Stop mutation, preserve current findings, and resolve authority or split a reversible experiment. | Approved behavior boundary and expected failure evidence. |
| `deterministic_tool_editorial_decision` | Automation: parser, score, or script chooses semantic relevance or sufficiency. | Tool output silently excludes or ranks claims without reviewer rationale. | Mechanical convenience becomes hidden policy. | Restrict tools to indexing, hashing, extraction, search, and validation; keep editorial choice explicit. | Complete candidate output plus reviewer selection record. |
| `checkpoint_summary_substitutes_canonical_input` | Context recovery: compact summary replaces exact artifact or selected source after interruption. | Agent cannot verify source hashes, precise clauses, or omitted alternatives. | Context drift changes requirements invisibly. | Reload canonical packet, fresh index when used, and complete selected sections. | Current canonical identities and reconstruction check. |
| `silent_match_or_packet_truncation` | Retrieval: search, packet, or selected section is cut without a fail state. | Counts disagree, tail is missing, or no truncation marker exists. | Relevant claim or counterexample disappears from consideration. | Fail closed, change phase or query, and preserve complete required input. | Complete-count reconciliation and deterministic retrieval. |
| `partial_feature_called_complete` | Delivery: structure, one layer, or one test lands without end-to-end behavior and recovery. | User-visible path, integration, docs, scripts, or required checks remain absent. | Version communicates completion while consumers receive a fragment. | Narrow the deliverable honestly or finish the one bounded feature end to end. | Acceptance journey and all linked gates pass. |
| `verification_command_cargo_cult` | Quality gate: familiar command is copied without checking repository fit or claim coverage. | Command is missing, irrelevant, too broad, or incapable of observing the promised behavior. | A green exit code becomes ceremonial approval. | Discover repository-native checks and state what each pass leaves unproven. | Command availability, expected failure fixture, and claim-capability review. |
| `measurement_plan_reported_as_result` | Performance: proposed benchmark is written in outcome language. | No execution record or raw observations exist. | Design choice anchors on fictional improvement. | Label the plan unexecuted and keep all values unknown until measured. | Reproducible run packet and reviewed analysis. |
| `percentile_theater_from_small_sample` | Statistics: tail labels are calculated from too few or mixed observations. | Sample count, quantile method, failures, or cohort identity is absent. | Precision-looking distribution claim has no stability. | Report raw observations and uncertainty; add data only under comparable conditions. | Justified distribution design and recalculable source. |
| `compatibility_exception_hidden` | Requirement and naming: existing API, format, schema, or migration obligation is omitted to satisfy a new convention. | New tests pass while legacy consumers or serialized data are unexamined. | Breaking change escapes local validation. | State compatibility boundary, migration, wrappers, and deprecation ownership explicitly. | Consumer inventory, compatibility fixtures, and rollout evidence. |
| `configuration_scope_generalization` | Verification: one feature flag, platform, tenant, or environment is treated as universal. | Result report lacks variant identity and exclusions. | Unchecked variants inherit false confidence. | Enumerate material variants or narrow the claim to the tested configuration. | Variant matrix or explicit owner-accepted scope. |
| `ownerless_unresolved_claim` | Handoff: uncertainty is documented but has no accountable next route. | Open item lacks owner, decision deadline, evidence need, or stop condition. | Risk silently broadens or remains permanently pending. | Assign owner and next capable mechanism or reject the dependent action. | Accepted scope, resolved claim, or explicit escalation state. |
| `stale_acceptance_reuse` | Lifecycle: prior Green evidence is reused after source, contract, implementation, workload, or policy changes. | Current identity differs from decision record without invalidation review. | Obsolete evidence authorizes a new state. | Mark dependent claims invalid and replay the smallest affected gate set. | New identities, rerun evidence, and owner review where needed. |

**Severity and handling**

| class | meaning | default response |
| --- | --- | --- |
| Advisory | Quality could improve, but the current reversible claim remains supported. | Record rationale and correct opportunistically without expanding scope. |
| Claim blocking | A statement exceeds its evidence, but other packet work may remain useful. | Downgrade or isolate the claim and continue only independent branches. |
| Implementation blocking | Desired behavior, capable check, or authority is missing. | Stop mutation until the prerequisite passes or the work is narrowed. |
| High-assurance stop | Security, deletion, migration completeness, compliance, or production risk lacks its evidence floor. | Route to domain mechanisms and accountable owner; no local override. |

**Registry admission and maintenance**

Add a durable entry only when the mechanism is observed or strongly evidenced, recurs or carries severe consequence, can be detected with a stable signal, and has a safer replacement plus regression route. Preserve `unclassified` for novel failures. Do not force a mismatch into a familiar row merely to close diagnosis.

An entry is verified when a negative fixture or reviewed target case demonstrates that the control rejects the named defect, preserves unaffected evidence, and releases only after the right premise changes. Checking that the pattern name appears in prose is not verification.

Good recovery: a proposed p99 target has no baseline or owner. The agent marks the requirement unresolved, continues functional contract work, defines workload and measurement questions, and promotes the target only after a controlled study. Bad recovery: the agent gives the value a stable requirement ID and considers the precision problem solved. Conditional experiment: an explicitly provisional value may bound a spike if it has an owner, expiration, measurement plan, and a hard rule against production acceptance.

The registry feeds back into source maps, templates, and tests. Repeated source omissions improve retrieval gates; repeated tautological tests improve oracle guidance; repeated stale reuse improves invalidation. Retire or narrow entries whose enforcement costs more than the distinct failure they prevent. Failure history becomes organizational memory only when it changes a future rejection path.

## Verification Gate Command Set

`verification_gate_command_set`: Select commands by evidence population and claim. Run cheap identity and structural checks first, semantic review next, target-repository behavior checks after the contract is stable, and whole-corpus completion only when every owner has finished.

**Gate dependency order**

| gate | property checked | evidence produced | what a pass does not prove | failure response |
| --- | --- | --- | --- | --- |
| A. Environment and ownership | Correct root, readable inputs, authorized outputs, exclusive file owner, required interpreter. | Preflight record and scoped paths. | Source freshness or requirement quality. | Stop before writes or commands with side effects. |
| B. Frozen identity | Working seed equality before editing, queue-span hashes, source-family hashes, and complete input coverage. | Hash and coverage audit. | That inherited claims are true or applicable. | Mark stale assignment and resolve with coordinator; never guess around a mismatch. |
| C. Packet integrity | Exact 26 packet sections, 260 question headings, ten exact question texts per section, six ordered fields per question, 1,560 populated values, raw and normalized uniqueness. | Focused parser result. | That the rationale is substantively correct. | Fix the current packet section before editing its reference section. |
| D. Reference evolution | Exact original heading levels, texts, and order; every section strictly exceeds its seed body. | Parsed heading and section-length comparison. | Useful detail, internal consistency, or factual accuracy. | Reopen the affected section and its packet conclusions. |
| E. Markdown and hygiene | ASCII policy, final newline, balanced fences, consistent tables, no tabs or trailing whitespace, clean diff, and prohibited placeholder absence. | Deterministic hygiene report. | Behavioral correctness. | Correct before semantic handoff. |
| F. Evidence and semantics | Source claims, counterarguments, uncertainty, examples, measurements, and external status match their evidence classes. | Complete reread and claim audit. | Target implementation success. | Narrow or retract unsupported claims and rerun dependent review. |
| G. Target behavior | Repository-native unit, integration, build, static, benchmark, runtime, or owner checks capable of observing each requirement. | Red/Green/Refactor and final project evidence. | Unselected variants or risks outside the test profile. | Keep the claim unresolved, revise the contract, or route to a stronger mechanism. |
| H. Handoff and lifecycle | Residual risk, owner, next action, recovery, invalidation, changed paths, and current test state. | Decision record and progress checkpoint. | Permanent validity after premises change. | Block completion until recovery and ownership are reconstructable. |

**Current 202607 shared structural checks**

The following read-only tests validate stable shared inventory and hygiene properties without requiring another lane to be complete:

```bash
python3 -m pytest -q \
  tests/test_idiomatic_reference_evolution.py::IdiomaticReferenceEvolutionTests::test_inventory_matches_specification \
  tests/test_idiomatic_reference_evolution.py::IdiomaticReferenceEvolutionTests::test_owner_mapping_unique \
  tests/test_idiomatic_reference_evolution.py::IdiomaticReferenceEvolutionTests::test_assignment_manifests_match \
  tests/test_idiomatic_reference_evolution.py::IdiomaticReferenceEvolutionTests::test_packet_content_uniqueness \
  tests/test_idiomatic_reference_evolution.py::IdiomaticReferenceEvolutionTests::test_reference_placeholders_absent
```

The full module also checks all references, all packets, and shared queue completion. While other owners are active, those whole-corpus tests may be red for files outside this assignment. Report the exact external population; do not call the failure irrelevant and do not modify another lane to make it green.

```bash
python3 -m pytest -q tests/test_idiomatic_reference_evolution.py
```

**Assignment-scoped focused verifier**

Run from the repository root after each atomic section and again after the complete reread. This compact form checks the principal shape and uniqueness contracts; final verification should add hygiene and table/fence checks.

```bash
python3 - <<'PY'
from pathlib import Path
import re
from tests.test_idiomatic_reference_evolution import (
    PACKET_FIELDS,
    load_specification_question_texts,
    normalize_packet_field_content,
    parse_markdown_heading_sections,
)

reference = Path("idiomatic-ref-202607/executable_metapattern_reference_digest-20260710.md")
seed = Path("agents-used-monthly-archive/idiomatic-references-202606/generated-references/executable_metapattern_reference_digest.md")
packet = Path("idiomatic-reference-evolution-work/delta/packets/executable_metapattern_reference_digest-20260710-question-packets.md")

reference_sections = parse_markdown_heading_sections(reference.read_text())
seed_sections = parse_markdown_heading_sections(seed.read_text())
assert [heading for heading, _ in reference_sections] == [heading for heading, _ in seed_sections]
assert len(reference_sections) == 26
assert all(
    len(current.strip()) > len(original.strip())
    for (_, current), (_, original) in zip(reference_sections, seed_sections)
)

packet_text = packet.read_text()
section_chunks = [
    chunk for chunk in re.split(r"(?=^## Section \d{3}:)", packet_text, flags=re.MULTILINE)
    if chunk.startswith("## Section ")
]
assert len(section_chunks) == 26
expected_questions = load_specification_question_texts()
values = []
for section in section_chunks:
    questions = [
        chunk for chunk in re.split(r"(?=^### Question \d{2}:)", section, flags=re.MULTILINE)
        if chunk.startswith("### Question ")
    ]
    assert len(questions) == 10
    for question_number, (question, expected_text) in enumerate(zip(questions, expected_questions), 1):
        assert question.splitlines()[0] == f"### Question {question_number:02d}: {expected_text}"
        fields = re.findall(r"^- \*\*([^*]+):\*\*\s+(.+)$", question, flags=re.MULTILINE)
        assert [name for name, _ in fields] == list(PACKET_FIELDS)
        values.extend(value.strip() for _, value in fields)
assert len(values) == 1560
assert len(set(values)) == 1560
assert len({normalize_packet_field_content(value) for value in values}) == 1560
print("focused assignment verifier: PASS")
PY
```

**Scoped diff and immutable-source checks**

```bash
git diff --check -- \
  idiomatic-ref-202607/executable_metapattern_reference_digest-20260710.md \
  idiomatic-reference-evolution-work/delta/packets/executable_metapattern_reference_digest-20260710-question-packets.md \
  idiomatic-reference-evolution-work/delta/progress.md

python3 - <<'PY'
from pathlib import Path
import hashlib

expected = {
    "agents-used-monthly-archive/idiomatic-references-202606/generated-references/executable_metapattern_reference_digest.md": "fac50f5eeb78e0a2a27033297d78721f5203cc23597c957b4cf0ba2f67249b5a",
    "agents-used-monthly-archive/codex-skills-202602/executable-specs-01/references/meta-patterns-reference.md": "78ead044feb402432f104e37f82578f3fad5f161a4df4bec809120cd2eea7882",
    "/Users/amuldotexe/.codex/skills/executable-specs-01/SKILL.md": "0647bbf3d63f2b3ad5097017fb888203d4b9125ae58457a61472140477d04066",
}
for raw_path, expected_hash in expected.items():
    actual_hash = hashlib.sha256(Path(raw_path).read_bytes()).hexdigest()
    assert actual_hash == expected_hash, (raw_path, actual_hash)
print("immutable source identities: PASS")
PY
```

**Legacy archive verifier**

The seed's original command is preserved below only for auditing the 202606 generated archive and its associated coverage, critique, and journal files. Complete code inspection shows that it does not read the 202607 working directory or Delta packets. Its result must not be reported as current assignment verification.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

**Project behavior gate discovery**

This reference cannot name a universal build or test command. Before implementation, inspect repository instructions, manifests, CI, and existing tests; record the exact commands that can observe each requirement. A valid pass record includes target revision, configuration, fixtures, expected failure reason, result, and what remains outside coverage.

| pending claim | likely gate family | mandatory rejection question |
| --- | --- | --- |
| Pure transformation or validation | Unit, property, or type/schema check. | Would a representative wrong result fail independently of implementation internals? |
| Component boundary | Integration or contract test. | Are real boundary semantics and failure behavior exercised? |
| Compatibility or migration | Consumer inventory, versioned fixture, build matrix, and rollback. | Can an old supported consumer or stored value still work as promised? |
| Quantitative constraint | Benchmark, profiler, load, or telemetry packet. | Are workload, environment, sample, units, and uncertainty sufficient for the claim? |
| Dynamic or configured behavior | Configuration matrix, runtime probe, trace, or end-to-end test. | Does the selected workload cover the path being generalized? |
| Security or policy | Threat-specific negative tests, configuration review, static/runtime evidence, and authorized owner. | Can this mechanism reject the relevant adversarial or unauthorized state? |

**Gate-harness verification**

A gate must be tested against malformed input or a controlled bad state. Examples include a duplicate normalized packet value, changed seed heading, unexpanded section, stale source hash, orphan requirement, irrelevant linked test, incorrect Red reason, and changed workload. The expected result is rejection at the earliest capable gate, preservation of diagnostics, and invalidation of only dependent claims.

Good use: the assignment-focused verifier passes while the full shared suite reports unfinished files owned elsewhere. Both results are retained with their populations, and the owned file advances. Bad use: the archive verifier exits successfully and the agent claims the 202607 packet and target feature are correct. Conditional use: rerunning the legacy verifier is useful after an archive-integrity concern, but its evidence stays historical.

Verification is a dependency graph. A failed source hash reopens packet reasoning; a failed packet field reopens its section before reference prose; a failed project check reopens the requirement or implementation; a changed policy reopens acceptance. Selective invalidation is stricter and cheaper than either ignoring red evidence or rerunning unrelated gates blindly.

## Agent Usage Decision Guide

`agent_usage_decision_guide`: A mention of executable specifications, TDD, requirement IDs, a mapped source path, or a nearby workflow should trigger a fit check. Apply the digest only when the next decision concerns desired observable behavior, verification, implementation sequencing, or durable acceptance evidence.

**Trigger and fit table**

| task signal | likely fit | first question | primary action |
| --- | --- | --- | --- |
| Ambiguous feature or change request | Strong fit after outcome clarification. | Who observes success, which boundary changes, and who owns unresolved policy? | Compile intent into behavior claims, checks, and open questions. |
| Existing acceptance criteria are vague or contradictory | Strong fit. | Which source and owner can resolve each conflict? | Build a source ledger, split claims, and revise before implementation. |
| User asks for TDD implementation | Strong fit with repository-specific coding guidance. | What behavior must fail first and which project check can observe it? | Write/identify failing check, implement minimal behavior, refactor, verify. |
| Requirement/test traceability audit | Strong fit. | Are mappings complete in both directions and semantically relevant? | Audit orphan requirements, orphan checks, assertions, and invalidation. |
| Quality-gate or completion review | Strong fit. | Which claims are structural, behavioral, measured, or owner-accepted? | Select capable gates and report limitations and recovery. |
| Large evolving artifact | Conditional fit. | Are repeated complete reads materially expensive, and is a global phase required? | Use measured context, deterministic index, complete selected sections, and explicit global review. |
| Exact source lookup or explanation | Usually too broad. | Can direct search and source reading answer the bounded question? | Use direct repository navigation; invoke the digest only if behavior must be specified. |
| Unknown failure cause | Not the primary method. | Can the defect be reproduced and causally isolated? | Route to systematic diagnosis, then specify the intended fix and regression. |
| Architecture alternative selection | Partial fit. | What evaluation criteria and acceptance conditions can be made executable? | Use architecture analysis for choice; use this digest for contracts and verification. |
| Security or authorization proof | Auxiliary only. | Which threat, configuration, and owner authority define sufficiency? | Route to domain assurance and retain traceability here. |
| Performance value without baseline | Specification of method only. | What workload, environment, sample, owner, and decision require measurement? | Define experiment; do not invent or claim a result. |

**Agent state machine**

| state | entry evidence | permitted work | prohibited promotion | exit |
| --- | --- | --- | --- | --- |
| `orienting` | User request and repository instructions are available. | Read complete bounded context, inspect existing contracts, identify owners and sources. | No behavior or target invention. | Decision and open questions stated. |
| `clarification_required` | Material desired behavior or authority is missing. | Search repository conventions, ask owner, or offer bounded alternatives. | No mutation that chooses the unresolved policy. | Owner decision, existing authority, or scoped experiment. |
| `specified` | Falsifiable requirements, source types, and non-goals are reviewed. | Design tests, fixtures, measurements, and implementation boundary. | No completion claim before capable checks exist. | Expected-failure plan accepted. |
| `red_observed` | Check fails for the missing or wrong behavior under a recorded state. | Implement the smallest behavior change needed for the claim. | No unrelated refactor or speculative feature expansion. | Relevant check becomes Green for the intended reason. |
| `green_observed` | Minimal behavior passes its direct checks. | Refactor, improve names, remove duplication, and add consequence-driven coverage. | No contract broadening hidden inside cleanup. | Relevant suite and contract checks remain Green. |
| `verification_ready` | Implementation and local checks are stable. | Run full applicable gates, review diff, reconcile traceability and counterevidence. | No unsupported performance, security, completeness, or variant claim. | Proceed, revise, reject, or escalate. |
| `verified_for_scope` | Evidence profile matches the bounded action and owner accepts where required. | Handoff, document recovery, and record invalidation. | No silent reuse after a premise changes. | Completed or later invalidated. |
| `blocked_or_unresolved` | Capability, access, policy, or evidence is insufficient. | Preserve verified branches, owner, missing mechanism, and release condition. | No confidence inflation or endless same-method retries. | New evidence, narrower scope, or owner decision. |
| `invalidated` | Source, requirement, implementation, configuration, workload, or policy changed. | Reopen only dependent claims and replay their gates. | No reuse of stale acceptance. | New scoped verification. |

State names can stay implicit for a tiny reversible change, but the evidence transitions cannot. A passing test without an expected failure capability is not equivalent to `red_observed -> green_observed`.

**Default agent sequence**

1. Read the newest user instructions, repository rules, ownership limits, and current progress state.
2. State the exact outcome, actor, boundary, consequence, non-goals, and unresolved owner choices.
3. Search for authoritative existing requirements, tests, interfaces, and conventions before creating a parallel specification.
4. Load one representative local rationale source, the current skill, and only complete selected templates needed by the decision.
5. Classify every material claim as observed, inherited, inferred, illustrative, unresolved, or owner-selected.
6. Write or reuse atomic requirements with stable IDs and explicit failure behavior.
7. Build bidirectional verification links and confirm the expected initial failure.
8. Implement proactively inside the authorized boundary when intent and evidence are sufficient.
9. Run claim-capable project checks, structural gates, evidence review, and diff/ownership review.
10. Return the bounded result, residual uncertainty, recovery, invalidation, and next action.

**Operating modes**

| mode | use when | output | stop condition |
| --- | --- | --- | --- |
| Planning-only | User asks for a plan, wants alternatives, or must approve a consequential choice before edits. | Requirement draft, test matrix, risks, open decisions, and proposed gates. | Do not mutate until requested or authority is resolved. |
| End-to-end implementation | Desired behavior and write scope are clear and user expects the change. | Tests, implementation, refactoring, verification, and concise handoff. | Stop only at completion or a material blocker after self-service investigation. |
| Review | Existing packet or code needs challenge rather than implementation. | Findings ordered by consequence, missing evidence, and precise remediation. | Do not rewrite unless review scope includes fixes. |
| Recovery | Prior work is interrupted, stale, contradictory, or failing. | Reconstructed canonical state, earliest false premise, affected claims, and changed-premise next attempt. | Do not restart valid work or overwrite another owner's changes. |
| Global artifact review | Every section is genuinely required for final consistency. | Complete reread checkpoints, cross-section reconciliation, focused verifier, and final hashes. | Do not disguise full loading as incremental retrieval. |

**Context and tool discipline**

- Prefer repository-native source, tests, manifests, and documented commands over generic examples.
- Read small required artifacts completely. For materially large repeated artifacts, measure and use a deterministic index that returns every candidate; then read selected sections completely.
- After compaction or handoff, reload canonical packet, current index when applicable, and exact selected content. A summary is orientation only.
- Use scripts for hashing, parsing, search, and validation. Do not delegate semantic relevance or risk acceptance to deterministic scores.
- Parallelize independent reads or files only. One owner writes each shared file, packet, or artifact directory.
- Preserve user and other-agent changes. Never use cleanup, retry, or refactoring as permission to revert unrelated work.
- Inspect side effects before commands and keep generated artifacts inside authorized paths.

**Minimum agent output**

| field | required answer |
| --- | --- |
| Decision | What action or explanation was requested and what is out of scope? |
| Evidence | Which exact sources and project observations support or refute it? |
| Contract | Which behavior requirements and negative cases govern the work? |
| Verification | Which checks ran, what did they establish, and what remains unproven? |
| Change | Which paths and interfaces changed, if implementation was authorized? |
| Uncertainty | Which claims remain unresolved, why, and who owns them? |
| Recovery | How can the action be reversed or diagnosed if a premise fails? |
| Invalidation | Which future source, code, configuration, workload, or policy change reopens the result? |
| Next action | What executable step, owner, and stop condition follows? |

**Good, bad, and conditional use**

Good: the user asks to reject duplicate submissions. The agent finds an existing idempotency policy, clarifies key scope from repository evidence, writes replay and concurrent-duplicate checks, observes the pre-fix failure, implements only the bounded behavior, and runs the relevant suite.

Bad: the word "metapattern" appears in a brainstorming note, so the agent writes a long formal specification, invents targets, and edits code before the user chooses a direction.

Conditional: one product choice remains unresolved while three independent validation rules are clear. The agent can specify and implement the three verified branches if their interfaces do not depend on the choice, while isolating the blocked branch with an owner and release condition.

**Usage review**

After durable work, ask whether the guide found an authoritative existing contract, exposed a missing owner decision, caught a contradiction before implementation, improved a rejection gate, reduced irrelevant context without losing evidence, or routed a claim to a stronger method. Record downstream reversals and escaped requirements. Do not infer productivity improvement from one successful task.

Appropriate abstention is a successful outcome. The guide has done its job when it prevents a specification-shaped answer from replacing product discovery, diagnosis, domain assurance, or measured evidence.

## User Journey Scenario

All repositories, requirement IDs, commands, observations, and outcomes in this journey are illustrative. They demonstrate a mechanism grounded in the local sources; no target service, fixture, benchmark, or runtime was created for this assignment.

Role based opening scenario: A technical lead and implementation agent receive the request, "Make webhook processing reliable and fast before the partner launch."

Primary user starting state: The repository has a webhook handler, a queue, a persistence layer, scattered tests, and no single acceptance contract. The request combines correctness, retry behavior, and a quantitative aspiration. The service owner is available, but the acceptable latency and launch workload have not been measured.

Decision being made: Which behavior can be specified and implemented now, which product or operational choices require an owner, which negative cases prove reliability, and what evidence would make a performance claim legitimate?

Reference opening trigger: Open this digest after the compound request is recognized as implementable work whose behavior, verification, and handoff need to survive beyond the initial conversation.

**Step 1: Clarify the action, not the wording**

The agent rewrites the surface request into four decision branches:

| branch | tentative question | consequence if wrong | initial state |
| --- | --- | --- | --- |
| Duplicate delivery | What constitutes the same event and which effects may occur once? | Duplicate downstream writes or incorrectly suppressed legitimate events. | Owner and repository evidence required. |
| Retry and recovery | Which failures are retryable, when is an attempt abandoned, and who owns dead-letter recovery? | Event loss, retry storm, or repeated nonidempotent work. | Existing queue policy may be authoritative. |
| Response semantics | What response tells the sender that ownership transferred successfully? | Sender retries unexpectedly or assumes a rejected event was accepted. | Protocol and current handler evidence required. |
| Performance | Which workload and percentile must meet which bound in which environment? | Invented target, poor capacity decision, or launch risk. | Unresolved until baseline and owner decision. |

Non-goals are stated early: this change does not redesign every event consumer, promise exactly-once delivery across independent systems, choose a partner SLO without authority, or generalize one local benchmark to production.

**Step 2: Build the evidence ledger**

| evidence item | illustrative observation | claim strength | missing evidence |
| --- | --- | --- | --- |
| Service owner discussion | Partner event ID is the deduplication key within a stated retention interval. | Owner-selected policy for that integration. | Expiry and migration behavior still need agreement. |
| Current handler source | Handler acknowledges after enqueue but before downstream processing. | Source observation under the inspected revision. | Runtime queue failure and partner interpretation need tests or protocol evidence. |
| Queue configuration | A bounded attempt policy and dead-letter route are configured. | Configuration observation for one environment. | Other deployments and operational ownership remain outside scope. |
| Persistence schema | No uniqueness constraint exists for partner and event key. | Current structural fact. | Transaction boundary and concurrent write behavior need integration evidence. |
| Existing tests | One successful request is covered; replay and concurrent duplicates are absent. | Test inventory observation. | No evidence that duplicate side effects are rejected. |
| Request phrase "fast" | No workload, bound, percentile, or owner is attached. | Unresolved aspiration. | Baseline, launch traffic model, environment, and decision threshold. |

The agent does not fill the performance gap with the digest's inherited figures or a template value. It returns a measurement question instead.

**Step 3: Resolve product and architecture choices**

The owner chooses a composite key and retention policy. The implementation team compares three mechanisms:

| mechanism | benefit | risk or cost | evidence needed before choice |
| --- | --- | --- | --- |
| Database uniqueness plus transactional state | Durable concurrency control near persistent effects. | Transaction contention, migration, and database-specific semantics. | Schema design, concurrent integration fixture, rollback, and operational review. |
| Distributed cache key | Potentially fast duplicate lookup and expiry. | Eviction, failover, split state, and weaker durability. | Failure injection, consistency contract, capacity, and recovery ownership. |
| Queue-level deduplication | Centralized admission control if the platform supports the exact contract. | Platform/version limits and downstream effects beyond deduplication window. | Versioned platform evidence, configured behavior, and local reproduction. |

The digest does not choose among them. It makes the guarantee and evidence cost explicit. The team selects one through its architecture and ownership process, then binds the requirements to that decision.

**Step 4: Compile atomic requirements**

Illustrative contracts:

```markdown
### REQ-HOOK-001.0: Accept first event attempt

**WHEN** a valid partner event key has no accepted record within the configured retention policy
**THEN** the service SHALL record one accepted event and transfer it to the configured processing boundary
**AND** SHALL return the documented acceptance response only after that transfer succeeds
**SHALL** return a typed rejection without an accepted record when transfer fails

### REQ-HOOK-002.0: Suppress duplicate effects

**WHEN** two or more requests with the same partner and event key race inside the retention policy
**THEN** the system SHALL create at most one accepted event record
**AND** SHALL prevent duplicate downstream effect initiation for that key
**SHALL** return the documented replay response for every recognized duplicate

### REQ-HOOK-003.0: Recover exhausted attempts

**WHEN** processing reaches the configured attempt limit for a retryable failure
**THEN** the event SHALL enter the configured recovery destination with its event key and final failure class
**AND** SHALL expose enough correlation for an authorized operator to resume or close it
**SHALL** avoid another automatic attempt until the recovery policy explicitly permits one
```

Each clause has one behavior center. The exact response code, retention interval, attempt limit, transaction mechanism, and recovery destination come from target policy and configuration, not this example.

The performance branch becomes a measurement contract rather than a fabricated acceptance value:

```markdown
### REQ-HOOK-PERF-001.0: Measure launch admission latency

**WHEN** the approved launch workload, event-size distribution, environment, and cache state are frozen
**THEN** the benchmark SHALL report request admission latency with raw sample count, failures, and justified distribution summaries
**AND** SHALL record database, queue, CPU, memory, and competing-load context needed to interpret the result
**SHALL** remain non-accepting until the service owner selects a bound using baseline and launch consequence
```

**Step 5: Design bidirectional verification**

| req_id | illustrative check | type | key assertion | important negative case |
| --- | --- | --- | --- | --- |
| `REQ-HOOK-001.0` | `TEST-INTEG-HOOK-001` | Integration | One valid first attempt records and transfers exactly once before acceptance. | Queue transfer failure leaves no falsely accepted state. |
| `REQ-HOOK-002.0` | `TEST-INTEG-HOOK-002` | Concurrent integration | Racing duplicates produce one accepted record and one downstream initiation. | Different partner or event key is not suppressed. |
| `REQ-HOOK-002.0` | `TEST-UNIT-HOOK-003` | Unit/property | Duplicate classification honors the owner-selected key and retention boundary. | Expired key follows the approved new-attempt policy. |
| `REQ-HOOK-003.0` | `TEST-INTEG-HOOK-004` | Integration | Exhausted retry enters recovery with correlation and stops automatic attempts. | Nonretryable failure does not consume the retry path. |
| `REQ-HOOK-PERF-001.0` | `TEST-BENCH-HOOK-005` | Benchmark design | Raw observations and environment identity are complete. | Missing workload or owner bound prevents acceptance. |

The reverse audit asks whether every behavior-defining test maps to a requirement or documented invariant. An old test that expects acknowledgement before queue transfer would contradict `REQ-HOOK-001.0`; the team must decide whether the requirement is a deliberate migration or mistaken assumption before editing either side.

**Step 6: Observe Red before implementation**

In a future replay, the concurrent duplicate check should fail because both requests can create accepted state under the initial schema. A setup failure, missing fixture, or syntax error would not be valid Red evidence. The agent records the failing assertion, target revision, configuration, and absence of unrelated failures.

**Step 7: Implement the bounded branches**

The implementation adds only the selected deduplication mechanism, response semantics, and recovery behavior needed by the reviewed requirements. It preserves public compatibility unless the contract and migration explicitly authorize a change. Refactoring follows Green evidence and cannot silently broaden keys, retention, attempts, or response policy.

**Step 8: Verify with split outcomes**

| branch | illustrative final evidence | state |
| --- | --- | --- |
| First acceptance | Transaction and transfer integration checks pass under the selected test configuration. | `verified_for_scope` for that configuration. |
| Concurrent duplicate | The pre-fix fixture failed as expected; the selected implementation passes replay, race, and distinct-key cases. | `verified_for_scope` under the fixture and chosen storage semantics. |
| Retry recovery | Exhaustion, correlation, and no-extra-attempt checks pass; operator ownership is documented. | `verified_for_scope` for the configured queue policy. |
| Performance | Benchmark method is defined, but workload baseline and owner bound are absent. | `unresolved`; no speed claim and no launch acceptance from this branch. |

This is a successful partial outcome. Functional branches can proceed if the launch decision does not require the missing performance acceptance. If it does, the owner keeps release blocked until measurement closes the branch.

**Step 9: Handoff and invalidation**

The record names changed paths, requirement and test identities, exact commands, configuration, contradictions, residual risk, rollback, and owner. It also states that changes to partner key semantics, retention, queue attempt policy, storage transaction behavior, response protocol, launch workload, or deployment configuration invalidate dependent claims.

Good example: verified idempotency and recovery ship with bounded evidence while performance remains explicitly unresolved. Bad example: all branches are marked complete because one unit suite is green and an arbitrary latency number was inserted. Borderline experiment: a temporary internal beta target can be owner-accepted with workload, expiry, recovery, and no-generalization language, but it remains a new local policy rather than a fact from this digest.

**Future replay criteria**

A controlled fixture should include first attempt, serial replay, concurrent replay, distinct key, expiry boundary, transfer failure, retryable failure, nonretryable failure, attempt exhaustion, and recovery. It should prove the expected pre-fix failures and final behavior without claiming production traffic equivalence. The transfer rule is the reusable lesson: split a compound request, let each claim earn its own state, and preserve shared premises so one change reopens only the affected branches.

## Decision Tradeoff Guide

Use the least costly route capable of falsifying the pending claim, then escalate when a remaining blind spot can change the action. Cost includes setup, context, maintenance, false confidence, late rework, rollback, and option loss. Sufficiency is claim-specific: evidence adequate for a reversible parser fix can be inadequate for a migration, security guarantee, or production performance target.

**Preserved posture guide**

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | Current local sources, target authority, repository conventions, and a capable verification surface support the full evidence-to-contract workflow. | Fastest durable route for a new bounded change, but can add unnecessary structure if a stronger existing contract already exists. | Does each material claim have a current authority, falsifiable behavior, capable check, and recovery state? |
| Adapt when | The metapattern is sound but repository syntax, compatibility, domain policy, artifact size, or assurance requirements require a different representation or deeper gate. | Preserves intent and local fit, but creates design and reconciliation work. | Which control is preserved, which mechanism changes, and how will equivalence or stronger assurance be demonstrated? |
| Avoid when | Product intent is undecided, causal diagnosis is primary, the decisive evidence is security/runtime/operational, or the reference would create a second authority beside a complete native contract. | Prevents false precision and drift, but requires a specialized route or a narrower answer. | Which missing observation or authority makes executable-spec work premature or redundant? |
| Cost of being wrong | Wrong guidance can implement unauthorized policy, miss a consumer, encode a tautological check, ship a partial behavior, or anchor on an invented target. | Rework ranges from revising a document to compatibility breakage, unsafe migration, launch delay, or production incident. | Can a reviewer identify the failed premise, affected claims, rollback, owner, and next evidence without reconstructing the entire session? |

Local/external agreement is not a universal adoption test. Duplicate local files can agree because they are identical, and public guidance can be current but inapplicable. Target behavior, owner authority, and claim-capable checks decide whether the workflow is sufficient.

**Specification production choices**

| choice | choose when | benefit | cost or blind spot | escalation or rejection trigger |
| --- | --- | --- | --- | --- |
| Reuse an existing contract | Current requirement, interface, test, and owner already govern the exact behavior. | Avoids duplicate truth and preserves repository conventions. | Existing artifact may be stale, scattered, or narrower than assumed. | Contradiction, missing negative case, stale identity, or changed action consequence. |
| Augment an existing contract | Core behavior is authoritative but one failure, variant, measurement, or recovery path is absent. | Smallest change and clearer review. | New clause can conflict with old consumers or implicit invariants. | Consumer or compatibility evidence shows broader migration is required. |
| Create a new bounded packet | No coherent current contract exists and the change will be implemented or handed off. | Centralizes source, behavior, checks, uncertainty, and invalidation. | Authoring and maintenance cost; risk of becoming a parallel authority. | Owner cannot designate its relationship to existing docs/tests. |
| Consolidate scattered contracts | Repeated ambiguity or drift causes real review and maintenance cost. | One durable decision surface and bidirectional traceability. | Migration, ownership, link updates, and risk of losing historical nuance. | No owner or safe transition plan exists. |
| Draft a nonaccepting experiment | A value or architecture premise needs evidence before commitment. | Enables learning without pretending the hypothesis is approved. | Prototype can leak into production or become de facto policy. | Missing expiry, owner, isolation, measurement, or promotion criteria. |
| Decline specification work | Desired behavior or authority cannot be established, or another artifact already settles the question. | Prevents false formality and redundant truth. | Progress may pause or route elsewhere. | Resume only after a material evidence or ownership change. |

**Requirement granularity choices**

| form | strength | failure mode | safe use |
| --- | --- | --- | --- |
| One atomic behavior per contract | Independent test, ownership, and invalidation. | Too many tiny clauses can hide a transaction invariant. | Default; explicitly link inseparable obligations. |
| Scenario contract | Captures multi-step user or system journey. | Intermediate failures and branch states can be underspecified. | Pair with atomic invariants and recovery cases. |
| Property or invariant | Covers broad generated state space. | Model can omit real integration and policy assumptions. | Combine with representative examples and boundary checks. |
| Type/schema contract | Prevents malformed states early. | Cannot express dynamic side effects, timing, or owner policy alone. | Use as one layer of behavior evidence. |
| Operational acceptance | Captures deployed behavior and recovery. | Environment and workload may be hard to reproduce. | Required when the claim depends on production-like state. |

**Verification choices**

| mechanism | strongest economical use | key blind spot | pair with when consequential |
| --- | --- | --- | --- |
| Unit/example test | Local input/output and edge behavior. | Integration, concurrency, configuration, and unknown cases. | Property, integration, or runtime evidence. |
| Property/model test | Invariants over generated cases or transitions. | Model fidelity and external boundaries. | Curated examples and real component checks. |
| Integration/contract test | Real component boundary semantics. | Unselected variants and production scale. | Unit diagnostics, configuration matrix, and operational observation. |
| Static/build gate | Type, dependency, schema, compilation, and policy constraints. | Runtime behavior and business outcome. | Behavioral tests and rollout evidence. |
| Benchmark/load test | Quantitative response under a frozen workload. | Other workloads, long-term effects, and owner value judgment. | Baseline, profiler, uncertainty, and production metrics. |
| Human review or owner acceptance | Meaning, tradeoffs, policy, and residual risk. | Hidden technical defects and reviewer bias. | Reproducible technical evidence and dissent record. |

Two checks are not independent merely because they are different commands. A unit test and integration test that share the same incorrect expected value can agree for the wrong reason. Select methods whose observation models can expose different material errors.

**Context strategy choices**

| strategy | use when | tradeoff | hard boundary |
| --- | --- | --- | --- |
| Complete read | Artifact is small or every section matters. | Highest context cost, lowest selection risk. | Do not truncate a required complete input. |
| Search plus complete selected sections | Artifact is materially large and the decision is local. | Efficient but depends on complete candidate retrieval and sound selection. | Index/search must return every match and selected sections must be read whole. |
| Deterministic structural index | Repeated edits need exact spans, hashes, headings, and stale-base rejection. | Adds index lifecycle and invalidation work. | Canonical artifact remains authoritative; no body copies or editorial scoring. |
| Summary checkpoint | Resume orientation and progress state. | Compact but lossy. | Never substitutes for canonical content required by the phase. |
| Explicit global-review phase | Cross-section consistency or final acceptance requires everything. | Expensive but honest about scope. | Persist review checkpoints and use measured input formulas. |

**Naming choices**

| choice | benefit | risk | decision rule |
| --- | --- | --- | --- |
| Four-word generated name | High semantic density and consistent retrieval. | Awkward vocabulary or conflict with ecosystem idiom. | Use where feasible for new internal symbols. |
| Existing public name | Compatibility and user familiarity. | May remain terse or inconsistent. | Preserve unless an authorized migration outweighs breakage. |
| Wrapper or adapter | New clear internal contract without immediate public break. | Additional layer and maintenance. | Use when it isolates compatibility cleanly and is tested. |
| Domain-native concise term | Matches ubiquitous language. | Automated word-count rule may reject it. | Prefer semantic accuracy over mechanical count and record exception. |

**Measurement choices**

| state | permitted claim | prohibited claim | next action |
| --- | --- | --- | --- |
| No baseline | Method and open measurement question only. | Target improvement, capacity, percentile, or guarantee. | Define workload, owner, environment, and baseline. |
| Controlled fixture | Causal mechanism under the fixture. | Production or heterogeneous repository generalization. | Add representative target cohort. |
| Representative target sample | Bounded target result with uncertainty. | Universal result or unselected variant claim. | Validate additional cohorts only when decision needs them. |
| Production observation | Behavior under observed traffic and configuration. | Unexercised path or future-state guarantee. | Preserve workload coverage and combine with static/test evidence. |

**Recommended evidence bundles**

| decision | minimum complementary bundle | stop rule |
| --- | --- | --- |
| Narrow behavior correction | Current contract/source, expected failing check, minimal implementation, relevant suite, diff review. | Stop when bounded behavior and regression are verified. |
| New standard feature | Source/owner decision, atomic requirements, bidirectional tests, negative cases, integration, recovery, final review. | Stop when all material claims are verified or explicitly split. |
| Compatibility change | Consumer and data inventory, versioned contract, migration fixtures, rollout/rollback, owner acceptance. | Stop only when supported consumers and recovery meet policy. |
| Performance target | Functional equivalence, frozen workload, baseline/candidate design, raw results, uncertainty, counter-metrics, owner decision. | Stop when measurement can change the target action or report unresolved. |
| Security or high-assurance claim | Domain requirements, threat model, static/configuration/runtime evidence, adversarial negatives, residual risk, authorized owner. | Stop at domain evidence floor; this digest remains traceability support. |

**Pre-action tradeoff audit**

1. What exact claim and action are being considered?
2. What is the cost, detectability, and reversibility of each plausible error?
3. Which source or owner can legitimately choose the behavior?
4. Which observation classes must the verification bundle cover?
5. Which selected methods share a premise or blind spot?
6. What independent signal would expose the most consequential miss before action?
7. Does this route create a second source of truth or preserve the repository authority?
8. Which option is lost if implementation begins now?
9. Which policy or domain assurance floor overrides cost optimization?
10. What evidence state, deadline, or owner decision ends exploration?

After action, record which route caused rework, which contradiction was caught before implementation, whether context was useful, and whether a cheaper or stronger route would have changed the result. Until comparable local data exists, these choices remain reasoned defaults rather than measured productivity rankings.

Good: reuse an authoritative parser contract, add the missing invalid-input case, demonstrate the pre-fix failure, and avoid a duplicate spec. Bad: write exhaustive WHEN/THEN prose whose tests call the implementation as their expected-value oracle. Conditional: consolidate scattered contracts only when an owner, migration plan, and link/invalidation strategy prevent two competing authorities.

The deeper tradeoff is option preservation. Early evidence should narrow the next choices without committing the team to unsupported values or irreversible migrations. A concise packet is valuable when it creates informative next actions; it stops being valuable when its formality is used to close a decision that only domain, runtime, measurement, or owner evidence can close.

## Local Corpus Hierarchy

Classification vocabulary includes canonical, supporting, historical, current, template, duplicate, conflicting, target-semantic, measured, owner-accepted, unrefreshed, and unknown-authority roles. These roles form a partial order by claim type rather than one universal rank.

**Preserved seed role metadata**

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | observed identity and reviewer question |
| --- | --- | --- | --- |
| `agents-used-monthly-archive/codex-skills-202602/executable-specs-01/references/meta-patterns-reference.md` | canonical primary source | AI-Native Meta-Patterns Digest; measured outcomes; seven principles. | Hash-equal to the 202603, unclassified, and current installed digest copies. What did this exact 202602 snapshot say? |
| `agents-used-monthly-archive/codex-skills-202603/executable-specs-01/references/meta-patterns-reference.md` | supporting detail source | AI-Native Meta-Patterns Digest; measured outcomes; seven principles. | Same observed bytes as the 202602 copy. Which guidance persisted at this later path, and what surrounding archive context differs? |
| `unclassified-yet/Executable Specifications Meta Patterns Reference.md` | supporting context source | AI-Native Meta-Patterns Digest; measured outcomes; seven principles. | Same observed bytes as both archive copies. What local routing value does this path provide, and who owns its classification? |

The seed labels are preserved as corpus metadata. No mapped note explains why one hash-identical copy is canonical and the others are supporting. The evolved hierarchy therefore does not invent a rationale or allow those labels to decide current workflow or target behavior.

**Role definitions**

| role | authority | limitation | conflict response |
| --- | --- | --- | --- |
| Canonical historical snapshot | Exact content of a designated dated file. | Designation does not prove empirical truth or current applicability. | Preserve the snapshot and test its claims through current or target evidence. |
| Supporting historical/context copy | Additional path, date, packaging, or rationale around a source. | Hash-equal content contributes provenance, not independent factual weight. | Read surrounding context when the temporal or packaging question requires it. |
| Duplicate content | Same observed bytes under another identity. | Does not add a new observation model. | Read once for meaning, retain every path/hash for provenance. |
| Current workflow guidance | Present installed skill rules and output contract. | Can lag the active repository or be inappropriate for a domain. | Prefer for current local process after repository instructions and applicability review. |
| Current template | Reusable artifact and test shape. | Example values, names, and assertions are not target authority. | Adapt to repository conventions and replace examples with owned values and checks. |
| Target semantic evidence | User/domain decisions, source, configuration, interfaces, tests, build, and runtime observations. | Every mechanism has variant and workload limits. | Prefer for desired and actual program behavior within scope. |
| Measured target evidence | Controlled benchmark, task study, defect review, or operational metric. | Cohort, environment, confounding, and uncertainty limit generalization. | Use for quantitative claims only within the measurement boundary. |
| Owner-accepted decision | Accountable authority chooses behavior or residual risk. | Acceptance is not technical truth outside its scope or duration. | Record authority, evidence reviewed, recovery, and invalidation. |
| Unrefreshed external pointer | Local source contains a public locator and historical description. | No current remote content, version, or availability. | Refresh primary source only when authorized and decision-relevant. |
| Conflicting source | Two sources make incompatible claims under apparently overlapping scope. | A fixed rank can conceal a version, configuration, or policy difference. | Narrow scope, identify owners and versions, and seek a capable deciding mechanism. |
| Unknown authority | Content exists but provenance, owner, or binding status is unclear. | Cannot authorize consequential behavior alone. | Use as a hypothesis or navigation aid and route to an accountable source. |

**Claim-specific precedence matrix**

| claim | first authority | corroborating authority | source that must not overrule it |
| --- | --- | --- | --- |
| What the 202602 digest said | Exact 202602 bytes and archive context. | Hash comparison with other copies. | Current skill cannot rewrite the historical snapshot. |
| What the 202603 or unclassified path contained | Exact bytes at that identity. | Duplicate-family ledger and surrounding package context. | Canonical label on another path cannot erase this path. |
| What workflow is currently documented locally | Current installed `SKILL.md`. | Current templates and interface metadata for consistency. | Historical digest cannot override explicit newer guardrails. |
| Which output shape is available | Current template bytes. | Skill output contract and target repository template. | An inherited example cannot choose target behavior or values. |
| Which requirement the system should satisfy | User, domain, protocol, and policy authority under a stated scope. | Existing source, tests, interfaces, and owner review. | A generic metapattern cannot invent product intent. |
| What the current implementation does | Target source and configuration plus capable build/test/runtime evidence. | Requirement packet and history for intended meaning. | Prose or template cannot override observed behavior. |
| Whether implementation satisfies a contract | Claim-capable project checks and semantic review. | Negative cases, integration, runtime, and owner acceptance as consequence requires. | Packet structure and traceability count alone cannot settle behavior. |
| Whether a number or improvement is real | Controlled measurement with workload, environment, sample, and uncertainty. | Representative target and operational evidence. | Inherited outcome figures, editorial scores, and template numbers cannot settle it. |
| What a public platform currently documents | Refreshed versioned primary source under authorization. | Installed reproduction and target case. | The locally retained URL cannot establish current external behavior. |
| Whether residual risk is acceptable | Accountable project or domain owner under applicable policy. | Technical evidence and reviewer dissent. | A test suite or metapattern cannot assume organizational authority. |

**Observed content families**

| family | identities | SHA-256 | hierarchy consequence |
| --- | ---: | --- | --- |
| Metapattern rationale digest | Four observed local paths. | `78ead044feb402432f104e37f82578f3fad5f161a4df4bec809120cd2eea7882` | One substantive source with four path/date contexts; no multiplied confidence. |
| Current skill | One installed path. | `0647bbf3d63f2b3ad5097017fb888203d4b9125ae58457a61472140477d04066` | Current local workflow authority subject to repository fit. |
| Current template set | One installed path. | `3562fbbdb7506edca27761ac246f75f6d173c18dd96054793e7c0be8d2d59629` | Current shapes and examples, separate from workflow and target evidence. |
| Current interface metadata | One installed path. | `ac7a1cc858b8d126cecb74ab5e4e1a1495d235583c084cbce85859b20a4d36cf` | Invocation presentation only. |

Content identity and contextual identity are distinct. Equal hashes show observed bytes match. They do not show that paths had the same owner, surrounding files, activation, or role.

**Default retrieval route**

1. Start with the complete user request, repository instructions, and existing target contract.
2. Read one representative digest copy for inherited rationale and caveats.
3. Read the complete current skill for new durable work; load complete relevant template sections on demand.
4. Use target source, configuration, tests, build, and runtime evidence for actual behavior.
5. Route quantitative claims to measurement and policy choices to accountable owners.
6. Return to every historical copy only for archive evolution, packaging, or role questions.
7. Refresh a public pointer only when authorization and decision consequence justify it.

This route optimizes orientation. It does not make the first-read source globally authoritative.

**Conflict-resolution rules**

| conflict | resolution |
| --- | --- |
| Digest suggestion and current skill guardrail disagree | Preserve historical guidance; follow current workflow after repository fit, and record the evolution. |
| Template value and owner requirement disagree | Treat template value as illustration and use the owner-approved target with measurement where needed. |
| Requirement and current implementation disagree | Classify bug, migration, compatibility behavior, or mistaken requirement before editing either side. |
| Test and requirement disagree | Inspect assertion capability, source authority, and historical contract; do not choose whichever is green. |
| Two owner sources disagree | Preserve both, identify decision authority and consequence, and block dependent implementation. |
| Target measurement contradicts inherited outcome | Use target measurement for its scope and retain inherited figure only as historical source content. |
| Refreshed public guidance conflicts with installed behavior | Version both, reproduce locally, narrow applicability, and escalate compatibility rather than averaging. |

**Targeted invalidation**

| changed node | reopen | retain unless separately affected |
| --- | --- | --- |
| Historical digest | Claims about that snapshot, duplicate family, and inherited rationale. | Independently verified target behavior. |
| Current skill | Workflow recommendations, context strategy, and output contract. | Historical statements and target evidence. |
| Template | Artifact-shape guidance and examples derived from it. | Approved behavior and tests not dependent on the template. |
| Requirement authority | Desired behavior, tests, implementation, and acceptance linked to that decision. | Unrelated source and historical facts. |
| Target source or configuration | Current behavior claims, pointers, tests, measurements, and decisions under old state. | General method guidance. |
| Test harness | Evidence that depended on its oracle, fixture, environment, or runner. | Requirement intent, unless the failure reveals a contract problem. |
| Workload or environment | Quantitative results and operational applicability. | Pure functional evidence under unaffected assumptions. |
| Owner or policy | Authorization, residual risk, and sufficiency floor. | Technical observations, clearly separated from acceptance. |
| Public primary source | Current external statements and compatibility guidance. | Historical local pointer and prior retrieval record. |

Good historical claim: "The 202602 path contains this guidance and its bytes match three other observed local paths." Good current claim: "The current skill prohibits invented context budgets, and this target workflow measures its required input." Bad claim: "Three local files independently prove that the workflow reduces defects." Conditional concise use: cite one representative digest in prose while retaining the complete duplicate ledger and current-skill identity in the decision record.

The hierarchy is causal and versioned: rationale informs workflow, workflow and templates help compile requirements, target evidence supports or refutes them, owners accept bounded decisions, and outcomes inform a later revision. Feedback creates a new trajectory; it must not retroactively strengthen the sources or decisions that preceded it.

## Theme Specific Artifact

Theme specific artifact: **Executable Metapattern Decision Packet**, a compact provenance and invalidation graph for one bounded decision and target state. It links sources rather than copying them, separates behavior claims from measurements and owner choices, and preserves why a check authorizes or blocks an action.

No separate theme artifact was created during this evolution because the authorized write surface contains only this reference, its question packet, and the Delta journal. The schema below is the completion contract for a future authorized implementation decision.

**Completion profiles**

| profile | use | required depth | explicitly unnecessary unless consequence changes |
| --- | --- | --- | --- |
| `lightweight_reuse` | A current authoritative requirement and regression check already settle a reversible narrow change. | Decision identity, source/test identity, expected failure or regression reproduction, changed path, relevant result, stop reason, and invalidation. | New requirement catalog, broad source map, quantitative study, or owner approval beyond existing policy. |
| `standard_implementation` | New feature, behavior correction, review handoff, or repeated agent work. | Full source/evidence ledger, atomic requirements, bidirectional verification, negative cases, TDD states, implementation boundary, project checks, contradictions, recovery, and invalidation. | Domain assurance beyond the claim's actual consequence. |
| `high_assurance` | Security, compliance, destructive migration, broad compatibility, production risk, or material absence/completeness claim. | Standard profile plus domain authority, variants, threat or failure model, independent checks, runtime/operational evidence, residual risk, rollback, and accountable acceptance. | No relevant omission may be silent; unavailable evidence remains a blocker or explicit owner-accepted risk under policy. |

Profiles prevent both bureaucracy and under-specification. A parser typo can reuse a current contract. A destructive migration cannot inherit that lightness merely because both changes have tests.

**Block A: packet and decision identity**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `packet_identifier` | Stable unique identifier for the decision and revision; do not encode an unverified conclusion in the name. | Issue, review, incident, or local decision sequence. |
| `packet_profile` | Select a profile and explain how consequence, reversibility, novelty, and lifespan justify it. | Tradeoff and reliability sections plus project policy. |
| `user_goal_statement` | State the concrete actor-visible outcome, affected boundary, and desired action. | User request and repository context. |
| `decision_question` | Phrase one falsifiable decision per claim branch; split functional, quantitative, compatibility, and owner-policy questions. | User journey and claim decomposition. |
| `non_goals` | List behavior, systems, consumers, variants, and optimizations deliberately outside scope. | User and owner confirmation. |
| `decision_consequence` | Describe false-positive and false-negative effects, reversibility, detectability, and who bears risk. | Domain context and change plan. |
| `decision_owner` | Name who can choose desired behavior and who can accept remaining risk. | Project ownership and policy. |
| `packet_state` | Use `collecting`, `specified`, `red_observed`, `green_observed`, `verification_ready`, `verified_for_scope`, `refuted`, `unresolved`, or `invalidated`, with actor and time. | State transitions and gate outcomes. |

Prohibited state values include "looks good," unexplained confidence percentages, or "safe" without a named scope and authority.

**Block B: target, source, and authority identity**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `target_identity` | Repository/service/artifact root, revision, branch when relevant, working state, deployment/configuration identity, and sensitive-data boundary. | Version control, environment, and project metadata. |
| `instruction_chain` | Record every applicable user, repository, directory, language, and domain instruction with precedence. | Active instruction files and task context. |
| `source_registry` | Assign stable evidence IDs with path/URL, hash/version, date, scope, authority, and complete-read or selected-section state. | Local corpus and target evidence. |
| `duplicate_and_conflict_state` | Group hash-equal sources, preserve path identities, and record unresolved contradictions without voting. | Hash ledger and source comparison. |
| `external_evidence_state` | Mark unrefreshed pointer, refreshed primary fact, locally reproduced, conflicting, inaccessible, or not applicable. | External research result card. |
| `owner_authority_state` | Record owner role, exact decision accepted, date, policy basis, and limitations. | Review or approval mechanism. |
| `source_invalidation` | Name hash, version, configuration, policy, or owner change that reopens dependent claims. | Source dependency graph. |

**Block C: evidence item registry**

Every material observation receives an identifier such as `EVIDENCE-001`; identifiers are references, not confidence scores.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `evidence_identifier` | Unique stable identifier inside the packet. | Packet-local sequence. |
| `evidence_type` | Use historical fact, current guidance, template example, target source, project check, measurement, runtime observation, owner decision, external fact, inference, illustration, or unresolved. | Evidence-boundary taxonomy. |
| `evidence_locator` | Exact path/range, hash, test, command, output row, trace, review, or direct URL. | Source and verification systems. |
| `evidence_observation` | State only what was observed without embedding the decision inference. | Raw source or retained result. |
| `evidence_scope` | Record revision, configuration, workload, sample, actor, and exclusions. | Target and experiment identity. |
| `evidence_reproduction` | Give the smallest authorized mechanism and expected observable result. | Verification gate set. |
| `evidence_claim_links` | Link support, refutation, context, or authority to claim identifiers. | Claim registry. |
| `evidence_freshness_trigger` | Name the change that invalidates reuse. | Source and target dependency graph. |

Do not paste whole repositories, long source documents, or opaque screenshots into this block. Preserve stable locators and enough bounded observation for reproduction under policy.

**Block D: claim and requirement registry**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `claim_identifier` | Stable packet-local identifier for one factual, behavioral, quantitative, or policy claim. | Decision decomposition. |
| `claim_text` | Bounded falsifiable statement with actor, condition, and scope. | User goal and evidence registry. |
| `claim_state` | Candidate, observed, inferred, specified, verified for scope, refuted, unresolved, or invalidated. | Promotion gates. |
| `claim_consequence` | Link to the exact action and error cost affected. | Decision identity. |
| `supporting_and_refuting_evidence` | Keep support, contradiction, and alternatives distinct. | Evidence registry. |
| `requirement_identifier` | Stable `REQ-<DOMAIN>-<NNN>.<REV>` or repository-native equivalent. | Current skill and project convention. |
| `trigger_and_preconditions` | State the condition, actor, input validity, and relevant system state. | Domain contract. |
| `observable_outcome` | One behavior per clause or explicitly coupled transaction invariant. | Requirement authoring review. |
| `failure_and_edge_behavior` | Empty, invalid, boundary, concurrency, cancellation, timeout, unavailable dependency, and recovery where material. | Failure model and anti-pattern registry. |
| `quantitative_constraint` | Include units, workload, environment, statistic, owner, and method, or mark unresolved. | Measurement packet. |
| `compatibility_and_migration` | Name supported consumers/data, transition, deprecation, rollback, and version scope. | Interface and history evidence. |
| `sufficiency_and_invalidation` | State promotion threshold, owner, and exact premise changes that reopen the claim. | Reliability profile and source graph. |

Confidence attaches to each claim, not to the packet. Functional correctness can be verified while a latency target remains unresolved.

**Block E: bidirectional verification matrix**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `check_identifier` | Stable test, review, benchmark, build, runtime, or owner-check identity. | Project verification surface. |
| `requirement_links` | Link every check to the requirements or documented invariants it observes. | Claim registry. |
| `check_type_and_layer` | Unit, property, type/schema, integration, contract, static/build, benchmark, runtime, review, or approval. | Verification tradeoff guide. |
| `fixture_or_workload` | Exact inputs, state, dependencies, variants, and sample-selection rule. | Test/measurement design. |
| `assertion_or_decision_rule` | State independently observable pass and fail behavior. | Requirement text and oracle. |
| `expected_failure_reason` | Record why the pre-implementation or regression check must fail and which unrelated failures would invalidate the run. | Red evidence. |
| `coverage_and_no_claim_boundary` | State what a pass leaves unobserved. | Risk and variant model. |
| `reverse_traceability_result` | Record orphan checks, undocumented invariants, or conflicting expectations. | Complete matrix audit. |

**Block F: TDD and implementation ledger**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `test_skeleton_state` | Record check intent, interface, fixture, and expected failure before production behavior is added. | Verification matrix. |
| `red_observation` | Exact failing check, reason, target identity, and absence of unrelated blocking failures. | Captured project output. |
| `green_change_boundary` | Smallest changed paths and behavior needed to satisfy the contract. | Diff and implementation plan. |
| `green_observation` | Exact direct checks that pass and any still-red independent branches. | Test results. |
| `refactor_decision` | Structural improvement, preserved behavior, alternatives rejected, and scope guard. | Source review and tests. |
| `full_verification` | Relevant complete suite, build/static checks, configuration/variant checks, and limitations. | Repository-native commands. |
| `changed_path_ownership` | Attribute each touched path and preserve unrelated workspace changes. | Status and owner map. |
| `implementation_recovery` | Rollback, feature control, migration recovery, or diagnostic route if the premise fails. | Project operations. |

**Block G: measurement and nonfunctional claims**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `measurement_hypothesis` | One causal change, expected metric direction, and decision effect. | Performance method. |
| `baseline_and_candidate` | Producer/code identity, relevant config, and unrelated-change exclusion. | Version control and experiment design. |
| `workload_and_environment` | Population, distribution, concurrency, data, hardware, software, cache, and load. | Benchmark or operational packet. |
| `sample_and_statistics` | Raw count, failures, exclusions, quantile method, uncertainty, and outlier policy. | Measurement output. |
| `quality_countermetrics` | Functional equivalence, errors, coverage, resource shifts, and downstream outcome. | Test and observability evidence. |
| `measurement_result_state` | Unexecuted design, diagnostic observation, controlled result, representative result, or operational observation. | Evidence taxonomy. |
| `measurement_owner_decision` | Adopt, reject, investigate, reroute, or choose target with rationale. | Accountable owner. |

**Block H: mismatch, uncertainty, and route ledger**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `mismatch_identifier` | Stable ID and earliest pipeline stage. | Failed gate or contradiction. |
| `expected_and_actual` | Separate expectation from exact observation. | Contract and result. |
| `bounded_hypotheses` | Plausible source, authority, requirement, oracle, implementation, configuration, workload, or policy causes. | Anti-pattern registry. |
| `distinguishing_check` | Smallest mechanism that separates leading causes. | Verification routes. |
| `resolved_or_unresolved_cause` | Confirmed mechanism or honest unresolved alternatives. | Diagnostic result. |
| `affected_claims` | Every claim, check, action, or measurement invalidated. | Dependency links. |
| `route_and_return_contract` | Destination capability, evidence expected back, owner, and stop condition. | Adjacent routing. |

Unresolved is a valid state. A complete-looking form must not force a cause or conclusion.

**Block I: decision, handoff, and invalidation**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `verification_outcome` | Pass, fail, contradiction, not applicable with reason, or not run with blocker. | Captured gate. |
| `decision_result` | Proceed, proceed within scope, revise, reject, or escalation required per claim. | Claim and owner ledger. |
| `authorized_change_boundary` | Files, interfaces, data, configs, rollout, tests, and non-goals included. | Approved plan. |
| `residual_risk_and_owner` | Remaining uncertainty, consequence, accountable acceptance, review date, and policy. | Owner decision. |
| `rollback_or_recovery` | Exact reversal or containment and evidence to inspect after failure. | Project operations. |
| `invalidation_matrix` | Source, requirement, code, test, environment, workload, owner, and policy changes mapped to dependent claims. | Provenance graph. |
| `next_action` | Nonempty executable step, owner, prerequisite, and stop condition. | Unresolved or accepted work. |
| `handoff_summary` | Highest-signal changed paths, checks, results, blockers, and identities without replacing canonical fields. | Packet review. |

**Packet acceptance checklist**

A standard or high-assurance packet is accepted only when:

- the decision, owner, target, instruction, source, and working-state identities are reconstructable;
- source duplicates and conflicts are explicit, and external evidence is accurately typed;
- every material behavior has an atomic requirement or documented coupling;
- quantitative values have owned measurement evidence or remain unresolved;
- every material requirement has a capable check and every behavior-defining check has an explained requirement/invariant;
- expected failure evidence demonstrates oracle sensitivity;
- negative, compatibility, configuration, concurrency, and recovery cases match consequence;
- implementation stayed inside the authorized boundary and preserved unrelated changes;
- contradictions reopen dependent claims rather than disappearing into prose;
- each verification pass states what it leaves unproven;
- split claim outcomes, residual risk, rollback, invalidation, and next action are nonempty;
- retained evidence follows project privacy and access policy.

**Quality contrast**

Good packet: links an owner-approved idempotency key policy to replay and concurrency requirements, independently observable checks, pre-fix failures, a bounded implementation, recovery, and a separate unresolved performance branch.

Bad packet: pastes a green test log, assigns an unexplained reliability percentage, omits configuration and owner, and declares the service safe.

Recoverable packet: preserves current source, requirements, and direct check results but lacks historical intent. It can support the observed behavior under the current revision; migration or policy claims remain downgraded until authority is reconstructed.

The packet is a human-readable provenance graph: sources and owners support or refute claims; claims compile into requirements; checks test requirements; evidence authorizes bounded actions; changes invalidate dependent nodes. For durable work, this permits review of the smallest changed evidence cut. For narrow reuse, the reduced profile prevents the artifact from costing more than the decision it protects.

## Worked Example Set

All repositories, symbols, requirements, checks, and outcomes in this section are illustrative. The examples use mechanisms supported by the local sources, but no target fixture was created or executed during this assignment.

Every example answers the same questions:

| field | question |
| --- | --- |
| Decision | What bounded action or explanation is being considered? |
| Authority | Which source or owner can choose or establish the behavior? |
| Contract | What falsifiable claim controls the action? |
| Expected failure | How can the check demonstrate sensitivity before acceptance? |
| Verification | Which mechanism can support or refute the claim? |
| Missing evidence | What remains outside the observation model? |
| Bounded conclusion | What can be said or done now? |
| Rejected overclaim | Which tempting statement exceeds the evidence? |
| Invalidation | What change reopens the result? |

**Example 1: Reuse an authoritative parser contract**

Decision: Correct a parser that currently accepts a trailing delimiter even though the repository's versioned grammar and existing negative fixture reject it.

Authority: The versioned grammar is the behavior contract; current parser source establishes implementation; the existing fixture establishes a check candidate.

Route: Do not create a parallel specification packet. Link the grammar clause and fixture, reproduce the current wrong acceptance, then implement the smallest correction.

| evidence | illustrative observation | interpretation |
| --- | --- | --- |
| Grammar source | Trailing delimiter is prohibited for the active format version. | Desired behavior is already authoritative. |
| Existing negative fixture | Input exists but no assertion covers the active parser entry point. | Reuse data, strengthen the capable check. |
| Pre-fix run | Active entry point accepts the prohibited form. | Valid Red evidence if harness and version identity are correct. |
| Post-change run | Prohibited form fails with the documented error and valid neighboring forms still parse. | Bounded behavior correction under the selected grammar version. |

Missing evidence: Other format versions and downstream consumers may have compatibility requirements. Rejected overclaim: "The parser is fully compliant." Invalidation: grammar version, parser entry point, error contract, or consumer-support policy changes.

Future replay: A fixture should contain the prohibited input, valid adjacent boundaries, and an older version case. It should fail if the implementation accepts the delimiter or if the new check accidentally rejects the supported older behavior.

Transferable rule: Prefer a current native contract over creating a second source of truth.

**Example 2: Convert an unmeasured target into an experiment**

Decision: Respond to "make export generation twice as fast" when no baseline, workload, environment, or owner-approved threshold exists.

Authority: The requester can define user consequence; target measurements establish current performance; an owner chooses an acceptance bound after evidence.

Contract state: Functional equivalence can be specified now. The improvement value remains a hypothesis, not an acceptance criterion.

| packet item | illustrative content | state |
| --- | --- | --- |
| Functional contract | Same selected records, ordering, encoding, and error behavior. | Specified and testable. |
| Workload question | Representative record counts, field distributions, output sizes, storage, and concurrency. | Unresolved until owner/workload input. |
| Experiment | Baseline/candidate under frozen source, environment, cache design, and repeated observations. | Designed but unexecuted. |
| Quality counter-gate | Structured output equivalence, errors, memory, and downstream compatibility. | Required before any performance adoption. |

Good conclusion: "The method for evaluating the optimization is defined; no speed result exists yet." Bad conclusion: "The change must achieve 2x because the requirement says so." Borderline experiment: a provisional internal target can guide a spike if isolated, owner-bound, expiring, and barred from production acceptance.

Future replay: Run a controlled baseline and a deliberately incorrect faster candidate that omits records. The quality gate must reject the candidate despite lower duration.

Transferable rule: A quantitative aspiration becomes executable only after workload, measurement, and decision authority exist.

**Example 3: Adapt four-word naming for compatibility**

Decision: Improve semantic clarity around a public SDK method named `send`, whose callers and generated clients depend on the existing name.

Authority: Published API compatibility policy and consumer inventory govern the public symbol; the metapattern offers an internal naming default.

Alternatives:

| option | benefit | cost | evidence needed |
| --- | --- | --- | --- |
| Rename public method immediately | Clearer new name. | Breaking clients, docs, serialized references, and generated bindings. | Authorized breaking release and migration plan. |
| Keep public method and improve documentation only | No compatibility break. | Internal ambiguity may remain. | Consumer review and clarity assessment. |
| Keep `send` as adapter to a descriptive internal function | Preserves public API and adds internal semantic density. | Extra layer and two names to maintain. | Compatibility tests, forwarding behavior, error equivalence, and deprecation decision. |

Bounded conclusion: A four-word internal name is useful only if the adapter preserves all public semantics and the added layer pays for clarity. Rejected overclaim: "All functions must have exactly four words." Invalidation: breaking-release policy, caller inventory, or API ownership changes.

Future replay: A compatibility fixture should compile or invoke old clients, compare outputs and errors through both paths, and fail if the adapter changes behavior.

Transferable rule: Preserve the semantic intent of naming guidance without making word count more authoritative than compatibility or domain language.

**Example 4: Index a large evolving artifact without replacing it**

Decision: Repeated agents edit a large canonical specification whose complete reread materially consumes context, but most passes affect a few sections.

Authority: The canonical artifact remains the source of truth; the current skill and template define deterministic index and selected-read contracts.

Design:

- Generate a byte-deterministic index from exact canonical bytes.
- Include artifact hash, exact heading text, complete section spans and hashes, provenance IDs, and direct links.
- Return every lexical candidate for the incoming packet; do not silently cap matches.
- Require the agent to read every selected section completely before editing it.
- Reject stale-base edits and rebuild the index atomically after save.
- Switch to an explicit global-review phase when every section matters.

Missing evidence: The artifact's actual size, churn, retrieval distribution, and model context constraints must show that indexing is worthwhile. Rejected overclaim: "A summary file is a safe replacement for the specification." Invalidation: canonical hash, heading/span algorithm, packet query, or index schema changes.

Future replay: Inject a stale hash, duplicate heading, omitted match, overlapping span, and summary-only resume. Every unsafe state must fail before mutation; identical canonical bytes must regenerate identical index bytes.

Transferable rule: Context optimization is valid only when canonical content, complete candidate recall, and stale-state rejection remain intact.

**Example 5: Reject a tautological test oracle**

Decision: Verify a pricing transformation whose proposed test computes expected totals by calling the same helper used by production code.

Authority: Product pricing rules define behavior; test fixtures or an independent model should encode expected outcomes.

Bad check:

```text
expected = production_price_helper(input)
actual = endpoint(input)
assert actual == expected
```

The check can pass when the shared helper is wrong. A better bundle uses hand-derived boundary examples reviewed against policy, a small independent model or property where appropriate, and an endpoint integration check that includes rounding and error semantics.

Expected-failure test: Deliberately mutate a known rule in the production helper or run against the pre-fix defect. The independent oracle must fail on the intended output difference. Missing evidence: A few examples do not establish every promotional combination or currency rule.

Bounded conclusion: The revised oracle detects the named rule and selected boundaries. Rejected overclaim: "All pricing behavior is correct." Invalidation: policy version, currency/rounding mode, product class, or oracle implementation changes.

Future replay: Include a mutation that both production and the original shared-helper test would accept. The independent check must catch it.

Transferable rule: A check is executable evidence only when it can disagree with the implementation for the right reason.

**Example 6: Make a runbook human-executable**

Decision: Update a recovery runbook for a stuck background job when part of the gate requires authorized human judgment rather than program code.

Authority: Operational policy, service owner, and current system controls define permitted recovery; a safe nonproduction fixture can test instructions.

Contract:

- Given a job in the documented recoverable state, an authorized operator can identify the owning workload and last successful checkpoint.
- The procedure refuses recovery when ownership, environment, or checkpoint identity is ambiguous.
- A successful replay changes only the intended job state and records correlation, actor, and outcome.
- A failed replay leaves containment and escalation instructions rather than recommending blind repetition.

Verification: An unfamiliar reviewer follows the runbook against a safe fixture containing a valid job, stale checkpoint, wrong environment, and missing authorization. The reviewer records every step that was ambiguous or unsafe.

Missing evidence: A fixture does not establish behavior of every production integration or operator under incident pressure. Rejected overclaim: "The runbook guarantees recovery." Invalidation: UI/CLI, permission model, checkpoint schema, service ownership, or recovery policy changes.

Future replay: The test must reject stale and unauthorized cases and demonstrate that a current valid case reaches the expected state without collateral mutation.

Transferable rule: Executable means a capable acceptance mechanism can fail unambiguously; it does not require every gate to be automated.

**Good, bad, and borderline synthesis**

| classification | behavior | promotion or downgrade trigger |
| --- | --- | --- |
| Good example | Uses the strongest applicable authority, preserves unknowns, proves expected rejection, and limits the conclusion to observed evidence. | Promote only after claim-specific gates and owner scope pass. |
| Bad example | Copies form, numbers, names, or green output while hiding authority, oracle, negative cases, or applicability. | Withdraw or reconstruct before implementation or handoff. |
| Borderline case | Retains a hypothesis, stale hint, or lightweight reuse only for a reversible narrow action with visible warning. | Promote through missing gates before broader use; downgrade immediately after invalidation. |

**Fixture promotion criteria**

Promote an explanatory example into an executable regression fixture when the mechanism recurs or has severe consequence, can be represented without sensitive data, has deterministic expected state differences, and has an owner. The fixture should record the unsafe inference it prevents, positive and negative cases, producer and environment identity, and retirement conditions. Do not create fixtures merely to mirror every paragraph; preserve cases whose replay protects a real decision boundary.

## Outcome Metrics and Feedback Loops

No outcome values were measured while evolving this reference. The measures below are future capture definitions, not current results, universal targets, or claimed productivity gains. Establish local baselines under stable definitions, retain raw evidence and cohort identity, and refuse comparison when task, template, repository, reviewer, or sampling policy changes materially.

Leading indicator: every material shipped behavior claim has a stable requirement or invariant identity, current source authority, a capable verification link, and explicit evidence state. Count and review material claims; do not reward creating extra IDs.

Failure signal: the packet describes test-driven or executable work without demonstrating that the check could reject the pre-implementation behavior for the intended reason, or without showing final claim-capable evidence.

Review cadence: run focused structural gates after every atomic reference/packet edit; review semantics at section and complete-file boundaries; refresh external evidence only after a relevant upstream change or decision trigger; review templates and routing after recurring mismatches or severe escapes. Do not invent periodic schedules without workload and owner evidence.

**Metric card contract**

Every reported measure includes:

| field | completion rule |
| --- | --- |
| Decision purpose | Name the template, route, gate, or implementation choice the result can change. |
| Definition | State numerator, denominator, unit, inclusion, exclusion, deduplication, and materiality rules. |
| Cohort | Record repository, revision range, task and risk profile, language/framework, template/skill version, agent/reviewer population, and period. |
| Sampling | State exhaustive, random, stratified, risk-based, fixture, or incident selection and why it represents the claim. |
| Raw evidence | Retain requirement/check IDs, source locators, decisions, reversals, defects, timings, or recalculation source. |
| Counter-metric | Name the quality or safety signal that prevents optimizing the measure alone. |
| Uncertainty | Report sample size, missing data, known bias, reviewer disagreement, and no-comparison state. |
| Trigger | Define what change prompts investigation rather than an unsupported universal threshold. |
| Action | Choose fix, adapt, reroute, retire, collect evidence, or no change. |
| Invalidation | State which definition, source, template, tool, repository, reviewer, or policy change breaks comparability. |

**Deterministic integrity gates**

These gates establish enumerated properties, not semantic effectiveness.

| gate metric | definition | pass interpretation | what it does not prove |
| --- | --- | --- | --- |
| `source_identity_complete` | Every material source has required path/version/hash, scope, authority, read state, and freshness classification. | Source claims are reconstructable. | Source truth, applicability, or owner authority. |
| `packet_shape_complete` | Required profiles, blocks, fields, IDs, and nonempty next actions satisfy the chosen schema. | Packet can be parsed and reviewed. | Requirement correctness or useful detail. |
| `requirement_link_complete` | Every material requirement links to at least one capable candidate check and every behavior-defining check links back to a requirement or documented invariant. | No structural orphan remains. | Oracle independence or adequate negative cases. |
| `expected_failure_recorded` | Every new/corrected behavior has a pre-implementation failure or justified regression reproduction with reason. | Detection intent is documented. | That the failure was caused by the exact behavior unless reviewed. |
| `quantitative_claim_packet_complete` | Every accepted numeric claim has units, workload, environment, sample, method, uncertainty, owner, and raw evidence. | Quantitative provenance fields exist. | Measurement validity, representativeness, or value judgment. |
| `invalidation_route_complete` | Every durable claim names premise changes, dependent claims, owner, and replay route. | Reuse lifecycle is explicit. | That invalidation will be noticed promptly. |

All deterministic gates can pass while the behavior or oracle is wrong. Never sum them into one accuracy score.

**Sampled requirement and verification quality indicators**

| indicator | numerator | denominator | required stratification | misuse warning |
| --- | --- | --- | --- | --- |
| `requirement_falsifiability_rate` | Sampled material requirements for which a reviewer can construct a clear pass and fail case from the text. | All sampled material requirements. | Functional/nonfunctional, novelty, risk, domain, and author. | Reviewer agreement does not establish product correctness. |
| `check_capability_rate` | Sampled linked checks that fail under a representative injected violation of the mapped requirement. | Sampled links with completed fault or mutation review. | Test layer, oracle type, language, failure class, and consequence. | Easy mutations can overstate capability against real defects. |
| `negative_case_coverage` | Sampled requirements whose consequence-relevant invalid, boundary, concurrency, cancellation, dependency-failure, and recovery cases are explicitly handled. | Sampled requirements for which those classes are applicable. | Requirement type and risk profile. | Counting cases rewards fragmentation unless semantic adequacy is reviewed. |
| `bidirectional_traceability_resolution` | Audited orphan requirements/checks that are linked, removed, or explicitly documented after review. | All orphan items found in the audited cohort. | Origin, age, layer, and behavior importance. | Forced links can hide genuine undocumented behavior. |
| `preimplementation_contradiction_capture` | Material source, owner, requirement, or test contradictions resolved or isolated before implementation commitment. | Material contradictions identified in the cohort. | Conflict type and consequence. | More contradictions can reflect better detection rather than worse inputs. |
| `expected_failure_semantic_hit` | Reviewed Red observations caused by missing/wrong target behavior rather than setup, syntax, permission, or unrelated failure. | Reviewed Red observations. | Test layer, harness maturity, and change type. | A valid Red does not prove final coverage. |
| `reviewer_reconstruction_success` | Packets another reviewer can use to identify decision, sources, requirements, evidence, blockers, and next action without original conversation. | Packets audited for handoff. | Profile, age, reviewer familiarity, and task complexity. | Familiar reviewers may fill gaps implicitly. |
| `invalidation_localization_rate` | Known premise changes correctly mapped to every dependent claim and no unrelated claim. | Invalidation events audited. | Source, requirement, code, workload, and policy changes. | Do not force a cause to improve the ratio; unresolved dependency is valid. |

Report raw counts alongside ratios. Controlled fixtures and target decisions stay separate cohorts. A small convenience sample must not look equivalent to a stratified review of consequential claims.

**Workflow and context indicators**

| indicator | definition | useful interpretation | counter-metric |
| --- | --- | --- | --- |
| `time_to_first_falsifiable_contract` | Elapsed time from clarified decision to the first requirement later retained and paired with a capable check. | Source routing and decomposition find an actionable boundary quickly. | Final sufficiency and late contradiction; speed can reward premature commitment. |
| `selected_context_usefulness` | Complete source units that support, refute, or materially contextualize final claims divided by inspected units under one unit definition. | Retrieval limits irrelevant reads while valuing eliminated hypotheses. | Missed-source and post-action reversal review. |
| `contract_reuse_acceptance` | Existing contracts accepted after identity, fit, and test review divided by reuse candidates. | Native authority avoids duplicate packets when compatible. | Stale-contract discoveries and duplicate-truth incidents. |
| `route_escalation_yield` | Completed escalations that find confirming, refuting, or boundary-changing evidence. | Stronger routes are selected for consequential uncertainty. | Missed escalation incidents; necessary precaution can legitimately find no contradiction. |
| `packet_maintenance_rework` | Changes caused by schema drift, duplicated truth, stale links, or unclear ownership. | Reveals artifact lifecycle cost. | Downstream defect prevention and handoff success. |
| `reviewer_active_time` | Carefully bounded time spent understanding and deciding, excluding unrelated interruption under a stated method. | Compares workflow burden inside a stable task cohort. | Decision quality, task difficulty, reviewer expertise, and observation effect. |

Collect time and context only when routing or maintenance efficiency is a real decision. Never compare unlike task sizes, risk profiles, repositories, or reviewers without explaining adjustment and uncertainty.

**Downstream outcome indicators**

| indicator | definition | feedback meaning | latency |
| --- | --- | --- | --- |
| `pre_action_claim_reversal` | Claim downgraded or refuted by evidence before implementation or approval. | Often a healthy sign that counterevidence prevented escape. | Immediate. |
| `post_action_evidence_reversal` | Decision reopened after action because a material premise was missed, stale, or misclassified. | Investigate source, requirement, gate, review, and handoff failures. | Delayed. |
| `specification_attributable_rework` | Rework whose verified cause includes wrong, vague, conflicting, or stale executable requirements. | Estimates downstream cost only after causal review. | Delayed and confounded. |
| `escaped_requirement_defect` | Production, integration, or review defect where promised behavior was absent or wrong after the packet claimed sufficient evidence. | High-severity lagging signal and potential gate boundary. | Potentially long. |
| `unsafe_policy_invention_event` | Agent-selected value or behavior reached implementation without legitimate owner/source authority. | Audit clarification and authority gates. | Immediate or delayed. |
| `safe_abstention_or_route` | Consequential claim was explicitly kept unresolved or handed to a capable method before unsupported action. | Shows appropriate negative capability. | Immediate; do not maximize without context. |
| `record_invalidation_timeliness` | Time between known premise change and downgrade/refresh of dependent packet claims. | Tests whether stale acceptance stops being reused. | Event-driven. |
| `reviewer_recovery_success` | Failure record identifies premise, dependents, rollback, and next evidence without full-session reconstruction. | Tests selective recovery and handoff. | Review or incident time. |

A pre-action reversal is not necessarily failure. Discovering that an existing test contradicts a new requirement before code is evidence that the loop worked. A post-action reversal from the same missed conflict is more concerning.

**Feedback routing table**

| observed signal | likely stage | first investigation | possible durable action |
| --- | --- | --- | --- |
| Reviewers cannot construct a fail case. | Requirement | Compound clauses, vague terms, hidden policy, and unobservable outcome. | Rewrite template guidance or route owner decision. |
| Linked checks survive representative violations. | Oracle/test design | Shared implementation premise, weak assertion, wrong layer, or mock boundary. | Add mutation/fault fixture and improve oracle guidance. |
| Orphan checks cluster around compatibility behavior. | Traceability/history | Undocumented legacy contract, migration, or stale test. | Version requirement, add consumer evidence, or retire check with owner. |
| Red observations often fail on setup. | Test harness | Fixture, environment, command, and prerequisite identity. | Improve preflight and classify Red reason explicitly. |
| Performance targets arrive without workload. | Authority/measurement | Template values, copied numbers, owner and baseline gap. | Make unresolved measurement contract mandatory. |
| Packets grow but reconstruction does not improve. | Artifact design | Unused fields, copied evidence, duplicated prose, and hidden key links. | Remove low-value fields and strengthen stable locators. |
| Fast completion correlates with later reversals. | Workflow incentive | Premature clarification, omitted negatives, and skipped full verification. | Add counter-metric and revise completion gate. |
| Severe defect escapes despite structural Green. | Gate overreach | Which deterministic pass was promoted into semantic sufficiency. | Narrow pass language and add capable domain evidence. |

**Good, bad, and sentinel interpretations**

Good: "Under the same template version and stratified task cohort, more reviewed checks detected their mapped injected violations, while post-action reversals and reviewer reconstruction did not worsen. Counts, mutations, and disagreements are retained." This is a bounded local process result, not a universal defect-reduction claim.

Bad: "The new process generated more requirement IDs and tests, so quality improved." Volume can rise through fragmentation and tautology.

Sentinel: one destructive migration defect caused by an undocumented consumer may justify a mandatory consumer-inventory gate even when there are too few events for a stable rate. Preserve it as a causal high-consequence event, not a percentage estimate.

**Feedback loop**

1. Capture a deterministic gate failure, semantic mismatch, route outcome, reversal, or escaped defect with complete identity.
2. Classify the earliest verified mechanism and dependent claims.
3. Decide whether to fix a template, improve a gate, adapt guidance, reroute a claim class, retire a pattern, or gather a better sample.
4. Replay relevant controlled fixtures and a representative target sample under the new version.
5. Begin a new comparable series only when definitions and cohorts remain compatible; retain old results historically.
6. Confirm improvement in the protected decision without degradation of its counter-metric.

The most important feedback outcome may be an earlier stop. If recurring evidence shows that one claim class cannot be specified safely without domain, runtime, or owner authority, success is routing it before formal-looking weak evidence reaches implementation.

## Completeness Checklist

Use this checklist as revisitable phase gates, not a one-pass form. Every completed item points to evidence. Every conditional omission includes a reason tied to the claim. A critical failure blocks dependent promotion even if later boxes were previously green.

**Status types**

| status | meaning | valid evidence |
| --- | --- | --- |
| Machine pass | Deterministic identity, shape, schema, hash, link, syntax, or hygiene property passed. | Captured parser or command result. |
| Semantic reviewer pass | Claim, authority, counterexample, oracle, scope, and interpretation were reviewed. | Decision record with exact evidence locators and rationale. |
| Project behavior pass | Target implementation produced the required observation under named state. | Test, build, static, benchmark, runtime, or operational result. |
| Authorized acceptance | Accountable owner accepted desired behavior or residual risk within policy. | Project approval mechanism with scope and invalidation. |

A machine pass never implies the other three statuses.

**Gate A: reference-construction completeness**

The following rows preserve and strengthen the seed checklist.

| seed requirement | completion evidence | severity if missing |
| --- | --- | --- |
| The role scenario names user, starting state, decision, and trigger. | Section 010 follows a compound request through source audit, branch-specific requirements, verification, split outcomes, recovery, and invalidation. | Stop reference completion because method use remains abstract. |
| The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong. | Section 011 preserves all four and adds production, granularity, verification, context, naming, measurement, and assurance tradeoffs. | Stop out-of-fit recommendations until choice and consequence are explicit. |
| The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning. | Section 012 preserves seed roles, hashes duplicate bytes, defines typed authority, and records unknown role rationale. | Stop source-backed claims until authority and uncertainty are visible. |
| The theme-specific artifact is reviewable without every mapped source. | Section 013 defines decision, evidence, requirement, check, implementation, measurement, mismatch, decision, and invalidation blocks with locators. | Stop durable handoff; narrow direct reuse may continue. |
| Examples cover good, bad, and borderline usage. | Section 014 provides six orthogonal examples, rejected overclaims, replay checks, and lifecycle transitions. | Warn for concise expert notes; stop training/reference completion if boundaries remain abstract. |
| Metrics name a leading indicator and failure signal. | Section 015 defines both plus deterministic gates, sampled quality, workflow, downstream outcomes, counter-metrics, and feedback without claiming results. | Stop outcome claims; workflow can continue without a measurement program. |
| Adjacent routing points to a better reference when this one is not the right fit. | Section 017 must route by missing authority or observation capability and define return/terminal states. | Stop claims outside executable-spec fit until a capable route is named. |

Additional evolution checks:

| requirement | verification | severity |
| --- | --- | --- |
| Exactly 26 original heading levels, texts, and order remain. | Parse live reference and compare with immutable seed. | Critical structural stop. |
| Every evolved section is strictly longer than its seed section. | Compare parsed stripped character lengths. | Critical evolution stop. |
| Packet has 26 sections and 260 exact question headings. | Parse packet and compare each question cycle with the specification. | Critical rationale stop. |
| Packet has 1,560 populated mandatory values with raw and normalized uniqueness. | Parse six ordered fields and normalize with current test helper. | Critical quality stop. |
| Source and outcome claims preserve evidence boundaries. | Audit hashes, local reads, no-browse states, illustrative labels, and measurement language. | Stop or narrow unsupported claims. |
| Exclusive write ownership was preserved. | Review status and scoped diff paths. | Critical shared-workspace stop. |
| Markdown and text hygiene pass. | Check ASCII policy, tables, fences, tabs, whitespace, final newline, clean diff, and prohibited placeholders. | Correct before handoff. |

**Gate B: task fit and authority**

| check | completion evidence | response if failed |
| --- | --- | --- |
| Actor-visible outcome and action are explicit. | Decision statement with non-goals and consequence. | Clarify or route to product discovery. |
| Desired behavior has legitimate authority. | User, owner, protocol, policy, or current repository contract. | Leave claim unresolved; do not invent policy. |
| This digest is the right method for the next question. | Fit rationale and alternatives considered. | Route diagnosis, architecture, security, operations, measurement, or direct search. |
| Write and command boundaries are authorized. | Exclusive paths, side-effect review, and owner. | Continue read-only or stop. |
| Existing contracts and checks were searched before creating new authority. | Reuse/adapt/reject record. | Inspect native sources and prevent duplicate truth. |
| Stop and escalation conditions are known. | Evidence threshold, owner, deadline if needed, and route-away signal. | Define before a successful command can become automatic approval. |

Fit failure can be a complete correct outcome when the claim is transferred with its evidence and consequence.

**Gate C: source and evidence integrity**

| check | evidence | what a pass does not prove | severity |
| --- | --- | --- | --- |
| Every source identity is reconstructable. | Path/URL, hash/version, date, scope, read state, and authority. | Truth or applicability. | Critical for durable claims. |
| Duplicate sources do not multiply weight. | Content-family hash ledger and path identities. | Independent external or target corroboration. | Stop inflated evidence claims. |
| Conflicts and counterevidence are separate. | Mismatch record, owners, and affected claims. | That conflict can be resolved technically. | Stop dependent implementation. |
| External status is accurate. | Unrefreshed, refreshed, reproduced, conflicting, unavailable, or not applicable. | Target applicability without local checks. | Stop current external claims when unrefreshed. |
| Inference and illustration are visible. | Premises, limits, and falsification route. | Empirical frequency or target outcome. | Narrow unsupported wording. |
| Freshness and invalidation are explicit. | Trigger mapped to dependent claims. | Prompt notification after future change. | Critical for reuse. |

**Gate D: requirement quality**

| check | completion evidence | response if failed |
| --- | --- | --- |
| Requirements are atomic or explicitly coupled by one invariant. | Clause review and independent failure cases. | Decompose before implementation. |
| Trigger, actor, state, and observable result are clear. | Reviewer can construct pass/fail examples. | Rewrite vague or hidden preconditions. |
| Invalid, empty, boundary, failure, concurrency, cancellation, and recovery classes are handled where consequential. | Failure-model coverage record. | Add cases or explain nonapplicability. |
| Numeric constraints have units, workload, environment, method, owner, and evidence. | Measurement claim card. | Keep unresolved; do not copy template values. |
| Compatibility and migration obligations are explicit. | Consumer/data inventory, version scope, rollback, and owner. | Block breaking change. |
| Every requirement has source authority and invalidation. | Claim/evidence links. | Downgrade to hypothesis or route. |

**Gate E: verification and oracle quality**

| check | completion evidence | response if failed |
| --- | --- | --- |
| Every material requirement maps to a capable check. | Bidirectional matrix with layer and assertion. | Add mechanism or leave claim unresolved. |
| Every behavior-defining check maps back to a requirement/invariant. | Reverse audit and orphan disposition. | Document behavior, fix stale check, or remove with authority. |
| Oracle is independent enough to catch the named defect. | Fault, mutation, differential, model, or hand-derived expected case. | Redesign check before trusting Green. |
| Expected initial failure has the correct reason. | Captured Red result and unrelated-failure review. | Repair harness or premise before code. |
| Negative and variant checks match consequence. | Risk-stratified test plan. | Strengthen profile or narrow claim. |
| Every pass states its no-claim boundary. | Coverage and applicability field. | Correct overbroad conclusion. |

**Gate F: implementation and refactoring**

| check | completion evidence | severity |
| --- | --- | --- |
| Change begins only after specified and Red states. | Phase ledger and authorized boundary. | Stop premature implementation. |
| Green change is minimal for the reviewed behavior. | Diff-to-requirement review. | Split unrelated feature or refactor. |
| Naming follows semantic intent without breaking compatibility. | API/consumer review and rationale. | Block incompatible mechanical rename. |
| Refactoring preserves contract and remains in scope. | Relevant Green checks and diff review. | Revert or revise structure. |
| Unrelated user/agent changes are preserved. | Status, owner attribution, and scoped diff. | Critical shared-workspace stop. |
| Relevant complete project gates run. | Exact commands, config, results, and limitations. | No implementation-complete state. |

**Gate G: measurement and nonfunctional evidence**

| check | completion evidence | response if failed |
| --- | --- | --- |
| Hypothesis and decision effect are predeclared. | Experiment card. | Keep timing diagnostic only. |
| Baseline/candidate and workload are comparable. | Frozen identities and abort criteria. | Abort or relabel result. |
| Raw counts, failures, statistics, and uncertainty are retained. | Recalculation source. | No percentile or improvement claim. |
| Functional and quality equivalence passes. | Structured outputs and counter-metrics. | Reject optimization despite speed. |
| Owner interprets the result within scope. | Adopt/reject/investigate decision. | Report measurement without policy conclusion. |

**Gate H: handoff, recovery, and lifecycle**

| check | completion evidence |
| --- | --- |
| Each claim has supported, refuted, unresolved, or invalidated state. | Claim cards. |
| Split outcomes cannot silently broaden one another. | Branch-specific decisions and dependencies. |
| Remaining uncertainty has owner, mechanism, release, and stop conditions. | Route ledger. |
| Decision result and authorized change boundary are explicit. | Proceed/revise/reject/escalate record. |
| Rollback or recovery identifies what to inspect after premise failure. | Project recovery plan. |
| Invalidation maps every mutable premise to dependent claims. | Invalidation matrix. |
| Handoff names changed paths, commands, results, blockers, and next action. | Concise summary linked to canonical packet. |
| Sensitive evidence follows project policy. | Storage, redaction, and access review. |

**Gate I: final evolution and complete-file QA**

Before declaring this evolved reference complete:

1. Confirm packet counts `26`, `260`, and `1,560`, with raw and prefix-stripped normalized unique counts both `1,560`.
2. Confirm exact reference heading levels/text/order and all 26 strict seed expansions.
3. Run the assignment-focused verifier and shared invariant tests that do not require another lane to finish.
4. Confirm immutable seed, queue spans, and local source hashes remain unchanged.
5. Check ASCII policy, table shape, fence balance, tabs, trailing whitespace, final newline, prohibited placeholders, and scoped diff.
6. Reread complete packet and reference in slices of at most five sections, persisting each checkpoint.
7. Record Green after production and Refactor after corrections and final focused PASS.
8. Report exact paths, counts, hashes, current global test state, blockers, and next assigned file without opening it early.

**Quality contrasts**

Good: a standard packet links owner-approved behavior to negative and integration evidence, leaves an unmeasured target unresolved, implements only verified branches, and records recovery and invalidation.

Bad: every heading and field exists, all IDs are linked, and a suite is green, but owner authority, oracle independence, configuration variants, and quantitative provenance are absent. This is document completeness without decision completeness.

Recoverable reuse: a current native requirement and regression fixture support a narrow parser correction. If the work later becomes a compatibility migration, the lightweight pass cannot be promoted; consumer, rollout, and owner gates must run.

The checklist is a prerequisite graph. Green propagates forward only from valid premises. Contradiction propagates backward to reopen the earliest false premise and every dependent conclusion. Selective invalidation avoids both ceremonial full replay and unsafe stale reuse.

## Adjacent Reference Routing

Adjacent reference guidance: route when the pending claim requires an authority, observation model, implementation discipline, or operational control that this digest does not supply. Route by the missing capability, not by topic resemblance.

Adjacent reference 1: use executable-specification tooling when the decision is mature enough to compile into contracts and tests; this digest supplies rationale and evidence boundaries rather than replacing the active skill and repository conventions.

Adjacent reference 2: use TDD, language/framework, or code-review guidance after behavior is scoped and implementation quality becomes the next question.

Adjacent reference 3: use completion verification, branch-finish, or release guidance after implementation and evidence are complete; specification evidence does not authorize publishing operations by itself.

Candidate capability names below are route examples, not claims that a binary, skill, connector, credential, or owner is currently available. Read the selected instructions and inspect repository policy before use.

**Capability-gap router**

| unresolved question | digest boundary | primary route or candidate capability | evidence expected on return |
| --- | --- | --- | --- |
| What outcome should the product choose? | Tests cannot select value, policy, or stakeholder preference. | Product discovery, brainstorming, PRD, and accountable owner. | Decision alternatives, user consequence, owner choice, non-goals, and acceptance boundary. |
| How should an actionable request become a formal packet? | This digest is a reference, not the active authoring workflow. | Executable specification skill or repository-native requirement template. | Stable claims, IDs, test matrix, TDD plan, gates, and open questions. Candidate: `executable-specs-01`. |
| What does current code do and where? | Metapatterns do not provide target source navigation. | Direct search, code graph, language server, or repository-native index. | Current revision-bound source, callers/consumers as required, configuration, and observation limits. |
| Why is the system failing? | A desired contract does not establish causal mechanism. | Systematic diagnosis with reproduction and instrumentation. | Reproduction, minimized case, hypotheses, distinguishing evidence, verified cause, fix, and regression. Candidates: `systematic-debugging` or `matt-engineering-diagnose`. |
| Which architecture or dependency boundary should change? | Requirements state desired behavior but not complete structural impact. | Architecture, dependency-map, or design-debate analysis. | Current graph/source evidence, alternatives, blast radius, contracts, ownership, and decision rationale. |
| How should code be implemented idiomatically? | Generic requirement guidance lacks language ownership, type, concurrency, framework, and runtime details. | Applicable language/framework implementation skill and project tests. | Design matching local idioms, compiler/type checks, behavioral evidence, and compatibility boundaries. |
| Does a security, permission, or compliance claim hold? | Traceability cannot substitute for threat and domain assurance. | Security-specific requirements, static/configuration/runtime analysis, adversarial tests, and authorized review. | Threat scope, variants, attack paths, negative evidence, residual risk, and owner acceptance. |
| Does a latency, memory, throughput, or scale claim hold? | A requirement or benchmark plan is not a measurement result. | Benchmarking, profiling, load test, task study, or operational telemetry. | Frozen workload/environment, raw data, uncertainty, quality equivalence, and bounded decision. |
| How should a service be operated or recovered? | Implementation contracts do not define live observability, access, incident state, or change controls automatically. | Runbook, SRE/operations, observability, incident, and owner workflow. | Deployed identity, signals, safe actions, rollback, access, escalation, and runtime evidence. |
| Why and when did a contract or boundary change? | Current packet cannot reconstruct historical intent by itself. | Version-control history, issue/PR archaeology, and decision records. | Dated commit/review/issue identities, exact source changes, recorded rationale, and separated inference. |
| Is the implementation complete and ready to hand off? | Authoring guidance does not perform independent final review. | Verification-before-completion and requesting-code-review workflows. | Fresh commands, diff review, requirement/test reconciliation, residual risk, and no-overclaim audit. |
| Should work be committed, pushed, published, or cleaned up? | This digest grants no repository publication authority. | Finishing-development-branch or project release workflow after user direction. | Confirmed branch scope, intentional changes, checks, commit/push decision, and cleanup ownership. |
| How should one large evolving artifact be edited repeatedly? | Generic context advice is insufficient when exact stale-state and match completeness matter. | Current executable-spec large-artifact protocol and deterministic indexing. | Measured phase inputs, canonical hash, complete index, complete selected reads, atomic save, and explicit global review. |

**Route-entry contract**

Before handoff, record:

| field | required content |
| --- | --- |
| Original decision | User action or explanation and non-goals, not only the latest tool failure. |
| Unresolved claim | One falsifiable behavior, authority, causal, structural, quantitative, or policy question. |
| Consequence | Error cost, reversibility, detectability, owner, and deadline when material. |
| Current evidence | Sources, requirements, checks, results, contradictions, and claim state already established. |
| Earliest verified gap | Intent, authority, source, requirement, oracle, implementation, configuration, runtime, measurement, history, policy, or authorization. |
| Current method boundary | Why more executable-spec work cannot settle the claim or why another route is cheaper and stronger. |
| Destination capability | Observation or authority needed, independent of product name. |
| Expected return | Evidence form that can support, refute, narrow, or safely assign the claim. |
| Stop condition | When to return, proceed, reject, wait, or escalate. |
| Sensitive-data boundary | Source, runtime, credential, customer, or policy data that cannot transfer. |

This packet prevents the destination from restarting generic orientation or losing the original consequence.

**Route-return contract**

The destination returns:

1. Tool, reference, owner, or system identity, version, configuration, and observation scope.
2. Exact claim addressed and why the method can observe or decide something the prior route could not.
3. Reproducible source, test, build, trace, benchmark, history, or decision evidence.
4. Agreement and contradiction with the existing packet.
5. A bounded state: supported, refuted, unresolved, invalidated, or escalation required.
6. Remaining variants, workloads, owners, and invalidation triggers.
7. Updated original decision and dependent claims to reopen.

**Complementary routes**

| gap | primary route | secondary route | why both may matter |
| --- | --- | --- | --- |
| Existing behavior contradicts desired contract | Target source/tests and history. | Owner or product decision. | History explains intent; owner decides whether to preserve, fix, or migrate. |
| Dynamic requirement | Configuration/runtime observation. | Static source and integration test. | Runtime proves selected occurrence; static evidence bounds implementation and unexercised paths. |
| Performance regression | Controlled benchmark/profile. | Functional equivalence and source review. | Performance evidence locates cost; functional checks prevent faster wrong output. |
| Security-sensitive migration | Domain security review. | Compatibility/consumer and operations evidence. | Assurance, rollout, and recovery have different failure modes. |
| Large cross-module refactor | Dependency/architecture analysis. | Executable requirements and language-specific implementation. | Current impact, desired contract, and implementation idiom are separate questions. |
| Requirement-caused incident | Systematic diagnosis. | Packet/history audit. | Diagnosis establishes cause; audit repairs the process and invalidation gap. |

Do not add routes merely to increase evidence count. Add one when it can fail differently in a way that matters to the action.

**Good, bad, and conditional routes**

Good: a runtime duplicate effect is reproduced and sent to diagnosis with the exact idempotency requirement, failing integration trace, configuration, and consequence. The return identifies a transaction boundary defect, updates the implementation claim, and adds a regression.

Bad: a production incident is sent back through requirement rewriting repeatedly. Clearer desired behavior cannot establish why the current system failed.

Conditional: a second static search cannot prove absence, but it may find a direct counterexample that refutes a universal claim cheaply. Use it for falsification, not as independent completeness evidence.

**Loop detection and terminal routes**

Stop routing and escalate to an owner when:

- the same claim returns twice without new evidence, narrower scope, or a changed premise;
- destinations share the material blind spot and no independent mechanism exists;
- required access, credentials, production state, sensitive data, or qualified authority is unavailable;
- sources conflict in a way that changes a consequential action and no designated resolver exists;
- policy or residual-risk acceptance, rather than technical observation, is the unresolved question;
- cost or deadline requires an explicit bounded decision under uncertainty.

Terminal escalation is not an empty handoff. Preserve the claim, evidence, contradictions, unavailable capability, consequence, candidate options, and exact owner decision required.

**Route verification**

A route succeeds when the destination consumes the stated gap, uses capable authority or observation, returns reproducible evidence, updates the original claim, preserves sensitive boundaries, and reduces, refutes, narrows, or safely assigns uncertainty. If none changes, the route added activity rather than information. Reconsider the problem formulation or terminal owner instead of opening another adjacent reference reflexively.

Adjacent routing is an evidence graph: edges mean "this claim lacks this capability," and returns mean "this evidence changes this decision state." That precision keeps specialized tools modular without fragmenting the user's reasoning.

## Workload Model

`combined_evidence_inference_note`: Treat Executable Metapattern Reference Digest as a quality gate operating reference, not as a prose summary.

The seed's `20 requirement IDs or fewer` value is not retained as an operational limit. No local benchmark, context formula, reviewer study, relationship model, or failure threshold supports it. Twenty independent validation clauses can be easy; one security, migration, or cross-system invariant can be difficult. Capacity must be measured from the actual source, claim graph, checks, variants, owners, environment, and assurance profile.

**Reconciled seed workload dimensions**

| workload_dimension_name | evolved boundary | verification_pressure_point |
| --- | --- | --- |
| `primary_usage_surface` | Specification, test, review, implementation, and verification work where ambiguous intent must become executable evidence. | Confirm that the digest changes a bounded next action, rejection, or route rather than adding generic prose. |
| `bounded_capacity_model` | No universal ID count. Bound work by measured source, claim/check relationships, variant and owner complexity, context, tool/runtime cost, and reviewer capacity. | Change mode, scope, or route before required evidence is truncated or silently omitted. |
| `source_pressure_model` | Distinct source families, total bytes/sections, churn, conflicts, authority diversity, external freshness, and required complete-read phases. | Compare every claim against capable current/target authority before following examples. |
| `artifact_pressure_model` | Decision packet size, link graph, reread cost, update frequency, handoff count, and invalidation complexity. | Require a reviewable packet or native equivalent before claiming durable operational use. |

**Workload variables**

| symbol | dimension | why it matters |
| --- | --- | --- |
| `S` | Distinct source families and their complete bytes or semantic sections. | Source discovery, complete reads, conflict review, and freshness cost grow with distinct evidence, not duplicate paths alone. |
| `C` | Material factual, behavioral, quantitative, and policy claims. | Each needs source type, scope, counterevidence, state, and invalidation. |
| `R` | Atomic requirements or explicitly coupled invariants. | Authoring, ownership, change review, and traceability grow with obligations and their relationships. |
| `K` | Checks across unit, property, type, integration, build, benchmark, runtime, review, and approval layers. | Design, execution time, flakiness, environment setup, and oracle review grow with verification surface. |
| `L` | Evidence-to-claim, claim-to-requirement, requirement-to-check, and invalidation links. | Reconstruction and selective rollback depend on link integrity; many-to-many graphs can dominate review. |
| `V` | Relevant configurations, platforms, features, consumers, data versions, workloads, and failure variants. | Assurance can grow combinatorially even when `R` is small. |
| `O` | Owners and authority boundaries. | Conflict, review, risk acceptance, handoff, and decision latency increase with organizational joins. |
| `Q` | Number and diversity of decisions or revisions that reuse the packet. | Determines whether authoring and indexing cost is amortized before state becomes stale. |
| `A` | Canonical artifact bytes, sections, headings, and churn when a large evolving artifact is involved. | Determines whether complete reads or deterministic indexed retrieval is appropriate. |
| `E` | Environments, runners, external dependencies, and runtime states needed for checks. | Setup and reproducibility can dominate the apparent size of the requirement set. |

No scalar describes the complete workload. A packet with many local validation requirements can be straightforward; a packet with one cross-owner availability claim may require several environments, runtime observation, and policy approval.

**Pipeline stage model**

| stage | work | primary growth drivers | evidence output |
| --- | --- | --- | --- |
| Orient and fit | Read request/instructions, inspect existing contracts, choose method and profile. | `S`, ownership, repository maturity, and request ambiguity. | Decision, non-goals, owners, fit, and open questions. |
| Map sources | Read distinct content, hash/version, classify authority, reconcile conflicts and duplicates. | `S`, source bytes, churn, and conflict count. | Source/evidence registry and invalidation. |
| Decompose claims | Split behavior, measurements, policy, variants, and shared premises. | `C`, `V`, domain complexity, and cross-system relationships. | Claim graph and consequences. |
| Author requirements | Define triggers, outcomes, failures, compatibility, and quantitative questions. | `R`, owner decisions, and requirement coupling. | Atomic contract set. |
| Design verification | Select checks, fixtures, oracles, environments, expected failures, and coverage. | `K`, `L`, `V`, `E`, and assurance. | Bidirectional matrix and Red plan. |
| Implement/refactor | Modify authorized paths and preserve compatibility and unrelated changes. | Diff size, language/framework, architecture, and integration count. | Source changes and Green evidence. |
| Verify/measure | Run checks, compare variants, collect measurements, inspect counterevidence. | `K`, `V`, `E`, suite duration, flakiness, and data volume. | Project results and claim states. |
| Review/handoff | Reconstruct decision, resolve mismatches, accept risk, record recovery/invalidation. | `L`, `O`, packet age, consequence, and reviewer familiarity. | Bounded decision and next action. |
| Maintain | Detect stale premises, update links, replay affected checks, evolve patterns. | `Q`, churn, invalidation fan-out, and outcome feedback. | New versioned trajectory. |

**Workload modes**

| mode | operation | best fit | stop or switch signal |
| --- | --- | --- | --- |
| Direct native reuse | Validate one existing contract/check, reproduce failure, apply bounded correction. | Small reversible change with current authority. | Contract conflict, missing negative, broader consumer, or stale identity. |
| Standard packet | Complete current skill and request context, map sources, author claims/checks, implement, verify, hand off. | New bounded feature or durable behavior correction. | Claims span independent systems/owners or assurance exceeds available mechanisms. |
| Indexed incremental artifact | Use deterministic fresh index and complete selected sections for repeated local edits. | Large canonical artifact with material repeated-read cost and local revisions. | Candidate recall is incomplete, stale hashes appear, or every section matters. |
| Explicit global review | Read complete packet, complete canonical artifact, all sections, and cross-section relationships with checkpoints. | Initial/final review, schema migration, or global consistency claim. | Input cannot fit safely; change model/phase or split with a global join contract, never truncate. |
| High-assurance augmentation | Add domain, configuration, runtime, operational, compatibility, and owner evidence. | Security, compliance, destructive migration, or production risk. | Required authority or observation remains unavailable; escalate. |
| Specialized route | Transfer product, diagnosis, architecture, performance, or operations question with its evidence. | Digest cannot observe or decide the consequential gap. | Return when the specified evidence changes the original claim. |

**Favorable workload signature**

- Desired outcome and owner are identifiable.
- Existing source and tests provide current behavior anchors.
- Requirement and variant relationships can be bounded explicitly.
- Project checks are deterministic enough to demonstrate expected failure and final behavior.
- Several decisions or agents reuse the same current packet and source identities.
- Reviewers can reconstruct claim links without loading unrelated source.
- Context optimization, if needed, has complete candidate recall and stale-state rejection.

**Unfavorable workload signature**

- Product or policy choices remain unresolved across several owners.
- Dynamic, security, production, or third-party behavior dominates and cannot be reproduced safely.
- Variant cross-product is material but no sampling or assurance policy exists.
- Canonical source changes faster than packets or indexes can be invalidated.
- Checks are slow, flaky, unavailable, or coupled to implementation oracles.
- Parallel agents share files or decision authority without merge semantics.
- Reviewers cannot understand the link graph within available time and context.
- The packet becomes a second unsynchronized source beside native requirements and tests.

**Safe narrowing contract**

Narrowing sources, claims, requirements, checks, variants, or owners is safe only when:

1. The user decision can be restated entirely inside the narrower boundary.
2. External interfaces, consumers, data, configurations, and owners are listed.
3. No global completeness, compatibility, security, or performance claim is made from local evidence.
4. Cross-boundary behavior has a separate capable route.
5. The narrowed scope reaches tests, implementation, handoff, and invalidation.
6. New evidence crossing the boundary has an expansion trigger.

Arbitrary splitting to satisfy a token or ID count creates a different evidence product; it is not a capacity fix.

**Sharding and multi-agent contract**

| concern | required rule |
| --- | --- |
| Partition | Stable requirement family, component, owner, or evidence boundary; avoid arbitrary equal-size chunks. |
| Shared identity | One global decision, canonical revision, instruction set, and packet schema. |
| Coverage | Union, overlap, and omitted-claim policy are explicit. |
| Shared premises | Common owner decisions, interfaces, data, and nonfunctional constraints have one authority. |
| Cross-shard links | Requirements, checks, consumers, and invalidation edges across partitions are reconciled. |
| Writer ownership | One writer per reference, packet, source file, test surface, or artifact directory. |
| Merge | Structured claim and evidence reconciliation, not concatenated summaries. |
| Conflict | Named owner and deciding mechanism for incompatible requirements or results. |
| Verification | Per-shard gates plus global integration, interface, variant, and recovery gates. |
| Handoff | Every shard persists exact state, blockers, hashes, and next action before merge. |

Parallel work can reduce elapsed time only when tasks and writes are independent. It increases coordination, context, and integration cost; measure both.

**Pressure signals and responses**

| observed pressure | investigate first | avoid | possible response |
| --- | --- | --- | --- |
| Source loading dominates | Distinct versus duplicate bytes, question breadth, churn, and required phase. | Skipping sources silently. | Deduplicate content, use complete selected sections, or declare global review. |
| Requirement count grows rapidly | Compound behavior, repeated variants, duplicated authority, and unnecessary fragmentation. | Enforcing a fixed cap or splitting transaction invariants. | Refactor into families with shared premises and explicit coupling. |
| Traceability matrix becomes unreadable | Many-to-many links, orphan behavior, generated rows, and missing hierarchy. | Removing links solely for presentation. | Use structured queryable representation and focused views over complete data. |
| Variant combinations explode | Equivalence classes, risk, owner policy, and real supported matrix. | Claiming universal coverage from one sample. | Pairwise/risk-based strategy plus hard gates for critical variants. |
| Project verification dominates | Slow/flaky layers, environment setup, wrong test layer, and claim consequence. | Replacing strong checks with fast irrelevant ones. | Test pyramid adjustment, deterministic fixtures, targeted reruns plus final suite. |
| Context compaction recurs | Canonical packet, index freshness, selected sections, and checkpoint quality. | Resuming from summary alone. | Persist and reload canonical required state; change phase if needed. |
| Reviewers cannot reconstruct | Link density, unclear authority, duplicated prose, missing decision hierarchy. | Adding more narrative indiscriminately. | Improve stable locators, claim cards, focused views, and owner routing. |
| Packet stales before reuse | `Q`, source churn, invalidation signals, and native contract availability. | Refreshing ceremonially on a fixed schedule. | Event-driven update, direct native reuse, or retire duplicate packet. |

**Workload measurement card**

| category | measurements |
| --- | --- |
| Identity | Skill/template/packet versions, target revision, working state, profile, phase, and owners. |
| Sources | Distinct families, bytes, sections, complete reads, selected reads, duplicates, conflicts, and freshness. |
| Graph | `C`, `R`, `K`, `L`, `V`, `O`, and cross-boundary joins. |
| Context | Input bytes/tokens where observable, compactions, index size, selected units, and required global units. |
| Execution | Commands, environment setup, wall/CPU time where relevant, failures, retries, and flaky reruns. |
| Review | Active time under a defined method, handoffs, disagreements, blocked owner time, and reconstruction outcomes. |
| Utility | Claims retained, contradictions caught, routes changed, rework avoided/caused, and next decision enabled. |
| Quality | Oracle samples, negative coverage, reversals, escaped defects, recovery, and invalidation timeliness. |

Repeat comparisons only under compatible conditions and disclose instrumentation overhead. Do not extrapolate from one small fixture or one reviewer to a heterogeneous program.

**Optimization impact ledger**

| optimization | likely benefit | evidence-contract impact |
| --- | --- | --- |
| Reuse current native contracts | Avoid duplicate authoring and preserve conventions. | Safe only after identity, fit, negative, and invalidation checks. |
| Deduplicate hash-equal sources | Reduce repeated context. | Preserve path/date provenance and surrounding-role differences. |
| Deterministic index | Reduce repeated large-artifact reads. | Adds index freshness, completeness, atomicity, and stale-base obligations. |
| Focused verification during iteration | Faster feedback. | Final relevant suite and cross-boundary gates remain required. |
| Requirement families | Improve navigation and shared-premise reuse. | Must not hide atomic outcomes or independent invalidation. |
| Parallel independent work | Reduce elapsed authoring or verification time. | Adds exclusive ownership, integration, and conflict resolution. |
| Sample semantic review | Bound review effort. | Requires representative stratification and no universal claim. |
| Native issue/test metadata | Reduce separate packet maintenance. | Must preserve source, counterevidence, recovery, and owner fields. |

Good workload decision: reuse a current contract for one parser behavior, run its expected-failure and regression checks, and avoid a new packet. Bad workload decision: truncate every source and split transaction invariants to stay under an inherited count. Conditional sharding: split a cross-component migration by owned interface only when consumer joins, global revision, integration gates, and rollback are retained.

Workload optimization and reliability are coupled. Every scoping, indexing, sampling, or parallelization change must state whether it alters evidence population, semantic selection, verification strength, freshness, or only presentation. Faster work is valuable only when the bounded decision remains equally or more falsifiable and recoverable.

## Reliability Target

**Reliability objective:** The workflow must produce reconstructable evidence, preserve authority and uncertainty, reject unsupported promotion before consequential action, detect material contract/check mismatches where practical, contain invalidation to dependent claims, and preserve a clear recovery or escalation route.

This is not a promise that every requirement, test, reviewer judgment, or route is correct. Reliability comes from separating deterministic invariants, sampled semantic quality, severe sentinel events, and owner-accepted risk, then controlling how each can authorize action.

**Target types**

| target type | appropriate use | expression | evidence |
| --- | --- | --- | --- |
| Hard invariant | Enumerated structure, provenance, ownership, policy, and promotion rules. | Every item in the defined population satisfies the rule, or dependent state fails. | Parser, complete enumeration, command, or decision-record audit. |
| Sampled indicator | Requirement clarity, oracle capability, route fit, reconstruction, and other task-dependent quality. | Raw counts and locally calibrated trends under a documented sampling frame. | Stratified samples, disagreements, uncertainty, and independent checks. |
| Sentinel event | Rare but severe counterexample such as unauthorized policy invention or destructive migration miss. | One verified event can trigger a gate or boundary review without becoming a rate. | Causal incident or controlled fixture. |
| Owner-accepted risk | Residual uncertainty that cannot or need not be eliminated for the bounded action. | Scope, owner, rationale, date, recovery, and invalidation. | Applicable project authorization mechanism. |

Do not combine these target types into one synthetic reliability score.

**Reconciled seed targets**

| reliability_target_name | evolved target | evidence_collection_method | boundary |
| --- | --- | --- | --- |
| `source_boundary_preservation` | Every material durable recommendation identifies exact source type and distinguishes historical/local fact, current guidance, target observation, refreshed external fact, inference, illustration, owner choice, and unresolved uncertainty. Missing classification blocks handoff. | Claim-to-source audit plus focused parser for structured fields. | Hard documentation invariant; it does not make the underlying claim true. |
| `decision_accuracy_sample` | Review routing decisions through a documented local task sample with raw counts, task/risk classes, reviewer rubric, dissent, consequences, and uncertainty. No universal eighteen-of-twenty threshold is asserted. | Stratified downstream-task review, route-return records, and reversal/defect analysis. | Applies only to sampled workflow, reviewers, repositories, and period. |
| `unsupported_claim_rate` | No accepted production, security, latency, reliability, completeness, compatibility, or policy claim may survive without claim-appropriate evidence, explicit inference where relevant, and verification or escalation. | Complete review of high-consequence final claims and negative tests of promotion gates. | Zero-tolerance policy is enforceable; reviewer detection is not guaranteed perfect. |
| `recovery_path_clarity` | Every avoid, contradiction, invalidation, failure, and accepted-risk case names failed premise, affected claims, containment/rollback, owner, next evidence route, and stop condition. | Decision-packet, failure-mode, and reconstruction audit. | Clear recovery does not guarantee recovery succeeds when access or tooling is unavailable. |

The seed's `100 percent`, `18 of 20`, `zero`, and `every` expressions mixed unlike properties. Exact completion is appropriate for enumerated required fields and policy gates. The unexplained routing fraction is retained only as historical source content; its task population, reviewer definition, and statistical meaning are absent.

**Reliability objective tree**

| dimension | hard objective | sampled/contextual objective | failure response |
| --- | --- | --- | --- |
| Prevention | Do not write outside authorization, invent owner policy, accept unmeasured numbers, or reuse stale evidence knowingly. | Track which fit/source gates prevent unsuitable work. | Stop, clarify, or route before mutation/promotion. |
| Source integrity | Required identity, authority, duplicate, conflict, freshness, and scope fields exist. | Review whether classifications match actual claim fit. | Relabel, narrow, or reject dependent claims. |
| Requirement integrity | Material obligations are falsifiable, sourced, bounded, and have failure behavior. | Sample semantic clarity and omitted risk classes. | Rewrite or route owner/domain decision. |
| Verification integrity | Bidirectional links, oracle review, expected failure, and no-claim boundary exist. | Sample mutation/fault detection and target agreement. | Redesign check and invalidate false Green evidence. |
| Implementation containment | Diff stays inside authorized contract and preserves unrelated work/compatibility. | Review minimality, design quality, and refactor safety. | Split, revert owned change, or revise contract. |
| Measurement integrity | Accepted numeric claims have complete comparable evidence and counter-metrics. | Assess representativeness and decision value. | Relabel diagnostic/unexecuted or rerun correctly. |
| Decision containment | Evidence profile matches consequence and lower-profile output cannot silently promote. | Review route choices and pre-action reversals. | Block, downgrade, or seek owner acceptance. |
| Recovery | Every durable claim has invalidation, owner, rollback, and next-step semantics. | Test reviewer reconstruction after failure. | Update packet, route, fixture, or guidance. |
| Learning | Guidance/template changes create new versioned trajectories. | Trend recurring mismatch and downstream outcomes without pooling incompatible cohorts. | Fix, adapt, reroute, retire, or collect stronger evidence. |

**Reliability profiles**

| profile | reliable outcome | required controls | prohibited promotion |
| --- | --- | --- | --- |
| Lightweight reuse | A current native contract and regression check support one reversible bounded correction. | Target identity, authority, expected failure/reproduction, changed boundary, relevant result, invalidation. | Cannot become broad compatibility, quantitative, security, or completeness evidence. |
| Standard implementation | Source-audited requirements and project checks support a new behavior or scoped change. | Full provenance, atomic claims, negative cases, bidirectional checks, Red/Green/Refactor, final suite, recovery. | Cannot authorize high-assurance claims by default. |
| High assurance | Domain, variant, independent, runtime/operational, recovery, and owner evidence support the consequential action. | Standard controls plus applicable policy floor and residual-risk acceptance. | A structural pass, one reviewer, or one green test cannot substitute for required domain evidence. |

Profile status is not transitive upward. Reusing lightweight evidence in a destructive migration requires the missing gates; adding a warning is not enough.

**Hard reliability invariants for durable work**

1. Every material source and target state is reconstructable and correctly typed.
2. Every requirement has legitimate authority or remains explicitly unresolved.
3. Every material obligation is falsifiable and includes consequence-relevant failure behavior.
4. Every requirement links to a capable check and every behavior-defining check links back.
5. Every changed behavior demonstrates a correct expected failure or justified regression reproduction.
6. Every quantitative acceptance claim has complete measurement identity and owner interpretation.
7. Every verification pass states what it does not prove.
8. Every contradiction reopens the earliest false premise and dependent conclusions.
9. Every unavailable evidence path produces explicit route or owner escalation rather than invented certainty.
10. Every action respects write, data, security, compatibility, and ownership boundaries.
11. Every durable acceptance has rollback/recovery, invalidation, and nonempty next state.

A high sampled reviewer-agreement result cannot compensate for failure of one hard invariant.

**Locally calibrated indicators**

| indicator | purpose | required report | no-claim boundary |
| --- | --- | --- | --- |
| Requirement falsifiability | Detect vague or compound contracts. | Counts, strata, reviewer rubric, examples, disagreements. | Cannot establish desired product behavior. |
| Oracle capability | Detect tautological or wrong-layer checks. | Fault/mutation identity, check layer, result, limitations. | Sample cannot establish all test quality. |
| Negative-case adequacy | Detect omitted error, boundary, concurrency, and recovery behavior. | Applicable classes, requirement consequence, reviewer result. | More cases do not automatically mean stronger coverage. |
| Route-review agreement | Improve fit and adjacent routing. | Task classes, reviewers, rubric, dissent, consequence. | Consensus is not program truth. |
| Reconstruction success | Test provenance and handoff usability. | Packet cohort, reviewer familiarity, missing fields, exact divergence. | Reconstructing a wrong contract does not validate it. |
| Pre-action versus post-action reversals | Separate healthy detection from escaped evidence failure. | Claim, timing, cause, consequence, and affected gates. | Sparse events remain events, not unstable percentages. |
| Invalidation timeliness | Detect stale acceptance reuse. | Premise change, detection time, dependents, response. | Does not prove every invalidation event was detected. |

Set local targets only after enough comparable observations reveal variance and bias. A target must name the decision it protects and the response when missed. This reference supplies no current baseline.

**Consumer reliability obligations**

Consumers must:

- inspect source authority and counterevidence rather than trusting a template label;
- preserve unresolved and refuted claim states;
- review requirement meaning before interpreting traceability counts;
- verify oracle capability and expected-failure reason before trusting Green;
- reject copied target numbers and generalization across untested variants;
- keep lower-profile evidence inside its action boundary;
- preserve unrelated workspace changes and owner scope;
- rerun affected gates after source, requirement, code, test, environment, workload, owner, or policy change;
- avoid counting multiple representations of one evidence pipeline as independent corroboration.

**Failure budget interpretation**

No numeric semantic-error budget is asserted. Response follows event class and consequence:

| event | acceptable containment | required response |
| --- | --- | --- |
| Vague clause caught during review | Rewrite before implementation. | Improve examples or template if recurring. |
| Wrong check link caught before Green | Remove link and add capable mechanism. | Review orphan and oracle class. |
| Expected failure is setup-related | No behavior evidence accepted. | Repair harness and repeat diagnostic state. |
| Performance candidate is faster but changes output | Functional gate rejects adoption. | Diagnose or redefine an explicitly semantic change. |
| Owner-policy invention caught before code | Claim remains unresolved. | Obtain authority or route. |
| Unsupported claim reaches durable handoff | No acceptable state. | Withdraw/narrow claim and audit promotion path. |
| Invalidated packet remains in use | No acceptable durable state once known. | Mark invalid, notify dependents, refresh or retire. |
| Optional explanatory diagram is absent while canonical packet is valid | Acceptable if no decision depends on it. | Record optional loss and continue. |

This consequence-aware model avoids treating all mismatches equally while refusing to normalize severe escapes into an average.

**Verification ladder**

1. Run deterministic identity, shape, link, schema, heading, uniqueness, and hygiene checks.
2. Exercise negative fixtures for source drift, orphan links, wrong oracles, stale hashes, variant gaps, and invalidation.
3. Audit stratified target requirements against authority, direct behavior, and independent checks.
4. Review route and promotion decisions with explicit rubrics and dissent.
5. Analyze pre-action catches, post-action reversals, rework, and escaped defects causally.
6. Confirm changes improve the protected outcome without degrading counter-metrics or silently changing the product.

**Target-language examples**

Good hard target: "Every high-consequence final claim has claim-appropriate evidence, owner or route, recovery, and invalidation; a missing required field blocks handoff." The population and response are enumerable.

Bad empirical target: "At least eighteen of twenty uses are correct, so routing is ninety percent reliable." Without task selection, rubric, reviewers, uncertainty, and consequence, the inference is unsupported.

Conditionally valid report: "In this documented local sample, reviewers agreed on eighteen routes and disagreed on two." This can be raw evidence when the cohort and dissent are retained. It is not a universal guarantee.

Reliability decomposes into prevention, detection, containment, recovery, and learning. A rough requirement candidate can be safe when review rejects it before implementation; a rare undetected owner-policy or migration error can be severe. Bounded propagation and recoverability therefore matter more than an uncalibrated average agreement rate.

## Failure Mode Table

Treat failure as a state transition. Identify the earliest verified stage, preserve diagnostics, reject claims whose integrity cannot be established, and invalidate every dependent decision. Continue only when remaining evidence is both valid and sufficient for a narrowed action.

| handling class | meaning | default action |
| --- | --- | --- |
| `fatal_workflow` | Required input, authority, command, parse, write, or project gate cannot support continuation. | Stop affected work, retain diagnostics, and resume only after a changed premise. |
| `silent_degradation` | Packet or implementation appears complete while source, coverage, oracle, variant, or freshness is weaker than reported. | Detect through invariants and samples, label degradation, and block dependent claims. |
| `claim_blocking` | Some work remains useful, but evidence cannot support the pending conclusion. | Preserve verified branches, downgrade claim, and route to stronger evidence. |
| `optional_output_loss` | Noncanonical presentation or convenience output failed. | Record loss and continue if no decision depends on it. |
| `informational_difference` | Source, environment, template, or tool differs without a contract failure yet. | Capture difference and avoid invalid comparison or reuse. |
| `method_boundary` | The claim requires authority or observation outside executable-spec work. | Transfer with entry/return contract; do not repeat formatting. |

**Intent, authority, and source failures**

| failure_mode_name | class | trigger | observable signal | required mitigation | invalidated or preserved evidence |
| --- | --- | --- | --- | --- | --- |
| source drift hides truth | `silent_degradation` | Local guidance, target contract, code, configuration, or external source changes after packet creation. | Hash/version/revision differs from retained identity. | Mark dependent claims invalid, inspect diff, replay affected gates, preserve prior record historically. | Reopens derived claims; unrelated historical facts remain. |
| generic advice escapes review | `claim_blocking` | Agent copies plausible best practice without theme and target evidence. | Recommendation lacks source type, scope, counterargument, falsification, or target fit. | Stop durable handoff and apply source/evidence/gate chain. | Idea may remain hypothesis; no implementation authorization survives. |
| wrong owner maps successfully | `silent_degradation` | Agent obtains a clear answer from someone without authority over the behavior or risk. | Approval exists but role/scope does not cover the decision. | Identify accountable owner, preserve prior input as context, and reopen policy claim. | Technical observations remain; accepted behavior/risk does not. |
| owner choice is invented | `claim_blocking` | Missing policy, target, or tradeoff is filled from template or intuition. | No user/domain/policy evidence supports selected value. | Downgrade to open question or isolated experiment. | Independent factual and functional branches can remain. |
| duplicate sources inflate confidence | `silent_degradation` | Hash-equal paths are counted as corroboration. | Several citations share bytes or copied language. | Collapse substantive weight and retain path/date provenance. | Source content remains observed; independence claim is invalid. |
| public pointer becomes current fact | `claim_blocking` | Retained URL is cited without retrieval/version/applicability. | No direct source observation or local reproduction. | Relabel unrefreshed, refresh only under authorization and need. | Historical pointer remains; current external claim is invalid. |
| historical outcome becomes current guarantee | `silent_degradation` | Inherited figure or editorial score is reused as target evidence. | No study design, target workload, raw data, or owner. | Preserve historical statement, remove guarantee, define measurement. | Practice rationale may remain; quantitative conclusion does not. |
| wrong instruction scope is applied | `fatal_workflow` | Agent misses newer user/repository/directory instructions or another owner. | Planned edits or commands violate active boundary. | Stop, reread instruction chain and progress, preserve others' changes. | Read-only observations may remain; mutation plan is invalid. |

**Requirement and traceability failures**

| failure_mode_name | class | trigger | observable signal | required mitigation | invalidated or preserved evidence |
| --- | --- | --- | --- | --- | --- |
| requirement ID hides vague behavior | `claim_blocking` | Formal identifier is attached to aspiration or ambiguous outcome. | Reviewer cannot derive an independent pass/fail case. | Rewrite trigger, result, failure, owner, and boundary. | Source evidence remains; contract and links reopen. |
| compound requirement hides branches | `silent_degradation` | Several actors/outcomes/constraints share one clause without coupling rationale. | One check cannot fail branches independently or one branch masks another. | Split claims or state one transactional invariant and branch evidence. | Shared premise remains; branch states reopen. |
| edge and recovery behavior omitted | `silent_degradation` | Happy path is specified while consequential invalid, boundary, concurrent, timeout, or failure states are absent. | Implementation behavior is accidental outside success case. | Add applicable negatives and recovery or narrow guarantee. | Happy-path claim may remain bounded. |
| compatibility obligation disappears | `claim_blocking` | New contract ignores public callers, stored data, prior versions, or rollout. | New tests pass while supported consumer evidence is absent. | Inventory consumers/data, version behavior, migration, rollback, and owner. | New local behavior may remain candidate; release claim invalid. |
| quantitative clause has no method | `claim_blocking` | Performance/reliability number appears without workload and measurement. | Units, baseline, environment, sample, uncertainty, or owner missing. | Keep unresolved and define experiment packet. | Functional requirements can continue independently. |
| one-way traceability looks complete | `silent_degradation` | Requirements list tests, but reverse audit is absent. | Orphan tests or unrelated assertions remain hidden. | Run bidirectional semantic mapping and resolve every orphan. | Valid links remain; completeness claim reopens. |
| generated traceability duplicates truth | `silent_degradation` | Matrix copies clauses and expected values into a separately edited artifact. | Source and matrix drift or disagree. | Store stable IDs/links, derive mechanical views, keep one authority. | Canonical contract remains; stale derived view invalid. |

**Verification and TDD failures**

| failure_mode_name | class | trigger | observable signal | required mitigation | invalidated or preserved evidence |
| --- | --- | --- | --- | --- | --- |
| green check misses requirement | `silent_degradation` | Command passes while a material requirement is orphaned or mapped check is incapable. | Traceability or injected violation review fails. | Add capable check and withdraw completion claim. | Unrelated passing checks remain valid. |
| shared implementation oracle agrees with bug | `silent_degradation` | Test expected value uses production helper or premise under test. | Representative mutation changes both actual and expected together. | Use independent expected values, model, differential source, or boundary observation. | Fixture inputs remain; result evidence invalid. |
| expected failure has wrong cause | `fatal_workflow` for TDD state | Initial check fails because of syntax, setup, permissions, or unrelated defect. | Failure message does not identify missing/wrong behavior. | Repair harness/preconditions and rerun before implementation. | Test intent remains; Red state is invalid. |
| no pre-change detection evidence | `claim_blocking` | Check is added after implementation and never shown sensitive to regression. | No pre-fix reproduction or mutation evidence. | Reproduce old behavior or inject representative violation. | Final pass is provisional until oracle capability is shown. |
| mock erases decisive behavior | `silent_degradation` | Test replaces transaction, concurrency, network, clock, filesystem, or policy semantics central to requirement. | Green unit test cannot observe named failure class. | Add integration/contract/runtime mechanism at the required boundary. | Pure local logic evidence remains. |
| flaky green is reported as reliable | `silent_degradation` | Repeated runs alternate without diagnosed environment or race. | Outcome depends on reruns or selective reporting. | Preserve all attempts, diagnose, stabilize, and withhold reliability claim. | Deterministic independent evidence may remain. |
| variant scope is generalized | `claim_blocking` | One platform, flag, tenant, or config result is reported universally. | Report lacks variant identity and exclusions. | Run material matrix or narrow language. | Tested variant remains supported for scope. |
| verifier targets wrong corpus | `fatal_workflow` for structural claim | Legacy/archive script is used to certify current packet/reference. | Verifier code reads different directories and contracts. | Run current focused tests; retain legacy result only historically. | Historical archive status may remain valid. |

**Implementation, measurement, and handoff failures**

| failure_mode_name | class | trigger | observable signal | required mitigation | invalidated or preserved evidence |
| --- | --- | --- | --- | --- | --- |
| implementation precedes authority | `claim_blocking` | Code changes begin while behavior or owner choice is unresolved. | Diff expands around open policy questions. | Stop mutation, clarify or split an isolated reversible experiment. | Source observations and independent requirements remain. |
| scope expands beyond packet | `fatal_workflow` for shared change | Refactor or feature touches unrelated files/interfaces without revised authorization. | Planned versus actual paths/claims differ. | Stop, attribute changes, split work, and obtain authority. | Verified in-scope work can remain. |
| naming convention breaks compatibility | `claim_blocking` | Mechanical word-count rule renames external API or domain term. | Callers, schemas, generated bindings, or public docs break. | Preserve public name, adapt internally, or execute authorized migration. | Semantic naming rationale remains; rename authorization does not. |
| partial feature is called complete | `silent_degradation` | One layer or check lands without end-to-end behavior, docs, integration, or recovery required by contract. | User journey cannot complete despite Green local test. | Finish bounded feature or narrow deliverable honestly. | Completed subcomponent remains partial evidence. |
| faster candidate changes semantics | `claim_blocking` | Optimization reduces duration by dropping work, checks, or output. | Equivalence/counter-metric fails. | Reject performance adoption or define an explicit semantic change. | Diagnostic timing remains; improvement claim invalid. |
| percentile label uses inadequate cohort | `silent_degradation` | Tiny or mixed observations are summarized as stable tail behavior. | Count, method, failed-run treatment, or comparability missing. | Report raw observations and redesign study. | Individual timings remain diagnostic. |
| measurement plan becomes result | `claim_blocking` | Designed experiment is written in past/result language. | No attempt manifest or raw data exists. | Relabel unexecuted and keep value unknown. | Method remains useful. |
| context summary replaces canonical packet | `silent_degradation` | Resume uses checkpoint prose without exact current contracts and links. | Source/requirement hashes or omitted alternatives cannot be reconstructed. | Reload canonical packet/index/selected sections. | Summary remains orientation aid only. |
| packet and code drift silently | `silent_degradation` | Implementation or tests change without packet invalidation. | Current revision differs from accepted identity. | Mark dependent claims invalid and replay gates. | Historical decision remains interpretable. |
| ownerless uncertainty survives handoff | `claim_blocking` | Open risk has no owner, mechanism, release, or stop condition. | Next step is vague or absent. | Assign route/owner or reject dependent action. | Other verified claim branches remain. |
| optional diagram fails | `optional_output_loss` | Presentation generation is unavailable or malformed while canonical packet and checks pass. | Diagram missing or invalid. | Record loss and continue unless decision requires it. | Canonical evidence remains. |
| method boundary triggers endless rewriting | `method_boundary` | Product, causal, security, runtime, or operational gap is repeatedly sent through spec formatting. | No material evidence state changes. | Stop, transfer claim to capable route or owner. | Existing specified claims remain as inputs. |

**Causal failure chains**

| chain | unsafe outcome | earliest break and recovery |
| --- | --- | --- |
| Duplicate digest copies -> apparent consensus -> inherited outcome accepted | Historical number becomes current target without measurement. | Hash-family gate and quantitative evidence classification. |
| Missing owner -> template value inserted -> precise requirement -> code implemented | Agent selects unauthorized product policy. | Authority gate before requirement promotion. |
| Compound requirement -> one broad test -> one branch passes -> all branches green | Unverified behavior inherits completion. | Claim decomposition and branch-specific states. |
| Production helper supplies expected result -> check passes -> wrong behavior ships | Tautological oracle hides defect. | Mutation/fault capability gate before Green trust. |
| Setup failure called Red -> code changes -> test later passes | TDD phase history does not establish detection. | Expected-failure reason check. |
| One configuration passes -> universal claim -> untested variant fails | Scope generalization escapes. | Variant identity and no-claim boundary. |
| Summary-only resume -> stale requirement -> implementation edits | Context compaction changes contract invisibly. | Reload canonical packet and stale-hash gate. |
| Performance plan -> no run -> result language -> architecture chosen | Fictional evidence drives irreversible choice. | Measurement result-state classification. |

**Future failure-injection plan**

| injected condition | expected observable state | required transition |
| --- | --- | --- |
| Changed source hash | Dependent claims become invalid. | Re-read source and replay affected gates. |
| Hash-equal duplicate added | Source count rises, substantive evidence count does not. | Update provenance only. |
| Requirement with no owner | Authority gate fails. | Clarification or owner route. |
| Orphan requirement or test | Bidirectional link gate fails. | Add capable link, document invariant, or remove stale item with authority. |
| Shared-helper oracle mutation | Original check stays green, capability audit fails. | Redesign independent oracle. |
| Setup error in initial check | Failure reason mismatch. | Repair harness; no TDD promotion. |
| Untested feature flag | Variant audit finds missing state. | Narrow claim or run required configuration. |
| Faster output with missing records | Equivalence gate fails. | Reject optimization result. |
| Stale packet revision | Invalidation gate fails before reuse. | Refresh or retire packet. |
| Missing optional diagram | Presentation warning only. | Continue with canonical evidence. |

Current local reads support these mechanisms, but occurrence rates and target severity are unmeasured. Classify severity by invisibility, action consequence, reversibility, and invalidation fan-out; collect incidence only under stable definitions.

The core recovery invariant is that another attempt changes a premise. Correct source, owner, requirement, oracle, harness, implementation, environment, workload, or method before retry. Unchanged repetition triggers backpressure and escalation, which the next section defines.

## Retry Backpressure Guidance

Retry only after the failed signal has a verified or testable class and the next attempt changes a premise. Name the changed source, authority, requirement, oracle, harness, implementation, environment, workload, authorization, or method; predict the first signal that should differ; isolate the attempt; and stop when the same mechanism recurs without new information.

**Retry state machine**

| state | entry evidence | permitted transition | prohibited action |
| --- | --- | --- | --- |
| `failure_observed` | Command error, invariant mismatch, contradiction, stale identity, malformed content, or unavailable evidence. | Preserve diagnostics and classify earliest stage. | Immediate blind rerun or overwrite. |
| `cause_classified` | Transient, source, authority, requirement, oracle, harness, code, config, environment, workload, contradiction, method, authorization, or unknown recorded. | Identify changed premise and expected signal, or route terminally. | Calling every failure transient. |
| `retry_ready` | Corrective condition exists, state/output is isolated, owner and stop condition are named. | Execute one bounded attempt and capture manifest. | Discard prior diagnostics or mix attempts. |
| `retry_running` | Attempt identity, target state, changed premise, resource owner, cancellation boundary recorded. | Complete, reveal new mechanism, or repeat same mechanism. | Concurrent writer on the same packet/file/output. |
| `retry_succeeded` | Predicted intermediate signal changes and all claim-relevant gates pass. | Compare attempts, retain causal conclusion, resume bounded work. | Treat eventual Green as proof of diagnosis without comparison. |
| `new_failure_discovered` | Attempt passes old stage and exposes a distinct earliest failure. | Return to classification with new evidence. | Count unrelated mechanism against the old retry rule. |
| `same_failure_repeated` | Same mechanism recurs without material information gain. | Apply backpressure, redesign, wait, route, or escalate. | Another unchanged attempt. |
| `claim_refuted` | Counterexample or authority disproves the claim as stated. | Update decision, reformulate narrower claim, or define authorized system change. | Retry until counterevidence disappears. |
| `method_boundary_reached` | Needed authority or observation is outside the digest/current method. | Transfer to product, diagnosis, security, runtime, measurement, operations, or owner route. | More formatting as substitute. |
| `authorization_blocked` | Required write, access, data, credential, or owner decision unavailable. | Wait for explicit change or answer within narrower read-only scope. | Circumvent permission or ownership. |

Success requires the predicted changed signal and downstream gates relevant to the claim. Fixing a test fixture can create valid Red evidence and then reveal an implementation defect; the first diagnosis was correct, but the feature remains incomplete.

**Failure-class guidance**

| failure class | retry eligibility | changed premise required | backpressure or terminal route |
| --- | --- | --- | --- |
| Wrong path, root, or target identity | Eligible after canonical identity correction. | Exact source/target and current state now verify. | Escalate scope when ownership is unclear. |
| Missing required local command | Eligible after authorized installation or path correction. | Exact capability probe now passes. | Use another method if installation is unavailable/prohibited. |
| Permission or storage pressure | Eligible after resource state changes. | Fresh authorized write succeeds safely. | Wait or choose owned location; never overwrite valuable output. |
| Source changes during read/review | Eligible after source stabilizes or revision freezes. | Pre/post identities match. | Use immutable snapshot or narrow observation. |
| Stale or mixed packet/output | Do not retry in place. | Fresh copy/state and complete manifest. | Quarantine old state diagnostically. |
| Requirement lacks owner authority | Not retryable by rewriting. | Accountable owner or authoritative contract appears. | Keep unresolved or route to product/policy. |
| Requirement is vague/compound | Eligible after behavior decomposition. | Reviewer can construct independent pass/fail branches. | Return to authority when ambiguity is product intent. |
| Oracle is tautological | Not eligible unchanged. | Independent expected source/model/fixture or capable layer introduced. | Route to domain or integration mechanism if needed. |
| Expected failure has setup cause | Eligible after harness correction. | Failure now identifies missing/wrong behavior. | Stop implementation until valid Red. |
| Optional presentation fails | Core work need not retry when canonical packet and gates pass. | Correct renderer only if presentation is required. | Continue with recorded optional loss. |
| Unsupported dynamic/security/operational claim | Not retryable within same observation model. | Capable domain/runtime/owner evidence becomes available. | Terminal for current method. |
| Positive evidence refutes claim | No retry of original claim. | System changes under a new authorized contract. | Mark refuted and block old action. |
| Public guidance is stale/ambiguous | Refresh only under authorization and decision need. | Versioned primary source plus local applicability evidence. | Route to owner/narrower source after no information gain. |
| Shared owner is editing same surface | Wait, do not race. | Explicit handoff or released boundary. | Never overwrite/revert another lane. |
| Unknown cause | One diagnostic attempt may add instrumentation. | Named hypotheses and distinguishing signal. | Stop after no information gain; route diagnosis. |

The one changed-premise attempt default is a reasoning safeguard for deterministic local work, not a distributed-systems constant. For APIs, queues, hosted runners, or services, follow established idempotency, delay, jitter, deadline, cancellation, and rate-limit policy. This reference invents no timing values.

**Attempt record**

| field | required content |
| --- | --- |
| `attempt_identifier` | Unique identity linked to decision and prior attempt. |
| `failure_signature` | Earliest failed stage, exact signal, and affected artifact/claim. |
| `cause_class` | Verified cause or bounded hypotheses with distinguishing check. |
| `changed_premise` | Exact source, authority, requirement, oracle, harness, code, environment, workload, method, or authorization change. |
| `expected_new_signal` | First observable result that should differ if diagnosis is correct. |
| `target_and_packet_identity` | Repository/artifact revision, working state, profile, and relevant configuration. |
| `output_identity` | Fresh or atomically owned state; never a mixed prior attempt. |
| `resource_owner` | Agent/operator with exclusive write responsibility. |
| `start_stop_cancel` | Launch, cancellation, wait, route, and acceptance conditions. |
| `result` | Predicted signal, full gates, new mechanism, repeated mechanism, contradiction, or blocked state. |
| `claim_effect` | Claims resumed, narrowed, invalidated, refuted, or transferred. |

Retain enough evidence to explain divergence without storing secrets or sensitive payload outside policy.

**Backpressure controls**

| pressure | control | release condition |
| --- | --- | --- |
| Red source/authority gate | Stop requirement promotion and implementation. | Current capable source or owner decision exists. |
| Red packet integrity gate | Stop matching reference edit/handoff. | Atomic packet section or full packet passes exact shape and uniqueness. |
| Red oracle/expected-failure gate | Stop trusting Green and code progression. | Check independently rejects intended wrong behavior. |
| Red consequential claim | Stop migration, security, compatibility, quantitative, or production approval. | Claim-appropriate evidence floor and owner acceptance pass. |
| Repeated same mechanism | Open circuit for method/claim pair. | Materially new source, capability, method, input, or authority. |
| CPU, memory, I/O, suite, or context pressure | Serialize, schedule, measure/narrow visibly, index, or switch method. | Resource and evidence contract restored. |
| Shared path contention | One writer and ordered handoff. | Current owner finishes or transfers explicitly. |
| Context-window pressure | Persist canonical packet/reference/progress before loading more. | Durable state reconstructs exact next action. |
| Reviewer/owner capacity | Queue consequential acceptance rather than auto-approve. | Qualified reviewer decides or requests evidence. |
| External service pressure | Apply service-specific policy and idempotency. | Service recovers or terminal policy activates. |

Backpressure is not merely waiting. It includes refusing generation, limiting concurrency, isolating state, narrowing claims visibly, persisting context, pausing promotion, and escalating authority.

**Long-running agent cadence for this evolution**

- Complete and save one section's ten-question packet before editing its reference section.
- Save the matching expanded reference section immediately and run an atomic heading, expansion, count, uniqueness, and marker sanity check.
- Record the Delta journal no later than every three completed sections and at Red, Green, and Refactor transitions.
- During complete rereads, persist review progress after at most five sections.
- Re-read current specification, newest user instructions, exclusive paths, and progress state before broad rewrites or phase changes.
- Never commit, push, clean, revert, or modify shared ownership surfaces without explicit authorization.
- Treat a new user instruction as a state change that can invalidate the current plan before the next write.

**Distributed execution rules**

1. Assign one owner per generated reference, packet, source change, or output directory.
2. Parallelize independent reads or disjoint writes only.
3. Use stable decision identity and explicit merge contracts across shards.
4. Preserve unrelated workspace changes and coordinate when another owner's work affects a shared premise.
5. Do not use retry to race an active owner or overwrite newer evidence.
6. Verify paths, headings, sources, packet counts, normalized uniqueness, claim links, and project behavior at integration.
7. Transfer blockers with last verified state, repeated signature, attempted premise changes, and release condition.

**Examples**

Good local retry: the initial integration check fails because its fixture uses the wrong schema version. The fixture is corrected, a fresh attempt now reaches the expected behavior assertion, and implementation begins only after that valid Red result.

Bad authority retry: an ownerless retention period is rewritten several times until it looks precise, then treated as approved. No authority changed.

Conditional source-stability retry: the first review spans a requirement edit and produces mismatched hashes. The agent records both states, reloads a stable revision, and repeats the affected review. Input consistency changed even though tools did not.

Good no-retry decision: an optional diagram cannot render, but canonical packet, source, tests, and handoff gates pass and no user decision depends on the visual. Record loss and continue.

**Future verification**

A fixture/orchestration suite should establish that corrected identity advances the predicted stage, unchanged deterministic repetition is blocked, every attempt preserves prior diagnostics, concurrent owners cannot claim one path, optional presentation loss remains local, authority/method gaps route instead of loop, a counterexample refutes rather than retries, and persisted checkpoints reconstruct the exact durable boundary.

Attempt history is an evidence trajectory. Recurring mechanisms should improve templates, fixtures, routing, or tool design so future agents do not repeat no-information work. Keep trivial corrections concise; retain sanitized causal records for durable or repeated failures.

## Observability Checklist

Observability makes a specification-derived decision reconstructable without turning the record into a source dump. Capture identities, boundaries, transitions, and bounded observations. Retain raw diagnostics only when reproduction, policy, and secure storage require them.

**Current assignment evidence surfaces**

| surface | observable fact | missing context or limitation |
| --- | --- | --- |
| Evolved reference | Current integrated guidance under one target path and final hash. | Passing shape does not prove every recommendation or target behavior. |
| Question packet | Explicit section/question rationale and unique field values. | High-level decisions are not hidden reasoning traces and do not replace source evidence. |
| Delta progress journal | Red/Green/Refactor states, counts, tests, paths, hashes, next actions, and reread checkpoints. | Append-only summaries require canonical artifacts for exact content. |
| Archive seed | Frozen original headings and baseline content. | Historical structure does not validate evolved claims. |
| Local skill/reference/template files | Exact current and historical local guidance at recorded hashes. | No guarantee that another environment has the same installation or that outcomes are calibrated. |
| Shared tests | Corpus inventory, ownership, packet, expansion, queue, and marker checks. | Whole-corpus status can be red due to other owners; structural Green is not behavior Green. |
| Focused verifier | Exact owned heading, expansion, packet, uniqueness, hygiene, and immutable-source checks. | Semantic claim quality still needs complete reread and evidence audit. |
| Git diff/status | Changed paths and textual integrity under the working tree. | Does not establish intent, behavior, or ownership by itself. |

No target code, runtime trace, benchmark, public retrieval, or production outcome was generated by this assignment. Future project work must add those surfaces when its claims require them.

**Minimum decision envelope**

| field | required observation | reason |
| --- | --- | --- |
| `decision_identifier` | Stable link to user outcome and claim graph. | Correlates source, test, implementation, measurement, and handoff. |
| `attempt_identifier` | Unique value for production, verification, or diagnostic attempt. | Prevents retries and outputs from merging. |
| `producer_chain` | Agent/workflow, skill/template versions, scripts/wrappers, command, and options. | Reconstructs how evidence was created. |
| `target_identity` | Repository/artifact root, revision, working state, branch/config/deployment where relevant. | Binds requirements, checks, diffs, and results to state. |
| `instruction_and_authorization` | Applicable instructions, write paths, data restrictions, commit/publish boundary, and owners. | Prevents evidence and mutation from escaping scope. |
| `time_identity` | Start/end, time zone, and clock/measurement source where comparisons matter. | Orders attempts and identifies long drift windows. |
| `completion_state` | Complete, failed stage, partial, cancelled, contradicted, route-away, or invalidated. | Exit code and document presence are insufficient. |
| `retention_and_privacy` | Storage class, access, redaction, expiry, and secure locator for sensitive evidence. | Keeps auditability from creating data risk. |

**Stage-event checklist**

| stage | start observation | completion observation | critical anomaly |
| --- | --- | --- | --- |
| Fit and authority | User outcome, owners, instructions, existing contracts, consequence. | Bounded decision, non-goals, profile, open questions, route choice. | Missing owner behavior is silently selected. |
| Source mapping | Candidate sources and expected authority. | Complete read/selection, hashes/versions, duplicates, conflicts, freshness. | Pointer or duplicate promoted beyond evidence. |
| Claim decomposition | Compound request and shared premises. | Claim IDs, types, consequences, branch states, owner links. | Weak branch inherits strong branch status. |
| Requirement authoring | Reviewed behavior and target conventions. | Atomic clauses, failure/edge behavior, compatibility, measurement questions. | Vague or copied quantitative target. |
| Verification design | Requirement graph and project surfaces. | Bidirectional links, check layer, fixture/workload, oracle, expected failure, no-claim boundary. | Check cannot observe mapped failure. |
| Red | Target state, command, fixture, predicted failure. | Exact intended failure and unrelated-failure review. | Setup/syntax failure reported as behavior evidence. |
| Green | Authorized minimal change and Red evidence. | Direct checks pass, independent branches retain state, changed paths recorded. | Scope expansion or eventual Green without causal link. |
| Refactor | Green behavior, source/design context, alternatives. | Structural change, preserved contract, relevant checks remain Green. | Contract changes silently during cleanup. |
| Measurement | Hypothesis, workload, baseline/candidate, environment, method. | Raw observations, failures, statistics, equivalence, uncertainty, owner interpretation. | One timing or plan promoted to result. |
| Final verification | Current source, requirements, checks, diff, configs, risks. | Bounded state, full applicable results, contradictions, recovery, invalidation, next action. | Structural pass promoted to semantic acceptance. |

Events can be a compact table or structured stream. They need not contain source bodies or full transcripts.

**Artifact and evidence manifest**

For every durable attempt retain:

- artifact or evidence identifier, filename/locator, role, and claim links;
- size, row/item count, schema, and hash where durable comparison matters;
- producer, target, requirement, check, environment, and owner identity;
- created/observed time and complete, conditional, diagnostic, derived, reconstructed, stale, or missing state;
- expected header/shape and validation result;
- privacy, access, and retention class;
- invalidation trigger and dependent claims.

Manifest checks should detect stale generated views or mixed attempt output, not merely confirm file existence.

**Source and context observability**

| question | retained evidence |
| --- | --- |
| Which user/repository instructions applied? | Exact identity, scope, precedence, and relevant clauses. |
| Which sources were loaded completely? | Paths, hashes/versions, read scope, and content-family grouping. |
| Which candidate sources were skipped? | Reason, expected authority, consequence, and future route. |
| Which context method was used? | Complete read, complete selected sections, deterministic index, or explicit global phase with measurement basis. |
| Was any input truncated or compacted? | Exact boundary, fail/route state, and canonical reload evidence. |
| Did source state change during work? | Pre/post identities and affected claims. |

Absence from loaded context is not evidence that a source or requirement does not exist. Observability must name the candidate population and selection rule.

**Claim, requirement, and check observability**

Every material claim exposes:

- identifier, bounded text, type, state, consequence, profile, and owner;
- supporting, refuting, and contextual evidence identifiers;
- requirement clauses and shared-premise links;
- check identity, type/layer, fixture/workload, oracle, assertion, and coverage boundary;
- expected failure and final result under named state;
- contradictions and earliest verified pipeline stage;
- promotion, downgrade, refutation, and invalidation events with actor/reason;
- residual risk, recovery, next action, and stop condition.

A screenshot or green badge can be a presentation artifact. It cannot be sole evidence of behavior, security, performance, or completeness.

**TDD and implementation observability**

| event | retain |
| --- | --- |
| Test skeleton/design | Requirement links, interface, fixture, oracle source, expected failure, and no-claim boundary. |
| Red | Exact command/check, target state, failure output summary, reason classification, and unrelated blockers. |
| Green | Minimal changed paths, direct pass, independent red/unresolved branches, and result scope. |
| Refactor | Structural intent, alternatives, compatibility, behavior-preserving evidence, and diff. |
| Final | Relevant suite/build/static/runtime/config results, failures, exclusions, reviewer decision, and owner acceptance. |

Record failed and contradicted attempts, not only successful ones. Otherwise feedback systematically hides the cases that should change guidance.

**Retry and backpressure observability**

| event | record |
| --- | --- |
| Failure | Earliest stage, signature, diagnostics locator, affected claims/artifacts. |
| Classification | Source, authority, requirement, oracle, harness, implementation, environment, workload, contradiction, authorization, method, or unknown. |
| Changed premise | Exact condition altered before another attempt. |
| Attempt | New identity/state, owner, expected signal, start/stop/cancel conditions. |
| Repeated mechanism | Circuit-open or route decision and release condition. |
| Recovery | Causal comparison, resumed claims, new invalidation, and regression action. |
| No retry | Why another attempt cannot add information and which system/owner owns the gap. |

**Timing and reviewer-effort measurements**

The seed requests p50/p95/p99 latency or reviewer-time measurements. Percentiles are appropriate only with enough comparable observations for the reported tail to be meaningful, a stated quantile method, raw counts, and stable boundaries. Never emit percentile labels solely because they sound operational.

| field | requirement |
| --- | --- |
| Workload | `S`, `C`, `R`, `K`, `L`, `V`, `O`, `A`, `E`, phase, and profile as relevant. |
| Environment | Machine, operating system, filesystem, tools, cache, load, and producer. |
| Sample | Count, inclusion/exclusion, failures/cancellations, task/reviewer population, and raw source. |
| Clock | Wall versus active versus CPU time, start/stop boundary, precision, and overhead. |
| Distribution | Median/tails only when justified; include range/variation, count, and uncertainty. |
| Interpretation | Decision effect, confounders, and no-generalization boundary. |
| Counter-metric | Claim sufficiency, reversals, defects, reconstruction, or evidence coverage. |

One run is one observation, not p50, p95, p99, typical, or guaranteed. Reviewer time depends heavily on task difficulty, expertise, interruption, and observation.

**Storage choices**

| sink | strength | risk | suitable content |
| --- | --- | --- | --- |
| Markdown packet/journal | Human-readable rationale and handoff. | Free-form drift and large diffs. | Claims, evidence locators, states, decisions, uncertainty, next actions. |
| Structured JSON/TSV | Machine validation and aggregation. | Schema lifecycle and sensitive fields. | Identities, links, counts, stage events, measurements. |
| Test/command log | High-fidelity execution diagnosis. | Noise, truncation, secrets, path exposure. | Secure failure details and reproducible command context. |
| CI artifact | Centralized execution and owner visibility. | Retention, runner variation, permissions. | Manifests, structured summaries, fixture results. |
| Metrics system | Comparable trends and alerts. | Lost raw context and incentive gaming. | Aggregates linked to definitions/evidence. |
| Runtime trace/log system | Dynamic correlation. | Privacy, sampling, cost, unexercised paths. | Routed runtime claims under service policy. |
| Issue/review system | Ownership, dissent, approval, follow-up. | Manual summaries stale. | Decision state and owner actions linked to canonical packet. |

Choose one authoritative identity and link secondary sinks. Do not copy mutable decision state into several places without synchronization ownership.

**Data minimization and integrity**

- Prefer hashes, stable IDs, pointers, command summaries, changed paths, mismatch classes, and unresolved-risk notes over source or transcript dumps.
- Do not retain credentials, tokens, private customer data, environment secrets, or unrestricted runtime payloads.
- Treat paths, symbols, requirements, and test names as potentially sensitive under project policy.
- Record truncation explicitly; missing tail output can hide the actual failure.
- Protect packet, manifest, and logs from concurrent writers and partial publication.
- Mark reconstructed state and identify which fields came from timestamps, version control, or later inference.
- Measure wrapper/instrumentation overhead when making timing claims.

**Profile examples**

Lightweight reuse: target revision, native requirement/test identity, pre-fix reproduction, changed path, relevant result, stop reason, and invalidation.

Standard implementation: full envelope, source/evidence registry, requirements/checks, Red/Green/Refactor, changed paths, contradictions, project results, recovery, and handoff.

High assurance: add domain authority, variants, threat/failure model, independent and runtime/operational evidence, residual risk, rollback, and authorized acceptance.

Bad observability: save only a green badge and elapsed time with no requirement, command, target revision, failure reason, source, configuration, or limitation. The record cannot explain behavior or performance.

**Reconstruction acceptance test**

Give a reviewer without the original conversation the retained record and ask them to identify:

1. Exact user decision, non-goals, consequence, and owner.
2. Instruction, source, target, working state, producer, and attempt identities.
3. Every material claim and its evidence type/state.
4. Requirement clauses, shared premises, variants, and compatibility boundaries.
5. Checks, fixtures/workloads, oracle sources, expected failures, and final results.
6. Changed paths and authorized implementation boundary.
7. Contradictions, failures, retries, routes, and preserved branches.
8. Quantitative evidence state and what remains unmeasured.
9. Current decision, residual uncertainty, recovery, invalidation, and next action.
10. What can be discarded without losing reproducibility or violating retention policy.

If the reviewer fills gaps from personal familiarity, repeat with less context. Successful handoff under context loss is the strongest observability test.

Observability closes the learning loop only when it preserves correlation. A vague-requirement defect without its template/version cannot improve authoring; a post-action failure without its claim route cannot improve promotion gates. Decision identity provides those edges while keeping evidence compact enough to review.

## Performance Verification Method

No performance experiment was executed for this evolution. Current latency, memory, context efficiency, throughput, capacity, p50/p95/p99 latency, reviewer time, productivity, and defect-reduction values are unknown. The method below defines how a future authorized study can make a bounded claim.

Performance method: measure one clearly named subject under frozen identity, preserve semantic/evidence equivalence or predeclare intended differences, and reject a faster result when quality counter-gates fail.

Leading indicator to measure: decision-relevant evidence reaches a capable check and bounded next action with less unnecessary work under comparable conditions.

Failure signal to watch: runtime, context, or reviewer speed improves because sources, negative cases, variants, checks, or recovery were omitted.

Pass condition: the predeclared cost measure improves sufficiently for the bounded decision, equivalence/intended-change gates pass, variability is understood, and no material counter-metric regresses.

Fail condition: comparability, sample, output, evidence quality, uncertainty, or owner-decision gates fail, even when one observed duration is lower.

**Separate the performance subject**

| subject | start boundary | stop boundary | primary measures | quality counter-metrics |
| --- | --- | --- | --- | --- |
| Packet/source production | Validated request, source identities, and profile are ready. | Packet/reference or native artifact passes structural and semantic review. | Wall/CPU time where meaningful, context/input units, artifact size, stage time, attempts. | Source coverage, claim quality, uniqueness, contradictions, and reconstruction. |
| Requirement/check design | Bounded decision and authority are established. | Reviewed atomic requirements and capable bidirectional matrix exist. | Active time, claims/links inspected, iterations, reviewer effort. | Falsifiability, oracle capability, negative coverage, owner conflicts. |
| Project verification | Target state and selected check set are ready. | Results are classified and claim states updated. | Suite/stage wall time, setup, retries, resource use, flaky attempts. | Check coverage, variant scope, expected-failure semantics, escaped defects. |
| Target implementation | Reviewed contract and valid Red evidence exist. | Minimal Green, refactor, and final project gates finish. | End-to-end elapsed/active time, changed paths, build/test cost, rework. | Behavior correctness, compatibility, diff scope, rollback, post-action reversal. |
| Artifact query/context retrieval | Canonical artifact/index and question are ready. | Complete relevant sections and evidence candidates are selected/read. | Query time, matches, units read, compactions, index cost. | Candidate recall, stale-hash rejection, missed source, reviewer reconstruction. |
| Target-system behavior | Deployed/build candidate and workload are ready. | Measurement packet and owner interpretation finish. | Latency, throughput, memory, CPU, I/O, errors, availability as applicable. | Functional equivalence, failures, resource shifts, workload coverage, operational risk. |

Do not combine these subjects into one unlabeled duration. Faster packet production can worsen project work by emitting vague requirements; faster target behavior can be achieved by dropping work.

**Experiment card**

| field | completion rule |
| --- | --- |
| Hypothesis | Name one causal change, stage, expected metric direction, and mechanism. |
| Decision | State what implementation, route, tool, template, or policy choice the result can change. |
| Baseline | Exact source/code/template/wrapper hashes, command, options, profile, and artifact contract. |
| Candidate | Exact changed producer/method, with unrelated changes excluded or recorded. |
| Workload | Sources/bytes, `C`, `R`, `K`, `L`, `V`, `O`, `A`, `E`, task class, data, and assurance as relevant. |
| Environment | Hardware, OS, filesystem, model/tool versions, runner, cache, power/load, reviewer population, and network as relevant. |
| Boundary | Exact start/stop, clock, profiler, sampling, warmup, timeout, cancellation, and active-time definition. |
| Repetition design | Count justified by observed variance and claim, ordering/randomization, failed-run treatment, and pairing. |
| Equivalence | Structural, semantic, behavioral, and decision properties that must match plus intended differences. |
| Counter-metrics | Coverage, oracle, negative cases, errors, resource shifts, reversals, and reconstruction that must not regress silently. |
| Pass rule | Predeclared evidence for adopt, reject, investigate, reroute, or no change. |
| No-claim boundary | Repositories, tasks, reviewers, machines, variants, workloads, and periods outside result scope. |

**Study tiers**

| tier | purpose | design | allowed claim |
| --- | --- | --- | --- |
| Mechanism fixture | Isolate parser, index, oracle, traceability, context, or test-stage behavior. | Small deterministic positive/negative cases. | Causal statement about that mechanism under fixture. |
| Repository/artifact snapshot | Estimate behavior on a real stable population. | Frozen revision, working-state policy, secure authorized outputs. | Bounded result for that target/environment. |
| Multi-target cohort | Assess portability across selected repositories, artifacts, or task classes. | Predeclared inclusion/strata and identical protocol. | Cohort-bounded trend with heterogeneity. |
| Reviewer/agent task study | Measure end-to-end decision and handoff effects. | Comparable tasks, profiles, agents/reviewers, outcomes, and follow-up. | Result under sampled people/tasks and procedure. |
| Operational observation | Understand live workload behavior. | Deployed identity, configuration, telemetry policy, workload coverage, and time. | Bounded observation, not unexercised guarantee. |

Keep fixture, target, task-study, and operational evidence separate. A fixture can explain mechanism without establishing monorepo or production capacity.

**Comparability abort gates**

Abort or relabel comparison when:

- source, requirement, target revision, dirty state, configuration, generated inputs, or owner decision differs unintentionally;
- template, skill, wrapper, model/tool, runner, command, option, or profile differs outside the hypothesis;
- candidate skips sources, checks, variants, or review performed by baseline;
- output schema, requirement meaning, check oracle, behavior, or decision product changes unexpectedly;
- one attempt is partial, cancelled, failed, stale, or mixed while the other completes;
- cache, filesystem, background load, power/thermal state, network, or environment makes observations unsuitable;
- reviewer expertise, task order, learning, interruption, or active-time method differs materially;
- instrumentation overhead differs or is unmeasured;
- quality gates show the candidate is a different evidence product.

Study real-world variation later as its own field distribution. Establish controlled causality first.

**Evidence and output equivalence**

| artifact or claim | equivalence check |
| --- | --- |
| Source population | Same distinct sources, versions/hashes, read scope, duplicate grouping, and conflicts. |
| Claim graph | Same material claims, types, consequences, states, and shared premises. |
| Requirements | Same behavior semantics, failure cases, compatibility, owners, and quantitative states. |
| Verification matrix | Same requirement/check links, oracle sources, fixtures/workloads, variants, and no-claim boundaries. |
| Project behavior | Same outputs, errors, side effects, ordering, concurrency, recovery, and supported configurations as applicable. |
| Decision state | Same supported/refuted/unresolved branches, residual risk, rollback, and next action. |
| Context retrieval | Same complete candidate set and selected canonical content under fresh hashes. |

Use byte hashes for deterministic serialized outputs. When ordering, timestamps, paths, or intentional semantics differ, compare structured fields, multisets, behavior, and claim states. An unexplained difference blocks a pure-performance conclusion. If semantics intentionally improve, define corrected, unaffected, and regression cases and version the new evidence product.

**Instrumentation plan**

| measurement | method class | caution |
| --- | --- | --- |
| Whole-command/process wall time | Monotonic clock around explicit start/stop and manifest validation. | State whether verification/setup is included. |
| CPU and peak memory | Platform-appropriate accounting including child processes. | Syntax/accounting vary; record tool and overhead. |
| Stage time | Wrapper events around source, packet, test, build, benchmark, and review phases. | Instrumentation becomes part of producer chain. |
| Context/input use | Exact bytes/tokens where observable, selected sections, index, compactions, and reloads. | Token estimates and model accounting can differ; do not infer quality from lower use. |
| Artifact size/links | Structured parser and manifest. | Fewer requirements/checks can mean missing behavior, not efficiency. |
| Test execution | Framework timing, setup, failures, retries, flakes, and layer. | Parallelism and caching change interpretation. |
| Reviewer active time | Instrumented study or carefully logged intervals. | Expertise, learning, interruption, difficulty, and observation effect confound. |
| Target resources | Profiler, benchmark harness, load system, or production telemetry. | Workload, environment, sampling, and privacy bound claims. |
| Evidence utility | Decision record of retained claims, contradictions, route changes, and correct next action. | Do not reduce heterogeneous value to one composite score. |

Tool-call count is useful only for a specific orchestration/cost question. Fewer calls are not inherently better when one call hides broad output or skips verification.

**Cache, order, and reviewer design**

- State cold, warm, or operationally mixed cache and how it was established.
- Do not call a run cold merely because the process is new; OS, build, model, and remote caches can persist.
- Alternate or randomize baseline/candidate order when learning, drift, and warmup matter.
- Use fresh or immutable outputs for every attempt.
- Disclose warmups and exclude only under predeclared rule.
- Keep failed, timed-out, cancelled, and invalid attempts in the ledger.
- Freeze source/packet identity before and after each multi-stage run.
- Counterbalance reviewer/task order where feasible and report learning effects.

Avoid privileged cache manipulation unless authorized and safe. If true cold control is impractical, measure operational state and narrow the claim.

**Distribution reporting**

Use p50/p95/p99 latency only when the sample contains enough comparable observations for each tail to be meaningful, quantile method is stated, and raw counts are retained. No fixed minimum is supplied because stability depends on variance and consequence.

Report:

- valid, failed, timed-out, cancelled, excluded, and missing observations;
- raw values or durable recalculation source;
- median, range/variation, and only justified tail summaries;
- paired/unpaired or within/between reviewer design;
- uncertainty/confidence method for inferential claims;
- outlier policy and sensitivity;
- exact cohort and no-generalization boundary.

One run is one observation. Report its conditions honestly; do not label it typical, percentile, or guaranteed.

**Quality counter-gates**

| speedup risk | required counter-gate |
| --- | --- |
| Faster source loading omits authority/counterevidence. | Complete candidate and source coverage reconciliation. |
| Fewer requirements hide coupled branches. | Semantic claim/requirement equivalence and branch-state review. |
| Faster tests skip integration or variants. | Requirement/check/variant equality and escaped-defect review. |
| Shorter context misses selected sections. | Complete match/index checks, reviewer reconstruction, and missed-source audit. |
| Faster implementation expands technical debt or scope. | Diff/architecture review, relevant suite, compatibility, recovery. |
| Faster target output drops work or errors. | Structured behavioral equivalence and resource/error counter-metrics. |
| Faster review comes from shallow approval. | Correct next action, contradiction detection, reversals, and defects. |
| More observability slows work. | Overhead measurement with equal reconstruction/privacy requirements. |

**Route-specific pass conditions**

| decision | pass condition |
| --- | --- |
| Adopt producer/template optimization | Predeclared cost improves under comparable workload, evidence equivalence or intended semantic change passes, variability is understood, and counter-metrics hold. |
| Adopt test optimization | Same requirement, failure, variant, and oracle coverage with lower measured cost and stable flake/error behavior. |
| Reduce context | Reviewer still identifies correct claims, source, checks, next action, and unresolved risk with complete candidate recall. |
| Reuse instead of rebuild | Validation plus query cost is lower than measured rebuild and compatibility gates pass. |
| Skip packet | Native contract answers claim with lower workflow cost and equal or stronger evidence. |
| Reject result | Any comparability, output, quality, sample, uncertainty, or owner gate fails. |

**Worked experiment design without results**

Hypothesis: a deterministic structural index for one large canonical specification reduces repeated context loading during local revisions without changing candidate recall, selected complete section content, edit authorization, stale-state rejection, or final decisions.

Plan:

1. Freeze canonical artifact, packet/query cohort, agent/reviewer procedure, and baseline/candidate versions.
2. Define baseline complete-read phases and candidate indexed local phases; keep explicit global-review tasks separate.
3. Generate fresh outputs and alternate route order where learning can be controlled.
4. Measure canonical/index bytes, context units, selected sections, query time, active review time, attempts, and compactions.
5. Inject omitted match, stale hash, duplicate heading, changed span, and summary-only resume.
6. Compare complete candidate sets, source bytes read for selected sections, edit diffs, claims, and reviewer next decisions.
7. Report raw observations, justified summaries, overhead, disagreements, and no-claim boundary.
8. Adopt only if context/resource improvement is repeatable and no completeness, semantic, or recovery regression appears.

This design is actionable but contains no duration, saving, percentile, capacity, or pass result.

**Result language**

Good: "Under the frozen artifact/task cohort, matched producer and environment, fresh outputs, and stated cache/reviewer design, the candidate reduced the predeclared context measure across repeated observations; complete candidate/section evidence and decision samples showed no observed regression within scope."

Bad: "One warm run used fewer tokens, so p99 productivity improved and the workflow scales." Neither tail behavior, decision quality, nor capacity follows.

Diagnostic only: "One observed review spent most recorded active time resolving requirement/check conflicts." This can motivate a controlled study but is not a general performance conclusion.

Performance verification is evidence-throughput verification. Time, context, and resources matter only alongside the decision-relevant truth and recoverability they produce. Sometimes the best optimization is deleting the packet stage because a current native contract already answers the question more strongly.

## Scale Boundary Statement

Scale is not a universal file, token, source, requirement, agent, or duration count. It is the point at which the current route can no longer preserve complete evidence, coherent authority, repeatable verification, and a correct bounded decision at acceptable cost. No capacity experiment was run for this evolution, so maximum safe values for any dimension remain unknown.

The recommended default is deliberately simple: one bounded decision, one frozen source population, one canonical artifact, and one accountable integration owner. Continue locally while complete source discovery, claim closure, variant enumeration, artifact validation, rereading, and focused verification remain repeatable. Escalate only for a named pressure or boundary event.

**Scale dimensions**

| dimension | pressure to measure | boundary signal | misleading shortcut |
| --- | --- | --- | --- |
| Sources and bytes | Distinct canonical sources, versions, bytes, duplicate groups, discovery time. | Discovery remains open-ended or complete candidate recall cannot be demonstrated. | Treating raw file count as semantic complexity. |
| Claims and coupling | Claims, shared premises, contradictions, dependency density, unresolved states. | Dependency closure no longer fits one reliable integration review. | Splitting every file even when claims cross file boundaries. |
| Requirements and checks | Atomic requirements, capable links, negative cases, fixtures, execution cost. | Verification fan-out cannot meet the decision window without staged or distributed execution. | Removing checks to make the workflow appear faster. |
| Variants and environments | Platforms, configurations, versions, workloads, permissions, failure modes. | Required combinations cannot be represented or exercised by one route. | Calling one happy-path environment representative. |
| Artifact state | Size, generated portions, churn, concurrent changes, stale-hash rejects. | The review snapshot changes faster than it can be validated and integrated. | Summarizing away changed source identities. |
| Ownership and authority | Owners, policy domains, approvals, conflict latency, unavailable decision makers. | Independent owners have incompatible or unresolved authority over one decision. | Assigning one agent to decide another team's policy. |
| Execution and coordination | Agents, queues, active time, retries, merge load, checkpoint recovery. | Reconciliation throughput or recovery falls below production rate. | Assuming more workers always increase throughput. |
| Consequence and assurance | Safety, security, compliance, reversibility, operational objective, evidence depth. | Required assurance exceeds local review or demands live controls. | Using repository size as a proxy for risk. |

A small artifact can cross a scale boundary because two authorities disagree about ten coupled claims. A very large generated corpus can remain locally tractable when identities are stable, a deterministic index provides complete recall, and only a small independent claim set requires judgment.

**Route ladder**

| route | use when | preserve | introduced cost |
| --- | --- | --- | --- |
| Continue locally | Discovery is bounded, authority coherent, identities stable, and full review is repeatable. | Canonical source bytes, one claim ledger, one owner, complete gates. | Long critical path if pressure grows. |
| Narrow by query or graph | The source population is large but the decision and dependency closure are bounded. | Complete candidate recall, selection rationale, canonical links, global final gates. | Index validation and risk of missed edges. |
| Stage verification | Checks are capable but too costly to run indiscriminately. | Requirement/check links, affected-set proof, fast feedback, final broad gate. | Scheduler, cache, and variant-accounting complexity. |
| Shard by decision cluster | Weakly coupled claim clusters can be owned and verified independently. | Frozen inputs, unique claim ownership, dependency edges, output contract, integration owner. | Handoffs, merge conflicts, duplicated premises. |
| Federate by authority | Different systems or teams must make their own policy decisions. | Local authority records, versioned interface contracts, unresolved-conflict route, cross-owner acceptance. | Coordination latency and compatibility management. |
| Persist or index | Repeated retrieval, restart, or historical comparison dominates cost. | Immutable source identity, freshness checks, canonical content, deterministic rebuild. | Storage lifecycle, schema migration, stale-index risk. |
| Operational control plane | Production traffic, live state, or an explicit service objective governs the decision. | Telemetry, deployment identity, access control, rollback, incident ownership, retention policy. | Continuous operations, privacy, security, and on-call burden. |

Do not jump directly from local inconvenience to distributed execution. First identify the constrained resource: retrieval, semantic review, owner resolution, check execution, persistence, or live reliability. Choose the smallest route that relieves that measured constraint.

**Hard boundaries and pressure indicators**

Hard boundary events require an immediate route change or stop:

- source discovery is unbounded or a complete candidate set cannot be established;
- the decision spans independent systems without a versioned interface and integration owner;
- more than one owner has unresolved authority over the same claim;
- concurrent work would write the same canonical region without serialization;
- the required variant or failure environment cannot be exercised or credibly substituted;
- artifact identity changes during review and stale work cannot be rejected;
- production traffic is involved without an explicit objective, telemetry, rollback path, and operational owner;
- safety, security, privacy, or compliance policy forbids the proposed evidence movement or execution.

Pressure indicators justify measurement, not automatic decomposition:

- repeated context compaction loses claim state or open risks;
- source selection or full rereads dominate active time;
- check queues exceed the decision window;
- retries repeat unchanged premises;
- merge reconciliation consumes more time than shard production;
- owner conflict remains unresolved past a local policy window;
- generated artifacts churn faster than review snapshots stabilize;
- a rising fraction of attempts end stale, cancelled, incomplete, or unreconstructable.

One slow run, one large file, or one high token estimate is not a boundary by itself. Record the distribution, failure consequence, and competing route before changing architecture.

**Narrowing without losing evidence**

Graph or index narrowing is appropriate for large codebases and corpora only when the narrowing mechanism is itself verified. A source list without canonical rank, version identity, dependency closure, and negative-search evidence is insufficient.

1. Freeze the source revision, working-state policy, generator identity, and query intent.
2. Build or validate an index that maps each candidate to canonical source spans and hashes.
3. Prove recall on deterministic positive, negative, duplicate, renamed, stale, and cross-file cases.
4. Select the bounded dependency closure for local work; retain why each candidate was included or excluded.
5. Read selected sections completely rather than relying on snippets as semantic truth.
6. Run global structural and behavior gates before accepting the integrated result.
7. Invalidate selections when sources, queries, ownership, or requirement semantics change.

Narrowing may reduce context while increasing index maintenance. It passes only when the reviewer still reaches the correct claims, sources, checks, unresolved risks, and next action.

**Safe sharding contract**

Parallel workers may write separate owned artifacts or non-overlapping regions. They must not rewrite the same canonical reference concurrently. Before dispatch, record:

| shard field | required content |
| --- | --- |
| Input identity | Source, requirement, template, tool, and profile hashes plus dirty-state policy. |
| Scope | Included claim IDs and explicit exclusions. |
| Dependencies | Required upstream claims and downstream consumers. |
| Ownership | One writer and one decision owner for every claim. |
| Output contract | Schema, heading/order rules, evidence links, completion state. |
| Verification | Local capable checks, negative cases, and returned evidence. |
| Checkpoint | Durable progress, unresolved risks, and exact restart action. |
| Integration | One merge owner, dependency-closure audit, conflict policy, and final broad gates. |

Shard by weakly coupled decision cluster rather than by arbitrary byte ranges or convenient filenames. If new evidence reveals a shared premise, stop the affected shards, update dependency ownership, and replan. Completion reports are not compositional proof: the integrated claim graph and behavior must be verified after merge.

**Backpressure and reconciliation**

Useful parallelism is bounded by integration capacity. Let worker admission depend on queue age, merge-owner availability, stale-output rate, unresolved dependencies, verification capacity, and consequence. When reconciliation falls behind:

1. stop admitting new shards;
2. finish or cancel work whose inputs are still valid;
3. reject stale outputs by identity rather than manually adapting them in place;
4. merge the highest-consequence dependency closure first;
5. measure whether the split reduced end-to-end decision cost;
6. return to fewer shards if handoff and merge work erase the gain.

Retries are not capacity. A shard may retry only after a changed premise such as repaired input, available owner, corrected environment, or later authorized time. Unchanged retries amplify saturation and produce duplicate evidence.

**Long-running workflow boundary**

Context drift is a reliability failure when current state cannot be reconstructed from durable artifacts. At every configured persistence boundary, save completed atomic work, source and producer identities, checks run, exact results, open claims, blockers, and the next valid action. A summary is an index into canonical evidence, not a replacement for it.

Resume by validating identities and rereading the complete active section plus required dependencies. If the canonical artifact changed, classify prior work as valid, stale, or conflict-prone before editing. Periodic checkpoints reduce loss; they do not excuse a complete final reread.

**Operational escalation**

This digest is a reference artifact, not a production scheduler, telemetry store, service-level objective monitor, access-control system, or incident manager. When production traffic or live state determines the decision, establish an operational route with:

- an explicit service objective and measurement window;
- deployment, configuration, and workload identity;
- health, error, saturation, latency, resource, and correctness signals as applicable;
- access, privacy, retention, and audit policy;
- idempotency, deadline, backpressure, degradation, and rollback behavior;
- an operational owner and incident escalation path;
- links back to the canonical requirement and evidence records.

The local digest can explain and audit that route, but it cannot substitute for live enforcement or telemetry.

**Worked examples**

Good local narrowing: a monorepo contains thousands of generated declarations. A hash-validated symbol/dependency index returns the complete candidate closure for one compatibility claim. The reviewer reads those sections completely, verifies negative rename and stale-index cases, and runs the repository-level compatibility suite before integration.

Good federation: an API change spans two services owned by different teams. Each owner produces a versioned contract packet and tests its local behavior. One integration owner resolves shared compatibility states, runs cross-service checks, and records rollback authority. Neither owner silently rewrites the other's policy.

Bad sharding: five agents receive overlapping headings in one reference and later concatenate their outputs. Each result can look complete while headings, claims, evidence states, and terminology conflict. More agent throughput has created unowned reconciliation work.

Borderline case: two files look independent but share a retry/idempotency contract. Pilot one reversible split with explicit dependency edges and an integration test. If merge conflicts or semantic disagreements dominate, recombine the cluster.

**Verification before adopting a scale route**

For a frozen representative workload:

1. Compare canonical source manifests before and after decomposition.
2. Verify every claim has exactly one current owner and every dependency resolves or remains explicitly open.
3. Reconcile shard outputs into the same requirement/check/variant matrix expected from the local route.
4. Inject stale inputs, missing candidates, duplicate claims, owner conflict, failed workers, and partial outputs.
5. Confirm checkpoints recover without invented completion or lost negative evidence.
6. Measure end-to-end decision time, context/resource use, queueing, retries, merge effort, and invalid work.
7. Sample semantic decisions and run final behavior gates; worker completion count is not a quality metric.
8. Adopt only when the bounded capacity or reliability benefit outweighs added coordination and no material evidence gate regresses.

Known with confidence: immutable identity, complete discovery, single-writer ownership, explicit dependency edges, durable checkpoints, and final integration verification reduce ambiguity. Unknown here: universal maximums for source count, bytes, claims, variants, agents, queue depth, duration, memory, context, throughput, or production traffic. Teams may set provisional budgets, but each budget must be labeled as local policy, tied to observed telemetry and consequence, assigned an owner, and given a review condition.

The mature scale model is reversible. Narrow, shard, federate, persist, or escalate when measured pressure requires it; collapse back to a simpler route when that pressure disappears. Every coordination layer must earn its continued existence through demonstrated evidence quality, reliability, or capacity.

## Future Refresh Search Queries

No query in this section was executed during this evolution. Browsing was prohibited, so no result, page, publication date, release state, compatibility conclusion, or external citation was observed. Every row below has status `unexecuted_no_browse`; the table is a future research backlog, not an evidence source.

Search only for a named stale or unresolved claim. Start with current local authoritative artifacts, then current official primary documentation or release records, then maintained source repositories and reproducible local behavior. A search result can nominate evidence; it cannot establish local behavior, owner policy, or production truth without the appropriate local route.

**Preserved seed discovery queries**

| search_query_label_name | search_query_text_value | status | bounded use |
| --- | --- | --- | --- |
| `official_docs_query_phrase` | executable metapattern reference digest official documentation best practices | `unexecuted_no_browse` | Broad discovery fallback when the defining producer or term is unknown; do not infer that official documentation exists. |
| `github_repository_query_phrase` | executable metapattern reference digest GitHub repository examples | `unexecuted_no_browse` | Candidate example discovery; repository examples are not automatically normative or compatible. |
| `release_notes_query_phrase` | executable metapattern reference digest changelog release notes migration | `unexecuted_no_browse` | Candidate change-history discovery; match any result to installed producer and consumer versions. |

These phrases are intentionally broad and are preserved exactly from the seed. Prefer the decision-bound queries below once the producer, version, and unresolved claim are known.

**Decision-bound query backlog**

| query id | unresolved decision | future query text | preferred primary evidence | expected extraction | status |
| --- | --- | --- | --- | --- | --- |
| `REFRESH-SKILL-FORMAT` | Does the current skill or agent instruction format require different metadata, discovery, or progressive loading? | `current official Codex skill agent instruction format metadata progressive disclosure version` | Current official product documentation and installed schema/source. | Required fields, loading semantics, compatibility, migration, effective version. | `unexecuted_no_browse` |
| `REFRESH-AGENT-CONTEXT` | Which current context-management behavior is specified rather than inferred? | `current official coding agent context compaction checkpoint resume behavior documentation` | Current official agent documentation and local harness behavior. | Persisted state, compaction limits, resume contract, failure semantics. | `unexecuted_no_browse` |
| `REFRESH-CI-SEMANTICS` | How should required checks, matrices, dependencies, cancellation, and merge queues be modeled now? | `GitHub Actions current official required checks matrix dependencies cancellation merge queue documentation` | Current official GitHub documentation and repository workflow schema. | Event semantics, result states, dependency rules, cancellation and protection behavior. | `unexecuted_no_browse` |
| `REFRESH-PROPERTY-TEST` | Which property-testing capabilities and shrinking semantics apply to the selected language/tool version? | `official property testing framework documentation generators shrinking replay seed current version` | Framework documentation and maintained source for the installed release. | Generator contract, shrink behavior, replay identity, failure persistence. | `unexecuted_no_browse` |
| `REFRESH-MUTATION-TEST` | Can mutation testing provide a capable oracle-strength signal for this stack? | `official mutation testing tool documentation equivalent mutants test impact current version` | Tool documentation, release record, and maintained implementation. | Supported languages, operator set, equivalent handling, output schema, limitations. | `unexecuted_no_browse` |
| `REFRESH-TRACEABILITY` | What current primary standards or tool contracts clarify bidirectional requirement-to-check traceability? | `official requirements traceability bidirectional verification evidence standard current` | Applicable standards body or defining tool documentation. | Scope, terminology, required links, audit expectations, version applicability. | `unexecuted_no_browse` |
| `REFRESH-BENCHMARK-STATS` | Which statistical method fits the intended benchmark and tail claim? | `official benchmark framework documentation warmup sampling confidence interval percentile methodology current version` | Selected benchmark framework documentation and primary statistical method source. | Sampling, warmup, quantile method, uncertainty, comparison and raw-output rules. | `unexecuted_no_browse` |
| `REFRESH-DETERMINISM` | Which current mechanism can provide deterministic source identity and index reconstruction? | `official deterministic build content hash source index reproducibility documentation current version` | Defining build/index tool documentation and source. | Hash inputs, ordering, environment dependencies, invalidation, reproducibility limits. | `unexecuted_no_browse` |
| `REFRESH-OBSERVABILITY` | Which telemetry conventions are current for the target runtime and privacy boundary? | `official telemetry semantic conventions traces metrics logs errors current version` | Current telemetry specification and target SDK documentation. | Required attributes, propagation, sampling, error status, compatibility, privacy controls. | `unexecuted_no_browse` |
| `REFRESH-RETRY` | Which external API retry, idempotency, deadline, and rate policies constrain this workflow? | `official target API retry idempotency rate limit deadline error documentation current version` | Defining API and SDK documentation for the deployed version. | Retryable states, idempotency key, delays, deadlines, quota headers, unsafe cases. | `unexecuted_no_browse` |
| `REFRESH-SECURITY` | Has the governing security, privacy, or retention policy changed? | `official target platform security privacy data retention audit documentation current version` | Accountable platform/policy authority and current contract. | Data classes, allowed movement, retention, deletion, audit, effective date. | `unexecuted_no_browse` |
| `REFRESH-METAPATTERN` | Has a mapped local metapattern producer changed enough to require regeneration? | `current executable metapattern reference digest producer schema release migration evidence` | Current local skill, templates, metadata, wrappers, and repository history first; public producer records only if applicable. | Producer identity, schema delta, migration behavior, affected claims, regeneration rule. | `unexecuted_no_browse` |

Query text is a starting point. Before execution, substitute the exact product, repository, framework, version, operating system, API, or policy name. For a high-consequence claim, use a precise query, a terminology-expansion query, and a counterevidence query. Do not endlessly paraphrase after the route stops yielding new primary candidates.

**When search is appropriate**

Search is appropriate when a current external producer may have changed:

- syntax, schema, agent/skill format, or tool behavior;
- release compatibility, deprecation, migration, or support policy;
- CI, test framework, benchmark, telemetry, or API semantics;
- public security, privacy, retention, or operational guidance;
- a contradiction whose authoritative source is outside the local corpus.

Trigger a refresh on a producer hash or version change, a broken capable check, a new contradiction, a high-consequence unknown, a changed owner policy, or an explicit review date. Frequency should follow volatility and consequence rather than a single calendar cadence.

**When to stop or reroute**

Do not search the public web to answer facts determined by:

| question | correct route |
| --- | --- |
| What code is in the current dirty worktree? | Read the local source, revision state, and generated outputs. |
| What behavior does the installed wrapper exhibit? | Inspect its code/schema and run a controlled reproduction. |
| What does a private organization permit? | Ask the accountable policy owner and record the effective decision. |
| What happened under production workload? | Use authorized telemetry, deployment identity, and incident records. |
| Does a change satisfy this repository's contract? | Run capable local checks and inspect their oracles. |
| Does an external example fit this architecture? | Compare versions, assumptions, failure semantics, and reproduce locally. |

A zero-result search means only that the declared retrieval route found no candidate. It does not establish absence, safety, unsupported behavior, or consensus.

**Source priority and admissibility**

1. Read the current local canonical producer, schema, template, wrapper, configuration, and tests.
2. Prefer current official primary documentation, specifications, release records, and maintained source from the defining producer.
3. Use repository issues, discussions, incident reports, or maintainer statements to identify caveats and hypotheses; record their status and authority.
4. Use secondary articles and examples for terminology or candidate discovery, not as sole support for consequential normative claims.
5. Reproduce behavior against the exact local/deployed version when the claim is testable.
6. Route policy and value judgments to the accountable owner.

Official prose can lag implementation or describe a different release. Source code can reveal implementation without defining support policy. A reproduction can prove observed behavior without proving future compatibility. Preserve these distinctions in the claim ledger.

**Refresh execution record**

For each executed query, create a durable record with:

- query ID, exact text, purpose, stale claim, and expected decision;
- execution timestamp, retrieval method or engine, and operator;
- candidates inspected, candidates excluded, and exclusion reasons;
- direct source identity, publisher/owner, title, version, publication/update date, and access outcome;
- exact supporting location or a bounded paraphrase plus the claim it supports;
- applicability to local producer, consumer, platform, configuration, and time;
- contradictions, duplicate-source grouping, confidence, and unresolved questions;
- local experiment, test, schema comparison, or owner review required;
- final claim transition and artifact paths changed.

Do not cite a search-results page or snippet as the evidence. Do not convert candidate count into confidence. Deduplicate by underlying producer and claim because syndicated pages can repeat one assertion without adding independent support.

**Refresh protocol**

1. Identify the stale or unresolved claim and its consequence.
2. Freeze current local source, producer, consumer, tool, and artifact identities.
3. Select the evidence route and draft decision-bound plus counterevidence queries.
4. Execute only under an authorization that permits external retrieval.
5. Inspect complete primary sources and record version applicability.
6. Compare external statements with local code, contracts, tests, and mapped evidence.
7. Reproduce testable behavior using a controlled fixture or representative target.
8. Classify the claim as supported, refuted, conflicting, unresolved, superseded, or inapplicable.
9. Update the smallest affected sections, traceability links, checks, and no-claim boundaries.
10. Run focused structural/behavior gates, then the required broader suite.
11. Obtain owner acceptance for policy or risk changes.
12. Record no-change, adopted, rejected, or unresolved outcome and schedule/trigger only necessary follow-up.

**Examples**

Good: `GitHub Actions current official required checks matrix cancellation merge queue documentation for the repository's enabled feature set`. The researcher records current official sources, matches them to the workflow schema and repository protection settings, reproduces a cancellation case, and updates only affected claims.

Bad: `best CI practices`. The researcher copies a snippet, omits the producer version, and declares the local merge policy correct without inspecting configuration or behavior.

Borderline: a maintained repository example demonstrates mutation testing for the same language. It is useful as a candidate fixture, but not normative until tool version, operator support, equivalent-mutant behavior, cost, and local test value are evaluated.

**Lifecycle states**

| state | meaning | allowed next states |
| --- | --- | --- |
| `queued` | A named claim and decision justify future research. | `executed`, `retired` |
| `unexecuted_no_browse` | The query is specified but external retrieval was not permitted here. | `executed`, `retired` |
| `executed` | Search ran and candidate disposition was recorded. | `evidence_captured`, `unresolved`, `retired` |
| `evidence_captured` | Applicable primary evidence was extracted and mapped. | `reproduced`, `adopted`, `rejected`, `unresolved` |
| `reproduced` | Testable behavior was checked against the target identity. | `adopted`, `rejected`, `unresolved` |
| `adopted` | Evidence and required owner gates changed the reference or contract. | `queued`, `retired` |
| `rejected` | Candidate evidence was inapplicable, weaker, contradicted, or failed verification. | `queued`, `retired` |
| `unresolved` | Conflict or missing authority remains explicit with a next route. | `executed`, `retired` |
| `retired` | The claim/integration disappeared, authority moved, or a stable local contract superseded search. | `queued` if premises later change |

Known now: the three seed phrases and the decision-bound queries are present locally, and none was executed in this evolution. Unknown now: whether any result exists, what it says, whether it is current, whether it is authoritative, and whether it applies. A polished query queue must never be cited as if it were completed research.

The long-term aim is not an ever-growing search backlog. Repeated searches for the same behavior often indicate a missing local schema, regression test, source map, or owner decision. As executable local contracts improve, retire the queries they supersede.

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.

These three seed labels remain valid, but they are not sufficient by themselves. A source category says where support is expected; it does not establish that the source is current, authoritative for the decision, applicable to the target version, semantically sufficient, or independently reproduced.

No external URL was opened during this evolution. Local artifacts and their mapped source text were read, but inherited external-source contents and freshness were not independently revalidated. Therefore, the existence of a URL in the local corpus is a local fact; the continuing truth and applicability of the external claim remains source-attributed within its recorded boundary.

**Minimum claim record**

Use a separate record for every consequential factual, quantitative, compatibility, causal, or normative claim:

| field | required meaning |
| --- | --- |
| Claim ID and text | One falsifiable or decision-relevant assertion, not a paragraph of mixed propositions. |
| Claim type | Behavior, requirement, compatibility, measurement, causal inference, method proposal, policy, risk, or other explicit type. |
| Provenance class | Local corpus, external primary source, local observation, combined inference, owner decision, or unknown. |
| Source identity | Path/URL/producer, version or revision, hash where available, date/access state, and exact supporting location. |
| Applicability | Target repository/system, platform, configuration, workload, time, and exclusions. |
| Evidence state | Supported, observed, proposed, conflicting, refuted, unresolved, superseded, or inapplicable. |
| Capability | What the source/check can actually prove and what it cannot. |
| Consequence | Which requirement, implementation, verification route, risk, or owner decision changes. |
| Verification route | Source inspection, structural check, controlled experiment, target test, telemetry, or owner review. |
| Uncertainty and next action | Residual doubt, counterevidence, responsible owner, trigger, and bounded follow-up. |

Low-consequence explanatory prose may group claims when provenance, state, applicability, and consequence are genuinely identical. Never group a factual premise, causal inference, and recommendation merely because they fit in one sentence.

**Operational evidence classes**

| label | means | can justify | cannot justify alone |
| --- | --- | --- | --- |
| `local_corpus_sourced_fact` | The assertion is directly supported by identified local source content. | Claims about that frozen local content and its explicit contract. | Current external behavior, production outcome, or broad effectiveness. |
| `external_research_sourced_fact` | An inspected public primary source directly supports the assertion for its version and scope. | What that authority states within recorded applicability. | Local installation behavior, hidden configuration, or independent causal effect. |
| `combined_evidence_inference_note` | Named premises from local and public evidence are joined by an explicit inference. | A bounded recommendation when premises and reasoning survive challenge. | Treating synthesis as direct observation or source quotation. |
| `local_observation_fact` | A command, test, benchmark, inspection, or telemetry sample produced a recorded result. | Observed target behavior under exact conditions. | Universal, typical, future, or causal behavior without an adequate design. |
| `proposed_verification_method` | A procedure is specified but has not produced a result. | Planning, review, and future execution. | Any pass, speed, capacity, reliability, or effectiveness claim. |
| `owner_policy_decision` | An accountable owner chose a rule, risk acceptance, or value tradeoff. | Authorized action within that ownership and effective period. | Empirical truth outside the decision or another owner's authority. |
| `conflicting_evidence_state` | Applicable sources or observations disagree and no governing resolution is established. | Branching, escalation, and targeted falsification. | Silent averaging or a definitive winner. |
| `explicit_unknown_state` | Required evidence is absent, inaccessible, unsuitable, or not yet interpreted. | A no-claim boundary and prioritized next action. | Positive or negative conclusions from missing evidence. |

`external_research_sourced_fact` requires an actually inspected source. A future search phrase, search snippet, inaccessible link, or URL copied from another artifact is not inspected external evidence. `combined_evidence_inference_note` must enumerate its premises and the reasoning step; it is not a license to make plausible guidance sound sourced.

**Evidence state lifecycle**

```text
proposed -> observed/supported -> challenged -> retained/superseded/refuted
             |                       |
             v                       v
         conflicting ------------> unresolved
                                      |
                                      v
                            new evidence or owner decision
```

States are not monotonic. A supported claim becomes conflicting when a current applicable observation disagrees; a previously observed behavior becomes superseded when target identity changes; an owner policy expires when authority or effective conditions change. Preserve history instead of rewriting old evidence as though it never existed.

**Authority, implementation, and observation**

Keep three questions separate:

1. What behavior does the governing contract or owner support?
2. What does the current implementation appear to do?
3. What occurred in the measured runtime under stated conditions?

Official documentation may define supported intent while local source reveals a defect. Source may reveal one implementation path while runtime configuration selects another. Production telemetry may show an outcome without revealing its cause. When they disagree, preserve all applicable claims, identify authority, and route the discrepancy to a test, fix, policy decision, or incident process.

**Atomicity and synthesis test**

Before labeling a sentence, ask whether every clause has the same source, state, applicability, and consequence. For example:

> The local template contains a verification matrix, therefore the workflow reduces defects by 90 percent and every project should adopt it.

This is at least three claims:

- a locally inspectable artifact-content fact;
- an unverified quantitative causal claim requiring a suitable comparative study;
- a normative recommendation requiring evidence, alternatives, project context, and owner judgment.

One local file cannot support all three. Split the sentence and classify each claim honestly.

**Quantitative and causal claims**

Any number that influences a decision must identify:

- metric definition, unit, population, and sampling frame;
- baseline and candidate identities;
- workload, environment, time window, and exclusions;
- measurement method, raw data, invalid/failed observations, and uncertainty;
- equivalence and quality counter-gates;
- causal design or the explicit statement that the result is observational;
- no-generalization boundary.

Numbers inherited from source material remain source-attributed unless their underlying data and method were independently reproduced. Repetition across derivative artifacts does not create independent evidence. Unsupported precision should be removed or converted to an explicit unknown plus a verification plan.

**Source identity and freshness**

For local files, record path, relevant span or section, revision/working state, hash where useful, generator identity, and read completeness. For external sources, record publisher/owner, direct source, title, version, publication/update date, access date, supporting location, and applicability. For runtime observations, record deployed/build identity, configuration, workload, instrumentation, time, and authorization.

Reject or relabel a claim when:

- the source cannot be recovered or its identity is ambiguous;
- the cited location does not support the whole claim;
- the source version differs materially from the target;
- a derivative source cites another derivative source in a circle;
- apparently independent sources reproduce one underlying assertion;
- material counterevidence or negative cases were omitted;
- the evidence is stale under a changed producer, consumer, environment, or policy;
- a proposed method is written as a completed result.

Freshness is claim-specific. A stable mathematical definition and a rapidly changing tool schema need different review triggers. Record the trigger rather than applying one arbitrary expiry period.

**Contradiction handling**

When evidence conflicts:

1. confirm that both claims are atomic and actually applicable to the same target and decision;
2. compare source identity, version, authority, conditions, and measurement capability;
3. preserve each claim and the exact disagreement;
4. identify whether an owner, source inspection, controlled experiment, broader workload, or production observation can discriminate;
5. protect the higher-consequence branch while uncertainty remains;
6. record resolution, residual risk, and why losing evidence was rejected or superseded.

Do not average incompatible policy and behavior claims. Do not choose the newest source merely because it is newer, or the official source when the question is an observed implementation defect. Authority depends on the question.

**Examples**

Good local evidence:

> `local_observation_fact`: For the frozen assignment artifact, the focused structural verifier counted 26 reference headings in seed order and 260 exact packet questions. The conclusion is limited to that artifact identity and verifier capability.

This supports structural compliance. It does not prove semantic quality, universal workflow effectiveness, or future compatibility.

Bad quantitative evidence:

> `external_research_sourced_fact`: This workflow improves productivity by a precise percentage because a public URL appears in the source map.

The label is invalid unless the source was inspected, the claim and method match, applicability is established, and the intended decision tolerates the study limitations. This evolution did not perform that external validation or a productivity experiment.

Borderline contract/behavior conflict:

> The current official contract says one error state should be retried, while a controlled local fixture observes that the installed wrapper classifies it as terminal.

Keep an `external_research_sourced_fact` for supported policy, a `local_observation_fact` for the installed behavior, and a `conflicting_evidence_state` for compatibility. Route to version inspection, reproduction, and the owning implementation or policy authority.

Good synthesis:

> `combined_evidence_inference_note`: Immutable source identities reduce stale-work acceptance because local validators can compare the current artifact with the producer input before integration; this does not establish a universal productivity gain.

The premises, mechanism, bounded recommendation, and no-claim boundary are explicit.

**Evidence audit**

Run structural and semantic review together:

1. Enumerate consequential claims and reject mixed atomicity.
2. Verify every provenance label has recoverable source identity and a supporting location.
3. Check hashes, versions, dates, access outcomes, and target applicability.
4. Group duplicate and derivative sources by underlying producer/claim.
5. Confirm each quantitative value has a method and each causal claim has a suitable design.
6. Trace requirements to capable checks and observations to retained raw evidence.
7. Search for contradictions, negative cases, expected failures, and absent authorities.
8. Sample claims and ask whether an independent reviewer can reconstruct the same bounded decision.
9. Remove one source at a time conceptually to expose circularity and single-source fragility.
10. Allow unresolved states when honest; fail only hidden, falsely supported, or falsely resolved claims.
11. Re-run focused artifact checks and the required broader suite after revisions.
12. Record the final known, unknown, conflicting, and owner-decided ledger.

Automation can verify labels, links, hashes, states, required fields, duplicate values, and traceability shape. It cannot by itself decide whether nuanced prose follows from a source, whether a policy owner accepted risk legitimately, or whether the evidence depth is proportionate. Those require semantic and authority review.

**Current known and unknown boundary**

Known from this local evolution and its recorded checks:

- the seed, evolved reference, packet, local mapped producers, and verification commands have identifiable workspace paths;
- the reference retains its original heading-defined structure;
- packet shape, counts, exact question text, field population, and uniqueness can be checked deterministically;
- source/reference length, hashes, marker scans, table/fence structure, whitespace, and reread progress can be observed locally;
- the refresh query backlog was not executed and no external page was opened.

Not established by this evolution:

- external source freshness or continued availability;
- universal effectiveness of the metapattern workflow;
- defect, productivity, onboarding, context-accuracy, or quality improvement percentages;
- target-system performance, p50/p95/p99, capacity, reliability, or production behavior;
- portability across every language, repository, agent, reviewer, organization, or risk class;
- owner acceptance for policies outside this assignment's file authority.

These unknowns do not invalidate the structural and systems guidance. They constrain its claims and identify the next discriminating route. An unknown is useful when paired with consequence, owner, and verification action; confidence without that record is not.

Evidence typing turns this digest into a versioned claim graph rather than a static authority artifact. The strongest future implementation will be able to show which recommendations become unsupported when a source, producer version, check, observation, or owner decision changes. Add structured machinery only when it measurably improves that reconstruction; retain readable causal explanation so humans can still judge applicability and tradeoffs.
