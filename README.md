# synthforge - AI-Driven Development Environment

> **🤖 FOR AI AGENTS**: Read [VIBE_GUIDE.md](VIBE_GUIDE.md) FIRST before proceeding. It contains the entry point and navigation guide for this workspace.

> **給 AI 代理**: 在繼續之前，請先閱讀 [VIBE_GUIDE.md](VIBE_GUIDE.md)。它包含此工作區的入口點和導航指南。

---

> A comprehensive, AI-driven development environment with professional devtools, multi-language support, and security-first design.

## 🎯 Vision

This workspace is designed to be your **personal AI development lab** - a centralized platform where you can:
- Build reusable AI capabilities (Skills)
- Create specialized AI agents (Agents)
- Develop projects that leverage these shared resources
- Scale from prototype to production seamlessly

## 🏗️ Architecture Overview

This workspace follows a **Studio/Monorepo** pattern where everything lives together:

```
AI_Workspace/
├── 🧠 agents/          # AI personas with specific roles
├── 🛠️ skills/         # Reusable capabilities
├── 📂 projects/        # Your actual work
├── 🔌 core_lib/        # The SDK that ties everything together
└── [30+ supporting systems for production readiness]
```

### Key Principles

1. **Write Once, Use Everywhere**: Skills and agents are shared across all projects
2. **Modular & Extensible**: Each component is independent and pluggable
3. **Production-Ready**: Built-in observability, testing, and deployment
4. **Developer-Friendly**: Templates, automation, and great DX

## 📚 Documentation

- **[ARCHITECTURE.md](./ARCHITECTURE.md)** - Detailed system design and patterns
- **[FEATURES.md](./FEATURES.md)** - Complete feature catalog (30+ features)
- **[ROADMAP.md](./ROADMAP.md)** - Implementation phases and priorities
- **[QUICKSTART.md](./QUICKSTART.md)** - Get started in 5 minutes
- **[AGENT_RULES.md](./AGENT_RULES.md)** - ⚠️ Mandatory rules for all agents (bilingual documentation standards)

## 🚀 Quick Start

```bash
# 1. Navigate to workspace
cd C:\Users\xx8897\ai_workspace

# 2. Set up Python environment
python -m venv .venv
.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements/base.txt

# 4. Create your first project
python core_lib/cli.py new-project --name=my_first_project

# 5. Start building!
cd projects/my_first_project
```

## 🎓 Core Concepts

### Skills
**Reusable capabilities** that agents can use. Think of them as tools in a toolbox.
- Example: `web_search`, `file_operations`, `data_analysis`
- Located in: `skills/`
- Versioned for stability

### Agents
**AI personas** with specific roles and expertise.
- Example: `researcher`, `coder`, `writer`
- Located in: `agents/`
- Can use multiple skills

### Projects
**Your actual work** that uses agents and skills.
- Example: `game_bot`, `data_pipeline`, `web_scraper`
- Located in: `projects/`
- Each project is its own git repository

## 🌟 Feature Highlights

This workspace includes **30 enterprise-grade features**:

### Foundation (Phase 1)
- ✅ Templates System - Instant project scaffolding
- ✅ Core Library - Unified SDK
- ✅ Shared Environment - One venv for all

### Production (Phase 2-3)
- 📊 Observability - Logs, metrics, monitoring
- 🏷️ Versioning - Prevent breaking changes
- 💰 Cost Tracking - Control API spending
- 🚢 Deployment - Docker, K8s, serverless

### Advanced (Phase 4-5)
- 🎭 Multi-Model Orchestration - Auto-select best model
- 🔄 Workflow Orchestration - Multi-agent pipelines
- 🧠 Self-Improving Agents - Learn from mistakes
- 🎨 Dynamic Skill Composition - Auto-generate new skills

See [FEATURES.md](./FEATURES.md) for the complete list.

## 📊 Current Status

**Phase**: Planning & Documentation ✅  
**Next**: Foundation Implementation

## 🤝 Contributing

This is your personal workspace, but the architecture is designed to support:
- Team collaboration (multi-tenancy)
- Skill sharing (federation)
- Plugin ecosystem

## 📄 License

Personal use. Extend as needed.

---

**Built with**: Python, Modern AI practices, Enterprise patterns  
**Inspired by**: OpenAI, Anthropic, Google DeepMind internal tools

---

# AI 工作區 - 世界級 AI 開發平台

> 一個全面的、生產級的環境，用於在所有專案中開發、管理和部署 AI Agent 和技能。

## 🎯 願景

此工作區旨在成為您的**個人 AI 開發實驗室** - 一個集中式平台，您可以：
- 建立可重複使用的 AI 能力（技能）
- 創建專業化的 AI Agent（代理）
- 開發利用這些共享資源的專案
- 從原型無縫擴展到生產環境

## 🏗️ 架構概覽

此工作區遵循 **Studio/Monorepo** 模式，所有內容都在一起：

```
AI_Workspace/
├── 🧠 agents/          # 具有特定角色的 AI 角色
├── 🛠️ skills/         # 可重複使用的能力
├── 📂 projects/        # 您的實際工作
├── 🔌 core_lib/        # 將所有內容連接在一起的 SDK
└── [30+ 個生產就緒的支援系統]
```

### 核心原則

1. **寫一次，到處使用**：技能和 Agent 在所有專案中共享
2. **模組化且可擴展**：每個組件都是獨立且可插拔的
3. **生產就緒**：內建可觀測性、測試和部署
4. **開發者友好**：模板、自動化和出色的開發體驗

## 📚 文檔

- **[ARCHITECTURE.md](./ARCHITECTURE.md)** - 詳細的系統設計和模式
- **[FEATURES.md](./FEATURES.md)** - 完整的功能目錄（30+ 個功能）
- **[ROADMAP.md](./ROADMAP.md)** - 實施階段和優先級
- **[QUICKSTART.md](./QUICKSTART.md)** - 5 分鐘快速開始
- **[AGENT_RULES.md](./AGENT_RULES.md)** - ⚠️ 所有 Agent 的強制性規則（雙語文檔標準）

## 🚀 快速開始

```bash
# 1. 導航到工作區
cd C:\Users\xx8897\ai_workspace

# 2. 設置 Python 環境
python -m venv .venv
.venv\Scripts\activate

# 3. 安裝依賴項
pip install -r requirements/base.txt

# 4. 創建您的第一個專案
python core_lib/cli.py new-project --name=my_first_project

# 5. 開始建構！
cd projects/my_first_project
```

## 🎓 核心概念

### 技能 (Skills)
Agent 可以使用的**可重複使用的能力**。將它們視為工具箱中的工具。
- 範例：`web_search`, `file_operations`, `data_analysis`
- 位於：`skills/`
- 版本化以確保穩定性

### 代理 (Agents)
具有特定角色和專業知識的 **AI 角色**。
- 範例：`researcher`, `coder`, `writer`
- 位於：`agents/`
- 可以使用多個技能

### 專案 (Projects)
使用 Agent 和技能的**您的實際工作**。
- 範例：`game_bot`, `data_pipeline`, `web_scraper`
- 位於：`projects/`
- 每個專案都是自己的 git 儲存庫

## 🌟 功能亮點

此工作區包含 **30 個企業級功能**：

### 基礎（階段 1）
- ✅ 模板系統 - 即時專案腳手架
- ✅ 核心庫 - 統一的 SDK
- ✅ 共享環境 - 所有專案使用一個 venv

### 生產（階段 2-3）
- 📊 可觀測性 - 日誌、指標、監控
- 🏷️ 版本控制 - 防止破壞性變更
- 💰 成本追蹤 - 控制 API 支出
- 🚢 部署 - Docker、K8s、無伺服器

### 進階（階段 4-5）
- 🎭 多模型編排 - 自動選擇最佳模型
- 🔄 工作流編排 - 多 Agent 管道
- 🧠 自我改進的 Agent - 從錯誤中學習
- 🎨 動態技能組合 - 自動生成新技能

查看 [FEATURES.md](./FEATURES.md) 以獲取完整列表。

## 📊 當前狀態

**階段**: 規劃與文檔 ✅  
**下一步**: 基礎實施

## 🤝 貢獻

這是您的個人工作區，但架構設計支援：
- 團隊協作（多租戶）
- 技能共享（聯邦）
- 插件生態系統

## 📄 授權

個人使用。根據需要擴展。

---

**建構使用**: Python, 現代 AI 實踐, 企業模式  
**靈感來自**: OpenAI, Anthropic, Google DeepMind 內部工具
