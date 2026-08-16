# 20 More Rust Hackathon Ideas After The First Shortlist

## Big Idea

The first note found the starters. This note finds the bench: 20 more Rust hackathon ideas that are still real, still useful, and still worth building if the top picks get blocked.

If the first shortlist was "what should we most likely do tonight?", this list is "what else is worth doing if our constraints change?"

You can read the first note here: [How To Win A Rust Hackathon In 6 Hours](./how-to-win-a-rust-hackathon-in-6-hours.md)

## Why It Matters

In a fast hackathon, picking the best idea is good.

Having a second board is better.

That is because real hackathons get messy:

- the top idea may secretly be harder than it looked
- one teammate may be stronger at desktop UI than macros
- a hardware-dependent demo may fail at the worst time
- a "great" idea may turn out to be hard to explain

So the goal of this follow-up research was not to prove the first note wrong.

It was to answer a simpler question:

> If the first five ideas do not fit tonight, what are the next 20 honest options?

Think of it like packing extra tools in a backpack.

You still want the lightest bag possible.

But you also want one or two backup tools in case the first plan jams.

## Core Ideas Made Simple

### 1. Not every good idea is a good tonight idea

Some ideas are good products.

Some ideas are good open-source repos.

Some ideas are good learning projects.

And some ideas are good **6-hour hackathon** projects.

Those are not the same thing.

This second list is full of ideas that are real and promising, but they miss the top band for one of four common reasons:

- the demo is less obvious
- the audience is narrower
- the polish work is bigger than it first appears
- the API surface grows faster than expected

### 2. We found two kinds of backup ideas

The second pass kept producing two main families:

- **crate ideas** that are publishable and technically clean
- **desktop utility ideas** that are demoable but less breakout-ready than the first list

The crate ideas are like building a sharp knife.

The utility ideas are like building a neat little tool on a workbench.

Both can win in the right setup.

The difference is mostly about **clarity, scope, and showmanship**.

### 3. The first shortlist still holds

This follow-up did **not** overturn the first conclusion.

The earlier top picks are still the safest bets because they combine:

- tiny scope
- clear story
- visible Rust advantage
- easy proof

What changed after the last commit is not the main rule.

What changed is that we now have a stronger backup board.

That means we can pivot faster without starting the research from scratch again.

## Research Base For This Second Pass

This note extends the earlier shortlist using the same local research pool.

The strongest source notes for this pass were:

- `FINAL_Research_Backed_PMF_Rankings.md`
- `OUTPUT_B_High_PMF_Low_LOC_Libraries.md`
- `new-tauri-apps-list-20260411.md`
- `compass_artifact_wf-14dbb238-10ac-4560-8506-ba2ca6c04fe3_text_markdown.md`

In plain English:

- one set helped with **crate ideas**
- one set helped with **low-LOC micro-libraries**
- one set helped with **Tauri product framing**
- one set helped with **small Electron rewrite targets**

## The 20 More Ideas

These are ranked as the next wave after the first shortlist, not as replacements for it.

| Rank | Idea | Type | Simple version | Why it is still interesting | Why it stayed out of the first note | Honest 6-hour cut |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `automotive-can` | New Rust library | A clean CAN bus library for automotive and EV work. | The niche is real, the need is strong, and the API can be small and serious. | The domain is narrower than general developer tools, so the audience is smaller. | Send and parse a few frame types, add examples, and ship tests plus a tiny benchmark. |
| 2 | `serde-validate` | New Rust library | Validate data while it is being deserialized instead of after. | It leans on a huge Rust habit pattern and has a very clear correctness story. | Less instantly demoable than `humanize-rs`, even if the engineering case is strong. | Support a few derive-based validations, add test matrix, and benchmark deserialization overhead. |
| 3 | `DevDock` | Rust/Tauri utility | One small app to see ports, processes, and Docker containers together. | Developer pain is real and the "what is using this port?" story is easy to show. | OS details and Docker plumbing create more edge cases than the top utilities. | Show port-to-process mapping, list running containers, and add one kill/open action. |
| 4 | `LogLens` | Rust/Tauri utility | Open a local log file and quickly filter the noisy parts away. | Extremely practical and easy to explain to engineers. | Strong utility, weaker "wow" factor than the top tray and privacy tools. | Open one file, filter by severity, search text, and demo error-only mode. |
| 5 | `CsvChameleon` | Rust/Tauri utility | A small CSV cleaner and editor for messy real-world tables. | Broad usefulness across engineering, ops, and PM work. | Table editing always needs a bit more polish than it first seems. | Import CSV, edit cells, validate rows, and export clean CSV. |
| 6 | `EncryptDrop` | Rust/Tauri utility | Drag-drop file encryption with one passphrase and one clean flow. | Clear privacy story and a very simple "before/after" demo. | Crypto UX needs careful wording and safe defaults, which adds pressure. | Encrypt one file, decrypt one file, show output, and document limitations clearly. |
| 7 | `StudyForge` | Rust/Tauri utility | Turn Markdown notes into flashcards and short study loops. | The value is real and the input format is simple. | The audience is narrower and the UX polish matters more than expected. | Parse one Markdown deck, quiz five cards, and save progress locally. |
| 8 | `wire-rs` | New Rust library | A Rust take on compile-time dependency wiring. | The idea has strong engineering appeal and a crisp architectural story. | It is more abstract than the top crates, so judges may need more explanation. | Wire a small service graph, generate providers, and ship one example app. |
| 9 | `async-simplified` | New Rust library | A small crate that makes common async patterns feel less annoying. | The pain is common and the promise is easy to understand. | The scope can become fuzzy fast unless the crate stays tiny and opinionated. | Ship a few helpers for timeout, retry, and task coordination with clear examples. |
| 10 | `Geminio` | New Rust library | A derive macro that gives numeric operator traits to newtype structs. | Very finishable, very crate-shaped, and easy to test. | Clever and tight, but the demand signal is weaker than the most obvious crates. | Support `Add`, `Sub`, `Mul`, and `Div` for tuple newtypes and publish good docs. |
| 11 | `go-kit-rs` | New Rust library | Service-kit patterns inspired by Go's service design tooling. | Useful for backend engineers who like explicit architecture. | Bigger surface area and lower immediate demo energy than the top picks. | Implement one transport plus middleware example, not a whole service framework. |
| 12 | `accessibility-utils` | New Rust library | A helper crate for accessibility-friendly UI and interaction patterns. | Important problem, under-served area, and good long-term value. | Harder to make visually exciting in a quick hackathon pitch. | Ship a few helpers, examples, and a short guide showing what they prevent. |
| 13 | `rich-rs` | New Rust library | Nicer terminal output with a friendlier API for styled text and tables. | Developer tooling is always useful and easy to try. | The category overlaps with existing terminal UI work, so differentiation must be sharp. | Styled text, one table component, one progress example, and benchmark render speed lightly. |
| 14 | `chrono-humanize++` | New Rust library | Better human-friendly time formatting without dragging in a giant API. | Small, understandable, and easier than a broad formatting crate. | It is partly shadowed by the stronger `humanize-rs` umbrella story. | Relative time, English-only output, and test matrix for common phrases. |
| 15 | `JournalFlow` | Rust/Tauri utility | A calm local journal app with daily entries and lightweight structure. | Simple local-first story and emotionally sticky use case. | Journaling tools are crowded and need taste, not just code. | Calendar view, one Markdown entry flow, and local save plus search. |
| 16 | `MockForge` | Rust/Tauri utility | A tiny GUI to stand up fake API endpoints fast. | Very practical for frontend and integration work. | Mock tooling can turn into a big platform if the first slice is not controlled. | One endpoint, one response body, request log, and start/stop server flow. |
| 17 | `DataPeek Mongo` | Rust/Tauri utility | A lighter Mongo browser for basic read-first inspection. | Clear value and obvious Rust-vs-heavy-GUI story. | Database GUIs expand fast once editing, auth, and indexing details arrive. | Connect, browse one database, inspect one collection, and keep it read-only. |
| 18 | `GlyphDeck` | Rust/Tauri utility | A tiny Unicode and emoji finder with instant copy. | Delightful micro-utility with a very clean single-screen demo. | Narrower audience than the strongest developer pain tools. | Search symbols, copy one, pin favorites, and keep the UI keyboard-first. |
| 19 | `Wallpaper Pulse` | Rust/Tauri utility | Change wallpaper from one remote source or one scheduled feed. | Very visual and easy to show on stage. | Lower day-to-day usefulness than the strongest dev or privacy tools. | Fetch one image source, set wallpaper, and schedule one refresh action. |
| 20 | `yup-rs` | New Rust library | A Rust version of a builder-style validation library. | Familiar problem, strong external demand pattern, and decent crate shape. | It is harder to separate cleanly from `zod-rs`, so the story is weaker. | Implement string, number, and object validation with readable errors and examples. |

## Tiny Example

Imagine the first note gave us five "start here tonight" ideas.

This note is what we reach for if one of those breaks.

For example:

- if `humanize-rs` feels too familiar, maybe `serde-validate` gives a more technical crate story
- if `RepoPing` feels too API-dependent, maybe `LogLens` is a safer local desktop tool
- if `ExifDrop` feels too tiny, maybe `DevDock` gives a slightly bigger but still practical dev utility

That is the real use of a second board.

It is not there to make us indecisive.

It is there to stop us from panicking.

## What Changed Since The Last Commit

The first hackathon note answered:

> What should we most likely build?

This note answers:

> What should we build if the first choice stops fitting the room, the team, or the clock?

So the strategy after the last commit got wider, not blurrier.

We did not abandon the original rule.

We strengthened it by separating:

- **starters** = highest-confidence 6-hour bets
- **bench ideas** = good backups with honest tradeoffs

That is useful because hackathons are not just about picking a smart idea.

They are about recovering quickly when reality changes.

## What To Remember

The best hackathon strategy is not having one perfect idea. It is having one sharp first choice and twenty honest backups that do not fool you about the clock.
