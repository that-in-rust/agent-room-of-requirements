# Stripe Payment Integration Reference

Companion reference for `SKILL.md`. Covers evidence boundaries, architectural tradeoffs, failure modes, retry/backpressure rules, observability, workload and scale limits, and refresh queries for Stripe integrations.

## Idiomatic Thesis Synthesis Statement

Choose the narrowest Stripe surface that fits the business model, while keeping payment and fulfillment decisions in a durable, server-owned state machine driven by authenticated, duplicate-safe asynchronous evidence and reconciled against the provider under a controlled API version.

Redirects, synchronous API responses, and event arrival order are observations, not the financial ledger. Define order/payment identities, immutable amounts and currencies, allowed monotonic transitions, provenance, idempotency, one-time fulfillment, refunds and disputes, reconciliation, version ownership, adverse-path tests, and recovery.

Alternatives:
- Hosted or embedded Checkout to minimize collection and compliance scope.
- Payment Element / custom orchestration only for a measured UX or checkout-state need.
- Billing / Subscriptions for recurring models; Payment Links or Invoicing for simpler journeys.
- Connect for multi-party platform funds flows.
- Defer surface selection until business, account, regional, and compliance constraints are known.

Worked grades:
- **Good:** monotonic validated transitions, duplicate-safe events, and one-time idempotent fulfillment backed by reconciliation.
- **Bad:** marking an order paid and shipping goods from a browser return URL.
- **Borderline:** using synchronous confirmation for UX feedback while withholding irreversible fulfillment until verified asynchronous evidence (or granting only a reversible, duplicate-guarded, expiring entitlement reconciled later).

## Source Evidence Mapping and Local Corpus Hierarchy

Authority must match the claim — no single source is canonical for every question:

| Claim domain | Authoritative source | Prohibited inference |
|---|---|---|
| Product/API semantics, webhook guarantees, idempotency windows, deprecations | Current official versioned Stripe docs and changelogs | Treating an unrefreshed local skill snapshot or blog post as current API truth |
| Enabled payment methods, account capabilities, live API version | Target Stripe account configuration (test and live differ) | Assuming latest docs match a pinned account |
| Local contracts, state transitions, serialization | Repository code, lockfiles, and automated tests | Inferring runtime compliance from passing unit tests alone |
| Legal, tax, PCI-DSS, accounting, fraud, regional obligations | Qualified business, legal, accounting, and compliance owners | Inferring compliance from code or documentation |
| CI secret scanning and test automation | CI platform documentation (e.g. GitHub Actions) | Citing CI or agent-instruction docs (`AGENTS.md`, Codex guides) for Stripe API behavior |

Corpus deduplication note: the historical local copies of the Stripe best-practices skill ([the curated skill](../../S02-curated-upstream-skill-snapshots/stripe/stripe-best-practices/SKILL.md)) were byte-identical (SHA-256 `838eb4e00a22f817b8577be230600547441493bf8c7aa15b0ee7e04f71f875cf`) and count as **one** textual source, not independent corroboration. Embedded official Stripe URLs remain refresh candidates until opened and verified against the target API version, account, and region.

Record for every evidence claim: boundary label (`local_corpus_sourced_fact`, `external_research_sourced_fact`, `combined_evidence_inference_note`), exact source, hash/version, retrieval date, account/region, conflict status, verification method, and owner. Preserve conflicts with an ADR, contract tests, and owner review rather than silently overriding them.

## Pattern Priority Ranking (Qualitative)

1. Server-authoritative state and invariant-preserving transitions.
2. Duplicate-safe commands and events (stable idempotency keys, event deduplication).
3. Authenticated asynchronous event handling (raw-body signature verification, out-of-order tolerance).
4. Fulfillment gating (at-most-once grant) and scheduled reconciliation.
5. Secret custody, test/live isolation, and payment-data boundaries.
6. Business-model and Stripe surface routing.
7. Observability, support recovery, and launch verification.

Rank separately for one-time, subscription, Connect, and migration work. Provider-hosted surfaces reduce card-collection complexity but do not remove server state, event, fulfillment, or reconciliation obligations.

## Decision Tradeoff Guide

Compare hosted Checkout, embedded Checkout, Payment Element, direct PaymentIntents orchestration, Billing, Invoicing/Payment Links, SetupIntents, and Connect across: business fit, UX control, compliance surface, state ownership, regional eligibility, migration cost, and recovery complexity. More customization transfers more lifecycle and failure responsibility to the merchant.

- **Adopt** when requirements and current official/account evidence agree.
- **Adapt** when local fit is strong but current Stripe guidance or account settings changed.
- **Avoid** when evidence is thin, conflicting, or relies on deprecated APIs.
- Cost includes duplicate charges, withheld fulfillment, negative-balance liability, migration, support, and accounting — not only engineering hours.
- Dynamic payment methods, taxes/discounts, saved-method consent/off-session mandates, Connect charge types (direct vs. destination, `on_behalf_of`), and API object changes directly affect amount authority, liability, and reconciliation.

## Theme-Specific Artifact: Payment Integration Decision and State Contract

Required before production money movement:

```yaml
user_goal_statement: "<concrete payment goal>"
decision_boundary_rule: "<when to use and when to avoid this integration>"
verification_gate_rule: "<commands, checklists, and review questions proving correctness>"
business_model: "<one-time | subscription | invoice | connect-direct | connect-destination>"
parties_and_liability: "<merchant of record, payer, beneficiary, negative-balance liability>"
funds_flow: "<source -> platform/connected account -> payout>"
amount_currency_authority: "<immutable server order snapshot; tax/discount source>"
surface_and_version:
  stripe_surface: "<CheckoutSessions | PaymentIntents | Billing | Connect>"
  api_version: "<pinned YYYY-MM-DD>"
  sdk_version: "<pinned package version>"
  evidence_refreshed_at: "<date and official doc URLs>"
identifiers:
  local_order_id: "<immutable primary key>"
  provider_ids: ["<checkout_session_id>", "<payment_intent_id>", "<charge_id>"]
state_machine:
  states: [created, pending, requires_action, paid, fulfilled, partially_refunded, refunded, disputed, failed, canceled]
  allowed_transitions: "<explicit monotonic transition table>"
idempotency:
  command_key_scope: "<logical command + stable order/action id>"
  event_dedupe_store: "<durable unique table on provider event id>"
fulfillment:
  grant_rule: "<at-most-once entitlement bound to order id>"
  reversal_rule: "<how refunds and disputes revoke or flag entitlements>"
reconciliation:
  cadence: "<e.g. daily>"
  drift_queries: ["provider_paid_local_unfulfilled", "local_paid_provider_refunded_or_disputed"]
secrets_and_mode:
  isolation: "<strict test/live key, webhook secret, and record separation>"
  redaction: "<no keys, webhook secrets, client secrets, PAN, or full payloads in logs>"
rollout_and_rollback:
  rollout: "<sandbox -> canary -> full>"
  rollback_owner: "<named owner>"
  support_recovery: "<authenticated, audited, idempotent operator tool>"
owners:
  engineering: "<owner>"
  reconciliation_and_support: "<owner>"
  compliance_and_accounting: "<owner>"
```

Add Billing, Connect, migration, dispute, fraud, tax, accounting, or regional appendices as needed. Isolate prototypes completely from live credentials.

## User Journey Scenario

End-to-end flow: discovery and owners -> surface routing and official doc refresh -> durable order/payment model -> provider interaction -> customer return and authenticated asynchronous events -> idempotent fulfillment -> daily reconciliation -> staged rollout -> audited support recovery and rollback.

Exercise every path: success, abandon, customer action (3DS/SCA), timeout, duplicate delivery, out-of-order delivery, delayed event, fulfillment failure, partial/full refund, dispute, and operator repair.

## Failure Mode Table

| Failure mode | Trigger | Containment and recovery |
|---|---|---|
| Duplicate initiation | Double-click, client retry, or worker retry | Reuse stable logical idempotency key; never create a second payment on timeout. |
| Lost acknowledgment / timeout | Network drop after remote effect or before local commit | Ambiguous state: query/reconcile under original idempotency domain before acting. |
| Forged, replayed, or out-of-order event | Unverified endpoint or async delivery skew | Verify raw-body signature; dedupe by event ID; enforce monotonic state transitions. |
| Client-authoritative success | Trusting browser return URL | Ignore redirect for ledger updates; wait for authenticated server/event evidence. |
| Amount or currency mismatch | Stale cart, client tampering, or FX/tax drift | Compare provider amount/currency against immutable server order snapshot; quarantine on mismatch. |
| Provider/local divergence | Missed webhook, crash after remote commit | Scheduled reconciliation detects drift and triggers audited, idempotent repair. |
| Fulfillment failure | Downstream service error after payment succeeds | Persist paid state separately from fulfilled state; retry fulfillment idempotently; alert on aged unfulfilled orders. |
| Refund or dispute drift | Dashboard refund or chargeback not mirrored locally | Handle refund/dispute events; model explicit entitlement reversal or support escalation. |
| Mode contamination or secret leak | Test/live keys or IDs mixed; secret logged | Hard environment separation, secret scanning in CI, immediate key rotation and audit. |
| Uncontrolled API version upgrade | Account default upgraded without contract tests | Pin API version per request/account; test migrations before upgrading. |

## Retry and Backpressure Guidance

- Retry only a stable logical command within a bounded deadline when current Stripe semantics support it.
- Never generate a new idempotency key for every timeout; query and reconcile lost acknowledgments instead.
- Never blindly retry validation errors, authorization/authentication failures, or customer-action prompts.
- Avoid nested retries across HTTP client, queue worker, and caller (they multiply load and conflict risk).
- Make event and fulfillment consumers idempotent; shed nonessential work or pause producers before queues grow without bound.
- Test five failure points: before send, after send, after remote effect, before local commit, and during acknowledgment.

## Observability Checklist

Log redacted, bounded fields with explicit timestamps and units:
- Stable local order ID and provider correlation IDs, event ID, test/live mode, API version.
- Prior state, next state, transition source, signature-verification result.
- Logical command ID, attempt count, queue age, fulfillment status, reconciliation run ID, audited support actions, trace ID.

Never log API keys, webhook secrets, client secrets, raw payment data, full webhook payloads, or uncontrolled PII. Watch for sensitive data leaking inside error bodies or metadata.

## Outcome Metrics and Reliability Targets

Hard release invariants (binary):
- Zero duplicate irreversible charges or fulfillments.
- Authenticated event admission only.
- Idempotent, monotonic state transitions.
- Amount and currency consistency between local order and provider.
- Strict test/live isolation and zero secret exposure.

Track: local/provider divergence count, aged pending/unfulfilled orders, duplicate command/event no-ops, idempotency conflicts, rejected signatures, fulfillment retries/reversals, reconciliation exceptions, refunds/disputes, manual support adjustments, API version drift, and rollback triggers. Do not treat checkout conversion, API 200 rate, zero webhook errors, or raw monetary totals as correctness proof.

## Workload, Performance, and Scale Boundaries

- **Performance verification:** correctness and redaction gates precede load tests. Separate customer initiation, merchant processing, provider round-trip, webhook ingestion, transition/fulfillment, queue saturation, and reconciliation. Load-test duplicate event bursts, assert one transition and one fulfillment, measure queue age and reconciliation drain, and stage a canary.
- **Scale boundary:** stay in one contract while one owner can enumerate parties, funds flow, states, evidence, effects, reconciliation, tests, and rollback. Split by legal entity, funds flow, recurring vs. one-time, connected-account model, region/currency, ledger, or migration phase — while keeping one integration verifier and complete input/output contracts per slice.
- **Adjacent routing:** route recurring billing details to current Stripe Billing docs; multi-party flows to current Connect docs; stack/service implementation to the language backend skill; secrets/security to dedicated security review; PCI, tax, accounting, fraud, and legal questions to qualified owners.

## Future Refresh Search Queries

Open complete primary pages, read caveats and migration notes, and test in sandbox before updating contracts (never rely on search snippets or blogs):

- `site:docs.stripe.com payments payment-methods integration-options`
- `site:docs.stripe.com api checkout sessions payment_intents setup_intents`
- `site:docs.stripe.com webhooks signatures best-practices idempotency`
- `site:docs.stripe.com get-started checklist go-live`
- `site:docs.stripe.com billing subscriptions designing-integration`
- `site:docs.stripe.com connect integration-recommendations controller-properties capabilities`
- `site:docs.stripe.com changelog api upgrades`
- `site:docs.stripe.com get-started data-migrations pan-import`
