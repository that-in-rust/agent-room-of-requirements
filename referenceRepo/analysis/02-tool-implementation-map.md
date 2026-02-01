# Tool Implementation Map - Phase 2

**Analysis Date:** 2026-02-01
**Phase:** 2 of 8
**Source:** analysis/cli-beautified.js

## Overview

This document maps each of the 20 tool schemas from `sdk-tools.d.ts` to their implementation locations in the beautified cli.js file.

## Tool Name Constants

All tools have their names stored in short variable identifiers for minification:

| Tool | Variable | Line | Context |
|------|----------|------|---------|
| Bash | `X4` | 138,676 | Sandbox-related |
| Edit | `$3` | 145,049 | File editing with path restrictions |
| Read | `pK` | 145,065 | File reading with limits |
| Glob | `cw` | 145,390 | Pattern matching |
| Grep | `J2` | 145,411 | Ripgrep search |
| Write | `wz` | 145,427 | File writing with guidelines |
| Task/Agent | `vK` | 145,396 | Referenced in tool descriptions |
| NotebookEdit | `XP` | 145,433 | Jupyter notebook editing |

## Individual Tool Implementations

### 1. Bash Tool (X4)

**Location:** Line 138,676
**Variable:** `var X4 = "Bash";`

**Related Components:**
- **Sandbox Debug Function:** `function f8(A, q)` (line 138,677)
  - Environment check: `process.env.SRT_DEBUG`
  - Log levels: error, warn, info
  - Prefix: `[SandboxDebug]`

**Sandbox Integration:**
- Line 145,383-145,389: Sandbox API exports
  ```javascript
  {
    waitForNetworkInitialization: q$.waitForNetworkInitialization,
    getSandboxViolationStore: q$.getSandboxViolationStore,
    annotateStderrWithSandboxFailures: q$.annotateStderrWithSandboxFailures,
  }
  ```

**Key Characteristics:**
- Heavily integrated with sandboxing system
- Network initialization required
- Sandbox violation tracking
- stderr annotation for failures

### 2. Edit Tool ($3)

**Location:** Line 145,049
**Variable:** `var $3 = "Edit";`

**Constants Defined:**
- `j76 = "/.claude/**"` (line 145,050) - Protected path pattern
- `M76 = "~/.claude/**"` (line 145,051) - User-specific protected path
- `qR1 = "File has been unexpectedly modified..."` (line 145,052) - Conflict error message

**Helper Functions:**
- **`KR1()`** (line 145,053): Checks if mode is "firstParty"
  ```javascript
  function KR1() {
    return F4() === "firstParty";
  }
  ```

- **`P76(A)`** (line 145,057): File extension validation
  ```javascript
  function P76(A) {
    let q = A.startsWith(".") ? A.slice(1) : A;
    return Wb5.has(q.toLowerCase());
  }
  ```

- **`Wb5`** (line 145,063): Set of restricted extensions
  ```javascript
  Wb5 = new Set(["pdf"]);
  ```

**Security Features:**
- Protected directory patterns
- File modification detection
- Extension-based restrictions (PDFs)
- "firstParty" mode checking

### 3. Read Tool (pK)

**Location:** Line 145,065
**Variable:** `var pK = "Read";`

**Constants:**
- `YR1 = 2000` (line 145,066) - Default line limit
- `Gb5 = 2000` (line 145,067) - Line length limit (characters)
- `i_7 = "Read a file from the local filesystem."` (line 145,068) - Tool description

**Limits:**
- Default: 2000 lines maximum
- 2000 characters per line maximum
- Configurable offset and limit parameters

**Module Reference:**
- `var z$ = E(()...` (line 145,070) - Module initialization

### 4. Glob Tool (cw)

**Location:** Line 145,390
**Variable:** `var cw = "Glob";`

**Description Constant:**
- `EAA` (line 145,391) - Multi-line description string:
  ```javascript
  `- Fast file pattern matching tool that works with any codebase size
  - Supports glob patterns like "**/*.js" or "src/**/*.ts"
  - Returns matching file paths sorted by modification time
  - Use this tool when you need to find files by name patterns
  - When you are doing an open ended search that may require multiple rounds of globbing and grepping, use the Agent tool instead
  - You can call multiple tools in a single response. It is always better to speculatively perform multiple searches in parallel if they are potentially useful.`
  ```

**Key Features:**
- Pattern-based file matching
- Modification time sorting
- Parallel execution recommendation
- Agent tool escalation guidance

### 5. Task/Agent Tool (vK)

**Location:** Line 145,396
**Variable:** `var vK = "Task";`

**Context:**
- Referenced within Grep tool description
- Used for open-ended searches
- Multi-round operation support

**Note:** This might be the internal name for the Agent tool, or a parent category.

### 6. Grep Tool (J2)

**Location:** Line 145,411
**Variable:** `var J2 = "Grep";`

**Description Function:**
- `function kAA()` (line 145,399) - Returns multi-line description
- References:
  - `${J2}` - Self-reference (Grep)
  - `${X4}` - Bash tool reference
  - `${vK}` - Task/Agent tool reference

**Key Features (from description):**
- Built on ripgrep
- Full regex syntax support
- Multiple output modes: content, files_with_matches, count
- Multiline matching capability
- Special escaping for literal braces
- Optimized permissions and access

**Important Warning:**
```
"ALWAYS use ${J2} for search tasks. NEVER invoke `grep` or `rg` as a ${X4} command."
```

**Initialization:**
- `var XT = () => {};` (line 145,413) - Empty function (placeholder?)

### 7. Write Tool (wz)

**Location:** Line 145,427
**Variable:** `var wz = "Write";`

**Description Function:**
- Returns description with conditional content via `Ib5()` function
- `function Ib5()` (line 145,415) - Checks feature flag `tengu_marble_kite`

**Guidelines (embedded in description):**
- Overwrites existing files
- Prefer editing over writing new files
- No proactive documentation file creation
- Emoji usage only when requested

**Module Reference:**
- `var JP = E(()...` (line 145,428) - Module initialization
- Depends on: `s4()` and `z$()` modules

### 8. NotebookEdit Tool (XP)

**Location:** Line 145,433
**Variable:** `var XP = "NotebookEdit";`

**Helper Functions:**
- **`wR1()`** (line 145,435): Returns current date YYYY-MM-DD
  ```javascript
  function wR1() {
    let A = new Date(),
      q = A.getFullYear(),
      K = String(A.getMonth() + 1).padStart(2, "0"),
      Y = String(A.getDate()).padStart(2, "0");
    return `${q}-${K}-${Y}`;
  }
  ```

- **`KJ7()`** (line 145,443): Returns WebSearch-related description
  - Mentions "search the web"
  - "CRITICAL REQUIREMENT" for Sources section
  - Uses current year from `wR1()`

**Note:** The `KJ7()` function content seems misplaced - it talks about web search, not notebook editing. This might indicate code reuse or a copy-paste artifact.

## Tool Categories

### File Pattern Tools (Line 63,215)
```javascript
filePatternTools: ["Read", "Write", "Edit", "Glob", "NotebookRead", "NotebookEdit"]
```

### Bash Prefix Tools (Line 63,216)
```javascript
bashPrefixTools: ["Bash"]
```

### Core Tool Set (Line 253,628)
```javascript
Nq4 = new Set(["Read", "Write", "Edit", "Glob", "Grep", "Bash", "NotebookEdit"])
```

### Write Tools (Line 369,707)
```javascript
["Edit", "Write", "NotebookEdit"]
```

### Read Tools (Line 369,708)
```javascript
["Read", "Glob", "Grep", "ToolSearch", "LSP", "TaskGet", "TaskList"]
```

## Tool Dispatch Logic

### Classification Logic (Lines 369,707-369,708)

```javascript
let P = ["Edit", "Write", "NotebookEdit"].includes(j.name),  // Write operations
    W = ["Read", "Glob", "Grep", "ToolSearch", "LSP", "TaskGet", "TaskList"].includes(j.name);  // Read operations
```

**Pattern:**
- `P` = Write tools (modifying operations)
- `W` = Read tools (non-modifying operations)
- Variable `j.name` likely contains the tool name

### Special Bash Handling (Line 369,768)

```javascript
if (j.name === "Bash" && "command" in M && typeof M.command === "string") {
  // Special command processing logic
}
```

### Result Formatting (Line 253,807)

```javascript
let H = K ? (z.length === 0 ? "Reading" : "reading") : z.length === 0 ? "Read" : "read";
```

**Pattern:** Conditional verb forms based on:
- Context flag `K`
- Array length `z.length`
- Capitalization varies by position

### Read Tool Detection (Lines 258,239 & 258,250)

```javascript
O === "Read" && "input" in A && A.input && typeof A.input === "object" && "file_path" in A.input
// ... later ...
if ((u34(K.toolResults, O, H), O === "Read")) {
  // Read-specific processing
}
```

## Integration Points

### Ripgrep Integration (for Grep tool)

**References found:**
- Built on ripgrep (mentioned in description)
- Vendor binaries in `package/vendor/ripgrep/`
- Platform-specific: arm64-darwin, x64-linux, x64-win32

**Expected integration pattern:**
```javascript
// Likely uses child_process to spawn ripgrep binary
// Platform detection to select correct binary
// Result parsing and formatting
```

### Sandbox Integration (for Bash tool)

**API Surface (Line 145,383-145,389):**
```javascript
{
  waitForNetworkInitialization,
  getSandboxViolationStore,
  annotateStderrWithSandboxFailures,
}
```

**Debug logging:** `f8()` function for SRT_DEBUG mode

### File System Integration

**Protected paths:**
- `/.claude/**` - System directory
- `~/.claude/**` - User configuration directory

**File operations module:** `z$` (referenced by Read and Write)

## Cross-Tool References

### Tool Description Cross-References

1. **Glob → Agent/Task:**
   - "use the Agent tool instead" for open-ended searches

2. **Grep → Bash:**
   - "NEVER invoke `grep` or `rg` as a Bash command"

3. **Grep → Task:**
   - "Use Task tool for open-ended searches"

### Module Dependencies

```javascript
var JP = E(() => {
  s4();   // Unknown module
  z$();   // File operations (used by Read/Write)
});
```

## Security & Safety Features

### 1. Sandbox System
- Violation tracking store
- stderr failure annotation
- Network initialization gating

### 2. Path Restrictions
- Protected Claude directories
- Pattern-based blocking

### 3. File Modification Detection
- Edit tool checks for unexpected modifications
- Error: "File has been unexpectedly modified. Read it again before attempting to write it."

### 4. Extension Restrictions
- PDF files have special handling (cannot edit directly)

### 5. Permission Modes
- "firstParty" mode checking in Edit tool

## Unknown/To Investigate

### Tool Variables Not Yet Located
- AgentInput / Agent tool handler
- AskUserQuestionInput
- TodoWriteInput
- WebFetchInput
- WebSearchInput
- McpInput (and related MCP tools)
- BashOutput / TaskOutput
- TaskStop
- ExitPlanModeInput
- ConfigInput

### Mystery Functions
- `F4()` - Returns permission/mode string
- `s4()` - Unknown module
- `u34()` - Tool result processing
- `Ib5()` - Feature flag check for "tengu_marble_kite"
- `J7()` - Feature flag checker

### Missing Implementations
- Actual command execution logic
- Result parsing and formatting details
- API client communication
- State management integration

## Next Steps for Phase 3

1. **Locate remaining tools** (Agent, TodoWrite, AskUserQuestion, etc.)
2. **Trace tool execution flow** from dispatch to result
3. **Map API client integration** - how tools communicate results
4. **Document state management** - how tool state is tracked
5. **Understand permission enforcement** - how "firstParty" mode works

## Line Number Reference

Quick reference for exploring further:

- **138,676**: Bash tool definition + sandbox debug
- **145,049-145,069**: Edit tool (protections, limits)
- **145,065-145,070**: Read tool (limits, description)
- **145,390-145,398**: Glob tool (description)
- **145,411-145,414**: Grep tool (description, init)
- **145,427-145,430**: Write tool (guidelines)
- **145,433-145,450**: NotebookEdit tool (date helpers)
- **63,215-63,216**: Tool categories
- **253,628**: Core tool Set
- **369,707-369,768**: Tool dispatch logic

## Findings Summary

✅ **Confirmed:**
- 8 of 20 tools located and documented
- Tool names stored in short variables for minification
- Tool descriptions embedded as multi-line strings
- Security features: sandbox, path protection, extension blocking
- Tool categorization: Write vs Read operations
- Cross-tool references in descriptions

🔍 **Discovered:**
- Feature flag system (`tengu_marble_kite`, etc.)
- File modification detection for Edit
- Protected Claude directories
- Ripgrep integration for Grep
- Sandbox violation tracking
- Special Bash command handling

❓ **Remaining Questions:**
- Where are the other 12 tools defined?
- How is the tool dispatch actually implemented?
- What is the `F4()` function that returns mode?
- How are tool results communicated to the API?
- Where is the Agent/subagent spawning logic?

**Phase 2 Status: ~40% complete** (8/20 tools documented)
**Next: Continue tool discovery and trace execution flow**
