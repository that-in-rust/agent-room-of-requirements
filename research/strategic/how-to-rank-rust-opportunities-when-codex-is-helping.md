# How To Rank Rust Opportunities When Codex Is Helping

## Big Idea

If the first note asked, "What can we finish in 6 hours?" and the second note asked, "What are the honest backup ideas?", this note asks a bigger question:

> Across all the research, what is actually worth rewriting or building in Rust when Codex can help with the repetitive, spec-heavy, and glue-code parts?

That is the shift.

This is not a pure hackathon board anymore.

It is a fuller Rust opportunity board.

It mixes rewrite targets, new libraries, desktop apps, backend tools, agent tooling, and protocol ideas into one ranked list.

The ranking is based on `Codex-Assisted Rust Migration ROI`, not just "what is easiest to demo tonight."

You can read the first two notes here:

- [How To Win A Rust Hackathon In 6 Hours](./how-to-win-a-rust-hackathon-in-6-hours.md)
- [20 More Rust Hackathon Ideas After The First Shortlist](./20-more-rust-hackathon-ideas-after-the-first-shortlist.md)

## Why It Matters

Hackathon strategy and product strategy are cousins, not twins.

In a 6-hour hackathon, the best move is usually a tiny thing with a crystal-clear demo.

But once Codex is part of the team, a different question becomes more useful:

> Which Rust ideas become realistic because an agent can help write tests, scaffolds, adapters, migration glue, docs, repetitive UI, and boring correctness work?

That does not mean Codex makes every huge rewrite easy.

It does not.

It means some projects get a lot more tractable when the work is made of clear drawers:

- parse this
- port that
- wrap this API
- generate those tests
- build the shell around the core

Think of it like moving furniture with a smart dolly.

The dolly does not make a piano light.

But it does change which things are practical to move.

## Core Ideas Made Simple

### 1. The earlier notes were about speed

The first two notes were mostly about one question:

> What can we actually finish cleanly in a short hackathon window?

That is why tiny crates and tiny Tauri utilities dominated those rankings.

This note is wider.

Now the question is:

> What is worth doing at all if we are allowed to use Codex as leverage?

So the board gets more ambitious, but it still tries to stay honest.

### 2. Codex helps most when the work has clear edges

Codex is strongest when the work can be split into repeatable chunks:

- small APIs
- migration steps
- parser rules
- deterministic tests
- table-driven specs
- interface parity work

That is why some rows score well even when they are not tiny.

The work is still hard, but it is hard in a way that can be decomposed.

### 3. Rust only wins when it removes real pain

"Rewrite it in Rust" is not a strategy by itself.

Rust matters most when it removes something painful:

- memory-heavy desktop apps
- slow or fragile tooling
- unsafe parsing
- hard-to-deploy CLIs
- concurrency pain
- giant Electron shells for small jobs

If Rust is just a style preference, the score should stay lower.

### 4. Existing Rust alternatives can shrink the opportunity

Some notes looked exciting on first pass, but then current ecosystem checks changed the picture.

For example:

- validation is not empty anymore because crates like [garde](https://docs.rs/garde/latest/garde/), [validator](https://docs.rs/validator/latest/validator/), and [validify](https://docs.rs/validify/latest/validify/) already cover serious ground
- config DX is less greenfield because [config](https://docs.rs/config/latest/config/) already exists
- a native Mastodon app is less open than old notes suggested because [Ice Cubes](https://github.com/Dimillian/IceCubesApp) is already strong
- a multi-session Codex shell is less empty than it first looked because [CodexMonitor](https://github.com/Dimillian/CodexMonitor) now exists

So the point is not just "is this cool?"

The point is "is there still room here?"

### 5. We turned a messy research pile into one board

The research pool had a lot of overlap:

- copied notes
- archive mirrors
- repeated ideas in different folders
- "maybe" ideas mixed with strong candidates
- rewrite targets mixed with fresh Rust builds

So this pass tried to do one useful cleanup:

- keep only positive opportunities
- merge duplicates into one canonical row
- rank them together
- penalize rows that are already well served

That makes the board much easier to act on.

## Research Base For This Pass

This pass used the authored research pools that kept showing up in the earlier work:

- `Notes2026/ab04-rust-library-ideation`
- `Downloads/ab202603`
- `Desktop/TauriAppsOSS/docs/strategic-research`
- `Desktop/TauriAppsOSS/App-Experiments/agent-session-cockpit`
- `Desktop/apr2026`

The strongest supporting note families were:

- `rust-opportunities`
- `rewrite-targets`
- `batch-analysis`
- `pmf-research`
- the Parseltongue project notes
- Tauri app gap-analysis notes
- Rust/Tauri feasibility writeups

The cleanup rule was simple:

- include only notes that positively argue for a Rust rewrite, Rust build, Rust/Tauri port, or a bigger Rust expansion
- exclude caches, dumps, logs, vendored docs, and obvious duplicates
- keep one canonical row per opportunity

For the final ranking, I also spot-checked top-tier rows against the current ecosystem so old notes would not mislead the board.

## What Changed Since The Last Commit

The last commit added the second hackathon note:

- `335080d docs: add second rust hackathon research note`

That note widened the bench.

This note widens the whole game board.

The conversation after that commit moved from:

- "what should we build tonight?"

to:

- "what is worth building or rewriting in Rust at all, if Codex is part of the team?"

That sounds like a small wording change.

It is not.

It changes the scoring logic in three important ways:

1. We care less about pure 6-hour speed.
2. We care more about migration upside and long-term leverage.
3. We explicitly reward projects where Codex can shoulder a lot of the grind work.

So some rows went up because the architecture was well-specified and agent-friendly.

And some rows went down because the market gap had already narrowed since the original notes were written.

## How The Scoring Works

The board uses one number:

`Codex-Assisted Rust Migration ROI (1-100)`

In plain English, the score asks:

> If we used Codex well, how attractive is this Rust opportunity after accounting for real pain removed, Rust fit, execution realism, and evidence quality?

The rough weight split was:

- `35` points for migration upside and pain removed
- `20` points for Rust-native advantage
- `20` points for Codex leverage
- `15` points for tractability
- `10` points for evidence density in the notes

I also applied penalties when:

- a mature Rust equivalent already exists
- the notes themselves showed weak PMF
- OS or platform blockers dominate the build

In the table:

- `F` means the claim is directly supported by the notes
- `I` means the claim is my inference from combining notes and current ecosystem reality

## The Full Leaderboard

Premise check: this pass collapsed archive mirrors, copied variants, and stale duplicates into `50` canonical opportunities.

| Rank | Opportunity | Category | Primary Notes | Rust Thesis | Why Codex Helps | Main Risk | Confidence | Codex-Assisted Rust Migration ROI (1-100) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Parseltongue semantic intelligence platform | Devtool/compiler/parser | `IdeaResearch20250926`, Parseltongue domain thesis | `F+I:` dense notes frame Parseltongue as a deterministic semantic brain for zero-hallucination workflows. | Parser, query, MCP, and UI work split cleanly into agent-sized slices. | Platform scope and market education. | High | 97 |
| 2 | Agent session cockpit | Agent/infrastructure/tooling | `agent-session-cockpit-eli5`, `STRATEGIC-GUIDANCE` | `F+I:` one-window multi-CLI PTY host solves a daily pain with unusually concrete architecture notes. | PTY, xterm, sidebar, IPC, and session semantics are already decomposed. | Existing tools like [CodexMonitor](https://github.com/Dimillian/CodexMonitor) narrow greenfield upside. | High | 96 |
| 3 | PDF Surgeon | Desktop/Tauri app | `shreyas-doshi-viral-tauri-apps-eli5` | `F+I:` the notes repeatedly identify PDF rearranging as the clearest paid-pain-to-free-native wedge. | PDF ops plus drag-grid UI are easy to spec, test, and iterate with agents. | UX polish bar is high. | High | 95 |
| 4 | Campfire-on-Rust parity rewrite | Backend/service | `Closing the Campfire Gap` | `F:` there is already a detailed feature-gap matrix and sprint ladder. `I:` this is the cleanest parity-rewrite opportunity in the corpus. | The roadmap is almost executable already: feature diff, tickets, tests, and phases. | Public repo state is muddy and parity breadth is large. | Medium | 94 |
| 5 | `humanize-rs` | Library rewrite | `FINAL_Research_Backed_PMF_Rankings` | `F+I:` the notes argue Rust still lacks one obvious, unified humanize layer. | Small API, benchmarkable behavior, and good docs/test surface. | Existing point solutions like [humantime](https://docs.rs/humantime/latest/humantime/) and [number_prefix](https://docs.rs/number_prefix/latest/number_prefix/) reduce moat. | Medium | 93 |
| 6 | Upscaler | Desktop/Tauri app | `shreyas-doshi-viral-tauri-apps-eli5` | `F+I:` before-and-after image enhancement is one of the highest-shareability desktop bets in the notes. | Model plumbing, tiling, and shell UX are agent-friendly and measurable. | Model size, inference speed, and GPU variance. | High | 92 |
| 7 | `zod-rs` / schema-first validation | Library rewrite | `FINAL_Research_Backed_PMF_Rankings` | `F+I:` schema-first DX is still attractive, but the gap is narrower than the original notes assumed. | DSL design, derive support, and examples are Codex-friendly work. | The ecosystem now includes [garde](https://docs.rs/garde/latest/garde/), [validator](https://docs.rs/validator/latest/validator/), and [validify](https://docs.rs/validify/latest/validify/). | Medium | 91 |
| 8 | `typer-rs` | Library rewrite | `FINAL_Research_Backed_PMF_Rankings` | `F+I:` there is still room for a function-first CLI experience despite a mature parser ecosystem. | Proc-macro scaffolding and CLI fixtures fit agentic iteration well. | [clap](https://docs.rs/clap/latest/clap/) is entrenched and polished. | Medium | 90 |
| 9 | ScanSnap | Desktop/Tauri app | `shreyas-doshi-viral-tauri-apps-eli5` | `F+I:` searchable local OCR PDFs hit a real paid-tool gap with a strong demo moment. | OCR plus PDF composition is objective, testable, and phaseable. | Apple OCR bridge and scan-quality edge cases. | High | 89 |
| 10 | Dual-pane file manager | Desktop/Tauri app | `linux-ecosystem-gap-analysis-eli5` | `F+I:` the Linux-gap work says this is the highest-value underserved Mac utility. | File ops, search, previews, and shortcuts are deterministic product work. | Large surface area and high polish expectations. | High | 88 |
| 11 | `tixati-rs` Mac client | Desktop/Tauri app | `tixati-rs-mac-client-eli5` | `F+I:` real Mac gap plus a protocol-first roadmap make this a meaningful Rust-native long play. | [rqbit](https://github.com/ikatson/rqbit) proves the Rust engine path and the notes phase the build well. | Multi-year scope, legal naming risk, and hard protocol features. | Medium | 87 |
| 12 | HackerRank Tauri replica | Desktop/Tauri app | `HACKERRANK_TAURI_RUST_FEASIBILITY_ANALYSIS_20260403153314` | `F:` the reverse-engineering corpus is unusually deep. `I:` it is viable as a blueprint-heavy rewrite, not a clean product bet. | Static analysis, requirements mapping, and plugin boundaries are already explicit. | Kiosk, hotkey interception, and content-protection blockers on modern macOS. | High | 86 |
| 13 | Kafka-to-Iggy migration bridge | Protocol/data system | `RD06_KAFKA_MIGRATION_STRATEGY` | `F:` the notes identify a real migration gap for Iggy. `I:` bridge tooling is the monetizable wedge. | Protocol tables, offset mapping, and connector flows are already written down. | Enterprise migration trust and protocol mismatch complexity. | Medium | 85 |
| 14 | Parseltongue conversational MCP | Agent/infrastructure/tooling | `parseltongue-conversational-mcp-simulation` | `F+I:` the notes argue for wrapping deterministic code intelligence in agent-friendly conversational surfaces. | MCP contracts, prompt scaffolds, and query engine seams are obvious agent work. | Could collapse into the broader Parseltongue platform if it is not sharply scoped. | Medium | 84 |
| 15 | Pixelpress | Desktop/Tauri app | `shreyas-doshi-next-10-viral-apps-eli5` | `F+I:` batch compression is a sharp paid-pain replacement with clear native value. | Image pipeline crates and batch UX can be built incrementally. | AVIF throughput and batch queue polish. | High | 83 |
| 16 | Clipstash | Desktop/Tauri app | `shreyas-doshi-next-10-viral-apps-eli5` | `F+I:` searchable clipboard history is sticky, obvious, and native-friendly. | SQLite plus FTS plus clipboard hooks are straightforward with good testability. | macOS permission friction and background stability. | High | 82 |
| 17 | Parseltongue visualization surface | Devtool/compiler/parser | `PARSELTONGUE_COMPREHENSIVE_VISUALIZATION_ROADMAP` | `F+I:` visualization is a repeat theme and a strong adoption wedge for the core engine. | Graph rendering, query summaries, and diff views can be split into small tasks. | Risk of becoming pretty-but-nonessential. | Medium | 81 |
| 18 | `serde-validate` | Library rewrite | `FINAL_Research_Backed_PMF_Rankings` | `F+I:` layering validation on top of serde is still a reasonable Rust-native play. | Derives, error messages, and examples are repetitive and specable. | Existing [validator](https://docs.rs/validator/latest/validator/), [garde](https://docs.rs/garde/latest/garde/), and [validify](https://docs.rs/validify/latest/validify/) eat into the gap. | Medium | 80 |
| 19 | `thefuck-rs` | Devtool/compiler/parser | `03-thefuck-rs-spec__fb2fd0a7` | `F:` there is already a full technical spec and PMF note for a low-latency Rust rewrite. | Rule engines, shell adapters, and tests are ideal for agentic delivery. | Shell integration quality determines trust. | High | 79 |
| 20 | `elasticsearch-dump` rewrite | Backend/service | `BATCH_20_repos_1901-2000__fb7f6d50` | `F+I:` the batch survey calls out a real CLI backup gap with Rust-native deployability upside. | Streaming, retry, and CLI behavior are easier to verify than a full platform rewrite. | Operational correctness on large clusters. | Medium | 78 |
| 21 | Dupefire | Desktop/Tauri app | `shreyas-doshi-next-10-viral-apps-eli5` | `F+I:` duplicate cleanup is boring but recurring and valuable. | Hashing pipeline and safe-delete flow are easy to spec. | One false positive destroys trust. | High | 77 |
| 22 | Trimcut | Desktop/Tauri app | `shreyas-doshi-next-10-viral-apps-eli5` | `F+I:` lossless trimming has strong user pain and clear native advantage. | FFmpeg sidecar plus timeline UI can be parallelized cleanly. | Timeline scrubber feel is the product. | Medium | 76 |
| 23 | `OpenEnv-rs` | Library rewrite | `OUTPUT_B_High_PMF_Low_LOC_Libraries` | `F+I:` RL environment compatibility is a neat, well-bounded Rust gap. | Small API contract and test harnesses make it agent-friendly. | Niche market compared with devtool or desktop rows. | Medium | 75 |
| 24 | Obsidian vault graph surface | Desktop/Tauri app | `obsidian-rust-ui-eli5` | `F+I:` the notes strongly argue that the graph surface is the smallest smart native wedge, not the full editor. | Rendering and interaction tasks are measurable and separable. | Scope creep into full-note-app territory. | Medium | 74 |
| 25 | `wire-rs` | Library rewrite | `FINAL_Research_Backed_PMF_Rankings` | `F+I:` DI and codegen ergonomics remain underexplored in Rust. | Repetitive provider and container generation is exactly the kind of work Codex speeds up. | Rust users are divided on DI as a pattern. | Medium | 73 |
| 26 | `xsv` modernization | Devtool/compiler/parser | `OUTPUT_C_High_PMF_High_LOC_Libraries` | `F+I:` the corpus sees room for a maintained, modern CSV toolkit refresh. | CLI modernization and test coverage are very agent-friendly. | The existing CSV ecosystem is already strong. | Medium | 72 |
| 27 | `tui-next` | Devtool/compiler/parser | `OUTPUT_C_High_PMF_High_LOC_Libraries` | `F+I:` there is still appetite for a maintained TUI foundation. | Migration guides, examples, and compatibility work are grindable by agents. | [ratatui](https://github.com/ratatui/ratatui) already absorbed much of the need. | Medium | 71 |
| 28 | `pydantic-rs` | Library rewrite | `FINAL_Research_Backed_PMF_Rankings` | `F+I:` model validation and parsing remain attractive, but not greenfield. | Schema parsing and typed error surfaces are automatable. | Ecosystem overlap with [validator](https://docs.rs/validator/latest/validator/), [garde](https://docs.rs/garde/latest/garde/), and [validify](https://docs.rs/validify/latest/validify/). | Medium | 70 |
| 29 | `config-manager` | Library rewrite | `FINAL_Research_Backed_PMF_Rankings` | `F+I:` there is still room for nicer config DX, but not for a blank-sheet category win. | Merge rules and source layering are straightforward to encode and test. | [config](https://docs.rs/config/latest/config/) already covers the core job. | Medium | 69 |
| 30 | Renametron | Desktop/Tauri app | `shreyas-doshi-next-10-viral-apps-eli5` | `F+I:` file rename pain is real and the MVP is extremely tractable. | Preview, undo, regex, and EXIF rules are deterministic. | Useful but not especially viral. | High | 68 |
| 31 | Chromapick | Desktop/Tauri app | `shreyas-doshi-next-10-viral-apps-eli5` | `F+I:` color picking and palette generation fit a small native utility well. | Color math and export templates are tight, objective tasks. | Screen-recording permission hurts activation. | Medium | 67 |
| 32 | Markdeck | Desktop/Tauri app | `shreyas-doshi-next-10-viral-apps-eli5` | `F+I:` simple Markdown-first editing still has room if it avoids full knowledge-base scope. | Markdown render plus export plus split-view are well-understood stacks. | VS Code and Typora are already good enough for many users. | Medium | 66 |
| 33 | Ledgersnap | Desktop/Tauri app | `shreyas-doshi-next-10-viral-apps-eli5` | `F+I:` local-only personal finance remains emotionally resonant after Mint. | CSV parsing, categorization, and charts iterate well with agents. | Bank CSV normalization is miserable. | Medium | 65 |
| 34 | Qwikcode | Desktop/Tauri app | `shreyas-doshi-next-10-viral-apps-eli5` | `F+I:` QR code tooling is tiny, clear, and shippable. | Encode and decode paths are benchmarkable and compact. | Commodity utility with limited retention. | High | 64 |
| 35 | `automotive-can` | Library rewrite | `FINAL_Research_Backed_PMF_Rankings` | `F+I:` low-saturation industrial Rust is compelling if the goal is a defensible B2B niche. | The API and protocol surface are bounded and test-heavy. | Domain access and hardware realism. | Medium | 63 |
| 36 | `aerospace-units` | Library rewrite | `FINAL_Research_Backed_PMF_Rankings` | `F+I:` this is another underserved industrial niche with better moat than generic developer tooling. | Units, conversions, and safety constraints are crisp to encode. | Narrow market and long sales cycles. | Medium | 62 |
| 37 | Native Matrix client | Desktop/Tauri app | `linux-ecosystem-gap-analysis-eli5` | `F+I:` the notes see room for a lighter native client than current Electron-heavy options. | Local cache, sync, and chat UI can be layered incrementally. | Existing clients already satisfy many users. | Medium | 61 |
| 38 | Photo manager plus tethering | Desktop/Tauri app | `linux-ecosystem-gap-analysis-eli5` | `F+I:` this is a real paid-tool gap, but it is hardware-heavy and broad. | Import, catalog, and edit flows can be phased. | Device matrix and photographer-grade expectations. | Medium | 60 |
| 39 | `async-simplified` | Library rewrite | `FINAL_Research_Backed_PMF_Rankings` | `F+I:` async pain is real, but abstracting it safely is hard. | Experiments and API comparisons are cheap for agents to run. | It is easy to oversimplify and leak complexity back to users. | Medium | 59 |
| 40 | `rich-rs` | Library rewrite | `FINAL_Research_Backed_PMF_Rankings` | `F+I:` pretty terminal output still matters, but the market is no longer empty. | Rendering primitives and snapshot tests are agent-friendly. | Strong incumbents around ratatui and terminal-formatting crates. | Medium | 58 |
| 41 | WASM binary parser | Library rewrite | `OUTPUT_B_High_PMF_Low_LOC_Libraries` | `F+I:` a small ergonomic parser is feasible and tightly scoped. | Binary format work pairs well with TDD and fuzzing. | Existing parsers reduce urgency. | Medium | 57 |
| 42 | `rope-rs` | Library rewrite | `OUTPUT_B_High_PMF_Low_LOC_Libraries` | `F+I:` ML infra notes rate RoPE support well, but it is narrower than the product rows. | Math kernels are compact and benchmarkable. | The audience is niche and fast-moving. | Low | 56 |
| 43 | NumericOps derive macro | Library rewrite | `OUTPUT_B_High_PMF_Low_LOC_Libraries` | `F+I:` clever and tractable, but more convenience than must-have platform. | Proc-macro scaffolding is exactly the kind of code agents excel at. | Narrow surface area limits upside. | Low | 55 |
| 44 | Native Mastodon client | Desktop/Tauri app | `linux-ecosystem-gap-analysis-eli5` | `F+I:` the local gap thesis is stale now; the remaining opportunity is differentiated UX, not category creation. | A thin native shell is still buildable quickly. | [Ice Cubes](https://github.com/Dimillian/IceCubesApp) is already strong, free, and native. | High | 54 |
| 45 | System-wide audio EQ | Desktop/Tauri app | `linux-ecosystem-gap-analysis-eli5` | `F+I:` the pain is real, but the notes themselves flag deep platform hostility. | Agents help on UI and config, not on the hardest OS hooks. | Kernel or low-level audio-hook complexity. | High | 53 |
| 46 | Music library manager | Desktop/Tauri app | `linux-ecosystem-gap-analysis-eli5` | `F+I:` local-media collectors are underserved, but the audience is smaller and fragmented. | Cataloging and metadata flows are deterministic. | Apple Music, Plex, and Swinsian blunt upside. | Medium | 52 |
| 47 | Fontcase | Desktop/Tauri app | `shreyas-doshi-next-10-viral-apps-eli5` | `F+I:` there is real paid competition, but it is still a niche pro-user tool. | Preview, compare, and toggle flows are manageable. | Designer-only audience limits ROI. | Medium | 51 |
| 48 | Clean email client | Desktop/Tauri app | `linux-ecosystem-gap-analysis-eli5` | `F+I:` the notes see a gap, but it is crowded and hard to make sticky. | IMAP and SMTP shells are buildable; product differentiation is the hard part. | Low-retention category with many acceptable incumbents. | Medium | 50 |
| 49 | RustHallows vertical RTOS stack | Protocol/data system | `RustHallows POC Architecture Design` | `F+I:` ambitious RTOS and microkernel notes exist, but this is a venture-scale bet, not a crisp Codex multiplier play. | Specs and blueprinting are rich, so Codex can help early. | Certification, kernel work, and years-long execution. | Low | 49 |
| 50 | `slugify-rs` | Library rewrite | `OUTPUT_B_High_PMF_Low_LOC_Libraries` | `F+I:` useful, but the opportunity is mostly closed now. | Tiny API and tests make it easy to ship. | [slugify](https://docs.rs/slugify/latest/slugify/) already covers the core use case. | High | 48 |

## Top Themes

Three themes kept repeating.

First, the strongest rows combine a real pain, a real Rust advantage, and notes that are already specific enough to act like a blueprint.

That is why Parseltongue, the session cockpit, PDF Surgeon, Campfire parity, and the best library gaps rose to the top.

Second, Codex leverage is highest when the notes already contain feature matrices, architecture slices, protocol tables, acceptance criteria, or staged roadmaps.

That kind of work is much easier for an agent to help with than a vague "build something cool" idea.

Third, the best desktop opportunities are narrow native shells around boring but useful cores:

- PDF work
- clipboard history
- OCR
- image processing
- file management
- data migration

Those are not flashy ideas in theory.

They are strong ideas in practice.

## Watchouts

The top risk is confusing "possible with Codex" for "easy because of Codex."

Some things are still ugly even with great agent help:

- kiosk-mode desktop security
- system-wide audio hooks
- hardware-heavy tethering workflows
- giant parity rewrites
- categories that already have strong native incumbents

That is why current-reality checks mattered.

They lowered several rows:

- validation and schema crates because of [garde](https://docs.rs/garde/latest/garde/), [validator](https://docs.rs/validator/latest/validator/), and [validify](https://docs.rs/validify/latest/validify/)
- config DX because of [config](https://docs.rs/config/latest/config/)
- native Mastodon because of [Ice Cubes](https://github.com/Dimillian/IceCubesApp)
- the agent cockpit wedge because of [CodexMonitor](https://github.com/Dimillian/CodexMonitor)
- tiny slug generation because of [slugify](https://docs.rs/slugify/latest/slugify/)

So the board should be read as:

- top rows = strong build targets
- middle rows = real but more conditional
- bottom rows = interesting, but only if there is a special reason to chase them

## Tiny Example

Imagine three different questions.

Question one:

> What can we ship tonight?

That gives us something like `humanize-rs` or `ExifDrop`.

Question two:

> What are our honest backup ideas if the first pick breaks?

That gives us the second-board notes.

Question three:

> What is worth doing in Rust at all if Codex can help with the boring work?

That gives us this bigger leaderboard.

Same research family.

Different question.

Different board.

## What To Remember

The smartest Rust opportunity is not the biggest rewrite or the tiniest demo. It is the project where real pain, real Rust advantage, and real Codex leverage all line up at the same time.
