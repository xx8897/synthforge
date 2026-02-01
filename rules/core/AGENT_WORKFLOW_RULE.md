# AI Agent 工作流規則 - AGENT_WORKFLOW_RULE.md
# Mandatory Workflow for AI Agents

**狀態**: MANDATORY 強制
**優先級**: CRITICAL 極高
**範圍**: 所有 AI Agent 執行的任務

---

## 🎯 規則目的 / Rule Purpose

確保 AI Agent 在執行任務前，**必須先檢查相關規則**，避免違反既定規範。

Ensure AI Agents **MUST check relevant rules** before executing tasks to avoid violating established norms.

---

## 🏗️ Architecture Integration / 架構整合

### synthforge Component Workflow / synthforge 組件工作流

Based on ARCHITECTURE.md, AI Agents must understand the component hierarchy:

基於 ARCHITECTURE.md，AI Agent 必須理解組件層次結構：

```
User Request / 用戶請求
    ↓
[Check AGENT_WORKFLOW_RULE] / [檢查 AGENT_WORKFLOW_RULE]
    ↓
Identify Component Layer / 識別組件層:
├── Rules Layer (rules/) → Check/Create rules / 檢查/創建規則
├── Infrastructure Layer (core_lib/) → Shared utilities / 共享工具
├── Development Layer (devtools/) → Development tools / 開發工具
├── Capabilities Layer (skills/, agents/) → Reusable capabilities / 可重用能力
├── Workflow Layer (workflows/) → Orchestration / 編排
└── Project Layer (projects/) → User applications / 用戶應用
    ↓
Execute Appropriate Workflow / 執行適當的工作流
```

### Component Interaction Principles / 組件交互原則

1. **Top-Down Dependency** / 上層依賴下層
   - Workflows can use Skills and Agents
   - Skills can use core_lib
   - Agents can use Skills and core_lib
   - ❌ core_lib cannot depend on Skills or Agents

2. **Horizontal Isolation** / 水平隔離
   - Skills are independent of each other
   - Agents are independent of each other
   - Workflows orchestrate but don't contain logic

3. **Rules Apply Everywhere** / 規則適用於所有層
   - All layers must follow rules/
   - Rules are checked before any operation

---

## 🔄 強制執行流程 / Mandatory Workflow


### Step 1: 接收任務 (Receive Task)

```
用戶請求任務
    ↓
理解任務類型
    ↓
進入 Step 2
```

---

### Step 2: 檢查規則 (Check Rules) ⚠️ MANDATORY

**在執行任何操作前，必須檢查以下規則**：

#### 2.1 檢查任務類型相關規則

| 任務類型 | 必須檢查的規則 |
|---------|---------------|
| **創建檔案** | FILE_NAMING_CONVENTION_RULE, FILE_CLASSIFICATION_RULE, BILINGUAL_OUTPUT_RULE |
| **修改結構** | DIRECTORY_README_RULE, VIBE_GUIDE_SYNC_RULE |
| **編寫程式碼** | CODING_STYLE_RULE, TOOLING_USAGE_RULE, SINGLE_SOURCE_OF_TRUTH_RULE |
| **開始新功能** | SPEC_DRIVEN_DEVELOPMENT_RULE |
| **系列任務完成** | SERIES_TASK_WORKFLOW_RULE, TASK_SUMMARY_RULE, TODO_UPDATE_RULE |
| **使用 .internal/** | INTERNAL_RULE |
| **提取知識** | KNOWLEDGE_BASE_RULE |
| **創建分析文檔** | FILE_CLASSIFICATION_RULE (analysis → .internal/analysis/) |
| **創建 Workflow** | WORKFLOW_RULE (workflows/templates/ or workflows/examples/) |
| **執行 Workflow** | WORKFLOW_RULE + AGENT_WORKFLOW_RULE |

**⚠️ 重要檔案分類規則**:
- **Analysis 文檔** → `.internal/analysis/` (分析、研究、設計方案)
- **Planning 文檔** → `.internal/planning/` (TODO, 對話總結)
- **Summary 文檔** → `.internal/summaries/` (任務總結)
- **Knowledge 文檔** → `.internal/knowledge/` (概念、最佳實踐)
- **Workflow 文檔** → `workflows/templates/` (可重用模板) 或 `workflows/examples/` (範例)

**避免重複文檔**: 同一主題只創建一個文檔，不要創建 summary + analysis

### Workflow-Specific Task Types / Workflow 特定任務類型

| 任務類型 | Workflow 模板 | 所需組件 |
|---------|--------------|---------|
| **新功能開發** | feature_development.yml | Spec → Tasks → Skills → Agents → Review |
| **Bug 修復** | bug_fix.yml | Issue → Diagnosis → Fix → Test |
| **重構** | refactoring.yml | Analysis → Plan → Refactor → Verify |
| **規則創建** | rule_creation.yml | Research → Draft → Review → Integrate |

**使用方式**:
```bash
# 執行 workflow
python devtools/cli.py workflow run workflows/templates/feature_development.yml

# 驗證 workflow
python devtools/cli.py workflow validate workflows/templates/feature_development.yml
```

#### 2.2 檢查通用規則（每次都檢查）

- ✅ DRY_RULE - 避免重複
- ✅ SINGLE_SOURCE_OF_TRUTH_RULE - 確保 SSOT

---

### Step 3: 執行任務 (Execute Task)

```
規則檢查完成
    ↓
按照規則執行任務
    ↓
進入 Step 4
```

---

### Step 4: 驗證與記錄 (Verify & Record)

```
任務執行完成
    ↓
驗證是否符合規則
    ↓
如果是系列任務 → 創建任務總結
    ↓
更新 TODO
```

---

## 🚨 違規處理 / Violation Handling

### 如果發現違反規則

1. **立即停止** 當前操作
2. **檢查規則** 確認正確做法
3. **修正錯誤** 按照規則重新執行
4. **向用戶說明** 錯誤原因和修正方式

---

## ✅ 執行檢查清單 / Execution Checklist

在執行任務前，確認：

- [ ] **已識別任務類型**
- [ ] **已檢查相關規則**（見 Step 2.1 表格）
- [ ] **已檢查通用規則**（DRY, SSOT）
- [ ] **已理解規則要求**
- [ ] **執行方式符合規則**

在任務完成後，確認：

- [ ] **結果符合規則要求**
- [ ] **如果是系列任務，已創建任務總結**
- [ ] **已更新 TODO**（如適用）

---

## 📚 規則優先級 / Rule Priority

**優先順序**：

1. **Rules** (強制性規範) - 必須遵守
2. **Skills** (可選能力) - 參考使用
3. **個人判斷** - 在規則範圍內靈活應用

**記住**：
- ✅ Rules 定義「必須怎麼做」
- ✅ Skills 提供「可以怎麼做」
- ❌ 永遠不要違反 Rules

---

## 🎯 Summary / 總結

**Key Points**:

1. ✅ **執行前必須檢查規則** - 根據任務類型查表
2. ✅ **Rules 優先於 Skills** - 強制性 > 可選性
3. ✅ **違規立即修正** - 不要繼續錯誤的操作
4. ✅ **任務完成後驗證** - 確保符合規則

**This rule ensures AI Agents always follow established norms.**  
**此規則確保 AI Agent 始終遵循既定規範。**

---

## 📚 相關規則 / Related Rules

### 強依賴 (Strong Dependencies)
- **所有其他 Rules** - 本規則是執行其他規則的入口

### 相關 (Related)
- **VIBE_GUIDE.md** - Agent 導航入口
- **SERIES_TASK_WORKFLOW_RULE** - 系列任務流程

---

**創建時間**: 2026-02-01
**狀態**: ACTIVE
**優先級**: CRITICAL
**強制執行**: MANDATORY
