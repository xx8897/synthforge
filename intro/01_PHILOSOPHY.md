---
title: "設計哲學與思想碰撞"
document_type: philosophy
version: 1.0
language: zh-TW
core_philosophies:
  - name: Progressive Disclosure
    summary: "AI 代理只讀需要的，逐層展開"
  - name: Governance over Control
    summary: "規則是治理框架，不是硬編碼約束"
  - name: Bilingual Layered Strategy
    summary: "核心雙語、內部純中文、代碼純英文，三層節省 token"
  - name: Balanced DRY
    summary: "三次才抽取，允許為可讀性重複"
design_decisions:
  - decision: "VIBE_GUIDE 採 Option B（引用而非內嵌）"
    rationale: "保持入口簡潔，避免 VIBE_GUIDE 膨脹"
  - decision: "雙語策略分層而非全雙語"
    rationale: "內部文件純中文省 50% token"
  - decision: "Skills 無狀態 / Agents 有狀態"
    rationale: "可重用性與上下文管理的取捨"
related_documents:
  - 00_OVERVIEW.md
  - 03_RULES_SYSTEM.md
  - 08_BUILDING_JOURNEY.md
tags: [philosophy, design-decisions, bilingual, progressive-disclosure]
---

# 設計哲學與思想碰撞

> 思想不是一次成型的。每一條規則、每一個接口、每一層分離，都經過了「為什麼」和「憑什麼」的來回。

## 一、Progressive Disclosure — 逐層展開，不要一次灌滿

### 問題

AI 代理的 context window 是有限的。一個 22 條規則的專案，如果把所有規則都塞進系統提示詞，代理在開始工作之前就已經花掉大量 token。

### 回答

**VIBE_GUIDE.md 作為唯一入口。** 代理進入專案時，只讀這一個文件。VIBE_GUIDE 提供決策樹——根據任務類型（新功能、修 bug、Git 操作……）指向不同的規則和文件。代理按需讀取，不預載。

```
VIBE_GUIDE.md（入口，~130 行）
  ├─ 問：新功能 → 讀 GIT_WORKFLOW.md + TDD_RULE.md
  ├─ 問：修 bug → 讀 bug_fix.yml 模板
  ├─ 問：Git 操作 → 讀 SMART_GIT_RULE.md
  └─ 問：查狀態 → 讀 ROADMAP_v2.md
```

### 碰撞點

最初 VIBE_GUIDE 包含了所有規則的摘要——這讓入口文件暴增到 300+ 行。後來改為 **Option B**：VIBE_GUIDE 只保留高層索引和決策樹，細節交給 ARCHITECTURE.md 和各規則文件。這個改動記錄在 `VIBE_GUIDE_SYNC_RULE.md` 裡，是設計演化的明確痕跡。

### 真相

Progressive Disclosure 的概念是對的，但執行有摩擦。AGENT_WORKFLOW_RULE 要求代理在執行任何任務之前先查規則映射表，這意味著「只讀需要的」反而變成「必須先讀映射規則才能知道要讀什麼」。啟動成本沒有消失，只是轉移了。

---

## 二、Governance over Control — 治理而非管制

### 問題

AI 代理在代碼庫裡自由行動，很容易破壞一致性。你是用硬約束（代碼層面強制）還是軟治理（規則文件引導）？

### 回答

**用規則文件治理，而不是用代碼鎖死。** 22 條規則分成三層：

| 層級 | 強制性 | 數量 | 範例 |
|------|--------|------|------|
| core | 🔴 強制（MUST） | 7 | DIRECTORY_README_RULE, BILINGUAL_OUTPUT_RULE |
| development | 🟡 推薦（SHOULD） | 11 | TDD_RULE, CODING_STYLE_RULE |
| management | 🔵 建議（MAY） | 4 | TASK_MANAGEMENT_RULE, KNOWLEDGE_BASE_RULE |

這不是由代碼強制執行的（沒有 pre-commit hook 來檢查你是不是真的讀了 README），而是靠 `.cursorrules`、`.github/copilot-instructions.md`、`VIBE_GUIDE.md` 三路同步來推動 AI 代理遵守。

### 碰撞點

治理的問題在於：**規則越多，遵守成本越高。** 22 條規則中，DIRECTORY_README_RULE 一條就有 573 行——它要求你在進入任何目錄之前先讀 README，修改任何文件之後更新 README。這保證了一致性，但也讓每次操作多了兩步強制讀寫。

治理和效率的平衡，是 synthforge 裡最根本的張力。

---

## 三、Bilingual Layered Strategy — 三層語言策略

### 問題

專案需要對國際開放（英文），但主要開發者的思維語言是中文。怎麼在 token 效率和可及性之間取捨？

### 回答

三層語言策略（記錄在 `BILINGUAL_OUTPUT_RULE.md`）：

| 層級 | 語言 | 場景 | Token 成本 |
|------|------|------|-----------|
| Layer 1 | 英文 + 繁體中文 | 核心規則、AI 配置、VIBE_GUIDE | 最高 |
| Layer 2 | 純繁體中文 | `.internal/` 內部文件、TODO、總結 | 約省 50% |
| Layer 3 | 純英文 | 代碼、變數名、註解 | 最低 |

### 碰撞點

理想很豐滿，執行有落差。很多開發規則（development 層）實際上是全雙語的，沒有嚴格走 Layer 2。這反映了雙語策略的深層矛盾：

> **你無法在寫規則的時候預判哪些人會讀它。** 如果規則只寫中文，國際貢獻者無法理解；如果全雙語，維護成本翻倍。

synthforge 的選擇是：核心規則雙語（妥協），內部文件純中文（效率），代碼純英文（行業標準）。這個選擇是合理的，但在實作中沒有 100% 貫徹。

---

## 四、Balanced DRY — 不過度抽取，允許合理重複

### 問題

傳統 DRY 原則說「不要重複自己」。但在規則系統和文件架構中，過度抽取會犧牲可讀性和解耦性。

### 回答

`DRY_RULE.md`（448 行，最長的開發規則之一）定義了三個閾值：

| 重複次數 | 行動 |
|---------|------|
| 1 次 | 放著，完全沒問題 |
| 2 次 | 考慮抽取，但不強制 |
| 3+ 次 | 必須抽取 |

同時允許例外：為了可讀性、為了解耦、為了不同受眾的重複是可以接受的。

### 碰撞點

INTERNAL_RULE 是 Balanced DRY 的實際案例。最初有四條獨立規則（CONFIRMATION_DOCUMENTS_RULE、INTERNAL_MANAGEMENT_RULE 等），後來合併為一條 INTERNAL_RULE。這代表規則本身也需要 DRY——治理規則的治理規則。

但反過來看：DIRECTORY_README_RULE 有 573 行，裡面包含大量重複的模式（每個目錄類型都有類似的指示）。這些重複是為了讓每條指示在不同上下文中自洽——這正是 Balanced DRY 所允許的「為了可讀性的重複」。

---

## 五、Spec-Driven Development — 規格驅動開發

### 問題

AI 代理容易「直接開始寫代碼」，跳過設計。怎麼強制規劃步驟？

### 回答

`SPEC_DRIVEN_DEVELOPMENT_RULE.md` 定義了四步流程：

```
Specify → Plan → Implement → Verify
```

每一個步驟都有明確的產出物：
- **Specify**: 實作計畫文件（implementation_plan.md）
- **Plan**: task.md 的 checklist
- **Implement**: 代碼 + 測試
- **Verify**: 測試通過 + 文件更新

這個流程和 Workflow Engine 的模板對齊：feature_development.yml 就是 `specify → plan → execute → test → review` 五個 phase。

### 碰撞點

SDD 是好的原則，但 synthforge 的實作有斷層：spec_parser skill 可以解析實作計畫，task_generator 可以生成任務清單，但 executor agent 的 `_implement_task_tdd` 方法是空的。**規格驅動到了實作這一步，沒有人真的在執行。** 這不是原則的問題，是資源和優先順序的問題。

---

## 六、Single Source of Truth — 但誰是權威來源？

### 問題

多個文件之間的資訊重複時，哪一個是權威版本？

### 回答

`SINGLE_SOURCE_OF_TRUTH_RULE.md`（只有 65 行，是規則裡最短的之一）定義了明確的階層：

| 資訊類型 | 權威來源 |
|---------|---------|
| 導航 | VIBE_GUIDE.md |
| 架構 | ARCHITECTURE.md |
| 規則 | rules/ 各規則文件 |
| 任務 | task.md |

### 碰撞點

理論上清晰，實際上有模糊地帶。例如 `DIRECTORY_README_RULE` 和 `VIBE_GUIDE_SYNC_RULE` 都在談「更新文件」，但前者要求「修改任何文件後更新所在目錄的 README」，後者要求「結構變更時更新 VIBE_GUIDE」。這兩條規則在不同層級談同一件事，有時候會讓代理不知道該先更新誰。

SSOT 原則解決了「更新的內容對不對」的問題，但沒有完全解決「更新的順序對不對」的問題。

---

## 設計哲學的總結

synthforge 的設計哲學不是一個統一的理論，而是一組在實作中不斷碰撞的價值觀：

| 價值觀 | 對立面 | 張力所在 |
|--------|--------|---------|
| Progressive Disclosure | 完整性 | 按需讀取 vs 一次告知 |
| Governance over Control | 效率 | 規則引導 vs 快速行動 |
| Bilingual Strategy | 維護成本 | 國際化 vs 雙倍維護 |
| Balanced DRY | 一致性 | 有理由的重複 vs 抽象化 |
| Spec-Driven Development | 執行力 | 規劃完美 vs 交付優先 |

這些張力不是缺點——它們是設計思考的痕跡。每一個選擇都有理由，每一個妥協都有原因。後面的文件會具體拆解這些選擇在架構、規則、引擎中的體現。