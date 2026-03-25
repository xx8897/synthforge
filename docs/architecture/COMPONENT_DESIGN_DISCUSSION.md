# Component Design Discussion
# 元件設計思考

**Date**: 2026-03-23
**Context**: 關於 Skills、Agents、Rules 的設計哲學，以及與 Claude Cowork Plugin 架構的對照

---

## 1. Skills 的拆分判斷

### 核心原則

> **拆分的邊界 = 可以獨立被調用的最小有意義單位**

「越小越好」這個思維不適用於 AI skill 系統。軟體元件的拆分成本很低（import 幾乎無代價），但 AI skill 的拆分成本是 context——每個 skill 都是一次 context 消耗。

### 三種情況

| 情況 | 設計 |
|------|------|
| 總是一起發生，理由相同 | 不拆，是一個動作 |
| 可以單獨發生，理由不同 | 拆成獨立 skills |
| 總是一起發生，但改動原因獨立 | 各自獨立，包一層 workflow |

### 拆分的三個問題

1. **能不能舉出「要左邊但不要右邊」的具體場景？**
2. **兩邊改動的原因是否獨立？**（是 → 拆）
3. **拆分後 context 成本是否合理？**（總是一起呼叫 → 不拆）

### 一句話總結

> 在「輸入格式不同」或「使用者不同」這兩個地方切，其他地方不切。

---

## 2. 兩個事件獨立才適合拆

更簡潔的判斷方式：

```
獨立 = 可以單獨發生，且發生的理由不同
```

- **總是順序執行** → 同一個 workflow，內部分函式
- **可以單獨被呼叫** → 拆成獨立 skill
- **總是一起用，但各自可能變動** → 獨立 skill + 提供 workflow 組合

---

## 3. Skills vs Agents：包含關係

### 三者本質

```
Rules  = 約束「怎麼做」，被動，永遠生效
Skills = 定義「能做什麼」，主動，按需呼叫
Agents = 決定「做什麼、何時做」，自主，協調者
```

### 包含關係的判斷

**Agent 包含 Skills**（私有）：只有當這個 skill 真的只屬於一個 agent 才適合。否則 skill 無法被其他 agent 重用。

**Skills 包含 Agents**：概念上不成立。Skills 是工具，不知道誰在用它。

**各自獨立，Agent 引用 Skills**：最靈活，skills 是共享 library，agents 是消費者。

### 最精巧的設計

```
skills/              ← 共享 library，任何 agent 都能引用
  spec_parser/
  task_generator/

agents/
  planner_agent/     ← 引用 skills，不擁有
    private_skill/   ← 只有這裡用的 skill，才內嵌
  executor_agent/
```

**判斷標準**：

| 情況 | 設計 |
|------|------|
| Skill 被多個 agent 使用 | 獨立放 skills/，agent 引用 |
| Skill 只有一個 agent 用 | 放進 agent 目錄，當私有能力 |
| Skill 是外部整合 | 獨立放 skills/integration/ |

---

## 4. Rules 的定位

### Rules 不是 Skills

最直接的測試：**「這個東西能被呼叫嗎？」**

```
parse_spec()          ← 能呼叫，有輸入輸出 → Skill
「命名必須用底線」     ← 不能呼叫，沒有輸入輸出 → Rule
```

Rules 不產生任何東西，不接受輸入，只是讓 agent 在做決定時受到約束。

### 誰在執行？

```
Skill → 被顯式呼叫才生效，執行完就結束
Rule  → 永遠在背景生效，不需要呼叫
```

### 類比

```
Rules  = 法律（所有人都得遵守，不屬於任何人）
Skills = 工具箱（任何人都能用）
Agents = 工人（決定用哪個工具，必須守法）
```

### 邊界案例

`BILINGUAL_OUTPUT_RULE`（輸出必須雙語）是 Rule，因為你不會去「呼叫雙語輸出」，它是對所有輸出的約束。

但如果有 `translate_to_bilingual(text)` 的轉換函式，那就是 Skill——因為它有輸入輸出，可以單獨呼叫。

**同樣的概念，表現形式不同，分類就不同。**

### Rules 的作用範圍

```
rules/
  core/     ← 全域，所有 agent 和 skill 都受約束
  agents/   ← 只約束特定 agent
  skills/   ← 只約束特定 skill 的行為
```

---

## 5. Claude Cowork 是什麼

**Cowork** 是 Claude Desktop 的本機工作環境，定位是「Claude Code 的能力，不需要終端機」。

### 核心特性

- **非同步執行**：交派任務後可以離開，回來看結果
- **多 agent 並行**：可以將複雜任務拆分給多個獨立 sub-agent 平行處理，每個都有獨立 context
- **本機運行**：直接讀寫你的資料夾，不上傳到雲端
- **工具整合**：透過 MCP connectors 串接 Slack、Google Drive、Calendar 等外部服務

> "Cowork can break complex tasks across independent sub-agents that work in parallel, each with fresh context."

### Plugin 在 Cowork 的定義

> 一組教 Claude 如何執行特定任務的檔案，編碼你的方法論、工作流程、工具連結。

Cowork Plugin 的三個元件：

| 元件 | 作用 |
|------|------|
| **Skills** | 編碼知識與工作流程（含方法論文件） |
| **Sub-agents** | 處理複雜任務的專門幫手，可並行或循序 |
| **Connectors** | 串接外部工具，mid-workflow 拉取資料並寫回系統 |

---

## 6. synthforge vs Cowork Plugin：架構對照

### Claude Code 官方 Plugin 結構

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json    ← manifest
├── skills/
├── agents/
├── hooks/
└── mcp/
```

### 三方對照

| | synthforge | Claude Code Plugin | Cowork Plugin |
|--|-----------|-------------------|---------------|
| Skills | ✓ skills/ | ✓ skills/ | ✓ Skills |
| Agents | ✓ agents/ | ✓ agents/ | ✓ Sub-agents |
| Rules | ✓ rules/ | hooks 替代 | Instructions panel |
| 外部整合 | ✗ 缺少 | ✓ mcp/ | ✓ Connectors |
| Manifest | ✗ | ✓ plugin.json | 隱性 |
| 分發 | ✗ | ✓ marketplace | 壓縮檔 / GitHub |

### 結論

synthforge 的三域並立設計（rules / skills / agents）與官方架構**高度收斂**，是自行推導出來的相近結果。

主要差距只有兩點：
1. **缺 Connectors / MCP 層**：外部工具整合尚未建立
2. **缺 Manifest**：沒有統一的入口描述，目前靠 README 層層導覽

如果未來要接入官方生態，補一個 `plugin.json` + `mcp/` 即可。

---

## 7. 官方 Skills 結構的精妙

官方設計的核心：**Progressive Context Loading（漸進式 context 載入）**

```
my-skill/
├── SKILL.md      ← 永遠載入，輕量概覽
├── reference.md  ← 按需載入，詳細 API
├── examples.md   ← 按需載入，使用範例
└── scripts/
    └── helper.py ← 執行，不載入進 context
```

AI 只在需要時才載入對應層級，`scripts/` 的內容完全不佔 context。

這與 synthforge 是**不同典範**：

| | 官方 Claude Code skills | synthforge skills |
|--|------------------------|------------------|
| 執行者 | AI 讀 prompt 後執行 | Python runtime |
| 消費者 | AI agent（讀 context） | Python 程式（import） |
| 精妙之處 | context 效率 | 型別安全、可測試 |

兩者不是好壞之別，是設計目標不同。

---

## 8. Cowork 的 Plugin 結構彈性

Cowork 對 plugin 的檔案結構**沒有嚴格規定**。Plugin 是透過對話建立的：

> 你描述想要什麼，Claude 問你工作流程、工具、標準，然後自動幫你生成 plugin 內容。

重點不是「資料夾有沒有叫 skills/」，而是「這組檔案能不能教會 Claude 如何執行任務」。

---

## 9. Claude 如何讀取 Plugin 檔案

### MD 是導覽地圖，不是目錄掃描

Claude 只知道被載入進 context 的內容。**沒寫在 MD 裡的東西，Claude 不會主動去找。**

```
SKILL.md 沒提到 examples/
→ Claude 不知道 examples/ 存在
→ examples/ 實際上被忽略
```

因此，如果有 `examples/` 資料夾，SKILL.md 裡必須明確指向它：

```markdown
## Examples
See [examples/](examples/) for usage patterns.
```

### 放錯位置不會報錯，但會造成語意混亂

Skills 資料夾裡放 AGENT.md，Claude 不會報錯——它照內容執行。但 skill 預期的是「給輸入、拿輸出」，agent 預期的是「自主決策」，兩者混用會讓執行行為不可預測。

---

## 10. Agent + Skill 同時存在時的運行模式

### 層次關係

Skills 和 Agents 是不同層次，不是同一東西的兩種形式：

```
主 Agent（決策者）
  ↓ 呼叫
Skills（工具）
  ↓ 遇到複雜任務
Sub-agents（平行工人，各自獨立 context）
  ↓ 也能呼叫
Skills（同一套工具）
```

### 具體執行流程

```
任務進來
→ 主 Agent 讀 AGENT.md，確認角色
→ 主 Agent 讀 SKILL.md，知道有哪些工具
→ 簡單任務：直接呼叫 skill 執行
→ 複雜任務：spawn sub-agents，各自拿獨立 context 平行處理
→ 主 Agent 收集結果，整合輸出
```

### Skills vs Sub-agents 的本質差異

| | Skill | Sub-agent |
|--|-------|-----------|
| 本質 | 工具，被呼叫 | Agent，自主執行 |
| Context | 不獨立 | 各自獨立 |
| 平行執行 | 不適用 | 可平行 |
| 決策能力 | 無 | 有 |

Skill 像函式呼叫——給輸入，拿輸出，沒有自己的意志。Sub-agent 才是真正獨立運行的個體。

> **注意**：以上執行機制是從 Cowork 文件推論的架構，官方文件沒有明確說明底層 dispatch 細節。

---

**Related**: [DESIGN_DECISIONS.md](DESIGN_DECISIONS.md) · [SKILLS_VS_RULES.md](SKILLS_VS_RULES.md)
