# 知識庫管理規則 - KNOWLEDGE_BASE_RULE.md
# 知識提取與結構化規範

**狀態**: MANDATORY 關鍵
**優先級**: HIGH 高
**範圍**: 所有對話中的知識提取與 `.internal/knowledge/` 管理

---

## 🎯 規則目的 / Rule Purpose

確保對話中產生的價值資訊與概念能夠被及時提取、結構化並持久化，避免知識碎片化或隨對話結束而遺失。

---

## 🔍 1. 知識提取觸發點 / Extraction Triggers

當滿足以下任一條件時，必須考慮提取至知識庫：

- **新概念解釋**: 當 AI 解釋了一個特定的架構概念（例如：AI Toggle Agent）。
- **流程規範**: 當定義了一個新的操作流程（例如：特定的 Git 分支工作流）。
- **疑難排解**: 當解決了一個具有普遍性的 Bug 或環境問題。
- **最佳實踐**: 當總結出一套行之有效的開發模式（例如：Clean Code 在本專案的具體應用）。
- **重複詢問**: 當用戶第二次詢問相同的設計原則或操作方法。

---

## 📁 2. 知識庫結構 / Knowledge Base Structure

知識庫位於 `.internal/knowledge/`，按類別組織：

- `concepts/`: 核心概念、架構設計
- `tutorials/`: 操作指南、教學、Step-by-step
- `troubleshooting/`: 錯誤修復記錄、解決方案
- `best_practices/`: 最佳實踐、模式總結
- `strategies/`: 決策記錄、技術選型理由

---

## 📝 3. 檔案命名與格式 / Naming & Format

- **命名**: 使用 `snake_case.md`（例如：`ai_toggle_agent.md`）。
- **語言**: 
  - 核心定義使用 **雙語 (Bilingual)**（繁體中文 + 英文）。
  - 詳細內容使用 **純繁體中文** 以節省 Token。
- **元數據**: 每個知識點檔案頂部必須包含：
  ```markdown
  ---
  category: [類別]
  tags: [標籤1, 標籤2]
  created: YYYY-MM-DD
  status: [Draft/Active/Archived]
  ---
  ```

---

## 🔄 4. 提取流程 / Extraction Process

1. **識別**: 在對話中識別出符合觸發點的知識。
2. **歸類**: 決定其所屬類別（Concepts, Tutorials 等）。
3. **編寫**: 創建對應的 `.md` 檔案，內容應精簡且具有權威性（SSOT）。
4. **關聯**: 在相關的 `README.md` 或 `VIBE_GUIDE.md` 中添加引用（若涉及架構）。
5. **通知**: 在對話中告知用戶「已將 X 知識點提取至知識庫」。

---

## ✅ 檢查清單 / Checklist

- [ ] 知識點是否具備重複使用價值？
- [ ] 命名是否符合 `snake_case.md`？
- [ ] 檔案是否包含元數據 (Metadata)？
- [ ] 內容是否使用了繁體中文？
- [ ] 是否已放在正確的子目錄中？

---

**創建時間**: 2026-02-01
**狀態**: ACTIVE
**強制執行**: MANDATORY
