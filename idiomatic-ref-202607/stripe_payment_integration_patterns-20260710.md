# Stripe Payment Integration Patterns

**Decision supported.** This section helps decide how to choose and verify a payment integration architecture without treating a short unrefreshed skill as current Stripe API authority. The seed title does not define whether the reference governs one-time checkout, saved payment methods, subscriptions, invoices, platform fund flows, migration, or only evidence synthesis.

**Recommended default and causal basis.** First classify merchant and platform model, payer journey, money movement, recurring behavior, liability, currencies, tax and discount ownership, fulfillment timing, trust boundaries, and recovery obligations; then verify the selected Stripe surface against current official versioned documentation before implementation or launch. Payment correctness depends on asynchronous state, duplicate delivery, partial failure, external authority, and regulatory boundaries that cannot be inferred safely from a frontend flow or one successful API response.

**Operating conditions and assumptions.** The design names business outcome, authoritative server state, Stripe object family as source-reported or freshly verified, amount and currency ownership, client/server boundary, idempotency domain, event verification and ordering, reconciliation, refunds and disputes, test/live separation, observability, rollout, and rollback. This reference supports architecture and verification planning; it does not provide legal, tax, PCI, accounting, fraud, or current Stripe product certification.

**Failure boundary and alternatives.** The browser declares payment success, a request response triggers irreversible fulfillment without durable confirmation, retries can duplicate effects, secrets reach clients or logs, raw payment data is handled casually, or local recommendations are called current without official refresh. Bounded alternatives and recoveries: use a hosted or embedded provider-managed flow, a custom element with server orchestration, invoicing or subscription APIs for recurring models, a platform flow for marketplace funds, or defer implementation until compliance and product constraints are known.

**Counterexample, gotchas, and operational comparison.** Authentication may require additional customer action, events can be delayed or repeated, business and provider state can diverge, refunds differ from payment failure, Connect changes liability, test and live identifiers differ, and API versions affect behavior. Good: create a durable local order before starting payment, correlate provider identifiers, verify asynchronous events, transition idempotently, and reconcile before fulfillment. Bad: trust a success redirect and mark paid. Borderline: fulfill on synchronous confirmation only when the exact official contract and a compensating reconciliation path prove it safe.

**Verification, evidence, and uncertainty.** Review current official Stripe docs and account settings when authorized, threat-model trust boundaries, replay duplicate and out-of-order events, inject timeouts and partial failures, test amount and currency invariants, reconcile provider and local ledgers, and rehearse rollback. The complete local skill directly identifies preferred integration families, deprecations, recurring and Connect decision points, dynamic payment methods, PCI cautions, and go-live documentation. Both local copies are one unrefreshed text, no official Stripe page was browsed, and current API versions, product names, dashboard behavior, regional rules, and compliance requirements are unknown.

**Second-order consequence.** A payment integration is a distributed state machine and ledger boundary, not a button plus charge request.

**Revision decision.** Add a business-model router, distributed-state contract, trust and compliance boundary, lifecycle verification, reconciliation, and explicit official-refresh gate before preserving seed evidence.

**Retained seed evidence.** The exact Stripe Payment Integration Patterns title and theme remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which evidence can support a payment architecture, current API claim, repository implementation fact, operational assertion, or agent-workflow rule. The seed treats two byte-identical Stripe skill paths as separate local sources and three agent-instruction websites as external payment analogues, while omitting the many official Stripe documentation links embedded in the local skill.

**Recommended default and causal basis.** Count the two local paths as one textual skill source, classify its product directions as unrefreshed local claims, treat its official Stripe URLs as future primary candidates, use repository code and tests for implementation facts, and restrict OpenAI, GitHub Actions, and AGENTS.md links to agent-process context. Authority must match the claim: instruction-format documentation cannot validate payment lifecycles, and duplicate bytes cannot provide independent corroboration.

**Operating conditions and assumptions.** Each row records path or URL, hash or version, source type, retrieval status, claim scope, account and regional applicability, duplication, conflicts, freshness, verification method, and prohibited inference. The table establishes evidence fitness and cannot approve compliance, account settings, money movement, or launch readiness.

**Failure boundary and alternatives.** Two copies raise confidence, link presence proves currency, a Stripe docs title proves account configuration, agent documentation supports money movement, or test-mode success is generalized to live behavior. Bounded alternatives and recoveries: use a claim-level evidence ledger, inspect current official versioned documentation when authorized, query repository lockfiles and API-version settings, consult account dashboard configuration, or mark the claim unresolved.

**Counterexample, gotchas, and operational comparison.** Official docs can be version-sensitive, dashboard features vary, API responses depend on account and region, source links may redirect, local code can pin an older version, and compliance evidence has separate ownership. Good: cite the local skill for what it recommends, then require a current official Stripe page and a repository test before implementing. Bad: cite developers.openai.com for Checkout behavior. Borderline: use GitHub Actions documentation only to design CI secret and test automation, never payment semantics.

**Verification, evidence, and uncertainty.** Recompute local hashes, compare duplicate bytes, classify every source by claim type, capture official version and retrieval date during future refresh, inspect repository configuration, reproduce behavior in isolated test mode, and record contradictions. The local files were completely read and proven byte-identical at 838eb4e00a22f817b8577be230600547441493bf8c7aa15b0ee7e04f71f875cf; their embedded URLs and the seed's unrelated external rows are directly observable. None of the embedded official Stripe pages or seed external websites was browsed, so current content, version, and applicability are unverified.

**Second-order consequence.** Source mapping is itself a payment control because false authority can send an integration onto an obsolete or unsafe state path.

**Revision decision.** Add duplicate detection, claim-type authority, embedded official candidates, retrieval and version status, repository evidence, applicability, conflicts, and prohibited inference while retaining every seed row.

**Retained seed evidence.** Both exact local paths and the OpenAI Codex, GitHub Actions, and AGENTS.md external rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/stripe/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/stripe/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | external_research_sourced_fact | primary agent instruction context model |
| https://docs.github.com/actions | external_research_source_material | external_research_sourced_fact | verification and automation model |
| https://agents.md/ | external_research_source_material | external_research_sourced_fact | general agent instruction format |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which integration safeguards deserve first attention when payment correctness, financial recovery, and implementation simplicity compete. The seed gives unsupported numeric scores to source loading, evidence splitting, and verification, but ranks no payment controls such as authoritative state, idempotency, event verification, reconciliation, trust boundaries, or business-model routing.

**Recommended default and causal basis.** Rank server-authoritative state and invariant-preserving transitions first, then duplicate-safe commands and events, authenticated asynchronous event handling, reconciliation and fulfillment gating, secret and payment-data boundaries, business-model-to-product routing, observability, and launch verification. These patterns prevent irreversible or financially consequential failure classes; process evidence controls remain necessary but should support rather than replace the payment state model.

**Operating conditions and assumptions.** Each tier states failure prevented, causal mechanism, supported lifecycle, assumptions, operational cost, counterexample, verification, source boundary, and escalation path without pretending an editorial rank is measured effectiveness. The ranking organizes engineering attention and does not estimate fraud loss, legal exposure, conversion rate, or provider endorsement.

**Failure boundary and alternatives.** Numeric precision implies probability, hosted checkout is always ranked above requirements, a successful request outranks durable event state, fraud or compliance is reduced to code style, or convenience hides inability to reconcile. Bounded alternatives and recoveries: use separate scoreboards for one-time payments, subscriptions, Connect platforms, and migrations; leave incomparable controls unranked; or elevate account-specific official guidance after refresh.

**Counterexample, gotchas, and operational comparison.** Provider-hosted surfaces reduce but do not remove server and fulfillment obligations, idempotency scope differs by operation, events may be duplicated or reordered, reconciliation latency is domain-specific, and platform funds add liability decisions. Good: place authoritative order and event transitions above UI customization. Bad: rank Payment Element by popularity. Borderline: prioritize a provider-hosted flow when customization is low, but only after verifying recurring, tax, locale, and liability needs.

**Verification, evidence, and uncertainty.** Define qualitative criteria before ranking, map each control to a failure injection and recovery test, compare task-specific product options, review costs and exclusions, and revise tiers when official documentation or incidents change the model. The local skill directly supports business-model and integration-surface routing; distributed-state, idempotency, event, reconciliation, and secret controls are systems inferences with explicit verification needs. No defect dataset, Stripe account evidence, current docs refresh, or quantitative control-effectiveness study supports exact scores.

**Second-order consequence.** The highest-value payment pattern is the one that preserves financial truth under duplicate, delayed, failed, and adversarial interactions.

**Revision decision.** Replace repeated numeric rows with stable qualitative payment-control tiers, disclosed causal criteria, task-specific variants, evidence status, and refresh triggers.

**Retained seed evidence.** Source Map First, Evidence Boundary Split, and Verification Gate Coupling remain preserved as cross-cutting evidence safeguards. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `stripe_payment_integration_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local stripe payment material before synthesizing integration patterns recommendations. |
| `stripe_payment_integration_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `stripe_payment_integration_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what principle should govern product selection, state transitions, fulfillment, retries, and evidence throughout a Stripe integration. The seed's local-first, public-second, verification-backed thesis is generic and does not state the governing payment invariant, asynchronous authority model, or need to control API-version migration.

**Recommended default and causal basis.** Choose the narrowest provider surface that fits the business model, but keep payment and fulfillment decisions in a durable server-owned state machine driven by authenticated, duplicate-safe evidence and reconciled against the provider under a controlled API version. Frontend redirects, synchronous responses, and event arrival order are observations rather than a complete financial ledger; durable transitions preserve truth when communications fail or repeat.

**Operating conditions and assumptions.** The thesis is applied with explicit order and payment identities, immutable amount and currency decisions, allowed transitions, event provenance, idempotency, fulfillment policy, reconciliation, refund and dispute handling, version ownership, tests, and operational recovery. The thesis structures technical reliability but does not determine legal merchant-of-record status, tax treatment, accounting policy, fraud strategy, or compliance scope.

**Failure boundary and alternatives.** The client owns paid state, any success-like response triggers fulfillment, an event can move state backward, the latest API is adopted without compatibility review, or product recommendations ignore subscriptions and platform liability. Bounded alternatives and recoveries: use provider-hosted checkout to reduce collection complexity, custom orchestration for justified control, Billing for recurring models, Connect for platform flows, Payment Links or invoices for simpler journeys, or defer until constraints are known.

**Counterexample, gotchas, and operational comparison.** Authorization and capture can be distinct, customer action may interrupt a flow, retries can create duplicate local commands, event delivery can lag the user journey, refunds and disputes are later states, and API-version changes can alter shapes. Good: local order state advances only through validated monotonic transitions and fulfillment is idempotent. Bad: mark paid from the return URL. Borderline: use synchronous confirmation for immediate UX while withholding irreversible fulfillment until the verified evidence policy is met.

**Verification, evidence, and uncertainty.** Model transitions and invariants, test duplicate and out-of-order inputs, inject network loss around every effect, verify secrets and signatures, reconcile test records, run versioned contract tests, and obtain current official and go-live review. The local skill directly supports business-model routing and official documentation checks; the state-machine, duplicate-safety, and reconciliation requirements are strong systems inferences. Current Stripe object semantics, webhook guarantees, API version behavior, and account capabilities were not refreshed.

**Second-order consequence.** The provider owns payment processing facts, the merchant owns business and fulfillment facts, and the integration must reconcile rather than collapse those authorities.

**Revision decision.** Replace the generic evidence-order statement with a server-authoritative, duplicate-safe, reconciled, version-controlled payment-state thesis and explicit product-routing limits.

**Retained seed evidence.** Local evidence retrieval, external freshness checks, and conversion into verification-backed decisions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `stripe_payment_integration_patterns` contains 2 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Stripe Payment Integration Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which exact local passage can inform a product-routing or deprecation question and what it cannot establish without current official evidence. The seed says 'no heading discovered' for two identical files and therefore hides the skill's actual topic sequence: integration options, API tour, go-live, Checkout and PaymentIntents, saved methods, dynamic methods, PCI and PAN migration, Billing, and Connect.

**Recommended default and causal basis.** Index the single textual source by topic and embedded Stripe URL, mark every recommendation as source-reported, map duplicates to one content hash, and attach a mandatory refresh gate for current product, version, account, region, or compliance claims. The source has no headings but still contains a recoverable argument structure; a topical map enables targeted use without pretending the thirty lines are a complete integration manual.

**Operating conditions and assumptions.** Entries identify line topic, recommendation, linked official candidate, affected business model, assumptions, exclusions, missing operational concerns, current-verification need, and downstream design question. The map supports retrieval and critique, not current product certification, implementation completeness, or compliance approval.

**Failure boundary and alternatives.** Two paths become two authorities, deprecation wording is repeated as current fact, 'latest API' means uncontrolled upgrade, product names substitute for lifecycle design, or embedded links are never opened before implementation. Bounded alternatives and recoveries: use a line-range map, build a claim ledger keyed by URL, rely on current repository integration and tests, or route directly to official Stripe design and migration documentation during authorized research.

**Counterexample, gotchas, and operational comparison.** The source compresses multiple products into one paragraph, uses absolute language, contains no webhook or idempotency guidance, Connect liability wording may require precise current interpretation, and dashboard-driven methods can vary. Good: retrieve the Billing paragraph for a recurring-revenue planning question, label it unrefreshed, and verify the current official use case. Bad: use the skill to implement subscription state transitions. Borderline: use its Checkout preference as an initial option only while evaluating required customization and account constraints.

**Verification, evidence, and uncertainty.** Recompute the shared hash, confirm byte identity, locate the exact paragraph and embedded URL, state what the paragraph does and does not cover, compare repository behavior, perform current official refresh when authorized, and test the chosen lifecycle. The two files were completely read and are byte-identical; every listed topic and embedded link is directly observable in the shared text. The source has no version, retrieval date, account context, changelog, or operational examples, and its linked pages were not opened.

**Second-order consequence.** A headingless skill still needs progressive disclosure; topic indexing prevents its shortest and strongest-sounding sentence from dominating unrelated payment decisions.

**Revision decision.** Replace 'no heading discovered' with a paragraph-level topic, claim, link, assumption, omission, and refresh map while retaining both file rows as duplicate locations.

**Retained seed evidence.** Both exact local paths, the stripe-best-practices title, and their reusable skill roles remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/stripe/SKILL.md | stripe-best-practices | no heading discovered | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/stripe/SKILL.md | stripe-best-practices | no heading discovered | skill entrypoint or reusable agent prompt |

## External Research Source Map

**Decision supported.** This section helps decide which public source category should answer payment semantics, automation, agent instructions, compliance routing, or account-specific behavior during a future refresh. The seed's three external rows cover Codex instructions, GitHub Actions, and AGENTS.md rather than Stripe payments, while the local skill embeds official Stripe links for integration options, API tour, go-live, product surfaces, migrations, Billing, and Connect.

**Recommended default and causal basis.** Use official versioned Stripe documentation and changelogs for product and API facts, account configuration for enabled behavior, repository tests for local contracts, GitHub Actions only for CI automation, and Codex or AGENTS.md only for agent instruction scope. Misclassifying an automation or prompt-format source as payment evidence can produce confidently wrong money movement, lifecycle, or launch guidance.

**Operating conditions and assumptions.** Each row states claim type, authority, exact version or account scope, retrieval date, complete-read status, region or feature assumptions, linked migration, reproduction, conflict, and expiry. The map plans evidence retrieval and cannot substitute for official support, legal advice, compliance assessment, or live-account validation.

**Failure boundary and alternatives.** Agent docs support checkout architecture, CI docs prove runtime semantics, Stripe marketing summaries replace API contracts, main docs are mixed across versions, or account-specific dashboard settings are generalized. Bounded alternatives and recoveries: inspect pinned SDK and API-version configuration, use official support or compliance channels for unresolved high-risk questions, consult repository history, or block launch until primary evidence is available.

**Counterexample, gotchas, and operational comparison.** Documentation can default to latest versions, SDK and API versions differ, dashboard settings are mutable, regional payment methods vary, Connect and Billing have specialized terminology, and compliance advice cannot be inferred from code examples. Good: use GitHub Actions docs to protect test secrets and official Stripe docs to validate webhook behavior as separate evidence rows. Bad: cite agents.md for PaymentIntent lifecycle. Borderline: use local SDK types as version evidence only after confirming the account API contract.

**Verification, evidence, and uncertainty.** Open the complete primary material when authorized, capture version, account, date, and feature context, read migrations and caveats, reproduce in isolated test mode, compare repository settings, and document conflicts or unresolved support questions. The role mismatch of the three seed external rows and the official Stripe URLs embedded in the local skill are directly observable. No public or account source was browsed, so current product status, API guarantees, regulatory scope, and page availability remain unknown.

**Second-order consequence.** External evidence should be partitioned by authority domain; payment semantics, CI process, and agent context are separate contracts even when one implementation touches all three.

**Revision decision.** Retain and reclassify the three seed links, add the embedded official Stripe candidate families, and require version, account, feature, migration, reproduction, and expiry metadata.

**Retained seed evidence.** The exact OpenAI Codex AGENTS.md, GitHub Actions, and AGENTS.md format links remain preserved for process-only use. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | primary agent instruction context model | external_research_sourced_fact |
| https://docs.github.com/actions | GitHub Actions documentation | verification and automation model | external_research_sourced_fact |
| https://agents.md/ | AGENTS.md open format | general agent instruction format | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which observable design or implementation smells should block a Stripe integration from progressing to launch and what recovery contains financial risk. The seed lists only generic source and verification failures, omitting payment-specific hazards such as client-authoritative success, duplicate effects, unverified events, order-dependent transitions, secret leakage, test/live mixing, raw payment-data handling, and business-model mismatch.

**Recommended default and causal basis.** Register client-owned paid state, redirect-driven fulfillment, non-idempotent commands, event signature bypass, missing event deduplication, backward state transitions, mutable amount or currency ambiguity, test/live identifier mixing, secret exposure, uncontrolled API upgrades, direct raw payment-data handling, and unreconciled local/provider ledgers. Each anti-pattern can produce money, entitlement, customer, or audit divergence even when the primary request returns successfully.

**Operating conditions and assumptions.** Rows name affected business invariant, trust boundary, trigger, causal mechanism, customer and financial consequence, detection, immediate containment, repair, data reconciliation, rollback, owner, and official-evidence requirement. The registry covers engineering safeguards and cannot quantify fraud, chargeback, compliance, tax, or accounting exposure.

**Failure boundary and alternatives.** Warnings are generic security slogans, remediation only retries, event verification is assumed from framework middleware, rollback ignores already fulfilled goods, or product deprecation claims are presented as current without refresh. Bounded alternatives and recoveries: use a provider-hosted surface, queue fulfillment behind durable state, add an idempotent transition table, quarantine inconsistent records, disable a payment method or rollout slice, or escalate compliance and account questions.

**Counterexample, gotchas, and operational comparison.** Valid signed events can be duplicates, event order may differ from business order, refunds do not automatically reverse fulfillment, secrets can leak through exception bodies, sandbox behavior can differ, and a version upgrade may be account-scoped. Good: detect a duplicate completion event, no-op the already-applied transition, and retain audit evidence. Bad: issue a second refund after a timeout because the first response was lost. Borderline: allow manual operator correction only through an authenticated, audited, idempotent workflow with reconciliation.

**Verification, evidence, and uncertainty.** Inject duplicate, reordered, forged, delayed, missing, and conflicting observations; simulate timeouts around effects; scan client bundles and logs for secrets; cross test/live IDs; reconcile provider records; and verify containment plus replay. The local skill directly supports product and data-boundary cautions; the state, event, idempotency, reconciliation, and secret failure classes are conservative distributed-systems inferences. Current Stripe signature schemes, event guarantees, product deprecations, and account controls were not verified.

**Second-order consequence.** The worst payment anti-patterns confuse an observation with an irreversible business fact.

**Revision decision.** Expand three process rows into a causal payment registry with invariant, trust boundary, containment, reconciliation, rollback, and official-refresh columns.

**Retained seed evidence.** Source-map-first synthesis, evidence-boundary labels, and concrete verification gates remain preserved as cross-cutting mitigations. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which layered evidence must pass before the evolved reference, an integration change, and a live rollout can each be called ready. The seed supplies only an archive-wide reference generator command, which cannot validate payment state transitions, duplicate safety, event authenticity, secret boundaries, reconciliation, test/live isolation, or launch configuration.

**Recommended default and causal basis.** Run the focused artifact verifier and frozen-span audit, then select repository gates for pure state transitions, API contract parsing, authenticated event handling, duplicate and out-of-order replay, timeout and partial failure, fulfillment idempotency, secret scanning, test/live separation, reconciliation, migration, and rollback; finish with a freshly reviewed official go-live checklist. Document structure, code behavior, provider interoperability, account configuration, and operational launch are separate contracts with different failure evidence.

**Operating conditions and assumptions.** Every gate states claim, environment, account mode, API and SDK version, fixture source, expected red condition, command or review method, actual status, skipped cases, owner, evidence retention, and blocking action. This gate set guides engineering verification and does not certify PCI, tax, legal, fraud, or accounting controls.

**Failure boundary and alternatives.** One sandbox checkout proves launch, mocks prove provider compatibility, the archive command proves payment safety, live credentials enter CI, a passing test omits duplicate delivery, or stale official checklist evidence is reused. Bounded alternatives and recoveries: use provider test fixtures or isolated accounts, contract-test recorded schemas with version metadata, perform structured manual account review, stage a canary with reversible fulfillment, or block launch when a critical gate is unavailable.

**Counterexample, gotchas, and operational comparison.** Test clocks and provider simulators may not match live timing, event endpoints can be reachable but misconfigured, skipped integration tests can hide behind green suites, feature flags can select different paths, and refunds or disputes need later lifecycle fixtures. Good: see duplicate fulfillment fail, implement an atomic idempotent transition, replay duplicates and reorderings, reconcile the resulting records, and verify rollback. Bad: run one create-payment unit test. Borderline: accept a mocked event test only for local logic while retaining a blocked provider-contract gate.

**Verification, evidence, and uncertainty.** Force each critical gate red or replay a known failing fixture, run fresh from the documented root and isolated mode, inspect collected and skipped cases, compare local and provider state, review secret exposure, and preserve exact output plus unresolved risks. The local skill explicitly requires official integration, API tour, and go-live documentation; the additional gate set follows directly from the inferred distributed-state and trust-boundary model. Exact Stripe CLI, SDK, event fixture, API version, and account review commands depend on the repository and current provider tooling.

**Second-order consequence.** Payment completion evidence is a chain: a green code suite cannot compensate for an unverified account or event endpoint, and a successful provider call cannot compensate for a broken local ledger.

**Revision decision.** Retain the archive verifier and add artifact, state, event, duplicate, failure, secret, mode, reconciliation, migration, account, launch, and rollback gates with evidence contracts.

**Retained seed evidence.** The existing `verify_reference_generation.py --stage final` command remains preserved as the archive-wide artifact gate. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide how an agent should classify a payment request and choose planning, implementation, review, migration, incident, or launch-readiness behavior before recommending a Stripe surface. The seed routes by theme keywords and then repeats generic source-first steps; its user journey still describes command, hook, plugin, MCP, and settings selection rather than payment integration.

**Recommended default and causal basis.** Identify whether the request concerns one-time payment, saved method, recurring billing, invoice, platform funds, migration, refund, dispute, reconciliation, or incident; then collect business, account, region, compliance, lifecycle, and repository constraints before selecting evidence and action. Product choice follows money movement and operational obligations, while a keyword such as checkout or subscription can hide materially different fulfillment, liability, and recovery models.

**Operating conditions and assumptions.** The decision record names merchant model, payer and beneficiary, funds flow, frequency, fulfillment, amount and currency authority, customer action, liability, existing objects, API and SDK versions, event path, reconciliation, compliance owner, evidence status, and allowed output. The guide may frame and review work but must not access live accounts, move money, change dashboard settings, or provide compliance conclusions without explicit authorization.

**Failure boundary and alternatives.** The agent picks an API from one noun, assumes greenfield code, gives current product advice without refresh, treats a redirect as success, changes live configuration, or handles raw payment data without explicit authorization and compliance expertise. Bounded alternatives and recoveries: produce a requirements and risk packet only, review an existing integration, design a migration plan, route Billing or Connect specialization, request current official evidence, or stop when account and compliance facts are missing.

**Counterexample, gotchas, and operational comparison.** One business may combine one-time and recurring flows, platform and merchant roles can overlap, existing objects constrain migration, regional methods affect customer action, subscriptions have long lifecycles, and incidents require containment before refactor. Good: for a marketplace subscription request, separate recurring customer billing from platform fund allocation, identify liability and reconciliation owners, and defer exact APIs until official current guidance is checked. Bad: recommend PaymentIntents from the word payment. Borderline: suggest hosted checkout as a low-complexity candidate with explicit unmet requirements.

**Verification, evidence, and uncertainty.** State the classified use case and unknowns, inspect existing code and provider configuration, confirm evidence authority, map the proposed state machine and failure paths, challenge with duplicate and delayed events, and run the matching gate ladder. The local skill explicitly distinguishes on-session, off-session, saved method, recurring, and Connect scenarios, providing a direct basis for a richer router. Exact current product fit, account eligibility, regional availability, compliance scope, and migration support remain unverified.

**Second-order consequence.** The first payment decision is not which API to call but which party owns each financial fact and recovery obligation.

**Revision decision.** Replace extension-surface language and keyword routing with payment-use-case, funds-flow, lifecycle, evidence, risk, authorization, and output-mode classification.

**Retained seed evidence.** Local source retrieval, gated recommendations, public freshness checks, evidence labels, and explicit opening triggers remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide how a payment engineer proceeds from a business request to a verified, observable, and reversible Stripe integration slice. The seed's actor is an agent-tool platform builder choosing commands, hooks, plugins, MCP, or settings, which is unrelated to a payer, merchant, subscription, platform, fulfillment, or financial recovery journey.

**Recommended default and causal basis.** Follow a merchant journey from business and compliance discovery through use-case routing, official evidence refresh, durable order and payment modeling, provider interaction, customer return, authenticated asynchronous updates, idempotent fulfillment, reconciliation, rollout, and support recovery. An end-to-end journey exposes the gaps between customer experience, provider processing, merchant state, and fulfillment that API-centric examples conceal.

**Operating conditions and assumptions.** The scenario names actor, customer goal, merchant and beneficiary, amount and currency, catalog authority, tax and discount ownership, lifecycle, evidence version, order creation, provider correlation, event path, duplicate policy, fulfillment, refund and dispute response, reconciliation, support tooling, rollout, and rollback. Adapt the journey to real business and regulatory owners; it is not a live runbook or authorization to transact.

**Failure boundary and alternatives.** The journey begins at API creation, excludes abandoned or interrupted payments, assumes the return page proves settlement, has no duplicate delivery case, omits support and accounting users, or ends after a sandbox success. Bounded alternatives and recoveries: model a recurring subscription, invoice collection, saved-method setup, Connect marketplace, legacy migration, refund flow, or incident containment journey when those govern the request.

**Counterexample, gotchas, and operational comparison.** Customers close browsers, authentication can redirect, amounts can change before confirmation, asynchronous updates can arrive after support action, fulfillment can partially fail, and refund or dispute states outlive checkout. A digital merchant creates an immutable order snapshot, starts a source-reported hosted checkout candidate after current validation, records provider correlation, handles repeated verified updates idempotently, grants entitlement once, runs reconciliation, and gives support an audited recovery action.

**Verification, evidence, and uncertainty.** Walk every actor and transition, replay abandon, customer-action, timeout, duplicate, reorder, delayed confirmation, fulfillment failure, refund, and dispute cases, compare local and provider records, and rehearse customer-safe rollback. The local skill directly supports checkout and business-model routing; the multi-actor lifecycle and recovery details are bounded engineering inference. No concrete merchant, product, country, tax model, account, fulfillment policy, or official current API contract is supplied.

**Second-order consequence.** The user journey is complete only when customer, merchant, provider, fulfillment, support, and accounting perspectives converge on the same financial state.

**Revision decision.** Replace the extension-platform scenario with an end-to-end payment, fulfillment, reconciliation, and recovery journey including adverse paths.

**Retained seed evidence.** A named role, starting state, decision, source trigger, and executable next step remain preserved as scenario structure. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The agent-tool platform builder is starting from a capability request that could become a command, hook, plugin, MCP server, or setting and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `stripe_payment_integration_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the right extension surface and proving install, invocation, permissions, and recovery behavior.
Reference opening trigger: Open this file when the task mentions stripe payment integration patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide which integration family and customization level best satisfies the business model while minimizing payment-data, lifecycle, compatibility, and operational burden. The seed reduces Adopt, Adapt, Avoid, and Cost of wrong to evidence agreement, without comparing source-reported Checkout, Payment Element, PaymentIntents, Billing, Payment Links, Invoicing, SetupIntents, or Connect against business and operational constraints.

**Recommended default and causal basis.** Compare provider-hosted checkout, embedded provider UI, custom payment UI, direct payment orchestration, recurring billing, invoicing or links, saved-method setup, and platform funds by business fit, customer experience, control, compliance surface, state ownership, account eligibility, migration cost, and recovery complexity. More customization transfers more lifecycle and failure obligations to the merchant, while a simpler surface can fail requirements for subscriptions, platform liability, tax, pricing, or user experience.

**Operating conditions and assumptions.** Each option states use conditions, source and freshness, supported lifecycle, data handled, server responsibilities, customer action, asynchronous events, idempotency, reconciliation, account settings, direct and second-order costs, migration, rollback, and owner. This guide informs technical selection but cannot choose commercial terms, legal liability, merchant-of-record status, tax policy, or compliance scope.

**Failure boundary and alternatives.** Adopt means the skill prefers it, hosted means no backend, custom means flexible without added proof, latest means upgrade immediately, or Cost of wrong mentions only engineering time instead of duplicate charges, withheld fulfillment, and liability. Bounded alternatives and recoveries: run a requirements matrix before selecting, stage a provider-hosted baseline, preserve a compatibility adapter during migration, use invoice or link flows for low-code needs, or escalate Connect and recurring design to specialists.

**Counterexample, gotchas, and operational comparison.** Feature availability varies, dynamic methods can change presentation, taxes and discounts alter amount authority, saved methods need consent and future-use semantics, platform charge types encode liability, and switching object families can complicate reconciliation. Good: choose a hosted one-time flow for low customization after validating current requirements, but keep server event and fulfillment logic. Bad: use direct payment orchestration for a subscription merely because code exists. Borderline: choose custom UI only when measured product needs justify the larger compliance and recovery surface.

**Verification, evidence, and uncertainty.** Build a signed requirements matrix, validate each candidate against current official docs and account settings, prototype the highest-risk interaction in test mode, inject lifecycle failures, estimate migration and operations, and record rollback. The local skill directly names these product families and preference directions, providing a basis for comparison rather than a current final selection. Current capabilities, pricing, regions, API versions, compliance impact, and account eligibility were not verified.

**Second-order consequence.** The best integration minimizes total obligation, not code lines: frontend convenience, backend correctness, support, accounting, and migration all count.

**Revision decision.** Expand generic adoption rows into a source-reported product and customization matrix with operational obligations, migration, evidence, and rollback.

**Retained seed evidence.** Adopt, Adapt, Avoid, and Cost of being wrong remain preserved as dispositions after option comparison. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the stripe payment integration patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong stripe payment integration patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which evidence should govern historical skill intent, current product semantics, local implementation behavior, account-specific configuration, and business risk. The seed calls the archived skill canonical and the identical live-path copy supporting, but byte equality means they are one textual source; the hierarchy also omits repository code, account configuration, official Stripe documentation, and business or compliance authority.

**Recommended default and causal basis.** Treat both local paths as duplicate locations for one historical skill, use current official Stripe documentation as prospective primary authority for product behavior, repository code and tests for implementation facts, account settings for enabled configuration, and designated business, accounting, legal, and compliance owners for their domains. A claim must be governed by the source that owns it; no short plugin skill can be canonical for every technical, financial, and regulatory question.

**Operating conditions and assumptions.** The hierarchy records claim family, source role, duplicate relation, version or account scope, direct evidence, conflicts, precedence, verification, owner, and refresh trigger. The hierarchy orders evidence for decisions and cannot delegate or replace accountable human ownership.

**Failure boundary and alternatives.** Archive location implies technical authority, identical files corroborate each other, official docs override local API pinning without migration, code determines business policy, or agent instruction websites influence payment semantics. Bounded alternatives and recoveries: retain a conflict set, require support confirmation for ambiguous provider behavior, use an ADR for local decisions, route compliance and accounting, or block the claim pending current primary evidence.

**Counterexample, gotchas, and operational comparison.** Account settings can override defaults, live and test modes differ, official docs may describe latest behavior, local code may intentionally lag, contractual terms can matter, and copied skill paths can drift later. Good: use the skill to identify a Checkout candidate, current official docs to validate it, repository contract tests to prove integration, and the product owner to approve fulfillment. Bad: call the archived copy canonical for Connect liability. Borderline: follow local pinned behavior during a controlled migration while documenting current official divergence.

**Verification, evidence, and uncertainty.** Recompute hashes and duplication, classify the claim, inspect the governing version or account state, compare local code and current primary evidence, obtain domain-owner review, run contract and failure tests, and record conflict resolution. Duplicate identity and the content of the skill are directly verified; the broader hierarchy follows conservative authority separation. Current official, account, contractual, and organizational authorities were not available for inspection.

**Second-order consequence.** Payment authority is plural but not ambiguous when each source owns a different fact: provider, merchant code, account, business policy, and compliance must be reconciled.

**Revision decision.** Replace canonical-versus-supporting duplicate labels with claim-specific provider, repository, account, business, compliance, and process authority while preserving seed metadata.

**Retained seed evidence.** Canonical, supporting, legacy, duplicate, and conflicting vocabulary plus both local file rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/stripe/SKILL.md | canonical primary source | no heading discovered | What guidance, warning, or example should this source contribute to Stripe Payment Integration Patterns? |
| claude-skills/plugins/stripe/SKILL.md | supporting context source | no heading discovered | What guidance, warning, or example should this source contribute to Stripe Payment Integration Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what concrete artifact allows engineers, product, support, accounting, and compliance reviewers to challenge a payment design before money moves. The seed's three-row artifact captures user goal, decision boundary, and verification gate but omits parties, funds flow, amount authority, product evidence, state transitions, idempotency, events, fulfillment, reconciliation, compliance, rollout, and recovery.

**Recommended default and causal basis.** Create a Payment Integration Decision and State Contract covering business model, parties and liability, funds flow, amount and currency source, chosen provider surface and version evidence, local/provider identifiers, states and transitions, commands, events, idempotency, fulfillment, reconciliation, refunds, disputes, secrets, data scope, tests, rollout, rollback, and owners. Payment failures occur between components and teams; one shared contract makes hidden assumptions and irreversible transitions reviewable before implementation.

**Operating conditions and assumptions.** Each state has entry evidence and allowed successors, every effect has duplicate policy, source claims have freshness, local and provider records can be reconciled, support actions are audited, and rollback addresses already-created financial objects. Require the full artifact for production money movement; prototypes must remain isolated from live credentials and cannot establish launch readiness.

**Failure boundary and alternatives.** The artifact is an API sequence, paid is one boolean, events lack authenticity and dedupe, customer return triggers fulfillment, test/live boundaries are absent, or compliance is self-approved by engineering. Bounded alternatives and recoveries: use a lighter hosted-checkout contract for simple one-time flows, add subscription, Connect, migration, dispute, or data-compliance appendices, or stop at requirements when authority is missing.

**Counterexample, gotchas, and operational comparison.** One provider object can represent several local orders poorly, amounts can be recalculated inconsistently, partial refunds complicate state, retries cross process restarts, subscriptions outlive sessions, and operator repair can bypass invariants. A complete contract freezes an order snapshot, correlates provider IDs, defines monotonic transition rules, authenticates and deduplicates events, grants one entitlement, reconciles daily, models refund and dispute outcomes, and names a live rollback owner.

**Verification, evidence, and uncertainty.** Review the state table with every owner, model-check or property-test legal transitions, replay duplicate and reordered events, inject failures around effects, compare ledgers, scan secrets, test support actions, and rehearse staged rollback. The local skill supplies business and product-routing inputs; the state, event, reconciliation, recovery, and ownership fields are conservative operational requirements. Specialized recurring, platform, fraud, tax, accounting, and regional flows require additional owner-approved fields and current official evidence.

**Second-order consequence.** The artifact converts payment architecture from implicit API choreography into an explicit financial consistency contract.

**Revision decision.** Expand three rows into a multi-owner payment decision, state, evidence, effect, reconciliation, compliance, rollout, and recovery contract.

**Retained seed evidence.** The concrete user goal, use-or-avoid boundary, and proof gate remain mandatory opening fields. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: worked stripe payment integration patterns example with user goal, decision point, failure mode, and verification gate.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Stripe Payment Integration Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide what concrete good, bad, and borderline integrations reveal about financial authority and the cost of customization. The seed's examples differ only in source-loading discipline and never show payment state, trust boundaries, duplicates, asynchronous events, fulfillment, recurring behavior, platform liability, or recovery.

**Recommended default and causal basis.** Judge examples by business fit, current evidence, amount and currency authority, client/server separation, state model, idempotency, event authenticity and ordering, fulfillment, reconciliation, data scope, operational recovery, and reversibility. A payment demo can look successful while containing the exact duplicate, timeout, and trust failures that appear under real customer and provider behavior.

**Operating conditions and assumptions.** The good case solves a named business journey with bounded obligations, the bad case is plausible and exposes concrete loss, and the borderline case states evidence and controls that make a narrower exception acceptable. Examples calibrate architecture and testing but are not production snippets, legal recommendations, or current API instructions.

**Failure boundary and alternatives.** The bad case is cartoonish, the good case assumes official currency, examples omit downstream fulfillment, a hosted surface is called risk-free, or the borderline exception has no expiry and reconciliation. Bounded alternatives and recoveries: use one-time hosted checkout, custom element, saved method, subscription, invoice, Connect platform, refund, migration, or incident examples according to the governing risk.

**Counterexample, gotchas, and operational comparison.** Customer return can precede final evidence, duplicate events are normal enough to design for, event authenticity does not imply order, fulfillment can fail after payment, partial refund changes accounting, and test mode can hide configuration. Good: one immutable order maps to provider correlation, verified repeated events advance an idempotent state machine, entitlement is granted once, and reconciliation catches drift. Bad: a browser callback marks paid and sends goods. Borderline: synchronous low-latency fulfillment is allowed only under a verified current contract, reversible entitlement, duplicate guard, and later reconciliation.

**Verification, evidence, and uncertainty.** Execute each case through success, abandon, additional customer action, timeout, duplicate, reorder, delayed event, fulfillment failure, refund, dispute, and operator repair; compare local and provider records and customer outcomes. The contrast is consistent with the source's product routing and cautious payment-data guidance, while lifecycle behavior is explicitly inferred and testable. Exact event names, statuses, timing, and current product behavior are not asserted without official refresh.

**Second-order consequence.** The borderline case shows that speed can be safe only when reversibility and reconciliation bound the consequence of early action.

**Revision decision.** Replace generic source examples with end-to-end state, event, fulfillment, reconciliation, and recovery contrasts plus a bounded early-action case.

**Retained seed evidence.** Good, bad, and confidence-warning borderline categories remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Stripe Payment Integration Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Stripe Payment Integration Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Stripe Payment Integration Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which operational and review signals show the integration preserves financial truth and where feedback should change design, tests, or provider configuration. The seed measures whether users can install, invoke, debug, and remove an extension and watches extension-type confusion, which is unrelated to payment correctness, customer outcomes, reconciliation, or financial recovery.

**Recommended default and causal basis.** Track local-provider state divergence, age of pending and stuck records, duplicate command and event handling, idempotency conflicts, rejected event verification, fulfillment attempts and reversals, reconciliation exceptions, refund and dispute processing, manual support adjustments, version drift, secret findings, and rollback triggers. Request success and aggregate payment rate can hide duplicate fulfillment, lost events, ledger mismatch, and support work; exception-oriented signals expose broken invariants.

**Operating conditions and assumptions.** Metrics define business state, population, numerator and denominator, amount and currency handling, test or live mode, API version, time window, exclusions, privacy constraints, owner, alert threshold rationale, investigation path, and corrective action. Engineering metrics do not establish revenue causality, fraud effectiveness, accounting close, tax accuracy, or regulatory compliance.

**Failure boundary and alternatives.** Conversion rate proves technical reliability, zero event errors means the endpoint works, raw monetary totals enter unsafe labels, retries inflate counts, one root incident becomes many successes or failures, or dashboards have no reconciliation source. Bounded alternatives and recoveries: use full exception enumeration at low volume, daily reconciliation reports, sampled audit trails, state-age queues, incident reviews, or qualitative support case analysis until stable baselines exist.

**Counterexample, gotchas, and operational comparison.** Delayed legitimate payments look stuck, duplicates can be safely ignored, disputes arrive much later, test traffic contaminates rates, currencies cannot be summed naively, partial refunds alter denominators, and provider reporting times vary. Good: alert on unreconciled paid-provider versus unfulfilled-local records with age and owner, then trace corrections to tests. Bad: celebrate 99 percent API success. Borderline: monitor checkout completion as product context only beside state divergence and fulfillment correctness.

**Verification, evidence, and uncertainty.** Publish definitions, query raw exceptions, sample audit trails, compare provider and local records, test alert generation and owner response, exclude test mode, protect sensitive values, and confirm corrective changes reduce the targeted failure without hiding it. The metric set follows directly from the explicit payment state, duplicate, fulfillment, reconciliation, version, and secret controls introduced in this reference. No merchant volume, baseline, loss tolerance, settlement timing, SLO, currency mix, or alert capacity is available.

**Second-order consequence.** The most valuable payment metric is explainable divergence, because every unexplained mismatch is a potential customer, accounting, or financial inconsistency.

**Revision decision.** Replace extension usability signals with payment-state, duplicate, fulfillment, reconciliation, support, version, and secret feedback loops tied to owners and corrective tests.

**Retained seed evidence.** A leading indicator, failure signal, per-edit verifier, and public-evidence refresh cadence remain preserved as metric structure. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: users can install, invoke, debug, and remove the extension without reading implementation code.
Failure signal: the reference confuses adjacent extension types or omits failure recovery.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide what evidence must exist before this reference is complete and before a concrete payment integration is ready for staged launch. The seed checks seven generic document features but not business model, parties, money flow, authority, amounts, lifecycle states, idempotency, event verification, fulfillment, reconciliation, secrets, API versions, test/live separation, refunds, disputes, subscriptions, Connect, or launch recovery.

**Recommended default and causal basis.** Require exact artifact structure and evidence labels plus a reviewed business and state contract, current official product evidence, repository and account configuration, trust boundaries, duplicate-safe commands and events, fulfillment and reversal policy, reconciliation, secret and data controls, test/live isolation, adverse-path tests, observability, support procedures, rollout, rollback, and accountable owners. Payment completeness spans code, provider, account, operations, and business policy; omitting any one can leave an apparently functional checkout financially inconsistent.

**Operating conditions and assumptions.** Every criterion points to a source version, requirement, state row, code site, account setting, test output, reconciliation query, owner approval, runbook step, or explicit out-of-scope decision. The artifact gate proves this reference; the launch gate remains conditional on a real integration, current provider evidence, account review, and accountable approvals.

**Failure boundary and alternatives.** A successful sandbox journey proves readiness, webhooks exist but duplicates are untested, compliance is a checkbox without owner, refunds are assumed to undo fulfillment, or artifact counts substitute for payment proof. Bounded alternatives and recoveries: use a reduced isolated prototype checklist with no live credentials, add Billing, Connect, migration, fraud, tax, or compliance annexes, or block launch when a governing owner or current official contract is absent.

**Counterexample, gotchas, and operational comparison.** Feature flags and account settings can select different paths, live identifiers can leak into tests, event endpoints can pass health checks but reject signatures, support tools can bypass state rules, and downstream entitlements can outlive refunds. A complete one-time flow has approved requirements, current product evidence, durable state transitions, duplicate and reorder tests, one-time fulfillment, reconciliation, secret review, staged rollout, support recovery, and rollback; a green UI demo is incomplete.

**Verification, evidence, and uncertainty.** Map every checklist row to evidence, recompute artifact counts and hashes, review official and account scope, run adverse lifecycle and reconciliation tests, inspect secret and mode boundaries, rehearse support and rollback, and reread the full contract. The accepted evolution gates and conservative payment systems model directly support this completion matrix. Specialized legal, PCI, tax, accounting, fraud, and regional criteria require qualified owners and cannot be completed from this corpus.

**Second-order consequence.** Payment completeness means every externally observable financial state has a local explanation, owner, verification path, and recovery.

**Revision decision.** Replace seven structural bullets with evidence-indexed artifact, business, state, trust, provider, operations, support, launch, and recovery checks.

**Retained seed evidence.** Role scenario, decision guide, hierarchy, artifact, examples, metrics, and adjacent routing remain preserved as document-level checks. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Stripe Payment Integration Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide when this general payment architecture reference should hand off to current Stripe product guidance, a stack-specific backend reference, or an accountable non-engineering owner. The seed routes to command, hook, MCP, settings, and manifest references and then offers tautological stripe, payment, and integration labels, which do not address Billing, Connect, backend reliability, security, compliance, accounting, or incident response.

**Recommended default and causal basis.** Stay here for cross-cutting state and evidence design; route recurring models to current official Billing guidance, platforms to current official Connect guidance, implementation to the repository's language and backend reliability reference, security and secrets to a dedicated review, and PCI, tax, accounting, fraud, and legal questions to qualified owners. Specialized domains control facts and obligations that a general, unrefreshed reference cannot safely synthesize.

**Operating conditions and assumptions.** The handoff names unresolved question, destination or owner, current source and version, inherited state contract, sensitive data scope, expected artifact, blocking conditions, return evidence, and one integration owner. This section cannot appoint compliance or business authorities and must preserve their ability to block launch.

**Failure boundary and alternatives.** Routing follows the word Stripe, an official product page replaces system tests, engineering answers liability or tax, stack guidance chooses money flow, or several owners mutate the same state model independently. Bounded alternatives and recoveries: combine provider and backend specialists under one decision record, request official support clarification, use repository architecture as primary, preserve a provisional blocked state, or isolate a prototype from live systems.

**Counterexample, gotchas, and operational comparison.** Billing and Connect can coexist, backend retries depend on provider semantics, security can change product choice, compliance scope depends on data flow, accounting state may differ from application state, and support procedures can bypass normal paths. Good: route marketplace liability to Connect and legal owners, implement event handling under the stack's reliability guide, then return to reconcile one state contract. Bad: send a webhook question to plugin manifest guidance. Borderline: use GitHub Actions only for CI secret controls while payment behavior remains under provider and backend evidence.

**Verification, evidence, and uncertainty.** Confirm the destination's authority and freshness, pass exact state and risk context, prohibit overlapping writers, collect the specialist artifact, run cross-boundary integration and reconciliation tests, and update the central decision contract. The local skill directly distinguishes Billing and Connect, while the seed's extension-surface routes are visibly mismatched to payment work. The repository inventory may contain several stack references, but no concrete implementation language or organizational owner is specified.

**Second-order consequence.** Routing is part of financial consistency because specialized decisions must return to one shared state and recovery model.

**Revision decision.** Replace extension and tautological routes with product, stack, security, compliance, accounting, fraud, legal, and support handoffs plus return conditions.

**Retained seed evidence.** The principle of moving to a narrower reference once a surface is selected remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use command, hook, MCP, settings, or manifest references when one extension surface is already selected.
Adjacent reference 1: consider the stripe adjacent reference when the current task pivots away from stripe payment integration patterns.
Adjacent reference 2: consider the payment adjacent reference when the current task pivots away from stripe payment integration patterns.
Adjacent reference 3: consider the integration adjacent reference when the current task pivots away from stripe payment integration patterns.

## Workload Model

**Decision supported.** This section helps decide how to bound an integration review so state, failure, test, and recovery evidence remains complete under the intended payment workload. The seed bounds one theme, mapped sources, one downstream review, and generic reference synthesis, but it provides no payment workload dimensions such as business models, currencies, regions, payment methods, event rates, fulfillment systems, subscription lifetimes, connected accounts, or reconciliation windows.

**Recommended default and causal basis.** Describe business flows, payer and beneficiary counts, order and payment volumes, burst and retry behavior, amount and currency ranges, regions, methods, customer-action paths, event types and lag, subscriptions or connected accounts, fulfillment effects, retention, reconciliation cadence, and support load. Capacity and correctness failures emerge from lifecycle diversity and asynchronous fan-out, not simply source count or changed symbols.

**Operating conditions and assumptions.** The workload packet states representative and worst-case scenarios, distributions, concurrency, duplication and reorder assumptions, downstream systems, provider and account limits pending verification, data classification, SLO owners, test fixtures, split triggers, and rollback units. This model frames verification and does not establish provider capacity, financial reserves, staffing, or live SLOs.

**Failure boundary and alternatives.** One successful payment represents workload, averages hide bursts, test mode models live scale, payment objects are counted without fulfillment, unlimited retries are assumed rare, or platform and subscription flows are combined without independent state models. Bounded alternatives and recoveries: split by business model, region, currency, method family, subscription lifecycle, connected-account funds flow, event consumer, fulfillment system, or reconciliation unit; stage a low-risk cohort.

**Counterexample, gotchas, and operational comparison.** Currency minor units differ, payment method behavior varies, events can burst after outage, subscription work is time-distributed, connected accounts multiply configuration, retries amplify load, and provider rate limits are current external facts. Good: bound a one-time launch to named regions, currencies, event cases, daily reconciliation, and one fulfillment system before expanding. Bad: claim one theme supports production traffic. Borderline: use synthetic burst tests as engineering evidence while keeping live capacity provisional.

**Verification, evidence, and uncertainty.** Derive fixtures from declared workload, stress duplicate and delayed events, test queue and database limits, measure reconciliation completion, simulate downstream outage, compare provider limits during official refresh, and revisit boundaries after rollout. The need for workload-specific product routing comes from the local skill; the detailed workload dimensions follow the distributed state and recovery model. No merchant volume, geography, methods, account limits, SLOs, retention, or downstream capacities are supplied.

**Second-order consequence.** The effective payment workload is every state transition and side effect that may need replay, reconciliation, or human recovery, not only API request rate.

**Revision decision.** Replace reference-synthesis capacity with payment lifecycle, volume, diversity, event, fulfillment, reconciliation, support, and staged-expansion boundaries.

**Retained seed evidence.** Bounded scope, all mapped evidence, one downstream review, split-on-excess, source comparison, and required worked artifact remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Stripe Payment Integration Patterns as a general reference operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | idiomatic reference selection and synthesis work where the reference must prevent generic advice and preserve evidence boundaries | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one theme, all mapped local sources, current external evidence when available, and one downstream task review | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include no heading discovered; no heading discovered | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is worked stripe payment integration patterns example with user goal, decision point, failure mode, and verification gate | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide which deterministic invariants and baseline-derived service targets define a trustworthy payment integration. The seed targets source labels, 18-of-20 routing accuracy, zero unsupported claims, and recovery clarity, but it omits duplicate financial effects, state divergence, event authenticity, stuck records, fulfillment consistency, reconciliation completion, secret exposure, and recovery objectives.

**Recommended default and causal basis.** Make no duplicate irreversible effect, authenticated event admission, idempotent transition application, amount and currency consistency, test/live isolation, and no secret exposure release invariants; define evidence-backed targets for pending-state age, event processing, fulfillment, reconciliation, support recovery, and rollback. Financial correctness needs hard state invariants, while timing and availability targets must reflect a merchant's real workload and recovery capacity rather than an invented global number.

**Operating conditions and assumptions.** Each target defines business state, population, unit, mode, API version, window, baseline, threshold rationale, detection source, owner, customer and financial consequence, breach containment, and recovery deadline. These targets do not certify provider uptime, bank settlement, fraud loss, tax accuracy, or compliance effectiveness.

**Failure boundary and alternatives.** 18 selected reviews become accuracy, zero observed divergence means monitoring works, averages replace tails, event receipt is confused with correct transition, or a target has no reconciliation source and response owner. Bounded alternatives and recoveries: enumerate every transaction at low volume, use queue age rather than latency, adopt stricter invariant checks before setting service targets, manually review exceptions, or block launch until baselines and ownership exist.

**Counterexample, gotchas, and operational comparison.** Legitimate asynchronous delay looks like failure, duplicate events can be harmless, provider and accounting cutoffs differ, partial refunds complicate equality, test traffic contaminates targets, and incident containment can temporarily reduce availability. Good: guarantee one fulfillment per order and alert on unreconciled provider-success/local-pending records within a merchant-approved window. Bad: promise 99.99 percent reliability without workload or recovery. Borderline: use a provisional reconciliation target during canary rollout with daily review and recalibration.

**Verification, evidence, and uncertainty.** Property-test state invariants, replay duplicates and reorderings, inject endpoint and fulfillment outages, reconcile complete test populations, scan secrets, exercise alert and containment paths, and review target performance after staged traffic. The hard invariants follow the designed state contract; source and unsupported-claim targets remain directly supported by the seed. No merchant baseline, live event lag, provider objective, support schedule, transaction volume, or loss tolerance is available.

**Second-order consequence.** Payment reliability is the ability to detect, explain, and recover every divergence without repeating an irreversible effect.

**Revision decision.** Retain evidence invariants, remove fixed routing precision, and add financial-state, event, fulfillment, reconciliation, secret, containment, and recovery targets.

**Retained seed evidence.** Source-boundary preservation, decision sampling, unsupported-claim rejection, and explicit recovery paths remain preserved as reference-level controls. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide how to classify payment failures by invariant, observation, containment, reconciliation, and customer-safe recovery rather than by API error alone. The seed lists source drift, generic advice, implicit decisions, and unsynthesized corpora but no failures that move, strand, duplicate, misattribute, expose, or misreport money and fulfillment.

**Recommended default and causal basis.** Cover duplicate initiation, lost response, forged or replayed event, out-of-order transition, client-authoritative success, amount or currency mismatch, local/provider divergence, fulfillment failure, stuck customer action, refund or dispute drift, subscription lifecycle miss, platform funds misrouting, secret leak, mode contamination, and API-version incompatibility. The same network timeout can mean no effect, a completed effect with lost acknowledgment, or a later asynchronous outcome, so cause and recovery cannot be inferred from the exception alone.

**Operating conditions and assumptions.** Rows state invariant, trigger, possible provider and local states, customer and financial impact, detection, immediate freeze or containment, safe retryability, reconciliation query, compensating action, communication, owner, and escalation. The table guides engineering incident design and does not replace provider support, accounting judgment, legal notification, or fraud response.

**Failure boundary and alternatives.** Mitigation says retry, refund is automatic compensation, event verification alone prevents duplicates, rollback ignores external objects, support edits the database directly, or a platform flow's liability assumption remains implicit. Bounded alternatives and recoveries: pause fulfillment, quarantine records, disable one route, reconcile manually, issue an audited compensating action, roll back a deployment while preserving schema compatibility, or escalate provider and compliance support.

**Counterexample, gotchas, and operational comparison.** Timeouts are ambiguous, event authenticity and freshness are distinct, duplicate refunds are possible, fulfillment may be irreversible, disputes arrive late, subscription changes have future effective times, and Connect movements involve several parties. Good: after a timeout, query or await authoritative evidence using the original idempotency domain, then apply one local transition and reconcile. Bad: submit a new payment. Borderline: manually fulfill after verified provider success only through an audited idempotent support action.

**Verification, evidence, and uncertainty.** Reproduce each failure around every side effect, capture provider and local state before and after, replay duplicates and reorderings, exercise containment and customer communication, run reconciliation, and prove repeated recovery is itself safe. The failure classes are conservative consequences of distributed financial state, while product-family boundaries are source-reported. Current provider statuses, event taxonomy, dispute timing, Connect ledger semantics, and available recovery APIs were not verified.

**Second-order consequence.** Payment failure handling begins by preserving ambiguity safely until authoritative evidence resolves it; premature compensation can create a second loss.

**Revision decision.** Replace generic process rows with a causal financial-state registry spanning initiation, events, fulfillment, reversals, subscriptions, platforms, secrets, modes, versions, and recovery.

**Retained seed evidence.** Source drift, generic unverified advice, implicit decisions, and unsynthesized lists remain preserved as upstream process failures. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| decision path remains implicit | reader cannot tell when to adopt, adapt, or avoid the pattern | add decision table, cost of being wrong, and adjacent-reference route |
| large corpus becomes list | many sources are indexed but not synthesized into ranked guidance | classify canonical, supporting, legacy, duplicate, and conflicting sources |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a failed payment operation may be retried, how one logical effect remains singular, and what backpressure prevents financial amplification. The seed discusses evidence refresh and agent checkpoints but does not distinguish payment reads, idempotent logical commands, ambiguous timeouts, event delivery, fulfillment, refunds, reconciliation, or queue overload.

**Recommended default and causal basis.** Classify the operation and failure; retry only within a stable logical-command identity and bounded deadline when current provider semantics support it, treat lost acknowledgments as ambiguous until queried or reconciled, make event and fulfillment consumers idempotent, and stop producers or shed nonessential work before queues become unbounded. A retry is another request, not proof that the first failed; without identity and reconciliation it can duplicate charges, refunds, entitlement, or fund movements.

**Operating conditions and assumptions.** The policy records operation, side effect, retryable classification, idempotency scope and retention assumption pending official verification, attempt and time budget, delay strategy, queue capacity, concurrency, cancellation, terminal state, reconciliation, telemetry, and owner. This guidance cannot define provider-specific retry parameters or authorize automated financial compensation without current contracts and business approval.

**Failure boundary and alternatives.** All timeouts retry with a new key, validation or authorization failures retry, customer confirmation is repeated automatically, refund retries can duplicate, nested client and worker retries multiply, or event backlog grows without admission control. Bounded alternatives and recoveries: query current state, wait for authenticated event evidence, mark the record ambiguous, pause fulfillment, enqueue bounded reconciliation, escalate manual review, reject new work, reduce concurrency, or roll back while draining safely.

**Counterexample, gotchas, and operational comparison.** The first effect can succeed after caller timeout, idempotency windows and endpoint support are current provider facts, a changed request under one key can conflict, customer action is not machine-retryable, and cancellation can occur after remote effect but before local commit. Good: a lost payment-creation response retains one logical identity, blocks duplicate fulfillment, resolves through provider evidence, and records one transition. Bad: loop creation with random keys. Borderline: retry a read under a parent deadline while isolating it from side-effect and event retry budgets.

**Verification, evidence, and uncertainty.** Inject failures before send, after send, after remote effect, before local commit, and during acknowledgment; count logical and physical attempts, inspect duplicate effects, saturate queues, cancel workers, reconcile records, and confirm terminal errors preserve ambiguity. Bounded retries and duplicate-safe effects are strong distributed-systems controls; exact Stripe idempotency and delivery behavior remains subject to current official evidence. Endpoint support, idempotency retention, provider retry schedule, rate limits, and recommended backoff were not verified.

**Second-order consequence.** The safe retry unit is a business command with one identity and reconciliation path, not an HTTP request.

**Revision decision.** Separate evidence refresh from payment operation retries and add logical identity, ambiguity, reconciliation, queue capacity, cancellation, stop, and escalation rules.

**Retained seed evidence.** Failure classification, one bounded external refresh, red-gate backpressure, frequent checkpoints, sole ownership, and merge invariants remain preserved for reference work. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide which structured observations let operators explain a payment outcome end to end without leaking secrets or payment data. The seed records sources, proof, reviewer time, uncertainty, and refresh triggers but omits payment correlation, state transitions, duplicate handling, event verification outcome, queue pressure, fulfillment, reconciliation, support actions, mode separation, and sensitive-data prohibitions.

**Recommended default and causal basis.** Record stable local order and payment identifiers, provider correlation identifiers, event identity, test or live mode, API version, prior and next state, transition source, verification result, logical-command identity, attempt count, queue age, fulfillment outcome, reconciliation status, support action, and trace correlation with strict redaction. Financial incidents require reconstructing causality across requests, events, workers, fulfillment, and operator actions, while raw payload logging can create a second security and compliance incident.

**Operating conditions and assumptions.** Fields have stable semantics and bounded cardinality, timestamps and units are explicit, transitions are auditable, duplicates are distinguishable from failures, sensitive values are absent, retention and access are controlled, and every alert has an owner and playbook. This checklist does not establish legal retention, PCI scope, privacy compliance, accounting audit sufficiency, or incident-notification duties.

**Failure boundary and alternatives.** API keys, webhook secrets, client secrets, raw payment details, full payloads, or customer PII enter logs; free-form strings replace state fields; amounts are aggregated without currency; or retries overwrite the first failure. Bounded alternatives and recoveries: store redacted audit records separate from application logs, retain provider object references for authorized lookup, sample high-volume success events, emit exception-only metrics, or use temporary incident diagnostics with expiry.

**Counterexample, gotchas, and operational comparison.** Identifiers can still be sensitive, metadata may contain user input, error bodies can echo payloads, metric labels can explode, clock skew affects event lag, support corrections need immutable audit, and test traffic can contaminate live dashboards. Good: trace one order from logical command through verified duplicate event, idempotent fulfillment, and reconciliation using opaque IDs and no payment details. Bad: log the webhook body and secret on signature failure. Borderline: retain a redacted payload digest for diagnosis only after privacy and collision review.

**Verification, evidence, and uncertainty.** Exercise success, duplicate, forged, delayed, failed fulfillment, refund, dispute, reconciliation, and manual repair; inspect logs and metrics for field coverage, redaction, cardinality, access, retention, correlation, and owner response. Secret and PCI cautions are directly supported by the local skill; the structured lifecycle schema follows the state contract. The correct retention, access, privacy classification, backend, sampling, and exact provider-safe fields require organizational and current provider review.

**Second-order consequence.** Payment observability must make state transitions explainable while making sensitive payment data unavailable by default.

**Revision decision.** Replace generic audit bullets with a redacted payment state, command, event, fulfillment, reconciliation, support, mode, access, and retention schema.

**Retained seed evidence.** Loaded sources, exact proof, reviewer or runtime timing, uncertainty, refresh trigger, leading and failure signals, and compact summaries remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture reviewer decision, unresolved uncertainty, and next refresh trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to measure payment integration performance without rewarding early fulfillment, unsafe retries, missing verification, or hidden state divergence. The seed imposes an unsupported ten-minute reviewer p95 and repeats extension usability, while omitting customer latency, provider dependency, event lag, queue age, fulfillment time, reconciliation duration, throughput, and financial correctness guards.

**Recommended default and causal basis.** Separate customer-perceived initiation, merchant server processing, provider round-trip, event ingestion, transition and fulfillment, queue saturation, and reconciliation; define representative workload, baseline, environment, metric, correctness guard, variance, threshold owner, and rollback for each claimed path. External latency and asynchronous completion are not one metric, and optimizing the visible request can shift work into unbounded queues or weaken the evidence required for financial action.

**Operating conditions and assumptions.** Benchmarks and load tests preserve state invariants, include duplicates and failures, distinguish test from live evidence, report distributions and saturation, correlate resources, and compare like-for-like API versions and configurations. Local measurements cannot certify provider latency, conversion, settlement speed, live capacity, or business impact.

**Failure boundary and alternatives.** Average checkout time proves reliability, a local mock predicts provider latency, events are acknowledged before durable work without recovery, queues hide slower consumers, reviewer time becomes payment performance, or one p95 is applied to every merchant. Bounded alternatives and recoveries: profile local hot paths, load-test event consumers with synthetic fixtures, measure queue age and reconciliation completion, stage a canary, optimize database transitions, or accept slower reversible behavior over faster unsafe action.

**Counterexample, gotchas, and operational comparison.** Provider and authentication latency vary, test mode differs, cold starts and caches distort runs, retries amplify traffic, webhook bursts follow outage, currencies and methods create different journeys, and instrumentation can leak data. Good: load-test duplicate event bursts, assert one transition and fulfillment, measure queue age and reconciliation drain, and roll back if saturation violates a merchant-owned target. Bad: skip event verification to reduce latency. Borderline: use synthetic provider latency for capacity planning while labeling live experience unknown.

**Verification, evidence, and uncertainty.** Freeze code and configuration, run correctness and redaction gates first, execute repeated representative and adverse workloads, inspect distributions and bottlenecks, test overload and recovery, compare state ledgers, reproduce, and record decision plus uncertainty. The method follows directly from the payment state, backpressure, observability, and reconciliation controls; no numerical performance claim is inherited from the source. No workload, provider objective, merchant SLO, infrastructure, region, account, or baseline is supplied.

**Second-order consequence.** Payment performance is acceptable only when the system remains duplicate-safe, explainable, and recoverable at the measured load.

**Revision decision.** Remove the reviewer-time threshold and extension signals, then add decomposed payment path metrics, correctness guards, adverse load, saturation, recovery, and merchant-owned thresholds.

**Retained seed evidence.** Input size, source count, tool calls, wall time, percentile structure, reviewer decision time, actionable next step, and stop condition remain preserved only for reference-work measurement. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require source-boundary preservation and p95 under 10 minutes for a reviewer to identify the next verification action.
Leading indicator to measure: users can install, invoke, debug, and remove the extension without reading implementation code.
Failure signal to watch: the reference confuses adjacent extension types or omits failure recovery.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide when this general reference can still coordinate one payment contract and when specialization, decomposition, and independent accountable owners are mandatory. The seed stops at multiple systems, more than one ownership boundary, unbounded discovery, or production traffic without an SLO, but ordinary payments already cross several ownership boundaries and the statement ignores currencies, regions, subscriptions, platforms, legal entities, ledgers, and migrations.

**Recommended default and causal basis.** Continue while one integration owner can enumerate parties, funds flow, states, evidence, effects, reconciliation, tests, and rollback; split or route when independent merchants, legal entities, connected accounts, recurring schedules, regions, currencies, methods, ledgers, fulfillment systems, data migrations, or compliance domains prevent that closure. Payment scale becomes unsafe when financial state and recovery cannot be explained and reversed within one coherent contract, not merely when data crosses a second module or owner.

**Operating conditions and assumptions.** The boundary review inventories businesses, accounts, parties, currencies, regions, products, provider objects, event consumers, ledgers, downstream effects, volumes, SLOs, compliance scopes, owners, merge and rollout order, and rollback units. This reference remains a shared control framework after routing but cannot own platform governance, global compliance, treasury, accounting consolidation, or live migration.

**Failure boundary and alternatives.** One state model hides several funds flows, parallel teams mutate shared transitions, a split loses end-to-end reconciliation, high traffic launches without objectives, or decomposition follows line count while liability remains mixed. Bounded alternatives and recoveries: split by merchant or legal entity, funds flow, recurring versus one-time lifecycle, connected-account model, region, currency, event consumer, ledger, fulfillment, migration phase, or rollback cohort; keep one integration ledger and verifier.

**Counterexample, gotchas, and operational comparison.** Subscriptions span releases, refunds and disputes cross historical versions, platform transfers couple accounts, currency conversion affects ledgers, shared event endpoints multiplex flows, and rollback cannot erase external financial records. Good: keep a bounded one-time merchant flow under one state contract, then split a marketplace launch by funds-flow and account model with shared reconciliation. Bad: use this reference alone for multi-country platform liability. Borderline: share infrastructure across flows only when identifiers, state namespaces, limits, and owners remain isolated.

**Verification, evidence, and uncertainty.** Map every party, state store, event route, effect, ledger, and recovery; prove each slice has complete input and output contracts; assign owners; run cross-slice reconciliation and incident tests; and reevaluate after scope or volume changes. The local skill directly distinguishes recurring and Connect platform surfaces; the evidence-closure boundary follows the payment consistency model. No universal account, currency, region, volume, legal-entity, or connected-account threshold defines scale.

**Second-order consequence.** Payment architecture scales safely by preserving explainable funds-flow and reconciliation units, not by centralizing all Stripe calls.

**Revision decision.** Replace the one-ownership cutoff with funds-flow and reconciliation closure, explicit scale multipliers, decomposition axes, integration ownership, and re-entry checks.

**Retained seed evidence.** Multiple systems, unbounded discovery, missing production SLOs, sole file ownership, merge checkpoints, context-drift control, and graph narrowing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Stripe Payment Integration Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which future authorized queries should refresh each consequential integration claim before implementation, migration, or go-live. The seed's generic title searches are less useful than the official Stripe URLs already embedded in the local skill and omit the exact lifecycle, version, event, idempotency, Billing, Connect, migration, data, and launch claims that can drift.

**Recommended default and causal basis.** Search official Stripe domains by exact obligation: integration options, API and SDK versioning, object lifecycle, idempotent requests, webhook verification and delivery, testing, go-live, saved methods, dynamic methods, Billing, subscriptions, Connect funds flow and controller properties, refunds, disputes, reconciliation, and PCI or data migration. Claim-specific queries return evidence that can update one state, trust, or product decision, whereas a generic best-practices search mixes eras and business models.

**Operating conditions and assumptions.** Each query row includes claim at risk, preferred official domain, product and API version, account or region scope, expected document type, linked migration, affected contract section, conflict rule, reproduction, owner, and expiry. Search results are candidate evidence and cannot approve live configuration, compliance, liability, tax, accounting, or launch.

**Failure boundary and alternatives.** Search snippets become guidance, third-party tutorials outrank primary docs, latest pages are applied to pinned integrations, one-time payment docs answer subscription questions, or a query result changes code without adverse-path tests. Bounded alternatives and recoveries: open the exact embedded URL, inspect SDK and lockfile docs offline, review account configuration, consult official support for ambiguity, use migration and changelog sources, or block the claim.

**Counterexample, gotchas, and operational comparison.** Docs can redirect, versions and SDKs differ, dashboard-managed behavior changes without code, Connect terminology evolves, regional methods vary, compliance pages are not legal advice, and examples can omit retries or reconciliation. Good: query official event-delivery and idempotency documentation for the pinned API context, then replay duplicates and ambiguous timeouts. Bad: search Stripe best code and copy a blog. Borderline: use a current official quickstart only for surface syntax while retaining the full state and failure contract.

**Verification, evidence, and uncertainty.** Open the complete primary source, capture date, version, account and region assumptions, read linked migrations and caveats, reproduce in isolated test mode, compare repository behavior, update the decision record, and rerun affected gates. The local skill directly supplies official candidate URLs and product topics, and the evolved state model identifies additional exact claims needing refresh. No queries were executed, so terminology, page location, current recommendations, and completeness remain unknown.

**Second-order consequence.** A refresh query should be designed to falsify one integration assumption, not merely find newer wording.

**Revision decision.** Replace three title-only searches with a versioned official-Stripe query matrix tied to state, product, event, trust, migration, and launch decisions.

**Retained seed evidence.** Official documentation, GitHub repository examples, and release or migration search families remain preserved, with official primary sources preferred. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | stripe payment integration patterns official documentation best practices |
| `github_repository_query_phrase` | stripe payment integration patterns GitHub repository examples |
| `release_notes_query_phrase` | stripe payment integration patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide how a reader can distinguish observed local skill text, current provider evidence, repository facts, account and owner decisions, and systems inference in every payment recommendation. The seed defines three labels but does not disclose that the local rows are byte-identical, that their Stripe statements were not refreshed, that official Stripe URLs are embedded but unopened, or that the mapped external rows cannot support payment semantics.

**Recommended default and causal basis.** Attach a claim ledger with boundary label, exact path or URL, local hash or provider version, duplicate status, complete-read state, retrieval date, account and region scope, faithful paraphrase, inference step, contradiction, confidence, verification, owner, and refresh trigger. Payment advice becomes hazardous when a source-reported preference, an engineering invariant, and a current API fact are written with the same authority.

**Operating conditions and assumptions.** Local statements cite the shared hash and wording, current provider claims require opened official versioned evidence, repository behavior cites code and tests, account facts cite configuration review, owner policies name approval, and inference names counterconditions. This ledger provides traceability, not provider endorsement, legal provenance, compliance certification, account approval, or authority to move money.

**Failure boundary and alternatives.** Duplicate files corroborate, embedded links count as reads, agent websites validate payments, a systems inference becomes a Stripe guarantee, current product deprecation is asserted from the unversioned skill, or a hash is treated as correctness. Bounded alternatives and recoveries: downgrade to provisional guidance, preserve a conflict, omit the claim, request official support, inspect current repository and account evidence, route a domain owner, or block implementation and launch.

**Counterexample, gotchas, and operational comparison.** Official pages are mutable, account versions and settings vary, product names can persist while behavior changes, local code may lag intentionally, source absolute language can hide exceptions, and compliance statements need qualified interpretation. Good: state that the shared local skill at 838eb4e00a22f817b8577be230600547441493bf8c7aa15b0ee7e04f71f875cf reports a Checkout preference, then require current official and account validation. Bad: say Checkout is universally current. Borderline: use duplicate-safe state transitions as combined inference while leaving exact webhook behavior unclaimed.

**Verification, evidence, and uncertainty.** Recompute local and seed hashes, compare duplicate bytes, audit every product statement for source-reported or refreshed status, confirm unrelated external rows stay process-only, inspect inference scope, scan numerical claims, and trace operational guidance to tests or unknowns. The complete local text, duplicate identity, embedded URLs, seed external roles, and no-browse status are directly verified. Current Stripe APIs, product recommendations, dashboard behavior, regional availability, pricing, contractual terms, event semantics, and compliance obligations remain unverified.

**Second-order consequence.** Strict evidence labels do not weaken payment guidance; they prevent architecture principles from impersonating provider guarantees and tell the next reviewer exactly what to refresh.

**Revision decision.** Expand three labels into duplicate-aware local, unopened official candidate, process-only external, repository, account, owner, and inference boundaries with version, scope, proof, and refresh rules.

**Retained seed evidence.** Local-corpus fact, external-research fact, and combined-evidence inference remain the required top-level labels. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
