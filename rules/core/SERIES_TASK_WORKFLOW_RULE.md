# SERIES_TASK_WORKFLOW_RULE.md - 系列任務工作流規則

**Status**: MANDATORY 強制  
**Priority**: CRITICAL 極高  
**Scope**: All series tasks 所有系列性任務  
**Version**: 1.0  
**Created**: 2026-02-01

---

## 🎯 規則目的 / Rule Purpose

定義系列任務完成後的標準工作流程，確保：
1. **TODO 始終最新** - 追蹤所有待辦和已完成任務
2. **總結持續記錄** - 延續記錄所有完成的工作
3. **自動化執行** - 單次多任務請求後自動執行
4. **避免重複檔案** - 智能檢查並更新現有檔案

Define standard workflow after series tasks completion to ensure:
1. **TODO stays current** - Track all pending and completed tasks
2. **Summaries are continuous** - Ongoing record of all work done
3. **Automated execution** - Auto-execute after multi-task requests
4. **Avoid duplicate files** - Smart check and update existing files

---

## 📋 何時觸發工作流 / When to Trigger Workflow

### 觸發條件 (Trigger Conditions)

**必須執行工作流**:
1. ✅ 完成系列任務（3+ 個相關任務）
2. ✅ 完成需求審查（用戶確認計劃）
3. ✅ 單次多個任務請求完成後
4. ✅ 執行了多個檔案操作（5+ 個檔案）

**範例**:
- ✅ 完成結構優化（修改 10+ 檔案）
- ✅ 用戶確認實施計劃
- ✅ 完成規則整合
- ✅ 完成文件重組

---

## 🔄 標準工作流程 / Standard Workflow

### 完整流程圖

```
系列任務完成
    ↓
Step 1: 檢查並更新 TODO
    ├─ 檢查當天是否有 TODO_MM_DD.md
    ├─ 有 → 更新現有 TODO
    └─ 無 → 創建新 TODO
    ↓
Step 2: 檢查並創建/更新總結
    ├─ 檢查當小時是否有 summary_YYYY-MM-DD_HH.md
    ├─ 有 → 更新現有總結
    └─ 無 → 創建新總結
    ↓
完成 ✅
```

---

## 📝 Step 1: 更新 TODO

### 1.1 檢查當天 TODO

```python
# 檢查流程
1. 獲取當前日期: YYYY-MM-DD
2. 構建 TODO 檔案名: TODO_MM_DD.md
3. 檢查 .internal/planning/ 中是否存在
4. 決定:
   - 存在 → 更新現有 TODO (Step 1.2)
   - 不存在 → 創建新 TODO (Step 1.3)
```

---

### 1.2 更新現有 TODO

**操作**:
```markdown
1. 讀取現有 TODO_MM_DD.md
2. 更新「最後更新」時間
3. 標記已完成任務為 [x]
4. 移動已完成任務到「已完成」section
5. 新增新任務（如有）
6. 調整優先級（如需要）
7. 保存檔案
```

**範例**:
```markdown
# TODO - 2026-02-01

**最後更新**: 2026-02-01 16:53  ← 更新時間

## ✅ 已完成 (Completed)

- [x] 創建 TASK_SUMMARY_RULE.md - 完成時間: 2026-02-01  ← 新增
- [x] 創建 TODO_UPDATE_RULE.md - 完成時間: 2026-02-01  ← 新增
```

---

### 1.3 創建新 TODO

**操作**:
```markdown
1. 創建 TODO_MM_DD.md
2. 使用標準模板
3. 列出所有待辦任務
4. 標記已完成任務
5. 保存到 .internal/planning/
```

**模板**:
```markdown
# TODO - YYYY-MM-DD

**創建日期**: YYYY-MM-DD  
**最後更新**: YYYY-MM-DD HH:MM  
**狀態**: ⏳ 進行中

---

## 🔴 高優先級 (High Priority)

- [ ] [任務 1]

---

## 🟡 中優先級 (Medium Priority)

- [ ] [任務 2]

---

## 🟢 低優先級 (Low Priority)

- [ ] [任務 3]

---

## ✅ 已完成 (Completed)

- [x] [已完成任務] - 完成時間: YYYY-MM-DD

---

**下次更新**: YYYY-MM-DD
```

---

## 📊 Step 2: 創建/更新總結

### 2.1 檢查當小時總結

```python
# 檢查流程
1. 獲取當前時間: YYYY-MM-DD HH
2. 構建總結檔案名: summary_YYYY-MM-DD_HH.md
3. 檢查 .internal/summaries/YYYY-MM/ 中是否存在
4. 決定:
   - 存在 → 更新現有總結 (Step 2.2)
   - 不存在 → 創建新總結 (Step 2.3)
```

---

### 2.2 更新現有總結

**操作**:
```markdown
1. 讀取現有 summary_YYYY-MM-DD_HH.md
2. 在「已完成任務」section 新增新任務
3. 更新統計數據（累加）
4. 新增重要決策（如有）
5. 更新「執行時間」範圍
6. 保存檔案
```

**範例**:
```markdown
# 任務總結 - 結構優化與規則建立

**執行時間**: 14:00 - 16:53  ← 更新結束時間

---

## ✅ 已完成任務

### 任務 8: 優化規則（新增）  ← 新增
- ✅ 更新 TASK_SUMMARY_RULE.md
- ✅ 更新 FILE_NAMING_CONVENTION_RULE.md

---

## 📊 統計數據

### 檔案操作
- 📝 修改: 8 個檔案  ← 更新數字（原本 6 個）
```

---

### 2.3 創建新總結

**操作**:
```markdown
1. 創建 summary_YYYY-MM-DD_HH.md
2. 使用標準模板
3. 記錄所有完成任務
4. 收集統計數據
5. 記錄重要決策
6. 保存到 .internal/summaries/YYYY-MM/
```

**模板**: 見 TASK_SUMMARY_RULE.md

---

## ✅ 檢查清單 / Checklist

執行工作流時，確認：

### TODO 更新
- [ ] 已檢查當天是否有 TODO
- [ ] 已決定創建或更新
- [ ] 已完成任務標記為 [x]
- [ ] 已完成任務移到「已完成」section
- [ ] 「最後更新」時間已更新

### 總結創建/更新
- [ ] 已檢查當小時是否有總結
- [ ] 已決定創建或更新
- [ ] 所有完成任務都記錄
- [ ] 統計數據準確
- [ ] 重要決策有記錄

### 檔案管理
- [ ] TODO 數量 ≤ 5 個
- [ ] 總結數量每月 ≤ 5 個
- [ ] 檔案命名正確

---

## 🎯 核心原則 / Core Principles

### 1. TODO 的角色

**TODO 始終追蹤**:
- ✅ 所有等待的未完成任務
- ✅ 所有已完成任務（含完成時間）
- ✅ 任務優先級
- ✅ 下次更新時間

**TODO 是**:
- 📋 任務追蹤器
- 🎯 行動清單
- ✅ 完成記錄

---

### 2. 總結的角色

**總結始終記錄**:
- 📝 完成了什麼任務
- 📊 統計數據
- 💡 重要決策
- 🚀 下一步計劃

**總結是**:
- 📚 持續記錄
- 📖 延續紀錄
- 🔍 可回顧的歷史

---

### 3. 執行時機

**工作流在以下時機自動執行**:
1. ✅ 系列任務完成後
2. ✅ 需求審查確認後
3. ✅ 單次多任務請求完成後

**不需要**:
- ❌ 單一簡單任務
- ❌ 臨時性問答
- ❌ 只是查看檔案

---

## 📋 實施範例 / Implementation Example

### 範例情境

**用戶請求**: "完成結構優化，創建規則，更新文件"

**執行**:
1. 完成 10 個任務
2. 修改 15 個檔案
3. 創建 5 個新檔案

**工作流執行**:

```python
# Step 1: 更新 TODO
1. 檢查 .internal/planning/TODO_02_01.md
2. 存在 → 更新
3. 標記 10 個任務為 [x]
4. 移動到「已完成」section
5. 更新「最後更新」時間

# Step 2: 創建/更新總結
1. 檢查 .internal/summaries/2026-02/summary_2026-02-01_16.md
2. 存在 → 更新
3. 新增 10 個完成任務
4. 更新統計數據（15 修改 + 5 創建）
5. 記錄重要決策
6. 更新執行時間範圍
```

---

## 🎯 Summary / 總結

**Key Points**:

1. ✅ **系列任務完成 → 自動執行工作流**
2. ✅ **Step 1: 檢查並更新 TODO**
   - 當天有 TODO → 更新
   - 當天無 TODO → 創建
3. ✅ **Step 2: 檢查並創建/更新總結**
   - 當小時有總結 → 更新
   - 當小時無總結 → 創建
4. ✅ **TODO = 任務追蹤器**（追蹤待辦和已完成）
5. ✅ **總結 = 持續記錄**（延續紀錄所有工作）
6. ✅ **單次多任務請求後執行**

**This rule ensures consistent workflow for all series tasks.**  
**此規則確保所有系列任務都有一致的工作流程。**

---

## 📚 相關規則 / Related Rules

### 強依賴 (Strong Dependencies)
- **TODO_UPDATE_RULE.md** - TODO 更新規則
- **TASK_SUMMARY_RULE.md** - 任務總結規則
- **FILE_NAMING_CONVENTION_RULE.md** - 檔案命名規範
- **INTERNAL_RULE.md** - 檔案數量限制

### 相關 (Related)
- **VIBE_GUIDE.md** - 系列性任務的定義
- **DRY_RULE.md** - 避免重複

### 衝突 (Conflicts)
- ❌ 無已知衝突

---

**Created**: 2026-02-01  
**Last Updated**: 2026-02-01  
**Status**: ACTIVE  
**Priority**: CRITICAL  
**Enforcement**: MANDATORY
