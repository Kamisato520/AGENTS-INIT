---
name: agent-init
description: Add or refresh a compact GPT-6 Astra aligned behavior section in a project's AGENTS.md. Use immediately after Codex /init, when setting up a repository, or when the user asks to initialize AGENTS.md with current OpenAI model guidance. Preserve all repository-specific instructions outside the managed AGENT-INIT block.
---

# AGENT-INIT

Use this skill immediately after native Codex `/init` to add a compact behavior section to the generated `AGENTS.md`.

The purpose is narrow: incorporate the current OpenAI GPT-6 Astra guidance on initiative, instruction following, writing style, and proportional verification into the project's initial agent instructions.

## Workflow

1. Prefer native Codex `/init` first so repository-specific commands and conventions are generated normally.
2. Locate the project-root `AGENTS.md`.
3. Run `scripts/apply_agent_init.py --file AGENTS.md` from this skill directory.
4. Read the final `AGENTS.md` and remove only direct conflicts or duplicate wording inside the managed block.

If `AGENTS.md` does not exist, create it only when the user explicitly asked AGENT-INIT to initialize the file without `/init`:

```bash
python scripts/apply_agent_init.py --file AGENTS.md --create
```

## Rules

- Preserve all content outside `AGENT-INIT:START` and `AGENT-INIT:END`.
- Never duplicate the managed block.
- Do not add project-specific research, testing, deployment, or coding policy unless `/init`, the repository, or the user already established it.
- Keep the managed block short because Astra is sensitive to instructions in `AGENTS.md` and skills.
- The user's explicit instructions override this skill's general guidance.
- Use the official OpenAI model guidance linked in `assets/astra.md` as the source of truth when reviewing this skill.
