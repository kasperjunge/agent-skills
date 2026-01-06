---
name: release
description: Generate release notes from git history. Use when preparing a release, creating a GitHub release, or when the user says "release", "/release", "release notes", or asks for help documenting what changed between versions. Analyzes commits since the last tag and produces categorized, human-readable release notes.
---

# Release Notes Generator

Generate release notes that users actually want to read.

## Workflow

1. Find the last release (tag)
2. Gather commits since then
3. Categorize changes
4. Generate formatted release notes

## Step 1: Find Last Release

```bash
# Get the most recent tag
git describe --tags --abbrev=0

# List recent tags
git tag --sort=-version:refname | head -5

# If no tags, use first commit
git rev-list --max-parents=0 HEAD
```

## Step 2: Gather Commits

```bash
# Commits since last tag (replace v1.0.0 with actual tag)
git log v1.0.0..HEAD --oneline

# With full messages
git log v1.0.0..HEAD --format="%h %s%n%b---"

# With file changes
git log v1.0.0..HEAD --stat --oneline
```

## Step 3: Categorize Changes

Analyze each commit and categorize:

| Category | Prefix/Keywords | Example |
|----------|-----------------|---------|
| ✨ Features | `feat`, `add`, `new` | New dark mode |
| 🐛 Bug Fixes | `fix`, `bug`, `patch` | Fix login crash |
| 🔧 Improvements | `improve`, `update`, `enhance` | Faster startup |
| 💥 Breaking | `BREAKING`, `!:` | API renamed |
| 📦 Dependencies | `deps`, `bump`, `upgrade` | Update React 19 |
| 📝 Docs | `docs`, `readme` | Update API docs |
| 🧪 Tests | `test` | Add unit tests |

Use conventional commit prefixes when available. Otherwise, infer from commit message content.

## Step 4: Generate Release Notes

Use this template:

```markdown
# v2.0.0 (YYYY-MM-DD)

[Optional: One paragraph summary of the release theme/highlights]

## ✨ New Features

- Add dark mode support (#123)
- New export to PDF functionality (#145)
- Implement user preferences panel

## 🐛 Bug Fixes

- Fix memory leak in data processing (#134)
- Resolve race condition in auth flow (#156)
- Fix incorrect timezone handling in reports

## 🔧 Improvements

- 40% faster startup time
- Reduced bundle size by 15%
- Better error messages for API failures

## 💥 Breaking Changes

- `oldMethod()` has been renamed to `newMethod()`
- Minimum Node.js version is now 18
- Config file format changed (see migration guide)

## 📦 Dependencies

- Upgraded React from 18.2 to 19.0
- Removed deprecated `moment` in favor of `date-fns`
- Added `zod` for schema validation

## 🙏 Contributors

Thanks to @contributor1, @contributor2 for their contributions!

---

**Full Changelog**: https://github.com/user/repo/compare/v1.0.0...v2.0.0

<sub>📋 Release notes generated with [agent-resources](https://github.com/kasperjunge/agent-resources) • `uvx add-skill kasperjunge/release`</sub>
```

## Formatting Guidelines

### Version Number
- Use semantic versioning (vX.Y.Z)
- Major: breaking changes
- Minor: new features
- Patch: bug fixes

### Each Entry
- Start with action verb (Add, Fix, Improve, Remove)
- Include PR/issue number if available
- Be specific but concise

### Breaking Changes
- Always highlight prominently
- Include migration steps or link to guide
- Explain what users need to do

## Handling Edge Cases

**No conventional commits**: Infer category from message content and changed files

**Large releases**: Add a "Highlights" section at top with 3-5 key changes

**Security fixes**: Always mention prominently, consider separate section

**Contributors**: Extract from commit authors, mention significant contributors

## Quick Commands

```bash
# Generate contributor list
git log v1.0.0..HEAD --format="%an" | sort -u

# Count commits by type (if using conventional commits)
git log v1.0.0..HEAD --oneline | grep -c "^[a-f0-9]* feat"

# Get PR numbers from commit messages
git log v1.0.0..HEAD --oneline | grep -oE "#[0-9]+"
```
