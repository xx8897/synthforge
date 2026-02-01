# core_lib - Core Library

**Purpose**: Shared utilities and infrastructure for synthforge  
**Files**: 3  
**Last Updated**: 2026-02-01

---

## 📁 Files / 檔案

| File | Purpose | Status |
|------|---------|--------|
| `__init__.py` | Package initialization | ✅ Complete |
| `loader.py` | Load skills and agents | 🟡 Future |
| `config.py` | Configuration management | 🟡 Future |
| `utils/` | Shared utility functions | ✅ Complete |

---

## 🎯 Purpose / 目的

core_lib provides shared infrastructure and utilities used across synthforge:
- **utils/** - Common utility functions (file operations, text processing, etc.)
- **loader** - Load and manage skills/agents (future)
- **config** - Centralized configuration (future)

core_lib 提供 synthforge 共用的基礎設施和工具：
- **utils/** - 通用工具函數（檔案操作、文字處理等）
- **loader** - 載入和管理 skills/agents（未來）
- **config** - 集中式配置（未來）

---

## 🔗 Dependencies / 依賴關係

### Internal Dependencies:
- None (core library)

### External Dependencies:
- Standard library only (no external packages)

---

## 📖 Usage / 使用方式

```python
# Import utilities
from core_lib.utils.files import batch_create_dirs, batch_move_files

# Use utilities
batch_create_dirs(['dir1', 'dir2'], Path('.'))
```

---

## 🏗️ Architecture / 架構

```
core_lib/
├── __init__.py         # Package init
├── loader.py           # (Future) Load skills/agents
├── config.py           # (Future) Configuration
└── utils/              # Shared utilities
    ├── __init__.py
    ├── files.py        # File operations
    ├── text.py         # Text processing (future)
    ├── tokens.py       # Token counting (future)
    └── cache.py        # Caching (future)
```

---

## 📝 Notes / 注意事項

- **SSOT Principle**: core_lib/utils is the single source for utility functions
- **No Duplication**: Do not duplicate these functions in skills or devtools
- **Import from here**: Always import from core_lib.utils, never copy-paste

---

**Created**: 2026-02-01  
**Last Updated**: 2026-02-01  
**Maintainer**: synthforge team
