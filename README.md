# JM Cyber

A personal **security lab that doubles as a CTF**. Deliberately-vulnerable
target apps live in `lab/`; the security tools we build to attack them
live in `tools/`. Each vulnerability hides a **flag** (`flag{...}`) you
capture by actually exploiting it.

> ⚠️ **Safety:** The apps here are *intentionally insecure*. They bind to
> `127.0.0.1` only and must **never** be exposed to the public internet.
> Only ever aim tools in this repo at this local lab — never at systems
> you don't own. See `AGENTS.md` for the full scope rules.

## Layout

```
lab/        intentionally-vulnerable targets (start here)
tools/      security tools we build and point at lab/ (coming next)
AGENTS.md   shared rules for AI agents + scope/safety (read first)
```

## Run the lab

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python lab/app.py
```

Then open http://127.0.0.1:5000 in a browser.

## Challenge 1 — "Front Door" (web / SQL injection)

The lab's login page trusts whatever you type a little too much. Get past
it **without** knowing a valid password, and the dashboard will hand you
your first flag.

- Goal: log in as `admin` without the password.
- Category: web exploitation (SQL injection).
- Flag format: `flag{...}`

(Once you've captured it by hand, we build a tool that does it for you —
then patch the login and watch the tool fail.)
