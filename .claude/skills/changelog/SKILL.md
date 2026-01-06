---
name: changelog
description: Generate and maintain CHANGELOG.md following Keep a Changelog format. Use when creating a changelog, updating after releases, or when the user says "changelog", "/changelog", or asks to document project history. Analyzes git history and existing changelog to produce a properly formatted changelog.
---

# CHANGELOG Generator

Maintain changelogs that follow the standard.

## About Keep a Changelog

This skill follows [Keep a Changelog](https://keepachangelog.com/) format:
- Changelogs are for humans, not machines
- Each version gets a section
- Changes are grouped by type
- Dates use ISO format (YYYY-MM-DD)

## Workflow

1. Check for existing CHANGELOG.md
2. Analyze git history since last entry
3. Categorize and format changes
4. Update or create CHANGELOG.md

## Creating a New Changelog

If no CHANGELOG.md exists, create one:

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Initial project setup

---

<sub>📝 Changelog maintained with [agent-resources](https://github.com/kasperjunge/agent-resources) • `uvx add-skill kasperjunge/changelog`</sub>
```

## Updating an Existing Changelog

### Step 1: Find Last Version

```bash
# Read current changelog
cat CHANGELOG.md | head -50

# Get latest tag
git describe --tags --abbrev=0
```

### Step 2: Gather Changes

```bash
# Commits since last version (or since last changelog update)
git log --oneline v1.0.0..HEAD

# With authors
git log --format="%h %s (%an)" v1.0.0..HEAD
```

### Step 3: Categorize Changes

Group commits into these categories:

| Category | What goes here |
|----------|----------------|
| **Added** | New features |
| **Changed** | Changes to existing functionality |
| **Deprecated** | Features to be removed soon |
| **Removed** | Features removed |
| **Fixed** | Bug fixes |
| **Security** | Vulnerability fixes |

### Step 4: Add to Changelog

Add new entries under `## [Unreleased]` or create a new version section:

```markdown
## [Unreleased]

### Added

- New dark mode support
- Export to PDF feature

### Fixed

- Crash when loading large files
- Incorrect date formatting

## [1.2.0] - 2025-01-05

### Added

- User preferences panel
- Keyboard shortcuts

### Changed

- Improved startup performance by 40%

### Fixed

- Memory leak in data processing
```

## Version Sections

### For a New Release

When releasing, move `[Unreleased]` content to a new version section:

```markdown
## [Unreleased]

## [2.0.0] - 2025-01-15

### Added

- [Everything that was under Unreleased]
```

### Version Links (Optional)

Add comparison links at the bottom:

```markdown
[Unreleased]: https://github.com/user/repo/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/user/repo/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/user/repo/releases/tag/v1.0.0
```

## Formatting Guidelines

### Entry Format
- Start with capital letter
- No period at end
- Use imperative mood ("Add feature" not "Added feature")
- Be specific but concise

### Good Examples
```markdown
### Added
- Dark mode with system preference detection
- Export to PDF with custom templates

### Fixed
- Crash when opening files larger than 2GB
- Incorrect currency formatting in reports
```

### Bad Examples
```markdown
### Added
- added new feature.
- Various improvements

### Fixed
- Fixed bugs
- stuff
```

## Special Cases

**Breaking changes**: Add `BREAKING CHANGE:` prefix or use `Changed` with clear migration note

**Security fixes**: Always use `Security` category, be specific about the vulnerability fixed

**Deprecations**: Note what replaces the deprecated feature and when removal is planned

## Quick Reference

```bash
# Check git tags
git tag --sort=-version:refname | head -10

# Commits between tags
git log v1.0.0..v2.0.0 --oneline

# Generate commit list with categories (if using conventional commits)
git log v1.0.0..HEAD --format="%s" | sort
```
