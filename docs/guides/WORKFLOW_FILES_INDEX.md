# Workflow System Files Index / Workflow 系統文件索引

**Comprehensive list of synthforge Workflow System documentation.**
**synthforge Workflow 系統完整文件清單。**

> [!NOTE]
> **Tip**: This document helps users navigate the Workflow system. If docs are missing, check the core rules.
> **提示**: 本文檔旨在幫助用戶快速導航和理解 Workflow 系統。如果您發現文檔缺失，請檢查現有的核心規則。

---

## 📚 Core Documentation / 核心文檔

### 1. System Overview / 系統概覽

#### [workflows/README.md](../workflows/README.md)
**Languages**: Bilingual / 中英雙語  
**Content**: System overview, quick start, directory structure, status.
**內容**: Workflow 系統總覽、快速開始、目錄結構、狀態更新。

#### [docs/architecture/GITHUB_SUPERPOWERS.md](../architecture/GITHUB_SUPERPOWERS.md)
**Languages**: Bilingual / 中英雙語  
**Content**: Architecture, GitHub Superpowers implementation, 100% feature list.
**內容**: synthforge 如何實現 GitHub Superpowers、完整架構說明、100% 功能清單。

#### [workflows/WORKFLOW_RULE.md](../workflows/WORKFLOW_RULE.md)
**Languages**: Bilingual / 中英雙語  
**Content**: Workflow creation and usage rules, naming conventions, best practices.
**內容**: Workflow 創建和使用規則、命名規範、最佳實踐。

---

### 2. Usage Guides / 使用指南

#### [docs/guides/WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md)
**Languages**: English / 英文  
**Content**: Full usage guide, template descriptions, Skills & Agents usage, troubleshooting.
**內容**: 完整的 workflow 使用指南、所有模板說明、Skills & Agents 使用、故障排除。

#### [docs/guides/GIT_WORKTREES_GUIDE.md](GIT_WORKTREES_GUIDE.md)
**Languages**: English / 英文  
**Content**: Git Worktrees usage, API documentation, best practices.
**內容**: Git Worktrees 完整使用指南、API 文檔、最佳實踐。

#### [docs/guides/WORKFLOW_SYSTEM_DETAILS_ZH.md](WORKFLOW_SYSTEM_DETAILS_ZH.md)
**Languages**: Chinese / 中文 [NEW]  
**Content**: Comprehensive guide to the workflow system in Chinese.
**內容**: 專門為中文用戶編寫的 Workflow 系統詳細全攻略。

#### [.github/workflows/README.md](../../.github/workflows/README.md)
**Languages**: English / 英文  
**Content**: GitHub Actions guide, setup, customization.
**內容**: GitHub Actions 使用指南、設置說明、自定義方法。

---

### 3. Rules Documentation / 規則文檔

#### [rules/development/WORKFLOW_INTEGRATION_RULE.md](../../rules/development/WORKFLOW_INTEGRATION_RULE.md)
**Languages**: Bilingual / 中英雙語  
**Content**: Standards for integrating Skills/Agents into workflows.
**內容**: Skills/Agents 如何整合到 workflows 的技術規範。

#### [rules/development/TDD_RULE.md](../../rules/development/TDD_RULE.md)
**Languages**: Bilingual / 中英雙語  
**Content**: TDD standards, Red-Green-Refactor process.
**內容**: 測試驅動開發規範、Red-Green-Refactor 流程。

#### [rules/development/AGENT_STRUCTURE_RULE.md](../../rules/development/AGENT_STRUCTURE_RULE.md)
**Languages**: Bilingual / 中英雙語  
**Content**: Agent development structure standards.
**內容**: Agent 開發結構規範。

---

## 🤖 GitHub Actions Workflows / GitHub Actions 工作流

### 1. [.github/workflows/ai_pr_review.yml](../../.github/workflows/ai_pr_review.yml)
- **AI PR Review**: Automatic code review on PRs using Gemini/Claude.
- **AI PR 審查**: 使用 Gemini/Claude 在 PR 時自動進行代碼審查。

### 2. [.github/workflows/ai_issue_triage.yml](../../.github/workflows/ai_issue_triage.yml)
- **AI Issue Triage**: Auto-labeling and prioritization of issues.
- **AI Issue 分類**: 自動對 Issue 進行標籤分類和優先級排序。

### 3. [.github/workflows/ai_code_analysis.yml](../../.github/workflows/ai_code_analysis.yml)
- **AI Code Analysis**: Weekly analysis of code quality and complexity.
- **AI 代碼分析**: 每週自動分析代碼質量、複雜度和測試覆蓋率。

---

## 📋 Workflow Templates / Workflow 模板

1. [feature_development.yml](../workflows/templates/feature_development.yml): **Feature Development / 功能開發**
2. [bug_fix.yml](../workflows/templates/bug_fix.yml): **Bug Fix / Bug 修復**
3. [refactoring.yml](../workflows/templates/refactoring.yml): **Refactoring / 代碼重構**
4. [rule_creation.yml](../workflows/templates/rule_creation.yml): **Rule Creation / 規則創建**

> [!WARNING]
> **Planned Components / 未來規劃**: Some components (e.g., `research_agent`) are placeholders for future implementation.
> **未來規劃**: 模板中提到的一些組件（如 `research_agent`）目前為預留位置，將在後續開發中逐步實現。

---

## 📊 Statistics / 統計

- **Total Files / 總文件數**: 16
- **Bilingual / 中英雙語**: 10
- **English Only / 純英文**: 5
- **Chinese Only / 純中文**: 1
