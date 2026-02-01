# Claude Code Architecture - Complete Analysis

**Package:** @anthropic-ai/claude-code v2.1.29
**Analysis Date:** 2026-02-01
**Build Time:** 2026-01-31T20:12:07Z

## Table of Contents

1. [High-Level Architecture](#high-level-architecture)
2. [Module System](#module-system)
3. [Tool System](#tool-system)
4. [Agent & Subagent System](#agent--subagent-system)
5. [API Communication Layer](#api-communication-layer)
6. [State Management](#state-management)
7. [Security & Sandbox](#security--sandbox)
8. [Plugin & Extension System](#plugin--extension-system)

---

## High-Level Architecture

```mermaid
graph TB
    User[User/CLI] --> Entry[CLI Entry Point]
    Entry --> Parser[Command Parser]
    Parser --> Session[Session Manager]

    Session --> Tools[Tool Dispatcher]
    Session --> Agents[Agent Manager]
    Session --> State[State Manager]

    Tools --> FileOps[File Operations]
    Tools --> Search[Search Tools]
    Tools --> Exec[Execution Tools]
    Tools --> UI[UI Tools]
    Tools --> Web[Web Tools]

    FileOps --> |Read/Write/Edit| FS[File System]
    Search --> |Glob/Grep| RG[Ripgrep Binary]
    Exec --> |Bash| Sandbox[Sandbox System]

    Agents --> Spawn[Agent Spawner]
    Spawn --> InProcess[In-Process Teammate]
    Spawn --> Background[Background Executor]

    State --> SessionDB[Session Storage]
    State --> CostTracker[Cost Tracker]
    State --> TaskList[Task Lists]

    Tools --> API[API Client]
    Agents --> API
    API --> Anthropic[Anthropic API]

    style User fill:#e1f5ff
    style Anthropic fill:#f9f,stroke:#333,stroke-width:4px
    style Sandbox fill:#ffe1e1
```

---

## Module System

### Bundle Structure

```mermaid
graph LR
    Bundle[cli.js 11.1MB] --> ES6[ES6 Imports]
    Bundle --> CJS[CommonJS Wrapper]

    ES6 --> NodeMods[Node Modules]
    NodeMods --> NM1[node:module]
    NodeMods --> NM2[node:fs]
    NodeMods --> NM3[node:path]

    CJS --> Wrapper[Module Wrapper fn]
    Wrapper --> Exports[__esModule Handler]

    Bundle --> Vendor[Vendor Binaries]
    Vendor --> RG[Ripgrep]
    Vendor --> TS[tree-sitter.wasm]
    Vendor --> TSB[tree-sitter-bash.wasm]
    Vendor --> SVG[resvg.wasm]

    style Bundle fill:#fff3cd
    style Vendor fill:#d1ecf1
```

### Module Wrapper Pattern

**Line 13:**
```javascript
var r = (A, q, K) => {
    K = A != null ? bNq(uNq(A)) : {};
    let Y = q || !A || !A.__esModule
        ? fZ1(K, "default", { value: A, enumerable: !0 })
        : K;
    for (let z of MBA(A))
        if (!PBA.call(Y, z))
            fZ1(Y, z, { get: () => A[z], enumerable: !0 });
    return Y;
}
```

**Purpose:** Converts CommonJS modules to ES6 format with __esModule marking

---

## Tool System

### Tool Hierarchy

```mermaid
graph TD
    Root[21 Tools] --> Cat1[File Operations - 4]
    Root --> Cat2[Search - 1]
    Root --> Cat3[Execution - 1]
    Root --> Cat4[Agent System - 5]
    Root --> Cat5[User Interaction - 2]
    Root --> Cat6[Web - 2]
    Root --> Cat7[Notebooks - 2]
    Root --> Cat8[MCP Integration - 3]
    Root --> Cat9[Plan Mode - 2]

    Cat1 --> T1[Read]
    Cat1 --> T2[Write]
    Cat1 --> T3[Edit]
    Cat1 --> T4[Glob]

    Cat2 --> T5[Grep]

    Cat3 --> T6[Bash]

    Cat4 --> T7[Task/Agent]
    Cat4 --> T8[TaskGet]
    Cat4 --> T9[TaskList]
    Cat4 --> T10[TaskStop]
    Cat4 --> T11[TaskOutput]

    Cat5 --> T12[TodoWrite]
    Cat5 --> T13[AskUserQuestion]

    Cat6 --> T14[WebFetch]
    Cat6 --> T15[WebSearch]

    Cat7 --> T16[NotebookEdit]
    Cat7 --> T17[NotebookRead]

    Cat8 --> T18[ListMcpResources]
    Cat8 --> T19[ReadMcpResource]
    Cat8 --> T20[Mcp]

    Cat9 --> T21[EnterPlanMode]
    Cat9 --> T22[ExitPlanMode]
```

### Tool Dispatch Flow

```mermaid
sequenceDiagram
    participant User
    participant Dispatcher
    participant Validator
    participant Handler
    participant Sandbox
    participant FS as File System
    participant API as Claude API

    User->>Dispatcher: Tool Request (e.g., Read)
    Dispatcher->>Dispatcher: Classify (Write vs Read)
    Dispatcher->>Validator: Validate Input
    Validator->>Validator: Check Permissions
    Validator->>Validator: Check Path Protection
    Validator-->>Dispatcher: Validation Result

    alt Valid Request
        Dispatcher->>Handler: Execute Tool
        Handler->>Sandbox: Check Sandbox (if Bash)
        Sandbox-->>Handler: Approval
        Handler->>FS: Perform Operation
        FS-->>Handler: Result
        Handler-->>Dispatcher: Format Result
        Dispatcher->>API: Send to Claude
        API-->>User: Response
    else Invalid Request
        Validator-->>User: Error Message
    end
```

### Tool Categories

**Write Tools (Line 369,707):**
- Edit
- Write
- NotebookEdit

**Read Tools (Line 369,708):**
- Read
- Glob
- Grep
- ToolSearch
- LSP
- TaskGet
- TaskList

**Bash Prefix Tools (Line 63,216):**
- Bash (special sandboxed execution)

### Tool Implementation Details

| Tool | Variable | Line | Key Features |
|------|----------|------|--------------|
| Bash | X4 | 138,676 | Sandbox, network init, violation tracking |
| Read | pK | 145,065 | 2000 line limit, 2000 char/line |
| Write | wz | 145,427 | Overwrite mode, no proactive docs |
| Edit | $3 | 145,049 | Modification detection, PDF blocking |
| Glob | cw | 145,390 | Pattern matching, mod time sort |
| Grep | J2 | 145,411 | Ripgrep-based, regex support |

---

## Agent & Subagent System

### Agent Architecture

```mermaid
graph TB
    Request[Agent Spawn Request] --> Validate[Validate Request]
    Validate --> Create[spawnInProcessTeammate]

    Create --> Identity[Create Agent Identity]
    Create --> Abort[Initialize AbortController]
    Create --> Perm[Set Permission Mode]

    Perm --> |plan mode| PlanMode[Requires Approval]
    Perm --> |default mode| DefaultMode[Standard Permissions]

    Create --> Register[Register in AppState]
    Register --> Cleanup[Attach Cleanup Handler]

    Cleanup --> Running[Agent Running]

    Running --> Execute[Execute Tools]
    Running --> Track[Track Usage]
    Running --> Messages[Handle Messages]
    Running --> Status[Report Status]

    Execute --> |tool results| Queue[Message Queue]
    Track --> |tokens, tool count| Metrics[Usage Metrics]

    Running --> |shutdown| Shutdown[Cleanup & Shutdown]
    Shutdown --> AbortCtrl[Abort Controller Triggered]
    AbortCtrl --> Unregister[Unregister from AppState]

    style PlanMode fill:#ffe1e1
    style Running fill:#e1f5e1
```

### Agent Object Structure

**Lines 323,850-323,900:**

```javascript
{
  type: "in_process_teammate",
  status: "running",              // running | idle | shutting_down
  identity: j,                    // Unique agent ID
  prompt: z,                      // Agent instructions
  model: O,                       // sonnet | opus | haiku
  abortController: X,             // Cancellation mechanism
  permissionMode: H ? "plan" : "default",  // Permission level
  awaitingPlanApproval: !1,
  isIdle: !1,
  shutdownRequested: !1,
  lastReportedToolCount: 0,
  lastReportedTokenCount: 0,
  pendingUserMessages: [],
  messages: [],                   // Conversation history
  localTaskId: W,                 // Task integration
  unregisterCleanup: Z            // Cleanup callback
}
```

### Team Coordination System

```mermaid
graph LR
    Team[Team] --> |1:1| TaskList[Task List]

    Team --> Agents[Multiple Agents]
    Agents --> A1[Agent 1]
    Agents --> A2[Agent 2]
    Agents --> A3[Agent N]

    A1 --> |join request| Approval[Approval System]
    Approval --> |approve| Join[Join Team]
    Approval --> |reject| Reject[Rejection]

    Join --> Shared[Shared Task List]
    Shared --> Tasks[Tasks]
    Tasks --> TC[TaskCreate]
    Tasks --> TG[TaskGet]
    Tasks --> TL[TaskList]
    Tasks --> TU[TaskUpdate]

    style Team fill:#d1ecf1
    style Shared fill:#d4edda
```

### Agent Lifecycle States

```mermaid
stateDiagram-v2
    [*] --> Spawning: spawnInProcessTeammate()
    Spawning --> Running: Registration Complete
    Running --> AwaitingApproval: Plan Mode Triggered
    AwaitingApproval --> Running: Approved
    AwaitingApproval --> Shutdown: Rejected
    Running --> Idle: No Active Tasks
    Idle --> Running: Task Assigned
    Running --> Shutdown: Shutdown Requested
    Shutdown --> Cleanup: Abort Triggered
    Cleanup --> [*]: Unregistered

    Running: Execute Tools
    Running: Track Metrics
    Running: Handle Messages

    Idle: isIdle = true
    Idle: Waiting for Work
```

---

## API Communication Layer

### API Configuration

```mermaid
graph LR
    Config[API Config] --> Prod[Production]
    Config --> Local[Local Dev]

    Prod --> ProdAPI[api.anthropic.com]
    Prod --> ProdOAuth[platform.claude.com]
    Prod --> ProdMCP[mcp-proxy.anthropic.com]

    Local --> LocalAPI[localhost:3000]
    Local --> LocalOAuth[localhost:3000]
    Local --> LocalMCP[localhost:8205]

    ProdAPI --> Client[Anthropic Client]
    LocalAPI --> Client

    Client --> Messages[messages.create]
    Client --> Streaming[SSE Stream]
    Client --> Tools[Tool Use Protocol]

    style ProdAPI fill:#f9f
    style Client fill:#d1ecf1
```

### API Endpoints

**Production (Lines 23,822-23,835):**

```
BASE_API_URL: https://api.anthropic.com
CONSOLE_AUTHORIZE_URL: https://platform.claude.com/oauth/authorize
CLAUDE_AI_AUTHORIZE_URL: https://claude.ai/oauth/authorize
TOKEN_URL: https://platform.claude.com/v1/oauth/token
API_KEY_URL: https://api.anthropic.com/api/oauth/claude_cli/create_api_key
ROLES_URL: https://api.anthropic.com/api/oauth/claude_cli/roles
MCP_PROXY_URL: https://mcp-proxy.anthropic.com
MCP_PROXY_PATH: /v1/mcp/{server_id}
CLIENT_ID: 9d1c250a-e61b-44d9-88ed-5944d1962f5e
```

### Request Flow

```mermaid
sequenceDiagram
    participant Agent
    participant Client
    participant API as Anthropic API
    participant Stream

    Agent->>Client: Create Message Request
    Client->>Client: Build Request Payload
    Client->>Client: Add Beta Headers
    Client->>Client: Set User-Agent
    Client->>API: POST /v1/messages

    alt Streaming Response
        API->>Stream: SSE Stream Start
        loop Message Chunks
            Stream->>Client: content_block_start
            Stream->>Client: content_block_delta
            Stream->>Agent: Progressive Update
        end
        Stream->>Client: message_stop
    else Non-Streaming
        API->>Client: Complete Response
    end

    Client->>Client: Parse Tool Use
    alt Tool Use Detected
        Client->>Agent: Execute Tools
        Agent->>Client: Tool Results
        Client->>API: Continue Conversation
    else No Tools
        Client->>Agent: Final Response
    end
```

### Beta Features

**Line 136,525:**
```javascript
headers: {
  "anthropic-beta": ["files-api-2025-04-14"].toString()
}
```

Enabled beta features:
- `files-api-2025-04-14` - File upload support

### User Agent

**Lines 125,797-125,803:**
```
claude-code/2.1.29 (external context)
claude-cli/2.1.29 (CLI mode)
```

---

## State Management

### State Architecture

```mermaid
graph TB
    State[Global State] --> Session[Session State]
    State --> Cost[Cost Tracking]
    State --> Tasks[Task State]
    State --> Agents[Agent State]
    State --> UI[UI State]

    Session --> SessionID[Session ID]
    Session --> Context[Conversation Context]
    Session --> Files[File Cache]

    Cost --> Tokens[Token Count]
    Cost --> API[API Calls]
    Cost --> Models[Model Usage]

    Tasks --> Team[Team Tasks]
    Tasks --> Individual[Individual Tasks]
    Tasks --> Status[Task Status]

    Agents --> InProc[In-Process Agents]
    Agents --> BG[Background Agents]
    Agents --> Metrics[Agent Metrics]

    UI --> Panes[Panes State]
    UI --> Messages[Message Display]
    UI --> Progress[Progress Bars]

    style State fill:#fff3cd
```

### Cost Tracking

```mermaid
graph LR
    Request[API Request] --> Track[Track Request]
    Track --> Model[Model Used]
    Track --> Tokens[Tokens Consumed]
    Track --> Tools[Tools Executed]

    Model --> Cost[Calculate Cost]
    Tokens --> Cost
    Tools --> Cost

    Cost --> Update[Update State]
    Update --> Display[Display to User]
    Update --> Persist[Persist Session]

    style Cost fill:#ffe1e1
```

---

## Security & Sandbox

### Security Layers

```mermaid
graph TB
    Request[User Request] --> Perm[Permission Check]
    Perm --> PathCheck[Path Protection]
    PathCheck --> SandboxCheck[Sandbox Validation]

    PathCheck --> Protected[/.claude/**]
    PathCheck --> UserConfig[~/.claude/**]

    SandboxCheck --> Network[Network Init Wait]
    SandboxCheck --> Violations[Violation Store]
    SandboxCheck --> Stderr[Stderr Annotation]

    Perm --> PlanMode{Plan Mode?}
    PlanMode -->|Yes| UserApproval[Require User Approval]
    PlanMode -->|No| DefaultPerm[Default Permissions]

    UserApproval --> Approved{Approved?}
    Approved -->|Yes| Execute[Execute]
    Approved -->|No| Reject[Reject]

    DefaultPerm --> Execute

    Execute --> Monitor[Monitor Execution]
    Monitor --> ViolationDetect{Violation?}
    ViolationDetect -->|Yes| Block[Block & Log]
    ViolationDetect -->|No| Allow[Allow]

    style Protected fill:#ffe1e1
    style Block fill:#ffe1e1
```

### Sandbox Features

**Bash Tool Sandbox (Lines 138,676-145,389):**

1. **Network Initialization Gating**
   - `waitForNetworkInitialization()`
   - Prevents network access before ready

2. **Violation Tracking**
   - `getSandboxViolationStore()`
   - Logs all sandbox violations

3. **stderr Annotation**
   - `annotateStderrWithSandboxFailures()`
   - Adds context to error messages

4. **Debug Mode**
   - `SRT_DEBUG` environment variable
   - Detailed sandbox logging

### Path Protection

**Edit Tool (Lines 145,050-145,051):**

```javascript
j76 = "/.claude/**"     // System directory
M76 = "~/.claude/**"    // User configuration
```

**Protected operations:**
- Cannot edit files in `/.claude/` subdirectories
- Cannot modify user configuration in `~/.claude/`
- PDF files blocked from direct editing

### File Limits

**Read Tool (Lines 145,066-145,067):**

```javascript
YR1 = 2000  // Max lines per read
Gb5 = 2000  // Max chars per line
```

Prevents:
- Reading excessively large files
- Memory exhaustion attacks
- Performance degradation

---

## Plugin & Extension System

### Plugin Architecture

```mermaid
graph TB
    Plugins[Plugin System] --> LSP[LSP Integration]
    Plugins --> MCP[MCP Servers]
    Plugins --> Custom[Custom Tools]

    LSP --> LSPConfig[LSP Configuration]
    LSP --> LSPServers[LSP Server Manager]
    LSP --> LSPMessages[LSP Message Protocol]

    LSPConfig --> ServerDef[Server Definitions]
    LSPConfig --> LangMap[Language Mappings]

    LSPServers --> Start[Server Startup]
    LSPServers --> Monitor[Health Monitoring]
    LSPServers --> Restart[Auto-Restart]

    LSPMessages --> Requests[LSP Requests]
    LSPMessages --> Responses[LSP Responses]
    LSPMessages --> Notifications[LSP Notifications]

    MCP --> MCPProxy[MCP Proxy]
    MCP --> MCPServers[MCP Server List]
    MCP --> MCPTools[MCP Tool Invocation]

    MCPProxy --> Remote[mcp-proxy.anthropic.com]
    MCPTools --> ListRes[ListMcpResources]
    MCPTools --> ReadRes[ReadMcpResource]

    style LSP fill:#d1ecf1
    style MCP fill:#d4edda
```

### LSP Integration Details

**Configuration Schema (Lines 63,720-63,770):**

```typescript
{
  lspServers: {
    // Server configuration
    command: string,          // "typescript-language-server"
    args: string[],          // ["--stdio"]

    // Language mapping
    languageIds: {
      ".ts": "typescript",
      ".js": "javascript"
    },

    // Options
    initializationOptions: object,
    workspaceFolders: string[]
  }
}
```

**LSP Error Types (Lines 234,774-234,784):**

1. `lsp-config-invalid` - Invalid server configuration
2. `lsp-server-start-failed` - Server failed to start
3. `lsp-server-crashed` - Server crashed (signal or exit code)
4. `lsp-request-timeout` - Request timeout exceeded
5. `lsp-request-failed` - Request execution failed

**LSP Message Format (Line 334,583):**

```javascript
{
  isLSPMessage: true,
  type: messageType,
  message: content,
  timestamp: Date.now()
}
```

### MCP Integration

**MCP Proxy Configuration:**

```javascript
// Production
MCP_PROXY_URL: "https://mcp-proxy.anthropic.com"
MCP_PROXY_PATH: "/v1/mcp/{server_id}"

// Local
MCP_PROXY_URL: "http://localhost:8205"
MCP_PROXY_PATH: "/v1/toolbox/shttp/mcp/{server_id}"
```

**MCP Tools:**
- `ListMcpResourcesTool` (Line 356,552)
- `ReadMcpResourceTool` (Line 356,684)
- `Mcp` (generic invocation)

---

## Data Flow Diagrams

### Complete System Data Flow

```mermaid
flowchart TB
    User[User Input] --> CLI[CLI Parser]

    CLI --> Session[Session Manager]
    Session --> |restore| SessionDB[(Session DB)]

    Session --> Dispatch{Route Request}

    Dispatch --> |tool request| Tools[Tool System]
    Dispatch --> |agent spawn| Agents[Agent System]
    Dispatch --> |query| Query[Direct Query]

    Tools --> Validate[Input Validation]
    Validate --> |invalid| Error[Error Response]
    Validate --> |valid| Execute[Tool Execution]

    Execute --> FileOps[File Operations]
    Execute --> SearchOps[Search Operations]
    Execute --> ExecOps[Execution Operations]

    FileOps --> |read/write| FS[(File System)]
    SearchOps --> |pattern match| Ripgrep[Ripgrep Binary]
    ExecOps --> |bash| Sandbox[Sandbox Container]

    Tools --> Results[Tool Results]
    Agents --> Results
    Query --> Results

    Results --> Format[Format Response]
    Format --> API[Anthropic API Client]

    API --> |with tools| Messages[messages.create]
    Messages --> |streaming| Stream[SSE Stream]
    Stream --> Parse[Parse Response]

    Parse --> |tool use| Tools
    Parse --> |text| Display[Display to User]

    Display --> UI[Terminal UI]
    UI --> User

    Parse --> |track| CostTracker[Cost Tracker]
    CostTracker --> SessionDB

    style User fill:#e1f5ff
    style API fill:#f9f
    style Sandbox fill:#ffe1e1
    style SessionDB fill:#fff3cd
```

---

## Key Discoveries Summary

### 1. Ultrathink Trigger

**Line 258,662:**
```javascript
$g9 = /\bultrathink\b/gi;
```

This regex pattern triggers autonomous exploration mode when the keyword "ultrathink" is detected in user input.

### 2. All 21 Tools Mapped

Complete tool inventory with exact line numbers and implementation details documented.

### 3. In-Process Agent Architecture

Agents run within the same Node.js process as the main CLI, using:
- AbortControllers for cancellation
- Permission modes (plan vs default)
- Usage tracking (tokens, tool count)
- Message queues for communication

### 4. LSP Integration

**FINDING:** Claude Code does NOT use LSP or rust-analyzer for dependency graph generation.

**LSP Purpose:** Plugin system support only
- Allows plugins to integrate LSP servers
- Used for IDE-like features in plugins
- Not used for core code analysis

**Evidence:**
- LSP config in plugin schema (lines 63,720-63,770)
- LSP error handling for plugin servers
- No dependency graph or call graph LSP usage found

### 5. tree-sitter Usage

**FOUND:** tree-sitter WASM modules included
- `tree-sitter.wasm` (201KB)
- `tree-sitter-bash.wasm` (1.3MB)

**Purpose:** Likely for:
- Bash syntax parsing
- Code structure analysis
- NOT for dependency graphs

### 6. Ripgrep for Search

Grep tool built entirely on ripgrep native binary, not LSP.

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Runtime | Node.js 24.9.0+ |
| Bundler | Custom/esbuild |
| Module System | ES6 + CommonJS wrapper |
| UI Framework | Likely Ink.js (React for CLIs) |
| Search | Ripgrep (native binary) |
| Parsing | tree-sitter (WASM) |
| Graphics | resvg (WASM) |
| API Client | Custom Anthropic client |
| State Management | Custom implementation |
| Sandbox | Custom (Linux: bubblewrap) |

---

## Conclusion

Claude Code is a sophisticated CLI tool with:

1. **21 tools** for file operations, search, execution, and more
2. **In-process agent system** for spawning subagents
3. **Team coordination** with 1:1 Team-TaskList mapping
4. **Multi-layered security** with sandbox, path protection, and permission modes
5. **Plugin architecture** with LSP and MCP support
6. **Optimized search** via ripgrep, NOT LSP
7. **No dependency graph generation** via LSP or rust-analyzer

The system achieves code intelligence through:
- Ripgrep for fast text search
- tree-sitter for syntax parsing
- Direct file system operations
- NOT through language servers or static analysis tools

---

**Version:** 2.1.29
**Build:** 2026-01-31T20:12:07Z
**Package:** @anthropic-ai/claude-code
