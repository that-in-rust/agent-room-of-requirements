# Parallel Agent Dispatch Patterns

**Decision supported.** This section helps decide whether a batch of problems should be dispatched to parallel agents and what shape each dispatch must take. The seed title names the theme without its core principle, dispatch one agent per independent problem domain and let them work concurrently, with independence as the gating test.

**Recommended default and causal basis.** Group failures by what is broken, verify domains are independent, dispatch one focused self-contained agent per domain, then review, conflict-check, and run the full suite. The skill's overview states that sequential investigation of unrelated failures wastes time exactly because each investigation is independent.

**Operating conditions and assumptions.** Two or more tasks exist that can be worked without shared state or sequential dependencies. This reference operationalizes the dispatching-parallel-agents skill and does not cover orchestration frameworks beyond its prompt-level pattern.

**Failure boundary and alternatives.** The doctrine collapses when failures are related, when shared state couples the agents, or when exploratory debugging means nobody knows what is broken yet. Bounded alternatives and recoveries: a single agent investigating all failures when they are related, or sequential agents when work is independent but state is shared.

**Counterexample, gotchas, and operational comparison.** The tempting misuse is parallelizing related failures, where fixing one might fix others, which the skill routes to a single investigating agent instead. Good: three test files with different root causes dispatched to three agents. Bad: parallel agents on failures that share one upstream bug. Borderline: sequential agents for independent problems touching the same files, the graph's shared-state branch.

**Verification, evidence, and uncertainty.** Confirm a dispatch produced under this reference passed the independence test and ended with a conflict check and a full-suite run. The SKILL.md overview, core principle, and decision graph state every element promoted here. How the pattern scales past the source's three-agent example is unaddressed by the skill.

**Second-order consequence.** The skill treats parallelism as a property of the problem, not the tooling, the decision graph asks about independence and shared state before any dispatch mechanics appear.

**Revision decision.** Open with the one-agent-per-domain principle, the independence test that gates it, and the four-step pattern from domain identification to integration.

**Retained seed evidence.** The exact theme title and its dispatch-patterns framing remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which recorded source may back which claim about parallel agent dispatch. The seed map lists two local rows without recording that they are byte-identical copies of one skill, an archive snapshot and a live claude-skills copy, so the corpus is one 180-line document, not two.

**Recommended default and causal basis.** Cite the skill once for each claim, note the duplicate only for path resolution, and mark external corroboration as absent. Claims in this document trace to a single text, and pretending two independent sources corroborate each other would inflate confidence.

**Operating conditions and assumptions.** Both paths stay identical, a future divergence would make the live copy authoritative for current practice. The table records provenance for this document's claims and does not rank multi-agent literature outside the archive.

**Failure boundary and alternatives.** The three external URLs concern AGENTS.md instruction formats, adjacent to agent work but silent on parallel dispatch, and none was retrieved. Bounded alternatives and recoveries: replace external candidates with multi-agent orchestration sources in a future retrieval pass, or diff the copies each cycle to catch divergence.

**Counterexample, gotchas, and operational comparison.** Citing both copies for one claim reads like corroboration while adding nothing. Good: citing the skill's decision graph for the independence test. Bad: citing agents.md for dispatch doctrine. Borderline: treating the live-tree copy as evidence of current adoption, plausible but inferred.

**Verification, evidence, and uncertainty.** Confirm every claim traces to the single skill text and the identity of the two copies is checked. Both mapped files were read in full and compared byte-identical during this evolution. Whether the copies will stay synchronized is unknown.

**Second-order consequence.** The duplication is itself information, the skill exists in both the dated archive and the live skills tree, suggesting it is actively used rather than merely archived.

**Revision decision.** Mark both local paths as read in full and identical, count the evidence base as one source, and downgrade the external URLs to unretrieved adjacent candidates.

**Retained seed evidence.** All five source rows with their category, confidence, and synthesis-role columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/superpowers/dispatching-parallel-agents/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/superpowers/dispatching-parallel-agents/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | external_research_sourced_fact | primary guidance for project instruction files and agent context loading |
| https://agents.md/ | external_research_source_material | external_research_sourced_fact | community format for predictable agent instructions |
| https://github.com/openai/codex | external_research_source_material | external_research_sourced_fact | GitHub implementation and project-level agent guidance |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which dispatch rules deserve default adoption when facing multiple independent problems. The seed scoreboard scores corpus hygiene while the skill's own load-bearing rules go unranked, the independence test, one agent per domain, focused self-contained prompts, and mandatory post-return verification.

**Recommended default and causal basis.** Apply all four rules on every multi-problem batch, in gate order. The skill sequences these as gates, independence decides whether to dispatch, prompt discipline decides whether dispatch succeeds, and verification decides whether the results integrate.

**Operating conditions and assumptions.** Each promoted rule keeps its falsifiable phrasing so a reviewer can point at the violation. The scoreboard ranks dispatch-discipline rules for adoption priority and does not rank agent platforms.

**Failure boundary and alternatives.** The seed's numeric scores were never measured and the skill offers no internal ranking beyond its gate order. Bounded alternatives and recoveries: order the rules by observed violation frequency once measured, or rank by blast radius with skipped verification as the widest.

**Counterexample, gotchas, and operational comparison.** Prompt discipline is the rule most often shaved, a dispatch can look correct while its prompts are too broad, context-free, or vague about output, the exact mistakes the skill lists. Good: a dispatch reviewed against all four rules. Bad: parallel agents launched on an unexamined failure list. Borderline: skipping the conflict check when agents touched disjoint directories, tolerated with the full suite still run.

**Verification, evidence, and uncertainty.** Trace each promoted rule to its stated section in the skill. The decision graph, pattern steps, prompt structure, and verification list state each promoted rule. Which rule violations occur most often in real dispatches is unmeasured.

**Second-order consequence.** The four rules mirror a function contract, precondition, decomposition, interface, and postcondition, which explains why skipping any one produces a characteristic failure the mistakes section names.

**Revision decision.** Promote a top tier of four rules, test independence before dispatching, scope one agent per problem domain, give each agent focused self-contained prompts with specified output, and verify with conflict checks plus a full-suite run.

**Retained seed evidence.** All three scored rows with their tier labels and failure-prevention targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `parallel_agent_dispatch_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local parallel agent material before synthesizing dispatch patterns recommendations. |
| `parallel_agent_dispatch_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `parallel_agent_dispatch_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what single orienting claim should govern parallel dispatch judgments. The seed thesis repeats the load-local-first formula instead of the skill's claim, that independent problems should be decomposed into focused, self-contained, concurrently dispatched agents whose results are verified together.

**Recommended default and causal basis.** Phrase the thesis as independence-gated decomposition with verified integration, with the three evidence labels kept on its clauses. Every section of the skill serves that claim, the graph gates it, the pattern executes it, the prompt structure interfaces it, and the verification list closes it.

**Operating conditions and assumptions.** The labels stay attached so skill-derived clauses remain distinguishable from inference. The thesis orients use of this reference and does not compress the prompt-level rules it stands on.

**Failure boundary and alternatives.** A parallelism-only thesis overstates the doctrine, the skill spends as many lines on when not to dispatch as on how. Bounded alternatives and recoveries: quote the core principle verbatim as the thesis, or phrase it as the four gates in order.

**Counterexample, gotchas, and operational comparison.** Paraphrases keep dispatch in parallel and drop the verification clause, the half of the doctrine that catches systematic agent errors. Good: citing the thesis to demand an independence check before a batch dispatch. Bad: quoting it to justify parallelizing an exploratory debug. Borderline: compressing to one agent per problem for a prompt, losing the verification clause.

**Verification, evidence, and uncertainty.** Check the thesis clauses against the core principle, pattern steps, and verification list. The overview, pattern, and verification sections ground every clause of the restated thesis. Whether the wider multi-agent literature phrases the discipline the same way is unknown without retrieval.

**Second-order consequence.** The thesis binds speed to discipline, the time saved by concurrency is paid for by scoping and verification work, and the skill's real example shows the trade paying off only because both sides were done.

**Revision decision.** Restate the combined inference as decompose by independent domain, dispatch focused self-contained agents concurrently, and trust no result until conflicts are checked and the full suite passes.

**Retained seed evidence.** The three labeled thesis lines with their local, external, and combined-inference structure remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `parallel_agent_dispatch_patterns` contains 2 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Parallel Agent Dispatch Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which local path a parallel-dispatch question should open first. The seed map records heading signals without the corpus's real shape, one skill duplicated across the dated archive and the live claude-skills tree, with the live copy the natural first stop.

**Recommended default and causal basis.** Read the live claude-skills copy, verify it still matches the archive snapshot, and cite whichever path the claim's dating requires. Path choice matters for freshness, the archive path is a monthly snapshot while the live path is where revisions would land.

**Operating conditions and assumptions.** Both files remain readable at their mapped paths. The map indexes the two mapped paths and does not cover sibling superpowers skills.

**Failure boundary and alternatives.** The copies are identical today, so the distinction is procedural until they diverge. Bounded alternatives and recoveries: record line anchors per section, diff-check the copies each cycle, or map the sibling skills in a future pass.

**Counterexample, gotchas, and operational comparison.** The sibling directory contains other superpowers skills whose doctrines may interlock with this one, unread and unmapped here. Good: reading the live copy and diffing against the archive. Bad: citing the archive as current practice after the copies diverge. Borderline: answering from either copy today, harmless while identical.

**Verification, evidence, and uncertainty.** Open both files and confirm they match and carry the sections described. Both files were read in full, 180 lines each, and compared byte-identical. Whether sibling skills in the superpowers tree overlap this doctrine is unknown until read.

**Second-order consequence.** The skill is self-contained by design, unlike multi-file skills it carries its graph, pattern, prompts, mistakes, and example in one document, so routing within the corpus is trivial and the map's job is freshness, not navigation.

**Revision decision.** Annotate the rows as identical copies, prefer the live path for future reads, and record the archive path as the dated snapshot for provenance.

**Retained seed evidence.** Both local source rows with their titles, heading signals, and usage roles remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/superpowers/dispatching-parallel-agents/SKILL.md | dispatching-parallel-agents | Dispatching Parallel Agents; Overview; When to Use; The Pattern; 1. Identify Independent Domains; 2. Create Focused Agent Tasks | skill entrypoint or reusable agent prompt |
| claude-skills/superpowers/dispatching-parallel-agents/SKILL.md | dispatching-parallel-agents | Dispatching Parallel Agents; Overview; When to Use; The Pattern; 1. Identify Independent Domains; 2. Create Focused Agent Tasks | skill entrypoint or reusable agent prompt |

## External Research Source Map

**Decision supported.** This section helps decide how much weight external rows may carry in parallel dispatch guidance. The seed map lists AGENTS.md guides and the Codex repository as external facts although none was retrieved and none addresses parallel dispatch, they concern agent instruction files, an adjacent topic at best.

**Recommended default and causal basis.** Rest all claims on the single read skill and treat external corroboration as absent until a targeted retrieval pass. External rows are meant to corroborate the theme, and instruction-format documents cannot corroborate dispatch decomposition or verification doctrine.

**Operating conditions and assumptions.** Each row keeps a note naming what it could and could not confirm. The map catalogs candidate external references and does not certify content, freshness, or relevance.

**Failure boundary and alternatives.** Removing the rows would break seed preservation, so they stay with downgraded labels and an adjacency note. Bounded alternatives and recoveries: a retrieval pass against agent-platform subagent docs if authorized, distributed-systems task-decomposition literature as a secondary candidate, or leaving the table annotated as is.

**Counterexample, gotchas, and operational comparison.** The rows' agent vocabulary makes them look on-topic, agents.md is about instructing agents, not dispatching them in parallel. Good: naming subagent platform docs as the retrieval target. Bad: citing the Codex repository for dispatch verification rules. Borderline: using agents.md conventions to shape dispatched agents' instruction files, adjacent but plausible with an inference label.

**Verification, evidence, and uncertainty.** Confirm no claim cites an external row as fact and the adjacency note is present. No external retrieval was performed and the three URLs' subject matter is evident from their titles. Whether platform subagent docs confirm the skill's pattern is unknown.

**Second-order consequence.** This theme's best external analogues are platform docs for subagent or task-tool features, since the skill's dispatch snippet is written against exactly such a platform primitive.

**Revision decision.** Downgrade all three rows to unretrieved adjacent candidates and name multi-agent orchestration writeups and subagent documentation from agent platforms as the natural replacement candidates.

**Retained seed evidence.** All three external rows with their names, roles, and boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | primary guidance for project instruction files and agent context loading | external_research_sourced_fact |
| https://agents.md/ | AGENTS.md open format | community format for predictable agent instructions | external_research_sourced_fact |
| https://github.com/openai/codex | OpenAI Codex repository | GitHub implementation and project-level agent guidance | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which recurring dispatch failures deserve standing detection rules. The seed registry lists corpus-hygiene failures while the skill ships a paired mistakes list, too-broad scope, missing context, missing constraints, and vague output, plus four when-not-to-use conditions.

**Recommended default and causal basis.** Scan each dispatch prompt for named scope, pasted context, stated constraints, and a required output, and scan the batch itself for coupling before launch. Each mistake arrives with its correction in the source, fix all the tests becomes fix this named file, fix the race condition becomes pasted errors and test names.

**Operating conditions and assumptions.** Each row pairs its smell with the observable test the source states. The registry names dispatch and prompt anti-patterns with detectors and does not police the dispatched agents' coding style.

**Failure boundary and alternatives.** The mistakes list covers prompt defects, while dispatch-level defects, parallelizing related failures or shared state, live in the when-not-to-use section and must be registered separately. Bounded alternatives and recoveries: encode the checks into a pre-dispatch checklist, fold detection into the completeness section, or keep the registry as mistake-to-correction pointers.

**Counterexample, gotchas, and operational comparison.** The no-constraints mistake fails loudest, an unconstrained agent might refactor everything, damage that outlives the dispatch. Good: rejecting a prompt reading fix all the tests. Bad: dispatching parallel agents into one shared config file. Borderline: a prompt without constraints for a read-only investigation task, low risk but still against the pattern.

**Verification, evidence, and uncertainty.** Replay each registry row against the mistakes and when-not-to-use sections and confirm its test is executable on a real prompt. The common-mistakes pairs and the when-not-to-use list supply every added row. Relative frequency of each anti-pattern in real dispatches is unmeasured.

**Second-order consequence.** Every prompt mistake is an underspecification, the skill's corrections all add information, a file name, error text, a constraint, an output contract, so the detector is asking what the agent would have to guess.

**Revision decision.** Add rows for the four prompt mistakes with their paired corrections and the four misdispatch conditions, related failures, full-context needs, exploratory debugging, and shared state.

**Retained seed evidence.** All three original registry rows with their causes, replacements, and detection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which gates must pass before dispatched agent results or this reference's guidance is trusted. The seed gate names the corpus verifier while the theme's real gates are the skill's post-return sequence, review each summary, check for conflicts, run the full suite, and spot check for systematic errors.

**Recommended default and causal basis.** Gate every integration on the four steps in order, recording what each summary claimed and what verification found. The skill makes integration conditional on these steps because agents can make systematic errors and independent fixes can still collide.

**Operating conditions and assumptions.** The dispatcher can read every agent's summary and run the project's full test suite. The gate set defines what must pass before dispatched results are integrated and does not gate the dispatch decision itself, which the decision graph owns.

**Failure boundary and alternatives.** The gates assume a runnable full suite, dispatches in codebases without one lose their strongest objective check. Bounded alternatives and recoveries: diff-based conflict detection when file overlap is suspected, sampled spot checks at volume, or sequential integration when the suite is slow.

**Counterexample, gotchas, and operational comparison.** Conflict checks on green suites feel redundant, yet two agents editing the same helper can pass tests while silently reverting each other's intent. Good: an integration record with four explicit gate outcomes. Bad: merging on the agents' own success claims. Borderline: skipping spot checks after repeated clean dispatches from the same decomposition, drift risk accepted knowingly.

**Verification, evidence, and uncertainty.** Run the four gates against a sample dispatch and confirm each yields a decidable outcome. The review-and-integrate step and the verification section state every gate verbatim. How often spot checks catch what suites miss is unmeasured.

**Second-order consequence.** The gates distrust success reports, an agent returning fixed is treated as a claim to verify, not a result to merge, which is the same stance the corpus takes toward its own references.

**Revision decision.** Adopt the four-step return gate verbatim, summaries read, conflicts checked, full suite green, and spot checks done, with integration blocked until all four pass.

**Retained seed evidence.** The original verification gate line and its repository verifier command block remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide when a working agent should open this reference and which section it should enter through. The seed guide keys usage to theme mentions instead of the state that triggers it, an agent facing two or more failures or tasks and deciding whether to fan out.

**Recommended default and causal basis.** Open this reference when holding a list of failures or tasks, and walk the decision graph before choosing dispatch. The skill's description names its trigger exactly, use when facing 2+ independent tasks that can be worked without shared state or sequential dependencies.

**Operating conditions and assumptions.** The environment offers an agent-dispatch primitive akin to the skill's Task calls. The guide routes readers into this reference and does not decompose their problems for them.

**Failure boundary and alternatives.** Keying to every mention of parallelism would drag the doctrine into tool-call parallelism and CI concurrency it does not govern. Bounded alternatives and recoveries: single-agent investigation for coupled failures, sequential agents for shared state, or in-context parallel tool calls for work below the agent-dispatch threshold.

**Counterexample, gotchas, and operational comparison.** Agents reach for dispatch at the wrong phase, during exploratory debugging when nobody knows what is broken, the skill's explicit exclusion. Good: entering at the decision graph with six failures across three files. Bad: opening this to parallelize independent file reads. Borderline: consulting only the prompt structure to write one focused subagent task, a fragment use that still helps.

**Verification, evidence, and uncertainty.** Walk a multi-failure state and a coupled-failure state through the guide and confirm each lands on the intended path. The skill's description line and decision graph partition the entry points as described. How often real batches are genuinely independent is unmeasured.

**Second-order consequence.** The guide's hardest call is distinguishing independent from related failures, and the skill's heuristic is causal, ask whether fixing one might fix others, a question answerable before any dispatch.

**Revision decision.** Trigger on multi-failure or multi-task states, route the coupled and exploratory cases to single-agent investigation, and enter dispatchers at the decision graph before any prompt writing.

**Retained seed evidence.** The original usage line and all four guidance bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide what end-to-end shape a competent parallel dispatch session should take. The seed scenario shows a builder choosing a pattern and stops before the journey the skill scripts, group failures into domains, write focused prompts, dispatch concurrently, then review, conflict-check, and integrate.

**Recommended default and causal basis.** Narrate a failures-to-integration pass using the skill's real example as the destination shape. The skill narrates its own real session, six failures across three files after a refactoring, three agents, three independent fixes, zero conflicts, which the journey should mirror.

**Operating conditions and assumptions.** The failures are enumerable and attributable to distinct subsystems before dispatch. The scenario dramatizes one representative dispatch journey and does not cover sequential-agent fallbacks.

**Failure boundary and alternatives.** One journey cannot cover the declined-dispatch path, where the graph routes related failures to a single investigator. Bounded alternatives and recoveries: a declined-dispatch journey ending in single-agent investigation, or a sequential journey for shared-state work.

**Counterexample, gotchas, and operational comparison.** Journeys that skip reading agent summaries integrate blind, the source reads all three before touching the suite. Good: a journey ending with conflicts checked and the suite green. Bad: one ending when the last agent reports done. Borderline: a journey integrating two of three agents while one still runs, order-of-return integration the skill neither blesses nor forbids.

**Verification, evidence, and uncertainty.** Check each journey beat against the four pattern steps and confirm none is skipped silently. The pattern section and the dated real example script exactly this sequence. Typical failure-batch sizes outside the source's example are unrecorded.

**Second-order consequence.** The journey's decisive beat is domain grouping, everything downstream inherits its quality, the source's clean integration traces directly to abort, batch, and race domains being genuinely disjoint.

**Revision decision.** Extend the journey through the source's session shape, domains identified per test file, each prompt carrying test names, root-cause hints, constraints, and an output contract, agents returning summaries, and integration gated on the full suite.

**Retained seed evidence.** The role-based opening, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The agent-system designer is starting from a task that needs context selection, tool use, delegation, and verification and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `parallel_agent_dispatch_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing what context to load, what to offload, when to delegate, and how to prove completion.
Reference opening trigger: Open this file when the task mentions parallel agent dispatch patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide how aggressively a batch should be parallelized and what being wrong costs. The seed guide keys adopt, adapt, and avoid to generic evidence agreement instead of this theme's variables, failure independence, state sharing, problem legibility, and the cost of a wrong decomposition.

**Recommended default and causal basis.** Dispatch in parallel only when the causal heuristic, might fixing one fix the others, answers no for every pair. The skill's own branches encode the trade, independent and stateless goes parallel, independent but state-sharing goes sequential, related goes single-agent.

**Operating conditions and assumptions.** The batch's failures are enumerated with enough diagnosis to attribute each to a subsystem. The guide calibrates dispatch aggressiveness per batch and cannot waive the post-return verification gates.

**Failure boundary and alternatives.** Independence judgments are fallible, failures that look disjoint can share a hidden root cause discovered only mid-investigation. Bounded alternatives and recoveries: a brief triage pass to establish independence before committing, hybrid dispatch with one investigator plus deferred parallel fixes, or staying sequential when stakes are low.

**Counterexample, gotchas, and operational comparison.** Being wrong costs twice, mid-flight discovery of coupling wastes the parallel work and still requires the single-agent investigation that should have run first. Good: parallel dispatch on three subsystem-distinct files. Bad: parallel dispatch on failures sharing one broken event structure. Borderline: dispatching two agents while holding back a third suspicious failure for triage.

**Verification, evidence, and uncertainty.** Audit past dispatches for mid-flight coupling discoveries and check declined dispatches for wasted caution. The decision graph's three branches and the key-benefits list state the trade this guide rekeys onto. The base rate of hidden coupling in apparently independent batches is unmeasured.

**Second-order consequence.** The trade prices coordination against speed, the skill's benefit list, focus, independence, three-for-one time, is bought entirely at decomposition time, so a wrong split refunds nothing and adds integration cost.

**Revision decision.** Rekey adopt to parallel dispatch for legible independent stateless batches, adapt to sequential agents or narrowed scopes when state couples the work, and avoid for related failures and exploratory debugging.

**Retained seed evidence.** The Adopt when, Adapt when, Avoid when, and Cost of being wrong rows with their verification prompts remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the parallel agent dispatch patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong parallel agent dispatch patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which copy outranks which when parallel-dispatch guidance conflicts or the copies diverge. The seed hierarchy names sources without ranking them, and this corpus is a single skill in two identical copies, so the ranking question is which copy speaks for current practice, not which document wins.

**Recommended default and causal basis.** Resolve doctrine from the live copy, cite the archive for dating, and re-diff whenever either path is read. The live claude-skills tree is where revisions would land while the monthly archive is frozen, so on divergence the live copy outranks the snapshot for practice and the snapshot wins for historical claims.

**Operating conditions and assumptions.** Both files remain at their mapped paths and the diff check stays part of the read ritual. The hierarchy ranks local retrieval priority for this theme and does not rank the unread sibling skills.

**Failure boundary and alternatives.** With byte-identical copies the ranking is untestable today, it matters only at first divergence. Bounded alternatives and recoveries: designating one path canonical in the mapping table, a scheduled diff in the refresh queries, or collapsing to one row with an alias note.

**Counterexample, gotchas, and operational comparison.** Archive paths look more official in this corpus's tables, inverting the freshness ranking a reader would assume. Good: preferring the live copy after a divergence adds a new mistake row. Bad: citing the stale archive as current practice post-divergence. Borderline: citing either today, harmless while identical.

**Verification, evidence, and uncertainty.** Confirm both paths exist and the identity check result is recorded here. The diff performed during this evolution found the copies byte-identical. Whether the live tree is actually maintained or merely mirrored is unknown.

**Second-order consequence.** The hierarchy's real risk is silent divergence, nothing forces the copies to stay synchronized, so the diff check is not bookkeeping but the mechanism that keeps this ranking honest.

**Revision decision.** Rank the live copy first for current doctrine, the archive copy first for dated provenance, and record the identity check that currently makes them interchangeable.

**Retained seed evidence.** The classification vocabulary line, the confidence warning, and the hierarchy rows with their reviewer questions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/superpowers/dispatching-parallel-agents/SKILL.md | canonical primary source | Dispatching Parallel Agents; Overview; When to Use | What guidance, warning, or example should this source contribute to Parallel Agent Dispatch Patterns? |
| claude-skills/superpowers/dispatching-parallel-agents/SKILL.md | supporting context source | Dispatching Parallel Agents; Overview; When to Use | What guidance, warning, or example should this source contribute to Parallel Agent Dispatch Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what concrete evidence object must exist before this reference counts as operational. The seed artifact names a lifecycle diagram while this theme's operational artifact is the dispatch record, the domain grouping, the per-agent prompts, and the four gate outcomes for one real batch.

**Recommended default and causal basis.** Carry one filled record from a real dispatch as the reviewable instance. Every pattern step emits a piece of that record, domains from step one, prompts from step two, summaries and gate results from step four.

**Operating conditions and assumptions.** The record captures the prompts verbatim, not paraphrased, since prompt defects are what the mistakes list detects. The artifact certifies this reference is operational and does not grade the dispatched agents' code.

**Failure boundary and alternatives.** Dispatch records for single-task sessions are ceremony, the null-instance convention applies. Bounded alternatives and recoveries: a declined-dispatch record documenting why the graph routed to a single agent, or a compressed record for two-agent batches.

**Counterexample, gotchas, and operational comparison.** Records reconstructed after integration flatter the dispatch, the independence reasoning should be written before launch while it can still change the decision. Good: a record with three verbatim prompts and four gate outcomes. Bad: a merged batch with no recorded prompts. Borderline: a record without spot-check notes for a trivial two-file dispatch.

**Verification, evidence, and uncertainty.** Check the artifact states the independence reasoning and carries every prompt and gate outcome. The pattern steps and the real example define exactly the fields the record instantiates. Whether record discipline measurably improves dispatch outcomes here is untested.

**Second-order consequence.** The record's prompts are its most reusable part, a well-scoped prompt with context, constraints, and an output contract is a template for every future dispatch into the same subsystem.

**Revision decision.** Define the artifact as one filled dispatch record, the independence reasoning per domain pair, each agent's full prompt, and the summary, conflict, suite, and spot-check outcomes.

**Retained seed evidence.** The artifact definition line and the three artifact field rows with completion rules remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: worked parallel agent dispatch patterns example with user goal, decision point, failure mode, and verification gate.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Parallel Agent Dispatch Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which dispatch behaviors should be taught as exemplary, negligent, or conditionally acceptable. The seed examples restate corpus verdicts and never grade real dispatch conduct against the skill's own contrasts, focused versus broad prompts, contextualized versus bare requests, constrained versus open-ended agents.

**Recommended default and causal basis.** Grade every example by the prompt structure's three properties, focused, self-contained, and specific about output, plus the batch-level independence test. The skill teaches through paired wrong-and-right lines, fix all the tests against fix agent-tool-abort.test.ts, so graded examples should reuse those exact contrasts.

**Operating conditions and assumptions.** Each example names the rule it exercises and the test that decides the verdict. The examples grade dispatch conduct, not the quality of the fixes the agents produced.

**Failure boundary and alternatives.** Examples fixed to the source's TypeScript test files may read as test-repair-specific, though the pattern covers any independent task batch. Bounded alternatives and recoveries: draw examples from this repository's own multi-assignment lanes, grade the source's prompt example directly, or add a declined-dispatch example.

**Counterexample, gotchas, and operational comparison.** The borderline case degrades silently, agents without output contracts still work, they just return unusable summaries discovered only at integration. Good: a prompt naming three failing tests with error text and a do-not rule. Bad: a prompt reading fix the race condition with no location. Borderline: a focused contextualized prompt that never says what to return.

**Verification, evidence, and uncertainty.** Scan each verdict against its cited rule and confirm the graded behavior is visible in the prompt or batch itself. The common-mistakes pairs and the agent prompt example ground all three verdicts. Which negligent shape dominates real dispatches is unmeasured.

**Second-order consequence.** The skill's bad examples all shift work from dispatcher to agent, a vague prompt makes the agent rediscover context the dispatcher already had, spending parallel time on duplicated diagnosis.

**Revision decision.** Recast good as the source's real session, three focused constrained agents integrating cleanly, bad as a fix-everything dispatch with no constraints, and borderline as a well-scoped dispatch missing output contracts.

**Retained seed evidence.** The good, bad, and borderline example lines with their original verdict framing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Parallel Agent Dispatch Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Parallel Agent Dispatch Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Parallel Agent Dispatch Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which observable signals should trigger revising dispatch practice or this reference. The seed metrics name lead time and generic signals without this theme's observables, conflict counts at integration, mid-flight coupling discoveries, and the fraction of dispatches passing all four gates first time.

**Recommended default and causal basis.** Record per dispatch the batch size, independence reasoning, gate outcomes, and any coupling discovered late. The skill's benefit is time saved with clean integration, so its instruments must count conflicts, wasted parallel work, and gate outcomes rather than raw dispatch volume.

**Operating conditions and assumptions.** Dispatch records exist so the counts have a source. The metrics gauge dispatch discipline, not the dispatched agents' code quality.

**Failure boundary and alternatives.** Zero conflicts can mean good decomposition or timid dispatching, the counts need the batch sizes beside them. Bounded alternatives and recoveries: sampled dispatch audits, per-domain conflict heatmaps at volume, or tracking only coupling discoveries at first.

**Counterexample, gotchas, and operational comparison.** Time-saved claims flatter parallel work by ignoring decomposition and integration overhead, the honest measure spans the whole session. Good: tightening the independence heuristic after two coupling discoveries. Bad: celebrating dispatch counts while integrations grow conflicts. Borderline: skipping metrics in a period with no multi-failure batches, noted.

**Verification, evidence, and uncertainty.** Reconcile recorded gate outcomes against sampled audits and check failures trace to named rules. The seed's lead-time indicator and the skill's verification steps anchor the added counters. Healthy baselines for conflicts and coupling rates are unmeasured, so first thresholds are provisional.

**Second-order consequence.** The cheapest telemetry is the coupling discovery, any mid-flight finding that fixing one failure affected another is direct evidence the independence test failed, and it needs no tooling to record.

**Revision decision.** Adopt first-pass gate yield, conflicts per dispatch, coupling discoveries per batch, and agents per batch as primary signals.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: the next run needs fewer clarifications and produces fewer unverifiable claims.
Failure signal: the reference tells agents what to do without defining context budget or escalation rules.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide when this reference may be declared ready to hand to an agent. The seed checklist confirms generic sections exist and never checks this document's specific obligations, the decision graph's three branches, all four pattern steps, the three prompt properties, the four mistakes with corrections, and the four when-not-to-use conditions.

**Recommended default and causal basis.** Tick structural items with citations, then grep this document for each branch, step, property, mistake, and exclusion. This document transmits a gating doctrine, so readiness means the gates, exclusions, and corrections survived transmission intact and uninverted.

**Operating conditions and assumptions.** Each added item names its target and whether a script or human verifies it. The checklist gates this document's readiness, not the quality of dispatches later run under it.

**Failure boundary and alternatives.** A reference that dropped the when-not-to-use list would still describe dispatch while losing the half that prevents misuse. Bounded alternatives and recoveries: generate coverage items from the skill's section list, deep-check two random items per review, or pair-review the dispatch record artifact.

**Counterexample, gotchas, and operational comparison.** Rule presence can pass while phrasing drifted, independent weakened to mostly independent changes the gate materially. Good: a tick citing the line carrying the shared-state exclusion. Bad: all ticks green from a headings glance. Borderline: carrying forward last cycle's phrasing check with a staleness note.

**Verification, evidence, and uncertainty.** Grep this document for the branches, steps, and exclusions, then spot-read two against the skill. The seed's seven structural items map onto real sections here and anchor the added fidelity layer. How much spot-reading each cycle needs depends on edit volume.

**Second-order consequence.** The doctrine's symmetry is its fragility, every use rule has a matching exclusion, and transmission errors that keep the uses while dropping the exclusions turn a discipline into an enthusiasm.

**Revision decision.** Append items requiring the independence test stated, the four pattern steps present, the prompt properties named, the mistake pairs carried, and the exclusion conditions listed.

**Retained seed evidence.** All seven structural checklist items covering scenario, decision guide, hierarchy, artifact, examples, metrics, and routing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Parallel Agent Dispatch Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide when a question should leave this reference and which neighbor owns it. The seed routing splits the theme name into keywords aimed at unnamed destinations instead of routing by need, dispatch decomposition stays here while subagent development, tool-call parallelism, and test-repair technique belong elsewhere.

**Recommended default and causal basis.** Ask whether the question concerns the fan-out and merge or the work inside one agent, and keep only the former here. Readers arrive with parallel-adjacent needs this doctrine does not own, building the agents themselves, parallelizing tool calls inside one agent, and diagnosing the failures being dispatched.

**Operating conditions and assumptions.** Each route names its trigger, a destination resolving to a real file, and what stays here. Routing redirects within this corpus and cannot authorize work in a destination's domain.

**Failure boundary and alternatives.** Keyword routes point at references that exist only as words, stranding the reader who follows them. Bounded alternatives and recoveries: consult the corpus index before adding routes, keep unresolved needs here with a gap note, or escalate genuine overlap to the user.

**Counterexample, gotchas, and operational comparison.** Prompt questions blur the seam, prompt structure for dispatch is owned here while general agent prompting is not, and both arrive worded identically. Good: keeping an independence-test question here. Bad: routing to the parallel adjacent reference, a keyword with no file. Borderline: a dispatched-agent prompt question split between the dispatch contract here and agent design elsewhere.

**Verification, evidence, and uncertainty.** Resolve each named destination to an existing corpus file and walk one sample question through each trigger. The skill's scope, from dispatch decision through integration, defines the seam the routes follow. Whether future themes will subdivide this doctrine's territory is unknown.

**Second-order consequence.** The doctrine's boundary is the dispatch seam, it owns everything between deciding to fan out and integrating results, and disowns both what happens inside each agent and how the problems arose.

**Revision decision.** Keep decomposition, prompt discipline, and integration gating here, route subagent construction to the subagent development reference already in this corpus, and record unowned needs like in-context tool parallelism as gaps.

**Retained seed evidence.** The adjacency guidance line and the three keyword-derived route stubs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use debate, subagent, context, or verification references when the task narrows to a specific agent behavior.
Adjacent reference 1: consider the parallel adjacent reference when the current task pivots away from parallel agent dispatch patterns.
Adjacent reference 2: consider the agent adjacent reference when the current task pivots away from parallel agent dispatch patterns.
Adjacent reference 3: consider the dispatch adjacent reference when the current task pivots away from parallel agent dispatch patterns.

## Workload Model

**Decision supported.** This section helps decide how much dispatch work one session may take on before splitting. The seed model bounds endpoints per batch but not this theme's working unit, one dispatch batch per session, with agent count and integration effort as the real cost drivers.

**Recommended default and causal basis.** Run one dispatch batch per focused session, sized so every prompt is written carefully and every summary read fully. The dispatcher's work scales with domains, each needs independence reasoning and a focused prompt before launch, plus a summary review and conflict check after.

**Operating conditions and assumptions.** The session can hold all domains and their independence reasoning in view at once. The model bounds the dispatcher's work per session and does not bound the dispatched agents' own effort.

**Failure boundary and alternatives.** Agent-count bounds are estimates, three agents into a tangled codebase can cost more integration than six into disjoint services. Bounded alternatives and recoveries: splitting decomposition and dispatch into separate passes for large batches, staged dispatch waves, or delegating integration review at volume.

**Counterexample, gotchas, and operational comparison.** Verification does not parallelize, agent summaries return concurrently but conflict checks and the suite run once over everything, so integration is the fixed serial cost. Good: one three-agent batch fully verified in a session. Bad: three overlapping batches with unread summaries. Borderline: a second small batch launched after the first integrates cleanly.

**Verification, evidence, and uncertainty.** Compare session outcomes at different batch sizes and record where summary review quality degrades. The real example's three-agent shape and the four-step pattern ground the batch-based model. The agent count at which dispatcher attention fails is unmeasured.

**Second-order consequence.** The dispatcher's cost is front-and-back loaded, decomposition and prompts before, verification after, with idle middle time that tempts overlapping batches, a temptation the one-batch bound exists to resist.

**Revision decision.** Rebound the model around one batch per session, the source's three agents as the demonstrated comfortable size, and integration effort budgeted to grow with file overlap between domains.

**Retained seed evidence.** The four workload dimensions with their boundary values and verification pressure points remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Parallel Agent Dispatch Patterns as a agent workflow operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | agent planning, tool use, context loading, delegation, or skill/plugin execution where bad guidance compounds across long-running sessions | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one primary task, up to 10 source files, up to 3 delegated subtasks, and a written completion audit for every run | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Dispatching Parallel Agents; Overview; When to Use; The Pattern; 1. Identify Independent Domains; 2. Create Focused Agent Tasks; Dispatching Parallel  | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is worked parallel agent dispatch patterns example with user goal, decision point, failure mode, and verification gate | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what measurable reliability this reference must demonstrate before its guidance is trusted. The seed table demands unmeasured percentages while this theme supports binary targets, every dispatch has recorded independence reasoning and every integration a completed four-gate record.

**Recommended default and causal basis.** Keep the four seed dimensions with methods attached and lead with the two per-batch scans. The doctrine's tests are per-batch and decidable, the reasoning exists or does not, the gates ran or did not, so targets can be scanned rather than sampled.

**Operating conditions and assumptions.** Each target names its metric, scan method, population, owner, and corrective action. The targets judge this reference and the dispatch discipline, not the dispatched agents' fix quality.

**Failure boundary and alternatives.** Quoting the seed's percentages as achieved performance manufactures rigor this corpus never earned. Bounded alternatives and recoveries: gate-yield targets instead of per-batch scans, sampled record audits, or postmortems per conflicted integration instead of rates.

**Counterexample, gotchas, and operational comparison.** Recorded reasoning does not prove the reasoning was sound, the coupling-discovery count is the independent second gate. Good: a scan showing every dispatch carries its independence reasoning. Bad: reporting the seed's numbers nobody sampled. Borderline: one undocumented emergency dispatch, recorded afterward with the gap noted.

**Verification, evidence, and uncertainty.** Scan one period's dispatches for both targets and record hits with resolutions. The decision graph and verification section give the operational definitions the scans check. No baseline exists for either target, so the first scanned period defines achievability.

**Second-order consequence.** The reasoning target audits the decision the whole pattern hangs on, and its absence predicts exactly the coupling discoveries that waste parallel work downstream.

**Revision decision.** Add binary targets, recorded independence reasoning per dispatch and a complete gate record per integration, each marked unbaselined and owned.

**Retained seed evidence.** All four reliability rows with their threshold values and evidence-collection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which dispatch failures deserve standing mitigations. The seed table carries hygiene and traffic rows and omits how dispatches actually fail, hidden coupling between domains, agents interfering through shared files, prompts too vague to act on, and systematic agent errors merged unspotted.

**Recommended default and causal basis.** Check any failed dispatch backward through the gates, spot check, suite, conflicts, then the original independence reasoning. The skill names each with its guard, the when-not-to-use list for coupling and shared state, the mistakes list for prompts, and the spot-check step for systematic errors.

**Operating conditions and assumptions.** Each row names its trigger, earliest observable signal, blast radius, containment, and correction. The table covers dispatch-level failures, while documentation-process failures stay with the seed rows.

**Failure boundary and alternatives.** Coupling failures surface mid-flight or at integration, after the parallel cost is sunk, which no pre-dispatch signal fully prevents. Bounded alternatives and recoveries: pre-dispatch triage to pre-empt coupling, file-claim conventions to pre-empt interference, or prompt review to pre-empt vagueness.

**Counterexample, gotchas, and operational comparison.** Interference can pass the suite, two agents editing one helper may leave tests green while destroying an invariant only spot checks would notice. Good: a conflicted integration triaged back to overlapping domains. Bad: relaunching the same vague prompts after a failed batch. Borderline: a coupling discovery mid-flight handled by halting one agent, salvage the skill does not script.

**Verification, evidence, and uncertainty.** Seed one failure per row in a review drill and confirm the named signal fires and maps to the right repair. The when-not-to-use list, mistakes pairs, and verification steps supply every added row. Failure frequencies in real dispatches are unmeasured.

**Second-order consequence.** The failures sort by when they are cheapest to catch, coupling at triage, state overlap at decomposition, prompt defects before launch, systematic errors only at spot check, so each guard has one right moment.

**Revision decision.** Add hidden-coupling, shared-state-interference, vague-prompt, and unspotted-systematic-error rows, each with its source-named signal, blast radius, and repair.

**Retained seed evidence.** All four seed failure rows with their triggers and mitigation actions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| context window loses plan | long-running session forgets early constraints or overwrites user intent | write checkpoint summaries and re-read plan before each destructive step |
| tool fanout outruns budget | parallel actions create conflicts, duplicate work, or unbounded external calls | cap fanout, assign ownership, and require merge/audit checkpoints |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a failed dispatch should be re-decomposed, re-prompted, collapsed, or escalated. The seed bullets classify verification failures generically and never carry this theme's retry rule, a failed dispatch is re-decomposed or re-prompted, never blindly relaunched.

**Recommended default and causal basis.** Diagnose which gate failed before any retry, change the decomposition or the prompts accordingly, and keep the seed's one-bounded-retry-then-escalate rule for verification reruns. The skill's failure causes are structural, wrong decomposition or defective prompts, and relaunching without changing either reproduces the failure at full parallel cost.

**Operating conditions and assumptions.** The failed batch's record exists so the retry can name what changed. This governs retrying dispatch batches and reference-verification work, kept as two labeled layers.

**Failure boundary and alternatives.** Re-decomposition assumes the coupling is now understood, a second wrong split wastes a second batch. Bounded alternatives and recoveries: escalation to the user when two decompositions fail on the same batch, sequential fallback for stubborn state sharing, or single-agent investigation as the terminal fallback.

**Counterexample, gotchas, and operational comparison.** Retrying with more agents feels like adding capacity but multiplies the interference surface the failure just demonstrated. Good: a conflicted batch re-split along the discovered coupling. Bad: the same batch relaunched unchanged. Borderline: re-prompting one agent while keeping two clean results, partial retry the skill neither blesses nor forbids.

**Verification, evidence, and uncertainty.** Audit retry sequences for changed decompositions or prompts between attempts and check verification reruns stayed bounded. The when-not-to-use list and mistakes pairs identify the two structural causes the retries must change. How often re-decomposition succeeds on the second attempt is unmeasured.

**Second-order consequence.** The collapse-to-one rule is the theme's distinctive backpressure, when independence fails the correct concurrency is one, not a smaller parallel batch, because the coupling itself is now the problem to investigate.

**Revision decision.** Add the dispatch-layer rules, conflicted integrations get re-decomposition with the coupling folded in, unusable summaries get re-prompting with the missing property added, and coupling discoveries collapse the batch to a single investigator.

**Retained seed evidence.** All five retry and backpressure bullets, including the one-owner-per-file rule, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what evidence must exist that a dispatch session happened as claimed. The seed bullets recycle generic evidence records and never name this theme's evidence stream, the dispatch record, the verbatim prompts, the agent summaries, and the four gate outcomes.

**Recommended default and causal basis.** Record per batch the reasoning, prompts, summaries, and gate outcomes, keeping the agents' full transcripts out of the record. The artifact section defines the record and the gate section its outcomes, so observability means persisting decomposition reasoning, prompts, summaries, and verification results for the feedback loop.

**Operating conditions and assumptions.** Sessions can persist small text records alongside their deliverables. This covers observing dispatch sessions, not the dispatched agents' internal traces.

**Failure boundary and alternatives.** Full records for trivial two-agent batches outgrow their value, the null-instance convention applies. Bounded alternatives and recoveries: prompt-and-outcome-only retention for routine batches, full retention for failed ones, or sampled retention at volume.

**Counterexample, gotchas, and operational comparison.** Summaries paraphrased into the record lose the discrepancies between claim and diff that spot checks feed on. Good: a batch record with three prompts, three summaries, and four gate outcomes. Bad: a merged batch with no record of what was dispatched. Borderline: a null-instance record for a declined dispatch.

**Verification, evidence, and uncertainty.** Spot-check batch records for reasoning, verbatim prompts, and gate outcomes. The seed's small-audit-evidence preference and the skill's expected-output rule anchor the record contents. The retention horizon for batch records is untuned.

**Second-order consequence.** The agent summaries are the stream's irreplaceable part, they are the only record of what each agent believed it did, and the skill's spot-check step exists precisely because that belief can be systematically wrong.

**Revision decision.** Recenter the checklist on session evidence, the independence reasoning, each prompt verbatim, each returned summary, and the gate outcomes with any conflicts named.

**Retained seed evidence.** All six observability bullets including the small-audit-evidence preference remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture tool-call count, context files loaded, delegated tasks, retry count, and completion-audit outcome.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to prove parallel dispatch is buying the time it claims. The seed method fixes handler latency numbers while this theme's performance question is the skill's own claim, three problems solved in the time of one, which no one here has measured.

**Recommended default and causal basis.** Record session time, batch size, and overhead per dispatch, and review whether the parallel fraction is large enough to justify the ceremony. The claim is testable, compare wall-clock session time for dispatched batches against sequential handling of comparable batches, net of decomposition and integration overhead.

**Operating conditions and assumptions.** Enough dispatches accumulate for the contrast to mean anything. This evaluates the dispatch discipline's speed claim, not agent platform latency, keeping the seed's latency defaults as the absent-SLO fallback.

**Failure boundary and alternatives.** Batch comparability is weak, no two failure sets are alike, so the contrast needs many sessions or within-batch estimates. Bounded alternatives and recoveries: gate-yield-only tracking, overhead-ratio tracking, or accepting the source's dated session as the sole evidence with its label.

**Counterexample, gotchas, and operational comparison.** Time saved is invisible without the counterfactual, recording a sequential estimate at triage, before knowing the outcome, is what makes the later comparison honest. Good: a batch record with triage-time sequential estimate and actual session time. Bad: quoting three-for-one as measured local performance. Borderline: adopting the claim unverified for one quarter while records accumulate, noted as assumed.

**Verification, evidence, and uncertainty.** Publish the contrast with batch counts and the estimate-recorded fraction. The real-world impact section states the speed claim this method tests, dated 2025-10-03 in the source. Effect size net of overhead and the batch count needed for signal are unknown.

**Second-order consequence.** The honest denominator includes the dispatcher's serial work, the skill's time-saved claim covers the investigation phase only, while decomposition, summary review, and verification remain sequential and cap the speedup.

**Revision decision.** Measure whole-session time per batch, agents per batch, and integration overhead, and compare against sequential estimates recorded at triage time.

**Retained seed evidence.** The performance method line, both indicator lines, the measurement packet, and the pass and fail conditions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require tool-call budgets, timeout budgets, and a resumable journal when the workflow exceeds one focused session.
Leading indicator to measure: the next run needs fewer clarifications and produces fewer unverifiable claims.
Failure signal to watch: the reference tells agents what to do without defining context budget or escalation rules.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what scale single-dispatcher discipline stops sufficing and what structure replaces it. The seed statement recites multi-system limits and misses this theme's scale walls, batches whose domain count exceeds dispatcher attention, dispatch trees where agents dispatch agents, and codebases too entangled for any independent decomposition.

**Recommended default and causal basis.** Dispatch batches small enough that every pair's independence was actually reasoned about and every summary actually read, staging larger work into waves. The doctrine assumes one dispatcher who can reason about every pairwise independence and read every summary, both of which grow with batch size, one quadratically.

**Operating conditions and assumptions.** Batch records make attention failures visible as unread summaries or unreasoned pairs. The boundaries bound this reference and its discipline, not agent platforms' concurrency limits.

**Failure boundary and alternatives.** Scaling advice beyond the source's three-agent example is inference here, the skill demonstrates one batch size. Bounded alternatives and recoveries: hierarchical dispatch with sub-dispatchers as an unverified extension, entanglement refactoring before dispatch, or accepting sequential work in tangled regions.

**Counterexample, gotchas, and operational comparison.** Waves hide cross-wave coupling, a wave-two domain can depend on a wave-one fix, silently reintroducing the sequencing the batch split was meant to avoid. Good: ten failures staged into two reasoned waves. Bad: ten agents launched on an unexamined failure list. Borderline: a sub-dispatcher handling one large domain, plausible recursion the sources never test.

**Verification, evidence, and uncertainty.** Track gate failures and unread-summary counts against batch size to locate the wall empirically. The skill's three-agent example and focus benefit support the attention-based inference, marked as extension beyond the sources. The batch size at which verification quality collapses is unmeasured.

**Second-order consequence.** The binding constraint is dispatcher attention, not agent capacity, the platform can run many agents but the pattern's safety comes entirely from one mind holding the decomposition and its verification.

**Revision decision.** Add scale signals, pairwise independence checks growing unmanageable, summaries arriving faster than they are read, and decompositions that keep discovering coupling, plus nested dispatch as an unscripted extension.

**Retained seed evidence.** All four scale boundary statements including the distributed split and context-drift rules remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Parallel Agent Dispatch Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which future searches would genuinely refresh this reference's external evidence. The seed query table drops the internal theme name into three templates whose literal phrasing targets a coinage no external author uses.

**Recommended default and causal basis.** Search platform subagent documentation on a fast cadence and orchestration commentary on a slow one, feeding the evidence map. Useful refresh queries speak the ecosystem's vocabulary, subagent dispatch, multi-agent task decomposition, agent orchestration patterns, not this corpus's file-naming scheme.

**Operating conditions and assumptions.** Each query names its target section, source type, and firing trigger. The queries refresh external analogues for this theme, while the local skill changes only through repository edits.

**Failure boundary and alternatives.** Empty results from a coinage query logged as freshness confirmed convert search blindness into false confidence. Bounded alternatives and recoveries: watching the superpowers skill tree itself for revisions, curated multi-agent reading lists, or dated retrieval records as the refresh driver.

**Counterexample, gotchas, and operational comparison.** Multi-agent search results skew toward framework marketing that names orchestration without carrying decomposition discipline. Good: a query for subagent dispatch platform docs feeding the dispatch snippet's assumptions. Bad: searching the literal theme title and logging zero hits as freshness. Borderline: adopting an orchestration framework's decomposition advice with an inference label pending corroboration.

**Verification, evidence, and uncertainty.** Run each query once, grade the top results for doctrinal substance, and rewrite phrasings that return mostly marketing noise. The seed's three-row structure targeting docs, repositories, and release notes fits this theme's platform-bound refresh needs. Which phrasings surface substantive orchestration guidance is unknowable in advance, so the queries need their own review cadence.

**Second-order consequence.** The fastest-moving refresh target is the platform primitive, the Task-style dispatch call the skill's snippet assumes, whose semantics and limits are set by platform releases rather than by doctrine.

**Revision decision.** Rephrase toward ecosystem vocabulary, agent platform subagent and task-tool docs, multi-agent orchestration writeups, and parallel debugging workflow commentary, each tied to the sections it would refresh.

**Retained seed evidence.** All three labeled query rows with their official-docs, repository, and release-notes targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | parallel agent dispatch patterns official documentation best practices |
| `github_repository_query_phrase` | parallel agent dispatch patterns GitHub repository examples |
| `release_notes_query_phrase` | parallel agent dispatch patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide how statements in this reference must be labeled so readers know what each claim rests on and how far its evidence reaches. The seed notes define the three labels but ignore this file's specific hazards, a single-source evidence base presented through two identical paths and a dated single-session impact claim that reads like a measured benchmark.

**Recommended default and causal basis.** Label per claim, mark the session numbers as single-instance evidence, and keep the three external URLs as unretrieved adjacent candidates. Downstream confidence calibrates on these labels, and the three-for-one speed claim quoted without its one-session provenance overstates what the skill demonstrated.

**Operating conditions and assumptions.** Labels stay stable corpus-wide and every combined-inference clause names the inputs it merges. The notes govern labeling in this reference and its reuses, not source ranking, which the hierarchy owns.

**Failure boundary and alternatives.** Labels applied per section rather than per claim let one labeled sentence launder its unlabeled neighbors. Bounded alternatives and recoveries: an explicit anecdote tag for single-session numbers, inline labels parenthetically on quantitative claims, or claim-to-label indexing during verification.

**Counterexample, gotchas, and operational comparison.** Packet and prompt reuse strips labels mechanically, so the speed claim needs its one-session context embedded in the same sentence. Good: the four pattern steps cited as local facts from the skill. Bad: quoting zero conflicts as the pattern's measured reliability. Borderline: the attention-based scale advice carried as combined inference with its extension note.

**Verification, evidence, and uncertainty.** Sample load-bearing claims, confirm correct labels, and verify quantitative claims carry the single-session qualifier. The three seed definitions match the corpus-wide label vocabulary and the dated example grounds the anecdote rule. Label durability through packet reuse and prompt quotation is unaudited, so leakage risk remains an assumption.

**Second-order consequence.** This theme's evidence has a sample-size hazard, every quantitative claim in the corpus traces to a single 2025-10-03 session, so the numbers are illustrations of the pattern, not measurements of it.

**Revision decision.** Add rules marking the impact numbers as one dated session's anecdote, the duplicate paths as one source, and the scale and recursion advice as inference beyond the skill.

**Retained seed evidence.** All three label definitions, local fact, external fact, and combined inference, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
