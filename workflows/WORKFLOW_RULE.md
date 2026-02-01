# WORKFLOW_RULE.md - Workflow 創建與執行規則

**Status**: MANDATORY 強制  
**Priority**: HIGH 高  
**Scope**: workflows/ 目錄的所有操作  
**Version**: 1.0  
**Created**: 2026-02-01

---

## 🎯 規則目的 / Rule Purpose

建立統一的 Workflow 創建和執行規範，確保：
1. **一致性** - 所有 Workflows 遵循相同格式
2. **可維護性** - Workflows 易於理解和修改
3. **可擴展性** - 易於添加新的 Skills 和 Agents
4. **可測試性** - Workflows 可被驗證和測試

Establish unified Workflow creation and execution standards to ensure:
1. **Consistency** - All workflows follow the same format
2. **Maintainability** - Workflows are easy to understand and modify
3. **Extensibility** - Easy to add new Skills and Agents
4. **Testability** - Workflows can be validated and tested

---

## 📋 Workflow 格式規範 / Workflow Format Specification

### 基本結構 / Basic Structure

```yaml
name: Workflow Name
description: Brief description of what this workflow does
version: 1.0.0
author: optional
tags: [tag1, tag2]  # optional

# Workflow configuration
config:
  timeout: 3600  # seconds, optional
  retry: 3       # retry count, optional
  
# Workflow phases (sequential execution)
phases:
  phase_name_1:
    - skill: skill_name
      input: input_file.md
      output: output_file.json
      config:
        param1: value1
        
  phase_name_2:
    - agent: agent_name
      action: action_name
      mode: execution_mode
      config:
        param1: value1
```

### 必填欄位 / Required Fields

- `name`: Workflow 名稱（字串）
- `phases`: 執行階段（字典）

### 可選欄位 / Optional Fields

- `description`: 描述（字串）
- `version`: 版本號（字串，建議使用 semver）
- `author`: 作者（字串）
- `tags`: 標籤（陣列）
- `config`: 配置（字典）

---

## 📝 命名規範 / Naming Conventions

### Workflow 檔案命名

**格式**: `[purpose]_[type].yml`

**範例**:
```
✅ feature_development.yml
✅ bug_fix.yml
✅ refactoring.yml
✅ rule_creation.yml
✅ simple_feature.yml

❌ FeatureDevelopment.yml  (不使用 PascalCase)
❌ feature-development.yml (不使用 kebab-case)
❌ feature.yml             (太簡短，不清楚)
```

### Phase 命名

**格式**: `[action]` 或 `[step_number]_[action]`

**範例**:
```yaml
phases:
  specify:      # ✅ 簡潔的動詞
  plan:         # ✅
  execute:      # ✅
  test:         # ✅
  review:       # ✅
  
  1_specify:    # ✅ 帶編號（用於複雜 workflow）
  2_plan:       # ✅
  
  ❌ phase1:    # 不清楚
  ❌ doStuff:   # 不專業
```

### Skill/Agent 命名

**格式**: `[noun]_[action]` 或 `[role]_agent`

**範例**:
```yaml
# Skills
skill: spec_parser      # ✅
skill: task_generator   # ✅
skill: test_runner      # ✅

# Agents
agent: planner_agent    # ✅
agent: executor_agent   # ✅
agent: reviewer_agent   # ✅
```

---

## 🔄 Workflow 執行規則 / Workflow Execution Rules

### 1. 順序執行 / Sequential Execution

**規則**: Phases 按定義順序執行

```yaml
phases:
  phase_1:  # 先執行
    - skill: skill_a
  phase_2:  # 後執行
    - skill: skill_b
```

### 2. Phase 內並行 / Parallel Within Phase

**規則**: 同一 Phase 內的 steps 可並行執行（如果獨立）

```yaml
phases:
  analyze:
    - skill: code_analyzer    # 可並行
    - skill: security_scanner # 可並行
```

### 3. 錯誤處理 / Error Handling

**規則**: 任何 step 失敗，整個 workflow 停止

```yaml
config:
  retry: 3           # 失敗時重試次數
  continue_on_error: false  # 是否繼續（預設 false）
```

### 4. 超時控制 / Timeout Control

**規則**: 每個 workflow 和 step 都可設定超時

```yaml
config:
  timeout: 3600  # Workflow 總超時（秒）
  
phases:
  execute:
    - agent: executor_agent
      config:
        timeout: 1800  # Step 超時（秒）
```

---

## 📂 檔案位置規範 / File Location Rules

### Workflow 模板 / Workflow Templates

**位置**: `workflows/templates/`

**用途**: 可重用的標準 workflows

**範例**:
- `feature_development.yml`
- `bug_fix.yml`
- `refactoring.yml`

### Workflow 範例 / Workflow Examples

**位置**: `workflows/examples/`

**用途**: 學習和參考的簡單範例

**範例**:
- `simple_feature.yml`
- `hello_world.yml`

### 自定義 Workflows / Custom Workflows

**位置**: `workflows/custom/` 或專案目錄

**用途**: 專案特定的 workflows

---

## ✅ Workflow 驗證 / Workflow Validation

### 必須驗證項目 / Required Validations

1. **YAML 語法正確** - 可被解析
2. **必填欄位存在** - name, phases
3. **Skills 存在** - 引用的 skills 在 `skills/` 中
4. **Agents 存在** - 引用的 agents 在 `agents/` 中
5. **輸入輸出匹配** - Phase 間的資料流正確

### 驗證命令 / Validation Command

```bash
python devtools/cli.py workflow validate workflows/templates/feature_development.yml
```

### 驗證輸出 / Validation Output

```
✅ YAML syntax valid
✅ Required fields present
✅ All skills exist
✅ All agents exist
✅ Data flow valid

Workflow is valid and ready to execute.
```

---

## 🎯 最佳實踐 / Best Practices

### 1. 保持簡單 / Keep It Simple

```yaml
# ✅ Good: 清晰的目的
name: Feature Development
phases:
  specify:
    - skill: spec_parser
  execute:
    - agent: executor_agent

# ❌ Bad: 過於複雜
name: Super Complex Multi-Stage Development Pipeline
phases:
  pre_pre_processing:
    - skill: thing1
    - skill: thing2
  # ... 10 more phases
```

### 2. 使用描述性名稱 / Use Descriptive Names

```yaml
# ✅ Good
name: Bug Fix Workflow
description: Automate bug fixing from diagnosis to verification

# ❌ Bad
name: Workflow 1
description: Does stuff
```

### 3. 文檔化配置 / Document Configuration

```yaml
phases:
  execute:
    - agent: executor_agent
      config:
        mode: TDD  # Use Test-Driven Development
        coverage_threshold: 80  # Minimum test coverage
```

### 4. 版本控制 / Version Control

```yaml
name: Feature Development
version: 1.2.0  # 使用 semver
# 1.0.0 -> 1.1.0: 新增 test phase
# 1.1.0 -> 1.2.0: 新增 review phase
```

---

## 🔗 與其他規則的整合 / Integration with Other Rules

### 與 AGENT_WORKFLOW_RULE 的關係

**AGENT_WORKFLOW_RULE**: 定義 AI Agent 如何執行任務  
**WORKFLOW_RULE**: 定義 Workflow 如何被創建和執行

**整合點**:
- AI Agent 使用 AGENT_WORKFLOW_RULE 決定執行哪個 Workflow
- Workflow 使用 WORKFLOW_RULE 定義執行流程

### 與 SPEC_DRIVEN_DEVELOPMENT 的關係

**SDD**: 定義如何從 Spec 開始開發  
**Workflow**: 自動化 SDD 流程

**整合點**:
```yaml
# feature_development.yml 實現 SDD
phases:
  specify:
    - skill: spec_parser
      input: implementation_plan.md  # SDD 的 Spec
  plan:
    - skill: task_generator
      output: task.md  # SDD 的 Tasks
```

---

## 📚 範例 / Examples

### 範例 1: 簡單 Feature Workflow

```yaml
name: Simple Feature Development
description: Basic feature development workflow
version: 1.0.0

phases:
  parse:
    - skill: spec_parser
      input: implementation_plan.md
      output: spec.json
      
  generate:
    - skill: task_generator
      input: spec.json
      output: task.md
      
  execute:
    - agent: executor_agent
      action: implement_tasks
      mode: TDD
```

### 範例 2: Bug Fix Workflow

```yaml
name: Bug Fix Workflow
description: Automated bug fixing workflow
version: 1.0.0

phases:
  diagnose:
    - agent: diagnostic_agent
      action: analyze_issue
      input: issue.md
      
  fix:
    - agent: executor_agent
      action: implement_fix
      mode: TDD
      
  verify:
    - skill: test_runner
      action: run_tests
      config:
        coverage_threshold: 80
```

---

## 🚨 常見錯誤 / Common Mistakes

### 錯誤 1: 缺少必填欄位

```yaml
# ❌ Bad: 缺少 name
phases:
  execute:
    - skill: something

# ✅ Good
name: My Workflow
phases:
  execute:
    - skill: something
```

### 錯誤 2: 引用不存在的 Skill/Agent

```yaml
# ❌ Bad: non_existent_skill 不存在
phases:
  execute:
    - skill: non_existent_skill

# ✅ Good: 使用存在的 skill
phases:
  execute:
    - skill: spec_parser  # 存在於 skills/workflow_skills/spec_parser/
```

### 錯誤 3: 資料流不匹配

```yaml
# ❌ Bad: phase_2 需要 spec.json，但 phase_1 輸出 task.md
phases:
  phase_1:
    - skill: skill_a
      output: task.md
  phase_2:
    - skill: skill_b
      input: spec.json  # 不匹配！

# ✅ Good: 資料流匹配
phases:
  phase_1:
    - skill: skill_a
      output: spec.json
  phase_2:
    - skill: skill_b
      input: spec.json
```

---

## 📋 檢查清單 / Checklist

創建 Workflow 時，確認：

- [ ] **檔案命名正確** (`[purpose]_[type].yml`)
- [ ] **必填欄位存在** (name, phases)
- [ ] **Phase 命名清晰** (動詞或編號+動詞)
- [ ] **Skills/Agents 存在** (已驗證)
- [ ] **資料流正確** (輸入輸出匹配)
- [ ] **已添加描述** (description 欄位)
- [ ] **已驗證** (`workflow validate`)
- [ ] **已測試** (執行過至少一次)

---

## 🔗 相關規則 / Related Rules

### 強依賴 (Strong Dependencies)
- **[AGENT_WORKFLOW_RULE.md](../rules/core/AGENT_WORKFLOW_RULE.md)** - AI Agent 工作流規則
- **[WORKFLOW_INTEGRATION_RULE.md](../rules/development/WORKFLOW_INTEGRATION_RULE.md)** - Skills/Agents 整合標準
- **[FILE_NAMING_CONVENTION_RULE.md](../rules/development/FILE_NAMING_CONVENTION_RULE.md)** - 檔案命名規範

### 相關 (Related)
- **[SPEC_DRIVEN_DEVELOPMENT_RULE.md](../rules/core/SPEC_DRIVEN_DEVELOPMENT_RULE.md)** - Spec 驅動開發
- **[TDD_RULE.md](../rules/development/TDD_RULE.md)** - 測試驅動開發規範
- **[AGENT_STRUCTURE_RULE.md](../rules/development/AGENT_STRUCTURE_RULE.md)** - Agent 結構規範
- **[CODING_STYLE_RULE.md](../rules/development/CODING_STYLE_RULE.md)** - 程式碼風格（用於 workflow engine）

### 文檔 (Documentation)
- **[Workflow Usage Guide](../docs/guides/WORKFLOW_GUIDE.md)** - 完整使用指南
- **[GitHub Superpowers](../docs/architecture/GITHUB_SUPERPOWERS.md)** - 系統架構說明
- **[Git Worktrees Guide](../docs/guides/GIT_WORKTREES_GUIDE.md)** - Git Worktrees 使用指南

---

**Created**: 2026-02-01  
**Last Updated**: 2026-02-01  
**Status**: ACTIVE  
**Priority**: HIGH  
**Enforcement**: MANDATORY
