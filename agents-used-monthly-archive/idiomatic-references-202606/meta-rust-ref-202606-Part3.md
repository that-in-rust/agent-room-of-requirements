# Meta Rust Reference 202606 Part 3

Purpose: encyclopedia-grade Rust reference extracted repo-by-repo from every Git repository under `/Users/amuldotexe/Desktop`, with special attention to tree-sitter, parser, compiler, graph, async, storage, FFI, CLI, testing, and architecture patterns.

Assigned repo slice: `meta-rust-ref-202606-Part3-repos.txt`

Coverage status: coordinator completion pass applied; verify with tools/verify_meta_rust_ref.py.

## Architecture Lens

This corpus uses the `matt-engineering-improve-codebase-architecture` vocabulary:

- Module: anything with an interface and an implementation.
- Interface: every fact callers must know, including invariants, ordering constraints, errors, configuration, and performance characteristics.
- Implementation: the code inside the module.
- Depth: leverage at the interface; a deep module hides substantial behavior behind a small interface.
- Seam: where an interface lives and behavior can vary without editing in place.
- Adapter: a concrete thing satisfying an interface at a seam.
- Leverage: caller benefit from depth.
- Locality: maintainer benefit from concentrated change and verification.

## Extraction Protocol

- Browse assigned repositories repo by repo.
- Record every repository as either `Repo Coverage` or `Skipped Repo`.
- Prefer Rust source, Cargo workspaces, parser implementations, tree-sitter grammars, query files, compiler frontends, tokenizer/lexer/parser code, graph walkers, code intelligence tools, and agentic code-assist infrastructure.
- Include exact relative or absolute file evidence and short snippets when they teach a reusable shape.
- Explain the module/interface/implementation/seam/depth lesson, not only the syntax.
- Include transfer rules, risks, and verification hooks so an agent can reuse the pattern safely.
- Capture non-Rust parser or grammar implementations only when they illuminate Rust parser work or a Rust-adjacent architecture pattern.

## Repo Slice

- `/Users/amuldotexe/Desktop/notes-plans-hub/Notes2026`
- `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/alien`
- `/Users/amuldotexe/Desktop/oss-read-only/arroyo`
- `/Users/amuldotexe/Desktop/oss-read-only/codex`
- `/Users/amuldotexe/Desktop/oss-read-only/great_expectations`
- `/Users/amuldotexe/Desktop/oss-read-only/materialize`
- `/Users/amuldotexe/Desktop/oss-read-only/parseltongue-rust-LLM-companion`
- `/Users/amuldotexe/Desktop/oss-read-only/risingwave`
- `/Users/amuldotexe/Desktop/oss-read-only/tao`
- `/Users/amuldotexe/Desktop/oss-read-only/xarray`
- `/Users/amuldotexe/Desktop/personal-repos-lane/DailyJournal202309`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/LiveMCPBench`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ToolRoute`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/confido-exploration-01`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/lazy-tool`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/tau2-bench`
- `/Users/amuldotexe/Desktop/personal-repos-lane/before-i-go`
- `/Users/amuldotexe/Desktop/personal-repos-lane/dima-20241129`
- `/Users/amuldotexe/Desktop/personal-repos-lane/extract_twitter202304`
- `/Users/amuldotexe/Desktop/personal-repos-lane/games-001`
- `/Users/amuldotexe/Desktop/personal-repos-lane/journal-202401`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/graph-data-science-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-dotnet-driver-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-javascript-driver-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4rs-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-arrow-rs-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-jena-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/blazegraph-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/datafusion-python-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/falkordb-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphblas-pointers-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gridgraph-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/janusgraph-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v1_impls-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/materialize-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/nebula-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/petgraph-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/redisgraph-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/sled-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tantivy-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/timely-dataflow-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/mermish`
- `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-fmt-fixed-capacity`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/0sec-labs__foxguard`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aaron-212__tree-sitter-mojo`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Akzestia__tree-sitter-cql`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__tree-sitter-xml`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diff-guardian`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Ataraxy-Labs__weave`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/BrendanJamesLynskey__CodingAgents_01_Repo_Understanding`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Christoph__treesitter-mcp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeEditApp__CodeEditSourceEditor`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Crysthamus__tree-sitter-sln`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DerekStride__tree-sitter-sql`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Egonex-AI__Understand-Anything`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Flakebi__tree-sitter-llvm-mir`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GDQuest__GDScript-formatter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GumTreeDiff__tree-sitter-parser`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Himujjal__tree-sitter-svelte`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Idorobots__tree-sitter-org`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/JavierPrior845__clean-ast-linter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/JoranHonig__tree-sitter-solidity`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Labpics-Team__Laborant`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ManahilShahid45__CodebaseAI`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OXY2DEV__tree-sitter-kitty`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OpenModelica__tree-sitter-metamodelica`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PedroZappa__tree-sitter-strdl`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RRethy__nvim-treesitter-endwise`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ReyNeill__Kontxt`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Shivam-vachhani__Codebase-QA-RAG-System`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Swastik-Gupta30__DevContext`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/TrySita__AutoDocs`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/WardBrian__tree-sitter-stan`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Xattaus__claude-brain`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/abiriadev__tree-sitter-melody`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/adsouza5__lens-api`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/airbus-cert__tree-sitter-powershell`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/albatrossSKY__tokenmin`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/alexmozaidze__tree-sitter-fennel`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aptos-labs__tree-sitter-move-on-aptos`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/asgerf__dts-tree-sitter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/awsum-lang__tree-sitter-awsum`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bennypowers__nvim-regexplainer`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/biomejs__biome`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/brianp__tree-sitter-aster`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/camdencheek__tree-sitter-dockerfile`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cathaysia__tree-sitter-jinja`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cmillstead__codesight-mcp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/comby-tools__comby`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cpkio__tree-sitter-asciidoc`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cursorless-dev__vscode-parse-tree`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dchinmay2__nvim-ts-rainbow`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/djacobsmeyer__repomap-go`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dooosp__ghostcode-auditor`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/elara-labs__code-context-engine`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/emacs-tree-sitter__ts-fold`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ethan-leba__tree-edit`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/fl0w1nd__repomap-mcp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/folke__twilight.nvim`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/gbprod__tree-sitter-gitcommit`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/github__semantic`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/glyphtrail__glyphtrail`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/grantjenks__py-tree-sitter-languages`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hesnotsoharry__codebase-graph-mcp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hzj-Jeff-07__AI-CodeGuard`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ikatyang__tree-sitter-vue`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/intersystems__tree-sitter-objectscript`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jhillacre__tree-sitter-ic10-typed`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jlcrochet__tree-sitter-html`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/joernio__joern`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/josteink__tree-sitter-structurizr`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kcl-lang__tree-sitter-kcl`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kristoferssolo__tree-sitter-bruno`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/langston-barrett__tree-sitter-edit`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/leandrocp__mdex`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lkwslm__tree-sitter-mcp-code-analyzer`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/marceline-cramer__tree-sitter-grain`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/merico-ai__tree-sitter-objc`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mitchellh__tree-sitter-proto`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/move-hub__tree-sitter-move`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/n24q02m__better-code-review-graph`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nendotools__tree-sitter-mcp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nick79__diffguard`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/njenia__envgrd`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nvim-treesitter__nvim-treesitter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/omarjatoi__tree-sitter-flix`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/opengrep__opengrep`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/palmcivet__kiwi-vscode`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pmd__pmd`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pssgowtham__codereviewer`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ralscha__tree-sitter-mcp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/reybits__ts-forge.nvim`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rmuir__tree-sitter-javadoc`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/s0__tree-sitter-hast`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/salesforce__CodeTF`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/scip-code__scip-java`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/semgrep__semgrep`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/simonbs__Runestone`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/smpanaro__tree-sitter-flatbuffers`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcegraph__scip-clang`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/spiritengine__wale`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/stadelmanma__tree-sitter-fortran`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sunny-chung__ktreesitter-json`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/taeezx44__ai-td-detector`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/the-mikedavis__tree-sitter-git-config`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tlaplus-community__tree-sitter-tlaplus`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-grammars__tree-sitter-diff`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-perl__tree-sitter-perl`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__haskell-tree-sitter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__parser-setup-action`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-cpp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-haskell`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-julia`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-regex`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-typescript`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/uncenter__tree-sitter-tera`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/urbit-pilled__tree-sitter-hoon`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vigoux__tree-sitter-viml`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vovasilenko__copycara`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/win4r__codebase-memory-mcp-pro`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/xberg-io__tree-sitter-language-pack`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/z16166__RustLines`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zeta1999__ocaml-tree-sitter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/pensieve2024`
- `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement`
- `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/lihengming__spring-boot-api-project-seed`
- `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/spring-guides__gs-securing-web`
- `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/sqshq__piggymetrics`
- `/Users/amuldotexe/Desktop/personal-repos-lane/rustASCII`
- `/Users/amuldotexe/Desktop/personal-repos-lane/tweet_scrolls_convert_tool`
- `/Users/amuldotexe/Desktop/personal-repos-lane/wandlorelabs2025`
- `/Users/amuldotexe/Desktop/personal-repos-lane/zztweetbook202408`
- `/Users/amuldotexe/Desktop/reference-repos-yard/aeneas`
- `/Users/amuldotexe/Desktop/reference-repos-yard/charon`
- `/Users/amuldotexe/Desktop/reference-repos-yard/eurydice`
- `/Users/amuldotexe/Desktop/reference-repos-yard/iggy`
- `/Users/amuldotexe/Desktop/reference-repos-yard/mempalace`
- `/Users/amuldotexe/Desktop/reference-repos-yard/rust-gpu`
- `/Users/amuldotexe/Desktop/reference-repos-yard/tauri`

## Pattern Entries

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter`

### Concept: FFI-backed syntax tree Module with Rust lifetime ownership at the seam

Evidence:
- `lib/binding_rust/lib.rs` defines Rust-facing Modules such as `Language`, `Tree`, `Node<'tree>`, `Parser`, `InputEdit`, `Range`, and `Point`.
- `lib/binding_rust/ffi.rs` is the unsafe Adapter seam to the C runtime, with explicit `from_raw` and `into_raw` functions for `TSLanguage`, `TSParser`, `TSTree`, `TSNode`, `TSTreeCursor`, `TSQuery`, and `TSQueryCursor`.
- `lib/src/parser.c`, `lib/src/query.c`, `lib/src/tree.c`, `lib/src/get_changed_ranges.c`, and `lib/src/tree_cursor.c` hold the implementation-heavy runtime that the Rust interface hides.

Architecture lens:
The Rust binding is a deep Module: callers learn `Parser`, `Tree`, `Node`, `Query`, and `InputEdit`, while the implementation hides generated C tables, parse stacks, incremental edit bookkeeping, query execution, and pointer ownership. The seam is not "Rust calls C" in the vague sense; it is the set of opaque wrappers with `NonNull`, `PhantomData`, and documented safety requirements. The Adapter is `ffi.rs`, and locality is excellent: raw pointer reconstruction, consumption, and C ABI names are concentrated in one file instead of leaking into parser callers. The deletion test is decisive: if `lib/binding_rust/lib.rs` disappeared, every caller would have to reason about `TSParser`, `TSTree`, `TSNode`, row/column conversion, and allocation lifetime directly.

Reusable code shape:

```rust
#[repr(transparent)]
pub struct Tree(NonNull<ffi::TSTree>);

#[derive(Clone, Copy)]
#[repr(transparent)]
pub struct Node<'tree>(ffi::TSNode, PhantomData<&'tree ()>);

impl Tree {
    pub const unsafe fn from_raw(ptr: *mut ffi::TSTree) -> Self {
        Self(unsafe { NonNull::new_unchecked(ptr) })
    }

    pub fn into_raw(self) -> *mut ffi::TSTree {
        ManuallyDrop::new(self).0.as_ptr()
    }
}
```

Transfer rule:
When wrapping a C parser or generated grammar in Rust, make the interface typed around domain concepts (`Tree`, `Node`, `Range`, `InputEdit`) rather than exposing raw handles. Put all pointer reconstruction in one Adapter module, use `PhantomData` to express borrowed tree lifetimes, and document every unsafe precondition at the seam. This gives callers leverage because most syntax-tree work becomes ordinary Rust method calls.

Verification hook:
Add tests that round-trip parse, edit, and query operations across the seam: parse source to a `Tree`, obtain a `Node<'tree>`, apply an `InputEdit`, call changed-range logic, and run a `Query`. Run under Miri or sanitizer builds when possible because the important correctness claim is pointer and lifetime locality, not just parse output.

### Concept: Incremental edit vocabulary as a portable parser interface

Evidence:
- `lib/binding_rust/lib.rs` defines `Point`, `Range`, and `InputEdit` as small public structs.
- `InputEdit::edit_point` calls `ffi::ts_point_edit`, and `InputEdit::edit_range` calls `ffi::ts_range_edit`.
- `lib/src/get_changed_ranges.c` and `lib/src/get_changed_ranges.h` implement changed-range computation for old/new trees.

Architecture lens:
Tree-sitter treats incremental parsing as an interface vocabulary, not a hidden optimization. Callers do not pass arbitrary closures or offsets only; they describe edits in bytes and row/column points. That makes the Module deep: the interface is a compact, stable edit shape, while the implementation can maintain reusable subtrees and changed ranges internally. The seam has leverage for IDEs, LSP servers, and code intelligence tools because all of them can share the same edit Module without learning parse-stack internals.

Reusable code shape:

```rust
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub struct InputEdit {
    pub start_byte: usize,
    pub old_end_byte: usize,
    pub new_end_byte: usize,
    pub start_position: Point,
    pub old_end_position: Point,
    pub new_end_position: Point,
}
```

Transfer rule:
If a Rust parser, graph indexer, or code intelligence tool supports incremental updates, define a first-class edit Module early. Include byte offsets and human text positions if both are used by callers. Do not let every caller invent its own "diff" shape; that makes the seam shallow and spreads invalid range bugs across the system.

Verification hook:
Use golden tests where a source file is parsed, edited, reparsed, and compared against a fresh parse of the final text. Assert both semantic equivalence and changed-range minimality for representative insertions, deletions, and multi-line edits.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/parseltongue-rust-LLM-companion`

### Concept: Query files as declarative parser Adapters

Evidence:
- `crates/parseltongue-core/src/query_extractor.rs` defines `QueryBasedExtractor` with `queries`, `dependency_queries`, and `parsers` maps keyed by `Language`.
- The same file embeds language queries with `include_str!("../../../entity_queries/rust.scm")` and dependency queries with `include_str!("../../../dependency_queries/rust.scm")`.
- `entity_queries/rust.scm` captures Rust functions, structs, enums, traits, impls, methods, and modules through tree-sitter query captures such as `@definition.function` and `@name`.
- `crates/parseltongue-core/tests/query_based_extraction_test.rs`, `query_json_graph_contract_tests.rs`, and `end_to_end_workflow.rs` exercise the extractor through integration-style tests.

Architecture lens:
`QueryBasedExtractor` moves per-language parser complexity behind a single Rust Module. The interface is "given source, language, and file path, emit entities/dependencies"; the implementation can vary by `.scm` Adapter files. This is a real seam because adding a language changes a query file and parser initialization, not the caller's extraction loop. The Module is deep because it hides parser selection, query compilation, capture interpretation, deduplication, and dependency extraction behind a small interface. Locality is especially strong for parser evolution: grammar-specific knowledge lives in `entity_queries/*.scm` and `dependency_queries/*.scm`.

Reusable code shape:

```rust
pub struct QueryBasedExtractor {
    queries: HashMap<Language, String>,
    dependency_queries: HashMap<Language, String>,
    parsers: HashMap<Language, Parser>,
}

queries.insert(
    Language::Rust,
    include_str!("../../../entity_queries/rust.scm").to_string(),
);
Self::init_parser(&mut parsers, Language::Rust, &tree_sitter_rust::LANGUAGE.into())?;
```

Transfer rule:
For multi-language code intelligence, make grammar-specific extraction declarative and data-backed. Use Rust to own the orchestration Module and `.scm` query files as Adapters at the language seam. Add a new language by adding a parser Adapter plus entity/dependency query files, then keep the graph-writing interface unchanged.

Verification hook:
For every language Adapter, keep one fixture with representative declarations and one fixture with imports/calls. Verify captures by entity type, name, line range, and dependency edge. Contract-test the JSON graph output so query edits cannot silently change downstream graph schema.

### Concept: Tool pipeline interface for code graph workflows

Evidence:
- `crates/parseltongue-core/src/interfaces.rs` defines the async `Tool` trait with `execute`, `validate_input`, and `metadata`.
- `ToolInput` and `ToolOutput` enumerate the six workflow operations: indexing, temporal changes, context generation, validation, write changes, and reset.
- `CodeGraphRepository`, `LanguageParser`, and `LspClient` traits define seams for storage, parsing, and validation.
- `crates/pt08-http-code-query-server/src/route_definition_builder_module.rs` and `http_server_startup_runner.rs` expose the graph workflow over HTTP.

Architecture lens:
The workflow is described as a small set of Modules with explicit interfaces: `Tool`, `CodeGraphRepository`, `LanguageParser`, and `LspClient`. This creates leverage because tests and HTTP handlers can use the same seams as production code. The implementation can use CozoDB, tree-sitter, or LSP clients without making callers know which Adapter is active. The potential risk is interface breadth: `ToolInput` and `ToolOutput` can become shallow if every operation variant accumulates bespoke fields. The current shape is still useful because it centralizes workflow invariants and error modes.

Reusable code shape:

```rust
#[async_trait]
pub trait Tool: Send + Sync {
    async fn execute(&self, input: ToolInput) -> Result<ToolOutput>;
    fn validate_input(&self, input: &ToolInput) -> Result<()>;
    fn metadata(&self) -> ToolMetadata;
}

#[async_trait]
pub trait CodeGraphRepository: Send + Sync {
    async fn store_entity(&mut self, entity: CodeEntity) -> Result<()>;
    async fn query_entities(&self, query: &TemporalQuery) -> Result<Vec<CodeEntity>>;
    async fn reset_temporal_state(&mut self) -> Result<()>;
}
```

Transfer rule:
Use trait seams when a code intelligence workflow has genuinely variable Adapters: in-memory tests, embedded database, remote database, mock parser, real parser, mock LSP, real LSP. Keep the interface behavior-focused and resist adding one trait per function. One Adapter is a hypothetical seam; the second Adapter should justify the trait.

Verification hook:
Write conformance tests against each Adapter: repository CRUD plus temporal reset, parser extraction for malformed and valid code, and LSP validation timeout/error behavior. Run the same test body against fake and production Adapters to verify the seam is real.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/codex`

### Concept: Tool registry plan as a deep Module for action-space construction

Evidence:
- `codex-rs/tools/src/tool_spec.rs` defines `ToolSpec` as a tagged enum for Responses API tools, local shell, image generation, web search, tool search, namespaces, and freeform tools.
- `codex-rs/tools/src/tool_registry_plan.rs` defines `build_tool_registry_plan`, which turns `ToolsConfig` and `ToolRegistryPlanParams` into a `ToolRegistryPlan`.
- `codex-rs/tools/src/tool_definition_tests.rs`, `tool_registry_plan_tests.rs`, `tool_discovery_tests.rs`, and `json_schema_tests.rs` verify serialization and registry behavior.

Architecture lens:
The action space is not scattered across the CLI, core agent loop, MCP code, and protocol serializer. It is concentrated in a registry-plan Module. The interface is "give me config and discovered tool context; get configured tool specs plus handler registration." The implementation owns policy details such as code mode nesting, local shell variants, MCP resource exposure, tool search, plugin install, web search, and parallel-call support. This is high depth: callers get a coherent action space without knowing the branching matrix. Locality is strong because adding a new tool means updating one construction Module and its tests.

Reusable code shape:

```rust
#[derive(Debug, Clone, Serialize, PartialEq)]
#[serde(tag = "type")]
pub enum ToolSpec {
    #[serde(rename = "function")]
    Function(ResponsesApiTool),
    #[serde(rename = "namespace")]
    Namespace(ResponsesApiNamespace),
    #[serde(rename = "tool_search")]
    ToolSearch { execution: String, description: String, parameters: JsonSchema },
    #[serde(rename = "local_shell")]
    LocalShell {},
    #[serde(rename = "custom")]
    Freeform(FreeformTool),
}

pub fn build_tool_registry_plan(
    config: &ToolsConfig,
    params: ToolRegistryPlanParams<'_>,
) -> ToolRegistryPlan { /* central action-space construction */ }
```

Transfer rule:
For agent runtimes, do not let each feature append tools directly to a request. Create a registry-plan Module whose interface returns a complete, validated action space. Put serialization shape, handler identity, parallel-call support, and progressive-disclosure policy behind this seam.

Verification hook:
Snapshot serialized tool JSON for representative configs: no environment, shell enabled, code mode nested, MCP resources, deferred tools, plugin install, and web search. Add negative tests for duplicate names and missing handler registration.

### Concept: Process-placement seam for stdio MCP servers

Evidence:
- `codex-rs/rmcp-client/src/stdio_server_launcher.rs` defines `StdioServerLauncher`, `StdioServerCommand`, and `StdioServerTransport`.
- The same file has `LocalStdioServerLauncher` for local child processes and `ExecutorStdioServerLauncher` for executor-backed process placement.
- `StdioServerTransportInner` privately switches between `TokioChildProcess` and `ExecutorProcessTransport` while implementing `rmcp::transport::Transport<RoleClient>`.
- `codex-rs/rmcp-client/tests/process_group_cleanup.rs` and streamable HTTP tests exercise lifecycle and recovery behavior around MCP transports.

Architecture lens:
The seam is deliberately placed at "launch stdio server and return an rmcp transport." `RmcpClient` does not know whether the implementation placed the process locally or through an executor. This is a real seam because there are two Adapters. It is also a deep Module: the interface is a command plus returned transport, while the implementation hides env overlay construction, cwd fallback, child process setup, executor process wiring, process group cleanup, and transport byte adaptation. Locality is valuable because process lifecycle bugs tend to be severe; this shape gives them one home.

Reusable code shape:

```rust
pub trait StdioServerLauncher: private::Sealed + Send + Sync {
    fn launch(
        &self,
        command: StdioServerCommand,
    ) -> BoxFuture<'static, io::Result<StdioServerTransport>>;
}

enum StdioServerTransportInner {
    Local(TokioChildProcess),
    Executor(ExecutorProcessTransport),
}
```

Transfer rule:
When a Rust async system can run a subprocess in multiple placements, make placement an Adapter behind a transport interface. Keep process handles and cleanup attached to the returned transport so callers cannot forget lifecycle obligations.

Verification hook:
Use tests that start a tiny stdio JSON-RPC fixture in both placements, exchange one request/response, close the transport, and assert no child process remains. On Unix, include process group termination tests; on all platforms, test env and cwd propagation.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/biomejs__biome`

### Concept: Lossless syntax tree crate as a shared compiler infrastructure Module

Evidence:
- `crates/biome_rowan/src/lib.rs` presents a generic lossless syntax tree interface and re-exports `SyntaxNode`, `SyntaxToken`, `SyntaxElement`, `SyntaxList`, `SyntaxRewriter`, `TreeBuilder`, `RawSyntaxKind`, `NodeCache`, `TextRange`, and `TextSize`.
- `crates/biome_rowan/src/green.rs`, `tree_builder.rs`, `syntax.rs`, and `cursor.rs` hold the implementation-heavy tree machinery.
- `crates/biome_text_size/src/lib.rs`, `size.rs`, and `range.rs` define newtypes for pervasive text offsets and ranges.
- Many parser/formatter crates use the same tree Module: `biome_yaml_parser`, `biome_html_formatter`, `biome_css_formatter`, `biome_markdown_formatter`, `biome_grit_patterns`, and language-specific syntax crates.

Architecture lens:
`biome_rowan` is a deep Module because it turns lossless syntax trees into a shared interface for parsers, formatters, analyzers, and transformations. Callers learn a stable vocabulary (`SyntaxNode`, `SyntaxToken`, `TextRange`, `TreeBuilder`) rather than each language inventing an AST infrastructure. The implementation can use green trees, caches, cursors, and builder checkpoints internally. The separate `biome_text_size` Module is a locality move: offset arithmetic gets a typed seam, reducing accidental `usize` misuse in higher-level compiler code.

Reusable code shape:

```rust
pub use crate::{
    green::{NodeCache, RawSyntaxKind},
    syntax::{SyntaxElement, SyntaxList, SyntaxNode, SyntaxToken, SyntaxRewriter},
    tree_builder::{Checkpoint, TreeBuilder},
};

pub use biome_text_size::{TextLen, TextRange, TextSize};
```

Transfer rule:
For a Rust compiler-like workspace, invest early in a shared syntax tree Module and typed text ranges. Make language crates Adapters over the shared tree interface. This creates leverage across parser, formatter, linter, and code action Modules and gives tests one interface to exercise.

Verification hook:
Use parser round-trip fixtures that assert lossless text preservation, syntax kind stability, range correctness, and formatter/analyzer compatibility. Include offset arithmetic tests for UTF-8 text so `TextSize` and `TextRange` stay trustworthy.

### Concept: Module graph resolution split into pure computation and Salsa storage

Evidence:
- `crates/biome_module_graph/src/module_graph.rs` exposes pure functions `resolve_js_module`, `resolve_css_module`, and `resolve_html_module`.
- The same file defines `ModuleInfo` as a `#[salsa::input]`, plus `ModuleInfoKind`, `SerializedModuleInfo`, and `ModuleDependencies`.
- `ModuleGraphFsProxy`, `PathInfoCache`, `FsWithResolverProxy`, and `ProjectLayout` are used to isolate filesystem and resolver behavior from module graph computation.
- `crates/biome_module_graph/tests/spec_tests.rs` and `benches/module_graph.rs` verify behavior and performance.

Architecture lens:
The graph Module has a clean two-step interface: resolve parsed roots into module info and dependencies, then store/query those facts through Salsa. That split gives locality. Pure resolution bugs live near visitors and path resolution; incremental storage bugs live near Salsa inputs. The seam between filesystem resolution and graph extraction is explicit through `FsWithResolverProxy` and `ModuleGraphFsProxy`, which lets tests provide Adapters without mutating the graph implementation.

Reusable code shape:

```rust
pub fn resolve_js_module(
    root: AnyJsRoot,
    path: &BiomePath,
    fs: &dyn FsWithResolverProxy,
    project_layout: &ProjectLayout,
    semantic_model: Arc<biome_js_semantic::SemanticModel>,
    path_info_cache: &PathInfoCache,
    enable_type_inference: bool,
) -> (JsModuleInfo, ModuleDependencies, Vec<ModuleDiagnostic>) {
    path_info_cache.prepopulate_directory_path_info(fs, &[path]);
    let fs_proxy = ModuleGraphFsProxy::new(fs, path_info_cache, project_layout);
    let visitor = JsModuleVisitor::new(root, path.to_path_buf(), directory, &fs_proxy, semantic_model, enable_type_inference);
    /* collect info and dependencies */
}
```

Transfer rule:
When building a Rust code graph, separate "extract graph facts from parsed input" from "store graph facts incrementally." Use pure functions for extraction and an incremental database Module for caching. Put filesystem and resolver access behind a seam so tests can cover path edge cases without touching the real filesystem.

Verification hook:
Golden-test module graphs for static imports, dynamic imports, CSS imports, HTML embedded content, cycles, missing files, and project-layout aliases. Add incremental tests that update one file and assert the recomputed dependency set is local.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-arrow-rs-src`

### Concept: Unsafe columnar array trait with specification-backed invariants

Evidence:
- `arrow/src/array/mod.rs` defines `pub unsafe trait Array: Debug + Send + Sync` with methods such as `as_any`, `to_data`, `into_data`, `data_type`, `slice`, and `len`.
- The same file explicitly states that implementations must comply with the Arrow specification and warns that third-party implementations are risky because internal code depends on `Array::data_type`.
- `arrow-schema/src/lib.rs`, `datatype.rs`, `field.rs`, and `schema.rs` define the logical type vocabulary.
- `arrow-data/src/data.rs`, `arrow-buffer`, and `arrow/src/compute/mod.rs` provide the implementation substrate and kernels.
- `arrow/tests/array_validation.rs`, `array_equal.rs`, `array_transform.rs`, and many `arrow/benches/*` files test invariants and performance.

Architecture lens:
Arrow makes its central data Module deep by placing a narrow trait interface over a large and highly constrained implementation. The important design point is that the interface includes invariants, not just methods: array implementors must obey the Arrow memory specification, type identity, slicing semantics, null validity, and `Send + Sync` behavior. The `unsafe trait` is an honest seam marker. It tells callers and implementors that violating the interface can invalidate internal assumptions. The `arrow-schema` Module supplies leverage by giving every array, compute kernel, IPC reader, and Parquet Adapter the same logical type vocabulary.

Reusable code shape:

```rust
pub unsafe trait Array: std::fmt::Debug + Send + Sync {
    fn as_any(&self) -> &dyn Any;
    fn to_data(&self) -> ArrayData;
    fn into_data(self) -> ArrayData;
    fn data_type(&self) -> &DataType;
    fn slice(&self, offset: usize, length: usize) -> ArrayRef;
    fn len(&self) -> usize;
}
```

Transfer rule:
Use an `unsafe trait` only when the interface has non-local invariants that Rust cannot check and downstream implementation may assume. For parser or graph systems, this applies to zero-copy arenas, typed buffers, FFI-backed syntax nodes, and offset-indexed storage. Keep the invariants in the trait docs and provide validation tests, because the interface is the test surface.

Verification hook:
Run a shared conformance suite over every concrete array Adapter: data type correctness, length/null consistency, zero-copy slicing, equality, transform, FFI, and panic-free invalid-data rejection. Add fuzz tests for offset and null-buffer combinations because unsafe interface bugs hide in edge cases.

### Concept: Builder-style semantic options instead of flag soup at call sites

Evidence:
- `arrow-schema/src/lib.rs` defines `SortOptions { descending, nulls_first }` with builder-like methods `desc`, `asc`, `nulls_first`, `nulls_last`, `with_descending`, and `with_nulls_first`.
- `arrow-ord/src/sort.rs`, `partition.rs`, and `comparison.rs` consume sort and comparison vocabulary from schema/array Modules.

Architecture lens:
`SortOptions` is a small Module, but it is deep enough to remove repeated boolean interpretation from callers. The interface names semantics (`DESC NULLS LAST`) rather than exposing positional booleans everywhere. That improves locality because sort option formatting, negation, and defaults live with the type. It also reduces shallow call sites in compute kernels where boolean arguments would be easy to invert.

Reusable code shape:

```rust
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub struct SortOptions {
    pub descending: bool,
    pub nulls_first: bool,
}

impl SortOptions {
    pub fn desc(mut self) -> Self { self.descending = true; self }
    pub fn nulls_last(mut self) -> Self { self.nulls_first = false; self }
}
```

Transfer rule:
When parser, graph, or storage code has repeated boolean pairs, promote them into a named options Module. Give the Module semantic constructors and display behavior so call sites say what they mean.

Verification hook:
Add table-driven tests for every option combination and verify both behavior and display/debug output. For sort-like options, include null and edge ordering cases.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tantivy-src`

### Concept: Query, Weight, and Scorer as staged execution Modules

Evidence:
- `src/query/query.rs` defines `EnableScoring`, `Query`, and `QueryClone`.
- The `Query` docs explain the staged model: `Query` is a recipe, `Weight` is the recipe tied to a `Searcher`, and `Scorer` is a cursor for one `SegmentReader`.
- `query-grammar/src/query_grammar.rs` and `query-grammar/src/user_input_ast.rs` parse user-facing query strings into an AST before lowering into query Modules.
- `src/schema/mod.rs` defines the schema vocabulary that query parsing, indexing, and retrieval share.
- `benches/query_parser_nested.rs`, `benches/and_or_queries.rs`, `benches/range_queries.rs`, and many `src/query/*` tests/benches verify staged query behavior.

Architecture lens:
Tantivy's search stack has excellent depth because it separates three concerns that are often tangled: declarative query intent, index-statistics binding, and per-segment iteration. The seam between `Query` and `Weight` gives implementation locality for scoring: BM25 statistics can be bound once per searcher instead of recomputed per segment. The `Scorer` seam gives per-segment execution locality. This transfer is especially useful for parser graph queries: parse a query to intent, bind it to a graph snapshot, then create cursors over shards or subgraphs.

Reusable code shape:

```rust
pub trait Query: QueryClone + Send + Sync + downcast_rs::Downcast + fmt::Debug {
    fn weight(&self, enable_scoring: EnableScoring<'_>) -> crate::Result<Box<dyn Weight>>;

    fn count(&self, searcher: &Searcher) -> crate::Result<usize> {
        let weight = self.weight(EnableScoring::disabled_from_searcher(searcher))?;
        let mut result = 0;
        for reader in searcher.segment_readers() {
            result += weight.count(reader)? as usize;
        }
        Ok(result)
    }
}
```

Transfer rule:
For graph walkers or code search, avoid one giant `execute_query` implementation. Split the Module into intent (`Query`), environment-bound plan (`Weight` or `BoundQuery`), and cursor (`Scorer` or `Walker`). This creates seams for caching, explainability, benchmarking, and shard-specific execution.

Verification hook:
For each query type, test parse-to-AST, AST-to-query, query-to-bound-plan, per-segment cursor results, count-only execution, and explanation output. Add benchmarks for scoring enabled/disabled because the interface explicitly promises a performance mode.

### Concept: Schema as the shared interface between ingestion and retrieval

Evidence:
- `src/schema/mod.rs` documents strict field definitions, index/storage flags, fast fields, field validation, and type-to-column mapping.
- It re-exports `Schema`, `SchemaBuilder`, `Field`, `FieldEntry`, `FieldType`, `TextOptions`, `NumericOptions`, `IndexRecordOption`, `FAST`, `INDEXED`, `STORED`, and `Term`.
- `query-grammar` and search examples depend on schema names and field options to determine what queries are valid.

Architecture lens:
The schema Module is deep because it hides a broad set of retrieval rules behind a builder and typed option vocabulary. Callers add fields with capabilities; the implementation uses those capabilities to determine indexing, storage, fast-field access, and query validity. The seam gives leverage to ingestion, query parsing, segment readers, and collectors. It also protects locality: changing how `FAST` maps to columnar storage belongs in schema/fastfield code, not every query caller.

Reusable code shape:

```rust
let mut schema_builder = Schema::builder();
schema_builder.add_u64_field("num_stars", INDEXED | STORED);
schema_builder.add_text_field("title", TEXT | STORED);
let schema = schema_builder.build();
```

Transfer rule:
Any code intelligence index should make "what can be queried, stored, sorted, or aggregated" explicit in a schema Module. Do not let parser extraction decide query capabilities ad hoc.

Verification hook:
Test invalid field names, unsupported query-on-field combinations, fast-field fallback paths, schema serialization, and backward compatibility of schema metadata.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/petgraph-src`

### Concept: Graph traversal traits as algorithm portability seams

Evidence:
- `crates/petgraph/src/visit/mod.rs` defines composable traits such as `GraphBase`, `GraphRef`, `IntoNeighbors`, `IntoNeighborsDirected`, `IntoEdges`, `IntoNodeIdentifiers`, `EdgeRef`, and `Visitable`.
- The same module documents that basic visitors such as `Dfs`, `Bfs`, `DfsPostOrder`, and `Topo` use walker methods and do not hold the graph borrowed except during `.next()`.
- `crates/petgraph/src/data.rs` defines `DataMap`, `DataMapMut`, `Build`, and `Create`.
- `crates/petgraph/tests/*.rs` cover algorithms across graph implementations: `graph`, `stable_graph`, `graphmap`, `csr`, `dijkstra`, `page_rank`, `maximal_cliques`, `min_spanning_tree`, and more.

Architecture lens:
Petgraph places the seam at graph capabilities, not concrete graph storage. Algorithms ask for the minimum interface they need: neighbor iteration, directed edges, node indexing, visit maps, or mutable data. This gives high leverage because one algorithm Module works with `Graph`, `StableGraph`, `GraphMap`, `MatrixGraph`, and `Csr` Adapters. It also improves locality: storage tradeoffs remain in graph implementations, while traversal behavior is verified through shared traits and tests.

Reusable code shape:

```rust
pub trait GraphBase {
    type EdgeId: Copy + PartialEq;
    type NodeId: Copy + PartialEq;
}

pub trait IntoNeighbors: GraphRef {
    type Neighbors: Iterator<Item = Self::NodeId>;
    fn neighbors(self, a: Self::NodeId) -> Self::Neighbors;
}

pub trait EdgeRef: Copy {
    type NodeId;
    type EdgeId;
    type Weight;
    fn source(&self) -> Self::NodeId;
    fn target(&self) -> Self::NodeId;
    fn weight(&self) -> &Self::Weight;
}
```

Transfer rule:
For dependency graphs and code graphs, define traits by traversal capability instead of one monolithic `Graph` trait. A blast-radius algorithm may only need `IntoNeighborsDirected`; a renderer may need `IntoNodeReferences`; a mutating import pass may need `Build`. This prevents shallow interfaces that force every Adapter to implement irrelevant behavior.

Verification hook:
Create an algorithm conformance matrix. Run the same traversal and mutation tests against adjacency-list, stable-index, map-backed, and CSR Adapters. Include borrow-check tests or examples showing walkers do not hold long graph borrows across user work.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/timely-dataflow-src`

### Concept: Timestamp and path-summary contracts for incremental progress

Evidence:
- `timely/src/progress/timestamp.rs` defines `Timestamp`, `PathSummary<T>`, and `Refines<T>`.
- `PathSummary::results_in` and `followed_by` document monotonicity, overflow/invalid-time behavior, and composition equivalence.
- `timely/src/dataflow/operators/mod.rs` re-exports operator Modules such as `Operator`, `Notificator`, `FrontierNotificator`, `Feedback`, `LoopVariable`, `Probe`, `Capture`, and `Input`.
- `timely/tests/barrier.rs`, `shape_scaling.rs`, and examples such as `pagerank.rs`, `bfs.rs`, `hashjoin.rs`, and `event_driven.rs` exercise dataflow progress behavior.

Architecture lens:
Timely's progress Module is deep because it reduces distributed dataflow correctness to a small timestamp interface with strict algebraic laws. The implementation can coordinate frontiers, capabilities, feedback loops, and nested scopes because timestamp advancement is not arbitrary. The seam gives leverage to operator authors: if their timestamp and path summary obey the interface, they can use the larger dataflow runtime without learning all progress internals. Locality is strong because time semantics live in `Timestamp`, `PathSummary`, and `Refines`.

Reusable code shape:

```rust
pub trait Timestamp: Clone + Eq + PartialOrder + Ord + Debug + Any + ExchangeData {
    type Summary: PathSummary<Self> + 'static;
    fn minimum() -> Self;
}

pub trait PathSummary<T>: Clone + Eq + PartialOrder + Debug + Default {
    fn results_in(&self, src: &T) -> Option<T>;
    fn followed_by(&self, other: &Self) -> Option<Self>;
}
```

Transfer rule:
For incremental code graph indexing, streaming parser updates, or async storage compaction, define progress as a typed Module with algebraic laws. Make "can this update advance?" and "how do two paths compose?" part of the interface, not incidental logic in each worker.

Verification hook:
Use property tests for monotonicity and composition: for summaries `a`, `b` and times `t`, `a.followed_by(b).and_then(|s| s.results_in(t))` should match sequential application. Add overflow/invalid progress tests and nested-scope conversion tests.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/sled-src`

### Concept: Guard-owned cache eviction as locality for storage correctness

Evidence:
- `src/tree.rs` defines `Tree<const LEAF_FANOUT: usize = 1024>` with `collection_id`, `ObjectCache`, `Index`, and shutdown dropper.
- `LeafReadGuard` and `LeafWriteGuard` own lock guards inside `ManuallyDrop` and implement `Drop` to release locks before calling `mark_access_and_evict`.
- `Tree::flush` documents a durable fsync contract and returns `FlushStats`.
- `tests/test_crash_recovery.rs`, `tests/concurrent_batch_atomicity.rs`, `tests/test_tree_failpoints.rs`, and `fuzz/fuzz_targets/fuzz_model.rs` verify storage behavior under failures and concurrency.

Architecture lens:
Sled's tree Module concentrates a hard storage invariant: cache access and eviction must happen after leaf locks are dropped. The guard types are the seam. Callers do ordinary tree operations; the implementation ensures lock release, eviction accounting, error recording, and flush-epoch coupling. This is deep because the interface hides concurrency and IO ordering. Locality is excellent: the cache eviction bug class lives in guard `Drop` implementations rather than every read/write path.

Reusable code shape:

```rust
struct LeafWriteGuard<'a, const LEAF_FANOUT: usize = 1024> {
    leaf_write: ManuallyDrop<ArcRwLockWriteGuard<RawRwLock, CacheBox<LEAF_FANOUT>>>,
    flush_epoch_guard: FlushEpochGuard<'a>,
    low_key: InlineArray,
    inner: &'a Tree<LEAF_FANOUT>,
    node: Object<LEAF_FANOUT>,
    external_cache_access_and_eviction: bool,
}

impl<const LEAF_FANOUT: usize> Drop for LeafWriteGuard<'_, LEAF_FANOUT> {
    fn drop(&mut self) {
        unsafe { ManuallyDrop::drop(&mut self.leaf_write); }
        /* then mark access and evict */
    }
}
```

Transfer rule:
When a storage Module has "release lock before side effect" invariants, encode them in guard types. The seam should make the correct lifecycle automatic. Do not rely on every caller to remember lock/eviction ordering.

Verification hook:
Add failpoint tests that trigger IO errors during eviction, crash tests around flush boundaries, and concurrency tests that stress reads/writes while eviction runs. Use fuzz models to compare tree behavior against a simple map.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/materialize`

### Concept: Storage collection interface with frontiers, read holds, and durable transaction seams

Evidence:
- `src/storage-client/src/storage_collections.rs` defines `StorageCollections` with methods for initialization, collection metadata, active collection frontiers, existence checks, snapshot stats, and read policy/frontier management.
- `src/storage-client/src/controller.rs` defines `StorageTxn`, `StorageWriteOp`, and `StorageController`.
- `src/compute-types/src/dataflows.rs` defines `DataflowDescription<P, S>` with imports, exports, `as_of`, `until`, `initial_storage_as_of`, refresh schedule, debug name, and invariant checks.
- `src/testdrive/src/parser.rs`, `src/sql/src/catalog.rs`, and `src/adapter/src/optimize/dataflows.rs` show parser/catalog/planner Modules feeding storage and compute dataflows.

Architecture lens:
Materialize makes time/frontier concepts part of the storage interface. That gives leverage because collection metadata, read holds, snapshot stats, since/upper frontiers, and durable metadata transactions can be reasoned about through explicit Modules. `StorageTxn` is a seam for durable state, while `StorageController` is a seam for orchestration. `DataflowDescription` is a separate deep Module: it packages all facts needed to build a dataflow, including time bounds and dependencies, instead of spreading those facts across planner call sites.

Reusable code shape:

```rust
#[async_trait]
pub trait StorageCollections: Debug + Sync {
    async fn initialize_state(
        &self,
        txn: &mut (dyn StorageTxn + Send),
        init_ids: BTreeSet<GlobalId>,
    ) -> Result<(), StorageError>;

    fn collection_metadata(&self, id: GlobalId)
        -> Result<CollectionMetadata, CollectionMissing>;

    fn collections_frontiers(
        &self,
        id: Vec<GlobalId>,
    ) -> Result<Vec<CollectionFrontiers>, CollectionMissing>;
}
```

Transfer rule:
For code graph stores that support snapshots, incremental indexing, or temporal queries, model frontiers and read holds explicitly. A graph query should say "as of this version/frontier" rather than indirectly depending on global mutable state.

Verification hook:
Test boot reconciliation, metadata transaction atomicity, read hold behavior, since/upper advancement, and invalid `as_of`/`until` dataflow descriptions. Add tests where stale readers prevent compaction or deletion until the hold is released.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/risingwave`

### Concept: StateStore iterator interface with borrowed items and stream conversion

Evidence:
- `src/storage/src/store.rs` defines `IterItem`, `StateStoreIter`, `StateStoreIterExt`, `FromStreamStateStoreIter`, `FusedStateStoreIter`, `StateStoreKeyedRowRef`, and `StateStoreKeyedRow`.
- `StateStoreIter::try_next` returns a future yielding borrowed item references tied to the iterator.
- `StateStoreIterExt::into_stream` converts an iterator into a `Stream` while applying a mapping function.
- `src/storage/src/store_impl.rs` defines `StateStoreImpl` with Hummock, memory, and sled Adapters, plus debug verification through `VerifyStateStore`.
- `src/tests/compaction_test/src/compaction_test_runner.rs` compares Hummock state across versions and snapshots.

Architecture lens:
The state-store iterator seam balances async storage with zero-copy-ish borrowed rows. The interface lets implementations reuse internal buffers while callers still get an async `try_next` shape. `FusedStateStoreIter` concentrates a misuse invariant: once an iterator returns `None` or an error, later calls panic. `StateStoreImpl` is a real Adapter enum because it can hold Hummock, memory, and sled stores behind the same interface. The debug verification Adapter adds locality for correctness checking by comparing actual and expected stores without changing callers.

Reusable code shape:

```rust
pub trait IterItem: Send + 'static {
    type ItemRef<'a>: Send + Copy + 'a;
}

pub trait StateStoreIter<T: IterItem = StateStoreKeyedRow>: Send {
    fn try_next(&mut self) -> impl StorageFuture<'_, Option<T::ItemRef<'_>>>;
}

pub enum StateStoreImpl {
    HummockStateStore(Monitored<HummockStorageType>),
    MemoryStateStore(Monitored<MemoryStateStoreType>),
    SledStateStore(Monitored<SledStateStoreType>),
}
```

Transfer rule:
For graph stores and parser indexes, design iterators around borrowed references when storage owns buffers, but provide a stream Adapter for ergonomic async composition. Add a verification Adapter when there is a simple-but-slow reference implementation.

Verification hook:
Run the same range-scan, point-get, epoch, compaction, and failure tests against Hummock, memory, sled, and verification Adapters. Include misuse tests for calling fused iterators after completion.

### Concept: Fragment graph builder state as locality for streaming plan rewrites

Evidence:
- `src/frontend/src/stream_fragmenter/mod.rs` defines `BuildFragmentGraphState` with the mutable state required to transform a streaming plan into a fragment graph.
- The same module tracks local fragment ids, table ids, operator ids, dependent table ids, share mappings, and backfill flags.
- `GraphJobType` maps job categories to configured parallelism.
- `graph`, `parallelism`, and `rewrite` submodules keep graph construction, parallelism derivation, and plan rewriting local to the fragmenter Module.

Architecture lens:
The fragmenter Module is deep because callers do not manually coordinate fragment ids, table ids, share operators, and backfill flags. Those implementation details live in one builder state. This improves locality for plan rewrites: adding a new rewrite that produces operators uses `gen_operator_id` and share mappings instead of duplicating identity allocation logic.

Reusable code shape:

```rust
pub struct BuildFragmentGraphState {
    fragment_graph: StreamFragmentGraph,
    next_local_fragment_id: FragmentId,
    next_table_id: u32,
    next_operator_id: u32,
    dependent_table_ids: HashSet<TableId>,
    share_mapping: HashMap<StreamNodeLocalOperatorId, LocalFragmentId>,
}
```

Transfer rule:
When lowering a parser AST, query plan, or graph query into executable fragments, put all identity allocation and rewrite bookkeeping into a builder-state Module. This keeps callers from coupling themselves to incidental numbering and sharing rules.

Verification hook:
Golden-test fragment graphs for joins, shares, backfills, sources, sinks, and indexes. Assert deterministic id allocation and parallelism choices for each `GraphJobType`.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/arroyo`

### Concept: Streaming operator lifecycle interface with checkpoint alignment built in

Evidence:
- `crates/arroyo-operator/src/operator.rs` defines `OperatorConstructor`, `ConstructedOperator`, `OperatorNode`, `SourceOperator`, `ArrowOperator`, `ChainedOperator`, and checkpoint handling paths.
- `OperatorNode::run_behavior` routes source and chained operators through startup, ready barrier, control responses, collection, close, and final messages.
- `crates/arroyo-operator/src/lib.rs` defines `CheckpointCounter`.
- `crates/arroyo-datastream/src/logical.rs` defines logical operator and chain shapes.
- `crates/arroyo-controller` and `crates/arroyo-api/src/jobs.rs` expose checkpoint-aware job control states.

Architecture lens:
Arroyo embeds checkpointing and watermarks into the operator interface rather than treating them as side channels. The Module is deep because a source or Arrow operator gets a lifecycle seam (`on_start`, `run`/`process`, checkpoint, watermark, close), while the implementation manages barriers, input queues, control messages, ready synchronization, and collector behavior. This gives leverage to operator authors and locality for checkpoint alignment bugs.

Reusable code shape:

```rust
pub enum ConstructedOperator {
    Source(Box<dyn SourceOperator + Send>),
    Operator(Box<dyn ArrowOperator + Send>),
}

pub enum OperatorNode {
    Source(SourceNode),
    Chained(ChainedOperator),
}
```

Transfer rule:
For async parser pipelines or graph ingestion workers, put lifecycle events in the operator interface: start, process, watermark/progress, checkpoint, and close. If checkpoints are correctness-critical, make them first-class in the seam.

Verification hook:
Use deterministic tests with multiple input queues: send checkpoint barriers on different inputs, assert alignment waits for all required inputs, then verify state snapshot and downstream broadcast. Include source finish and close behavior.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/alien`

### Concept: Cloud provider APIs as many small Adapter seams over one platform model

Evidence:
- `crates/alien-bindings/src/traits.rs` defines platform binding interfaces such as `Storage`, `Build`, `ServiceAccount`, `ArtifactRegistry`, `Vault`, `Kv`, `Queue`, `Function`, `Container`, and `BindingsProviderApi`.
- Provider client crates define concrete provider seams: `alien-aws-clients/src/aws/*.rs`, `alien-gcp-clients/src/gcp/*.rs`, `alien-azure-clients/src/azure/*.rs`, and `alien-k8s-clients/src/kubernetes/*.rs` contain traits such as `S3Api`, `CloudRunApi`, `StorageAccountsApi`, and `DeploymentApi`.
- `crates/alien-terraform/src/emitter.rs`, `alien-helm/src/emitter.rs`, and `alien-cloudformation/src/emitter.rs` define infrastructure emitters.
- `crates/alien-deployment/src/transport.rs` defines `DeploymentLoopTransport`; `crates/alien-manager/src/traits/deployment_store.rs` defines `DeploymentStore`.
- Tests under `crates/alien-bindings/tests/*`, `alien-permissions/tests/*`, and `alien-manager/tests/*` exercise provider and store seams.

Architecture lens:
Alien is less parser-adjacent but useful for Rust architecture. It shows how a large workspace uses many real seams because behavior genuinely varies by cloud provider and renderer. The platform binding Modules create a domain interface, while AWS/GCP/Azure/Kubernetes clients and Terraform/Helm/CloudFormation emitters are Adapters. This avoids a shallow "provider enum everywhere" design. Locality is good when provider behavior changes: provider-specific request signing, API errors, long-running operations, and emit syntax stay in provider modules.

Reusable code shape:

```rust
pub trait Binding: Send + Sync + std::fmt::Debug {}

pub trait Storage: Binding + ObjectStore { /* object storage behavior */ }
pub trait Function: Binding { /* function deployment behavior */ }
pub trait BindingsProviderApi: Send + Sync + std::fmt::Debug { /* resolve bindings */ }
```

Transfer rule:
Use many small seams when the domain has many real Adapters. For a parser corpus, this maps to many language Adapters behind stable entity/dependency interfaces; for deployment, it maps to many provider Adapters behind platform bindings. Avoid introducing a seam before the second Adapter exists.

Verification hook:
Use provider conformance tests with fake clients plus selected live/integration tests. Verify every Adapter handles auth, idempotency, not-found, retryable errors, and rendering output consistently.

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/charon`

### Concept: Rust compiler extraction pipeline with explicit intermediate AST Modules

Evidence:
- `charon/src/lib.rs` documents and re-exports `ullbc_ast` and `llbc_ast`; ULLBC is a cleaned-up MIR-like AST and LLBC is the reconstructed structured form.
- `charon/src/options.rs` exposes translation controls such as `ullbc`, `mir`, `MirLevel`, `StartFrom`, `translate_all_methods`, `print_ullbc`, `print_built_llbc`, and `print_llbc`.
- `charon/src/ast/visitor.rs` defines `AstVisitable`, `BodyVisitable`, `VisitAst`, `VisitAstMut`, and visitor helpers for ULLBC/LLBC bodies, statements, terminators, and binders.
- `charon/hax-frontend/src/*` and `charon/tests/ui/*.rs` show rustc-facing extraction plus broad compiler feature regression fixtures.

Architecture lens:
Charon is a compiler-front-end reference for deep intermediate Modules. It does not try to make every analysis consume rustc internals directly. Instead, the interface is a translated crate in one of several explicit IR layers, with options controlling MIR level and reconstruction stage. The seam between rustc and Charon IR gives leverage: downstream verification tools can reason over stable AST Modules while Charon localizes rustc churn, name matching, drop elaboration, monomorphization, and reconstruction. The visitor interfaces add locality for traversals and transformations.

Reusable code shape:

```rust
pub enum MirLevel { Built, Analysis, Promoted, Optimized, Elaborated }

pub trait AstVisitable: Any { /* generated visit surface */ }
pub trait BodyVisitable: Any { /* ULLBC/LLBC body visit surface */ }

pub fn deserialize_llbc(path: &std::path::Path)
    -> anyhow::Result<ast::TranslatedCrate>;
```

Transfer rule:
When building compiler or parser tooling, introduce explicit IR Modules instead of coupling analyses to the source parser's raw tree. Keep translation options and debug dumps at the seam so failures can be localized to extraction, normalization, or reconstruction.

Verification hook:
Use UI fixture suites that cover language edge cases: closures, GATs, dyn traits, drops, constants, arrays, associated types, unsafe, vtables, and cross-compilation layout. Snapshot each IR layer when possible so transformations are explainable.

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/tauri`

### Concept: Runtime trait seam plus macro-generated command interface

Evidence:
- `crates/tauri-runtime/src/lib.rs` defines `RuntimeHandle<T: UserEvent>` and `Runtime<T: UserEvent>` traits.
- `crates/tauri-runtime-wry/src/lib.rs`, `webview.rs`, and `window.rs` provide the Wry runtime Adapter.
- `crates/tauri/src/plugin.rs`, `crates/tauri-plugin/src/lib.rs`, and `crates/tauri-plugin/src/runtime.rs` define plugin Modules.
- `crates/tauri-macros/src/command/wrapper.rs` and `command/handler.rs` parse command definitions, infer plugin names, filter unused commands, and generate IPC wrappers.
- `crates/tests/acl/src/lib.rs` and `crates/tauri-utils/src/acl/*` verify command and permission surfaces.

Architecture lens:
Tauri keeps native window/webview behavior behind a runtime interface and keeps app-facing command IPC behind macros. The runtime seam is real because Wry is a concrete Adapter and the trait abstracts window, webview, monitor, event, and handle behavior. The command macro Module is deep: users write ordinary Rust functions, while the implementation handles IPC argument parsing, async/blocking differences, plugin command prefixes, ACL filtering, and dead-code removal. Locality is strong because command security rules are concentrated in macro/ACL Modules.

Reusable code shape:

```rust
pub trait RuntimeHandle<T: UserEvent>: Debug + Clone + Send + Sync + Sized + 'static {
    /* event loop and window/webview handle behavior */
}

pub trait Runtime<T: UserEvent>: Debug + Sized + 'static {
    type Dispatcher: RuntimeHandle<T>;
    /* runtime construction and dispatch behavior */
}
```

Transfer rule:
For agent desktop tools or parser workbenches, keep platform/runtime behavior behind a trait seam and generate command glue from declarative inputs. Let the macro own transport-specific argument decoding and permission checks rather than copying that logic into every command.

Verification hook:
Test command macro expansion for app commands and plugin commands, async commands requiring `Result`, ACL filtering, unused command removal, and runtime Adapter behavior through integration examples.

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/iggy`

### Concept: Binary protocol and append-only partition storage as separate deep Modules

Evidence:
- `core/binary_protocol/src/codes.rs`, `codec.rs`, `framing.rs`, `message_layout.rs`, and `dispatch.rs` define wire protocol Modules.
- `core/partitions/src/iggy_partition.rs`, `journal.rs`, `log.rs`, `segment.rs`, `messages_writer.rs`, and `iggy_index_writer.rs` define partitioned message storage.
- `core/journal/src/file_storage.rs` and `metadata_journal.rs` define journal persistence.
- `core/cli/src/args/stream.rs` and `core/cli/src/main.rs` turn stream/topic/partition/message commands into command Modules.
- `bdd/rust/tests/basic_messaging.rs`, `bdd/rust/tests/leader_redirection.rs`, and `core/integration/tests/*` verify behavior end to end.

Architecture lens:
Iggy is relevant to Rust storage and CLI design. It keeps wire encoding, command dispatch, journal metadata, partition logs, and CLI command parsing as separate Modules. That gives interface depth because storage code does not need to know CLI argument shapes, and protocol code does not need to know segment layout. The seam between binary protocol and partition storage is a useful pattern for parser graph servers: wire commands should decode into domain operations before touching storage.

Reusable code shape:

```rust
// Shape, not exact code:
enum Command {
    Stream(StreamAction),
    Topic(TopicAction),
    Partition(PartitionAction),
    Message(MessageAction),
}

// Storage Modules then handle partition log, segment, index, and journal details.
```

Transfer rule:
For graph/query servers, split protocol decoding, command routing, and storage mutation into separate Modules. Keep append-only durability concerns in journal/segment Modules with their own verification.

Verification hook:
Run binary codec round-trip tests, malformed-frame tests, CLI command routing tests, journal recovery tests, and integration tests that produce/consume messages across restarts.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/tao`

### Concept: Window/event-loop crate as a platform Adapter reference

Evidence:
- Bounded scan found `Cargo.toml`, `src/event_loop.rs`, `src/window.rs`, platform-specific modules under `src/platform_impl`, and tests/examples in the Rust workspace.

Architecture lens:
Tao is relevant as a Rust platform Adapter library. The Module interface is a portable window and event-loop vocabulary; the implementation hides macOS, Windows, Linux, iOS, Android, and web platform differences. This is the same architectural shape used by parser workbenches and desktop code intelligence tools when UI/event sources vary by platform.

Reusable code shape:

```text
Portable interface Module:
  EventLoop, EventLoopWindowTarget, Window, WindowBuilder, WindowId
Platform Adapters:
  platform_impl::{macos, windows, linux, android, ios, web}
```

Transfer rule:
When platform behavior varies, put platform-specific code behind an Adapter seam and keep the caller-facing event/window vocabulary stable.

Verification hook:
Run cross-platform event-loop/window tests and example apps on each supported target; add compile-only checks for platform modules.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4rs-src`

### Concept: Async graph database client as protocol Adapter

Evidence:
- Bounded scan found a Rust workspace with `Cargo.toml`, driver source under `lib/src`, tests, and examples for Neo4j/Cypher access.

Architecture lens:
Neo4rs is relevant to graph walker tooling because it separates Cypher query construction, async connection management, row decoding, and transaction behavior from caller code. The graph database protocol is an Adapter seam: callers work with queries and rows while the implementation owns Bolt/network details.

Reusable code shape:

```text
Graph client Module:
  connect/configure -> run query -> stream rows -> decode values
Adapter:
  Bolt transport and Neo4j protocol implementation
```

Transfer rule:
For graph-backed code intelligence, keep database protocol behavior behind a client Module. Do not let query consumers own connection pooling, retry, and value decoding.

Verification hook:
Use containerized Neo4j integration tests plus unit tests for query parameter encoding and row decoding.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/datafusion-python-src`

### Concept: Python binding as FFI Adapter over Rust query engine

Evidence:
- Bounded scan found Rust crates with `Cargo.toml`, Python binding source, and DataFusion integration files.

Architecture lens:
DataFusion Python is a Rust-adjacent FFI pattern: Python receives a small interface for sessions, DataFrames, expressions, and execution, while Rust owns the query optimizer and execution implementation. The Adapter seam is PyO3/native binding code.

Reusable code shape:

```text
Python-facing Module:
  SessionContext, DataFrame, Expression, RecordBatch conversion
Rust implementation:
  DataFusion logical plan, physical plan, Arrow arrays
```

Transfer rule:
If a parser or graph engine needs Python ergonomics, keep the Rust core authoritative and expose a narrow binding Adapter. Convert data at the seam and keep lifetimes/errors explicit.

Verification hook:
Run Python integration tests that create sessions, register data, execute queries, and verify Arrow/Pandas conversion round trips.

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/rust-gpu`

### Concept: Rust compiler backend workspace as shader compilation Adapter

Evidence:
- Bounded scan found a large Rust workspace with compiler/backend crates, examples, and tests under `/Users/amuldotexe/Desktop/reference-repos-yard/rust-gpu`.

Architecture lens:
Rust GPU is relevant as compiler architecture: the interface lets users write Rust-shaped shader code, while the implementation adapts rustc/MIR/codegen concepts to SPIR-V output. The seam is the compilation pipeline and target backend, not individual shader functions.

Reusable code shape:

```text
Source Module:
  Rust crate written for GPU target
Compiler Adapter:
  rustc-facing driver -> SPIR-V lowering -> validation/output
```

Transfer rule:
For domain-specific compilers, keep source-language ergonomics separate from target lowering. Make backend selection and validation explicit at the compilation seam.

Verification hook:
Compile shader fixtures, validate SPIR-V output, and run rendering/compute examples where available.
## Repo Coverage: `/Users/amuldotexe/Desktop/notes-plans-hub/Notes2026`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `notes-plans-hub/Notes2026`
Evidence: `/Users/amuldotexe/Desktop/notes-plans-hub/Notes2026/ab_09_parseltongue_research/docs202603/stable/archive-docs-v2/archive-p1/A-20260227164745-test_live_update.rs`; scan counts include rust_files=2, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
// Test file for live update verification - MODIFIED

pub fn test_function_one() {
    println!("Testing auto-watch detection!");
}

pub fn test_function_two() {
    test_function_one();
}

pub fn test_function_three() {
    println!("New function added!");
    test_function_one();
    test_function_two();
}
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/notes-plans-hub/Notes2026/ab_09_parseltongue_research/docs202603/stable/archive-docs-v2/archive-p1/A-20260227164745-test_live_update.rs` and run `git -C /Users/amuldotexe/Desktop/notes-plans-hub/Notes2026 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/great_expectations`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `oss-read-only/great_expectations`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/great_expectations/contrib/experimental/great_expectations_experimental/expectations/expect_column_kolmogoro_smirnov_test_p_value_to_be_greater_than.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
)


class ColumnKolmogorovSmirnovTestPValueGreaterThan(TableMetricProvider):
    # This is the id string that will be used to reference your Metric.
    metric_name = "column.p_value_greater_than_threshold"
    value_keys = (
        "column_a",
        "column_b",
    )

    # This method implements the core logic for the PandasExecutionEngine
    @metric_value(engine=PandasExecutionEngine)
    def _pandas(
        cls,
        execution_engine,
        metric_domain_kwargs,
        metric_value_kwargs,
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/oss-read-only/great_expectations/contrib/experimental/great_expectations_experimental/expectations/expect_column_kolmogoro_smirnov_test_p_value_to_be_greater_than.py` and run `git -C /Users/amuldotexe/Desktop/oss-read-only/great_expectations ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/xarray`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `oss-read-only/xarray`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/xarray/xarray/tests/test_sparse.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
param = pytest.param
xfail = pytest.mark.xfail

sparse = pytest.importorskip("sparse")
sparse_array_type = array_type("sparse")


def assert_sparse_equal(a, b):
    assert isinstance(a, sparse_array_type)
    assert isinstance(b, sparse_array_type)
    np.testing.assert_equal(a.todense(), b.todense())


def make_ndarray(shape):
    return np.arange(math.prod(shape)).reshape(shape)


def make_sparray(shape):
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/oss-read-only/xarray/xarray/tests/test_sparse.py` and run `git -C /Users/amuldotexe/Desktop/oss-read-only/xarray ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/DailyJournal202309`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/DailyJournal202309`; scan counts include file_count=14, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/DailyJournal202309 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/LiveMCPBench`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/LiveMCPBench`; scan counts include file_count=102, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/LiveMCPBench ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ToolRoute`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ToolRoute`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ToolRoute/scripts/autoloop/lib/parse-battery.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
/**
 * parse-battery.ts — markdown pipe-table parsers for the two eval files.
 *
 * Both files use GitHub pipe tables under `##`/`###` section headers. We parse
 * data rows (skip header + separator), tracking the current section.
 */
import { readFileSync } from 'fs'

function splitRow(line: string): string[] {
  return line.trim().replace(/^\|/, '').replace(/\|$/, '').split('|').map(c => c.trim())
}
function isSep(line: string): boolean {
  return /^\|?[\s:|-]+\|[\s:|-]+$/.test(line.trim()) && line.includes('-')
}

export interface SkillRow {
  section: string
  query: string
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ToolRoute/scripts/autoloop/lib/parse-battery.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ToolRoute ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/confido-exploration-01`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/accio-tools/ignore-references/git-ref-repo/confido-exploration-01`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/confido-exploration-01/Sol-variant-01/src/prompt_parser.rs`; scan counts include rust_files=21, cargo_manifests=2, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
use crate::{AssignmentPrompt, PieError};

pub fn parse_assignment_prompt_json(input: &str) -> Result<AssignmentPrompt, PieError> {
    let prompt: AssignmentPrompt =
        serde_json::from_str(input).map_err(|error| PieError::InvalidPromptJson {
            message: error.to_string(),
        })?;

    if prompt.agent_name.trim().is_empty() {
        return Err(PieError::MissingRequiredField {
            field: "agent_name",
        });
    }
    if prompt.model.trim().is_empty() {
        return Err(PieError::MissingRequiredField { field: "model" });
    }
    if prompt.general_prompt.trim().is_empty() {
        return Err(PieError::MissingRequiredField {
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/confido-exploration-01/Sol-variant-01/src/prompt_parser.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/confido-exploration-01 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/lazy-tool`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/lazy-tool`; scan counts include file_count=172, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/lazy-tool ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/tau2-bench`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/accio-tools/ignore-references/git-ref-repo/tau2-bench`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/tau2-bench/tests/test_voice/test_audio_native/test_gemini/test_parse_response.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
"""Unit tests for GeminiLiveProvider._parse_response.

Tests verify that events are parsed from the correct paths only,
after removing duplicate parsing paths per Gemini team guidance:
- Audio: only from response.data (not inline_data)
- Output transcript: only from server_content.output_transcription (not response.text)
- Function calls: only from response.tool_call (not model_turn.parts)

Uses SimpleNamespace mocks -- no real API calls needed.
"""

import asyncio
from types import SimpleNamespace

from tau2.voice.audio_native.gemini.events import (
    GeminiAudioDeltaEvent,
    GeminiFunctionCallDoneEvent,
    GeminiGoAwayEvent,
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/tau2-bench/tests/test_voice/test_audio_native/test_gemini/test_parse_response.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/tau2-bench ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/before-i-go`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/before-i-go`; scan counts include file_count=4, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/before-i-go ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/dima-20241129`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/dima-20241129`; scan counts include file_count=34, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/dima-20241129 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/extract_twitter202304`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/extract_twitter202304`; scan counts include file_count=11, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/extract_twitter202304 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/games-001`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/games-001`; scan counts include file_count=24, rust_files=0, cargo_manifests=0, candidate_paths=2.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/games-001 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/journal-202401`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/journal-202401`; scan counts include file_count=18, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/journal-202401 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/graph-data-science-src`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/graph-data-science-src`; scan counts include file_count=18, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/graph-data-science-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-dotnet-driver-src`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-dotnet-driver-src`; scan counts include file_count=969, rust_files=0, cargo_manifests=0, candidate_paths=44.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-dotnet-driver-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-javascript-driver-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-javascript-driver-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-javascript-driver-src/packages/bolt-connection/src/load-balancing/least-connected-load-balancing-strategy.js`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```javascript
import RoundRobinArrayIndex from './round-robin-array-index'
import LoadBalancingStrategy from './load-balancing-strategy'

export default class LeastConnectedLoadBalancingStrategy extends LoadBalancingStrategy {
  /**
   * @constructor
   * @param {Pool} connectionPool the connection pool of this driver.
   */
  constructor (connectionPool) {
    super()
    this._readersIndex = new RoundRobinArrayIndex()
    this._writersIndex = new RoundRobinArrayIndex()
    this._connectionPool = connectionPool
  }

  /**
   * @inheritDoc
   */
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-javascript-driver-src/packages/bolt-connection/src/load-balancing/least-connected-load-balancing-strategy.js` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-javascript-driver-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-jena-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-jena-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-jena-src/jena-arq/src/main/java/org/apache/jena/atlas/csv/CSVParseException.java`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text

package org.apache.jena.atlas.csv;

class CSVParseException extends RuntimeException
{
    private static final long serialVersionUID = -7804460281144630746L;
    public CSVParseException(String msg, Throwable cause)    { super(msg, cause) ; }
    public CSVParseException(String msg)                     { super(msg) ; }
    public CSVParseException(Throwable cause)                { super(cause) ; }
    public CSVParseException()                               { super() ; }
}
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-jena-src/jena-arq/src/main/java/org/apache/jena/atlas/csv/CSVParseException.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-jena-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/blazegraph-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/blazegraph-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/blazegraph-src/bigdata-client/src/main/java/com/bigdata/rdf/sail/webapp/client/AST2SPARQLUtil.java`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import org.openrdf.model.URI;
import org.openrdf.model.Value;
import org.openrdf.model.vocabulary.XMLSchema;
import org.openrdf.query.parser.sparql.SPARQLUtil;

/**
 * Utility class for externalizing SPARQL prefix declaration management.
 *
 * @author <a href="mailto:thompsonbry@users.sourceforge.net">Bryan Thompson</a>
 * @version $Id$
 */
public class AST2SPARQLUtil {

    /**
     * The prefix declarations used within the SERVICE clause (from the original
     * query).
     */
    private final Map<String, String> prefixDecls;
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/blazegraph-src/bigdata-client/src/main/java/com/bigdata/rdf/sail/webapp/client/AST2SPARQLUtil.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/blazegraph-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/falkordb-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/falkordb-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/falkordb-src/deps/GraphBLAS/CUDA/select/GB_cuda_select_sparse.cpp`; scan counts include rust_files=7, cargo_manifests=2, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
    GB_cuda_stream_pool_release (&stream) ; \
}

GrB_Info GB_cuda_select_sparse
(
    GrB_Matrix C,               // C is jumbled if A is jumbled
    const bool C_iso,
    const GrB_IndexUnaryOp op,
    const bool flipij,
    const GrB_Matrix A,         // A can be jumbled, in all cases
    const GB_void *athunk,
    const GB_void *ythunk,
    GB_Werk Werk
)
{

    // check inputs
    GrB_Info info = GrB_NO_VALUE ;
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/falkordb-src/deps/GraphBLAS/CUDA/select/GB_cuda_select_sparse.cpp` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/falkordb-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphblas-pointers-src`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphblas-pointers-src`; scan counts include file_count=11, rust_files=0, cargo_manifests=0, candidate_paths=2.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphblas-pointers-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gridgraph-src`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gridgraph-src`; scan counts include file_count=24, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gridgraph-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/janusgraph-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/janusgraph-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/janusgraph-src/docs/index-backend/elasticsearch.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
# Elasticsearch

> Elasticsearch is a distributed, RESTful search and analytics engine
> capable of solving a growing number of use cases. As the heart of the
> Elastic Stack, it centrally stores your data so you can discover the
> expected and uncover the unexpected.
>
> —  [Elasticsearch
> Overview](https://www.elastic.co/elasticsearch/)

JanusGraph supports [Elasticsearch](https://www.elastic.co/) as an index
backend. Here are some of the Elasticsearch features supported by
JanusGraph:

-   **Full-Text**: Supports all `Text` predicates to search for text
    properties that matches a given word, prefix or regular expression.
-   **Geo**: Supports all `Geo` predicates to search for geo properties
    that are intersecting, within, disjoint to or contained in a given
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/janusgraph-src/docs/index-backend/elasticsearch.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/janusgraph-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics-src/graphalytics-core/src/main/java/science/atlarge/graphalytics/configuration/FormattedGraphParser.java`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
 * @author Tim Hegeman
 * @author Wing Lung Ngai
 */
public final class FormattedGraphParser {

	private final Configuration config;
	private final String name;
	private final String graphRootDirectory;

	private long vertexCount;
	private long edgeCount;
	private boolean isDirected;
	private String vertexFilePath;
	private String edgeFilePath;
	private PropertyList vertexProperties;
	private PropertyList edgeProperties;

	private FormattedGraph formattedGraph;
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics-src/graphalytics-core/src/main/java/science/atlarge/graphalytics/configuration/FormattedGraphParser.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v1_impls-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust-Adjacent Parser Reference From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v1_impls-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v1_impls-src/cypher/queries/README.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```text
# Cypher queries

Implementations using [standard openCypher](https://github.com/opencypher/openCypher/blob/master/docs/standardisation-scope.adoc) features.

Use the `./check-feature.sh` script to check for Cypher features used in the implementations. Some examples:

```bash
# variable-length paths
./check-feature.sh ':\w*\*'
# count
./check-feature.sh 'count('
# negative pattern conditions (approximative)
./check-feature.sh 'NOT ('
# UNWIND
./check-feature.sh 'UNWIND'
```
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v1_impls-src/cypher/queries/README.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v1_impls-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/materialize-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust Module Architecture Slice From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/materialize-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/materialize-src/console/src/queries/cancelQuery.ts`; scan counts include rust_files=1454, cargo_manifests=128, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```text
export function useCancelQuery() {
  return useMutation({
    mutationKey: cancelQueryQueryKeys.all(),
    mutationFn: async (params: CancelQueryParams) => {
      return cancelQuery({
        params,
        getConnectionIdFromSessionIdQueryKey:
          cancelQueryQueryKeys.connectionIdFromSessionId(params),
        cancelQueryQueryKey: cancelQueryQueryKeys.cancelQuery(params),
      });
    },
    onError: (error, variables) => {
      Sentry.captureException(error, {
        extra: { variables },
      });
    },
  });
}
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/materialize-src/console/src/queries/cancelQuery.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/materialize-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/nebula-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/nebula-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/nebula-src/src/common/expression/TypeCastingExpression.cpp`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
 * This source code is licensed under Apache 2.0 License.
 */

#include "common/expression/TypeCastingExpression.h"

#include "common/expression/ExprVisitor.h"

namespace nebula {

// first:operand's type  second:vType
static std::unordered_multimap<Value::Type, Value::Type> typeCastMap = {
    // cast to INT
    {Value::Type::INT, Value::Type::INT},
    {Value::Type::FLOAT, Value::Type::INT},
    {Value::Type::STRING, Value::Type::INT},
    {Value::Type::__EMPTY__, Value::Type::INT},
    // cast to STRING
    {Value::Type::STRING, Value::Type::STRING},
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/nebula-src/src/common/expression/TypeCastingExpression.cpp` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/nebula-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/redisgraph-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/redisgraph-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/redisgraph-src/deps/GraphBLAS/GraphBLAS/@GrB/private/mexfunctions/gbsemiringinfo.c`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
//------------------------------------------------------------------------------
// gbsemiringinfo: print a GraphBLAS semiring (for illustration only)
//------------------------------------------------------------------------------

// SuiteSparse:GraphBLAS, Timothy A. Davis, (c) 2017-2022, All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

//------------------------------------------------------------------------------

// Usage:

// gbsemiringinfo (semiring_string)
// gbsemiringinfo (semiring_string, type)

#include "gb_interface.h"

#define USAGE "usage: GrB.semiringinfo (s) or GrB.semiringinfo (s,type)"

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/redisgraph-src/deps/GraphBLAS/GraphBLAS/@GrB/private/mexfunctions/gbsemiringinfo.c` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/redisgraph-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/mermish`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/mermish`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/mermish/A01_STUDY_GUIDES/A03GenericTechNotes/A05UsefulParseltongue.md`; scan counts include rust_files=31, cargo_manifests=11, tree_sitter_query_files=12, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
│  ─────────────────────────────────────────────────────────────────────────  │
│  • get_callers(key)         → Who calls this?                               │
│  • get_callees(key)         → What does this call?                          │
│  • get_blast_radius(key, d) → Multi-hop traversal                           │
│  • find_cycles()            → Circular dependencies                         │
│                                                                              │
│  CODE TOOLS                                                                 │
│  ─────────────────────────────────────────────────────────────────────────  │
│  • get_code(key)            → THE way to see source code                    │
│  • get_entity_details(key)  → Full info + deps + code                       │
│                                                                              │
│  ADMIN TOOLS                                                                │
│  ─────────────────────────────────────────────────────────────────────────  │
│  • list_files()             → Files in codebase                             │
│  • get_stats()              → Entity counts                                 │
│  • get_schema()             → DB introspection                              │
│  • datalog_query(q)         → Raw Datalog                                   │
│
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/mermish/A01_STUDY_GUIDES/A03GenericTechNotes/A05UsefulParseltongue.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/mermish ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-fmt-fixed-capacity`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust Module Architecture Slice From `personal-repos-lane/nostd-fmt-fixed-capacity`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-fmt-fixed-capacity/src/error.rs`; scan counts include rust_files=5, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```rust
//! Error types for fixed-capacity buffer operations
//!
//! This module defines structured error types following the thiserror pattern
//! for library error handling.

use core::fmt;

/// Errors that can occur during fixed-capacity buffer operations
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum FixedBufferError {
    /// Buffer capacity exceeded during write operation
    ///
    /// # Fields
    /// - `bytes_needed`: Total bytes required for the operation
    /// - `bytes_available`: Remaining bytes in the buffer
    CapacityExceeded {
        /// Total bytes required for the operation
        bytes_needed: usize,
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-fmt-fixed-capacity/src/error.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/nostd-fmt-fixed-capacity ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/0sec-labs__foxguard`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/0sec-labs__foxguard`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/0sec-labs__foxguard/src/engine/parser.rs`; scan counts include rust_files=117, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
use crate::Language;
use std::path::Path;

/// Parse source code into a tree-sitter Tree for the given language.
pub fn parse_file(source: &str, language: Language) -> Option<tree_sitter::Tree> {
    parse_source_for_path(source, language, None)
}

/// Parse source code, selecting path-specific grammar variants where needed.
pub fn parse_path(source: &str, language: Language, path: &Path) -> Option<tree_sitter::Tree> {
    parse_source_for_path(source, language, Some(path))
}

fn parse_source_for_path(
    source: &str,
    language: Language,
    path: Option<&Path>,
) -> Option<tree_sitter::Tree> {
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/0sec-labs__foxguard/src/engine/parser.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/0sec-labs__foxguard ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aaron-212__tree-sitter-mojo`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aaron-212__tree-sitter-mojo`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aaron-212__tree-sitter-mojo/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aaron-212__tree-sitter-mojo/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aaron-212__tree-sitter-mojo ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Akzestia__tree-sitter-cql`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Akzestia__tree-sitter-cql`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Akzestia__tree-sitter-cql/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Akzestia__tree-sitter-cql/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Akzestia__tree-sitter-cql ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__tree-sitter-xml`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__tree-sitter-xml`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__tree-sitter-xml/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=4, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

typedef uint16_t TSStateId;

#ifndef TREE_SITTER_API_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__tree-sitter-xml/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__tree-sitter-xml ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diff-guardian`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diff-guardian`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diff-guardian/src/parsers/ast-mapper.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
/**
 * src/parsers/ast-mapper.ts
 *
 * THE ORCHESTRATOR.
 * Receives FileDiff[] from git-diff.ts.
 * Dispatches each file to the correct language translator.
 * Injects filePath into every FunctionSignature (parser doesn't know filenames).
 * Returns ParseResult[] to the classifier.
 *
 * Responsibilities:
 *  1. WASM grammar lifecycle — lazy load, deduplicate, cache
 *  2. Sequential parsing — tree-sitter is fast, sequential keeps WASM heap flat
 *  3. Memory safety — tree.delete() in finally block, always
 *  4. Error isolation — one bad file never aborts the entire diff run
 *  5. filePath injection — the one place that knows both filename and signature
 */

import { Parser, Language as WasmLanguage, Tree } from 'web-tree-sitter';
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diff-guardian/src/parsers/ast-mapper.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diff-guardian ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Ataraxy-Labs__weave`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Ataraxy-Labs__weave`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Ataraxy-Labs__weave/crates/weave-cli/src/commands/mod.rs`; scan counts include rust_files=46, cargo_manifests=7, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
pub mod apply;
pub mod bench;
pub mod bench_repo;
pub mod claim;
pub mod preview;
pub mod release;
pub mod setup;
pub mod stats;
pub mod status;
pub mod summary;
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Ataraxy-Labs__weave/crates/weave-cli/src/commands/mod.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Ataraxy-Labs__weave ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/BrendanJamesLynskey__CodingAgents_01_Repo_Understanding`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/BrendanJamesLynskey__CodingAgents_01_Repo_Understanding`; scan counts include file_count=2, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/BrendanJamesLynskey__CodingAgents_01_Repo_Understanding ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Christoph__treesitter-mcp`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Christoph__treesitter-mcp`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Christoph__treesitter-mcp/benches/parse_bench.rs`; scan counts include rust_files=110, cargo_manifests=3, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
//! Performance benchmarks for view_code operations
//!
//! Run with: cargo bench --bench parse_bench

use criterion::{black_box, criterion_group, criterion_main, BenchmarkId, Criterion};
use serde_json::json;
use std::path::PathBuf;

fn fixture_path(lang: &str, file: &str) -> PathBuf {
    PathBuf::from(env!("CARGO_MANIFEST_DIR"))
        .join("tests")
        .join("fixtures")
        .join(format!("{}_project", lang))
        .join(file)
}

fn bench_view_code_by_language(c: &mut Criterion) {
    let mut group = c.benchmark_group("view_code_by_language");
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Christoph__treesitter-mcp/benches/parse_bench.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Christoph__treesitter-mcp ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeEditApp__CodeEditSourceEditor`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeEditApp__CodeEditSourceEditor`; scan counts include file_count=228, rust_files=0, cargo_manifests=0, candidate_paths=4.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeEditApp__CodeEditSourceEditor ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Crysthamus__tree-sitter-sln`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Crysthamus__tree-sitter-sln`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Crysthamus__tree-sitter-sln/bindings/c/tree_sitter/tree-sitter-sln.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=4, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_SLN_H_
#define TREE_SITTER_SLN_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_sln(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_SLN_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Crysthamus__tree-sitter-sln/bindings/c/tree_sitter/tree-sitter-sln.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Crysthamus__tree-sitter-sln ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DerekStride__tree-sitter-sql`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DerekStride__tree-sitter-sql`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DerekStride__tree-sitter-sql/bindings/c/tree_sitter/tree-sitter-sql.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_SQL_H_
#define TREE_SITTER_SQL_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_sql(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_SQL_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DerekStride__tree-sitter-sql/bindings/c/tree_sitter/tree-sitter-sql.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DerekStride__tree-sitter-sql ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Egonex-AI__Understand-Anything`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Egonex-AI__Understand-Anything`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Egonex-AI__Understand-Anything/understand-anything-plugin/packages/core/src/__tests__/parsers.test.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import { describe, it, expect } from "vitest";
import { MarkdownParser } from "../plugins/parsers/markdown-parser.js";
import { YAMLConfigParser } from "../plugins/parsers/yaml-parser.js";
import { JSONConfigParser, stripJsoncSyntax } from "../plugins/parsers/json-parser.js";
import { TOMLParser } from "../plugins/parsers/toml-parser.js";
import { EnvParser } from "../plugins/parsers/env-parser.js";
import { DockerfileParser } from "../plugins/parsers/dockerfile-parser.js";
import { SQLParser } from "../plugins/parsers/sql-parser.js";
import { GraphQLParser } from "../plugins/parsers/graphql-parser.js";
import { ProtobufParser } from "../plugins/parsers/protobuf-parser.js";
import { TerraformParser } from "../plugins/parsers/terraform-parser.js";
import { MakefileParser } from "../plugins/parsers/makefile-parser.js";
import { ShellParser } from "../plugins/parsers/shell-parser.js";
import { registerAllParsers } from "../plugins/parsers/index.js";
import { PluginRegistry } from "../plugins/registry.js";

describe("MarkdownParser", () => {
  const parser = new MarkdownParser();
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Egonex-AI__Understand-Anything/understand-anything-plugin/packages/core/src/__tests__/parsers.test.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Egonex-AI__Understand-Anything ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Flakebi__tree-sitter-llvm-mir`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Flakebi__tree-sitter-llvm-mir`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Flakebi__tree-sitter-llvm-mir/bindings/c/tree-sitter-llvm_mir.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_LLVM_MIR_H_
#define TREE_SITTER_LLVM_MIR_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_llvm_mir(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_LLVM_MIR_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Flakebi__tree-sitter-llvm-mir/bindings/c/tree-sitter-llvm_mir.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Flakebi__tree-sitter-llvm-mir ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GDQuest__GDScript-formatter`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GDQuest__GDScript-formatter`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GDQuest__GDScript-formatter/queries/gdscript.scm`; scan counts include rust_files=31, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```scheme
  "class_name" "extends" "var" "func" "class"
  "if" "elif" "else" "for" "while"
  "const" "return" "match" "signal" "enum"
  "await" "remote" "master" "puppet" "remotesync"
  "mastersync" "puppetsync"
  (static_keyword)]
@append_space

; Preserve comments and strings as they are
(comment) @leaf
(string) @leaf
(string_name) @leaf
(node_path) @leaf
(region_start) @leaf
(region_end) @leaf

; TYPE ANNOTATION SPACING
(typed_parameter ":" @append_space)
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GDQuest__GDScript-formatter/queries/gdscript.scm` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GDQuest__GDScript-formatter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GumTreeDiff__tree-sitter-parser`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GumTreeDiff__tree-sitter-parser`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GumTreeDiff__tree-sitter-parser/tree-sitter-parser.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#!/usr/bin/env python3

import argparse
import os
from io import StringIO

import yaml
from tree_sitter_parser import (
    EMPTY_CONFIG,
    init_parsers,
    parse_and_translate,
    pretty_print_ast,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="path to the file to parse")
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GumTreeDiff__tree-sitter-parser/tree-sitter-parser.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GumTreeDiff__tree-sitter-parser ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Himujjal__tree-sitter-svelte`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Himujjal__tree-sitter-svelte`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Himujjal__tree-sitter-svelte/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=6, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

typedef uint16_t TSStateId;

#ifndef TREE_SITTER_API_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Himujjal__tree-sitter-svelte/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Himujjal__tree-sitter-svelte ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Idorobots__tree-sitter-org`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Idorobots__tree-sitter-org`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Idorobots__tree-sitter-org/docs/plans/tree-sitter-parser-impl.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
# Tree-sitter Parser Implementation Plan

> Implementation plan for the `tree-sitter-org` parser, based on the
> formal grammar in [`syntax.md`](syntax.md).

---

## Table of Contents

1. [Overview](#1-overview)
2. [Project Layout](#2-project-layout)
3. [Phase 1 — Scaffold & Tooling](#3-phase-1--scaffold--tooling)
4. [Phase 2 — Core Grammar](#4-phase-2--core-grammar)
5. [Phase 3 — External Scanner](#5-phase-3--external-scanner)
6. [Phase 4 — Error Recovery](#6-phase-4--error-recovery)
7. [Phase 5 — Test Corpus](#7-phase-5--test-corpus)
8. [Phase 6 — Integration Testing](#8-phase-6--integration-testing)
9. [Risks & Tradeoffs](#9-risks--tradeoffs)
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Idorobots__tree-sitter-org/docs/plans/tree-sitter-parser-impl.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Idorobots__tree-sitter-org ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/JavierPrior845__clean-ast-linter`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/JavierPrior845__clean-ast-linter`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/JavierPrior845__clean-ast-linter`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
N/A: no source file selected during bounded scan.
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/JavierPrior845__clean-ast-linter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` if this repo changes later.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/JoranHonig__tree-sitter-solidity`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/JoranHonig__tree-sitter-solidity`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/JoranHonig__tree-sitter-solidity/bindings/c/tree-sitter-solidity.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=4, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_SOLIDITY_H_
#define TREE_SITTER_SOLIDITY_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_solidity(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_SOLIDITY_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/JoranHonig__tree-sitter-solidity/bindings/c/tree-sitter-solidity.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/JoranHonig__tree-sitter-solidity ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Labpics-Team__Laborant`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Labpics-Team__Laborant`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Labpics-Team__Laborant/src/repo-intelligence/ast-indexer.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
/**
 * @module repo-intelligence/ast-indexer
 * @description AST-based code indexer using tree-sitter to extract symbol information
 * from source files across multiple programming languages. Builds a complete call
 * graph by performing a two-pass analysis: first extracting symbols and their
 * outgoing call references, then resolving those references into incoming-call
 * (calledBy) edges.
 *
 * Supported languages: TypeScript/TSX, Python, Go, Rust.
 */

import { glob } from 'node:fs/promises';
import { readFile } from 'node:fs/promises';
import { join, relative } from 'node:path';
import Parser from 'tree-sitter';
import Go from 'tree-sitter-go';
import Python from 'tree-sitter-python';
import Rust from 'tree-sitter-rust';
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Labpics-Team__Laborant/src/repo-intelligence/ast-indexer.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Labpics-Team__Laborant ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ManahilShahid45__CodebaseAI`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ManahilShahid45__CodebaseAI`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ManahilShahid45__CodebaseAI/backend/ingestor/ast_chunker.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import tree_sitter_python as tspy
import tree_sitter_javascript as tsjs
from tree_sitter import Language, Parser
from dataclasses import dataclass
from typing import List, Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    PY_LANGUAGE = Language(tspy.language())
    JS_LANGUAGE = Language(tsjs.language())
except Exception as e:
    logger.error(f"Failed to load tree-sitter languages: {e}")
    PY_LANGUAGE = None
    JS_LANGUAGE = None

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ManahilShahid45__CodebaseAI/backend/ingestor/ast_chunker.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ManahilShahid45__CodebaseAI ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode/src/store/block_trait.rs`; scan counts include rust_files=111, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
// See the License for the specific language governing permissions and
// limitations under the License.

//! Generic block type trait for reducing code duplication in store operations

use anyhow::Result;
use arrow_array::RecordBatch;

use super::{CodeBlock, CommitBlock, DocumentBlock, TextBlock};

/// Trait for block types to enable generic store operations
pub trait BlockType: Clone + Send + Sync + 'static {
	/// The table name for this block type
	const TABLE_NAME: &'static str;

	/// Convert blocks to Arrow RecordBatch
	fn to_batch(blocks: &[Self], embeddings: &[Vec<f32>], vector_dim: usize)
		-> Result<RecordBatch>;
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode/src/store/block_trait.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OXY2DEV__tree-sitter-kitty`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OXY2DEV__tree-sitter-kitty`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OXY2DEV__tree-sitter-kitty/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OXY2DEV__tree-sitter-kitty/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OXY2DEV__tree-sitter-kitty ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OpenModelica__tree-sitter-metamodelica`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OpenModelica__tree-sitter-metamodelica`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OpenModelica__tree-sitter-metamodelica/tree-sitter.json`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
{
  "$schema": "https://tree-sitter.github.io/tree-sitter/assets/schemas/config.schema.json",
  "grammars": [
    {
      "name": "metamodelica",
      "camelcase": "MetaModelica",
      "scope": "source.metamodelica",
      "file-types": [
        "mo"
      ],
      "highlights": [
        "queries/highlights.scm"
      ],
      "tags": [
        "queries/tags.scm"
      ],
      "injection-regex": "^mo$"
    }
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OpenModelica__tree-sitter-metamodelica/tree-sitter.json` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OpenModelica__tree-sitter-metamodelica ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PedroZappa__tree-sitter-strdl`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PedroZappa__tree-sitter-strdl`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PedroZappa__tree-sitter-strdl/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PedroZappa__tree-sitter-strdl/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PedroZappa__tree-sitter-strdl ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RRethy__nvim-treesitter-endwise`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RRethy__nvim-treesitter-endwise`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RRethy__nvim-treesitter-endwise/queries/bash/endwise.scm`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=9, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```scheme
((if_statement "then" @cursor) @endable @indent (#endwise! "fi"))
((do_group "do" @cursor) @endable @indent (#endwise! "done"))
((case_statement "in" @cursor) @endable @indent (#endwise! "esac"))
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RRethy__nvim-treesitter-endwise/queries/bash/endwise.scm` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RRethy__nvim-treesitter-endwise ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ReyNeill__Kontxt`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ReyNeill__Kontxt`; scan counts include file_count=9, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ReyNeill__Kontxt ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Shivam-vachhani__Codebase-QA-RAG-System`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Shivam-vachhani__Codebase-QA-RAG-System`; scan counts include file_count=19, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Shivam-vachhani__Codebase-QA-RAG-System ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Swastik-Gupta30__DevContext`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Swastik-Gupta30__DevContext`; scan counts include file_count=12, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Swastik-Gupta30__DevContext ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/TrySita__AutoDocs`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/TrySita__AutoDocs`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/TrySita__AutoDocs/ingestion/src/ast_parsing/queries/__init__.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
"""
Tree-sitter query definitions for AST parsing.
Centralized exports for all query modules.
"""

from .python import PYTHON_QUERY
from .javascript import JAVASCRIPT_QUERY
from .typescript import TYPESCRIPT_QUERY

# Query mapping by language and type
QUERIES = {
    "javascript": {
        "definitions": JAVASCRIPT_QUERY,
    },
    "typescript": {
        "definitions": TYPESCRIPT_QUERY,
    },
    "jsx": {
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/TrySita__AutoDocs/ingestion/src/ast_parsing/queries/__init__.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/TrySita__AutoDocs ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/WardBrian__tree-sitter-stan`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/WardBrian__tree-sitter-stan`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/WardBrian__tree-sitter-stan/grammars/stan/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=6, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/WardBrian__tree-sitter-stan/grammars/stan/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/WardBrian__tree-sitter-stan ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Xattaus__claude-brain`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Xattaus__claude-brain`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Xattaus__claude-brain`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
N/A: no source file selected during bounded scan.
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Xattaus__claude-brain ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` if this repo changes later.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/abiriadev__tree-sitter-melody`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/abiriadev__tree-sitter-melody`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/abiriadev__tree-sitter-melody/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/abiriadev__tree-sitter-melody/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/abiriadev__tree-sitter-melody ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/adsouza5__lens-api`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/adsouza5__lens-api`; scan counts include file_count=11, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/adsouza5__lens-api ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/airbus-cert__tree-sitter-powershell`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/airbus-cert__tree-sitter-powershell`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/airbus-cert__tree-sitter-powershell/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/airbus-cert__tree-sitter-powershell/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/airbus-cert__tree-sitter-powershell ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/albatrossSKY__tokenmin`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/albatrossSKY__tokenmin`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/albatrossSKY__tokenmin/src/languages/mod.rs`; scan counts include rust_files=11, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
pub mod rust;
pub mod python;
pub mod javascript;
pub mod go;
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/albatrossSKY__tokenmin/src/languages/mod.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/albatrossSKY__tokenmin ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/alexmozaidze__tree-sitter-fennel`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/alexmozaidze__tree-sitter-fennel`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/alexmozaidze__tree-sitter-fennel/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/alexmozaidze__tree-sitter-fennel/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/alexmozaidze__tree-sitter-fennel ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aptos-labs__tree-sitter-move-on-aptos`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aptos-labs__tree-sitter-move-on-aptos`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aptos-labs__tree-sitter-move-on-aptos/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aptos-labs__tree-sitter-move-on-aptos/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aptos-labs__tree-sitter-move-on-aptos ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/asgerf__dts-tree-sitter`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/asgerf__dts-tree-sitter`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/asgerf__dts-tree-sitter/examples/javascript/tree-sitter-javascript-typing.d.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
// We just need to tell TypeScript that this module exists.
declare module 'tree-sitter-javascript' {}
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/asgerf__dts-tree-sitter/examples/javascript/tree-sitter-javascript-typing.d.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/asgerf__dts-tree-sitter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/awsum-lang__tree-sitter-awsum`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/awsum-lang__tree-sitter-awsum`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/awsum-lang__tree-sitter-awsum/src/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/awsum-lang__tree-sitter-awsum/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/awsum-lang__tree-sitter-awsum ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bennypowers__nvim-regexplainer`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bennypowers__nvim-regexplainer`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bennypowers__nvim-regexplainer/queries/c_sharp/regexplainer.scm`; scan counts include rust_files=1, cargo_manifests=0, tree_sitter_query_files=19, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```scheme
; new Regex("...") or new Regex(@"...")
(object_creation_expression
  type: (identifier) @_type
  arguments: (argument_list .
    (argument
      [(string_literal) @regexplainer.string_pattern
       (verbatim_string_literal) @regexplainer.string_pattern]))
  (#eq? @_type "Regex"))

; Regex.IsMatch / Regex.Match / Regex.Matches / Regex.Replace / Regex.Split
(invocation_expression
  function: (member_access_expression
    expression: (identifier) @_type
    name: (identifier) @_method)
  arguments: (argument_list
    (argument
      [(string_literal) @regexplainer.string_pattern
       (verbatim_string_literal) @regexplainer.string_pattern]))
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bennypowers__nvim-regexplainer/queries/c_sharp/regexplainer.scm` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bennypowers__nvim-regexplainer ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/brianp__tree-sitter-aster`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/brianp__tree-sitter-aster`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/brianp__tree-sitter-aster/src/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=4, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/brianp__tree-sitter-aster/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/brianp__tree-sitter-aster ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/camdencheek__tree-sitter-dockerfile`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/camdencheek__tree-sitter-dockerfile`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/camdencheek__tree-sitter-dockerfile/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/camdencheek__tree-sitter-dockerfile/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/camdencheek__tree-sitter-dockerfile ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cathaysia__tree-sitter-jinja`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cathaysia__tree-sitter-jinja`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cathaysia__tree-sitter-jinja/tree-sitter-jinja/Cargo.toml`; scan counts include rust_files=4, cargo_manifests=2, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
[package]
name = "tree-sitter-jinja"
description = "Jinja grammar for tree-sitter"
version = "0.13.0"
license = "Apache-2.0"
readme = "../README.md"
keywords = ["incremental", "parsing", "tree-sitter", "jinja"]
categories = ["parsing", "text-editors"]
repository = "https://github.com/cathaysia/tree-sitter-jinja"
edition = "2021"
autoexamples = false

build = "bindings/rust/build.rs"
include = ["bindings/rust/*", "grammar.js", "queries/*", "src/*"]

[lib]
path = "bindings/rust/lib.rs"

```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cathaysia__tree-sitter-jinja/tree-sitter-jinja/Cargo.toml` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cathaysia__tree-sitter-jinja ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cmillstead__codesight-mcp`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cmillstead__codesight-mcp`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cmillstead__codesight-mcp/_bmad/core/agents/bmad-master.md`; scan counts include rust_files=1, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
---
name: "bmad master"
description: "BMad Master Executor, Knowledge Custodian, and Workflow Orchestrator"
---

You must fully embody this agent's persona and follow all activation instructions exactly as specified. NEVER break character until given an exit command.

```xml
<agent id="bmad-master.agent.yaml" name="BMad Master" title="BMad Master Executor, Knowledge Custodian, and Workflow Orchestrator" icon="🧙" capabilities="runtime resource management, workflow orchestration, task execution, knowledge custodian">
<activation critical="MANDATORY">
      <step n="1">Load persona from this current agent file (already in context)</step>
      <step n="2">🚨 IMMEDIATE ACTION REQUIRED - BEFORE ANY OUTPUT:
          - Load and read {project-root}/_bmad/core/config.yaml NOW
          - Store ALL fields as session variables: {user_name}, {communication_language}, {output_folder}
          - VERIFY: If config not loaded, STOP and report error to user
          - DO NOT PROCEED to step 3 until config is successfully loaded and variables stored
      </step>
      <step n="3">Remember: user's name is {user_name}</step>
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cmillstead__codesight-mcp/_bmad/core/agents/bmad-master.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cmillstead__codesight-mcp ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/comby-tools__comby`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/comby-tools__comby`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/comby-tools__comby/docs/third-party-licenses/bisect_ppx/LICENSE.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
Copyright © 2008-2021 Xavier Clerc, Leonid Rozenberg, Anton Bachin

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the “Software”), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/comby-tools__comby/docs/third-party-licenses/bisect_ppx/LICENSE.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/comby-tools__comby ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cpkio__tree-sitter-asciidoc`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cpkio__tree-sitter-asciidoc`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cpkio__tree-sitter-asciidoc/src/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cpkio__tree-sitter-asciidoc/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cpkio__tree-sitter-asciidoc ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cursorless-dev__vscode-parse-tree`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cursorless-dev__vscode-parse-tree`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cursorless-dev__vscode-parse-tree`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
N/A: no source file selected during bounded scan.
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cursorless-dev__vscode-parse-tree ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` if this repo changes later.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dchinmay2__nvim-ts-rainbow`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dchinmay2__nvim-ts-rainbow`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dchinmay2__nvim-ts-rainbow/queries/angle/parens.scm`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=66, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```scheme
"<" @left
">" @right
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dchinmay2__nvim-ts-rainbow/queries/angle/parens.scm` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dchinmay2__nvim-ts-rainbow ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/djacobsmeyer__repomap-go`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/djacobsmeyer__repomap-go`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/djacobsmeyer__repomap-go/internal/parser/markdown_test.go`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
package parser

import (
	"os"
	"path/filepath"
	"testing"
)

// writeMD writes a markdown file under root and returns its relpath.
func writeMD(t *testing.T, root, rel, body string) string {
	t.Helper()
	abs := filepath.Join(root, rel)
	if err := os.MkdirAll(filepath.Dir(abs), 0o755); err != nil {
		t.Fatal(err)
	}
	if err := os.WriteFile(abs, []byte(body), 0o644); err != nil {
		t.Fatal(err)
	}
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/djacobsmeyer__repomap-go/internal/parser/markdown_test.go` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/djacobsmeyer__repomap-go ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dooosp__ghostcode-auditor`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dooosp__ghostcode-auditor`; scan counts include file_count=32, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dooosp__ghostcode-auditor ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/elara-labs__code-context-engine`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/elara-labs__code-context-engine`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/elara-labs__code-context-engine/benchmarks/results/fastapi.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
# Benchmark: fastapi

**Date:** 2026-05-01
**Project:** fastapi (53 files, 179,794 tokens)
**Index:** 425 chunks from 53 files in 12.1s

## Results Summary

| Metric | Value |
|--------|-------|
| Retrieval savings | **94.1%** (full files → relevant chunks) |
| Compression savings | **89.4%** (chunks → signatures) |
| Combined | **99.4%** (full files → compressed chunks) |
| Avg full-file baseline | 83,681 tokens/query |
| Avg after retrieval | 4,927 tokens/query |
| Avg after compression | 523 tokens/query |
| Precision@10 | 0.24 |
| Recall@10 | 0.90 |
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/elara-labs__code-context-engine/benchmarks/results/fastapi.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/elara-labs__code-context-engine ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/emacs-tree-sitter__ts-fold`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/emacs-tree-sitter__ts-fold`; scan counts include file_count=23, rust_files=0, cargo_manifests=0, candidate_paths=2.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/emacs-tree-sitter__ts-fold ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ethan-leba__tree-edit`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ethan-leba__tree-edit`; scan counts include file_count=25, rust_files=0, cargo_manifests=0, candidate_paths=2.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ethan-leba__tree-edit ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/fl0w1nd__repomap-mcp`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/fl0w1nd__repomap-mcp`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/fl0w1nd__repomap-mcp/queries/tree-sitter-language-pack/arduino-tags.scm`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=56, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```scheme
(function_declarator
  declarator: (identifier) @name.definition.function) @definition.function

(call_expression
  function: (identifier) @name.reference.call) @reference.call
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/fl0w1nd__repomap-mcp/queries/tree-sitter-language-pack/arduino-tags.scm` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/fl0w1nd__repomap-mcp ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/folke__twilight.nvim`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/folke__twilight.nvim`; scan counts include file_count=25, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/folke__twilight.nvim ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/gbprod__tree-sitter-gitcommit`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/gbprod__tree-sitter-gitcommit`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/gbprod__tree-sitter-gitcommit/bindings/c/tree-sitter-gitcommit.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_GITCOMMIT_H_
#define TREE_SITTER_GITCOMMIT_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_gitcommit(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_GITCOMMIT_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/gbprod__tree-sitter-gitcommit/bindings/c/tree-sitter-gitcommit.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/gbprod__tree-sitter-gitcommit ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/github__semantic`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/github__semantic`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/github__semantic/docs/why-tree-sitter.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
# How we parse source code into ASTs

#### Table of Contents
1. [Problem space and possible solutions](#problem-space-and-possible-solutions)
2. [Why we use tree-sitter](#why-we-use-tree-sitter)
3. [Drawbacks of tree-sitter](#drawbacks-of-tree-sitter)

## Problem space and possible solutions

Parsing is a well studied problem and there are known trade-offs in the design space. Grammar development often requires seeing beyond the parser generator abstraction and understanding the implementation context. For the context of the Semantic Code team, transforming source code into ASTs via parsing and semantic modeling is necessary to support our work in program analysis and to generate semantic diffs.

To serve these goals, the following options were considered alongside `tree-sitter`:

- Use existing language parsers (maybe run them in docker containers).
- Join in with another open source effort like [Babelfish](https://doc.bblf.sh/).
- Write our own parsers (perhaps directly in Haskell).
- Write our own parsers (perhaps based on language parsers) in something like [Yacc](https://en.wikipedia.org/wiki/Yacc), [Bison](https://www.gnu.org/software/bison/), [ANTLR](http://www.antlr.org/).
- Use [tree-sitter](https://github.com/tree-sitter/tree-sitter).
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/github__semantic/docs/why-tree-sitter.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/github__semantic ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/glyphtrail__glyphtrail`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/glyphtrail__glyphtrail`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/glyphtrail__glyphtrail/crates/glyphtrail-parse/queries/bash.scm`; scan counts include rust_files=100, cargo_manifests=10, tree_sitter_query_files=23, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```scheme
; Definitions
(function_definition name: (word) @name) @def.function

; Calls — the command word in a simple command (function/command invocation)
(command_name (word) @call)

; Comments
(comment) @comment
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/glyphtrail__glyphtrail/crates/glyphtrail-parse/queries/bash.scm` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/glyphtrail__glyphtrail ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/grantjenks__py-tree-sitter-languages`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/grantjenks__py-tree-sitter-languages`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/grantjenks__py-tree-sitter-languages/tests/test_tree_sitter_languages.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
from tree_sitter_languages import get_language, get_parser

LANGUAGES = [
    'bash',
    'c',
    'c_sharp',  # c-sharp
    'commonlisp',
    'cpp',
    'css',
    'dockerfile',
    'dot',
    'elisp',
    'elixir',
    'elm',
    'embedded_template',  # embedded-template
    'erlang',
    'fixed_form_fortran',
    'fortran',
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/grantjenks__py-tree-sitter-languages/tests/test_tree_sitter_languages.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/grantjenks__py-tree-sitter-languages ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hesnotsoharry__codebase-graph-mcp`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hesnotsoharry__codebase-graph-mcp`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hesnotsoharry__codebase-graph-mcp/dist/cypherEngineParser.d.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
/**
 * cypherEngineParser.ts — Clause extraction and WHERE/ORDER BY parsing helpers
 * extracted from CypherEngine class methods.
 *
 * All functions are pure (no class state). They transform query strings into
 * structured types defined in cypherEngineSupport.ts.
 */
import type { OrderByClause, WhereCondition } from './cypherEngineSupport';
/**
 * Throw a clear error if the query contains a top-level clause that the engine
 * does not support. OPTIONAL MATCH and UNWIND are handled by dedicated parse paths.
 * WITH is supported as a single-stage passthrough pipe (Wave 1 Phase 2).
 */
export declare function assertNoUnsupportedClauses(_query: string): void;
/** Extract the content of a named clause from the query string. */
export declare function extractClause(query: string, clause: string): string | null;
/** Extract the OPTIONAL MATCH clause content, or null if absent. */
export declare function extractOptionalMatchClause(query: string): string | null;
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hesnotsoharry__codebase-graph-mcp/dist/cypherEngineParser.d.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hesnotsoharry__codebase-graph-mcp ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hzj-Jeff-07__AI-CodeGuard`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hzj-Jeff-07__AI-CodeGuard`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hzj-Jeff-07__AI-CodeGuard/src/parser/tree-sitter/languages.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
const require = createRequire(import.meta.url);
const packageRoot = findPackageRoot(dirname(fileURLToPath(import.meta.url)));

const BUNDLED_CORE_WASM_PATH = join(packageRoot, 'dist', 'tree-sitter', 'web-tree-sitter.wasm');
const BUNDLED_GRAMMAR_WASM_PATHS: Record<Language, string> = {
  javascript: join(packageRoot, 'dist', 'tree-sitter', 'tree-sitter-javascript.wasm'),
  typescript: join(packageRoot, 'dist', 'tree-sitter', 'tree-sitter-tsx.wasm'),
  python: join(packageRoot, 'dist', 'tree-sitter', 'tree-sitter-python.wasm'),
  go: join(packageRoot, 'dist', 'tree-sitter', 'tree-sitter-go.wasm'),
  java: join(packageRoot, 'dist', 'tree-sitter', 'tree-sitter-java.wasm'),
  php: join(packageRoot, 'dist', 'tree-sitter', 'tree-sitter-php.wasm'),
};

const FALLBACK_GRAMMAR_WASM_PATHS: Record<Language, string> = {
  javascript: require.resolve('tree-sitter-javascript/tree-sitter-javascript.wasm'),
  typescript: require.resolve('tree-sitter-typescript/tree-sitter-tsx.wasm'),
  python: require.resolve('tree-sitter-python/tree-sitter-python.wasm'),
  go: require.resolve('tree-sitter-go/tree-sitter-go.wasm'),
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hzj-Jeff-07__AI-CodeGuard/src/parser/tree-sitter/languages.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hzj-Jeff-07__AI-CodeGuard ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ikatyang__tree-sitter-vue`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ikatyang__tree-sitter-vue`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ikatyang__tree-sitter-vue/src/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

typedef uint16_t TSStateId;

#ifndef TREE_SITTER_API_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ikatyang__tree-sitter-vue/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ikatyang__tree-sitter-vue ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/intersystems__tree-sitter-objectscript`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/intersystems__tree-sitter-objectscript`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/intersystems__tree-sitter-objectscript/bindings/python/tree_sitter_objectscript/queries/__init__.py`; scan counts include rust_files=6, cargo_manifests=3, tree_sitter_query_files=29, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
N/A: selected file was empty.
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/intersystems__tree-sitter-objectscript/bindings/python/tree_sitter_objectscript/queries/__init__.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/intersystems__tree-sitter-objectscript ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jhillacre__tree-sitter-ic10-typed`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jhillacre__tree-sitter-ic10-typed`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jhillacre__tree-sitter-ic10-typed/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jhillacre__tree-sitter-ic10-typed/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jhillacre__tree-sitter-ic10-typed ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jlcrochet__tree-sitter-html`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jlcrochet__tree-sitter-html`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jlcrochet__tree-sitter-html/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jlcrochet__tree-sitter-html/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jlcrochet__tree-sitter-html ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/joernio__joern`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/joernio__joern`; scan counts include file_count=2190, rust_files=0, cargo_manifests=0, candidate_paths=80.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/joernio__joern ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/josteink__tree-sitter-structurizr`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/josteink__tree-sitter-structurizr`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/josteink__tree-sitter-structurizr/bindings/c/tree-sitter-structurizr.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_STRUCTURIZR_H_
#define TREE_SITTER_STRUCTURIZR_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_structurizr(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_STRUCTURIZR_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/josteink__tree-sitter-structurizr/bindings/c/tree-sitter-structurizr.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/josteink__tree-sitter-structurizr ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kcl-lang__tree-sitter-kcl`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kcl-lang__tree-sitter-kcl`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kcl-lang__tree-sitter-kcl/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kcl-lang__tree-sitter-kcl/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kcl-lang__tree-sitter-kcl ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kristoferssolo__tree-sitter-bruno`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kristoferssolo__tree-sitter-bruno`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kristoferssolo__tree-sitter-bruno/bindings/c/tree_sitter/tree-sitter-bruno.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=5, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_BRUNO_H_
#define TREE_SITTER_BRUNO_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_bruno(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_BRUNO_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kristoferssolo__tree-sitter-bruno/bindings/c/tree_sitter/tree-sitter-bruno.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kristoferssolo__tree-sitter-bruno ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/langston-barrett__tree-sitter-edit`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/langston-barrett__tree-sitter-edit`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/langston-barrett__tree-sitter-edit/src/lib.rs`; scan counts include rust_files=10, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```rust
//! tree-sitter-edit is a crate for printing modified tree-sitter parse trees,
//! intended for use in multi-language code refactoring, linting, or
//! modification (codemod) tools.

mod editor;
mod editors;
mod id;
mod print;
mod traversal;

pub use editor::*;
pub use editors::*;
pub use id::*;
pub use print::*;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/langston-barrett__tree-sitter-edit/src/lib.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/langston-barrett__tree-sitter-edit ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/leandrocp__mdex`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/leandrocp__mdex`; scan counts include file_count=83, rust_files=0, cargo_manifests=0, candidate_paths=5.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/leandrocp__mdex ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lkwslm__tree-sitter-mcp-code-analyzer`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lkwslm__tree-sitter-mcp-code-analyzer`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lkwslm__tree-sitter-mcp-code-analyzer/src/core/base_parser.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
"""
核心解析器模块
定义了tree-sitter解析器的抽象基类和通用功能
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional, Tuple
import tree_sitter
from pathlib import Path
import logging

class CodeNode:
    """代码节点类，表示代码结构中的一个元素"""

    def __init__(self,
                 node_type: str,
                 name: str,
                 start_line: int,
                 end_line: int,
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lkwslm__tree-sitter-mcp-code-analyzer/src/core/base_parser.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lkwslm__tree-sitter-mcp-code-analyzer ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/marceline-cramer__tree-sitter-grain`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/marceline-cramer__tree-sitter-grain`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/marceline-cramer__tree-sitter-grain/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

typedef uint16_t TSStateId;

#ifndef TREE_SITTER_API_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/marceline-cramer__tree-sitter-grain/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/marceline-cramer__tree-sitter-grain ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/merico-ai__tree-sitter-objc`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/merico-ai__tree-sitter-objc`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/merico-ai__tree-sitter-objc/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

typedef uint16_t TSStateId;

#ifndef TREE_SITTER_API_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/merico-ai__tree-sitter-objc/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/merico-ai__tree-sitter-objc ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mitchellh__tree-sitter-proto`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mitchellh__tree-sitter-proto`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mitchellh__tree-sitter-proto/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

typedef uint16_t TSStateId;

#ifndef TREE_SITTER_API_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mitchellh__tree-sitter-proto/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mitchellh__tree-sitter-proto ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/move-hub__tree-sitter-move`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/move-hub__tree-sitter-move`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/move-hub__tree-sitter-move/src/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSSymbol;
typedef uint16_t TSFieldId;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/move-hub__tree-sitter-move/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/move-hub__tree-sitter-move ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/n24q02m__better-code-review-graph`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/n24q02m__better-code-review-graph`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/n24q02m__better-code-review-graph/src/better_code_review_graph/parser.py`; scan counts include rust_files=1, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
"""Tree-sitter based multi-language code parser.

Extracts structural nodes (classes, functions, imports, types) and edges
(calls, inheritance, contains) from source files.
"""

from __future__ import annotations

import hashlib
import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, cast

import tree_sitter_language_pack as tslp

if TYPE_CHECKING:
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/n24q02m__better-code-review-graph/src/better_code_review_graph/parser.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/n24q02m__better-code-review-graph ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nendotools__tree-sitter-mcp`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nendotools__tree-sitter-mcp`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nendotools__tree-sitter-mcp/src/analysis/syntax.ts`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
/**
 * Syntax error analysis using tree-sitter error nodes
 */

import type { Project } from '../types/core.js'
import type { Finding, SyntaxMetrics } from '../types/analysis.js'
import { countErrorNodes } from './errors.js'

export interface SyntaxError {
  file: string
  line: number
  column: number
  endLine: number
  endColumn: number
  message: string
  errorType: string
  context: string
}
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nendotools__tree-sitter-mcp/src/analysis/syntax.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nendotools__tree-sitter-mcp ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nick79__diffguard`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nick79__diffguard`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nick79__diffguard/src/diffguard/ast/__init__.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
"""AST parsing and language detection for diffguard."""

from __future__ import annotations

from typing import TYPE_CHECKING

from diffguard.ast.languages import Language, detect_language
from diffguard.ast.parser import clear_parser_cache, get_parser, parse_file
from diffguard.ast.python import Import
from diffguard.ast.scope import Scope, extract_scope_context, find_enclosing_scope

if TYPE_CHECKING:
    from pathlib import Path

    from tree_sitter import Tree

__all__ = [
    "Import",
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nick79__diffguard/src/diffguard/ast/__init__.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nick79__diffguard ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/njenia__envgrd`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/njenia__envgrd`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/njenia__envgrd/internal/envfile/parsers.go`; scan counts include rust_files=1, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
	return "env"
}

// parseEnvrc parses direnv .envrc files
// Supports: export VAR=value
func parseEnvrc(path string) (map[string]string, error) {
	vars := make(map[string]string)

	file, err := os.Open(path)
	if err != nil {
		if os.IsNotExist(err) {
			return vars, nil
		}
		return nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/njenia__envgrd/internal/envfile/parsers.go` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/njenia__envgrd ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nvim-treesitter__nvim-treesitter`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nvim-treesitter__nvim-treesitter`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nvim-treesitter__nvim-treesitter/runtime/queries/ada/folds.scm`; scan counts include rust_files=19, cargo_manifests=0, tree_sitter_query_files=1182, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```scheme
; Support for folding in Ada
;    za     toggles folding a package, subprogram, if statement or loop
[
  (package_declaration)
  (generic_package_declaration)
  (package_body)
  (subprogram_body)
  (block_statement)
  (if_statement)
  (loop_statement)
  (gnatprep_declarative_if_statement)
  (gnatprep_if_statement)
] @fold
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nvim-treesitter__nvim-treesitter/runtime/queries/ada/folds.scm` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nvim-treesitter__nvim-treesitter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/omarjatoi__tree-sitter-flix`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/omarjatoi__tree-sitter-flix`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/omarjatoi__tree-sitter-flix/bindings/c/tree_sitter/tree-sitter-flix.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=4, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_FLIX_H_
#define TREE_SITTER_FLIX_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_flix(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_FLIX_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/omarjatoi__tree-sitter-flix/bindings/c/tree_sitter/tree-sitter-flix.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/omarjatoi__tree-sitter-flix ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/opengrep__opengrep`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/opengrep__opengrep`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/opengrep__opengrep/cli/src/semdep/parsers/__init__.py`; scan counts include rust_files=79, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
N/A: selected file was empty.
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/opengrep__opengrep/cli/src/semdep/parsers/__init__.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/opengrep__opengrep ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/palmcivet__kiwi-vscode`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/palmcivet__kiwi-vscode`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/palmcivet__kiwi-vscode/prettier-plugin-kiwi/test/tree-sitter-parser.test.ts`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
import { strict as assert } from 'node:assert';
import * as fs from 'node:fs';
import * as path from 'node:path';
import Parser from 'tree-sitter';
import Kiwi from 'tree-sitter-kiwi';
import { FIXTURES_PATH } from './utils';

describe('tree-sitter parser', () => {
  let parser: Parser;

  before(async () => {
    parser = new Parser();
    parser.setLanguage(Kiwi);
  });

  it('should parse kiwi file correctly', () => {
    const testFilePath = path.join(FIXTURES_PATH, 'space.kiwi');
    assert.ok(fs.existsSync(testFilePath), 'test file not found');
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/palmcivet__kiwi-vscode/prettier-plugin-kiwi/test/tree-sitter-parser.test.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/palmcivet__kiwi-vscode ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pmd__pmd`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pmd__pmd`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pmd__pmd/docs/pages/pmd/projectdocs/committers/infrastructure.md`; scan counts include rust_files=1, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
---
title: Infrastructure
permalink: pmd_projectdocs_committers_infrastructure.html
author: Andreas Dangel <andreas.dangel@pmd-code.org>
last_updated: February 2025 (7.11.0)
---

This page describes, which infrastructure and services is used by the pmd project.

## GitHub

The main repository is hosted on <https://github.com/pmd>. We own the organization "pmd".

*   source code in git repositories
*   releases
*   issue tracker
*   discussions
*   pull requests
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pmd__pmd/docs/pages/pmd/projectdocs/committers/infrastructure.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pmd__pmd ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pssgowtham__codereviewer`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pssgowtham__codereviewer`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pssgowtham__codereviewer/src/codereviewer/parsing/ast_parser.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
"""Tree-sitter AST parsing for Python, JavaScript, Go, Java.

Extracts structural facts (functions, classes, imports, call sites) that we feed
to the review agent alongside the raw diff. Grounding reviews in AST structure
avoids hallucinated line numbers and missed edits.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from tree_sitter_languages import get_parser

LANGUAGES = {
    ".py": "python",
    ".js": "javascript",
    ".jsx": "javascript",
    ".ts": "typescript",
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pssgowtham__codereviewer/src/codereviewer/parsing/ast_parser.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pssgowtham__codereviewer ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ralscha__tree-sitter-mcp`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ralscha__tree-sitter-mcp`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ralscha__tree-sitter-mcp/internal/models/ast.go`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
// Package models provides data types for ASTs and related entities.
package models

import (
	"strings"

	sitter "github.com/tree-sitter/go-tree-sitter"
)

// NodeToMap converts a tree-sitter node to a map representation.
func NodeToMap(node *sitter.Node, sourceBytes []byte, includeChildren bool, includeText bool, maxDepth int) map[string]any {
	if node == nil {
		return nil
	}

	sp := node.StartPosition()
	ep := node.EndPosition()

```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ralscha__tree-sitter-mcp/internal/models/ast.go` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ralscha__tree-sitter-mcp ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/reybits__ts-forge.nvim`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/reybits__ts-forge.nvim`; scan counts include file_count=6, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/reybits__ts-forge.nvim ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rmuir__tree-sitter-javadoc`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rmuir__tree-sitter-javadoc`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rmuir__tree-sitter-javadoc/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rmuir__tree-sitter-javadoc/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rmuir__tree-sitter-javadoc ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/s0__tree-sitter-hast`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/s0__tree-sitter-hast`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/s0__tree-sitter-hast/src/hast.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
/**
 * Typescript implementation of the spec here: https://github.com/syntax-tree/hast
 *
 * TODO: Move this to DefinitelyTyped
 */

import * as Unist from 'unist';

export interface Parent extends Unist.Parent {
  children: (Element | Doctype | Comment | Text)[];
}

export interface Literal extends Unist.Literal {
  value: string;
}

export interface Root extends Parent {
  type: 'root';
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/s0__tree-sitter-hast/src/hast.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/s0__tree-sitter-hast ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/salesforce__CodeTF`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/salesforce__CodeTF`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/salesforce__CodeTF/codetf/code_utility/ast_parser.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import re
from typing import List, Dict, Any, Set, Optional
import logging
from tree_sitter import Parser, Language
import os
import platform
from pathlib import Path
DOCSTRING_REGEX_TOKENIZER = re.compile(r"[^\s,'\"`.():\[\]=*;>{\}+-/\\]+|\\+|\.+|\(\)|{\}|\[\]|\(+|\)+|:+|\[+|\]+|{+|\}+|=+|\*+|;+|>+|\++|-+|/+")


def tokenize_docstring(docstring: str) -> List[str]:
    return [t for t in DOCSTRING_REGEX_TOKENIZER.findall(docstring) if t is not None and len(t) > 0]


def tokenize_code(node, blob: str, nodes_to_exclude: Optional[Set]=None) -> List:
    tokens = []
    traverse(node, tokens)
    return [match_from_span(token, blob) for token in tokens if nodes_to_exclude is None or token not in nodes_to_exclude]
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/salesforce__CodeTF/codetf/code_utility/ast_parser.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/salesforce__CodeTF ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/scip-code__scip-java`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/scip-code__scip-java`; scan counts include file_count=315, rust_files=0, cargo_manifests=0, candidate_paths=4.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/scip-code__scip-java ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/semgrep__semgrep`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/semgrep__semgrep`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/semgrep__semgrep/cli/src/semdep/parsers/__init__.py`; scan counts include rust_files=69, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
N/A: selected file was empty.
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/semgrep__semgrep/cli/src/semdep/parsers/__init__.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/semgrep__semgrep ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/simonbs__Runestone`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/simonbs__Runestone`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/simonbs__Runestone/Example/Languages/Sources/TreeSitterJavaScript/src/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=8, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

typedef uint16_t TSStateId;

#ifndef TREE_SITTER_API_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/simonbs__Runestone/Example/Languages/Sources/TreeSitterJavaScript/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/simonbs__Runestone ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/smpanaro__tree-sitter-flatbuffers`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/smpanaro__tree-sitter-flatbuffers`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/smpanaro__tree-sitter-flatbuffers/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/smpanaro__tree-sitter-flatbuffers/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/smpanaro__tree-sitter-flatbuffers ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcegraph__scip-clang`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcegraph__scip-clang`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcegraph__scip-clang/indexer/AstConsumer.cc`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
#include "absl/container/flat_hash_set.h"
#include "perfetto/perfetto.h"

#include "clang/AST/DeclCXX.h"
#include "clang/AST/RecursiveASTVisitor.h"
#include "clang/AST/TypeLoc.h"
#include "clang/Basic/SourceLocation.h"
#include "clang/Sema/Sema.h"

#include "indexer/AstConsumer.h"
#include "indexer/IdPathMappings.h"
#include "indexer/Indexer.h"
#include "indexer/LlvmAdapter.h"
#include "indexer/Preprocessing.h"
#include "indexer/SymbolFormatter.h"
#include "indexer/Tracing.h"

namespace scip_clang {
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcegraph__scip-clang/indexer/AstConsumer.cc` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcegraph__scip-clang ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/spiritengine__wale`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/spiritengine__wale`; scan counts include file_count=15, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/spiritengine__wale ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/stadelmanma__tree-sitter-fortran`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/stadelmanma__tree-sitter-fortran`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/stadelmanma__tree-sitter-fortran/bindings/c/tree-sitter-fortran.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=5, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_FORTRAN_H_
#define TREE_SITTER_FORTRAN_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_fortran(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_FORTRAN_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/stadelmanma__tree-sitter-fortran/bindings/c/tree-sitter-fortran.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/stadelmanma__tree-sitter-fortran ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sunny-chung__ktreesitter-json`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sunny-chung__ktreesitter-json`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sunny-chung__ktreesitter-json`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
N/A: no source file selected during bounded scan.
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sunny-chung__ktreesitter-json ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` if this repo changes later.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/taeezx44__ai-td-detector`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/taeezx44__ai-td-detector`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/taeezx44__ai-td-detector/engine/parsers/tree_sitter_parser.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
"""
Tree-sitter based code parser for AI-TD Detector

Supports multiple programming languages and provides AST-based analysis.
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

# Tree-sitter imports
try:
    import tree_sitter
except ImportError:
    print("Warning: tree_sitter not installed. Some features may not work.")
    tree_sitter = None

```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/taeezx44__ai-td-detector/engine/parsers/tree_sitter_parser.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/taeezx44__ai-td-detector ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/the-mikedavis__tree-sitter-git-config`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/the-mikedavis__tree-sitter-git-config`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/the-mikedavis__tree-sitter-git-config/src/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/the-mikedavis__tree-sitter-git-config/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/the-mikedavis__tree-sitter-git-config ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tlaplus-community__tree-sitter-tlaplus`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tlaplus-community__tree-sitter-tlaplus`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tlaplus-community__tree-sitter-tlaplus/bindings/c/tree-sitter-tlaplus.h`; scan counts include rust_files=3, cargo_manifests=2, tree_sitter_query_files=6, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_TLAPLUS_H_
#define TREE_SITTER_TLAPLUS_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_tlaplus(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_TLAPLUS_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tlaplus-community__tree-sitter-tlaplus/bindings/c/tree-sitter-tlaplus.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tlaplus-community__tree-sitter-tlaplus ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-grammars__tree-sitter-diff`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-grammars__tree-sitter-diff`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-grammars__tree-sitter-diff/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-grammars__tree-sitter-diff/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-grammars__tree-sitter-diff ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-perl__tree-sitter-perl`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-perl__tree-sitter-perl`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-perl__tree-sitter-perl/bindings/c/tree_sitter/tree-sitter-perl.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=5, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PERL_H_
#define TREE_SITTER_PERL_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_perl(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_PERL_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-perl__tree-sitter-perl/bindings/c/tree_sitter/tree-sitter-perl.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-perl__tree-sitter-perl ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__haskell-tree-sitter`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__haskell-tree-sitter`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__haskell-tree-sitter/tree-sitter-c-sharp/ChangeLog.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
# v0.1.0.0

* add tree-sitter-c-sharp parser
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__haskell-tree-sitter/tree-sitter-c-sharp/ChangeLog.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__haskell-tree-sitter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__parser-setup-action`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__parser-setup-action`; scan counts include file_count=4, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__parser-setup-action ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-cpp`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-cpp`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-cpp/bindings/c/tree-sitter-cpp.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_CPP_H_
#define TREE_SITTER_CPP_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_cpp(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_CPP_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-cpp/bindings/c/tree-sitter-cpp.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-cpp ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-haskell`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-haskell`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-haskell/bindings/c/tree-sitter-haskell.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_HASKELL_H_
#define TREE_SITTER_HASKELL_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_haskell(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_HASKELL_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-haskell/bindings/c/tree-sitter-haskell.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-haskell ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-julia`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-julia`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-julia/bindings/c/tree_sitter/tree-sitter-julia.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_JULIA_H_
#define TREE_SITTER_JULIA_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_julia(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_JULIA_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-julia/bindings/c/tree_sitter/tree-sitter-julia.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-julia ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-regex`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-regex`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-regex/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-regex/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-regex ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-typescript`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-typescript`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-typescript/bindings/c/tree-sitter-tsx.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_TSX_H_
#define TREE_SITTER_TSX_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_tsx(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_TSX_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-typescript/bindings/c/tree-sitter-tsx.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-typescript ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/uncenter__tree-sitter-tera`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/uncenter__tree-sitter-tera`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/uncenter__tree-sitter-tera/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/uncenter__tree-sitter-tera/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/uncenter__tree-sitter-tera ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/urbit-pilled__tree-sitter-hoon`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/urbit-pilled__tree-sitter-hoon`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/urbit-pilled__tree-sitter-hoon/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/urbit-pilled__tree-sitter-hoon/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/urbit-pilled__tree-sitter-hoon ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vigoux__tree-sitter-viml`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vigoux__tree-sitter-viml`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vigoux__tree-sitter-viml/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

typedef uint16_t TSStateId;

#ifndef TREE_SITTER_API_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vigoux__tree-sitter-viml/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vigoux__tree-sitter-viml ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vovasilenko__copycara`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vovasilenko__copycara`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vovasilenko__copycara/src/ignore.rs`; scan counts include rust_files=15, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
impl IgnoreRules {
    pub fn load() -> Self {
        let content = fs::read_to_string(IGNORE_FILE).unwrap_or_else(|_| DEFAULT_RULES.to_string());
        Self::parse(&content)
    }

    fn parse(content: &str) -> Self {
        let patterns = content
            .lines()
            .map(str::trim)
            .filter(|line| !line.is_empty() && !line.starts_with('#'))
            .map(str::to_string)
            .collect();

        Self { patterns }
    }

    pub fn is_ignored(&self, path: &Path) -> bool {
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vovasilenko__copycara/src/ignore.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vovasilenko__copycara ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/win4r__codebase-memory-mcp-pro`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/win4r__codebase-memory-mcp-pro`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/win4r__codebase-memory-mcp-pro/internal/cbm/vendored/common/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/win4r__codebase-memory-mcp-pro/internal/cbm/vendored/common/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/win4r__codebase-memory-mcp-pro ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/xberg-io__tree-sitter-language-pack`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/xberg-io__tree-sitter-language-pack`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/xberg-io__tree-sitter-language-pack/.ai-rulez/domains/parser-compilation/context/tree-sitter-overview.md`; scan counts include rust_files=67, cargo_manifests=16, tree_sitter_query_files=9, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
priority: high
---

# Tree-Sitter Overview

Tree-sitter is an incremental parsing library that builds concrete syntax trees for source code.

Key concepts:

- **Grammar**: A JSON/JS definition describing a language's syntax
- **Parser**: C code generated from the grammar by `tree-sitter generate`
- **External Scanner**: Optional C/C++ code for context-sensitive parsing (e.g., indentation)
- **ABI Version**: Binary interface version for runtime compatibility
- **Language Pack**: A collection of pre-compiled parsers bundled for multi-language use

This project compiles 306 grammars into a single Rust crate with bindings for Python, Node.js, Ruby, PHP, Go, Java, JNI, C#, Elixir, WebAssembly, Dart, Kotlin Android, Swift, Zig, and C FFI.
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/xberg-io__tree-sitter-language-pack/.ai-rulez/domains/parser-compilation/context/tree-sitter-overview.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/xberg-io__tree-sitter-language-pack ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/z16166__RustLines`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/z16166__RustLines`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/z16166__RustLines/src/lib.rs`; scan counts include rust_files=5, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
pub mod counter;
pub mod test_detector;
pub mod walker;

pub use counter::{LineStats, LineKind, count_file, count_file_with_debug};
pub use walker::{walk_project, FilterConfig};
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/z16166__RustLines/src/lib.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/z16166__RustLines ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zeta1999__ocaml-tree-sitter`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zeta1999__ocaml-tree-sitter`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zeta1999__ocaml-tree-sitter/lang/c/grammar.js`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```javascript
/*
  Copied from https://github.com/tree-sitter/tree-sitter-c

The MIT License (MIT)

Copyright (c) 2014 Max Brunsfeld

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zeta1999__ocaml-tree-sitter/lang/c/grammar.js` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zeta1999__ocaml-tree-sitter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/pensieve2024`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/pensieve2024`; scan counts include file_count=4, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/pensieve2024 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/room-of-requirement`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.claude/skills/run-parseltongue-1-7-2/SKILL.md`; scan counts include rust_files=26, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
---
name: run-parseltongue-1-7-2
description: Install and run parseltongue 1.7.2 in an isolated user-space run folder, verify the actual bound server URL, and query a codebase through the HTTP API for orientation, entity lookup, forward and backward dependency tracing, blast radius, architecture scans, incremental reindexing, and higher-order graph workflows such as meet-in-the-middle debugging, safe refactoring, seam discovery, boundary audits, cycle breaking, migration choreography, and derived control-flow or data-flow investigations. Use when Codex must pin to version 1.7.2, needs graph-based code understanding, or must refresh an existing run folder without version drift.
---

## Room of Requirement Adaptation

- Public skill name: `run-parseltongue-1-7-2`.
- This skill is installed for the `room-of-requirement` repository.
- This repository is a Rust CLI that queries GitHub and stores repository search results in PostgreSQL for later analysis.
- Prefer explicit reasoning, idiomatic Rust, behavior-focused tests, and small verifiable edits that are easy to review.
- Read `CONTEXT.md`, `docs/agents/issue-tracker.md`, `docs/agents/triage-labels.md`, and `docs/agents/domain.md` before applying workflow-heavy advice.
- If the upstream guidance conflicts with the repository docs, the repository docs win.
- This skill was mirrored from the active Codex home skill catalog into `vendor/agent-skills/codex-home/` and exposed repo-locally for both Claude and Codex.


# Run Parseltongue 1.7.2

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.claude/skills/run-parseltongue-1-7-2/SKILL.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/lihengming__spring-boot-api-project-seed`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/lihengming__spring-boot-api-project-seed`; scan counts include file_count=26, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/lihengming__spring-boot-api-project-seed ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/spring-guides__gs-securing-web`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/spring-guides__gs-securing-web`; scan counts include file_count=70, rust_files=0, cargo_manifests=0, candidate_paths=4.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/spring-guides__gs-securing-web ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/sqshq__piggymetrics`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust-Adjacent Parser Reference From `personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/sqshq__piggymetrics`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/sqshq__piggymetrics/auth-service/src/main/java/com/piggymetrics/auth/service/security/MongoUserDetailsService.java`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```text

import com.piggymetrics.auth.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

@Service
public class MongoUserDetailsService implements UserDetailsService {

	@Autowired
	private UserRepository repository;

	@Override
	public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {

		return repository.findById(username).orElseThrow(()->new UsernameNotFoundException(username));
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/sqshq__piggymetrics/auth-service/src/main/java/com/piggymetrics/auth/service/security/MongoUserDetailsService.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/sqshq__piggymetrics ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/rustASCII`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/rustASCII`; scan counts include file_count=3, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/rustASCII ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/tweet_scrolls_convert_tool`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust Module Architecture Slice From `personal-repos-lane/tweet_scrolls_convert_tool`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/tweet_scrolls_convert_tool/src/lib.rs`; scan counts include rust_files=54, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```rust
//! Tweet-Scrolls: Twitter Archive JSON to CSV/TXT Processor
//!
//! This library provides functionality to process Twitter archive data, analyze interactions,
//! and generate meaningful insights from tweets and direct messages.

#![warn(missing_docs)]

pub mod models;
pub mod services;
pub mod utils;
pub mod processing;
pub mod relationship;
pub mod main_integration;
pub mod main_process;
pub mod cli;

// Re-exports for common types
pub use models::interaction::*;
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/tweet_scrolls_convert_tool/src/lib.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/tweet_scrolls_convert_tool ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/wandlorelabs2025`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/wandlorelabs2025`; scan counts include file_count=45, rust_files=0, cargo_manifests=0, candidate_paths=3.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/wandlorelabs2025 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/zztweetbook202408`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust Module Architecture Slice From `personal-repos-lane/zztweetbook202408`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/zztweetbook202408/p002_thread_extractor_202409v1/src/main.rs`; scan counts include rust_files=22, cargo_manifests=3, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```rust
version https://git-lfs.github.com/spec/v1
oid sha256:66d3f05619304d949475f0ec75f8b0e5d3e9f0f46ded95a4c034027177cdff13
size 9489
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/zztweetbook202408/p002_thread_extractor_202409v1/src/main.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/zztweetbook202408 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/aeneas`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `reference-repos-yard/aeneas`
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/aeneas/tests/src/cast_signed.rs`; scan counts include rust_files=97, cargo_manifests=3, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
N/A: could not read `/Users/amuldotexe/Desktop/reference-repos-yard/aeneas/tests/src/cast_signed.rs`: [Errno 2] No such file or directory: '/Users/amuldotexe/Desktop/reference-repos-yard/aeneas/tests/src/cast_signed.rs'
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/reference-repos-yard/aeneas/tests/src/cast_signed.rs` and run `git -C /Users/amuldotexe/Desktop/reference-repos-yard/aeneas ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/eurydice`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `reference-repos-yard/eurydice`
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/eurydice/out/test-castunsize/castunsize.c`; scan counts include rust_files=67, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text

 */

#include "castunsize.h"

typedef struct const_uint32_t__x2_s
{
  const uint32_t *fst;
  const uint32_t *snd;
}
const_uint32_t__x2;

void castunsize_main1(void)
{
  castunsize_S_f9 x = { .foo = 0U, .my_data = { .data = { 0U } } };
  Eurydice_dst_ref_shared_88 x0 = { .ptr = (const castunsize_T *)&x, .meta = (size_t)4U };
  /* original Rust expression is not an lvalue in C */
  uint32_t lvalue = 0U;
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/reference-repos-yard/eurydice/out/test-castunsize/castunsize.c` and run `git -C /Users/amuldotexe/Desktop/reference-repos-yard/eurydice ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/mempalace`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust-Adjacent Parser Reference From `reference-repos-yard/mempalace`
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/mempalace/tests/test_init_gitignore_protection.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```text
N/A: could not read `/Users/amuldotexe/Desktop/reference-repos-yard/mempalace/tests/test_init_gitignore_protection.py`: [Errno 2] No such file or directory: '/Users/amuldotexe/Desktop/reference-repos-yard/mempalace/tests/test_init_gitignore_protection.py'
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/reference-repos-yard/mempalace/tests/test_init_gitignore_protection.py` and run `git -C /Users/amuldotexe/Desktop/reference-repos-yard/mempalace ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.
