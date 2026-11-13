# CLAUDE.md

Claude's working notes for JM Cyber. **`AGENTS.md` is the source of
truth** for project purpose, scope, safety rules, stack, and the
two-agent workflow — read it first and follow it. This file only adds
Claude-specific reminders.

## Reminders

- Scope is `localhost` only. Lab apps are deliberately vulnerable and
  bind to `127.0.0.1`. Never expose them; never aim tools off-box.
- Work on `claude/<feature>` branches and push for Codex to review on
  GitHub. Don't edit a file Codex is currently working.
- Lab code: planted vulns are intentional — flag them with `# VULN:`.
  Tool code: write it securely.
- Teaching context: explain the *why* as we build, keep each step small
  and reviewable.
