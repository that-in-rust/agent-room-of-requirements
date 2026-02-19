``` text
                                                                                                                                                                                                                                                                              
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                                                                                                                                                                                
                MINTO PYRAMID: WHY DROID IS LOVED 
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                            
                           ▲                      
                          ╱ ╲                                                                                     
                         ╱   ╲                                                                                                                                               
                        ╱DROID ╲                  
                       ╱ REMOVES╲                 
                      ╱THE MENTAL╲                                                                                                                                           
                     ╱   LOAD OF  ╲
                    ╱ DECOMPOSITION╲
                   ╱────────────────╲

    People don't love the TOOL. They love that it does
    the HARDEST PART of coding: breaking big into small.
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  THE CONTROL FLOW (from decompiled binary)

    Here's what ACTUALLY happens when you type:
    $ droid exec "refactor the auth system"


    ┌──────────────────────────────────────────────────────────┐
    │ PHASE 0: SESSION BOOTSTRAP                               │
    │                                                          │
    │  1. CLI parses args (clap v2)                            │
    │  2. Bun runtime boots (embedded JSC engine)              │
    │  3. React/Ink TUI initializes                            │
    │  4. Model selected (Claude by default, or --model X)     │
    │  5. Reasoning effort set (low/medium/high/off)           │
    │  6. Autonomy level set (--auto low|medium|high)          │
    │  7. Session created (UUID)                               │
    │  8. AGENTS.md loaded from repo root (if exists)          │
    │  9. .factory/droids/ loaded (custom droid configs)       │
    │ 10. .factory/skills/ indexed (available skills)          │
    └──────────┬───────────────────────────────────────────────┘
               │
               ▼
    ┌──────────────────────────────────────────────────────────┐
    │ PHASE 1: MODE DETECTION                                  │
    │                                                          │
    │  Is this a simple task or a complex mission?             │
    │                                                          │
    │  SIMPLE ("fix this typo"):                               │
    │    → Stay in SINGLE-AGENT mode                           │
    │    → Standard tool loop (same as Claude Code)            │
    │                                                          │
    │  COMPLEX ("refactor auth system"):                       │
    │    → Upgrade to ORCHESTRATOR mode ("AGI mode")           │
    │    → session.upgradeToOrchestratorSession()              │
    │    → Load orchestrator system prompt                     │
    │    → Enter MISSION PLANNING                              │
    │                                                          │
    │  The user can also toggle this with a key press.         │
    └──────────┬───────────────────────────────────────────────┘
               │
               ▼  (complex path — this is what people love)

    ┌──────────────────────────────────────────────────────────┐
    │ PHASE 2: MISSION PROPOSAL (the "SpecMode")               │
    │                                                          │
    │  Orchestrator LLM call with special system prompt:       │
    │                                                          │
    │  "You are an architect. You NEVER write implementation   │
    │   code yourself."                                        │
    │                                                          │
    │  "Echo back every requirement you've captured at least   │
    │   once to confirm understanding."                        │
    │                                                          │
    │  "Treat casual mentions ('oh and it should also...')     │
    │   with the same weight as formal requirements."          │
    │                                                          │
    │  LLM calls: propose-mission tool                         │
    │    input: {                                              │
    │      title: "Auth System Refactoring",                   │
    │      proposal: "Detailed markdown plan...",              │
    │      workingDirectory: "/path/to/project"                │
    │    }                                                     │
    │                                                          │
    │  User sees the proposal and approves/modifies it.        │
    │  On approval → missionDir created, mission.md written.   │
    └──────────┬───────────────────────────────────────────────┘
               │
               ▼

    ┌──────────────────────────────────────────────────────────┐
    │ PHASE 3: ARTIFACT CREATION (the "scaffolding")           │
    │                                                          │
    │  Before ANY code is written, orchestrator creates:       │
    │                                                          │
    │  missionDir/                                             │
    │  ├── mission.md            ← the "what" (requirements)   │
    │  └── user-facing-          ← every user interaction      │
    │      touchpoints.md           mapped: action → result    │
    │                               → edge case → error        │
    │                                                          │
    │  .factory/                                               │
    │  ├── services.yaml         ← THE source of truth for     │
    │  │                            commands, ports, services   │
    │  ├── skills/                                             │
    │  │   └── {worker-type}/    ← one SKILL.md per worker     │
    │  │       └── SKILL.md         type (YAML front matter    │
    │  │                            + procedure markdown)      │
    │  └── library/              ← shared state files          │
    │      └── *.md                 (perf-state, migration)    │
    │                                                          │
    │  AGENTS.md                 ← updated with project rules  │
    │                                                          │
    │  features.json             ← THE feature breakdown       │
    │    [                                                     │
    │      { id: "F1", desc: "Extract JWT...", skill: "..." }, │
    │      { id: "F2", desc: "Add refresh...", skill: "..." }, │
    │      { id: "F3", desc: "Write migration", skill: "..." }│
    │    ]                                                     │
    └──────────┬───────────────────────────────────────────────┘
               │
               ▼

    ┌──────────────────────────────────────────────────────────┐
    │ PHASE 4: WORKER DISPATCH (the "execution engine")        │
    │                                                          │
    │  Orchestrator calls: start-run tool                      │
    │                                                          │
    │  For each feature in features.json (status: "pending"):  │
    │                                                          │
    │  ┌────────────────────────────────────────────┐          │
    │  │ WORKER LIFECYCLE (per feature)              │          │
    │  │                                             │          │
    │  │  1. Spawn worker sub-session                │          │
    │  │     (new UUID, own conversation history)    │          │
    │  │                                             │          │
    │  │  2. Worker reads:                           │          │
    │  │     • mission.md (what's the project?)      │          │
    │  │     • AGENTS.md (what are the rules?)       │          │
    │  │     • .factory/services.yaml (how to run?)  │          │
    │  │     • features.json (what's MY feature?)    │          │
    │  │     • .factory/skills/{type}/SKILL.md       │          │
    │  │       (what's the procedure?)               │          │
    │  │                                             │          │
    │  │  3. Worker executes using tools:            │          │
    │  │     view_file, edit_file, shell, grep_tool  │          │
    │  │     (same tools as Claude Code)             │          │
    │  │                                             │          │
    │  │  4. Worker runs verification commands       │          │
    │  │                                             │          │
    │  │  5. Worker git commits                      │          │
    │  │                                             │          │
    │  │  6. Worker returns HANDOFF:                 │          │
    │  │     {                                       │          │
    │  │       featureId: "F1",                      │          │
    │  │       resultState: "pass" | "fail",         │          │
    │  │       whatWasImplemented: "...",             │          │
    │  │       whatWasLeftUndone: "...",              │          │
    │  │       verification: { cmds, results },      │          │
    │  │       tests: { written, updated },          │          │
    │  │       discoveredIssues: [...],              │          │
    │  │       commitId: "abc123"                    │          │
    │  │     }                                       │          │
    │  └────────────────────────────────────────────┘          │
    │                                                          │
    │  Each handoff written to per-worker JSON file.           │
    │  Orchestrator gets: workerHandoffs array + nextAction.   │
    └──────────┬───────────────────────────────────────────────┘
               │
               ▼

    ┌──────────────────────────────────────────────────────────┐
    │ PHASE 5: ORCHESTRATOR REVIEW LOOP                        │
    │                                                          │
    │  nextAction = "continue" | "orchestrator" | "completed"  │
    │                                                          │
    │  "continue"     → dispatch next pending feature          │
    │  "orchestrator" → worker needs help, return to orch      │
    │  "completed"    → all features done, report to user      │
    │                                                          │
    │  On "fail" handoff:                                      │
    │    Orchestrator reads the discoveredIssues,              │
    │    may create new features, retry, or escalate.          │
    │                                                          │
    │  On scope change (user says "oh also add X"):            │
    │    Orchestrator updates mission.md,                      │
    │    user-facing-touchpoints.md,                           │
    │    features.json — adds new features.                    │
    │    "Never remove completed or cancelled features —       │
    │     they serve as history."                              │
    │                                                          │
    │  CRITICAL RULE from system prompt:                       │
    │    "You are an architect. You NEVER write code."         │
    │    "Your job is to manage WHAT gets built."              │
    │    "Workers build."                                      │
    └──────────┬───────────────────────────────────────────────┘
               │
               ▼
             DONE

  THE DATA FLOW (what travels between layers)

    ┌─────────┐     prompt      ┌──────────────┐
    │  USER   │ ──────────────→ │ ORCHESTRATOR  │
    │         │ ←────────────── │  (LLM call)   │
    │         │   proposal       │              │
    │         │                  │  reads:      │
    │ approves│                  │  AGENTS.md   │
    │         │                  │  .factory/   │
    └─────────┘                  └──────┬───────┘
                                        │
                                 mission.md
                                 features.json
                                 services.yaml
                                 skills/*.md
                                 touchpoints.md
                                        │
                      ┌─────────────────┼─────────────────┐
                      ▼                 ▼                  ▼
               ┌───────────┐    ┌───────────┐     ┌───────────┐
               │ WORKER 1  │    │ WORKER 2  │     │ WORKER 3  │
               │           │    │           │     │           │
               │ reads:    │    │ reads:    │     │ reads:    │
               │ mission.md│    │ mission.md│     │ mission.md│
               │ SKILL.md  │    │ SKILL.md  │     │ SKILL.md  │
               │ services  │    │ services  │     │ services  │
               │           │    │           │     │           │
               │ uses:     │    │ uses:     │     │ uses:     │
               │ view_file │    │ grep_tool │     │ shell     │
               │ edit_file │    │ edit_file │     │ edit_file │
               │ shell     │    │ shell     │     │ view_file │
               │           │    │           │     │           │
               │ outputs:  │    │ outputs:  │     │ outputs:  │
               │ git commit│    │ git commit│     │ git commit│
               │ handoff{} │    │ handoff{} │     │ handoff{} │
               └─────┬─────┘    └─────┬─────┘     └─────┬─────┘
                     │                │                   │
                     └────────────────┼───────────────────┘
                                      │
                                      ▼
                             ┌────────────────┐
                             │  ORCHESTRATOR  │
                             │  reviews all   │
                             │  handoffs      │
                             │                │
                             │  nextAction?   │
                             │  ├── continue  │
                             │  ├── retry F3  │
                             │  └── completed │
                             └────────┬───────┘
                                      │
                                      ▼
                              ┌──────────────┐
                              │    USER      │
                              │  sees final  │
                              │  result      │
                              └──────────────┘

  THE RISK ASSESSMENT FLOW (from decompiled Zod schemas)

    Every shell command goes through risk assessment:

    Worker wants to run: "rm -rf node_modules && npm install"

    ┌─────────────────────────────────────────────────────┐
    │ TOOL INPUT (from LLM)                               │
    │                                                     │
    │ {                                                   │
    │   command: "rm -rf node_modules && npm install",    │
    │   cwd: "/absolute/path/to/project",   ← REQUIRED   │
    │   riskLevel: {                         ← REQUIRED   │
    │     value: "medium",                                │
    │     reason: "Deletes local deps but can be          │
    │              restored with npm install"             │
    │   },                                                │
    │   timeout: 30000,                                   │
    │   ignoreTimeout: true  ← for long installs          │
    │ }                                                   │
    └────────────────────┬────────────────────────────────┘
                         │
                         ▼
    ┌─────────────────────────────────────────────────────┐
    │ RISK GATE                                           │
    │                                                     │
    │  LOW:    "git status", "cat file", "ls"             │
    │          → auto-approve (if autonomy allows)        │
    │                                                     │
    │  MEDIUM: "git commit", "npm install"                │
    │          → auto-approve at medium+ autonomy         │
    │          → ask user at low autonomy                 │
    │                                                     │
    │  HIGH:   "git push --force", "curl | bash",         │
    │          "rm -rf /"                                 │
    │          → ALWAYS ask user (unless --skip-unsafe)   │
    │                                                     │
    │  Examples from binary:                              │
    │  "curl | bash executes untrusted code" → HIGH      │
    │  "git commit changes working tree" → MEDIUM        │
    │  "git push --force overwrites remote" → HIGH       │
    └─────────────────────────────────────────────────────┘

  THE STOP CONDITIONS (from embedded orchestrator prompt)

    ┌─────────────────────────────────────────────────────┐
    │ WHEN DROID STOPS AND ASKS THE HUMAN                 │
    │ (from decompiled system prompt)                     │
    │                                                     │
    │  1. Human action required                           │
    │     "approve a purchase, authenticate with          │
    │      third-party, physically connect hardware"      │
    │                                                     │
    │  2. Decision requires human judgment                │
    │     "security decisions, significant architectural  │
    │      trade-offs, business implications"             │
    │                                                     │
    │  3. Unrestorable external dependency                │
    │     "service down, credentials expired, missing     │
    │      environment" — but NOT retry-able things       │
    │                                                     │
    │  4. Requirements need clarification                 │
    │     "ambiguity or conflicts that can't be resolved  │
    │      from existing context"                         │
    │                                                     │
    │  5. Scope significantly exceeds agreement           │
    │     "work required is substantially larger than     │
    │      proposed and accepted"                         │
    │                                                     │
    │  6. Mission boundaries need to change               │
    │     "cannot proceed without violating agreed-upon   │
    │      boundaries (ports, resources, off-limits)"     │
    └─────────────────────────────────────────────────────┘

  WHY PEOPLE LOVE IT (predicted from control flow + data flow)

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    REASON 1: IT DOES THE HARD PART
    ════════════════════════════════

    The hardest part of coding isn't writing code.
    It's DECOMPOSING a vague request into concrete steps.

    What a developer does:                 What Droid does:
    ─────────────────────                  ─────────────────
    "Refactor auth"                        "Refactor auth"
         │                                      │
         ▼                                      ▼
    Stare at screen 20 min                 Propose mission:
    thinking "where do I start?"           F1: Extract JWT logic
                                           F2: Add refresh tokens
         │                                 F3: Write migration
         ▼                                 F4: Update tests
    Open 12 files trying to                F5: Update API docs
    understand the codebase
                                                │
         │                                      ▼
         ▼                                 "Do you approve?"
    Start coding F1, discover                   │
    you needed F3 first                         ▼
                                           Execute F1..F5 in order
         │                                 with git commits
         ▼
    3 hours later, partial work


    DROID REMOVES THE DECOMPOSITION TAX.
    That's 60% of the cognitive load of coding.

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    REASON 2: THE ARTIFACT SYSTEM BUILDS TRUST
    ═══════════════════════════════════════════

    Before writing ONE line of code, Droid creates:

    ┌──────────────────────┐
    │ mission.md           │ ← "here's what I understood"
    │                      │    USER CAN VERIFY
    ├──────────────────────┤
    │ user-facing-         │ ← "here's every user interaction
    │ touchpoints.md       │    including edge cases"
    │                      │    USER CAN VERIFY
    ├──────────────────────┤
    │ features.json        │ ← "here's my task breakdown"
    │                      │    USER CAN VERIFY
    ├──────────────────────┤
    │ services.yaml        │ ← "here's how I'll run things"
    │                      │    USER CAN VERIFY
    ├──────────────────────┤
    │ skills/*.md          │ ← "here's the procedure I'll follow"
    │                      │    USER CAN VERIFY
    └──────────────────────┘

    Every artifact is a CHECKPOINT where the user can say
    "no, that's wrong" BEFORE any code is written.

    Claude Code: starts coding immediately, you see it go.
    Droid:       shows you the blueprint, waits for your OK.

    This is why people trust it with bigger tasks.

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    REASON 3: STRUCTURED HANDOFFS MAKE PROGRESS VISIBLE
    ═══════════════════════════════════════════════════

    Each worker returns:

    {
      featureId: "F1",
      resultState: "pass",               ← did it work?
      whatWasImplemented: "Extracted      ← what was done
        JWT validation into standalone
        module with 3 exported functions",
      whatWasLeftUndone: "",              ← what's missing
      verification: {
        commands: ["cargo test"],         ← proof it works
        results: ["42 passed, 0 failed"]
      },
      tests: {
        written: ["test_jwt_decode"],     ← new tests
        updated: ["test_auth_flow"]       ← modified tests
      },
      discoveredIssues: [],               ← surprises
      commitId: "a1b2c3d"                ← git proof
    }

    Compare to Claude Code:
      "I've made the changes. Let me know if you
       need anything else."   ← WHAT changes? Prove it.

    Droid gives you a RECEIPT for every unit of work.
    You can audit it. You can reject it. You can retry it.

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    REASON 4: THE ORCHESTRATOR NEVER CODES
    ═══════════════════════════════════════

    From the decompiled system prompt:

    "You are an architect. You NEVER write implementation
     code yourself."

    "When a user asks you to fix, build, or change:
     1. Update mission.md
     2. Decompose into features
     3. Update AGENTS.md
     4. Call start_mission_run to let workers implement
     Your job is to manage WHAT. Workers build."

    This is a SEPARATION OF CONCERNS in the agent itself:

    ┌─────────────────┐
    │  ORCHESTRATOR   │  Thinks in: requirements, features,
    │  (architect)    │  scope, priorities, tradeoffs
    │                 │  Tools: propose-mission, start-run
    │  NEVER codes    │  Never: edit_file, create_file
    └────────┬────────┘
             │ delegates
             ▼
    ┌─────────────────┐
    │  WORKER         │  Thinks in: code, tests, commands
    │  (implementer)  │  Tools: edit_file, shell, grep_tool
    │                 │  Never: propose-mission, start-run
    │  ONLY codes     │
    └─────────────────┘

    Why this works:
    - Architects that code get lost in details
    - Coders that architect lose sight of the goal
    - Splitting them means each session's context window
      is FOCUSED on one concern

    This is why Droid handles bigger tasks than Claude Code.
    Claude Code is one brain doing both. Droid is TWO brains.

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    REASON 5: CASUAL REQUIREMENTS ARE TREATED SERIOUSLY
    ═══════════════════════════════════════════════════

    From the decompiled orchestrator prompt:

    "Treat casual mentions ('oh and it should also...')
     with the same weight as formal requirements."

    "Echo back every requirement you've captured at least
     once to confirm understanding."

    This means:

    User: "oh and make sure it works on mobile"
                      │
                      ▼
    Droid: updates mission.md, adds feature to features.json,
           creates touchpoint in user-facing-touchpoints.md

    vs

    Claude Code: "Sure, I'll keep that in mind."
                 (probably forgets by turn 15)

    Droid PERSISTS every requirement to DISK FILES.
    Mission.md and touchpoints.md are the memory.
    Workers read them. Nothing gets lost.

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    REASON 6: RISK-AWARE TOOL EXECUTION
    ════════════════════════════════════

    Every shell command MUST include a risk assessment:

    LLM is FORCED by Zod schema to output:
    {
      command: "git push --force origin main",
      cwd: "/absolute/path",           ← must be absolute
      riskLevel: {
        value: "high",                 ← low/medium/high
        reason: "Force push can        ← must explain why
                 overwrite remote
                 repository history"
      }
    }

    The LLM can't just run commands. It must REASON about
    the risk of each command, in writing, before executing.

    LOW:    auto-approve → user sees nothing
    MEDIUM: auto-approve at medium+ autonomy
    HIGH:   ALWAYS pauses for human approval

    This is why people trust it with `--auto high`.
    The risk classification means HIGH autonomy still has
    guardrails for destructive operations.

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    SUMMARY: THE 6 REASONS MAPPED TO CONTROL FLOW
    ═══════════════════════════════════════════════

    Phase 0-1 (Bootstrap + Mode Detection)
      → REASON 4: Splits architect from implementer
      → REASON 6: Risk level set before any tool runs

    Phase 2 (Mission Proposal)
      → REASON 1: Does the decomposition FOR you
      → REASON 5: Captures every casual requirement

    Phase 3 (Artifact Creation)
      → REASON 2: All artifacts are human-verifiable
      → REASON 5: Requirements persisted to disk

    Phase 4 (Worker Dispatch)
      → REASON 3: Structured handoffs with proof
      → REASON 6: Every command risk-assessed

    Phase 5 (Review Loop)
      → REASON 1: Retries/redecomposes on failure
      → REASON 3: Handoff receipts for every feature


    THE META-INSIGHT:
    ─────────────────
    Droid is loved because it turns VAGUE INTENT into
    AUDITABLE ARTIFACTS before writing code. The user
    feels IN CONTROL even though the agent is autonomous.

    It's not about the tools (same as Claude Code).
    It's not about the model (BYOK, any model works).
    It's the ORCHESTRATION PROTOCOL:
      propose → verify → decompose → execute → prove

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```