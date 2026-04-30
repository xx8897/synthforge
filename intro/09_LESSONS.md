---
title: "經驗萃取"
document_type: lessons-learned
version: 1.0
language: zh-TW
carry_forward:
  - lesson: "治理先行是對的，但不要 22 條那麼多"
    detail: "7-10 條精煉規則比 22 條完備規則更可持續"
  - lesson: "Progressive Disclosure 真的有效"
    detail: "VIBE_GUIDE 作為入口、ARCHITECTURE 作為地圖、規則按需載入，這個模式值得保留"
  - lesson: "executor placeholder 是策略性推遲，不是偷懶"
    detail: "先把骨架和接口定好，實作可以漸進到位"
  - lesson: "YAML 宣告式工作流比 Python 命令式更可讀"
    detail: "但 v2.0 需要條件邏輯，純 YAML 不夠，這是真正的設計挑戰"
  - lesson: "雙語策略分層是對的方向，執行不夠徹底"
    detail: "核心雙語、內部純中文、代碼英文——下次從一開始就嚴格分層"
  - lesson: "知識圖譜是規則系統的自我調節工具"
    detail: "當規則太多時，需要工具幫你找關聯——knowledge_graph.py 就是答案"
  - lesson: "task.md 作為 Mission Control 是人機協調的最佳實踐"
    detail: "簡單、視覺化、Git 友好，比任何任務管理工具都有效"
over_engineered:
  - area: "22 條規則體系"
    better: "精煉為 7-10 條核心規則，其餘用指引而非強制"
  - area: "全雙語文件"
    better: "嚴格分層，內部文件一律中文即可"
  - area: "rules 的 rules（管理規則的規則）"
    better: "元規則可以存在，但用簡短指引而非完整規則文件"
next_time:
  - "先做出可跑的 executor，再補規則"
  - "YAML v2.0 從一開始就考慮條件邏輯"
  - "tests 和功能同步開發，TDD 不要只流於規則"
  - "依賴管理從第一天就做好"
related_documents:
  - 01_PHILOSOPHY.md
  - 07_STRENGTHS_AND_GAPS.md
  - 08_BUILDING_JOURNEY.md
tags: [lessons, carry-forward, over-engineered, next-time]
---

# 經驗萃取

> 從試驗中學到的，比從成功中學到的多。以下是帶得走的東西。

## 帶得走的經驗

### 1. 治理先行是對的，但 22 條太多

規則體系的建立順序是對的——先定義「該遵守什麼」，再寫代碼。這避免了 AI 代理在代碼庫裡自由行動時破壞一致性。

但 22 條規則的啟動成本太高。每次 AI 代理啟動，需要讀取 VIBE_GUIDE + AGENT_WORKFLOW_RULE（路由表）+ 路由到的 1-5 條規則 + 目錄 README。這是 300-3000 行的「啟動稅」。

**下次這樣做**：精煉為 7-10 條核心規則。其餘的用指引（guideline）而非規則（rule）——指引是建議，不需要每次啟動都讀取。

具體來說，可以合併的規則：
- TODO_UPDATE_RULE、TASK_SUMMARY_RULE、SERIES_TASK_WORKFLOW_RULE → 合併為一條「任務生命週期規則」
- FILE_CLASSIFICATION_RULE、FILE_NAMING_CONVENTION_RULE → 合併為一條「文件管理規則」
- SMART_GIT_RULE、GIT_EXECUTION_RULE → 合併為一條「Git 規則」
- TASK_MANAGEMENT_RULE、KNOWLEDGE_BASE_RULE、GRAPH_RELATIONSHIP_RULE → 合併為一條「知識管理規則」

從 22 條壓縮到 ~8 條，保留的是：
1. DIRECTORY_README_RULE（一致性核心）
2. BILINGUAL_OUTPUT_RULE（語言策略）
3. AGENT_WORKFLOW_RULE（路由核心）
4. DRY_RULE（代碼品質）
5. 任務生命週期規則（合併後）
6. 文件管理規則（合併後）
7. Git 規則（合併後）
8. 知識管理規則（合併後）

### 2. Progressive Disclosure 真的有效

VIBE_GUIDE 作為唯一入口、ARCHITECTURE 作為結構地圖、規則按需載入——這個三層模型是有效的。

AI 代理不需要一次讀完所有規則，只需要根據任務類型讀取相關規則。AGENT_WORKFLOW_RULE 的路由表方案雖然有「多讀一層」的成本，但比載入全部 22 條規則好得多。

**下次保留**：Progressive Disclosure 的理念不變，但路由機制可以更輕量——用一個簡短的映射表（10 行）而不是一條完整的規則文件。

### 3. executor placeholder 是策略性推遲，不是偷懶

先定義接口（`skill_function` 和 `async action`），再定義流程（YAML 模板和引擎管線），最後才填充實作。這讓整個架構在不到一半的代碼量下就完整展現了設計意圖。

**下次保留**：placeholder 策略有效，但要設定明確的「什麼時候填充」的時間線。沒有時間線的 placeholder 會永遠是 placeholder。

### 4. YAML 宣告式工作流值得保留

YAML 模板可讀、可驗證、可擴展。非程式設計師也能看懂工作流定義。這比 Python 命令式工作流更適合宣告式的開發流程。

**但**：v2.0 需要條件邏輯（if-then-else）和重試策略，純 YAML 做不到。下次從一開始就考慮混合方案：YAML 定義流程結構，Jinja2 模板或 Python 表達式處理條件邏輯。

### 5. 雙語策略方向正確，執行不夠徹底

三層語言策略（核心雙語、內部中文、代碼英文）的理念是對的——節省 token、保持國際可及性、符合代碼行業標準。

但實作中沒有嚴格貫徹。很多開發規則仍然是全雙語的，內部文件也混雜了中英文。

**下次這樣做**：從第一天就嚴格分層。
- Layer 0（代碼）：純英文
- Layer 1（核心規則 + VIBE_GUIDE）：雙語
- Layer 2（內部文件 + .internal/）：純中文
- 其他一切：純中文

不允許中間地帶。

### 6. 知識圖譜是規則系統的自我調節工具

當規則多到需要一個專門的工具來理解它們之間的關聯時，這個工具本身就是有價值的。`knowledge_graph.py` 掃描規則的 YAML frontmatter 和交叉引用，生成 Mermaid 圖。

**下次保留**：知識圖譜不管是在規則系統還是文檔系統中都有用。它讓複雜系統可視化，發現孤立節點和死鏈。

### 7. task.md 是人機協調的最佳實踐

`task.md` 使用簡單的 Markdown checklist 格式：`[ ]` 待辦、`[/]` 進行中、`[x]` 完成。這個格式：
- Git 友好（純文本，版本可控）
- 人類可讀（視覺化的進度追蹤）
- AI 可解析（結構化的狀態標記）
- 無需額外工具（不需要 Jira、Trello 或 Notion）

**下次保留**：task.md 的格式可以成為任何 AI 驅動專案的標準實踐。唯一改進：加入優先級標記（`[!]` 緊急、`[?]` 待確認）。

---

## 過度設計的地方

### 1. 22 條規則體系

如前面所說，7-10 條精煉規則比 22 條完備規則更可持續。完備不等於有效——太多規則會導致：
- 啟動成本過高
- 規則之間的引用網路複雜
- 維護成本倍增（雙語版本 × 22）

### 2. 全雙語文件

核心規則全雙語是必要的（國際可及性）。但開發規則和管理規則也全雙語，這超過了實際需求。如果團隊只有中文開發者，開發規則只需要中文。

### 3. rules 的 rules

INTERNAL_RULE 管理規則是一個元規則——管理規則的規則。TASK_SUMMARY_RULE 定義總結的格式。TODO_UPDATE_RULE 定義 TODO 的格式。這些「規則的規則」增加了系統的複雜度，但對實際開發的直接影響有限。

**更好的做法**：元規則用簡短的指引（guideline）代替完整的規則文件。指引可以是 10 行的文檔，不需要 100+ 行的規則文件。

---

## 下次會怎麼做

### 1. 先做出可跑的 executor，再補規則

synthforge 的推進順序是：規則 → 工具 → 骨架 → placeholder。下次的順序應該是：

```
最小可跑系統 → 驗證規則 → 補充規則 → 擴展工具
```

先有一個能跑的 executor（哪怕很簡陋），再圍繞實際問題添加規則。規則應該解決已知的問題，而不是預防想像的問題。

### 2. YAML v2.0 從一開始就考慮條件邏輯

v1.0 用純 YAML 定義工作流，這在線性流程中工作良好。但開發流程天生包含條件分支（測試失敗怎麼辦？重試幾次？循環檢測？）。

下次一開始就設計混合方案：
- YAML 定義流程結構
- Jinja2 模板處理條件邏輯
- Python 表達式處理動態計算

### 3. 測試和功能同步開發，TDD 不要只流於規則

TDD_RULE 在規則文件裡寫得很好——Red-Green-Refactor，80% 覆蓋率。但 synthforge 本身的測試基礎設施不完整：
- 沒有 `requirements.txt`
- 測試檢查檔案存在而非功能正確
- 沒有 CI/CD

下次：每寫一個功能，同時寫測試。TDD 應該是自己遵守的，不只是寫給 AI 代理看的規則。

### 4. 依賴管理從第一天就做好

`click`、`pyyaml`、`pytest`、`pytest-asyncio` 是必需的外部依賴，但專案從一開始就沒有 `requirements.txt` 或 `pyproject.toml`。

下次：在 Phase 1 就建立依賴管理。這不是 Phase 4 才做的事。

---

## 最後的總結

synthforge 是一個試驗性專案。它的價值不在於能跑起來——executor 是 placeholder，代理的核心方法是 `pass`。

它的價值在於提出的問題和做的選擇：

> AI 代理在專案裡該守什麼規矩？
> Skills 和 Agents 怎麼分？
> 工作流用 YAML 還是 Python？
> 規則怎麼做到完備但不壓迫？
> 雙語怎麼做到國際化但不翻倍維護？

這些問題的回答——22 條規則、三層分類、Progressive Disclosure、宣告式工作流、YAML + dataclass 管線——是有參考價值的。

但最有參考價值的，可能是做得過頭的地方：規則太多、雙語不徹底、placeholder 沒有時間線。知道在哪裡停下來，比知道怎麼繼續走更難。

**帶走什麼**：治理框架的理念、Progressive Disclosure 的模式、Skills/Agents 的區分、YAML 宣告式工作流的可讀性、task.md 的人機協調格式、知識圖譜的自我調節功能。

**留下什麼**：22 條規則的完備性、全雙語的維護成本、placeholder 的無限期推遲、過度設計的元規則。

這是試驗的意義——你從中得到的不只是可以用的東西，還有不該再做的東西。