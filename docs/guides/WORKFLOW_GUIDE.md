# Workflow System Usage Guide

**synthforge Workflow 系統使用指南**

---

## 📋 Table of Contents

1. [Quick Start](#quick-start)
2. [Workflow Basics](#workflow-basics)
3. [Using Workflow Templates](#using-workflow-templates)
4. [Creating Custom Workflows](#creating-custom-workflows)
5. [Skills & Agents](#skills--agents)
6. [Git Worktrees Integration](#git-worktrees-integration)
7. [GitHub Actions Integration](#github-actions-integration)
8. [Best Practices](#best-practices)
9. [Troubleshooting](#troubleshooting)

---

## 🚀 Quick Start

### Installation

```bash
# Clone synthforge
git clone <your-repo-url>
cd synthforge

# Install dependencies
pip install -r requirements.txt
```

### Your First Workflow

```bash
# 1. List available workflows
python devtools/cli.py workflow list

# 2. Validate a workflow
python devtools/cli.py workflow validate workflows/templates/feature_development.yml

# 3. Run a workflow
python devtools/cli.py workflow run workflows/templates/feature_development.yml
```

---

## 📚 Workflow Basics

### What is a Workflow?

A **workflow** is a YAML file that defines a sequence of automated tasks using **skills** and **agents**.

**Example**:
```yaml
name: Simple Feature Development
description: Basic feature development workflow
version: 1.0.0

phases:
  specify:
    - skill: spec_parser
      input: implementation_plan.md
      output: spec.json
  
  execute:
    - agent: executor_agent
      action: implement_tasks
      mode: TDD
```

### Workflow Components

1. **Phases**: Sequential stages (specify, plan, execute, test, review)
2. **Skills**: Stateless functions (spec_parser, task_generator, test_runner)
3. **Agents**: Stateful decision-makers (planner_agent, executor_agent, reviewer_agent)

### Workflow Lifecycle

```
Create/Select Workflow
    ↓
Validate Workflow
    ↓
Execute Workflow
    ├─ Phase 1
    ├─ Phase 2
    ├─ Phase 3
    └─ ...
    ↓
Review Results
```

---

## 🎯 Using Workflow Templates

### Available Templates

#### 1. Feature Development (`feature_development.yml`)

**Purpose**: Automate feature development from spec to code

**Usage**:
```bash
python devtools/cli.py workflow run workflows/templates/feature_development.yml
```

**Phases**:
1. **Specify**: Parse implementation plan
2. **Plan**: Generate tasks
3. **Execute**: Implement with TDD
4. **Test**: Run automated tests
5. **Review**: AI code review

**When to use**:
- ✅ Developing new features
- ✅ Following spec-driven development
- ✅ Need TDD automation

---

#### 2. Bug Fix (`bug_fix.yml`)

**Purpose**: Automate bug fixing workflow

**Usage**:
```bash
python devtools/cli.py workflow run workflows/templates/bug_fix.yml
```

**Phases**:
1. **Diagnose**: Analyze issue
2. **Fix**: Implement fix
3. **Test**: Verify fix
4. **Review**: Code review

**When to use**:
- ✅ Fixing bugs
- ✅ Need quick diagnosis
- ✅ Want automated testing

---

#### 3. Refactoring (`refactoring.yml`)

**Purpose**: Automate code refactoring

**Usage**:
```bash
python devtools/cli.py workflow run workflows/templates/refactoring.yml
```

**Phases**:
1. **Analyze**: Identify refactoring opportunities
2. **Plan**: Create refactoring plan
3. **Refactor**: Execute refactoring
4. **Verify**: Ensure no regressions

**When to use**:
- ✅ Improving code quality
- ✅ Reducing technical debt
- ✅ Need regression testing

---

#### 4. Rule Creation (`rule_creation.yml`)

**Purpose**: Automate rule creation process

**Usage**:
```bash
python devtools/cli.py workflow run workflows/templates/rule_creation.yml
```

**Phases**:
1. **Research**: Gather requirements
2. **Draft**: Create rule draft
3. **Review**: Review and refine
4. **Integrate**: Add to rules system

**When to use**:
- ✅ Creating new rules
- ✅ Standardizing processes
- ✅ Need structured approach

---

## 🛠️ Creating Custom Workflows

### Step 1: Create YAML File

```yaml
name: My Custom Workflow
description: Brief description of what this workflow does
version: 1.0.0
author: Your Name
tags: [custom, example]

config:
  timeout: 3600  # seconds
  retry: 3       # retry count

phases:
  phase_1:
    - skill: skill_name
      input: input_file.md
      output: output_file.json
      config:
        param1: value1
  
  phase_2:
    - agent: agent_name
      action: action_name
      mode: execution_mode
      config:
        param1: value1
```

### Step 2: Validate

```bash
python devtools/cli.py workflow validate workflows/custom/my_workflow.yml
```

### Step 3: Test

```bash
# Dry run
python devtools/cli.py workflow run workflows/custom/my_workflow.yml --dry-run

# Actual run
python devtools/cli.py workflow run workflows/custom/my_workflow.yml
```

### Workflow Naming Conventions

**Format**: `[purpose]_[type].yml`

**Examples**:
- ✅ `feature_development.yml`
- ✅ `bug_fix.yml`
- ✅ `api_integration.yml`
- ❌ `MyWorkflow.yml` (use snake_case)
- ❌ `workflow1.yml` (not descriptive)

---

## 🎨 Skills & Agents

### Available Skills

#### 1. spec_parser

**Purpose**: Parse implementation_plan.md into structured JSON

**Usage**:
```yaml
- skill: spec_parser
  input: implementation_plan.md
  output: spec.json
  config:
    format: json
    validate: true
```

---

#### 2. task_generator

**Purpose**: Generate task.md from specification

**Usage**:
```yaml
- skill: task_generator
  input: spec.json
  output: task.md
  config:
    max_depth: 5
    include_estimates: true
```

---

#### 3. test_runner

**Purpose**: Run automated tests

**Usage**:
```yaml
- skill: test_runner
  config:
    test_path: tests/
    coverage_threshold: 80
    generate_report: true
```

---

### Available Agents

#### 1. planner_agent

**Purpose**: Task planning and validation

**Actions**:
- `validate_tasks`: Validate task.md

**Usage**:
```yaml
- agent: planner_agent
  action: validate_tasks
  input: task.md
  config:
    max_depth: 5
    check_dependencies: true
```

---

#### 2. executor_agent

**Purpose**: Code execution with TDD

**Actions**:
- `implement_tasks`: Implement tasks using TDD

**Usage**:
```yaml
- agent: executor_agent
  action: implement_tasks
  mode: TDD
  config:
    use_worktree: true
    coverage_threshold: 80
```

---

#### 3. reviewer_agent

**Purpose**: AI code review

**Actions**:
- `review_code`: Review code changes

**Usage**:
```yaml
- agent: reviewer_agent
  action: review_code
  config:
    check_style: true
    check_security: true
    check_performance: true
```

---

## 🌳 Git Worktrees Integration

### What are Git Worktrees?

Git Worktrees allow parallel development on different branches without switching contexts.

### Using Worktrees in Workflows

```yaml
phases:
  execute:
    - agent: executor_agent
      action: implement_tasks
      config:
        use_worktree: true
        branch_name: feature/auto-generated
        auto_cleanup: true
```

**Benefits**:
- ✅ No branch switching
- ✅ Parallel development
- ✅ Context preservation

**See**: [Git Worktrees Guide](GIT_WORKTREES_GUIDE.md)

---

## 🤖 GitHub Actions Integration

### Automatic PR Review

When you create a PR, GitHub Actions automatically:
1. Reviews changed files
2. Checks code style
3. Runs tests
4. Comments on PR with results

### Automatic Issue Triage

When you create an issue, GitHub Actions automatically:
1. Analyzes issue content
2. Adds appropriate labels
3. Sets priority
4. Suggests relevant workflows

### Weekly Code Analysis

Every Monday, GitHub Actions automatically:
1. Analyzes code complexity
2. Runs linting
3. Checks test coverage
4. Validates workflows
5. Creates issues for critical findings

**See**: [GitHub Actions README](../../.github/workflows/README.md)

---

## 📋 Best Practices

### 1. Start with Templates

```bash
# Good: Use existing templates
python devtools/cli.py workflow run workflows/templates/feature_development.yml

# Customize only when needed
cp workflows/templates/feature_development.yml workflows/custom/my_feature.yml
```

### 2. Validate Before Running

```bash
# Always validate first
python devtools/cli.py workflow validate workflows/custom/my_workflow.yml

# Then run
python devtools/cli.py workflow run workflows/custom/my_workflow.yml
```

### 3. Use Descriptive Names

```yaml
# Good
name: User Authentication Feature Development
description: Implement user login and registration

# Bad
name: Workflow 1
description: Does stuff
```

### 4. Keep Workflows Simple

```yaml
# Good: Clear and focused
phases:
  specify:
    - skill: spec_parser
  execute:
    - agent: executor_agent

# Bad: Too complex
phases:
  pre_pre_processing:
    - skill: thing1
    - skill: thing2
  # ... 10 more phases
```

### 5. Document Configuration

```yaml
phases:
  execute:
    - agent: executor_agent
      config:
        mode: TDD  # Use Test-Driven Development
        coverage_threshold: 80  # Minimum test coverage
        use_worktree: true  # Isolate in Git worktree
```

---

## 🐛 Troubleshooting

### Issue 1: Workflow Validation Fails

**Problem**: `Workflow validation failed: Skill 'xyz' not found`

**Solution**:
```bash
# Check available skills
ls skills/workflow_skills/

# Use correct skill name
- skill: spec_parser  # Not spec-parser or SpecParser
```

---

### Issue 2: Workflow Execution Hangs

**Problem**: Workflow seems stuck

**Solution**:
```yaml
# Add timeout
config:
  timeout: 1800  # 30 minutes

phases:
  execute:
    - agent: executor_agent
      config:
        timeout: 900  # 15 minutes per phase
```

---

### Issue 3: Test Coverage Too Low

**Problem**: `Test coverage 65% below threshold 80%`

**Solution**:
```yaml
# Adjust threshold or write more tests
- skill: test_runner
  config:
    coverage_threshold: 65  # Lower threshold
    # OR write more tests to reach 80%
```

---

### Issue 4: Git Worktree Conflicts

**Problem**: `Worktree already exists`

**Solution**:
```bash
# List worktrees
git worktree list

# Remove existing
git worktree remove /path/to/worktree

# Or use different branch name
```

---

## 📚 Additional Resources

### Documentation
- [Workflow System README](../../workflows/README.md)
- [WORKFLOW_RULE](../../workflows/WORKFLOW_RULE.md)
- [GitHub Superpowers Architecture](../architecture/GITHUB_SUPERPOWERS.md)

### Rules
- [SPEC_DRIVEN_DEVELOPMENT_RULE](../../rules/core/SPEC_DRIVEN_DEVELOPMENT_RULE.md)
- [AGENT_WORKFLOW_RULE](../../rules/core/AGENT_WORKFLOW_RULE.md)
- [TDD_RULE](../../rules/development/TDD_RULE.md)
- [WORKFLOW_INTEGRATION_RULE](../../rules/development/WORKFLOW_INTEGRATION_RULE.md)

### Guides
- [Git Worktrees Guide](GIT_WORKTREES_GUIDE.md)
- [GitHub Actions README](../../.github/workflows/README.md)

---

## ✅ Summary

The synthforge Workflow System provides:
- ✅ Automated spec-to-code transformation
- ✅ TDD-driven development
- ✅ AI-powered code review
- ✅ GitHub Actions integration
- ✅ Git worktrees support
- ✅ Comprehensive testing

**Start automating your development workflow today!** 🚀

---

**Created**: 2026-02-01  
**Version**: 1.0.0  
**Status**: Production Ready
