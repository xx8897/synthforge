---
name: Structure Management
category: automation
description: Manage directory structures and file operations
difficulty: beginner
tags: [automation, files, directories, structure]
dependencies:
  - core_lib
version: 1.0.0
---

# Structure Management Skill

## 📋 摘要 / Summary

Manage directory structures and file operations efficiently.

高效管理目錄結構和檔案操作。

---

## 🎯 觸發情境 / When to Use

Use this skill when you need to:
- Batch create multiple directories
- Batch move files
- Restructure project directories
- List directory trees

當你需要時使用此技能：
- 批量創建多個目錄
- 批量移動檔案
- 重組專案目錄
- 列出目錄樹

---

## 🚀 使用方式 / Usage

### Import from core_lib

```python
from core_lib.utils.files import (
    ensure_dir_exists,
    batch_create_dirs,
    batch_move_files,
    list_directory_tree,
)
from pathlib import Path

# Create directories
directories = ['dir1', 'dir2/subdir', 'dir3']
batch_create_dirs(directories, Path('.'))

# Move files
moves = [
    ('old/file1.txt', 'new/file1.txt'),
    ('old/file2.txt', 'new/file2.txt'),
]
batch_move_files(moves, Path('.'))

# List directory tree
tree = list_directory_tree(Path('.'), max_depth=3)
print(tree)
```

---

## 📁 Files / 檔案

| File | Purpose |
|------|---------|
| `SKILL.md` | This file - skill documentation |
| `examples/` | Usage examples from real restructuring tasks |

---

## 📖 Examples / 範例

See `examples/` directory for real-world usage:
- `restructure_devtools.py` - How to reorganize devtools/
- `restructure_rules.py` - How to reorganize rules/
- `create_directory_structure.py` - How to create .internal/ structure
- `batch_move_files.py` - How to batch move files

---

## 🔗 相關 / Related

### Uses (使用):
- **core_lib/utils/files.py** - Core utility functions (SSOT)

### Related Skills (相關技能):
- None yet (first skill)

### Related Rules (相關規則):
- **DIRECTORY_README_RULE.md** - Always create README when creating directories
- **FILE_NAMING_CONVENTION_RULE.md** - Follow naming conventions

---

## 📝 Notes / 注意事項

- **SSOT Principle**: This skill uses core_lib/utils/files.py as the single source
- **Don't Duplicate**: Never copy-paste these functions, always import from core_lib
- **Examples**: The examples/ directory shows real usage from synthforge restructuring

---

**Created**: 2026-02-01  
**Version**: 1.0.0  
**Status**: Active  
**Difficulty**: Beginner
