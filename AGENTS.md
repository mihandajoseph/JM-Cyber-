# JM Cyber — Agent Guide

This file is the shared brain for every AI agent working in this repo
(Codex reads `AGENTS.md`, Claude reads `CLAUDE.md` which points here).
Read it before doing anything. Scope and safety rules below are binding.

## What this project is

JM Cyber is a **personal security lab that doubles as a CTF**. It is a
deliberately-vulnerable environment the owner builds to learn offensive
and defensive security by pointing self-built tools at it.

Two halves live here as they grow:

- **`lab/`** — intentionally-vulnerable target apps. Each weakness hides a
  **flag** (`flag{...}`) you can only reach by actually exploiting it.
- **`tools/`** — the security tools we build (recon, scanners, exploit
  scripts) and aim at `lab/`. (Created as we go.)

The learning loop: build a vulnerable target → build a tool → run the
tool at the target → capture the flag → patch the target → confirm the
tool goes quiet.

## Scope — read this before touching anything

This is the discipline a real engagement runs on, practiced where the
stakes are zero. **It is not optional.**

- **Allowed target: `localhost` / `127.0.0.1` only.** Every tool in this
  repo points at the local lab and nothing else.
- **Never** run any tool in this repo against a host, IP, domain, or
  network the owner does not own. No "quick tests" against real sites.
- The lab apps are **deliberately insecure**. They bind to `127.0.0.1`
  only and must **never** be exposed to the public internet. If the lab
  is ever opened to other trainees, it runs on an isolated/local network
  or VPN — never a public server.
- No real credentials, real personal data, or secrets ever go in this
  repo. Flags and seed data are fake by design.

If a task would require acting outside this scope, **stop and ask the
owner** instead of doing it.

## Stack

- **Python 3** throughout — target apps and tools, one language to learn.
- **Flask + SQLite** for lab web apps. Runs at `http://127.0.0.1:5000`.
- Dependencies pinned in `requirements.txt`. Use a local virtualenv
  (`.venv/`, git-ignored).

## How the two agents work together

Claude and Codex both edit this repo on disk. The repo + git is the only
shared channel — neither agent can see the other's chat.

- **Never edit the same file at the same time.** Work on separate
  branches, one feature each.
- Branch naming: `claude/<feature>` and `codex/<feature>`.
- Flow: build on a branch → push → the *other* agent reviews the diff on
  GitHub → reconcile → merge to `main` via PR.
- Keep changes small enough to review in one sitting.

## Conventions

- In the **lab** apps, comments explaining a *planted* vulnerability are
  wanted — mark them clearly, e.g. `# VULN: ...`. This is teaching code;
  the vulnerability is the point.
- In the **tools**, write normal secure code. Explain *why*, not *what*.
- Keep the first version of anything minimal. Add complexity only when a
  tool we're building needs it.
