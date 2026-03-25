# synthforge - AI-Driven Development Environment
# synthforge - AI 驅動的開發環境

> **🤖 FOR AI AGENTS**: Read [VIBE_GUIDE.md](VIBE_GUIDE.md) FIRST before proceeding.  
> **給 AI 代理**: 請先閱讀 [VIBE_GUIDE.md](VIBE_GUIDE.md)。

[![Version](https://img.shields.io/badge/version-1.1.3-blue.svg)](https://github.com/xx8897/synthforge)
[![License](https://img.shields.io/badge/license-Dual--License-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Production%20Ready-success.svg)](docs/architecture/ROADMAP_v2.md)

---

## 🎯 What is synthforge? / 什麼是 synthforge？

**synthforge** is a production-ready AI development environment that automates your entire development workflow from specification to deployment.

**synthforge** 是一個生產就緒的 AI 開發環境，可自動化從規格到部署的整個開發工作流程。

### Key Features / 核心功能

- **🤖 4 Specialized AI Agents** - Planner, Executor, Reviewer, Self-Improvement
- **⚡ Automated Workflows** - TDD, Feature Development, Bug Fixing, Refactoring
- **🔧 Unified CLI** - One command for all operations
- **📋 23 Governance Rules** - Ensure code quality and consistency
- **🌳 Git Worktrees** - Isolated development environments
- **🔒 Security First** - Built-in security scanning and auditing
- **📊 Mission Control** - Integrated progress tracking via `task.md`

---

## 🚀 Quick Start / 快速開始

### Prerequisites / 前置需求

- Python 3.8+
- Git 2.30+
- Windows/Linux/macOS

### Installation / 安裝

```bash
# Clone the repository
git clone https://github.com/xx8897/synthforge.git
cd synthforge

# Install dependencies (if needed)
# pip install -r requirements.txt
```

### Basic Usage / 基本使用

```bash
# Interactive mode - recommended for beginners
# 互動模式 - 推薦給初學者
python devtools/cli.py interactive

# List all available workflows
# 列出所有可用的工作流
python devtools/cli.py workflow list

# Run a feature development workflow
# 執行功能開發工作流
python devtools/cli.py workflow run workflows/templates/feature_development.yml

# Git operations
# Git 操作
python devtools/cli.py git commit -m "feat: add new feature" -a
python devtools/cli.py git push
python devtools/cli.py git pr --title "New Feature"

# Security check
# 安全檢查
python devtools/cli.py check --all

# Document processing
# 文件處理
python devtools/cli.py doc load spec.pdf --split
```

---

## 📁 Project Structure / 專案結構

```
synthforge/
├── 📄 README.md                 ← You are here / 你在這裡
├── 📄 VIBE_GUIDE.md             ← AI agent entry point / AI 代理入口
├── 📄 task.md                   ← Mission Control Tracker
├── 📄 LICENSE                   ← Dual License (AGPL-3.0 + Commercial)
│
├── 📁 rules/                    ← 23 governance rules / 23 條治理規則
│   ├── core/                    ← Mandatory rules / 強制規則
│   ├── development/             ← Development rules / 開發規則
│   └── management/              ← Management rules / 管理規則
│
├── 📁 devtools/                 ← Development toolkit / 開發工具包
│   ├── cli.py                   ← Unified CLI / 統一 CLI
│   ├── security/                ← Security tools / 安全工具
│   ├── analyzers/               ← Code analyzers / 代碼分析器
│   └── knowledge_graph.py       ← Knowledge mapping / 知識映射
│
├── 📁 workflows/                ← Automated workflows / 自動化工作流
│   ├── engine/                  ← Workflow engine / 工作流引擎
│   └── templates/               ← Workflow templates / 工作流模板
│
├── 📁 agents/                   ← AI agents / AI 代理
│   ├── planner_agent/           ← Planning & design / 規劃與設計
│   ├── executor_agent/          ← Implementation / 實作
│   ├── reviewer_agent/          ← Code review / 代碼審查
│   └── self_improvement_agent/  ← Learning / 學習
│
├── 📁 skills/                   ← Reusable capabilities / 可重用能力
│   ├── automation/              ← Structure management / 結構管理
│   └── workflow_skills/         ← Spec parser, task generator / 規格解析器、任務生成器
│
├── 📁 core_lib/                 ← Shared infrastructure / 共享基礎設施
│   ├── utils/                   ← Utilities / 工具
│   └── git/                     ← Git automation / Git 自動化
│
└── 📁 docs/                     ← Documentation / 文件
    ├── architecture/            ← System design / 系統設計 (ROADMAP_v2.md)
    └── guides/                  ← User guides / 使用指南
```

---

## 🔄 Git Workflow / Git 工作流程

synthforge uses **Feature Branch Workflow** with **Git Worktrees** for clean, isolated development.

synthforge 使用**功能分支工作流程**和 **Git Worktrees** 來實現乾淨、隔離的開發。

### Recommended Workflow / 推薦工作流程

```bash
# 1. Start a new feature
# 1. 開始新功能
python devtools/cli.py workflow run workflows/templates/feature_development.yml

# This will:
# 這將會：
# - Create a new branch (e.g., feature/user-auth)
# - Set up a Git worktree (isolated workspace)
# - Guide you through TDD implementation
# - Run tests automatically
# - Create a PR when done

# 2. Commit changes
# 2. 提交變更
python devtools/cli.py git commit -m "feat: add user authentication" -a

# 3. Push to remote
# 3. 推送到遠端
python devtools/cli.py git push

# 4. Create pull request
# 4. 創建 Pull Request
python devtools/cli.py git pr --title "Add User Authentication" --body "Implements login/logout"

# 5. After PR is merged, cleanup
# 5. PR 合併後，清理
git worktree remove .worktrees/feature_user-auth
git branch -d feature/user-auth
```

> **💡 Pro Tip**: The `-a` parameter automatically stages all modified files, so you don't need `git add`!  
> **💡 專業提示**: `-a` 參數會自動暫存所有已修改的文件，所以您不需要 `git add`！

---

## 📊 Current Status / 當前狀態

| Phase | Status | Completion |
|-------|--------|------------|
| **Phase 1: Foundation** | ✅ Complete | 100% |
| **Phase 2: Developer Experience** | ✅ Complete | 100% |
| **Phase 3: Intelligence** | ✅ Complete | 100% |
| **Phase 4: Production & Scale** | 🚧 In Progress | 30% |

See [ROADMAP_v2.md](docs/architecture/ROADMAP_v2.md) for detailed progress.

查看 [ROADMAP_v2.md](docs/architecture/ROADMAP_v2.md) 了解詳細進度。

---

## 📚 Documentation / 文件

- **[VIBE_GUIDE.md](VIBE_GUIDE.md)** - AI agent entry point / AI 代理入口
- **[ARCHITECTURE.md](docs/architecture/ARCHITECTURE.md)** - System architecture / 系統架構
- **[ROADMAP_v2.md](docs/architecture/ROADMAP_v2.md)** - Strategic roadmap / 戰略路線圖
- **[GIT_WORKFLOW.md](docs/guides/GIT_WORKFLOW.md)** - Git workflow guide / Git 工作流程指南
- **[rules/README.md](rules/README.md)** - All governance rules / 所有治理規則

---

## 🎯 Core Principles / 核心原則

1. **Automation First** - Automate repetitive tasks / 自動化優先
2. **Test-Driven Development** - Write tests first / 測試驅動開發
3. **Security by Default** - Built-in security checks / 預設安全
4. **Documentation as Code** - Keep docs in sync / 文件即代碼
5. **Continuous Improvement** - Learn from every iteration / 持續改進

---

## 📄 License / 授權

This project is licensed under a Dual License (AGPL-3.0 + Commercial) - see the [LICENSE](LICENSE) file for details.

本專案採用雙重授權 (AGPL-3.0 + 商業授權) - 詳見 [LICENSE](LICENSE) 文件。

---

## 👤 Author / 作者

**xx8897**

---

**Built with ❤️ using Python and AI**  
**使用 Python 和 AI 用心打造**
