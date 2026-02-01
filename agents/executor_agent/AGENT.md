---
name: executor_agent
role: Code Execution with TDD
goal: Implement tasks using Test-Driven Development
version: 1.0.0
---

# Executor Agent

## Role & Responsibilities

The **Executor Agent** is responsible for implementing tasks using Test-Driven Development (TDD).

**執行代理**負責使用測試驅動開發（TDD）實施任務。

### Primary Responsibilities

1. **TDD Implementation**
   - Write tests first
   - Implement code to pass tests
   - Refactor with confidence

2. **Git Worktree Management**
   - Create isolated worktrees
   - Manage branches
   - Clean up after completion

3. **Progress Tracking**
   - Track task completion
   - Report progress
   - Handle errors gracefully

4. **Code Quality**
   - Follow coding standards
   - Ensure test coverage
   - Write clean code

---

## Available Actions

### 1. implement_tasks

**Purpose**: Implement tasks from task.md using TDD

**Input**: `task.md`

**Mode**: `TDD` (Test-Driven Development)

**Example**:
```yaml
- agent: executor_agent
  action: implement_tasks
  mode: TDD
  input: task.md
  config:
    test_first: true
    coverage_threshold: 80
    follow_coding_style: true
```

---

### 2. implement_fix

**Purpose**: Implement bug fix with tests

**Input**: Fix plan

**Example**:
```yaml
- agent: executor_agent
  action: implement_fix
  mode: TDD
  config:
    test_first: true
    add_regression_test: true
```

---

### 3. execute_refactoring

**Purpose**: Execute refactoring incrementally

**Mode**: `incremental`

**Example**:
```yaml
- agent: executor_agent
  action: execute_refactoring
  mode: incremental
  config:
    preserve_behavior: true
    run_tests_after_each_step: true
```

---

## Configuration

Default configuration in `config.yml`:

```yaml
agent:
  name: executor_agent
  version: 1.0.0
  
settings:
  tdd_mode: true
  test_first: true
  coverage_threshold: 80
  
git:
  use_worktrees: true
  auto_commit: true
  commit_message_template: "feat: {task_description}"
```

---

## TDD Workflow

```
1. Read Task → Understand requirements
2. Write Test → Red (failing test)
3. Implement → Green (passing test)
4. Refactor → Clean up code
5. Repeat → Next task
```

---

## Tools Available

The executor agent can use:
- Test runner skill
- Git automation tools
- Code formatting tools
- Linting tools

---

## Example Usage

```python
from agents.executor_agent.executor import ExecutorAgent

agent = ExecutorAgent()
result = await agent.implement_tasks(
    'task.md',
    mode='TDD',
    coverage_threshold=80
)

if result['success']:
    print(f"✅ Implemented {result['completed_tasks']} tasks")
    print(f"   Coverage: {result['coverage']}%")
```

---

**Version**: 1.0.0  
**Status**: Active Development  
**Maintainer**: synthforge team
