# Workflow Skills - synthforge

**Purpose**: Skills specifically designed for workflow automation  
**用途**: 專為工作流自動化設計的技能

---

## 📋 Available Skills

### 1. spec_parser
**Purpose**: Parse `implementation_plan.md` into structured format  
**用途**: 將 `implementation_plan.md` 解析為結構化格式

**Input**: `implementation_plan.md`  
**Output**: `spec.json`

---

### 2. task_generator
**Purpose**: Generate `task.md` from parsed specification  
**用途**: 從解析的規格生成 `task.md`

**Input**: `spec.json`  
**Output**: `task.md`

---

### 3. test_runner
**Purpose**: Run automated tests  
**用途**: 執行自動化測試

**Input**: Test configuration  
**Output**: Test results

---

## 🔧 How to Use in Workflows

```yaml
phases:
  parse:
    - skill: spec_parser
      input: implementation_plan.md
      output: spec.json
      
  generate:
    - skill: task_generator
      input: spec.json
      output: task.md
      
  test:
    - skill: test_runner
      config:
        coverage_threshold: 80
```

---

## 📚 Skill Structure

Each skill follows this structure:

```
skills/workflow_skills/[skill_name]/
├── SKILL.md              # Skill metadata and documentation
├── [skill_name].py       # Main skill implementation
├── tests/                # Skill tests
│   └── test_[skill_name].py
└── README.md             # Detailed documentation (optional)
```

---

**Created**: 2026-02-01  
**Status**: Active Development
