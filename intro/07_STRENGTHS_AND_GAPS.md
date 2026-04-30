---
title: "優劣分析"
document_type: evaluation
version: 1.0
language: zh-TW
strengths:
  - area: 規則體系
    detail: "22+ 條規則覆蓋開發全流程，從命名到測試到 Git 策略"
  - area: 架構分層
    detail: "清晰的依賴方向：Rules > Skills/Agents > core_lib，devtools 不反向依賴"
  - area: 工作流引擎設計
    detail: "YAML 宣告式定義 + dataclass 解析 + 驗證器，可擴展"
  - area: 文件完備
    detail: "每個目錄有 README，每條規則有完整範例，VIBE_GUIDE 作為 AI 入口"
  - area: Progressive Disclosure
    detail: "AI 代理從 VIBE_GUIDE 入口，按需讀取，不一次灌滿 context"
  - area: 自我改進代理
    detail: "self_improvement_agent 設計了學習資料庫，展示遞迴改進的思維"
  - area: 任務管理協調
    detail: "task.md 作為 Mission Control，[ ] [/] [x] 狀態標記是人機協調的巧思"
gaps:
  - area: Executor 是 placeholder
    detail: "工作流引擎的 executor 找到 skill/agent 但不匯入執行，返回模擬結果"
  - area: 規則啟動成本高
    detail: "AI 代理每次任務前需讀取多條規則，warm-up 負擔重"
  - area: 循環引用風險
    detail: "規則之間互相引用，有時 SSOT 原則與實際操作矛盾"
  - area: 缺少實際測試基礎設施
    detail: "測試檢查檔案存在而非功能，test_runner 依賴未配置的 pytest 環境"
  - area: core_lib/git 缺失
    detail: "GitAutomation/SmartGitHandler/GitWorktreeManager 被引用但實作未找到"
  - area: 雙語維護成本
    detail: "核心規則全雙語，維護量翻倍，分層策略未完全貫徹"
  - area: 無 requirements.txt
    detail: "click/pyyaml/pytest 等依賴未管理"
related_documents:
  - 00_OVERVIEW.md
  - 03_RULES_SYSTEM.md
  - 09_LESSONS.md
tags: [strengths, gaps, evaluation, honest-assessment]
---

# 優劣分析

> 架構很漂亮，骨架很完整，但有些地方只有骨架。這不是批評，是記錄。

## 優點

### 1. 規則體系完整且有層次

22 條規則覆蓋了開發全流程：命名、文件、Git、測試、DRI、任務管理、知識管理、代碼風格……每一條都有對應的問題場景和解決方案。

更重要的是，規則不是平的——它們分 core（強制）、development（推薦）、management（建議）三層，對應「違反會死」「違反會病」「違反會慢」三個等級。這個分層比「所有規則都一樣重要」的做法好很多。

### 2. 架構分層清晰

依賴方向是單向的：

```
rules（被讀取，不依賴任何人）
  ↑
devtools → core_lib
skills  → core_lib
agents  → core_lib + skills
  ↑
workflows（編排層，調用 skills 和 agents）
```

`TOOLING_USAGE_RULE.md` 明確規定：`core_lib` 是 runtime 依賴，`devtools` 是 dev 依賴，`core_lib` 不能反向 import `devtools`。這條規則防止了循環依賴。

### 3. 工作流引擎設計合理

Parser → Validator → Executor → Context 的管線設計是乾淨的。每個模組有明確的職責：

- Parser：解析 YAML，不關心執行
- Validator：驗證正確性，不關心執行
- Executor：執行流程，不關心定義和驗證
- Context：管理狀態，不關心流程邏輯

即使 Executor 是 placeholder，這個分層讓填充實作變得有路可循。

### 4. 文件完備到異常

每個目錄有 README，每條規則有完整範例，每個代理和技能有 AGENT.md/SKILL.md。VIBE_GUIDE.md 作為 AI 代理的入口文件，提供清晰的決策樹。

這不是偶然——DIRECTORY_README_RULE 強制要求這樣做。規則驅動了文件品質。

### 5. Progressive Disclosure 有效

AI 代理進入專案時只讀 VIBE_GUIDE.md（~130 行），然後根據決策樹按需讀取更多規則。這比一次性載入所有規節省了大量 context window。

### 6. self_improvement_agent 有前瞻性

一個會學習的代理——從錯誤中改進、優化工作流、監控效能。即使目前只是骨架，這個設計方向是正確的：AI 開發流程本身就應該可改進。

### 7. task.md 作為 Mission Control

`task.md` 使用簡單的 checklist 格式（`[ ]`、`[/]`、`[x]`），Git 友好、人類可讀、AI 可解析。它是人機協調的單一窗口——比任何任務管理工具都簡單有效。

---

## 缺口

### 1. Executor 是 placeholder —— 最關鍵的缺口

工作流引擎的 executor 能找到 skill/agent 的路徑，但不會動態匯入和執行。它打印 `[PLACEHOLDER] Would execute skill at: ...`，然後返回模擬結果。

這意味著：
- parser 和 validator 可以正常工作
- 但工作流的實際執行從未發生
- 所有 agent 的核心方法都是 `pass`
- 整個系統是「可解析、可驗證、不可執行」

**為什麼是這樣**：這是策略性的——先定義接口和流程，再填充實作。骨架到位了，肌肉還沒長。

**影響**：整個系統目前只能做流程演練，不能做真正的開發工作。

### 2. 規則啟動成本高

AI 代理每次啟動的流程：
1. 讀 VIBE_GUIDE.md（~130 行）
2. 讀 AGENT_WORKFLOW_RULE（路由表）
3. 讀路由到的具體規則（1-5 個文件，每個 100-600 行）
4. 讀目錄 README（每次進入新目錄）

總計：300-3000 行的「啟動稅」。對於簡單任務，這個成本不合理。

### 3. 循環引用風險

規則互相引用形成網路：
- DIRECTORY_README_RULE 引用 VIBE_GUIDE_SYNC_RULE
- VIBE_GUIDE_SYNC_RULE 引用 ARCHITECTURE.md
- ARCHITECTURE.md 引用各規則的 README
- SSOT 規則說 VIBE_GUIDE 是導航的權威，但 DIRECTORY_README_RULE 是最被引用的規則

有時候「誰是權威」和「誰最常被引用」是矛盾的。

### 4. 測試基礎設施不完整

`workflows/tests/` 存在，但測試主要檢查「檔案是否存在」而非「功能是否正確」。`test_runner` skill 依賴 pytest 環境，但 `requirements.txt` 不存在。

TDD_RULE 要求 80% 覆蓋率，但專案本身沒有依賴管理，也沒有 CI 配置。

### 5. core_lib/git 模組缺失

`GitAutomation`、`SmartGitHandler`、`GitWorktreeManager` 在多處被引用（executor_agent、CLI、規則文件），但實作文件不在目前可見的檔案系統中。可能是：
- 在 .gitignore 排除的目錄中
- 在其他分支
- 尚未建立

### 6. 雙語維護成本

BILINGUAL_OUTPUT_RULE 定義了三層策略（雙語/純中文/純英文），但實際執行中很多開發規則仍然是全雙語的。這意味著：
- 每次修改規則要改兩個語言版本
- 兩個版本可能不同步
- 沒有自動同步機制

### 7. 缺少依賴管理

`click`、`pyyaml`、`pytest`、`pytest-asyncio` 是必需的依賴，但沒有 `requirements.txt` 或 `setup.py`。安裝 synthforge 需要手動 `pip install` 每個依賴。

---

## 優劣對照表

| 優點 | 對應缺口 | 張力 |
|------|---------|------|
| 規則體系完整 | 啟動成本高 | 更多規則 = 更高品質但更慢 |
| 架構分層清晰 | executor 是 placeholder | 好架構不等於可執行 |
| 文件完備 | 雙語維護成本 | 文件好 = 維護重 |
| Progressive Disclosure | 循環引用風險 | 按需讀取 = 需要路由規則 = 額外複雜度 |
| 工作流引擎可擴展 | YAML 無法表達條件邏輯 | 可擴展 = 需要更複雜的語法 |
| task.md 簡單有效 | 無法追蹤複雜依賴 | 簡單 = 功能有限 |

---

## 最誠實的一句話

synthforge 是一個**架構精良但執行未落地**的專案。它的價值不在於能跑起來，在於它提出的問題和設計選擇。規則怎麼定？Skills 和 Agents 怎麼分？工作流引擎怎麼編排？這些問題的回答比最終的 placeholder 更有參考價值。