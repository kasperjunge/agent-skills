---
name: onboard
description: Generate comprehensive codebase onboarding guides. Use when someone needs to understand a new codebase, when asked to explain the architecture, or when the user says "onboard", "/onboard", "explain this codebase", or asks for help understanding how a project works. Analyzes project structure, patterns, and key files to produce a complete onboarding document.
---

# Codebase Onboarding Generator

Turn weeks of confusion into minutes of clarity.

## Workflow

1. Analyze project structure (files, directories, patterns)
2. Identify architecture (frameworks, data flow, entry points)
3. Find key files and patterns
4. Generate onboarding guide

## Step 1: Analyze Project Structure

```bash
# Directory structure (excluding noise)
find . -type f \( -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.go" -o -name "*.rs" \) | grep -v node_modules | grep -v __pycache__ | grep -v .git | head -100

# Package/dependency info
cat package.json pyproject.toml Cargo.toml go.mod 2>/dev/null

# Configuration files
ls -la *.config.* .env* tsconfig.json 2>/dev/null
```

## Step 2: Identify Architecture

Look for and read:
- **Entry points**: `main.py`, `index.ts`, `App.tsx`, `main.go`
- **Config**: Environment variables, settings files
- **Core logic**: `src/`, `lib/`, `pkg/`, `internal/`
- **API layer**: `routes/`, `api/`, `handlers/`, `controllers/`
- **Data layer**: `models/`, `schemas/`, `db/`, `repositories/`
- **Tests**: `tests/`, `__tests__/`, `*_test.go`

## Step 3: Identify Key Patterns

Common patterns to look for:
- **Auth**: How authentication/authorization works
- **Data flow**: Request → processing → storage → response
- **State management**: How state is managed (Redux, Context, etc.)
- **Error handling**: How errors are caught and reported
- **Configuration**: How config/env vars are loaded

## Step 4: Generate Guide

Use this template:

```markdown
# Onboarding Guide: [Project Name]

> [One sentence: what this project does]

## Quick Start

```bash
# Clone and setup
git clone <repo>
cd <project>
[install commands]
[run commands]
```

## Architecture Overview

[2-3 sentences describing the high-level architecture]

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   [Layer]   │────▶│   [Layer]   │────▶│   [Layer]   │
└─────────────┘     └─────────────┘     └─────────────┘
```

## Directory Structure

| Directory | Purpose |
|-----------|---------|
| `src/` | [What's in here] |
| `lib/` | [What's in here] |
| `tests/` | [What's in here] |

## Key Files

| File | Purpose | Read When |
|------|---------|-----------|
| `src/index.ts` | App entry point | Understanding startup |
| `src/config.ts` | Configuration | Changing settings |
| `src/db/schema.ts` | Database schema | Working with data |

## Core Concepts

### [Concept 1: e.g., Authentication]

[How it works, key files involved, important decisions]

### [Concept 2: e.g., Data Flow]

[How data moves through the system]

### [Concept 3: e.g., API Design]

[How the API is structured]

## Common Tasks

### Adding a new API endpoint

1. Create route in `src/routes/`
2. Add handler in `src/handlers/`
3. Add tests in `tests/`

### Adding a new database table

1. Add schema in `src/db/schema.ts`
2. Run migration: `npm run migrate`
3. Create model in `src/models/`

### Running tests

```bash
npm test           # All tests
npm test -- auth   # Specific tests
```

## Environment Setup

| Variable | Purpose | Example |
|----------|---------|---------|
| `DATABASE_URL` | Database connection | `postgres://...` |
| `API_KEY` | External API auth | `sk-...` |

## Gotchas & Tribal Knowledge

- ⚠️ [Thing that's not obvious but important]
- ⚠️ [Common mistake to avoid]
- 💡 [Helpful tip]

## Resources

- [Link to design docs]
- [Link to API docs]
- [Link to runbooks]

---

<sub>📚 Onboarding guide generated with [agent-resources](https://github.com/kasperjunge/agent-resources) • `uvx add-skill kasperjunge/onboard`</sub>
```

## Section Guidelines

### Architecture Overview
- Keep it high-level (boxes and arrows)
- Focus on major components only
- Show data/request flow

### Key Files
- Include the "Read When" column
- Limit to 5-10 most important files
- Focus on files new devs will touch first

### Common Tasks
- Write as step-by-step instructions
- Cover the tasks new devs do first
- Include exact commands

### Gotchas
- Things that waste hours if unknown
- Non-obvious decisions and why
- Common mistakes from past devs

## Adapt to Project Type

**Backend API**: Focus on routes, middleware, database
**Frontend App**: Focus on components, state, styling
**CLI Tool**: Focus on commands, arguments, configuration
**Library**: Focus on public API, usage patterns
**Monorepo**: Add section on package relationships
