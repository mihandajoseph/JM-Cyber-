# JM Cyber

A hands-on cybersecurity lab, built from scratch to learn by doing.

The lab follows the full security lifecycle, in this order:

1. **Build** an isolated lab network of virtual machines, secure by design
2. **Secure** it: threat model, hardening, verification
3. **Monitor** it: central logging and detection rules
4. **Test** it: attack it from inside the lab and check what was detected
5. **Forensics**: investigate a compromise and build a timeline
6. **Threat intel**: map attacks to MITRE ATT&CK and write intel reports

## Safety

Everything here runs only inside an isolated lab on systems I own.
Nothing in this repo is aimed at any outside system. See `AGENTS.md` for
the full scope and safety rules.

## Repo layout

- `AGENTS.md`: rules for every AI agent working in this repo
- `CLAUDE.md`: Claude's instructions, pointing to `AGENTS.md`
- `.gitignore`: files Git must never track, including secrets
