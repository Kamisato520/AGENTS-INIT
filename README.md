<div align="center">

# AGENTS-INIT

**Inject OpenAI GPT-6 Astra prompting guidance into a project's `AGENTS.md` at initialization time.**

[English](README.md) · [简体中文](README.zh-CN.md)

</div>

AGENTS-INIT is a small Codex skill designed to run immediately after native `/init`. Codex creates the repository-specific `AGENTS.md`; AGENTS-INIT then adds a compact managed block derived from the current [OpenAI Model Guidance for GPT-6 Astra](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra#gpt-6-astra-personality-and-writing-style).

It focuses only on the model behaviors that are useful as project-level agent instructions: initiative and follow-through, instruction priority, writing style, and proportional testing and verification.

## Install

```bash
npx skills add Kamisato520/AGENTS-INIT
```

Codex-only global install:

```bash
npx skills add Kamisato520/AGENTS-INIT --global --agent codex --skill agent-init --yes --copy
```

## Use with native `/init`

For a new repository:

```text
/init
$agent-init
```

`/init` remains responsible for discovering the repository and creating project-specific instructions. `$agent-init` only creates or refreshes the block between:

```text
<!-- AGENT-INIT:START -->
...
<!-- AGENT-INIT:END -->
```

Running `$agent-init` again updates that block without duplicating it or overwriting the rest of `AGENTS.md`.

## Why this exists

OpenAI's Astra guidance notes that the model can be especially sensitive to instructions found in skills and files such as `AGENTS.md`. It recommends making instruction priority explicit and tuning initiative, writing style, and testing behavior for the workflow.

One of the official prompt recommendations is:

> “The user's instructions take precedence over guidelines provided in a skill.”

AGENTS-INIT packages the relevant guidance into a small project-level block instead of consuming global prompt context.

## OpenAI guidance

The images below are live screenshots of the official OpenAI documentation, rendered from the linked public page.

### Astra behavior and `AGENTS.md`

[![OpenAI GPT-6 Astra behavior guidance](https://image.thum.io/get/width/1200/crop/900/noanimate/?url=https%3A%2F%2Fdevelopers.openai.com%2Fapi%2Fdocs%2Fguides%2Flatest-model%3Fmodel%3Dgpt-6-astra%23gpt-6-astra-behavior)](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra#gpt-6-astra-behavior)

### Personality and writing style

[![OpenAI GPT-6 Astra personality and writing style guidance](https://image.thum.io/get/width/1200/crop/900/noanimate/?url=https%3A%2F%2Fdevelopers.openai.com%2Fapi%2Fdocs%2Fguides%2Flatest-model%3Fmodel%3Dgpt-6-astra%23gpt-6-astra-personality-and-writing-style)](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra#gpt-6-astra-personality-and-writing-style)

Source: [OpenAI Model Guidance — GPT-6 Astra](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra)

## Install by prompt

You can also give Codex this prompt:

```text
Install the agent-init skill from Kamisato520/AGENTS-INIT with the skills CLI for Codex. Verify the installation. For this repository, run native /init first, then use $agent-init to add the OpenAI Astra guidance to AGENTS.md while preserving the repository-specific instructions.
```

## What AGENT-INIT adds

The managed block stays intentionally small. It covers:

- carrying an authorized task through to completion when the scope is clear;
- keeping explicit user instructions above general skill guidance;
- using clear, concise technical language with the main point early;
- keeping testing and verification proportional to the change.

The wording stays close to the intent of OpenAI's published prompts while remaining compact enough for a project-level instruction file.

## Repository layout

```text
agent-init/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── astra.md
└── scripts/
    └── apply_agent_init.py
```

## Attribution

AGENTS-INIT is an independent community project and is not affiliated with or endorsed by OpenAI. The linked guidance and screenshots are sourced from the public OpenAI developer documentation. GPT-6 Astra, Codex, and OpenAI are product names or trademarks of OpenAI.
