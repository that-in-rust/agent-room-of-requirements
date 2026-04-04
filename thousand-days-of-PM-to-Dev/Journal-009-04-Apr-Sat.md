# 04 Apr 2026 Saturday

## Raw Notes

### Opportunity 01: Apache Iggy contribute x build something with it x build videos for dev rel
Apache Iggy contribute x build something with it x build videos for dev rel
the attached picture is of a devrel conversation with apache iggy ceo the company laser data - what i interpret is that they don't have other candidates also and they would basically wait for somebody to come and show this and then they will hire them. probably this is a good opportunity for me to constantly build stuff with apache iggy and showcase it. it might be a great idea to actually ideate more on apache iggy apart from contributing to it.

### Opportunity 02: Hackerrank 2 week assignment proctored app in Tauri
Hackerrank 2 week assignment proctored app in Tauri

the second opportunity appeared to me. last year i had a full round of interviews with hackerrank and they liked me. the hr rejected me because i had already told them that i wanted to be in a dev role and they were hiring me for a pm role.

i just went to a conference a couple of days back and the head of product identified me. he was like "hey this is why we could not offer because you already told you would move to dev and you did." he then introduced me to their head of engineering, the first employee, and they can hire me without a dsa. i asked them "can i just do an assignment for you?" it was very surprising that they remembered me and offered me this opportunity.

here i have thought that i'll create a hackerrank proctor which is right now in electron in tori and if i can do that they will be impressed. obviously there are some areas where tori does not have the relevant plugins so what i will do is i will look at tori as also one place i can build something around. maybe i'll check out their repo as well. the second opportunity is tori app which is again rust and will hopefully compound.


### Opportunity 03: Rust contribution opportunity in upcoming Agent Orchestrator library
Rust contribution opportunity in upcoming Agent Orchestrator library - it is exploding and the creator is a twitter friend who is excited to have me guide this on the product side, it might be a good way to rack up a lot of small PR merges

# How to read code

## Research 01

``` text
# Mastering Large Codebases: A Field Guide for Engineers

## Executive Summary

Navigating a large, unfamiliar codebase is one of the most practically demanding skills in software engineering — yet it is seldom formally taught. The challenge is not fundamentally about reading comprehension; it is about *mental model construction*: building an accurate internal map of what a system does, why it was built that way, how its parts interrelate, and where the critical paths live. This guide synthesizes evidence-based strategies from experienced practitioners, academic research on program comprehension, and modern tooling to provide a comprehensive framework for any engineer — from a fresh joiner to a senior architect tackling an inherited legacy system.[1]

***

## Phase 0 — Orient Before You Read: The "Top-Down before Bottom-Up" Principle

The single most common mistake engineers make is diving straight into source files. Large codebases are built by many developers over thousands of hours; no individual can absorb them in a single top-to-bottom read. The correct starting posture is *orientation* — understanding the system's shape and purpose before understanding its internals.[2]

### Start With the Product, Not the Code

Use the finished product yourself before touching a single file. Understanding the user-visible behavior creates a semantic anchor against which every piece of code can be interpreted. When you later encounter a function like `recalculate_cart_totals`, you already know *what a cart is* and *why totals matter*. This bridges the gap between the domain language embedded in the code and your own mental model.[3]

### Read Architecture Documents and ADRs First

Look for architecture decision records (ADRs), system design documents, wiki pages, and README files before anything else. Even if they are incomplete or partially out of date, they reveal the *intended* structure and the vocabulary the original authors used. Gaps in the documentation are themselves informative: they signal where the system grew organically beyond its original design. A research study on developer onboarding found that reviewing architecture overviews early significantly accelerates the path to first-contribution confidence.[4][5]

### Build Your Own Visual Map

Even with good documentation available, create your own map of the codebase using a drawing tool such as draw.io, Excalidraw, or even pen and paper. Sketch the system at multiple scales: a high-level diagram showing major services and their interactions, and lower-level diagrams for specific subsystems as you explore them. This active-construction process forces comprehension rather than passive reading. Crucially, show this map to experienced colleagues; they will correct misconceptions and point out paths you missed.[6][7]

***

## Phase 1 — Establish Entry Points: Follow Data Through the Maze

Most code is fundamentally a pipeline that transforms inputs into outputs. Identifying entry points — the places where data enters the system — is the most efficient way to bootstrap understanding of any unfamiliar codebase.[8]

### Identify the Key Entry Points

Locate the main entry points of the application first: the `main()` function or equivalent, HTTP route handlers, message queue consumers, CLI argument parsers, and event listeners. These are the "front doors" of the system. From any entry point you can follow the data flow forward through service layers, business logic, and storage, gaining a structural understanding of each component's role. For a Rust codebase, for example, the `compiler/rustc_driver` crate is the outermost entry point, and the entire compilation pipeline fans out from `rustc_interface`.[9][10][11]

### Prioritize the Data Model

Read and understand the data model before anything else in the business logic. The classes or structs that represent REST entities, the database schemas, the protocol buffer definitions — these reveal the *nouns* of the system. Code logic is just verbs acting on those nouns. Understanding the data model lets you interpret otherwise opaque transformation functions. Ask: what is stored in the database, and how are those entities related?[9]

### Apply the 80/20 Rule to Files

The Pareto principle applies to codebases: a small fraction of files — the highest-traffic modules, the core data transformations, the critical infrastructure code — are touched in nearly every feature. Ask experienced colleagues which files they modify most often, then prioritize those. Tools like `git log --oneline --all -- <file>` reveal which files have the highest churn, a reliable proxy for importance.[10][12]

***

## Phase 2 — Git Archaeology: Mining the History for Intent

Source control is not just a backup mechanism; it is a living historical record of every decision, trade-off, and refactor the system has ever undergone. Mining this history — a practice called *code archaeology* — is one of the most underutilized techniques for understanding legacy systems.[13][14]

### Use `git blame` and `git log` Aggressively

`git blame` reveals who wrote every line and when. This is useful not for assigning blame but for identifying the *original author* of a confusing piece of logic, so you can ask them about the design intent. More powerful is `git log -S <string>` (the "pickaxe" command), which finds every commit that added or removed a particular string — invaluable for tracing when a specific function or constant was introduced and why. The `git log --follow -p -- <file>` command shows the complete evolution of a single file across renames and moves.[14][2]

### Use `git bisect` to Find Regressions

`git bisect` performs a binary search through commit history to find the exact commit that introduced a behavioral change. This is far more efficient than manual binary search through PRs. The workflow: mark a known-good commit, mark a known-bad commit, then compile/run/test at each bisect step. This technique is especially powerful for understanding *why* code became the way it is — the breaking commit's diff and message typically contain the crucial context.[15][16]

### Read Recent Pull Requests

Pull requests are annotated, reviewed, and discussed diffs — arguably the richest documentation in any codebase. Reading recent merged PRs in the code paths you're working on reveals patterns, norms, debate, and reviewer feedback that no documentation captures. Participating in ongoing code reviews on PRs you didn't write is one of the most effective onboarding techniques for experienced developers.[17][9]

***

## Phase 3 — Structural Analysis: Visualizing the Architecture

For large codebases — especially those spanning multiple modules, microservices, or language boundaries — visual structural analysis is indispensable. Human working memory cannot hold the full dependency graph of a 500-KLOC system; externalization through diagrams is cognitively necessary.[18]

### Dependency Graphs and Call Graphs

Static analysis tools can generate dependency graphs that reveal which modules depend on which others, and call graphs that show the function-call topology at runtime. Academic research confirms that call graphs and class collaboration networks are among the most useful representations for software comprehension tasks. Tools like NDepend (for .NET), Understand by SciTools (multi-language), and RefExpo (Java/Python/JavaScript) can generate these automatically. For Rust projects specifically, `cargo-llvm-lines` and `cargo-call-stack` can produce call graph data.[19][20][21][22][18]

### Identify Hotspots and Coupling

Dependency matrices — a compact tabular representation of the dependency graph — are particularly effective for spotting problematic coupling patterns such as circular dependencies. A module with an unusually high number of incoming edges is a hotspot: changes there ripple everywhere, and it therefore deserves deeper study first. The *COD (Change-Oriented Dependencies) model* combines change frequency with coupling complexity to surface the files where both understanding and care are most needed.[23][24]

### Sequence Diagrams for Dynamic Behavior

While dependency graphs describe structural relationships, sequence diagrams describe runtime *behavior*. For systems driven by events, RPC chains, or complex asynchronous workflows, drawing a sequence diagram of a single end-to-end request flow (e.g., "what happens when a user submits an order") is extremely effective. Tools like PlantUML and Mermaid can generate these from textual descriptions, making them maintainable alongside code.[7]

***

## Phase 4 — Active Exploration: Running, Breaking, and Rebuilding

Reading code statically is like studying a map without ever hiking the terrain. The only way to develop true intuition for a codebase is to run it, modify it, observe its behavior, and reason about the gap between expectation and reality.[6][1]

### Build and Run First

Before any serious exploration, ensure you can compile the code, make changes, run the test suite, and observe the application through a debugger and profiler. This is non-negotiable. Developers who skip this step form mental models based purely on static reading, which are systematically incomplete because they miss the effects of configuration, environment, runtime polymorphism, and lazy initialization.[1]

### Use a Debugger, Not Just Logs

Debuggers provide dramatically more information than log statements: the full call stack at any breakpoint, the current values of all local and closed-over variables, and the ability to step into any called function on demand. Setting a breakpoint at the entry point of a request handler and stepping through the entire execution reveals the real runtime control flow, which often diverges significantly from what static analysis suggests. For understanding a specific behavior, run the relevant unit tests under the debugger rather than the entire application — this provides a tight, reproducible execution context.[25][26][2]

### Write Experimental Tests

Writing small, throwaway tests against the code you are trying to understand serves a dual purpose: it forces you to formalize your hypotheses about the code's behavior, and it immediately reveals when those hypotheses are wrong. Tests are also executable documentation — after removing or committing them, they serve as a record of learned behavior. For codebases with low test coverage, adding tests while onboarding is a valuable contribution that simultaneously builds understanding.[27][6]

### Do Small Tasks First

The most effective onboarding strategy for a commercial codebase is to pick up small, isolated tasks — bug fixes, minor refactors, or technical debt items — before tackling large features. These tasks force engagement with real code in a low-risk context, and the act of solving a small problem in an unfamiliar system builds far more confidence and knowledge than passive reading ever could. In open-source projects, these are the "good first issue" tickets.[5][2]

***

## Phase 5 — Social Learning: Humans as Documentation

No tool, diagram, or git log substitutes for direct knowledge transfer from engineers who have internalized the system over years. Social strategies for learning a codebase are consistently among the highest-leverage interventions available.[4]

### Pair Programming with Domain Experts

Pair programming with an experienced team member accelerates onboarding faster than almost any solo technique. Watching an expert navigate and debug a codebase in real time reveals navigation habits, IDE shortcuts, diagnostic heuristics, and architectural intuitions that would take months to develop independently. Even a few hours of pairing per week dramatically compresses the ramp-up curve. The research on agile onboarding confirms pairing as one of the most highly recommended techniques for both speed and knowledge transfer quality.[28][29][3]

### Ask Targeted Questions at the Right Abstraction Level

Vague questions ("how does the auth module work?") generate vague answers. Targeted questions tied to specific code paths ("why does `UserSession::refresh()` call `PermissionCache::invalidate()` before returning — is there a race condition concern here?") generate precise, memorable answers that are anchored to the actual code. This forces you to have done preliminary reading before asking, which makes the answer far more retainable.[8]

### The "Feynman Technique" for Code

Explaining code to others — whether to a colleague, in a team wiki, or even aloud to an imaginary listener (the "rubber duck") — is a powerful comprehension technique grounded in cognitive science. The verbalization process engages language-processing neural pathways in addition to visual ones, activating both Broca's and Wernicke's areas. More importantly, it forces linearization of understanding: you cannot explain something sequentially without discovering the gaps in your own model. Writing up a brief explanation of a newly-learned module in the team wiki serves triple duty: it cements your own understanding, it produces documentation, and it invites correction from experts.[30][31][32]

***

## Phase 6 — AI-Augmented Exploration (2025–2026 Landscape)

The emergence of large-context AI coding assistants has added a significant new layer to codebase exploration, particularly for onboarding to large, complex repositories with millions of lines of code.

### Cursor: Codebase-Aware Chat and Navigation

Cursor (built on VS Code) allows engineers to query entire codebases in natural language: "how does our user authentication flow work?" triggers a traversal of relevant files from controllers to service layers to schemas, returning a coherent plain-English explanation. For 2026, Cursor introduced predictive indexing — anticipating which files are relevant based on current architectural changes — which dramatically reduces context-setting overhead.[33]

### Sourcegraph Cody: Enterprise-Scale Code Intelligence

For Fortune 500 monorepos with tens of millions of lines of code, Sourcegraph Cody is purpose-built for scale. Unlike tools that re-index code on demand, Cody leverages Sourcegraph's pre-built precise code graph — containing all symbol definitions, references, and dependencies — to answer complex cross-referential questions with high accuracy. It supports queries like "find all callers of this function across the entire monorepo" or "show me every place where this configuration key is consumed".[34][35][36][33]

### AI Tool Comparison for Codebase Learning

| Tool | Codebase Scale Strength | Best Use Case | Limitation |
|------|------------------------|---------------|------------|
| Cursor | Mid-to-large repos | Interactive Q&A, navigation, root cause analysis | Requires re-indexing on context switch |
| Sourcegraph Cody | Enterprise monorepos (millions of lines) | Deep cross-repo dependency queries | Setup complexity; enterprise cost |
| GitHub Copilot Workspace | Single-repo tasks | Guided exploration via task-oriented sessions | Less suited for pure exploration queries |
| Claude Code | Any size | Architectural explanation, refactoring guidance | Context window limits for very large repos |

[35][37][33]

### Graph-Based AI Understanding

An emerging approach represents the codebase as a property graph (nodes = functions/classes/modules, edges = calls/imports/inherits) and layers AI query capabilities on top. This enables questions like "what is the maximum function call chain in this repo?" — answered by running a Cypher graph query rather than an LLM context-window scan — providing deterministic, scalable answers over very large codebases.[38][39]

***

## Phase 7 — Cognitive Strategies and Mental Model Construction

Beyond tools and tactics, expert code readers employ specific cognitive strategies that distinguish them from novices. Understanding these strategies allows deliberate practice.

### Chunking and Pattern Recognition

Expert developers "chunk" code into meaningful patterns — they recognize a repository pattern, a factory method, an event sourcing architecture — and process these chunks as single units rather than reading line-by-line. This is why experience in multiple codebases accelerates learning each new one: every new system shares patterns with previous ones. Actively cataloging the design patterns you encounter in a new codebase builds this chunking vocabulary faster.[40]

### Program Slicing (Mental and Tooled)

When debugging or understanding a specific behavior, mentally or tooled "slice" the program to only the statements that affect a particular variable or output. This is a well-studied software comprehension technique that filters out noise and reduces the cognitive space from "the whole codebase" to "the 30 lines that actually matter for this question." IDE features like "Find Usages" and "Go to Definition" implement lightweight program slicing interactively.[7]

### The "Campsite" Strategy

Rather than attempting to understand the entire codebase uniformly, deeply master one specific feature area and use it as a base camp. From this well-understood area, venture into adjacent modules as needed by tasks, always returning to extend the base camp rather than starting fresh. This is how expert engineers in large organizations naturally develop: they are deep experts in a subsystem and have progressively expanding shallow familiarity with surrounding systems.[6]

### Accept Asymptotic Understanding

Large, long-lived codebases are never fully understood by any single person — not even the original authors. The goal is not complete comprehension but *sufficient comprehension for the task at hand*, combined with the navigational skill to rapidly acquire new understanding when needed. Setting the expectation of full understanding creates anxiety and paralysis; accepting asymptotic, task-driven understanding enables productive contribution from day one.[3]

***

## Tooling Reference

### Static Analysis and Visualization

| Tool | Language | Capability |
|------|----------|------------|
| Understand (SciTools) | Multi-language | Dependency graphs, call graphs, UML, metrics |
| NDepend | .NET/C# | Dependency matrix, coupling analysis |
| RefExpo | Java, Python, JS | Dependency graph extraction |
| Sourcetrail | C/C++/Java/Python | Interactive code map |
| `cargo-call-stack` | Rust | Static call graph for embedded/no-std |

[20][21][22]

### Git Archaeology Commands

```
# Who wrote this line and when?
git blame -L 42,55 src/main.rs

# When was this string introduced?
git log -S "some_function_name" --oneline

# Find the commit that broke behavior (binary search)
git bisect start
git bisect bad HEAD
git bisect good v1.2.0

# Full history of a file including renames
git log --follow -p -- src/auth/session.rs

# Commits that touched both fileA and fileB
git log --all -- fileA.rs fileB.rs
```



### Recommended IDE Features to Master

- **Go to Definition / Find All References**: The foundation of interactive code navigation
- **Call Hierarchy**: Shows all callers and callees of a function, typically available in VS Code, IntelliJ, and rust-analyzer
- **Type Hierarchy**: For object-oriented systems, reveals inheritance trees
- **Structural Search and Replace** (IntelliJ): AST-aware search that finds patterns rather than string literals
- **Git Lens / Git Blame Inline**: Brings commit history inline without leaving the editor[14]

***

## A Staged Timeline for Onboarding

| Week | Focus | Milestone |
|------|-------|-----------|
| 1 | Product familiarization, architecture docs, team meetings, visual map | Can describe what the system does and its major components |
| 2 | Entry points, data model, key files, first small task | First PR merged |
| 3–4 | Debugger-driven deep dives, test runs, git archaeology on worked areas | Can independently locate relevant code for any bug report |
| 5–8 | Broader module exploration, pair programming on complex features | Can propose and implement features with architectural awareness |
| 3–6 months | Subsystem ownership, contributing to code reviews | Recognized as a domain expert in at least one subsystem |

[5][17][4]

***

## Conclusion

Learning a large codebase is not a reading problem — it is a mental-model-building problem. The highest-leverage investments are: starting with product understanding and architecture documents before touching code; using the git history as a first-class source of intent and rationale; constructing visual dependency and call graphs to externalize what working memory cannot hold; running code through a debugger rather than only reading it; picking up small tasks to force engagement with real execution paths; pairing with domain experts to transfer tacit knowledge quickly; and — in 2025–2026 — leveraging AI coding assistants like Cursor and Sourcegraph Cody for cross-referential queries at scale. The goal is not omniscience but navigational fluency: the ability to rapidly locate, understand, and modify any piece of the system as tasks demand.[2][1][6]

```