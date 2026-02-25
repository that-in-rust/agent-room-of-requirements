# OrbStack Notes (Opportunity Scan)

Date: 2026-02-25
Source: https://orbstack.dev/ and docs pages under https://docs.orbstack.dev/

## What OrbStack is positioning as

- "Fast, light, simple" Docker + Linux experience on macOS.
- Drop-in replacement positioning versus Docker Desktop and Colima.
- Single app that covers:
  - Docker containers
  - Linux machines
  - Local Kubernetes

## Feature surface highlighted by OrbStack

From the homepage and compare docs, OrbStack emphasizes:

- Fast startup and networking
- Low CPU / low power usage and dynamic memory behavior
- Native macOS app UX (menu bar + GUI)
- CLI integration (`docker`, `compose`, `orb`, `orbctl`)
- Kubernetes conveniences (NodePort + ClusterIP + LoadBalancer access, GUI)
- Networking ergonomics (domains, IPv6, proxy support)
- Linux machine workflows (SSH integration, distro management)

## Pricing and licensing snapshot

From pricing/licensing pages:

- Free tier: personal, non-commercial use
- Pro tier: business/commercial usage, listed at `$8` per user per month (yearly billing shown as `$96`)
- Enterprise: SAML SSO and enterprise purchasing/support motions
- Licensing doc states commercial/professional users must purchase licenses per user

## Constraints and gaps visible from docs

- macOS-first product footprint (compare docs include Windows support as a differentiator in favor of Docker Desktop)
- Some advanced ecosystem pieces still marked as absent/limited in compare pages (example: Docker Desktop extensions/scout parity)
- FAQ calls out areas still not supported (e.g., Linux graphical apps/GPU, USB passthrough)

## OSS alternative opportunities

1. Cross-platform first (macOS + Linux + Windows parity), not macOS-only.
2. Fully open governance + transparent roadmap for enterprise trust.
3. Extensibility story (plugin APIs, marketplace, hooks) from day one.
4. Reproducible benchmark suite published in-repo (startup, IO, network, battery).
5. Developer-experience parity layer:
   - seamless Docker context switching,
   - Linux VM workflow,
   - local k8s quick-start,
   - migration helpers from Docker Desktop/Colima.
6. Enterprise controls without lock-in:
   - policy packs,
   - auditable config state,
   - identity/SSO integration via open standards.

## Practical build direction (MVP)

- Start with Docker-compatible runtime + context switching UX.
- Add Linux machine primitives with solid file/network integration.
- Add opinionated local Kubernetes profile once core container/VM paths are stable.
- Ship migration tooling and compatibility docs early to reduce switching cost.

