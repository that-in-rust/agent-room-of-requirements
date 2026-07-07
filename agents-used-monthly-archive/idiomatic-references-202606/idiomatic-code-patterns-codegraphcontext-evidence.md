# Idiomatic Code Patterns CodeGraphContext Evidence

Purpose: record CodeGraphContext graph evidence used during the `idiomatic-code-patterns-*` extraction workstream. Graph results are navigational evidence only; pattern claims still require direct source reads.

## Completed Smoke Runs

| repo_path | output_directory | graph_summary |
| --- | --- | --- |
| `/Users/amuldotexe/Desktop/personal-repos-lane/codecrafters-http-server-rust` | `/tmp/codex-code-intel/codegraphcontext/codecrafters-http-server-rust-20260706-225736` | 7 files, 1 function, 1 module |
| `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-fmt-fixed-capacity` | `/tmp/codex-code-intel/codegraphcontext/nostd-fmt-fixed-capacity-20260706-225736` | 12 files, 47 functions, 1 struct, 1 enum, 9 modules |
| `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker` | `/tmp/codex-code-intel/codegraphcontext/knight-bus-graph-walker-20260706-225736` | 259 files, 560 functions, 3 classes, 6 traits, 66 structs, 25 enums, 80 modules |
| `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/bytecodealliance__tree-sitter-wit` | `/tmp/codex-code-intel/codegraphcontext/bytecodealliance__tree-sitter-wit-20260706-230156` | 50 files, 36 functions, 15 classes, 14 structs, 1 enum, 40 modules |
| `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/casey__tree-sitter-just` | `/tmp/codex-code-intel/codegraphcontext/casey__tree-sitter-just-20260706-230234` | 44 files, 47 functions, 16 classes, 14 structs, 1 enum, 46 modules |

## Timed-Out Smoke Runs

These CGC attempts did not produce usable graph evidence. The corresponding pattern entries rely on direct source reads only.

| repo_path | output_directory | status |
| --- | --- | --- |
| `/Users/amuldotexe/Desktop/reference-repos-yard/hax` | `/tmp/codex-code-intel/codegraphcontext/hax-20260706-230205` | timed out; no graph claims used |
| `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/apple__tree-sitter-pkl` | `/tmp/codex-code-intel/codegraphcontext/apple__tree-sitter-pkl-20260706-230857` | timed out; no graph claims used |
| `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter` | `/tmp/codex-code-intel/codegraphcontext/tree-sitter__tree-sitter-20260706-230210` | timed out; no graph claims used |
| `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter-grammars__tree-sitter-hcl` | `/tmp/codex-code-intel/codegraphcontext/tree-sitter-grammars__tree-sitter-hcl-20260706-230223` | timed out; no graph claims used |

## Query Evidence

### codecrafters-http-server-rust

CodeGraphContext function query returned:

```text
main
```

Interpretation: this repo is small enough that direct `src/main.rs` reading is the right evidence path; graph indexing confirms the project shape is compact.

### nostd-fmt-fixed-capacity

CodeGraphContext function query returned representative functions:

```text
bench_simple_string_write
bench_different_capacity_sizes
bench_utf8_multi_byte_writes
bench_integer_formatting_operations
bench_multiple_write_operations
bench_clear_and_reuse_pattern
bench_complex_formatting_patterns
bench_buffer_access_patterns
write_bytes_to_buffer_safe
capacity_remaining_bytes_available
```

Interpretation: the graph confirms that the repo is organized around a small fixed-capacity writer plus benchmark functions that exercise capacity, UTF-8, integer formatting, reuse, and buffer access patterns.

### knight-bus-graph-walker

CodeGraphContext function query returned representative functions:

```text
run_knight_bus_rust_measurement_now
write_report_bundle_now
run_benchmark_now
failed_measurement_now
parse_kv_line_output_now
build_arg_parser_now
resolve_neo4j_server_process_now
measure_engine_latency_now
validate_engine_parity_now
run_query_now
```

Interpretation: the graph confirms repeated measurement, report-bundle, parser, process-resolution, latency, and parity-verification function families. These are candidates for idiomatic benchmarking and verification patterns, subject to direct source reads before inclusion in the encyclopedia files.

## Use In Final Corpus

- Use CodeGraphContext to find candidate function families and structural clusters.
- Confirm every pattern with source reads before writing an encyclopedia entry.
- Prefer graph evidence for large repos where plain `rg` finds too many matches.
- Record timeouts, stale paths, or empty query results explicitly rather than silently dropping repos.
