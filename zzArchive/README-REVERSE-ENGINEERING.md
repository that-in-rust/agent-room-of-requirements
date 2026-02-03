# Claude Code v2.1.29 Reverse Engineering Project

**Project Goal:** Comprehensive architectural understanding of @anthropic-ai/claude-code v2.1.29
**Timeline:** 30 days (8 phases)
**Status:** Phase 0 Complete, Phase 1 Ready
**Started:** 2026-02-01

---

## Quick Links

- **Main Progress Tracker:** [REVERSE-ENGINEERING-PROGRESS.md](./REVERSE-ENGINEERING-PROGRESS.md)
- **Phase 1 Guide:** [analysis/QUICK-START-PHASE-1.md](./analysis/QUICK-START-PHASE-1.md)
- **Tool Schema Analysis:** [analysis/findings/TOOL-SCHEMA-ANALYSIS.md](./analysis/findings/TOOL-SCHEMA-ANALYSIS.md)

---

## Project Structure

```
/referenceRepo/
├── README-REVERSE-ENGINEERING.md        # This file (project overview)
├── REVERSE-ENGINEERING-PROGRESS.md      # Main progress tracker (update here)
│
├── package/                              # Extracted claude-code package
│   ├── cli.js (11.1MB)                  # PRIMARY ANALYSIS TARGET
│   ├── sdk-tools.d.ts                   # Tool schemas (20 tools)
│   ├── tree-sitter.wasm                 # AST parser
│   ├── tree-sitter-bash.wasm            # Bash parser
│   ├── resvg.wasm                       # SVG renderer
│   └── vendor/ripgrep/                  # Platform binaries (5 platforms)
│
└── analysis/                             # All analysis outputs
    ├── QUICK-START-PHASE-1.md           # Phase 1 execution guide
    ├── findings/                        # Per-investigation findings
    │   └── TOOL-SCHEMA-ANALYSIS.md      # Deep dive on 20 tools
    ├── reports/                         # Phase completion reports
    └── tool-flow-diagrams/              # Mermaid diagrams (future)
```

---

## 8-Phase Roadmap (30 Days)

### Phase 0: Initial Setup ✅ COMPLETE (Day 0)
- Downloaded and extracted package (71MB)
- Mapped 20 tool schemas from sdk-tools.d.ts
- Created analysis infrastructure
- Set up parseltongue (localhost:7778)

### Phase 1: Bundle Reconnaissance 🔵 READY (Days 1-2)
**Goal:** Identify bundler, extract module map, beautify code
**Guide:** [analysis/QUICK-START-PHASE-1.md](./analysis/QUICK-START-PHASE-1.md)
**Deliverables:**
- cli-beautified.js
- module-map.json
- bundler detection report

### Phase 2: Tool Layer Mapping 🔵 PENDING (Days 3-5)
**Goal:** Map 20 tools to implementation code
**Deliverables:**
- Tool implementation map
- Flow diagrams (Mermaid)
- Ripgrep/WASM integration docs

### Phase 3: Agent System (Days 6-8)
**Goal:** Understand subagent spawning and lifecycle

### Phase 4: API Communication (Days 9-11)
**Goal:** Document Anthropic API integration

### Phase 5: State & Permissions (Days 12-14)
**Goal:** Map state management and permission system

### Phase 6: Dynamic Analysis (Days 15-17)
**Goal:** Runtime tracing and profiling

### Phase 7: Advanced AST Analysis (Days 18-20)
**Goal:** Call graph extraction, data flow analysis

### Phase 8: Documentation Synthesis (Days 21-23)
**Goal:** Master architecture document and diagrams

---

## Key Discoveries (So Far)

### Architecture Hypothesis
```
User Input → CLI Parser → Tool Dispatcher → API Client → Claude API
                    ↓
               Agent Manager → Background Executor
                    ↓
             State Manager → Session Storage
                    ↓
          Permission System → Sandbox Enforcer
```

### 20 Tools Identified
1. **Agent** - Subagent spawning (multi-model: sonnet/opus/haiku)
2. **Bash** - Command execution (sandboxed)
3. **TaskOutput** - Background task monitoring
4. **ExitPlanMode** - Plan-based permissions
5. **FileEdit** - String replacement editing
6. **FileRead** - File reading (paginated)
7. **FileWrite** - File creation
8. **Glob** - Pattern-based file finding
9. **Grep** - Ripgrep content search
10. **TaskStop** - Background task termination
11. **ListMcpResources** - MCP resource listing
12. **Mcp** - MCP tool invocation
13. **NotebookEdit** - Jupyter cell manipulation
14. **ReadMcpResource** - MCP resource reading
15. **TodoWrite** - Task tracking
16. **WebFetch** - URL fetching + AI processing
17. **WebSearch** - Web search (domain filtering)
18. **AskUserQuestion** - Interactive prompts
19. **Config** - Settings management
20. **BashOutput** - (inferred) Background shell output

**Full Analysis:** [analysis/findings/TOOL-SCHEMA-ANALYSIS.md](./analysis/findings/TOOL-SCHEMA-ANALYSIS.md)

### Critical Features Discovered
- **MCP Integration:** Extensibility via Model Context Protocol
- **Multi-Model Agents:** Task-specific model selection (haiku for speed, opus for complexity)
- **Plan-Based Permissions:** Semantic action approval ("run tests" vs. exact commands)
- **Sandbox Override:** `dangerouslyDisableSandbox` flag (security concern)
- **Background Execution:** Non-blocking task system

---

## How to Use This Project

### For Active Analysis Sessions
1. **Check current status:** Read [REVERSE-ENGINEERING-PROGRESS.md](./REVERSE-ENGINEERING-PROGRESS.md)
2. **Start next phase:** Follow guide in `/analysis/QUICK-START-PHASE-*.md`
3. **Document findings:** Update progress tracker after each session
4. **Save artifacts:** Place all outputs in `/analysis/` with phase prefixes

### For Resuming After Interruption
1. **Read "Current Focus" section** in progress tracker
2. **Check "Next Steps"** for immediate actions
3. **Review "Context Notes"** for recent decisions
4. **Continue from last incomplete deliverable**

### For Collaboration
1. **Clone progress tracker** for personal notes
2. **Submit findings** as separate markdown files in `/analysis/findings/`
3. **Reference phase number** in all artifact filenames (e.g., `03-agent-system.md`)

---

## Toolchain Requirements

### Installed (Phase 0)
- npm (package management)
- tar (extraction)
- parseltongue (HTTP server at localhost:7778)

### To Install (Phase 1)
```bash
npm install -g prettier       # Code beautification
npm install -g restringer     # Deobfuscation
npm install -g wakaru         # Bundle unpacking
npm install -g madge          # Dependency graphs
npm install -g @ast-grep/cli  # AST-based search
```

### Optional (Later Phases)
- Node.js debugger (Phase 6: dynamic analysis)
- Wireshark/mitmproxy (Phase 6: network capture)
- Chrome DevTools (Phase 6: profiling)

---

## File Naming Conventions

### Analysis Outputs
```
/analysis/
├── {phase}-{topic}.md              # Phase reports (e.g., 01-bundle-structure.md)
├── {phase}-{artifact}.json         # Data artifacts (e.g., module-map.json)
├── findings/{TOPIC}.md             # Deep-dive analyses (all caps)
├── reports/phase-{N}-complete.md   # Phase summaries
└── tool-flow-diagrams/{tool}.mmd   # Mermaid diagrams
```

### Examples
- `01-bundle-structure.md` - Phase 1 main report
- `module-map.json` - Module metadata
- `findings/AGENT-SYSTEM-INTERNALS.md` - Deep dive
- `reports/phase-02-complete.md` - Phase 2 summary
- `tool-flow-diagrams/bash.mmd` - Bash tool flow

---

## Progress Tracking Protocol

### After Each Work Session
1. Update [REVERSE-ENGINEERING-PROGRESS.md](./REVERSE-ENGINEERING-PROGRESS.md):
   - Phase completion percentages
   - Deliverables checklist (check off completed items)
   - Critical discoveries log (add new findings)
   - Session notes (date, duration, achievements)

2. Create artifacts in `/analysis/` with proper naming

3. Update "Next Steps" section for future sessions

### Phase Completion
1. Create phase summary report in `/analysis/reports/`
2. Update phase progress bar to 100%
3. Move "Blockers" from completed phase to next phase
4. Update "Overall Progress" percentage

---

## Investigation Priorities

### HIGH Priority (Core Architecture)
1. Agent system (subagent spawning, orchestration)
2. Permission system (ExitPlanMode, sandbox)
3. Grep/ripgrep integration (platform binaries)
4. API client (Claude API communication)
5. Background execution (task lifecycle)

### MEDIUM Priority (Extensibility)
6. MCP integration (server registration)
7. WebFetch (AI processing pipeline)
8. State management (persistence)

### LOW Priority (Utilities)
9. File operations (straightforward)
10. TodoWrite, Config, AskUserQuestion (UI features)

---

## Open Research Questions

### Phase 1 Questions
1. What bundler created cli.js? (webpack/rollup/esbuild/custom)
2. How many modules are in the bundle?
3. What obfuscation techniques are used?
4. Can we extract a clean module map?

### Phase 2+ Questions
5. How does ExitPlanMode match semantic prompts to commands?
6. How are platform-specific ripgrep binaries selected?
7. What is the agent state persistence mechanism?
8. How does the `resume` parameter work?
9. What are MCP server registration mechanisms?
10. How does the internal `_simulatedSedEdit` work?

---

## Success Metrics

### Phase-Level Success
- All deliverables created ✓
- All blockers resolved ✓
- Success criteria met ✓
- Next phase ready to begin ✓

### Project-Level Success
- Complete architecture document
- All 20 tools mapped to implementation
- System diagrams (data flow, state machine, call graph)
- Reproducible implementation guide
- Security audit completed

---

## Contact & Collaboration

**Maintainer:** TDD Context Retention Specialist (Claude)
**Project Type:** Reverse Engineering (Static + Dynamic Analysis)
**Methodology:** 8-Phase Incremental Discovery

**For Questions:**
- Check [REVERSE-ENGINEERING-PROGRESS.md](./REVERSE-ENGINEERING-PROGRESS.md) "Open Questions" section
- Review phase-specific guides in `/analysis/`
- Consult [TOOL-SCHEMA-ANALYSIS.md](./analysis/findings/TOOL-SCHEMA-ANALYSIS.md) for tool details

---

## Version History

### v0.1.0 - 2026-02-01 (Phase 0 Complete)
- Initial project setup
- Package downloaded and extracted (71MB)
- 20 tools identified from sdk-tools.d.ts
- Analysis infrastructure created
- Parseltongue operational (localhost:7778)
- 30-day roadmap established

**Next Milestone:** v0.2.0 - Phase 1 completion (bundle reconnaissance)

---

**Last Updated:** 2026-02-01
**Current Phase:** 1 (Bundle Reconnaissance)
**Overall Progress:** 5% (1/8 phases complete)
