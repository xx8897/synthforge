# 檔案分類規則 - FILE_CLASSIFICATION_RULE.md
# 檔案類型決策樹

**狀態**: MANDATORY
**優先級**: MEDIUM
**範圍**: 工作區內所有新檔案的創建

---

## 🎯 規則目的 / Rule Purpose

明確定義何時該創建哪種類型的檔案，解決「這個內容該放哪裡？」的困惑，維持目錄結構的語義清晰度。

---

## 🌳 決策樹 / Decision Tree

### Q1: 這是程式碼 (Code) 還是文件 (Doc)?

- **程式碼 (Code)** -> Go to Q2
- **文件 (Doc)** -> Go to Q3

### Q2 [Code]: 它的用途是什麼？

- **通用工具/基礎設施** (Runtime) -> `core_lib/utils/`
- **開發輔助工具/腳本** (Devtime) -> `devtools/`
- **單元測試/集成測試** -> `devtools/tests/`
- **AI 代理實現** -> `agents/[agent_name]/`
- **可重用能力** -> `skills/[skill_name]/`
- **專案業務邏輯** -> `projects/[project_name]/`

### Q3 [Doc]: 它是給誰看的？

- **AI 代理 (Agent)**:
  - 入口導航 -> `VIBE_GUIDE.md`
  - 任務上下文 -> `.internal/planning/`
- **開發者 (Developer)**:
  - 架構設計 -> `docs/architecture/`
  - 操作指南 -> `docs/guides/`
  - 規則規範 -> `rules/`
- **系統 (System)**:
  - 配置 -> `.cursorrules`, `.gitignore`

---

## 📂 常見檔案類型表

| 檔案類型 | 命名規範 | 存放位置 | 備註 |
|---|---|---|---|
| **規則 (Rule)** | `[TOPIC]_RULE.md` | `rules/` | 分為 core, development, management |
| **知識 (Knowledge)** | `[topic]_concept.md` | `.internal/knowledge/` | 概念性知識 |
| **任務總結 (Summary)** | `summary_YYYY-MM-DD_HH.md` | `.internal/summaries/` | 任務執行記錄 |
| **工具 (Tool)** | `[function].py` | `devtools/` 或 `core_lib/` | 依運行時依賴區分 |
| **測試 (Test)** | `test_[module].py` | `devtools/tests/` | 測試腳本 |

---

**創建時間**: 2026-02-01
**狀態**: ACTIVE

---

## 🔗 相關規則 / Related Rules
- [FILE_NAMING_CONVENTION_RULE](FILE_NAMING_CONVENTION_RULE.md): 檔案命名規範
- [TOOLING_USAGE_RULE](TOOLING_USAGE_RULE.md): 工具程式碼的分類
- [DIRECTORY_README_RULE](../core/DIRECTORY_README_RULE.md): 目錄結構規範
