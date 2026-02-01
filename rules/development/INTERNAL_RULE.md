# INTERNAL_RULE.md - .internal 目錄管理規則

**狀態**: MANDATORY 強制  
**優先級**: CRITICAL 極高  
**範圍**: .internal/ 目錄的所有操作  
**版本**: 2.0  
**最後更新**: 2026-02-01

---

## 🎯 規則目的

建立高效、精簡的內部管理系統：
1. **專注當下** - 只保留必要的檔案（每目錄最多 5 個）
2. **TODO 驅動** - 執行前必讀最新 TODO
3. **知識累積** - 觸發式知識點查詢
4. **自動清理** - 超過限制自動處理

---

## 📁 Part 1: 目錄結構與檔案限制

### 1.1 目錄結構

```
.internal/
├── README.md                    ← 操作手冊（與本規則強依賴）
├── planning/
│   └── TODO_MM_DD.md           ← 最多 5 個
├── confirmations/
│   ├── pending/                ← 最多 5 個（待確認）
│   └── archived/               ← 最多 5 個（已確認）
├── summaries/
│   └── YYYY-MM/
│       └── summary_YYYY-MM-DD_HH.md  ← 每月最多 5 個
├── analysis/                   ← 最多 5 個
└── knowledge/
    ├── README.md
    ├── best_practices/         ← 無限制（永久保留）
    ├── patterns/
    ├── troubleshooting/
    ├── references/
    ├── tools/
    └── lessons_learned/
```

### 1.2 檔案數量限制規則

**限制目錄**（最多 5 個檔案）:
- `planning/` - TODO 檔案
- `confirmations/pending/` - 待確認文件
- `confirmations/archived/` - 已確認文件
- `summaries/YYYY-MM/` - 每月總結
- `analysis/` - 分析文件

**無限制目錄**:
- `knowledge/` - 所有子目錄（永久保留）

### 1.3 自動清理機制

**觸發條件**: 目錄檔案數 > 5

**清理流程**:
```
1. 找出最老的檔案（按修改時間）
2. 檢查檔案狀態標記：
   - 有 "✅ 已完成" / "✅ 完成" → 自動刪除
   - 有 "⏳ 進行中" / "❌ 未完成" → 請示用戶
   - 無明確標記 → 請示用戶
3. 刪除後重新檢查，直到 ≤ 5 個
```

**請示格式**:
```markdown
⚠️ 檔案數量超過限制

**目錄**: planning/
**當前數量**: 7 個
**限制**: 5 個

**建議刪除**:
1. TODO_01_15.md (最後修改: 2026-01-15)
   - 狀態: ⏳ 進行中
   - 內容: [簡要摘要]
   - 建議: 請確認是否已完成

是否刪除？(Y/N)
```

---

## 📋 Part 2: TODO 管理

### 2.1 TODO 檔案規範

**命名格式**: `TODO_MM_DD.md`

**範例**: `TODO_02_01.md` (2 月 1 日)

**位置**: `.internal/planning/`

**數量限制**: 最多 5 個

### 2.2 執行前必讀流程

**MANDATORY**: 每次開始工作前

**步驟**:
```
1. 進入 .internal/planning/
2. 列出所有 TODO_*.md
3. 按日期排序（最新優先）
4. 讀取最新的 TODO
5. 確認當前任務
```

**範例**:
```bash
planning/
├── TODO_02_01.md  ← 讀這個（最新）
├── TODO_01_30.md
├── TODO_01_28.md
├── TODO_01_25.md
└── TODO_01_20.md
```

### 2.3 TODO 檔案格式

```markdown
# TODO - 2026-02-01

## 🔥 今日優先

- [ ] 任務 A（最重要）
- [ ] 任務 B

## 📋 本週待辦

- [ ] 任務 C
- [ ] 任務 D

## 💡 想法與備註

- 備註 1
- 備註 2

## ✅ 已完成

- [x] 任務 X (2026-01-31)
- [x] 任務 Y (2026-01-30)

---

**創建**: 2026-02-01  
**最後更新**: 2026-02-01 14:30
```

### 2.4 TODO 更新規則

**觸發時機**:
1. 每次對話結束前
2. 完成重要任務後
3. 新增待辦事項時

**更新流程**:
```
1. 讀取最新 TODO
2. 標記已完成項目 (✅)
3. 新增新任務
4. 如果日期變更 → 創建新 TODO_MM_DD.md
5. 如果超過 5 個 → 觸發清理機制
```

---

## 📝 Part 3: 確認文件管理

### 3.1 pending/ 管理

**用途**: 需要用戶確認的決策

**命名**: `[topic]_confirmation.md`

**數量限制**: 最多 5 個

**必須包含**:
1. 問題陳述
2. 選項分析
3. 專家建議
4. 確認問題（⏳ 標記）

### 3.2 pending → archived 強制流程

**MANDATORY**: 確認完成後必須執行

**流程**:
```
1. 用戶確認決策
2. 在檔案頂部加上 "✅ 已確認 - YYYY-MM-DD"
3. 立即移動到 archived/
4. 更新 TODO（移除此確認項目）
```

**範例**:
```bash
# Before
confirmations/pending/api_choice_confirmation.md

# After (用戶確認後)
confirmations/archived/api_choice_confirmation.md
```

**檢查機制**:
- 每次對話結束前檢查 pending/
- 如有已確認但未搬移的檔案 → 提醒並執行搬移

### 3.3 archived/ 管理

**用途**: 已確認的決策記錄

**數量限制**: 最多 5 個

**清理規則**:
- 超過 5 個時，刪除最老的
- 刪除前確認內容已整合到正式文件

---

## 📊 Part 4: 任務總結管理

### 4.1 總結檔案規範

**命名格式**: `summary_YYYY-MM-DD_HHMM.md`

**範例**: `summary_2026-02-01_1430.md`

**位置**: `.internal/summaries/YYYY-MM/`

**數量限制**: 每月最多 5 個

### 4.2 對話結束流程

**MANDATORY**: 每次對話結束前執行

**步驟**:
```
1. 檢查 TODO 未執行項目
2. 更新 TODO（標記完成、新增項目）
3. 檢查 pending/ 是否有已確認但未搬移的檔案
4. 創建任務總結
5. 計算並報告 token 消耗
6. 檢查各目錄檔案數量
7. 如超過限制 → 執行清理
```

### 4.3 總結模板

```markdown
# 任務總結 - YYYY-MM-DD HH:MM

## ✅ 已完成的任務

| # | 任務 | 狀態 | 成果 |
|---|------|------|------|
| 1 | ... | ✅ 完成 | ... |

## 📋 創建/修改的文件

1. ✅ `path/to/file.md` - 描述

## 🎯 關鍵決策

- 決策 1: ...

## 📝 TODO 更新

### 新增:
- [ ] 任務 A

### 已完成:
- [x] 任務 B

## ⚠️ Token 消耗

**本次對話**: X tokens  
**累計**: Y tokens  
**狀態**: ✅/⚠️/🚨

## 📊 檔案數量檢查

| 目錄 | 數量 | 限制 | 狀態 |
|------|------|------|------|
| planning/ | 3 | 5 | ✅ |
| pending/ | 2 | 5 | ✅ |
| archived/ | 4 | 5 | ✅ |
| summaries/02/ | 2 | 5 | ✅ |
| analysis/ | 5 | 5 | ⚠️ 已達上限 |

---

**時間**: YYYY-MM-DD HH:MM  
**狀態**: ✅ 完成
```

---

## 📚 Part 5: 知識點管理與觸發機制

### 5.1 知識庫結構（類似 skills/）

```
knowledge/
├── README.md                   ← 知識點索引
├── best_practices/
│   ├── KNOWLEDGE.md           ← 類似 SKILL.md
│   └── dry_principle.md
├── patterns/
│   ├── KNOWLEDGE.md
│   └── singleton_pattern.md
├── troubleshooting/
│   ├── KNOWLEDGE.md
│   └── import_error.md
├── references/
│   ├── KNOWLEDGE.md
│   └── python_ast.md
├── tools/
│   ├── KNOWLEDGE.md
│   └── click_usage.md
└── lessons_learned/
    ├── KNOWLEDGE.md
    └── token_optimization.md
```

### 5.2 KNOWLEDGE.md 格式

```markdown
---
category: best_practices
description: Best practices knowledge points
count: 5
---

# Best Practices Knowledge

## 知識點列表

1. [DRY Principle](dry_principle.md) - Don't Repeat Yourself
2. [SOLID Principles](solid_principles.md) - Object-oriented design
3. ...

## 觸發情境

**何時查詢此類別**:
- 設計新功能時
- 重構程式碼時
- Code review 時

## 快速索引

- DRY → dry_principle.md
- SOLID → solid_principles.md
```

### 5.3 觸發機制

**自動觸發情境**:

| 情境 | 觸發條件 | 搜尋目錄 |
|------|---------|---------|
| 遇到錯誤 | 執行失敗、異常、錯誤訊息 | troubleshooting/ |
| 需要最佳實踐 | 設計新功能、重構程式碼 | best_practices/ |
| 使用工具 | 使用特定工具或框架 | tools/ |
| 設計模式 | 架構設計、程式碼組織 | patterns/ |
| 查找參考 | 需要 API 文件、語法參考 | references/ |
| 回顧經驗 | 類似問題、過去決策 | lessons_learned/ |

**觸發流程**:
```
1. 識別情境（錯誤、設計、工具使用等）
2. 確定對應的知識類別
3. 讀取該類別的 KNOWLEDGE.md
4. 搜尋相關知識點
5. 應用知識點內容
```

**範例**:
```
情境: 遇到 "ImportError: No module named 'click'"
    ↓
觸發: troubleshooting/
    ↓
搜尋: import_error.md
    ↓
應用: 解決方案
```

### 5.4 知識點檔案格式

```markdown
# [知識點標題]

**類別**: [category]  
**建立**: YYYY-MM-DD  
**標籤**: #tag1 #tag2

---

## 摘要

[一句話總結]

---

## 觸發情境

**何時使用**:
- 情境 1
- 情境 2

---

## 內容

[詳細內容]

### 範例

\`\`\`python
[程式碼]
\`\`\`

---

## 相關知識點

- [相關 1](../category/file.md)
- [相關 2](../category/file.md)

---

**最後更新**: YYYY-MM-DD
```

---

## 🔢 Part 6: Token 管理

### 6.1 Token 消耗標準

| 級別 | 預估 Token | 狀態 |
|------|-----------|------|
| Excellent | < 5K | ✅ |
| Good | 5K-10K | ✅ |
| Warning | 10K-15K | ⚠️ |
| High | 15K-20K | 🚨 |
| Critical | > 20K | 🔴 |

### 6.2 每次對話結束報告

**MANDATORY**: 報告本次 token 消耗

**格式**:
```markdown
## ⚠️ Token 消耗報告

**本次對話**: 2,345 tokens  
**累計（本月）**: 15,678 tokens  
**狀態**: ⚠️ Warning

**建議**: 考慮清理 analysis/ 目錄（已達 5 個上限）
```

---

## 🔄 Part 7: 完整工作流程

### 7.1 開始工作前

```
1. 讀取 VIBE_GUIDE.md
2. 讀取相關規則
3. 進入 .internal/planning/
4. 讀取最新 TODO_MM_DD.md
5. 確認當前任務
6. 檢查 confirmations/pending/
```

### 7.2 工作進行中

```
1. 執行任務
2. 更新文件
3. 記錄決策
4. 如需確認 → 創建 pending/
```

### 7.3 對話結束前（MANDATORY）

```
1. 檢查 TODO 未執行項目
2. 更新 TODO（標記完成、新增項目）
3. 檢查 pending/ 是否有已確認但未搬移的檔案
   - 如有 → 執行搬移到 archived/
4. 創建任務總結 summary_YYYY-MM-DD_HHMM.md
5. 計算並報告 token 消耗
6. 檢查各目錄檔案數量
   - planning/ ≤ 5?
   - pending/ ≤ 5?
   - archived/ ≤ 5?
   - summaries/MM/ ≤ 5?
   - analysis/ ≤ 5?
7. 如超過限制 → 執行清理機制
8. 提醒用戶未完成事項
```

---

## 📖 與 .internal/README.md 的關係

**強依賴關係**:
- **INTERNAL_RULE.md** = 完整規則（為什麼、怎麼做）
- **.internal/README.md** = 快速操作手冊（檢查清單）

**README 必須包含**:
1. 快速檢查清單
2. 檔案命名範例
3. 常見問題
4. 與 INTERNAL_RULE 的對應章節

---

## ✅ Summary

**核心原則**:
1. ✅ 執行前必讀最新 TODO
2. ✅ 每目錄最多 5 個檔案（knowledge/ 除外）
3. ✅ pending → archived 強制搬移
4. ✅ 對話結束前必創建總結
5. ✅ 報告 token 消耗
6. ✅ 知識點觸發式查詢

**This rule ensures focused, efficient .internal management with automatic cleanup.**  
**此規則確保專注、高效的 .internal 管理與自動清理。**

---

**建立**: 2026-02-01  
**版本**: 2.0  
**狀態**: ACTIVE  
**優先級**: CRITICAL  
**執行**: MANDATORY
