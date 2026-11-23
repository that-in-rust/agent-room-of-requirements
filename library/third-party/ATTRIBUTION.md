# Third-party skills: attribution

Skills in this folder were written by other people. They are kept word for word, each
project in its own directory with its licence file. Only projects under the MIT licence are
kept this way. Everything else is listed below as a link, and the ideas this library took
from it are restated in the library's own skills.

## Kept verbatim

| Directory | Project | Source | Licence |
|---|---|---|---|
| `superpowers/` | Superpowers, by Jesse Vincent | <https://github.com/obra/superpowers> (`skills/`) | MIT, see `superpowers/LICENSE` |
| `stripe/` | Stripe agent skills, by Stripe | <https://github.com/stripe/ai> (`skills/stripe-best-practices`) | MIT, see `stripe/LICENSE` |

The 14 Superpowers skills kept: `brainstorming`, `dispatching-parallel-agents`,
`executing-plans`, `finishing-a-development-branch`, `receiving-code-review`,
`requesting-code-review`, `subagent-driven-development`, `systematic-debugging`,
`test-driven-development`, `using-git-worktrees`, `using-superpowers`,
`verification-before-completion`, `writing-plans`, `writing-skills`.

The copies were taken in 2026 and are not updated automatically. The Stripe skill upstream
has changed since the copy was taken; read the source for the current version.

## Linked, not copied

These were once copied into this repository. They are not MIT-licensed or their licence was
not confirmed, so the copies were removed.

| Material | Source | Licence | Where its ideas are used here |
|---|---|---|---|
| Claude Code plugins `plugin-dev` (agent, command, hook, MCP, settings, structure and skill development), `hookify`, `example-plugin`, `claude-code-setup` | <https://github.com/anthropics/claude-plugins-official/tree/main/plugins> | Apache-2.0 | `library/skills/claude-plugin-development` |
| Claude Code plugins `skill-creator` and `plugin-dev/skill-development` | same repository | Apache-2.0 | `library/skills/authoring-skills-and-references` |
| Claude Code plugin `claude-md-management` | same repository | Apache-2.0 | `library/skills/agent-context-and-orchestration` |
| Claude Code plugins `frontend-design`, `playground` | same repository | Apache-2.0 | `library/skills/react-frontend`, `library/skills/visual-explainers` |
| OpenAI Codex system skills `imagegen`, `openai-docs`, `plugin-creator`, `skill-creator`, `skill-installer` | <https://github.com/openai/skills/tree/main/skills/.system> | not confirmed | `generative-art-and-images`, `agent-context-and-orchestration`, `claude-plugin-development`, `authoring-skills-and-references` |
| `agent-debate` protocol | <https://github.com/gumbel-ai/agent-debate> | none published | `library/skills/explore-and-decide` (the link between the earlier local skill and this project was not confirmed) |
| Hermes `local-vision-ollama` skill | source not known | none found | `library/skills/generative-art-and-images` |
