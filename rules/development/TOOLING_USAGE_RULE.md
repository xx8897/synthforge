# 工具使用規範 - TOOLING_USAGE_RULE.md
# Core Lib vs Devtools

**狀態**: MANDATORY
**優先級**: MEDIUM
**範圍**: 工具開發與使用

---

## 🎯 規則目的 / Rule Purpose

明確區分 `core_lib` 與 `devtools` 的職責邊界，並規範新工具的開發位置，防止依賴混亂與程式碼重複。

---

## ⚖️ Core Lib vs Devtools

| 特性 | core_lib | devtools |
|---|---|---|
| **定位** | Runtime Dependencies (運行時依賴) | Development Dependencies (開發依賴) |
| **用途** | 應用程式運行的基礎設施 | 輔助開發、檢查、構建的工具 |
| **穩定性** | 高 (API 變更需謹慎) | 中 (可隨開發需求調整) |
| **依賴方向**| 被 projects 和 devtools 引用 | 引用 core_lib |
| **例子** | 檔案操作、日誌、配置讀取 | 代碼掃描器、腳手架、測試腳本 |

---

## 📍 開發決策指南 / Development Guidelines

當你需要編寫一段 Python 程式碼時：

**1. 這是應用程式的一部分嗎？**
   - 是 -> `projects/` 或 `agents/`

**2. 這是通用的工具函數嗎？** (如 `read_file`, `parse_json`)
   - 是，且會在正式環境運行 -> `core_lib/utils/`
   - 是，但只在開發時用 -> 評估是否放入 `devtools/utils/` (若有)

**3. 這是自動化腳本嗎？** (如 `lint.py`, `build.py`)
   - 是 -> `devtools/`

**4. 這是測試嗎？**
   - 是 -> `devtools/tests/`

---

## 🔄 依賴規則 / Dependency Rules

1. **Devtools 可以引用 Core Lib**: ✅
   - `from core_lib.utils import files` -> OK

2. **Core Lib 不可引用 Devtools**: ❌
   - `core_lib` 必須保持獨立，不可依賴開發工具。

3. **Projects 引用**:
   - 引用 `core_lib` -> ✅
   - 引用 `devtools` -> ❌ (產品代碼不應依賴開發工具)

---

**創建時間**: 2026-02-01
**狀態**: ACTIVE
**優先級**: HIGH

---

## 🔗 相關規則 / Related Rules
- [FILE_CLASSIFICATION_RULE](FILE_CLASSIFICATION_RULE.md): 檔案分類決策樹
- [SINGLE_SOURCE_OF_TRUTH_RULE](../core/SINGLE_SOURCE_OF_TRUTH_RULE.md): 避免工具程式碼重複
- [CODING_STYLE_RULE](CODING_STYLE_RULE.md): 程式碼組織原則
