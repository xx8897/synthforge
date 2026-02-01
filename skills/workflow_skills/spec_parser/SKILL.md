---
name: spec_parser
description: Parse implementation_plan.md into structured JSON format
version: 1.0.0
tags: [workflow, parsing, spec]
---

# Spec Parser Skill

## Description

Parses `implementation_plan.md` files into structured JSON format for use in automated workflows.

將 `implementation_plan.md` 檔案解析為結構化 JSON 格式，用於自動化工作流。

## When to Use

Use this skill when you need to:
- Convert implementation plans to machine-readable format
- Extract tasks from specifications
- Prepare specs for automated task generation

## Input

- **File**: `implementation_plan.md`
- **Format**: Markdown following SPEC_DRIVEN_DEVELOPMENT_RULE

## Output

- **File**: `spec.json`
- **Format**: JSON with structured specification data

```json
{
  "goal": "Goal description",
  "proposed_changes": [
    {
      "component": "Component name",
      "files": [
        {
          "action": "MODIFY|NEW|DELETE",
          "path": "file/path",
          "description": "Change description"
        }
      ]
    }
  ],
  "verification_plan": {
    "automated_tests": [],
    "manual_verification": []
  }
}
```

## Configuration

```yaml
- skill: spec_parser
  input: implementation_plan.md
  output: spec.json
  config:
    validate_spec: true        # Validate spec structure
    extract_requirements: true # Extract requirements
```

## Example

```python
from skills.workflow_skills.spec_parser import parse_spec

spec = parse_spec('implementation_plan.md')
# Returns structured JSON object
```

## Dependencies

- Python 3.10+
- PyYAML (for YAML frontmatter)
- Markdown parser

## Related Skills

- `task_generator` - Generates tasks from parsed spec
- `spec_validator` - Validates spec structure

---

**Version**: 1.0.0  
**Status**: Active Development  
**Maintainer**: synthforge team
