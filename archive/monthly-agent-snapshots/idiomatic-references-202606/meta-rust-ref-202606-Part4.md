# Meta Rust Reference 202606 Part 4

Purpose: encyclopedia-grade Rust reference extracted repo-by-repo from every Git repository under `/Users/amuldotexe/Desktop`, with special attention to tree-sitter, parser, compiler, graph, async, storage, FFI, CLI, testing, and architecture patterns.

Assigned repo slice: `meta-rust-ref-202606-Part4-repos.txt`

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

- `/Users/amuldotexe/Desktop/notes-plans-hub/hogwarts202603`
- `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/container_registry-rs`
- `/Users/amuldotexe/Desktop/oss-read-only/auron`
- `/Users/amuldotexe/Desktop/oss-read-only/dask`
- `/Users/amuldotexe/Desktop/oss-read-only/hermes-agent`
- `/Users/amuldotexe/Desktop/oss-read-only/omnigraph`
- `/Users/amuldotexe/Desktop/oss-read-only/pi_agent_rust`
- `/Users/amuldotexe/Desktop/oss-read-only/sail`
- `/Users/amuldotexe/Desktop/oss-read-only/tauri`
- `/Users/amuldotexe/Desktop/oss-read-only/zed-gpui`
- `/Users/amuldotexe/Desktop/personal-repos-lane/JobSearchGames`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/MCP-Zero`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ToolSandbox`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/contextweaver`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/mcp-bench`
- `/Users/amuldotexe/Desktop/personal-repos-lane/algo-free-twitter-marination`
- `/Users/amuldotexe/Desktop/personal-repos-lane/before-i-go-org-github`
- `/Users/amuldotexe/Desktop/personal-repos-lane/dobby-subagent-code-summarizer`
- `/Users/amuldotexe/Desktop/personal-repos-lane/fawkes-body-doubling-phoenix`
- `/Users/amuldotexe/Desktop/personal-repos-lane/graph-data-science`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-apoc-procedures-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-gds-client-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-ogm-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/opencypher-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-arrow-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-parquet-format-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/cayley-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/dgraph-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/fjall-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphblas-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gunrock-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/jemalloc-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics_docs-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v2_driver-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/memgraph-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/networkit-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/python-graphblas-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/risingwave-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/snap-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/terminusdb-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tracing-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/mission-grindelwald`
- `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-toposort-kahns-algorithm`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/1broseidon__cymbal`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AbstractMachinesLab__tree-sitter-erlang`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__android-tree-sitter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndyInternet__indexer`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diffguardian`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Benjamin-Davies__tree-sitter-relview`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/BrianHicks__tree-grepper`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ChronosTeamx__FuncUndo`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeGraphContext__CodeGraphContext`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DNSZLSK__lexluthor`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DeusData__codebase-memory-mcp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/EmranMR__tree-sitter-blade`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Flakebi__tree-sitter-tablegen`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GhentCDH__tree-sitter-wikitext`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/HelgeSverre__tree-sitter-applescript`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Hubro__tree-sitter-robot`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Isopod__tree-sitter-pascal`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Joakker__tree-sitter-json5`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Julian__lean.nvim`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/LdBeth__tree-sitter-rnc`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Manikanta-Reddy-Pasala__AiForgeMemory`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Neverdecel__CodeRAG`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OXY2DEV__tree-sitter-lua_patterns`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OpenModelica__tree-sitter-modelica`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PranavNagothu__FlakeShield`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RRethy__nvim-treesitter-textsubjects`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RooCodeInc__Roo-Code`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/SonarSource__sonarqube`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/TabbyML__tabby`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/UserNobody14__tree-sitter-dart`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/WhatsApp__tree-sitter-erlang`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/YPYT1__EverMind`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/acp-protocol__acp-cli`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/afnanenayet__diffsitter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aishasurve2007__codebase-agent`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/albfan__rust-tree-sitter-ast-viewer`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/alexpovel__srgn`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/arborist-ts__arborist.nvim`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ast-grep__ast-grep`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bakhliustov__askgraph`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bennypowers__tree-sitter-handlebars`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/biomejs__gritql`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/buzz-language__tree-sitter-buzz`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/camdencheek__tree-sitter-go-mod`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cdeust__automatised-pipeline`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cocoindex-io__cocoindex-code`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/constantitus__tree-sitter-jai`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/crystal-lang-tools__crystal-tree-sitter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cyberNoman__universal-code-review-graph`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/demirmusa__nanocontext`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dlvandenberg__tree-sitter-angular`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dsully__tree-sitter-pyproject`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/elixir-lang__tree-sitter-elixir`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/emiasims__tree-sitter-org`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/euclidianAce__tree-sitter-teal`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/fluffypony__mcp-code-indexer`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/forloopcodes__contextplus`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/geigerzaehler__tree-sitter-jinja2`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/github__stack-graphs`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/gmlarumbe__tree-sitter-systemverilog`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/greglas75__codesift`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hippietrail__tree-sitter-harper-dict`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/iamsaquib8__tessera`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ikatyang__tree-sitter-yaml`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ionide__tree-sitter-fsharp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jimhester__rtreesitter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jlcrochet__tree-sitter-razor`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/johnhuang316__code-index-mcp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jrmoulton__tree-sitter-slint`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kentookura__tree-sitter-forester`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kristoferssolo__tree-sitter-jsonl`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/langston-barrett__tree-sitter-souffle`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/levnikolaevich__claude-code-skills`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lumen-oss__luarocks-build-treesitter-parser`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mariusgreuel__tree-sitter-dotnet-bindings`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mertcanaltin__composto`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mizlan__iswap.nvim`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mrnugget__tree-sitter-tucan`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/naidaon__tree-sitter-astra`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/neo4j__neo4j`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nielsenko__tree-sitter-dart`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nushell__tree-sitter-nu`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nvim-treesitter__nvim-treesitter-textobjects`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/omnetpp__tree-sitter-ned`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/openrewrite__rewrite`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/parth-maheta__BugRadar`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/polarmutex__tree-sitter-astro`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pstuifzand__tree-sitter-printf`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rayen03__CodeBase_RAG`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ribru17__tree-sitter-man`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rockerBOO__boo-colorscheme-nvim`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sairam0424__ag-bash`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/salsa-rs__salsa`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/scip-code__scip-rust`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/serenadeai__java-tree-sitter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/simonbs__TreeSitterLanguages`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/snip-ai__snip`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcegraph__scip-python`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/srazzak__tree-sitter-mdx`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/stormwarning__tree-sitter-nunjucks`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/surrealdb__surrealql-tree-sitter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tarungulati1988__onboard`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/the-mikedavis__tree-sitter-git-rebase`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tong__tree-sitter-haxe`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-grammars__tree-sitter-hcl`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-perl__tree-sitter-pod`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__java-tree-sitter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__parser-test-action`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-bash`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-css`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-html`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-ocaml`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-ruby`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-verilog`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/unhappychoice__gitlogue`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/uyha__tree-sitter-cmake`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/viktorstrate__swift-tree-sitter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vrischmann__tree-sitter-templ`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/wingyplus__tree-sitter-elixir`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/y1hanh__codebase-indexer-mcp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zackradisic__glyph`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ziglibs__tree-sitter-zig`
- `/Users/amuldotexe/Desktop/personal-repos-lane/pm2dev`
- `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/codecentric__spring-boot-admin`
- `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/mybatis__spring-boot-starter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/spring-guides__gs-spring-boot`
- `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/xkcoding__spring-boot-demo`
- `/Users/amuldotexe/Desktop/personal-repos-lane/servo-test-202411`
- `/Users/amuldotexe/Desktop/personal-repos-lane/tweetbook202409`
- `/Users/amuldotexe/Desktop/personal-repos-lane/zip-revelio`
- `/Users/amuldotexe/Desktop/personal-repos-lane/zztweets-of-amuldotexe2023`
- `/Users/amuldotexe/Desktop/reference-repos-yard/aquascope`
- `/Users/amuldotexe/Desktop/reference-repos-yard/codemogger`
- `/Users/amuldotexe/Desktop/reference-repos-yard/fff.nvim`
- `/Users/amuldotexe/Desktop/reference-repos-yard/kani`
- `/Users/amuldotexe/Desktop/reference-repos-yard/miri`
- `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_clr`
- `/Users/amuldotexe/Desktop/reference-repos-yard/tauri-template`

## Pattern Entries

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/tauri`

### Concept: Runtime trait as a platform Adapter seam

Evidence:

- `/Users/amuldotexe/Desktop/oss-read-only/tauri/crates/tauri-runtime/src/lib.rs` defines the runtime Interface with `pub trait Runtime<T: UserEvent>`, associated dispatcher types, and methods such as `new`, `create_proxy`, `handle`, `create_window`, `create_webview`, `run_return`, and `run`.
- The same file defines adjacent dispatcher Interfaces: `RuntimeHandle`, `EventLoopProxy`, `WebviewDispatch`, and `WindowDispatch`.
- `/Users/amuldotexe/Desktop/oss-read-only/tauri/crates/tauri-runtime-wry/src/lib.rs` is the concrete Adapter: `impl<T: UserEvent> Runtime<T> for Wry<T>` binds `WindowDispatcher = WryWindowDispatcher<T>`, `WebviewDispatcher = WryWebviewDispatcher<T>`, `Handle = WryHandle<T>`, and `EventLoopProxy = EventProxy<T>`.

Architecture lens:

The `tauri-runtime` crate makes the runtime a deep Module. Its Interface is not merely a Rust trait signature; it also encodes ordering constraints and platform facts: `new` must be used on the main thread, `new_any_thread` is gated by platform cfgs, dispatcher handles must be `Send + Sync`, and many calls return `Result` because the underlying webview/window system is fallible. The `tauri-runtime-wry` crate is an Adapter at that seam. This gives Tauri leverage because application code can talk in terms of windows, webviews, event loops, proxies, and dispatchers without importing tao/wry directly. It gives maintainers locality because platform-specific cfgs and webview quirks concentrate in the Wry implementation instead of leaking across application-facing Modules.

Reusable code shape:

```rust
pub trait Runtime<T: UserEvent>: Debug + Sized + 'static {
    type WindowDispatcher: WindowDispatch<T, Runtime = Self>;
    type WebviewDispatcher: WebviewDispatch<T, Runtime = Self>;
    type Handle: RuntimeHandle<T, Runtime = Self>;
    type EventLoopProxy: EventLoopProxy<T>;

    fn new(args: RuntimeInitArgs) -> Result<Self>;
    fn create_proxy(&self) -> Self::EventLoopProxy;
    fn handle(&self) -> Self::Handle;
    fn create_window<F: Fn(RawWindow) + Send + 'static>(
        &self,
        pending: PendingWindow<T, Self>,
        after_window_creation: Option<F>,
    ) -> Result<DetachedWindow<T, Self>>;
    fn run<F: FnMut(RunEvent<T>) + 'static>(self, callback: F);
}

pub struct Wry<T> {
    context: RuntimeContext<T>,
    // tao/wry state hidden inside the Adapter implementation
}

impl<T: UserEvent> Runtime<T> for Wry<T> {
    type WindowDispatcher = WryWindowDispatcher<T>;
    type WebviewDispatcher = WryWebviewDispatcher<T>;
    type Handle = WryHandle<T>;
    type EventLoopProxy = EventProxy<T>;
    /* platform implementation */
}
```

Transfer rule:

Use this shape when a Rust workspace needs to support multiple platform backends or runtime providers. Put the seam at the smallest vocabulary that callers actually need, then move every platform-specific detail behind an Adapter. Avoid introducing this seam if there is only one Adapter and no credible second implementation; in that case the deletion test may show a shallow Module.

Verification hook:

- Compile at least one concrete Adapter crate and one caller crate so associated type drift is caught by the type checker.
- Add a smoke test or example that exercises `create_window`, `create_webview`, and event-loop dispatch through the trait Interface rather than through the Adapter type.
- In CI, build with platform cfg coverage where practical, because the Interface includes cfg-gated invariants.

### Concept: Plugin Builder converts callback sprawl into one deep extension Module

Evidence:

- `/Users/amuldotexe/Desktop/oss-read-only/tauri/crates/tauri/src/plugin.rs` defines `pub trait Plugin<R: Runtime>: Send` with lifecycle hooks: `initialize`, `initialization_script`, `window_created`, `webview_created`, `on_navigation`, `on_page_load`, `on_event`, and `extend_api`.
- The same file defines `pub struct Builder<R: Runtime, C: DeserializeOwned = ()>` with fields for each callback and a fluent construction Interface.
- `pub struct TauriPlugin<R: Runtime, C: DeserializeOwned = ()>` stores the callbacks and implements `Plugin<R> for TauriPlugin<R, C>`.

Architecture lens:

The raw plugin lifecycle has a wide Interface because plugins can participate in startup, command dispatch, navigation, webview creation, page loading, runtime events, URI schemes, and teardown. Tauri deepens that Module by offering a Builder Adapter: plugin authors supply only the callbacks they need, while defaults cover the rest. The seam remains the `Plugin<R>` trait, and `TauriPlugin` is the Adapter that turns user callbacks into a trait object stored by `PluginStore`. The leverage is ergonomic extension without forcing every plugin to implement the full lifecycle. The locality is strong because config deserialization, reserved-name validation, URI scheme registration, and callback dispatch are all concentrated in `plugin.rs`.

Reusable code shape:

```rust
pub trait Plugin<R: Runtime>: Send {
    fn name(&self) -> &'static str;
    fn initialize(&mut self, app: &AppHandle<R>, config: JsonValue) -> Result<(), Box<dyn Error>>;
    fn on_event(&mut self, app: &AppHandle<R>, event: &RunEvent) {}
    fn extend_api(&mut self, invoke: Invoke<R>) -> bool { false }
}

pub struct Builder<R: Runtime, C: DeserializeOwned = ()> {
    name: &'static str,
    setup: Option<Box<SetupHook<R, C>>>,
    on_event: Box<OnEvent<R>>,
    invoke_handler: Box<InvokeHandler<R>>,
}

impl<R: Runtime, C: DeserializeOwned> Plugin<R> for TauriPlugin<R, C> {
    fn initialize(&mut self, app: &AppHandle<R>, config: JsonValue) -> Result<(), Box<dyn Error>> {
        // deserialize config, run setup, register protocols
        Ok(())
    }
    fn extend_api(&mut self, invoke: Invoke<R>) -> bool {
        (self.invoke_handler)(invoke)
    }
}
```

Transfer rule:

When an extension point has many optional lifecycle hooks, keep one canonical trait Interface and provide a Builder-backed Adapter for common callers. This preserves a single seam for the host while sparing extension authors from implementing pass-through hooks. Keep lifecycle ordering in the Interface documentation, not in scattered examples.

Verification hook:

- Unit-test default callbacks so omitted hooks are inert.
- Add integration tests for config deserialization failure text, reserved names, and callback ordering.
- Exercise the extension through `Box<dyn Plugin<R>>` to verify the host seam, not only through the Builder type.

### Concept: Codegen cache by content checksum

Evidence:

- `/Users/amuldotexe/Desktop/oss-read-only/tauri/crates/tauri-codegen/src/lib.rs` exposes `get_config` and an internal `Cached` Module.
- `checksum(bytes: &[u8]) -> Result<String, fmt::Error>` creates a blake3 checksum.
- `impl TryFrom<Vec<u8>> for Cached` writes content to `$OUT_DIR/<checksum>` through `write_if_changed`.
- `impl ToTokens for Cached` emits `concat!(env!("OUT_DIR"), "/", checksum)`, letting generated Rust refer to the cached artifact.

Architecture lens:

This is a small but deep Module: callers hand it generated content and receive a tokenizable path. The Interface hides filesystem idempotence, hashing, output directory selection, and codegen token emission. The seam is not a trait seam; it is a value seam between build-time content and generated Rust source. The leverage is reproducible codegen without rewriting identical generated artifacts. The locality is high because checksum choice, `$OUT_DIR` policy, and write-if-changed behavior can evolve in one implementation.

Reusable code shape:

```rust
struct Cached {
    checksum: String,
}

impl TryFrom<Vec<u8>> for Cached {
    type Error = EmbeddedAssetsError;

    fn try_from(content: Vec<u8>) -> Result<Self, Self::Error> {
        let checksum = checksum(content.as_ref())?;
        let path = ensure_out_dir()?.join(&checksum);
        write_if_changed(&path, &content)?;
        Ok(Self { checksum })
    }
}

impl ToTokens for Cached {
    fn to_tokens(&self, tokens: &mut TokenStream) {
        let path = &self.checksum;
        tokens.append_all(quote!(::std::concat!(::std::env!("OUT_DIR"), "/", #path)))
    }
}
```

Transfer rule:

Use content-addressed build artifacts when proc-macro or build-script output must be stable, deduplicated, and referable from generated tokens. Keep the hash-and-write Module private until multiple callers need the seam.

Verification hook:

- Test that identical input maps to the same path and does not rewrite content.
- Test that changed input changes the checksum path.
- Use a trybuild or snapshot test for generated tokens so path emission stays valid.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ast-grep__ast-grep`

### Concept: Language trait separates parser quirks from structural search

Evidence:

- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ast-grep__ast-grep/crates/core/src/language.rs` defines `pub trait Language: Clone + 'static`.
- That trait includes `pre_process_pattern`, `meta_var_char`, `expando_char`, `extract_meta_var`, `from_path`, `kind_to_id`, `field_to_id`, and `build_pattern`.
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ast-grep__ast-grep/crates/core/src/tree_sitter/mod.rs` defines `pub trait LanguageExt: Language` with `ast_grep`, `get_ts_language`, `injectable_languages`, and `extract_injections`.
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ast-grep__ast-grep/crates/language/src/lib.rs` implements many language Adapters through `impl_lang!`, `impl_lang_expando!`, and `SupportLang`.

Architecture lens:

`Language` is the key parser seam. It gives the search engine a small Interface for language-specific facts: how pattern metavariables are represented, how parser-hostile query text is preprocessed, how node kinds and fields map to tree-sitter IDs, and how a pattern is built. `LanguageExt` deepens the tree-sitter Adapter side by adding parsing, injections, and concrete `TSLanguage` access. The core matcher can stay generic over `L: Language` or `L: LanguageExt`; language quirks have locality inside language Adapters rather than in the matcher. This is high leverage because adding a language usually means implementing the language Interface and reusing the same matching, traversal, replacement, config, CLI, LSP, N-API, PyO3, and WASM Modules.

Reusable code shape:

```rust
pub trait Language: Clone + 'static {
    fn pre_process_pattern<'q>(&self, query: &'q str) -> Cow<'q, str> {
        Cow::Borrowed(query)
    }
    fn meta_var_char(&self) -> char { '$' }
    fn expando_char(&self) -> char { self.meta_var_char() }
    fn kind_to_id(&self, kind: &str) -> u16;
    fn field_to_id(&self, field: &str) -> Option<u16>;
    fn build_pattern(&self, builder: &PatternBuilder) -> Result<Pattern, PatternError>;
}

pub trait LanguageExt: Language {
    fn ast_grep<S: AsRef<str>>(&self, source: S) -> AstGrep<StrDoc<Self>> {
        AstGrep::new(source, self.clone())
    }
    fn get_ts_language(&self) -> TSLanguage;
    fn extract_injections<L: LanguageExt>(&self, _root: Node<StrDoc<L>>) -> Vec<(String, Vec<TSRange>)> {
        Vec::new()
    }
}
```

Transfer rule:

For multi-language parser tooling, make parser quirks an explicit language Interface before they leak into search, replace, or CLI Modules. Split pure language semantics from tree-sitter access when possible: `Language` can support abstract matching facts, while `LanguageExt` can carry parser-engine dependencies.

Verification hook:

- For every new Adapter, test positive and negative pattern matches in `crates/language`.
- Test expando languages with patterns that contain metavariables the native parser would reject.
- Test injection extraction separately from top-level parsing so multi-language documents do not become a shallow special case in the matcher.

### Concept: SupportLang enum dispatch keeps many language Adapters behind one CLI-facing Interface

Evidence:

- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ast-grep__ast-grep/crates/language/src/lib.rs` defines the supported language registry and dispatch macros.
- `SupportLang` implements `Language` by forwarding `kind_to_id`, `field_to_id`, `meta_var_char`, `expando_char`, `extract_meta_var`, `build_pattern`, and `pre_process_pattern` to the concrete language.
- `SupportLang` implements `LanguageExt`, including HTML injection extraction as a special Adapter path.
- `extensions(lang: SupportLang) -> &'static [&'static str]` centralizes file extension mapping.

Architecture lens:

This is an enum-dispatch Adapter that converts many zero-sized language Modules into one CLI-facing Interface. The seam is the `SupportLang` value: callers can parse a language from a flag or file path, then continue through the same `Language` and `LanguageExt` Interfaces used by generic code. This offers leverage because CLI, config, and LSP Modules do not need their own per-language registries. It preserves locality because extension mapping and language dispatch live in one registry Module.

Reusable code shape:

```rust
pub enum SupportLang {
    Rust,
    TypeScript,
    Html,
    // ...
}

impl Language for SupportLang {
    fn kind_to_id(&self, kind: &str) -> u16 {
        execute_lang_method!(self, kind_to_id, kind)
    }

    fn from_path<P: AsRef<Path>>(path: P) -> Option<Self> {
        from_extension(path.as_ref())
    }
}

impl LanguageExt for SupportLang {
    fn get_ts_language(&self) -> TSLanguage {
        execute_lang_method!(self, get_ts_language,)
    }
}
```

Transfer rule:

Use enum dispatch when a CLI or config file must select from a closed set of language Adapters. Use trait objects or plugin loading only when languages are open-ended at runtime. The deletion test should show that removing the enum registry would force file-extension mapping and Adapter dispatch back into several callers.

Verification hook:

- Snapshot the language list and extension mapping.
- Test `FromStr` and `from_path` for common aliases.
- Run at least one shared matcher test through `SupportLang` rather than through a concrete language type.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/github__stack-graphs`

### Concept: StackGraph as an incremental name-resolution Module

Evidence:

- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/github__stack-graphs/stack-graphs/src/lib.rs` explains the core model: name binding is represented as paths in a graph, path finding keeps a symbol stack and a scope stack, and graph chunks depend on local source-file information for incrementality.
- The same file exports Modules including `graph`, `partial`, `paths`, `stitching`, `storage`, `cycles`, `serde`, and `visualization`.
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/github__stack-graphs/stack-graphs/src/graph.rs` defines `pub struct StackGraph`.
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/github__stack-graphs/stack-graphs/src/partial.rs` defines `PartialPath`, `PartialPathEdge`, `PartialPathEdgeList`, and `PartialPaths`.

Architecture lens:

The deep Module here is not a parser; it is the graph model for language-agnostic name resolution. The Interface is the vocabulary of stack graph nodes, paths, partial paths, scopes, symbols, cancellation, storage, and stitching. The implementation can perform sophisticated path finding and incremental reuse while language frontends emit only local graph facts. The seam between language-specific graph construction and language-independent path stitching gives strong leverage: new languages do not rewrite name resolution. It gives locality because resolution correctness lives in stack/graph/path Modules rather than in every parser Adapter.

Reusable code shape:

```rust
pub mod graph;
pub mod partial;
pub mod paths;
pub mod stitching;

pub trait CancellationFlag {
    fn check(&self, at: &'static str) -> Result<(), CancellationError>;
}

pub struct NoCancellation;
impl CancellationFlag for NoCancellation {
    fn check(&self, _at: &'static str) -> Result<(), CancellationError> {
        Ok(())
    }
}

pub struct CancelAfterDuration {
    limit: Duration,
    start: Instant,
}
```

Transfer rule:

When building code intelligence for multiple languages, move semantic resolution into a graph Module and make language frontends emit local graph facts. Keep cancellation in the Interface from the beginning; graph searches are exactly where users need bounded work.

Verification hook:

- Add language-independent tests for path stitching and cycle handling.
- Add cancellation tests that force `CancellationFlag::check` at known search locations.
- Use fixture graphs that model cross-file resolution so incrementality is tested outside any one parser Adapter.

### Concept: Tree-sitter graph DSL as a declarative Adapter into StackGraph

Evidence:

- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/github__stack-graphs/tree-sitter-stack-graphs/src/lib.rs` documents the tree-sitter graph construction DSL and the stack-graph vocabulary it expects: node `type`, `symbol`, `source_node`, `is_definition`, `is_reference`, `scope`, `is_exported`, `syntax_type`, `definiens_node`, and `edge`/`precedence`.
- The same file defines `pub struct StackGraphLanguage` and methods including `build_stack_graph_into`, `builder_into_stack_graph`, and `build`.
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/github__stack-graphs/tree-sitter-stack-graphs/src/loader.rs` defines `pub struct Loader` with `load_tree_sitter_language_for_file`, `load_for_file`, `load_globals_from_config_path`, and `load_globals_from_config_str`.
- `tree-sitter-stack-graphs/src/lib.rs` contains loader functions such as `load_drop_scopes`, `load_pop_scoped_symbol`, `load_pop_symbol`, `load_push_scoped_symbol`, `load_push_symbol`, `load_scope`, `load_source_info`, and `load_definiens_info`.

Architecture lens:

This repo places a declarative DSL seam between syntax trees and semantic stack graphs. Tree-sitter grammars are not asked to implement name resolution directly. Instead, language Adapters provide graph construction rules in a shared DSL vocabulary, and `StackGraphLanguage` interprets them into the core `StackGraph` Module. The Interface is deeper than "run this query": it includes required attributes, source-location invariants, definition/reference flags, exported-scope requirements, edge precedence, and debug metadata. The leverage is substantial because a language implementer writes rules while the implementation handles parsing, graph building, validation, cancellation, and diagnostics.

Reusable code shape:

```rust
pub struct StackGraphLanguage {
    language: tree_sitter::Language,
    tsg: GraphConstructionRules,
    // builtins, globals, cancellation-aware loaders
}

impl StackGraphLanguage {
    pub fn build_stack_graph_into<'a>(
        &self,
        graph: &'a mut StackGraph,
        source: &str,
        cancellation_flag: &dyn CancellationFlag,
    ) -> Result<(), BuildError> {
        // parse source, execute TSG, load stack-graph nodes and edges
        Ok(())
    }
}
```

Transfer rule:

Use a declarative Adapter DSL when syntax-to-semantics mapping must vary per language but the target semantic graph should stay uniform. Make the DSL vocabulary match the destination Module's Interface, not the parser's accidental node shapes.

Verification hook:

- Test invalid DSL attributes with precise errors.
- Fixture-test each language's `.tsg` rules against expected stack graph nodes and paths.
- Include source span tests for definitions and references because code navigation depends on the Interface invariant, not just graph connectivity.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/salsa-rs__salsa`

### Concept: Incremental database Interface with tracked query Modules

Evidence:

- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/salsa-rs__salsa/src/lib.rs` documents the public construct vocabulary: `input`, `tracked`, `interned`, `accumulator`, `Supertype`, return modes, tracked functions, memoized values, backdating, LRU eviction, specification, and cycles.
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/salsa-rs__salsa/src/database.rs` defines `pub trait Database: Send + ZalsaDatabase + AsDynDatabase`.
- The `Database` Interface includes revision-affecting operations: `trigger_lru_eviction`, `synthetic_write`, `trigger_cancellation`, `cancellation_token`, `report_untracked_read`, `ingredient_debug_name`, and `unwind_if_revision_cancelled`.
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/salsa-rs__salsa/src/function.rs` defines a tracked function `Configuration` Interface with `DbView`, `SalsaStruct`, `Input`, `Output`, `Eviction`, cycle strategy, equality/backdating, `id_to_input`, `heap_size`, `execute`, `cycle_initial`, and cycle recovery.
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/salsa-rs__salsa/src/accumulator.rs` defines `pub trait Accumulator` and an `IngredientImpl` that panics if values are accumulated outside an active tracked function.

Architecture lens:

Salsa is a reference example of making the database the seam for incremental computation. The Interface is intentionally richer than "call a query": callers must understand revisions, cancellation, durability, memo retention, return modes, and identity. The implementation hides dependency graph maintenance, red/green validation, memo tables, backdating, cycle iteration, and accumulator plumbing. The leverage is huge for compiler-like systems because the user writes ordinary-looking tracked functions while Salsa manages invalidation. The locality is also high: invalidation and memo correctness are concentrated inside Salsa Modules instead of being reimplemented in each compiler analysis.

Reusable code shape:

```rust
pub trait Database: Send + ZalsaDatabase + AsDynDatabase {
    fn synthetic_write(&mut self, durability: Durability) {
        let zalsa_mut = self.zalsa_mut();
        zalsa_mut.new_revision();
        zalsa_mut.runtime_mut().report_tracked_write(durability);
    }

    fn report_untracked_read(&self) {
        let (zalsa, zalsa_local) = self.zalsas();
        zalsa_local.report_untracked_read(zalsa.current_revision())
    }
}

pub trait Configuration: Any {
    type DbView: ?Sized + crate::Database;
    type Input<'db>: Send + Sync;
    type Output<'db>: Send + Sync;
    type Eviction: EvictionPolicy;

    fn execute<'db>(db: &'db Self::DbView, input: Self::Input<'db>) -> Self::Output<'db>;
    fn values_equal<'db>(old: &Self::Output<'db>, new: &Self::Output<'db>) -> bool;
}
```

Transfer rule:

Use this pattern when a Rust compiler, language server, graph indexer, or analyzer has mostly pure derived facts over mutable inputs. Make "input identity", "derived identity", and "canonical interned identity" separate Modules early; collapsing them produces shallow cache keys and invalidation bugs. Keep diagnostics as an accumulator-like side channel when they should not affect a query's main result equality.

Verification hook:

- Test that changing an input field invalidates only queries that read that field.
- Test backdating: if a query recomputes to an equal output, downstream queries should not re-run.
- Test cancellation with an outstanding snapshot to catch deadlock-sensitive Interface misuse.
- Test that accumulator output is only available through a tracked execution and is replaced when the producing query reruns.

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/miri`

### Concept: Interpreter Machine Adapter concentrates execution semantics

Evidence:

- `/Users/amuldotexe/Desktop/reference-repos-yard/miri/src/machine.rs` defines `pub struct MiriMachine<'tcx>` with global interpreter state: `tcx`, borrow tracker, data race handler, allocation address state, environment variables, file descriptors, directory descriptors, epoll interests, monotonic clock, thread manager, primitive layouts, static roots, profiler, exported-symbol cache, random generator, native library state, page/stack settings, symbolic alignment, pthread sanity cells, and other execution configuration.
- The same file implements `impl<'tcx> Machine<'tcx> for MiriMachine<'tcx>`.
- That implementation binds interpreter associated types such as `MemoryKind`, `ExtraFnVal`, `FrameExtra`, `AllocExtra`, `Provenance`, `ProvenanceExtra`, `Bytes`, and `MemoryMap`.
- It overrides semantic hooks like `enforce_alignment`, `alignment_check`, `enforce_validity`, `enforce_validity_recursively`, `ignore_optional_overflow_checks`, and `check_fn_target_features`.

Architecture lens:

`MiriMachine` is a large implementation behind the rustc interpreter's `Machine` Interface. It is deep because a compact trait Adapter slot controls memory representation, provenance, validity, alignment, target-feature checks, thread state, foreign interactions, and diagnostic behavior. The seam is load-bearing: rustc's interpreter can call through the `Machine` Interface while Miri provides a concrete execution semantics Adapter. The locality benefit is clear: UB-checking policy, isolation policy, borrow tracking, data-race detection, and host shims live in one machine Module rather than being scattered through every MIR operation.

Reusable code shape:

```rust
pub struct AnalysisMachine<'tcx> {
    tcx: TyCtxt<'tcx>,
    provenance: ProvenanceState,
    threads: ThreadManager<'tcx>,
    validation: ValidationMode,
    // analysis-specific global state
}

impl<'tcx> Machine<'tcx> for AnalysisMachine<'tcx> {
    type MemoryKind = AnalysisMemoryKind;
    type FrameExtra = FrameExtra<'tcx>;
    type AllocExtra = AllocExtra<'tcx>;
    type Provenance = Provenance;

    fn enforce_alignment(ecx: &InterpCx<'tcx, Self>) -> bool {
        ecx.machine.validation.requires_alignment()
    }

    fn enforce_validity(ecx: &InterpCx<'tcx, Self>, layout: TyAndLayout<'tcx>) -> bool {
        ecx.machine.validation.requires_validity(layout)
    }
}
```

Transfer rule:

For MIR interpreters and static analyses, resist adding ad hoc flags to each operation. Put execution policy behind a Machine Adapter and let the interpreter core call semantic hooks. This increases depth because the caller learns one Interface and receives many cross-cutting behaviors.

Verification hook:

- Add targeted tests for each associated semantic hook: alignment, validity, provenance, unsupported target features, and host operation policy.
- Run the same MIR fixture under two Machine Adapters if possible to prove the seam is real.
- Include regression tests for diagnostics because the Machine Interface includes error modes, not only execution results.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/fjall-src`

### Concept: Keyspace handle hides LSM tree, journal, and deletion invariants

Evidence:

- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/fjall-src/src/keyspace/mod.rs` defines `pub struct KeyspaceInner` with internal ID, keyspace name, config, deleted/poisoned flags, `AnyTree`, supervisor, stats, worker sender, and lock guard.
- The same file defines `pub struct Keyspace(pub(crate) Arc<KeyspaceInner>)`, implements `Clone`, `Deref`, `PartialEq`, `Eq`, and `Hash`, and documents keyspace aliases: column family, locality group, and table.
- `impl Drop for KeyspaceInner` deletes the manifest before the keyspace directory to avoid resurrecting a deleted keyspace if cleanup is interrupted.
- `Keyspace::clear` writes to the journal, persists unless manual persist is configured, poisons the keyspace on fatal persist failure, and clears the tree.

Architecture lens:

`Keyspace` is a deep storage Module. Its public Interface is a cloneable handle with operations like `name`, `clear`, and key-value access, but the implementation hides LSM internals, manifest ordering, poison state, locks, journaling, stats, worker communication, and deferred deletion. This is a strong locality pattern for storage systems: correctness-critical ordering, like "delete manifest before directory", is pinned inside `Drop` and cannot be accidentally skipped by callers. The leverage is that callers can treat a keyspace like a logical table while inheriting durability and cleanup semantics.

Reusable code shape:

```rust
pub struct KeyspaceInner {
    id: InternalKeyspaceId,
    name: KeyspaceKey,
    config: CreateOptions,
    is_deleted: AtomicBool,
    is_poisoned: Arc<AtomicBool>,
    tree: AnyTree,
    supervisor: Supervisor,
}

#[derive(Clone)]
pub struct Keyspace(pub(crate) Arc<KeyspaceInner>);

impl Drop for KeyspaceInner {
    fn drop(&mut self) {
        if self.is_deleted.load(Ordering::Acquire) {
            // delete manifest first so interrupted cleanup cannot resurrect data
            remove_manifest_then_directory(&self.tree.tree_config().path);
        }
    }
}
```

Transfer rule:

Use an `Arc<Inner>` handle Module when storage resources must remain alive while operations, snapshots, or background workers still refer to them. Put crash-safety ordering in `Drop` or a single deletion Module, not in every caller that removes data.

Verification hook:

- Test interrupted or partial deletion ordering by checking that missing manifest means the keyspace is treated as uninitialized.
- Test poison behavior after simulated journal persist failure.
- Test clone/drop behavior so disk cleanup does not occur while any handle remains.

### Concept: Readable trait unifies snapshots and write transactions

Evidence:

- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/fjall-src/src/readable.rs` defines `pub trait Readable`.
- Its documentation says a write transaction can be passed into a function that expects a snapshot.
- The Interface includes `get`, `contains_key`, `first_key_value`, `last_key_value`, `size_of`, and range/iteration methods further down the same file.
- Examples emphasize repeatable read: after a `Database` snapshot is created, later inserts into the keyspace do not alter the snapshot's result.

Architecture lens:

`Readable` is a seam over multiple read-capable Adapters. The Interface carries more than method names: it promises snapshot semantics, repeatable reads, IO error modes, keyspace-scoped access, and ordered key operations. This yields leverage because query helpers can accept `impl Readable` and work with both snapshots and transactions. It yields locality because repeatable-read mechanics stay in the Adapters rather than in query code.

Reusable code shape:

```rust
pub trait Readable {
    fn get<K: AsRef<[u8]>>(
        &self,
        keyspace: impl AsRef<Keyspace>,
        key: K,
    ) -> crate::Result<Option<UserValue>>;

    fn contains_key<K: AsRef<[u8]>>(
        &self,
        keyspace: impl AsRef<Keyspace>,
        key: K,
    ) -> crate::Result<bool>;

    fn first_key_value(&self, keyspace: impl AsRef<Keyspace>) -> Option<Guard>;
    fn last_key_value(&self, keyspace: impl AsRef<Keyspace>) -> Option<Guard>;
}
```

Transfer rule:

Introduce a read Interface when snapshots, transactions, and live stores all need to satisfy the same query Modules. Do not include write methods on the read seam; that would make the Interface shallow and erase the repeatable-read invariant.

Verification hook:

- Write one query helper generic over `Readable` and run it against a snapshot and a write transaction.
- Test repeatable-read behavior by mutating after snapshot creation.
- Test ordered operations at empty, single-key, and multi-key ranges.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tracing-src`

### Concept: Subscriber and Layer split separates recording core from composable observers

Evidence:

- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tracing-src/tracing-core/src/subscriber.rs` defines `pub trait Subscriber: 'static`.
- Its Interface documents callsite registration, interest caching, dynamic filters via `Interest::sometimes`, `enabled`, dispatch registration, and memory-leak avoidance using `WeakDispatch`.
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tracing-src/tracing-subscriber/src/layer/mod.rs` defines `pub trait Layer<S> where S: Subscriber`.
- `Layer` has `on_register_dispatch`, `on_layer`, `register_callsite`, `enabled`, and event/span notification hooks; it explicitly distinguishes globally enabling a span from a layer choosing to ignore a notification.
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tracing-src/tracing-subscriber/src/registry/sharded.rs` defines `pub struct Registry` with pooled span data, current span stacks, filter IDs, extensions, and `CloseGuard` cleanup coordination.

Architecture lens:

Tracing's design uses two related seams. `Subscriber` is the core recording Interface: it decides whether spans/events exist and receives lifecycle notifications. `Layer` is an Adapter seam for composable behavior around a Subscriber: formatting, filtering, metrics, distributed traces, and other observers can be stacked without each becoming the root Subscriber. `Registry` is a deep implementation Module for span storage and extension typemaps. The leverage is high because application code emits spans once, while observers can be composed independently. The locality is high because callsite interest caching and span lifecycle management are not duplicated by each observer.

Reusable code shape:

```rust
pub trait Subscriber: 'static {
    fn register_callsite(&self, metadata: &'static Metadata<'static>) -> Interest {
        if self.enabled(metadata) { Interest::always() } else { Interest::never() }
    }
    fn enabled(&self, metadata: &Metadata<'_>) -> bool;
}

pub trait Layer<S>
where
    S: Subscriber,
    Self: 'static,
{
    fn on_layer(&mut self, subscriber: &mut S) {}
    fn register_callsite(&self, metadata: &'static Metadata<'static>) -> Interest {
        if self.enabled(metadata, Context::none()) { Interest::always() } else { Interest::never() }
    }
    fn enabled(&self, metadata: &Metadata<'_>, ctx: Context<'_, S>) -> bool { true }
}
```

Transfer rule:

Use this split when one central runtime decision controls whether work happens, but many independent observers want to react to that work. Keep the "should this event exist?" Interface separate from "what should this observer do with it?" Otherwise filters and output Adapters become tightly coupled.

Verification hook:

- Test static callsite caching by asserting `enabled` is not re-run when `Interest::always` is returned.
- Test dynamic filters with `Interest::sometimes`.
- Test layer stacks where one layer filters globally and another merely ignores notifications.
- Test span close ordering with multiple registry-backed layers.

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/aquascope`

### Concept: rustc-driver plugin seam for body-scoped analyses

Evidence:

- `/Users/amuldotexe/Desktop/reference-repos-yard/aquascope/crates/aquascope_front/src/plugin.rs` defines `pub struct AquascopePlugin`, implements `RustcPlugin for AquascopePlugin`, parses `AquascopePluginArgs`, and dispatches commands.
- The same file defines `pub trait AquascopeAnalysis: Sized + Send + Sync` with associated `Output` and `fn run<'tcx>(tcx: TyCtxt<'tcx>, id: BodyId) -> AquascopeResult<Self::Output>`.
- It implements `AquascopeAnalysis` for functions of `(TyCtxt<'tcx>, BodyId) -> AquascopeResult<O>`.
- `AquascopeCallbacks<A: AquascopeAnalysis>` implements `rustc_driver::Callbacks`.
- `/Users/amuldotexe/Desktop/reference-repos-yard/aquascope/crates/aquascope/src/analysis/mod.rs` defines the core `AquascopeAnalysis<'tcx>` context around `TyCtxt`, `BodyId`, `BodyWithBorrowckFacts`, loan/move maps, region data, and analysis output.

Architecture lens:

Aquascope makes rustc itself the host and places a narrow analysis seam at `(TyCtxt, BodyId) -> Output`. The front plugin Module owns CLI/rustc-driver integration, while the core analysis Module owns MIR/HIR/borrowck facts. This creates leverage because any body-scoped analysis function can become an Adapter satisfying `AquascopeAnalysis`. It also gives locality: command parsing, rustc callbacks, and analysis execution are separated from the dataflow and visualization implementation.

Reusable code shape:

```rust
pub trait BodyAnalysis: Sized + Send + Sync {
    type Output: Serialize;

    fn run<'tcx>(
        tcx: TyCtxt<'tcx>,
        body_id: BodyId,
    ) -> Result<Self::Output, AnalysisError>;
}

impl<F, O> BodyAnalysis for F
where
    F: for<'tcx> Fn(TyCtxt<'tcx>, BodyId) -> Result<O, AnalysisError> + Send + Sync,
    O: Serialize,
{
    type Output = O;
    fn run<'tcx>(tcx: TyCtxt<'tcx>, body_id: BodyId) -> Result<O, AnalysisError> {
        (self)(tcx, body_id)
    }
}
```

Transfer rule:

For rustc-based tools, keep the rustc-driver Adapter thin and define the analysis Interface around the smallest stable compiler context needed by the work. Body-scoped tools should usually use `TyCtxt` plus `BodyId` or `BodyWithBorrowckFacts`, not pass the entire callback object around.

Verification hook:

- Compile fixture crates through the driver binary, not only unit-test analysis functions.
- Snapshot JSON output for representative HIR/MIR bodies.
- Test that one generic driver can run multiple analysis functions through the same `AquascopeAnalysis` seam.

### Concept: Cleaned MIR graph Adapter for control-flow algorithms

Evidence:

- `/Users/amuldotexe/Desktop/reference-repos-yard/aquascope/crates/aquascope/src/analysis/ir_mapper/body_graph.rs` defines `pub(crate) struct CleanedBody<'tcx>(pub &'tcx Body<'tcx>)`.
- It implements `DirectedGraph`, `StartNode`, `Successors`, and `Predecessors` for `CleanedBody`.
- The file documents that `CleanedBody` represents MIR locations reachable via the control-flow graph, and filters basic blocks through `keep_block` and `is_imaginary_target`.
- Tests in the same file create `CleanedBody(&wfacts.body)` from borrowck facts.

Architecture lens:

`CleanedBody` is a small Adapter Module that makes rustc MIR satisfy graph algorithm Interfaces. Its depth comes from hiding rustc-specific block filtering and imaginary target removal behind standard graph traits. The leverage is that dominance, post-dominance, traversal, and mapper Modules can operate on a graph Interface rather than on raw MIR details. The locality is useful because quirks of rustc's MIR blocks are concentrated in one Adapter.

Reusable code shape:

```rust
pub(crate) struct CleanedBody<'tcx>(pub &'tcx Body<'tcx>);

impl DirectedGraph for CleanedBody<'_> {
    type Node = BasicBlock;
}

impl StartNode for CleanedBody<'_> {
    fn start_node(&self) -> BasicBlock {
        START_BLOCK
    }
}

impl Successors for CleanedBody<'_> {
    fn successors(&self, node: BasicBlock) -> impl Iterator<Item = BasicBlock> {
        self.body().basic_blocks.successors(node).filter(|bb| self.keep_block(*bb))
    }
}
```

Transfer rule:

When compiler analyses need graph algorithms, adapt the compiler IR to graph traits once. Do not make every algorithm know about unreachable blocks, cleanup blocks, fake targets, or compiler-internal edge quirks.

Verification hook:

- Fixture-test successors and predecessors for functions with early returns, panics, and cleanup-like blocks.
- Compare algorithm output on raw MIR versus `CleanedBody` for cases where filtering matters.
- Add regression tests for every rustc version update because compiler IR graph invariants can shift.

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_clr`

### Concept: Rustc CodegenBackend Adapter translates MIR into a checkable intermediate CIL

Evidence:

- `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_clr/src/lib.rs` documents the project as an experimental rustc backend compiling Rust for .NET.
- The same file states that the project translates MIR to CIL in a precise but inefficient fashion to reduce bugs and enable checking of generated CIL, then allows optimizations in an `opt` Module.
- `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_clr/src/lib.rs` defines `struct MyBackend` and `impl CodegenBackend for MyBackend`.
- `__rustc_codegen_backend() -> Box<dyn CodegenBackend>` returns `Box::new(MyBackend)`.
- `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_clr/src/assembly.rs` contains function assembly code that translates MIR statements, terminators, locals, and entrypoint setup into `CILTree`, `CILRoot`, and `Assembly` structures, with optional conversion from v1 to v2 CIL roots for type checking.
- `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_clr/src/builder.rs` defines `CodegenCx<'tcx>` and `Builder<'tcx>`, implementing rustc backend traits such as `BackendTypes`.

Architecture lens:

This repo has a classic compiler Adapter seam: rustc calls a `CodegenBackend`, and the backend translates rustc MIR into its own CIL Modules. The implementation deliberately uses a checkable intermediate CIL before optimization. That adds depth because the backend Interface to rustc stays fixed while the internal implementation can expose a verification seam between "faithful MIR lowering" and "optimization". The locality benefit is large: translation bugs can be traced to individual MIR statements before later CIL optimization muddies the source mapping.

Reusable code shape:

```rust
struct MyBackend;

impl CodegenBackend for MyBackend {
    fn codegen_crate(&self, tcx: TyCtxt<'_>, metadata: EncodedMetadata, need_metadata_module: bool)
        -> Box<dyn Any>
    {
        let mut asm = Assembly::default();
        // lower each mono item from MIR into checkable CIL trees
        Box::new((crate_name, asm, crate_info))
    }

    fn join_codegen(&self, ongoing_codegen: Box<dyn Any>, sess: &Session, outputs: &OutputFilenames)
        -> (CodegenResults, FxIndexMap<WorkProductId, WorkProduct>)
    {
        let (_name, asm, crate_info) = *ongoing_codegen.downcast::<(IString, Assembly, CrateInfo)>().unwrap();
        // type-check or optimize CIL, then produce rustc CodegenResults
    }
}

#[no_mangle]
pub extern "Rust" fn __rustc_codegen_backend() -> Box<dyn CodegenBackend> {
    Box::new(MyBackend)
}
```

Transfer rule:

For alternate Rust backends, split lowering and optimization with an internal IR that can be checked and debugged. Keep one rustc-facing Adapter, then make MIR-to-IR and IR-to-output separate Modules so verification has locality.

Verification hook:

- Add compile fixtures that disable optimization and snapshot the checkable IR.
- Type-check CIL immediately after lowering and again after optimization.
- Include cargo integration tests for `build_core`, `build_alloc`, and ordinary binary crates because the backend Interface includes crate metadata, linking, and standard-library shape, not only function lowering.
## Repo Coverage: `/Users/amuldotexe/Desktop/notes-plans-hub/hogwarts202603`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust-Adjacent Parser Reference From `notes-plans-hub/hogwarts202603`
Evidence: `/Users/amuldotexe/Desktop/notes-plans-hub/hogwarts202603/idiomatic2026/01-typescript/04-async-patterns.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```text
# TypeScript Async Patterns

> Async code is the backbone of modern TypeScript applications. These patterns ensure your async operations are cancellable, retryable, properly bounded, and don't leak resources.

---

## Quick Reference

| ID | Pattern | One-liner |
|----|---------|-----------|
| TS-ASYNC-01 | Promise.allSettled | Handle mixed success/failure in parallel operations |
| TS-ASYNC-02 | AbortController | Cancel async operations gracefully |
| TS-ASYNC-03 | Retry with Backoff | Retry transient failures with exponential delay |
| TS-ASYNC-04 | Async Iterators | Process streams of data lazily |
| TS-ASYNC-05 | Concurrency Limiter | Control parallel execution count |
| TS-ASYNC-06 | Promise.withResolvers | Externalize promise resolution |
| TS-ASYNC-07 | Timeout Wrapper | Add timeout to any promise |
| TS-ASYNC-08 | Debounced Async | Debounce async operations without race conditions |
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/notes-plans-hub/hogwarts202603/idiomatic2026/01-typescript/04-async-patterns.md` and run `git -C /Users/amuldotexe/Desktop/notes-plans-hub/hogwarts202603 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/container_registry-rs`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust Module Architecture Slice From `oss-read-only/alienplatform/container_registry-rs`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/container_registry-rs/src/lib.rs`; scan counts include rust_files=9, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```rust
//! let storage = tempdir::TempDir::new("container_registry_test")
//!     .expect("could not create storage dir");
//!
//! // Setup an auth scheme that allows uploading with a master password, read-only
//! // access otherwise.
//! let auth = Arc::new(auth::Anonymous::new(
//!     auth::Permissions::ReadOnly,
//!     Secret::new("master password".to_owned())
//! ));
//!
//! // Instantiate the registry.
//! let registry = container_registry::ContainerRegistry::builder()
//!     .storage(storage.path())  // Note: When testing, use `build_for_testing` instead.
//!     .auth_provider(auth)
//!     .build()
//!     .expect("failed to instantiate registry");
//!
//! // Create an axum app router and mount our new registry on it.
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/container_registry-rs/src/lib.rs` and run `git -C /Users/amuldotexe/Desktop/oss-read-only/alienplatform/container_registry-rs ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/auron`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust Module Architecture Slice From `oss-read-only/auron`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/auron/auron-core/src/main/java/org/apache/auron/arrowio/AuronArrowFFIExporter.java`; scan counts include rust_files=178, cargo_manifests=9, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```text
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.auron.arrowio;

```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/oss-read-only/auron/auron-core/src/main/java/org/apache/auron/arrowio/AuronArrowFFIExporter.java` and run `git -C /Users/amuldotexe/Desktop/oss-read-only/auron ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/dask`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `oss-read-only/dask`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/dask/dask/array/tests/test_cupy_sparse.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
cupyx = pytest.importorskip("cupyx")


def test_sparse_hstack_vstack_csr():
    pytest.importorskip("cupyx")
    x = cupy.arange(24, dtype=cupy.float32).reshape(4, 6)

    sp = da.from_array(x, chunks=(2, 3), asarray=False, fancy=False)
    sp = sp.map_blocks(cupyx.scipy.sparse.csr_matrix, dtype=cupy.float32)

    y = sp.compute()

    assert cupyx.scipy.sparse.isspmatrix(y)
    assert_eq(x, y.todense())


@pytest.mark.parametrize("axis", [0, 1])
def test_sparse_concatenate(axis):
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/oss-read-only/dask/dask/array/tests/test_cupy_sparse.py` and run `git -C /Users/amuldotexe/Desktop/oss-read-only/dask ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/hermes-agent`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `oss-read-only/hermes-agent`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/hermes-agent/gateway/mirror.py`; scan counts include rust_files=9, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
"""
Session mirroring for cross-platform message delivery.

When a message is sent to a platform (via send_message or cron delivery),
this module appends a "delivery-mirror" record to the target session's
transcript so the receiving-side agent has context about what was sent.

Standalone -- works from CLI, cron, and gateway contexts without needing
the full SessionStore machinery.
"""

import json
import logging
from datetime import datetime
from typing import Optional

from hermes_cli.config import get_hermes_home

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/oss-read-only/hermes-agent/gateway/mirror.py` and run `git -C /Users/amuldotexe/Desktop/oss-read-only/hermes-agent ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/omnigraph`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `oss-read-only/omnigraph`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/omnigraph/crates/omnigraph-compiler/src/query/ast.rs`; scan counts include rust_files=192, cargo_manifests=10, tree_sitter_query_files=0, pest_files=2, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
pub const NOW_PARAM_NAME: &str = "__nanograph_now";

#[derive(Debug, Clone)]
pub struct QueryFile {
    pub queries: Vec<QueryDecl>,
}

#[derive(Debug, Clone)]
pub struct QueryDecl {
    pub name: String,
    pub description: Option<String>,
    pub instruction: Option<String>,
    pub params: Vec<Param>,
    pub match_clause: Vec<Clause>,
    pub return_clause: Vec<Projection>,
    pub order_clause: Vec<Ordering>,
    pub limit: Option<u64>,
    pub mutations: Vec<Mutation>,
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/oss-read-only/omnigraph/crates/omnigraph-compiler/src/query/ast.rs` and run `git -C /Users/amuldotexe/Desktop/oss-read-only/omnigraph ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/pi_agent_rust`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `oss-read-only/pi_agent_rust`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/pi_agent_rust/fuzz/fuzz_targets/fuzz_sse_parser.rs`; scan counts include rust_files=491, cargo_manifests=2, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
#![no_main]

//! Fuzz harness for `SseParser` — coverage-guided fuzzing of `feed()`/`flush()`.
//!
//! **Invariant under test:** Parsing a complete SSE stream in one call vs.
//! feeding it character-by-character MUST produce the same events (the
//! "chunking invariant" from the proptest suite, now under libFuzzer guidance).

use libfuzzer_sys::fuzz_target;
use pi::fuzz_exports::SseParser;

fuzz_target!(|data: &[u8]| {
    // Convert to UTF-8 lossily — SseParser works on &str, not raw bytes.
    let input = String::from_utf8_lossy(data);

    // --- Strategy 1: Feed the entire input at once ---
    let mut parser_whole = SseParser::new();
    let events_whole = parser_whole.feed(&input);
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/oss-read-only/pi_agent_rust/fuzz/fuzz_targets/fuzz_sse_parser.rs` and run `git -C /Users/amuldotexe/Desktop/oss-read-only/pi_agent_rust ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/sail`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `oss-read-only/sail`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/sail/crates/sail-catalog-iceberg/src/models/assert_last_assigned_field_id.rs`; scan counts include rust_files=1165, cargo_manifests=38, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
 * Generated by: https://openapi-generator.tech
 */

use serde::{Deserialize, Serialize};

use crate::models;

/// AssertLastAssignedFieldId : The table's last assigned column id must match the requirement's `last-assigned-field-id`
#[derive(Clone, Default, Debug, PartialEq, Serialize, Deserialize)]
pub struct AssertLastAssignedFieldId {
    #[serde(rename = "type", skip_serializing_if = "Option::is_none")]
    pub r#type: Option<String>,
    #[serde(rename = "last-assigned-field-id")]
    pub last_assigned_field_id: i32,
}

impl AssertLastAssignedFieldId {
    /// The table's last assigned column id must match the requirement's `last-assigned-field-id`
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/oss-read-only/sail/crates/sail-catalog-iceberg/src/models/assert_last_assigned_field_id.rs` and run `git -C /Users/amuldotexe/Desktop/oss-read-only/sail ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/zed-gpui`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust Module Architecture Slice From `oss-read-only/zed-gpui`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/zed-gpui/crates/collab/src/db/queries/buffers.rs`; scan counts include rust_files=1747, cargo_manifests=239, tree_sitter_query_files=147, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```rust
use super::*;
use anyhow::Context as _;
use prost::Message;
use text::{EditOperation, UndoOperation};

pub struct LeftChannelBuffer {
    pub channel_id: ChannelId,
    pub collaborators: Vec<proto::Collaborator>,
    pub connections: Vec<ConnectionId>,
}

impl Database {
    /// Open a channel buffer. Returns the current contents, and adds you to the list of people
    /// to notify on changes.
    pub async fn join_channel_buffer(
        &self,
        channel_id: ChannelId,
        user_id: UserId,
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/oss-read-only/zed-gpui/crates/collab/src/db/queries/buffers.rs` and run `git -C /Users/amuldotexe/Desktop/oss-read-only/zed-gpui ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/JobSearchGames`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/JobSearchGames`; scan counts include file_count=0, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/JobSearchGames ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/MCP-Zero`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/MCP-Zero`; scan counts include file_count=24, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/MCP-Zero ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ToolSandbox`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust-Adjacent Parser Reference From `personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ToolSandbox`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ToolSandbox/tool_sandbox/scenarios/insufficient_information_scenarios.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```text
                    "sender": RoleType.SYSTEM,
                    "recipient": RoleType.USER,
                    "content": USER_INSTRUCTION
                    + "Update the phone number of the last person you sent a message to to +10293847563. "
                    "You do not have any more information about that person.",
                },
                {
                    "sender": RoleType.USER,
                    "recipient": RoleType.AGENT,
                    "content": "Update the phone number of the last person I sent a message to to +10293847563",
                },
            ],
            tool_allow_list=[
                "get_current_timestamp",
                "modify_contact",
                "search_contacts",
            ],
            # Deny anything that can leak messages database
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ToolSandbox/tool_sandbox/scenarios/insufficient_information_scenarios.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ToolSandbox ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/contextweaver`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/accio-tools/ignore-references/git-ref-repo/contextweaver`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/contextweaver/docs/integration_puppetmaster.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
# Puppetmaster Integration

> Consume [Puppetmaster](https://github.com/dgenio/puppetmaster)-style job artifacts,
> worker summaries, logs, and follow-up reads through contextweaver so the LLM
> never sees raw multi-KB artifacts unless it explicitly asks for them.

## Why

Puppetmaster orchestrates long-running, multi-step jobs. Each job produces:

- **Worker summaries** (small, structured)
- **Execution logs** (often multi-KB)
- **Intermediate artifacts** (files, JSON blobs, traces)
- **Follow-up prompts** (conditional next steps)

Dumping all of this into the model context on every turn causes the same three
failures contextweaver exists to prevent:

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/contextweaver/docs/integration_puppetmaster.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/contextweaver ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/mcp-bench`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/accio-tools/ignore-references/git-ref-repo/mcp-bench`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/mcp-bench/mcp_servers/bibliomantic-mcp-server/bibliomantic_fastmcp.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
#!/usr/bin/env python3
"""
Bibliomantic MCP Server using FastMCP

A Model Context Protocol server that integrates I Ching divination with AI responses,
following the bibliomantic approach described in Philip K. Dick's "The Man in the High Castle".

This version uses the official MCP Python SDK's FastMCP framework for maximum simplicity
and professional compliance with the MCP specification.
"""

import logging
import sys
from typing import Optional

# Import the official FastMCP framework
from mcp.server.fastmcp import FastMCP

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/mcp-bench/mcp_servers/bibliomantic-mcp-server/bibliomantic_fastmcp.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/mcp-bench ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/algo-free-twitter-marination`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/algo-free-twitter-marination`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/algo-free-twitter-marination/refTaskDocs/S69_PARSELTONGUE_QUERY_COOKBOOK.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
# RD09: Parseltongue Query Cookbook

## A Practical Guide to Code Graph Analysis

This document captures all queries executed during real-world codebase analysis, serving as a reference for Parseltongue users.

---

## Table of Contents

1. [Setup & Installation](#1-setup--installation)
2. [Basic Usage](#2-basic-usage)
3. [Core HTTP Endpoints](#3-core-http-endpoints)
4. [Real-World Query Examples](#4-real-world-query-examples)
5. [Entity Key Format](#5-entity-key-format)
6. [Language Support](#6-language-support)
7. [Common Query Patterns](#7-common-query-patterns)

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/algo-free-twitter-marination/refTaskDocs/S69_PARSELTONGUE_QUERY_COOKBOOK.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/algo-free-twitter-marination ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/before-i-go-org-github`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/before-i-go-org-github`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/before-i-go-org-github/JsonFiles202508/RawDocs20250827/# Parselmouth_ A Revolutionary Rust-Based Browser... (1).md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
Of course. I have processed the refined "Parselmouth" framework brief. Here is the deep analysis and ideation you requested, produced through my optimized workflow.

# **Parselmouth: A Formal Blueprint for a Provably Secure, Post-Web UI Ecosystem**

## **Executive Summary**

The "Parselmouth" project represents a paradigm shift in application development, moving beyond mere performance enhancement to establish a new foundation of **provable security, architectural simplicity, and deterministic behavior** for the business application domain. By systematically excising the entire legacy web stack (HTML, CSS, JS, DOM), Parselmouth introduces a vertically integrated, Rust-native ecosystem. This architecture leverages compile-time guarantees to eliminate entire classes of runtime errors and security vulnerabilities, offering a level of integrity that is unattainable with current technologies.

The core of this vision is a trio of innovations: the **Parsel DSL**, a formally-defined UI grammar that makes invalid layouts unrepresentable; the **Horcrux Compiler**, which uses cryptographic principles to ensure component integrity; and the **Parselmouth Engine**, a minimalist CPU renderer built on a novel "Box Model Zero" that guarantees single-pass layout resolution. This document provides a rigorous technical deep-dive into this revolutionary architecture.

## **I. Strategic Rationale**

### **A. Market Opportunity & Value Proposition**

The target domain of business applications—dashboards, data-entry systems, and internal tooling—is currently served by a web stack that was designed for hypermedia documents, not stateful applications. This architectural mismatch creates significant and well-documented pain points 1:

* **DOM Overhead**: The DOM is a verbose, tree-structured API
...
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/before-i-go-org-github/JsonFiles202508/RawDocs20250827/# Parselmouth_ A Revolutionary Rust-Based Browser... (1).md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/before-i-go-org-github ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/dobby-subagent-code-summarizer`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/dobby-subagent-code-summarizer`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/dobby-subagent-code-summarizer/PARSELTONGUE_README.md`; scan counts include rust_files=53, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
# Parseltongue - Code Analysis CLI

## Overview

Parseltongue is an ultra-minimalist CLI toolkit designed for code analysis and temporal modification, supporting LLM-driven code transformation workflows. It provides a unified 6-tool pipeline packaged in a single binary.

## Download & Installation

### Binary Download (macOS Apple Silicon)

The project offers pre-compiled binaries available through GitHub Releases:

```bash
curl -L https://github.com/that-in-rust/parseltongue/releases/latest/download/parseltongue-macos-arm64 -o parseltongue
chmod +x parseltongue
sudo mv parseltongue /usr/local/bin/
parseltongue --help
```
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/dobby-subagent-code-summarizer/PARSELTONGUE_README.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/dobby-subagent-code-summarizer ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/fawkes-body-doubling-phoenix`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/fawkes-body-doubling-phoenix`; scan counts include file_count=2, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/fawkes-body-doubling-phoenix ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/graph-data-science`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/graph-data-science`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/graph-data-science/algo-params/similarity-params/src/main/java/org/neo4j/gds/similarity/knn/KnnNodePropertySpecParser.java`; scan counts include rust_files=1, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import static org.neo4j.gds.core.StringIdentifierValidations.validateNoWhiteCharacter;
import static org.neo4j.gds.utils.StringFormatting.formatWithLocale;

public final class KnnNodePropertySpecParser {

    private KnnNodePropertySpecParser() {}

    /**
     * User input is one of
     *     * {@code java.lang.String}
     *     * {@code java.util.List<java.lang.String>}
     *     * {@code java.util.Map<java.lang.String, java.lang.String>}
     *
     * The single string is parsed as a property name.
     * The list of strings is parsed as a list of property names.
     * The map of string to string is parsed as a map from property names to similarity metrics.
     */
    public static List<KnnNodePropertySpec> parse(@NotNull Object userInput) {
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/graph-data-science/algo-params/similarity-params/src/main/java/org/neo4j/gds/similarity/knn/KnnNodePropertySpecParser.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/graph-data-science ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/benchmarks/walk_hopper_v1/generate_code_sparse_data.py`; scan counts include rust_files=23, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[2]))

from benchmarks.walk_hopper_v1.common import (
    DEFAULT_DEGREE_PALETTE,
    DEFAULT_LAYER_COUNT,
    GRAPH_MODEL_CODE_SPARSE,
    build_degree_summary_now,
    build_layer_ranges_now,
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/benchmarks/walk_hopper_v1/generate_code_sparse_data.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-apoc-procedures-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-apoc-procedures-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-apoc-procedures-src/core/src/main/java/apoc/util/DateParseUtil.java`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import java.lang.invoke.MethodHandles;
import java.lang.invoke.MethodType;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.time.temporal.TemporalAccessor;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class DateParseUtil {

    private static Map<Class<? extends TemporalAccessor>, MethodHandle> parseDateMap = new ConcurrentHashMap<>();
    private static Map<Class<? extends TemporalAccessor>, MethodHandle> simpleParseDateMap = new ConcurrentHashMap<>();
    private static String METHOD_NAME = "parse";

    public static TemporalAccessor dateParse(String value, Class<? extends TemporalAccessor> date, String... formats) {
        try {
            if (formats != null && formats.length > 0) {
                for (String form : formats) {
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-apoc-procedures-src/core/src/main/java/apoc/util/DateParseUtil.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-apoc-procedures-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-gds-client-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-gds-client-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-gds-client-src/src/graphdatascience/procedure_surface/api/node_embedding/fastrp_endpoints.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
from graphdatascience.procedure_surface.api.estimation_result import EstimationResult


class FastRPEndpoints(ABC):
    @abstractmethod
    def mutate(
        self,
        G: GraphV2,
        mutate_property: str,
        embedding_dimension: int,
        iteration_weights: list[float] = [0.0, 1.0, 1.0],
        normalization_strength: float = 0.0,
        node_self_influence: float = 0.0,
        property_ratio: float = 0.0,
        feature_properties: list[str] | None = None,
        relationship_types: list[str] = ALL_TYPES,
        node_labels: list[str] = ALL_LABELS,
        sudo: bool = False,
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-gds-client-src/src/graphdatascience/procedure_surface/api/node_embedding/fastrp_endpoints.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-gds-client-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-ogm-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-ogm-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-ogm-src/core/src/main/java/org/neo4j/ogm/session/request/RowDataStatement.java`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
/**
 * @author Luanne Misquitta
 */
public class RowDataStatement implements Statement {

    private String statement;
    private OptimisticLockingConfig optimisticLockingConfig;
    private Map<String, Object> parameters;
    private String[] resultDataContents = new String[] { "row" };

    public RowDataStatement() {
    }

    public RowDataStatement(String statement, Map<String, Object> parameters) {
        this.statement = statement;
        this.parameters = parameters;
    }

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-ogm-src/core/src/main/java/org/neo4j/ogm/session/request/RowDataStatement.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-ogm-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/opencypher-src`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/opencypher-src`; scan counts include file_count=262, rust_files=0, cargo_manifests=0, candidate_paths=5.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/opencypher-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-arrow-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-arrow-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-arrow-src/c_glib/arrow-glib/timestamp-parser.cpp`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
 * under the License.
 */

#include <arrow-glib/timestamp-parser.hpp>

G_BEGIN_DECLS

/**
 * SECTION: timestamp-parser
 * @section_id: timestamp-parser-classes
 * @title: TimestamParser classes
 * @include: arrow-glib/arrow-glib.h
 *
 * #GArrowTimestampParser is a base class for parsing timestamp text.
 *
 * #GArrowStrptimeTimestampParser is a class for parsing timestamp
 * text used by the given stprtime(3) format.
 *
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-arrow-src/c_glib/arrow-glib/timestamp-parser.cpp` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-arrow-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-parquet-format-src`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-parquet-format-src`; scan counts include file_count=48, rust_files=0, cargo_manifests=0, candidate_paths=5.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-parquet-format-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/cayley-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/cayley-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/cayley-src/graph/gaedatastore/config.go`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
// See the License for the specific language governing permissions and
// limitations under the License.

package gaedatastore

import (
	"encoding/json"
	"fmt"
	"os"
	"strconv"
	"time"
)

// Config defines the behavior of cayley database instances.
type Config struct {
	DatabaseType       string
	DatabasePath       string
	DatabaseOptions    map[string]interface{}
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/cayley-src/graph/gaedatastore/config.go` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/cayley-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/dgraph-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/dgraph-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/dgraph-src/chunker/json_parser.go`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
	}, str)
}

// handleBasicFacetsType parses a facetVal to string/float64/bool/datetime type.
func handleBasicFacetsType(key string, facetVal interface{}) (*api.Facet, error) {
	var jsonValue interface{}
	var valueType api.Facet_ValType
	switch v := facetVal.(type) {
	case string:
		if t, err := types.ParseTime(v); err == nil {
			valueType = api.Facet_DATETIME
			jsonValue = t
		} else {
			facet, err := facets.FacetFor(key, strconv.Quote(v))
			if err != nil {
				return nil, err
			}

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/dgraph-src/chunker/json_parser.go` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/dgraph-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphblas-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphblas-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphblas-src/CUDA/select/GB_cuda_select_sparse.cpp`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphblas-src/CUDA/select/GB_cuda_select_sparse.cpp` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphblas-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gunrock-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gunrock-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gunrock-src/docs/sphinx/_extensions/nw_exhale/parse.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
# This file is part of exhale.  Copyright (c) 2017-2022, Stephen McDowell.             #
# Full BSD 3-Clause license available here:                                            #
#                                                                                      #
#                https://github.com/svenevs/exhale/blob/master/LICENSE                 #
########################################################################################

from __future__ import unicode_literals

from . import configs
from . import utils

import textwrap
from bs4 import BeautifulSoup

__all__       = ["walk", "convertDescriptionToRST", "getBriefAndDetailedRST"]


def walk(textRoot, currentTag, level, prefix=None, postfix=None, unwrapUntilPara=False):
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gunrock-src/docs/sphinx/_extensions/nw_exhale/parse.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gunrock-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/jemalloc-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/jemalloc-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/jemalloc-src/test/unit/conf_parse.c`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
#include "test/jemalloc_test.h"

#include "jemalloc/internal/conf.h"

TEST_BEGIN(test_conf_handle_bool_true) {
	bool result = false;
	bool err = conf_handle_bool("true", sizeof("true") - 1, &result);
	expect_false(err, "conf_handle_bool should succeed for \"true\"");
	expect_true(result, "result should be true");
}
TEST_END

TEST_BEGIN(test_conf_handle_bool_false) {
	bool result = true;
	bool err = conf_handle_bool("false", sizeof("false") - 1, &result);
	expect_false(err, "conf_handle_bool should succeed for \"false\"");
	expect_false(result, "result should be false");
}
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/jemalloc-src/test/unit/conf_parse.c` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/jemalloc-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics_docs-src`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics_docs-src`; scan counts include file_count=85, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics_docs-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v2_driver-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust-Adjacent Parser Reference From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v2_driver-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v2_driver-src/src/main/java/org/ldbcouncil/snb/driver/workloads/interactive/queries/LdbcDelete1RemovePerson.java`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```text
import org.ldbcouncil.snb.driver.workloads.interactive.LdbcOperation;
import com.google.common.collect.ImmutableMap;

import com.fasterxml.jackson.annotation.JsonProperty;

public class LdbcDelete1RemovePerson extends LdbcOperation<LdbcNoResult>{
    public static final int TYPE = 1009;
    public static final String PERSON_ID = "personId";

    private final long removePersonIdD1;

    public LdbcDelete1RemovePerson(
        @JsonProperty("removePersonIdD1")    long removePersonIdD1
    )
    {
        this.removePersonIdD1 = removePersonIdD1;
    }

```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v2_driver-src/src/main/java/org/ldbcouncil/snb/driver/workloads/interactive/queries/LdbcDelete1RemovePerson.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v2_driver-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/memgraph-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/memgraph-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/memgraph-src/licenses/third-party/cppitertools/LICENSE.md`; scan counts include rust_files=28, cargo_manifests=3, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
Copyright (c) 2013, Ryan Haining, Aaron Josephs, Google
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

  Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

  Redistributions in binary form must reproduce the above copyright notice, this
  list of conditions and the following disclaimer in the documentation and/or
  other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/memgraph-src/licenses/third-party/cppitertools/LICENSE.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/memgraph-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/networkit-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/networkit-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/networkit-src/include/networkit/algebraic/Semirings.hpp`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
/*
 * Semirings.hpp
 *
 *  Created on: May 31, 2016
 *      Author: Michael Wegner (michael.wegner@student.kit.edu)
 */

#ifndef NETWORKIT_ALGEBRAIC_SEMIRINGS_HPP_
#define NETWORKIT_ALGEBRAIC_SEMIRINGS_HPP_

#include <algorithm>

// *****************************************************
// 					Semiring Definitions
// *****************************************************

/**
 * @ingroup algebraic
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/networkit-src/include/networkit/algebraic/Semirings.hpp` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/networkit-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/python-graphblas-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/python-graphblas-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/python-graphblas-src/graphblas/core/operator/semiring.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import itertools
import re

from ... import _STANDARD_OPERATOR_NAMES, binary, monoid, op, semiring
from ...dtypes import (
    BOOL,
    FP32,
    FP64,
    INT8,
    INT16,
    INT32,
    INT64,
    UINT8,
    UINT16,
    UINT32,
    UINT64,
    _supports_complex,
)
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/python-graphblas-src/graphblas/core/operator/semiring.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/python-graphblas-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/risingwave-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/risingwave-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/risingwave-src/dashboard/hook/useErrorToast.ts`; scan counts include rust_files=2636, cargo_manifests=80, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
 * limitations under the License.
 */

import { AlertStatus, useToast } from "@chakra-ui/react"
import { useCallback } from "react"

export default function useErrorToast() {
  const toast = useToast()

  return useCallback(
    (e: any, status: AlertStatus = "error") => {
      let title: string
      let description: string | undefined

      if (e instanceof Error) {
        title = e.message
        description = e.cause?.toString()
      } else {
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/risingwave-src/dashboard/hook/useErrorToast.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/risingwave-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/snap-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/snap-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/snap-src/glib-adv/prologparser.cpp`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
/////////////////////////////////////////////////
// Includes
#include "prologparser.h"

TPlChDef::TPlChDef(){
  // prepare character types (ChTypeV)
  ChTypeV.Gen(TPlChDef::MxChar-TPlChDef::MnChar+1);
  IAssert(TPlChDef::MnChar==0); IAssert(TPlChDef::MxChar==255);
  for (int Ch=MnChar; Ch<=MxChar; Ch++){ChTypeV[Ch]=plctUnDef;}
  for (int Ch=MnChar; Ch<=' '; Ch++){ChTypeV[Ch]=plctBl;}
  ChTypeV[EofCh]=plctEof;
  ChTypeV['!']=plctSolo;
  ChTypeV['"']=plctDQuo;
  ChTypeV['#']=plctSym;
  ChTypeV['$']=plctSym;
  ChTypeV['%']=plctComm;
  ChTypeV['&']=plctSym;
  ChTypeV['\'']=plctSQuo;
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/snap-src/glib-adv/prologparser.cpp` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/snap-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/terminusdb-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/terminusdb-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/terminusdb-src/src/rust/terminusdb-community/src/path/parse.rs`; scan counts include rust_files=37, cargo_manifests=4, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
use nom::bytes::complete::{tag, take_while, take_while1};
use nom::multi::separated_list1;
use nom::sequence::preceded;
use nom::{
    branch::alt,
    combinator::{map, map_res},
    error::ErrorKind,
    sequence::{delimited, pair, separated_pair, terminated},
    IResult,
};
use std::rc::Rc;

/*

P := '.' | String
Q,R := P> | <P | Q,R | Q;R | Q+ | Q* | Q{N,M} | P@T

 */
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/terminusdb-src/src/rust/terminusdb-community/src/path/parse.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/terminusdb-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/mission-grindelwald`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/mission-grindelwald`; scan counts include file_count=3, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/mission-grindelwald ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-toposort-kahns-algorithm`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust Module Architecture Slice From `personal-repos-lane/nostd-toposort-kahns-algorithm`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-toposort-kahns-algorithm/src/error.rs`; scan counts include rust_files=5, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```rust
//! Error types for topological sort operations
//!
//! This module defines structured error types using thiserror for
//! clear, actionable error reporting.

use core::fmt;

/// Errors that can occur during topological sort operations
#[derive(Debug, Clone, PartialEq, Eq)]
pub enum TopoSortError {
    /// Graph contains a cycle, making topological sort impossible
    ///
    /// # Details
    /// - Contains the number of nodes that were successfully processed
    /// - Remaining nodes form one or more cycles
    CycleDetected {
        /// Number of nodes successfully sorted before cycle was detected
        processed_count: usize,
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-toposort-kahns-algorithm/src/error.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/nostd-toposort-kahns-algorithm ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/1broseidon__cymbal`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/1broseidon__cymbal`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/1broseidon__cymbal/internal/tsgrammars/tree-sitter-dart/src/parser.c`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#include "tree_sitter/parser.h"

#if defined(__GNUC__) || defined(__clang__)
#pragma GCC diagnostic ignored "-Wmissing-field-initializers"
#endif

#define LANGUAGE_VERSION 14
#define STATE_COUNT 3577
#define LARGE_STATE_COUNT 494
#define SYMBOL_COUNT 524
#define ALIAS_COUNT 1
#define TOKEN_COUNT 163
#define EXTERNAL_TOKEN_COUNT 7
#define FIELD_COUNT 20
#define MAX_ALIAS_SEQUENCE_LENGTH 10
#define PRODUCTION_ID_COUNT 98

enum ts_symbol_identifiers {
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/1broseidon__cymbal/internal/tsgrammars/tree-sitter-dart/src/parser.c` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/1broseidon__cymbal ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AbstractMachinesLab__tree-sitter-erlang`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AbstractMachinesLab__tree-sitter-erlang`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AbstractMachinesLab__tree-sitter-erlang/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AbstractMachinesLab__tree-sitter-erlang/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AbstractMachinesLab__tree-sitter-erlang ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__android-tree-sitter`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__android-tree-sitter`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__android-tree-sitter/android-tree-sitter/src/main/cpp/ts_parser.cc`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=4, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
/*
 *  This file is part of android-tree-sitter.
 *
 *  android-tree-sitter library is free software; you can redistribute it and/or
 *  modify it under the terms of the GNU Lesser General Public
 *  License as published by the Free Software Foundation; either
 *  version 2.1 of the License, or (at your option) any later version.
 *
 *  android-tree-sitter library is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 *  Lesser General Public License for more details.
 *
 *   You should have received a copy of the GNU General Public License
 *  along with android-tree-sitter.  If not, see <https://www.gnu.org/licenses/>.
 */

#include <atomic>
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__android-tree-sitter/android-tree-sitter/src/main/cpp/ts_parser.cc` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__android-tree-sitter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndyInternet__indexer`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndyInternet__indexer`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndyInternet__indexer/src/indexer/parsing/parser.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
"""Tree-sitter parsing wrapper."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import tree_sitter

from .languages import detect_language, get_parser


@dataclass
class ParseResult:
    tree: tree_sitter.Tree
    source: bytes
    language: str
    file_path: str
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndyInternet__indexer/src/indexer/parsing/parser.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndyInternet__indexer ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diffguardian`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diffguardian`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diffguardian/src/parsers/ast-mapper.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diffguardian/src/parsers/ast-mapper.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diffguardian ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Benjamin-Davies__tree-sitter-relview`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Benjamin-Davies__tree-sitter-relview`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Benjamin-Davies__tree-sitter-relview/bindings/c/tree_sitter/tree-sitter-relview.h`; scan counts include rust_files=4, cargo_manifests=2, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_RELVIEW_H_
#define TREE_SITTER_RELVIEW_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_relview(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_RELVIEW_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Benjamin-Davies__tree-sitter-relview/bindings/c/tree_sitter/tree-sitter-relview.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Benjamin-Davies__tree-sitter-relview ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/BrianHicks__tree-grepper`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/BrianHicks__tree-grepper`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/BrianHicks__tree-grepper/src/main.rs`; scan counts include rust_files=9, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
mod language;
mod tree_view;

use anyhow::{bail, Context, Result};
use cli::{Invocation, QueryFormat, QueryOpts, TreeOpts};
use crossbeam::channel;
use language::Language;
use rayon::iter::{IntoParallelRefIterator, ParallelIterator};
use std::env;
use std::fs;
use std::io::{self, BufWriter, Write};
use tree_sitter::Parser;

#[global_allocator]
static ALLOCATOR: bump_alloc::BumpAlloc = bump_alloc::BumpAlloc::new();

fn main() {
    let mut buffer = BufWriter::new(io::stdout());
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/BrianHicks__tree-grepper/src/main.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/BrianHicks__tree-grepper ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ChronosTeamx__FuncUndo`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ChronosTeamx__FuncUndo`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ChronosTeamx__FuncUndo/chronos/src/worker/astTraverser.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import type { SyntaxNode } from 'web-tree-sitter';
import { ParsedFunction } from '../lib/types';
import { generateStructuralHash } from './semanticHasher';
import { ImportedSymbol } from '../lib/types';

const FUNCTION_TYPES = new Set(['function_declaration', 'arrow_function', 'method_definition']);

function extractFunctionName(node: SyntaxNode): string {
  const nameNode = node.childForFieldName('name');
  if (nameNode) return nameNode.text;

  if (node.type === 'arrow_function' && node.parent?.type === 'variable_declarator') {
    const idNode = node.parent.childForFieldName('name');
    if (idNode) return idNode.text;
  }

  return 'anonymous_function';
}
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ChronosTeamx__FuncUndo/chronos/src/worker/astTraverser.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ChronosTeamx__FuncUndo ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeGraphContext__CodeGraphContext`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeGraphContext__CodeGraphContext`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeGraphContext__CodeGraphContext/src/codegraphcontext/tools/tree_sitter_parser.py`; scan counts include rust_files=12, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
# src/codegraphcontext/tools/tree_sitter_parser.py
"""Tree-sitter parser dispatch by language name."""

from pathlib import Path
from typing import TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from tree_sitter import Language

from ..utils.tree_sitter_manager import get_tree_sitter_manager


class TreeSitterParser:
    """A generic parser wrapper for a specific language using tree-sitter."""

    def __init__(self, language_name: str):
        self.language_name = language_name
        self.ts_manager = get_tree_sitter_manager()
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeGraphContext__CodeGraphContext/src/codegraphcontext/tools/tree_sitter_parser.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeGraphContext__CodeGraphContext ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DNSZLSK__lexluthor`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DNSZLSK__lexluthor`; scan counts include file_count=125, rust_files=0, cargo_manifests=0, candidate_paths=2.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DNSZLSK__lexluthor ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DeusData__codebase-memory-mcp`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DeusData__codebase-memory-mcp`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DeusData__codebase-memory-mcp/internal/cbm/vendored/common/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DeusData__codebase-memory-mcp/internal/cbm/vendored/common/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DeusData__codebase-memory-mcp ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/EmranMR__tree-sitter-blade`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/EmranMR__tree-sitter-blade`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/EmranMR__tree-sitter-blade/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/EmranMR__tree-sitter-blade/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/EmranMR__tree-sitter-blade ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Flakebi__tree-sitter-tablegen`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Flakebi__tree-sitter-tablegen`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Flakebi__tree-sitter-tablegen/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Flakebi__tree-sitter-tablegen/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Flakebi__tree-sitter-tablegen ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GhentCDH__tree-sitter-wikitext`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GhentCDH__tree-sitter-wikitext`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GhentCDH__tree-sitter-wikitext/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GhentCDH__tree-sitter-wikitext/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GhentCDH__tree-sitter-wikitext ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/HelgeSverre__tree-sitter-applescript`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/HelgeSverre__tree-sitter-applescript`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/HelgeSverre__tree-sitter-applescript/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/HelgeSverre__tree-sitter-applescript/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/HelgeSverre__tree-sitter-applescript ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Hubro__tree-sitter-robot`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Hubro__tree-sitter-robot`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Hubro__tree-sitter-robot/bindings/c/tree_sitter/tree-sitter-robot.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_ROBOT_H_
#define TREE_SITTER_ROBOT_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_robot(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_ROBOT_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Hubro__tree-sitter-robot/bindings/c/tree_sitter/tree-sitter-robot.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Hubro__tree-sitter-robot ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Isopod__tree-sitter-pascal`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Isopod__tree-sitter-pascal`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Isopod__tree-sitter-pascal/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Isopod__tree-sitter-pascal/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Isopod__tree-sitter-pascal ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Joakker__tree-sitter-json5`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Joakker__tree-sitter-json5`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Joakker__tree-sitter-json5/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Joakker__tree-sitter-json5/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Joakker__tree-sitter-json5 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Julian__lean.nvim`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Julian__lean.nvim`; scan counts include file_count=324, rust_files=0, cargo_manifests=0, candidate_paths=11.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Julian__lean.nvim ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/LdBeth__tree-sitter-rnc`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/LdBeth__tree-sitter-rnc`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/LdBeth__tree-sitter-rnc/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/LdBeth__tree-sitter-rnc/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/LdBeth__tree-sitter-rnc ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Manikanta-Reddy-Pasala__AiForgeMemory`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Manikanta-Reddy-Pasala__AiForgeMemory`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Manikanta-Reddy-Pasala__AiForgeMemory/aiforge_memory/features/symbol/queries/java.scm`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=4, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```scheme
; tree-sitter Java query — symbols + imports + calls

; class
(class_declaration
  name: (identifier) @class.name) @class.def

; interface (captured separately so the graph distinguishes interface
; from concrete class — useful for Spring DI / mock-resolution lookups)
(interface_declaration
  name: (identifier) @interface.name) @interface.def

; enum
(enum_declaration
  name: (identifier) @enum.name) @enum.def

; annotation type
(annotation_type_declaration
  name: (identifier) @annotation.name) @annotation.def
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Manikanta-Reddy-Pasala__AiForgeMemory/aiforge_memory/features/symbol/queries/java.scm` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Manikanta-Reddy-Pasala__AiForgeMemory ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Neverdecel__CodeRAG`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Neverdecel__CodeRAG`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Neverdecel__CodeRAG/coderag/chunking/python_ast.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
"""Symbol extraction for Python using the standard library ``ast``.

Faster and more accurate than tree-sitter for Python, with zero extra dependencies.
Emits a span per function/method and per class (the class span's non-method lines — its
docstring and class-level attributes — become their own chunks via line ownership).
"""

from __future__ import annotations

import ast
from typing import List, cast

from coderag.chunking.base import SymbolSpan


def extract_spans(text: str) -> List[SymbolSpan]:
    tree = ast.parse(text)  # may raise SyntaxError -> caller falls back to windows
    spans: List[SymbolSpan] = []
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Neverdecel__CodeRAG/coderag/chunking/python_ast.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Neverdecel__CodeRAG ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OXY2DEV__tree-sitter-lua_patterns`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OXY2DEV__tree-sitter-lua_patterns`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OXY2DEV__tree-sitter-lua_patterns/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OXY2DEV__tree-sitter-lua_patterns/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OXY2DEV__tree-sitter-lua_patterns ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OpenModelica__tree-sitter-modelica`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OpenModelica__tree-sitter-modelica`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OpenModelica__tree-sitter-modelica/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OpenModelica__tree-sitter-modelica/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OpenModelica__tree-sitter-modelica ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PranavNagothu__FlakeShield`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PranavNagothu__FlakeShield`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PranavNagothu__FlakeShield/analyzer/internal/parser/parser.go`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
// Package parser wraps go-tree-sitter to provide language-agnostic AST parsing
// for the FlakeShield static analysis engine.
package parser

import (
	"context"
	"fmt"

	sitter "github.com/smacker/go-tree-sitter"
	"github.com/smacker/go-tree-sitter/python"
	"github.com/smacker/go-tree-sitter/typescript/typescript"
)

// Language represents a supported analysis target.
type Language string

const (
	Python     Language = "python"
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PranavNagothu__FlakeShield/analyzer/internal/parser/parser.go` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PranavNagothu__FlakeShield ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RRethy__nvim-treesitter-textsubjects`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RRethy__nvim-treesitter-textsubjects`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RRethy__nvim-treesitter-textsubjects/queries/c/textsubjects-container-inner.scm`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=57, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```scheme
; {} blocks
([
    (compound_statement . "{" . (_) @_start @_end (_)? @_end . "}" .)
    (declaration_list . "{" . (_) @_start @_end (_)? @_end . "}" . )
    (enumerator_list . "{" . (_) @_start @_end (_)? @_end . "}" . )
    (field_declaration_list . "{" . (_) @_start @_end (_)? @_end . "}" . )
    (initializer_list . "{" . (_) @_start @_end (_)? @_end . "}" . )
] (#make-range! "range" @_start @_end))

; () blocks
([
    (argument_list . "(" . (_) @_start @_end (_)? @_end . ")" . )
    (parameter_list . "(" . (_) @_start @_end (_)? @_end . ")" . )
    (sizeof_expression (parenthesized_expression (_) @_start @_end)) ; sizeof(expr)
    (sizeof_expression . "(" . (_) @_start @_end . ")" . ) ; sizeof(type)
    (do_statement condition: (parenthesized_expression (_) @_start @_end))
    (if_statement condition: (parenthesized_expression (_) @_start @_end))
    (switch_statement condition: (parenthesized_expression (_) @_start @_end))
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RRethy__nvim-treesitter-textsubjects/queries/c/textsubjects-container-inner.scm` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RRethy__nvim-treesitter-textsubjects ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RooCodeInc__Roo-Code`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RooCodeInc__Roo-Code`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RooCodeInc__Roo-Code/apps/cli/src/commands/cli/__tests__/parse-stdin-command.test.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import { parseStdinStreamCommand, shouldSendMessageAsAskResponse } from "../stdin-stream.js"

describe("parseStdinStreamCommand", () => {
	describe("valid commands", () => {
		it("parses a start command", () => {
			const result = parseStdinStreamCommand(
				JSON.stringify({ command: "start", requestId: "req-1", prompt: "hello" }),
				1,
			)
			expect(result).toEqual({ command: "start", requestId: "req-1", prompt: "hello" })
		})

		it("parses a start command with taskId", () => {
			const result = parseStdinStreamCommand(
				JSON.stringify({
					command: "start",
					requestId: "req-task-id",
					prompt: "hello",
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RooCodeInc__Roo-Code/apps/cli/src/commands/cli/__tests__/parse-stdin-command.test.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RooCodeInc__Roo-Code ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/SonarSource__sonarqube`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/SonarSource__sonarqube`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/SonarSource__sonarqube/plugins/sonar-xoo-plugin/src/main/java/org/sonar/xoo/lang/CpdTokenizerSensor.java`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import org.sonar.api.batch.sensor.Sensor;
import org.sonar.api.batch.sensor.SensorContext;
import org.sonar.api.batch.sensor.SensorDescriptor;
import org.sonar.api.batch.sensor.cpd.NewCpdTokens;
import org.sonar.xoo.Xoo;

/**
 * Tokenize files for CPD
 */
public class CpdTokenizerSensor implements Sensor {

  private void tokenize(InputFile inputFile, SensorContext context) {
    int lineIdx = 1;
    NewCpdTokens newCpdTokens = context.newCpdTokens().onFile(inputFile);
    try {
      StringBuilder sb = new StringBuilder();
      for (String line : FileUtils.readLines(inputFile.file(), inputFile.charset())) {
        int startOffset = 0;
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/SonarSource__sonarqube/plugins/sonar-xoo-plugin/src/main/java/org/sonar/xoo/lang/CpdTokenizerSensor.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/SonarSource__sonarqube ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/TabbyML__tabby`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/TabbyML__tabby`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/TabbyML__tabby/clients/tabby-agent/src/dataStore/dataFile.ts`; scan counts include rust_files=272, cargo_manifests=19, tree_sitter_query_files=9, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import { isBrowser } from "../env";
import { getLogger } from "../logger";

export class FileDataStore extends EventEmitter {
  private readonly logger = getLogger("DataStore");
  private watcher?: ReturnType<typeof chokidar.watch>;

  constructor(private readonly filepath: string) {
    super();
  }

  async read(): Promise<unknown> {
    try {
      const json = await fs.readJson(this.filepath, { throws: false });
      return json ?? {};
    } catch (err) {
      this.logger.warn(`Failed to read ${this.filepath}: ${err}`);
      return {};
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/TabbyML__tabby/clients/tabby-agent/src/dataStore/dataFile.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/TabbyML__tabby ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/UserNobody14__tree-sitter-dart`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/UserNobody14__tree-sitter-dart`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/UserNobody14__tree-sitter-dart/assets/tree-sitter.js`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```javascript
var Module=void 0!==Module?Module:{},TreeSitter=function(){var e,t="object"==typeof window?{currentScript:window.document.currentScript}:null;class Parser{constructor(){this.initialize()}initialize(){throw new Error("cannot construct a Parser before calling `init()`")}static init(r){return e||(Module=Object.assign({},Module,r),e=new Promise(e=>{var r,n={};for(r in Module)Module.hasOwnProperty(r)&&(n[r]=Module[r]);var s,o,_=[],a="./this.program",u=function(e,t){throw t},i=!1,l=!1;i="object"==typeof window,l="function"==typeof importScripts,s="object"==typeof process&&"object"==typeof process.versions&&"string"==typeof process.versions.node,o=!i&&!s&&!l;var d,c,m,f,p,h="";s?(h=l?require("path").dirname(h)+"/":__dirname+"/",d=function(e,t){return f||(f=require("fs")),p||(p=require("path")),e=p.normalize(e),f.readFileSync(e,t?null:"utf8")},m=function(e){var t=d(e,!0);return t.buffer||(t=new Uint8Array(t)),k(t.buffer),t},process.argv.length>1&&(a=process.argv[1].replace(/\\/g,"/")),_=process.argv.slice(2),"undefined"!=typeof module&&(module.exports=Module),u=function(e){process.exit(e)},Module.inspect=function(){return"[Emscripten Module object]"}):o?("undefined"!=typeof read&&(d=function(e){return read(e)}),m=function(e){var t;return"function"==typeof readbuffer?new Uint8Array(readbuffer(e)):(k("object"==typeof(t=read(e,"binary"))),t)},"undefined"!=typeof scriptArgs?_=scriptArgs:void 0!==arguments&&(_=arguments),"function"==typeof quit&&(u=function(e){quit(e)}),"undefined"!=typeof print&&("undefined"==typeof console&&(console={}),console.log=print,console.warn=console.error="undefined"!=typeof printErr?printErr:print)):(i||l)&&(l?h=self.location.href:void 0!==t&&t.currentScript&&(h=t.currentScript.src),h=0!==h.indexOf("blob:")?h.substr(0,h.lastIndexOf("/")+1):"",d=function(
...
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/UserNobody14__tree-sitter-dart/assets/tree-sitter.js` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/UserNobody14__tree-sitter-dart ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/WhatsApp__tree-sitter-erlang`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/WhatsApp__tree-sitter-erlang`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/WhatsApp__tree-sitter-erlang/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
// @generated

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
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/WhatsApp__tree-sitter-erlang/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/WhatsApp__tree-sitter-erlang ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/YPYT1__EverMind`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/YPYT1__EverMind`; scan counts include file_count=108, rust_files=0, cargo_manifests=0, candidate_paths=2.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/YPYT1__EverMind ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/acp-protocol__acp-cli`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/acp-protocol__acp-cli`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/acp-protocol__acp-cli/src/ast/languages/go.rs`; scan counts include rust_files=108, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
//! @acp:layer parsing

use super::{node_text, LanguageExtractor};
use crate::ast::{ExtractedSymbol, FunctionCall, Import, Parameter, SymbolKind, Visibility};
use crate::error::Result;
use tree_sitter::{Language, Node, Tree};

/// Go language extractor
pub struct GoExtractor;

impl LanguageExtractor for GoExtractor {
    fn language(&self) -> Language {
        tree_sitter_go::LANGUAGE.into()
    }

    fn name(&self) -> &'static str {
        "go"
    }
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/acp-protocol__acp-cli/src/ast/languages/go.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/acp-protocol__acp-cli ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/afnanenayet__diffsitter`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/afnanenayet__diffsitter`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/afnanenayet__diffsitter/plugins/tree-sitter-mcp/agents/ast-explorer.md`; scan counts include rust_files=35, cargo_manifests=2, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
---
name: ast-explorer
description: "Explores code structure using tree-sitter AST navigation. Use when the user asks to analyze code structure, find symbols, understand scope nesting, or run tree-sitter queries across files."
tools: Read, Glob, Grep
model: sonnet
maxTurns: 15
effort: medium
---

You are an AST exploration agent with access to tree-sitter MCP tools. You can structurally navigate and analyze source code across 14+ languages.

Your workflow:
1. Use `list_symbols` to get an overview of what a file defines
2. Use `get_definition` to read specific symbols
3. Use `get_scope` and `navigate` to understand nesting and relationships
4. Use `query` for complex structural pattern matching

Always prefer the MCP tools over reading raw file text when you need structural information. The MCP tools give you precise AST-level information that's language-aware.
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/afnanenayet__diffsitter/plugins/tree-sitter-mcp/agents/ast-explorer.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/afnanenayet__diffsitter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aishasurve2007__codebase-agent`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aishasurve2007__codebase-agent`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aishasurve2007__codebase-agent/src/ingestion/parser.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
"""
Code parser (tree-sitter).

Turns a Python source file into a list of *definitions* -- functions, classes,
and methods -- each with the exact source text and 1-indexed start/end lines.
Those line numbers are what make citations exact and un-hallucinatable later.

It handles the real-world cases that trip up naive parsing:
  - methods inside classes  (named "ClassName.method", type "method")
  - decorators              (@app.route etc. -> included in the chunk + lines)
  - nested functions        (found via full-tree recursion)
  - module-level imports     (collected into one "module" context chunk)

Run standalone to inspect a repo's definitions:
    python -m src.ingestion.parser path/to/repo_dir
"""
import tree_sitter_python as tspython
from tree_sitter import Language, Parser
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aishasurve2007__codebase-agent/src/ingestion/parser.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aishasurve2007__codebase-agent ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/albfan__rust-tree-sitter-ast-viewer`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/albfan__rust-tree-sitter-ast-viewer`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/albfan__rust-tree-sitter-ast-viewer/fixtures/tree-sitter-c/grammar.js`; scan counts include rust_files=3, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```javascript
  SHIFT: 9,
  ADD: 10,
  MULTIPLY: 11,
  CAST: 12,
  UNARY: 13,
  CALL: 14,
  FIELD: 15,
  SUBSCRIPT: 16
};

module.exports = grammar({
  name: 'c',

  extras: $ => [
    /\s/,
    $.comment,
  ],

```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/albfan__rust-tree-sitter-ast-viewer/fixtures/tree-sitter-c/grammar.js` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/albfan__rust-tree-sitter-ast-viewer ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/alexpovel__srgn`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/alexpovel__srgn`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/alexpovel__srgn/docs/python_cond_query.scm`; scan counts include rust_files=47, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```scheme
(if_statement
  consequence: (block
    (return_statement (identifier)))
  alternative: (else_clause
    body: (block
      (return_statement (identifier))))) @cond
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/alexpovel__srgn/docs/python_cond_query.scm` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/alexpovel__srgn ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/arborist-ts__arborist.nvim`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/arborist-ts__arborist.nvim`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/arborist-ts__arborist.nvim/queries/ada/folds.scm`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=1182, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/arborist-ts__arborist.nvim/queries/ada/folds.scm` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/arborist-ts__arborist.nvim ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bakhliustov__askgraph`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bakhliustov__askgraph`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bakhliustov__askgraph/src/askgraph/indexing/parsers.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
"""Tree-sitter based structural parsing (extensible).

Goal (inspired by Graphify): extract real entities (Module, Function, Class, Method)
and basic relationships (imports, contains) instead of blind text chunks.
This enables better "god node" detection, neighborhood expansion, and reports.

Core language: Python (always available).
Additional languages (JS/TS, etc.) loaded if the optional tree-sitter-* packages
from the [tree-sitter-full] extra are installed.
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Any

from tree_sitter import Language, Parser, Tree
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bakhliustov__askgraph/src/askgraph/indexing/parsers.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bakhliustov__askgraph ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bennypowers__tree-sitter-handlebars`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bennypowers__tree-sitter-handlebars`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bennypowers__tree-sitter-handlebars/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bennypowers__tree-sitter-handlebars/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bennypowers__tree-sitter-handlebars ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/biomejs__gritql`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/biomejs__gritql`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/biomejs__gritql/crates/cli/src/commands/parse.rs`; scan counts include rust_files=415, cargo_manifests=42, tree_sitter_query_files=48, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
use crate::{flags::GlobalFormatFlags, jsonl::JSONLineMessenger, resolver::GritModuleResolver};
use anyhow::{bail, Result};
use clap::Args;
use grit_util::Position;
use marzano_core::{
    api::{AnalysisLog, MatchResult, PatternInfo},
    parse::parse_input_file,
};
use marzano_language::target_language::{PatternLanguage, TargetLanguage};
use marzano_messenger::{
    emit::{Messager, VisibilityLevels},
    output_mode::OutputMode,
};
use serde::{Deserialize, Serialize};
use std::io;
use std::path::PathBuf;
use tokio::fs;

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/biomejs__gritql/crates/cli/src/commands/parse.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/biomejs__gritql ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/buzz-language__tree-sitter-buzz`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/buzz-language__tree-sitter-buzz`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/buzz-language__tree-sitter-buzz/src/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/buzz-language__tree-sitter-buzz/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/buzz-language__tree-sitter-buzz ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/camdencheek__tree-sitter-go-mod`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/camdencheek__tree-sitter-go-mod`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/camdencheek__tree-sitter-go-mod/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/camdencheek__tree-sitter-go-mod/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/camdencheek__tree-sitter-go-mod ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cdeust__automatised-pipeline`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cdeust__automatised-pipeline`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cdeust__automatised-pipeline/src/parser/c/extract/g1.rs`; scan counts include rust_files=122, cargo_manifests=3, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
// parser::c::extract::g1 — see ../extract/mod.rs.

use tree_sitter::Node;
use crate::parser::*;      // ExtractedNode, ExtractedRef, node_text, qual, LABEL_*, …
use super::super::*;       // parent module: Ctx, TS_* consts, kept helpers
use super::*;              // sibling extract fns (glob re-export)


pub(crate) fn extract_top(ctx: &mut Ctx, parent: Node, scope: &str) {
    let mut cursor = parent.walk();
    for child in parent.children(&mut cursor) {
        match child.kind() {
            TS_STRUCT | TS_UNION => extract_struct(ctx, child, scope, LABEL_STRUCT),
            TS_ENUM => extract_enum(ctx, child, scope),
            TS_TYPEDEF => extract_typedef(ctx, child, scope),
            TS_FUNCTION_DEF => extract_function(ctx, child, scope),
            TS_INCLUDE => extract_include(ctx, child, scope),
            TS_FUNCTION_DECL => {
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cdeust__automatised-pipeline/src/parser/c/extract/g1.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cdeust__automatised-pipeline ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cocoindex-io__cocoindex-code`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cocoindex-io__cocoindex-code`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cocoindex-io__cocoindex-code/tests/e2e_docker/test_docker_workspace.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
        ["ls", "/var/cocoindex/cache/sentence-transformers"],
    )
    assert check.returncode == 0
    # At least one model directory should be present from the bake stage.
    assert check.stdout.strip() != ""

    # Daemon log should not contain a "Downloading" line.
    log_result = subprocess.run(
        ["docker", "logs", container],
        capture_output=True,
        text=True,
        check=True,
    )
    # sentence-transformers prints "Downloading" when it fetches a model. A
    # missing bake would trigger that.
    assert "Downloading" not in log_result.stdout
    assert "Downloading" not in log_result.stderr

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cocoindex-io__cocoindex-code/tests/e2e_docker/test_docker_workspace.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cocoindex-io__cocoindex-code ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/constantitus__tree-sitter-jai`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/constantitus__tree-sitter-jai`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/constantitus__tree-sitter-jai/bindings/c/tree-sitter-jai.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_JAI_H_
#define TREE_SITTER_JAI_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_jai(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_JAI_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/constantitus__tree-sitter-jai/bindings/c/tree-sitter-jai.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/constantitus__tree-sitter-jai ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/crystal-lang-tools__crystal-tree-sitter`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/crystal-lang-tools__crystal-tree-sitter`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/crystal-lang-tools__crystal-tree-sitter`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
N/A: no source file selected during bounded scan.
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/crystal-lang-tools__crystal-tree-sitter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` if this repo changes later.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cyberNoman__universal-code-review-graph`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cyberNoman__universal-code-review-graph`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cyberNoman__universal-code-review-graph/qa-agents/QA-MASTER-PLAN.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text

## Launch Readiness Validation

This directory contains **5 QA agent prompts** — one for each AI model. Paste each file into its respective AI and let it run through every test. All 5 must return **PASS** before we launch.

| Agent File | AI Model | Focus Area |
|------------|----------|------------|
| `claude-qa-agent.md` | Claude / Claude Code | Architecture + Security + Edge cases |
| `kimi-k2-qa-agent.md` | Kimi K2.5 | MCP protocol compliance + Token savings validation |
| `codex-qa-agent.md` | OpenAI Codex / ChatGPT | Code correctness + Python best practices |
| `qwen-qa-agent.md` | Qwen | Multi-language parsing + Cross-file resolution |
| `gemini-qa-agent.md` | Gemini Pro | Documentation + API consistency + UX |

## How to use

1. Open the AI model (Kimi, ChatGPT, Gemini, Qwen, Claude)
2. Copy-paste the entire contents of the corresponding `.md` file
3. Attach / provide access to the `universal-code-graph/` directory
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cyberNoman__universal-code-review-graph/qa-agents/QA-MASTER-PLAN.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cyberNoman__universal-code-review-graph ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/demirmusa__nanocontext`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/demirmusa__nanocontext`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/demirmusa__nanocontext/src/core/interfaces/IParser.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import { ParsedFile } from './types';

export interface ILanguageParser {
  readonly language: string;
  readonly extensions: string[];
  parse(content: string, filePath: string): Promise<ParsedFile>;
}

export interface IParserRegistry {
  register(parser: ILanguageParser): void;
  getParser(filePath: string): ILanguageParser | null;
  getSupportedLanguages(): string[];
  getSupportedExtensions(): string[];
}
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/demirmusa__nanocontext/src/core/interfaces/IParser.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/demirmusa__nanocontext ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dlvandenberg__tree-sitter-angular`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dlvandenberg__tree-sitter-angular`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dlvandenberg__tree-sitter-angular/bindings/c/tree-sitter-angular.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=4, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_ANGULAR_H_
#define TREE_SITTER_ANGULAR_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_angular(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_ANGULAR_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dlvandenberg__tree-sitter-angular/bindings/c/tree-sitter-angular.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dlvandenberg__tree-sitter-angular ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dsully__tree-sitter-pyproject`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dsully__tree-sitter-pyproject`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dsully__tree-sitter-pyproject/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dsully__tree-sitter-pyproject/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dsully__tree-sitter-pyproject ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/elixir-lang__tree-sitter-elixir`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/elixir-lang__tree-sitter-elixir`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/elixir-lang__tree-sitter-elixir/bindings/c/tree-sitter-elixir.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_ELIXIR_H_
#define TREE_SITTER_ELIXIR_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_elixir(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_ELIXIR_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/elixir-lang__tree-sitter-elixir/bindings/c/tree-sitter-elixir.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/elixir-lang__tree-sitter-elixir ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/emiasims__tree-sitter-org`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/emiasims__tree-sitter-org`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/emiasims__tree-sitter-org/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/emiasims__tree-sitter-org/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/emiasims__tree-sitter-org ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/euclidianAce__tree-sitter-teal`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/euclidianAce__tree-sitter-teal`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/euclidianAce__tree-sitter-teal/bindings/c/tree_sitter/tree-sitter-teal.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_TEAL_H_
#define TREE_SITTER_TEAL_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_teal(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_TEAL_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/euclidianAce__tree-sitter-teal/bindings/c/tree_sitter/tree-sitter-teal.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/euclidianAce__tree-sitter-teal ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/fluffypony__mcp-code-indexer`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/fluffypony__mcp-code-indexer`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/fluffypony__mcp-code-indexer/src/mcp_code_indexer/vector_mode/chunking/ast_chunker.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
"""
Main AST-based code chunker for vector mode.

Coordinates language-specific parsing and produces optimized code chunks
for embedding generation while preserving semantic meaning.
"""

import hashlib
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional, Set
from dataclasses import dataclass
from datetime import datetime

from .language_handlers import get_language_handler, ParsedChunk
from .chunk_optimizer import ChunkOptimizer, OptimizedChunk
from ..security.redactor import SecretRedactor, RedactionResult
from ...database.models import ChunkType
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/fluffypony__mcp-code-indexer/src/mcp_code_indexer/vector_mode/chunking/ast_chunker.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/fluffypony__mcp-code-indexer ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/forloopcodes__contextplus`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/forloopcodes__contextplus`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/forloopcodes__contextplus/src/core/tree-sitter.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
// Web-tree-sitter based multi-language parser using WASM grammars
// Supports 36 languages via tree-sitter-wasms, extracts symbols from AST

import { readFile } from "fs/promises";
import { join, dirname } from "path";
import { fileURLToPath } from "url";
import type { CodeSymbol, SymbolKind } from "./parser.js";

type TSParser = any;
type TSLanguage = any;
type TSNode = any;

const GRAMMAR_DIR = join(dirname(fileURLToPath(import.meta.url)), "../../node_modules/tree-sitter-wasms/out");

const EXT_TO_GRAMMAR: Record<string, string> = {
  ".ts": "typescript", ".tsx": "tsx", ".js": "javascript", ".jsx": "javascript",
  ".mjs": "javascript", ".cjs": "javascript", ".py": "python", ".rs": "rust",
  ".go": "go", ".java": "java", ".c": "c", ".h": "c", ".cpp": "cpp",
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/forloopcodes__contextplus/src/core/tree-sitter.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/forloopcodes__contextplus ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/geigerzaehler__tree-sitter-jinja2`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/geigerzaehler__tree-sitter-jinja2`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/geigerzaehler__tree-sitter-jinja2/bindings/c/tree-sitter-jinja2.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=4, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_JINJA2_H_
#define TREE_SITTER_JINJA2_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_jinja2(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_JINJA2_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/geigerzaehler__tree-sitter-jinja2/bindings/c/tree-sitter-jinja2.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/geigerzaehler__tree-sitter-jinja2 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/gmlarumbe__tree-sitter-systemverilog`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/gmlarumbe__tree-sitter-systemverilog`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/gmlarumbe__tree-sitter-systemverilog/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/gmlarumbe__tree-sitter-systemverilog/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/gmlarumbe__tree-sitter-systemverilog ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/greglas75__codesift`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/greglas75__codesift`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/greglas75__codesift/docs/specs/2026-03-29-ast-frequency-analysis-plan.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
# Implementation Plan: AST Frequency Analysis

**Spec:** docs/specs/2026-03-29-ast-frequency-analysis-spec.md
**Created:** 2026-03-29
**Tasks:** 5
**Estimated complexity:** 4 standard, 1 complex

## Architecture Summary

Single new module `src/tools/frequency-tools.ts` following the established analysis-tool pattern (like `clone-tools.ts`). Dependencies: `getCodeIndex` (index-tools), `parseFile` (parser-manager), types (types.ts). Registration via `TOOL_DEFINITIONS` array in `register-tools.ts`. Zero new npm dependencies.

Data flow: `getCodeIndex(repo)` → filter symbols → re-parse each `symbol.source` via `parseFile` → post-order AST walk → normalize nodes (identifiers→`_`, strings→`_S`, numbers→`_N`, booleans→`_B`) → Merkle hash bottom-up → `Map<hash, symbols[]>` → filter min_nodes → sort by count desc → top_n → serialize with token_budget.

## Technical Decisions

- **Normalization:** tree-sitter re-parse (not regex) — precise node type awareness
- **Hash:** djb2 Merkle bottom-up: `hash(node) = djb2(node.type + childHashes)`
- **Walker:** iterative post-order (explicit stack) to avoid stack overflow on deep ASTs
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/greglas75__codesift/docs/specs/2026-03-29-ast-frequency-analysis-plan.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/greglas75__codesift ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hippietrail__tree-sitter-harper-dict`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hippietrail__tree-sitter-harper-dict`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hippietrail__tree-sitter-harper-dict/src/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hippietrail__tree-sitter-harper-dict/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hippietrail__tree-sitter-harper-dict ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/iamsaquib8__tessera`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/iamsaquib8__tessera`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/iamsaquib8__tessera/src/lib.rs`; scan counts include rust_files=22, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
//!
//! Local semantic code graph for AI coding agents. Index a repository into
//! SQLite + a memory-mapped snapshot; ask deterministic questions about
//! symbols, references, blast radius, and hallucinated identifiers.
//!
//! ```no_run
//! use tessera_codegraph::{Index, IndexOptions};
//!
//! # fn main() -> anyhow::Result<()> {
//! Index::build("./my-repo", "./my-repo/.tessera/tessera.db", IndexOptions::default())?;
//! let idx = Index::open("./my-repo/.tessera/tessera.db")?;
//! let impact = idx.impact("findById", 4)?;
//! for caller in impact.callers.iter().take(5) {
//!     println!(
//!         "{:5.1}  {} @ {}:{}",
//!         caller.criticality,
//!         caller.symbol.qualified_name,
//!         caller.symbol.path,
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/iamsaquib8__tessera/src/lib.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/iamsaquib8__tessera ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ikatyang__tree-sitter-yaml`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ikatyang__tree-sitter-yaml`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ikatyang__tree-sitter-yaml/src/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ikatyang__tree-sitter-yaml/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ikatyang__tree-sitter-yaml ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ionide__tree-sitter-fsharp`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ionide__tree-sitter-fsharp`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ionide__tree-sitter-fsharp/.opencode/skills/tree-sitter-parse-testing/SKILL.md`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=5, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
---
name: tree-sitter-parse-testing
description: Use when testing tree-sitter parser behavior for specific F# code snippets
---

# Tree-Sitter Parse Testing

## Overview
Use `tree-sitter parse -d` to debug parsing issues. The debug output shows the state machine transitions, helping identify where parsing fails.

## Parsing a Code Snippet

Run from the parser directory (`fsharp/` or `fsharp_signature/`):

```bash
echo 'let x = 1' | npx tree-sitter parse -d
```

```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ionide__tree-sitter-fsharp/.opencode/skills/tree-sitter-parse-testing/SKILL.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ionide__tree-sitter-fsharp ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jimhester__rtreesitter`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jimhester__rtreesitter`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jimhester__rtreesitter/src/tree-sitter/cli/benches/benchmark.rs`; scan counts include rust_files=70, cargo_manifests=5, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```rust
use std::path::{Path, PathBuf};
use std::time::Instant;
use std::{env, fs, str, usize};
use tree_sitter::{Language, Parser, Query};
use tree_sitter_cli::error::Error;
use tree_sitter_cli::loader::Loader;

include!("../src/tests/helpers/dirs.rs");

lazy_static! {
    static ref LANGUAGE_FILTER: Option<String> =
        env::var("TREE_SITTER_BENCHMARK_LANGUAGE_FILTER").ok();
    static ref EXAMPLE_FILTER: Option<String> =
        env::var("TREE_SITTER_BENCHMARK_EXAMPLE_FILTER").ok();
    static ref REPETITION_COUNT: usize = env::var("TREE_SITTER_BENCHMARK_REPETITION_COUNT")
        .map(|s| usize::from_str_radix(&s, 10).unwrap())
        .unwrap_or(5);
    static ref TEST_LOADER: Loader = Loader::new(SCRATCH_DIR.clone());
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jimhester__rtreesitter/src/tree-sitter/cli/benches/benchmark.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jimhester__rtreesitter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jlcrochet__tree-sitter-razor`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jlcrochet__tree-sitter-razor`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jlcrochet__tree-sitter-razor/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jlcrochet__tree-sitter-razor/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jlcrochet__tree-sitter-razor ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/johnhuang316__code-index-mcp`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/johnhuang316__code-index-mcp`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/johnhuang316__code-index-mcp/test/sample-projects/rust/conversation/src/conversation.rs`; scan counts include rust_files=1, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
    Active,
}

pub trait Runnable {
    fn execute(&self);
}
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/johnhuang316__code-index-mcp/test/sample-projects/rust/conversation/src/conversation.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/johnhuang316__code-index-mcp ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jrmoulton__tree-sitter-slint`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jrmoulton__tree-sitter-slint`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jrmoulton__tree-sitter-slint/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jrmoulton__tree-sitter-slint/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jrmoulton__tree-sitter-slint ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kentookura__tree-sitter-forester`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kentookura__tree-sitter-forester`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kentookura__tree-sitter-forester/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kentookura__tree-sitter-forester/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kentookura__tree-sitter-forester ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kristoferssolo__tree-sitter-jsonl`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kristoferssolo__tree-sitter-jsonl`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kristoferssolo__tree-sitter-jsonl/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kristoferssolo__tree-sitter-jsonl/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kristoferssolo__tree-sitter-jsonl ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/langston-barrett__tree-sitter-souffle`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/langston-barrett__tree-sitter-souffle`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/langston-barrett__tree-sitter-souffle/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/langston-barrett__tree-sitter-souffle/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/langston-barrett__tree-sitter-souffle ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/levnikolaevich__claude-code-skills`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/levnikolaevich__claude-code-skills`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/levnikolaevich__claude-code-skills/mcp/hex-graph-mcp/lib/queries/c_sharp.scm`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=5, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```scheme
; C# tree-sitter queries for codegraph
; MVP: definitions + imports only, no call edges

; --- Classes & Interfaces ---
(class_declaration) @definition.class
(interface_declaration) @definition.class
(struct_declaration) @definition.class
(enum_declaration) @definition.class
(record_declaration) @definition.class

; --- Methods ---
(method_declaration) @definition.method
(constructor_declaration) @definition.method

; --- Properties ---
(property_declaration) @definition.variable

; --- Imports ---
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/levnikolaevich__claude-code-skills/mcp/hex-graph-mcp/lib/queries/c_sharp.scm` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/levnikolaevich__claude-code-skills ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lumen-oss__luarocks-build-treesitter-parser`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lumen-oss__luarocks-build-treesitter-parser`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lumen-oss__luarocks-build-treesitter-parser`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
N/A: no source file selected during bounded scan.
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lumen-oss__luarocks-build-treesitter-parser ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` if this repo changes later.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mariusgreuel__tree-sitter-dotnet-bindings`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mariusgreuel__tree-sitter-dotnet-bindings`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mariusgreuel__tree-sitter-dotnet-bindings`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
N/A: no source file selected during bounded scan.
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mariusgreuel__tree-sitter-dotnet-bindings ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` if this repo changes later.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mertcanaltin__composto`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mertcanaltin__composto`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mertcanaltin__composto/docs/blastradius-proof-v2.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
# BlastRadius — Quality Proof v2 (Plan 5b · time-travel)

> **⚠️ SUPERSEDED (2026-06-21).** This 2-repo run (composto, picomatch) was not representative. A later honest 4-repo backtest (fastify, express, got, flask) found the signals are weak discriminators (AUC ~0.45-0.55): recall is good on mature repos (0.67-0.80) but **precision caps ~0.55**, and the picomatch 0.65/0.78 "ship gate cleared" result did NOT hold across repos. Adding a co-change signal + multiplicative gate moved precision past 0.60 only on fastify, not the others, so the gate now ships OFF by default. Composto positions the causal layer as **high-recall advisory** (not a precision gate) and leads with compression. See the project README. Numbers below are a historical record only.

**Date:** 2026-04-20 (this run), 2026-04-21 (doc written)
**Scope:** Two public repos (composto, picomatch) evaluated against the new time-travel harness. Third repo (vitest / zod) deferred — the two-repo signal is already load-bearing for the Phase 0 ship gate decision (see §4).
**Harness:** `scripts/backtest/time-travel.ts` + `scripts/blastradius-backtest.ts --time-travel`

---

## Ship-gate decision: **NOT MET**

Spec §9.3 defines the ship gate as **precision ≥ 0.60 and recall ≥ 0.40** on the `medium|high` verdict band across at least three public repos. The signal-attributed runs (revert_match excluded) fail this threshold on both repos. The unattributed run on composto itself also fails. **Phase 0 ship gate is blocked pending Plan 2 signal revision.**

This is a material revision of the v1 proof's claim. See §5.

---

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mertcanaltin__composto/docs/blastradius-proof-v2.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mertcanaltin__composto ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mizlan__iswap.nvim`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mizlan__iswap.nvim`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mizlan__iswap.nvim/queries/c/iswap-list.scm`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=27, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```scheme
[
  (argument_list)
  (enumerator_list)
  (initializer_list)
  (parameter_list)
] @iswap-list
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mizlan__iswap.nvim/queries/c/iswap-list.scm` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mizlan__iswap.nvim ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mrnugget__tree-sitter-tucan`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mrnugget__tree-sitter-tucan`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mrnugget__tree-sitter-tucan/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mrnugget__tree-sitter-tucan/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mrnugget__tree-sitter-tucan ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/naidaon__tree-sitter-astra`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/naidaon__tree-sitter-astra`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/naidaon__tree-sitter-astra/src/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/naidaon__tree-sitter-astra/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/naidaon__tree-sitter-astra ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/neo4j__neo4j`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/neo4j__neo4j`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/neo4j__neo4j/community/bolt/src/main/java/org/neo4j/bolt/discovery/handler/packet/RecurringBroadcastHandler.java`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
 */
package org.neo4j.bolt.discovery.handler.packet;

import static org.neo4j.bolt.discovery.packet.DiscoveryConstants.BROADCAST_PORT;

import io.netty.channel.ChannelHandlerAdapter;
import io.netty.channel.ChannelHandlerContext;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;
import org.neo4j.bolt.discovery.config.DiscoveryConfiguration;
import org.neo4j.bolt.discovery.info.DiscoveryInformationProvider;
import org.neo4j.bolt.discovery.info.DiscoveryInformationProvider.DiscoveryInformation;
import org.neo4j.bolt.discovery.packet.DiscoveryConstants;
import org.neo4j.bolt.discovery.packet.PacketEnvelope;
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/neo4j__neo4j/community/bolt/src/main/java/org/neo4j/bolt/discovery/handler/packet/RecurringBroadcastHandler.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/neo4j__neo4j ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nielsenko__tree-sitter-dart`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nielsenko__tree-sitter-dart`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nielsenko__tree-sitter-dart/bindings/c/tree_sitter/tree-sitter-dart.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_DART_H_
#define TREE_SITTER_DART_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_dart(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_DART_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nielsenko__tree-sitter-dart/bindings/c/tree_sitter/tree-sitter-dart.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nielsenko__tree-sitter-dart ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nushell__tree-sitter-nu`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nushell__tree-sitter-nu`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nushell__tree-sitter-nu/bindings/c/tree_sitter/tree-sitter-nu.h`; scan counts include rust_files=3, cargo_manifests=1, tree_sitter_query_files=5, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_NU_H_
#define TREE_SITTER_NU_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_nu(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_NU_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nushell__tree-sitter-nu/bindings/c/tree_sitter/tree-sitter-nu.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nushell__tree-sitter-nu ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nvim-treesitter__nvim-treesitter-textobjects`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nvim-treesitter__nvim-treesitter-textobjects`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nvim-treesitter__nvim-treesitter-textobjects/queries/astro/textobjects.scm`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=79, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```scheme
; inherits: html
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nvim-treesitter__nvim-treesitter-textobjects/queries/astro/textobjects.scm` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nvim-treesitter__nvim-treesitter-textobjects ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/omnetpp__tree-sitter-ned`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/omnetpp__tree-sitter-ned`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/omnetpp__tree-sitter-ned/bindings/c/tree-sitter-ned.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=6, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_NED_H_
#define TREE_SITTER_NED_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_ned(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_NED_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/omnetpp__tree-sitter-ned/bindings/c/tree-sitter-ned.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/omnetpp__tree-sitter-ned ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/openrewrite__rewrite`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/openrewrite__rewrite`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/openrewrite__rewrite/doc/adr/0005-parser-lst-conventions.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
# 5. Parser and LST Design Conventions and Best Practices

## Status

Draft

## Context

As we have developed parsers for more programming languages and data formats a number of conventions and best practices
have emerged. This document is intended to capture and codify those conventions and best practices.

## Decision


```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/openrewrite__rewrite/doc/adr/0005-parser-lst-conventions.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/openrewrite__rewrite ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/parth-maheta__BugRadar`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/parth-maheta__BugRadar`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/parth-maheta__BugRadar/src/parser/parserManager.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import * as vscode from "vscode";
import * as path from "path";
import Parser from "web-tree-sitter";

/**
 * Maps VS Code language identifiers to their tree-sitter WASM grammar filenames.
 */
const LANGUAGE_WASM_FILES: ReadonlyMap<string, string> = new Map([
  ["python", "tree-sitter-python.wasm"],
  ["javascript", "tree-sitter-javascript.wasm"],
]);

/**
 * Manages tree-sitter parsers for all supported languages.
 *
 * Responsibilities:
 * - Initialises the tree-sitter WASM runtime exactly once.
 * - Loads language grammars from `.wasm` files bundled in `out/parsers/`.
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/parth-maheta__BugRadar/src/parser/parserManager.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/parth-maheta__BugRadar ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/polarmutex__tree-sitter-astro`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/polarmutex__tree-sitter-astro`; scan counts include file_count=2, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/polarmutex__tree-sitter-astro ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pstuifzand__tree-sitter-printf`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pstuifzand__tree-sitter-printf`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pstuifzand__tree-sitter-printf/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pstuifzand__tree-sitter-printf/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pstuifzand__tree-sitter-printf ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rayen03__CodeBase_RAG`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rayen03__CodeBase_RAG`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rayen03__CodeBase_RAG/app/tree_sitter_parser.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

import tree_sitter
import tree_sitter_python
import tree_sitter_javascript
import tree_sitter_typescript
import tree_sitter_go
import tree_sitter_java
import tree_sitter_rust
import tree_sitter_c
import tree_sitter_cpp

from app.config import settings
from app.schemas import CodeChunk

logger = logging.getLogger(__name__)

```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rayen03__CodeBase_RAG/app/tree_sitter_parser.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rayen03__CodeBase_RAG ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ribru17__tree-sitter-man`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ribru17__tree-sitter-man`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ribru17__tree-sitter-man/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ribru17__tree-sitter-man/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ribru17__tree-sitter-man ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rockerBOO__boo-colorscheme-nvim`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rockerBOO__boo-colorscheme-nvim`; scan counts include file_count=19, rust_files=0, cargo_manifests=0, candidate_paths=2.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rockerBOO__boo-colorscheme-nvim ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sairam0424__ag-bash`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sairam0424__ag-bash`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sairam0424__ag-bash/examples/website/app/components/lite-terminal/ansi-parser.ts`; scan counts include rust_files=0, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
/**
 * Result of parsing a chunk of text with ANSI escape codes
 */
export interface ParseResult {
  type: "text" | "style" | "cursor" | "clear";
  text?: string;
  style?: Partial<TextStyle>;
  cursor?: { action: "left" | "right" | "home"; count?: number };
  clear?: "line" | "screen" | "scrollback";
}

// SGR (Select Graphic Rendition) parameter handlers
const SGR_HANDLERS: Record<number, (style: TextStyle) => void> = {
  0: (s) => {
    // Reset all attributes
    delete s.bold;
    delete s.dim;
    delete s.italic;
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sairam0424__ag-bash/examples/website/app/components/lite-terminal/ansi-parser.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sairam0424__ag-bash ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/scip-code__scip-rust`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/scip-code__scip-rust`; scan counts include file_count=9, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/scip-code__scip-rust ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/serenadeai__java-tree-sitter`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/serenadeai__java-tree-sitter`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/serenadeai__java-tree-sitter/src/main/java/ai/serenade/treesitter/Parser.java`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
import java.io.UnsupportedEncodingException;
import java.nio.charset.StandardCharsets;

public class Parser implements AutoCloseable {
  private long pointer;

  Parser(long pointer) {
    this.pointer = pointer;
  }

  public Parser() {
    this(TreeSitter.parserNew());
  }

  public void setLanguage(long language) {
    TreeSitter.parserSetLanguage(pointer, language);
  }

```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/serenadeai__java-tree-sitter/src/main/java/ai/serenade/treesitter/Parser.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/serenadeai__java-tree-sitter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/simonbs__TreeSitterLanguages`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/simonbs__TreeSitterLanguages`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/simonbs__TreeSitterLanguages/Sources/TreeSitterAstro/src/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=69, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/simonbs__TreeSitterLanguages/Sources/TreeSitterAstro/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/simonbs__TreeSitterLanguages ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/snip-ai__snip`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/snip-ai__snip`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/snip-ai__snip/src/compaction/parse.rs`; scan counts include rust_files=211, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
//! Wall-clock-bounded tree-sitter parse for the model-blocking Read path.
//!
//! snip's promise is to optimize *every* file, including large ones — so the
//! parse deadline **scales with input size** rather than capping at a flat
//! `< 15 ms`. The budget is a *deadline*, not a fixed cost: a file that parses
//! quickly returns immediately (small/medium files keep their sub-millisecond
//! speed), while a large file is granted proportionally more time so it still
//! gets compacted instead of being passed through unoptimized. A generous
//! [`PARSE_BUDGET_CEILING`] remains as an anti-hang backstop so a pathological
//! input can never freeze the tool call; only then does [`parse_bounded`] abandon
//! the parse and return `None` (the caller passes the file through unchanged —
//! always safe).

use std::ops::ControlFlow;
use std::time::{Duration, Instant};

use tree_sitter::{ParseOptions, ParseState, Parser, Tree};

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/snip-ai__snip/src/compaction/parse.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/snip-ai__snip ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcegraph__scip-python`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcegraph__scip-python`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcegraph__scip-python/packages/pyright-internal/src/analyzer/parseTreeCleaner.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
/*
 * parseTreeCleaner.ts
 * Copyright (c) Microsoft Corporation.
 * Licensed under the MIT license.
 * Author: Eric Traut
 *
 * A parse tree walker that's used to clean any analysis
 * information hanging off the parse tree. It's used when
 * dependent files have been modified and the file requires
 * reanalysis. Without this, we'd need to generate a fresh
 * parse tree from scratch.
 */

import { ModuleNode, ParseNode } from '../parser/parseNodes';
import * as AnalyzerNodeInfo from './analyzerNodeInfo';
import { ParseTreeWalker } from './parseTreeWalker';

export class ParseTreeCleanerWalker extends ParseTreeWalker {
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcegraph__scip-python/packages/pyright-internal/src/analyzer/parseTreeCleaner.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcegraph__scip-python ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/srazzak__tree-sitter-mdx`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/srazzak__tree-sitter-mdx`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/srazzak__tree-sitter-mdx/bindings/c/tree_sitter/tree-sitter-mdx.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=6, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_MDX_H_
#define TREE_SITTER_MDX_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_mdx(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_MDX_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/srazzak__tree-sitter-mdx/bindings/c/tree_sitter/tree-sitter-mdx.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/srazzak__tree-sitter-mdx ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/stormwarning__tree-sitter-nunjucks`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/stormwarning__tree-sitter-nunjucks`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/stormwarning__tree-sitter-nunjucks/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/stormwarning__tree-sitter-nunjucks/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/stormwarning__tree-sitter-nunjucks ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/surrealdb__surrealql-tree-sitter`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/surrealdb__surrealql-tree-sitter`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/surrealdb__surrealql-tree-sitter/src/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/surrealdb__surrealql-tree-sitter/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/surrealdb__surrealql-tree-sitter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tarungulati1988__onboard`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tarungulati1988__onboard`; scan counts include file_count=1, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tarungulati1988__onboard ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/the-mikedavis__tree-sitter-git-rebase`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/the-mikedavis__tree-sitter-git-rebase`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/the-mikedavis__tree-sitter-git-rebase/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/the-mikedavis__tree-sitter-git-rebase/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/the-mikedavis__tree-sitter-git-rebase ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tong__tree-sitter-haxe`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tong__tree-sitter-haxe`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tong__tree-sitter-haxe/bindings/c/tree_sitter/tree-sitter-haxe.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=5, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_HAXE_H_
#define TREE_SITTER_HAXE_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_haxe(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_HAXE_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tong__tree-sitter-haxe/bindings/c/tree_sitter/tree-sitter-haxe.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tong__tree-sitter-haxe ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-grammars__tree-sitter-hcl`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-grammars__tree-sitter-hcl`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-grammars__tree-sitter-hcl/dialects/terraform/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-grammars__tree-sitter-hcl/dialects/terraform/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-grammars__tree-sitter-hcl ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-perl__tree-sitter-pod`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-perl__tree-sitter-pod`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-perl__tree-sitter-pod/bindings/c/tree_sitter/tree-sitter-pod.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_POD_H_
#define TREE_SITTER_POD_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_pod(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_POD_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-perl__tree-sitter-pod/bindings/c/tree_sitter/tree-sitter-pod.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-perl__tree-sitter-pod ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__java-tree-sitter`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__java-tree-sitter`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__java-tree-sitter/src/main/java/io/github/treesitter/jtreesitter/ParseCallback.java`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text

/** A function that retrieves a chunk of text at a given byte offset and point. */
@FunctionalInterface
public interface ParseCallback {
    /**
     * Applies this function to the given arguments.
     *
     * @param offset the current byte offset
     * @param point the current point
     * @return A chunk of text or {@code null} to indicate the end of the document.
     */
    @Nullable
    String read(@Unsigned int offset, @NonNull Point point);

    /**
     * Applies this function to the given arguments.
     *
     * @param offset the current byte offset
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__java-tree-sitter/src/main/java/io/github/treesitter/jtreesitter/ParseCallback.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__java-tree-sitter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__parser-test-action`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__parser-test-action`; scan counts include file_count=11, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__parser-test-action ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-bash`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-bash`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-bash/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-bash/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-bash ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-css`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-css`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-css/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-css/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-css ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-html`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-html`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-html/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-html/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-html ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-ocaml`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-ocaml`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-ocaml/grammars/interface/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-ocaml/grammars/interface/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-ocaml ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-ruby`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-ruby`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-ruby/bindings/c/tree-sitter-ruby.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_RUBY_H_
#define TREE_SITTER_RUBY_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_ruby(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_RUBY_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-ruby/bindings/c/tree-sitter-ruby.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-ruby ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-verilog`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-verilog`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-verilog/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-verilog/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-verilog ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/unhappychoice__gitlogue`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/unhappychoice__gitlogue`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/unhappychoice__gitlogue/src/syntax/languages/astro.rs`; scan counts include rust_files=67, cargo_manifests=1, tree_sitter_query_files=6, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
pub fn language() -> tree_sitter::Language {
    tree_sitter_astro_next::LANGUAGE.into()
}

pub const HIGHLIGHT_QUERY: &str = tree_sitter_astro_next::HIGHLIGHTS_QUERY;

pub const INJECTION_QUERY: &str = tree_sitter_astro_next::INJECTIONS_QUERY;
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/unhappychoice__gitlogue/src/syntax/languages/astro.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/unhappychoice__gitlogue ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/uyha__tree-sitter-cmake`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/uyha__tree-sitter-cmake`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/uyha__tree-sitter-cmake/bindings/c/tree_sitter/tree-sitter-cmake.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=4, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_CMAKE_H_
#define TREE_SITTER_CMAKE_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_cmake(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_CMAKE_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/uyha__tree-sitter-cmake/bindings/c/tree_sitter/tree-sitter-cmake.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/uyha__tree-sitter-cmake ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/viktorstrate__swift-tree-sitter`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/viktorstrate__swift-tree-sitter`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/viktorstrate__swift-tree-sitter/Sources/TreeSitterLanguages/css_parser.c`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
N/A: could not read `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/viktorstrate__swift-tree-sitter/Sources/TreeSitterLanguages/css_parser.c`: [Errno 2] No such file or directory: '/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/viktorstrate__swift-tree-sitter/Sources/TreeSitterLanguages/css_parser.c'
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/viktorstrate__swift-tree-sitter/Sources/TreeSitterLanguages/css_parser.c` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/viktorstrate__swift-tree-sitter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vrischmann__tree-sitter-templ`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vrischmann__tree-sitter-templ`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vrischmann__tree-sitter-templ/bindings/c/tree-sitter-templ.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=5, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_TEMPL_H_
#define TREE_SITTER_TEMPL_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_templ(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_TEMPL_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vrischmann__tree-sitter-templ/bindings/c/tree-sitter-templ.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vrischmann__tree-sitter-templ ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/wingyplus__tree-sitter-elixir`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/wingyplus__tree-sitter-elixir`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/wingyplus__tree-sitter-elixir/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/wingyplus__tree-sitter-elixir/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/wingyplus__tree-sitter-elixir ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/y1hanh__codebase-indexer-mcp`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/y1hanh__codebase-indexer-mcp`; scan counts include file_count=13, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/y1hanh__codebase-indexer-mcp ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zackradisic__glyph`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zackradisic__glyph`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zackradisic__glyph/glyph/lsp/src/parse.rs`; scan counts include rust_files=18, cargo_manifests=5, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
use combine::{
    from_str,
    parser::{
        combinator::{any_send_partial_state, AnySendPartialState},
        range::{range, take, take_while1},
    },
    skip_many, ParseError, Parser, RangeStream,
};

pub fn decode_header<'a, I>(
) -> impl Parser<I, Output = Vec<u8>, PartialState = AnySendPartialState> + 'a
where
    I: RangeStream<Token = u8, Range = &'a [u8]> + 'a,
    // Necessary due to rust-lang/rust#24159
    I::Error: ParseError<I::Token, I::Range, I::Position>,
{
    let content_length =
        range(&b"Content-Length: "[..]).with(from_str(take_while1(|b: u8| b.is_ascii_digit())));
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zackradisic__glyph/glyph/lsp/src/parse.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zackradisic__glyph ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ziglibs__tree-sitter-zig`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ziglibs__tree-sitter-zig`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ziglibs__tree-sitter-zig/grammar.js`; scan counts include rust_files=0, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```javascript

const expr_list = $ => seq(repeat(seq($.expr, ",")), optional($.expr));

module.exports = grammar({
    name: "zig",

    externals: (_) => [],
    inline: (_) => [],
    extras: ($) => [/\s/, $.line_comment],
    // TODO: Investigate these - can we fix them?
    conflicts: ($) => [[$.root], [$.container_decl_auto]],

    rules: {
        root: $ => seq(optional($.container_doc_comment), container_members($)),

        // *** Keywords ***
        pub: _ => "pub",
        anyframe: _ => "anyframe",
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ziglibs__tree-sitter-zig/grammar.js` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ziglibs__tree-sitter-zig ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/pm2dev`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/pm2dev`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/pm2dev/ideation-new-oss-repos/RubyRust202601/02-Parseltongue-Analysis-Rails-Codebase.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
# Parseltongue Analysis: Rails Codebase Transpilability

## Date: 2026-02-04

## Analysis Methodology

Used parseltongue v1.4.7 to analyze the Rails framework codebase:
- Ingested `rails-framework/` directory
- 3,416 files processed
- 113,803 CODE entities created
- 158,170 dependency edges mapped

## Quantitative Findings

### Total Codebase Statistics

| Metric | Value |
|--------|-------|
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/pm2dev/ideation-new-oss-repos/RubyRust202601/02-Parseltongue-Analysis-Rails-Codebase.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/pm2dev ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/codecentric__spring-boot-admin`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/codecentric__spring-boot-admin`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/codecentric__spring-boot-admin/spring-boot-admin-docs/src/site/docs/04-integration/40-hazelcast.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
  icon: 'server'
---

# Hazelcast Clustering

Hazelcast provides distributed data structures for clustering multiple Spring Boot Admin Server instances. This enables
high availability and shared state across servers.

## Overview

With Hazelcast clustering:

- Multiple Admin Server instances share event store
- No single point of failure
- Automatic synchronization across nodes
- Distributed notifications

## Architecture
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/codecentric__spring-boot-admin/spring-boot-admin-docs/src/site/docs/04-integration/40-hazelcast.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/codecentric__spring-boot-admin ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/mybatis__spring-boot-starter`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/mybatis__spring-boot-starter`; scan counts include file_count=296, rust_files=0, cargo_manifests=0, candidate_paths=2.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/mybatis__spring-boot-starter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/spring-guides__gs-spring-boot`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/spring-guides__gs-spring-boot`; scan counts include file_count=54, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/spring-guides__gs-spring-boot ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/xkcoding__spring-boot-demo`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/xkcoding__spring-boot-demo`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/xkcoding__spring-boot-demo/demo-elasticsearch-rest-high-level-client/README.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
# spring-boot-demo-elasticsearch-rest-high-level-client

> 此 demo 主要演示了 Spring Boot 如何集成 `elasticsearch-rest-high-level-client` 完成对 `ElasticSearch 7.x` 版本的基本 CURD 操作

## Elasticsearch 升级

先升级到 6.8，索引创建，设置 mapping 等操作加参数：include_type_name=true，然后滚动升级到 7，旧索引可以用 type 访问。具体可以参考：

https://www.elastic.co/cn/blog/moving-from-types-to-typeless-apis-in-elasticsearch-7-0

https://www.elastic.co/guide/en/elasticsearch/reference/7.0/removal-of-types.html

## 注意

作者编写本 demo 时，ElasticSearch 版本为 `7.3.0`，使用 docker 运行，下面是所有步骤：

1.下载镜像：`docker pull elasticsearch:7.3.0`

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/xkcoding__spring-boot-demo/demo-elasticsearch-rest-high-level-client/README.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/xkcoding__spring-boot-demo ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/servo-test-202411`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/servo-test-202411`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/servo-test-202411/components/config_plugins/parse.rs`; scan counts include rust_files=1049, cargo_manifests=58, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at https://mozilla.org/MPL/2.0/. */

use proc_macro2::Span;
use syn::parse::{Parse, ParseStream, Result};
use syn::punctuated::Punctuated;
use syn::{braced, token, Attribute, Ident, Path, Token, Type};

#[allow(non_camel_case_types)]
mod kw {
    syn::custom_keyword!(accessor_type);
    syn::custom_keyword!(gen_accessors);
    syn::custom_keyword!(gen_types);
}

pub struct MacroInput {
    pub type_def: RootTypeDef,
    pub gen_accessors: Ident,
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/servo-test-202411/components/config_plugins/parse.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/servo-test-202411 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/tweetbook202409`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust Module Architecture Slice From `personal-repos-lane/tweetbook202409`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/tweetbook202409/p002_thread_extractor_202409v1/src/main.rs`; scan counts include rust_files=9, cargo_manifests=2, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```rust
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use tokio::fs as async_fs;
use chrono::{DateTime, Utc, Local};
use std::time::Instant;

// Step 1: Define Your Avengers (Data Structures)
// Imagine we're creating a profile for each Avenger. Each field is like a special skill or characteristic.
#[derive(Deserialize, Serialize, Debug, Clone)]
struct Tweet {
    id_str: String,            // This is like Captain America's shield - unique and identifiable
    favorite_count: String,    // Think of this as Thor's lightning - how much power (popularity) the tweet has
    full_text: String,         // This is like Iron Man's speech - the actual content of the tweet
    in_reply_to_status_id: Option<String>, // Like Black Widow's spy network - who this tweet is connected to
    retweeted: bool,           // This is like Hulk's transformation - has this tweet changed form?
    in_reply_to_screen_name: Option<String>, // Like Hawkeye's target - who is this tweet aimed at?
    retweet_count: String,     // Think of this as how many times the Avengers have assembled for this tweet
    created_at: String,        // This is like the timestamp in Dr. Strange's Time Stone - when the tweet came into existence
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/tweetbook202409/p002_thread_extractor_202409v1/src/main.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/tweetbook202409 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/zip-revelio`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust Module Architecture Slice From `personal-repos-lane/zip-revelio`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/zip-revelio/src/lib.rs`; scan counts include rust_files=4, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```rust
use thiserror::Error;

pub const MAX_SIZE: u64 = 4 * 1024 * 1024 * 1024; // 4GB

mod zip;
pub use zip::FileZipReader;

#[derive(Error, Debug)]
pub enum Error {
    #[error("ZIP file too large: {size} bytes (max: 4GB)")]
    SizeLimit { size: u64 },
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),
    #[error("Invalid ZIP format: {0}")]
    Format(String),
}

pub type Result<T> = std::result::Result<T, Error>;
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/zip-revelio/src/lib.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/zip-revelio ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/zztweets-of-amuldotexe2023`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/zztweets-of-amuldotexe2023`; scan counts include file_count=2, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/zztweets-of-amuldotexe2023 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Skipped Repo: `/Users/amuldotexe/Desktop/reference-repos-yard/codemogger`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/codemogger`; scan counts include file_count=45, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/reference-repos-yard/codemogger ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/fff.nvim`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `reference-repos-yard/fff.nvim`
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/fff.nvim/crates/fff-core/benches/parse_bench.rs`; scan counts include rust_files=101, cargo_manifests=8, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
use criterion::{BenchmarkId, Criterion, Throughput, black_box, criterion_group, criterion_main};
use fff_query_parser::*;

fn bench_parse_simple(c: &mut Criterion) {
    let parser = QueryParser::default();

    c.bench_function("parse_simple_text", |b| {
        b.iter(|| parser.parse(black_box("hello world")));
    });

    c.bench_function("parse_extension", |b| {
        b.iter(|| parser.parse(black_box("*.rs")));
    });

    c.bench_function("parse_text_with_extension", |b| {
        b.iter(|| parser.parse(black_box("name *.rs")));
    });
}
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/reference-repos-yard/fff.nvim/crates/fff-core/benches/parse_bench.rs` and run `git -C /Users/amuldotexe/Desktop/reference-repos-yard/fff.nvim ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/kani`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust Module Architecture Slice From `reference-repos-yard/kani`
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/kani/kani-compiler/src/kani_queries/mod.rs`; scan counts include rust_files=1762, cargo_manifests=213, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```rust
// Copyright Kani Contributors
// SPDX-License-Identifier: Apache-2.0 OR MIT
//! Define the communication between KaniCompiler and the codegen implementation.

use crate::args::Arguments;
use crate::kani_middle::kani_functions::{
    KaniFunction, find_kani_functions, validate_kani_functions,
};
use rustc_public::ty::FnDef;
use std::cell::{OnceCell, RefCell};
use std::collections::HashMap;

thread_local! {
    pub static QUERY_DB: RefCell<QueryDb> = RefCell::new(QueryDb::default());
}

/// This structure is only accessed via thread_local storage to ensure thread safety.
///
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/reference-repos-yard/kani/kani-compiler/src/kani_queries/mod.rs` and run `git -C /Users/amuldotexe/Desktop/reference-repos-yard/kani ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/tauri-template`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `reference-repos-yard/tauri-template`
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/tauri-template/docs/developer/writing-ast-grep-rules.md`; scan counts include rust_files=12, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
# Writing ast-grep Rules

Reference for creating custom ast-grep rules. Intended for AI agents but readable by humans.

## When to Add Rules

Add ast-grep rules when:

- You identify a repeated architectural violation
- ESLint can't express the rule (pattern-based matching needed)
- The pattern has caused bugs or performance issues

## Rule Structure

```yaml
id: rule-name
message: |
  Brief description with examples.
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/reference-repos-yard/tauri-template/docs/developer/writing-ast-grep-rules.md` and run `git -C /Users/amuldotexe/Desktop/reference-repos-yard/tauri-template ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

