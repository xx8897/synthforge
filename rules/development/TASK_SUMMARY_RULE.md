# TASK_SUMMARY_RULE.md - 任務總結規則

**Status**: MANDATORY 強制  
**Priority**: CRITICAL 極高  
**Scope**: All series tasks 所有系列性任務  
**Version**: 1.0  
**Created**: 2026-02-01

---

## 🎯 規則目的 / Rule Purpose

確保系列性任務完成後，必須創建任務總結：
1. **記錄完成的工作** - 詳細記錄所有完成的任務
2. **保留知識** - 將重要決策和經驗保存下來
3. **追蹤進度** - 明確標記任務狀態
4. **便於回顧** - 未來可以快速了解做了什麼

Ensure task summaries are created after series tasks completion:
1. **Record completed work** - Detail all completed tasks
2. **Preserve knowledge** - Save important decisions and experiences
3. **Track progress** - Clearly mark task status
4. **Easy review** - Quickly understand what was done in the future

---

## 📋 何時創建任務總結 / When to Create Task Summary

### 必須創建 (MUST Create)

**觸發條件**:
1. ✅ 系列性問答完成（多輪對話，完成一個完整目標）
2. ✅ 執行了多個相關任務（3+ 個任務）
3. ✅ 涉及多個檔案的修改（5+ 個檔案）
4. ✅ 完成了一個 Phase 或 Milestone

**範例**:
- ✅ 完成結構優化（修改 10+ 檔案）
- ✅ 完成規則整合（整合 4 個規則）
- ✅ 完成文件重組（移動/刪除/重命名多個檔案）

---

### 可選創建 (MAY Create)

**觸發條件**:
1. ⚠️ 單一任務但很重要
2. ⚠️ 簡單任務但需要記錄決策
3. ⚠️ 用戶明確要求

---

## 📝 任務總結格式 / Task Summary Format

### 檔案命名

**格式**: `summary_YYYY-MM-DD_HH.md`

**範例**: `summary_2026-02-01_16.md`

**位置**: `.internal/summaries/YYYY-MM/`

**重要**: 避免檔案過多，使用小時（HH）而非分鐘（HHMM）

---

### 內容結構

```markdown
# 任務總結 - [任務名稱]

**執行日期**: YYYY-MM-DD  
**執行時間**: HH:MM  
**狀態**: ✅ 完成 / ⏳ 進行中 / ❌ 未完成

---

## 📋 任務概述

[簡要描述這次任務的目標和背景]

---

## ✅ 已完成任務

### 任務 1: [任務名稱]
- ✅ [具體完成項目 1]
- ✅ [具體完成項目 2]

### 任務 2: [任務名稱]
- ✅ [具體完成項目 1]

---

## 📊 統計數據

### 檔案操作
- 📄 創建: X 個檔案
- 📝 修改: Y 個檔案
- 🗑️ 刪除: Z 個檔案
- 📦 移動: W 個檔案

### 程式碼變更
- ➕ 新增: XXX 行
- ➖ 刪除: YYY 行

---

## 🎯 達成目標

1. ✅ [目標 1]
2. ✅ [目標 2]

---

## ⚠️ 未完成任務

1. ⏳ [任務 1] - 原因: [說明]
2. ❌ [任務 2] - 原因: [說明]

---

## 📝 重要決策

1. **決策 1**: [說明]
   - 原因: [為什麼這樣做]
   - 影響: [對專案的影響]

---

## 🚀 下一步

1. [ ] [下一步任務 1]
2. [ ] [下一步任務 2]

---

**總執行時間**: X 小時  
**狀態**: ✅ 完成
```

---

## 🔄 執行流程 / Execution Flow

### Step 1: 任務完成時

```
系列性任務完成
    ↓
檢查是否符合觸發條件
    ↓
是 → 創建任務總結
否 → 不需要
```

---

### Step 2: 創建任務總結前檢查

```python
# 檢查流程
1. 查看當天最新的任務總結
   - 檢查 .internal/summaries/YYYY-MM/ 中是否有今天的總結
   - 如果有，決定是否:
     a) 更新現有總結（同一小時內）
     b) 創建新總結（不同小時）
2. 如果是同一小時，更新現有總結而非創建新的
```

---

### Step 3: 創建任務總結

```python
# 自動化流程
1. 確認任務完成
2. 收集統計數據
3. 記錄重要決策
4. 標記未完成任務
5. 規劃下一步
6. 創建 summary_YYYY-MM-DD_HH.md
7. 保存到 .internal/summaries/YYYY-MM/
```

---

### Step 3: 更新 TODO

**重要**: 創建任務總結後，必須更新 TODO（見 TODO_UPDATE_RULE.md）

---

## ✅ 檢查清單 / Checklist

創建任務總結時，確認：

- [ ] **已查看當天最新的任務總結**（重要！）
- [ ] 決定是更新現有總結還是創建新的
- [ ] 任務概述清楚
- [ ] 所有完成任務都列出
- [ ] 統計數據準確
- [ ] 重要決策有記錄
- [ ] 未完成任務有說明
- [ ] 下一步有規劃
- [ ] 檔案命名正確（`summary_YYYY-MM-DD_HH.md`）
- [ ] 保存位置正確
- [ ] **已更新 TODO**（重要！）

---

## 🎯 Summary / 總結

**Key Points**:

1. ✅ **創建前必須查看當天最新的任務總結**
2. ✅ **系列性任務完成 → 必須創建任務總結**
3. ✅ **格式**: `summary_YYYY-MM-DD_HH.md`（使用小時，避免檔案過多）
4. ✅ **位置**: `.internal/summaries/YYYY-MM/`
5. ✅ **內容**: 概述、完成任務、統計、決策、下一步
6. ✅ **重要**: 創建後必須更新 TODO

**This rule ensures all series tasks are properly documented.**  
**此規則確保所有系列性任務都被妥善記錄。**

---

## 📚 相關規則 / Related Rules

### 強依賴 (Strong Dependencies)
- **TODO_UPDATE_RULE.md** - 創建總結後必須更新 TODO
- **FILE_NAMING_CONVENTION_RULE.md** - summary 檔案命名規範
- **INTERNAL_RULE.md** - .internal/summaries/ 結構

### 相關 (Related)
- **VIBE_GUIDE.md** - 系列性任務的定義
- **DRY_RULE.md** - 避免重複記錄

### 衝突 (Conflicts)
- ❌ 無已知衝突

---

**Created**: 2026-02-01  
**Last Updated**: 2026-02-01  
**Status**: ACTIVE  
**Priority**: CRITICAL  
**Enforcement**: MANDATORY
