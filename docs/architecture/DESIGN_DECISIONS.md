# Design Decisions

**Last Updated**: 2026-02-01

---

## 🎯 Core Design Decisions

This document records major design decisions made for synthforge.

---

## 1. Directory Structure

### Decision: Use visible directories for core components

**Date**: 2026-01-29

**Context**: Deciding between `.rules/` `.agents/` `.skills/` (hidden) vs `rules/` `agents/` `skills/` (visible)

**Decision**: Use visible directories (`rules/`, `agents/`, `skills/`)

**Rationale**:
- Aligns with industry standards (LangChain, CrewAI, AutoGPT)
- Core components should be discoverable
- Hidden directories reserved for tool configs (`.cursor/`, `.internal/`)

**Reference**: [Dotfiles Convention](../../.internal/knowledge/references/dotfiles_convention.md)

---

## 2. INTERNAL_RULE v2.0

### Decision: Implement 5-file limit per directory

**Date**: 2026-02-01

**Context**: Managing .internal/ directory growth and token consumption

**Decision**: Limit most .internal/ subdirectories to 5 files maximum

**Rationale**:
- Keeps focus on current work
- Automatic cleanup prevents accumulation
- Forces integration of completed work

**Exceptions**: knowledge/ has no limit (permanent storage)

---

## 3. docs/ vs analysis/ vs knowledge/

### Decision: Clear separation of concerns

**Date**: 2026-02-01

**Context**: Overlapping content between three directories

**Decision**:
- **docs/** = Formal documentation (for humans)
- **.internal/analysis/** = Temporary analysis (for AI, 5-file limit)
- **.internal/knowledge/** = Knowledge base (for AI triggers, permanent)

**Workflow**:
```
analysis/ (temporary) → knowledge/ or docs/ (permanent) → delete analysis/
```

**Reference**: See implementation plan

---

## 4. GitHub Strategy

### Decision: Hybrid Git approach

**Date**: 2026-01-29

**Strategy**:
1. Workspace root: NOT a git repo
2. Common assets (rules, skills, agents): ONE git repo
3. Each project: Separate git repository

**Benefits**:
- Clean project repositories
- Shared assets versioned together
- Easy to share projects

**Full Details**: [GITHUB_STRATEGY.md](GITHUB_STRATEGY.md)

---

## 5. Skills vs Rules

### Decision: Clear distinction between skills and rules

**Date**: 2026-01-29

**Distinction**:
- **Skills**: Reusable capabilities, patterns AI can learn
- **Rules**: Mandatory guidelines AI must follow

**Reference**: [SKILLS_VS_RULES.md](SKILLS_VS_RULES.md)

---

## 6. Bilingual Documentation

### Decision: English + Chinese for all user-facing docs

**Date**: 2026-01-29

**Rationale**:
- Accessibility for Chinese speakers
- Professional appearance
- .internal/ uses pure Chinese for token efficiency

---

## 7. DRY Principle Application

### Decision: Balanced DRY approach

**Date**: 2026-01-29

**Guidelines**:
- MUST: Extract if repeated 3+ times
- SHOULD: Consider if repeated 2 times
- MAY: Keep separate if different concepts or for readability

**Principle**: Wrong abstraction is worse than duplication

**Reference**: [DRY_RULE.md](../../rules/core/DRY_RULE.md)

---

**Maintained**: This document should be updated whenever major design decisions are made.
