---
name: stripe-payments
description: >-
  Stripe payment architecture, API surface selection, server-owned state machines,
  idempotent webhook and fulfillment handling, reconciliation, refunds, disputes,
  Billing, and Connect. Use when designing, implementing, reviewing, migrating, or
  hardening a Stripe integration, checkout flow, subscription, Connect platform,
  webhook handler, or payment reconciliation job. Not for legal, tax, PCI,
  accounting, or fraud certification, or for non-Stripe payment providers.
---

# Stripe Payments

## Purpose

Design and verify Stripe integrations as a durable, server-owned payment state machine and ledger boundary. Choose the narrowest Stripe surface that fits the business model, keep amount/currency authority on the server, drive state transitions from authenticated, duplicate-safe asynchronous events, and reconcile against Stripe under a controlled API version.

For Stripe's verbatim MIT best-practices checklist and official documentation URLs, see `../../curated-upstream-skill-snapshots/stripe/stripe-best-practices/SKILL.md`. Always verify API/SDK versions, regional payment methods, account capabilities, and compliance rules against current official Stripe documentation and the live account configuration before launch.

## When to use and when not to use

Use when:
- Choosing a Stripe surface (Checkout, Payment Element, PaymentIntents, SetupIntents, Billing, Payment Links, Invoicing, Connect).
- Designing order/payment state machines, idempotency, webhook verification, fulfillment gating, refunds, disputes, or reconciliation.
- Reviewing or migrating an existing integration (for example away from legacy Charges, Sources, Tokens, Card Element, or legacy Connect account types).

Do not use when:
- Seeking legal, tax, PCI-DSS, accounting, fraud, or regulatory sign-off — route those to qualified owners.
- Acting on a live Stripe account, moving money, or changing dashboard settings without explicit owner authorization.

## Core thesis

Payment and fulfillment decisions stay in a durable, server-owned state machine. Browser redirects, synchronous API responses, and webhook arrival order are observations, never the financial ledger. Never let a return URL, client callback, unverified webhook, retry, or unrefreshed recommendation trigger irreversible fulfillment.

## Surface selection (verify against current Stripe docs)

Classify the business model before picking an API: merchant vs. platform model, payer/beneficiary, funds flow, recurrence, liability for negative balances, currencies, tax/discount authority, fulfillment timing, trust boundaries, and recovery obligations.

| Need | Default surface | Notes and boundaries |
|---|---|---|
| On-session web payment (one-time or subscription) | **Checkout** (Stripe-hosted or embedded) + **CheckoutSessions** | Narrowest compliance and collection surface; models taxes and discounts. |
| Custom web payment UI | **Payment Element** (prefer CheckoutSessions; PaymentIntents when custom checkout state is needed) | More customization transfers more lifecycle and failure work to the merchant. Never use legacy Card Element or Payment Element in card mode. |
| Off-session payment or server-orchestrated charge | **PaymentIntents** | Never use the deprecated Charges API; migrate existing Charges integrations. |
| Save payment method for future use | **SetupIntents** | Never use deprecated Sources or outdated Tokens APIs. |
| Inspect card details before creating an Intent (e.g. surcharging) | **Confirmation Tokens** | Do not call `createPaymentMethod` or `createToken` in Stripe.js. |
| Payment methods list | **Dynamic payment methods** in Dashboard | Prefer dashboard-managed dynamic methods over hardcoding `payment_method_types`. |
| Recurring revenue / SaaS | **Stripe Billing / Subscriptions** + Checkout | Do not hand-roll recurring billing directly on PaymentIntents. |
| Simpler journeys without custom checkout | **Payment Links** or **Invoicing** | Lowest engineering and maintenance footprint. |
| Multi-party platform funds flow | **Stripe Connect** with **controller properties** and **capabilities** | Choose **direct charges** (Stripe takes negative-balance risk) or **destination charges** (platform accepts negative-balance liability); use `on_behalf_of` for merchant of record. Never mix charge types. Avoid legacy Standard/Express/Custom terminology. |
| Server-side raw PAN or processor migration | Formal **PCI compliance** proof + Stripe **PAN import** process | Never handle raw card data casually; escalate to security/compliance owner. |

Default to the latest pinned API and SDK versions unless the repository pins an explicit version contract.

## Workflow

1. **Discover and assign owners.** Record merchant/platform model, parties and liability, funds flow, currencies, tax/discount authority, fulfillment system, API/SDK versions, test/live accounts, and compliance/accounting/support owners.
2. **Refresh official evidence.** Check current versioned Stripe documentation, changelogs, and account settings for every product/API claim you rely on.
3. **Write the Payment Integration Decision and State Contract** (see Output contract below) before writing production payment code.
4. **Model immutable orders and monotonic state.** Freeze order amount/currency snapshots on the server, correlate local order IDs with provider object IDs, and enforce allowed forward transitions.
5. **Make commands and events duplicate-safe.** Scope idempotency keys to stable logical commands (never generate a fresh key on a timeout retry). Verify webhook signatures, persist event IDs for deduplication, and handle out-of-order and delayed delivery.
6. **Gate fulfillment and reconcile.** Grant each entitlement at most once from verified state. Run scheduled reconciliation (daily where appropriate) to catch local/provider drift, and model refunds, partial refunds, disputes, and audited support repairs explicitly.
7. **Run adverse-path verification gates** before any live traffic.

## Output contract: Payment Integration Decision and State Contract

Before production money movement, produce a single contract covering:
- **User goal, decision boundary, and verification gate rule** (when to use/avoid, and what proves it works).
- **Business model, parties, liability, and funds flow** (merchant vs. platform, beneficiary, charge type).
- **Amount and currency authority** (immutable server snapshot; tax/discount source).
- **Chosen surface and version evidence** (API version, SDK version, account/region, retrieval date).
- **Identifiers and state machine** (local order ID, provider IDs, states, allowed monotonic transitions).
- **Commands, idempotency, and asynchronous events** (idempotency scope/retention, signature verification, dedupe, out-of-order handling).
- **Fulfillment and reversal policy** (one-time grant, failure handling, refund/dispute entitlement reversal).
- **Reconciliation** (cadence, divergence queries, owner, alert thresholds).
- **Secrets, data boundaries, and test/live isolation** (no secrets/PAN/raw payloads in logs; strict mode separation).
- **Adverse-path tests, rollout, rollback, and owners** (canary, live rollback owner, audited support recovery).

## Verification gates

A green sandbox UI demo is not launch proof. Verify each gate with explicit environment/mode, API/SDK version, expected red condition, and retained evidence:

1. **Pure state transitions:** unit-test allowed forward transitions and reject backward or illegal transitions.
2. **API contract parsing:** validate pinned API/SDK payload parsing against recorded fixtures.
3. **Authenticated events:** reject missing, invalid, or expired webhook signatures; verify raw-body signature checking.
4. **Duplicate and out-of-order replay:** replay the same event multiple times and out of order; assert a single state transition and no-op duplicates with audit evidence.
5. **Timeout and partial failure:** test failure before send, after send, after remote effect, before local commit, and during acknowledgment; resolve via the original idempotency key and provider query — never create a second payment or refund.
6. **Idempotent fulfillment:** assert one entitlement per paid order across retries and concurrent event deliveries.
7. **Secret scanning and log redaction:** verify no API keys, webhook secrets, client secrets, raw payment details, or full payloads appear in code or logs.
8. **Test/live separation:** verify test and live keys, webhook secrets, and provider IDs cannot mix.
9. **Reconciliation:** verify the reconciliation query detects provider-paid / local-unfulfilled and local-paid / provider-refunded drift.
10. **Migration and rollback:** verify safe migration from legacy APIs/versions and a rehearsed rollback path, plus a freshly reviewed official Stripe Go-Live Checklist.

## Anti-patterns

- **Client-owned paid state or redirect-driven fulfillment:** marking an order paid from a return URL or browser callback.
- **Fresh idempotency key on timeout:** submitting a second charge or refund after a lost response instead of querying/reconciling under the original logical command.
- **Signature-only webhook trust:** assuming a verified signature guarantees once-only or in-order delivery.
- **Mutable amount/currency:** letting client parameters alter order totals after creation.
- **Refund-equals-reversal assumption:** assuming a Stripe refund automatically revokes downstream entitlements.
- **Uncontrolled API upgrades or mixed test/live IDs:** upgrading account API versions without contract tests, or storing provider IDs without mode isolation.
- **Legacy APIs for new builds:** recommending Charges, Sources, Tokens, Card Element, or legacy Connect Standard/Express/Custom labels.
- **Using conversion or zero webhook errors as correctness proof:** ignoring local/provider divergence and aged pending orders.

## Self-check

Before claiming a Stripe integration is ready:
1. Are all payment and fulfillment decisions driven by a durable server state machine rather than browser redirects?
2. Is the Payment Integration Decision and State Contract complete, with named owners for reconciliation, support, compliance, and rollback?
3. Have duplicate, out-of-order, forged, delayed, timeout, fulfillment-failure, refund, and dispute paths all been tested?
4. Have API/SDK versions, account settings, and the Go-Live Checklist been refreshed against current official Stripe documentation?

See `reference.md` for full evidence-boundary rules, tradeoffs, failure modes, retry/backpressure policy, observability, workload/scale boundaries, and refresh queries.
