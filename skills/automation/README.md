# Automation Skills

**Purpose**: Automation and structure management capabilities  
**Skills**: 1  
**Last Updated**: 2026-02-01

---

## 📁 Skills / 技能

| Skill | Purpose | Status |
|-------|---------|--------|
| [structure_management/](structure_management/SKILL.md) | Directory and file operations | ✅ Active |

---

## 🎯 Purpose / 目的

Automation skills help with repetitive tasks:
- **Structure Management**: Create directories, move files, list trees
- **Git Operations**: (Future) Automated git workflows
- **Build Automation**: (Future) Build and deployment automation

自動化技能幫助處理重複性任務：
- **結構管理**: 創建目錄、移動檔案、列出樹狀結構
- **Git 操作**: （未來）自動化 git 工作流程
- **構建自動化**: （未來）構建和部署自動化

---

## 📖 Usage / 使用方式

```python
# Use structure management skill
from core_lib.utils.files import batch_create_dirs, batch_move_files

# Create directories
batch_create_dirs(['dir1', 'dir2'], Path('.'))

# Move files
moves = [('old.txt', 'new/old.txt')]
batch_move_files(moves, Path('.'))
```

---

**Created**: 2026-02-01  
**Last Updated**: 2026-02-01  
**Maintainer**: synthforge team
