---
name: planner_agent
role: Task Planning and Validation
goal: Validate and optimize task plans for efficient execution
version: 1.0.0
---

# Planner Agent

## Role & Responsibilities

The **Planner Agent** is responsible for task planning, validation, and optimization.

**規劃代理**負責任務規劃、驗證和優化。

### Primary Responsibilities

1. **Task Validation**
   - Validate task.md structure
   - Check task completeness
   - Verify task dependencies

2. **Dependency Analysis**
   - Identify task dependencies
   - Detect circular dependencies
   - Optimize execution order

3. **Effort Estimation**
   - Estimate task complexity
   - Estimate time requirements
   - Identify high-risk tasks

4. **Plan Optimization**
   - Suggest task grouping
   - Recommend parallel execution
   - Identify optimization opportunities

---

## Available Actions

### 1. validate_tasks

**Purpose**: Validate task plan

**Input**: `task.md`

**Output**: Validation report

**Example**:
```yaml
- agent: planner_agent
  action: validate_tasks
  input: task.md
  config:
    check_dependencies: true
    estimate_effort: true
```

---

### 2. create_fix_plan

**Purpose**: Create plan for bug fix

**Input**: `issue.md`

**Output**: Fix plan

**Example**:
```yaml
- agent: planner_agent
  action: create_fix_plan
  input: issue.md
  config:
    minimal_changes: true
    consider_side_effects: true
```

---

### 3. create_refactoring_plan

**Purpose**: Create refactoring plan

**Input**: Analysis results

**Output**: Refactoring plan

**Example**:
```yaml
- agent: planner_agent
  action: create_refactoring_plan
  config:
    ensure_backward_compatibility: true
    plan_incremental_steps: true
```

---

## Configuration

Default configuration in `config.yml`:

```yaml
agent:
  name: planner_agent
  version: 1.0.0
  
settings:
  max_task_depth: 5
  dependency_check: true
  effort_estimation: true
  
thresholds:
  max_complexity: 10
  max_dependencies: 5
```

---

## Tools Available

The planner agent can use:
- Task analysis tools
- Dependency graph tools
- Estimation algorithms

---

## Example Usage

```python
from agents.planner_agent.planner import PlannerAgent

agent = PlannerAgent()
result = await agent.validate_tasks('task.md')

if result['valid']:
    print(f"✅ Task plan is valid")
    print(f"   Estimated effort: {result['estimated_hours']} hours")
else:
    print(f"❌ Validation errors:")
    for error in result['errors']:
        print(f"   - {error}")
```

---

**Version**: 1.0.0  
**Status**: Active Development  
**Maintainer**: synthforge team
