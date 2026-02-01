# SPEC_DRIVEN_DEVELOPMENT_RULE.md - Spec-Driven Development Rule
# From Specification to Implementation

**Status**: MANDATORY 強制
**Priority**: CRITICAL 關鍵
**Scope**: All features and complex tasks

---

## 🎯 規則目的 / Rule Purpose

建立「規格驅動開發」(SDD) 的標準工作流，確保在編寫任何程式碼之前，先有清晰、經確認的規格。
整合 "Spec-as-Source" 概念，讓文件成為程式碼的真實來源。

Establish Spec-Driven Development (SDD) workflow to ensure specific, confirmed specifications exist before coding.
Integrate "Spec-as-Source" concept, making documentation the source of truth for code.

---

## 🔄 SDD Workflow / SDD 工作流程

### Step 1: Specify (定義規格)
- **Action**: Create `implementation_plan.md` (or update existing).
- **Content**:
    - **Goal**: What are we building?
    - **Context**: Why are we building it?
    - **Proposed Changes**: Exact files to create/modify.
    - **Design**: Data structures, API signatures, algorithms.
- **動作**: 創建或更新 `implementation_plan.md`。
- **內容**: 目標、背景、預計變更、詳細設計。

### Step 2: Clarify & Review (釐清與審查)
- **Action**: Ask USER to review the plan.
- **Tool**: `notify_user`
- **Rule**: DO NOT proceed to coding until plan is approved.
- **動作**: 請求用戶審查計畫。
- **規則**: 未獲批准絕不開始編碼。

### Step 3: Spec-as-Source (規格即源碼)
- **Concept**: The plan IS the code structure.
- **Action**: Generate file skeletons, strictures, and tests directly from the plan.
- **概念**: 計畫即是程式碼結構。
- **動作**: 直接從計畫生成檔案骨架、結構和測試。

### Step 4: Tasks (任務細分)
- **Action**: Break down plan into `task.md` checklist.
- **Granularity**: Each task should be atomic (e.g., "Create class X", "Add method Y").
- **動作**: 將計畫分解為 `task.md` 檢查清單。
- **粒度**: 每個任務應是原子的。

### Step 5: Implement (實作)
- **Action**: Write code following the spec strictly.
- **Mode**: EXECUTION
- **動作**: 嚴格依照規格編寫程式碼。

### Step 6: Verify (驗證)
- **Action**: Run tests defined in the spec.
- **Artifact**: Create `walkthrough.md` to demonstrate results.
- **動作**: 執行規格中定義的測試。
- **產出**: 創建 `walkthrough.md` 展示結果。

---

## 📄 Implementation Plan Format / 實施計畫格式

```markdown
# Implementation Plan - [Feature Name]

## 🎯 Goal
[Description]

## ⚙️ Design & Specifications
- **Class**: `MyClass`
    - `method_a(arg: int) -> bool`: Description...
- **API**: `/api/v1/resource` (GET)

## 📂 Proposed File Changes
### [NEW] path/to/file.py
- Implement `MyClass`
- Add validation logic

## ✅ Verification Plan
- [ ] Unit test: `test_method_a`
- [ ] Manual check: ...
```

---

## 🤖 Spec-as-Source Integration

**Why**: To avoid "Hallucinated Implementation" where AI forgets the plan while coding.
**How**:
1. Keep `implementation_plan.md` open.
2. Refer to it in EVERY code generation step.
3. If code must deviate from spec -> **Update spec FIRST**.

**為什麼**: 避免「幻覺實作」，即 AI 在編碼時忘記計畫。
**如何**:
1. 保持 `implementation_plan.md` 開啟。
2. 在每個程式碼生成步驟都參考它。
3. 如果程式碼必須偏離規格 -> **先更新規格**。

---

## ✅ Checklist / 檢查清單

Before starting to code:
- [ ] Is `implementation_plan.md` created?
- [ ] Does it contain detailed API/Data designs?
- [ ] Has the user approved the plan?
- [ ] Is `task.md` updated with breakdown?

Before finishing:
- [ ] Did implementation follow the plan exactly?
- [ ] If changed, was the plan updated?

---

**Created**: 2026-02-01
**Status**: ACTIVE
**Enforcement**: MANDATORY
