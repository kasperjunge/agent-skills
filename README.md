# agent-skills

A collection of reusable Claude Code skills. Install them in any project using [skill-add](https://github.com/kasperjunge/skill-add).

## Available Skills

| Skill | Description |
|-------|-------------|
| `frontend-design` | Create distinctive, production-grade frontend interfaces with high design quality |

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

## Creating Your Own Skills

Want to share your own Claude Code skills? Create an `agent-skills` repository with this structure:

```
agent-skills/
└── .claude/
    └── skills/
        └── your-skill-name/
            └── SKILL.md
```

### SKILL.md Format

Each skill needs a `SKILL.md` file with frontmatter and instructions:

```markdown
---
name: your-skill-name
description: Brief description shown in Claude Code's skill list
---

Instructions for Claude Code when this skill is invoked.

Explain:
- What the skill does
- How Claude should approach the task
- Any guidelines or constraints
```

### Adding Supporting Files

You can include additional files alongside `SKILL.md`:

```
your-skill-name/
├── SKILL.md
├── scripts/
│   └── helper.py
└── templates/
    └── example.html
```

### Publishing

1. Push your `agent-skills` repo to GitHub
2. Others can install your skills with:

```bash
uvx skill-add <your-username>/<skill-name>
```
