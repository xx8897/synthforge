---
title: "治理規則體系"
document_type: analysis
version: 1.0
language: zh-TW
rule_categories:
  - category: core
    enforcement: mandatory
    count: 7
    purpose: "所有任務必須遵守的底層規則"
    key_rules:
      - DIRECTORY_README_RULE
      - BILINGUAL_OUTPUT_RULE
      - AGENT_WORKFLOW_RULE
      - DRY_RULE
      - SINGLE_SOURCE_OF_TRUTH_RULE
      - SERIES_TASK_WORKFLOW_RULE
      - VIBE_GUIDE_SYNC_RULE
  - category: development
    enforcement: recommended
    count: 11
    purpose: "開發流程與代碼品質"
  - category: management
    enforcement: advisory
    count: 4
    purpose: "任務管理與知識管理"
design_tensions:
  - tension: "完整性 vs 啟動成本"
    description: "22條規則保證品質，但 AI 代理每次啟動需讀取大量規則"
  - tension: "雙語 vs 維護成本"
    description: "雙語提高可及性，但文檔維護量翻倍"
  - tension: "強制 vs 靈活"
    description: "強制規則確保一致性，但可能阻礙快速原型"
related_documents:
  - 01_PHILOSOPHY.md
  - 02_ARCHITECTURE.md
  - 07_STRENGTHS_AND_GAPS.md
tags: [rules, governance, mandatory, design-tensions]
---

# 治理規則體系

> 22 條規則不是亂定的。每一條背後都有問題、有取捨、有碰撞。這些文件記錄的是規則的「為什麼」，而不只是「是什麼」。

## 規則分層邏輯

規則分三層，不是按主題分，而是按**違反後果的嚴重性**分：

| 層級 | 強制性 | 違反後果 | 數量 | 定義位置 |
|------|--------|---------|------|---------|
| 🔴 core | MUST | 專案一致性崩潰 | 7 | `rules/core/` |
| 🟡 development | SHOULD | 開發品質下降 | 11 | `rules/development/` |
| 🔵 management | MAY | 協調效率降低 | 4 | `rules/management/` |

這三層對應的是：**沒有這個會死 → 沒有這個會病 → 沒有這個會慢。**

## Core 規則（7 條，強制）

### 1. DIRECTORY_README_RULE — 最長的規則，573 行

**做什麼**：每個目錄必須有 README.md，進入目錄之前先讀 README，修改文件之後更新 README。

**為什麼這麼長**：因為它不只定義「要有 README」，還定義了目錄分類體系（source/、config/、doc/、test/、tool/ 五類），每類目錄的 README 格式不同，更新觸發條件也不同。它還定義了遞迴更新規則：修改深層文件時，需要一路更新到根目錄的 ARCHITECTURE.md。

**張力**：這是執行成本最高的規則。每次修改一個文件，理論上需要更新至少兩個 README（所在目錄 + 上層目錄），如果涉及結構變更還要更新 ARCHITECTURE.md 和 VIBE_GUIDE.md。

### 2. BILINGUAL_OUTPUT_RULE — 三層語言策略

**做什麼**：定義三層語言策略（Layer 1 雙語、Layer 2 純中文、Layer 3 純英文）。

**為什麼需要**：AI 代理的 token 是成本。核心規則需要雙語因為可能有國際貢獻者；內部筆記用中文因為開發者思維語言是中文；代碼用英文因為這是行業標準。

**張力**：執行不夠徹底。很多開發規則仍然是全雙語的，沒有嚴格走 Layer 2。

### 3. AGENT_WORKFLOW_RULE — 任務→規則路由表

**做什麼**：AI 代理在執行任務之前，先查這條規則的映射表，決定需要讀取哪些其他規則。

```
任務類型           → 必須遵守的規則
────────────────────────────────────────
新建功能           → TDD_RULE, CODING_STYLE_RULE, SPEC_DRIVEN_DEVELOPMENT_RULE
修改代碼           → CODING_STYLE_RULE, FILE_CLASSIFICATION_RULE
Git 操作          → SMART_GIT_RULE, GIT_EXECUTION_RULE
結構變更           → DIRECTORY_README_RULE, VIBE_GUIDE_SYNC_RULE
```

**這是 Progressive Disclosure 的實作機制**——但有一個悖論：代理為了知道要讀哪些規則，必須先讀這條路由規則。啟動成本沒有消除，只是轉移了一層。

### 4. DRY_RULE — 平衡的 DRY，448 行

**做什麼**：定義三次抽取閾值（1次不管、2次考慮、3次必須），允許為可讀性、解耦、不同受眾的重複。

**為什麼這麼長**：包含大量範例和例外情況，特別是規則本身的 DRY（INTERNAL_RULE 從 4 條合併為 1 條的案例）。

### 5. SINGLE_SOURCE_OF_TRUTH_RULE — 65 行，最短

**做什麼**：定義哪個文件是哪種資訊的權威來源。

**為什麼最短**：因為概念簡單——VIBE_GUIDE 是導航、ARCHITECTURE 是結構、規則文件是規則、task.md 是任務。短不是因為不重要，而是因為原則清晰。

### 6. SERIES_TASK_WORKFLOW_RULE — 串聯任務的工作流

**做什麼**：完成一系列任務後的必做事項：檢查/更新 TODO、檢查/創建/更新總結。

**為什麼**：AI 代理容易「做完就忘」——完成一個任務後不更新追蹤。這條規則強制代理收尾。

### 7. VIBE_GUIDE_SYNC_RULE — 入口文件更新策略

**做什麼**：VIBE_GUIDE.md 只在頂層變更時更新（Option B），結構細節交給 ARCHITECTURE.md。

**碰撞歷史**：最初 VIBE_GUIDE 包含所有規則摘要（Option A），導致入口文件膨脹到 300+ 行。改為 Option B 後，VIBE_GUIDE 維持在 ~130 行。

---

## Development 規則（11 條，推薦）

### 開發流程類

| 規則 | 核心要求 | 設計意圖 |
|------|---------|---------|
| TDD_RULE | Red-Green-Refactor，80% 覆蓋率 | 確保代理不跳過測試 |
| SPEC_DRIVEN_DEVELOPMENT_RULE | Specify → Plan → Implement → Verify | 防止代理直接寫代碼 |
| WORKFLOW_INTEGRATION_RULE | Skill/Agent 標準接口 | 確保組件可插拔 |
| AGENT_STRUCTURE_RULE | Agent 目錄結構標準 | 確保代理有一致的結構 |

### 代碼品質類

| 規則 | 核心要求 | 設計意圖 |
|------|---------|---------|
| CODING_STYLE_RULE | 函數 <20 行、SRP、型別提示強制 | 防止代理生成大函數 |
| FILE_CLASSIFICATION_RULE | 檔案分類決策樹 | code/doc/runtime/devtime 四象限 |
| FILE_NAMING_CONVENTION_RULE | TOPIC_RULE.md、module.py 等 | 統一命名 |
| TOOLING_USAGE_RULE | core_lib ≠ devtools 依賴方向 | 防止循環依賴 |

### 內部管理類

| 規則 | 核心要求 | 設計意圖 |
|------|---------|---------|
| INTERNAL_RULE | .internal/ 5 文件限制 | 防止 AI 代理的隱藏層膨脹 |
| TASK_SUMMARY_RULE | 總結格式和更新規則 | 跨會話連續性 |
| TODO_UPDATE_RULE | TODO 追蹤格式 | 防止任務丟失 |

### Git 類

| 規則 | 核心要求 | 設計意圖 |
|------|---------|---------|
| SMART_GIT_RULE | 語義化版本 + 智慧提交訊息 | 自動化 Git 操作品質 |
| GIT_EXECUTION_RULE | 統一 CLI 操作、驗證提交成功 | 防止直接 git 操作繞過規則 |

---

## Management 規則（4 條，建議）

| 規則 | 核心要求 | 設計意圖 |
|------|---------|---------|
| TASK_MANAGEMENT_RULE | task.md 為 Mission Control，全完成時重置 | 人機協調的單一窗口 |
| KNOWLEDGE_BASE_RULE | 何時萃取知識到 .internal/knowledge/ | 避免重複學習 |
| GRAPH_RELATIONSHIP_RULE | 文件嵌入機器可讀的關聯元資料 | 支援知識圖譜自動生成 |

---

## 規則的設計模式

分析 22 條規則，可以發現幾個共同模式：

### 模式一：觸發式

```
IF 事情發生
THEN 必須做某事
```

例如：DIRECTORY_README_RULE 是「進入目錄時讀 README，修改文件後更新 README」。INTERNAL_RULE 是「累積到 5 個文件時觸發清理」。

### 模式二：路由式

```
IF 任務類型 = X
THEN 讀取規則 A, B, C
```

AGENT_WORKFLOW_RULE 就是這個模式。它是規則的規則——一個超級索引。

### 模式三：格式式

```
輸出必須符合格式 X
```

BILINGUAL_OUTPUT_RULE 定義雙語格式、TASK_SUMMARY_RULE 定義總結格式、FILE_NAMING_CONVENTION_RULE 定義命名格式。

### 模式四：關係式

```
A 是 B 的權威來源
```

SINGLE_SOURCE_OF_TRUTH_RULE 定義資訊階層、VIBE_GUIDE_SYNC_RULE 定義更新方向。

---

## 規則之間的引用網路

規則不是獨立的——它們互相引用，形成一張網：

```
AGENT_WORKFLOW_RULE（路由）
    ├── 引用 TDD_RULE
    ├── 引用 CODING_STYLE_RULE
    ├── 引用 SPEC_DRIVEN_DEVELOPMENT_RULE
    └── 引用 DIRECTORY_README_RULE

DIRECTORY_README_RULE（最被引用）
    ├── 引用 VIBE_GUIDE_SYNC_RULE
    ├── 引用 BILINGUAL_OUTPUT_RULE
    └── 引用 ARCHITECTURE.md（作為 SSOT）

SERIES_TASK_WORKFLOW_RULE
    ├── 引用 TODO_UPDATE_RULE
    └── 引用 TASK_SUMMARY_RULE

GRAPH_RELATIONSHIP_RULE
    └── 被 knowledge_graph.py 消費
```

這張引用網在 `knowledge_graph.py` 中被自動掃描和視覺化——這是規則系統對自身複雜度的回應：**當規則多到需要圖譜來理解的時候，你可能需要反思規則是不是太多了。**

---

## 三個根本張力

### 張力一：完整性 vs 啟動成本

22 條規則保證了開發全流程的品質控制。但 AI 代理每次啟動時，至少需要讀取 VIBE_GUIDE + AGENT_WORKFLOW_RULE + 路由到的具體規則。這是 3-5 個文件的「啟動稅」。

### 張力二：治理 vs 靈活

強制規則確保了一致性，但也讓快速原型變得困難。如果每次修改文件都要更新 README、每次提交都要走統一 CLI、每次任務都要檢查規則映射表，開發速度必然受影響。

### 張力三：規則的文章 vs 規則的代碼

所有 22 條規則都是 Markdown 文件，沒有一條是代碼強制執行的。規則的執行完全依賴 AI 代理的自覺讀取和遵守。這是「治理」而非「管制」的精髓，也是最大的脆弱點。