# Systematic Debugging Method Patterns

**Decision supported.** This section helps decide how to frame a discipline whose subject is resisting one's own shortcuts. The seed no seed line states what this theme's source really is, a 296-line pressure-hardened debugging discipline whose core is the Iron Law, no fixes without root cause investigation first, enforced through four gated phases, root cause investigation, pattern analysis, hypothesis and testing, implementation, shipped with three companion technique files, backward tracing, defense-in-depth, condition-based waiting.

**Recommended default and causal basis.** Treat the Iron Law as the theme's non-negotiable center and everything else as machinery serving it. The skill exists because random fixes waste time and create new bugs, its own opening claim, and every structural element, gates, red flags, rationalization tables, exists to resist the moment when guessing feels faster than investigating.

**Operating conditions and assumptions.** Both byte-identical copies remain at their mapped paths. This reference covers the debugging method corpus, test-driven development and verification-before-completion are named related skills with their own themes.

**Failure boundary and alternatives.** Reading it as a checklist misses that it is primarily an anti-rationalization device, half its text anticipates the excuses an agent under pressure will produce and pre-refutes them. Bounded alternatives and recoveries: the corpus's TDD and verification themes for the phases this skill explicitly delegates.

**Counterexample, gotchas, and operational comparison.** The skill's numeric impact claims, 95 percent versus 40 percent first-time fix rate, 15 to 30 minutes versus 2 to 3 hours, come from its author's own debugging sessions, motivating anecdote rather than measured study. Good: citing the Iron Law with its phase-gate enforcement mechanism. Bad: summarizing the skill as read errors carefully and test your fix. Borderline: quoting the 95 percent no-root-cause claim, real content, flag it as the author's estimate.

**Verification, evidence, and uncertainty.** Confirm the Iron Law block and four phase headings before structural claims. Both copies and all companion files read in full this session. The upstream CLAUDE.md the log says it was extracted from is not in this corpus.

**Second-order consequence.** The skill's creation log documents its manufacture, extracted from a personal CLAUDE.md, condensed to principles, then bulletproofed with pressure-test scenarios that simulate a manager demanding a fix during a 15,000-dollar-per-minute outage, making it one of the corpus's few sources whose own hardening process is part of the evidence.

**Revision decision.** Open with the Iron Law, the four-phase gate structure, and the pressure-resistance design intent recorded in the skill's own creation log.

**Retained seed evidence.** The exact theme title and framing remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide what the effective evidence set for this theme actually is. The seed two local rows list what checksum comparison shows to be one document twice, md5 3a08f3330fce34e3b2104e7d97f64af0 at both the archive path and the live claude-skills path, so the effective local evidence is a single 296-line skill plus its seven-file companion directory, which the mapping omits entirely.

**Recommended default and causal basis.** Cite the live path as primary, note the archive twin as corroborating the freeze, and cite companions by filename. The corpus sweep mapped SKILL.md entrypoints, but this skill explicitly delegates depth to sibling files, see root-cause-tracing.md in this directory, making the unmapped companions load-bearing evidence rather than optional context.

**Operating conditions and assumptions.** The checksum equality holds, divergence between copies would be a corpus-integrity event worth investigating. Provenance for this theme's claims, the three external URLs stayed unretrieved and confer nothing.

**Failure boundary and alternatives.** Synthesizing from the mapped rows alone would miss the tracing walkthrough, the four validation layers, the polling implementation, and the bisection script, most of the theme's concrete technique. Bounded alternatives and recoveries: retrieving the named upstream CLAUDE.md, impossible locally, it lives outside the corpus.

**Counterexample, gotchas, and operational comparison.** The companion pressure-test files are evaluation harnesses, not guidance, quoting their scenario text as debugging advice would invert their purpose. Good: citing defense-in-depth layers to defense-in-depth.md. Bad: counting the two identical copies as independent corroboration. Borderline: citing CREATION-LOG.md's extraction decisions as skill guidance, it is meta-evidence about design, label it so.

**Verification, evidence, and uncertainty.** Re-run the md5 comparison at each audit before duplication claims. Checksum equality and full companion reads from this session. Which copy future sweeps will treat as canonical if they ever diverge.

**Second-order consequence.** The live and archive copies being byte-identical dates the skill as stable across at least one archive cycle, and the creation log inside the directory names its upstream, a personal CLAUDE.md, giving this theme a rare complete provenance chain, upstream named, extraction decisions recorded, product frozen twice.

**Revision decision.** Annotate the duplication as one effective source and extend the evidence inventory to the companion files with their line counts and roles.

**Retained seed evidence.** The two local rows and three external rows with their column values remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/superpowers/systematic-debugging/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/superpowers/systematic-debugging/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | external_research_sourced_fact | primary agent instruction context model |
| https://docs.github.com/actions | external_research_source_material | external_research_sourced_fact | verification and automation model |
| https://agents.md/ | external_research_source_material | external_research_sourced_fact | general agent instruction format |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which debugging patterns deserve default-tier adoption on this evidence. The seed three corpus-process rows stand where the source's own hierarchy is explicit, the Iron Law outranks everything as the single gating rule, then the four-phase sequence as its enforcement structure, then backward tracing to the original trigger as the core investigative move, then single-hypothesis minimal testing, then the three-strikes architecture rule, three failed fixes mean question the pattern, not attempt a fourth.

**Recommended default and causal basis.** Adopt the Iron Law and phase gates unconditionally and the companion techniques as the situation triggers them. Each pattern exists to block a specific shortcut, the Iron Law blocks fix-first instinct, phase gates block skipping, backward tracing blocks symptom patching, single hypothesis blocks shotgun fixes, and three-strikes blocks infinite thrash.

**Operating conditions and assumptions.** Ranking reflects this skill's design, not a survey of debugging literature. Ranking the source's debugging patterns, corpus-process patterns rank in the seed rows.

**Failure boundary and alternatives.** Ranking by frequency of use would invert the design, the three-strikes rule fires rarely but prevents the costliest failure mode, architectural denial disguised as persistence. Bounded alternatives and recoveries: the seed's process-tier scoreboard for corpus workflow ranking.

**Counterexample, gotchas, and operational comparison.** The most tempting demotion is the phase-gate rule for simple bugs, which the skill pre-refutes twice, simple issues have root causes too and the process is fast for simple bugs. Good: ranking the Iron Law first with its gate mechanism cited. Bad: ranking condition-based waiting top because it has the most code. Borderline: ranking the bisection script high, niche trigger, decisive when test pollution strikes.

**Verification, evidence, and uncertainty.** Spot-check each ranked pattern against its skill section at audit. The full skill and companion reads this session. Real-world firing frequency of each pattern is not recorded in the source.

**Second-order consequence.** The patterns rank by what they protect against rather than what they produce, the skill is organized as a defense stack where each layer catches the failure the previous layer's bypass would cause, mirroring exactly the defense-in-depth doctrine its own companion file teaches for code.

**Revision decision.** Present the shortcut-blocking hierarchy with each pattern's targeted rationalization quoted from the red-flags and excuse tables.

**Retained seed evidence.** The three scored seed rows with tier labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `systematic_debugging_method_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local systematic debugging material before synthesizing method patterns recommendations. |
| `systematic_debugging_method_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `systematic_debugging_method_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide whether investigation discipline may ever yield to urgency. The seed generic corpus formulas stand where the source states its thesis in one line, symptom fixes are failure, with the corollary that systematic debugging is faster than guess-and-check thrashing even under emergency pressure, the exact claim its pressure tests exist to defend.

**Recommended default and causal basis.** Under any pressure, run Phase 1 first, the skill holds that the systematic path is also the fast path. Guessing feels faster because its first step is immediate, but the skill's arithmetic says otherwise, 15 to 30 minutes systematic versus 2 to 3 hours thrashing, because unverified fixes multiply into new bugs and repeated attempts.

**Operating conditions and assumptions.** The issue is technical with a traceable cause, the skill's no-root-cause clause handles the truly environmental residue. The thesis governs debugging conduct, its speed numbers are author-reported session anecdotes.

**Failure boundary and alternatives.** The thesis dies by exception-granting, each just-this-once emergency bypass reestablishes guessing as the norm, which is why the skill words its pressure clauses absolutely, use this especially when under time pressure. Bounded alternatives and recoveries: quick-patch-now-investigate-later doctrine, the exact first entry in the skill's red-flag list.

**Counterexample, gotchas, and operational comparison.** The 95 percent line cuts both ways, most no-root-cause conclusions are incomplete investigations, so declaring an issue environmental requires having completed the process, not abandoned it. Good: an on-call engineer instrumenting layer boundaries during an outage before touching config. Bad: adding a retry because a similar service needed one last week. Borderline: a genuine one-line typo fix from a clear error message, still Phase 1, just a fast one, the error was read carefully.

**Verification, evidence, and uncertainty.** Audit incident writeups for investigation-before-fix ordering. The thesis lines, excuse table, and pressure scenarios read this session. The speed ratio generalizes on argument, not on measured data.

**Second-order consequence.** The thesis inverts who the discipline is for, novices guess from ignorance but experienced agents guess from confidence, I see the problem, let me fix it, and the skill's excuse table targets exactly that confident voice, making the discipline most binding precisely when the debugger feels most sure.

**Revision decision.** State the thesis with its speed rationale and the pressure-test scenarios as the designed counterweight to emergency rationalization.

**Retained seed evidence.** The three labeled thesis statements remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `systematic_debugging_method_patterns` contains 2 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Systematic Debugging Method Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which file answers which kind of debugging question. The seed heading signals stop at Phase 1 while the working map is the whole directory, SKILL.md as the discipline spine, root-cause-tracing.md for the backward-trace walkthrough with its five-level worked example, defense-in-depth.md for the four validation layers, condition-based-waiting.md for flaky-test polling patterns, find-polluter.sh as runnable bisection, CREATION-LOG.md as design provenance, and three pressure tests as evaluation harnesses.

**Recommended default and causal basis.** Enter at SKILL.md, follow its pointers for depth, and touch pressure tests only when evaluating adherence. The skill was deliberately factored, the spine keeps rules terse for pressure moments while companions carry depth, so navigation means entering at the spine and following its explicit see-this-file pointers.

**Operating conditions and assumptions.** The directory structure survives future sweeps intact at either mapped path. Navigation of this theme's nine-file directory, duplicated identically at two paths.

**Failure boundary and alternatives.** Spine-only reading yields rules without technique, an agent knows to trace backward but lacks the instrumentation recipe, stack capture, console.error over suppressed loggers, grep on test output, that makes tracing executable. Bounded alternatives and recoveries: treating the SKILL.md alone as the theme, refuted by its own delegation pointers.

**Counterexample, gotchas, and operational comparison.** Find-polluter.sh is the directory's only executable and assumes a JS test layout in its usage example, its bisection logic generalizes but the invocation does not. Good: answering a flaky-test question from condition-based-waiting.md's patterns table. Bad: answering it from the spine's one-line mention alone. Borderline: adapting find-polluter.sh to pytest, sound reuse, note the adaptation.

**Verification, evidence, and uncertainty.** Trace synthesis claims to file and section at review. All nine files read in full this session. None about structure, the directory was enumerated and read wholesale.

**Second-order consequence.** The directory separates three document species, normative rules in the spine, executable technique in companions and the script, and evaluative scenarios in the pressure tests, and correct usage differs per species, obey the first, apply the second, and never quote the third as guidance.

**Revision decision.** Annotate the map with all nine files, their line counts, roles, and the spine-to-companion pointer structure.

**Retained seed evidence.** The two local source rows with title, heading signals, and usage role remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/superpowers/systematic-debugging/SKILL.md | systematic-debugging | Systematic Debugging; Overview; The Iron Law; When to Use; The Four Phases; Phase 1: Root Cause Investigation | skill entrypoint or reusable agent prompt |
| claude-skills/superpowers/systematic-debugging/SKILL.md | systematic-debugging | Systematic Debugging; Overview; The Iron Law; When to Use; The Four Phases; Phase 1: Root Cause Investigation | skill entrypoint or reusable agent prompt |

## External Research Source Map

**Decision supported.** This section helps decide which external dependencies this theme actually carries. The seed three inherited agent-format anchors stand while the theme's real external surface is small and behavioral, the upstream CLAUDE.md named by the creation log, the superpowers skill ecosystem whose test-driven-development and verification-before-completion skills the spine cross-references, and the TypeScript-and-bash tooling idioms its examples assume.

**Recommended default and causal basis.** Reuse the conduct rules without currency caveats and the cross-skill pointers with an ecosystem-drift flag. A self-contained discipline needs little external grounding, its claims are about conduct rather than platform behavior, so the external rows matter mainly for tracing the skill's lineage and its sibling-skill contracts.

**Operating conditions and assumptions.** Sibling skills remain resolvable wherever this skill is deployed. External anchors for lineage and cross-skill contracts, all URLs stayed unretrieved this evolution.

**Failure boundary and alternatives.** The volatile-claim risk here is not version drift but ecosystem drift, the superpowers namespace and its skill names could be renamed or retired, silently breaking the spine's related-skills pointers. Bounded alternatives and recoveries: the seed's inherited AGENTS.md and Actions anchors, retained for ecosystem context.

**Counterexample, gotchas, and operational comparison.** The impact numbers look like external benchmarks but are internal anecdotes, 1847 tests passed and 60 to 100 percent pass rates describe one author's one session. Good: flagging superpowers:test-driven-development as a resolvable-or-not dependency at deploy time. Bad: citing the 40 percent faster test-suite claim as a published benchmark. Borderline: treating console.error-over-logger as universal, it is a JS-test-runner observation that generalizes with judgment.

**Verification, evidence, and uncertainty.** Check sibling-skill resolvability wherever the skill is installed. Zero fetches this assignment and the cross-reference inventory from the spine. The upstream CLAUDE.md's current contents are unknowable locally.

**Second-order consequence.** Unlike platform themes whose external claims decay at release cadence, this theme's guidance is almost entirely evergreen conduct rules, the only perishables are its two dated session anecdotes from 2025-10-03 and its sibling-skill names, giving it one of the corpus's slowest decay profiles.

**Revision decision.** Keep the inherited rows and add the named upstream and sibling-skill dependencies as archive-quoted references.

**Retained seed evidence.** All three external rows with their boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | primary agent instruction context model | external_research_sourced_fact |
| https://docs.github.com/actions | GitHub Actions documentation | verification and automation model | external_research_sourced_fact |
| https://agents.md/ | AGENTS.md open format | general agent instruction format | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which thoughts and signals must trigger an immediate process stop. The seed three corpus-process rows stand where the source is itself mostly an anti-pattern registry, eleven red-flag thoughts including quick fix for now, just try changing X, and one more fix attempt, an eight-row excuse-versus-reality table, five human-partner signals like is that not happening and stop guessing, and the structural anti-patterns, symptom fixing, multi-fix bundling, skipping the failing test, fix stacking after failure.

**Recommended default and causal basis.** On matching any registry entry from any channel, stop immediately and re-enter Phase 1, the response is uniform by design. The skill was built by cataloging how debugging actually goes wrong under pressure, then wiring a stop condition to each observed failure thought, so its registry is keyed to internal monologue rather than code smells.

**Operating conditions and assumptions.** The agent honestly surfaces its own monologue, the channel the registry most depends on. Debugging conduct failures from the source, corpus-process failures stay in the seed rows.

**Failure boundary and alternatives.** The registry only works if consulted at the moment of temptation, an agent that reads it once and trusts memory will reproduce the exact thoughts it lists, they are listed because they feel reasonable. Bounded alternatives and recoveries: post-incident review taxonomies, downstream of what this registry interrupts in real time.

**Counterexample, gotchas, and operational comparison.** The most dangerous entry is the confident one, I see the problem, let me fix it, because it does not feel like a rationalization, the reality column answers that seeing symptoms is not understanding root cause. Good: halting on catching oneself about to bundle three changes into one test run. Bad: continuing after a partner asks is that not happening. Borderline: a documented two-tick timeout in a timing test, the waiting companion explicitly permits it with a comment stating why.

**Verification, evidence, and uncertainty.** Check incident logs for stop-and-return events matched to registry entries. The red-flag, excuse, and signal inventories read this session. How reliably agents notice their own listed thoughts in the moment.

**Second-order consequence.** The partner-signal list is the registry's most novel channel, it treats the human's frustrated questions, will it show us, we're stuck, as telemetry indicating the agent has drifted into guessing, externalizing failure detection to the collaborator when self-monitoring has already failed.

**Revision decision.** Add the native registry organized by detection channel, self-observed thoughts, partner signals, and structural violations, each with its mandated response, stop and return to Phase 1.

**Retained seed evidence.** The three seed process rows with their detection signals remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide what evidence must exist before proposing, applying, and accepting a fix. The seed document verifier text stands where the source defines conduct gates, Phase 1 gates any fix proposal on completed investigation, Phase 4 gates any fix on a failing test case created first, fix acceptance gates on the test passing plus no other tests broken plus the issue actually resolved, and the three-strikes counter gates a fourth attempt on an architectural discussion with the human partner.

**Recommended default and causal basis.** Treat each gate's artifact, trace notes, failing test, green suite, strike count, as required evidence before the next phase. Each gate converts a judgment call into a checkable precondition, has investigation happened, does a failing test exist, did the counter reach three, which is what makes the discipline enforceable rather than aspirational.

**Operating conditions and assumptions.** A test harness exists, the skill allows one-off scripts where no framework does. Verification gates the source teaches, this document's own structural verification keeps the seed's retained block.

**Failure boundary and alternatives.** The commonest bypass is the test-after promise, I'll write the test after confirming the fix works, which the excuse table refutes, untested fixes don't stick, test first proves it. Bounded alternatives and recoveries: the corpus verifier command in the seed's retained block for this document's own checks.

**Counterexample, gotchas, and operational comparison.** The no-other-tests-broken clause makes the whole suite part of the gate, a fix that greens its own test while reddening another is a failed gate, not a partial success. Good: a fix PR containing the failing-test commit before the fix commit. Bad: a manually-verified fix with the test promised later. Borderline: a one-off reproduction script where no framework exists, explicitly permitted, keep the script.

**Verification, evidence, and uncertainty.** Sample fixes for gate artifacts in order at review. The phase-gate and companion testing rules read this session. Gate compliance costs in very small repositories are unmeasured.

**Second-order consequence.** The gates are ordered so each produces the evidence the next consumes, investigation yields the root cause the hypothesis names, the hypothesis yields the failing test, the test yields the pass-fail verdict, and the verdict feeds the strike counter, a pipeline where skipping any stage starves every later gate of its input.

**Revision decision.** Inventory the four gates with their precondition, evidence artifact, and bypass excuse, plus the layer-bypass testing rule from defense-in-depth, try to defeat each validation layer and verify the next catches it.

**Retained seed evidence.** The seed's document verifier command block remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide when a working agent must switch from building to investigating. The seed four generic bullets stand where the skill defines its own dispatch, its description fires on any bug, test failure, or unexpected behavior before proposing fixes, its when-to-use list covers production bugs through build failures, and its especially-when list inverts intuition, invoke hardest under time pressure, after failed fixes, and when a quick fix seems obvious.

**Recommended default and causal basis.** Enter the process on any technical anomaly before forming a fix opinion, with extra strictness when skipping feels justified. The trigger is deliberately broad and early, before proposing fixes, because the skill's value is front-loaded, once a first guess-fix ships, the pattern it warns against has already started.

**Operating conditions and assumptions.** The agent notices the anomaly before acting, dispatch cannot fire on unexamined output. When agents enter this discipline, sibling skills own test authorship and completion verification.

**Failure boundary and alternatives.** The natural mis-dispatch is severity-scaling, invoking the process only for hard bugs, which the don't-skip list refutes item by item, simple issues, hurries, and impatient managers are all named non-exemptions. Bounded alternatives and recoveries: the corpus's verification theme when the question is whether work is done rather than why it broke.

**Counterexample, gotchas, and operational comparison.** The trigger includes unexpected behavior without an error, silent wrong results dispatch the process too, waiting for a stack trace is already a narrowed reading. Good: halting feature work to run Phase 1 on a flaky CI job. Bad: patching a prod timeout under manager pressure because it worked elsewhere. Borderline: a cosmetic log typo, still an anomaly, Phase 1 is one glance at the format string.

**Verification, evidence, and uncertainty.** Sample incident starts for dispatch-before-first-fix ordering. The description, trigger lists, and pressure scenarios read this session. Dispatch reliability when anomalies are subtle is untested here.

**Second-order consequence.** The especially-when list is a pressure inversion, every condition that psychologically argues for skipping the process is listed as a reason to apply it more strictly, encoding the skill's core bet that temptation strength predicts guessing damage.

**Revision decision.** Recast the section around the source's trigger taxonomy, the six issue types, the five especially-when amplifiers, the three don't-skip refusals.

**Retained seed evidence.** The four seed usage bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide what the disciplined path concretely looks like at the worst moment. The seed one generic engineer stands where the source scripts a sharply specific journey, the on-call agent five minutes into a full outage, manager demanding a fix now, a plausible two-minute patch remembered from last week, and the skill requiring the counterintuitive move, instrument the component boundaries first, exactly the scenario its pressure-test files stage with dollar figures attached.

**Recommended default and causal basis.** Narrate the investigation state to stakeholders while it runs rather than promising an untested fix time. The journey was chosen adversarially, the skill's authors built the test around the moment the discipline is most likely to break, because a rule that survives only calm conditions is not the rule they needed.

**Operating conditions and assumptions.** The agent has instrumentation access to the failing path, the multi-layer echo recipe assumes it. Journeys through debugging conduct, journeys through corpus tooling belong to process themes.

**Failure boundary and alternatives.** The journey's failure branch is scripted too, the remembered retry gets applied, masks the symptom or fails, a second and third fix follow, and three strikes later the real problem surfaces as architectural, hours and trust spent. Bounded alternatives and recoveries: the calm-workday journey, same phases with lighter narration, pressure just makes the gates visible.

**Counterexample, gotchas, and operational comparison.** The pressure tests forbid hypothetical hedging, you must choose and act, adherence is measured on the decision taken, not on knowing the right answer abstractly. Good: four echo probes across workflow, build, signing, and execution finding the broken layer in one run. Bad: shipping the remembered retry then diagnosing its failure in production. Borderline: applying a reversible mitigation like a traffic drain while Phase 1 runs, containment differs from fixing, keep the investigation gate intact.

**Verification, evidence, and uncertainty.** Review incident timelines for evidence-first ordering under pressure. The multi-layer example and pressure scenarios read this session. The journey's revenue arithmetic is illustrative staging, not field data.

**Second-order consequence.** The journey embeds a communication move often missed, the systematic path gives the agent something honest to tell the demanding manager at each step, evidence gathered so far and the failing layer once found, whereas the guessing path offers only maybe this works, so the discipline also repairs the incident's human channel.

**Revision decision.** Recast the scenario as the outage journey with its decision fork, the two-minute patch versus layered evidence gathering, and the skill's claim that the second path is also the faster one.

**Retained seed evidence.** The role, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The system designer or debugger is starting from a design choice, failure symptom, dependency map, or unclear boundary and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `systematic_debugging_method_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the evidence, option set, tradeoff, and validation probe before changing structure.
Reference opening trigger: Open this file when the task mentions systematic debugging method patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide which side wins each recurring debugging trade-off and why. The seed template rows skip the trade-offs the source actually adjudicates, speed of first action versus time to resolution, fix at symptom site versus trace to source, single minimal change versus batched fixes, one validation point versus four defense layers, arbitrary sleep versus condition polling, and persist with fixes versus question the architecture at three strikes.

**Recommended default and causal basis.** When a local shortcut and a systematic path disagree, take the systematic side and log why if deviating. Each trade-off pits a locally cheaper move against a globally cheaper one, and the skill consistently rules for the global side with a stated mechanism, batched fixes cannot be isolated, symptom fixes recur, single validations get bypassed.

**Operating conditions and assumptions.** The three-strikes threshold and layer counts are the source's defaults, teams may tune numbers but not directions. Trade-off structure the source teaches, corpus-process trade-offs stay in the seed rows.

**Failure boundary and alternatives.** The trade-offs are lost when framed as style preferences, the source frames them as arithmetic, thrashing hours versus process minutes, recurring bugs versus structurally impossible ones. Bounded alternatives and recoveries: severity-scaled process, applying rigor only to big bugs, rejected by the simple-bugs-have-root-causes clause.

**Counterexample, gotchas, and operational comparison.** Condition polling has its own carve-out, genuinely timing-dependent behavior like debounce intervals may use documented timeouts, the ruling bans guessed delays, not time itself. Good: refusing a bundled three-change fix in favor of sequenced single changes. Bad: a fourth fix attempt to avoid an awkward architecture conversation. Borderline: fixing at an intermediate layer when the true source is third-party code, trace as far as reachable, then guard the boundary and document the residue.

**Verification, evidence, and uncertainty.** Review fix history for single-change sequencing and strike counting. The excuse table, tracing doctrine, and layer rationale read this session. Optimal strike thresholds beyond the default three are unstudied.

**Second-order consequence.** All six rulings share one generator, distrust of unverified locality, the near fix, the single check, the guessed delay all assume the visible spot is the whole story, and the skill's rulings systematically pay upfront cost to escape that assumption, which is why they cohere as one doctrine rather than six opinions.

**Revision decision.** Add the six trade-off rows with each side's cost profile and the skill's ruling plus its stated mechanism.

**Retained seed evidence.** The adopt, adapt, avoid, and cost-of-being-wrong rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the systematic debugging method patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong systematic debugging method patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which file's wording wins when directory contents overlap. The seed role labels rank two byte-identical copies while the real precedence structure is inside the directory, the spine's normative rules outrank companion elaborations where they overlap, companions outrank the spine's quick versions for technique detail, the creation log explains but never overrides, and pressure tests rank as evaluation fixtures with no guidance authority at all.

**Recommended default and causal basis.** Resolve overlaps by speech act first, then by specificity within the tier. The skill's own pointers establish the ranking, the spine says see root-cause-tracing.md for the complete technique, delegating depth downward while keeping rules at the top.

**Operating conditions and assumptions.** The directory's pointer structure stays intact through future sweeps. Precedence within this theme's one effective source directory, cross-theme precedence belongs to the corpus hierarchy.

**Failure boundary and alternatives.** Quoting the spine's quick version where a companion holds the full recipe undersources technique, while elevating a pressure-test scenario line into doctrine fabricates rules the skill never made. Bounded alternatives and recoveries: flat ranking of all nine files, which would let a fixture's staged bad advice tie with the Iron Law.

**Counterexample, gotchas, and operational comparison.** The two copies create a trivial cross-path tie, broken by citing the live path as primary per the source-mapping ruling, never by treating the twins as disagreeing. Good: citing the polling implementation from condition-based-waiting.md over the spine's mention. Bad: quoting test-pressure-1's tempting retry suggestion as skill guidance. Borderline: citing the creation log's extraction rationale to interpret an ambiguous rule, legitimate interpretive evidence, not a rule itself.

**Verification, evidence, and uncertainty.** Test citation tiers against the speech-act rule at audit. The pointer lines and full directory read this session. None material, the directory is small enough for total inspection.

**Second-order consequence.** The tiers correspond to document speech acts, commands, recipes, history, and tests, so precedence resolves by asking what kind of statement is needed, a must comes from the spine, a how from a companion, a why from the log, and nothing citable from the fixtures.

**Revision decision.** State the four-tier internal ranking, normative spine, technical companions, explanatory log, evaluative fixtures, with the pointer lines as its textual basis.

**Retained seed evidence.** The hierarchy rows and the classification vocabulary remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/superpowers/systematic-debugging/SKILL.md | canonical primary source | Systematic Debugging; Overview; The Iron Law | What guidance, warning, or example should this source contribute to Systematic Debugging Method Patterns? |
| claude-skills/superpowers/systematic-debugging/SKILL.md | supporting context source | Systematic Debugging; Overview; The Iron Law | What guidance, warning, or example should this source contribute to Systematic Debugging Method Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what standing record makes phase-gate compliance auditable. The seed generic worked-example artifact misses this theme's natural object, a debugging session ledger, one running record per incident holding the phase log with entry and exit evidence, the trace chain from symptom to original trigger, the single hypothesis with its minimal test, the strike counter, and the final root-cause-versus-symptom disposition.

**Recommended default and causal basis.** Open a ledger at dispatch, fill parts as phases complete, and close with the disposition and any residual monitoring added. The skill's gates all consume evidence artifacts, investigation notes, failing tests, verdicts, strike counts, and a single ledger gives those artifacts a place to exist, turning phase compliance from claimed to inspectable.

**Operating conditions and assumptions.** Incidents are discrete enough to ledger, continuous firefighting needs the discipline even more but resists the paperwork. One ledger per debugging incident, extensible with team conventions for storage and review.

**Failure boundary and alternatives.** Without the ledger, phase completion is self-asserted memory, and the red-flag thoughts the skill lists are exactly the voices that will assert it falsely. Bounded alternatives and recoveries: leaving evidence scattered across terminal history and chat, recoverable in principle, ungated in practice.

**Counterexample, gotchas, and operational comparison.** The ledger must record failed hypotheses, not just the winning one, erasing failures resets the strike counter that the architecture rule depends on. Good: a ledger showing two failed hypotheses, a strike-two pause, and a source-level fix with its failing test linked. Bad: a ledger written retroactively after the fix shipped. Borderline: a two-line ledger for a typo fix, proportionate, the form scales down with the incident.

**Verification, evidence, and uncertainty.** Check closed incidents for ledgers with all five parts evidenced. The gate-artifact mapping assembled from the full read this session. Ledger discipline under real outage pressure is behavioral and unproven.

**Second-order consequence.** The ledger doubles as the architecture-question trigger, a visible strike counter makes the third failure undeniable at the moment it happens, converting the skill's hardest rule, stop and question fundamentals, from a memory test into a form field.

**Revision decision.** Define the artifact as the five-part session ledger with each part mapped to the gate it evidences.

**Retained seed evidence.** The artifact field rows with completion rules and evidence hints remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: symptom-to-hypothesis loop with repro minimization, probes, and confidence scoring.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Systematic Debugging Method Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which exercises build tracing fluency fastest on this evidence. The seed abstract usage lines stand where the source carries a complete worked case, the empty-projectDir incident, a git init landing in the source tree, traced five levels from symptom through WorktreeManager, Session, and test setup to a top-level variable read before beforeEach, fixed at source with a throwing getter, then hardened with all four defense layers, with 1847 tests passing after.

**Recommended default and causal basis.** Certify understanding by reproducing the five-level trace and naming why each intermediate frame is the wrong fix site. The case exercises every companion at once, backward tracing finds the trigger, defense-in-depth makes recurrence structurally impossible, and the fix-at-source ruling shows why patching the git call would have merely relocated the bug.

**Operating conditions and assumptions.** Drills start from the symptom line only, reading the answer first collapses the exercise. Teaching this theme's method, the case is TypeScript-flavored but its moves are language-neutral.

**Failure boundary and alternatives.** Studying rules without the worked case leaves the trace move abstract, the case shows the actual questions asked at each level, what called this, what value was passed, where did the empty string originate. Bounded alternatives and recoveries: live incidents as training, richer and unschedulable, the drill is always available.

**Counterexample, gotchas, and operational comparison.** The case's four defense layers each caught real bypasses during its own testing, per the companion's key insight, so a drill answer proposing only entry validation is incomplete against the source's own record. Good: a drill answer tracing to the premature tempDir read and proposing the getter plus layers. Bad: a drill answer adding a null check at the git call and stopping. Borderline: proposing the getter without defense layers, root cause fixed, hardening doctrine missed.

**Verification, evidence, and uncertainty.** Grade drill answers on trace depth and fix-site reasoning, not code style. The worked case read across both companions this session. Transfer from the drill to unfamiliar stacks is unmeasured.

**Second-order consequence.** The case's punchline is that the fix touched none of the five frames where the bug was visible, the throwing getter lives in test scaffolding upstream of them all, concretely demonstrating the skill's least intuitive claim, that the right fix is often far from every place the error appears.

**Revision decision.** Anchor the section on the projectDir case as the canonical drill, re-derive the trace chain from the symptom alone, then compare against the file's answer, adding the flaky-test case from the waiting companion as the second drill.

**Retained seed evidence.** The good, bad, and borderline seed lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Systematic Debugging Method Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Systematic Debugging Method Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Systematic Debugging Method Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which numbers show the discipline is working or eroding. The seed compile-centric indicator misses the source's own outcome vocabulary, first-time fix rate, time-to-fix versus thrash time, new bugs introduced by fixes, strike counts per incident, test pass-rate recovery, and suite-time change, the measures its impact notes and session records actually cite.

**Recommended default and causal basis.** Log the six measures from each ledger and treat strike-count drift as the earliest alarm. The discipline's thesis is an empirical claim, systematic is faster and cleaner, so its adoption should be scored on exactly the quantities the thesis predicts, fix-rate up, thrash down, regression near zero.

**Operating conditions and assumptions.** Incidents are ledgered consistently enough for the series to mean something. Outcome measures for debugging conduct plus this node's own evidence series, corpus-process metrics stay in the seed lines.

**Failure boundary and alternatives.** Without measurement the discipline's cost is visible, slower first action, while its benefit is invisible, the thrashing that did not happen, biasing teams to abandon it during exactly the pressure periods it serves. Bounded alternatives and recoveries: the evaluation theme's rubric metrics for skill artifacts rather than debugging conduct.

**Counterexample, gotchas, and operational comparison.** The source's own numbers, 95 versus 40 percent, 15 to 30 minutes, are its author's anecdotes and serve as motivation, a team's baseline must be its own measured history, not these figures. Good: a quarterly review showing first-time fix rate climbing after ledger adoption. Bad: declaring success by quoting the skill's 95 percent figure as one's own. Borderline: counting a documented-timeout flaky fix as a win, legitimate if the condition-first rule was followed.

**Verification, evidence, and uncertainty.** Confirm ledger fields feed the six series at each review cycle. The impact notes and session records read across the directory this session. No baseline exists in this corpus, the loop starts unprimed.

**Second-order consequence.** The strike counter is the leading indicator among the six, rising strike averages signal either eroding investigation quality or an aging architecture generating unfixable symptom bugs, both worth catching quarters before fix-rate collapse makes them undeniable.

**Revision decision.** Adopt the source's six measures as the loop, tracked per incident via the session ledger and reviewed at whatever cadence incidents accumulate.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: the chosen boundary reduces blast radius or uncertainty measured by explicit probes.
Failure signal: the reference jumps to a pattern before proving the problem shape.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide what must be confirmed before this synthesis is declared faithful. The seed shape items never audit this theme's distinctive claims, the byte-identical duplication of the two mapped copies, the nine-file directory inventory with the spine's delegation pointers intact, the four-tier internal precedence, the anecdote labeling on all impact numbers, and the fixture quarantine keeping pressure-test text out of guidance.

**Recommended default and causal basis.** Run all distinctive checks wholesale at each audit cycle and date the results. The theme's synthesis leans on structural facts about a small directory, if a companion vanishes or the copies diverge, citations break silently unless the audit checks the structure itself.

**Operating conditions and assumptions.** The directory remains under a thousand lines, growth past that revisits the regime choice. Auditing this reference against its nine-file source directory, read wholesale this session.

**Failure boundary and alternatives.** A shape-only audit passes while an impact anecdote circulates as a benchmark or a fixture line surfaces as doctrine, the two mislabelings this theme is most prone to. Bounded alternatives and recoveries: sampled auditing, unjustified overhead at this scale.

**Counterexample, gotchas, and operational comparison.** The md5 check must cover both paths, a sweep updating one copy but not the other would silently break the one-effective-source premise this whole synthesis rests on. Good: an audit logging checksum equality, nine files present, pointers resolving, labels intact. Bad: declaring fidelity from seed-shape checks alone. Borderline: skipping the fixture quarantine check because no reuse occurred, cheap enough to run anyway.

**Verification, evidence, and uncertainty.** Execute the distinctive items and date each result in the audit record. The claim structure of every distinctive statement in this document. Future sweep behavior on duplicated paths is the main structural unknown.

**Second-order consequence.** At 962 total lines across nine files this theme sits in the wholesale-audit regime, every check can re-read its target completely in minutes, so unlike compendium themes no sampling strategy is needed and audit findings here are exhaustive rather than statistical.

**Revision decision.** Add the distinctive items, md5 equality check, nine-file inventory, pointer integrity, anecdote labels, and fixture quarantine, to the audit list.

**Retained seed evidence.** All seven seed checklist bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Systematic Debugging Method Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide where to send a question arriving at the debugging theme. The seed token-split rows point nowhere while this theme's borders are drawn by the source itself, failing-test authorship routes to the test-driven development theme the spine names for Phase 4 step 1, done-ness checking routes to the verification-before-completion theme it also names, system-level failure design routes to the system design theme's fault-tolerance doctrine, and skill-format questions route to the skill-development themes.

**Recommended default and causal basis.** Route by the question's activity verb, investigate here, author there, verify there, design there. The skill declares its own seams, delegating test creation and completion verification to sibling skills, so routing follows the source's explicit contracts rather than editorial judgment.

**Operating conditions and assumptions.** The named sibling themes remain evolved and reachable through the corpus routing tables. Sending away what this theme holds only incidentally, destination doctrine is deliberately not restated.

**Failure boundary and alternatives.** Keeping test-authorship questions here duplicates a delegation the source refused, while routing away a root-cause question because it mentions tests loses the theme's core competence. Bounded alternatives and recoveries: for the upstream superpowers ecosystem itself, nothing local, only the archive-quoted names.

**Counterexample, gotchas, and operational comparison.** The condition-based-waiting companion looks like test-authorship content but is diagnostic, it exists to fix flaky tests found during investigation, keep flakiness diagnosis here and new-test style guidance there. Good: forwarding how do I structure this failing test to the TDD theme after Phase 1 completes here. Bad: answering a saga-compensation design question from debugging doctrine. Borderline: a flaky CI job question, starts here for root cause, may end at system design if the cause is architectural.

**Verification, evidence, and uncertainty.** Sample recent answers for activity-verb routing consistency. The spine's related-skills contracts and theme boundaries read this session. Future sweeps may add sibling debugging themes that share this load.

**Second-order consequence.** This theme and the system design theme meet at retry logic from opposite sides, that theme prescribes retries as architecture while this one's worked pressure test stages a retry as the tempting wrong fix, the routing rule that reconciles them is diagnosis before prescription, this theme decides whether a retry treats the root cause, that one decides how to build it if so.

**Revision decision.** Route by activity, why-it-broke stays here, how-to-write-the-failing-test goes to TDD, is-it-actually-done goes to verification, how-systems-should-fail goes to system design.

**Retained seed evidence.** The three seed adjacent-reference lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use dependency, debugging, timeline, or system design references when the inquiry narrows.
Adjacent reference 1: consider the systematic adjacent reference when the current task pivots away from systematic debugging method patterns.
Adjacent reference 2: consider the debugging adjacent reference when the current task pivots away from systematic debugging method patterns.
Adjacent reference 3: consider the method adjacent reference when the current task pivots away from systematic debugging method patterns.

## Workload Model

**Decision supported.** This section helps decide how to budget a theme whose cost is per-incident conduct rather than maintenance. The seed symbol-count boundary misprices this node's work, whose units are the sunk directory read, 962 lines across nine files in well under an hour, per-incident process overhead, minutes of ledger and gate bookkeeping per debugging session, per-audit wholesale checks, minutes, and the drill investment, re-deriving the projectDir trace at under an hour.

**Recommended default and causal basis.** Budget audits as trivial, drills as scheduled capability work, and defend the per-incident toll with the repayment argument when challenged. The theme's cost center is not maintenance but adoption, the discipline charges a small toll on every single incident forever, and the source's whole argument is that the toll is repaid by avoided thrashing within the same incident.

**Operating conditions and assumptions.** Incident volume stays high enough for the toll-repayment arithmetic to accumulate evidence. Budgeting this node's upkeep and the discipline's runtime cost, not the incidents themselves.

**Failure boundary and alternatives.** Accounting the per-incident toll without the avoided-thrash credit makes the discipline look like pure overhead, the exact framing that gets it abandoned under deadline pressure. Bounded alternatives and recoveries: the seed's crate-slice and symbol boundaries, retained as outer limits on any single consultation's scope.

**Counterexample, gotchas, and operational comparison.** The toll is front-loaded within each incident, all investigation before any fix, so cash-flow intuition rebels even when total cost is lower, the model should name this explicitly. Good: a team logging ledger minutes against thrash-hours avoided in the same quarter. Bad: cutting the investigation phase to save minutes on a revenue-down incident. Borderline: skipping the ledger on trivial fixes, acceptable scaling if the phase gates still run.

**Verification, evidence, and uncertainty.** Check audit and adoption records against the four-unit model. The line-count ledger and toll structure from this session's full read. Actual toll-versus-repayment ratios await the metrics loop's data.

**Second-order consequence.** This theme's maintenance is nearly free while its usage cost recurs on every incident, the inverse of compendium themes whose maintenance dominates and usage is cheap lookups, so corpus effort here should flow to adoption support, ledgers and drills, rather than to source-watching.

**Revision decision.** Restate the model in its four units, sunk read, per-incident toll with its claimed repayment, wholesale audit, and drill investment.

**Retained seed evidence.** The workload dimension rows with boundary values remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Systematic Debugging Method Patterns as a general reference operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | idiomatic reference selection and synthesis work where the reference must prevent generic advice and preserve evidence boundaries | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one theme, all mapped local sources, current external evidence when available, and one downstream task review | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Systematic Debugging; Overview; The Iron Law; When to Use; The Four Phases; Phase 1: Root Cause Investigation; Systematic Debugging; Overview; The Iro | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is symptom-to-hypothesis loop with repro minimization, probes, and confidence scoring | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide which invariants must demonstrably hold for this node's claims to stay citable. The seed document-property thresholds stand where this node's invariants should, checksum equality across the two mapped copies, the nine-file inventory with delegation pointers resolving, anecdote labels persisting on every impact number, fixture quarantine holding pressure-test text out of guidance reuse, and phase-order fidelity, no synthesis here ever presenting fix-then-investigate as acceptable.

**Recommended default and causal basis.** Hold all five invariants at wholesale-audit cadence with the phrasing review weighted heaviest. Each invariant guards a distinct corruption, structure drift breaks citations, label loss inflates anecdotes into benchmarks, quarantine breach fabricates doctrine, and phase-order corruption would invert the theme's entire point.

**Operating conditions and assumptions.** The source directory stays stable at both paths and reuse remains observable. Invariants for this node's claims, reliability of debugged systems belongs to their owners.

**Failure boundary and alternatives.** The worst breach is the last, a paraphrase that softens no fixes without investigation into investigate when feasible would circulate under this theme's authority while contradicting its Iron Law. Bounded alternatives and recoveries: fact-only invariants, blind to the ordering corruption that matters most here.

**Counterexample, gotchas, and operational comparison.** The phrasing review must cover this reference's own evolved sections, the synthesis is the likeliest place a softened ordering would first appear. Good: an audit confirming checksums, pointers, labels, quarantine, and Iron Law wording in one pass. Bad: a downstream summary rendering the Iron Law as a strong recommendation. Borderline: a condensed reuse citing phases without gates, acceptable only with a pointer back to the gate rules.

**Verification, evidence, and uncertainty.** Review the five invariant series at each corpus checkpoint with dated evidence. The claim structure established across this document. None about current truth, all five invariants were verified during this evolution.

**Second-order consequence.** Phase-order fidelity is the invariant unique to conduct themes, fact themes guard truth values while this one must guard an ordering, investigation strictly precedes fixing, and orderings corrupt more quietly than facts because every individual sentence can remain true while the sequence inverts.

**Revision decision.** Publish the five invariants with evidence methods, checksum runs, inventory checks, label audits, quarantine scans, and Iron Law phrasing review.

**Retained seed evidence.** All four seed reliability rows with thresholds remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which decay modes need standing probes for a conduct-mandate theme. The seed generic rows miss how this node specifically dies, copy divergence, one mapped path updated while its twin freezes, anecdote inflation, session numbers circulating as measured benchmarks, fixture leakage, pressure-test staging quoted as guidance, and mandate softening, the Iron Law and phase gates paraphrased into suggestions.

**Recommended default and causal basis.** Run the four probes at each audit, weighting the phrasing diff toward the most-summarized claims. All four attack what makes the theme trustworthy, a verified single source, honestly-labeled evidence, quarantined test material, and an uncompromised core mandate.

**Operating conditions and assumptions.** Reuse is observable enough to scan, unobserved reuse defaults probes to fixed cadence. Decay of this node's claims and reuse, debugging failures themselves are the theme's subject, not its failure mode.

**Failure boundary and alternatives.** They compound through reuse, a softened mandate plus an inflated anecdote yields research shows careful debugging is usually faster, so investigate when time permits, authoritative-sounding and doubly wrong. Bounded alternatives and recoveries: quotation-only reuse, immune to softening but unable to adapt the discipline to new contexts.

**Counterexample, gotchas, and operational comparison.** Softening can hide in mood rather than words, an example set where every borderline case excuses a skipped gate teaches the inversion without misquoting a single rule. Good: a probe catching where practical appended to the Iron Law in a derived doc. Bad: a quarter of reuse citing the 95 percent figure as industry data. Borderline: a translation rendering must as should for tone, flag it, ordering language is load-bearing here.

**Verification, evidence, and uncertainty.** Confirm each failure row names its probe and trigger point. The decay structure consolidated from this document's preceding sections. Reuse observability determines probe weighting.

**Second-order consequence.** Mandate softening is the dominant risk because it is performed by helpful editors, every summarizer instinctively rounds absolute rules toward reasonable ones, so the probe must diff reused phrasings against the source's absolutes, always, never, must, rather than checking mere topical fidelity.

**Revision decision.** Add the four rows with probes, checksum comparison for divergence, label audits for inflation, quarantine scans for leakage, and phrasing review for softening.

**Retained seed evidence.** All four seed failure rows with mitigations remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| decision path remains implicit | reader cannot tell when to adopt, adapt, or avoid the pattern | add decision table, cost of being wrong, and adjacent-reference route |
| large corpus becomes list | many sources are indexed but not synthesized into ranked guidance | classify canonical, supporting, legacy, duplicate, and conflicting sources |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide how many fix attempts are permitted and what happens at the limit. The seed corpus-process bullets stand beside the source's most distinctive retry doctrine, retries here govern hypotheses rather than requests, each failed fix mandates a return to Phase 1 with the new information, never a stacked second fix, the attempt counter is explicit, and the budget is three, at which point retrying stops entirely and the architecture itself goes under question with the human partner.

**Recommended default and causal basis.** Count every failed fix, re-enter Phase 1 between attempts, and hard-stop at three for the architecture discussion. Fix attempts are not idempotent, each failed fix changes the system and the debugger's mental model, so the doctrine forces re-investigation between attempts and treats repeated failure as evidence about the design, not about persistence.

**Operating conditions and assumptions.** The counter survives context switches and handoffs, the session ledger is its designed home. Retry doctrine for debugging conduct, request-level retry engineering belongs to the system design theme.

**Failure boundary and alternatives.** The anti-pattern is fix stacking, don't add more fixes on top, which converts a diagnosable system into an archaeology site where the original bug hides under three partial patches. Bounded alternatives and recoveries: the system design theme's exponential backoff for network calls, same philosophy, different substrate.

**Counterexample, gotchas, and operational comparison.** Reverting the failed fix before the next attempt is implied but easy to skip, a lingering half-fix contaminates the next investigation's evidence. Good: strike two prompting a fresh Phase 1 that finds the earlier hypothesis tested the wrong layer. Bad: a fourth quiet fix attempt to avoid admitting the pattern is unsound. Borderline: two related one-line fixes from one hypothesis, allowed only if the hypothesis genuinely predicted both.

**Verification, evidence, and uncertainty.** Audit ledgers for strike counts and re-investigation between attempts. The phase 4 rules and architecture clause read this session. Whether three is optimal is untested, the source asserts it as doctrine.

**Second-order consequence.** The three-strikes rule is backpressure in the load-shedding sense, it detects that demand for fixes exceeds the architecture's capacity to absorb them, each fix revealing new coupling elsewhere, and sheds the load upward to a design conversation instead of letting fix attempts queue indefinitely.

**Revision decision.** State the hypothesis-retry loop, fail, revert to investigation, single new hypothesis, single minimal test, with the three-strike stop and the architectural escalation as its backpressure valve.

**Retained seed evidence.** All five seed retry and backpressure bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what instrumentation must exist before a fix may be proposed. The seed generic records stand beside the source's diagnostic instrumentation doctrine, log entry and exit data at every component boundary before proposing fixes, capture stacks with new Error before dangerous operations, prefer console.error in tests where loggers are suppressed, include directory, cwd, environment, and timestamps in context, and run once to see where the chain breaks before touching anything.

**Recommended default and causal basis.** Before any fix proposal in a multi-component failure, instrument every boundary, run once, and read the break point off the output. Multi-component failures hide in the gaps between layers, secrets reaching the workflow but not the build script, so the doctrine instruments the boundaries themselves, converting where does it break from speculation into a single evidence-gathering run.

**Operating conditions and assumptions.** The failing path is re-runnable, non-reproducible issues fall back to the skill's gather-more-data rule. Observability for debugging investigations, production telemetry doctrine belongs to the system design theme.

**Failure boundary and alternatives.** Fixing before instrumenting is the skill's named sequence error, the will-it-show-us partner signal exists precisely for proposals that lack an evidence plan. Bounded alternatives and recoveries: attaching a step debugger, powerful locally, unavailable across CI and multi-process boundaries where the echo recipe still works.

**Counterexample, gotchas, and operational comparison.** The suppressed-logger trap generalizes, any observability channel the failing context filters, quieted test loggers, sampled traces, buffered stdout, will eat the one probe that mattered, verify the channel before trusting its silence. Good: four boundary probes revealing secrets die between workflow and build script. Bad: proposing a signing fix with no evidence of which layer loses the identity. Borderline: keeping diagnostic probes after the fix, useful as Layer 4 forensics if converted to proper logging.

**Verification, evidence, and uncertainty.** Check incident ledgers for boundary evidence predating the first fix proposal. The instrumentation recipes read across spine and companions this session. The recipes assume shell-and-JS stacks, other runtimes need translated equivalents.

**Second-order consequence.** This doctrine is disposable observability, probes added for one diagnostic run and removed after, the complement of the system design theme's permanent telemetry, and the skill's Layer 4 debug logging bridges them, instrumentation worth keeping becomes permanent forensics for the next incident.

**Revision decision.** Adopt the boundary-instrumentation recipe as the checklist core, the four-layer echo example, stack capture, suppressed-logger workaround, and the run-once-then-analyze sequencing.

**Retained seed evidence.** All six seed observability bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture reviewer decision, unresolved uncertainty, and next refresh trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how debugging and test performance are measured and improved on this evidence. The seed latency packet stands beside the source's performance teaching, debugging speed comes from eliminating rework rather than rushing steps, measured in its session records as fifteen flaky tests fixed with pass rates going 60 to 100 percent and the suite running 40 percent faster once guessed delays became condition polls with 10-millisecond intervals and explicit timeouts.

**Recommended default and causal basis.** Convert guessed delays to condition polls with documented timeouts, and measure debugging speed as time-to-verified-fix, never time-to-first-attempt. Arbitrary sleeps set to worst-case guesses waste time on every run and still fail under load, while condition polling exits the instant the condition holds, so correctness-driven waiting is simultaneously the faster waiting.

**Operating conditions and assumptions.** Conditions are cheaply pollable, the companion's 10-millisecond guidance balances latency against CPU waste. Performance of the debugging process and its test suites, production latency budgets belong to the system design theme.

**Failure boundary and alternatives.** Tightening timeouts to speed a suite without converting to conditions trades one flake population for another, the polling conversion is the fix, not braver guessing. Bounded alternatives and recoveries: parallelizing a flaky suite for speed, which amplifies race conditions the polling conversion would have removed.

**Counterexample, gotchas, and operational comparison.** The legitimate-timeout carve-out has three requirements, wait for the triggering condition first, base the delay on known timing, and comment why, a bare documented sleep meets only the third. Good: a suite converting fifteen sleeps to polls and getting faster while stabilizing. Bad: reporting time-to-first-patch as debugging speed. Borderline: a 200-millisecond documented wait for two 100-millisecond ticks, permitted, it meets all three carve-out requirements.

**Verification, evidence, and uncertainty.** Sample test diffs for poll conversions and incident records for verified-fix timing. The waiting companion's patterns and impact notes read this session. The 40 percent figure is one session's report, direction is argued, magnitude is not.

**Second-order consequence.** Both claims share one mechanism, replacing time-based guesses with evidence-based exits, the process exits investigation when the root cause is found rather than when patience runs out, and the test exits its wait when the condition holds rather than when the sleep expires, one principle expressed at two scales.

**Revision decision.** State the two performance claims with their mechanisms, process speed via first-time fixes, suite speed via condition polling, both labeled as the source's session-reported numbers.

**Retained seed evidence.** The method, indicator, measurement packet, and pass and fail lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require source-boundary preservation and p95 under 10 minutes for a reviewer to identify the next verification action.
Leading indicator to measure: the chosen boundary reduces blast radius or uncertainty measured by explicit probes.
Failure signal to watch: the reference jumps to a pattern before proving the problem shape.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide where individual debugging ends and collaborative or architectural work begins. The seed task-splitting bounds stand beside the source's own scale limits, the discipline is written for one agent, one incident, and one hypothesis at a time, its escalation boundary is explicit, three failed fixes end individual debugging and require the human partner, and its architecture clause marks where debugging itself stops scaling, when each fix reveals new coupling elsewhere, the problem has outgrown the method.

**Recommended default and causal basis.** Serialize hypotheses within an incident, escalate at three strikes, and read repeated cross-cutting fixes as architecture signal rather than bad luck. The phases assume a single coherent investigation state, parallel hypotheses or multiple debuggers on one bug fragment the evidence chain the gates depend on, so the method scales by sequencing incidents, not by parallelizing within one.

**Operating conditions and assumptions.** A human partner is reachable for the escalation the third strike mandates. Scale limits of the debugging method, this evolution's own task splitting keeps the seed paragraphs.

**Failure boundary and alternatives.** The scale failure the source names is unbounded persistence, fix four, five, six, each locally reasonable, collectively the sheer-inertia pattern its architecture clause exists to break. Bounded alternatives and recoveries: the system design theme's doctrine for the redesign that begins where this method's horizon ends.

**Counterexample, gotchas, and operational comparison.** Swarming a sev-1 with multiple debuggers is compatible only if evidence gathering parallelizes while hypothesis testing stays serialized through one ledger, split the reading, never the fixing. Good: strike three on a shared-state bug triggering a design review that finds the module boundary wrong. Bad: five parallel speculative fixes from three engineers on one incident. Borderline: two debuggers splitting boundary instrumentation on one outage, fine while a single ledger serializes the hypotheses.

**Verification, evidence, and uncertainty.** At each design review, check whether escalations fired at the documented boundaries. The strike rules and architecture clause read this session. Team-scale adaptations of the single-agent method are beyond the source's coverage.

**Second-order consequence.** The architecture clause is a scale detector disguised as a stopping rule, fixes that keep surfacing new coupling are measuring the system's hidden interconnectedness, so the strike counter does double duty, bounding effort while cheaply estimating whether the codebase itself has exceeded its design's coherent scale.

**Revision decision.** State the three boundaries, single-hypothesis serialization, the three-strike human escalation, and the architectural horizon where fixing yields to redesign.

**Retained seed evidence.** All four seed scale-boundary paragraphs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Systematic Debugging Method Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which probes reveal decay in this node's claims and on what clocks. The seed theme-name queries would surface generic debugging content while this node's staleness has exact homes, the two mapped copies whose checksums must stay equal, the sweep inventory that could gain newer superpowers snapshots, the sibling-skill names whose resolvability the spine assumes, and the upstream ecosystem whose evolution only external windows can reveal.

**Recommended default and causal basis.** Run the checksum and sweep probes each cycle and the ecosystem check at external windows. The theme's conduct core is evergreen, its perishables are purely referential, paths, twin checksums, and cross-skill names, so refresh effort belongs entirely on the reference layer.

**Operating conditions and assumptions.** Both paths remain in the repository, removal of either converts the probe into a single-copy integrity check. Refreshing this node's evidence and pointers, live debugging practice needs no refresh from here.

**Failure boundary and alternatives.** Undirected refreshing would re-debate debugging philosophy while missing the one silent break that matters, a sweep replacing one copy with a revised skill while the twin and this synthesis still describe the old one. Bounded alternatives and recoveries: declaring the theme frozen, safe for conduct content, blind to the reference rot the probes exist to catch.

**Counterexample, gotchas, and operational comparison.** A newer archive snapshot appearing would not invalidate this synthesis but would fork the evidence, the probe response is a dated comparison of versions, not a silent re-target. Good: a refresh logging checksum equality and no new superpowers snapshots this cycle. Bad: logging that systematic debugging searches returned nothing new. Borderline: skipping the ecosystem check for lack of an external window, acceptable, record the skip.

**Verification, evidence, and uncertainty.** Record each probe with its date and the claim it confirmed or updated. The twin-path structure and dependency inventory established this session. Future sweep contents and external window availability are what the probes exist to learn.

**Second-order consequence.** The twin-copy structure turns the checksum probe into a drift alarm, any future sweep touching one path first will break equality before anything else changes, making one cheap comparison the earliest possible signal that this theme's evidence base moved.

**Revision decision.** Replace name queries with targeted probes, checksum comparison across both paths, sweep scans for newer superpowers archives, pointer-resolution checks on the named sibling skills, and an external-window check on the upstream ecosystem when available.

**Retained seed evidence.** The three seed query rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | systematic debugging method patterns official documentation best practices |
| `github_repository_query_phrase` | systematic debugging method patterns GitHub repository examples |
| `release_notes_query_phrase` | systematic debugging method patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide under what label, chain, and state each claim class here may be reused. The seed label definitions stand without this assignment's distinctive ledger, two byte-identical copies checksum-verified, all nine directory files read in full totaling 962 lines, zero external URLs fetched, the named upstream CLAUDE.md unretrieved, and no debugging incident conducted, so every conduct claim here is a faithful reading of the skill, not a demonstration of its results.

**Recommended default and causal basis.** Before reusing a claim, declare it structural fact, quoted mandate, author anecdote, or designed inference, and treat unlabeled claims as inference. Conduct disciplines can only be locally evidenced as texts, their empirical payoffs, fix rates and thrash ratios, live in future incidents this corpus has not run, splitting the theme cleanly into verified content and unverified efficacy.

**Operating conditions and assumptions.** The source stays unedited at both paths and labels persist through reuse, both watched by the established probes. Reuse rules for this document's claims, each claim travels with class, source file, and verification state.

**Failure boundary and alternatives.** The costliest mislabel would present the skill's efficacy anecdotes as corpus-verified outcomes, or the pressure-test fixtures as observed behavior, both are authored artifacts inside one directory. Bounded alternatives and recoveries: running a ledgered incident under the full discipline to earn a demonstrated-outcome layer, declined for scope, queued as the natural verification upgrade.

**Counterexample, gotchas, and operational comparison.** The theme's most quotable line, the Iron Law, is exactly where paraphrase pressure will concentrate, quoted-mandate status protects its absolutes only while the quoting stays verbatim. Good: reusing the four-phase structure as quoted mandate and the strike-drift alarm as designed inference. Bad: citing the 95 percent first-time fix rate as a corpus-measured result. Borderline: reusing the projectDir case as evidence the method works, it is the author's account of one success, label it anecdote.

**Verification, evidence, and uncertainty.** Sample claims from earlier sections and confirm each declares its class cleanly. This assignment's ledger, nine files read, checksums equal, zero fetches, zero incidents run. Empirical efficacy awaits ledgered incidents under the discipline.

**Second-order consequence.** Normative texts occupy a special evidence position, quoting a rule accurately makes the claim about what the rule says fully verified even while the rule's wisdom stays empirically open, so this theme's citations can be simultaneously airtight and unproven, a distinction reuse must keep visible.

**Revision decision.** Publish the strata explicitly, directory contents and structure as same-session local facts, the skill's rules as accurately-quoted normative text, its impact numbers as author anecdotes, and all extensions here, the ledger, the six-measure loop, the strike-drift alarm, as labeled inference.

**Retained seed evidence.** The three labeled boundary definitions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
