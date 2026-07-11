# Ai Native Explanation Patterns

Use this reference to turn dense AI-native engineering material into a plain-English explanation that helps one named audience make one concrete next decision. The default reader is a curious beginner, a non-engineer teammate, or a new developer who needs the idea before the jargon. The output is not merely shorter prose: it must preserve the source's core claim, causal reasoning, important limits, exact terms that matter, and evidence status.

The recommended teaching arc is progressive disclosure. Start with the big idea in one sentence. Give a short mental model or story. Explain the major concepts through one bounded everyday analogy each. Then restore exact terminology, show a concrete example or counterexample, and end with rules the reader can apply plus one sticky sentence they can repeat accurately. Plain words come first; technical words are defined once rather than removed.

Choose this format for onboarding, architecture orientation, agent-method explanations, and dense notes whose first barrier is vocabulary. Route elsewhere when the reader needs an executable specification, command sequence, security policy, benchmark report, exhaustive reference, or production runbook. A plain-language overview may introduce those artifacts, but it must not replace authoritative detail where exact behavior or consequence controls correctness.

Keep simplicity honest. Analogies are bridges with boundaries, not proof. Claims such as "67% faster" or "90% fewer bugs" remain claims from the source unless independently measured in the target project. A friendly explanation fails if it becomes wrong-but-cute, repeats hype as fact, drowns the reader in new jargon, or gives a memorable slogan without the causal steps that make it useful.

Verify two dimensions separately: fidelity and comprehension. A source-aware reviewer checks that the explanation preserves meaning, conditions, and uncertainty. A representative reader should be able to teach back the idea, identify the next action and stop condition, and predict how the principle applies to a new example. A readable paragraph that teaches the wrong model does not pass; a perfectly faithful paragraph that the intended reader cannot use does not pass either.

## Source Evidence Mapping Table

This table is a retrieval map, not a vote count. The two local files answer different questions: the skill defines how to teach a smart beginner, while the ELI5 note demonstrates one explanation of the repo's AI-native meta-patterns. The three public URLs are retained context or verification pointers. They do not become current evidence unless inspected for the exact product, version, and claim.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/explain_ai_native_eli5/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/explain_ai_native_eli5/references/ai_native_engineering_eli5.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | unrefreshed_external_pointer | primary agent instruction context model |
| https://docs.github.com/actions | external_research_source_material | unrefreshed_external_pointer | verification and automation model |
| https://agents.md/ | external_research_source_material | unrefreshed_external_pointer | general agent instruction format |

Use the sources in this order:

1. Read the user's actual source or the specific material being explained. It governs subject content, including claims, terms, examples, and uncertainty.
2. Read `explain_ai_native_eli5/SKILL.md` for audience, writing rules, the three-layer workflow, analogy discipline, output shape, and completion checks.
3. Inspect `ai_native_engineering_eli5.md` when the task concerns this repo's meta-patterns or when a worked transformation helps calibrate tone and depth. Do not substitute it for a different source.
4. Use public documentation only to resolve a named question about instruction context, automation, verification, or general agent format. This no-browse pass preserves those links but does not confirm their current content.
5. Stop loading evidence when the core claim, important terms, material caveats, one concrete example, and a verification method are covered for the named audience.

Source authority is claim-specific. A local writing skill can govern output style without validating "67% faster" or "90% fewer bugs." An example can demonstrate a drawer-label analogy without proving that four-word names are universally optimal. GitHub Actions can illustrate automated checks without establishing every workflow as equivalent. Reader feedback verifies comprehension and usefulness; it does not establish the truth of the engineering claim being taught.

For each consequential explanation element, record the selected source and span, what it establishes, what remains inference, the intended audience decision, and the check that would reveal distortion. Prioritize memorable numbers, analogies, and action rules because those are most likely to be reused after their original context is forgotten. Record intentionally skipped sources and why so brevity remains deliberate rather than accidental.

When a required content source is missing, request it or produce a clearly bounded teaching framework. Do not reconstruct a confident explainer from theme keywords. When sources conflict, preserve the conflict, narrow the statement, and route the reader to the authoritative detail instead of forcing a beginner-friendly certainty that the evidence does not support.

## Pattern Scoreboard Ranking Table

The scores below are inherited corpus-prioritization metadata. They preserve ordering across generated references; they are not learner-outcome measurements, probabilities, confidence levels, or proof that a 95-point pattern is more effective than an 88-point pattern. Audience fit, source consequence, and risk of misunderstanding may override numeric order.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `ai_native_explanation_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local ai native material before synthesizing explanation patterns recommendations. |
| `ai_native_explanation_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `ai_native_explanation_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

Use the three patterns as controls inside the local teaching workflow:

1. **Source Map First:** identify the subject source, the local explanation method, and only the external evidence needed for unresolved claims. The artifact is a ranked source ledger, not a pile of links.
2. **Evidence Boundary Split:** distinguish what the source says, what an analogy interprets, what a public source establishes, and what remains editorial judgment. Numbers and current product behavior receive explicit status.
3. **Verification Gate Coupling:** verify source fidelity and reader transfer separately. The explanation must preserve the claim and let the intended reader identify or apply the next action.
4. **Repair the failed layer:** an unsupported metric returns to evidence; a confusing paragraph returns to audience and teaching structure; an overextended analogy receives a boundary or replacement; a failed action test revises the operating guidance.

Each control leaves evidence that a reviewer can inspect: selected sources and spans, claim labels, analogy-to-term mappings with limits, and comprehension or decision fixtures. For a low-risk one-sentence definition, one source and one teach-back check may be enough. A durable onboarding reference or quantitative engineering claim deserves deeper traceability and broader representative-reader review.

The triad is necessary but not sufficient. It controls evidence and release discipline; the local skill supplies the audience model, plain-words-first rule, three teaching layers, concrete example, low-drama tone, and sticky ending. An explanation can be perfectly sourced yet unusable, or beautifully simple yet false. Both dimensions must pass.

**Application contrast:** A good explanation attributes a source-reported speed claim, uses the drawer-label analogy as bounded interpretation, restores the exact naming term, and asks the reader to choose a clearer name in a new example. A bad explanation cites several sources, repeats "AI works better," and declares success because the prose is short. A borderline explanation is factually accurate but uses an analogy that hides an important exception; constrain reuse until the exception is taught and tested.

Change scores only with recorded criteria or observations. More importantly, maintain the dependency path `source -> claim -> analogy or explanation rule -> reader check -> owner`. That path enables targeted refresh when a source or audience changes without turning every edit into a complete rewrite.

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The local row for `ai_native_explanation_patterns` contains two source paths. The skill is the canonical teaching-method entrypoint: it names the default reader, plain-words-first rule, one-analogy-per-concept guidance, three explanation layers, Markdown shape, source-claim guardrail, and done check. The ELI5 note is a worked explanation of this repository's AI-native meta-patterns. It demonstrates method application but does not independently prove the source note's quantitative or causal claims.

`external_research_sourced_fact`: The external map retains public pointers for agent instruction context, automation, verification, and general instruction format. They may clarify a specific subject claim when refreshed. Because this pass performs no browsing, their current content and version alignment remain unverified; they are not new present-tense evidence here.

`combined_evidence_inference_note`: Reliable AI-native explanation requires four connected decisions. First, identify one reader and the decision they need to make. Second, separate subject-source facts, source-reported numbers, external facts, analogies, and editorial inference. Third, teach through a big idea, bounded mental model, exact terms, concrete example, and actionable takeaway. Fourth, verify fidelity and reader transfer independently.

Adopt source wording when it is already clear and precise. Adapt dense material when jargon or structure blocks the named reader, while preserving terms and caveats that control correctness. Avoid an ELI5-only artifact when exact syntax, policy, measurement, or production procedure is the real need. If sources conflict, explain stable common ground, label disagreement, and route consequential detail instead of manufacturing beginner-friendly certainty.

The causal sequence is `source -> claim -> teaching choice -> reader model -> next action -> check`. A correct source does not guarantee an effective explanation, and a memorable analogy does not guarantee a correct reader model. High fidelity with low transfer calls for teaching repair; high memorability with low fidelity calls for content repair. Keep those diagnoses separate.

For reusable explanations, maintain the reader belief and action produced by each major section. When evidence changes, review the linked claim, analogy, example, and comprehension fixture. When the audience changes, preserve source truth while adjusting prerequisite knowledge, vocabulary, and examples. Ephemeral answers can use lighter records; shared onboarding and decision references need ownership and refresh triggers.

## Local Corpus Source Map

The local corpus has two complementary roles. The skill is normative for the repository's explanation method; the reference is illustrative for one AI-native subject. Neither should displace the actual notes, code, policy, or research that the user asks to understand.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/explain_ai_native_eli5/SKILL.md | explain_ai_native_eli5 | Explain AI Native ELI5; Goal; Default Reader; Writing Rules; Workflow; AI-Native Cheat Sheet | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/explain_ai_native_eli5/references/ai_native_engineering_eli5.md | AI Native Engineering ELI5 | AI Native Engineering ELI5; Big Idea; The Easy Mental Model; The Main Ideas Made Simple; 1. Good names are like drawer labels; 2. Tests are like the answer key before the exam | reference detail file for deeper pattern evidence |

| local_source_role | decisions_it_can_govern | decisions_it_cannot_govern_alone |
| --- | --- | --- |
| skill entrypoint | default reader, plain-words-first style, exact-term restoration, short sections, analogy discipline, three teaching layers, Markdown output, source-claim guardrails, and done check | truth of the subject's technical or quantitative claims, or whether one analogy works for every audience |
| worked ELI5 reference | local tone, depth, progression, concrete examples, sticky takeaway, and treatment of the repo's naming, tests, context, and agent ideas | a different user's source content, current platform behavior, universal effectiveness, or required implementation detail |
| actual task source | claims, terminology, conditions, examples, disagreements, and uncertainty that the requested explanation must preserve | the best teaching order or evidence that the audience understood it |
| audience evidence | whether representative readers can teach back, distinguish boundaries, and apply the idea | whether the subject claim is objectively true |

For a substantial or reusable explainer, read the skill completely, then the user's source completely. Load the built-in ELI5 note when the subject matches or when calibration would reduce uncertainty about tone and depth. For a short low-risk definition, the skill's core checklist may be sufficient. Always return to the user's source after reading an example so familiar drawer, answer-key, bookmark, or backpack metaphors do not silently shape unrelated claims.

The two mapped files are locally coherent: both emphasize a fast big idea, plain language, simple analogies, concrete examples, and caution around reported performance claims. That agreement establishes repository convention, not independent pedagogical proof. The skill takes precedence for method because it explicitly states rules and guardrails; the note demonstrates one implementation and may omit constraints for brevity.

Stop or route when the request needs capabilities the map does not supply. Use the subject's code and tests for executable detail, a visual-layout method for a diagram companion, primary research for scientific claims, product documentation for current behavior, and representative readers for comprehension evidence. One owner should reconcile these inputs into a coherent teaching arc rather than allowing each specialist to produce a disconnected fragment.

Verify the local map at three levels: paths and contents exist; the explanation's method choices and subject claims trace to relevant spans; and the intended reader can use the result. Audit from analogy back to technical term as well as source forward to prose. If the supporting claim disappears during refresh, remove or replace the analogy rather than leaving a memorable orphan.

## External Research Source Map

These public sources are bounded analogues. They can make context loading, automated verification, and reusable instruction structure concrete, but they do not define AI-native engineering as a whole and they do not replace the local explanation method or the user's subject source.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | primary agent instruction context model | unrefreshed_external_pointer |
| https://docs.github.com/actions | GitHub Actions documentation | verification and automation model | unrefreshed_external_pointer |
| https://agents.md/ | AGENTS.md open format | general agent instruction format | unrefreshed_external_pointer |

| external_source | appropriate_explanation_use | invalid_extrapolation |
| --- | --- | --- |
| OpenAI Codex AGENTS.md guide | illustrate that project instructions shape the context an agent receives | claiming that one product's loading semantics define every agent system or current host behavior |
| GitHub Actions documentation | illustrate checks that run automatically and turn expectations into repeatable evidence | treating CI automation as equivalent to TDD, correctness, or all AI-native workflow design |
| AGENTS.md open format | illustrate a shared instruction surface intended for predictable agent guidance | copying format or precedence claims into an incompatible host without validation |

No browsing was performed during this evolution pass. The URLs and intended roles are preserved, while current content, redirects, versions, and exact supporting passages remain unverified. Before using one for a present-tense claim, record the access date, product or installed version, relevant passage or implementation location, the concept it illustrates, and the sentence that states where the analogy stops.

Use an authority order appropriate to the question. Supported official documentation governs documented product semantics. Installed help, schemas, or controlled local behavior can answer version-specific operational questions. Public repositories may clarify implementation but can expose unreleased or incidental behavior. Community formats support portability discussion, not vendor-specific guarantees. If sources disagree, preserve the conflict and narrow the example rather than teaching a forced certainty.

Make the concept understandable before naming the product. For example: "Automated checks are like a referee who applies the same written rule every time. GitHub Actions is one system that can run such checks." That teaches a transferable mechanism. The claim "GitHub Actions proves TDD works" is invalid because automation and test-first design are distinct decisions.

Keep product examples modular. A durable explanation should retain a product-neutral mental model and isolate current implementation examples so they can be refreshed without rewriting the core. Verify that a reader can still explain the principle when the product name is removed. If the explanation collapses, it is probably teaching the tool instead of the concept.

Stop external discovery when more detail no longer changes the core model, a material caveat, a concrete example, or the reader's next action. When no current authoritative evidence is available, preserve the source as a future refresh target and label the operational statement as uncertain instead of searching until a convenient confirmation appears.

## Anti Pattern Registry Table

Use this registry to decide whether an explanation can be released, needs a targeted repair, or should be routed to a more exact artifact. The decisive question is not whether every sentence is elegant. It is whether a defect would change the reader's belief, confidence, or next action. A memorable false model, an unattributed quantitative claim, or an instruction with no stop condition blocks durable publication. A minor stylistic rough edge can remain when it does not obstruct comprehension or alter meaning.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | The writer skips the local corpus and substitutes generally plausible advice, so the result may be polished yet unrelated to the repository's actual method. | source_map_first_synthesis | Trace every material recommendation to a listed local source or mark it as bounded synthesis; also ask which source-specific distinction would disappear if the prose were generic. |
| unsourced_recommendation_claims | Guidance appears authoritative without distinguishing source evidence, external context, and editorial judgment. Readers cannot tell what can be repeated as fact. | evidence_boundary_split_pattern | Label the origin and confidence of quantitative, causal, historical, and normative claims; sample each label against the underlying passage. |
| unverified_agent_instruction | A recommendation cannot be checked by a command, inspection, or reader outcome, so compliance becomes a matter of tone rather than evidence. | verification_gate_coupling | Require a concrete gate with an observable pass condition, then confirm that passing the gate actually supports the claim rather than merely checking formatting. |
| wrong_but_cute_simplification | A charming story removes the condition that makes the concept true. It is easy to remember and therefore easy to propagate into later decisions. | simple_then_exact_restoration | State the simple model, restore the exact term and omitted condition, and include one counterexample where the shortcut stops working. |
| jargon_substitution | Technical words are exchanged for fashionable AI vocabulary rather than explained. The apparent simplification moves the prerequisite instead of removing it. | plain_words_then_defined_terms | Circle every term a new reader may not know, define each once in ordinary language, and remove synonyms that add no new distinction. |
| analogy_overreach | Correspondence between analogy and mechanism is left unlimited, causing readers to infer properties the real system does not have. | bounded_analogy_mapping | Name what maps, what does not map, and where the analogy must be abandoned; test the model against a near-boundary example. |
| hype_as_explanation | Superlatives, inevitability, or dramatic outcome claims replace a causal account. Confidence rises while inspectable understanding does not. | mechanism_evidence_uncertainty_sequence | Remove promotional adjectives, describe the mechanism, attribute evidence, and state what remains project-specific or unmeasured. |
| audience_free_explanation | No reader, prerequisite, or decision is named, so the draft oscillates between basic definitions and expert shorthand. | audience_decision_contract | Record who the reader is, what they already know, what they must decide next, and which detail belongs in a linked advanced artifact. |
| source_map_without_synthesis | The output lists files or quotations but never resolves their relationship into a usable mental model. Retrieval is mistaken for explanation. | claim_relationship_teaching_arc | Connect sources through one governing idea, show agreement or tension, and derive a bounded rule the reader can apply. |
| actionless_summary | The reader can repeat the topic but cannot recognize when to use it, what to do first, or when to stop. | rule_example_stop_condition | End with a decision rule, a concrete worked example, a counterexample or limit, and an observable completion check. |

Review in six passes: identify the reader decision; trace material claims; inspect analogy correspondence; test the examples and counterexamples; ask for teach-back and application to a new case; then delete prose that does not improve fidelity, understanding, or action. Deletion is a legitimate repair. Adding another paragraph cannot rescue a vivid analogy that encodes the wrong mechanism.

Use a lightweight version of this review for a one-off conversation: verify the consequential claim, ask the reader to restate the idea, and qualify reuse. Use the full sequence for onboarding pages, reusable prompts, templates, or references that other agents will copy. Durable artifacts have a wider propagation radius, so they need source ownership, regression examples, and a way to update downstream copies when the model changes.

Good, bad, and borderline fragments expose different failure modes. "Context is like a backpack: capacity is limited, so choose task-relevant material; unlike a backpack, attention quality can also decline as distracting text grows" is bounded and restores the mechanism. "The AI forgets like a child" is bad because it anthropomorphizes several different context failures and supplies no operational response. "Tests are the model's answer key" is borderline: it may introduce feedback, but it becomes misleading unless the explanation also says that tests can be incomplete and that refactoring preserves behavior while improving design.

Verification must combine deterministic and semantic checks. Structure checks can confirm that sources, evidence labels, examples, limits, and gates exist. A source-aware reviewer must still test whether they are accurate. A representative reader must be able to teach back the claim without inheriting the analogy's fictional properties, choose the right action in a new case, and identify a case where the rule should not be used. As a stronger regression probe, remove a caveat or substitute an attractive but inaccurate analogy and confirm that review catches the conceptual mutation.

The seed's three failures and the explanation-specific warnings from the inspected local skill are reliable review categories. Their prevalence and relative severity are not measured here, so rank them by consequence and reuse rather than pretending to have universal frequencies. Record which checks cause real revisions, retire warnings that no longer discriminate quality, and promote recurring high-impact defects into templates and examples. A registry that only grows eventually becomes background noise; maintained selectivity is part of its reliability.

## Verification Gate Command Set

`verification_gate_command_set`: Treat verification as a ladder, not a single green light. Run cheap assignment-local checks first, investigate their failures before continuing, and retain semantic review even after every command exits successfully.

**Gate 1, saved-section sanity:** Immediately after each section, confirm that its packet contains ten exact question headings and sixty populated mandatory fields, that the matching reference heading still occurs once, and that the rewritten section is longer than the archive seed. Also scan both saved sections for prohibited work markers. This gate catches truncation, an edit applied at the wrong boundary, and accidental heading drift while the repair is still small.

**Gate 2, focused file policy:** Run the current single-file verifier from the repository root:

```bash
python3 tests/verify_idiomatic_reference_file.py \
  --path idiomatic-ref-202607/ai_native_explanation_patterns-20260710.md
```

Do not reduce its result to the exit code. Record the reported reference section count, packet section count, question count, field count, exact-text unique field count, expansion result, heading-order result, and marker result. For this reference the intended final counts are 26 reference sections, 26 packet sections, 260 questions, 1,560 mandatory field values, and `uniqueFieldCount=1560`.

**Gate 3, source-aware comparison:** Compare all 26 heading texts and their order against the archive seed, then compare each complete section rather than only the line count. A section passes when it retains the seed's accurate facts, makes its evidence boundaries clearer, and adds usable causal explanation, limits, alternatives, examples, verification, uncertainty, or second-order consequences. More characters are necessary for this evolution task but not sufficient: duplicated prose and invented authority are failures even when the size check passes.

**Gate 4, explanation fidelity and transfer:** Have a source-aware reviewer identify each material claim's origin and check that analogies do not add fictional properties. Then ask a representative reader to state the main idea in their own words, identify the next action and stop condition, apply the rule to one unseen example, and name a case where it should not be used. Record the audience's prerequisites. One successful reader session supports that bounded case; it does not prove universal accessibility.

**Gate 5, corpus integration:** The archive seed records this final-stage command:

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

The command currently exposes `--stage {red,final}`. It is broader than one Delta assignment, so in a shared workspace it may report failures owned by references that are still being evolved. Preserve that evidence, localize every failure to its path, and never repair another lane merely to make a global result green. A focused pass plus an attributable unrelated corpus failure is different from a target-file failure, but the wider queue still remains unfinished.

Use a risk-to-gate match when the edit is small. A punctuation correction may need saved-section and focused checks plus a quick semantic reread. A changed analogy needs source mapping, boundary review, and a new-case reader exercise. A changed quantitative claim needs provenance and measurement review. A changed reusable template needs downstream inventory and regression examples because its propagation radius is larger.

Good verification says, for example, "the focused verifier passed this exact path with 26/260/1,560 counts; all 1,560 field values are unique; all sections exceed their seeds; a new developer correctly applied the context-budget rule to a code-review example and rejected it for an exact legal specification." Bad verification says "the prose looks clear." A borderline result is a structurally perfect file whose reader repeats the analogy but reverses the causal mechanism; that file remains unverified for explanation quality.

Commands provide reproducible evidence only for their encoded assertions. Inspect the verifier when policy changes, run it against the current saved state, and retain the tested path and result in the progress journal. Improve the ladder when a consequential defect escapes: add a fixture, rubric question, or assertion that would catch the same class of error, but do not accumulate low-signal checks indefinitely. The maintained goal is the smallest set of independent gates that supports every consequential release claim.

## Agent Usage Decision Guide

`agent_usage_decision_guide`: Use this reference when a task mentions AI-native explanation, one of the listed local source paths, or a nearby technology or workflow whose first barrier is vocabulary. Before drafting, decide whether the requested deliverable should be a plain-language explanation, an accessible introduction attached to a more exact artifact, or a different artifact entirely.

Follow this default sequence:

1. Name the reader, their likely prerequisites, the question they are trying to answer, and the next decision or action the explanation should enable. Infer low-risk details from context, but state or ask about an assumption when it would change the artifact route.
2. Start with the local corpus source map. Read both the explanation-method source and the subject source; one governs how to teach, while the other governs what may be claimed.
3. Extract the governing idea, causal steps, exact terms, conditions, counterexamples, quantitative claims, and uncertainty before choosing an analogy.
4. Choose the smallest teaching arc that removes the reader's prerequisite barrier: main idea, bounded mental model, exact vocabulary, concrete example, applicable rule, and sticky recap.
5. Prefer patterns with explicit verification gates. Attach each consequential recommendation to an observable result, source check, reader exercise, or linked authority.
6. Treat external sources as freshness and ecosystem checks, not replacements for local repository conventions. Under a no-browse constraint, retain them as unrefreshed pointers rather than current evidence.
7. Preserve evidence-boundary labels when reusing recommendations. Source-specific outcomes stay attributed unless independently reproduced in the target setting.
8. Verify fidelity and transfer separately, then route the reader to the next layer of detail instead of forcing every technical caveat into the first explanation.

| task_signal | recommended_artifact | reason_and_boundary |
| --- | --- | --- |
| A new teammate asks what context offloading means and why a plan file helps. | Plain-language explanation | The primary gap is a mental model; define the exact term, bound the analogy, and end with a small usage rule. |
| A developer asks how to perform a release in this repository. | Runbook or exact procedure with a short explanation in front | Commands, preconditions, failure recovery, and authoritative order control correctness; a metaphor may orient but cannot replace them. |
| A reviewer asks whether a latency claim is true. | Benchmark report or measurement plan | The decision depends on environment, workload, statistics, and reproducible evidence rather than explanatory simplicity. |
| A product partner asks why tests help an agent implement a feature. | Explanation linked to the actual acceptance tests | The concept benefits from plain language, but the repository's tests remain the inspectable contract. |
| A team must approve a security or legal requirement. | Policy, threat model, or specification | Consequence demands exact definitions and precedence; provide a glossary or overview only as a companion. |
| An expert asks two architectures to be compared. | Decision memo with a concise shared mental model | Plain language can expose causal disagreement, while explicit alternatives, constraints, and evidence carry the decision. |

This route works especially well for onboarding, architecture orientation, concept comparisons, method explanations, and summaries of dense notes. It also helps experts when familiar jargon hides different causal assumptions. Adjust vocabulary and density to the reader; do not assume that plain language requires a childish voice or that an expert needs no definitions.

Do not silently turn a request for exact API behavior, an executable specification, an incident procedure, a security control, a benchmark, or acceptance criteria into an explainer. For mixed requests, split the output: provide a short orienting model, name the authoritative artifact, state which one has precedence, and connect them with a clear handoff. This keeps the front door accessible without making abstraction carry operational weight it cannot safely bear.

Three routing examples sharpen the boundary. A good agent explains a context budget as deliberately selecting task-relevant material, restores the exact notion of limited attention, and asks the reader to apply it to a code review. A bad agent replaces a deployment rollback procedure with a "safety net" story and omits commands and stop conditions. A borderline agent clearly explains why benchmarking matters but repeats the source's performance number as a general fact; the teaching is useful, yet the evidence boundary is wrong.

Audit the route by checking that the named reader and next action agree with the chosen artifact, every material claim can be traced, the analogy has an explicit boundary, linked exact detail has a clear source of truth, and the reader can apply the rule to a new case. Keep detailed routing rationale in the working packet when it would clutter the reader-facing explanation. The final artifact should expose the assumptions and boundaries needed for correct use, not the entire editorial process.

When an ephemeral answer is stored, templated, broadly linked, or used for consequential decisions, promote it to a maintained reference. Give it an owner, source list, refresh triggers, and at least one regression example that catches its most plausible distortion. Propagation and consequence, rather than polish alone, determine that maintenance threshold.

## User Journey Scenario

Role-based opening scenario: a new contributor or agent starts from an unfamiliar AI-native theme and must decide whether this reference is the right tool. The user has an `ai_native_explanation_patterns` task, one or more local source paths, and uncertainty about which pattern should drive the explanation. They need to choose what to load, what to trust, what to avoid, what artifact to produce, and what evidence proves that a reader can use it.

Open this file when the task mentions AI-native explanation patterns, any mapped local source path, or an adjacent workflow whose primary failure mode is prerequisite-heavy prose. Do not treat the trigger as automatic permission to simplify an exact contract. First determine whether an explainer is the deliverable or merely the introduction to a specification, runbook, benchmark, policy, or implementation.

**Stage 1, arrive and frame:** The contributor starts with a broad request such as "Explain why context selection matters for coding agents." They name a provisional audience, current prerequisites, the decision the reader must make, and the consequence of a wrong model. The stage is complete when the contributor can state: "A new developer should be able to choose which repository context to load for a small code review and explain why." If the decision cannot yet be named, exploration continues with a clearly marked provisional question rather than an invented final purpose.

**Stage 2, orient to evidence:** The contributor reads the local method source to learn the explanation constraints, then reads the subject source to identify the actual claim, mechanism, limits, exact vocabulary, examples, and evidence status. Public URLs remain secondary pointers under the no-browse constraint. The evidence artifact is a compact claim map that distinguishes source facts, source-reported measurements, and editorial synthesis. This stage ends when every material teaching claim has a source or an explicit judgment label.

If local subject evidence is absent, pause claims that depend on it and either request the missing source or produce a narrowly labeled conceptual overview. If local sources conflict, expose the conflict and route it for resolution rather than averaging it into smooth prose. If the requested decision is high-consequence and exact, keep the overview bounded and attach the authoritative artifact that governs action.

**Stage 3, build the mental model:** The contributor writes the main idea before selecting an analogy: context is finite, and selecting task-relevant evidence can improve the model's chance of making a grounded decision. They may use a backpack to introduce capacity, but explicitly say that model attention is not a physical container and that extra distracting text can affect quality even when it technically fits. Exact terms such as context window, relevance, and source boundary are then restored. This stage passes when a source-aware reviewer can map every part of the explanation back to the mechanism and identify where the analogy stops.

**Stage 4, test understanding:** A representative new developer explains the idea in their own words. They are then shown an unseen code-review task with a changed function, a nearby test, an unrelated large design document, and a stale incident log. They choose the changed function and relevant test first, justify the exclusion of unrelated material, and name when broader blast-radius context would be needed. Remembering the backpack story is not enough. The observable result is a correct new-case selection with a bounded reason.

If teach-back fails, return to the earliest faulty assumption or causal step. Do not append more detail indiscriminately. A reversed causal claim requires repairing the core model; an undefined term needs a local definition; a correct model with a wrong new-case choice needs a better contrastive example or decision rule. In a live explanation, this loop can happen immediately. In an asynchronous reference, regression examples and reviewer notes carry the feedback forward.

**Stage 5, act and stop:** The contributor turns comprehension into an executable next step: inspect the task, select direct evidence, add broader context only when an identified dependency or uncertainty requires it, and stop when the decision can be justified against the source and verification fixture. For an exact operational task, this stage hands off to the linked procedure and states that the procedure takes precedence over the analogy.

**Stage 6, preserve and improve:** The contributor records source paths, important evidence labels, verification results, unresolved uncertainty, and refresh triggers if the explanation will be reused. A one-off conversation may retain only the consequential claim check and reader correction. A maintained onboarding artifact needs an owner and regression fixture. Repeated confusion at the same stage should update the source documentation, glossary, example, or routing rule rather than be blamed on each new reader.

The good outcome is not "the reader liked the story." It is that the reader can reconstruct the core claim, choose correctly in a changed case, recognize the boundary, and reach the next authoritative artifact. A bad outcome is a generic AI summary assembled without the local corpus. A borderline outcome is a reader who fluently repeats the analogy but still loads every available file; that journey has achieved recall without operational transfer and must loop back before release.

This six-stage journey is a default, not a fixed ceremony. Compress it for low-risk familiar material when the decisions and evidence remain visible. Add facilitated dialogue or expert review when uncertainty and consequence justify the cost. Time follows risk and unresolved assumptions, not a predetermined number of explanation rounds.

## Decision Tradeoff Guide

Choose among adoption, adaptation, and routing by evaluating six variables: local evidence fit, source freshness, audience prerequisites, decision consequence, reuse horizon, and available verification. Do not infer fit merely because two sources use similar words. Their conditions, evidence status, or intended actions may differ.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | The canonical local subject claim, evidence status, audience model, and target decision align; any public evidence used as a freshness check does not reveal a material conflict. | This is the fastest path and preserves local vocabulary, but it can copy stale assumptions or an example that no longer fits the reader. | Can each material claim and condition be traced, and does a representative reader apply the unchanged model correctly to the target decision? |
| Adapt when | Local sources are strong but the audience, example, delivery mode, product surface, or current ecosystem context differs. | Adaptation preserves repository fit while increasing author-owned inference and synchronization cost. | Are source fact, observed external fact, presentation change, and combined inference distinguishable, and is the new boundary verified? |
| Pause or route when | Evidence is thin or conflicting, the requested output requires exact operational authority, or the explanation pattern is unrelated to the user's actual journey. | Routing prevents false confidence but may delay a complete answer or require research, expert review, a specification, or a runbook. | Does the output preserve the bounded supportable portion, name what blocks the remainder, and point to the artifact or evidence that resolves it? |
| Cost of being wrong | Incorrect AI-native explanation guidance can send an agent to the wrong files, tests, abstraction, or confidence level. | The immediate cost is a wasted implementation and review loop; propagated false models also increase correction and maintenance work. | Would a reviewer know which belief and action to undo, which downstream artifacts may contain it, and what evidence should be inspected next? |

Adoption means faithful reuse under matched conditions, not copying sentences without review. Minor vocabulary or example changes are still presentation adaptations, and they should be visible in the working record even when they introduce no new factual claim. Meaningful adaptation is a first-class choice rather than an embarrassed compromise: the author owns the inference connecting source material to the new setting.

When "avoid" is too coarse, choose a reason-specific recovery. Missing factual evidence calls for source inspection or bounded uncertainty. A mismatched audience calls for a redesigned teaching arc. A high-consequence exact action calls for a companion authoritative artifact. Conflicting sources call for explicit disagreement and resolution. Give the supportable part immediately when useful, but do not fill the unresolved part with fluent generalities.

| tradeoff_pair | recommended_default | accepted_cost | reverse_the_choice_when | verification_question |
| --- | --- | --- | --- | --- |
| Simplicity versus fidelity | Use plain words first, then restore exact terms, conditions, and one boundary. | The explanation is slightly longer than a slogan. | The added detail does not change belief or action and overwhelms the named reader. | Can the reader state both the simple rule and a case where it stops? |
| Analogy versus mechanism | Use at most one bounded analogy per major concept and map it back to causality. | Analogy review takes time and some mechanisms remain less vivid. | The audience already understands the mechanism or the analogy creates more prerequisites than it removes. | Can a reviewer list what maps, what does not, and which inference would be invalid? |
| Breadth versus cognitive load | Teach only the concepts required for the next decision, then link deeper layers. | The first artifact is intentionally incomplete. | Omitting a concept would cause a predictable wrong decision or hide a safety condition. | Can the reader act correctly without the deferred material, and can they find it when needed? |
| Speed versus validation | Use quick local checks during drafting and source plus transfer checks before durable reuse. | Publication is slower than producing a fluent first response. | The output is ephemeral, low-consequence, and clearly qualified. | Is validation depth proportional to consequence and propagation? |
| One audience versus several | Optimize the main explanation for one named audience and route other depths to owned layers. | Multiple artifacts require synchronization. | The audiences share prerequisites and action closely enough that one layer remains clear. | Can each audience find its next action without skipping or wading through most of the artifact? |
| Local convention versus current public practice | Local sources govern repository behavior; current external evidence may trigger a labeled adaptation. | Local fit can preserve deliberate divergence or accidental staleness. | Public change affects correctness, compatibility, security, or the user's stated target. | Is the difference intentional, current, and documented with precedence? |
| Ephemeral answer versus durable reference | Keep one-off answers light; promote reused or consequential explanations to owned artifacts. | Durable references require sources, refresh triggers, and regression fixtures. | Reuse and consequence remain low and the answer will not drive shared behavior. | Who owns correction if this model is copied tomorrow? |

Progressive disclosure resolves some apparent binaries by sequencing them: a simple overview can lead to an exact appendix, and an analogy can precede a mechanism. It does not eliminate maintenance cost. Every additional layer needs a stable purpose, explicit precedence, and a refresh path when its source changes.

For example, adopt the local context-budget model when onboarding a new contributor to select evidence for a code review. Adapt it for legal document review by strengthening authority and completeness boundaries; omission has different consequences there. Reject it as a replacement for an exact token-accounting specification because a qualitative selection model cannot provide numerical contract behavior. The reversal variable is not the topic name but the decision and consequence.

Record the chosen option, source conditions, rejected alternative, expected cost of error, and a reversal trigger such as a changed source, failed reader fixture, new audience, or increased operational consequence. Predicted costs are judgment until observed, so do not invent precise forecasts. Track actual correction and refresh work. Over time, that evidence can show which seemingly cheap simplifications create the largest downstream burden.

## Local Corpus Hierarchy

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles. These labels describe a source's relationship to a claim and task; they are not permanent quality rankings. A file may be canonical for how to explain a concept and only supporting context for whether a technical or quantitative claim is true.

| local_source_filepath_value | corpus_hierarchy_role_and_scope | heading_signal_to_convert | required_contribution_and_exclusion | reviewer_question_to_answer |
| --- | --- | --- | --- | --- |
| `agents-used-monthly-archive/codex-skills-202603/explain_ai_native_eli5/SKILL.md` | Canonical primary source for explanation method, default reader, output shape, guardrails, and quality checks. It is not independent proof of subject outcomes. | `Explain AI Native ELI5`; `Goal`; `Default Reader`; the method, guardrails, and quality-check portions of the complete file. | Contribute audience-first framing, plain-words-before-terms, bounded analogies, progressive layers, concrete examples, sticky recap, and warnings against hype, jargon, exhaustive detail, and wrong-but-cute prose. Do not use its instructions as empirical evidence that an AI-native practice improves performance. | Does the artifact follow the source's teaching constraints while allowing subject complexity to change the route or depth? |
| `agents-used-monthly-archive/codex-skills-202603/explain_ai_native_eli5/references/ai_native_engineering_eli5.md` | Supporting detail source for the subject's big idea, mental models, examples, metrics presented by that source, and summary rules. It does not by itself verify those metrics in the target project. | `AI Native Engineering ELI5`; `Big Idea`; `The Easy Mental Model`; concept and example portions of the complete file. | Contribute the subject model and concrete teaching material. Preserve numbers and outcome statements as source-reported claims unless a separate measurement establishes them locally. Do not promote a memorable example beyond the condition stated by the source. | Can every borrowed model, example, and outcome be traced, bounded, and distinguished from new synthesis? |

Use the hierarchy in two passes. First read the complete skill to establish the intended reader and explanation guardrails without locking in an analogy. Then read the complete supporting reference to extract the governing claim, causal mechanism, exact terms, examples, conditions, evidence status, and uncertainty. Headings are orientation signals, not evidence substitutes. A relevant heading should lead to a complete passage read so that conditions outside the quoted line are not lost.

After extraction, build claim-level provenance. For each material output claim, record whether it comes from the method source, the subject source, the current task state, or editorial synthesis. The method source may justify "define the exact term after plain language"; the subject source may supply a context-window mental model; neither automatically proves that a reported percentage will hold in this repository. Connective prose needs less annotation, but causal, quantitative, historical, normative, and action-bearing claims need enough provenance for a reviewer to reconstruct their status.

The classification roles behave as follows:

- **Canonical** means the maintained source governs a defined decision within this assignment's scope. Record the scope and the evidence for precedence.
- **Supporting** means the source adds detail, examples, or corroboration without replacing the canonical rule for another concern.
- **Legacy** means the source remains useful for history or examples but no longer governs current behavior; identify its successor before reusing normative guidance.
- **Duplicate** means material repeats another source without independent authority; retain whichever path ownership and freshness establish, and avoid counting repetition as corroboration.
- **Conflicting** means two applicable sources imply incompatible beliefs or actions. Expose the disagreement, identify ownership and dates where available, and pause the affected recommendation until resolved.

Only canonical and supporting roles are observed in the two-path map above. The other definitions specify what to do if future refresh work finds those conditions; they do not assert that such files are currently present. Likewise, archive location alone does not prove obsolescence or current authority. Use task instructions, path lineage, source content, ownership evidence, and explicit supersession rather than guessing from a filename.

Good synthesis uses the skill to shape an adult beginner's teaching arc and the subject reference to supply the actual context model. Bad synthesis cites an instruction such as "use a sticky sentence" as evidence for a performance outcome. Borderline synthesis accurately copies a reported number but removes its source-specific status, causing a reader to repeat it as a universal fact. Fidelity includes preserving epistemic status, not merely preserving words.

Verify the hierarchy deterministically by confirming exact paths and recording source identity when reproducible handoff matters. Verify it semantically by reading each complete mapped source, sampling claim-to-passage mappings, and checking every transformed claim for changed scope or confidence. A content hash can show that reviewers inspected the same bytes; it cannot show that the file remains correct or canonical.

Treat this as a complete map for the local corpus explicitly assigned to this reference, not as a universal inventory of AI-native explanation evidence. If a mapped source changes, reopen only its dependent method rules, claims, examples, metrics, and reader fixtures first. That lightweight provenance graph makes refresh work targeted while preserving the option to broaden review when the changed claim is foundational.

## Theme Specific Artifact

Theme-specific artifact: an AI-native explanation brief with a worked example. Complete it before polishing durable prose so audience, evidence, boundaries, action, and verification constrain the draft. Reconcile the fields after drafting; contradictions such as a beginner audience paired with undefined expert terms indicate unfinished design rather than harmless template variance.

| artifact_field_name | artifact_completion_rule | evidence_source_hint | worked_context_selection_example |
| --- | --- | --- | --- |
| `audience_and_prerequisites` | Name one primary reader, what they already know, and vocabulary they do not need to know yet. | User request plus representative-reader evidence. | New contributor who understands files and tests but not context engineering or token budgets. |
| `user_goal_statement` | State the concrete decision or action the explanation must enable, not merely the topic to cover. | Local corpus hierarchy plus task findings. | Select useful repository evidence for a small code review and justify exclusions. |
| `consequence_and_reuse` | Describe what a wrong model could cause and whether the artifact is ephemeral, repeated, or durable. | Task context, downstream inventory, and owner judgment. | Wrong selection can omit a relevant test or flood the review with unrelated files; this onboarding note will be reused. |
| `governing_claim` | Give one plain-language claim that preserves the source's causal direction. | Complete subject-source read and claim map. | An agent has finite attention, so deliberate relevance-based context selection can make its next decision more grounded. |
| `causal_steps` | List the smallest sequence that explains why the claim follows. | Source passages plus explicitly labeled synthesis. | Identify the task; find directly relevant code and tests; add dependency context when evidence calls for it; exclude unrelated material; verify the decision. |
| `exact_terms_to_restore` | Define technical terms once after the simple model and retain distinctions needed for action. | Method guardrails and subject vocabulary. | Context window, relevance signal, source boundary, direct dependency, and blast radius. |
| `bounded_analogy` | State what the analogy maps, what it does not map, and when to abandon it. | Teaching design reviewed against the mechanism. | A backpack introduces finite capacity and selection. It does not model attention quality exactly, and a file that fits may still distract. |
| `concrete_positive_fixture` | Show the rule applied to a realistic case with inputs and a visible decision. | Local workflow and representative task. | For a changed parser function, load the function, direct callers, affected tests, and error path before a large unrelated architecture history. |
| `counterexample_or_limit` | Show a near case where the shortcut fails or a different artifact takes precedence. | Source boundaries, anti-pattern registry, and tradeoff guide. | A security review may require broader threat and policy evidence even when it is not a direct caller; relevance is consequence-aware, not proximity-only. |
| `decision_boundary_rule` | Define when to use this reference, when to adapt it, and when to route away. | Decision tradeoff guide and artifact routing matrix. | Use it to teach evidence selection; link an exact token counter or mandated review checklist when numerical or contractual completeness governs. |
| `next_action_and_stop` | Give the first action, expansion trigger, and observable stop condition. | User journey and operational fixture. | Start with task-local code and tests, widen on identified dependencies or uncertainty, and stop when the review conclusion is source-supported and its remaining uncertainty is named. |
| `evidence_status` | Attribute source facts, source-reported outcomes, external observations, and author inference separately. | Source evidence mapping table. | The finite-context model comes from the local subject source; any performance percentage remains source-reported unless measured on this repository. |
| `verification_gate_rule` | Define independent checks for source fidelity, reader comprehension, new-case transfer, and file policy. | Verification gate command set. | Reviewer maps claims and analogy boundaries; new contributor selects evidence for an unseen change; focused verifier confirms file invariants. |
| `confidence_and_unknowns` | State what is established, what is contextual judgment, and what evidence would change the guidance. | Evidence boundary notes and observed verification. | The local teaching rule is explicit; optimal context selection varies by task, consequence, model, and available graph evidence. |
| `owner_and_refresh_trigger` | Name who corrects durable use and which source, audience, workflow, or failed fixture reopens review. | Corpus hierarchy and downstream dependency record. | The reference maintainer reviews when either mapped source changes, onboarding transfer fails repeatedly, or review tooling changes. |

**Completion mode:** For a low-risk conversational clarification, use a light form containing audience, goal, governing claim, one boundary, next action, and an immediate teach-back question. Do not claim that this supports broad reuse. For onboarding, prompts, training material, or consequential decisions, complete every applicable durable field, record sources, and retain verification evidence. An optional field may be marked not applicable only with a reason tied to the artifact's purpose; generic filler is not completion.

**Artifact boundary:** This brief is the canonical decision model for the explanation, not a substitute for the underlying source, an executable specification, a runbook, or a benchmark. Derived prose, slides, or prompts may change delivery but must preserve the brief's governing claim, evidence status, decision boundary, and gate. If an exact artifact governs action, link it and state its precedence.

**Contrastive quality check:** "Teach a new contributor to choose context for review" is a usable goal; "explain context" is not discriminating enough. "Use relevant context" is a circular rule; the worked causal steps and fixtures make relevance observable. A backpack analogy with no distracting-file counterexample is borderline because it teaches capacity but not selective attention. The counterexample is not decoration: it prevents the template from being copied as a generic story.

Release the artifact only when a reviewer can trace every material field, the teaching arc has no internal contradiction, and a representative reader can perform the unseen decision rather than merely repeat the wording. Keep role responsibilities visible even when one person serves as subject expert, writer, reviewer, and maintainer. This allows missing evidence to be identified and lets larger teams parallelize extraction, teaching design, and verification against one shared contract.

## Worked Example Set

Use each worked example as both teaching material and a conceptual regression fixture. Record the audience, source claim, teaching move, boundary, next action, verification method, and expected failure signal. The reader-facing paragraph may stay natural; the annotation makes quality comparable without forcing every explanation into the same voice.

**Example 1, context selection for a new developer**

- **Audience and decision:** A developer who understands files and tests must choose what evidence to give an agent for reviewing a changed parser function.
- **Source model:** Context is finite, and relevance-based selection is preferable to indiscriminate raw-file loading. The local source supplies the model; this artifact does not claim a universally optimal token budget.
- **Good explanation:** "Think of the context window as a workbench with limited usable space. Put the changed parser function, its direct callers, affected tests, and error path on the bench first. Add broader architecture only when a dependency or uncertainty requires it. The workbench analogy is about selection, not exact capacity: text can technically fit and still distract the review."
- **Boundary and action:** The developer starts with task-local evidence, widens on an identified dependency or consequence, and stops when the review conclusion can be justified and residual uncertainty is named. A security review may require broader policy and threat evidence than call proximity suggests.
- **Verification:** Give the reader an unseen change containing one relevant test, one indirect but consequential caller, a large unrelated design note, and a stale incident log. Pass requires selecting the relevant test and caller, excluding the unrelated material, and explaining the consequence-based expansion.
- **Bad contrast:** "Give the AI everything so it cannot forget." This ignores finite attention, provides no selection rule, and mistakes volume for coverage.
- **Borderline contrast:** "Only load direct callers and tests." It is operational but too rigid; it fails when an indirect dependency or safety policy changes the decision.

**Example 2, tests as an executable feedback contract**

- **Audience and decision:** A product partner asks why writing a test before implementation helps an agent without needing a detailed testing tutorial.
- **Source model:** Tests reduce ambiguity by making expected behavior inspectable and provide correction signals during implementation. They do not prove that every requirement or failure mode has been captured.
- **Good explanation:** "A test is a concrete question the implementation must answer. Writing it first turns 'filter the right entities' into an example with inputs and an expected result. The failing run confirms the behavior is not already present; the smallest passing change answers that question; refactoring improves the design while the behavior check stays green. The test is useful evidence, not an infallible answer key, because a missing edge case remains missing."
- **Boundary and action:** Start with one behavior and its meaningful failure, observe that failure, implement the smallest supported behavior, then improve structure while retaining the check. Link the actual test suite when exact behavior governs work.
- **Verification:** Ask the reader what a passing test does and does not establish, then present a test that covers normal input but omits an empty case. Pass requires identifying both the verified behavior and the uncovered risk.
- **Bad contrast:** "Tests stop the model from hallucinating and guarantee correct code." This replaces a feedback mechanism with an unsupported guarantee.
- **Borderline contrast:** "Tests are the model's answer key." The phrase may introduce expected outputs, but without test gaps and refactoring it teaches excessive confidence and an incomplete cycle.

**Example 3, the four-word naming recommendation and reported outcomes**

- **Audience and decision:** A maintainer wants to explain why descriptive naming may help agents search a codebase, and whether every function must literally contain four words.
- **Source model:** The supporting source advocates a four-part naming pattern and reports results such as lower average compile attempts in its originating project. Those numbers are source-reported evidence, not a universal measurement reproduced here.
- **Good explanation:** "A descriptive name works like a compact search query: action, scope, target, and qualifier give an agent more clues than `filter`. The source recommends names such as `filter_implementation_entities_only` and reports improvement in its project after adopting that convention. Treat four words as a local design heuristic to test against language idioms and readability, not as proof that every four-word name is good or every shorter name is bad."
- **Boundary and action:** Prefer semantic density and repository consistency. Keep established short idioms where extra words merely repeat type or module context. Measure search, review, compile, or correction outcomes locally before repeating the source's percentages as project results.
- **Verification:** Compare realistic names in their modules, ask reviewers to locate intended behavior, and inspect whether added words disambiguate rather than pad. Any performance claim needs a defined baseline, sample, workload, and measurement method.
- **Bad contrast:** "Exactly four words makes development 67% faster." It turns a source-specific association into a universal causal guarantee and ignores confounders.
- **Borderline contrast:** "Longer names always give an AI more context." More tokens can add noise, duplicate surrounding scope, or violate local idiom; semantic usefulness matters more than raw length.

**Example 4, mixed request requiring an artifact route**

- **Audience and decision:** An operator asks both why context offloading helps long-running agents and exactly how to recover a failed production run.
- **Good route:** Give a short model of moving durable state from transient context into inspected files, then hand off to the current recovery runbook for commands, preconditions, authority, and stop conditions. State that the runbook governs execution.
- **Bad route:** Replace recovery steps with a library or notebook analogy and leave the operator to infer commands.
- **Borderline route:** Provide accurate commands inside a friendly narrative but omit version, environment, or rollback precedence. The prose is accessible while the operational artifact remains unsafe.
- **Verification:** A reader should explain the concept and separately execute or simulate the runbook fixture under its documented preconditions. Success in one layer does not substitute for the other.

The original good-use principle remains: load the canonical local method source, inspect the subject evidence, preserve the evidence boundary, and define verification before treating the explanation as complete. Under this task's no-browse constraint, public URLs are unrefreshed pointers rather than confirmed current ecosystem evidence. The original bad-use warning also remains: a generic tutorial that ignores mapped local paths, source hierarchy, and cost of error is not repository-grounded. Where local evidence is thin or conflicting, a confidence warning alone is only a borderline repair; provide the bounded supported portion, identify the unresolved claim, and route to the evidence or authority that can settle it.

Refresh an example when its source, product detail, audience, or decision changes, or when readers pass by memorizing its wording but fail a structurally equivalent new case. A source change should rerun the claim mapping and transfer fixture. Keep the set small enough to maintain and broad enough to expose distinct failure classes: unsupported certainty, incomplete causality, unbounded analogy, and incorrect artifact routing.

## Outcome Metrics and Feedback Loops

The governing outcome remains: the next task uses the reference to make a better decision with less ambiguity. Make that observable through a stack of independent signals rather than one composite quality score. A score can hide whether the defect is source fidelity, reader comprehension, transfer, action, or maintenance.

| metric_layer | observable_signal | collection_method | interpretation_boundary | revision_response |
| --- | --- | --- | --- | --- |
| Production process | Required source paths were read, claims were mapped, and the focused file gate passed. | Working packet, source review record, and verifier output tied to the saved path. | This establishes process and structure, not that the explanation is true or understood. | Repair missing provenance or file invariants before broader evaluation. |
| Source fidelity | A source-aware reviewer can trace material claims, conditions, evidence status, and analogy mappings without finding a changed causal direction. | Claim sampling against complete local passages and explicit synthesis labels. | Reviewer agreement is bounded by source quality and expertise. | Correct the governing claim or boundary; rerun dependent examples and reader fixtures. |
| Immediate comprehension | A representative reader states the main idea and exact term in their own words without being coached toward the source sentence. | Short teach-back recorded with audience prerequisites. | Recall may reflect prior knowledge and does not establish application. | Repair terminology, causal order, or analogy correspondence according to the error. |
| New-case transfer | The reader applies the rule to an unseen but structurally related case and identifies a limit. | Rotating decision fixture with expected rationale and discriminating distractors. | One fixture supports only the tested decision class; repeated evidence is needed for broader claims. | Add or replace contrastive examples; revisit audience assumptions if errors cluster. |
| Action outcome | The next task chooses the intended files, tests, artifact route, or verification step and reaches its defined stop condition. | Task observation, review record, or resulting artifact inspection. | Implementation skill, tools, and task difficulty also affect the result, so do not infer sole causality. | Distinguish explanation error from workflow or implementation error before changing prose. |
| Confidence calibration | Reader confidence is proportionate to correctness and they can name what remains uncertain. | Ask for confidence and boundary before revealing the expected analysis. | Self-reported confidence is noisy but can expose confidently wrong models. | Prioritize correction of high-confidence misconceptions because they propagate readily. |
| Correction burden | Reviewers record how many substantive model, evidence, or routing corrections were needed and where they originated. | Qualitative defect log linked to explanation version. | Raw counts differ in severity and reviewer style; preserve categories and consequence. | Fix recurrent upstream causes and add a regression fixture for consequential escapes. |
| Maintenance health | Mapped sources, examples, commands, audience assumptions, and owners remain current. | Event-triggered audit plus an owner-selected periodic stale-evidence review. | A fresh timestamp does not prove semantic currency. | Refresh dependent sections selectively through the provenance map. |

Use two measurement modes. For an ephemeral low-consequence answer, check the consequential source claim, ask for immediate teach-back or a decision, and qualify reuse. For a durable onboarding artifact, reusable prompt, or high-consequence explanation, retain source review, an unseen transfer fixture, downstream action evidence where available, version identity, owner, and refresh triggers.

Define each fixture before interpreting improvement: name the reader prerequisites, decision, expected rationale, changed variable, distractors, observer, and explanation version. Rotate unseen cases so readers cannot pass by memorizing wording. Report observed counts and error categories honestly. A small convenience sample does not support a precise universal percentage, and a downstream success does not prove that the explanation alone caused it.

Guardrail metrics remain useful when labeled narrowly. Readability can reveal sentence complexity; length can reveal accidental truncation or bloat; satisfaction can reveal tone and perceived usefulness; command results can reveal encoded policy compliance; source-link counts can reveal missing provenance. None alone establishes conceptual fidelity or operational transfer. A longer document is not automatically more detailed in the useful sense, and a highly rated analogy can still teach the wrong mechanism.

A good record says: "The reader defined context selection accurately, excluded an unrelated design file, included an indirect caller after noticing its consequence, and named when a security policy would widen the search." A bad record says: "The revised section has more words and all commands passed." A borderline record says: "The reader rated the explanation highly but repeatedly selected only direct dependencies." That disagreement is actionable: tone succeeded while the decision rule remained too narrow.

Keep the original failure signal visible: if the reference remains a source map and never becomes an operating guide, readers will not reach a verified next action. Other failure signals include exact paraphrase without transfer, structurally green files with changed source meaning, rising confidence paired with wrong decisions, repeated corrections at the same stage, and owners unable to identify which source change affects which section.

Close the loop at the layer that owns the defect:

1. A source-trace failure returns to the local corpus map and claim extraction.
2. A causal or analogy failure returns to the teaching model and counterexample.
3. A terminology failure returns to progressive disclosure and definitions.
4. A transfer failure returns to the decision rule and contrastive fixture.
5. An action failure is triaged between explanation, tooling, procedure, and implementation skill.
6. A freshness failure follows the provenance dependency to affected claims and examples.

Re-run deterministic verification after every generated-reference edit. Revisit public sources when browsing is permitted and relevant APIs, documentation, or tooling releases change; during this no-browse evolution, record those URLs as unrefreshed pointers rather than current evidence. Also review on local source change, repeated reader failure, audience change, workflow change, or increased consequence. Owners may add a lightweight periodic stale-evidence audit because event triggers can be missed, but no unsupported universal calendar interval is prescribed.

Retire a metric that never changes a decision, duplicates stronger evidence, or rewards behavior unrelated to the outcome. Promote a new one after a consequential escape recurs or presents high propagation risk. The desired loop is not maximal measurement; it is enough independent evidence to locate defects and improve the source, explanation, fixture, tool, or workflow that actually owns them.

## Completeness Checklist

Use this checklist as an index to release evidence, not as proof by box-counting. A complete explanation may still be wrong, and a faithful explanation may still be unusable. Every consequential item needs an observable path, passage, fixture, result, owner, or reasoned exclusion; the source review and reader-transfer gates decide semantic adequacy.

**Reader and decision contract**

- The role scenario names one primary reader, their starting state, the decision or action they need, the consequence of error, and the trigger for AI-native explanation patterns.
- Prerequisites are explicit enough that a reviewer can tell whether unexplained vocabulary is acceptable.
- The artifact route is named: explanation, companion overview, or a different authoritative format. Mixed outputs state which artifact governs exact action.
- The next action, expansion trigger, and stop condition are observable rather than summarized as "understand the concept."
- Evidence response: point to the completed explanation brief and user-journey fixture. "Audience covered" without a named reader is a failure.

**Source and evidence contract**

- The local corpus hierarchy identifies canonical and supporting sources or gives a bounded confidence warning when required evidence is absent.
- Every mapped local source has been read completely; heading signals were used for orientation rather than isolated quotation.
- Material causal, quantitative, historical, normative, and action-bearing claims have source or synthesis status.
- Source-reported outcomes remain attributed unless target-project measurement independently supports a broader claim.
- External URLs are labeled by actual inspection status. During no-browse work they remain unrefreshed pointers, not current corroboration.
- Conflicts, missing authority, and stale assumptions are exposed and routed rather than blended into confident prose.
- Evidence response: point to the source map, claim mapping, and relevant confidence note. A list of paths without claim relationships is incomplete.

**Teaching contract**

- The governing idea appears before supporting detail, and its causal direction matches the source.
- Plain language precedes exact terminology; important technical distinctions are defined once rather than deleted.
- Each major concept uses no more analogy than the reader needs, and every analogy states what maps, what does not, and where it stops.
- At least one concrete positive example demonstrates the intended decision with realistic inputs.
- At least one counterexample or near-boundary case prevents the reader from overgeneralizing the shortcut.
- The explanation uses progressive layers so deferred exact detail remains findable without crowding the first mental model.
- Tone respects the reader's intelligence and avoids hype, childish framing, jargon substitution, and unsupported certainty.
- Evidence response: point to the teaching arc and analogy mapping. An implied limitation is a needs-review state until a reader can state it.

**Decision and tradeoff contract**

- The decision guide includes Adopt when, Adapt when, Pause or route when, and Cost of being wrong.
- The chosen option states the source conditions, audience conditions, consequence, rejected alternative, and reversal trigger.
- Simplicity versus fidelity, analogy versus mechanism, breadth versus cognitive load, and speed versus validation have been resolved for the named task rather than ignored.
- The explanation does not silently replace an executable specification, benchmark, policy, runbook, or expert reference.
- Evidence response: point to the tradeoff record and linked authority. An unexplained route is a failure even if the prose is clear.

**Artifact and example contract**

- The theme-specific artifact is concrete enough to review without rereading every mapped source, while retaining links that permit source reconstruction.
- Required fields contain discriminating content; optional exclusions state why they do not affect the artifact's purpose.
- Worked examples cover good, bad, and borderline usage and name the specific quality dimension each changes.
- At least one unseen transfer fixture differs in surface details so memorized wording cannot pass.
- Product-specific details are separable from the durable mechanism and have refresh triggers.
- Evidence response: point to the completed brief and worked-example set. Generic template language is not completion.

**Verification and outcome contract**

- The saved packet section and matching reference section passed their immediate shape, expansion, heading, and marker checks.
- The complete file passes the focused verifier with exact expected counts and exact-text field uniqueness.
- A source-aware reviewer checked meaning, evidence status, and analogy boundaries rather than only formatting.
- A representative reader can teach back the idea, apply it to a changed case, identify a limit, and reach the intended next action.
- The metrics section names a leading indicator, an intermediate transfer signal, a downstream outcome, a failure signal, and interpretation boundaries.
- Verification evidence identifies the tested path or version and does not overgeneralize from a single reader or task.
- Evidence response: cite verifier output and reader fixture. "Looks clear" is a failure; a structural pass with failed transfer remains incomplete.

**Routing and maintenance contract**

- The adjacent routing section points to a more suitable artifact when this reference is not the right fit and explains the handoff trigger.
- Durable use has an owner, downstream dependency awareness, and event-based refresh triggers for sources, examples, commands, audience, or workflow.
- Recurrent defects route back to the owning source, teaching model, fixture, tool, or operational artifact.
- The complete evolved section and complete evolved file have been reread for coherence, duplication, unsupported precision, and accidental contradiction.
- The completion record states unresolved judgment and the assumptions under which release remains acceptable.
- Evidence response: point to the progress journal and maintenance note. Ownerless repeated reuse is a release risk.

For an ephemeral, low-consequence explanation, use a reduced set: named reader and decision; consequential claim source; one bounded model; next action and limit; immediate teach-back or decision check; and qualified reuse. Use the full set for generated references, onboarding, reusable prompts, broad distribution, or consequential decisions. Add domain-specific gates through the governing authority for security, legal, medical, financial, incident, or similarly high-consequence content; this checklist does not supersede them.

A good completion response says, "The new-developer fixture passed the unseen context-selection case; the source reviewer confirmed the reported metric remains attributed; focused counts passed at the saved path; the runbook is linked for exact release action." A bad response says only "all sections covered." A legitimate needs-review response says, "The analogy boundary is present, but two representative readers inferred different expansion rules"; keep the release decision open and repair or narrow the audience.

Reopen affected checklist categories when a dependent source, audience, example, command, artifact route, owner, or workflow changes. Use provenance to target revalidation, then reread the complete file for cross-section coherence. If the checklist never blocks, narrows, or changes a release, review whether its items still discriminate quality and retire low-signal duplication.

## Adjacent Reference Routing

Adjacent reference guidance: use the language, workflow, agent, documentation, or evidence reference that owns the reader's next authoritative decision when the theme becomes concrete. "Nearest" means scope and verification fit, not filename similarity. Keep this explanation as an orientation layer when useful, but do not let it retain authority over exact work that another artifact defines.

Route through four steps:

1. State the unresolved decision in one sentence and the consequence of getting it wrong.
2. Identify the capability that governs that decision: implementation, testing, prompt construction, state persistence, current documentation, evidence adjudication, or release operation.
3. Preflight the destination path, stated purpose, authority, and verification gate before handing off.
4. Carry the reader and evidence context forward, then define what result returns control or completes the task.

| route_trigger | adjacent_capability_and_current_path_example | handoff_payload_and_precedence | return_or_completion_condition |
| --- | --- | --- | --- |
| The reader understands AI-native prompting conceptually and now needs to construct or evaluate a prompt. | Prompt-engineering guidance, currently `idiomatic-ref-202607/ai_native_prompt_engineering-20260710.md`. | Carry audience, desired decision, local sources, claim boundaries, and failure fixture. The prompt reference governs prompt structure; this reference governs accessible explanation of why choices matter. | The prompt has an inspectable contract and gate, or an unresolved prompt-specific question is returned. |
| The task becomes creation of an agent or its context instructions. | Agent design references, currently `idiomatic-ref-202607/agent_creation_prompt_patterns-20260710.md` and `idiomatic-ref-202607/agent_context_instruction_patterns-20260710.md`. | Carry the user's agent goal, trigger conditions, constraints, evidence state, and explanation assumptions. The agent reference governs the actual definition. | The agent artifact is reviewable and its behavior can be tested; explanation resumes only for stakeholder orientation. |
| The concept becomes concrete test-first implementation or resumable testing work. | Testing and progress references, currently `idiomatic-ref-202607/tdd_cycle_skill_patterns-20260710.md`, `idiomatic-ref-202607/tdd_context_retainer_skills-20260710.md`, and `idiomatic-ref-202607/tdd_progress_journal_schema-20260710.md`. | Carry the behavior contract, current test state, source-specific caveats, and expected evidence. The workflow reference governs phase order and records. | The requested behavior has current test evidence and a nonempty next step or completion record. |
| The reader needs to preserve or recover long-running context rather than merely understand offloading. | Context checkpoint guidance, currently `idiomatic-ref-202607/chat_checkpoint_context_patterns-20260710.md` or the TDD context references above. | Carry the objective, settled decisions, exact paths, current evidence, open uncertainty, and ownership boundary. The persistence artifact governs resume state. | A fresh agent can resume without reconstructing hidden assumptions or touching unowned work. |
| A claim depends on current OpenAI API or product behavior. | Current documentation workflow, currently `idiomatic-ref-202607/openai_api_documentation_patterns-20260710.md`. | Carry the exact fact to verify and mark static local prose as insufficient for freshness. Current official documentation takes precedence over an old teaching example. | The fact is supported by current authoritative evidence, or remains explicitly unresolved under a no-browse constraint. |
| Sources disagree and the task requires evidence-based convergence rather than a simplified synthesis. | Evidence debate guidance, currently `idiomatic-ref-202607/agent_debate_evidence_patterns-20260710.md`. | Carry each claim, source, condition, consequence, and unresolved disagreement without averaging positions. The debate record governs convergence status. | The dispute is resolved with evidence, narrowed to a bounded uncertainty, or escalated to an owner. |
| The task moves from explaining worktree or release concepts to executing branch completion. | Branch-finish workflow, currently `idiomatic-ref-202607/branch_finish_worktree_patterns-20260710.md`. | Carry repository state, test evidence, user intent, unowned changes, and prohibited operations. The operational workflow governs commands and stop conditions. | The branch outcome is verified or a concrete blocker and safe next step are recorded. |
| The output becomes a generated image or specialized image prompt rather than prose explanation. | Image-prompt guidance, currently `idiomatic-ref-202607/image_generation_prompt_patterns-20260710.md`. | Carry subject, audience, visual purpose, factual boundaries, and inspection criteria. The image workflow governs generation and visual verification. | The produced visual communicates the intended model without introducing unsupported visual claims. |

These paths are current local examples observed by filename, not proof that each destination is complete or canonical for every task. Validate enough of the destination's scope to establish fit, then load its details on demand. If no adequate destination exists, preserve the bounded explanation, name the missing authority, and record the corpus gap. Do not select a plausible file merely to avoid admitting that the route is unresolved.

A handoff payload should contain the primary reader, starting state, unresolved decision, consequence, sources already read, settled claims, evidence labels, open question, chosen destination, and expected gate. Keep it compact by carrying decisions and evidence rather than repeating the full explanation. This is a typed boundary in documentation form: missing authority, changed confidence, and ambiguous ownership should be visible to the receiving artifact.

Good routing explains test-first feedback briefly, then sends exact phase behavior and evidence recording to the TDD workflow with the behavior contract intact. Bad routing sends a current API-freshness question to a static analogy because both mention AI. Borderline routing links a prompt reference but drops the source-specific status of a performance number; the topic survives while the epistemic boundary does not.

Avoid premature, delayed, circular, and dead-end routing. Premature splitting makes readers traverse several files for one simple concept. Delayed routing lets an analogy govern commands or contracts. Circular routing passes responsibility without resolving the decision. A dead end names a destination with no suitable gate or owner. Split when the adjacent artifact has a distinct source of truth or verification responsibility; otherwise embed the small necessary detail and preserve one authority.

Verify a route by checking destination existence, scope fit, authority, payload preservation, destination gate, and closure of the original open decision. A return condition keeps the handoff from becoming abandonment. Track repeated routes and unresolved gaps lightly; if the corpus grows, those records can reveal duplicate authorities, high-traffic references, cycles, and missing bridges. The goal is the shortest maintainable path to a verified decision, not the largest cross-link network.

## Workload Model

`combined_evidence_inference_note`: Treat AI-native explanation patterns as a documentation operating reference, not as a prose summary. Size work around the verified reader decision and its evidence relationships. File count and word count are secondary pressure signals; they do not measure conceptual complexity directly.

| workload_dimension_name | workload_unit_and_seed_boundary | pressure_signal | default_response | verification_pressure_point |
| --- | --- | --- | --- | --- |
| `primary_usage_surface` | Reference selection, writing, roadmap, or explanation work where the output should improve one next human or agent decision. | The topic is broad but the next decision cannot be stated, or the requested output mixes explanation with exact operation. | Frame a provisional decision, then route exact authorities before expanding prose. | Verify that the reference changes the next implementation, review, or routing action. |
| `audience_pressure_model` | One primary audience with stated shared prerequisites is the default unit. | Beginner, expert, operator, and auditor need different depth, authority, or actions. | Choose one primary layer and create explicit companion routes rather than averaging every audience. | Each audience can find its action without traversing mostly irrelevant depth. |
| `decision_pressure_model` | One verified decision is the preferred decomposition unit. Closely related decisions may stay together when they share prerequisites, governing claim, sources, and fixture. | Several decisions require different evidence, authorities, stop conditions, or costs of error. | Split by decision and retain a governing overview with typed handoffs. | Every child artifact has one observable completion condition and no duplicated authority. |
| `bounded_capacity_model` | The seed proposes one audience, one decision, up to 12 source documents, and one verification checklist per reference use. Treat 12 as a reassessment trigger, not a measured universal limit. | The source count crosses the trigger, or fewer sources contain substantial conflict, density, or uncertainty. | Inspect effective claim contributions and conflicts; narrow, batch, or continue based on semantic pressure. | Record why the workload proceeded or split and compare the result with correction effort. |
| `source_pressure_model` | Local heading signals include `Explain AI Native ELI5`, `Goal`, `Default Reader`, writing rules and workflow guidance, `AI-Native Cheat Sheet`, `AI Native Engineering ELI5`, `Big Idea`, and `The Easy Mental Model`. | Sources duplicate one another, disagree, carry different evidence status, or change at different rates. | Read complete relevant sources, deduplicate by claim contribution, expose conflict, and map dependencies. | Compare guidance with canonical local sources before using external examples or author synthesis. |
| `claim_pressure_model` | Count distinct causal, quantitative, normative, and action-bearing claims plus their conditions, not sentences. | One explanation needs many caveats, several evidence labels, or incompatible analogies. | Narrow the decision, layer detail, or create a claim map and companion evidence artifact. | A reviewer can reconstruct every material claim without reading unrelated source material. |
| `artifact_pressure_model` | Required artifact is a worked AI-native explanation example with user goal, decision point, failure mode, and verification gate; durable use adds the complete explanation brief. | The task also needs a specification, runbook, benchmark, prompt, or visual with separate authority. | Choreograph artifacts and state precedence rather than stretching one explainer across all purposes. | Require the artifact and handoff gates before claiming operational usability. |
| `verification_pressure_model` | At least one fidelity check and one transfer check per consequential explanation; deterministic file checks are additional. | Consequence, propagation, audience diversity, or source conflict rises. | Add expert review, multiple fixtures, or downstream action observation proportionately. | Verification layers provide independent evidence and their limits are recorded. |
| `lifecycle_pressure_model` | Track source dependencies, volatile examples, downstream copies, owners, and refresh triggers for durable work. | Many dependencies change independently or no owner can identify affected sections. | Reduce volatile detail, modularize examples, add ownership, or avoid promotion to a durable reference. | Source changes reopen only dependent claims first, followed by whole-file coherence review. |

Use a simple intake record before drafting: primary audience and prerequisites; one target decision; consequence of error; distinct material claims; local sources per claim; known conflicts; required artifact types; verification fixtures; reuse horizon; and owner. Use ordinal pressure such as low, moderate, or high with a reason. No formula here converts those fields into reliable hours or token limits.

Proceed as one workload when sources mostly agree, one audience can share a teaching layer, and one fixture family tests the action. For example, four aligned local passages may support one onboarding explanation about selecting review context. Split when beginner orientation, operator execution, and auditor evidence require separate authorities even if all discuss the same system. Preserve a short overview so the reader understands how the pieces relate.

Do not split mechanically at the twelfth source. Thirteen files that duplicate three stable claims may remain one manageable explanation after deduplication. Conversely, two authoritative sources with incompatible safety conditions may require conflict resolution before any explanation can proceed. The number is retained as the seed's coordination heuristic: crossing it prompts reassessment and a recorded decision, not automatic rejection.

Choose the decomposition boundary carefully. Splitting by arbitrary file batches or token slices can sever causal context and create duplicate authority. Split by a reader decision or source of truth, and carry audience, settled claims, evidence status, open question, and gate across the handoff. Progressive disclosure controls reader load; source batching controls author load. They solve different pressures and can be used together.

Alternative lenses have useful but bounded roles. A token budget constrains what enters an agent's current context but does not preserve claim relationships automatically. A claim graph preserves dependencies but costs more to build. A time box limits exploration but may stop before conflict is resolved. Audience layers manage depth but add synchronization. An artifact pipeline distributes work but requires ownership at interfaces. Select the lens that matches the binding resource while keeping the verified decision as the governing unit.

Calibrate the model after work. Record the planned pressure, actual source and fixture use, substantive corrections, elapsed review effort if already captured, and whether decomposition helped or caused duplication. Use these records for local trend learning, not universal productivity claims; reviewer experience and task difficulty confound direct comparison. Consistent underestimation indicates a missing dimension, while a threshold that never changes a decision may be unnecessary.

Creation size is not the whole workload. A narrow explanation with volatile product examples and many downstream copies can demand more maintenance than a broad explanation built from stable principles. Consider dependency edges, trigger frequency, correction recurrence, and ownership before promoting an answer to a durable reference. This lifecycle view prevents an easy first draft from creating an expensive correction surface later.

## Reliability Target

These are seed policy targets for release and reuse, not observed results from a completed reliability study. Enforce a target as a guardrail where applicable, then report actual evidence with its numerator, denominator, sample, audience, version, and uncertainty. Do not convert `18 of 20` into a universal reliability percentage.

| reliability_target_name | target_and_unit | target_status | evidence_collection_method | breach_response |
| --- | --- | --- | --- | --- |
| `source_boundary_preservation` | 100 percent of material recommendations keep local, external, and inference boundaries visible. The unit is a recommendation that could change belief, confidence, or action. | Seed release policy; achievement must be measured for the inspected artifact or sample. | Enumerate material recommendations, classify their origin, sample against complete source passages, and record ambiguous classifications. | Block durable reuse until boundaries are restored or the recommendation is removed. |
| `decision_accuracy_sample` | At least 18 of 20 sampled uses route to the correct adopt, adapt, pause-or-route, or adjacent-reference decision. The unit is one independently reviewable task decision. | Seed sampled target; no 20-case result is reported here. | Define task strata and rubric before sampling, include realistic borderline cases, record reviewer verdict and rationale, and preserve all misses. | Repair each miss, add it as a regression fixture, and rerun affected strata; any critical misroute blocks reuse even if the aggregate remains 18/20. |
| `unsupported_claim_rate` | Zero unsupported production, security, latency, or reliability claims in final guidance. The unit is a consequential claim, not a sentence. | Zero-tolerance seed policy, not an assertion that no future defect will occur. | Reject a claim without a supporting source row, explicit bounded inference, or a verification method appropriate to its consequence. | Remove or qualify the claim immediately, inventory maintained derivatives, and correct high-consequence copies. |
| `recovery_path_clarity` | Every avoid or failure case names a rollback, escalation, evidence request, or next-reference route with a completion condition. | Seed completeness policy. | Inspect failure-mode and adjacent-routing sections together, then simulate one route to ensure it resolves rather than circulates. | Add the missing route and owner; withhold operational use when failure would strand the reader. |
| `source_fidelity_gate` | Every sampled governing claim preserves causal direction, conditions, and epistemic status. | Added semantic release target derived from the local explanation method. | A source-aware reviewer maps claims and analogy components to complete local passages and records any changed implication. | Repair the mental model and rerun all dependent examples and transfer fixtures. |
| `reader_transfer_gate` | The named reader applies the rule correctly to at least one unseen representative case and identifies a boundary before the artifact is promoted for reuse. | Added bounded acceptance target; one case does not establish universal accessibility. | Record prerequisites, fixture variation, chosen action, rationale, confidence, and limit without coaching toward exact wording. | Narrow the audience or claim, repair examples or rules, and retest with a fresh case. |

For a new reference without 20 live uses, bootstrap with pre-release fixtures covering ordinary, boundary, and high-consequence routes. Report those as fixture results. As real tasks accumulate, record the observed denominator rather than waiting to publish a rounded rate. Synthetic fixtures test policy conformance; live samples test ecological fit. They answer different questions and should not be pooled without explanation.

Before measuring decision accuracy, define the target population, explanation version, audience groups, task strata, sampling method, correct-route rubric, severity levels, reviewer independence, and disagreement process. Repeated judgments by the same user are correlated; twenty decisions are not necessarily twenty independent users or contexts. Raw numerator and denominator come first. Statistical intervals are useful only if the sampling design makes them meaningful.

Use severity as an override rather than hiding every miss inside an aggregate. A routine ambiguity that causes a harmless extra source read is not equivalent to routing an operator away from the governing recovery runbook or repeating an unsupported security claim. Define a critical defect as one that changes a consequential action, authority boundary, or confidence in a way that can propagate. Reviewer judgment remains involved, so retain the rationale and calibrate on examples.

A good report says: "On the tested saved reference version, 18 of 20 stratified routing fixtures matched the adjudicated route; the misses were one audience mismatch and one delayed specification handoff; both were repaired and retained as regression cases. No critical unsupported claim was found in the inspected material claims." A bad report says: "The reference is 90% reliable." A borderline report meets 18/20 but includes one severe operational misroute; the aggregate target does not authorize release until that outlier is corrected.

Anti-gaming controls matter. Do not choose only obvious tasks, change the denominator after seeing failures, count duplicate cases as independent coverage, coach readers toward the expected answer, or redefine "recommendation" to exclude inconvenient prose. Report reviewer disagreement. Ambiguous classification may indicate that the guidance itself is not stable enough to measure.

Keep target, observation, and inference separate. "The policy requires zero unsupported high-consequence claims" is a firm rule. "The reviewed version contained none in the sampled claims" is a bounded observation. "Future readers will never encounter one" would be unsupported. Policy strictness can be high even when occurrence frequency is unknown.

Reliability extends into maintained derivatives. An accurate source explanation can lose caveats when copied into a prompt, slide, or onboarding summary. Inventory durable high-consequence derivatives, carry governing claim and evidence status as part of their contract, and sample reuse when propagation matters. If a critical model is withdrawn, name affected copies and the corrected route rather than silently fixing only the source file.

## Failure Mode Table

Use this table to route response, not merely name defects. For durable or consequential explanations, follow the failure lifecycle: detect the wrong belief or action; contain reuse; preserve a discriminating fixture; locate the owning layer; apply the smallest causal repair; rerun source, reader, and file gates; then inspect maintained derivatives and record residual risk. For a low-impact conversational defect, the same logic may be compressed into immediate correction and teach-back.

| failure_mode_name | likely_trigger_and_detection_signal | immediate_containment | causal_repair_and_owner | recovery_evidence |
| --- | --- | --- | --- | --- |
| `source_drift_hides_truth` | Local guidance, public documentation, API behavior, or tooling changes after the reference was written; a mapped claim no longer matches its authority. | Mark affected claims stale and stop unqualified reuse; under no-browse constraints, do not imply external freshness. | Source owner refreshes public evidence when permitted, reruns local corpus comparison, and updates dependent claims and examples through provenance links. | Current source status is recorded, claim mappings pass, affected fixtures are rerun, and unresolved drift remains visibly bounded. |
| `generic_advice_escapes_review` | An agent copies plausible best practices with no source-specific distinction, concrete fixture, or theme-specific gate. | Block promotion and identify which recommendations could change action. | Writer returns to the local hierarchy and explanation brief; reviewer rejects generic completion until each consequential recommendation has evidence and a relevant check. | A reviewer can name what is unique to this corpus, and the chosen gate tests the actual decision rather than formatting. |
| `decision_path_remains_implicit` | A reader understands the topic but cannot tell when to adopt, adapt, pause, avoid, or route. | Prevent action based solely on the explanation and expose the unresolved boundary. | Artifact owner adds decision variables, cost of error, reversal trigger, adjacent authority, and stop condition. | An unseen routing fixture reaches the adjudicated artifact with a bounded rationale. |
| `large_corpus_becomes_list` | Many paths are indexed but no governing claim, relationship, conflict, or ranked guidance emerges. | Stop adding sources and preserve the current inventory for analysis. | Evidence owner classifies canonical, supporting, legacy, duplicate, and conflicting roles at claim scope, then synthesizes around the reader decision. | The resulting model changes a concrete next action and every material claim can be reconstructed. |
| `wrong_but_cute_model_propagates` | Readers remember an analogy but infer a fictional mechanism or apply it beyond its limit. | Withdraw or flag the analogy in maintained copies and state the corrected mechanism directly. | Teaching owner remaps correspondence, adds a counterexample, or removes the analogy; source reviewer checks causal direction. | A fresh reader applies the rule correctly to a near-boundary case and identifies where the analogy stops. |
| `evidence_confidence_escalates` | A source-reported metric, author inference, or unrefreshed public pointer becomes phrased as universal fact. | Qualify or remove the claim and inventory high-consequence derivatives. | Evidence owner restores origin, scope, conditions, measurement status, and uncertainty; local measurement is added only if actually performed. | Sampled copies preserve the boundary, and reviewers can distinguish target, observation, and inference. |
| `audience_averaging_obscures_action` | One artifact alternates between beginner definitions, expert shorthand, operator commands, and auditor evidence without a primary reader. | Name the current audience and suspend claims of broad accessibility. | Product or documentation owner creates progressive layers or separate companion artifacts with precedence and handoffs. | Each named audience can find its own next action and limit without traversing mostly irrelevant material. |
| `teach_back_passes_transfer_fails` | Readers repeat the source or analogy accurately but choose incorrectly in a changed task. | Do not promote the explanation for operational reuse despite positive readability or satisfaction feedback. | Teaching owner repairs the decision rule and contrastive fixtures; reviewer checks whether prerequisites or coaching invalidated the initial test. | An unseen structurally equivalent case passes without relying on memorized wording. |
| `explanation_claims_wrong_authority` | A metaphor or overview is used in place of a specification, runbook, benchmark, security policy, or current documentation source. | Route exact action to the governing artifact and state its precedence. | Routing owner adds trigger, handoff payload, destination gate, and return condition; remove duplicate normative detail if it creates competing authority. | The destination resolves the original decision and a reviewer can identify which artifact governs execution. |
| `verification_theater_masks_semantics` | Commands pass and required labels exist, but claims, analogies, or reader actions remain wrong. | Mark the artifact structurally green but semantically unverified. | Reviewer adds source-aware and transfer gates that target the escaped defect rather than another presence check. | The original failure fixture and a changed variant pass; machine results retain their stated coverage limits. |
| `metric_optimization_replaces_outcome` | Writers optimize word count, readability, satisfaction, link count, or easy samples while decision quality stagnates. | Stop using the proxy as release evidence and preserve conflicting outcome observations. | Measurement owner restores independent fidelity and transfer signals, transparent denominators, and severity overrides. | Metric movement agrees with observed behavior, or the proxy is narrowed to its valid diagnostic role. |
| `stale_derivative_survives_source_fix` | The canonical explanation is corrected but prompts, slides, onboarding notes, or copied summaries retain the old model. | Flag known derivatives and prioritize those with high consequence or broad reuse. | Maintainer updates derivative contracts, ownership, and propagation inventory; obsolete copies are retired or redirected. | Sampled maintained derivatives carry the corrected claim and evidence status, with residual untracked copies acknowledged. |
| `recovery_route_becomes_dead_end` | A failure case points to a nonexistent, circular, unauthoritative, or unverifiable destination. | Keep the unresolved decision visible and do not imply recovery is complete. | Routing owner validates path, scope, owner, payload, gate, and completion condition or records a corpus gap. | A simulated handoff resolves or explicitly escalates the open decision without returning unchanged. |

Do not force every incident into one label. Record one primary causal mode and contributing factors when, for example, source drift combines with stale derivatives or audience averaging hides an authority error. Add a new category only when it changes detection, containment, ownership, or recovery. Otherwise retain the case as an example under an existing mechanism so the taxonomy remains useful.

Preserve enough evidence to reproduce consequential failures: explanation version, relevant source state, reader prerequisites, task fixture, observed belief or action, confidence, expected result, and downstream copies if known. When those details are unavailable, contain high-consequence reuse first and reconstruct only what is needed to classify the risk. Uncertain root cause should lead to a narrower claim and stronger monitoring, not a random rewrite.

A good failure record says: "After the workbench analogy, a new contributor loaded every file that fit. Reuse was paused; review found that capacity was explained but relevance was not. The rule and distracting-file counterexample were added, and a fresh fixture with an indirect consequential caller passed." A bad record says, "Wording simplified." A borderline record fixes this file but leaves a reusable agent prompt with the old rule; local recovery is incomplete until derivative risk is handled or explicitly bounded.

Close a failure only when the specific wrong belief or action no longer appears in a changed representative fixture, source and evidence status are correct, the focused file policy passes, and any required route completes. Absence of recurrence in one small sample is bounded evidence, so severe failures retain monitoring. Recovery confidence follows fixture strength and representativeness, not the number of edited paragraphs.

Use recurrence to look upstream. Repeated source drift may indicate missing provenance; repeated route errors may reveal overlapping authorities; repeated transfer failures may expose a mistaken audience model; repeated stale copies may indicate ownerless distribution. Apply local containment even when systemic work belongs elsewhere, then escalate evidence to that owner. The fastest wording repair is not the right system repair when the same cause will regenerate the defect.

## Retry Backpressure Guidance

Retry only after classifying the failed verification signal. A valid retry changes an input, hypothesis, teaching mechanism, source state, or verifier that could plausibly repair the failure. Repeatedly asking for more detail from unchanged evidence is another generation attempt, not a causal retry strategy.

| classified_failure_state | bounded_intervention | gate_to_rerun | stop_or_escalation_condition |
| --- | --- | --- | --- |
| Transient command or file-read failure | Preserve the command, path, and output; confirm saved state; retry the same idempotent read or check once the transient condition clears. | The smallest deterministic gate affected by the failure. | Escalate when the condition repeats or state may have changed; do not assume a missing output means the edit failed or succeeded. |
| Stale external evidence | When browsing is permitted, use one bounded freshness attempt against the authoritative source and record its date and scope. Under a no-browse constraint, mark the claim unrefreshed and narrow it. | Claim provenance, changed-source dependency fixtures, and any current-fact route. | After one unsuccessful refresh, escalate to a human, request access, or route to a narrower local source-specific reference. |
| Missing local context | Identify the exact decision blocked, read the smallest authoritative source or task state that supplies it, and update the claim map. | Source coverage and the dependent explanation or routing fixture. | Ask for the missing artifact or publish only the bounded portion when no authorized source exists. |
| True source contradiction | Preserve both claims, conditions, and authorities; stop synthesis of the affected recommendation; route for evidence adjudication. | Conflict resolution record and every dependent claim. | Resume only when ownership resolves the conflict or the artifact explicitly narrows around it. |
| Analogy or causal-model failure | Preserve the failed reader fixture; repair the earliest wrong correspondence, add a counterexample, or remove the analogy. | Source fidelity plus a fresh unseen transfer case. | Narrow the audience or escalate teaching design when the same consequential misconception recurs without new evidence for another intervention. |
| Terminology comprehension failure | Define the necessary term after plain language, remove redundant synonyms, and check prerequisite assumptions. | Unprompted teach-back for the same concept with different wording. | Split the layer or revise the audience contract if added definitions overload the primary decision. |
| Artifact-routing failure | Carry the original reader, evidence labels, open decision, consequence, and expected gate to the authority that owns exact action. | Destination acceptance and return condition. | Record a corpus gap rather than circulating among references when no adequate authority exists. |
| Structural verifier failure | Localize the assertion to the owned path, preserve unrelated shared-work failures, and make the smallest file repair. | Saved-section sanity followed by the focused file verifier. | Stop broad edits when failure ownership is unclear; do not alter another lane to make a global result green. |
| Downstream action failure with correct teach-back | Diagnose whether the defect belongs to the explanation, fixture, tool, procedure, or implementation skill before editing prose. | A discriminating task fixture targeted at the proposed cause. | Escalate when available evidence cannot separate causes; narrow any outcome claim meanwhile. |

Apply backpressure to dependencies, not indiscriminately to all work. Stop new generation or implementation that depends on red source coverage, critique coverage, claim fidelity, authority routing, or verification gates. Independent work may continue when its sources, ownership, and gates do not rely on the failed premise and that independence is recorded. For high-consequence uncertainty, contain broadly until dependency scope is understood.

Backpressure is released by evidence that repairs or removes the failed dependency. Elapsed time, repeated attempts, a deadline, or an unrelated green command does not change the state. Provide verified partial service when useful: explain established material, label the withheld claim, and name the evidence or authority needed for the rest. Partial output becomes unsafe when its boundary is subtle or the omitted fact controls the reader's action.

For long-running agent workflows, checkpoint after each batch and reread the current specification and saved state before a broad rewrite or any operation that changes repository history, remote state, or other owners' work. The checkpoint records objective, exact owned paths, complete sections, current test evidence, unresolved failures, and nonempty next steps. It prevents a retry from using stale in-memory assumptions after another agent or user changes the workspace.

For distributed execution, assign one owner per generated file or theme batch. Parallelize only independent evidence questions, give each worker exclusive paths, and define a convergence record. At integration, verify exact paths, original heading order, evidence boundaries, packet counts, and semantic gates. Do not use parallel retries on the same prose unless one owner explicitly reconciles variants; otherwise, competing plausible edits can erase valid work and obscure which intervention succeeded.

A minimal retry record contains the failure class, affected decision, preserved fixture, evidence state, changed input or hypothesis, owned paths, targeted gate, result, residual risk, and next state. Record decision-bearing facts rather than every draft. A good trace says, "The reader treated the workbench as a fill-to-capacity rule; the analogy mapping and distracting-file counterexample changed; a fresh case passed." A bad trace says, "Generated a longer version." A borderline trace refreshes an external source but does not reopen the claim map and copied examples; the intervention occurred, but dependent state remains stale.

The seed's one bounded external-refresh retry is a coordination policy, not a universal limit for all semantic iteration. More teaching iterations are justified when each supplies new reader or source evidence that distinguishes the next intervention. Repeated same-mode consequential failure without new evidence should escalate or narrow rather than consume an open-ended retry loop. If owners need a time or cost limit, set it for the task and record what evidence remains unresolved; no universal budget is asserted here.

Feed meaningful retry patterns back into the system. Repeated missing-context retries suggest weak intake or source maps. Repeated analogy repair suggests the teaching model is unstable. Repeated routing retries suggest overlapping or absent authorities. Repeated structural failures suggest poor section-save tooling. Preserve recurrent or high-consequence traces, improve the owning layer, and retire retries that merely mask the same upstream defect.

## Observability Checklist

Observability should let a maintainer reconstruct why an explanation was released, narrowed, routed, retried, refreshed, or withdrawn. Collect the smallest decision-bearing evidence that supports that reconstruction. Raw transcript accumulation is not the default: it increases privacy and review burden and can still hide the governing claim.

| event_or_record | minimum_fields | decision_supported | privacy_and_size_boundary |
| --- | --- | --- | --- |
| `explanation_intake` | Artifact identity, primary audience and prerequisites, target decision, consequence, reuse horizon, owner. | Selects workload mode and artifact route. | Do not retain unrelated personal background; use role-relevant prerequisites. |
| `source_selection` | Exact local paths loaded, source identity when handoff reproducibility matters, paths intentionally skipped with reason, public-source inspection status. | Establishes evidence scope and makes omissions interpretable. | Record claim relevance rather than copying complete sources into the journal. |
| `claim_decision` | Governing claim, origin label, conditions, confidence, transformation, and dependent section or example. | Supports fidelity review and targeted refresh. | Keep sensitive source passages in their authority; store a pointer and bounded summary. |
| `artifact_change` | Saved path, changed sections, previous and current explanation version or content identity, concise rationale. | Localizes regressions and prevents stale-state retries. | Prefer changed-section summaries over full conversation replay. |
| `verification_run` | Exact command or reviewer question, target path or artifact, current result, coverage meaning, failure ownership, and timestamp when freshness matters. | Supports release, failure triage, and resume. | Summarize command output while retaining decisive counts and errors. |
| `reader_fixture` | Audience prerequisites, unseen case, chosen action, rationale, confidence, identified limit, coaching or prior exposure. | Distinguishes recall, comprehension, transfer, and calibration. | Redact identity; retain only task-relevant behavior and consented evidence. |
| `route_handoff` | Open decision, destination, payload, precedence, destination gate, completion or returned blocker. | Shows whether adjacent routing resolved the user's need. | Carry settled evidence rather than duplicating the entire origin artifact. |
| `retry_attempt` | Failure class, preserved fixture, changed input or hypothesis, owned paths, targeted gate, result, and next state. | Detects retry loops and validates backpressure release. | Journal the learning, not every generated variant. |
| `reliability_sample` | Explanation version, population and sample method, numerator, denominator, strata, misses, severity, reviewer disagreement. | Supports bounded reliability claims and regression selection. | Avoid reader profiling and do not publish universal rates from convenience samples. |
| `refresh_or_withdrawal` | Trigger, affected claims and derivatives, owner action, residual uncertainty, next trigger. | Maintains provenance and propagation reliability. | Inventory maintained high-consequence copies rather than attempting indiscriminate surveillance. |

Record which local sources were loaded and which were intentionally skipped. "Skipped" needs a reason such as duplicate claim, outside decision scope, known stale status, missing authority, or deferred layer. Absence of a source record is not evidence that no source was needed. Distinguish `not observed`, `not collected`, `not applicable`, and a measured zero; collapsing those states creates false certainty.

Record the exact verification command, reviewer question, or rendered artifact used as proof. Include the target and coverage meaning. "Focused verifier passed 26 reference headings, 260 questions, 1,560 fields, and exact uniqueness for this path" is useful. "Passed" alone cannot establish what was checked. Preserve failures owned by other shared-work paths rather than summarizing a global red result as a target-file defect.

When the reference affects runtime or workflow speed, record individual latency or reviewer-time observations with task definition, start and stop boundaries, environment, sample count, warm-up or cache state where relevant, and missing runs. Report p50, p95, or p99 only when repeated samples and a stated percentile method make those values meaningful. A single duration can be reported as one observation, not a distribution. Documentation review time is also confounded by reviewer experience and task complexity, so comparisons need matched or explicitly different conditions.

Capture reviewer decision, unresolved uncertainty, confidence, next refresh trigger, and owner. A release decision without residual risk makes later failures harder to interpret. A refresh trigger such as source hash change, failed transfer fixture, workflow update, or new audience is more actionable than "review later"; if a local policy requires calendar review, record that policy rather than inventing a universal interval here.

Record the leading indicator and failure signal from this file in the coverage manifest or progress journal when the reference drives real work. Preserve the actual next action and whether it changed, not only that the reference was consulted. Useful aggregate signals include recurrent misconception category, unresolved route count, source-skip reason, retry cause, correction origin, and stale dependency. They generate hypotheses about corpus architecture; task mix must be reviewed before inferring cause.

A compact good record looks like this:

```text
artifact: ai_native_explanation_patterns-20260710.md / Section 014
reader_decision: new developer selects evidence for parser review
sources: method skill + subject reference loaded; public pointers unrefreshed
change: bounded workbench analogy and added indirect-caller counterexample
gates: source review pass; unseen transfer fixture pass; focused file gate pass
uncertainty: one reader fixture does not establish broad audience reliability
next_trigger: mapped source change or repeated context-selection error
```

A bad record says only "all checks green." A borderline record stores a full transcript but cannot identify the explanation version, governing claim, or decision. Evidence too large to inspect reliably is functionally hidden. Link a bounded source passage, artifact snapshot, or failure fixture only when the compact summary cannot preserve causal evidence.

Audit observability itself. Sample records against saved artifacts, verifier results, source identity, reader fixtures, route closure, and current ownership. Ask a fresh reviewer to reconstruct one release or failure without hidden conversation context. Use independent review for critical events and proportionate spot checks for routine records. Track missing or unclassifiable events so the system reveals blind spots rather than silently treating absent data as success.

For a one-off low-consequence explanation, retain only the consequential claim check, immediate reader correction, and any unresolved boundary needed for the user. Durable references need the structured records above. Access, retention, and deletion must follow local policy; none is specified here, so do not invent a duration or store personal data indefinitely. Evidence should expire when its decision value ends unless a governing requirement says otherwise.

## Performance Verification Method

Performance means quality-preserving time to a correct next action, not raw reading speed. The seed target requires a reader to find the correct next action in 10 minutes or less during review sampling. Retain that as an uncalibrated local target: this section contains no completed measurement packet proving that the target is currently achieved or universally appropriate.

Define a run before starting the clock:

1. **Reader:** Record role, relevant prerequisites, prior exposure to this reference, and whether the run is individual, assisted, or agent-mediated.
2. **Fixture:** Provide a representative task with input size, source count, decision consequence, discriminating distractors, and one unseen variation. State the adjudicated action, acceptable alternatives, verification gate, and stop condition.
3. **Environment:** Record artifact version, permitted files and tools, cache or warm-up state where runtime applies, concurrent delays, and any assistance.
4. **Clock:** Start when the reader receives the task and reference. Record time to first proposed action, time to verified action, pauses, and excluded delays. Stop only when the action, rationale, gate, and boundary are stated.
5. **Quality guardrails:** Independently review source fidelity, correct route, new-case transfer, and uncertainty. A wrong or unsupported action fails regardless of speed.
6. **Record:** Preserve every valid run, including slow and failed cases, with the actual denominator and reasons for any exclusion defined before analysis.

| measurement | question_answered | required_context | important_blind_spot |
| --- | --- | --- | --- |
| Time to first correct action | How quickly can the reader identify a viable route? | Start event, first proposal, correctness rubric, assistance. | May ignore later verification or boundary errors. |
| Time to verified action | How long until action, gate, and stop condition are all correct? | Full fixture and stop definition. | Mixes reference usability with tool and workflow latency. |
| Search steps or unrelated files opened | Does the reference reduce navigation and ambiguity? | File access sequence and relevance rationale. | Fewer steps are not better if necessary evidence is skipped. |
| Substantive correction count | How much reviewer intervention is needed? | Error categories and severity. | Reviewer style and expertise vary. |
| Reader confidence calibration | Does confidence track correctness and limits? | Confidence captured before expected result is revealed. | Self-report is noisy and culturally variable. |
| Runtime latency | Does a tool-backed explanation workflow meet its operational target? | Input distribution, environment, repeated runs, warm-up, concurrency, and percentile method. | Does not establish conceptual quality. |
| Reviewer decision time | Does the documentation make the next decision easier to locate and justify? | Comparable tasks, reader prerequisites, clock boundaries, and artifact version. | Learning and task mix confound direct comparison. |
| Repeated-use trend | Does the mental model reduce later effort? | Same or comparable reader over multiple unseen tasks. | Practice and external learning contribute to improvement. |
| Downstream rework | Did a fast initial decision create delayed correction cost? | Review changes, failure records, and route history. | Attribution to the reference alone is rarely justified. |

The required measurement packet captures input size, source count, distinct claim or conflict count when available, tool-call count, wall-clock time, reader decision time, correction categories, action correctness, confidence, and artifact version. Record p50, p95, or p99 latency only where repeated runtime or workflow measurements and a stated percentile method make them meaningful. Do not calculate tail percentiles from a handful of documentation reviews and present them as stable performance.

The leading indicator remains: the next task uses the reference to make a better decision with less ambiguity. Operationalize it as a correct route and rationale on a representative unseen case, with fewer irrelevant searches or fewer substantive corrections when a suitable baseline exists. The failure signal remains: the reference is still a source map and never becomes an operating guide. A reader who can list files but cannot choose an action, gate, and stop condition has not passed.

The seed pass condition remains: the reference lets a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files. Add two quality requirements: the rationale preserves source boundaries, and the reader can identify a case where the action changes. The seed fail condition also remains: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit. A run also fails if it is fast but chooses the wrong authority, repeats unsupported evidence, or skips a consequential condition.

Illustrative interpretation, not measured results: a reader who reaches the correct route in eight minutes, preserves the source-specific metric caveat, and identifies the stop condition passes the seed target. A reader who reaches a wrong operational route in three minutes fails. A reader who takes twelve minutes because they detect a genuine source contradiction missed by the fixture does not simply prove the reference slow; the fixture and ten-minute target need review because reliability work was omitted from the expected path.

Use staged evidence language:

- A single timed run is an observation under named conditions.
- Repeated runs with one reader show a local learning trajectory, confounded by practice.
- Matched or within-reader comparison can suggest a difference when task order and prior exposure are addressed.
- A broader comparative claim needs a defined population, sampling, sufficient observations, stable fixtures, and analysis appropriate to the design.
- A causal claim that the reference produced the improvement requires stronger controls than this local method specifies.

Do not exclude slow runs, source-conflict discoveries, or tool failures after seeing results merely to improve the summary. Classify exclusions using predeclared validity rules and report them. Keep reviewer-time and agent tool latency separate where possible because their interventions differ: reorganize navigation for human search cost, optimize tooling for runtime delay, and repair evidence or teaching for decision error.

For repeated-use references, inspect cumulative correct work. A slower first encounter may establish an exact model that reduces later ambiguity; a seductive shortcut may win the first timing and create downstream rework. Track later unseen-case time and correction burden as bounded observations. Optimize the shortest first encounter only when that is the actual product requirement and all reliability guardrails remain satisfied.

## Scale Boundary Statement

AI-native explanation patterns stop being sufficient as the sole authority when the task spans independent systems with incompatible contracts, multiple ownership boundaries, unbounded source discovery, or production traffic without an explicit service objective. The pattern may remain a useful overview, but exact behavior must move to owned operational artifacts with their own gates.

| scale_dimension | stay_with_one_reference_when | boundary_signal | scaling_response | acceptance_evidence |
| --- | --- | --- | --- | --- |
| Reader reach | Readers share enough prerequisites, decision, consequence, and vocabulary for one progressive teaching arc. | Beginner, expert, operator, and auditor need incompatible depth or authority. | Keep one governing overview and create audience-specific layers or companions with precedence. | Each audience finds its next action and limit without crossing mostly irrelevant material. |
| Decision count | Decisions share one governing claim, source authority, and fixture family. | Separate decisions require different sources, owners, stop conditions, or costs of error. | Partition by verified decision and carry shared semantics through a compact contract. | Every child artifact has one observable completion condition and routes unresolved work correctly. |
| System count | The explanation describes one coherent system or a cross-system model without owning exact local behavior. | System APIs, failure handling, or change cadence cannot be governed by one owner. | Retain a map of contracts; route implementation and operation to each system authority. | Cross-system examples preserve interface assumptions and local owners verify their contracts. |
| Source graph | Evidence is bounded, deduplicated, reconcilable, and traceable to material claims. | Discovery is open-ended, contradictions remain unresolved, or a source list replaces ranked guidance. | Narrow by claim and dependency, classify source roles, and split research from explanation. | A reviewer reconstructs each material claim and sees all unresolved conflicts. |
| Artifact graph | One explanation and a small number of linked authorities have clear precedence. | Prompts, slides, runbooks, specifications, and copied summaries duplicate normative claims. | Establish one source of truth per decision, derivative contracts, and change-impact routing. | A source change identifies affected maintained derivatives and no competing authority remains hidden. |
| Agent concurrency | One owner edits each path and independent evidence tasks have explicit convergence. | Parallel agents touch the same reference, use stale state, or disagree silently on terminology. | Assign exclusive paths, save after each section, checkpoint batches, and appoint one semantic integration owner. | Exact headings, evidence boundaries, and shared terms survive integration; no unowned change is overwritten. |
| Workflow duration | The agent can retain current objective, evidence, risks, and saved state without drift. | Long execution loses earlier constraints, repeats completed work, or applies a broad rewrite from stale memory. | Treat context drift as a reliability failure; checkpoint, reread the specification and current files, and resume from the next incomplete unit. | A fresh agent can continue safely using the journal and saved artifacts alone. |
| Consequence and production traffic | Errors remain bounded and the explanation is not standing in for a live operational control. | Guidance influences production traffic, safety, security, legal obligations, or a service without explicit objectives and monitoring. | Route to the governing system design, runbook, policy, SLO, and incident process; keep explanation non-authoritative. | Owners provide current operational evidence and the overview states its authority limit. |
| Change rate | Core concepts are stable and volatile product details are modular. | Sources, tools, examples, and audience assumptions change independently faster than owners can refresh them. | Reduce volatile embedding, generate views from owned data where justified, or narrow distribution. | Refresh triggers and ownership keep high-consequence derivatives within policy. |

Keep a single reference when one owner can verify all consequential claims, readers share a viable first layer, and source relationships remain bounded. Use progressive disclosure before splitting solely because the document is long: reader load is a presentation problem, while authority and governance load are ownership problems. Treating both as "too many words" produces the wrong remedy.

Under distributed execution, split work by theme file or independent decision and preserve one verification owner per split. Do not let parallel agents rewrite the same reference without a merge checkpoint. Centralize only shared semantics: governing claim, evidence status, terminology, routes, and cross-artifact invariants. Leave examples and delivery details with their owners. This reduces coordination without making a central file responsible for every sentence.

Under long-running agent workflows, treat context drift as a reliability failure. Checkpoint the objective, exact owned paths, completed units, current verification evidence, open risks, and next steps. Reread the current specification and filesystem state before continuing after interruption. A fresh-agent resume test is practical evidence that hidden conversational assumptions are not carrying the workflow.

Under large-codebase scale, require dependency or source-graph narrowing before applying this reference. A source list without ranked canonical guidance is not enough. Start from the reader decision, identify directly supporting entities or sources, widen through consequential dependencies, and preserve conflicts. Graph tooling can help with selection, but graph proximity does not automatically equal relevance or authority.

Good scaling uses one cross-system overview to explain shared intent and interfaces, then routes exact API and recovery behavior to owned system references. Bad scaling copies every system's runbook into the overview, creating stale competing authority. A borderline design partitions files among owners but lets each define "verified" differently; file distribution occurred, while semantic ownership did not. Appoint an adjudication owner for unavoidable shared terms.

Choose the least complex structure that preserves authority, routing, and verification. A monolith favors coherence but concentrates ownership. Layered guides manage reader depth but add synchronization. Federated references preserve local authority but need discoverable interfaces. Generated views reduce duplication only when source relationships are stable and machine-readable. Expert facilitation handles ambiguity but does not scale availability or durable memory automatically.

Verify scale boundaries by sampling ownership interfaces, route closure, source dependencies, fresh-agent recovery, semantic integration, and production objectives where applicable. No universal team, source, traffic, or token threshold is established here. Escalate on observable authority mismatch, repeated gate failure, or correction cost, and collect local evidence before defining numeric capacity.

Finally, reduce explanation demand where the system itself creates recurring ambiguity. Clearer names, APIs, tests, source documentation, defaults, and tooling may make the correct path visible without another guide. This does not eliminate conceptual learning, but it prevents the explanation corpus from scaling as compensation for avoidable design confusion.

## Future Refresh Search Queries

No search was executed during this evolution because browsing was prohibited. The queries below are future retrieval plans, not evidence and not citations. Run them only after a concrete refresh trigger, record actual source status, and reconcile results with the local corpus before changing guidance.

| search_query_label_name | search_query_text_value | use_trigger_and_source_priority | acceptance_and_update_rule |
| --- | --- | --- | --- |
| `local_method_source_change` | `rg -n -e "Default Reader" -e "Writing Rules" -e "Workflow" -e "Guardrails" -e "Quality Check" agents-used-monthly-archive/codex-skills-202603/explain_ai_native_eli5` | Run when the mapped skill identity changes or teaching defects recur; the complete local file remains primary for this repository's explanation method. | Reopen audience, teaching arc, anti-pattern, checklist, and reader fixtures affected by changed rules; a text match only locates passages. |
| `local_subject_source_change` | `rg -n -e "Big Idea" -e "Mental Model" -e "TDD" -e "context" -e "naming" -e "agent" agents-used-monthly-archive/codex-skills-202603/explain_ai_native_eli5/references/ai_native_engineering_eli5.md` | Run when the subject source changes or a borrowed model is disputed; read complete surrounding sections. | Update only dependent claims, examples, evidence labels, and fixtures, then reread the complete evolved file for coherence. |
| `official_docs_query_phrase` | `AI agent context management official documentation filesystem shell CLI progressive disclosure` | Use when a current product or platform claim enters the explanation; prioritize the named product's official documentation and versioned manuals. | Accept only evidence applicable to the named product and version; do not convert one vendor's design into a universal agent rule. |
| `official_context_window_query` | `official documentation context window limits attention retrieval long context current model` | Use when an example names current context limits or behavior; restrict to authoritative model or platform documentation first. | Record model, date, limits, and stated behavior; replace volatile numbers modularly without rewriting stable selection principles unless the mechanism changes. |
| `official_prompt_cache_query` | `official documentation prompt caching cache hit rate pricing coding agents` | Use when this reference explains current cache semantics or cost; prioritize vendor documentation and current pricing or lifecycle pages. | Separate documented mechanism and price from author inference about production viability; refresh any dependent cost example. |
| `primary_research_long_context_query` | `long context language models performance degradation retrieval distraction primary research paper` | Use when making a causal or empirical claim about context quality beyond official product behavior; prioritize peer-reviewed or original research. | Inspect population, task, model, context length, metric, and limitations; do not generalize one benchmark to all agent work. |
| `primary_research_tdd_query` | `test driven development large language model code generation empirical study executable specification` | Use before broad claims that tests reduce AI coding defects or implementation attempts. | Distinguish controlled study, observational report, and opinion; preserve local source outcomes as source-reported until independently reproduced. |
| `primary_research_naming_query` | `identifier naming semantic search code language model comprehension empirical study descriptive function names` | Use before asserting that a four-word naming rule causes a specific productivity improvement. | Evaluate whether the study tests semantic naming, exact word count, code search, or human comprehension; narrow the claim to the measured construct. |
| `github_repository_query_phrase` | `AI native explanation patterns GitHub repository context offloading TDD naming examples` | Use for implementation examples after governing claims are established; inspect repository activity, code, tests, and issue history. | Treat prevalence as implementation evidence, not proof of correctness or causality; isolate copied product details for later refresh. |
| `release_notes_query_phrase` | `AI coding agent changelog release notes context management prompt caching migration` | Use when a named tool, command, API, or example may have changed. | Confirm release date, affected versions, migration scope, and deprecation status; update routes and commands with source precedence. |
| `reader_efficacy_query` | `plain language technical explanation analogy transfer learning counterexample primary research` | Use when revising the teaching method itself rather than the AI-native subject. | Prefer evidence that measures comprehension or transfer, not only preference or readability; record audience and task differences. |
| `generic_discovery_fallback` | `ai native explanation patterns official documentation best practices GitHub examples changelog release notes migration` | Use only to discover vocabulary or possible authorities when the specific claim and source are unknown. | Trace every material result to its governing or primary source; repeated derivative pages count as one lineage, not independent confirmation. |

Choose the channel from the claim type. Local behavior starts with local sources, repository history, and current tests. Current product behavior starts with official versioned documentation and release notes. Empirical outcome claims start with primary studies or reproducible local measurement. Design rationale may require issue or maintainer history. Reader-effect claims need representative reader evidence or learning research; another technical blog post does not establish teaching efficacy.

Before searching, record the trigger, questioned claim, current wording, applicable product or version, preferred authority, and what evidence would preserve, revise, narrow, or retire it. This prevents broad results from redefining the question after the fact. Broad search is acceptable for vocabulary discovery, but source-count voting is not: ten pages copying one unsourced statement provide one weak lineage.

Reject or quarantine results that are undated where date matters, describe a different version, contain no primary evidence for an empirical claim, optimize for search visibility rather than traceability, or cite one another circularly. GitHub examples can show that an implementation exists and reveal operational tradeoffs; popularity does not make the pattern safe or canonical. A negative search result means evidence was not found with the recorded method, not that the claim is false.

Use a minimal refresh record:

```text
trigger: mapped source, product, example, command, or reader fixture changed
claim: exact statement under review and its current evidence label
query: search text, source restrictions, date, and tool
result: inspected authority, version, relevant passage, and conflicts
decision: preserve, revise, narrow, route, or retire
impact: dependent sections, examples, derivatives, and gates rerun
uncertainty: what remains uninspected or unresolved
```

Record failed query paths when their absence influences the conclusion. Scale detail to consequence: a low-impact product example may need source URL, date, claim, and replacement decision; a security, reliability, or quantitative claim needs stronger provenance and review. After any update, rerun claim mappings, changed examples, transfer fixtures, focused file policy, and complete-file coherence.

Refresh horizons differ. Core causal principles may remain stable while product examples, commands, limits, prices, and release details change quickly. Audience assumptions can also age when the reference reaches a new group. Classify dependencies by volatility and consequence, prefer event-triggered refresh, and add an owner-selected stale-link review where quiet aging matters. No universal interval is asserted.

Keep volatile examples modular. A timeless mechanism plus one clearly labeled current example is easier to maintain than a principle expressed entirely through a product snapshot. This reduces future search demand and prevents a routine example refresh from causing unnecessary semantic churn in the governing mental model.

## Evidence Boundary Notes

Evidence status determines what a reader may repeat as fact, follow as local policy, test as a hypothesis, or leave unresolved. A path or URL alone does not establish that a source was inspected, current, primary, applicable, or correct. Classify material claims by origin, inspection status, scope, evidence type, transformation, and uncertainty before drafting.

| evidence_boundary_label | precise_meaning | permitted_wording | prohibited_upgrade |
| --- | --- | --- | --- |
| `local_corpus_sourced_fact` | A statement tied directly to an inspected local source path, preserving that source's conditions and epistemic status. | "The local skill instructs writers to put plain language before exact terminology." | Do not imply that local presence proves empirical effectiveness or universal practice. |
| `external_research_sourced_fact` | A statement tied to a public source that was actually opened, evaluated for authority, date, version, and applicability, and recorded in the refresh evidence. | "The inspected official documentation states this behavior for the named version." | Do not apply this label to an unvisited URL, derivative summary, or mismatched product. |
| `combined_evidence_inference_note` | Author synthesis that connects inspected evidence into guidance and states the reasoning, boundary, and reversal trigger. | "Given the local source-first rule and the observed audience fixture, keep detailed provenance in the review record and surface decision-changing boundaries." | Do not phrase the connecting judgment as though a source stated it verbatim or an experiment proved it. |
| `source_reported_measurement` | A quantitative or outcome claim reported by a source but not independently reproduced for this repository. | "The supporting source reports 67% faster development in its originating account." | Do not write "four-word names make development 67% faster" or call the value a local result. |
| `current_task_observation` | A directly observed property of the files, commands, verifier output, or reader fixture used in this evolution. | "The focused verifier reported 26 sections and 1,560 unique field values for this saved path." | Do not generalize one file result to the whole corpus or future revisions. |
| `policy_target_or_guardrail` | A required or proposed threshold that governs release but is not evidence that the threshold has been achieved. | "The seed target requires at least 18 of 20 sampled routing decisions." | Do not report a target as a measured rate or reliability result. |
| `editorial_recommendation` | A local choice supported by method, systems judgment, and stated tradeoffs rather than direct empirical proof. | "Use one bounded analogy per major concept by default and remove it when it adds more prerequisites than it removes." | Do not describe the recommendation as universally optimal or scientifically calibrated. |
| `unrefreshed_external_pointer` | A public URL or future query retained for later verification but not inspected under the current no-browse constraint. | "This pointer may be used in a future refresh; current applicability is unknown." | Do not cite it as current corroboration or infer its contents from the URL. |
| `unresolved_or_conflicting_claim` | Evidence is missing, incompatible, or insufficient for the requested scope. | "The available local sources do not establish this outcome for the target project." | Do not average conflicting claims, fill the gap with generic advice, or hide uncertainty in confident tone. |

Apply this taxonomy to material causal, quantitative, historical, normative, and action-bearing claims. Connective prose and ordinary definitions do not need noisy sentence-level labels unless origin changes meaning. When one sentence combines statuses, split it. For example, "The local source reports a naming improvement, so every project should enforce four words" contains a source-reported observation and an unsupported universal recommendation; one citation cannot legalize the second claim.

Use layered presentation. The reader-facing explanation states boundaries where they change confidence or action: "the source reports," "in this repository," "the current official documentation states," "this is our recommended default," or "evidence remains unresolved." The source table and working packet retain paths, passages, conditions, transformations, and conflicts for review. This preserves flow without hiding epistemology.

Good wording says, "The supporting source reports a 67% improvement in its project after adopting its naming convention; test whether semantic naming improves this repository before repeating that percentage as a local result." Bad wording says, "Four-word names are 67% faster." Borderline wording links the source but says the value "proves" the convention generally. The change from "reports" to "proves" crosses an evidence boundary even though the citation is unchanged.

Treat provenance labels as routing metadata, not truth certificates. A local source can be stale, mistaken, or normative rather than empirical. An external official source can be current for its product and irrelevant to local behavior. Several derivative pages may trace to one unsupported origin. Disagreement inside one category remains disagreement; do not average all local or external sources into an artificial consensus.

Verify boundaries semantically. Sample each material claim against the complete source passage, inspect whether conditions and causal direction survived, check authority and version where freshness matters, compare the receiving wording's confidence, and sample maintained derivatives. Automated checks can confirm that labels exist but cannot establish that they are correctly assigned. As a regression probe, remove "source reports" or one applicability condition and confirm that review catches the confidence escalation.

The current evidence ledger for this evolved file is:

- The two mapped local explanation sources were read completely and support the method, mental models, examples, and source-reported claims described here.
- Public URLs and future web queries were not refreshed because browsing was prohibited. They remain `unrefreshed_external_pointer` entries and provide no current factual support in this evolution.
- Numerical values inherited from the seed, including the 12-source workload trigger, 100-percent source-boundary target, 18-of-20 decision sample target, zero unsupported-claim target, and 10-minute performance target, are policy or heuristic values unless a separate observation is explicitly recorded.
- File counts, heading order, section lengths, packet counts, exact field uniqueness, marker scans, and command interfaces observed locally are `current_task_observation` values bounded to their saved versions and commands.
- Expanded decisions about analogy limits, artifact routing, workload decomposition, observability, retry behavior, and maintenance are `editorial_recommendation` or `combined_evidence_inference_note` guidance unless directly attributed otherwise.
- No new empirical performance, reliability, security, or general reader-population claim was established by this prose evolution.

Confidence has at least two dimensions. Review can be highly confident about what an inspected source says while remaining uncertain that its result generalizes to another project, model, reader, or year. Record both source fidelity and applicability. Strong local policy and uncertain empirical benefit can coexist without contradiction.

For maintained derivatives, carry a compact contract with the governing claim, evidence status, applicable conditions, authority, and refresh trigger. A prompt, slide, or summary may omit the full provenance table, but it must not silently upgrade confidence. When a claim is corrected or retired, identify high-consequence maintained copies and update or redirect them. Evidence metadata should travel with a claim like a type so invalid transformations become visible at artifact boundaries.
