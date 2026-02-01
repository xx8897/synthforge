# synthforge Architecture

**Version**: 2.0  
**Last Updated**: 2026-01-29  
**Status**: Active Development

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
│       └── copilot-instructions.md  ← GitHub Copilot configuration
│
├── 📁 rules/ ← Rules集中管理
│   ├── README.md                    ← Rules index
│   ├── core/                        ← Core rules (MANDATORY)
│   │   ├── DIRECTORY_README_RULE.md
│   │   ├── VIBE_GUIDE_SYNC_RULE.md
│   │   ├── BILINGUAL_OUTPUT_RULE.md
│   │   └── DRY_RULE.md
│   └── development/                 ← Development rules
│       ├── FILE_NAMING_CONVENTION_RULE.md
│       └── INTERNAL_RULE.md
│
├── 📁 devtools/ ← Development Tools (核心工具)
│   ├── README.md
│   ├── cli.py                       ← Unified CLI
│   ├── __init__.py
│   ├── security/                    ← Security tools
│   │   ├── security_auditor.py
│   │   ├── advanced_security.py
│   │   ├── filters.yaml
│   │   └── SECURITY_STRATEGY.md
│   ├── analyzers/                   ← Analysis tools
│   │   ├── dep_analyzer.py
│   │   └── license_checker.py
│   ├── release/                     ← Release tools
│   │   └── release_cleaner.py
│   └── project/                     ← Project tools
│       └── scaffolder.py
│
├── 📁 skills/ ← Reusable Capabilities (可重複使用的能力)
│   ├── README.md                    ← Skills index
│   └── examples/                    ← Examples and best practices
│       └── structure_management/    ← Structure management examples
│           ├── SKILL.md             ← Skill metadata
│           ├── scripts/
│           │   ├── create_directory_structure.py
│           │   ├── batch_move_files.py
│           │   ├── example_rules_restructure.py
│           │   └── example_devtools_restructure.py
│           └── references/
│               └── best_practices.md
│
├── 📁 agents/ ← AI Agents (future)
│   └── README.md                    ← Agents index
│
├── 📁 docs/ ← Documentation
│   ├── architecture/
│   │   ├── ARCHITECTURE.md          ← This file
│   │   └── SKILLS_VS_RULES.md
│   ├── guides/
│   │   ├── AGENT_RULES.md
│   │   └── DOC_GUIDE.md
│   ├── planning/
│   │   ├── TASKS.md
│   │   └── IMPLEMENTATION_TRACKER.md
│   ├── strategies/
│   │   └── GIT_STRATEGY.md
│   │   └── [archived session docs]
│
├── 📁 projects/ ← User Projects
│   └── [independent projects]
│
└── 📁 .internal/ ← Internal Management
    ├── README.md
    ├── summaries/
    │   └── 2026-01/
    ├── confirmations/
    │   ├── pending/
    │   └── archived/
    ├── analysis/
    ├── planning/
    │   └── 待辦.md
    ├── knowledge/
    │   ├── README.md
    │   └── best_practices/
    │       └── dry_principle.md
    └── temp/
```

---

## 🔧 Component Details / 組件詳情

### Core Files / 核心檔案

#### VIBE_GUIDE.md
**Purpose**: AI agent entry point  
**用途**: AI 代理入口

**Content**:
- Workspace overview
- Document hierarchy
- Core rules index
- Quick reference

**When to read**: Every time entering workspace

---

#### rules/
**Purpose**: Centralized rule management  
**用途**: 規則集中管理

**Structure**:
- `core/` - Mandatory rules (DIRECTORY_README, VIBE_GUIDE_SYNC, BILINGUAL_OUTPUT, DRY)
- `development/` - Development rules (FILE_NAMING, INTERNAL)

**Format**: All rules use `[TOPIC]_RULE.md` naming

---

### devtools/
**Purpose**: Core development tools  
**用途**: 核心開發工具

**Organization**: Functional subdirectories

**Categories**:
1. **security/** - Security scanning and auditing
2. **analyzers/** - Dependency and license analysis
3. **release/** - Release preparation
4. **project/** - Project scaffolding

**CLI**: Unified command-line interface
```bash
python devtools/cli.py [COMMAND] [OPTIONS]
```

**Commands**:
- `new` - Create new project
- `check` - Run checks (security, licenses, deps)
- `release` - Prepare release
- `analyze` - Analyze project
- `info` - Show devtools information

---

### skills/
**Purpose**: Reusable capabilities and examples  
**用途**: 可重複使用的能力和範例

**Structure**: Each skill in its own directory

**Standard Format**:
```
skills/[skill_name]/
├── SKILL.md                 ← Metadata + instructions
├── scripts/                 ← Executable code
├── references/              ← Detailed documentation
└── assets/                  ← Templates, configs
```

**SKILL.md Format**:
```markdown
---
name: skill_name
description: Brief description
version: 1.0.0
tags: [tag1, tag2]
---

# Skill Name

## Description
## When to Use
## Available Tools
## References
```

**Current Skills**:
- `examples/structure_management` - Project restructuring examples

---

### agents/
**Purpose**: AI agents with specific roles  
**用途**: 具有特定角色的 AI 代理

**Structure**: Each agent in its own directory

**Standard Format**:
```
agents/[agent_name]/
├── AGENT.md                 ← Agent definition
├── config.yaml              ← Configuration
├── workflows/               ← Task workflows
├── prompts/                 ← System prompts
├── tools/                   ← Available tools (links to skills)
└── memory/                  ← Persistent state
```

**AGENT.md Format**:
```markdown
---
name: agent_name
role: Agent role
goal: Primary goal
version: 1.0.0
---

# Agent Name

## Role & Responsibilities
## Available Tools
## Workflows
## Prompts
```

**Status**: Future implementation

---

### docs/
**Purpose**: Comprehensive documentation  
**用途**: 完整文件

**Organization**:
- `architecture/` - System design and architecture
- `guides/` - How-to guides and rules
- `planning/` - Tasks and implementation tracking
- `strategies/` - Strategic decisions
- `sessions/` - Archived session documents

---

### .internal/
**Purpose**: Internal management and state  
**用途**: 內部管理和狀態

**Structure**: 6 subdirectories

**Categories**:
1. **summaries/** - Task summaries (by month)
2. **confirmations/** - Pending and archived confirmations
3. **analysis/** - Analysis documents
4. **planning/** - To-do lists and plans
5. **knowledge/** - Knowledge base (categorized)
6. **temp/** - Temporary files

**Token Management**:
- ✅ Good: < 10K tokens
- ⚠️ Warning: 10K-20K tokens
- 🚨 Critical: > 20K tokens

**Language**: Pure Chinese (for token efficiency)

---

## 🔄 Data Flow / 資料流

### AI Agent Workflow / AI 代理工作流程

```
User Request
    ↓
1. Read VIBE_GUIDE.md
    ↓
2. Read relevant rules (rules/)
    ↓
3. Check .internal/ for pending tasks
    ↓
4. Execute task
    ↓
5. Update documentation
    ↓
6. Create task summary (.internal/summaries/)
    ↓
7. Remind pending tasks
```

### Skill Discovery / 技能發現

```
Agent needs capability
    ↓
Search skills/ directory
    ↓
Read SKILL.md (metadata only)
    ↓
If match: Load full SKILL.md
    ↓
Access scripts/ and references/
    ↓
Execute skill
```

### Rule Enforcement / 規則執行

```
Before ANY task
    ↓
Read VIBE_GUIDE.md
    ↓
Read DIRECTORY_README_RULE.md
    ↓
If in subdirectory: Read [subdirectory]/README.md
    ↓
Check .internal/confirmations/pending/
    ↓
Check .internal/planning/待辦.md
    ↓
Execute task following rules
```

---

## 📊 Design Decisions / 設計決策

### Why Functional Organization for devtools?
**為什麼 devtools 使用功能組織？**

**Reason**: Easier to find tools by purpose  
**理由**: 更容易按用途查找工具

**Before**:
```
devtools/
├── security_auditor.py
├── dep_analyzer.py
├── release_cleaner.py
...
```

**After**:
```
devtools/
├── security/
├── analyzers/
├── release/
└── project/
```

---

### Why Separate rules/ Directory?
**為什麼獨立 rules/ 目錄？**

**Reason**: Centralized rule management  
**理由**: 規則集中管理

**Benefits**:
- Easy to find all rules
- Clear categorization (core vs development)
- Better organization

---

### Why skills/ for Examples?
**為什麼 skills/ 用於範例？**

**Reason**: Skills are reusable capabilities  
**理由**: Skills 是可重複使用的能力

**Philosophy**:
- Skills = Patterns and examples AI can learn
- devtools = Core tools for development
- agents = AI personas with specific roles

---

### Why .internal/ in Chinese?
**為什麼 .internal/ 用中文？**

**Reason**: Token efficiency  
**理由**: Token 效率

**Analysis**:
- Chinese content: 2-2.5x more tokens than English
- .internal/ is internal-only
- Using Chinese saves 50-65% tokens

---

## 🎯 Scalability / 可擴展性

### Current Phase: Solo Developer
**當前階段：個人開發者**

**Focus**:
- Core tools (devtools)
- Basic skills (examples)
- Documentation

**Future Phases**:
- Phase 2: Add more skills
- Phase 3: Implement agents
- Phase 4: Multi-agent workflows

---

## 🔗 Integration Points / 整合點

### AI Tools Integration
**AI 工具整合**

**Supported**:
- Cursor AI (`.cursorrules`)
- GitHub Copilot (`.github/copilot-instructions.md`)
- ChatGPT/Claude/Gemini (README.md instructions)

**Configuration**:
All AI tools configured to read VIBE_GUIDE.md first

---

### Git Strategy
**Git 策略**

**Current**: Single repository for entire workspace  
**當前**: 整個工作區單一儲存庫

**Future**: Hybrid approach
- Common assets (rules, skills, agents) → One repo
- Each project → Separate repo

---

## 📝 File Naming Conventions / 檔案命名規範

**Rules**: `[TOPIC]_RULE.md` (UPPER_CASE)  
**Confirmations**: `[topic]_confirmation.md` (lower_case)  
**Analysis**: `[topic]_analysis.md` (lower_case)  
**Knowledge**: `[descriptive_name].md` (lower_case)  
**Summaries**: `任務總結_YYYY-MM-DD_HHMM.md` (Chinese)  
**Code**: `[module_name].py` (lower_case)

---

## 🚀 Future Roadmap / 未來路線圖

### Phase 1: Foundation (Current)
- ✅ Core rules established
- ✅ devtools organized
- ✅ skills/ structure defined
- ⏳ ARCHITECTURE.md updated

### Phase 2: Skills Expansion
- Add web scraping skill
- Add data processing skill
- Add API integration skill
- Add code generation skill

### Phase 3: Agents Implementation
- Implement code_reviewer agent
- Implement doc_generator agent
- Implement test_writer agent
- Implement refactoring_assistant agent

### Phase 4: Advanced Features
- Multi-agent workflows
- Agent collaboration
- Skill marketplace
- Web UI dashboard

---

**Created**: 2026-01-29  
**Version**: 2.0  
**Status**: Active Development
