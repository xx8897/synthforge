# Skills - Reusable Capabilities

**Purpose**: Modular, reusable capabilities for synthforge  
**Files**: 1 category  
**Last Updated**: 2026-02-01

---

## 📁 Categories / 類別

| Category | Purpose | Skills |
|----------|---------|--------|
| [automation/](automation/README.md) | Automation and structure management | 1 |
| [workflow_skills/](workflow_skills/README.md) | Workflow automation skills | 3 |
| web/ | Web-related capabilities | 🟡 Future |
| data/ | Data processing | 🟡 Future |
| advanced/ | Advanced/composite skills | 🟡 Future |

---

## 🎯 Purpose / 目的

Skills are reusable capabilities that can be used across synthforge:
- **Modular**: Each skill does one thing well
- **Reusable**: Can be used by multiple agents or projects
- **Self-contained**: Includes all necessary code and documentation

Skills 是可在 synthforge 中重用的能力：
- **模組化**: 每個 skill 專注做好一件事
- **可重用**: 可被多個 agents 或專案使用
- **自包含**: 包含所有必要的程式碼和文件

---

## 📖 Usage / 使用方式

**For AI Agents**:
1. Read skills/README.md (this file)
2. Browse category README (e.g., automation/README.md)
3. Read specific SKILL.md for usage

**For Developers**:
```python
# Import from skills
from skills.automation.structure_management import create_dirs
```

---

## 🏗️ Structure / 結構

Each skill follows this structure:
```
skills/[category]/[skill_name]/
├── SKILL.md          # Skill documentation
├── scripts/          # Implementation scripts
├── examples/         # Usage examples
└── templates/        # (Optional) Templates
```

---

## 📝 Notes / 注意事項

- **No suffix**: Skill directories don't have `_skill` suffix
- **SKILL.md**: Main documentation file (not `skill_name.md`)
- **SSOT**: Skills use core_lib/utils for common functions

---

**Created**: 2026-02-01  
**Last Updated**: 2026-02-01  
**Maintainer**: synthforge team
