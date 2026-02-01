# synthforge Workflow 系統全攻略 (詳細指南)

**本文專為中文用戶設計，旨在深度介紹 synthforge 的自動化工作流架構、設計理念及日常操作。**

---

## 🌟 核心理念：AI 驅動的自動化 (Agentic Automation)

synthforge 的 Workflow 系統不僅僅是一個「腳本執行器」，它是一個基於 **GitHub Superpowers** 理念構建的「代理工作流」。它的核心目的是：**讓 AI (Gemini/Claude) 自動完成從「規格定義」到「代碼實現」的全過程。**

### 為什麼我們需要它？
- **告別手動轉換**: 您寫完 `implementation_plan.md`，系統自動幫您拆解成 `task.md`。
- **隔離開發環境**: 透過 **Git Worktrees**，AI 在背後的小房間寫代碼，不會把您的主目錄弄亂。
- **質量保證**: 強制執行 **TDD (測試驅動開發)**，代碼寫完自動測試，沒過不收。
- **全天候監控**: 透過 **GitHub Actions**，即使您關掉電腦，AI 還是在幫您審查 PR 和分析代碼。

---

## 🏗️ 系統三大支柱 (The Three Pillars)

### 1. Workflows (工作流模板)
工作流是 YAML 格式的指令集，定義了「先做什麼，後做什麼」。
- **位於**: `workflows/templates/`
- **主要模板**:
  - `feature_development.yml`: 開發新功能的最強工具。
  - `bug_fix.yml`: 自動診斷並修復 Bug。
  - `refactoring.yml`: 代碼優化與重構，確保功能不變。

### 2. Agents (AI 代理)
Agent 是「大腦」，負責決策和複雜任務。
- **Planner Agent**: 負責規劃，確保任務清單邏輯通順。
- **Executor Agent**: 負責寫代碼，它是 TDD 的忠實執行者。
- **Reviewer Agent**: 負責挑刺，從性能、安全、風格各方面審核代碼。

### 3. Skills (模組化技能)
Skill 是「工具箱」，負責具備特定功能的無狀態操作。
- **spec_parser**: 閱讀您的計畫書。
- **task_generator**: 畫出任務地圖。
- **test_runner**: 像考官一樣檢查代碼。

---

## 🚀 實戰操作流程

如果您要開始一個新的功能開發，典型的流程如下：

### 第一步：撰寫規格 (Spec-as-Source)
您只需要寫一份詳細的 `implementation_plan.md`，定義好您的目標和改動。

### 第二步：啟動工作流 (Execution)
在終端機輸入：
```bash
python devtools/cli.py workflow run workflows/templates/feature_development.yml
```
此時系統會：
1. **Specify**: 呼叫 `spec_parser` 解析計畫書。
2. **Plan**: 呼叫 `task_generator` 產出 `task.md`。
3. **Draft**: AI 會在大腦中構思各個文件的改動。
4. **Implement**: 啟動 **Git Worktrees**，在獨立分支執行 TDD（紅燈 -> 綠燈 -> 重構）。
5. **Review**: 完成後，AI 自己先審核一遍產出的代碼。

### 第三步：提交並觸發雲端審核 (Cloud Verification)
當您將代碼推送到 GitHub：
- **AI PR Review**: GitHub Actions 會自動啟動，Gemini 或 Claude 會在您的 PR 下方留言指出改進點。
- **AI Code Analysis**: 定期檢查您的代碼複雜度，並在儀表板更新統計數據。

---

## 🔍 關鍵技術名詞通俗解釋

| 名詞 | 白話解釋 |
|------|----------|
| **GitHub Actions** | 住在雲端的 24 小時守衛。專門自動化 PR 審查和測試。 |
| **Git Worktrees** | 專案的「影子分身」。讓 AI 在分身裡寫代碼，您在主身工作，互不干擾。 |
| **GitHub Models** | AI 的「轉運中心」。讓我們可以自由選用 Gemini 或 Claude 等多種大腦。 |
| **TDD (測試驅動開發)** | 「先寫試卷答案，再教學生寫內容」。確保代碼 100%符 合規範。 |

---

## 🔗 導航地圖

- [快速導航手冊](WORKFLOW_FILES_INDEX.md)
- [如何撰寫工作流 (規則)](../../workflows/WORKFLOW_RULE.md)
- [如何將組件接入系統](../../rules/development/WORKFLOW_INTEGRATION_RULE.md)

---

**最後更新**: 2026-02-01  
**編寫者**: synthforge Core Team
