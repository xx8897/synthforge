---
title: "開發工具箱"
document_type: reference
version: 1.0
language: zh-TW
cli_command_groups:
  - group: new
    purpose: "從模板建立專案"
    templates: [python-cli, python-fastapi, node-express, static-web]
  - group: check
    purpose: "安全稽核、授權檢查、依賴分析"
  - group: release
    purpose: "專案發布準備"
  - group: analyze
    purpose: "依賴與授權分析"
  - group: workflow
    purpose: "工作流執行、驗證、列表"
  - group: git
    purpose: "自動化 Git 操作（commit/push/tag/pr）"
  - group: graph
    purpose: "知識圖譜建構與視覺化"
  - group: task
    purpose: "任務歸檔"
  - group: doc
    purpose: "PDF/URL 文件載入與分割"
  - group: interactive
    purpose: "互動式 Shell 模式"
other_tools:
  - name: knowledge_graph.py
    purpose: "掃描規則 YAML frontmatter 與關聯連結，生成 Mermaid 圖"
  - name: structure_optimizer.py
    purpose: "自動化檔案重構（搬移、刪除、重命名），支援 dry-run"
related_documents:
  - 02_ARCHITECTURE.md
  - 05_WORKFLOW_ENGINE.md
tags: [devtools, cli, knowledge-graph, structure-optimizer]
---

# 開發工具箱

> CLI 是人和 AI 代理的共同入口。一個命令可以做的事，就不需要手動操作。

## CLI — 七大命令群

`devtools/cli.py` 是 synthforge 的統一入口，726 行，使用 `click` 框架。

### 1. `new` — 從模板建立專案

```bash
python devtools/cli.py new my-project --template python-fastapi
```

四個模板：
- `python-cli` — Python CLI 應用
- `python-fastapi` — FastAPI Web 服務
- `node-express` — Express.js 後端
- `static-web` — 靜態網站

每個模板會建立完整的目錄結構、配置文件、初始測試。

### 2. `check` — 安全稽核

```bash
python devtools/cli.py check --all        # 全部檢查
python devtools/cli.py check --security   # 安全檢查
python devtools/cli.py check --license    # 授權檢查
python devtools/cli.py check --deps       # 依賴分析
```

三個子檢查：
- **security**：掃描敏感文件（`.env`、金鑰檔案、硬編碼密鑰）
- **license**：檢查依賴的授權相容性
- **deps**：分析依賴結構和版本

### 3. `release` — 發布準備

```bash
python devtools/cli.py release --clean --security-check
```

準備發布，可選擇清理臨時文件和安全檢查。

### 4. `analyze` — 依賴分析

```bash
python devtools/cli.py analyze --deps --licenses
```

與 `check` 類似但更深入，提供依賴圖和授權報告。

### 5. `workflow` — 工作流操作

```bash
python devtools/cli.py workflow list                          # 列出所有工作流
python devtools/cli.py workflow run workflows/templates/feature_development.yml  # 執行
python devtools/cli.py workflow validate workflows/templates/bug_fix.yml        # 驗證
```

三個子命令：
- `list`：掃描 `workflows/templates/` 和 `workflows/examples/`，列出所有 YAML
- `run`：呼叫 WorkflowEngine 執行指定工作流
- `validate`：呼叫 Validator 驗證工作流定義

### 6. `git` — 自動化 Git 操作

```bash
python devtools/cli.py git commit -m "feat: add feature" -a   # 智慧提交
python devtools/cli.py git push                                  # 推送
python devtools/cli.py git tag v1.0.0                            # 標籤
python devtools/cli.py git pr --title "Feature" --body "Desc"   # PR
```

`-a` 參數自動暫存所有修改文件，省去 `git add`。提交訊息建議遵循語義化提交規範（定義在 `SMART_GIT_RULE.md`）。

### 7. `graph` — 知識圖譜

```bash
python devtools/cli.py graph build    # 建構圖譜
python devtools/cli.py graph show     # 顯示圖譜
```

掃描規則文件和知識文件，生成 Mermaid 格式的關聯圖。詳見下方 `knowledge_graph.py`。

### 8. `task` — 任務管理

```bash
python devtools/cli.py task archive
```

歸檔已完成的任務（將 `[x]` 項目從 `task.md` 移出）。

### 9. `doc` — 文件處理

```bash
python devtools/cli.py doc load spec.pdf --split
python devtools/cli.py doc load https://example.com/api-docs
```

載入 PDF 或 URL 文件，可選擇分割成較小的段落。

### 10. `interactive` — 互動式 Shell

```bash
python devtools/cli.py interactive
```

進入互動式模式，可以連續下命令而不需要反覆輸入 `python devtools/cli.py`。

---

## knowledge_graph.py — 規則關聯映射

### 做什麼

掃描專案中所有規則文件（Markdown）和知識文件，提取：
- YAML frontmatter 中的元資料
- 文件內的交叉引用連結
- `related_rules`、`related_concepts` 等關聯欄位

然後生成 Mermaid 格式的關聯圖。

### 怎麼做

```python
class KnowledgeGraph:
    def build(self) -> Dict:
        # 1. 掃描 rules/ 目錄下所有 .md 文件
        # 2. 解析 YAML frontmatter
        # 3. 提取關聯連結
        # 4. 建構節點和邊
        # 5. 生成 Mermaid 圖表示
        
    def show(self) -> str:
        # 輸出 Mermaid 圖
```

### 為什麼需要

22 條規則互相引用，形成一張複雜的網路。知識圖譜讓這張網路可視化，幫助：
1. 發現引用死鏈（規則引用了不存在的規則）
2. 發現孤立節點（沒有被任何規則引用的規則）
3. 理解規則之間的影響鏈（修改一條規則會影響哪些其他規則）

**這是對規則系統複雜度的自我回應**——當你需要一個工具來理解你自己制定的規則時，規則可能已經太多了。

---

## structure_optimizer.py — 檔案重構工具

### 做什麼

自動化檔案重構操作：搬移、刪除、重命名。

### 怎麼做

```python
class StructureOptimizer:
    def optimize(self, plan: List[Dict]) -> Dict:
        # plan 是一組操作指令
        # 每個指令格式：{'action': 'move'|'delete'|'rename', 'from': ..., 'to': ...}
        
    def dry_run(self, plan: List[Dict]) -> Dict:
        # dry-run 模式：只顯示會做什麼，不真的做
```

### 設計亮點

**dry-run 模式**：在真正執行之前，可以先看會發生什麼。這是破壞性操作的安全網。

### 與規則的關聯

`DIRECTORY_README_RULE` 要求每次修改文件結構後更新 README。`structure_optimizer.py` 可以在重構後自動觸發 README 更新——工具和規則的配合。

---

## 安全工具

`devtools/security/` 提供安全稽核功能：

- 掃描 `.env`、金鑰檔案、硬編碼密鑰
- 檢查依賴的已知漏洞
- 授權相容性分析

與 CLI `check --security` 命令整合。

---

## 分析器

`devtools/analyzers/` 提供代碼分析功能：

- 依賴關係分析
- 授權合規檢查
- 代碼指標統計

與 CLI `analyze` 命令整合。

---

## 設計觀察

CLI 的設計有幾個值得注意的選擇：

### 1. 統一入口 vs 分散工具

所有操作都透過 `cli.py` 一個入口。這是對的——工具分散的時候，人類和 AI 代理都需要記住每個工具的路徑和用法。統一入口降低了認知負擔。

### 2. 依賴方向清晰

`cli.py` 可以 import `core_lib`，但 `core_lib` 不能 import `devtools`。這條規則寫在 `TOOLING_USAGE_RULE.md` 裡。

### 3. 缺少依賴管理

CLI 使用 `click`、`pyyaml`、`pytest` 等外部依賴，但專案中沒有 `requirements.txt` 或 `setup.py`。這是一個明顯的缺口——安裝 synthforge 需要手動安裝每個依賴。

### 4. 知識圖譜的定位

`knowledge_graph.py` 是一個有趣的存在：它是工具，但它的目的是理解規則。工具服務治理，治理反過來又定義工具。這種循環是 synthforge 的特色——規則系統足夠複雜，需要專門的工具來管理。