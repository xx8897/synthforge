# TASK_MANAGEMENT_RULE - Standards for Progress Tracking
# TASK_MANAGEMENT_RULE - 進度追蹤標準化規則

**Status**: MANDATORY  
**Priority**: CRITICAL (10/10)  
**Version**: 1.0  

---

## 🎯 Purpose / 目的

Define the role, structure, and lifecycle of `task.md` as the primary coordination point between Humans and AI Agents. This ensures that the current state of work is always visible and actionable.

定義 `task.md` 的角色、結構和生命週期，將其作為人類與 AI 代理之間的主要協調點。這確保了工作當前狀態始終可見且可操作。

---

## 📋 Standard Structure / 標準結構

`task.md` MUST follow this Markdown structure:

### 1. Header / 標題
- Title of the current objective.

### 2. Status Indicators / 狀態指示器
- `[ ]`: Pending / 待處理
- `[/]`: In-progress / 處理中
- `[x]`: Completed / 已完成

### 3. Sections / 區段
Organize tasks by logical phases (e.g., Planning, Execution, Verification). Each phase should have nested items.

---

## 🔄 Lifecycle & Reset Protocol / 生命週期與重置協議

### 1. Distinction Strategy / 區分策略
- **Combat Zone (`task.md`)**:
    - **Scope**: Immediate, tactical objectives (1-2 days max).
    - **Content**: Detailed operational steps.
    - **Focus**: "What am I executing *right now*?"
- **War Room (`.internal/planning/TODO_*.md`)**:
    - **Scope**: Long-term, strategic roadmap.
    - **Content**: High-level features and milestones.
    - **Focus**: "What is the *next* battle?"

### 2. When to Reset? / 何時重置？
Reset `task.md` ONLY when the current objective is **fully verified**.

**Trigger Conditions**:
1.  All items in `task.md` are marked `[x]`.
2.  The "Smart Commit" for the finished task has been verified.
3.  You are ready to pull the next item from the **War Room**.

### 3. Archive & Sync Workflow / 歸檔與同步流程
1.  **Archive**: Move current `task.md` content to `.internal/planning_archive/{Date}_{TaskName}.md`.
2.  **Sync**: Read `.internal/planning/TODO_*.md`.
3.  **Draft**: Select the next high-priority item and write a new plan into `task.md`.
4.  **Update**: If new discoveries were made, update the **War Room** documents before starting.

**Automated Command** (Recommended):
```bash
python devtools/cli.py task archive
```

---

## 📍 Location / 位置

- **Active Task**: `task.md` (Root directory for maximum visibility).
- **Future/Secondary Tasks**: `.internal/planning/TODO_*.md`.

---

## 🔗 Related Rules / 相關規則
- [GIT_EXECUTION_RULE](rules/development/GIT_EXECUTION_RULE.md)
- [SMART_GIT_RULE](rules/development/SMART_GIT_RULE.md)
- [GRAPH_RELATIONSHIP_RULE](rules/management/GRAPH_RELATIONSHIP_RULE.md)

---

**Last Updated**: 2026-02-02  
**Maintainer**: xx8897
