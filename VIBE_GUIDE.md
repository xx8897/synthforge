# VIBE GUIDE - AI Agent Entry Point
# VIBE 指南 - AI 代理入口

**Purpose**: This is the FIRST file AI agents should read when entering the synthforge workspace.  
**目的**: 這是 AI 代理進入 synthforge 工作區時應該首先閱讀的檔案。

---

## 📖 Terminology / 術語

**Workspace** = **synthforge**  
When we say "workspace" or "工作區", we mean the synthforge development environment.

當我們說「workspace」或「工作區」時，我們指的是 synthforge 開發環境。

**Location**: `C:\Users\xx8897\synthforge`  
**GitHub**: `https://github.com/xx8897/synthforge` (private)

---

## 🎯 What is synthforge?

**synthforge** is an AI-driven development environment that combines:
- **Development Tools** (`devtools/`) - Security, release management, dependency analysis
- **AI Agents** (`agents/`) - Autonomous code assistants (future)
- **Reusable Skills** (`skills/`) - Modular capabilities (future)
- **Projects** (`projects/`) - Independent applications
- **Documentation** (`docs/`) - Organized guides, architecture, planning

**synthforge** 是一個 AI 驅動的開發環境，結合了：
- **開發工具** (`devtools/`) - 安全、發布管理、依賴分析
- **AI 代理** (`agents/`) - 自主程式碼助手（未來）
- **可重用技能** (`skills/`) - 模組化能力（未來）
- **專案** (`projects/`) - 獨立應用程式
- **文件** (`docs/`) - 組織化的指南、架構、規劃

---

## 📚 Navigation Architecture - Strong & Weak Links
## 導航架構 - 強弱連結

### 🔴 Strong Links (MUST Read) - 強連結（必讀）

**From VIBE_GUIDE, you MUST read these directory entry points:**

**從 VIBE_GUIDE，你必須閱讀這些目錄入口點：**

1. **[README.md](README.md)** - Workspace Overview
   - High-level introduction to synthforge
   - Features, philosophy, quick start

2. **[rules/README.md](rules/README.md)** - Rules Index
   - All mandatory and recommended rules
   - Rule categories and priorities
   - **⚠️ CRITICAL**: Read [rules/core/AGENT_WORKFLOW_RULE.md](rules/core/AGENT_WORKFLOW_RULE.md) FIRST
     - Defines mandatory workflow for ALL tasks
     - Must check rules BEFORE executing any task
     - Rules > Skills priority

3. **[docs/README.md](docs/README.md)** - Documentation Index
   - All documentation categories
   - Links to architecture and guides

4. **[docs/architecture/ARCHITECTURE.md](docs/architecture/ARCHITECTURE.md)** - System Design
   - Complete system architecture (SSOT)
   - Component relationships and data flow

5. **[docs/guides/AGENT_RULES.md](docs/guides/AGENT_RULES.md)** - AI Agent Behavior
   - How AI agents should behave
   - Communication style, bilingual requirements

6. **[devtools/README.md](devtools/README.md)** - Development Tools
   - All available devtools
   - Usage examples and API reference

7. **[core_lib/README.md](core_lib/README.md)** - Core Library
   - Shared utilities and infrastructure
   - Import from here, don't duplicate

---

### 🟡 Weak Links (Read as Needed) - 弱連結（按需閱讀）

**From directory READMEs, read specific files as needed:**

**從目錄 README，按需閱讀具體文件：**

**From docs/architecture/README.md**:
- DESIGN_DECISIONS.md - Design decision records
- ROADMAP.md - Feature roadmap
- GIT_STRATEGY.md - Git and GitHub strategy

**From docs/guides/README.md**:
- QUICKSTART.md - Quick start guide
- DOC_GUIDE.md - Documentation standards
- SKILLS_VS_RULES.md - Concepts explanation

**From rules/README.md**:
- rules/core/ - Mandatory rules
- rules/development/ - Recommended rules

---

### 📊 Linking Principle - 連結原則

```
VIBE_GUIDE.md (ROOT)
    ↓ [STRONG] 強連結
Directory README.md (Entry Point)
    ↓ [WEAK] 弱連結
Specific Files (As Needed)
```

**Rules / 規則**:
1. ✅ VIBE_GUIDE only links to **directory READMEs**
2. ✅ Directory READMEs manage all files in their directory
3. ✅ Add new files → update directory README only
4. ❌ Don't add direct links from VIBE_GUIDE to specific files

**Why? / 為什麼？**
- **Scalability**: Adding files doesn't require VIBE_GUIDE changes
- **Maintainability**: Each directory manages itself
- **SSOT**: Directory README is the single source for directory contents

---

## 🤖 For AI Agents: Decision Tree
## 給 AI 代理：決策樹

```
START: Read VIBE_GUIDE.md (this file)
  ↓
QUESTION: What is your task?
  ↓
  ├─ "Create new project"
  │   → Read: QUICKSTART.md, devtools/README.md (scaffolder)
  │   → Use: devtools/cli.py new
  │
  ├─ "Security audit"
  │   → Read: devtools/SECURITY_STRATEGY.md
  │   → Use: devtools/cli.py check --security --deep
  │
  ├─ "Analyze dependencies"
  │   → Read: devtools/analyzers/README.md
  │   → Use: devtools/cli.py analyze
  │
  ├─ "Prepare release"
  │   → Read: devtools/README.md (release cleaner)
  │   → Use: devtools/cli.py release --clean --audit
  │
  ├─ "Understand architecture"
  │   → Read: ARCHITECTURE.md
  │
  ├─ "Check implementation status"
  │   → Read: TASKS.md, IMPLEMENTATION_TRACKER.md
  │
  ├─ "Write documentation"
  │   → Read: DOC_GUIDE.md, AGENT_RULES.md
  │
  └─ "Git operations"
      → Read: GIT_STRATEGY.md
```

---

## 🎨 For AI Agents: Skill Selection
## 給 AI 代理：技能選擇

### When to Use Skills:

**Skills** are reusable capabilities in `skills/` directory.

**技能** 是 `skills/` 目錄中的可重用能力。

| Task | Skill to Use | Location |
|------|--------------|----------|
| Web scraping | `web_search` | `skills/web_search/` |
| Data analysis | `data_analysis` | `skills/data_analysis/` |
| API calls | `api_client` | `skills/api_client/` |
| File operations | `file_ops` | `skills/file_ops/` |
| Git automation | `git_ops` | `skills/git_ops/` |

**How to Load a Skill**:
```python
from skills.web_search import WebSearchSkill

skill = WebSearchSkill()
result = skill.search("AI development tools")
```

---

## 🎯 For AI Agents: Agent Selection
## 給 AI 代理：代理選擇

### When to Use Agents:

**Agents** are autonomous assistants in `agents/` directory.

**代理** 是 `agents/` 目錄中的自主助手。

| Task | Agent to Use | Location |
|------|--------------|----------|
| Code review | `code_reviewer` | `agents/code_reviewer/` |
| Documentation | `doc_writer` | `agents/doc_writer/` |
| Test generation | `test_generator` | `agents/test_generator/` |
| Refactoring | `refactoring_assistant` | `agents/refactoring_assistant/` |

**How to Invoke an Agent**:
```bash
python devtools/cli.py agent run code-reviewer --file=main.py
```

---

## 📊 Workspace Structure - Quick Reference
## 工作區結構 - 快速參考

**🔍 For complete directory tree with all files**:  
→ Read [docs/architecture/ARCHITECTURE.md](docs/architecture/ARCHITECTURE.md)

**🔍 完整目錄樹及所有檔案**:  
→ 閱讀 [docs/architecture/ARCHITECTURE.md](docs/architecture/ARCHITECTURE.md)

### High-Level Overview / 高階概覽:

```
synthforge/                          ← C:\Users\xx8897\synthforge
├── 📄 README.md                     ← Main entry point
├── 📄 VIBE_GUIDE.md                 ← AI agent entry (YOU ARE HERE)
├── 📄 DIRECTORY_README_RULE.md      ← 🚨 CRITICAL: Read before entering dirs
├── 📄 VIBE_GUIDE_SYNC_RULE.md       ← 🚨 CRITICAL: Keep docs in sync
├── 📄 .gitignore
│
├── 📁 docs/                         ← All documentation
│   ├── guides/                      ← User guides
│   ├── architecture/                ← System design & decisions
│   ├── planning/                    ← Roadmap & tasks
│   ├── strategies/                  ← Strategies (Git, GitHub, etc.)
│   └── sessions/                    ← Session records
│
├── 📁 devtools/                     ← Development toolkit
│   ├── README.md                    ← Tool documentation (read first!)
│   ├── cli.py                       ← Unified CLI
│   ├── security/                    ← Security tools (future)
│   ├── analyzers/                   ← Dependency analysis
│   ├── release/                     ← Release tools (future)
│   ├── project/                     ← Project scaffolding (future)
│   └── config/                      ← Configuration (future)
│
├── 📁 rules/                        ← All rules (future)
│   ├── core/                        ← Core rules (MANDATORY)
│   ├── development/                 ← Development rules
│   ├── documentation/               ← Documentation rules
│   └── security/                    ← Security rules
│
├── 📁 agents/                       ← AI assistants (future)
├── 📁 skills/                       ← Reusable capabilities (future)
├── 📁 projects/                     ← User projects (gitignored)
├── 📁 templates/                    ← Project templates (future)
└── 📁 .internal/                    ← Personal notes (gitignored)
```

**Note**: This is a high-level overview. For detailed file listings, dependencies, and design decisions, see [ARCHITECTURE.md](docs/architecture/ARCHITECTURE.md).

**注意**: 這是高階概覽。詳細的檔案清單、依賴關係和設計決策，請參閱 [ARCHITECTURE.md](docs/architecture/ARCHITECTURE.md)。

---
│   ├── file_ops/
│   └── git_ops/
│
├── 📁 projects/              ← Independent projects
│   └── (user projects here)
│
└── 📁 templates/             ← Project templates (future)
    ├── python-cli/
    ├── python-fastapi/
    ├── nodejs-express/
    └── static-web/
```

---

## 🔄 Workflow: Graph-Based Navigation
## 工作流程：基於圖的導航

synthforge uses a **graph-based approach** to navigate knowledge:

synthforge 使用**基於圖的方法**來導航知識：

```
VIBE_GUIDE.md (Entry Point)
    ↓
    ├→ README.md → ARCHITECTURE.md → TASKS.md
    ├→ AGENT_RULES.md → DOC_GUIDE.md
    ├→ devtools/README.md → specific tool docs
    ├→ skills/ → specific skill
    └→ agents/ → specific agent
```

**Rule**: Always start from VIBE_GUIDE.md, then follow the graph to relevant documents.

**規則**: 始終從 VIBE_GUIDE.md 開始，然後沿著圖到相關文件。

---

---

## 📋 Critical Rules Index
## 關鍵規則索引

**🚨 MUST READ** before coding / 編碼前必讀:

### Core Rules (MANDATORY) / 核心規則（強制）

1. **[DIRECTORY_README_RULE.md](rules/core/DIRECTORY_README_RULE.md)** 🔴 MOST CRITICAL
   - Read directory README.md before viewing/using/modifying files
   - Update README.md after any file changes
   - Update ARCHITECTURE.md when structure changes
   - 進入目錄前讀 README，修改後更新 README 和 ARCHITECTURE

2. **[VIBE_GUIDE_SYNC_RULE.md](rules/core/VIBE_GUIDE_SYNC_RULE.md)** 🔴 CRITICAL
   - Keep VIBE_GUIDE and ARCHITECTURE in sync
   - Update ARCHITECTURE.md for all structure changes
   - Update VIBE_GUIDE.md only for high-level changes
   - 保持 VIBE_GUIDE 和 ARCHITECTURE 同步

3. **[BILINGUAL_OUTPUT_RULE.md](rules/core/BILINGUAL_OUTPUT_RULE.md)** 🟡 HIGH
   - Layered language strategy
   - Core rules: Bilingual (EN + ZH)
   - .internal/: Chinese only
   - 分層語言策略

4. **[DRY_RULE.md](rules/core/DRY_RULE.md)** 🟡 HIGH
   - Don't Repeat Yourself principle
   - MUST/SHOULD/MAY enforcement
   - Balance DRY with readability
   - 避免重複原則

5. **[FILE_NAMING_CONVENTION_RULE.md](rules/development/FILE_NAMING_CONVENTION_RULE.md)** � MEDIUM
   - File naming standards
   - Consistent naming across project
   - 檔案命名規範

6. **[INTERNAL_RULE.md](rules/development/INTERNAL_RULE.md)** 🟢 MEDIUM
   - .internal/ directory management
   - Task summaries, confirmations, knowledge
   - .internal/ 目錄管理

**See also** / 另見:
- [rules/README.md](rules/README.md) - Complete rules index
- [docs/architecture/SKILLS_VS_RULES.md](docs/architecture/SKILLS_VS_RULES.md) - Understanding Skills vs Rules
- [docs/strategies/GITHUB_STRATEGY.md](docs/strategies/GITHUB_STRATEGY.md) - Git workflow

---

## 🎯 Core Principles
## 核心原則

### 0. **Directory README Rule** 🚨 MOST CRITICAL
**Read [DIRECTORY_README_RULE.md](rules/core/DIRECTORY_README_RULE.md) for full details.**

**MANDATORY**: Before entering ANY subdirectory, MUST read its README.md first.

**強制**: 進入任何子目錄之前，必須先閱讀其 README.md。

**Why**: Every directory's README.md contains:
- File manifest (what files exist)
- Functionality overview
- Dependencies between files
- Usage instructions
- Last updated timestamp

**為什麼**: 每個目錄的 README.md 包含：
- 檔案清單（存在哪些檔案）
- 功能概覽
- 檔案之間的依賴關係
- 使用說明
- 最後更新時間戳記

**Workflow**:
```
1. User asks to work on devtools/cli.py
   ↓
2. STOP! Read devtools/README.md FIRST
   ↓
3. Understand what files exist and how they relate
   ↓
4. NOW work on cli.py
   ↓
5. After modification: UPDATE devtools/README.md
```

**This rule prevents**:
- Broken dependencies (modifying A without updating B)
- Lost context (not knowing what files do)
- Duplicate work (creating files that already exist)

**此規則防止**:
- 破壞依賴（修改 A 而不更新 B）
- 失去上下文（不知道檔案的作用）
- 重複工作（創建已存在的檔案）

---

### 1. **Separation of Concerns**
- `devtools/` = Development tools (not runtime dependencies)
- `projects/` = Independent applications
- `agents/` = AI assistants
- `skills/` = Reusable capabilities

### 2. **Graph-Based Knowledge**
- Documents link to each other
- Follow the graph, don't read linearly
- VIBE_GUIDE.md is the root node

### 3. **Bilingual Everything**
- All documentation: English + Chinese
- All tool outputs: English + Chinese
- Format: Full English, then Full Chinese

### 4. **Security First**
- Always run security checks before release
- Filter sensitive information
- Validate all inputs

### 5. **Modular & Reusable**
- Skills are composable
- Agents are independent
- Tools are standalone

---

## 🚀 Quick Actions
## 快速操作

### For AI Agents:
```bash
# Create new project
python devtools/cli.py new --name=my_app --type=python-fastapi

# Security scan
python devtools/cli.py check projects/my_app --security --deep

# Analyze dependencies
python devtools/cli.py analyze projects/my_app

# Prepare release
python devtools/cli.py release projects/my_app dist/my_app_v1.0 --clean --audit

# Show all tools
python devtools/cli.py info
```

---

## 📝 Remember
## 記住

1. **ALWAYS** start with VIBE_GUIDE.md
2. **FOLLOW** the document graph
3. **USE** the right tool/agent/skill for the task
4. **RESPECT** AGENT_RULES.md guidelines
5. **MAINTAIN** bilingual output

---

**Welcome to synthforge!**  
**歡迎來到 synthforge！**

**Let's build something amazing together.**  
**讓我們一起打造驚人的作品。**

---

**Version**: 1.1  
**Last Updated**: 2026-01-29  
**Maintainer**: synthforge team
