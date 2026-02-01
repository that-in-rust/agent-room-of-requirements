# Tool Schema Deep Analysis

**Source:** `/package/sdk-tools.d.ts`
**Lines:** 1566
**Tools Identified:** 20
**Analysis Date:** 2026-02-01

---

## Complete Tool Inventory

### 1. Agent - Subagent Spawning & Orchestration

**Interface:** `AgentInput`
**Primary Purpose:** Spawn specialized sub-agents with custom configurations

**Parameters:**
```typescript
{
  description: string;           // Short 3-5 word task summary
  prompt: string;                // Full task description
  subagent_type: string;         // Type of specialized agent
  model?: "sonnet" | "opus" | "haiku";  // Optional model override
  resume?: string;               // Agent ID to resume from
  run_in_background?: boolean;   // Background execution flag
  max_turns?: number;            // Max API round-trips (internal warmup)
  name?: string;                 // Agent display name
  team_name?: string;            // Team context (inherits if omitted)
  mode?: "acceptEdits" | "bypassPermissions" | "default" |
         "delegate" | "dontAsk" | "plan";  // Permission mode
}
```

**Critical Features:**
- **Multi-Model Support:** Can spawn haiku for quick tasks, sonnet for standard, opus for complex
- **Context Inheritance:** Team context and settings inherit from parent
- **Resume Capability:** Can continue from previous execution transcript
- **Permission Propagation:** Child agent permission mode configurable

**Investigation Priority:** HIGH (core orchestration system)

---

### 2. Bash - Command Execution Engine

**Interface:** `BashInput`
**Primary Purpose:** Execute shell commands with sandbox and timeout controls

**Parameters:**
```typescript
{
  command: string;                    // Shell command to run
  timeout?: number;                   // Max timeout (600000ms = 10min)
  description?: string;               // Human-readable command description
  run_in_background?: boolean;        // Background execution
  dangerouslyDisableSandbox?: boolean; // Override sandbox (SECURITY RISK)
  _simulatedSedEdit?: {               // Internal: sed preview result
    filePath: string;
    newContent: string;
  };
}
```

**Critical Features:**
- **Sandbox Mode:** Default sandboxing with override capability
- **Timeout Protection:** 10-minute hard limit
- **Background Execution:** Non-blocking command support
- **Sed Simulation:** Internal preview mechanism for file edits
- **Description Field:** AI-generated command explanations for user clarity

**Security Notes:**
- `dangerouslyDisableSandbox` should be heavily restricted
- Internal `_simulatedSedEdit` suggests preview-before-execute pattern

**Investigation Priority:** HIGH (security and execution model)

---

### 3. TaskOutput - Background Task Monitoring

**Interface:** `TaskOutputInput`
**Primary Purpose:** Retrieve output from background tasks

**Parameters:**
```typescript
{
  task_id: string;     // Target task identifier
  block: boolean;      // Wait for completion vs. check status
  timeout: number;     // Max wait time (milliseconds)
}
```

**Critical Features:**
- **Blocking/Non-Blocking:** Can poll or wait
- **Timeout Control:** Prevent infinite waits

**Related Tools:** Bash (run_in_background), Agent (run_in_background), TaskStop

**Investigation Priority:** MEDIUM (background execution system)

---

### 4. ExitPlanMode - Plan-Based Permission System

**Interface:** `ExitPlanModeInput`
**Primary Purpose:** Exit planning mode with pre-approved permissions

**Parameters:**
```typescript
{
  allowedPrompts?: Array<{
    tool: "Bash";              // Currently only Bash supported
    prompt: string;            // Semantic action description
  }>;
  pushToRemote?: boolean;      // Push to claude.ai session
  remoteSessionId?: string;    // Remote session identifier
  remoteSessionUrl?: string;   // Remote session link
  remoteSessionTitle?: string; // Remote session display name
}
```

**Critical Features:**
- **Semantic Permissions:** "run tests" vs. specific command whitelisting
- **Remote Integration:** Can push plans to claude.ai web interface
- **Bash-Only Currently:** Only Bash tool supports prompt-based permissions

**Investigation Questions:**
- How are semantic prompts matched to actual commands?
- What's the matching algorithm? (exact, fuzzy, LLM-based?)
- Can this be extended to other tools beyond Bash?

**Investigation Priority:** HIGH (permission model critical to understand)

---

### 5. FileEdit - Exact String Replacement

**Interface:** `FileEditInput`
**Primary Purpose:** Edit files via exact string replacement (not line-based)

**Parameters:**
```typescript
{
  file_path: string;         // Absolute path required
  old_string: string;        // Exact text to replace
  new_string: string;        // Replacement text (must differ)
  replace_all?: boolean;     // Replace all occurrences (default: false)
}
```

**Critical Features:**
- **String-Based:** NOT line-based (more flexible than sed)
- **Uniqueness Requirement:** old_string must be unique unless replace_all=true
- **Absolute Paths:** Relative paths not supported

**Investigation Priority:** MEDIUM (core editing primitive)

---

### 6. FileRead - File Content Retrieval

**Interface:** `FileReadInput`
**Primary Purpose:** Read file contents with pagination support

**Parameters:**
```typescript
{
  file_path: string;     // Absolute path required
  offset?: number;       // Starting line number
  limit?: number;        // Number of lines to read
}
```

**Critical Features:**
- **Pagination:** Offset/limit for large files
- **Line-Based:** Returns with line numbers (cat -n format)

**Investigation Priority:** LOW (straightforward implementation expected)

---

### 7. FileWrite - File Creation/Overwriting

**Interface:** `FileWriteInput`
**Primary Purpose:** Write/overwrite files completely

**Parameters:**
```typescript
{
  file_path: string;     // Absolute path required
  content: string;       // Full file content
}
```

**Critical Features:**
- **Full Replacement:** No append/partial write support
- **Absolute Paths:** Relative paths not supported

**Investigation Priority:** LOW (straightforward)

---

### 8. Glob - File Pattern Matching

**Interface:** `GlobInput`
**Primary Purpose:** Find files matching glob patterns

**Parameters:**
```typescript
{
  pattern: string;       // Glob pattern (e.g., "**/*.js")
  path?: string;         // Search directory (default: cwd)
}
```

**Critical Features:**
- **Standard Glob:** Supports **, *, ?, [] patterns
- **Fast:** Likely uses native implementation

**Investigation Priority:** LOW (standard glob implementation expected)

---

### 9. Grep - Content Search (Ripgrep-Powered)

**Interface:** `GrepInput`
**Primary Purpose:** Fast regex-based content search using ripgrep

**Parameters:**
```typescript
{
  pattern: string;                    // Regex pattern
  path?: string;                      // Search path (default: cwd)
  glob?: string;                      // File filter (e.g., "*.js")
  output_mode?: "content" | "files_with_matches" | "count";
  "-B"?: number;                      // Lines before match
  "-A"?: number;                      // Lines after match
  "-C"?: number;                      // Lines before + after (context)
  context?: number;                   // Alias for -C
  "-n"?: boolean;                     // Line numbers (default: true)
  "-i"?: boolean;                     // Case insensitive
  type?: string;                      // File type (js, py, rust, etc.)
  head_limit?: number;                // Limit output lines
  offset?: number;                    // Skip first N results
  multiline?: boolean;                // Multiline regex mode
}
```

**Critical Features:**
- **Ripgrep Integration:** Uses bundled ripgrep binary from /vendor/ripgrep/
- **Three Output Modes:** content, files_with_matches, count
- **Context Support:** Show surrounding lines
- **Type Filtering:** Built-in file type recognition
- **Pagination:** head_limit + offset for large result sets
- **Multiline Regex:** Advanced pattern matching across lines

**Platform Support:**
- arm64-darwin
- x64-darwin
- arm64-linux
- x64-linux
- x64-win32

**Investigation Priority:** HIGH (complex tool, platform-specific binaries)

---

### 10. TaskStop - Background Task Termination

**Interface:** `TaskStopInput`
**Primary Purpose:** Stop running background tasks

**Parameters:**
```typescript
{
  task_id?: string;      // Task identifier
  shell_id?: string;     // Deprecated: old identifier
}
```

**Critical Features:**
- **Graceful Termination:** (vs. kill -9?)
- **Deprecated Field:** shell_id suggests API evolution

**Investigation Priority:** MEDIUM (background task lifecycle)

---

### 11. ListMcpResources - MCP Resource Discovery

**Interface:** `ListMcpResourcesInput`
**Primary Purpose:** List available Model Context Protocol resources

**Parameters:**
```typescript
{
  server?: string;       // Optional server filter
}
```

**Critical Features:**
- **MCP Integration:** External server support
- **Optional Filtering:** Can list all or specific server

**Investigation Questions:**
- What is the MCP server registration mechanism?
- How are MCP servers discovered/configured?
- What resource types are supported?

**Investigation Priority:** MEDIUM (extensibility mechanism)

---

### 12. Mcp - MCP Tool Invocation

**Interface:** `McpInput`
**Primary Purpose:** Generic MCP tool execution

**Parameters:**
```typescript
{
  [k: string]: unknown;  // Dynamic schema (tool-dependent)
}
```

**Critical Features:**
- **Dynamic Schema:** Parameters depend on MCP tool being called
- **Extensibility:** Allows third-party tool integration

**Investigation Priority:** MEDIUM (extensibility mechanism)

---

### 13. NotebookEdit - Jupyter Notebook Manipulation

**Interface:** `NotebookEditInput`
**Primary Purpose:** Edit Jupyter notebook cells

**Parameters:**
```typescript
{
  notebook_path: string;              // Absolute path to .ipynb
  cell_id?: string;                   // Target cell ID
  new_source: string;                 // New cell content
  cell_type?: "code" | "markdown";    // Cell type
  edit_mode?: "replace" | "insert" | "delete";  // Operation type
}
```

**Critical Features:**
- **Cell-Level Operations:** Granular editing (not whole-file)
- **Three Edit Modes:** Replace, insert, delete
- **Cell Types:** Code and markdown support
- **Cell IDs:** Stable identifiers across edits

**Investigation Priority:** LOW (Jupyter-specific, likely uses standard libraries)

---

### 14. ReadMcpResource - MCP Resource Access

**Interface:** `ReadMcpResourceInput`
**Primary Purpose:** Read content from MCP resource URIs

**Parameters:**
```typescript
{
  server: string;        // MCP server name
  uri: string;           // Resource URI to read
}
```

**Critical Features:**
- **URI-Based Access:** Resource identification via URIs
- **Server Namespacing:** Resources scoped to servers

**Investigation Priority:** MEDIUM (MCP integration)

---

### 15. TodoWrite - Task Tracking System

**Interface:** `TodoWriteInput`
**Primary Purpose:** Manage task lists with state tracking

**Parameters:**
```typescript
{
  todos: Array<{
    content: string;                          // Task description
    status: "pending" | "in_progress" | "completed";
    activeForm: string;                       // Present continuous form
  }>;
}
```

**Critical Features:**
- **State Machine:** pending → in_progress → completed
- **Dual Forms:** content (imperative) vs. activeForm (continuous)
- **Array Replacement:** Entire list replaced on each update

**Investigation Questions:**
- How is state persisted between sessions?
- Is there undo/history support?

**Investigation Priority:** LOW (UI/UX feature, less critical)

---

### 16. WebFetch - URL Content Retrieval

**Interface:** `WebFetchInput`
**Primary Purpose:** Fetch and process web content with AI

**Parameters:**
```typescript
{
  url: string;           // Target URL
  prompt: string;        // Processing instruction for AI
}
```

**Critical Features:**
- **AI Processing:** Content processed through model
- **HTML→Markdown:** Conversion mentioned in docs
- **Caching:** 15-minute self-cleaning cache

**Investigation Priority:** MEDIUM (AI-powered processing interesting)

---

### 17. WebSearch - Web Search Integration

**Interface:** `WebSearchInput`
**Primary Purpose:** Perform web searches with domain filtering

**Parameters:**
```typescript
{
  query: string;                  // Search query
  allowed_domains?: string[];     // Whitelist
  blocked_domains?: string[];     // Blacklist
}
```

**Critical Features:**
- **Domain Filtering:** Include/exclude control
- **US-Only:** Geographic restriction noted in docs

**Investigation Questions:**
- What search provider is used? (Google, Bing, custom?)
- How are results ranked/filtered?

**Investigation Priority:** LOW (external API integration)

---

### 18. AskUserQuestion - Interactive User Prompts

**Interface:** `AskUserQuestionInput`
**Primary Purpose:** Collect structured user input during execution

**Parameters:**
```typescript
{
  questions: Array<{
    question: string;                // Full question text
    header: string;                  // Short label (max 12 chars)
    options: Array<{                 // 2-4 options
      label: string;                 // Option text (1-5 words)
      description: string;           // Explanation
    }>;
    multiSelect: boolean;            // Allow multiple selections
  }>;  // 1-4 questions
  answers?: { [k: string]: string }; // Collected answers
  metadata?: {
    source?: string;                 // Analytics tracking (e.g., "remember")
  };
}
```

**Critical Features:**
- **Structured Prompts:** Not freeform input
- **Multi-Question:** 1-4 questions per call
- **Multi-Select:** Optional checkbox behavior
- **Auto "Other":** Other option provided automatically
- **Analytics:** Metadata for tracking prompt sources

**Investigation Priority:** LOW (UI/interaction feature)

---

### 19. Config - Settings Management

**Interface:** `ConfigInput`
**Primary Purpose:** Get/set configuration values

**Parameters:**
```typescript
{
  setting: string;                      // Setting key (e.g., "theme")
  value?: string | boolean | number;    // New value (omit to get)
}
```

**Critical Features:**
- **Dot Notation:** Supports nested keys (e.g., "permissions.defaultMode")
- **Get/Set:** Value optional for read operations
- **Type Support:** String, boolean, number

**Investigation Questions:**
- Where are settings persisted? (file, database, memory?)
- What settings are available?

**Investigation Priority:** LOW (configuration plumbing)

---

### 20. BashOutput (Inferred)

**Interface:** Not explicitly in sdk-tools.d.ts (mentioned in docs)
**Primary Purpose:** Read output from background bash shells

**Expected Parameters:**
```typescript
{
  bash_id: string;       // Shell identifier
  filter?: string;       // Regex filter for output lines
}
```

**Status:** INFERRED (not in TypeScript definitions)

**Investigation Priority:** MEDIUM (background execution system)

---

## Cross-Cutting Concerns

### Background Execution Pattern
**Supporting Tools:** Agent, Bash, TaskOutput, TaskStop, BashOutput
**Pattern:**
1. Start task with `run_in_background: true`
2. Receive task_id/bash_id in response
3. Poll with TaskOutput/BashOutput
4. Optionally stop with TaskStop

### Permission System
**Supporting Tools:** Agent (mode), ExitPlanMode (allowedPrompts), Bash (dangerouslyDisableSandbox)
**Modes:**
- `acceptEdits` - Require approval for file changes
- `bypassPermissions` - No prompts (dangerous)
- `default` - Standard behavior
- `delegate` - Defer to parent agent
- `dontAsk` - Assume approval
- `plan` - Require upfront plan approval

### MCP Integration
**Supporting Tools:** ListMcpResources, Mcp, ReadMcpResource
**Purpose:** Third-party tool/resource integration via Model Context Protocol

### File Operations
**Supporting Tools:** FileEdit, FileRead, FileWrite, Glob, Grep
**Path Requirements:** All require absolute paths (no relative paths)

---

## Architectural Implications

### Layered Design
```
User Interface Layer
    ↓
Tool Dispatch Layer (20 tools)
    ↓
Execution Layer (Bash, Agent orchestration)
    ↓
Platform Layer (ripgrep, WASM parsers)
    ↓
API Layer (Claude API, MCP servers, Web APIs)
```

### Extensibility Mechanisms
1. **MCP Protocol:** Third-party tools and resources
2. **Multi-Model Agents:** Task-specific model selection
3. **Permission Modes:** Flexible approval workflows
4. **Background Execution:** Non-blocking operations

### Security Boundaries
1. **Sandbox:** Default for Bash execution
2. **Permission Modes:** Multi-level approval system
3. **Absolute Paths:** Prevent directory traversal attacks
4. **Timeout Limits:** Prevent runaway processes (10min max)

---

## Investigation Priorities for Phase 2

### HIGH Priority (Days 3-4):
1. **Agent System:** Subagent spawning, context inheritance, model selection
2. **Bash + Permissions:** Sandbox implementation, ExitPlanMode matching logic
3. **Grep + Ripgrep:** Binary selection, platform detection, performance

### MEDIUM Priority (Day 5):
4. **Background Execution:** TaskOutput, TaskStop, task lifecycle
5. **MCP Integration:** Server registration, tool invocation
6. **WebFetch:** AI processing pipeline

### LOW Priority (Optional):
7. File operations (straightforward)
8. TodoWrite (UI feature)
9. Config (settings plumbing)
10. AskUserQuestion (UI interaction)

---

## Open Questions

1. **How does ExitPlanMode match semantic prompts to actual Bash commands?**
   - Exact string matching?
   - Fuzzy matching?
   - LLM-based intent matching?

2. **What is the Agent state persistence mechanism?**
   - How is `resume` parameter implemented?
   - Where are agent transcripts stored?

3. **How are MCP servers registered and discovered?**
   - Configuration file?
   - Runtime registration API?
   - Auto-discovery?

4. **What is the internal `_simulatedSedEdit` mechanism?**
   - Preview-before-execute pattern?
   - Dry-run validation?
   - User confirmation flow?

5. **How are platform-specific ripgrep binaries selected at runtime?**
   - Process.platform detection?
   - Fallback chain?
   - User override?

---

**Analysis Complete:** 2026-02-01
**Next Phase:** Map these 20 schemas to implementation code in cli.js
**Tool Count:** 20 confirmed, 1 inferred (BashOutput)
