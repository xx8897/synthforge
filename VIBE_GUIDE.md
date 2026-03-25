# VIBE GUIDE - AI Agent Entry Point
# VIBE 指南 - AI 代理入口

**Purpose**: This is the FIRST file AI agents should read when entering the synthforge workspace.  
**目的**: 這是 AI 代理進入 synthforge 工作區時應該首先閱讀的檔案。

related_rules:
  - TASK_MANAGEMENT_RULE
  - SMART_GIT_RULE
  - GIT_EXECUTION_RULE
  - GRAPH_RELATIONSHIP_RULE
  - CORE_RULE

## 🚀 Mission Control / 任務控制中心
The file [task.md](file:///c:/Users/xx8897/synthforge/task.md) is the **Mission Control** of this project. 
- **AI Rule**: ALWAYS check `task.md` first to understand the current priority.
- **AI Rule**: ALWAYS update `task.md` when progress is made.

---

## 📖 Terminology / 術語

**Workspace** = **synthforge**  
**GitHub**: `https://github.com/xx8897/synthforge` (private)
**Branching Strategy**: Feature Branch Workflow with Git Worktrees.

---

## 🎯 What is synthforge?

**synthforge** is an AI-driven development environment that combines:
- **Unified CLI** (`devtools/cli.py`) - One entry point for all tools.
- **Workflow Engine** (`workflows/`) - Automated TDD and Refactoring.
- **AI Agents** (`agents/`) - Specialized autonomous agents (Planner, Executor, etc.).
- **Reusable Skills** (`skills/`) - Modular capabilities (Parser, Runner, etc.).
- **Rules System** (`rules/`) - 23 strict governance rules.

---

## 📚 Navigation Architecture - Strong Links
## 導航架構 - 強連結

**From VIBE_GUIDE, you MUST read these directory entry points:**

1. **[rules/README.md](rules/README.md)** - Rules Index (🚨 Read FIRST)
2. **[docs/architecture/ARCHITECTURE.md](docs/architecture/ARCHITECTURE.md)** - System Design
3. **[docs/architecture/ROADMAP_v2.md](docs/architecture/ROADMAP_v2.md)** - Completion Status
4. **[docs/guides/GIT_WORKFLOW.md](docs/guides/GIT_WORKFLOW.md)** - Git & Workflow Guide
5. **[devtools/README.md](devtools/README.md)** - Tooling Index

---

## 🤖 For AI Agents: Decision Tree
## 給 AI 代理：決策樹

```
START: Read VIBE_GUIDE.md (this file)
  ↓
QUESTION: What is your task?
  ↓
  ├─ "Start new feature"
  │   → Read: docs/guides/GIT_WORKFLOW.md
  │   → Use: python devtools/cli.py workflow run workflows/templates/feature_development.yml
  │
  ├─ "Fix a bug"
  │   → Use: python devtools/cli.py workflow run workflows/templates/bug_fix.yml
  │
  ├─ "Git operations"
  │   → Use: python devtools/cli.py git commit/push/pr
  │
  ├─ "Security check"
  │   → Use: python devtools/cli.py check --all
  │
  └─ "Check Status"
      → Read: docs/architecture/ROADMAP_v2.md
```

---

## 🎨 Knowledge Graph & Mapping
## 知識圖譜與映射

synthforge implements automated relationship mapping:
- **Visual Graph**: Read `devtools/knowledge_graph.py`.
- **Knowledge Map**: Check `.internal/knowledge/knowledge_map.md`.

---

## 📋 Critical Rules Index
## 關鍵規則索引

**🚨 MUST COMPLY** / 必須遵守:

1. **[DIRECTORY_README_RULE.md](rules/core/DIRECTORY_README_RULE.md)** 🔴 CRITICAL
   - Read directory README before touching any file.
2. **[BILINGUAL_OUTPUT_RULE.md](rules/core/BILINGUAL_OUTPUT_RULE.md)** 🔴 CRITICAL
   - Summaries and main docs MUST be English + Chinese.
3. **[AGENT_WORKFLOW_RULE.md](rules/core/AGENT_WORKFLOW_RULE.md)** 🔴 CRITICAL
   - Follow Spec -> Design -> Implement -> Review workflow.
4. **[TDD_RULE.md](rules/development/TDD_RULE.md)** 🔴 CRITICAL
   - Test-Driven Development is mandatory for all features.

---

## 🚀 Quick Actions
## 快速操作

```bash
# Workflow list
python devtools/cli.py workflow list

# Secure commit
python devtools/cli.py git commit -m "feat: description" -a

# Interactive shell
python devtools/cli.py interactive

# Project status
python devtools/cli.py info
```

---

**Welcome to synthforge v1.0!**  
**歡迎來到 synthforge v1.0！**

**Status**: Production Ready ✅  
**Version**: 3.0  
**Last Updated**: 2026-02-02
