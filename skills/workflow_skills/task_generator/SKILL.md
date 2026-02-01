---
name: task_generator
description: Generate task.md from parsed specification JSON
version: 1.0.0
tags: [workflow, task-generation, automation]
---

# Task Generator Skill

## Description

Generates `task.md` files from parsed specification JSON, creating structured task lists with dependencies and priorities.

從解析的規格 JSON 生成 `task.md` 檔案，創建帶有依賴關係和優先級的結構化任務列表。

## When to Use

Use this skill when you need to:
- Convert specifications to actionable tasks
- Generate task checklists automatically
- Analyze task dependencies
- Prioritize tasks based on specification

## Input

- **File**: `spec.json`
- **Format**: JSON from spec_parser skill

## Output

- **File**: `task.md`
- **Format**: Markdown checklist following TASK_SUMMARY_RULE format

```markdown
# Task: [Task Name]

## ✅ Checklist

### Phase 1: [Phase Name]
- [ ] Task 1
- [ ] Task 2

### Phase 2: [Phase Name]
- [ ] Task 3
```

## Configuration

```yaml
- skill: task_generator
  input: spec.json
  output: task.md
  config:
    analyze_dependencies: true  # Analyze task dependencies
    prioritize_tasks: true      # Sort by priority
    group_by_component: true    # Group by component
```

## Example

```python
from skills.workflow_skills.task_generator import generate_tasks

tasks = generate_tasks('spec.json', 'task.md')
# Generates task.md file
```

## Dependencies

- Python 3.10+
- JSON parser

## Related Skills

- `spec_parser` - Parses specs into JSON
- `planner_agent` - Validates and optimizes tasks

---

**Version**: 1.0.0  
**Status**: Active Development  
**Maintainer**: synthforge team
