# agent-resources

A collection of reusable Claude Code skills, slash commands, and subagents. Install them in any project using [skill-add](https://github.com/kasperjunge/skill-add).

## What's Included

This repository demonstrates the three main ways to extend Claude Code:

| Type | Location | Invocation | Best For |
|------|----------|------------|----------|
| **Skills** | `.claude/skills/` | Automatic (context-based) | Complex workflows with multiple files |
| **Slash Commands** | `.claude/commands/` | Manual (`/command-name`) | Frequently used prompts |
| **Subagents** | `.claude/agents/` | Automatic or explicit | Specialized tasks with own context |

## Available Extensions

### Skills

| Skill | Description |
|-------|-------------|
| `hello-world` | Example skill demonstrating skill structure |
| `frontend-design` | Create distinctive, production-grade frontend interfaces |

### Slash Commands

| Command | Description |
|---------|-------------|
| `/hello-world` | Example command that greets the user |

### Subagents

| Agent | Description |
|-------|-------------|
| `hello-world` | Example subagent that provides greetings |

## Installation

Add a skill to your project:

```bash
uvx skill-add kasperjunge/<skill-name>
```

For example:

```bash
uvx skill-add kasperjunge/frontend-design
```

This downloads the skill to `.claude/skills/` in your current project.

## Directory Structure

```
agent-skills/
└── .claude/
    ├── skills/
    │   └── hello-world/
    │       └── SKILL.md
    ├── commands/
    │   └── hello-world.md
    └── agents/
        └── hello-world.md
```

## Creating Your Own Extensions

### Skills

Skills are automatically discovered based on conversation context. Create a directory in `.claude/skills/` with a `SKILL.md` file:

```markdown
---
name: your-skill-name
description: Brief description shown in Claude Code's skill list
---

Instructions for Claude Code when this skill is invoked.
```

You can include supporting files:

```
your-skill-name/
├── SKILL.md
├── scripts/
│   └── helper.py
└── templates/
    └── example.html
```

### Slash Commands

Slash commands are manually invoked with `/command-name`. Create a markdown file in `.claude/commands/`:

```markdown
---
description: Brief description of the command
argument-hint: [optional-args]
---

Prompt instructions for Claude...
```

Use `$ARGUMENTS` to access user-provided arguments.

### Subagents

Subagents are specialized agents with their own context. Create a markdown file in `.claude/agents/`:

```markdown
---
name: agent-name
description: What this agent does
allowed_tools: []
---

System prompt and behavior instructions...
```

## Publishing

1. Push your repo to GitHub
2. Others can install your extensions with:

```bash
uvx skill-add <your-username>/<extension-name>
```

## Learn More

- [Skills Documentation](https://code.claude.com/docs/en/skills)
- [Slash Commands Documentation](https://code.claude.com/docs/en/slash-commands)
- [Subagents Documentation](https://code.claude.com/docs/en/sub-agents)
