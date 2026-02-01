# synthforge Architecture

**Version**: 3.0  
**Last Updated**: 2026-02-02  
**Status**: v1.0.0 Production Ready

---

## 🎯 Design Philosophy / 設計哲學

synthforge is an AI-driven development environment built on three core principles:

synthforge 是一個基於三個核心原則的 AI 驅動開發環境：

### 1. Modular Organization / 模組化組織
- Clear separation of concerns
- Each component has a single responsibility
- Easy to understand and maintain

### 2. Progressive Disclosure / 漸進式揭露
- Only load what you need
- Skills and agents use SKILL.md/AGENT.md for metadata
- Full content loaded only when required

### 3. DRY Principle / 避免重複
- Single source of truth for all knowledge
- Reference instead of duplicate
- Balance DRY with readability

---

## 📁 Directory Structure / 目錄結構

```
synthforge/
├── 📄 Core Files / 核心檔案
│   ├── README.md                    ← Project overview
│   ├── VIBE_GUIDE.md                ← AI agent entry point
│   ├── .cursorrules                 ← Cursor AI configuration
│   └── .github/
│       └── workflows/               ← GitHub Actions (PR review, Issue triage)
│
├── 📁 rules/ ← Rules 集中管理
│   ├── README.md                    ← Rules index
│   ├── core/                        ← Core rules (MANDATORY)
│   ├── development/                 ← Development rules
│   └── management/                  ← Management rules
│
├── 📁 devtools/ ← Development Tools (核心工具)
│   ├── cli.py                       ← Unified CLI (Main entry point)
│   ├── knowledge_graph.py           ← Rule relationship visualization
│   ├── security/                    ← Security scanning tools
│   ├── analyzers/                   ← Code and dependency analyzers
│   ├── release/                     ← Release preparation tools
│   └── project/                     ← Scaffolding tools
│
├── 📁 skills/ ← Reusable Capabilities (可重複使用的能力)
│   ├── automation/                  ← Structure management skills
│   └── workflow_skills/             ← spec_parser, task_generator, test_runner
│
├── 📁 agents/ ← AI Agents (智能代理)
│   ├── planner_agent/               ← Planning and strategy
│   ├── executor_agent/              ← Implementation (TDD, Worktrees)
│   ├── reviewer_agent/              ← Code review and auditing
│   └── self_improvement_agent/      ← Learning and optimization
│
├── 📁 core_lib/ ← Shared Infrastructure (共享基礎設施)
│   ├── utils/                       ← File and general utilities
│   └── git/                         ← Git automation and worktree management
│
├── 📁 workflows/ ← Workflow Engine (工作流引擎)
│   ├── engine/                      ← Parser, Executor, Context
│   ├── templates/                   ← Feature, BugFix, Refactor templates
│   └── tests/                       ← Integration tests
│
├── 📁 docs/ ← Documentation (文件)
│   ├── architecture/                ← ARCHITECTURE.md, ROADMAP.md
│   ├── guides/                      ← GIT_WORKFLOW.md, WORKFLOW_GUIDE.md
│   └── README.md
│
└── 📁 .internal/ ← Internal Management (內部管理)
    ├── summaries/                   ← Task summaries (Bilingual)
    ├── knowledge/                   ← Knowledge base and map
    └── planning/                    ← TODO lists and trackers
```

---

## 🔧 Component Details / 組件詳情

### 1. Unified CLI (`devtools/cli.py`)
**Purpose**: Central command center for all developer tasks.  
**用途**: 所有開發任務的中央控制中心。

**Features**:
- `new`: Scaffolding for 4 project types.
- `check`: Security, licenses, and dependency checks.
- `workflow`: Run and manage automated workflows.
- `git`: Auto-commit, push, and PR creation.
- `interactive`: Interactive shell mode.

---

### 2. Workflow System (`workflows/`)
**Purpose**: Automate complex development sequences.  
**用途**: 自動化複雜的開發序列。

**Engine**:
- `parser.py`: Parses YAML workflow definitions.
- `executor.py`: Executes phases and steps.
- `context.py`: Manages state and data between steps.

**Templates**:
- `feature_development.yml`: Full TDD feature branch workflow.
- `bug_fix.yml`: Diagnosis, fix, and verification.
- `refactoring.yml`: Incremental code improvement.

---

### 3. AI Agents (`agents/`)
**Purpose**: Autonomous specialized assistants.  
**用途**: 自主的專業化助手。

**Roles**:
- **Planner Agent**: Design implementation plans from specifications.
- **Executor Agent**: Implements code using TDD and Git Worktrees.
- **Reviewer Agent**: Performs automated code reviews and audits.
- **Self-Improvement Agent**: Learns from errors and optimizes workflows.

---

### 4. Git Automation (`core_lib/git/`)
**Purpose**: Hassle-free version control.  
**用途**: 無憂的版本控制。

**Capabilities**:
- **Automation**: One-click commit/push/PR.
- **Worktrees**: Isolated development environments to keep the main branch clean.
- **Strategy**: Feature-branch workflow enforced by tools.

---

### 5. Knowledge Graph (`devtools/knowledge_graph.py`)
**Purpose**: Visualize relationships between project components.  
**用途**: 視覺化專案組件之間的關係。

**Output**:
- **Mermaid Diagrams**: Visual map of dependencies.
- **Knowledge Map**: Automated cross-referencing of rules and patterns.

---

## 🔄 Data Flow / 資料流

### Workflow Execution Process
```
User Spec ──► Planner Agent ──► Implementation Plan
                                     │
                                     ▼
PR Review ◄── Reviewer Agent ◄── Executor Agent (TDD + Git Worktree)
      │                              │
      ▼                              ▼
Merge to Main ◄──────────────────────┘
      │
      ▼
Self-Improvement Agent (Learn from the cycle)
```

---

## 🎯 Implementation Status / 實施狀態

- **Phase 1: Foundation** ✅ Complete
- **Phase 2: DevEx** ✅ Complete
- **Phase 3: Intelligence** ✅ Complete
- **Phase 4: Optimization** 🚧 In Progress

---

**Last Updated**: 2026-02-02  
**Maintainer**: xx8897
