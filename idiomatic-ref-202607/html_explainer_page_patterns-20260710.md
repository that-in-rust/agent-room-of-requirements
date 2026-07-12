# Html Explainer Page Patterns

Use this reference to decide whether a technical subject should become a source-grounded, standalone HTML explainer and, when it should, how to shape and verify that artifact. The target is a teammate who needs a guided mental model of code, architecture, a lifecycle, a connector, a workflow, or mixed technical evidence. The target is not a product landing page, an exhaustive API manual, or a production application disguised as documentation.

`local_corpus_sourced_fact`: The repository's canonical skill defaults to one self-contained HTML file with inline CSS and JavaScript, direct opening from disk, a short narrative journey, restrained visuals, and a footer naming the source artifacts. Its supporting pattern asks the author to move from intuition to mechanism, reveal the core loop by the second act, distinguish metaphor from mechanics, explain state and recovery, and finish with a compressed takeaway.

**Recommended default:** read the evidence first; identify the thesis, actors, lifecycle, persisted state, failure classes, and extension boundaries; then build a five-to-eight-act page that opens with the real mystery and reaches the system heartbeat early. Delete scaffold sections that do not serve that story. Use exact source nouns and verbs, one or two telling code excerpts, text-legible diagrams, and only enough interaction to improve orientation.

This default works well when ordering is part of understanding: a bounded data path, repeated lifecycle, recovery branch, architectural boundary, or asymmetric comparison can be revealed in conceptual sequence. Prefer a lighter medium when the reader mainly needs exhaustive lookup, terminal portability, low-maintenance prose, or a small static diagram. Prefer a tested frontend application when authentication, live data, server state, or substantial user input is essential to the explanation.

An explainer has two independent truth surfaces. Its claims must trace to code, notes, specifications, tests, or explicitly labeled uncertainty; its rendered page must also open locally, remain readable at intended viewports, preserve keyboard access, tolerate unavailable enhancement scripts, and contain no scaffold residue. A polished visual journey that invents behavior is a failure, as is accurate prose hidden inside a broken or inaccessible page.

`combined_evidence_inference_note`: Treat the explainer as a maintained interface between changing source and a reader's mental model. Scale review rigor to reuse and consequence: a disposable team sketch may need a short evidence and browser check, while an onboarding or decision artifact should carry source traceability, repeatable visual evidence, and a refresh trigger. If a source change invalidates the final one-sentence compression, review the narrative spine before polishing individual components.

## Source Evidence Mapping Table

Use this map to decide what a source can prove, not merely where it lives. `Inspected` means the artifact was read completely during this evolution. `Inherited, unrefreshed` means the URL remains a future research lead and supports no current factual claim.

| source_location_path_key | evidence_role_and_status | contribution_to_this_reference | limit_or_verification_action |
| --- | --- | --- | --- |
| `agents-used-monthly-archive/codex-skills-202603/explain-html-skill/SKILL.md` | canonical local instruction; inspected | Establishes the single-file, direct-open artifact; source-first workflow; five-to-eight-act guidance; visual restraint; guardrails; and finish checks. | Re-read when the skill changes; distinguish required workflow from examples and aesthetic language. |
| `agents-used-monthly-archive/codex-skills-202603/explain-html-skill/references/elegant-explainer-pattern.md` | supporting local pattern; inspected | Defines the mystery-to-mechanism narrative spine, evidence inputs, component purposes, writing rules, visual rules, and source-grounding checklist. | Treat suggested beats as a deletable baseline, not a mandatory seven-act schema. |
| `agents-used-monthly-archive/codex-skills-202603/explain-html-skill/scripts/create_elegant_explainer_html.py` | linked implementation support; inspected | Demonstrates scaffold generation, HTML escaping, repeatable source-footer arguments, seven default acts, parent-directory creation, and refusal to overwrite without `--force`. | Describes bundled generator behavior only; run it in a disposable path before relying on environment-specific execution. |
| `agents-used-monthly-archive/codex-skills-202603/explain-html-skill/assets/elegant-explainer-template.html` | linked rendered-shell support; inspected as source | Shows inline styling and scripting, responsive grid collapse, hidden dot navigation below 960 px, scroll reveals, active-section observation, and template tokens. | Source inspection does not prove rendered usability; open generated output and test target browsers, viewports, keyboard paths, and script-failure behavior. |
| `https://developers.openai.com/codex/guides/agents-md` | inherited external pointer; unrefreshed | Potential future context for repository instruction discovery and source hierarchy. | Do not cite as current evidence until an authorized refresh records the inspected page and relevant claim. |
| `https://docs.github.com/actions` | inherited external pointer; unrefreshed | Potential future context for automating artifact checks. | The broad documentation root does not establish a specific workflow; narrow and inspect a relevant primary page before use. |
| `https://agents.md/` | inherited external pointer; unrefreshed | Potential future context for general agent-instruction conventions. | It is adjacent rather than HTML-explainer evidence; retain only as a refresh route, not support for narrative or browser claims. |

**Evidence hierarchy:** use the canonical skill for local intent, the pattern file for explanatory detail, and the linked script and template for observable scaffold behavior. Use an existing output page, when supplied by the task, to establish house pacing and tone. Use refreshed primary standards or browser documentation for normative accessibility and platform claims. If those classes disagree, preserve the conflict and narrow the recommendation instead of averaging them.

**Gap disclosure:** no existing rendered explainer was mapped by the frozen seed, and no public source was opened in this no-browse task. Consequently, this reference can state the repository workflow and archived scaffold behavior confidently, but audience comprehension, browser compatibility, accessibility conformance, and current ecosystem practice still require artifact-specific evidence.

## Pattern Scoreboard Ranking Table

The frozen scores `95`, `91`, and `88` had no rubric, sample, or measurement record. They are therefore not retained as evidence. The tiers below express local acceptance priority: an author may explore out of order, but should not accept a lower-tier refinement while its stated prerequisite is red.

| adoption_priority | pattern_and_default_action | depends_on | primary_failure_prevented | observable proof signal |
| --- | --- | --- | --- | --- |
| `required_01` | **Evidence inventory first:** inspect the minimum implementation, interface, specification, test, issue, and prior-explainer sources needed to explain the subject honestly. | Identified audience question and bounded subject. | Confident copy invented from filenames, generic patterns, or visual intuition. | Every major claim maps to an inspected artifact or is visibly labeled as inference or uncertainty. |
| `required_02` | **Mechanism by the second act:** show the core loop, lifecycle, decision path, or state transition early using the source's actual verbs. | A defensible one-sentence thesis and actor list. | A long atmospheric opening that never gives the reader the system heartbeat. | A reviewer can locate and restate the primary causal path before reaching secondary variants. |
| `required_03` | **Mechanism-metaphor binding:** use analogy only when it lowers initial cognitive cost, then immediately connect each mapped element to exact mechanics. | Source-grounded mechanism. | A memorable analogy that replaces, distorts, or overgeneralizes real behavior. | Removing the metaphor leaves a complete technical explanation; keeping it improves orientation. |
| `required_04` | **Dual-surface verification:** review semantic claims and rendered browser behavior independently. | Draft narrative and runnable artifact. | Correct prose in a broken page, or polished rendering that communicates unsupported behavior. | Claim-source review passes, and direct-open, keyboard, viewport, console, and content-state checks pass for declared targets. |
| `strong_default_05` | **Single-file portability:** keep CSS and JavaScript inline and avoid a build step for a bounded explainer. | No requirement for server state, authentication, or a shared application runtime. | An artifact that reviewers cannot reproduce or open without author-specific setup. | A fresh local browser opens the copied file and reaches all essential content without installation. |
| `strong_default_06` | **Intentional component economy:** choose flow steps, diagrams, comparisons, code excerpts, cards, and tables only for information each form expresses better than prose. | Stable narrative spine. | A page that becomes a gallery of widgets and repeated card containers. | Each visual answers a named reader question; deleting any one has an explainable information cost. |
| `strong_default_07` | **Scaffold deletion and subject adaptation:** remove unused acts, generic labels, example failures, source prompts, and template assumptions. | Scaffold generated or copied. | Template residue presented as system fact, including false symmetry between modes. | Automated text scan and human source review find no generic scaffold copy or unsupported category. |
| `conditional_08` | **Motion and persistent navigation:** add subtle orientation aids only when page length and audience justify them, with reduced-motion and non-script fallbacks. | Complete static reading path. | Decorative movement, hidden content, pointer-only navigation, or script-dependent comprehension. | Essential content is visible and ordered with scripting disabled; keyboard and reduced-motion checks preserve the journey. |

**Dependency rule:** evidence constrains the narrative; the narrative determines which components deserve space; rendered verification then tests the resulting artifact. Authoring can loop backward when a diagram or browser review exposes a faulty source model. Acceptance still fails closed at the earliest unresolved required row.

Project-specific risks may promote a conditional practice to required status. Examples include localization for a multilingual audience, privacy review for real operational data, or formal accessibility criteria for a public artifact. Record the reason for promotion and its proof method; do not create a new unexplained score.

## Idiomatic Thesis Synthesis Statement

**Thesis:** An idiomatic HTML explainer is an evidence-grounded guided tour that lets a defined reader form and inspect a correct causal model of a bounded technical subject. Narrative order reveals the mechanism; visuals compress relationships that prose handles poorly; browser behavior preserves access to the same argument across declared conditions. Style serves those outcomes and is never evidence by itself.

`local_corpus_sourced_fact`: The canonical local skill requires source-first authoring, one directly openable HTML file with inline CSS and JavaScript, a clear title, a mystery or problem opening, the main mechanism by the second act, selective visual components, restrained motion, mobile readability, deleted scaffold residue, and a source list. The supporting pattern adds explicit attention to actors, persisted state, recovery, extension boundaries, failure classes, and a final compression sentence.

`unknown_or_not_evaluated`: No public source was inspected during this no-browse evolution. The inherited URLs remain refresh leads and do not establish current accessibility, browser, automation, or agent-instruction facts in this file.

`combined_evidence_inference_note`: Optimize for time to a correct mental model, not component count, scroll depth, or visual novelty. Begin with the smallest trustworthy source set, identify what the reader should be able to explain or predict, reveal the earliest causal structure, and use only components that reduce a named comprehension burden. Keep essential meaning available without motion, pointer input, or successful enhancement scripts.

The default can be adapted: a familiar audience may need a direct mechanism rather than a mystery, and a subject may have a decision tree or transformation path rather than a loop. The invariant is that intuition earns depth and then yields to exact mechanics. Omitted detail is acceptable when scope and uncertainty are visible; invented behavior, hidden caveats, inaccessible essentials, and false confidence are not.

**Thesis gate:**

1. Can a reviewer identify the page's audience question and trace every major answer to inspected evidence?
2. Can the reviewer restate the core causal path before secondary implementation detail dominates the page?
3. Can keyboard, narrow-screen, reduced-motion, and script-failure readings reach the essential mechanism and caveats?
4. Can the reviewer use the final compression to predict at least one state transition, failure, or recovery outcome without exceeding the page's declared scope?

If a presentation defect changes which information is available, its order, attribution, or apparent causal relation, treat it as an explanatory correctness defect. If it affects only decoration, classify it separately and prioritize accordingly.

## Local Corpus Source Map

The local package provides the method for explaining; it does not provide facts about the system a new page will explain. Before drafting, build two inventories:

- **Method evidence:** the sources below establish artifact shape, narrative defaults, component purposes, and review guardrails.
- **Subject evidence:** implementation files, interfaces, specifications, tests, diagrams, issue discussions, and prior explainers establish actors, behavior, state, failures, and terminology for the actual topic.

| retrieval_order | local_source_filepath_value | extract_for_decisions | do_not_infer | cross_check |
| ---: | --- | --- | --- | --- |
| 1 | `agents-used-monthly-archive/codex-skills-202603/explain-html-skill/SKILL.md` | Activation boundary; direct-open and single-file default; source-reading sequence; five-to-eight-act range; scaffold deletion; mobile and source-footer checks. | Do not infer subject behavior, universal audience preference, or mandatory use of every template component. | Does the proposed deliverable still match the skill description, and which explicit guardrail rejects the weakest design choice? |
| 2 | `agents-used-monthly-archive/codex-skills-202603/explain-html-skill/references/elegant-explainer-pattern.md` | Inputs to gather; mystery-to-mechanism pacing; state and recovery questions; architecture boundaries; failure buckets; component selection rules; final compression. | Do not force seven acts, symmetrical comparisons, metaphors, or connector-specific examples onto a different subject. | Can every retained act answer one reader question, and was every inapplicable default deleted? |
| 3, when bootstrapping | `agents-used-monthly-archive/codex-skills-202603/explain-html-skill/scripts/create_elegant_explainer_html.py` | Actual command options, HTML escaping, source-footer rendering, section generation, output-directory creation, and overwrite refusal unless `--force` is supplied. | Do not assume the archived script is installed, current, or safe to point at a valued output without a disposable run. | Does a temporary invocation produce the expected artifact, and is an existing destination protected? |
| 4, when building or diagnosing | `agents-used-monthly-archive/codex-skills-202603/explain-html-skill/assets/elegant-explainer-template.html` | Inline style and script behavior, layout primitives, responsive breakpoints, reveal logic, dot navigation, template tokens, and external font dependency. | Do not equate archived colors, gradients, rounded components, motion, or breakpoints with requirements for every page. | Does generated output preserve essential content when external fonts or enhancement scripts are unavailable? |

**Default retrieval path for creation:** read the two prose sources completely, inventory the target system, write the thesis and causal path, and inspect the script and template before invoking or modifying the scaffold. For critique or regression work, inspect the existing output first to capture the observed failure, then trace it back through subject evidence and the relevant method artifact. For an explicit redesign, preserve an existing page's pacing and tone only when the user asks or local convention requires it.

**Drift checks:** resolve every relative link; record which source changed a decision; compare prose intent with generated behavior; and identify any subject fact that entered from example scaffold copy rather than the target system. The archived files are read-only evidence in this task. Finding an upstream defect establishes a future owner and action, not permission to edit outside the assigned reference, packet, and journal.

## External Research Source Map

**Current status:** no external page was opened for this evolution. The table records inherited refresh leads, not current factual support. Do not cite a row as evidence until an authorized refresh records the exact inspected page, relevant section, supported proposition, date, and applicability to the declared artifact environment.

| external_source_url_value | potential_question_to_answer | refresh_trigger | why_the_uninspected_pointer_is_insufficient |
| --- | --- | --- | --- |
| `https://developers.openai.com/codex/guides/agents-md` | How should repository instruction files guide source discovery and local workflow when an agent creates an explainer? | The task depends on current Codex instruction precedence, scope, or product behavior. | An inherited URL does not establish present content, and agent-instruction guidance does not by itself support HTML narrative, accessibility, or browser claims. |
| `https://docs.github.com/actions` | Which current automation primitives could run repeatable static or browser checks in a specific repository? | The explainer needs a maintained CI gate and the repository has selected GitHub Actions as its runner. | This broad documentation root neither defines a workflow nor proves a particular browser tool, permission model, or action version. |
| `https://agents.md/` | Which general conventions might make explainer instructions discoverable to different coding agents? | Cross-agent instruction compatibility is an explicit requirement. | The source is adjacent to artifact creation; without an inspected relevant passage it cannot establish page structure or verification behavior. |

Refresh external evidence when a claim is normative, versioned, compatibility-sensitive, security-sensitive, accessibility-sensitive, or dependent on a current service API. Internal drafting may proceed without a refresh only when claims remain bounded to inspected local evidence and explicitly recorded test environments. A public, regulated, or cross-browser deliverable should not use the archived template as a substitute for current primary standards and platform documentation.

**Minimum refresh record:**

1. State the unresolved decision before searching.
2. Prefer the primary standard, platform, or official tool documentation that directly governs that decision.
3. Record the exact page and section, inspection date, concise supported claim, version or environment boundary, and any contradictory evidence.
4. Verify observable behavior against the actual artifact; documentation alone does not prove rendering or interaction.
5. Mark the record stale when the dependency, target browser matrix, delivery environment, or governing requirement changes.

Search snippets, broad documentation roots, and reputable domain names are navigation aids, not final proof. A useful citation has a removable consequence: a reviewer can name which recommendation becomes unsupported if that evidence disappears. If no such recommendation exists, omit the citation rather than using it as authority decoration.

## Anti Pattern Registry Table

Apply truth-and-access blockers even to drafts; apply the complete registry before an artifact is accepted or shared as authoritative. An exception must show how the underlying risk is controlled, not merely explain why the preferred surface pattern was skipped.

| anti_pattern_failure_name | observable_signal_and_consequence | safer_replacement_or_recovery | primary_detection_mode |
| --- | --- | --- | --- |
| `evidence_free_visual_confidence` | Major behavior claims have no inspected source, while polished layout makes them appear settled. | Build a claim-source ledger; remove, narrow, or label unsupported statements before styling review continues. | Compare every major mechanism, state, failure, and guarantee against subject artifacts. |
| `heartbeat_buried_after_context` | The reader encounters history, definitions, or decoration before the core loop or causal path and cannot predict what the system does. | Move the mechanism to the second act or earlier; defer secondary context until it explains a visible step. | Ask a cold reviewer to locate and restate the causal path without scanning the full page. |
| `metaphor_replaces_mechanism` | Analogy vocabulary persists without a one-to-one return to source nouns, state, timing, or failure behavior. | Follow the metaphor immediately with exact mechanics; delete any mapped element that distorts the model. | Remove the analogy and verify that the technical explanation remains complete. |
| `scaffold_residue_as_fact` | Labels such as Path A, generic retry buckets, replacement copy, or sample state names survive into the final artifact. | Replace with source terms or delete the entire component when the subject lacks that structure. | Scan visible text and source for scaffold phrases, then review every retained act against evidence. |
| `forced_symmetric_comparison` | Two paths receive matching cards and categories even though reality is asymmetric, hiding unsupported capabilities or caveats. | Compare only shared decision dimensions and give unequal space where the evidence is unequal. | Trace each cell or bullet independently; reject empty symmetry and invented counterparts. |
| `component_gallery_narrative` | Cards, diagrams, tables, and code blocks accumulate without a question each uniquely answers. | Keep one dominant visual direction and select the lowest-complexity component that clarifies the relation. | For every component, record the information lost if it is removed; remove components with no material loss. |
| `code_dump_substitutes_explanation` | Large implementation excerpts force readers to reconstruct the model and create maintenance drift. | Use one or two short excerpts that reveal a decisive interface, condition, query, or state transition; explain why each matters. | Check excerpt length, source pointer, surrounding interpretation, and relevance to the current act. |
| `script_gated_essential_content` | Reveal styles leave content invisible, navigation is pointer-only, or an enhancement error blocks the reading path. | Make content visible and ordered by default; layer observation and smooth scrolling as optional enhancement. | Open with scripts disabled or forced to fail, inspect the DOM, and complete the essential path by keyboard. |
| `motion_without_reader_control` | Smooth scrolling or reveal movement ignores reduced-motion preference or creates disorientation without adding meaning. | Honor reduced motion, avoid animation-dependent sequencing, and keep transitions subtle and interruptible. | Test the declared reduced-motion path and verify equivalent content order without animation. |
| `narrow_viewport_overflow` | Tables, code, diagrams, long tokens, or card grids clip, overlap, or force incoherent horizontal reading. | Reflow grids, constrain media, provide deliberate overflow for code or tables, and wrap or break long identifiers safely. | Capture target-width screenshots and inspect boundaries, text fit, focus visibility, and scroll containment. |
| `source_footer_without_traceability` | A footer lists broad paths, but claims cannot be connected to specific artifacts or unresolved conflicts. | Keep a concise source ledger and add inline attribution where a disputed or surprising claim needs it. | Sample major claims in both directions: claim to source and source to represented conclusion. |
| `template_overwrite_or_orphan` | A bootstrap command replaces valued work, or generated output cannot be reproduced because inputs and invocation were not recorded. | Generate to a new or disposable path, respect overwrite refusal, and retain the command plus source list in review evidence. | Exercise the helper against an existing temporary destination and inspect the resulting source footer. |

Use a layered diagnostic order: first verify the source model, then the narrative spine, then component choice, then browser behavior. Repair the earliest responsible layer. A sound narrative may still have a runtime defect, but repairing CSS cannot make an invented recovery guarantee true.

Machine scans are appropriate for scaffold tokens, missing attributes, broken links, syntax, and some overflow signals. Human source review is required for causal fidelity and false symmetry. Target-reader tasks are required when the outcome claim is comprehension rather than mere structural conformance.

## Verification Gate Command Set

Verification has four layers: source truth, artifact structure, rendered reading paths, and this reference's own corpus contract. A pass in one layer says nothing about an untested layer. Record `pass`, `fail`, or `not_evaluated` for each declared target.

**Gate A: Safe scaffold preflight**

Run the archived generator only when that package is the intended baseline, and generate into a disposable path before touching valued work:

```bash
python3 agents-used-monthly-archive/codex-skills-202603/explain-html-skill/scripts/create_elegant_explainer_html.py \
  --output /tmp/html-explainer-preflight/index.html \
  --hero-label "Technical Explainer" \
  --hero-title "How The Example System Works" \
  --hero-subtitle "A source-grounded preflight for the explainer shell." \
  --source idiomatic-ref-202607/html_explainer_page_patterns-20260710.md
```

Expected result: a directly openable file is created, supplied text is HTML-escaped, and a second invocation without `--force` refuses to overwrite it. This proves archived generator behavior in the current environment; it does not prove the final story or design.

**Gate B: Artifact residue and structure**

Set the path to the actual output under review, then scan for bundled scaffold phrases and unresolved template tokens:

```bash
artifact=.prd/ELI5/index.html
test -f "$artifact"
if matches=$(rg -n 'Replace this|Path A|Path B|Choose One Helpful Metaphor|__PAGE_TITLE__|__SECTION_ITEMS__|__FOOTER_SOURCES__' "$artifact"); then
  printf '%s\n' "$matches"
  echo "FAIL scaffold residue: $artifact"
  exit 1
else
  status=$?
  if [ "$status" -ne 1 ]; then
    exit "$status"
  fi
fi
echo "PASS scaffold residue: $artifact"
```

Expected result: one `PASS scaffold residue` line and no preceding matches. A match fails the automated precheck; review it rather than deleting blindly because a subject could legitimately use one phrase. Then run a standard-library structural check:

```bash
artifact=.prd/ELI5/index.html
python3 - "$artifact" <<'PY'
import pathlib
import sys
from html.parser import HTMLParser

class StructureProbe(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.viewport = False
        self.language = False

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        self.tags.append(tag)
        self.viewport |= tag == "meta" and values.get("name") == "viewport"
        self.language |= tag == "html" and bool(values.get("lang"))

path = pathlib.Path(sys.argv[1])
probe = StructureProbe()
probe.feed(path.read_text(encoding="utf-8"))
required = {"html", "head", "title", "body", "h1", "footer"}
missing = sorted(required.difference(probe.tags))
assert not missing, f"missing structural elements: {missing}"
assert probe.viewport, "missing viewport metadata"
assert probe.language, "missing document language"
print(f"PASS structure: {path}")
PY
```

This parser checks a small contract, not full HTML validity, accessibility, or visual layout. Add project-native validators when they are already available and record their versions.

**Gate C: Rendered and semantic review**

Open the final file directly from disk first. If the declared deployment surface is HTTP, repeat the same checks there. At minimum inspect:

| scenario | required observation | evidence to retain |
| --- | --- | --- |
| Desktop and narrow target widths | No clipping, incoherent overlap, hidden caveat, or uncontrolled page-level horizontal scroll. | Named viewport, full-page screenshot, and finding summary. |
| Keyboard-only reading | Every interactive control is reachable, focus is visible, order matches the argument, and no essential route requires hover. | Traversal notes and focused-state screenshot for any defect. |
| Reduced motion | Orientation remains clear and essential content does not depend on smooth scrolling or reveal transitions. | Declared preference state and observed result. |
| Enhancement script unavailable | Essential sections are visible and readable; navigation loss does not remove content. | Script-off screenshot plus console or failure note. |
| External asset unavailable | Text remains legible and layout stable enough when a font or optional media request fails. | Blocked-resource result and affected region. |
| Source truth | Core mechanism, state, failures, tradeoffs, and final compression agree with inspected artifacts. | Claim-source sample and unresolved uncertainty list. |

For onboarding or consequential decisions, add a target-reader task: ask the reader to restate the causal path and predict one failure or recovery outcome. Record the prompt, answer quality rubric, and observed misconception; DOM presence is not comprehension evidence.

**Gate D: Reference and corpus integrity**

Run the archive generator verifier retained by the seed:

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

Run the focused verifier for this evolved reference and its packet:

```bash
python3 tests/verify_idiomatic_reference_file.py --path idiomatic-ref-202607/html_explainer_page_patterns-20260710.md
```

The focused gate must report 26 reference sections, 26 packet sections, 260 exact question headings, 1,560 populated field values, and 1,560 exact and prefix-stripped normalized-unique values. It also confirms preserved heading order and growth beyond each frozen seed section.

**Evidence packet:** retain the artifact hash, exact commands, working directory, environment or browser versions, declared targets, concise outcomes, screenshots only where they prove a finding, and unresolved risks. Any artifact-byte change invalidates prior visual evidence until the affected gates are rerun.

## Agent Usage Decision Guide

Use this reference when a task needs a standalone, source-grounded visual journey through a technical subject, or when an existing explainer needs factual, narrative, responsive, accessibility, or runtime review. Theme-word matching is only a retrieval hint. Confirm the audience question, medium fit, evidence sufficiency, output path, and edit authority before writing.

| primary_agent_mode | trigger_and_first_move | required_work | stop_or_route_condition | exit_evidence |
| --- | --- | --- | --- | --- |
| `create_new_explainer` | A user asks how a bounded system works and wants a direct-open visual page. First inventory subject sources and read the local method pair completely. | Define audience, thesis, causal path, actors, state, failures, scope, and final prediction; outline only useful acts; generate safely; replace or delete all scaffold copy; verify both truth surfaces. | Stop implementation when essential behavior lacks evidence, ownership is unclear, or required interaction implies a real application. Narrow scope or route the medium. | Source ledger, outline rationale, changed path, artifact hash, declared browser conditions, gate results, and unresolved uncertainty. |
| `adapt_existing_explainer` | A page exists and the user asks for extension, correction, or subject reuse. First open and inspect the current artifact and its sources. | Preserve established pacing and tone unless redesign is requested; identify changed claims and impacted acts; retain valid work; update source footer and rerun affected paths. | Stop before broad redesign when the request is local, concurrent edits are present, or the artifact's ownership boundary is unknown. | Before-and-after behavior summary, retained design decisions, changed claim map, and focused visual evidence. |
| `diagnose_rendering_or_interaction` | A viewport, navigation, motion, loading, asset, or browser behavior is reported broken. Reproduce the exact condition before editing. | Minimize the failing state, identify whether the cause is content, CSS, script, dependency, or environment, repair the earliest responsible layer, and add a regression check. | Route to subject review when the observed symptom exposes a false claim; route to an application workflow when the page has become stateful product UI. | Reproduction condition, root cause, focused diff, passing regression scenario, and residual browser risk. |
| `review_content_and_narrative` | The user wants critique, accuracy review, or a clearer journey. Read the page and mapped subject evidence before judging style. | Trace major claims, test early mechanism visibility, inspect metaphor binding, remove false symmetry and detail overload, and verify the final compression against source behavior. | Report rather than rewrite when review-only intent is explicit; stop a factual approval when critical evidence remains unavailable. | Severity-ordered findings, claim-source samples, proposed narrative changes, and confidence boundaries. |
| `refresh_stale_explainer` | Source changes, a stale compression sentence, broken links, or changed delivery targets indicate drift. Start from the previous maintenance contract and current subject artifacts. | Revalidate scope and causal model, identify affected claims and visuals, refresh only authorized external evidence, rerun target conditions, and update provenance. | Replace rather than patch when the core mechanism or audience question changed enough that the old narrative creates negative transfer. | Drift trigger, old and new compression, impacted sections, refreshed evidence record, and new artifact hash. |
| `route_to_other_medium` | The requested outcome is exhaustive lookup, terminal-native explanation, a small static diagram, presentation delivery, or repeated live operation. | Recommend Markdown, ASCII, Mermaid, slides, a generated document, or a tested frontend according to the essential experience; preserve any useful source model. | Do not force HTML merely because the user said visual; do honor an explicit HTML requirement while disclosing and controlling its material costs. | Medium decision, rejected alternatives, retained evidence, and next artifact-specific verification route. |

**Universal sequence:** clarify the reader's decision or prediction; confirm exclusive write paths; gather the minimum honest subject evidence; read the relevant method evidence; establish the narrative spine; save work incrementally; verify semantic claims and rendered paths; report exact changed files, evidence, and unresolved risks. A diagnosis may start from the symptom and a review may stop at findings, but every mode must converge on the same evidence boundaries before claiming completion.

**Source-sufficiency gate:** do not fill a missing state transition, guarantee, failure class, or ownership boundary from a familiar architecture pattern. Mark it unknown, ask for the missing artifact when genuinely blocking, or narrow the page to what the evidence supports. A smaller accurate explainer is preferable to a complete-looking invented model.

The page may move through several modes over its lifetime. Retain the source list, declared target conditions, artifact hash, unresolved risks, and final compression sentence at each durable handoff. Those fields let a future maintainer detect drift and choose the next mode without reconstructing the original conversation.

## User Journey Scenario

`combined_evidence_inference_note`: This is an illustrative workflow, not a production case study. The system, subject paths, review outcomes, and reader response below are hypothetical. Transfer the decision sequence and replace every technical claim with evidence from the actual task.

**Role and starting state:** Mira is a new teammate who can find the code for an event-ingestion worker but cannot answer, "After a crash, where does processing resume, and under what conditions might an event be observed again?" The documentation author has implementation, state-store interface, recovery tests, and a short architecture note. There is no existing explainer and no evidence for a formal end-to-end delivery guarantee.

**Decision 1, choose the outcome:** The author defines success as Mira being able to trace one event from discovery through transformation and application, identify when progress becomes durable, and predict the restart branch. This is more specific than "understand the worker" and rules out unrelated configuration detail.

**Decision 2, choose the medium:** A long Markdown reference would be easier to maintain but would not control the order in which polling, tentative work, persistence, and retry are introduced. A live dashboard would show current state but require application behavior and would not explain why recovery works. A standalone HTML journey is selected as the onboarding entry surface; API facts and operational monitoring remain companion artifacts.

**Decision 3, test evidence sufficiency:** The author reads the worker entry point, state interface, recovery tests, and architecture note completely. The artifacts support the loop and restart behavior but do not establish exactly-once delivery. The page therefore explains observed checkpoint and replay mechanics, labels the formal guarantee unresolved, and points to the responsible source boundary. It does not infer a guarantee from the presence of retries.

**Decision 4, shape the story:** The outline uses six acts: the duplicate-or-loss mystery; the source-named processing loop; tentative versus durable progress; the crash branch; component and runtime ownership; and failure tradeoffs plus compression. The heartbeat appears in Act II. A short library-card metaphor introduces the checkpoint, then the exact stored fields and persistence event replace the analogy. A comparison is asymmetric because retry and clean-start paths do not have matching responsibilities.

**Decision 5, build conservatively:** The author generates a disposable scaffold, copies only the useful shell into the owned output, and replaces or deletes every generic act, label, failure example, and source prompt. Essential content is visible in document order without JavaScript. One diagram shows the branch around durable progress, and one short test excerpt demonstrates restart expectation. The footer lists the four inspected subject artifacts.

**Decision 6, verify both truth surfaces:** Claim sampling finds one sentence that overstates when persistence occurs; it is corrected before browser review. Desktop and narrow screenshots expose a state table that pushes the page horizontally, so the author changes its small-screen presentation. Keyboard traversal reaches the navigation where present, reduced-motion mode avoids smooth transitions, a script-off run retains all sections, and the console is clean for declared local conditions.

**Decision 7, test the mental model:** Mira correctly restates the loop but predicts that a crash after application can never repeat an event. That answer reveals that the distinction between applied and durably checkpointed work is visually underweighted. The author returns to the state act, strengthens the branch diagram and wording, and repeats the question. The second answer distinguishes the two states and preserves the page's explicit uncertainty about the overall delivery guarantee.

**Durable handoff:** The author records the source list, output hash, declared viewport and input conditions, commands and concise outcomes, unresolved guarantee question, and final compression: "Discover, transform, apply, persist progress, and recover from the last durable point." A future source change that invalidates this rhythm triggers narrative review.

The good outcome is not that the page looks finished. It is that a defined reader can make the intended prediction from traceable evidence, alternate reading paths preserve the argument, and unresolved behavior remains visibly unresolved. If reader review is unavailable, report comprehension as `not_evaluated`; do not substitute author confidence.

## Decision Tradeoff Guide

Choose the smallest artifact architecture that preserves the essential reader experience. The defaults below are local operating choices, not universal web-design results. Adapt only for a named benefit and record the new proof burden.

| decision_surface | conservative_default | adapt_when | avoid_or_split_when | verification_question_prompt |
| --- | --- | --- | --- | --- |
| **Output medium** | Standalone HTML for a bounded causal journey whose order and visual relations improve understanding. | A companion Markdown reference, diagram, or presentation serves lookup, terminal, or meeting needs. | The primary job is exhaustive lookup, repeated live operation, authenticated data, or substantial user input. | What can the target reader understand or predict in HTML that the cheaper medium does not preserve? |
| **Packaging** | One file with inline CSS and JavaScript, directly openable without a build step. | A maintained explainer family has proven reuse that justifies shared assets and a documented build. | External packaging makes the artifact unreproducible, or stateful requirements have turned it into an application. | Can a fresh reviewer reproduce and open the declared artifact from its recorded inputs? |
| **Scaffold use** | Generate safely, then replace or delete every default act and component according to subject evidence. | An existing local explainer intentionally establishes pacing and tone that the task should preserve. | Template assumptions define the story, introduce generic system semantics, or require broad redesign the user did not request. | Can every retained scaffold structure be justified by one reader question and one subject source? |
| **Narrative opening** | State the real problem or mystery, then expose the core causal structure by the second act. | An expert audience benefits from beginning directly with the mechanism or decision boundary. | Context delays the heartbeat, or a manufactured mystery obscures a straightforward operational question. | How soon can a cold reader restate the mechanism, and what earlier material is necessary for that restatement? |
| **Metaphor** | Use at most a short analogy that immediately maps back to exact nouns, state, timing, and failure behavior. | A difficult abstraction has a faithful mapping that lowers entry cost for the named audience. | The analogy requires exceptions, survives longer than the mechanics, or creates a false guarantee. | Does the technical explanation remain complete and accurate when the metaphor is removed? |
| **Visual component density** | One dominant visual direction and the lowest-complexity form for each relation. | Different relation types genuinely require flow, branch, comparison, excerpt, and summary forms. | Components repeat the same point, create card-heavy scanning cost, or exist mainly to fill the scaffold. | What unique information disappears if each component is deleted? |
| **Interaction and motion** | Essential content in static document order; subtle optional orientation enhancement. | A control lets readers compare states or paths more accurately than static presentation, with keyboard and fallback equivalence. | Meaning depends on hover, pointer input, animation timing, or successful script execution. | Can all essential claims and caveats be reached with keyboard, reduced motion, and failed enhancement scripts? |
| **Assets and typography** | System-capable text presentation and text-first diagrams with minimal optional dependencies. | A local image, font, or media asset conveys essential subject evidence and has loading, licensing, fallback, and size controls. | An external request breaks direct opening, leaks data, causes unstable layout, or supplies atmosphere instead of inspectable information. | What happens to meaning, layout, privacy, and load behavior when the asset is unavailable? |
| **Code and detail depth** | One or two short telling excerpts plus links or paths to exhaustive sources. | More detail is required for a decision-bearing interface, invariant, or failure branch and remains readable. | The page becomes a code dump or reference manual whose maintenance burden hides the narrative. | Can a reader explain why every excerpt is present, and does its source pointer make drift review practical? |
| **Verification depth** | Source traceability, direct-open check, target-width review, keyboard path, script-failure path, console check, and scaffold scan. | Public reach, long life, high consequence, or complex interaction justifies automation, broader matrices, accessibility review, and reader studies. | Evidence is generated but not inspected, targets are undefined, or a screenshot is treated as proof of semantic accuracy. | Which failure classes does each retained item of evidence actually close? |

**Adopt:** use the baseline when the subject is bounded, evidence is sufficient, essential meaning is static, and direct local portability matters. **Adapt:** preserve the thesis while changing a default for a measured or clearly testable audience benefit. **Avoid or split:** route to another medium or companion artifact when the page is being asked to serve incompatible narrative, reference, and operational jobs.

Re-evaluate coupled adaptations. External assets can weaken direct-open portability; motion adds reduced-motion states; shared components add build and version dependencies; wide comparisons add narrow-screen burden. Two exceptions that pass independently may jointly invalidate the reason the single-file default was chosen.

The cost of a wrong choice is not only initial rework. It includes misleading reader decisions, inaccessible caveats, evidence that cannot be reproduced, and future updates that repeatedly patch the wrong layer. At the first substantive refresh, compare actual maintenance effort and reader findings against the original rationale and simplify or re-architect accordingly.

## Local Corpus Hierarchy

Hierarchy is claim-scoped. A source may be canonical for workflow intent, supporting for narrative detail, executable for observed generator behavior, or irrelevant to the target system's mechanics. Authority to approve a new design is also distinct from evidence about what archived sources or current code actually do.

| local_source_or_source_class | hierarchy_role | can_establish | cannot_establish | reviewer_question_to_answer |
| --- | --- | --- | --- | --- |
| `explain-html-skill/SKILL.md` | canonical entry and deliverable-intent source | When the skill applies; direct-open single-file baseline; required source reading; broad story shape; guardrails; finish criteria. | The target system's behavior, universal design effectiveness, or exact runtime behavior of a modified page. | Which explicit instruction governs this decision, and is it a requirement, default, or example? |
| `references/elegant-explainer-pattern.md` | supporting narrative and component source | Input categories, seven deletable beats, component purposes, writing rules, visual rules, and source-grounding checklist. | A mandatory act count, subject-specific mechanics, or normative browser and accessibility requirements. | Which reader question does the borrowed beat or component answer, and why is it retained for this subject? |
| `scripts/create_elegant_explainer_html.py` | executable scaffold-behavior source | Parsed arguments, escaping, generated section structure, source rendering, output creation, and overwrite refusal in the archived script. | Behavior of another generator, successful execution in an untested environment, or quality of generated content. | Was the exact script version exercised safely, and does prose intent agree with observed output? |
| `assets/elegant-explainer-template.html` | executable shell and default-style source | Archived CSS, markup, breakpoints, external font import, reveal observers, and dot-navigation behavior. | Required aesthetics, actual accessibility, target-browser support, or behavior after local modification without testing. | Which template behaviors remain in the final artifact, and what alternate states do they add to verification? |
| Existing task-specific explainer | observed local artifact and possible tone source | Current rendered behavior, content, pacing, defects, and local adaptations; intended tone when the task says to preserve it. | Accuracy of its technical claims or universal policy merely because it already exists. | Is this observation about actual output, desired convention, or subject truth, and what corroborates it? |
| Target implementation, interfaces, tests, specifications, and owner decisions | subject-truth evidence with claim-specific precedence | Actors, causal path, persisted state, failure semantics, extension boundaries, terminology, and approved scope according to source type. | Explainer-method defaults unless the artifact explicitly governs documentation. | Does the selected evidence actually entail the claim, and are desired, tested, and observed behavior being kept distinct? |

Use `canonical`, `supporting`, `executable`, `observed_output`, `subject_truth`, `legacy`, `duplicate`, `conflicting`, and `task_irrelevant` as review roles. A legacy source can establish historical intent but not current behavior. A duplicate adds no independent confidence. A conflicting source is preserved until the disagreement is assigned and resolved or disclosed.

**Conflict protocol:**

1. Name the exact disputed claim and classify each source by role, version, and scope.
2. Preserve both desired and observed behavior when they differ; do not make code erase intent or prose erase implementation.
3. Route method conflicts to the explainer-package owner, subject-mechanism conflicts to the system owner, and rendered-behavior conflicts to the artifact owner with reproduction evidence.
4. Record an owner override as a new decision with rationale; do not rewrite what an older source said.
5. Narrow or mark the page uncertain until a high-consequence contradiction is resolved.

Verify the hierarchy bidirectionally. Sample every high-consequence page claim back to its closest authoritative evidence, and sample each important source constraint forward to the page decision that represents it. The first direction finds unsupported claims; the second finds omitted constraints.

## Theme Specific Artifact

**Artifact:** a source-grounded explainer brief and storyboard. It is a pre-build decision contract and a post-build evidence index, not a second copy of the final page. Store it in the task's normal planning surface; the schema matters more than a particular filename.

| artifact_field_name | completion_rule | evidence_or_quality_test | post_build_reconciliation |
| --- | --- | --- | --- |
| `reader_role_and_starting_state` | Name a concrete reader, what they already know, and the gap preventing the next decision or prediction. | A role label such as "developer" is insufficient without prior knowledge and task context. | Confirm the final page does not assume terms or context absent from the stated starting state. |
| `reader_outcome_or_prediction` | State one primary question the reader can answer, choice they can justify, or behavior they can predict. | Reject goals such as "understand the system" that cannot be observed. | Run the target-reader task when consequence warrants it; otherwise mark comprehension `not_evaluated`. |
| `one_sentence_thesis` | Compress the subject's purpose and mechanism into one accurate, bounded sentence. | Trace every noun and verb to inspected subject evidence. | Compare with the final takeaway; disagreement requires narrative or brief revision. |
| `scope_and_non_goals` | Name included path, excluded detail, environment, and claims intentionally left unresolved. | Check exclusions against the user's decision and the highest-risk source gaps. | Verify links or companion artifacts carry optional depth without hiding essential meaning. |
| `source_and_claim_ledger` | List the minimum subject sources and the major claim each supports; mark conflict and uncertainty. | Sample both claim-to-source and source-to-represented-decision directions. | Update paths and statuses; record any final claim introduced after briefing. |
| `actors_and_exact_vocabulary` | Define the primary actors, state objects, boundaries, and exact source terms once in plain language. | Reject renamed concepts that create false simplicity or collide with source terminology. | Scan the page for inconsistent aliases and unexplained jargon. |
| `core_causal_path` | Write the mechanism as source-named steps, branches, or transformations and identify the earliest safe reveal point. | A reviewer can predict what happens next at each transition and identify its evidence. | Confirm the mechanism appears by the second act unless a documented audience reason changes the order. |
| `state_safety_and_recovery` | When applicable, identify tentative and durable state, commit timing, crash behavior, retry boundary, and unknown guarantee. | Mark `not_applicable` with rationale for genuinely stateless subjects; never manufacture a state act. | Verify diagrams and wording do not imply stronger semantics than source evidence. |
| `variants_boundaries_and_tradeoffs` | List only comparisons and extension seams that change a reader decision; preserve real asymmetry. | Trace every side of a comparison independently and remove empty categories. | Check responsive presentation and ensure no path is visually promoted without reason. |
| `surprises_and_misconceptions` | Name up to three details likely to produce an incorrect mental model and how the story corrects each one. | Draw from tests, issue history, conflicting notes, or explicit owner input rather than generic pitfalls. | Use reader findings to add, remove, or reprioritize misconceptions. |
| `act_storyboard` | For each retained act, record its reader question, answer, source, transition from the prior act, and exit takeaway. | Delete acts whose answer duplicates another section or does not advance the primary outcome. | Map final sections back to acts and explain every substantial divergence. |
| `component_information_roles` | Assign each diagram, flow, comparison, excerpt, table, or control a unique relation it expresses better than prose. | Ask what information disappears if the component is removed. | Remove decorative or redundant components; add tests for retained interactive complexity. |
| `static_and_alternate_reading_plan` | Define semantic document order, script-failure behavior, keyboard route, reduced-motion response, narrow layout, and optional asset fallback. | Essential mechanism and caveats must remain reachable without motion, pointer-only interaction, or successful enhancement scripts. | Execute declared conditions and attach concise evidence or unresolved findings. |
| `visual_direction_and_density` | Choose one subject-appropriate visual direction, text measure, hierarchy, and component density; note existing tone to preserve. | Reject a grab bag of widgets or visual treatment that competes with inspectable subject information. | Review screenshots for scan path, contrast, fit, repeated containers, and unintended emphasis. |
| `source_footer_and_attribution` | List key files or notes and identify where disputed or surprising claims need closer inline attribution. | A footer path list must be sufficient to reopen evidence; broad roots alone are not traceability. | Confirm all final major sources appear and removed sources no longer imply support. |
| `verification_and_handoff` | Declare artifact path, target environments, gate methods, expected outcomes, owner, refresh trigger, and evidence retention. | Include pass, fail, and not-evaluated states; avoid a single undifferentiated completion claim. | Record final hash, commands, browser conditions, screenshots tied to findings, reader evidence, and residual risks. |

**Minimum durable subset for a short-lived internal page:** reader outcome, thesis, scope, source ledger, causal path, act storyboard, alternate reading plan, target conditions, and final proof. A maintained or public artifact should retain every applicable field and its post-build reconciliation.

Review the brief before broad implementation. Any unresolved field blocks only work that depends on it; for example, uncertain delivery semantics block a guarantee diagram but need not block a source-backed architecture overview. Any substantial final component absent from the brief must either be added with rationale and evidence or removed from the page.

## Worked Example Set

`combined_evidence_inference_note`: All systems, artifacts, findings, and outcomes in these cases are illustrative. They demonstrate review decisions, not repository incidents or measured production results.

**Good case: a restart path explainer with a repaired state defect**

- **Inputs:** an ingestion worker entry point, state interface, restart tests, architecture note, and one issue describing a past misunderstanding. The audience question is whether a crash resumes before or after the last durable checkpoint.
- **Decisions:** the author uses six acts rather than retaining all seven scaffold acts. The core poll-transform-apply-persist path appears in Act II. A branch diagram distinguishes tentative work from durable progress; one short recovery test excerpt anchors the surprising branch. A broad exactly-once claim is excluded because the sources do not establish it.
- **Artifact:** essential sections are visible in source order without enhancement scripts. The page uses one comparison, one branch diagram, and one excerpt rather than repeating the loop in several cards. The footer lists every inspected artifact.
- **Verification finding:** claim review catches wording that implies persistence happens before application, while a narrow screenshot catches a clipped state label. Both are repaired and the relevant checks rerun. A target reader can then restate the sequence and predict the documented restart branch; no population-level comprehension claim is made.
- **Disposition:** accept for the declared internal onboarding use, with the unresolved end-to-end guarantee visibly out of scope. Transfer the source-first narrowing and repair loop, not the example's event-processing vocabulary.

**Bad case: a polished architecture tour shaped by the scaffold**

- **Inputs:** only a top-level README and filenames, despite available interfaces and tests. The author starts from the template and assumes every system has two comparable modes, a retry split, and persisted progress.
- **Decisions:** seven acts are retained because they already exist. "Path A" and "Path B" receive symmetric cards, a library metaphor substitutes for actual storage semantics, and generic transient-versus-fatal examples appear without source support. Scroll reveals leave sections initially invisible, and no script-failure path is checked.
- **Artifact:** visual consistency and responsive card collapse look competent at one desktop width. The footer cites the repository root, but a reviewer cannot connect major claims to files. A long code excerpt creates technical texture without explaining why it matters.
- **Verification finding:** desktop screenshots pass a superficial visual review, yet source comparison reveals invented state and failure behavior. Keyboard and script-off checks were not evaluated, and the reader outcome was never defined.
- **Disposition:** reject as an authoritative explainer. Preserve any independently useful CSS only if ownership permits; rebuild the evidence model and narrative before further polish. The important diagnostic is that scaffold assumptions entered before subject evidence stabilized.

**Borderline case: a useful subsystem map with an unsupported recovery claim**

- **Inputs:** reliable architecture and interface sources support actor boundaries and the happy path, but recovery tests and state ownership are missing. The reader needs both an architecture overview and restart guidance.
- **Decisions:** the author creates a clear four-act map and labels uncertainty in prose, but a summary diagram still draws a restart arrow that implies a specific recovery point. The page opens locally, fits declared viewports, and preserves keyboard reading order.
- **Artifact:** source fidelity is strong for boundaries and weak for recovery. The warning is easy to miss because the diagram carries more visual weight than the caveat.
- **Verification finding:** bidirectional claim review identifies the restart arrow as unsupported. Rendering checks cannot resolve the semantic gap, and no source owner has confirmed the behavior.
- **Disposition:** do not average good layout and accurate architecture against the unsupported high-impact claim. Either remove recovery from scope and accept the page as an architecture explainer, or obtain the missing evidence and rebuild that act. Borderline is a temporary state with a named route to narrow, repair, or reject.

Classify by the highest unresolved semantic or access risk. A low-impact spacing defect need not block an internal draft; an invented guarantee or inaccessible essential caveat does. Proposed checks in a hypothetical example are not collected evidence, so apply the real gate to the real artifact.

## Outcome Metrics and Feedback Loops

Do not infer comprehension from page views, scroll depth, visual polish, or the author's confidence. Define the reader task, artifact version, environment, sample, rubric, and response before interpreting a result. No universal numeric effectiveness target is established by the local corpus.

| signal | collection_method_and_denominator | interpretation_boundary | required_response |
| --- | --- | --- | --- |
| `major_claim_traceability` | Sample every high-consequence mechanism, state, failure, and guarantee claim plus representative lower-risk claims; record supported, inferred, conflicting, or unknown. | A listed source is not enough; the inspected artifact must entail the claim. Unknown is not a traced pass. | Remove, narrow, attribute, or escalate unsupported content before authoritative sharing. |
| `core_mechanism_discoverability` | Give a cold reviewer the page and ask them to locate and restate the causal path; record where they found it and what they omitted. | Fast location does not prove correct understanding, but delayed discovery indicates pacing or hierarchy risk. | Move or simplify the heartbeat, then repeat with the same task on the new artifact hash. |
| `reader_prediction_quality` | Ask the declared reader to predict one meaningful state transition, failure, comparison outcome, or recovery path and explain the reasoning. | Report observed answers and rubric; do not generalize a small sample to a population. | Diagnose the exact misconception, repair the earliest responsible act or component, and retest when consequence justifies it. |
| `uncertainty_visibility` | Ask reviewers to identify what the page does not establish and where deeper evidence lives. | A caveat that exists but is visually or navigationally buried has failed its purpose. | Rebalance emphasis, narrow the main claim, or route unresolved behavior more clearly. |
| `alternate_reading_coverage` | Execute every declared viewport, keyboard, reduced-motion, script-failure, and optional-asset condition; count pass, fail, and not-evaluated separately. | Coverage is relative to the declared support matrix, which must itself fit the audience and delivery surface. | Block or disclose affected paths according to semantic impact; never count missing evaluation as pass. |
| `scaffold_and_generic_residue` | Scan visible and source text for template tokens, sample labels, generic failures, and unexplained example categories, followed by human review of matches. | A zero-match scan does not prove subject specificity, while a textual match can be legitimate. | Replace or delete unsupported residue and rerun claim review for surrounding content. |
| `reproduction_and_local_open_success` | From a fresh recorded environment, open or regenerate the exact artifact using retained inputs and invocation; record failures and external requests. | One environment proves only that environment and artifact bytes. | Repair portability, narrow the support claim, or document the required runtime explicitly. |
| `review_rework_location` | Classify findings by source model, narrative, component, or runtime layer and track where accepted repairs occur. | Counts are diagnostic, not productivity scores; a difficult source domain may naturally create more upstream findings. | If repeated defects cluster downstream from one root, change the brief or scaffold workflow rather than patching outputs repeatedly. |
| `refresh_effort_and_drift` | At each source-triggered update, record affected claims, acts, components, evidence rerun, and whether final compression changed. | First-refresh data is a baseline, not a universal maintenance estimate. | Simplify duplication, improve provenance, or re-architect packaging when updates repeatedly require broad rereads or rebuilds. |
| `author_support_dependency` | Record questions a target reader must ask the author before completing the declared outcome, including the missing context. | Zero questions can indicate clarity or disengagement; combine with the prediction task. | Add only the missing context that changes the outcome, or narrow the promise when the page cannot remain self-sufficient. |

**Minimum internal feedback loop:** run structural and alternate-path gates; conduct claim sampling; ask one outcome-aligned prediction when a suitable reader is available; classify findings by responsible layer; repair the highest-impact issue; rerun affected checks; and record residual uncertainty. Mark reader comprehension `not_evaluated` when no suitable sample exists.

**Maintained-artifact loop:** attach the artifact hash, audience, task prompt, rubric, environment, and source versions to every measurement record. Review after a source change, target-environment change, reported misconception, failed gate, or meaningful audience change rather than on an arbitrary universal calendar. Repeatedly compare the final compression sentence with current source behavior as a cheap drift signal.

Audit the metrics themselves. If component clicks encourage adding controls, page views reward broad promotion, or easy recall questions replace causal prediction, the measurement system is changing the artifact away from its promise. Retain qualitative misconceptions and repair decisions alongside any aggregate; those details often carry more diagnostic value than a rate.

## Completeness Checklist

Use `pass`, `fail`, `not_applicable_with_reason`, and `not_evaluated` explicitly. An omitted scenario is not a pass. Critical evidence is bound to the artifact hash; substantive byte changes invalidate affected checks.

**Scope and evidence readiness**

- [ ] The primary reader, starting knowledge, decision or prediction, and artifact trigger are concrete.
- [ ] The one-sentence thesis, included causal path, non-goals, and unresolved questions are source-bounded.
- [ ] Method sources and subject sources were read completely for every claim that depends on them.
- [ ] Major mechanism, state, failure, boundary, guarantee, and tradeoff claims map to inspected evidence or carry a visible inference, conflict, or unknown label.
- [ ] Output path and edit ownership are explicit; concurrent work and existing artifacts will be preserved.
- [ ] HTML is preferable to a lighter explanation medium for a named reader benefit, or an explicit user requirement governs the choice.

**Narrative and content model**

- [ ] The page opens with the real problem, decision, or direct mechanism appropriate to audience knowledge.
- [ ] The core loop, lifecycle, branch, transformation, or dependency path is visible by the second act unless a documented reason changes the order.
- [ ] Exact source nouns and verbs are defined once and then used consistently.
- [ ] Every metaphor returns immediately to mechanics and can be removed without making the explanation incomplete.
- [ ] State, safety, persistence, restart, retry, and guarantee semantics are included only where applicable and supported.
- [ ] Comparisons preserve real asymmetry; no empty counterpart was created to fit a card layout.
- [ ] Failure modes and tradeoffs use concrete subject evidence rather than scaffold examples.
- [ ] The final compression is accurate, bounded, memorable, and useful as a future drift signal.

**Storyboard and component discipline**

- [ ] Every retained act answers one reader question and advances the declared outcome.
- [ ] Unused scaffold acts, generic labels, sample state, example failures, replacement prompts, and template tokens are gone.
- [ ] Each flow, diagram, comparison, code excerpt, option set, table, or control has a unique information role.
- [ ] Code excerpts are short, source-linked, interpreted, and selected for a decisive mechanism rather than technical texture.
- [ ] Text-first diagrams remain meaningful when copied or read without styling.
- [ ] Visual direction and component density fit the subject; repeated cards or decoration do not dominate the explanation.

**HTML, responsive, and alternate reading paths**

- [ ] The document has meaningful language, title, viewport metadata, semantic reading order, and one clear top-level title.
- [ ] The final file opens directly under the declared local condition, or any required runtime is stated and reproducible.
- [ ] Essential content is visible and ordered when enhancement JavaScript is unavailable.
- [ ] Keyboard-only reading reaches every meaningful control, focus is visible, and no required action depends on hover.
- [ ] Reduced-motion behavior preserves orientation without animation-dependent meaning.
- [ ] Declared narrow, medium, and wide widths have no incoherent overlap, clipping, hidden caveat, or uncontrolled page-level overflow.
- [ ] Long code, tables, diagrams, identifiers, and source paths have deliberate wrapping, reflow, or contained scrolling.
- [ ] Optional fonts, images, and other assets have acceptable failure behavior; external requests and privacy implications are known.
- [ ] Console and network findings are reviewed under declared conditions; failures are repaired, disclosed, or removed.

**Source truth, reader outcome, and handoff**

- [ ] Claim-to-source and source-to-represented-decision samples pass for all high-consequence content.
- [ ] A cold reviewer can locate and restate the core mechanism without hidden author context.
- [ ] A target-reader prediction or decision task was run when consequence warrants it, or comprehension is marked `not_evaluated`.
- [ ] The source footer lists the key files and notes; surprising or disputed claims receive closer attribution where needed.
- [ ] The pre-build brief and final artifact are reconciled; every substantial divergence has rationale and evidence.
- [ ] Exact artifact hash, commands, working directory, browser or environment conditions, declared matrix, concise outcomes, and residual risks are retained.
- [ ] Refresh triggers and owner are named for source change, target change, reported misconception, or dependency drift.
- [ ] Adjacent references or companion artifacts carry exhaustive, operational, or alternate-medium detail without hiding essentials.

**Final complete pass**

- [ ] Reread the page from beginning to end as an argument, checking transitions, emphasis, omissions, repetition, caveat visibility, and final compression.
- [ ] Repeat the complete reading through at least the narrow keyboard path and any other declared high-risk condition.
- [ ] Confirm that local section repairs did not introduce a whole-page contradiction or shift the audience promise.
- [ ] Review all `not_evaluated`, exceptions, and warnings as explicit risk decisions before completion is reported.

For a short-lived internal page, evidence retention may be smaller, but truth, ownership, essential static access, responsive fit, and source provenance remain core. Formal accessibility or broad compatibility claims require the appropriate current standards evidence and specialist process; this checklist alone does not certify them.

## Adjacent Reference Routing

Retain this reference when the essential deliverable is a bounded, directly openable browser journey whose narrative order and visual relations improve a technical mental model. Pair it with another artifact when readers need a different moment of use. Replace it when another medium or runtime carries the primary outcome more directly.

The paths below exist in the current repository inventory but were not read as evidence for this assignment. Treat each as a candidate: inspect its current contents, evidence boundaries, and verification gates before use.

| reader_or_output_need | route_decision | adjacent_reference_candidate | handoff_and_verification_rule |
| --- | --- | --- | --- |
| A visual explainer requiring a different or broader visual-explanation workflow | Inspect and decide whether to pair or replace. | `idiomatic-ref-202607/visual_explainer_skill_patterns-20260710.md` | Hand off audience, thesis, source ledger, causal path, uncertainty, and intended interaction; do not transfer HTML screenshot evidence automatically. |
| A diagram that must survive terminal display and plain-text copy-paste | Replace the diagram work with ASCII guidance; optionally embed the verified result in the HTML page. | `idiomatic-ref-202607/ascii_diagram_layout_patterns-20260710.md` | Preserve exact system relations and test the diagram in its native text surface before responsive HTML embedding. |
| A primarily argumentative memo or top-down written explanation | Replace or pair according to whether browser presentation adds an essential relation. | `idiomatic-ref-202607/minto_pyramid_writing_patterns-20260710.md` | Transfer governing question and evidence, then re-evaluate sequence for the written medium rather than copying acts mechanically. |
| A reusable writing workflow or authoring-skill validation task | Route the method-building portion away from the page artifact. | `idiomatic-ref-202607/writing_skills_validation_patterns-20260710.md` | Keep page-specific source and browser checks here; verify the destination before claiming skill-level behavior. |
| A custom bitmap image, illustration, texture, or visual asset is the principal deliverable | Replace asset generation work; pair only when the final page truly needs the asset. | `idiomatic-ref-202607/image_generation_prompt_patterns-20260710.md` | Record asset purpose, provenance, licensing or policy constraints, loading fallback, size, and whether the image conveys inspectable subject evidence. |
| An immersive or essential 3D visualization carries the explanation | Replace the single-file baseline with the appropriate tested visualization architecture. | `idiomatic-ref-202607/threejs_react_visualization_patterns-20260710.md` | Preserve the evidence model but establish new scene, interaction, performance, fallback, and viewport proof; the current page gates are insufficient. |
| Current OpenAI API facts, product behavior, or cited official documentation dominate the content | Pair the narrative artifact with current documentation research or route the factual task first. | `idiomatic-ref-202607/openai_api_documentation_patterns-20260710.md` | Refresh authoritative sources before drafting; do not use this no-browse reference to establish current API behavior. |
| The primary need is exhaustive API lookup rather than a guided journey | Replace the main deliverable with a reference-oriented documentation surface; retain HTML only as an optional overview. | Inspect the domain's documentation reference before selection. | Make essential signatures, constraints, and version facts searchable and source-linked; avoid forcing them through story pacing. |
| The primary need is a stateful operational tool with authentication, live data, or repeated user actions | Replace with a tested frontend or application workflow. | Inspect the repository's relevant frontend or application reference before selection. | Carry forward subject truth and user outcome, then define application states, security boundaries, persistence, and runtime tests independently. |

**Retain example:** the page explains a recovery lifecycle and needs only one static branch diagram. **Pair example:** an HTML onboarding journey links to an exhaustive API reference and an operational dashboard, each serving a separate reader moment. **Replace example:** a request for a live authenticated simulator is an application task even if the user also calls it an explainer.

Every handoff includes the reader and starting state, promised outcome, one-sentence thesis, source and claim ledger, scope and non-goals, unresolved questions, output ownership, and proof expected from the destination. The route is valid only when it states why this reference stops and why the candidate begins. If no candidate fits, return to task planning rather than selecting by filename resemblance.

Evidence about subject behavior may transfer when the source and scope remain identical. Narrative fit, accessibility, rendering, interaction, and comprehension evidence belong to the actual output medium and must be recollected there.

## Workload Model

`combined_evidence_inference_note`: Treat Html Explainer Page Patterns as a frontend experience operating reference, not as a prose summary.

The sourced baseline is one directly openable file and roughly five to eight useful acts. That range is a pacing default, not a universal capacity number. Delete simple subjects down to fewer acts. Split or change architecture when independent outcomes, owners, or runtime needs weaken one coherent journey.

| workload_dimension_name | healthy_single_explainer_signal | pressure_or_boundary_signal | least_disruptive_response |
| --- | --- | --- | --- |
| `audience_and_outcome` | One primary reader starting state and one prediction, decision, or causal model organize all acts. | Different audiences require incompatible prerequisites, vocabulary, depth, or actions. | Create a shared bounded overview plus audience-specific companion journeys, or select one primary audience explicitly. |
| `causal_cohesion` | Steps, branches, variants, and caveats contribute to one thesis and share enough context to build progressively. | Acts contain independent systems or several unrelated heartbeats that can be read in any order. | Narrow to the central relation, split by lifecycle or subsystem, and preserve clear routing. |
| `claim_and_evidence_pressure` | Major claims map to a minimum trustworthy source set with visible uncertainty and manageable conflict. | High-consequence claims depend on different owners, stale sources, or unresolved contradictions. | Isolate uncertain claims, split ownership, or stop that act until evidence is resolved; do not fill gaps from convention. |
| `state_and_variant_pressure` | State, modes, and comparisons share meaningful dimensions and fit a readable causal model. | Variants have unrelated state machines, false symmetry, or enough branches that the main outcome disappears. | Compare only the central decision dimensions or create separate deep dives linked from a high-level overview. |
| `narrative_density` | Each act answers one question, transitions naturally, and contains only detail needed for the next prediction. | Sections become reference catalogs, repeated explanations, or dense caveat collections that break pacing. | Move exhaustive material to companion documentation, strengthen scope, and keep the journey as an entry surface. |
| `component_pressure` | Each diagram, flow, excerpt, table, or control has a unique information role and a clear responsive plan. | The page becomes a widget gallery, repeated cards dominate, or components need more explanation than the relation they show. | Remove or consolidate components and return the relation to prose or a simpler text-first diagram. |
| `runtime_and_dependency_pressure` | Essential content is static; optional scripts and assets have bounded, testable failure behavior. | Authentication, server state, live updates, large media, complex controls, or external dependencies become essential. | Route to a tested frontend or application architecture; retain a static explainer only as a companion overview. |
| `support_matrix_pressure` | Declared viewport, input, motion, script, asset, and browser conditions are proportionate to audience and can be exercised. | Target combinations multiply beyond owned test capacity or carry incompatible layout and interaction designs. | Narrow declared support honestly, automate stable high-value paths, or split delivery surfaces with clear ownership. |
| `lifecycle_and_reuse_pressure` | One owner can refresh the page when its bounded sources or audience change. | Multiple pages duplicate styles and facts, source volatility causes broad rewrites, or shared behavior needs coordinated releases. | Introduce shared infrastructure only after reuse is demonstrated; separate content truth from presentation code and migrate with regression evidence. |
| `ownership_pressure` | One artifact owner can reconcile subject, narrative, and runtime findings with named source owners. | Parallel contributors edit the same output, method and subject disputes lack escalation, or no one owns stale claims. | Split exclusive paths and responsibilities, establish merge or review checkpoints, and retain one final verification owner. |

**Pre-build capacity review:** map every major claim to an act, every act to the primary outcome, every component to an information role, and every retained dependency to an alternate-state check. If several items cannot be connected without vague transitions, reduce scope before styling. Use observed counts as local signals, not universal thresholds.

**Fit example:** one onboarding page compares two adapters only along the shared setup, state, and recovery decision. **Overloaded example:** one file attempts to be tutorial, exhaustive API reference, live dashboard, and simulator for three independent systems. **Borderline example:** two implementations have different state models; keep them together only when explaining that asymmetry is the reader's central decision.

Revisit the model after the first substantive refresh. Record which sources, claims, acts, components, and gates changed. Broad unexpected impact indicates that the original workload boundary or packaging choice was too coupled. A page has crossed the application boundary when runtime requirements become an independent product surface rather than optional support for the explanatory story.

## Reliability Target

Reliability means that the intended reader receives a truthful, reachable, reproducible, and maintainable explanation under declared conditions. It does not mean universal browser support, formal accessibility conformance, or a measured comprehension rate unless those claims have their own current evidence.

| reliability_dimension | target_type_and_acceptance_boundary | evidence_collection_method | miss_response |
| --- | --- | --- | --- |
| `high_consequence_claim_truth` | **Critical invariant:** no mechanism, state transition, recovery behavior, guarantee, security property, or runtime claim is presented as settled without supporting evidence or visible uncertainty. | Sample all high-consequence claims against inspected subject artifacts; preserve conflict and unknown states. | Block authoritative sharing of the affected claim; remove, narrow, attribute, or escalate it. |
| `essential_content_reachability` | **Critical invariant:** the core mechanism, important caveats, source route, and final takeaway are reachable on every declared essential viewport, input, motion, and script condition. | Execute the declared matrix with screenshots or interaction notes tied to findings; inspect static document order. | Block the affected support path or narrow the declared promise until repaired and rerun. |
| `narrative_causal_integrity` | **Critical invariant:** ordering, emphasis, metaphor, and visuals do not alter the source-backed causal model or hide a material boundary. | Cold review of mechanism restatement, metaphor removal test, and claim review of diagrams and summaries. | Repair the earliest responsible act or component and repeat dependent reader tasks. |
| `artifact_reproducibility` | **Core objective:** another reviewer can open or regenerate the exact artifact under the documented local conditions from retained inputs without author-only knowledge. | Record output hash, command or opening path, working directory, required dependencies, and fresh-environment result. | Fix the workflow, narrow portability claims, or document the required runtime explicitly. |
| `provenance_and_evidence_validity` | **Critical invariant:** proof is tied to the artifact bytes, source versions, and test conditions it actually covers. | Store hashes or version identifiers, claim ledger, evidence dates, and change-impact decisions. | Invalidate stale evidence and rerun affected gates; do not reuse screenshots or reader findings across unknown changes. |
| `uncertainty_and_recovery_clarity` | **Core objective:** every avoid, unknown, failed path, and unsupported claim names the consequence and next owner, evidence need, rollback, or adjacent route. | Ask a reviewer to locate limitations and state what happens next; inspect failure and routing sections together. | Increase visibility, assign ownership, or reduce scope before completion. |
| `reader_outcome_quality` | **Locally calibrated objective:** target readers can perform the declared prediction or decision task to the artifact owner's explicit rubric. | Record task, rubric, audience, sample, observed misconceptions, and artifact hash. | Diagnose misunderstanding, repair the responsible layer, and avoid generalizing beyond observed readers. |
| `responsive_and_interaction_stability` | **Declared-matrix objective:** no incoherent overlap, clipping of essential text, invisible focus, pointer-only requirement, or script-caused content loss occurs in tested conditions. | Targeted viewport captures, keyboard traversal, reduced-motion run, script or optional-asset failure, and console review. | Classify semantic impact, repair or disclose, then rerun the affected condition. |
| `refreshability` | **Lifecycle objective:** a source or audience change can be traced to affected claims, acts, components, and gates without unaudited whole-page drift. | Use brief-to-artifact traceability and record impact plus effort at each substantive refresh. | Improve source mapping, reduce duplication, split workload, or change packaging when broad unexpected impact repeats. |

The frozen sample target of "18 of 20" has no supplied rubric, baseline, or corpus and is not retained. Numeric objectives may be introduced only with an owner, sample definition, measurement method, baseline, decision consequence, and stated uncertainty. Binary invariants are reserved for clearly defined critical defects, not subjective polish.

**No-compensation rule:** excellent visual quality, load speed, or reader satisfaction cannot offset an unsupported high-consequence claim or inaccessible essential caveat. Apply this weakest-link rule only to declared critical dimensions; track low-severity visual and editorial findings separately so they do not block proportionate internal use.

Every reliability record names artifact hash, audience, support conditions, source versions, methods, pass or fail or not-evaluated status, and residual risk. A change invalidates only evidence whose dependency is affected when that impact can be shown; otherwise rerun conservatively.

## Failure Mode Table

Classify consequence for the declared reader and artifact status. Critical semantic or essential-access failures block authoritative use; lower-impact quality findings may be documented for a draft. Repair the earliest responsible layer and retire any evidence invalidated by the change.

| failure_mode_name | detection_and_reader_impact | immediate_containment | durable_repair_and_owner | recovery_proof |
| --- | --- | --- | --- | --- |
| `unsupported_or_false_high_consequence_claim` | Source comparison finds an invented guarantee, transition, security property, or recovery behavior that can drive a wrong decision. | Remove or visibly withdraw the claim; stop authoritative sharing of the affected artifact. | Subject owner supplies evidence or narrows semantics; narrative owner reconciles diagrams, summaries, and takeaway. | Repeat claim sampling and the reader prediction affected by the false model; retire stale copies where distribution warrants it. |
| `source_drift_invalidates_causal_model` | Implementation or specification changes make an act or final compression inaccurate. | Mark the page stale or restrict use before readers rely on old behavior. | Artifact owner traces changed sources to claims, acts, components, and gates, then updates the brief and page. | Record old and new source versions, compression, artifact hash, impacted checks, and residual uncertainty. |
| `conflicting_evidence_hidden` | Prose, tests, implementation, or owner statements disagree while the page presents one settled story. | Restore visible conflict and avoid selecting a convenient interpretation. | Route method, subject, or observed-behavior conflict to the appropriate owner; record the resulting decision separately. | Bidirectional evidence review confirms the resolution or the page's bounded unknown state. |
| `reader_outcome_mismatch` | Target readers can navigate the page but cannot perform the promised prediction or decision, or consistently infer the wrong outcome. | Avoid claiming comprehension; provide the source route or corrected operational guidance separately if needed. | Narrative owner repairs the earliest misunderstood relation, wording, emphasis, or component after diagnosing the misconception. | Repeat the same task against the new hash and record answer plus rubric without overgeneralizing the sample. |
| `scaffold_semantics_escape` | Generic modes, retry examples, state labels, or replacement text are mistaken for subject behavior. | Remove the affected component or label the artifact as incomplete. | Author rebuilds that act from subject evidence and adds a residue scan plus human scaffold review. | Text scan is clean, every retained category traces to evidence, and the complete story remains coherent. |
| `essential_content_hidden_by_script` | Reveal CSS, observer failure, or JavaScript error leaves the mechanism or caveat invisible. | Disable the hiding behavior or serve a static visible fallback. | Frontend owner makes content visible by default and layers enhancement without changing semantic order. | Script-off and forced-failure runs reach all essential content; console findings are reviewed. |
| `keyboard_or_focus_path_breaks` | Controls cannot be reached or operated, focus disappears, or order no longer matches the argument. | Expose an equivalent static route or remove the nonessential control. | Frontend owner uses semantic controls, restores focus visibility and order, and avoids pointer-only behavior. | Complete the declared keyboard path at target widths and retain focused-state evidence for repaired defects. |
| `reduced_motion_path_disorients` | Smooth scrolling or reveals ignore preference, hide sequence, or cause disorientation. | Disable nonessential transitions for the affected path. | Frontend owner implements preference-aware behavior and ensures content order carries the story without motion. | Repeat navigation under reduced motion and verify equivalent orientation and meaning. |
| `narrow_layout_hides_or_distorts_meaning` | Text, table cells, code, diagrams, or labels clip, overlap, reorder incorrectly, or require incoherent page scrolling. | Narrow declared support or provide an alternate readable representation until repaired. | Layout owner reflows or contains the specific component without changing information priority silently. | Capture affected widths, inspect full journey and focus, and rerun any screenshot or reader evidence dependent on layout. |
| `optional_asset_becomes_required` | Font, image, media, or network request fails and removes meaning, destabilizes layout, or prevents direct opening. | Fall back to local text or remove the dependency from the essential path. | Artifact owner makes the asset optional, packages it appropriately, or documents a required runtime with privacy and loading controls. | Block the resource deliberately and verify content, layout, source attribution, and console behavior. |
| `artifact_cannot_be_reproduced` | A teammate cannot open or regenerate the output from recorded inputs, or a helper risks overwriting valued work. | Preserve existing bytes and stop destructive generation. | Workflow owner records exact invocation, environment, dependencies, output protection, source list, and artifact hash. | Reproduce in a fresh temporary location and verify overwrite refusal or the approved replacement path. |
| `evidence_outlives_artifact` | Screenshots, reader findings, or command results refer to older bytes or conditions but remain presented as current. | Mark evidence stale and remove it from the completion claim. | Artifact owner performs impact analysis and recollects affected evidence with current hash and environment. | Evidence index contains no unqualified item whose dependency version is unknown. |
| `ownership_collision_or_absence` | Parallel edits conflict, source questions have no decision owner, or stale content persists because responsibilities are implicit. | Freeze overlapping writes and preserve all durable work. | Coordinator assigns exclusive paths, subject and method escalation, merge checkpoints, and final verification ownership. | Changed-path audit and handoff record show one accountable owner for each unresolved risk. |

Several low-severity failures can combine into an essential-path failure, such as hidden navigation plus clipped content plus a failed font. Review the journey as a whole after focused repairs. A warning is useful containment for genuine uncertainty, but it does not neutralize a visually dominant contradictory claim.

For high-impact misinformation already shared, recovery may include correcting linked documents, notifying the affected audience, retiring stale screenshots, or recording the superseding artifact. Scale that response to distribution and consequence rather than treating file repair as automatically sufficient.

## Retry Backpressure Guidance

Retry only when repeating the smallest operation can plausibly change its result without changing the unresolved question. A changed source, clarified requirement, repaired artifact, or new owner decision begins a new evidence cycle; calling it a retry would hide the input that enabled progress.

**Retry contract:** classify the failure; persist current artifact and evidence; establish idempotency or a disposable target; define why another attempt should differ; bound attempts by local cost and risk; compare outcomes; then accept, fall back, escalate, narrow, or stop. An unchanged failure signal after the planned bound is diagnosis evidence, not permission for another identical loop.

| failure_class | retry_eligibility | backpressure_and_safe_response | evidence_before_continuing |
| --- | --- | --- | --- |
| Temporary browser, process, or capture interruption | Eligible when environment recovery is observable and the operation does not mutate valued output. | Preserve artifact hash, restart only the failed tool or capture, and label each attempt. | Environment change, exact condition, attempt outcome, and final screenshot or interaction evidence. |
| Optional font, image, or network resource unavailable | Retry only when the dependency is declared and transient; otherwise exercise fallback. | Keep essential content available, remove the dependency, or narrow support instead of looping. | Blocked-resource test plus proof that meaning and layout survive the chosen response. |
| Static check or generation command fails deterministically | Not eligible until the command, input, path, or implementation changes. | Diagnose the first failing assertion; use a temporary destination; never add `--force` merely to bypass overwrite protection. | Reproduction, root cause, focused change, and a passing rerun against preserved or disposable output. |
| Flaky visual or interaction result | A bounded replication is eligible only with fixed artifact bytes, conditions, and a hypothesis about instability. | Do not select the favorable attempt; classify environment noise, race, font variance, or actual nondeterminism. | All attempt summaries, condition differences, and the stabilization or accepted uncertainty decision. |
| Missing subject source or owner decision | Not retryable because repetition cannot create authority. | Stop dependent claims and components; request evidence, mark unknown, narrow scope, or route to the responsible owner. | New inspected source or explicit decision with provenance before dependent drafting resumes. |
| Contradictory implementation, test, specification, or prose | Not retryable as a generation problem. | Preserve the conflict, stop authoritative synthesis of that claim, and escalate by claim type. | Recorded resolution, bounded uncertainty, or scope removal plus updated claim ledger. |
| Reader misunderstands the intended mechanism | Repeating the same task on unchanged wording is not repair. | Diagnose the misconception, change the earliest responsible act or component, then rerun the outcome task. | New artifact hash, changed rationale, same or deliberately revised rubric, and observed response. |
| Ownership collision or concurrent edit conflict | Not retryable through overwrite or repeated patching. | Freeze overlapping writes, preserve all durable work, re-establish exclusive paths, and reconcile at a named checkpoint. | Ownership decision, changed-path audit, and post-merge heading, evidence, and behavior gates. |
| Stale external pointer | Refresh only when browsing is authorized and the unresolved decision requires current external evidence. | Keep current claim unknown; perform targeted primary-source research rather than broad repeated search. | Exact inspected page, section, date, supported proposition, applicability, and artifact consequence. |

**Dependency-scoped backpressure:** a red source claim stops only acts, diagrams, summaries, and metrics that depend on it. A red essential-content gate stops authoritative sharing on that support path. Independent evidence gathering or disposable prototypes may continue when they cannot overwrite work or turn provisional assumptions into accepted content. Downstream visual investment never converts an upstream unknown into a pass.

For long-running or shared work, persist atomic progress before moving on: complete the smallest packet or plan unit, save the matching artifact change, run focused sanity, and record the durable boundary. Re-read governing requirements before broad rewrites or after context transitions. One owner controls each output path, and one final verifier reconciles cross-section and whole-page behavior.

**Minimal retry record:** artifact hash, failure class, affected gate, preserved state, hypothesis, why the attempt may differ, operation and environment, attempt outcome, comparison, and final disposition. Keep summaries small and decision-bearing. Raw repeated logs without a changed hypothesis are not useful progress evidence.

## Observability Checklist

Collect the smallest evidence set that can reproduce a finding, show coverage, assign responsibility, and detect staleness. Do not retain raw transcripts, reader behavior, sensitive source detail, or screenshot collections merely because collection is easy.

**Provenance and content truth**

- [ ] Record every inspected method and subject source, its relevant version or hash when practical, and the decision it changed.
- [ ] Record intentionally skipped sources and why their absence does or does not narrow the page.
- [ ] Track major claims as supported, inferred, conflicting, or unknown; keep local, refreshed external, and combined inference boundaries visible.
- [ ] Record the source footer and any closer attribution used for surprising or disputed claims.
- [ ] Review provenance for sensitive paths, code, operational detail, credentials, personal data, or information that should not enter a shared artifact.

**Artifact identity and reproduction**

- [ ] Record the exact output path, artifact hash, generation or opening command, working directory, and required runtime or dependencies.
- [ ] Record whether output was generated into a new or disposable path and how overwrite protection was verified.
- [ ] Record the audience, promised outcome, scope, non-goals, final compression sentence, owner, and refresh trigger.
- [ ] Link the pre-build brief to the final artifact and explain substantial divergence.

**Rendered-condition evidence**

- [ ] For every screenshot or interaction finding, record artifact hash, browser or renderer, viewport dimensions, input mode, motion preference, script state, asset state, and observed consequence.
- [ ] Record keyboard route, visible-focus finding, reduced-motion result, script-failure result, optional-asset result, console finding, and network finding for declared conditions.
- [ ] Keep screenshots only when they prove layout, focus, state, or regression evidence; annotate the relevant region or pair them with a concise finding.
- [ ] Record `not_evaluated` separately from pass and explain why any declared condition remains uncovered.
- [ ] Record latency only when runtime responsiveness is material, the interaction boundary is defined, and the environment and sampling method make the number interpretable. Do not collect p50, p95, or p99 by ritual.

**Reader and review evidence**

- [ ] Record the exact cold-review or target-reader task, prior knowledge, rubric, artifact hash, observed answer or misconception, and limitation of the sample.
- [ ] Distinguish exposure, recall, navigation, prediction, decision quality, and self-reported clarity; do not substitute one outcome for another.
- [ ] Retain the repair decision and responsible layer for each material finding, not only an aggregate result.
- [ ] If analytics are considered, document the decision need, privacy and consent basis, data minimization, access, retention, and deletion policy before collection.

**Change, retry, and ownership history**

- [ ] Record changed paths, source changes, affected claims, invalidated evidence, rerun gates, and residual risk at each durable handoff.
- [ ] For retries, record failure class, preserved state, hypothesis, why another attempt may differ, outcomes, and final disposition.
- [ ] For shared work, record exclusive output owner, source-owner escalations, merge or reconciliation checkpoint, and final verification owner.
- [ ] Mark stale evidence explicitly when artifact bytes, sources, environment, audience, or support matrix changes.

**Concise finding schema:** `status; artifact_hash; condition; location; observed_behavior; reader_or_system_impact; evidence; responsible_layer; owner; next_action; rerun_scope`. Root cause may remain unknown initially; reproduction and consequence must not.

Keep one small evidence index even when screenshots, issues, command logs, or reader notes live elsewhere. Each entry names the decision it supports and the event that makes it stale. At final handoff and refresh, sample the index by reproducing a finding and locate every not-evaluated critical condition.

Temporary diagnostic traces can be useful during a hard failure, but distill their decision-bearing result, sanitize sensitive material, and expire raw detail according to local policy. Uncontextualized evidence invites false comparison; no evidence is better than a screenshot or percentile presented as universal proof.

## Performance Verification Method

The frozen `p95 under 100 ms` rule has no defined interaction, environment, workload, sample, or evidence basis and is not retained. A static explainer often needs no percentile target. Measure performance only when a bounded runtime or workflow cost materially affects the declared reader outcome.

Keep metric families separate:

| metric_family | valid_question | invalid_substitution |
| --- | --- | --- |
| `load_and_availability` | When does essential content become available under a declared file or HTTP delivery condition, including dependency failures? | A fast process or response does not prove visible, accurate, or readable content. |
| `interaction_response` | How long does a named retained control take to produce its defined visible state under fixed conditions? | Mixed clicks, scrolls, and navigation events cannot share one latency distribution. |
| `visual_stability` | Does content move, reveal late, or reflow after fonts, assets, or scripts settle in a way that disrupts reading or input? | Static overlap at one width is layout correctness, not a latency percentile. |
| `artifact_weight_and_dependencies` | Which bytes and requests are required for essential meaning, and what cost or failure state does each add? | File size alone does not establish perceived or causal reading quality. |
| `authoring_or_refresh_time` | How much reviewable effort does a defined generation, verification, or refresh workflow require? | Tool-call count or wall time does not prove reader comprehension. |
| `reader_task_time` | How long does a defined audience take to perform the promised prediction or decision, and where do they become confused? | Faster reading is not automatically better; background and answer quality must accompany time. |

**Claim-driven procedure:**

1. State the reader consequence and the exact claim, such as "the state comparison responds without interrupting keyboard reading" rather than "the page is fast."
2. Define the boundary: trigger, start and end event, expected visible result, artifact hash, delivery surface, viewport, input, motion setting, script state, asset or cache state, and browser or renderer.
3. Establish correctness first. Essential content must exist, state must be right, and the control must be reachable before timing has meaning.
4. Choose realistic or controlled conditions deliberately. Do not mix cold and warm runs, font-cache states, different artifacts, or several interactions in one summary.
5. Select a run and sampling protocol proportional to the claim. Use percentile language only when the sample and method support its interpretation; otherwise report per-run observations, range, or a qualitative finding honestly.
6. Define the owner-approved acceptance consequence before collecting the gate result. Without one, the measurement is diagnostic evidence rather than a pass threshold.
7. Investigate outliers and confounders, including external requests, animation, delayed reveal, observer timing, tooling overhead, and resource contention.
8. Report exact method, raw summary sufficient for review, statistic and uncertainty, result, artifact and environment, and repair or accepted risk. Rerun affected correctness and accessibility paths after optimization.

**Valid example:** measure a retained comparison toggle from keyboard activation to the correct labeled state in one declared browser, viewport, cache condition, and artifact hash; report all attempts and the locally approved budget. **Invalid example:** report p95 from a handful of mixed clicks and scrolls. **Qualitative example:** record that an external font keeps headings unstable during a local file read, block that request, and compare the reader-visible result before deciding whether to remove the dependency.

Treat no overlap, readable text, visible focus, and coherent narrow-screen flow as correctness gates. Treat movement after loading or input as visual stability only when time and sequence matter. Treat reader prediction quality as an outcome metric. A fast blank reveal, inaccessible control, or quickly delivered false claim fails regardless of timing.

Optimize architecture before micro-timing. Remove unnecessary external requests, hidden reveal defaults, heavy media, duplicate scripts, and controls whose explanatory value is unproven. Retain complexity only when its reader benefit is named and its added states are tested. This can improve load, stability, fallback behavior, and verification cost together.

## Scale Boundary Statement

This pattern remains sufficient while one bounded reader outcome, one coherent causal spine, one accountable artifact owner, and one support promise can organize a directly openable file. Length, source count, or number of named systems alone does not define scale. Several systems may fit when their interaction is the subject; one small page may already be overloaded when it combines unrelated reader jobs.

| observed_scale_signal | what_has_changed | appropriate_transition | evidence_and_safeguard |
| --- | --- | --- | --- |
| Different audiences require incompatible prerequisites or depth. | Narrative cohesion, not rendering, has broken. | Create a bounded shared overview and audience-specific journeys or select one primary reader. | Preserve one claim ledger; test each artifact with its own reader task and alternate paths. |
| Several independent causal models compete for the second act. | The page no longer has one heartbeat. | Split by lifecycle, subsystem, or decision and provide explicit routing. | Verify each split is self-sufficient and the overview does not invent cross-system guarantees. |
| Multiple systems are present but their interaction is the central decision. | Scope is broader but can remain coherent at a higher abstraction. | Keep one overview and route implementation detail to owned deep dives. | State abstraction and non-goals; trace every cross-boundary arrow to evidence. |
| A family of pages repeatedly duplicates styles and shell behavior. | Presentation reuse pressure is demonstrated. | Consider a generated static site or shared component shell while keeping content provenance separate. | Use first-refresh and change-impact evidence, version shared behavior, preserve rollback, and rerun each affected page. |
| Pages repeat or contradict the same technical claims. | Source-truth governance, not merely style reuse, has failed. | Establish shared evidence or content ownership and derive page claims from a maintained source model where practical. | Keep claim-level authority, conflict state, and per-page scope; visual consistency is not semantic proof. |
| Live data, authentication, personalization, server persistence, or substantial input becomes essential. | The artifact has crossed from document enhancement into application behavior. | Build a tested application or interactive tool and retain a static explainer as a companion when useful. | Add security, state, lifecycle, failure, performance, deployment, and accessibility gates for the actual application. |
| Target browser, device, input, localization, or policy combinations exceed owned verification capacity. | The support promise is larger than the artifact's operations model. | Narrow support honestly, automate stable high-value paths, or split delivery surfaces with explicit owners. | Record the matrix, uncovered states, release gate, fallback, and escalation; do not imply universal support. |
| Source discovery is unbounded or ownership is unclear. | Truth reconstruction cannot be completed reliably inside page authoring. | Pause dependent claims, narrow with dependency or source-graph analysis, and assign subject owners. | Ranked evidence and resolved critical conflicts precede narrative acceptance. |
| Parallel contributors need the same output file. | Coordination risk threatens durable work and final coherence. | Partition exclusive paths or acts in separate artifacts; reconcile through one owner and merge checkpoint. | Preserve all concurrent edits, run heading and content invariants, and perform one complete final reread. |

Scale through the least disruptive reversible step: narrow the claim, change abstraction, add a companion, create a series, introduce shared static infrastructure after demonstrated reuse, and move to an application only when runtime needs are essential. Early consolidation can create a correlated build and migration failure larger than the duplication it removes.

Treat source truth and rendering infrastructure as separate migration tracks. Common style should be able to evolve without rewriting technical claims; a source change should be traceable to affected pages without uncontrolled visual churn. Assign distinct owners and tests even when one team fills both roles.

For long-running or distributed agent work, checkpoint complete atomic units, keep exclusive write boundaries, preserve one final artifact verifier, and reread governing requirements after context transitions. Context drift, stale evidence, and overlapping writes are scale failures even when the final file remains small.

Retain a static explainer alongside a richer system when it continues to provide a bounded mental model. Do not let the companion page become a hidden control plane or let the application become the only place where essential explanatory caveats can be found.

## Future Refresh Search Queries

These frozen queries were not executed during this no-browse evolution. They are discovery leads, not external evidence. Begin a future refresh from a named stale, conflicting, or unknown claim; stop when that decision is supported, narrowed, or explicitly unresolved.

| search_query_label_name | exact_inherited_search_query_text | intended_discovery_question | preferred_evidence_and_stop_condition | current_status |
| --- | --- | --- | --- | --- |
| `official_docs_query_phrase` | html explainer page patterns official documentation best practices | Which current primary standards or official platform guidance govern the specific browser, accessibility, or artifact behavior now in question? | Inspect the precise primary page and relevant section; stop when the bounded claim and applicability are established or the gap is recorded. | `unexecuted_no_browse` |
| `github_repository_query_phrase` | html explainer page patterns GitHub repository examples | Which version-pinned implementations or maintained examples expose practical patterns, failures, or tool usage not visible in broad prose? | Record repository, revision, path, behavior, license or reuse relevance, and why it applies; examples remain comparative unless independently authoritative. | `unexecuted_no_browse` |
| `release_notes_query_phrase` | html explainer page patterns changelog release notes migration | Did a relevant browser, framework, automation tool, or local explainer package change in a way that invalidates a recommendation or migration path? | Prefer official release notes or repository history tied to a known dependency; stop after impact is determined and affected guidance or tests are identified. | `unexecuted_no_browse` |

**Refresh protocol:**

1. Write the unresolved claim, consequence, current evidence, and freshness trigger before searching.
2. Run the exact inherited query when it remains useful, then record every refined query separately with its rationale; do not replace the frozen text silently.
3. Use search results only to reach inspectable sources. Do not cite snippets, result pages, broad documentation roots, or undated copies as final support.
4. Prefer current primary standards, official platform or tool documentation, and version-pinned implementation history. Use community examples for comparison, edge-case discovery, or contradiction, then test applicable behavior directly.
5. Record exact page or revision, relevant section or path, inspection date, concise supported proposition, scope, contradictions, and confidence boundary. Avoid retaining indiscriminate source dumps.
6. Reconcile the result with local method evidence and subject evidence. Mark whether the recommendation, brief, artifact, target matrix, or no-browse status changes.
7. Rerun affected claim and browser gates. Updating a citation does not update a generated page or its prior screenshots automatically.

Search is the wrong method for local audience comprehension, source-owner intent, or the behavior of an artifact already available for direct inspection. Use reader tasks, owner decisions, source review, and browser evidence instead. Research is complete when it changes or reaffirms a reviewable decision, not when a quota of sources has been collected.

## Evidence Boundary Notes

Use evidence labels where the provenance or claim strength changes materially. Do not prefix every sentence mechanically. High-consequence mechanics, guarantees, compatibility claims, measured outcomes, and disputed statements need closer attribution than ordinary local workflow guidance.

| evidence_status | what_it_means_here | permissible_use | required_follow_up_or_limit |
| --- | --- | --- | --- |
| `local_corpus_sourced_fact` | The statement is tied to content read completely from the mapped local skill or supporting pattern. | State repository workflow, narrative defaults, component rules, and guardrails within their local scope. | Cite or name the relevant artifact when surprising; do not generalize local preference into universal effectiveness. |
| `local_implementation_observation` | The statement describes behavior directly inspected in the archived generator or template source. | State exact archived arguments, replacement behavior, markup, CSS, script, breakpoint, dependency, or overwrite logic. | Name the artifact and version boundary; reproduce runtime behavior before claiming it works in the current environment or modified output. |
| `external_research_sourced_fact` | The statement is tied to a precise public source that was actually inspected and recorded during an authorized refresh. | Support current normative, platform, tool, release, or ecosystem claims within the inspected source's scope. | Record exact page or revision, relevant section, date, applicability, and contradiction. No statement in this evolution newly qualifies because browsing did not occur. |
| `combined_evidence_inference_note` | The statement synthesizes local evidence, observed artifact behavior, systems reasoning, or future refreshed evidence into a recommendation. | Provide decision rules, tradeoffs, severity models, workload guidance, and verification methods when assumptions are explicit. | Verify against the actual task; do not phrase inferred benefit, threshold, or outcome as measured fact. |
| `illustrative_example_not_observed` | The scenario, artifact, reader response, or result was invented to demonstrate a decision pattern. | Teach process, contrast, and diagnostic reasoning without claiming history. | Replace all technical semantics, paths, outcomes, and proof with task-specific evidence before implementation. |
| `conflicting_evidence_unresolved` | Inspected sources disagree or desired, tested, and observed behavior do not align. | Preserve the disagreement, narrow claims, and route it to the correct owner. | Do not average or silently choose a source for high-consequence guidance; record resolution as a new decision. |
| `unknown_or_not_evaluated` | Required evidence, target condition, reader outcome, or external freshness was unavailable or intentionally not collected. | Continue independent work, narrow scope, or disclose risk when consequence permits. | Never count unknown as pass; name the evidence, owner, or condition required to change status. |
| `owner_decision_or_local_override` | An accountable owner selected a policy, scope, support promise, or exception for the current artifact. | Govern future work within the recorded ownership and artifact boundary. | Record rationale, date or version, affected defaults, and proof burden; do not rewrite what older sources or implementations said. |

**Current evidence boundary:** both mapped local prose sources, the linked bootstrap script, the linked template, the complete frozen seed, the working reference, the governing spec, and the focused tests were inspected locally. The three inherited public URLs and three future query strings were not opened or executed. Consequently, this file provides strong local workflow synthesis and observed archived implementation detail, but no refreshed external standard, browser, product, or ecosystem claim.

The exact local facts include the single-file and direct-open default, inline CSS and JavaScript, source-first workflow, roughly five-to-eight-act guidance, mystery-to-mechanism pacing, core mechanism by the second act, deletable scaffold sections, intentional component palette, restrained motion, mobile readability, source footer, and final checklist. Observations about overwrite refusal, default seven-act generation, HTML escaping, external font import, breakpoints, reveal observers, and dot navigation are scoped to the inspected archived assets.

This reference's reliability tiers, workload model, retry classification, observability schema, performance method, scale transitions, and many accessibility-oriented fallback controls are engineering synthesis. They are designed to be testable and bounded, but they are not a substitute for current normative evidence, specialist review, or target-reader data when those are required.

**Boundary audit:** sample every high-consequence claim and every transition into a stronger verb such as `requires`, `prevents`, `proves`, or `reliable`; reopen the claimed source; reproduce implementation observations where runtime matters; locate all conflicts and not-evaluated states; and confirm that examples remain visibly illustrative. Audit claim-to-source and source-to-represented-decision directions.

Evidence transfers only when the claim, scope, source version, and relevant conditions remain the same. Source truth may transfer into another medium after review; screenshots, interaction results, responsive behavior, and reader comprehension generally do not. Artifact changes invalidate dependent proof until impact is established and affected gates rerun.

**Minimum reusable evidence packet:** reader and outcome; thesis and scope; source and claim ledger; conflicts and unknowns; artifact path and hash; declared conditions; exact verification methods and concise results; illustrative-status notes; owner; refresh trigger; and residual risk. Stop reuse when a high-consequence claim cannot be traced, when evidence conditions are unknown, or when the destination medium requires uncollected behavior proof.
