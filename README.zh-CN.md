<div align="center">

# AGENTS-INIT

**在项目初始化时，把 OpenAI GPT-6 Astra 的提示词建议加入项目级 `AGENTS.md`。**

[English](README.md) · [简体中文](README.zh-CN.md)

</div>

AGENTS-INIT 是一个轻量级 Codex skill，设计为紧接原生 `/init` 使用。Codex 先生成与仓库相关的 `AGENTS.md`，随后 AGENTS-INIT 根据当前的 [OpenAI GPT-6 Astra 模型指引](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra#gpt-6-astra-personality-and-writing-style) 加入一个紧凑、可重复更新的托管区块。

它只处理适合放进项目级 agent 指令的部分：主动执行与持续完成、指令优先级、表达风格，以及与改动规模相匹配的测试和验证。

## 安装

```bash
npx skills add Kamisato520/AGENTS-INIT
```

仅为 Codex 全局安装：

```bash
npx skills add Kamisato520/AGENTS-INIT --global --agent codex --skill agent-init --yes --copy
```

## 与原生 `/init` 配合使用

新项目中执行：

```text
/init
$agent-init
```

`/init` 继续负责识别仓库结构并生成项目本身需要的说明。`$agent-init` 只创建或刷新下面两个标记之间的内容：

```text
<!-- AGENT-INIT:START -->
...
<!-- AGENT-INIT:END -->
```

再次运行 `$agent-init` 时，只会更新这一托管区块，不会重复插入，也不会覆盖 `AGENTS.md` 的其他内容。

## 为什么需要它

OpenAI 的 Astra 指引指出，模型对 skill 和 `AGENTS.md` 等文件中的指令会更敏感，因此这类项目级指令应当清晰、容易审计。官方同时建议根据实际工作流调整主动执行、指令优先级、写作风格以及测试强度。

其中一条官方提示词建议是：

> “The user's instructions take precedence over guidelines provided in a skill.”

AGENTS-INIT 把这些与项目初始化直接相关的建议集中到一个小型 `AGENTS.md` 区块中，避免长期占用全局 prompt 上下文。

## OpenAI 官方指引

下面两张图是从 OpenAI 官方公开文档实时渲染的网页截图，点击图片可直接打开对应章节。

### Astra 行为与 `AGENTS.md`

[![OpenAI GPT-6 Astra behavior guidance](https://image.thum.io/get/width/1200/crop/900/noanimate/?url=https%3A%2F%2Fdevelopers.openai.com%2Fapi%2Fdocs%2Fguides%2Flatest-model%3Fmodel%3Dgpt-6-astra%23gpt-6-astra-behavior)](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra#gpt-6-astra-behavior)

### Personality and writing style

[![OpenAI GPT-6 Astra personality and writing style guidance](https://image.thum.io/get/width/1200/crop/900/noanimate/?url=https%3A%2F%2Fdevelopers.openai.com%2Fapi%2Fdocs%2Fguides%2Flatest-model%3Fmodel%3Dgpt-6-astra%23gpt-6-astra-personality-and-writing-style)](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra#gpt-6-astra-personality-and-writing-style)

来源：[OpenAI Model Guidance — GPT-6 Astra](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra)

## 通过 Prompt 安装

也可以直接把下面这段交给 Codex：

```text
Install the agent-init skill from Kamisato520/AGENTS-INIT with the skills CLI for Codex. Verify the installation. For this repository, run native /init first, then use $agent-init to add the OpenAI Astra guidance to AGENTS.md while preserving the repository-specific instructions.
```

## AGENT-INIT 会加入什么

托管区块会尽量保持紧凑，主要包含：

- 在范围明确时，把已经授权的任务持续执行到完成；
- 让用户的明确指令优先于 skill 的一般性建议；
- 使用清晰、简洁的技术表达，并尽早说明核心结论；
- 根据改动规模控制测试和验证强度。

具体措辞尽量贴近 OpenAI 已发布提示词的意图，同时控制长度，使其适合作为项目级 `AGENTS.md` 指令。

## 仓库结构

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

## 归属说明

AGENTS-INIT 是独立的社区项目，与 OpenAI 不存在官方隶属或背书关系。文中链接的模型指引与网页截图均来自 OpenAI 公开开发者文档。GPT-6 Astra、Codex 与 OpenAI 为 OpenAI 的产品名称或商标。
