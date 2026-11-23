# Repository rules

These rules apply to people and agents changing **this library**. They are not instructions to install in a client repository.

## Git Rules — MANDATORY

### NEVER push without explicit permission

- Do NOT run `git push` unless the user explicitly says "push"
- Always ask before pushing

### NEVER reference external issue numbers in commit messages

- This repo's commits show up as cross-references on GitHub issues
- Commit messages must NEVER contain patterns like `org/repo#123`, `apache/iggy#2739`, or bare `#123`
- Strip all issue number references from commit messages
- Put issue references inside file content only, never in commit messages
- BAD: `Add deep analysis for MongoDB connector (apache/iggy#2739)`
- GOOD: `Add MongoDB connector deep analysis for iggy`
