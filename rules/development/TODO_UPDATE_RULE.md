# TODO_UPDATE_RULE.md - TODO 更新規則

**Status**: MANDATORY 強制  
**Priority**: CRITICAL 極高  
**Scope**: All series tasks 所有系列性任務  
**Version**: 1.0  
**Created**: 2026-02-01

---

## 🎯 規則目的 / Rule Purpose

確保 TODO 在系列性問答確認後進行更新：
1. **保持 TODO 最新** - 反映當前計劃和進度
2. **避免過時資訊** - 刪除已完成或不再相關的項目
3. **明確下一步** - 清楚標記接下來要做什麼
4. **追蹤進度** - 知道完成了多少，還剩多少

Ensure TODO is updated after series Q&A confirmation:
1. **Keep TODO current** - Reflect current plans and progress
2. **Avoid stale info** - Remove completed or irrelevant items
3. **Clear next steps** - Clearly mark what to do next
4. **Track progress** - Know how much is done and remaining

---

## 📋 何時更新 TODO / When to Update TODO

### 必須更新 (MUST Update)

**觸發條件**:
1. ✅ **系列性問答確認後** - 用戶確認計劃或方向
2. ✅ **任務總結創建後** - 完成系列性任務
3. ✅ **計劃變更時** - 新增、刪除或修改計劃
4. ✅ **階段完成時** - 完成一個 Phase 或 Milestone

**範例**:
- ✅ 用戶確認實施計劃 → 更新 TODO
- ✅ 完成結構優化 → 更新 TODO
- ✅ 決定暫緩某些任務 → 更新 TODO

---

### 不需要更新 (NO Update)

**情況**:
1. ❌ 單一簡單任務（如修改一個檔案）
2. ❌ 臨時性問答（如解釋概念）
3. ❌ TODO 本身就是最新的

---

## 📝 TODO 格式 / TODO Format

### 檔案命名

**格式**: `TODO_MM_DD.md`

**範例**: `TODO_02_01.md` (2 月 1 日)

**位置**: `.internal/planning/`

**限制**: 最多 5 個 TODO 檔案（見 INTERNAL_RULE.md）

---

### 內容結構

```markdown
# TODO - YYYY-MM-DD

**創建日期**: YYYY-MM-DD  
**最後更新**: YYYY-MM-DD HH:MM  
**狀態**: ⏳ 進行中 / ✅ 完成

---

## 🔴 高優先級 (High Priority)

- [ ] [任務 1] - 預計: X 小時
- [ ] [任務 2] - 預計: Y 小時

---

## 🟡 中優先級 (Medium Priority)

- [ ] [任務 3]
- [ ] [任務 4]

---

## 🟢 低優先級 (Low Priority)

- [ ] [任務 5]
- [ ] [任務 6]

---

## ⏸️ 暫緩 (On Hold)

- [ ] [任務 7] - 原因: [說明]

---

## ✅ 已完成 (Completed)

- [x] [任務 8] - 完成時間: YYYY-MM-DD
- [x] [任務 9] - 完成時間: YYYY-MM-DD

---

## 📝 備註 (Notes)

[重要備註或上下文]

---

**下次更新**: YYYY-MM-DD
```

---

## 🔄 更新流程 / Update Flow

### Step 1: 觸發更新

```
系列性問答確認
    ↓
或
任務總結創建
    ↓
檢查 TODO 是否需要更新
    ↓
是 → 執行更新流程
```

---

### Step 2: 更新 TODO

```python
# 更新步驟
1. 讀取最新的 TODO_MM_DD.md
2. 標記已完成任務為 [x]
3. 移動已完成任務到「已完成」section
4. 新增新任務（如有）
5. 調整優先級（如需要）
6. 更新「最後更新」時間
7. 保存檔案
```

---

### Step 3: 清理舊 TODO

**規則**: 最多保留 5 個 TODO 檔案

```python
# 清理流程
1. 檢查 .internal/planning/ 中的 TODO 數量
2. 如果 > 5:
   - 找出最老的 TODO
   - 檢查狀態:
     - ✅ 完成 → 刪除
     - ⏳ 進行中 → 請示用戶
   - 刪除後重新檢查
```

---

## ✅ 檢查清單 / Checklist

更新 TODO 時，確認：

- [ ] 已完成任務標記為 [x]
- [ ] 已完成任務移到「已完成」section
- [ ] 新任務已新增
- [ ] 優先級正確
- [ ] 「最後更新」時間已更新
- [ ] 備註有更新（如需要）
- [ ] TODO 數量 ≤ 5 個
- [ ] **已創建任務總結**（如適用）

---

## 🎯 Summary / 總結

**Key Points**:

1. ✅ **系列性問答確認後 → 必須更新 TODO**
2. ✅ **任務總結創建後 → 必須更新 TODO**
3. ✅ **格式**: `TODO_MM_DD.md`
4. ✅ **位置**: `.internal/planning/`
5. ✅ **限制**: 最多 5 個 TODO 檔案
6. ✅ **重要**: 與 TASK_SUMMARY_RULE 配合使用

**This rule ensures TODO stays current and actionable.**  
**此規則確保 TODO 保持最新和可執行。**

---

## 📚 相關規則 / Related Rules

### 強依賴 (Strong Dependencies)
- **TASK_SUMMARY_RULE.md** - 任務總結創建後必須更新 TODO
- **INTERNAL_RULE.md** - TODO 檔案數量限制（最多 5 個）
- **FILE_NAMING_CONVENTION_RULE.md** - TODO 檔案命名規範

### 相關 (Related)
- **VIBE_GUIDE.md** - 系列性任務的定義
- **DRY_RULE.md** - 避免 TODO 重複

### 衝突 (Conflicts)
- ❌ 無已知衝突

---

**Created**: 2026-02-01  
**Last Updated**: 2026-02-01  
**Status**: ACTIVE  
**Priority**: CRITICAL  
**Enforcement**: MANDATORY
