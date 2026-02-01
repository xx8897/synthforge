# Workflow System - synthforge

**Version**: 1.0  
**Created**: 2026-02-01  
**Status**: Active Development

---

## 🎯 What is the Workflow System?

The **Workflow System** is synthforge's automation framework that orchestrates **Skills** and **Agents** to execute complex development tasks automatically.

**工作流系統**是 synthforge 的自動化框架，編排**技能**和**代理**以自動執行複雜的開發任務。

---

## 📋 Core Concepts

### Workflows (工作流)
**Definition**: YAML-based declarative specifications that define task execution sequences.

**定義**: 基於 YAML 的聲明式規範，定義任務執行序列。

**Example**:
```yaml
name: Feature Development
phases:
  specify:
    - skill: spec_parser
      input: implementation_plan.md
  execute:
    - agent: executor_agent
      mode: TDD
```

### Skills (技能)
**Definition**: Stateless, reusable functions that perform specific tasks.

**定義**: 無狀態、可重用的函數，執行特定任務。

**Examples**: `spec_parser`, `task_generator`, `test_runner`

### Agents (代理)
**Definition**: Stateful, decision-making entities that orchestrate complex tasks.

**定義**: 有狀態、具決策能力的實體，編排複雜任務。

**Examples**: `planner_agent`, `executor_agent`, `reviewer_agent`

---

## 📁 Directory Structure

```
workflows/
├── README.md                          # This file
├── WORKFLOW_RULE.md                   # Workflow creation rules
├── templates/                         # Workflow templates
│   ├── feature_development.yml        # Feature development workflow
│   ├── bug_fix.yml                    # Bug fix workflow
│   ├── refactoring.yml                # Refactoring workflow
│   └── rule_creation.yml              # Rule creation workflow
├── engine/                            # Workflow execution engine
│   ├── __init__.py
│   ├── parser.py                      # YAML parser
│   ├── executor.py                    # Workflow executor
│   ├── context.py                     # Execution context
│   └── validators.py                  # Workflow validators
└── examples/                          # Example workflows
    └── simple_feature.yml             # Simple feature example
```

---

## 🚀 Quick Start

### 1. View Available Workflows

```bash
python devtools/cli.py workflow list
```

### 2. Run a Workflow

```bash
python devtools/cli.py workflow run workflows/templates/feature_development.yml
```

### 3. Validate a Workflow

```bash
python devtools/cli.py workflow validate workflows/templates/feature_development.yml
```

---

## 📝 Creating a Workflow

### Step 1: Define Workflow Structure

Create a YAML file in `workflows/templates/` or `workflows/examples/`:

```yaml
name: My Custom Workflow
description: Brief description of what this workflow does
version: 1.0.0

phases:
  phase_1:
    - skill: skill_name
      input: input_file.md
      output: output_file.json
      
  phase_2:
    - agent: agent_name
      action: action_name
      config:
        param1: value1
```

### Step 2: Validate

```bash
python devtools/cli.py workflow validate workflows/templates/my_workflow.yml
```

### Step 3: Execute

```bash
python devtools/cli.py workflow run workflows/templates/my_workflow.yml
```

---

## 🔄 Integration with synthforge Components

### With Skills

Workflows invoke skills from `skills/` directory:

```yaml
phases:
  parse:
    - skill: spec_parser  # Loads from skills/workflow_skills/spec_parser/
      input: implementation_plan.md
```

### With Agents

Workflows invoke agents from `agents/` directory:

```yaml
phases:
  execute:
    - agent: executor_agent  # Loads from agents/executor_agent/
      action: implement_tasks
      mode: TDD
```

### With Rules

Workflows respect all rules from `rules/`:
- `AGENT_WORKFLOW_RULE.md` - Workflow execution rules
- `WORKFLOW_RULE.md` - Workflow creation rules
- `CODING_STYLE_RULE.md` - Code quality rules
- All other applicable rules

---

## 📚 Workflow Templates

### 1. Feature Development (`feature_development.yml`)

**Purpose**: Automate feature development from spec to code

**Phases**:
1. **Specify**: Parse implementation plan
2. **Plan**: Generate tasks
3. **Execute**: Implement with TDD
4. **Test**: Run automated tests
5. **Review**: AI code review

### 2. Bug Fix (`bug_fix.yml`)

**Purpose**: Automate bug fixing workflow

**Phases**:
1. **Diagnose**: Analyze issue
2. **Fix**: Implement fix
3. **Test**: Verify fix
4. **Review**: Code review

### 3. Refactoring (`refactoring.yml`)

**Purpose**: Automate code refactoring

**Phases**:
1. **Analyze**: Identify refactoring opportunities
2. **Plan**: Create refactoring plan
3. **Refactor**: Execute refactoring
4. **Verify**: Ensure no regressions

### 4. Rule Creation (`rule_creation.yml`)

**Purpose**: Automate rule creation process

**Phases**:
1. **Research**: Gather requirements
2. **Draft**: Create rule draft
3. **Review**: Review and refine
4. **Integrate**: Add to rules system

---

## 🎯 Best Practices

### 1. Keep Workflows Simple
- One workflow = One clear purpose
- Break complex workflows into smaller ones
- Use phases to organize steps

### 2. Use Descriptive Names
- Workflow name: `feature_development.yml`
- Phase name: `specify`, `execute`, `review`
- Skill/Agent name: `spec_parser`, `executor_agent`

### 3. Document Your Workflows
- Add `description` field
- Comment complex logic
- Provide examples

### 4. Test Before Use
- Always validate workflows
- Test with simple examples first
- Verify all dependencies exist

---

## 🔗 Related Documentation

- [WORKFLOW_RULE.md](WORKFLOW_RULE.md) - Workflow creation rules
- [AGENT_WORKFLOW_RULE.md](../rules/core/AGENT_WORKFLOW_RULE.md) - Agent workflow rules
- [skills/README.md](../skills/README.md) - Skills documentation
- [agents/README.md](../agents/README.md) - Agents documentation

---

## 🚧 Current Status

**All Phases**: ✅ **COMPLETE (100%)**

### Phase 2.1: Foundation ✅ COMPLETE
- ✅ Directory structure created
- ✅ README.md created
- ✅ WORKFLOW_RULE.md created
- ✅ Workflow templates created (4 templates + 1 example)
- ✅ Workflow engine implemented

### Phase 2.2: Engine & Skills ✅ COMPLETE
- ✅ Workflow engine (parser, executor, validators, context)
- ✅ 3 core skills (spec_parser, task_generator, test_runner)
- ✅ All components tested

### Phase 2.3: Agents ✅ COMPLETE
- ✅ 3 core agents (planner, executor, reviewer)
- ✅ All agents documented
- ✅ Git worktrees integration

### Phase 2.4: CLI & GitHub Integration ✅ COMPLETE
- ✅ CLI commands (run, validate, list)
- ✅ Integration tests (14 tests)
- ✅ GitHub Actions (3 workflows)
- ✅ Complete documentation

---

## 🎯 New Features

### Git Worktrees Support
- Parallel development on different branches
- Context preservation
- Automated worktree management
- See: [Git Worktrees Guide](../docs/guides/GIT_WORKTREES_GUIDE.md)

### GitHub Actions Integration
- AI-powered PR review
- Automated issue triage
- Weekly code analysis
- See: [GitHub Actions README](../.github/workflows/README.md)

### TDD Automation
- Red-Green-Refactor cycle
- Automated test generation
- Coverage enforcement
- See: [TDD_RULE](../rules/development/TDD_RULE.md)

---

## 📚 Complete Documentation

### Getting Started
- [Workflow Usage Guide](../docs/guides/WORKFLOW_GUIDE.md) - Comprehensive usage guide
- [WORKFLOW_RULE](WORKFLOW_RULE.md) - Workflow creation rules

### Architecture
- [GitHub Superpowers](../docs/architecture/GITHUB_SUPERPOWERS.md) - System architecture
- [WORKFLOW_INTEGRATION_RULE](../rules/development/WORKFLOW_INTEGRATION_RULE.md) - Integration standards

### Advanced Topics
- [Git Worktrees Guide](../docs/guides/GIT_WORKTREES_GUIDE.md) - Git worktrees usage
- [GitHub Actions README](../.github/workflows/README.md) - GitHub Actions setup

---

**Created**: 2026-02-01  
**Last Updated**: 2026-02-01  
**Status**: ✅ Production Ready  
**Version**: 1.0.0  
**Maintainer**: synthforge team
