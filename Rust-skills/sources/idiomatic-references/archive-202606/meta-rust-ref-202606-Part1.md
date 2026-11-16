# Meta Rust Reference 202606 Part 1

Purpose: encyclopedia-grade Rust reference extracted repo-by-repo from every Git repository under `/Users/amuldotexe/Desktop`, with special attention to tree-sitter, parser, compiler, graph, async, storage, FFI, CLI, testing, and architecture patterns.

Assigned repo slice: `meta-rust-ref-202606-Part1-repos.txt`

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

- `/Users/amuldotexe/Desktop/TauriAppsOSS`
- `/Users/amuldotexe/Desktop/oss-read-only/airflow`
- `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/quickwit`
- `/Users/amuldotexe/Desktop/oss-read-only/claude-peers-mcp`
- `/Users/amuldotexe/Desktop/oss-read-only/dbt-core`
- `/Users/amuldotexe/Desktop/oss-read-only/iggy`
- `/Users/amuldotexe/Desktop/oss-read-only/openobserve`
- `/Users/amuldotexe/Desktop/oss-read-only/plotly.py`
- `/Users/amuldotexe/Desktop/oss-read-only/streamlit`
- `/Users/amuldotexe/Desktop/oss-read-only/warp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/CodeEDA`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/StableToolBench`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/appworld`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/gorilla`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/n2-QLN`
- `/Users/amuldotexe/Desktop/personal-repos-lane/apache-spark-shallow`
- `/Users/amuldotexe/Desktop/personal-repos-lane/confido-exploration-01`
- `/Users/amuldotexe/Desktop/personal-repos-lane/dynamic-analysis`
- `/Users/amuldotexe/Desktop/personal-repos-lane/floo-network`
- `/Users/amuldotexe/Desktop/personal-repos-lane/hackerrank-exploration-202604`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/cypher-shell-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-browser-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-go-driver-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/antlr-grammars-v4-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-hugegraph-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/arangodb-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/cugraph-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/duckdb-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gapbs-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphchi-cpp-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/igraph-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ladybug-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics_platforms_graphblas-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/libcypher-parser-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/nalgebra-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ongdb-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/raphtory-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/rust-rocksdb-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/sprs-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tigergraph-ecosys-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/law-diagrams`
- `/Users/amuldotexe/Desktop/personal-repos-lane/mp4-to-mp3`
- `/Users/amuldotexe/Desktop/personal-repos-lane/notes202408`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AB498__code-context-provider-mcp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aerijo__tree-sitter-biber`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__tree-sitter-log`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AperturePlus__augmented-codebase-indexer`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AryanSaini26__CodeAtlas`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Boottify__glyph`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CI124__auto-ime`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeBendKit__codeseek`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Corbell-AI__Corbell`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DeepSourceCorp__globstar`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/EarthChen__knowledge-base-service`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/EvgeniyPeshkov__syntax-highlighter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/FosterG4__tree-sitter-mcpsaver`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Graphify-Labs__graphify`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/HiPhish__nvim-ts-rainbow2`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/INS-JVidal__code-primer`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Jakedismo__codegraph-rust`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/JoosepAlviste__nvim-ts-context-commentstring`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Knaackee__code-explorer`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/LhKipp__tree-sitter-nu`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/MikeRecognex__mcp-codebase-index`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Nymphium__graft`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OpenHands__OpenHands`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PRQL__tree-sitter-prql`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PrestonKnopp__tree-sitter-godot-resource`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RahulModugula__odin`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/SaumyaJoshi2005__AlgoSnap`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/SrGaabriel__tree-sitter-soma`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/TheYoxy__tree-sitter-coda`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ViperJuice__Code-Index-MCP`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Wilfred__tree-sitter-elisp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aMOPel__tree-sitter-nim`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/adamdelezuch89__repo-map-mcp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aheber__tree-sitter-sfapex`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ajeetdsouza__loxcraft`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/alessandrobrunoh__Semantic-Delta-Protocol`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aorwall__moatless-tools`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/arnarg__tree-sitter-todotxt`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/audityzer-org__audityzer-rust-analyzer`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bearcove__arborium`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bezhermoso__tree-sitter-ghostty`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bonede__tree-sitter-ng`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bytecodealliance__tree-sitter-wit`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/casouri__tree-sitter-module`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/chunkhound__chunkhound`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/coder3101__tree-sitter-proto`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cozodb__cozo`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cshuaimin__ssr.nvim`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/daun__tree-sitter-latte`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dhawwal__code-intelligence-ai`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dominiclynchwoodlands-ui__codebaser`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/egibs__tree-sitter-poe`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/emacs-tree-sitter__elisp-tree-sitter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/er77__code-graph-rag-mcp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/facebook__rocksdb`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/flurie__tree-sitter-jq`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/frozolotl__tree-sitter-typst`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ggfevans__zed-hujson`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/glehmann__tree-sitter-earthfile`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/google-gemini__gemini-cli`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/haasonsaas__semantic-sast`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hrayleung__Cocode`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ikatyang__tree-sitter-markdown`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/indradb__indradb`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jbpraxxys__opencode-indexer`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jiyee__tree-sitter-objc`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jobindex-open__tree-sitter-embedded-perl`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/joowani__tree-sitter-graphql`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kaermorchen__tree-sitter-explorer`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kopecs__tree-sitter-c0`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kylegoetz__tree-sitter-unison`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lapce__tree-sitter-grammars`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lezer-parser__import-tree-sitter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/m-demare__hlargs.nvim`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/maxxnino__tree-sitter-zig`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mickeynp__combobulate`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/monaqa__tree-sitter-satysfi`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mufeedvh__code2prompt`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/navgupta15__DTGS`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/neurocyte__flow`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nix-community__tree-sitter-nix`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nvim-neorg__tree-sitter-norg`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nxrvl__codedocgen`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/open-compress__claw-compactor`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/orzechowskid__tree-sitter-css-in-js`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pfeiferj__tree-sitter-hurl`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/prateekky__FastGraphRAG`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/r-lib__tree-sitter-r`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rest-nvim__tree-sitter-http`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/riyonp23__Probe`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rotmh__tree-sitter-dunstrc`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sakakibara__tree-sitter-organ`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sapai5__plagiarism-checker`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/semgrep__ocaml-tree-sitter-languages`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/shruti25838__CodeMentor-AI`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/skrider__softgrep`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcebot-dev__sourcebot`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcegraph__scip-typescript`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sscba__code-intelligence-mcp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/stsewd__tree-sitter-comment`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/syncable-dev__memtrace-public`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tera-language__tree-sitter-teralang`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/thmsmlr__tree-sitter-rec`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/traxys__tree-sitter-lalrpop`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-grammars__tree-sitter-markdown`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__fuzz-action`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__node-tree-sitter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__py-tree-sitter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-c-sharp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-go`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-javascript`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-python`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-scala`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__zig-tree-sitter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/universal-ctags__ctags`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/victorhqc__tree-sitter-prisma`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vitali87__code-graph-rag`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/wenkokke__tree-sitter-talon`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/wrale__mcp-server-tree-sitter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/yijunyu__tree-sitter-parsers`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zed-industries__zed`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zzxn__tree-sitter-ast-dfg`
- `/Users/amuldotexe/Desktop/personal-repos-lane/proof-of-effort-2024`
- `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/eugenp__tutorials`
- `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/spring-guides__gs-actuator-service`
- `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/spring-projects__spring-boot`
- `/Users/amuldotexe/Desktop/personal-repos-lane/rust-100-exercises-notes`
- `/Users/amuldotexe/Desktop/personal-repos-lane/that-in-rust-org-github`
- `/Users/amuldotexe/Desktop/personal-repos-lane/useful-rc-files`
- `/Users/amuldotexe/Desktop/personal-repos-lane/zz_archived_journal2023`
- `/Users/amuldotexe/Desktop/reference-repos-yard/RAPx`
- `/Users/amuldotexe/Desktop/reference-repos-yard/cachebro`
- `/Users/amuldotexe/Desktop/reference-repos-yard/creusot`
- `/Users/amuldotexe/Desktop/reference-repos-yard/flux`
- `/Users/amuldotexe/Desktop/reference-repos-yard/marker`
- `/Users/amuldotexe/Desktop/reference-repos-yard/polonius`
- `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_jvm`
- `/Users/amuldotexe/Desktop/reference-repos-yard/zed`

## Pattern Entries

## Repo Coverage: /Users/amuldotexe/Desktop/oss-read-only/alienplatform/quickwit

### Concept: Storage resolver as a real seam over object, local, and memory adapters

Evidence:
- `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/quickwit/quickwit/quickwit-storage/src/lib.rs` exposes `Storage`, `StorageFactory`, `StorageResolver`, `RamStorage`, `LocalFileStorage`, `S3CompatibleObjectStorage`, `TimeoutAndRetryStorage`, and the `storage_test_suite`.
- `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/quickwit/quickwit/quickwit-storage/src/storage.rs` defines the `Storage` Interface: `put`, `copy_to`, `copy_to_file`, `get_slice`, `get_slice_stream`, `get_all`, `delete`, `bulk_delete`, `exists`, `file_num_bytes`, and `uri`.
- `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/quickwit/quickwit/quickwit-storage/src/storage_factory.rs` defines the smaller `StorageFactory` Interface: `backend()` and `resolve(&Uri) -> Arc<dyn Storage>`.
- `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/quickwit/quickwit/quickwit-storage/src/storage_resolver.rs` maps URI protocol to `StorageBackend`, then dispatches to a registered `StorageFactory`.
- `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/quickwit/quickwit/quickwit-storage/src/ram_storage.rs` implements `StorageFactory` for `RamStorageFactory` and runs the shared storage test suite against `RamStorage`.

Architecture lens:
This is a deep Module split into two seams. `Storage` is the operational seam for callers that need bytes, ranges, streams, deletes, and object-style path semantics. `StorageFactory` is the construction seam for adapters that are selected by URI. The seam is real because there are multiple adapters: local file, RAM, S3-compatible object storage, optional Azure, optional GCS, unsupported-backend adapters, and wrappers such as timeout/retry and cache. The resolver gives leverage by making storage selection a URI concern instead of spreading protocol branching across callers. Locality is high: feature-gated backend differences sit in `StorageResolver::configured`, while storage behavior is verified through the shared test suite.

Reusable code shape:
```rust
#[async_trait]
pub trait BlobStore: Send + Sync + 'static {
    async fn put(&self, path: &Path, payload: Box<dyn PutPayload>) -> Result<()>;
    async fn get_range(&self, path: &Path, range: Range<usize>) -> Result<Bytes>;
    async fn delete_many(&self, paths: &[&Path]) -> Result<(), BulkDeleteError>;
    fn uri(&self) -> &Uri;
}

#[async_trait]
pub trait BlobStoreFactory: Send + Sync + 'static {
    fn backend(&self) -> Backend;
    async fn resolve(&self, uri: &Uri) -> Result<Arc<dyn BlobStore>>;
}

pub struct BlobStoreResolver {
    factories: HashMap<Backend, Box<dyn BlobStoreFactory>>,
}
```

Transfer rule:
Use this shape when callers need one storage Interface but deployment needs multiple concrete adapters. Keep the resolver shallow and the storage Module deep: callers should learn path/range/error semantics once, not rediscover S3/file/RAM differences at every call site. Apply the deletion test to the resolver: deleting it should cause protocol branching to reappear across many callers; if not, the seam is hypothetical.

Verification hook:
Port Quickwit's shared-suite pattern: write adapter-independent tests that accept `&mut dyn BlobStore` or `Arc<dyn BlobStore>` and assert missing-file behavior, write/read slice behavior, stream behavior, all-bytes behavior, delete idempotence, bulk-delete partial failure behavior, and URI identity. Then run the same suite against memory and filesystem adapters before adding object storage.

### Concept: Actor interface packages lifecycle, scheduling, backpressure, and observability

Evidence:
- `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/quickwit/quickwit/quickwit-actors/src/actor.rs` defines `Actor`, `Handler<M>`, `DeferableReplyHandler<M>`, and `ActorExitStatus`.
- `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/quickwit/quickwit/quickwit-actors/src/mailbox.rs` defines typed `Mailbox<A>` send, try-send, high-priority send, ask, and backpressure counter methods.
- `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/quickwit/quickwit/quickwit-actors/src/universe.rs` provides `Universe::create_mailbox`, `create_test_mailbox`, `spawn_builder`, `observe`, `quit`, and tests with `CountingMinutesActor`, `ExitPanickingActor`, and scheduled loops.
- `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/quickwit/quickwit/quickwit-actors/src/lib.rs` re-exports the actor Interface so callers do not need internal module paths.

Architecture lens:
The `Actor` Module is deep because a small Interface carries lifecycle rules that would otherwise leak everywhere: initialization, runner selection, queue capacity, yield policy, observable state, drained-message behavior, and finalization. `Mailbox<A>` is the caller-facing seam. It hides the implementation detail that messages are wrapped into envelopes, prioritized, sent through channels, and answered through oneshot receivers. The typed `Handler<M>` and `DeferableReplyHandler<M>` traits give leverage by encoding message/reply compatibility at compile time. The backpressure counter keeps locality: queue delay instrumentation lives inside the mailbox rather than in every sender.

Reusable code shape:
```rust
#[async_trait]
pub trait Worker: Send + Sized + 'static {
    type Observable: Clone + Send + Sync;

    fn queue_capacity(&self) -> QueueCapacity { QueueCapacity::Unbounded }
    fn observable_state(&self) -> Self::Observable;
    async fn initialize(&mut self, ctx: &WorkerContext<Self>) -> Result<(), ExitStatus> { Ok(()) }
    async fn finalize(&mut self, status: &ExitStatus, ctx: &WorkerContext<Self>) -> Result<()> { Ok(()) }
}

#[async_trait]
pub trait Handles<M>: Worker {
    type Reply: Send + 'static;
    async fn handle(&mut self, message: M, ctx: &WorkerContext<Self>) -> Result<Self::Reply, ExitStatus>;
}

pub struct Mailbox<W: Worker> { /* priority queues, oneshot replies, metrics */ }
```

Transfer rule:
Use a typed mailbox seam when async Modules need stateful processing, lifecycle hooks, and backpressure semantics. Do not expose raw channels as the Interface unless callers truly need to manage envelopes and priorities. One adapter is hypothetical; this actor seam becomes real when tests, production workers, and scheduler-backed workers all cross the same mailbox Interface.

Verification hook:
Write tests at the mailbox seam, not inside the queue implementation: send when connected, send after actor exit, `try_send` on a bounded queue, `ask` reply success, `ask` reply dropped, high-priority ordering, backpressure counter increments, graceful quit, and panic propagation through `ActorExitStatus`.

## Repo Coverage: /Users/amuldotexe/Desktop/oss-read-only/iggy

### Concept: Sans-IO frame codecs make binary protocol parsing portable across transports

Evidence:
- `/Users/amuldotexe/Desktop/oss-read-only/iggy/core/binary_protocol/src/framing.rs` is documented as a Sans-IO frame codec. `RequestFrame<'a>` borrows payload bytes and provides `payload_length`, `from_parts`, `decode`, `encode`, and `encoded_size`.
- `/Users/amuldotexe/Desktop/oss-read-only/iggy/core/binary_protocol/src/message_view.rs` defines zero-copy `WireMessageView<'a>`, `WireMessageViewMut<'a>`, `WireMessageIterator<'a>`, and cursor-style `WireMessageIteratorMut<'a>`.
- `message_view.rs` validates frame sizes once in `validate_frame`, after which accessors such as `id`, `offset`, `timestamp`, `payload`, and `user_headers` are infallible borrowed views.
- Tests in `message_view.rs` include `iterator_zero_count`, `iterator_single_message`, and `iterator_multiple_messages`.
- `/Users/amuldotexe/Desktop/oss-read-only/iggy/core/server/src/quic/listener.rs` imports `RequestFrame` and dispatch helpers, showing the transport can hand decoded payloads into server logic.

Architecture lens:
The frame codec is a deep Module because the Interface is a few constructors/accessors, while the Implementation concentrates byte offsets, length validation, overflow checks, endian details, and mutable-borrow limitations. It creates a seam between transport adapters and protocol interpretation. TCP, QUIC, WebSocket, and test buffers can all feed the same decoder without duplicating framing rules. The mutable iterator intentionally avoids implementing standard `Iterator` because its yielded view borrows `&mut self`; that is a good example of the Interface teaching a Rust lifetime invariant instead of pretending the common trait fits.

Reusable code shape:
```rust
pub struct Frame<'a> {
    buf: &'a [u8],
    payload_len: usize,
}

impl<'a> Frame<'a> {
    pub fn decode(buf: &'a [u8]) -> Result<(Self, usize), WireError> {
        let len = validate_header(buf)?;
        Ok((Self { buf: &buf[..len], payload_len: len - HEADER }, len))
    }

    pub fn payload(&self) -> &'a [u8] {
        &self.buf[HEADER..HEADER + self.payload_len]
    }
}

pub struct FrameIter<'a> {
    buf: &'a [u8],
    pos: usize,
    remaining: u32,
}
```

Transfer rule:
For Rust protocol work, make byte parsing Sans-IO first. Transport Modules should handle reads, timeouts, TLS, and backpressure; codec Modules should handle length fields, offsets, payload slices, and validation. This preserves locality for binary compatibility bugs and gives leverage because fuzz tests and unit tests can exercise the parser without a socket.

Verification hook:
Add unit tests for short headers, declared length longer than buffer, overflow in computed total length, valid single frame, multiple contiguous frames, zero-count iterators, mutable frame edits, and encode/decode round trips. Add a fuzz target that feeds arbitrary bytes into `decode` and asserts no panic.

### Concept: Journal and storage traits separate consensus durability from positional file IO

Evidence:
- `/Users/amuldotexe/Desktop/oss-read-only/iggy/core/journal/src/lib.rs` defines `Journal<S>`, `Storage`, and `JournalHandle`.
- The `Journal<S>` Interface contains `header`, `previous_header`, `append`, `entry`, `remaining_capacity`, and `drain`.
- The `Storage` Interface is smaller: associated `Buffer`, `write_at`, and `read_at`.
- `/Users/amuldotexe/Desktop/oss-read-only/iggy/core/journal/src/file_storage.rs` implements `Storage` for `FileStorage` using compio positional reads/writes and tracks `write_offset`.
- `/Users/amuldotexe/Desktop/oss-read-only/iggy/core/journal/src/prepare_journal.rs` implements `Journal<FileStorage>` for `PrepareJournal` and tests with temp directories plus synthetic `PrepareHeader` messages.

Architecture lens:
This is a useful split between two Modules with different depths. `Storage` is intentionally narrow: positional IO only. `Journal` is deeper: it owns header lookup, append semantics, capacity, entry recovery, and draining. The seam keeps consensus durability logic from depending directly on `compio::fs::File`, while the file adapter keeps unsafe single-threaded runtime assumptions local to `FileStorage`. The leverage is strongest for tests and future adapters: an in-memory storage adapter can verify journal behavior without touching compio, while the production adapter can focus on file semantics.

Reusable code shape:
```rust
pub trait PositionalStorage {
    type Buffer;
    fn write_at(&self, offset: usize, buf: Self::Buffer) -> impl Future<Output = io::Result<usize>>;
    fn read_at(&self, offset: usize, buf: Self::Buffer) -> impl Future<Output = io::Result<Self::Buffer>>;
}

pub trait DurableJournal<S: PositionalStorage> {
    type Header;
    type Entry;

    fn append(&self, entry: Self::Entry) -> impl Future<Output = io::Result<()>>;
    fn entry(&self, header: &Self::Header) -> impl Future<Output = Option<Self::Entry>>;
    fn drain(&self, ops: RangeInclusive<u64>) -> impl Future<Output = io::Result<Vec<Self::Entry>>>;
}
```

Transfer rule:
Use this pattern when a durable state machine needs append/replay semantics but the storage substrate might vary. Keep the file adapter honest about its runtime invariants, and keep journal invariants in the journal Module. The deletion test should show that removing `Journal<S>` would scatter header ordering, entry decoding, and capacity rules across consensus code.

Verification hook:
Run the same journal behavior tests against a temp-file adapter and an in-memory adapter: append N entries, fetch by header, fetch previous header, recover after reopen, drain a range, preserve sorted drained entries, reject corrupted entries, and calculate remaining capacity after snapshot advancement.

## Repo Coverage: /Users/amuldotexe/Desktop/oss-read-only/warp

### Concept: Embedded tree-sitter language registry as a parser/query adapter seam

Evidence:
- `/Users/amuldotexe/Desktop/oss-read-only/warp/crates/languages/src/lib.rs` embeds `grammars` with `RustEmbed`, defines `SUPPORTED_LANGUAGES`, and exposes `language_by_name` plus `language_by_filename`.
- `LanguageRegistry` caches `Arc<Language>` values in a `Mutex<HashMap<String, Arc<Language>>>`.
- `Language` packages parser grammar, highlight query, optional indent query, indent unit, comment prefix, bracket pairs, optional symbols query, and display name.
- `load_language` maps internal names to arborium names, loads YAML config, loads highlight query text from arborium, and optionally loads `indents.scm` and `identifiers.scm`.
- `/Users/amuldotexe/Desktop/oss-read-only/warp/crates/syntax_tree/src/lib.rs` consumes `Language` through `SyntaxTreeState::set_language`, `parse_text`, `highlights_in_ranges`, and `indentation_at_point`.
- `/Users/amuldotexe/Desktop/oss-read-only/warp/crates/syntax_tree/src/queries/indent_query_tests.rs` tests Rust indentation through `language_by_filename("test.rs")`, `SyntaxTreeState::parse_text`, and `indentation_delta`.

Architecture lens:
The `Language` Module is a deep Interface over several parser-adjacent implementation details: tree-sitter grammar identity, highlight query, indent query, symbols query, comment syntax, brackets, and display labels. The registry is the seam between editor Modules and grammar adapters. Editor code asks for `Language` by file or name; it does not learn where grammars are embedded, which query files exist, or how aliases like `rs` and `go` normalize. Locality is strong because grammar/query loading failures live in `load_language` and `load_query`, while editor behavior crosses the stable `Language` Interface.

Reusable code shape:
```rust
pub struct Language {
    pub grammar: tree_sitter::Language,
    pub highlights: Query,
    pub indents: Option<Query>,
    pub symbols: Option<Query>,
    pub comment_prefix: Option<String>,
    pub brackets: Vec<(char, char)>,
}

pub struct LanguageRegistry {
    languages: Mutex<HashMap<String, Arc<Language>>>,
}

impl LanguageRegistry {
    pub fn by_filename(&self, path: &Path) -> Option<Arc<Language>> {
        let name = normalize_extension(path)?;
        self.by_name(name)
    }
}
```

Transfer rule:
For parser-heavy Rust tools, make `Language` the Interface consumed by highlighters, indenters, symbol extractors, and code-intelligence Modules. Do not let each caller open query files or decide aliases. Add adapters for each grammar behind the registry seam and keep the editor-facing Interface stable.

Verification hook:
For every supported language, test filename detection, alias normalization, YAML/config loading, highlight query compilation, optional indent query compilation, optional symbol query compilation, and one behavior-level parser test. Warp's Rust indentation test is a good model: parse a real snippet and assert indent deltas at specific points.

### Concept: Language server candidate trait decouples detection, installation, and metadata

Evidence:
- `/Users/amuldotexe/Desktop/oss-read-only/warp/crates/lsp/src/language_server_candidate.rs` defines `LanguageServerCandidate` with `should_suggest_for_repo`, `is_installed_in_data_dir`, `is_installed_on_path`, default `is_installed`, `install`, and `fetch_latest_server_metadata`.
- `/Users/amuldotexe/Desktop/oss-read-only/warp/crates/lsp/src/supported_servers.rs` defines `LSPServerType`, maps servers to language IDs, returns display names and arguments, and constructs concrete `LanguageServerCandidate` adapters.
- `/Users/amuldotexe/Desktop/oss-read-only/warp/crates/lsp/src/install.rs` contains install/metadata helpers such as asset URL and checksum handling.
- `/Users/amuldotexe/Desktop/oss-read-only/warp/crates/lsp/src/command_builder.rs` provides the command execution wrapper used by candidates.

Architecture lens:
This is a real seam because each language server has a different adapter: rust-analyzer, gopls, pyright, TypeScript language server, clangd, and others. The Interface is not merely "start a server"; it includes detection heuristics, install location, PATH fallback, metadata fetching, and command execution constraints. That makes the Module deep enough for callers to ask "what should I suggest/install?" without knowing npm, Go, PATH, binary URLs, or checksums. The `CommandBuilder` dependency is also a seam: tests can adapt process execution without editing candidate logic.

Reusable code shape:
```rust
#[async_trait]
pub trait ToolCandidate: Send + Sync {
    async fn should_suggest_for_repo(&self, repo: &Path, commands: &CommandRunner) -> bool;
    async fn is_installed_in_data_dir(&self, commands: &CommandRunner) -> bool;
    async fn is_installed_on_path(&self, commands: &CommandRunner) -> bool;
    async fn install(&self, metadata: ToolMetadata, commands: &CommandRunner) -> anyhow::Result<()>;
    async fn fetch_latest_metadata(&self) -> anyhow::Result<ToolMetadata>;
}
```

Transfer rule:
Use this shape when a code-intelligence tool needs pluggable external tool discovery. Put runtime-specific knowledge behind candidate adapters, keep caller logic in terms of suggestions/installability/metadata, and only introduce the seam once at least two tools differ in install or detection behavior.

Verification hook:
Use fake command adapters to verify repository heuristics, data-dir detection, PATH fallback, install command construction, metadata digest enforcement, and multi-language server mapping. The behavior to test is the candidate Interface, not the subprocess implementation.

## Repo Coverage: /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cozodb__cozo

### Concept: Fixed-rule payload turns graph algorithms into query-language adapters

Evidence:
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cozodb__cozo/cozo-core/src/fixed_rule/mod.rs` defines `FixedRulePayload`, `FixedRuleInputRelation`, `FixedRule`, and `SimpleFixedRule`.
- `FixedRuleInputRelation` exposes `arity`, `ensure_min_len`, `get_binding_map`, `iter`, and `prefix_iter`.
- `FixedRulePayload` exposes `inputs_count`, `get_input`, `name`, `span`, and typed option extractors such as `expr_option`, `string_option`, `integer_option`, `pos_integer_option`, `non_neg_integer_option`, `float_option`, `unit_interval_option`, and `bool_option`.
- The `FixedRule` Interface requires `init_options`, `arity`, and `run(payload, out, poison)`.
- The same file imports `graph::prelude::{CsrLayout, DirectedCsrGraph, GraphBuilder}`, showing fixed rules are used to host graph algorithms behind the query execution seam.

Architecture lens:
`FixedRule` is a deep Module because it lets query execution call arbitrary algorithms through one Interface while hiding relation lookup, arity checking, typed options, source-span diagnostics, output materialization, and cancellation. `FixedRulePayload` is the Adapter context: it converts query-language manifests into algorithm-friendly relation iterators and typed options. This keeps locality for parser and execution errors; algorithms do not parse option expressions by hand, and the query planner does not learn each algorithm's internal graph representation. The seam is real because algorithms vary while the payload contract remains stable.

Reusable code shape:
```rust
pub trait QueryAlgorithm: Send + Sync {
    fn init_options(&self, options: &mut BTreeMap<String, Expr>, span: SourceSpan) -> Result<()> { Ok(()) }
    fn arity(&self, options: &BTreeMap<String, Expr>, head: &[Symbol], span: SourceSpan) -> Result<usize>;
    fn run(&self, payload: AlgorithmPayload<'_, '_>, out: &mut TempRelation, cancel: CancelToken) -> Result<()>;
}

pub struct AlgorithmPayload<'a, 'tx> {
    manifest: &'a AlgorithmCall,
    stores: &'a BTreeMap<Symbol, EpochStore>,
    tx: &'a SessionTx<'tx>,
}
```

Transfer rule:
For Rust query engines or graph walkers, put user-extensible algorithms behind a payload Module rather than passing raw parser nodes into algorithms. The payload Interface should own option typing, relation lookup, arity checking, spans, and cancellation. That gives leverage to every algorithm and keeps syntax evolution local to the payload.

Verification hook:
Test at the fixed-rule seam: missing option reports the rule name and span, wrong option type reports expected type, relation arity errors include source span, in-memory and stored relations both iterate through the same `FixedRuleInputRelation`, prefix iterators return the expected subset, and `poison` cancellation stops a long-running rule.

### Concept: Storage and transaction traits encode MVCC/time-travel invariants explicitly

Evidence:
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cozodb__cozo/cozo-core/src/storage/mod.rs` defines `Storage<'s>` with associated `Tx: StoreTx<'s>`.
- `Storage<'s>` requires `storage_kind`, `transact(write)`, `range_compact`, and `batch_put`.
- `StoreTx<'s>` requires `get`, `multi_get`, `put`, `supports_par_put`, `par_put`, `del`, `par_del`, `del_range_from_persisted`, `exists`, `commit`, `range_scan_tuple`, `range_skip_scan_tuple`, `range_scan`, `range_count`, and `total_scan`.
- The module has concrete storage adapters under `storage/mem.rs`, plus feature-gated adapters for RocksDB, Sled, SQLite, TiKV, and newer RocksDB variants.
- The docs on `get` and `exists` describe `for_update` MVCC behavior; the docs on `range_skip_scan_tuple` describe validity/time-travel semantics.

Architecture lens:
This is a storage seam with a broad but meaningful Interface. It is not shallow because the Interface expresses the database invariants callers must rely on: MVCC conflict behavior, ascending batch puts, range compaction, parallel put capability, validity-aware scans, raw scans, decoded tuple scans, and commit failure semantics. Adapters differ substantially, so the seam is real. Locality is the main payoff: backend-specific details live in adapter Modules, while query execution can reason in terms of transactions, tuple scans, and validity timestamps.

Reusable code shape:
```rust
pub trait Engine<'e>: Send + Sync + Clone {
    type Tx: EngineTx<'e>;

    fn engine_kind(&self) -> &'static str;
    fn transact(&'e self, write: bool) -> Result<Self::Tx>;
    fn batch_put<'a>(&'a self, rows: Box<dyn Iterator<Item = Result<(Vec<u8>, Vec<u8>)>> + 'a>) -> Result<()>;
}

pub trait EngineTx<'e>: Sync {
    fn get(&self, key: &[u8], for_update: bool) -> Result<Option<Vec<u8>>>;
    fn commit(&mut self) -> Result<()>;
    fn range_scan<'a>(&'a self, lower: &[u8], upper: &[u8]) -> Box<dyn Iterator<Item = Result<(Vec<u8>, Vec<u8>)>> + 'a>
    where
        'e: 'a;
}
```

Transfer rule:
Use this pattern when a query engine supports multiple storage backends and the transaction semantics are part of correctness. Do not hide MVCC or time-travel semantics in comments near call sites; put them in the Interface and require adapters to either implement them or fail with explicit unsupported errors.

Verification hook:
Run a backend-independent transaction suite: write/read/commit, write conflict with `for_update`, range order, batch-put ascending assumptions, range delete, decoded tuple scan, validity/time-travel scan, unsupported time-travel error, parallel-put capability consistency, and compaction no-op tolerance.

## Repo Coverage: /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/indradb__indradb

### Concept: Object-safe graph transaction interface enables plugins and remote adapters

Evidence:
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/indradb__indradb/lib/src/database.rs` defines `DynIter<'a, T>`, `Transaction<'a>`, `Datastore`, and `Database<D: Datastore>`.
- `Transaction<'a>` intentionally avoids generic method arguments because object safety is needed for plugins.
- The `Transaction` Interface includes graph reads (`all_vertices`, `range_vertices`, `specific_vertices`, `all_edges`, `range_edges`, `specific_edges`), property queries, deletes, `sync`, creates, `bulk_insert`, property indexing, and property updates.
- `Datastore` has an associated transaction type and a single `transaction()` method.
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/indradb__indradb/lib/src/tests/mod.rs` exports datastore implementation tests for reuse outside the crate.
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/indradb__indradb/proto/src/tests.rs` implements `Transaction<'a>` and `Datastore` for a remote client test adapter, then reuses database behavior through the same Interface.
- Plugin examples under `plugins/naive_vertex_count/src/lib.rs` accept `&mut dyn indradb::Transaction<'a>`.

Architecture lens:
The graph transaction Module is deliberately deep: one Interface hides memory storage, RocksDB storage, remote protocol clients, and plugin execution. The Interface is large, but it earns its keep because graph database semantics are large: vertex/edge identity, property indexing, range scans, mutation, deletion, syncing, and bulk insert all need consistency. Object safety is a design constraint baked into the Interface, not an afterthought; this gives leverage to plugin adapters that receive `dyn Transaction` and locality to datastore implementers. The shared test module makes the Interface the test surface.

Reusable code shape:
```rust
pub type DynIter<'a, T> = Box<dyn Iterator<Item = Result<T>> + 'a>;

pub trait GraphTransaction<'a> {
    fn all_vertices(&'a self) -> Result<DynIter<'a, Vertex>>;
    fn specific_edges(&'a self, edges: Vec<Edge>) -> Result<DynIter<'a, Edge>>;
    fn create_vertex(&mut self, vertex: &Vertex) -> Result<bool>;
    fn create_edge(&mut self, edge: &Edge) -> Result<bool>;
    fn bulk_insert(&mut self, items: Vec<BulkInsertItem>) -> Result<()>;
}

pub trait GraphDatastore {
    type Transaction<'a>: GraphTransaction<'a>
    where
        Self: 'a;
    fn transaction(&self) -> Self::Transaction<'_>;
}
```

Transfer rule:
Use object-safe transaction Interfaces when extension Modules or plugin Modules need to operate over local and remote adapters uniformly. Keep generic convenience on query builder types, but make the execution seam object-safe if plugins must cross it.

Verification hook:
Build an implementation-independent graph suite like IndraDB's exported tests: vertex create/get/delete, edge create/get/delete, range order, reversed edge range, property set/get/delete, property indexing, bulk insert, sync behavior, remote adapter parity, and plugin execution through `&mut dyn Transaction`.

## Repo Coverage: /Users/amuldotexe/Desktop/reference-repos-yard/polonius

### Concept: Facts-in, output-out borrow analysis makes algorithm variants swappable

Evidence:
- `/Users/amuldotexe/Desktop/reference-repos-yard/polonius/polonius-engine/src/lib.rs` states the engine input is `AllFacts` and outputs are returned via `Output`; it re-exports `AllFacts`, `Atom`, `FactTypes`, `Algorithm`, and `Output`.
- `/Users/amuldotexe/Desktop/reference-repos-yard/polonius/polonius-engine/src/output/mod.rs` defines `Algorithm` variants: `Naive`, `DatafrogOpt`, `LocationInsensitive`, `Compare`, and `Hybrid`.
- The same file defines `Output<T: FactTypes>` with error outputs plus optional debug relations such as `loan_live_at`, `origin_contains_loan_at`, `subset`, liveness, initialization, and known containment maps.
- `Output::compute(all_facts, algorithm, dump_enabled)` performs common preparation: initialization data, liveness, shared `datafrog::Relation` inputs, and algorithm-specific execution.
- `/Users/amuldotexe/Desktop/reference-repos-yard/polonius/src/cli.rs` loads tab-delimited facts, calls `Output::compute`, then optionally dumps tuples or graphviz output.
- `/Users/amuldotexe/Desktop/reference-repos-yard/polonius/src/program.rs` converts parser IR effects into `AllFacts` by interning origins, loans, variables, paths, and points.

Architecture lens:
Polonius is a clean compiler-analysis Module: the external Interface is facts plus an algorithm selector; the implementation can swap Datalog/datafrog strategies without changing callers. `Algorithm::Compare` is an especially useful verification adapter because it treats two implementations as mutually checking adapters behind the same analysis Interface. The leverage is high for code intelligence: parsing, fact loading, analysis, and output dumping are separate Modules joined by stable fact and output shapes. Locality is also strong: adding an optimized algorithm should touch the output implementation, not the CLI or fact parser.

Reusable code shape:
```rust
pub enum Algorithm {
    Naive,
    Optimized,
    Compare,
}

pub struct AnalysisOutput<F: FactTypes> {
    pub errors: FxHashMap<F::Point, Vec<F::Loan>>,
    pub debug_relations: DebugRelations<F>,
}

impl<F: FactTypes> AnalysisOutput<F> {
    pub fn compute(facts: &AllFacts<F>, algorithm: Algorithm, dump: bool) -> Self {
        let context = SharedContext::prepare(facts);
        run_algorithm(context, algorithm, dump)
    }
}
```

Transfer rule:
For compiler/code-intelligence analyses, make extracted facts the seam and keep algorithm variants behind an enum or trait that returns the same output shape. Add a compare mode whenever a new optimized implementation is intended to preserve the semantics of a naive one.

Verification hook:
Run the same fact fixtures through every algorithm variant and assert identical user-facing errors. Add a `Compare` variant that fails if optimized and naive outputs diverge. Keep dump/graphviz output behind the same `Output` shape so debugging does not create a second analysis path.

## Repo Coverage: /Users/amuldotexe/Desktop/reference-repos-yard/flux

### Concept: rustc driver callback as a compiler-extension seam

Evidence:
- `/Users/amuldotexe/Desktop/reference-repos-yard/flux/crates/flux-driver/src/callbacks.rs` defines `FluxCallbacks` implementing `rustc_driver::Callbacks`.
- `config` asserts no existing query override, overrides `mir_borrowck`, and injects predefined Flux symbols.
- `after_analysis` calls `verify`, then either continues or stops compilation based on configuration.
- `verify` builds a `FluxSession`, registers query providers from `flux_desugar` and `flux_fhir_analysis`, loads the crate store, creates a `GlobalEnv`, runs `check_crate`, saves metadata, finalizes Lean encoding, prints timings, and finishes diagnostics.
- `trigger_queries` explicitly calls query providers per `DefKind`, creating a traversal table for traits, impls, functions, constructors, enums, structs, aliases, and opaque types.
- `mir_borrowck` uses `rustc_borrowck::consumers::get_bodies_with_borrowck_facts`, stores MIR body data, then delegates back to the original borrowck provider.
- `/Users/amuldotexe/Desktop/reference-repos-yard/flux/tests/tests/compiletest.rs` runs positive and negative UI tests through compiletest with the Flux binary as `rustc_path`.

Architecture lens:
The rustc callback Module is a high-leverage Adapter at the compiler seam. Its Interface is dictated by rustc, but the implementation converts that narrow seam into Flux-specific providers, metadata, diagnostics, proof encoding, query triggering, and borrow-check fact capture. Locality is critical here: all unstable rustc integration assumptions are concentrated in the callback Module and compiletest harness. The query override is deep because it alters one compiler query while preserving the original provider call after extracting facts.

Reusable code shape:
```rust
pub struct ToolCallbacks;

impl rustc_driver::Callbacks for ToolCallbacks {
    fn config(&mut self, config: &mut rustc_interface::interface::Config) {
        config.override_queries = Some(|_, providers| {
            providers.mir_borrowck = capture_then_delegate_borrowck;
        });
    }

    fn after_analysis(&mut self, compiler: &Compiler, tcx: TyCtxt<'_>) -> Compilation {
        verify_crate(compiler, tcx);
        Compilation::Stop
    }
}
```

Transfer rule:
For Rust compiler extensions, keep the rustc-driver Adapter thin at the trait boundary and move tool-specific analysis into a `GlobalEnv` or equivalent Module. Override rustc queries only where the tool needs compiler-private facts, then delegate to the original provider to preserve rustc behavior.

Verification hook:
Use compiletest with positive and negative fixture directories. Assert diagnostics, metadata emission, auxiliary crate handling, query override behavior, and full-compilation mode. Add a small fixture that exercises borrow facts so the `mir_borrowck` capture path is covered.

## Repo Coverage: /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PRQL__tree-sitter-prql

### Concept: Tree-sitter grammar crate as a minimal parser adapter

Evidence:
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PRQL__tree-sitter-prql/grammar.js` defines the `prql` grammar with extras, precedence levels, `program`, keyword rules, `prql` header rules, target dialects, pipelines, variables, function definitions, parameters, and calls.
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PRQL__tree-sitter-prql/queries/highlights.scm` and `queries/injections.scm` exist as editor-facing query adapters.
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PRQL__tree-sitter-prql/test/corpus` exists for tree-sitter corpus verification.
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PRQL__tree-sitter-prql/bindings/rust/lib.rs` exposes `language() -> tree_sitter::Language`, `NODE_TYPES`, and `test_can_load_grammar`.

Architecture lens:
This repo shows the smallest useful tree-sitter Module shape. The JavaScript grammar is the implementation of syntax recognition; the Rust binding is the Interface consumed by Rust parser clients. The seam is intentionally tiny: `language()` plus static node types. Highlight and injection queries are separate adapter files so editor features can evolve without changing grammar loading. For Rust-adjacent parser work, this is a good baseline for keeping generated parser internals out of application code.

Reusable code shape:
```rust
extern "C" {
    fn tree_sitter_domain_lang() -> tree_sitter::Language;
}

pub fn language() -> tree_sitter::Language {
    unsafe { tree_sitter_domain_lang() }
}

pub const NODE_TYPES: &str = include_str!("../../src/node-types.json");

#[test]
fn grammar_loads() {
    let mut parser = tree_sitter::Parser::new();
    parser.set_language(language()).unwrap();
}
```

Transfer rule:
For any language grammar intended for Rust consumers, expose a tiny Rust binding Module and keep grammar, query, and corpus concerns in their normal tree-sitter locations. Resist adding semantic analysis to the grammar crate unless the Interface needs it; downstream code-intelligence Modules can consume the parse tree and query files separately.

Verification hook:
Run `tree-sitter test` against `test/corpus`, compile the Rust binding, load the grammar in a Rust unit test, compile highlight and injection queries against the language, and parse representative snippets with `root_node().has_error() == false`.

## Repo Coverage: /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bytecodealliance__tree-sitter-wit

### Concept: Grammar helpers and generated LanguageFn make WIT parser integration version-stable

Evidence:
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bytecodealliance__tree-sitter-wit/grammar.js` defines a WIT grammar with helper `commaSeparatedList`, `extras`, `externals`, `supertypes`, package declarations, use paths, worlds, interfaces, imports, exports, includes, resources, variants, records, flags, types, and functions.
- The grammar uses external tokens for block comments, doc comments, error sentinels, and line doc content.
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bytecodealliance__tree-sitter-wit/queries/highlights.scm`, `queries/folds.scm`, and `queries/injections.scm` exist as query adapters.
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bytecodealliance__tree-sitter-wit/bindings/rust/lib.rs` exposes `LANGUAGE: tree_sitter_language::LanguageFn`, `NODE_TYPES`, optional query constants behind cfg flags, and a grammar-load test.

Architecture lens:
The WIT grammar Module demonstrates a slightly deeper grammar Interface than older `language() -> Language` bindings. `LanguageFn` keeps the exported Rust Interface aligned with newer tree-sitter loading conventions, while cfg-gated query constants let package features decide which editor adapters are exposed. The helper function `commaSeparatedList` improves grammar locality: repeated comma-list syntax is one implementation detail, not duplicated through records, variants, includes, and params.

Reusable code shape:
```rust
use tree_sitter_language::LanguageFn;

extern "C" {
    fn tree_sitter_my_language() -> *const ();
}

pub const LANGUAGE: LanguageFn = unsafe { LanguageFn::from_raw(tree_sitter_my_language) };
pub const NODE_TYPES: &str = include_str!("../../src/node-types.json");

#[cfg(with_highlights_query)]
pub const HIGHLIGHTS_QUERY: &str = include_str!("../../queries/highlights.scm");
```

Transfer rule:
Use `LanguageFn` bindings for modern tree-sitter Rust crates and expose query files as cfg-gated constants when package consumers may want a slim parser-only build. In grammar.js, introduce helper Modules for repeated syntactic forms so dialect evolution has locality.

Verification hook:
Test grammar loading through `Parser::set_language(&LANGUAGE.into())`, run corpus fixtures, compile optional queries under each cfg feature, and include at least one fixture for external-token behavior such as nested comments, doc comments, and sentinel recovery.

## Repo Coverage: /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-grammars__tree-sitter-markdown

### Concept: Combined block/inline parser hides two tree-sitter grammars behind one Markdown tree

Evidence:
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-grammars__tree-sitter-markdown/tree-sitter-markdown/grammar.js` parses CommonMark block structure and sections.
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-grammars__tree-sitter-markdown/tree-sitter-markdown-inline/grammar.js` exists as the inline grammar sibling.
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-grammars__tree-sitter-markdown/bindings/rust/lib.rs` exposes `LANGUAGE`, `INLINE_LANGUAGE`, block/inline highlight and injection query constants, block/inline node-type constants, and grammar-load tests for both grammars.
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-grammars__tree-sitter-markdown/bindings/rust/parser.rs` defines `MarkdownParser`, `MarkdownTree`, `MarkdownCursor`, and `MarkdownParseOptions`.
- `MarkdownParser::parse_with_options` first parses the block tree, then switches parser language to inline grammar, sets included ranges for inline-bearing nodes, and builds inline trees plus an `inline_indices` map.
- `MarkdownTree::edit` applies a single `InputEdit` to both block and inline trees; `MarkdownCursor` abstracts walking across block and inline trees.
- Tests in `parser.rs` assert inline tree lookup and incremental reparse behavior after `InputEdit`.

Architecture lens:
This is a deep parser Module. The public Interface is one `MarkdownParser`, one `MarkdownTree`, and one cursor; the implementation hides two grammars, included ranges, inline-tree indexing, edit propagation, and cursor transitions. That is exactly the right depth for Markdown, where callers want a document tree and do not want to coordinate block and inline parsers themselves. The seam gives leverage to code-intelligence consumers: they can walk a combined tree while still knowing whether a node is inline when field IDs or grammar-specific internals matter.

Reusable code shape:
```rust
pub struct DualGrammarParser {
    parser: tree_sitter::Parser,
    outer_language: Language,
    inner_language: Language,
}

pub struct CombinedTree {
    outer_tree: Tree,
    inner_trees: Vec<Tree>,
    inner_indices: HashMap<usize, usize>,
}

impl CombinedTree {
    pub fn edit(&mut self, edit: &InputEdit) {
        self.outer_tree.edit(edit);
        for tree in &mut self.inner_trees {
            tree.edit(edit);
        }
    }
}
```

Transfer rule:
Use this pattern for languages with nested syntactic regimes: Markdown block/inline, HTML with script/style, notebooks with code cells, templating languages, and doc-comment examples. Expose a combined tree/cursor Interface so callers get locality; keep included-range orchestration inside the parser Module.

Verification hook:
Test block grammar load, inline grammar load, parse of nested inline constructs, cursor traversal from outer to inner tree and back, `InputEdit` propagation, incremental parse with old tree, query constants compiling for both grammars, and benchmarks that reparse after a small edit.

## Repo Coverage: /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/yijunyu__tree-sitter-parsers

### Concept: Vendored parser bundle for regression comparison across language grammars

Evidence:
- The bounded scan found many tree-sitter parser snapshots under one repo path, including `tree-sitter-rust-0.20.0/grammar.js`, `tree-sitter-rust-0.20.0/queries/highlights.scm`, `tree-sitter-rust-0.20.0/queries/injections.scm`, and older `tree-sitter-rust-0.19.1` fixtures.
- The same bundle includes Rust-binding-ready `Cargo.toml` files and grammars for PHP, Kotlin, Bash, C++, C, C#, HTML, Python, Go, Ruby, JavaScript, Solidity, CSS, Scala, and more.
- Several snapshots include `test/corpus`, `corpus`, `queries/tags.scm`, `queries/locals.scm`, `queries/highlights.scm`, and `queries/injections.scm`.

Architecture lens:
This repo is less a single Module and more a corpus Adapter: a versioned bundle of grammar implementations that can feed parser compatibility tests. Its leverage is comparative. A code-intelligence tool can run the same query compiler, parse harness, or symbol extractor across many grammar snapshots and detect assumptions that only work for one grammar version. Locality comes from treating grammars as data fixtures rather than as dependencies wired into production code.

Reusable code shape:
```text
parser-corpus/
  tree-sitter-rust-0.19.1/
    grammar.js
    queries/highlights.scm
  tree-sitter-rust-0.20.0/
    grammar.js
    queries/highlights.scm
  tree-sitter-python-0.19.0/
    grammar.js
    queries/tags.scm
```

Transfer rule:
For parser/code-intelligence projects, keep a vendored grammar corpus separate from the production registry. Use it to test assumptions across grammar families and versions: query names, node-type stability, injection patterns, tags, locals, generated Rust binding compatibility, and parse error tolerance.

Verification hook:
Build a harness that walks each grammar snapshot, checks for `grammar.js`, compiles available `.scm` queries where a generated parser exists, parses corpus examples, records node-type diffs across versions, and flags missing queries. Keep failures per grammar so one stale snapshot does not hide the rest of the corpus signal.

## Repo Coverage: /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/raphtory-src

### Concept: Inherited core graph operations make graph views thin without making callers shallow

Evidence:
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/raphtory-src/raphtory-storage/src/core_ops.rs` defines `is_view_compatible`, `CoreGraphOps`, `InheritCoreGraphOps`, and blanket implementations for `Arc<T>` and `&T`.
- `CoreGraphOps` has a small required Interface, `core_graph(&self) -> &GraphStorage`, with many default methods over it: `id_type`, event id reads, unfiltered node/edge/layer counts, single-layer resolution, `core_edges`, `core_edge`, `core_nodes`, `core_node`, `node_meta`, and `edge_meta`.
- `CoreGraphOps` is implemented directly for `GraphStorage`.
- `InheritCoreGraphOps` plus the `Base` trait delegates `core_graph()` through wrapped graph view types.

Architecture lens:
This is a strong Rust trait-depth pattern. The Interface implementers must provide only the underlying graph seam; the trait supplies shared graph operations. That gives leverage to every graph view and preserves locality for storage access rules. It also keeps graph view Modules thin without becoming shallow pass-throughs: the view's implementation decides how it owns or references a base graph, while callers get the rich `CoreGraphOps` behavior uniformly.

Reusable code shape:
```rust
pub trait CoreOps: Send + Sync {
    fn core(&self) -> &CoreStorage;

    fn nodes(&self) -> Nodes<'_> {
        self.core().nodes()
    }

    fn edges(&self) -> Edges<'_> {
        self.core().edges()
    }
}

pub trait InheritCoreOps: Base {}

impl<T: InheritCoreOps + Send + Sync> CoreOps for T
where
    T::Base: CoreOps,
{
    fn core(&self) -> &CoreStorage {
        self.base().core()
    }
}
```

Transfer rule:
Use this pattern when many view/adaptor types should share core operations but differ in filtering, ownership, or lifetime shape. Put defaults in the deep trait and require one small method only if the default behavior is truly universal.

Verification hook:
Create tests that compare direct storage and wrapped views through the same trait: pointer compatibility, node/edge count parity, metadata access, layer resolution, `Arc<T>` and `&T` blanket behavior, and behavior after applying filters or materialized views.

### Concept: Validated graph paths encode filesystem safety as types

Evidence:
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/raphtory-src/raphtory-graphql/src/paths.rs` defines `ValidGraphPaths`, `ValidPath`, `ExistingGraphFolder`, `ValidGraphFolder`, `NewPath`, `ValidWriteableGraphFolder`, `InternalPathValidationError`, and `PathValidationError`.
- `valid_path_inner` rejects double slashes, backslashes, roots, parent directories, current-directory components, hidden paths, symlinks, and nested graph folders.
- `ExistingGraphFolder` and `ValidWriteableGraphFolder` both implement `ValidGraphPaths`.
- `WithPath` and `with_internal_errors` attach the user-facing path to internal validation failures.

Architecture lens:
The Module turns filesystem/path invariants into the Interface. Callers that accept `ValidGraphFolder` or `ValidWriteableGraphFolder` no longer need to remember root traversal, symlink, hidden path, metadata, namespace, and dirty-marker rules. The seam is real because existing and writeable graph paths are different adapters over the same validated path concept. Locality is excellent: path safety errors and user-facing error rendering live in one Module.

Reusable code shape:
```rust
pub trait ValidProjectPath {
    fn local_path(&self) -> &str;
    fn root(&self) -> &impl ProjectPaths;
}

pub struct ExistingProjectPath(ValidPath);
pub struct WriteableProjectPath {
    path: ValidPath,
    cleanup: Option<CleanupPath>,
}

fn validate_relative_path(root: PathBuf, relative: &str) -> Result<PathBuf, PathValidationError> {
    // reject root, parent, hidden, symlink, nested metadata, malformed separators
    todo!()
}
```

Transfer rule:
When graph/database artifacts live on disk, do not pass raw `PathBuf` past the validation seam. Promote validated paths into newtypes that encode whether the target exists, is writable, is a namespace, or is a graph. This gives downstream Modules stronger Interfaces and removes repeated filesystem checks.

Verification hook:
Test empty path, root path, parent traversal, current directory, backslash, double slash, hidden path, symlink, parent-is-graph, namespace-is-graph, graph-is-namespace, missing metadata, dirty-marker cleanup, and error messages that include the original user path.

## Repo Coverage: /Users/amuldotexe/Desktop/reference-repos-yard/zed

### Concept: Language registry loads native and WASM grammars behind one editor Interface

Evidence:
- `/Users/amuldotexe/Desktop/reference-repos-yard/zed/crates/language/src/language.rs` documents that the crate provides `Language`, `Grammar`, and `LanguageRegistry`, and exposes `LanguageConfig` for editor behavior such as brackets and line comments.
- The same file defines `Language` with config and optional grammar fields, query cursor pooling, `build_highlight_map`, `parse_text(grammar, text, old_tree)`, and tests that register test languages.
- `/Users/amuldotexe/Desktop/reference-repos-yard/zed/crates/language/src/language_registry.rs` defines `LanguageRegistry`, `LanguageRegistryState`, and `AvailableGrammar`.
- `AvailableGrammar` covers native grammars, unloaded WASM paths, loading state with waiters, loaded WASM grammars, and load failures.
- `/Users/amuldotexe/Desktop/reference-repos-yard/zed/crates/language/src/syntax_map.rs` and `syntax_map/syntax_map_tests.rs` exercise injection/syntax layering with a test registry.
- `/Users/amuldotexe/Desktop/reference-repos-yard/zed/crates/language/src/buffer.rs` owns `TreeSitterData`, parse status, highlights, outline, and buffer-level integration with language registry.

Architecture lens:
Zed's language Module is deep because editor callers interact with `Language`, `LanguageRegistry`, buffers, highlights, and syntax maps without knowing whether a grammar is native, unloaded WASM, currently loading, failed, or already loaded. The registry is the seam; grammar adapters vary behind it. Locality is high for parser lifecycle and query cursor reuse, which would otherwise leak into buffers, outline generation, injection layers, and language tools.

Reusable code shape:
```rust
enum AvailableGrammar {
    Native(Arc<Grammar>),
    Unloaded(PathBuf),
    Loading(PathBuf, Vec<oneshot::Sender<Result<Arc<Grammar>>>>),
    Loaded(PathBuf, Arc<Grammar>),
    LoadFailed(Arc<anyhow::Error>),
}

pub struct LanguageRegistry {
    state: RwLock<RegistryState>,
}

pub struct Language {
    config: LanguageConfig,
    grammar: Option<Arc<Grammar>>,
}
```

Transfer rule:
For IDE/code-intelligence Rust apps, model grammar availability as state in the registry rather than as ad hoc booleans at call sites. The registry Interface should hide native versus WASM loading, fan-out concurrent waiters, cache failures, and return a stable `Language` Module to consumers.

Verification hook:
Use test registries to cover native grammar registration, unloaded WASM transition to loading, concurrent load waiters, load failure caching, language config overrides, syntax injection layers, parse reuse with old trees, highlight map building, and buffer behavior when language support is unavailable.

## Repo Coverage: /Users/amuldotexe/Desktop/reference-repos-yard/marker

### Concept: Lint API and rustc driver adapter separate lint crates from compiler internals

Evidence:
- `/Users/amuldotexe/Desktop/reference-repos-yard/marker/marker_api/src/lint.rs` defines the public `Lint` struct and `declare_lint!` macro.
- `Lint` includes lint name, default level, explanation, macro reporting policy, fully qualified name, and an explicit instability acknowledgment field for manual construction.
- `/Users/amuldotexe/Desktop/reference-repos-yard/marker/marker_rustc_driver/src/lint_pass.rs` defines `RustcLintPass`, initializes a thread-local `Adapter`, registers Marker lints with rustc, then processes the crate in a single pass.
- `process_crate_lifetime` creates a storage-backed `'ast` lifetime, builds `RustcContext`, sets the Marker AST context, converts the local crate, and calls `adapter.process_krate`.
- `/Users/amuldotexe/Desktop/reference-repos-yard/marker/marker_rustc_driver/src/context.rs` defines `RustcContext` with `TyCtxt`, `LintStore`, storage, marker converter, rustc converter, and a `MarkerContext` wrapper.
- `RustcContext` implements `MarkerContextDriver` to emit Marker diagnostics through rustc lint diagnostics.

Architecture lens:
Marker separates the lint crate Interface from the rustc adapter. Lint authors see `marker_api`, `declare_lint!`, and `MarkerContext`; the driver owns rustc lifetimes, AST conversion, lint registration, and diagnostic bridging. This seam is deep because rustc integration is volatile and lifetime-heavy, while lint crates need a stable, plugin-like Interface. The `Storage<'ast>` lifetime anchor is especially important: it gives locality to arena allocation and prevents borrowed AST data from escaping the driver pass.

Reusable code shape:
```rust
pub struct Lint {
    pub name: &'static str,
    pub default_level: Level,
    pub explanation: &'static str,
}

pub struct CompilerLintPass;

impl<'tcx> rustc_lint::LateLintPass<'tcx> for CompilerLintPass {
    fn check_crate(&mut self, cx: &rustc_lint::LateContext<'tcx>) {
        let storage = Storage::default();
        let adapter_context = RustcContext::new(cx.tcx, lint_store(cx), &storage);
        adapter.process_crate(adapter_context.api_context(), adapter_context.local_crate());
    }
}
```

Transfer rule:
For lint/plugin ecosystems, keep compiler-private types behind a driver adapter and expose a stable lint author Interface. Make diagnostics, spans, AST maps, and semantic queries callback-based so the driver can translate them from rustc without lint crates depending on rustc internals.

Verification hook:
Run UI tests for sample lints, diagnostic spans, macro-report settings, lint-level attributes, panic/ICE handling, AST item lookup, type conversion, and driver registration. Add a test lint that emits every diagnostic part and verify rustc receives the correct span/note/help/suggestion.

## Repo Coverage: /Users/amuldotexe/Desktop/reference-repos-yard/creusot

### Concept: Verification models and ghost values encode proof-only interfaces

Evidence:
- `/Users/amuldotexe/Desktop/reference-repos-yard/creusot/creusot-std/src/model.rs` defines `View` and `DeepModel`.
- `View` uses `#[logic]` and `#[intrinsic("view")]` to expose shallow logical models through `@` notation.
- `DeepModel` exposes recursive logical models for equality, hashing, ordering, and data-structure specifications.
- `/Users/amuldotexe/Desktop/reference-repos-yard/creusot/creusot-std/src/ghost.rs` defines `Ghost<T>`, documents that ghost code is erased during normal compilation, and restricts deref/borrow operations to `#[check(ghost)]` contexts.
- `Ghost<T>` implements proof-only borrow helpers with `#[erasure(_)]`, `#[trusted]`, and `#[ensures]` contracts.
- `/Users/amuldotexe/Desktop/reference-repos-yard/creusot/why3/src/printer.rs` renders Why3 declarations and modules, and maintains a scope stack to produce fresh binder names.

Architecture lens:
Creusot's verification stdlib shows an Interface that deliberately does not exist at runtime. `View`, `DeepModel`, and `Ghost<T>` are proof Modules: callers use them to express specifications, while the implementation is erased, intrinsic, or trusted. The Why3 printer is a separate backend Adapter that turns translated declarations into stable text while keeping name-disambiguation locality inside `Scope`. This is the right seam for formal-methods Rust: runtime code, logical model, ghost proof state, and solver output each have different Interfaces.

Reusable code shape:
```rust
pub trait View {
    type ViewTy;
    #[logic]
    fn view(self) -> Self::ViewTy;
}

pub trait DeepModel {
    type DeepModelTy;
    #[logic]
    fn deep_model(self) -> Self::DeepModelTy;
}

#[opaque]
pub struct Ghost<T: ?Sized>(PhantomData<T>);
```

Transfer rule:
When embedding specifications into Rust, separate runtime Interfaces from proof Interfaces. Use model traits for logical views, ghost newtypes for erased proof state, and a backend printer/encoder Module for solver output. Do not let proof-only operations become normal callable runtime helpers.

Verification hook:
Use should-succeed and should-fail fixtures: view notation resolves only with `View`, deep models recurse through inner types, ghost deref fails outside ghost context, borrow helpers preserve ensures clauses, erased ghost code does not affect runtime output, and Why3 rendering avoids binder collisions.
## Repo Coverage: `/Users/amuldotexe/Desktop/TauriAppsOSS`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `TauriAppsOSS`
Evidence: `/Users/amuldotexe/Desktop/TauriAppsOSS/OSS-strategy-2026/2026-05-10-oss-clusters-and-hiring-timelines.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
# OSS Clusters And Hiring Timelines

Date: 2026-05-10

This note classifies the cloned OSS workspace through a Shreyas Doshi lens:

- Which repo clusters solve top-3 pains for maintainers and users
- Which clusters create the strongest hiring signal if contributions are consistent
- Which likely employers or org types may notice sustained contributions

Important note: the hiring predictions below are strategic inference, not a guarantee. They are based on local repo inventory plus a GitHub CLI activity snapshot for 2026-05-03 through 2026-05-10.

## Cluster Summary

| Cluster | Repos | 7d merged PRs | Open `good first issue` | Core pain solved | Hiring pull | Likely employer pull |
| --- | --- | ---: | ---: | --- | ---: | --- |
| AI devtools and agents | `codex`, `warp`, `zed-gpui`, `cocoindex`, `agent-debate`, `claude-peers-mcp`, `parseltongue-rust-LLM-companion` | 698 | 0 | Developer speed, agent UX, context quality, editor workflows | 5/5 | OpenAI, Warp, Zed, agent-tool startups, AI-native devtools teams |
| Core data and lakehouse engines | `polars`, `arrow-rs`, `datafusion`, `opendal`, `sail`, `auron` | 170 | 86 | Query correctness, performance, interoperability, file formats, execution engines | 5/5 | LakeHQ, Polars-adjacent teams, Arrow/DataFusion adopters, data infra startups, warehouse and lakehouse companies |
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/TauriAppsOSS/OSS-strategy-2026/2026-05-10-oss-clusters-and-hiring-timelines.md` and run `git -C /Users/amuldotexe/Desktop/TauriAppsOSS ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/airflow`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `oss-read-only/airflow`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/airflow/airflow-core/src/airflow/api_fastapi/__init__.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/oss-read-only/airflow/airflow-core/src/airflow/api_fastapi/__init__.py` and run `git -C /Users/amuldotexe/Desktop/oss-read-only/airflow ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/oss-read-only/claude-peers-mcp`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/claude-peers-mcp`; scan counts include file_count=14, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/oss-read-only/claude-peers-mcp ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/dbt-core`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `oss-read-only/dbt-core`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/dbt-core/crates/dbt-adapter-sql/src/tokenizer.rs`; scan counts include rust_files=1358, cargo_manifests=123, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
N/A: could not read `/Users/amuldotexe/Desktop/oss-read-only/dbt-core/crates/dbt-adapter-sql/src/tokenizer.rs`: [Errno 2] No such file or directory: '/Users/amuldotexe/Desktop/oss-read-only/dbt-core/crates/dbt-adapter-sql/src/tokenizer.rs'
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/oss-read-only/dbt-core/crates/dbt-adapter-sql/src/tokenizer.rs` and run `git -C /Users/amuldotexe/Desktop/oss-read-only/dbt-core ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/openobserve`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `oss-read-only/openobserve`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/openobserve/src/config/src/tantivy/tokenizer/mod.rs`; scan counts include rust_files=1118, cargo_manifests=9, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
N/A: could not read `/Users/amuldotexe/Desktop/oss-read-only/openobserve/src/config/src/tantivy/tokenizer/mod.rs`: [Errno 2] No such file or directory: '/Users/amuldotexe/Desktop/oss-read-only/openobserve/src/config/src/tantivy/tokenizer/mod.rs'
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/oss-read-only/openobserve/src/config/src/tantivy/tokenizer/mod.rs` and run `git -C /Users/amuldotexe/Desktop/oss-read-only/openobserve ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/plotly.py`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust-Adjacent Parser Reference From `oss-read-only/plotly.py`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/plotly.py/doc/unconverted/python/logos.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```text
    language: python
    name: python2
  plotly:
    description: How to add images as logos to Plotly charts.
    display_as: advanced_opt
    language: python
    layout: base
    name: Logos
    order: 6
    page_type: example_index
    permalink: python/logos/
    thumbnail: thumbnail/your-tutorial-chart.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/oss-read-only/plotly.py/doc/unconverted/python/logos.md` and run `git -C /Users/amuldotexe/Desktop/oss-read-only/plotly.py ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/oss-read-only/streamlit`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/streamlit`; scan counts include file_count=9524, rust_files=0, cargo_manifests=0, candidate_paths=80.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/oss-read-only/streamlit ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/CodeEDA`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/CodeEDA`; scan counts include file_count=0, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/CodeEDA ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust Module Architecture Slice From `personal-repos-lane/accio-tools`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/why-this-folder-exists.md`; scan counts include rust_files=9, cargo_manifests=6, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```text
  -> CPU candidate generator returns top 5 with scores and reasons
  -> cheap LLM judge reviews only those 5 compact cards
  -> system returns top 1 selected tool, abstain, or needs-more-metadata
  -> eval report proves recall, abstention, token reduction, and failure buckets
```

The CPU layer should optimize top-5 recall and explainability. The judge can only choose among what the CPU layer surfaced.

## Reference Repos In `git-ref-repo`

| repo | role in our study | why it was shortlisted | most useful local evidence |
| --- | --- | --- | --- |
| `VOTR` | Primary router algorithm reference | Strongest match for the assignment: MCP-scale tool retrieval, hybrid retrieval, field-aware reranking, confidence handoff, abstention/null-route guards, and ablations. | `README.md` highlights dense + BM25 + SPLADE-lite with weighted RRF, field-aware reranking, dynamic k, and robustness suites. |
| `lazy-tool` | Local-first implementation reference | Shows how to build a practical local router with exact/name search, FTS5 BM25, optional vector search, score weights, `why_matched`, and passthrough fallback. | `README.md` search algorithm section and `internal/search/weights.go`. |
| `contextweaver` | Choice-card and bounded-context reference | Shows how to turn a large tool catalog into compact `ChoiceCard`s without exposing full schemas, plus deterministic routing, bounded graphs, and benchmark framing. | `docs/tool_router.md`, `docs/benchmarks.md`, `src/contextweaver/routing/`. |
| `graph-tool-call` | Graph/path routing reference | Useful for multi-tool workflows where the answer is a chain, not one tool. Demonstrates BM25 + graph traversal + embeddings + MCP annotations via weighted RRF. | `README.md` sections on workflow retrieval, weighted RRF, graph traversal, reranking, and
...
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/why-this-folder-exists.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/accio-tools ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/StableToolBench`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/accio-tools/ignore-references/git-ref-repo/StableToolBench`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/StableToolBench/server/main_mirrorapi.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import os, sys
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.requests import Request
import uvicorn
import time
import json
import yaml
import requests
from typing import Union
from utils import standardize, change_name

from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
import openai
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/StableToolBench/server/main_mirrorapi.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/StableToolBench ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/appworld`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/accio-tools/ignore-references/git-ref-repo/appworld`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/appworld/experiments/code/common/tool_parsers.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
from appworld.common.types import FromDict


class ToolParser(FromDict):
    def parse(self, text: str) -> list[dict[str, Any]]:
        raise NotImplementedError


@ToolParser.register("kimi-k2-instruct")
class KimiK2InstructToolParser(ToolParser):
    # Note: Not needed with the official Kimi provider.
    def parse(self, text: str) -> list[dict[str, Any]]:
        # Taken from:
        # https://huggingface.co/moonshotai/Kimi-K2-Instruct/blob/main/docs/tool_call_guidance.md
        if "<|tool_calls_section_begin|>" not in text:
            return []
        pattern = r"<\|tool_calls_section_begin\|>(.*?)<\|tool_calls_section_end\|>"
        tool_calls_sections = re.findall(pattern, text, re.DOTALL)
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/appworld/experiments/code/common/tool_parsers.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/appworld ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/gorilla`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/accio-tools/ignore-references/git-ref-repo/gorilla`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/gorilla/berkeley-function-call-leaderboard/bfcl_eval/eval_checker/ast_eval/__init__.py`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
N/A: selected file was empty.
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/gorilla/berkeley-function-call-leaderboard/bfcl_eval/eval_checker/ast_eval/__init__.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/gorilla ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/n2-QLN`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/n2-QLN`; scan counts include file_count=34, rust_files=0, cargo_manifests=0, candidate_paths=2.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/n2-QLN ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/apache-spark-shallow`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust-Adjacent Parser Reference From `personal-repos-lane/apache-spark-shallow`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/apache-spark-shallow/common/unsafe/src/main/java/org/apache/spark/sql/catalyst/expressions/HiveHasher.java`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```text

/**
 * Simulates Hive's hashing function from Hive v1.2.1
 * org.apache.hadoop.hive.serde2.objectinspector.ObjectInspectorUtils#hashcode()
 */
public class HiveHasher {

  @Override
  public String toString() {
    return HiveHasher.class.getSimpleName();
  }

  public static int hashInt(int input) {
    return input;
  }

  public static int hashLong(long input) {
    return (int) ((input >>> 32) ^ input);
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/apache-spark-shallow/common/unsafe/src/main/java/org/apache/spark/sql/catalyst/expressions/HiveHasher.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/apache-spark-shallow ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/confido-exploration-01`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/confido-exploration-01`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/confido-exploration-01/Sol-variant-01/src/prompt_parser.rs`; scan counts include rust_files=21, cargo_manifests=2, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/confido-exploration-01/Sol-variant-01/src/prompt_parser.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/confido-exploration-01 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/dynamic-analysis`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust Module Architecture Slice From `personal-repos-lane/dynamic-analysis`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/dynamic-analysis/data/render/src/bin/main.rs`; scan counts include rust_files=5, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```rust
use anyhow::{Context, Result};
use askama::Template;
use pico_args::Arguments;
use render::types::{Entry, ParsedEntry, Tag, Tags, Type};
use render::{check_deprecated, create_api, create_catalog};
use std::collections::BTreeMap;
use std::env;
use std::ffi::OsStr;
use std::fs;
use std::io;
use std::path::PathBuf;

struct Args {
    tags: PathBuf,
    tools: PathBuf,
    md_out: PathBuf,
    json_out: PathBuf,
    skip_deprecated: bool,
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/dynamic-analysis/data/render/src/bin/main.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/dynamic-analysis ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/floo-network`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust Module Architecture Slice From `personal-repos-lane/floo-network`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/floo-network/src/main.rs`; scan counts include rust_files=1, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```rust
N/A: selected file was empty.
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/floo-network/src/main.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/floo-network ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/hackerrank-exploration-202604`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/hackerrank-exploration-202604`; scan counts include file_count=16665, rust_files=0, cargo_manifests=0, candidate_paths=80.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/hackerrank-exploration-202604 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/cypher-shell-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/cypher-shell-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/cypher-shell-src/cypher-shell/src/main/java/org/neo4j/shell/parser/ShellStatementParser.java`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
package org.neo4j.shell.parser;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.regex.Pattern;
import javax.annotation.Nonnull;

/**
 * A cypher aware parser which can detect shell commands (:prefixed) or cypher.
 */
public class ShellStatementParser implements StatementParser
{

    private static final Pattern SHELL_CMD_PATTERN = Pattern.compile( "^\\s*:.+\\s*$" );
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/cypher-shell-src/cypher-shell/src/main/java/org/neo4j/shell/parser/ShellStatementParser.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/cypher-shell-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-browser-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-browser-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-browser-src/src/browser/modules/Stream/CypherFrame/RelatableView/relatable/utils/is-last-index.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 */
export default function isLastIndex(arr: any[], index: number) {
  return index === arr.length - 1
}
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-browser-src/src/browser/modules/Stream/CypherFrame/RelatableView/relatable/utils/is-last-index.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-browser-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-go-driver-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-go-driver-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-go-driver-src/neo4j/internal/bolt/parseroutingtable.go`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
	idb "github.com/neo4j/neo4j-go-driver/v6/neo4j/internal/db"
)

// Parses a record assumed to contain a routing table into common DB API routing table struct
// Returns nil if error while parsing
func parseRoutingTableRecord(rec *db.Record) *idb.RoutingTable {
	ttl, ok := rec.Values[0].(int64)
	if !ok {
		return nil
	}
	listOfX, ok := rec.Values[1].([]any)
	if !ok {
		return nil
	}

	table := &idb.RoutingTable{
		TimeToLive: int(ttl),
	}
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-go-driver-src/neo4j/internal/bolt/parseroutingtable.go` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-go-driver-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-src/community/bolt/src/main/java/org/neo4j/bolt/protocol/common/message/decoder/util/TransactionInitiatingMetadataParser.java`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import org.neo4j.packstream.util.PackstreamConversions;
import org.neo4j.values.virtual.MapValue;

public final class TransactionInitiatingMetadataParser {
    public static final String FIELD_DATABASE_NAME = "db";
    private static final String FIELD_IMPERSONATED_USER = "imp_user";

    private TransactionInitiatingMetadataParser() {}

    public static String readDatabaseName(MapValue meta) throws PackstreamReaderException {
        var databaseName =
                PackstreamConversions.asNullableStringValue(FIELD_DATABASE_NAME, meta.get(FIELD_DATABASE_NAME));

        // we permit both empty strings and null values as a reference to the default user/system
        // database, so we'll unify it at decoder level
        if (databaseName != null && databaseName.isEmpty()) {
            return null;
        }
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-src/community/bolt/src/main/java/org/neo4j/bolt/protocol/common/message/decoder/util/TransactionInitiatingMetadataParser.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/antlr-grammars-v4-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/antlr-grammars-v4-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/antlr-grammars-v4-src/ada/ada2012/Antlr4ng/AdaLexerBase.ts`; scan counts include rust_files=18, cargo_manifests=1, tree_sitter_query_files=0, pest_files=8, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import { Lexer, CharStream, Token } from "antlr4ng";
import { AdaLexer } from "./AdaLexer.js";

export abstract class AdaLexerBase extends Lexer {
    _lastTokenType: number;

    constructor(input: CharStream) {
        super(input);
        this._lastTokenType = 0;
    }

    nextToken() {
        var token = super.nextToken();
        if (token.channel === Token.DEFAULT_CHANNEL) {
            this._lastTokenType = token.type;
        }
        return token;
    }
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/antlr-grammars-v4-src/ada/ada2012/Antlr4ng/AdaLexerBase.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/antlr-grammars-v4-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-hugegraph-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-hugegraph-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-hugegraph-src/hugegraph-pd/hg-pd-core/src/main/java/org/apache/hugegraph/pd/meta/ConfigMetaStore.java`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import org.apache.hugegraph.pd.config.PDConfig;
import org.apache.hugegraph.pd.grpc.Metapb;

public class ConfigMetaStore extends MetadataRocksDBStore {

    private final long clusterId;

    public ConfigMetaStore(PDConfig pdConfig) {
        super(pdConfig);
        this.clusterId = pdConfig.getClusterId();
    }

    /**
     * Update the storage status of the graph space
     *
     * @param
     */
    public Metapb.GraphSpace setGraphSpace(Metapb.GraphSpace graphSpace) throws PDException {
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-hugegraph-src/hugegraph-pd/hg-pd-core/src/main/java/org/apache/hugegraph/pd/meta/ConfigMetaStore.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-hugegraph-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/arangodb-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/arangodb-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/arangodb-src/3rdParty/boost/1.78.0/boost/any/bad_any_cast.hpp`; scan counts include rust_files=5, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text

// See http://www.boost.org/libs/any for Documentation.

#ifndef BOOST_ANYS_BAD_ANY_CAST_HPP_INCLUDED
#define BOOST_ANYS_BAD_ANY_CAST_HPP_INCLUDED

#include <boost/config.hpp>
#ifdef BOOST_HAS_PRAGMA_ONCE
#   pragma once
#endif

#ifndef BOOST_NO_RTTI
#include <typeinfo>
#endif

#include <stdexcept>

namespace boost {
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/arangodb-src/3rdParty/boost/1.78.0/boost/any/bad_any_cast.hpp` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/arangodb-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/cugraph-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/cugraph-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/cugraph-src/thirdparty/mmio/mmio.c`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text

#include "mmio.h"

int mm_read_unsymmetric_sparse(const char *fname, int *M_, int *N_, int *nz_,
                double **val_, int **I_, int **J_)
{
    FILE *f;
    MM_typecode matcode;
    int M, N, nz;
    int i;
    double *val;
    int *I, *J;

    if ((f = fopen(fname, "r")) == NULL)
            return -1;


    if (mm_read_banner(f, &matcode) != 0)
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/cugraph-src/thirdparty/mmio/mmio.c` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/cugraph-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/duckdb-src`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/duckdb-src`; scan counts include file_count=14646, rust_files=0, cargo_manifests=0, candidate_paths=80.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/duckdb-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gapbs-src`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gapbs-src`; scan counts include file_count=46, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gapbs-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphchi-cpp-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphchi-cpp-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphchi-cpp-src/toolkits/collaborative_filtering/parser.hpp`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
#define MAX_FEATURES 256
#define FEATURE_WIDTH 68 //MAX NUMBER OF ALLOWED FEATURES IN TEXT FILE

#include "../parsers/common.hpp"

char tokens[]={"\n\r\t ;,"};
char csv_tokens[] = {",\n\r"};
char * ptokens = tokens;
int csv = 0;
int limit_rating = 0;
int has_header_titles = 0;
int file_columns = 0;
int train_only = 0;
int validation_only = 0;
std::vector<std::string> header_titles;
double inputGlobalMean = 0;
int latent_factors_inmem_size = 0;
int num_feature_bins_size = 0;
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphchi-cpp-src/toolkits/collaborative_filtering/parser.hpp` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphchi-cpp-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/igraph-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/igraph-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/igraph-src/examples/simple/igraph_community_fastgreedy.c`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text

    igraph_small(&graph, 6, IGRAPH_UNDIRECTED,
                 0,1, 1,2, 2,3, 2,4, 2,5, 3,4, 3,5, 4,5, -1);
    igraph_community_fastgreedy(&graph, &weights, &merges,
                                /*modularity*/ NULL,
                                /*membership=*/ NULL);
    igraph_matrix_int_print(&merges);
    igraph_destroy(&graph);
    igraph_vector_destroy(&weights);
    igraph_matrix_int_destroy(&merges);

    return 0;
}
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/igraph-src/examples/simple/igraph_community_fastgreedy.c` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/igraph-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ladybug-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ladybug-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ladybug-src/src/function/cast/cast_array.cpp`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
#include "function/cast/functions/cast_array.h"

#include "common/exception/conversion.h"
#include "common/type_utils.h"
#include <format>

namespace lbug {
namespace function {

bool CastArrayHelper::checkCompatibleNestedTypes(LogicalTypeID sourceTypeID,
    LogicalTypeID targetTypeID) {
    switch (sourceTypeID) {
    case LogicalTypeID::ANY: {
        return true;
    }
    case LogicalTypeID::LIST: {
        return targetTypeID == LogicalTypeID::ARRAY || targetTypeID == LogicalTypeID::LIST;
    }
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ladybug-src/src/function/cast/cast_array.cpp` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ladybug-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics_platforms_graphblas-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust-Adjacent Parser Reference From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics_platforms_graphblas-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics_platforms_graphblas-src/src/main/java/science/atlarge/graphalytics/graphblas/algorithms/lcc/LocalClusteringCoefficientJob.java`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```text
package science.atlarge.graphalytics.graphblas.algorithms.lcc;

import science.atlarge.graphalytics.domain.graph.Graph;
import science.atlarge.graphalytics.execution.RunSpecification;
import science.atlarge.graphalytics.graphblas.GraphblasConfiguration;
import science.atlarge.graphalytics.graphblas.GraphblasJob;

/**
 * Local Clustering Coefficient job implementation for GraphBLAS. This class is responsible for formatting LCC-specific
 * arguments to be passed to the platform executable, and does not include the implementation of the algorithm.
 *
 * @author Bálint Hegyi
 */
public final class LocalClusteringCoefficientJob extends GraphblasJob {

	/**
	 * Creates a new LocalClusteringCoefficientJob object with all mandatory parameters specified.
	 * @param platformConfig the platform configuration.
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics_platforms_graphblas-src/src/main/java/science/atlarge/graphalytics/graphblas/algorithms/lcc/LocalClusteringCoefficientJob.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics_platforms_graphblas-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/libcypher-parser-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/libcypher-parser-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/libcypher-parser-src/lib/src/ast.c`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
 * limitations under the License.
 */
#include "../../config.h"
#include "ast.h"
#include "astnode.h"
#include "util.h"
#include <assert.h>
#include <math.h>


struct cypher_astnode_vts
{
    const struct cypher_astnode_vt *statement;
    const struct cypher_astnode_vt *statement_option;
    const struct cypher_astnode_vt *cypher_option;
    const struct cypher_astnode_vt *cypher_option_param;
    const struct cypher_astnode_vt *explain_option;
    const struct cypher_astnode_vt *profile_option;
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/libcypher-parser-src/lib/src/ast.c` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/libcypher-parser-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/nalgebra-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/nalgebra-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/nalgebra-src/nalgebra-sparse/src/convert/impl_std_ops.rs`; scan counts include rust_files=428, cargo_manifests=6, tree_sitter_query_files=0, pest_files=2, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
use crate::csr::CsrMatrix;
use nalgebra::storage::RawStorage;
use nalgebra::{ClosedAddAssign, DMatrix, Dim, Matrix, Scalar};
use num_traits::Zero;

impl<'a, T, R, C, S> From<&'a Matrix<T, R, C, S>> for CooMatrix<T>
where
    T: Scalar + Zero,
    R: Dim,
    C: Dim,
    S: RawStorage<T, R, C>,
{
    fn from(matrix: &'a Matrix<T, R, C, S>) -> Self {
        convert_dense_coo(matrix)
    }
}

impl<'a, T> From<&'a CooMatrix<T>> for DMatrix<T>
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/nalgebra-src/nalgebra-sparse/src/convert/impl_std_ops.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/nalgebra-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ongdb-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ongdb-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ongdb-src/community/collections/src/main/java/org/neo4j/helpers/collection/CastingIterator.java`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import java.util.Iterator;

/**
 * An iterator which filters for elements of a given subtype, and casts to this type.
 *
 * @param <T> the type of elements returned by this iterator.
 * @param <A> the type of elements read by this iterator. This must be a supertype of T.
 */
public class CastingIterator<T extends A, A> extends PrefetchingIterator<T>
{
    private final Iterator<A> source;
    private Class<T> outClass;

    public CastingIterator( Iterator<A> source, Class<T> outClass )
    {
        this.source = source;
        this.outClass = outClass;
    }
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ongdb-src/community/collections/src/main/java/org/neo4j/helpers/collection/CastingIterator.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ongdb-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/rust-rocksdb-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust Module Architecture Slice From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/rust-rocksdb-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/rust-rocksdb-src/librocksdb-sys/tests/ffi.rs`; scan counts include rust_files=66, cargo_manifests=2, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```rust
// limitations under the License.
//

// This code is based on <https://github.com/facebook/rocksdb/blob/master/db/c_test.c>, revision a10e8a056d569acf6a52045124e6414ad33bdfcd.

#![allow(
    non_snake_case,
    non_upper_case_globals,
    static_mut_refs,
    unused_mut,
    unused_unsafe,
    unused_variables
)]

use libc::*;
use librocksdb_sys::*;
use std::borrow::Cow;
use std::env;
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/rust-rocksdb-src/librocksdb-sys/tests/ffi.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/rust-rocksdb-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/sprs-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/sprs-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/sprs-src/sprs/benches/sparse_dense_products.rs`; scan counts include rust_files=71, cargo_manifests=13, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
use ndarray::{Array, Array2, ShapeBuilder};
use sprs::{CsMat, CsVec};

fn sparse_dense_dotprod_default(bench: &mut Bencher) {
    let w = Array::range(0., 10., 0.00001);
    let x = CsVec::new(1000000, vec![0, 200000, 800000], vec![1., 2., 3.]);
    bench.iter(|| {
        x.dot(&w);
    });
}

fn sparse_dense_dotprod_specialized(bench: &mut Bencher) {
    let w = Array::range(0., 10., 0.00001);
    let x = CsVec::new(1000000, vec![0, 200000, 800000], vec![1., 2., 3.]);
    bench.iter(|| {
        x.dot_dense(w.view());
    });
}
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/sprs-src/sprs/benches/sparse_dense_products.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/sprs-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tigergraph-ecosys-src`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust-Adjacent Parser Reference From `personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tigergraph-ecosys-src`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tigergraph-ecosys-src/demos/guru_scripts/loop_detection_demo/queries/ExprFunctions.hpp`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```text
/******************************************************************************
 * Copyright (c) 2015-2016, GraphSQL Inc.
 * All rights reserved.
 * Project: GraphSQL Query Language
 * udf.hpp: a library of user defined functions used in queries.
 *
 * - This library should only define functions that will be used in
 *   GraphSQL Query scripts. Other logics, such as structs and helper
 *   functions that will not be directly called in the GQuery scripts,
 *   must be put into "ExprUtil.hpp" under the same directory where
 *   this file is located.
 *
 * - Supported type of return value and parameters
 *     - int
 *     - float
 *     - double
 *     - bool
 *     - string (don't use std::string)
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tigergraph-ecosys-src/demos/guru_scripts/loop_detection_demo/queries/ExprFunctions.hpp` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tigergraph-ecosys-src ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/law-diagrams`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/law-diagrams`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/law-diagrams/.kiro/steering/mermaid-syntax-guide.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
inclusion: always
---

# Mermaid Syntax Guide and Best Practices

## Purpose
This guide provides comprehensive rules and best practices for creating syntactically correct Mermaid diagrams in the Constitution of India analysis project.

## Common Syntax Errors and Fixes

### 1. Direction Declaration Issues

**❌ WRONG:**
```mermaid
graph TD
    direction TD E1[General Provisions]  # Invalid - direction mixed with node
```

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/law-diagrams/.kiro/steering/mermaid-syntax-guide.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/law-diagrams ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/mp4-to-mp3`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/mp4-to-mp3`; scan counts include file_count=1, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/mp4-to-mp3 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/notes202408`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/notes202408`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/notes202408/twitter_analysis_202408/json_files_archive/periscope-broadcast-metadata.js`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```javascript
version https://git-lfs.github.com/spec/v1
oid sha256:26c9070ff5bdf00b9929c4fda11a62a7ee3e19c19bfecd22502a56e051a3eccc
size 4200
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/notes202408/twitter_analysis_202408/json_files_archive/periscope-broadcast-metadata.js` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/notes202408 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AB498__code-context-provider-mcp`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AB498__code-context-provider-mcp`; scan counts include file_count=12, rust_files=0, cargo_manifests=0, candidate_paths=2.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AB498__code-context-provider-mcp ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aerijo__tree-sitter-biber`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aerijo__tree-sitter-biber`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aerijo__tree-sitter-biber/src/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aerijo__tree-sitter-biber/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aerijo__tree-sitter-biber ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__tree-sitter-log`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__tree-sitter-log`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__tree-sitter-log/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__tree-sitter-log/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__tree-sitter-log ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AperturePlus__augmented-codebase-indexer`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AperturePlus__augmented-codebase-indexer`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AperturePlus__augmented-codebase-indexer/src/aci/cli/parser.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
"""
Command parser module for ACI interactive REPL.

Provides parsing functionality to convert user input strings into
structured command objects with proper handling of quoted strings,
escape characters, and keyword arguments.
"""

import shlex
from dataclasses import dataclass, field
from typing import Any


@dataclass
class ParsedCommand:
    """
    Represents a parsed command from user input.

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AperturePlus__augmented-codebase-indexer/src/aci/cli/parser.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AperturePlus__augmented-codebase-indexer ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AryanSaini26__CodeAtlas`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AryanSaini26__CodeAtlas`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AryanSaini26__CodeAtlas/src/codeatlas/parsers/__init__.py`; scan counts include rust_files=1, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
"""Parser registry - routes files to the correct language parser."""

from pathlib import Path

from codeatlas.models import ParseResult
from codeatlas.parsers.base import BaseParser
from codeatlas.parsers.bash_parser import BashParser
from codeatlas.parsers.c_parser import CParser
from codeatlas.parsers.cpp_parser import CppParser
from codeatlas.parsers.csharp_parser import CSharpParser
from codeatlas.parsers.elixir_parser import ElixirParser
from codeatlas.parsers.go_parser import GoParser
from codeatlas.parsers.haskell_parser import HaskellParser
from codeatlas.parsers.java_parser import JavaParser
from codeatlas.parsers.javascript_parser import JavaScriptParser
from codeatlas.parsers.julia_parser import JuliaParser
from codeatlas.parsers.kotlin_parser import KotlinParser
from codeatlas.parsers.lua_parser import LuaParser
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AryanSaini26__CodeAtlas/src/codeatlas/parsers/__init__.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AryanSaini26__CodeAtlas ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Boottify__glyph`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Boottify__glyph`; scan counts include file_count=6, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Boottify__glyph ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CI124__auto-ime`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CI124__auto-ime`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CI124__auto-ime/src/ASTAnalyzer.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import * as vscode from 'vscode';
import Parser from 'web-tree-sitter';
import * as path from 'path';
import { LogSink } from './logger';

/**
 * 【开发者必读】：WASM 文件存放与构建说明
 *
 * 1. web-tree-sitter 需要对应的 language wasm 文件 (例如: tree-sitter-javascript.wasm, tree-sitter-typescript.wasm, tree-sitter-python.wasm)。
 * 2. 在实际发布时，你需要从 npm 获取对应的包 (例如 `tree-sitter-javascript`)，
 *    然后将其中的 `.wasm` 文件拷贝到扩展的输出目录 (通常是本项目的 ./wasm 文件夹)。
 * 3. 本实现动态映射 VSCode languageId 到 wasm 文件名称。
 * 4. 如果遇到找不到 wasm 的情况，语法树解析会平滑降级，返回 false，此时不会触发任何输入法切换。
 */

export class ASTAnalyzer {
    private parser: Parser | null = null;
    private initialized = false;
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CI124__auto-ime/src/ASTAnalyzer.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CI124__auto-ime ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeBendKit__codeseek`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeBendKit__codeseek`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeBendKit__codeseek/rust-core/src/codegraph/parser.rs`; scan counts include rust_files=66, cargo_manifests=2, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
    FileIndex, SnippetIndex
};
use crate::codegraph::graph::CodeGraph;
use crate::codegraph::treesitter::TreeSitterParser;

/// 代码解析器，负责解析源代码文件并提取函数调用关系
pub struct CodeParser {
    /// 文件路径 -> 函数列表映射
    file_functions: HashMap<PathBuf, Vec<FunctionInfo>>,
    /// 函数名 -> 函数信息映射（用于解析调用关系）
    function_registry: HashMap<String, FunctionInfo>,
    /// Tree-sitter解析器
    ts_parser: TreeSitterParser,
    /// 文件索引
    file_index: FileIndex,
    /// 代码片段索引
    snippet_index: SnippetIndex,
}
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeBendKit__codeseek/rust-core/src/codegraph/parser.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeBendKit__codeseek ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Corbell-AI__Corbell`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Corbell-AI__Corbell`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Corbell-AI__Corbell/corbell/core/workspace.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
class NotionIntegration(BaseModel):
    """Notion integration config."""

    token: Optional[str] = None
    parent_page_id: Optional[str] = None

    model_config = {"extra": "ignore"}


class LinearIntegration(BaseModel):
    """Linear integration config."""

    api_key: Optional[str] = None
    team_id: Optional[str] = None
    default_project_id: Optional[str] = None

    model_config = {"extra": "ignore"}

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Corbell-AI__Corbell/corbell/core/workspace.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Corbell-AI__Corbell ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DeepSourceCorp__globstar`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DeepSourceCorp__globstar`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DeepSourceCorp__globstar/checkers/go/unsafe_pkg.test.go`; scan counts include rust_files=1, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text

import (
	"fmt"
	"os"
	// <expect-error>
	"unsafe"
)

func unsafeOperation() {
	var x int = 42
	ptr := unsafe.Pointer(&x) //unsafe operation
	fmt.Println("Unsafe operation with pointer:", ptr)
}


func safeOperation() {
	fmt.Println("Safe operation without unsafe package")
	fmt.Println("Current working directory:", os.Getwd())
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DeepSourceCorp__globstar/checkers/go/unsafe_pkg.test.go` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DeepSourceCorp__globstar ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/EarthChen__knowledge-base-service`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/EarthChen__knowledge-base-service`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/EarthChen__knowledge-base-service/indexer/tree_sitter_parser.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
"""Tree-sitter multi-language AST parser.

Parses source code files into structured AST data for extracting
functions, classes, imports, and call relationships.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

from tree_sitter import Node, Query, QueryCursor
from tree_sitter_language_pack import get_language, get_parser

from core.log import get_logger

if TYPE_CHECKING:
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/EarthChen__knowledge-base-service/indexer/tree_sitter_parser.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/EarthChen__knowledge-base-service ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/EvgeniyPeshkov__syntax-highlighter`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/EvgeniyPeshkov__syntax-highlighter`; scan counts include file_count=31, rust_files=0, cargo_manifests=0, candidate_paths=3.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/EvgeniyPeshkov__syntax-highlighter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/FosterG4__tree-sitter-mcpsaver`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/FosterG4__tree-sitter-mcpsaver`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/FosterG4__tree-sitter-mcpsaver/node-tree-sitter/README.md`; scan counts include rust_files=152, cargo_manifests=35, tree_sitter_query_files=65, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
# Node Tree-sitter

[![CI][ci]](https://github.com/tree-sitter/node-tree-sitter/actions/workflows/ci.yml)
[![npm][npm]](https://npmjs.com/package/tree-sitter)
[![docs][docs]](https://tree-sitter.github.io/node-tree-sitter)

This module provides Node.js bindings to the [tree-sitter] parsing library.

## Installation

```sh
npm install tree-sitter
```

## Basic Usage

### Prerequisites

```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/FosterG4__tree-sitter-mcpsaver/node-tree-sitter/README.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/FosterG4__tree-sitter-mcpsaver ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Graphify-Labs__graphify`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Graphify-Labs__graphify`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Graphify-Labs__graphify/tests/test_astro_extraction.py`; scan counts include rust_files=3, cargo_manifests=2, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
"""Tests for `.astro` extraction (#850).

Astro files have a TypeScript frontmatter block (`---...---`) at the top where
nearly all imports live, followed by an HTML-with-expressions template and
optionally `<script>` blocks. Tree-sitter-javascript fed the whole file produces
a top-level ERROR node because the template is not valid JS, so the JS AST pass
recovers nothing. The :func:`extract_astro` regex pass salvages imports from the
frontmatter and any `<script>` blocks — same strategy as :func:`extract_svelte`.
"""
from __future__ import annotations

from pathlib import Path

from graphify.detect import CODE_EXTENSIONS
from graphify.extract import (
    _make_id,
    extract_astro,
)
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Graphify-Labs__graphify/tests/test_astro_extraction.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Graphify-Labs__graphify ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/HiPhish__nvim-ts-rainbow2`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/HiPhish__nvim-ts-rainbow2`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/HiPhish__nvim-ts-rainbow2/queries/bash/rainbow-parens.scm`; scan counts include rust_files=1, cargo_manifests=0, tree_sitter_query_files=51, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```scheme
(command_substitution
  "$(" @opening
  ")"  @closing) @container

(expansion
  "${" @opening
  (":-" @intermediate)?
  "}" @closing) @container

;;; The double-bracket variant is a bashism
(test_command
  ["[[" "["] @opening
  ["]]" "]"] @closing) @container

(subshell
 "(" @opening
 ")" @closing) @container
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/HiPhish__nvim-ts-rainbow2/queries/bash/rainbow-parens.scm` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/HiPhish__nvim-ts-rainbow2 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/INS-JVidal__code-primer`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/INS-JVidal__code-primer`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/INS-JVidal__code-primer/src/parser.rs`; scan counts include rust_files=9, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
use anyhow::{Context, Result};

#[derive(Debug)]
pub struct TranslationUnit {
    pub kind: &'static str,
    pub name: String,
    pub signature: String,
    pub source: String,
    pub line_start: usize,
    pub line_end: usize,
    pub doc_comment: String,
    pub receiver: String,
}

#[derive(Debug)]
pub struct FileUnits {
    pub path: String,
    pub units: Vec<TranslationUnit>,
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/INS-JVidal__code-primer/src/parser.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/INS-JVidal__code-primer ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Jakedismo__codegraph-rust`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Jakedismo__codegraph-rust`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Jakedismo__codegraph-rust/crates/codegraph-core/src/integration/parser_graph.rs`; scan counts include rust_files=260, cargo_manifests=15, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
use crate::traits::{CodeParser, GraphStore};
use crate::{CodeNode, EdgeType, Result};
use async_trait::async_trait;
use parking_lot::RwLock;
use std::collections::{HashMap, HashSet};
use std::path::{Path, PathBuf};
use std::sync::Arc;
use tokio::fs;
use tokio::sync::Semaphore;
use tracing::{debug, info, warn};

/// Pluggable edge writer so core does not depend on graph crate edge APIs.
#[async_trait]
pub trait EdgeSink: Send + Sync {
    async fn add_edge(
        &self,
        from: crate::NodeId,
        to: crate::NodeId,
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Jakedismo__codegraph-rust/crates/codegraph-core/src/integration/parser_graph.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Jakedismo__codegraph-rust ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/JoosepAlviste__nvim-ts-context-commentstring`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/JoosepAlviste__nvim-ts-context-commentstring`; scan counts include file_count=16, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/JoosepAlviste__nvim-ts-context-commentstring ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Knaackee__code-explorer`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Knaackee__code-explorer`; scan counts include file_count=46, rust_files=0, cargo_manifests=0, candidate_paths=2.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Knaackee__code-explorer ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/LhKipp__tree-sitter-nu`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/LhKipp__tree-sitter-nu`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/LhKipp__tree-sitter-nu/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=4, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/LhKipp__tree-sitter-nu/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/LhKipp__tree-sitter-nu ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/MikeRecognex__mcp-codebase-index`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/MikeRecognex__mcp-codebase-index`; scan counts include file_count=36, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/MikeRecognex__mcp-codebase-index ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Nymphium__graft`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Nymphium__graft`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Nymphium__graft/src/cli/mod.rs`; scan counts include rust_files=10, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
use crate::graft::Transformer;
use crate::graft::languages::LANGUAGES;
use crate::graft::rules::RuleFile;
use anyhow::{Context, Result, anyhow};
use clap::Parser;
use glob::glob;
use rayon::prelude::*;
use serde::Serialize;
use std::fs;
use std::io::{self, Read};
use std::path::PathBuf;
use std::sync::{Arc, Mutex};

#[derive(Parser, Debug)]
#[command(
    author,
    version,
    about,
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Nymphium__graft/src/cli/mod.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Nymphium__graft ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OpenHands__OpenHands`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OpenHands__OpenHands`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OpenHands__OpenHands/enterprise/migrations/versions/113_bitbucket_dc_webhook_last_synced_tz.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
"""bitbucket_dc_webhook.last_synced TIMESTAMP WITHOUT TIME ZONE -> WITH TIME ZONE

Revision ID: 113
Revises: 112
Create Date: 2026-05-19 00:00:00.000000

The original migration (112) created ``last_synced`` as
``TIMESTAMP WITHOUT TIME ZONE``, which meant the route layer had to
strip ``tzinfo`` from every ``datetime.now(timezone.utc)`` value before
asyncpg would accept it. Converting to ``TIMESTAMP WITH TIME ZONE``
lets the model store offset-aware datetimes directly and removes the
``.replace(tzinfo=None)`` workarounds in ``bitbucket_dc_webhook_store``.

The conversion is in-place — Postgres reads existing naive values as
UTC during the column-type change, which is what they always
semantically were.
"""

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OpenHands__OpenHands/enterprise/migrations/versions/113_bitbucket_dc_webhook_last_synced_tz.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/OpenHands__OpenHands ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PrestonKnopp__tree-sitter-godot-resource`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PrestonKnopp__tree-sitter-godot-resource`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PrestonKnopp__tree-sitter-godot-resource/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PrestonKnopp__tree-sitter-godot-resource/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/PrestonKnopp__tree-sitter-godot-resource ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RahulModugula__odin`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RahulModugula__odin`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RahulModugula__odin/backend/app/parsers/tree_sitter_parser.py`; scan counts include rust_files=1, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
from tree_sitter import Node, Parser

from app.models.enums import Language
from app.models.schemas import (
    ClassInfo,
    CodeMetrics,
    CodeStructure,
    FunctionInfo,
)
from app.parsers.languages import get_language

# Node types that increase cyclomatic complexity
_COMPLEXITY_NODES: dict[str, set[str]] = {
    "python": {
        "if_statement",
        "elif_clause",
        "for_statement",
        "while_statement",
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RahulModugula__odin/backend/app/parsers/tree_sitter_parser.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/RahulModugula__odin ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/SaumyaJoshi2005__AlgoSnap`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/SaumyaJoshi2005__AlgoSnap`; scan counts include file_count=11, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/SaumyaJoshi2005__AlgoSnap ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/SrGaabriel__tree-sitter-soma`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/SrGaabriel__tree-sitter-soma`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/SrGaabriel__tree-sitter-soma/bindings/c/tree_sitter/tree-sitter-soma.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=4, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_SOMA_H_
#define TREE_SITTER_SOMA_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_soma(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_SOMA_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/SrGaabriel__tree-sitter-soma/bindings/c/tree_sitter/tree-sitter-soma.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/SrGaabriel__tree-sitter-soma ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/TheYoxy__tree-sitter-coda`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/TheYoxy__tree-sitter-coda`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/TheYoxy__tree-sitter-coda/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/TheYoxy__tree-sitter-coda/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/TheYoxy__tree-sitter-coda ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ViperJuice__Code-Index-MCP`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ViperJuice__Code-Index-MCP`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ViperJuice__Code-Index-MCP/ai_docs/tree_sitter_overview.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
# Tree-sitter Overview

## Introduction
Tree-sitter is a parser generator tool and incremental parsing library that builds a concrete syntax tree for source code and efficiently updates it as the code is edited. It's designed for use in text editors and development tools.

## Key Features

### Core Capabilities
- **Incremental Parsing**: Efficiently updates parse tree on edits
- **Error Recovery**: Produces useful trees even for syntax errors
- **Language Agnostic**: Supports 100+ programming languages
- **Fast Performance**: Written in C, with efficient memory usage
- **Thread Safe**: Can be used from multiple threads

### Why Tree-sitter for MCP Server
- Parse multiple languages with consistent API
- Extract accurate symbol information
- Handle malformed/incomplete code
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ViperJuice__Code-Index-MCP/ai_docs/tree_sitter_overview.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ViperJuice__Code-Index-MCP ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Wilfred__tree-sitter-elisp`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Wilfred__tree-sitter-elisp`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Wilfred__tree-sitter-elisp/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Wilfred__tree-sitter-elisp/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Wilfred__tree-sitter-elisp ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aMOPel__tree-sitter-nim`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aMOPel__tree-sitter-nim`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aMOPel__tree-sitter-nim/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=6, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aMOPel__tree-sitter-nim/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aMOPel__tree-sitter-nim ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/adamdelezuch89__repo-map-mcp`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/adamdelezuch89__repo-map-mcp`; scan counts include file_count=0, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/adamdelezuch89__repo-map-mcp ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aheber__tree-sitter-sfapex`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aheber__tree-sitter-sfapex`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aheber__tree-sitter-sfapex/apex/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=7, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aheber__tree-sitter-sfapex/apex/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aheber__tree-sitter-sfapex ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ajeetdsouza__loxcraft`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ajeetdsouza__loxcraft`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ajeetdsouza__loxcraft/src/syntax/ast.rs`; scan counts include rust_files=25, cargo_manifests=2, tree_sitter_query_files=0, pest_files=0, lalrpop_files=1.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct Var {
    pub name: String,
    /// This field is initialized as [`None`] by the parser, and is later
    /// filled by the resolver.
    pub depth: Option<usize>,
}
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ajeetdsouza__loxcraft/src/syntax/ast.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ajeetdsouza__loxcraft ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/alessandrobrunoh__Semantic-Delta-Protocol`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/alessandrobrunoh__Semantic-Delta-Protocol`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/alessandrobrunoh__Semantic-Delta-Protocol/src/error.rs`; scan counts include rust_files=13, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum SrpError {
    #[error("Internal error: {0}")]
    Internal(String),

    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),

    #[error("Parse error: {0}")]
    Parse(String),

    #[error("Serialization error: {0}")]
    Serialization(#[from] serde_json::Error),

    #[error("Analysis error: {0}")]
    Analysis(String),
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/alessandrobrunoh__Semantic-Delta-Protocol/src/error.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/alessandrobrunoh__Semantic-Delta-Protocol ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aorwall__moatless-tools`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aorwall__moatless-tools`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aorwall__moatless-tools/moatless/codeblocks/parser/queries/__init__.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
N/A: selected file was empty.
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aorwall__moatless-tools/moatless/codeblocks/parser/queries/__init__.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/aorwall__moatless-tools ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/arnarg__tree-sitter-todotxt`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/arnarg__tree-sitter-todotxt`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/arnarg__tree-sitter-todotxt/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/arnarg__tree-sitter-todotxt/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/arnarg__tree-sitter-todotxt ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/audityzer-org__audityzer-rust-analyzer`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/audityzer-org__audityzer-rust-analyzer`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/audityzer-org__audityzer-rust-analyzer/src/analyzer/detectors/mod.rs`; scan counts include rust_files=4, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
        "overflow-detector"
    }

    fn detect(&self, tree: &tree_sitter::Tree, source: &str) -> Vec<Vulnerability> {
        Vec::new() // TODO: Implement overflow detection
    }
}

impl crate::analyzer::VulnerabilityDetector for AccessControlDetector {
    fn name(&self) -> &str {
        "access-control-detector"
    }

    fn detect(&self, tree: &tree_sitter::Tree, source: &str) -> Vec<Vulnerability> {
        Vec::new() // TODO: Implement access control detection
    }
}
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/audityzer-org__audityzer-rust-analyzer/src/analyzer/detectors/mod.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/audityzer-org__audityzer-rust-analyzer ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bearcove__arborium`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bearcove__arborium`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bearcove__arborium/crates/arborium-highlight/src/tree_sitter.rs`; scan counts include rust_files=76, cargo_manifests=3, tree_sitter_query_files=204, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```rust
//! Tree-sitter based highlighting with thread-safe grammar sharing.
//!
//! This module provides a split architecture for efficient multi-threaded highlighting:
//!
//! - [`CompiledGrammar`]: Thread-safe compiled queries, shareable via `Arc`
//! - [`ParseContext`]: Per-thread parser state, cheap to create
//!
//! # Single-threaded Usage
//!
//! ```rust,ignore
//! use arborium_highlight::tree_sitter::{CompiledGrammar, ParseContext};
//!
//! let grammar = Arc::new(CompiledGrammar::new(config)?);
//! let mut ctx = ParseContext::for_grammar(&grammar)?;
//! let result = grammar.parse(&mut ctx, "fn main() {}");
//! ```
//!
//! # Multi-threaded Usage
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bearcove__arborium/crates/arborium-highlight/src/tree_sitter.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bearcove__arborium ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bezhermoso__tree-sitter-ghostty`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bezhermoso__tree-sitter-ghostty`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bezhermoso__tree-sitter-ghostty/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bezhermoso__tree-sitter-ghostty/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bezhermoso__tree-sitter-ghostty ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bonede__tree-sitter-ng`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bonede__tree-sitter-ng`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bonede__tree-sitter-ng/tree-sitter-agda/src/main/c/org_treesitter_TreeSitterAgda.c`; scan counts include rust_files=2, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text

#include <jni.h>
void *tree_sitter_agda();
/*
 * Class:     org_treesitter_TreeSitterAgda
 * Method:    tree_sitter_agda
 * Signature: ()J
 */
JNIEXPORT jlong JNICALL Java_org_treesitter_TreeSitterAgda_tree_1sitter_1agda
  (JNIEnv *env, jclass clz){
   return (jlong) tree_sitter_agda();
}
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bonede__tree-sitter-ng/tree-sitter-agda/src/main/c/org_treesitter_TreeSitterAgda.c` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bonede__tree-sitter-ng ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/casouri__tree-sitter-module`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/casouri__tree-sitter-module`; scan counts include file_count=9, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/casouri__tree-sitter-module ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/chunkhound__chunkhound`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/chunkhound__chunkhound`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/chunkhound__chunkhound/chunkhound/api/cli/parsers/__init__.py`; scan counts include rust_files=1, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
"""Argument parser utilities for ChunkHound CLI commands."""

from .main_parser import create_main_parser, setup_subparsers
from .mcp_parser import add_mcp_subparser
from .run_parser import add_run_subparser
from .search_parser import add_search_subparser

__all__ = [
    "create_main_parser",
    "setup_subparsers",
    "add_run_subparser",
    "add_mcp_subparser",
    "add_search_subparser",
]
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/chunkhound__chunkhound/chunkhound/api/cli/parsers/__init__.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/chunkhound__chunkhound ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/coder3101__tree-sitter-proto`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/coder3101__tree-sitter-proto`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/coder3101__tree-sitter-proto/bindings/c/tree-sitter-proto.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=4, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PROTO_H_
#define TREE_SITTER_PROTO_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_proto(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_PROTO_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/coder3101__tree-sitter-proto/bindings/c/tree-sitter-proto.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/coder3101__tree-sitter-proto ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cshuaimin__ssr.nvim`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cshuaimin__ssr.nvim`; scan counts include file_count=9, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cshuaimin__ssr.nvim ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/daun__tree-sitter-latte`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/daun__tree-sitter-latte`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/daun__tree-sitter-latte/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=5, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/daun__tree-sitter-latte/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/daun__tree-sitter-latte ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dhawwal__code-intelligence-ai`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dhawwal__code-intelligence-ai`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dhawwal__code-intelligence-ai/services/parser_service.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
from typing import List, Dict
import os
from tree_sitter import Language, Parser
import tree_sitter_python
import tree_sitter_javascript
from utils.file_utils import get_code_files

# Setup Languages
PY_LANGUAGE = Language(tree_sitter_python.language())
JS_LANGUAGE = Language(tree_sitter_javascript.language())
# Note: Further language bindings for Java/TS can be added similarly.
# We map simple extensions to available parsers.
LANGUAGE_MAP = {
    ".py": PY_LANGUAGE,
    ".js": JS_LANGUAGE,
    ".jsx": JS_LANGUAGE,
    ".ts": JS_LANGUAGE, # Fallback TS to JS tree-sitter since bindings are identical structurally for AST basic symbols
    ".tsx": JS_LANGUAGE
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dhawwal__code-intelligence-ai/services/parser_service.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dhawwal__code-intelligence-ai ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dominiclynchwoodlands-ui__codebaser`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dominiclynchwoodlands-ui__codebaser`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dominiclynchwoodlands-ui__codebaser/src/parsers/tree-sitter.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
/**
 * Tree-sitter based parser for Python, Go, Rust, Java, C, C++.
 *
 * Uses `web-tree-sitter` (WASM) — pure JS runtime, no native build. WASM
 * grammars come from `tree-sitter-wasms`. Tree-sitter is the parser used by
 * GitHub, Neovim, Atom, etc. — it produces a real AST, not regex approximations.
 *
 * Each language has its own node type names but the overall strategy is the
 * same: walk the top-level AST, extract declarations and imports, assemble
 * DeclaredSymbol records with line ranges and signatures.
 */

import * as path from 'node:path';
import * as fs from 'node:fs';
import { fileURLToPath } from 'node:url';
import {
  Parser,
  Language,
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dominiclynchwoodlands-ui__codebaser/src/parsers/tree-sitter.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/dominiclynchwoodlands-ui__codebaser ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/egibs__tree-sitter-poe`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/egibs__tree-sitter-poe`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/egibs__tree-sitter-poe/bindings/c/tree-sitter-path_of_exile.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_PATH_OF_EXILE_H_
#define TREE_SITTER_PATH_OF_EXILE_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_path_of_exile(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_PATH_OF_EXILE_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/egibs__tree-sitter-poe/bindings/c/tree-sitter-path_of_exile.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/egibs__tree-sitter-poe ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/emacs-tree-sitter__elisp-tree-sitter`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/emacs-tree-sitter__elisp-tree-sitter`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/emacs-tree-sitter__elisp-tree-sitter/core/src/parser.rs`; scan counts include rust_files=14, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```rust
use std::{cell::RefCell, rc::Rc};

use emacs::{defun, Result, Value, Vector, Env, ResultExt};
use tree_sitter::{Parser, Tree};

use crate::{
    types::{BytePos, Point, Range, Shared},
    lang::Language,
    error,
};

fn shared<T>(t: T) -> Shared<T> {
    Rc::new(RefCell::new(t))
}

impl_pred!(parser_p, &RefCell<Parser>);

/// Create a new parser.
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/emacs-tree-sitter__elisp-tree-sitter/core/src/parser.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/emacs-tree-sitter__elisp-tree-sitter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/er77__code-graph-rag-mcp`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/er77__code-graph-rag-mcp`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/er77__code-graph-rag-mcp/examples/parser-agent-demo.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
/**
 * TASK-001: Parser Agent Demo
 *
 * Demonstrates the high-performance parser agent with tree-sitter.
 * Shows incremental parsing, caching, and batch processing capabilities.
 */

import { EventEmitter } from "node:events";
import { ParserAgent } from "../src/agents/parser-agent.js";
import type { ParserTask } from "../src/types/parser.js";

async function main() {
  console.log("=".repeat(60));
  console.log("Parser Agent Demo - TASK-001");
  console.log("=".repeat(60));

  // Create knowledge bus for agent communication
  const knowledgeBus = new EventEmitter();
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/er77__code-graph-rag-mcp/examples/parser-agent-demo.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/er77__code-graph-rag-mcp ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/facebook__rocksdb`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/facebook__rocksdb`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/facebook__rocksdb/.github/scripts/parse-claude-review.js`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```javascript
// Parse Claude Code execution log and produce a markdown review comment.
//
// Usage from actions/github-script:
//   const parse = require('./.github/scripts/parse-claude-review.js');
//   const markdown = parse({ executionFile, conclusion, meta });
//
// Parameters:
//   executionFile - path to the JSON execution log from claude-code-base-action
//   conclusion    - 'success' or 'failure' from the action output
//   meta          - { trigger, autoMode, headSha, reviewer, isQuery, isPartial
//   }

const fs = require('fs');
const buildComment = require('./build-ai-review-comment.js');

module.exports = function parseClaude({executionFile, conclusion, meta}) {
  function getTriggerLine() {
    if (meta.trigger !== 'auto') {
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/facebook__rocksdb/.github/scripts/parse-claude-review.js` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/facebook__rocksdb ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/flurie__tree-sitter-jq`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/flurie__tree-sitter-jq`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/flurie__tree-sitter-jq/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/flurie__tree-sitter-jq/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/flurie__tree-sitter-jq ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/frozolotl__tree-sitter-typst`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/frozolotl__tree-sitter-typst`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/frozolotl__tree-sitter-typst/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/frozolotl__tree-sitter-typst/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/frozolotl__tree-sitter-typst ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ggfevans__zed-hujson`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ggfevans__zed-hujson`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ggfevans__zed-hujson/languages/hujson/brackets.scm`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=4, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```scheme
; Bracket pairs for editor matching.
("{" @open "}" @close)
("[" @open "]" @close)
("\"" @open "\"" @close)
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ggfevans__zed-hujson/languages/hujson/brackets.scm` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ggfevans__zed-hujson ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/glehmann__tree-sitter-earthfile`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/glehmann__tree-sitter-earthfile`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/glehmann__tree-sitter-earthfile/src/tree_sitter/parser.h`; scan counts include rust_files=3, cargo_manifests=2, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/glehmann__tree-sitter-earthfile/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/glehmann__tree-sitter-earthfile ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/google-gemini__gemini-cli`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/google-gemini__gemini-cli`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/google-gemini__gemini-cli/evals/redundant_casts.eval.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import path from 'node:path';
import fs from 'node:fs/promises';

describe('redundant_casts', () => {
  evalTest('USUALLY_PASSES', {
    suiteName: 'default',
    suiteType: 'behavioral',
    name: 'should not add redundant or unsafe casts when modifying typescript code',
    files: {
      'src/cast_example.ts': `
export interface User {
  id: string;
  name: string;
}

export function processUser(user: User) {
  // Narrowed check
  console.log("Processing user: " + user.name);
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/google-gemini__gemini-cli/evals/redundant_casts.eval.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/google-gemini__gemini-cli ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/haasonsaas__semantic-sast`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/haasonsaas__semantic-sast`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/haasonsaas__semantic-sast/semantic_sast/__main__.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
"""Main entry point for Semantic SAST."""

from .cli.main import main

if __name__ == '__main__':
    main()
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/haasonsaas__semantic-sast/semantic_sast/__main__.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/haasonsaas__semantic-sast ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hrayleung__Cocode`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hrayleung__Cocode`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hrayleung__Cocode/src-rust/code_parser.rs`; scan counts include rust_files=7, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
use ahash::AHashSet;
use pyo3::prelude::*;
use tree_sitter::{Language, Node, Parser};

fn ts_language(language: &str) -> Option<Language> {
    match language {
        "python" => Some(tree_sitter_python::LANGUAGE.into()),
        "go" => Some(tree_sitter_go::LANGUAGE.into()),
        "rust" => Some(tree_sitter_rust::LANGUAGE.into()),
        "c" => Some(tree_sitter_c::LANGUAGE.into()),
        "cpp" => Some(tree_sitter_cpp::LANGUAGE.into()),
        "javascript" => Some(tree_sitter_javascript::LANGUAGE.into()),
        "typescript" => Some(tree_sitter_typescript::LANGUAGE_TYPESCRIPT.into()),
        "tsx" => Some(tree_sitter_typescript::LANGUAGE_TSX.into()),
        _ => None,
    }
}

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hrayleung__Cocode/src-rust/code_parser.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/hrayleung__Cocode ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ikatyang__tree-sitter-markdown`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ikatyang__tree-sitter-markdown`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ikatyang__tree-sitter-markdown/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ikatyang__tree-sitter-markdown/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/ikatyang__tree-sitter-markdown ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jbpraxxys__opencode-indexer`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jbpraxxys__opencode-indexer`; scan counts include file_count=16, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jbpraxxys__opencode-indexer ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jiyee__tree-sitter-objc`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jiyee__tree-sitter-objc`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jiyee__tree-sitter-objc/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jiyee__tree-sitter-objc/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jiyee__tree-sitter-objc ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jobindex-open__tree-sitter-embedded-perl`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jobindex-open__tree-sitter-embedded-perl`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jobindex-open__tree-sitter-embedded-perl/bindings/c/tree_sitter/tree-sitter-embedded-perl.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=5, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_EMBEDDED_PERL_H_
#define TREE_SITTER_EMBEDDED_PERL_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_embedded_perl(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_EMBEDDED_PERL_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jobindex-open__tree-sitter-embedded-perl/bindings/c/tree_sitter/tree-sitter-embedded-perl.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/jobindex-open__tree-sitter-embedded-perl ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/joowani__tree-sitter-graphql`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/joowani__tree-sitter-graphql`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/joowani__tree-sitter-graphql/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/joowani__tree-sitter-graphql/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/joowani__tree-sitter-graphql ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kaermorchen__tree-sitter-explorer`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kaermorchen__tree-sitter-explorer`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kaermorchen__tree-sitter-explorer/src/parsers.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
import packageJson from "../package.json";

export interface IParser {
  id: string;
  name: string;
  wasmUrl: string;
  initCode: string;
  version: string;
  homepage: string;
}

export const parsers: IParser[] = [
  {
    id: "tree-sitter-bash",
    name: "Bash",
    wasmUrl: `/tree-sitter-explorer/parsers/tree-sitter-bash.wasm`,
    version: packageJson.dependencies["tree-sitter-bash"],
    initCode: [
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kaermorchen__tree-sitter-explorer/src/parsers.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kaermorchen__tree-sitter-explorer ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kopecs__tree-sitter-c0`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kopecs__tree-sitter-c0`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kopecs__tree-sitter-c0/src/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kopecs__tree-sitter-c0/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kopecs__tree-sitter-c0 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kylegoetz__tree-sitter-unison`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kylegoetz__tree-sitter-unison`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kylegoetz__tree-sitter-unison/script/tree-sitter-parse.js`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```javascript
#/usr/bin/env node --trace-warnings --unhandled-rejections=strict

const fs = require('fs')
const Parser = require('web-tree-sitter')

if (process.argv.length < 3) {
  console.log('Usage: script/tree-sitter-parse.js <unison-file..>')
  process.exit(1)
}

Parser.init().then(() => {
  Parser.Language.load('tree-sitter-unison.wasm').then((Unison) => {
    const parser = new Parser
    parser.setLanguage(Unison)
    process.argv.slice(2).forEach(filename => {
      const source = fs.readFileSync(filename, 'utf8')
      const tree = parser.parse(source)
    })
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kylegoetz__tree-sitter-unison/script/tree-sitter-parse.js` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kylegoetz__tree-sitter-unison ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lapce__tree-sitter-grammars`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lapce__tree-sitter-grammars`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lapce__tree-sitter-grammars/src/main.rs`; scan counts include rust_files=1, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```rust
use anyhow::{anyhow, bail, Result};
use clap::Parser;
use dunce::canonicalize;
use serde::{Deserialize, Serialize};
use std::{
    fs,
    io::{stderr, stdout},
    path::{Path, PathBuf},
    process::Command,
};
use tracing::{error, Level};
use tracing_subscriber::FmtSubscriber;

#[derive(Parser)]
struct Cli {
    dir: Option<PathBuf>,
    #[clap(short, long)]
    output: PathBuf,
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lapce__tree-sitter-grammars/src/main.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lapce__tree-sitter-grammars ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lezer-parser__import-tree-sitter`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lezer-parser__import-tree-sitter`; scan counts include file_count=7, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/lezer-parser__import-tree-sitter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/m-demare__hlargs.nvim`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/m-demare__hlargs.nvim`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/m-demare__hlargs.nvim/queries/bash/function_body.scm`; scan counts include rust_files=1, cargo_manifests=0, tree_sitter_query_files=103, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```scheme
(function_definition
  body: (compound_statement) @body)

```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/m-demare__hlargs.nvim/queries/bash/function_body.scm` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/m-demare__hlargs.nvim ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/maxxnino__tree-sitter-zig`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/maxxnino__tree-sitter-zig`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/maxxnino__tree-sitter-zig/bindings/python/tree_sitter_zig/__init__.py`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=4, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
"Zig grammar for tree-sitter"

from ._binding import language

__all__ = ["language"]
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/maxxnino__tree-sitter-zig/bindings/python/tree_sitter_zig/__init__.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/maxxnino__tree-sitter-zig ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mickeynp__combobulate`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mickeynp__combobulate`; scan counts include file_count=748, rust_files=0, cargo_manifests=0, candidate_paths=16.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mickeynp__combobulate ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/monaqa__tree-sitter-satysfi`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/monaqa__tree-sitter-satysfi`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/monaqa__tree-sitter-satysfi/src/tree_sitter/parser.h`; scan counts include rust_files=8, cargo_manifests=1, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/monaqa__tree-sitter-satysfi/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/monaqa__tree-sitter-satysfi ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mufeedvh__code2prompt`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mufeedvh__code2prompt`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mufeedvh__code2prompt/crates/code2prompt-core/src/tokenizer.rs`; scan counts include rust_files=71, cargo_manifests=4, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
//! This module encapsulates the logic for counting the tokens in the rendered text.
use log::debug;
use serde::{Deserialize, Serialize};
use std::fmt;
use std::sync::OnceLock;
use tiktoken_rs::{CoreBPE, cl100k_base, o200k_base, p50k_base, p50k_edit, r50k_base};

#[derive(Default, Debug, Clone, Copy, PartialEq, Deserialize, Serialize)]
#[serde(rename_all = "lowercase")]
pub enum TokenFormat {
    #[default]
    Raw,
    Format,
}

impl fmt::Display for TokenFormat {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mufeedvh__code2prompt/crates/code2prompt-core/src/tokenizer.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/mufeedvh__code2prompt ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/navgupta15__DTGS`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/navgupta15__DTGS`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/navgupta15__DTGS/test_ast.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
from pathlib import Path
from toolmaker.analyzer.java_analyzer import _parser
import json

src = Path("testrepo/src/MyCtrl.java").read_bytes()
tree = _parser.parse(src)

def print_tree(node, indent=0):
    print(" " * indent + node.type + " " + (node.text.decode('utf-8') if not node.children else ""))
    for child in node.children:
        print_tree(child, indent + 2)

print_tree(tree.root_node)
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/navgupta15__DTGS/test_ast.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/navgupta15__DTGS ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/neurocyte__flow`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/neurocyte__flow`; scan counts include file_count=204, rust_files=0, cargo_manifests=0, candidate_paths=15.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/neurocyte__flow ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nix-community__tree-sitter-nix`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nix-community__tree-sitter-nix`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nix-community__tree-sitter-nix/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=4, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nix-community__tree-sitter-nix/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nix-community__tree-sitter-nix ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nvim-neorg__tree-sitter-norg`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nvim-neorg__tree-sitter-norg`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nvim-neorg__tree-sitter-norg/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nvim-neorg__tree-sitter-norg/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nvim-neorg__tree-sitter-norg ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nxrvl__codedocgen`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nxrvl__codedocgen`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nxrvl__codedocgen/codedocgen/queries/go/functions.scm`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=13, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```scheme
; Go function declarations
(function_declaration
  name: (identifier) @function.name
  parameters: (parameter_list) @function.params
  result: (_)? @function.return_type
  body: (block) @function.body
) @function.def
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nxrvl__codedocgen/codedocgen/queries/go/functions.scm` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nxrvl__codedocgen ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/open-compress__claw-compactor`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/open-compress__claw-compactor`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/open-compress__claw-compactor/scripts/lib/fusion/neurosyntax.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
"""Neurosyntax — AST-aware code compression FusionStage.

Uses tree-sitter for multi-language AST parsing when available; falls back to
safe regex-based compression that strips comments and normalizes whitespace
without touching code semantics.

Critical safety rule: identifier names are NEVER shortened.  Class names,
function names, and variable names are semantic anchors that LLMs use to
understand code context.  Shortening them destroys comprehension and causes
downstream task failures (validated on SWE-bench).

Supports: Python, JavaScript, TypeScript, Go, Rust, Java, C, C++, Ruby,
PHP, Swift, Kotlin, Scala, Bash, R, Perl.

Part of claw-compactor v7. License: MIT.
"""
from __future__ import annotations

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/open-compress__claw-compactor/scripts/lib/fusion/neurosyntax.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/open-compress__claw-compactor ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/orzechowskid__tree-sitter-css-in-js`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/orzechowskid__tree-sitter-css-in-js`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/orzechowskid__tree-sitter-css-in-js/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/orzechowskid__tree-sitter-css-in-js/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/orzechowskid__tree-sitter-css-in-js ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pfeiferj__tree-sitter-hurl`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pfeiferj__tree-sitter-hurl`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pfeiferj__tree-sitter-hurl/bindings/c/tree-sitter-hurl.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=4, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_HURL_H_
#define TREE_SITTER_HURL_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_hurl(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_HURL_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pfeiferj__tree-sitter-hurl/bindings/c/tree-sitter-hurl.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pfeiferj__tree-sitter-hurl ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/prateekky__FastGraphRAG`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/prateekky__FastGraphRAG`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/prateekky__FastGraphRAG/build/CMakeFiles/tree-sitter-cpp.dir/compiler_depend.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
# CMAKE generated file: DO NOT EDIT!
# Timestamp file for compiler generated dependencies management for tree-sitter-cpp.
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/prateekky__FastGraphRAG/build/CMakeFiles/tree-sitter-cpp.dir/compiler_depend.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/prateekky__FastGraphRAG ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/r-lib__tree-sitter-r`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/r-lib__tree-sitter-r`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/r-lib__tree-sitter-r/bindings/c/tree-sitter-r.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=5, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_R_H_
#define TREE_SITTER_R_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_r(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_R_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/r-lib__tree-sitter-r/bindings/c/tree-sitter-r.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/r-lib__tree-sitter-r ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rest-nvim__tree-sitter-http`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rest-nvim__tree-sitter-http`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rest-nvim__tree-sitter-http/src/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rest-nvim__tree-sitter-http/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rest-nvim__tree-sitter-http ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/riyonp23__Probe`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/riyonp23__Probe`; scan counts include file_count=41, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/riyonp23__Probe ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rotmh__tree-sitter-dunstrc`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rotmh__tree-sitter-dunstrc`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rotmh__tree-sitter-dunstrc/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rotmh__tree-sitter-dunstrc/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rotmh__tree-sitter-dunstrc ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sakakibara__tree-sitter-organ`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sakakibara__tree-sitter-organ`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sakakibara__tree-sitter-organ/src/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sakakibara__tree-sitter-organ/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sakakibara__tree-sitter-organ ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sapai5__plagiarism-checker`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sapai5__plagiarism-checker`; scan counts include file_count=4, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sapai5__plagiarism-checker ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/semgrep__ocaml-tree-sitter-languages`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/semgrep__ocaml-tree-sitter-languages`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/semgrep__ocaml-tree-sitter-languages/lang/semgrep-grammars/src/semgrep-c-sharp/grammar.js`; scan counts include rust_files=1, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```javascript
/*
 * semgrep-csharp
 *
 * Extend the original tree-sitter C# grammar with semgrep-specific constructs
 * used to represent semgrep patterns.
 *
 * The language is renamed from c-sharp to csharp to match language name
 * conventions in ocaml-tree-sitter and semgrep.
 */

const standard_grammar = require('tree-sitter-c-sharp/grammar');

module.exports = grammar(standard_grammar, {
  name: 'c_sharp'
});
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/semgrep__ocaml-tree-sitter-languages/lang/semgrep-grammars/src/semgrep-c-sharp/grammar.js` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/semgrep__ocaml-tree-sitter-languages ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/shruti25838__CodeMentor-AI`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/shruti25838__CodeMentor-AI`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/shruti25838__CodeMentor-AI/codeatlas/services/parsing/tree_sitter_parser.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
import logging
from pathlib import Path

from tree_sitter import Node
from tree_sitter_languages import get_parser

from codeatlas.models.function_node import FunctionNode
from codeatlas.models.parsed_repository import ParsedRepository
from codeatlas.models.repository import Repository
from codeatlas.models.source_file import SourceFile
from codeatlas.services.parsing.interfaces import AstParser


class TreeSitterAstParser(AstParser):
    def parse_repository(self, repository: Repository) -> ParsedRepository:
        root = Path(repository.root_path)
        files: list[SourceFile] = []
        functions: list[FunctionNode] = []
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/shruti25838__CodeMentor-AI/codeatlas/services/parsing/tree_sitter_parser.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/shruti25838__CodeMentor-AI ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/skrider__softgrep`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/skrider__softgrep`; scan counts include file_count=36, rust_files=0, cargo_manifests=0, candidate_paths=3.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/skrider__softgrep ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcebot-dev__sourcebot`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcebot-dev__sourcebot`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcebot-dev__sourcebot/packages/queryLanguage/src/parser.terms.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
// This file was generated by lezer-generator. You probably shouldn't edit it.
export const
  negate = 23,
  openParen = 24,
  word = 25,
  closeParen = 26,
  or = 27,
  Program = 1,
  OrExpr = 2,
  AndExpr = 3,
  NegateExpr = 4,
  PrefixExpr = 5,
  ArchivedExpr = 6,
  RevisionExpr = 7,
  ContentExpr = 8,
  ContextExpr = 9,
  FileExpr = 10,
  ForkExpr = 11,
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcebot-dev__sourcebot/packages/queryLanguage/src/parser.terms.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcebot-dev__sourcebot ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcegraph__scip-typescript`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcegraph__scip-typescript`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcegraph__scip-typescript/snapshots/input/syntax/src/ClassWithPrivate.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
export class ClassWithPrivate {
  #privateField
  #privateFieldWithInitializer = 42

  #privateMethod() {
    this.#privateField = 'private field'
    return this.#privateField
  }

  static #privateStaticField
  static #privateStaticFieldWithInitializer = 42

  static #privateStaticMethod() {}
  public publicMethod(): any[] {
    return [
      this.#privateField,
      this.#privateFieldWithInitializer,
      this.#privateMethod(),
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcegraph__scip-typescript/snapshots/input/syntax/src/ClassWithPrivate.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sourcegraph__scip-typescript ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sscba__code-intelligence-mcp`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sscba__code-intelligence-mcp`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sscba__code-intelligence-mcp/src/db/queries/annotations.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
// SQL string constants for annotation operations.

export const INSERT_ANNOTATION = `
INSERT INTO annotations (project, node_id, author, content, kind, created_at, updated_at)
VALUES (@project, @node_id, @author, @content, @kind, @created_at, @updated_at)
RETURNING id
`;

export const GET_ANNOTATIONS_BY_NODE = `
SELECT id, project, node_id, author, content, kind, created_at, updated_at
FROM annotations WHERE node_id = ?
ORDER BY created_at
`;

export const GET_ANNOTATIONS_BY_PROJECT = `
SELECT id, project, node_id, author, content, kind, created_at, updated_at
FROM annotations WHERE project = ?
ORDER BY created_at
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sscba__code-intelligence-mcp/src/db/queries/annotations.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/sscba__code-intelligence-mcp ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/stsewd__tree-sitter-comment`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/stsewd__tree-sitter-comment`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/stsewd__tree-sitter-comment/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/stsewd__tree-sitter-comment/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/stsewd__tree-sitter-comment ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/syncable-dev__memtrace-public`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/syncable-dev__memtrace-public`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/syncable-dev__memtrace-public/benchmarks/suite/benches/bench_3_graph_queries/__init__.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
"""Bench #3 — Graph queries.

Primary axis: `callers_of.recall`.
Secondary: `callers_of.precision`, `impact_of.recall`, `find_dead_code.f1`,
latency.

Ground truth: pyright LSP call-hierarchy over the mempalace corpus
(see benchmarks/suite/datasets/bench_3_graph.json when present)."""
from .run import (
    BENCH_ID, PRIMARY_AXIS, DATASET_VERSION,
    load_dataset, run_with_adapter,
)

__all__ = [
    "BENCH_ID", "PRIMARY_AXIS", "DATASET_VERSION",
    "load_dataset", "run_with_adapter",
]
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/syncable-dev__memtrace-public/benchmarks/suite/benches/bench_3_graph_queries/__init__.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/syncable-dev__memtrace-public ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tera-language__tree-sitter-teralang`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tera-language__tree-sitter-teralang`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tera-language__tree-sitter-teralang/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tera-language__tree-sitter-teralang/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tera-language__tree-sitter-teralang ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/thmsmlr__tree-sitter-rec`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/thmsmlr__tree-sitter-rec`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/thmsmlr__tree-sitter-rec/src/tree_sitter/parser.h`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/thmsmlr__tree-sitter-rec/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/thmsmlr__tree-sitter-rec ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/traxys__tree-sitter-lalrpop`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/traxys__tree-sitter-lalrpop`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/traxys__tree-sitter-lalrpop/bindings/c/tree-sitter-lalrpop.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=3, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_LALRPOP_H_
#define TREE_SITTER_LALRPOP_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_lalrpop(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_LALRPOP_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/traxys__tree-sitter-lalrpop/bindings/c/tree-sitter-lalrpop.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/traxys__tree-sitter-lalrpop ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__fuzz-action`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__fuzz-action`; scan counts include file_count=9, rust_files=0, cargo_manifests=0, candidate_paths=2.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__fuzz-action ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__node-tree-sitter`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__node-tree-sitter`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__node-tree-sitter/tree-sitter.d.ts`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
/** @module */
declare module "tree-sitter" {
  class Parser {
    /**
     * Parse UTF8 text into a syntax tree.
     *
     * @param input - The text to parse, either as a string or a custom input function
     * that provides text chunks. If providing a function, it should return text chunks
     * based on byte index and position.
     *
     * @param oldTree - An optional previous syntax tree from the same document.
     * If provided and the document has changed, you must first edit this tree using
     * {@link Parser.Tree.edit} to match the new text.
     *
     * @param options - Optional parsing settings:
     * - bufferSize: Size of internal parsing buffer
     * - includedRanges: Array of ranges to parse within the input
     * - progressCallback: A callback that receives the current parse state
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__node-tree-sitter/tree-sitter.d.ts` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__node-tree-sitter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__py-tree-sitter`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__py-tree-sitter`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__py-tree-sitter/tree_sitter/binding/parser.c`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
PyObject *point_new_internal(ModuleState *state, TSPoint point);

#define SET_ATTRIBUTE_ERROR(name)                                                                  \
    (name != NULL && name != Py_None && parser_set_##name(self, name, NULL) < 0)

typedef struct {
    PyObject *read_cb;
    Py_buffer *previous_retval;
    ModuleState *state;
} ReadWrapperPayload;

typedef struct {
    PyObject *callback;
    PyTypeObject *log_type_type;
} LoggerPayload;

static void free_logger(const TSParser *parser) {
    TSLogger logger = ts_parser_logger(parser);
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__py-tree-sitter/tree_sitter/binding/parser.c` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__py-tree-sitter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-c-sharp`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-c-sharp`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-c-sharp/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-c-sharp/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-c-sharp ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-go`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-go`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-go/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-go/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-go ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-javascript`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-javascript`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-javascript/bindings/c/tree_sitter/tree-sitter-javascript.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=6, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_JAVASCRIPT_H_
#define TREE_SITTER_JAVASCRIPT_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_javascript(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_JAVASCRIPT_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-javascript/bindings/c/tree_sitter/tree-sitter-javascript.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-javascript ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-python`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-python`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-python/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=2, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-python/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-python ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-scala`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-scala`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-scala/bindings/c/tree-sitter-scala.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=4, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
#ifndef TREE_SITTER_SCALA_H_
#define TREE_SITTER_SCALA_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_scala(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_SCALA_H_
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-scala/bindings/c/tree-sitter-scala.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter-scala ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__zig-tree-sitter`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__zig-tree-sitter`; scan counts include file_count=29, rust_files=0, cargo_manifests=0, candidate_paths=2.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__zig-tree-sitter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/universal-ctags__ctags`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/universal-ctags__ctags`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/universal-ctags__ctags/Tmain/json-output-much-parser-fields.d/input.h`; scan counts include rust_files=8, cargo_manifests=0, tree_sitter_query_files=5, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
@protocol V
(V(V(V(V(V(V
/*  Takne from #2053 submitted by @chrismwendt */
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/universal-ctags__ctags/Tmain/json-output-much-parser-fields.d/input.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/universal-ctags__ctags ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/victorhqc__tree-sitter-prisma`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/victorhqc__tree-sitter-prisma`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/victorhqc__tree-sitter-prisma/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=1, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/victorhqc__tree-sitter-prisma/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/victorhqc__tree-sitter-prisma ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vitali87__code-graph-rag`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vitali87__code-graph-rag`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vitali87__code-graph-rag/benchmarks/bench_ast_cache.py`; scan counts include rust_files=1, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
        key = Path(f"/fake/path/module_{i}.py")
        cache[key] = (MockNode(item_size), "python")
        while len(cache) > max_size:
            cache.popitem(last=False)
    return time.perf_counter() - start


def bench_getsizeof_overhead(cache: OrderedDict) -> float:
    start = time.perf_counter()
    _ = sum(sys.getsizeof(v) for v in cache.values())
    return time.perf_counter() - start


def run_benchmark(name: str, func, *args) -> dict[str, float]:
    for _ in range(WARMUP_RUNS):
        func(*args)

    times = []
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vitali87__code-graph-rag/benchmarks/bench_ast_cache.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/vitali87__code-graph-rag ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/wenkokke__tree-sitter-talon`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/wenkokke__tree-sitter-talon`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/wenkokke__tree-sitter-talon/src/tree_sitter/parser.h`; scan counts include rust_files=2, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
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
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/wenkokke__tree-sitter-talon/src/tree_sitter/parser.h` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/wenkokke__tree-sitter-talon ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/wrale__mcp-server-tree-sitter`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/wrale__mcp-server-tree-sitter`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/wrale__mcp-server-tree-sitter/src/mcp_server_tree_sitter/cache/parser_cache.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
"""Caching system for tree-sitter parse trees."""

import logging
import threading
import time
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

# Import global_context at runtime to avoid circular imports
from ..utils.tree_sitter_types import (
    Parser,
    Tree,
    ensure_language,
    ensure_parser,
    ensure_tree,
)

```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/wrale__mcp-server-tree-sitter/src/mcp_server_tree_sitter/cache/parser_cache.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/wrale__mcp-server-tree-sitter ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zed-industries__zed`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zed-industries__zed`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zed-industries__zed/crates/collab/src/db/queries/buffers.rs`; scan counts include rust_files=1877, cargo_manifests=253, tree_sitter_query_files=149, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
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
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zed-industries__zed/crates/collab/src/db/queries/buffers.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zed-industries__zed ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zzxn__tree-sitter-ast-dfg`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Tree-Sitter Grammar Or Query Module From `personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zzxn__tree-sitter-ast-dfg`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zzxn__tree-sitter-ast-dfg/parser/DFG.py`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The grammar/query files form a parser Module whose Interface is the language grammar plus query captures. The implementation is generated parser code and query text. The useful seam is the registry or caller that consumes grammar artifacts without learning generator internals, giving leverage to highlighters, indexers, and code-assist tools.
Reusable code shape:
```text
from tree_sitter import Language, Parser
from .utils import (remove_comments_and_docstrings,
                   tree_to_token_index,
                   index_to_code_token,
                   tree_to_variable_index)


def DFG_python(root_node,index_to_code,states):
    assignment=['assignment','augmented_assignment','for_in_clause']
    if_statement=['if_statement']
    for_statement=['for_statement']
    while_statement=['while_statement']
    do_first_statement=['for_in_clause']
    def_statement=['default_parameter']
    states=states.copy()
    if (len(root_node.children)==0 or root_node.type=='string') and root_node.type!='comment':
        idx,code=index_to_code[(root_node.start_point,root_node.end_point)]
        if root_node.type==code:
```
Transfer rule: Use this pattern when Rust tooling needs language-aware parsing, highlighting, symbols, or indentation. Keep generated grammar artifacts behind a stable language adapter seam and test queries with real snippets.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zzxn__tree-sitter-ast-dfg/parser/DFG.py` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/zzxn__tree-sitter-ast-dfg ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/proof-of-effort-2024`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Rust Module Architecture Slice From `personal-repos-lane/proof-of-effort-2024`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/proof-of-effort-2024/src/f04_tokio_01.rs`; scan counts include rust_files=6, cargo_manifests=1, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: This Rust Module is valuable as an architecture slice when it hides ownership, error, async, storage, CLI, or workspace complexity behind a smaller Interface. The transfer question is whether deleting the module would scatter that complexity across callers.
Reusable code shape:
```rust
pub async fn async_main() {
    println!(
        "===f04_tokio_01===
        printing from main function which is async"
    );
}
```
Transfer rule: Use this pattern when the cited module earns depth: a small caller Interface hides meaningful implementation complexity. Avoid copying local project names or generated code without revalidating invariants in the target codebase.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/proof-of-effort-2024/src/f04_tokio_01.rs` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/proof-of-effort-2024 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/eugenp__tutorials`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/eugenp__tutorials`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/eugenp__tutorials/akka-modules/akka-streams/src/main/java/com/baeldung/akkastreams/AverageRepository.java`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
package com.baeldung.akkastreams;


import java.util.concurrent.CompletableFuture;
import java.util.concurrent.CompletionStage;

public class AverageRepository {
    CompletionStage<Double> save(Double average) {
        return CompletableFuture.supplyAsync(() -> {
            System.out.println("saving average: " + average);
            return average;
        });
    }
}
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/eugenp__tutorials/akka-modules/akka-streams/src/main/java/com/baeldung/akkastreams/AverageRepository.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/eugenp__tutorials ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/spring-guides__gs-actuator-service`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/spring-guides__gs-actuator-service`; scan counts include file_count=40, rust_files=0, cargo_manifests=0, candidate_paths=3.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/spring-guides__gs-actuator-service ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/spring-projects__spring-boot`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/spring-projects__spring-boot`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/spring-projects__spring-boot/buildSrc/src/main/java/org/springframework/boot/build/mavenplugin/PluginXmlParser.java`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
import java.util.List;
import java.util.Map;

import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;

import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

/**
 * A parser for a Maven plugin's {@code plugin.xml} file.
 *
 * @author Andy Wilkinson
 * @author Mike Smithson
 */
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/spring-projects__spring-boot/buildSrc/src/main/java/org/springframework/boot/build/mavenplugin/PluginXmlParser.java` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/spring-projects__spring-boot ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/rust-100-exercises-notes`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/rust-100-exercises-notes`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/rust-100-exercises-notes/book/src/01_intro/01_syntax.md`; scan counts include rust_files=135, cargo_manifests=102, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
# Syntax

<div class="warning">

Don't jump ahead!\
Complete the exercise for the previous section before you start this one.\
It's located in `exercises/01_intro/00_welcome`, in the [course GitHub's repository](https://github.com/mainmatter/100-exercises-to-learn-rust).\
Use [`wr`](00_welcome.md#wr-the-workshop-runner) to start the course and verify your solutions.

</div>

The previous task doesn't even qualify as an exercise, but it already exposed you to quite a bit of Rust **syntax**.
We won't cover every single detail of Rust's syntax used in the previous exercise.
Instead, we'll cover _just enough_ to keep going without getting stuck in the details.\
One step at a time!

## Comments

```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/rust-100-exercises-notes/book/src/01_intro/01_syntax.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/rust-100-exercises-notes ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/that-in-rust-org-github`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `personal-repos-lane/that-in-rust-org-github`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/that-in-rust-org-github/zz-archive/ideaHub/parseltongue_diagram.md`; scan counts include rust_files=0, cargo_manifests=0, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```text
# Parseltongue Snapshot Analysis

This document contains a visual representation of the Rust code structure captured in `parseltongue_snapshot.json`.

## Code Structure Diagram

```mermaid
graph TD
    %% Define styles for different node types
    classDef structClass fill:#e1f5fe,stroke:#01579b,stroke-width:2px,color:#000
    classDef traitClass fill:#f3e5f5,stroke:#4a148c,stroke-width:2px,color:#000
    classDef implClass fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px,color:#000
    classDef otherClass fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#000

    %% Create subgraphs by file path
    subgraph "axum/src/boxed.rs"
        %% Nodes from boxed.rs
        A[BoxedIntoRoute<br/>Struct] --> B[ErasedIntoRoute<br/>Trait]
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/personal-repos-lane/that-in-rust-org-github/zz-archive/ideaHub/parseltongue_diagram.md` and run `git -C /Users/amuldotexe/Desktop/personal-repos-lane/that-in-rust-org-github ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/useful-rc-files`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/useful-rc-files`; scan counts include file_count=2, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/useful-rc-files ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/zz_archived_journal2023`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/zz_archived_journal2023`; scan counts include file_count=13, rust_files=0, cargo_manifests=0, candidate_paths=0.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/personal-repos-lane/zz_archived_journal2023 ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/RAPx`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `reference-repos-yard/RAPx`
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/RAPx/rapx/src/analysis/safetyflow_analysis/hir_visitor.rs`; scan counts include rust_files=441, cargo_manifests=267, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
N/A: could not read `/Users/amuldotexe/Desktop/reference-repos-yard/RAPx/rapx/src/analysis/safetyflow_analysis/hir_visitor.rs`: [Errno 2] No such file or directory: '/Users/amuldotexe/Desktop/reference-repos-yard/RAPx/rapx/src/analysis/safetyflow_analysis/hir_visitor.rs'
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/reference-repos-yard/RAPx/rapx/src/analysis/safetyflow_analysis/hir_visitor.rs` and run `git -C /Users/amuldotexe/Desktop/reference-repos-yard/RAPx ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

## Skipped Repo: `/Users/amuldotexe/Desktop/reference-repos-yard/cachebro`

### Concept: Repo skipped because bounded scan found no Rust, Cargo, tree-sitter, or parser-adjacent source evidence
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/cachebro`; scan counts include file_count=22, rust_files=0, cargo_manifests=0, candidate_paths=1.
Architecture lens: No Rust Module, parser Module, grammar Interface, or reusable seam was visible in the bounded `git ls-files` scan. Recording the skip preserves full Desktop coverage without inventing a pattern.
Reusable code shape:
```text
N/A: no Rust or parser-adjacent source evidence was present in the bounded scan.
```
Transfer rule: Do not use this repo as Rust evidence unless future changes add `Cargo.toml`, `*.rs`, tree-sitter grammar/query files, parser source, or code-intelligence infrastructure.
Verification hook: `git -C /Users/amuldotexe/Desktop/reference-repos-yard/cachebro ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"`

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_jvm`

Coordinator completion note: added after the parallel worker batch using `meta-rust-ref-202606-evidence-index.json` plus a bounded source read. Treat the cited source path as the authority and re-open it before transferring the pattern.

### Concept: Parser And Syntax Module From `reference-repos-yard/rustc_codegen_jvm`
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_jvm/src/oomir.rs`; scan counts include rust_files=50, cargo_manifests=24, tree_sitter_query_files=0, pest_files=0, lalrpop_files=0.
Architecture lens: The parser Module should keep tokenization, syntax shaping, error reporting, and downstream AST/HIR consumers behind a small Interface. The deepest shape concentrates grammar drift and parse errors in one implementation, improving locality for tests and callers.
Reusable code shape:
```rust
// src/oomir.rs
//! This is the output of the stage 1 lowering pass of the compiler.
//! It is responsible for converting the MIR into a lower-level IR, called OOMIR (defined in this file).
use crate::lower2::BIG_DECIMAL_CLASS;

use super::lower2::BIG_INTEGER_CLASS;
use core::panic;
use ristretto_classfile::attributes::Instruction as JVMInstruction;
use std::{collections::HashMap, fmt};

pub mod interpret;

// OOMIR definitions
#[derive(Debug, Clone)]
pub struct Module {
    pub name: String,
    pub functions: HashMap<String, Function>,
    pub data_types: HashMap<String, DataType>,
```
Transfer rule: Use this pattern when a Rust tool must parse a structured language or command stream. Keep parse input, parse output, and error contracts explicit; do not let downstream modules depend on raw parser internals.
Verification hook: Re-open `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_jvm/src/oomir.rs` and run `git -C /Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_jvm ls-files | rg "Cargo.toml|\.rs$|tree-sitter|tree_sitter|grammar|parser|parse|lexer|syntax|ast|queries/|\.scm$|\.pest$|\.lalrpop$"` before reusing the pattern.

