---
title: "工作流引擎"
document_type: technical-deep-dive
version: 1.0
language: zh-TW
engine_components:
  - module: parser.py
    purpose: "將 YAML 解析為 WorkflowDefinition dataclass"
    status: ✅ 完成
  - module: validators.py
    purpose: "驗證工作流定義（結構、組件存在、資料流、配置）"
    status: ✅ 完成
  - module: executor.py
    purpose: "逐階段逐步驟執行工作流"
    status: ⚠️ placeholder（找到 skill/agent 路徑但未動態匯入執行）
  - module: context.py
    purpose: "管理執行狀態、變數、步驟結果，可序列化"
    status: ✅ 完成
execution_flow: "YAML → parser.parse_workflow() → WorkflowDefinition → validator.validate() → executor.execute() → ExecutionContext"
builtin_templates:
  - feature_development.yml
  - bug_fix.yml
  - refactoring.yml
  - rule_creation.yml
v2_plans:
  - conditional_edges: "YAML 支援 if-then-else"
  - retry_strategy: "失敗重試機制"
  - cycle_detection: "基礎循環檢測"
related_documents:
  - 02_ARCHITECTURE.md
  - 04_SKILLS_AND_AGENTS.md
  - 08_BUILDING_JOURNEY.md
tags: [workflow, engine, yaml, parser, executor, v2-roadmap]
---

# 工作流引擎

> 工作流引擎是 synthforge 的心臟。YAML 定義「做什麼」，引擎決定「怎麼做」。問題是——心臟還在用模擬器跳動。

## 設計理念

工作流引擎的核心設計選擇是：**YAML 宣告式定義 + Python 引擎執行**。

為什麼不直接用 Python 寫工作流？因為 YAML 有幾個好處：

1. **可讀性**：非程式設計師也能看懂工作流的定義
2. **可擴展性**：新增工作流只需要寫 YAML，不需要改代碼
3. **可驗證性**：YAML 可以在執行前驗證結構正確性
4. **分離關注**：流程定義和執行邏輯分離，修改流程不影響引擎

但 YAML 也有代价——它無法表達複雜的條件邏輯，這是 v2.0 要解決的問題。

## 引擎架構

引擎由四個核心模組組成，形成一條清晰的管線：

```
                    輸入：YAML 工作流定義
                             │
                             ▼
                    ┌─────────────────┐
                    │   parser.py     │
                    │  YAML → Dataclass│
                    └────────┬────────┘
                             │ WorkflowDefinition
                             ▼
                    ┌─────────────────┐
                    │  validators.py   │
                    │  驗證定義正確性   │
                    └────────┬────────┘
                             │ List[ValidationError] 或通過
                             ▼
                    ┌─────────────────┐
                    │  executor.py     │
                    │  逐階段執行      │
                    └────────┬────────┘
                             │
                    ┌────────┴────────┐
                    │                 │
                    ▼                 ▼
              ┌──────────┐    ┌──────────┐
              │  Skills  │    │  Agents  │
              │ (無狀態)  │    │ (有狀態)  │
              └──────────┘    └──────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  context.py      │
                    │  執行狀態管理     │
                    └─────────────────┘
                             │
                             ▼
                    輸出：ExecutionContext（結果 + 變數 + 日誌）
```

### parser.py — YAML 到 Dataclass

**做什麼**：將 YAML 文件解析為 `WorkflowDefinition` dataclass。

**核心 dataclass 結構**：
```python
@dataclass
class StepDefinition:
    name: str
    skill: Optional[str] = None     # 使用哪個 Skill
    agent: Optional[str] = None     # 使用哪個 Agent
    input: Optional[Dict] = None    # 輸入參數
    output: Optional[str] = None     # 輸出變數名稱

@dataclass
class PhaseDefinition:
    name: str
    description: str
    steps: List[StepDefinition]

@dataclass
class WorkflowDefinition:
    name: str
    version: str
    description: str
    phases: List[PhaseDefinition]
    config: Optional[Dict] = None
```

**設計選擇**：使用 dataclass 而不是 dict，是因為 dataclass 提供了型別安全和IDE自動補全。這是「代碼品質」優先於「開發速度」的選擇。

### validators.py — 四層驗證

驗證器執行四層檢查：

1. **結構驗證**：YAML 是否符合 WorkflowDefinition 的 dataclass 結構？
2. **組件驗證**：引用的 Skill 和 Agent 是否存在於檔案系統？
3. **資料流驗證**：步驟之間的輸入輸出是否連接正確？
4. **配置驗證**：配置參數是否在允許範圍內？

```python
class Validator:
    def validate(self, workflow: WorkflowDefinition) -> List[ValidationError]:
        errors = []
        errors.extend(self._validate_structure(workflow))
        errors.extend(self._validate_components(workflow))
        errors.extend(self._validate_data_flow(workflow))
        errors.extend(self._validate_config(workflow))
        return errors
```

**實作狀態**：✅ 完成。這是引擎中最完整的模組。

### executor.py — 逐階段執行

**做什麼**：按照 WorkflowDefinition 的 phases 順序，逐步驟執行。

**執行流程**：
```python
async def execute(self, workflow: WorkflowDefinition, context: ExecutionContext) -> ExecutionContext:
    for phase in workflow.phases:
        for step in phase.steps:
            if step.skill:
                result = await self._execute_skill(step, context)
            elif step.agent:
                result = await self._execute_agent(step, context)
            context.set_step_result(phase.name, step.name, result)
    return context
```

**實作狀態**：⚠️ placeholder。`_execute_skill()` 和 `_execute_agent()` 目前只做了：
1. 在檔案系統中找到對應的 skill/agent 路徑
2. 打印 `[PLACEHOLDER] Would execute skill at: ...`
3. 返回模擬結果

**這是整個引擎最關鍵的缺口**——引擎能找到正確的組件，但不能真正執行它們。動態匯入和執行的邏輯尚未實作。

### context.py — 執行狀態管理

**做什麼**：管理工作流的執行狀態，包括：
- 變數存儲（步驟之間的資料傳遞）
- 階段結果記錄
- 步驟結果記錄
- JSON 序列化/反序列化（暫停/恢復工作流）

```python
class ExecutionContext:
    def set_variable(self, key: str, value: Any) -> None
    def get_variable(self, key: str, default: Any = None) -> Any
    def set_phase_result(self, phase: str, result: Dict) -> None
    def set_step_result(self, phase: str, step: str, result: Dict) -> None
    def to_json(self) -> str
    @classmethod
    def from_json(cls, json_str: str) -> 'ExecutionContext'
```

**實作狀態**：✅ 完成。支援序列化意味著工作流可以暫停和恢復。

---

## 內建模板

四個 YAML 模板覆蓋了主要開發場景：

### feature_development.yml — 功能開發

```yaml
name: feature_development
version: "1.0"
phases:
  - specify    # 規格定義（spec_parser）
  - plan       # 規劃（planner_agent）
  - execute    # 實作（executor_agent）
  - test       # 測試（test_runner）
  - review     # 審查（reviewer_agent）
```

五階段流程，對應 SDD（Spec-Driven Development）的 Specify → Plan → Implement → Verify，加上最後的 Review。

### bug_fix.yml — 修 Bug

```yaml
phases:
  - diagnose   # 診斷
  - plan       # 規劃
  - fix        # 修復
  - verify     # 驗證
```

四階段，先診斷再動手。

### refactoring.yml — 重構

```yaml
phases:
  - analyze    # 分析
  - plan       # 規劃
  - refactor   # 重構
  - verify     # 驗證
```

和 bug_fix 類似，但起點是分析而非診斷。

### rule_creation.yml — 規則建立

```yaml
phases:
  - research    # 研究
  - draft       # 草擬
  - review      # 審查
  - integrate   # 整合
```

這是 meta 層的工作流——用工作流來建立規則。

---

## 資料流全景

一個完整的工作流執行，資料是這樣流的：

```
1. 使用者啟動
   python devtools/cli.py workflow run workflows/templates/feature_development.yml
   
2. CLI 解析命令，呼叫 WorkflowEngine
   
3. parser.py 讀取 YAML → WorkflowDefinition dataclass
   
4. validators.py 驗證定義 → 通過或報錯
   
5. executor.py 開始執行：
   
   Phase: specify
     Step: spec_parser
       input: implementation_plan.md
       output: parsed_spec → 存入 ExecutionContext.variables
   
   Phase: plan
     Step: planner_agent
       input: parsed_spec（從 context 取出）
       output: execution_plan → 存入 ExecutionContext.variables
   
   Phase: execute
     Step: executor_agent
       input: execution_plan（從 context 取出）
       output: implementation_result → 存入 context
   
   Phase: test
     Step: test_runner
       input: test_config（從 context 取出）
       output: test_results → 存入 context
   
   Phase: review
     Step: reviewer_agent
       input: all_results（從 context 取出）
       output: review_report → 最終輸出
   
6. ExecutionContext 可序列化為 JSON，用於暫停/恢復/記錄
```

**關鍵洞察**：ExecutionContext 是步驟之間的橋樑。每一個步驟的輸出都存入 context，下一步從 context 取出輸入。這解決了步驟之間的資料傳遞問題，也讓工作流可以中斷後恢復。

---

## v2.0 路線圖

`task.md` 目前顯示的狀態是「Phase 5B: Workflow Intelligence」，計畫中的 v2.0 功能：

### 條件邊（Conditional Edges）

v1.0 的工作流是線性的——每個 phase 按順序執行。v2.0 要加入 `if-then-else` 條件：

```yaml
phases:
  - name: test
    steps:
      - name: run_tests
        skill: test_runner
  - name: handle_failure
    condition: "test_results.success == false"
    steps:
      - name: retry
        agent: executor_agent
```

這讓工作流可以根據前一步的結果決定下一步。

### 失敗重試（Retry Strategy）

```yaml
steps:
  - name: deploy
    agent: executor_agent
    retry:
      max_attempts: 3
      backoff: exponential
```

### 循環檢測（Cycle Detection）

防止工作流進入無限循環。

**v2.0 的挑戰**：純 YAML 無法表達複雜邏輯。加入條件邊和重試策略後，YAML 是不是太受限了？要不要引入 Jinja2 模板或 Python 表達式？這是待決的設計問題。

---

## 引擎的真相

引擎的四個模組，完成度不均：

| 模組 | 完成度 | 說明 |
|------|--------|------|
| parser.py | 🟢 90% | YAML 解析完整，缺少邊界情況處理 |
| validators.py | 🟢 85% | 四層驗證完整，自定義驗證規則未開放 |
| context.py | 🟢 80% | 序列化/反序列化完整，變數作用域管理待完善 |
| executor.py | 🔴 30% | 找路徑正確，但只返回模擬結果，未動態匯入執行 |

executor 是瓶頸。沒有真正的執行，整個引擎就是一個精緻的前端——可以解析、驗證、但最終不能跑。

這不是設計的失敗，是優先順序的選擇：**先讓骨架到位，證明架構可行，再填充肌肉。** 骨架確實到位了。肌肉還沒長出來。