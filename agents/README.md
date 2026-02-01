# Agents - AI Agents for Workflow Automation

**Purpose**: AI agents with specific roles for automated development  
**用途**: 具有特定角色的 AI 代理，用於自動化開發

---

## 🎯 What are Agents?

**Agents** are stateful, decision-making entities that orchestrate complex tasks in workflows.

**代理**是有狀態、具決策能力的實體，在工作流中編排複雜任務。

### Agents vs Skills

| Aspect | Agents | Skills |
|--------|--------|--------|
| **State** | Stateful (maintain context) | Stateless (pure functions) |
| **Decision Making** | Yes (AI-powered) | No (deterministic) |
| **Complexity** | High (orchestration) | Low (single task) |
| **Usage** | Workflow orchestration | Task execution |

---

## 📁 Available Agents

### 1. planner_agent
**Role**: Task planning and validation  
**角色**: 任務規劃與驗證

**Responsibilities**:
- Validate task plans
- Analyze dependencies
- Estimate effort
- Optimize task order

---

### 2. executor_agent
**Role**: Code execution with TDD  
**角色**: 使用 TDD 執行代碼

**Responsibilities**:
- Implement tasks using TDD
- Manage Git worktrees
- Track progress
- Handle errors

---

### 3. reviewer_agent
**Role**: Code review and quality assurance  
**角色**: 代碼審查與質量保證

**Responsibilities**:
- Review code changes
- Check against rules
- Verify tests
- Provide improvement suggestions

---

## 🔧 How to Use in Workflows

```yaml
phases:
  plan:
    - agent: planner_agent
      action: validate_tasks
      input: task.md
      
  execute:
    - agent: executor_agent
      action: implement_tasks
      mode: TDD
      
  review:
    - agent: reviewer_agent
      action: code_review
      config:
        checks: [style, security, performance]
```

---

## 🏗️ Agent Structure

Each agent follows this structure:

```
agents/[agent_name]/
├── AGENT.md              # Agent definition and documentation
├── config.yml            # Agent configuration
├── [agent_name].py       # Main agent implementation
├── prompts/              # System prompts (optional)
└── tools/                # Agent-specific tools (optional)
```

---

## 📚 Agent Lifecycle

```
1. Initialize → Load config and prompts
2. Receive Task → Get task from workflow
3. Plan → Decide on approach
4. Execute → Perform actions (using skills)
5. Report → Return results to workflow
```

---

## 🔗 Integration with Workflow Engine

Agents are loaded and executed by `workflows/engine/executor.py`:

```python
# Workflow executor loads agent
agent = load_agent('planner_agent')

# Execute agent action
result = await agent.execute(
    action='validate_tasks',
    input='task.md',
    context=execution_context
)
```

---

**Created**: 2026-02-01  
**Status**: Active Development  
**Maintainer**: synthforge team
