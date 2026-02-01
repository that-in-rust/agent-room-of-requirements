# START HERE - Claude Code Reverse Engineering

**Quick Reference for Resuming This Project**

---

## Current Status

- **Phase:** 0 Complete ✅, Phase 1 Ready 🔵
- **Progress:** 5% (1/8 phases)
- **Next Action:** Begin Phase 1 (Bundle Reconnaissance)
- **Estimated Time:** 3-4 hours
- **Blockers:** None

---

## What Is This Project?

Reverse engineering @anthropic-ai/claude-code v2.1.29 to understand its complete architecture:
- 20 tools (Agent, Bash, Grep, File operations, MCP integration, etc.)
- 11.1MB minified JavaScript bundle (cli.js)
- 30-day analysis plan (8 phases)
- Goal: Complete architectural documentation and implementation guide

---

## Key Files (Read These First)

### 1. Project Status (You Are Here)
**File:** `PROJECT-STATUS.txt`
**Purpose:** Quick visual overview of all phases and metrics

### 2. Main Progress Tracker (Update After Each Session)
**File:** `REVERSE-ENGINEERING-PROGRESS.md`
**Purpose:** Comprehensive tracking document with all phases, discoveries, and notes
**Key Sections:**
- Phase Progress Overview (lines 30-50)
- Detailed Phase Tracking (lines 52-600)
- Critical Discoveries Log (lines 602-700)
- Session Notes (lines 800+)

### 3. Project Overview
**File:** `README-REVERSE-ENGINEERING.md`
**Purpose:** Quick reference guide with structure, conventions, and tooling

### 4. Today's Session Summary
**File:** `SESSION-SUMMARY-20260201.md`
**Purpose:** What was accomplished today and what's next

---

## Next Steps (Phase 1 Start)

### Option A: Quick Start (Just Do It)

```bash
# 1. Navigate to project
cd /Users/amuldotexe/Desktop/A01_20260131/agent-room-of-requirements/referenceRepo

# 2. Install tools (5 minutes)
npm install -g prettier restringer wakaru madge @ast-grep/cli

# 3. Beautify main bundle (10-15 minutes - will be SLOW)
prettier package/cli.js > analysis/cli-beautified.js

# 4. Extract first 500 lines for inspection
head -n 500 analysis/cli-beautified.js > analysis/cli-first-500-lines.js

# 5. Check for bundler signature
grep -n "webpackBootstrap" analysis/cli-beautified.js | head -n 5
grep -n "rollup" analysis/cli-beautified.js | head -n 5
grep -n "esbuild" analysis/cli-beautified.js | head -n 5
```

### Option B: Guided Walkthrough (Recommended)

**File:** `analysis/QUICK-START-PHASE-1.md` (400+ lines)

This file contains:
- Step-by-step commands with explanations
- Expected outputs for verification
- Troubleshooting tips
- Time estimates per step
- Success criteria

---

## What's Been Done (Phase 0 Recap)

✅ **Package Analysis:**
- Downloaded claude-code v2.1.29 (71MB unpacked)
- Located in: `./package/`
- Main target: `package/cli.js` (11.1MB minified)
- Tool schemas: `package/sdk-tools.d.ts` (1566 lines)

✅ **Tool Inventory:**
- Identified all 20 tools from TypeScript definitions
- Deep analysis completed (see `analysis/findings/TOOL-SCHEMA-ANALYSIS.md`)
- Key tools: Agent, Bash, Grep, ExitPlanMode, MCP integration

✅ **Progress Tracking System:**
- Main tracker: `REVERSE-ENGINEERING-PROGRESS.md`
- Phase guides created
- Directory structure established

---

## File Locations (Important Paths)

```
/referenceRepo/
├── START-HERE.md                    ← You are here
├── PROJECT-STATUS.txt               ← Visual overview
├── REVERSE-ENGINEERING-PROGRESS.md  ← Main tracker (UPDATE THIS)
├── README-REVERSE-ENGINEERING.md    ← Quick reference
├── SESSION-SUMMARY-20260201.md      ← Today's notes
│
├── package/
│   ├── cli.js                       ← 11.1MB PRIMARY TARGET
│   └── sdk-tools.d.ts               ← 20 tool schemas (analyzed)
│
└── analysis/
    ├── QUICK-START-PHASE-1.md       ← Phase 1 guide
    ├── findings/
    │   └── TOOL-SCHEMA-ANALYSIS.md  ← 20 tools deep dive
    ├── reports/                     ← Phase summaries (empty)
    └── tool-flow-diagrams/          ← Mermaid diagrams (empty)
```

---

## Critical Discoveries So Far

**20 Tools Mapped:**
1. Agent - Multi-model subagent spawning (sonnet/opus/haiku)
2. Bash - Sandboxed command execution
3. Grep - Ripgrep-powered search (5 platform binaries)
4. ExitPlanMode - Plan-based permission system
5. MCP Tools - Third-party integration (ListMcpResources, Mcp, ReadMcpResource)
6. File Operations - Edit, Read, Write, Glob
7. Background Execution - TaskOutput, TaskStop
8. And 13 more... (see TOOL-SCHEMA-ANALYSIS.md)

**Architecture Hypothesis:**
```
User Input → CLI → Tools → API Client → Claude API
               ↓
          Agent Manager → Background Tasks
               ↓
          State + Permissions
```

**Extensibility Mechanisms:**
- MCP Protocol (third-party tools)
- Multi-model agents (task-specific model selection)
- Plan-based permissions (semantic action approval)

---

## Open Questions (To Be Answered)

**Phase 1 (Bundle Analysis):**
1. What bundler created cli.js?
2. How many modules in the bundle?
3. What obfuscation is used?
4. Where is the CLI entry point?

**Phase 2+ (Implementation):**
5. How does ExitPlanMode match semantic prompts to commands?
6. How are ripgrep binaries selected at runtime?
7. How does agent state persistence work?
8. What is the MCP server registration mechanism?

---

## How to Update Progress

**After Each Work Session:**

1. **Open:** `REVERSE-ENGINEERING-PROGRESS.md`

2. **Update Phase Section:**
   - Change completion percentage
   - Check off completed deliverables
   - Add any blockers

3. **Add Discoveries:**
   - Scroll to "Critical Discoveries Log"
   - Add new findings with evidence and implications

4. **Update Session Notes:**
   - Scroll to "Session Notes & Context"
   - Add new session entry with date, duration, achievements

5. **Set Next Steps:**
   - Update "Current Focus" section
   - List 3-5 immediate next actions

---

## Tools Required

**Already Installed:**
- npm ✅
- tar ✅
- parseltongue ✅ (localhost:7778)

**Need to Install (Phase 1):**
```bash
npm install -g prettier       # Code formatting
npm install -g restringer     # Deobfuscation
npm install -g wakaru         # Bundle unpacking
npm install -g madge          # Dependency graphs
npm install -g @ast-grep/cli  # AST search
```

---

## Timeline

**Phase 0:** Day 0 (2026-02-01) ✅ COMPLETE
**Phase 1:** Days 1-2 (2026-02-02 to 2026-02-03) 🔵 READY
**Phase 2:** Days 3-5 (2026-02-04 to 2026-02-06)
**Phase 3:** Days 6-8 (2026-02-07 to 2026-02-09)
**Phase 4:** Days 9-11 (2026-02-10 to 2026-02-12)
**Phase 5:** Days 12-14 (2026-02-13 to 2026-02-15)
**Phase 6:** Days 15-17 (2026-02-16 to 2026-02-18)
**Phase 7:** Days 18-20 (2026-02-19 to 2026-02-21)
**Phase 8:** Days 21-23 (2026-02-22 to 2026-02-24)

**Total:** 30 days (assuming 2-3 hours/day)

---

## Quick Commands

**View project status:**
```bash
cat PROJECT-STATUS.txt
```

**Read main tracker:**
```bash
less REVERSE-ENGINEERING-PROGRESS.md
# Press 'q' to exit
```

**Check package size:**
```bash
ls -lh package/cli.js
# Output: 11.1MB
```

**Start Phase 1:**
```bash
cat analysis/QUICK-START-PHASE-1.md
```

**List all markdown docs:**
```bash
ls -lh *.md analysis/*.md analysis/findings/*.md
```

---

## Success Indicators

**Phase 0:** ✅ COMPLETE
- Package downloaded and extracted ✅
- 20 tools identified ✅
- Analysis roadmap created ✅
- Progress tracking operational ✅

**Phase 1:** 🔵 READY TO BEGIN
- Toolchain to be installed
- cli.js to be beautified
- Bundler to be identified
- Module map to be extracted

**Overall Project:** 5% complete (1/8 phases)

---

## When You're Ready

1. **Read:** `analysis/QUICK-START-PHASE-1.md` (full guide)
2. **Install:** 5 npm packages (prettier, restringer, wakaru, madge, ast-grep)
3. **Execute:** Follow step-by-step instructions
4. **Document:** Update `REVERSE-ENGINEERING-PROGRESS.md`
5. **Continue:** Move to Phase 2 when Phase 1 complete

---

## Need Help?

**Process Questions:** Read `README-REVERSE-ENGINEERING.md`
**Tool Details:** Read `analysis/findings/TOOL-SCHEMA-ANALYSIS.md`
**Phase 1 Questions:** Read `analysis/QUICK-START-PHASE-1.md`
**Current Status:** Read `REVERSE-ENGINEERING-PROGRESS.md`

---

**Status:** Phase 0 Complete, Phase 1 Ready
**Next Action:** Install toolchain and begin bundle analysis
**Estimated Time:** 3-4 hours for Phase 1
**Location:** `/Users/amuldotexe/Desktop/A01_20260131/agent-room-of-requirements/referenceRepo`

**You are ready to begin whenever you choose. Good luck!**
