---
title: "建構旅程"
document_type: narrative
version: 1.0
language: zh-TW
phases:
  - phase: 1
    name: Foundation
    status: ✅ 完成
    scope: "規則體系、目錄結構、VIBE_GUIDE、CLI 基礎"
    key_insight: "先建規則再寫代碼——治理先行的實驗"
  - phase: 2
    name: Developer Experience
    status: ✅ 完成
    scope: "CLI 七大命令群、知識圖譜、結構優化器、Git 自動化"
    key_insight: "工具要服務流程，而非反過來"
  - phase: 3
    name: Intelligence
    status: ✅ 完成
    scope: "Agents 四代理、Skills 五能力、Workflow Engine v1"
    key_insight: "骨架先到位，executor placeholder 是策略性推遲"
  - phase: 4
    name: Production & Scale
    status: 🚧 30%
    scope: "YAML v2.0、條件邊、重試策略、循環檢測"
    key_insight: "從 v1 到 v2 的斷層，是真正要解決的難題"
pivotal_moments:
  - moment: "VIBE_GUIDE 同步策略從 Option A 改為 Option B"
    impact: "入口文件保持簡潔，細節交給 ARCHITECTURE.md"
  - moment: "INTERNAL_RULE 從 4 條合併為 1 條"
    impact: "DRY_RULE 的實踐，規則本身也要精簡"
  - moment: "Skills vs Agents 的分界確立"
    impact: "無狀態 vs 有狀態的設計取捨確定"
  - moment: "Workflow Engine 選擇 YAML 宣告式而非 Python 命令式"
    impact: "可讀性和可擴展性優先，犧牲了動態靈活性"
related_documents:
  - 01_PHILOSOPHY.md
  - 05_WORKFLOW_ENGINE.md
  - 09_LESSONS.md
tags: [journey, phases, pivotal-moments, evolution]
---

# 建構旅程

> 這不是一個「做完」的專案，是一個「想清楚」的專案。四個 Phase 推進的不是功能，是理解。

## 四個 Phase

### Phase 1: Foundation — 治理先行

**時間線**：2026 年初
**完成度**：✅ 100%

Phase 1 的核心問題是：

> 在 AI 代理進入代碼庫之前，我們需要什麼規矩？

答案是 22 條規則、一個 VIBE_GUIDE、一個目錄結構、一個 .cursorrules。

**做了什麼**：

1. **規則體系**：從零開始定義了 22 條規則，分 core/development/management 三層。每一條規則都是對一個具體問題的回答：
   - 「AI 代理進入目錄前要先讀什麼？」→ DIRECTORY_README_RULE
   - 「雙語文件怎麼管？」→ BILINGUAL_OUTPUT_RULE
   - 「代理怎麼知道要遵守哪些規則？」→ AGENT_WORKFLOW_RULE
   - 「規則重複了怎麼辦？」→ DRY_RULE

2. **VIBE_GUIDE.md**：一個 130 行的入口文件，提供決策樹。AI 代理進入專案時只讀這一個文件。

3. **task.md**：Mission Control，用 `[ ]`、`[/]`、`[x]` 追蹤任務進度。

4. **.cursorrules**：確保 Cursor AI 遵守規則的配置文件。

**思想碰撞**：

最初 VIBE_GUIDE 包含所有規則的摘要（Option A），這讓入口文件膨脹到 300+ 行。後來改為 Option B：VIBE_GUIDE 只保留高層索引和決策樹，細節交給 ARCHITECTURE.md 和各規則文件。

這個改動是 VIBE_GUIDE_SYNC_RULE 的起源——規則本身就是碰撞的產物。

**關鍵洞察**：治理先行的代價是——規則體系完整了，但開始寫代碼之前，你要先讀完 VIBE_GUIDE + AGENT_WORKFLOW_RULE + 路由到的規則。啟動成本是實實在在的。

---

### Phase 2: Developer Experience — 工具服務流程

**時間線**：Phase 1 完成後
**完成度**：✅ 100%

Phase 2 的核心問題是：

> 有了規則，AI 代理和人類用什麼工具來遵守這些規則？

答案是 CLI、知識圖譜、結構優化器。

**做了什麼**：

1. **統一 CLI**（726 行）：10 大命令群，所有操作一個入口。`cli.py` 是整個專案最大的單一文件，也是使用頻率最高的入口。

2. **知識圖譜**（`knowledge_graph.py`）：掃描規則文件的 YAML frontmatter，生成 Mermaid 格式的關聯圖。這是對規則系統複雜度的回應——當你需要一個工具來理解你制定的規則時，規則可能已經太多了。

3. **結構優化器**（`structure_optimizer.py`）：自動化檔案重構，支援 dry-run。配合 DIRECTORY_README_RULE 使用——重構後自動更新 README。

4. **Git 自動化**：定義了 `GitAutomation`、`SmartGitHandler`、`GitWorktreeManager` 的接口（雖然實作未見）。

5. **安全工具**：安全稽核、授權檢查、依賴分析。

**思想碰撞**：

知識圖譜的出現是一個值得注意的時刻。它的存在說明了一件事：**規則系統的複雜度已經超過了人類心智模型的承載能力。** 當你需要自動化工具來理解你制定的規則時，可能需要反思規則的數量。

但知識圖譜也是正確的回應——與其減少規則，不如提供工具來管理複雜度。這是「治理 vs 效率」張力的具體體現。

**關鍵洞察**：工具要服務流程，而非反過來。每一個 CLI 命令都對應一條規則或一個工作流步驟。不是「有什麼工具用什麼」，而是「需要什麼做什麼」。

---

### Phase 3: Intelligence — 骨架到位

**時間線**：Phase 2 完成後
**完成度**：✅ 100%（骨架）

Phase 3 的核心問題是：

> AI 代理應該是什麼形狀？它們之間怎麼分工？怎麼編排？

答案是四個代理、五個技能、一個工作流引擎。

**做了什麼**：

1. **四個代理**：
   - planner_agent：規劃與設計
   - executor_agent：實作與執行
   - reviewer_agent：代碼審查
   - self_improvement_agent：自我學習

   每個代理都有標準結構：AGENT.md + config.yml + `<name>.py`。

2. **五個技能**：
   - spec_parser：解析實作計畫
   - task_generator：生成任務清單
   - test_runner：執行測試
   - structure_management：目錄重構
   - document_skill：文件處理

   每個技能都遵循統一接口：`skill_function(input_data, config=None) -> Dict[str, Any]`。

3. **工作流引擎 v1**：
   - parser.py：YAML → WorkflowDefinition dataclass
   - validators.py：四層驗證
   - executor.py：逐步驟執行（placeholder）
   - context.py：狀態管理，支援序列化
   - 四個內建模板：feature_development、bug_fix、refactoring、rule_creation

**思想碰撞**：Skills vs Agents 的分界不是一開始就清晰的。

最初的想法是「所有 AI 能力都是 Agent」。後來意識到：解析規格、生成任務、執行測試——這些不需要上下文，不需要狀態，它們是純函數。只有規劃、實作、審查才需要累積上下文。

所以確立了：**Skills 無狀態、Agents 有狀態。** 這個區分讓工作流模板可以自由組合 Skills 和 Agents——同一個 Skill 可以被不同的 Agent 使用，同一個 Agent 可以在不同的工作流中起作用。

**另一個碰撞**：executor 為什麼是 placeholder？

因為 executor 需要真正的 AI 推理能力——它要理解規格、寫代碼、跑測試、根據結果修改代碼。這超越了「定義接口」的範圍，需要接入 LLM。在沒有確定 LLM 供應商和調用方式之前，把 executor 做成 placeholder 是合理的——先定義「長什麼樣」，再決定「怎麼跑」。

**關鍵洞察**：骨架先到位，肌肉後填充。這是設計的勝利，也是實作的缺口。 Placeholder 不是偷懶，是策略性推遲。

---

### Phase 4: Production & Scale — 斷層開始

**時間線**：Phase 3 完成後至今
**完成度**：🚧 30%

Phase 4 的核心問題是：

> 從 v1 到 v2，引擎需要什麼才能真的跑起來？

答案是條件邏輯、重試策略、循環檢測——但這些都還沒有實作。

**做了什麼**：

1. **YAML v2.0 規約定義**：定義了條件邊（if-then-else）的語法規約。
2. **工作流 v2.0 執行邏輯設計**：部分完成（`task.md` 中標記為 `[/]`）。
3. **.github/ 配置**：添加了 `copilot-instructions.md`，讓 GitHub Copilot 也遵守規則。

**還沒做的**：

- 條件邏輯實作
- 失敗重試機制
- 循環檢測
- v1 → v2 遷移指南
- Executor 的真正實作
- 依賴管理
- CI/CD

**思想碰撞**：

Phase 4 是斷層開始的地方。前三個 Phase 的推進相對順利——規則體系是設計問題，工具是實作問題，骨架是定義問題。但 Phase 4 的每個問題都觸及核心設計選擇：

- **條件邏輯**：YAML 不支援條件。要加 Jinja2 模板？要加 Python 表達式？要建立自己的 DSL？每一個選擇都影響工作流的可讀性和可維護性。
- **Executor 實作**：接什麼 LLM？怎麼管理 API key？怎麼處理成本？怎麼處理上下文窗口限制？
- **測試基礎設施**：TDD_RULE 要求 80% 覆蓋率，但專案本身連 `requirements.txt` 都沒有。

Phase 4 還在進行中。`task.md` 顯示的狀態：

```markdown
## Phase 5B: Workflow Intelligence
- [x] 定義 YAML v2.0 規約 [x]
- [/] 撰寫 Workflow v2.0 執行邏輯設計文檔 [/]
- [ ] 實作條件邊 (Conditional Edges) 邏輯 [ ]
- [ ] 支援失敗重試 (Retry Strategy) 機制 [ ]
- [ ] 實作基礎循環檢測 (Cycle Detection) [ ]
```

第一項完成了，第二項進行中，其餘未開始。

---

## 四個關鍵轉折

### 轉折 1：VIBE_GUIDE 從 Option A 到 Option B

最初 VIBE_GUIDE 包含所有規則摘要（Option A），入口文件暴增到 300+ 行。改為 Option B 後，VIBE_GUIDE 只保留索引和決策樹，維持在 ~130 行。

這是一個「做減法」的決策——入口文件不是越完整越好，而是越容易導航越好。

### 轉折 2：INTERNAL_RULE 從 4 條合併為 1 條

CONFIRMATION_DOCUMENTS_RULE、INTERNAL_MANAGEMENT_RULE、TASK_SUMMARY_RULE、TODO_UPDATE_RULE 四條規則有大量重疊。按照 DRY_RULE 的邏輯（3 次以上必須抽取），它們被合併為一條 INTERNAL_RULE。

這是 DRY_RULE 對自身的實踐——治理規則也需要精簡。

### 轉折 3：Skills vs Agents 分界確立

最初所有 AI 能力都被設想為「Agent」。後來區分了 Skills（無狀態、純函數、高可重用）和 Agents（有狀態、有上下文、需要編排）。

這個區分影響了整個架構：
- Skills 可以被任何 Agent 使用
- Agents 可以在 Skills 之上建立複雜行為
- 工作流模板可以自由組合 Skills 和 Agents

### 轉折 4：YAML 宣告式 vs Python 命令式

工作流定義語言的選擇：YAML（宣告式，可讀）還是 Python（命令式，靈活）？

選了 YAML。理由：
1. 非程式設計師也能看懂
2. 可以在執行前驗證結構
3. 修改流程不需要改代碼

代價：YAML 無法表達複雜條件邏輯。v2.0 的條件邊和重試策略需要擴展 YAML 語法，這帶來了新的設計挑戰。

---

## 時間線總結

```
Phase 1: Foundation（治理先行）
  ├─ 22 條規則
  ├─ VIBE_GUIDE（Option A → Option B）
  ├─ task.md
  ├─ .cursorrules + .github/copilot-instructions.md
  └─ 三層規則分類（core/development/management）

Phase 2: Developer Experience（工具服務流程）
  ├─ CLI（726 行，10 大命令群）
  ├─ 知識圖譜
  ├─ 結構優化器
  ├─ Git 自動化（接口定義）
  └─ 安全工具

Phase 3: Intelligence（骨架到位）
  ├─ 四個代理（標準結構，placeholder 實作）
  ├─ 五個技能（大部分完成）
  ├─ 工作流引擎 v1（Parser ✅ Validator ✅ Executor ⚠️ Context ✅）
  └─ 四個內建模板

Phase 4: Production & Scale（斷層開始）
  ├─ YAML v2.0 規約定義 ✅
  ├─ Executor 實作 ❌
  ├─ 條件邏輯 ❌
  ├─ 重試策略 ❌
  ├─ 循環檢測 ❌
  └─ 依賴管理 ❌
```

**日期參考**：LICENSE 文件標註 `Last Updated: 2026-02-02`，VIBE_GUIDE.md 版本標記為 `Version: 3.0`。專案在 2026 年初積極開發，Phase 4 仍在進行中。