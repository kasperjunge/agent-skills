---
name: readme
description: Generate beautiful, comprehensive README.md files for any codebase. Use when asked to create a README, improve documentation, or when the user says "readme", "/readme", or wants help documenting their project. Analyzes the codebase structure, dependencies, and code to produce professional documentation.
---

# README Generator

Generate READMEs that make projects shine.

## Workflow

1. Analyze the codebase (structure, dependencies, entry points)
2. Identify key information (what it does, how to use it)
3. Generate README following the template
4. Output polished markdown

## Step 1: Analyze Codebase

Gather information about the project:

```bash
# Project structure
find . -type f -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.go" | head -50

# Package info
cat package.json 2>/dev/null || cat pyproject.toml 2>/dev/null || cat Cargo.toml 2>/dev/null

# Existing docs
cat README.md 2>/dev/null | head -100
```

Look for:
- **Entry points**: main files, CLI commands, exports
- **Dependencies**: what the project uses
- **Scripts**: available commands (npm scripts, Makefile, etc.)
- **Tests**: how to run them
- **Config**: environment variables, config files

## Step 2: Identify Key Information

Answer these questions:
1. **What is it?** One sentence description
2. **Why use it?** Key benefits/features
3. **How to install?** Step-by-step setup
4. **How to use?** Quick start example
5. **What are the options?** Configuration, API, CLI flags

## Step 3: Generate README

Use this template (adapt sections as needed):

```markdown
<div align="center">

# 🚀 Project Name

**One-line description of what this project does.**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

[Installation](#installation) • [Usage](#usage) • [API](#api) • [Contributing](#contributing)

</div>

---

## Features

- ✨ **Feature 1** — Brief description
- 🔥 **Feature 2** — Brief description
- 🛠 **Feature 3** — Brief description

## Installation

```bash
npm install package-name
# or
pip install package-name
```

## Quick Start

```javascript
// Minimal example showing core functionality
import { thing } from 'package-name';

const result = thing.doSomething();
console.log(result);
```

## Usage

### Basic Usage

[Show the most common use case with code example]

### Advanced Usage

[Show more complex scenarios if applicable]

## API Reference

### `functionName(param1, param2)`

Description of what it does.

**Parameters:**
- `param1` (string) — Description
- `param2` (object) — Description

**Returns:** Description of return value

**Example:**
```javascript
const result = functionName('hello', { option: true });
```

## Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `option1` | string | `"default"` | What it does |
| `option2` | boolean | `false` | What it does |

## Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

```bash
git clone https://github.com/username/repo
cd repo
npm install
npm test
```

## License

[MIT](LICENSE) © [Author Name](https://github.com/username)

---

<sub>📖 README generated with [agent-resources](https://github.com/kasperjunge/agent-resources) • `uvx add-skill kasperjunge/readme`</sub>
```

## Section Guidelines

### Header
- Use centered div for visual appeal
- Add relevant badges (license, version, build status)
- Include navigation links

### Features
- 3-5 key features max
- Use emojis sparingly but effectively
- Focus on benefits, not just features

### Installation
- Show ALL installation methods (npm, yarn, pip, etc.)
- Include prerequisites if any
- Keep it copy-pasteable

### Quick Start
- Show the simplest working example
- Should work after copy-paste
- Include expected output if helpful

### API Reference
- Only include for libraries/packages
- Group related functions
- Show examples for complex functions

## Adapt to Project Type

**CLI Tool**: Emphasize installation and command examples
**Library**: Focus on API reference and integration examples
**Web App**: Include screenshots, demo links, deployment
**Framework**: Add guides, tutorials, architecture overview

## Quality Checklist

- [ ] Can someone understand what this does in 10 seconds?
- [ ] Can they install and run it in 2 minutes?
- [ ] Are code examples copy-pasteable and working?
- [ ] Is it scannable (headers, bullets, tables)?
- [ ] Does it answer "why should I use this?"
