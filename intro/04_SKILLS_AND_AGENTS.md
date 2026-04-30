---
title: "技能與代理"
document_type: analysis
version: 1.0
language: zh-TW
concept_distinction:
  skills:
    nature: 無狀態
    interface: "skill_function(input_data, config=None) -> Dict"
    return_format: "{'success': bool, 'output': Any, 'errors': []}"
    reusability: 高（純函數）
    examples: [spec_parser, task_generator, test_runner, structure_management, document_skill]
  agents:
    nature: 有狀態
    interface: "async action(input, config) -> Dict"
    return_format: "{'success': bool, ...}"
    reusability: 中（需上下文）
    examples: [planner_agent, executor_agent, reviewer_agent, self_improvement_agent]
implementation_status:
  skills:
    spec_parser: "✅ 完成（Regex 解析 Markdown）"
    task_generator: "✅ 完成（生成 task.md）"
    test_runner: "✅ 完成（subprocess 呼叫 pytest）"
    structure_management: "✅ 完成"
    document_skill: "⚠️ 部分（CLI 整合完成，獨立執行未驗證）"
  agents:
    planner_agent: "⚠️ 骨架完成，實作為模擬結果"
    executor_agent: "⚠️ 骨架完成，核心方法為 pass/placeholder"
    reviewer_agent: "⚠️ 骨架完成，檢查方法多為 pass"
    self_improvement_agent: "⚠️ 骨架完成，學習資料庫存在但未真實運作"
related_documents:
  - 02_ARCHITECTURE.md
  - 05_WORKFLOW_ENGINE.md
  - 07_STRENGTHS_AND_GAPS.md
tags: [skills, agents, stateless, stateful, implementation-status]
---

# 技能與代理

> Skills 概念剛出來的時候，所有人都在想「AI 能做什麼」。synthforge 的回答是：先分清楚「能力」（Skill）和「角色」（Agent），再決定誰來編排它們。

## 核心區分：Skills vs Agents

這是 synthforge 架構中最重要的概念區分：

| | Skills | Agents |
|---|---|---|
| **本質** | 無狀態的純函數 | 有狀態的自主實體 |
| **接口** | `skill_function(input_data, config=None) -> Dict` | `async action(input, config) -> Dict` |
| **返回** | `{'success': bool, 'output': Any, 'errors': []}` | `{'success': bool, ...}` |
| **可重用性** | 高——任何工作流都可以調用 | 中——需要上下文和狀態管理 |
| **副作用** | 無——同樣輸入永遠同樣輸出 | 有——結果取決於內部狀態和歷史 |
| **類比** | 工具箱裡的扳手 | 使用扳手的工人 |
| **由誰調用** | Workflow Engine 或 Agent | Workflow Engine |

**設計意圖**：Skills 是可組合的原子能力，Agents 是有上下文的编排者。一個 Agent 可以使用多個 Skill，但一個 Skill 不應該知道 Agent 的存在。

## Skills — 五個無狀態能力

### 1. spec_parser（規格解析器）

**位置**：`skills/workflow_skills/spec_parser/`

**做什麼**：將 `implementation_plan.md`（人類寫的實作計畫）解析為結構化 JSON。

**怎麼做**：用 Regex 解析 Markdown，提取：
- `goal`（目標）
- `background`（背景）
- `components`（組件列表）
- `file_changes`（檔案變更計畫）
- `verification_plan`（驗證方案）

**實作狀態**：✅ 完成，核心邏輯在 `spec_parser.py`。

**設計觀察**：spec_parser 是 Skills 設計理念的典型體現——輸入是結構化的（Markdown 文件），輸出是結構化的（JSON），過程是確定性的（Regex），副作用為零。

### 2. task_generator（任務生成器）

**位置**：`skills/workflow_skills/task_generator/`

**做什麼**：從 spec_parser 輸出的 JSON，生成 `task.md` 格式的 checklist。

**怎麼做**：讀取 JSON 中的 components 和 file_changes，按組件分組，生成 `[ ]` checklist，並添加驗證區段。

**實作狀態**：✅ 完成。

**鏈路**：這是 spec_parser 的下游。spec_parser 解析規格 → task_generator 生成任務 → 人類或代理確認後開始工作。

### 3. test_runner（測試執行器）

**位置**：`skills/workflow_skills/test_runner/`

**做什麼**：執行 pytest 並解析覆蓋率報告。

**怎麼做**：透過 subprocess 呼叫 pytest，解析 JSON 格式的覆蓋率輸出，返回結構化的測試結果。

**實作狀態**：✅ 完成，但依賴 pytest 環境配置。

**設計觀察**：test_runner 是「技能邊界」的有趣案例——它透過 subprocess 與外部系統互動，這引入了環境依賴。純函數在理想情況下不應該依賴外部狀態，但 test_runner 的本質就是與外部互動。

### 4. structure_management（結構管理）

**位置**：`skills/automation/structure_management/`

**做什麼**：目錄結構重構操作（建立、搬移、刪除、重命名）。

**實作狀態**：✅ 完成。與 devtools/structure_optimizer.py 協同工作。

### 5. document_skill（文件處理）

**位置**：`skills/integration/document_skill/`

**做什麼**：PDF 和 URL 文件的載入與分割。

**實作狀態**：⚠️ 部分完成。CLI 整合（`devtools/cli.py doc load`）已完成，但獨立執行未充分驗證。

---

## Agents — 四個有狀態代理

### 1. planner_agent（規劃代理）

**位置**：`agents/planner_agent/`

**標準結構**：
```
planner_agent/
├── AGENT.md      # 代理文檔
├── config.yml    # 配置（模型、溫度、最大 token）
└── planner_agent.py  # 實作
```

**做什麼**：
- 分析任務需求
- 估算工作量
- 識別依賴關係
- 生成執行計畫

**實作狀態**：⚠️ 骨架完成。`plan_task()` 方法解析 task.md 並返回模擬的規劃結果。沒有真正的 AI 推理——它只是讀取任務列表，返回一個固定格式的回應。

**關鍵代碼觀察**：
```python
async def plan_task(self, task: str, context: Dict[str, Any]) -> Dict[str, Any]:
    # 讀取 task.md 解析任務
    task_content = self._read_task_md()
    # ... 生成模擬規劃結果
    return {'success': True, 'plan': {...}, 'estimates': {...}}
```
返回格式正確，但內容是模擬的。

### 2. executor_agent（執行代理）

**位置**：`agents/executor_agent/`

**做什麼**：
- 使用 TDD 流程實作代碼
- 管理 Git worktree
- 執行測試

**實作狀態**：⚠️ 骨架完成，核心方法為空。

**關鍵代碼觀察**：
```python
async def _implement_task_tdd(self, task: str, ...):
    pass  # ← TDD 實作是空的

async def _implement_task_standard(self, task: str, ...):
    pass  # ← 標準實作也是空的
```

這是架構完成但實作未落地最明顯的地方。`_implement_task_tdd` 和 `_implement_task_standard` 是整個系統的核心方法，但裡面是 `pass`。

### 3. reviewer_agent（審查代理）

**位置**：`agents/reviewer_agent/`

**做什麼**：
- 代碼審查
- 安全檢查
- 品質保證

**實作狀態**：⚠️ 骨架完成。`check_code_style()`、`check_security()`、`check_best_practices()` 等方法都是 `pass`。

### 4. self_improvement_agent（自我改進代理）

**位置**：`agents/self_improvement_agent/`

**做什麼**：
- 從錯誤中學習（儲存到 `.internal/learning/improvements.json`）
- 優化工作流
- 監控效能

**實作狀態**：⚠️ 骨架完成。學習資料庫的 JSON 檔案存在，可以寫入和讀取，但沒有真正的「從錯誤學習」邏輯。

**設計觀察**：self_improvement_agent 是 synthforge 最有前瞻性的設計——一個會學習的代理。它的存在反映了「AI 開發流程本身應該可改進」的信念。

---

## 標準接口設計

### Skill 接口

```python
def skill_function(input_data: Any, config: Optional[Dict] = None) -> Dict[str, Any]:
    """
    標準 Skill 接口
    
    Args:
        input_data: 技能輸入（通常是結構化資料）
        config: 可選配置
    
    Returns:
        {'success': bool, 'output': Any, 'errors': List[str]}
    """
```

### Agent 接口

```python
async def action(input: Dict[str, Any], config: Dict[str, Any]) -> Dict[str, Any]:
    """
    標準 Agent 接口
    
    Args:
        input: 代理輸入（包含任務和上下文）
        config: 代理配置（從 config.yml 載入）
    
    Returns:
        {'success': bool, ...}  # 代理自定義返回欄位
    """
```

兩個接口的關鍵差異：
- **Skill 是同步的**，Agent 是異步的（`async`）
- **Skill 的返回格式嚴格**（必須有 `success`/`output`/`errors`），**Agent 的返回格式寬鬆**（只要有 `success`）
- **Skill 不保持狀態**，Agent 有 `self.context`

---

## Agent 的標準目錄結構

每個代理遵循相同的目錄結構（定義在 `AGENT_STRUCTURE_RULE.md`）：

```
agent_name/
├── AGENT.md          # 代理的文檔（能力、限制、示例）
├── config.yml        # 配置（模型參數等）
└── agent_name.py     # 實作
```

`AGENT.md` 不是裝飾——它是 Progressive Disclosure 在代理層的體現。Workflow Engine 在載入代理時先讀 AGENT.md 了解能力，然後按需載入完整實作。

---

## Skill 與 Agent 的協作模式

在 Workflow Engine 中，技能和代理是這樣協作的：

```
Workflow YAML Template:
  phases:
    - name: specify
      steps:
        - skill: spec_parser        # ← 無狀態能力
          input: implementation_plan.md
    
    - name: plan
      steps:
        - agent: planner_agent       # ← 有狀態代理
          input: parsed_spec
    
    - name: execute
      steps:
        - agent: executor_agent      # ← 有狀態代理
          input: task_plan
    
    - name: test
      steps:
        - skill: test_runner          # ← 無狀態能力
          input: test_config
    
    - name: review
      steps:
        - agent: reviewer_agent      # ← 有狀態代理
          input: code_changes
```

**模式**：Skills 在可預測的步驟中使用（解析、測試），Agents 在需要判斷力的步驟中使用（規劃、執行、審查）。

---

## 實作狀態誠實評估

| 組件 | 接口 | 文檔 | 核心邏輯 | 狀態 |
|------|------|------|---------|------|
| spec_parser | ✅ | ✅ | ✅ | 完成 |
| task_generator | ✅ | ✅ | ✅ | 完成 |
| test_runner | ✅ | ✅ | ✅ | 完成（依賴 pytest 環境） |
| structure_management | ✅ | ✅ | ✅ | 完成 |
| document_skill | ✅ | ⚠️ | ⚠️ | 部分 |
| planner_agent | ✅ | ✅ | ❌（模擬） | 骨架 |
| executor_agent | ✅ | ✅ | ❌（pass） | 骨架 |
| reviewer_agent | ✅ | ✅ | ❌（pass） | 骨架 |
| self_improvement_agent | ✅ | ✅ | ⚠️（寫讀 JSON） | 骨架 |

**真相**：接口和文檔完整，核心邏輯大部分是 placeholder。這是「設計走在了實作前面」的直接體現——不是偷懶，而是有意識地先定義邊界，再填充內容。

Skills 的完成度比 Agents 高很多，因為 Skills 是無狀態的純函數，實作門檻低。Agents 需要真正的 AI 推理能力，這超出了純框架設計的範圍。