# Strata Kits

Use `describe_kit` for the live source of truth. This file captures the observed Strata 0.9.0 grammar so agents do not have to rediscover it every time.

## Kit Selection

| Kit | Use |
|---|---|
| `user_flow` | UI navigation, product journeys, branch points, E2E smoke-test flows. |
| `discovery_tree` | Outcomes, nested tasks, dependency trees, backlog planning. |
| `freeform` | Raw D2 for architecture, systems, data flow, state machines, ownership maps. |

## `user_flow`

Purpose: model UI navigation and branching logic as a flow you can build and test against.

Syntax:

```d2
@direction down

start open: Open app

screen home: Home
  action create: Click create
  decision has_data: Has required data?

system save: Save draft
end done success: Draft created
end blocked error: Missing data

open -> home
home -> create
create -> has_data
has_data -> save: yes
has_data -> blocked: no
save -> done
```

Node types:

| Token | Meaning |
|---|---|
| `start` | Entry point, often from an email, deep link, browser, or command. |
| `screen` | Full page or screen. Can contain indented actions/decisions. |
| `surface` | Region within a screen, such as a modal, panel, or dialog. |
| `action` | User action. Usually indented under a screen or surface. |
| `decision` | Branch point. Label outgoing edges with answers. |
| `system` | Backend/system step with no UI. |
| `connector` | Junction to merge or split flow without a UI node. |
| `end` | Terminal outcome. Add `success`, `drop-off`, or `error`; default is success. |

Directives:

- `@direction down | left | right | up` as the first line. Default is down.
- `@status { <path>: building | verified }` to highlight progress. Paths not listed are backlog.

Authoring rules:

- Use one node per line: `<type> <id>: <label>`.
- Keep IDs short and unique; edges and status paths reference IDs.
- Put edges on their own lines: `from -> to: optional label`.
- Use `#` comments for notes.
- Validate before create/update.

## `discovery_tree`

Purpose: break work into outcomes and nested tasks.

Syntax:

```d2
# Top-level bullets are outcomes. Nested bullets are tasks.
- Replace MoEngage transactional email
  - done: Prove org invite email via Resend ^org-invite
  - doing: Improve email copy
  - Build durable outbox blocked-by ^org-invite
```

Rules:

- One item per line: `<indent>- [status:] label [^handle] [blocked-by ^id]`.
- Top-level bullets are outcomes and should not carry status.
- Indent by two spaces for tasks and subtasks.
- Supported task statuses: default todo, `doing:`, `done:`.
- Parent tasks derive status from children; avoid explicit status on parents with children.
- Use `^handle` for dependency anchors and `blocked-by ^id` for blocked tasks.
- Use `#` for comments.

## `freeform`

Purpose: draw anything in raw D2.

Use it for architecture and codebase maps when Strata should preserve a visual spec, but use Clarity or codebase-memory first for code discovery.

Example:

```d2
direction: right

gateway: dashtoon-gateway
email_port: TransactionalEmailSender
adapter: ResendEmailAdapter
provider: Resend API

gateway -> email_port: EmailIntent
email_port -> adapter: send()
adapter -> provider: HTTPS
```

Freeform is raw D2. If syntax fails, run Strata `validate_diagram` and use the returned line/column log to fix it.
