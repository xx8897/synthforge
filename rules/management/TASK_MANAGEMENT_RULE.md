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

## 🔄 Lifecycle & AI Interaction / 生命週期與 AI 互動

### 1. Initialization / 初始化
Before starting any significant work, the **Planner Agent** (or the AI) MUST generate a task breakdown in `task.md`.

### 2. Real-time Updates / 即時更新
As the **Executor Agent** works:
1.  **Start**: Mark task as `[/]`.
2.  **Finish**: Mark task as `[x]`.
3.  **Cross-Reference**: Use the completed task name in Git commit messages (enabled by `SummarySkill`).

### 3. Archive / 歸檔
When all tasks in `task.md` are marked `[x]`, the agent MUST:
1.  Perform a final "Smart Commit".
2.  Archive the completed `task.md` to `.internal/planning_archive/` (optional, based on project size).

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
