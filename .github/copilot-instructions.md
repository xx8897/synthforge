# GitHub Copilot Instructions for synthforge

## Before Coding

1. Read [VIBE_GUIDE.md](../VIBE_GUIDE.md)
2. Read [DIRECTORY_README_RULE.md](../DIRECTORY_README_RULE.md)
3. Read subdirectory README.md before working in that directory

## Core Rules

### Directory README Rule
- Read directory README.md before entering
- Update README.md after modifying files
- Update ARCHITECTURE.md when structure changes

### Bilingual Output
- All documentation must be bilingual (EN + ZH)
- Format: English first, then Traditional Chinese

### File Naming
- Rules: `[TOPIC]_RULE.md` (UPPER_CASE)
- Code: `[module_name].py` (lower_case with underscores)
- Knowledge: `[descriptive_name].md` (lower_case)

### Knowledge Management
- Store knowledge in `.internal/knowledge/[category]/`
- Categories: best_practices, patterns, troubleshooting, references, tools, lessons_learned

## Workflow

1. Check `.internal/planning/待辦.md` for current tasks
2. Read relevant documentation
3. Follow naming conventions
4. Update documentation after changes
5. Use bilingual format

## Output Format

```markdown
[English content]

---

[Traditional Chinese content]
```

## Never Do

- Skip reading README.md
- Use single language only
- Violate naming conventions
- Forget to update documentation

## Always Do

- Read VIBE_GUIDE.md first
- Follow bilingual format
- Update README.md after changes
- Use correct naming conventions

---

**This ensures consistent code generation aligned with synthforge standards.**
