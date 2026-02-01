# Development Rules - 開發規則

**用途**: 規範 synthforge 的開發流程、代碼風格與組件整合。

---

## 📋 規則清單 (Rule List)

### 1. 核心開發工作流 (Core Development Workflow)

#### [SPEC_DRIVEN_DEVELOPMENT_RULE.md](SPEC_DRIVEN_DEVELOPMENT_RULE.md)
**用途**: 規格驅動開發工作流 (SDD)  
**內容**: Specify -> Plan -> Implement -> Verify 的完整流程。

#### [TDD_RULE.md](TDD_RULE.md)
**用途**: 測試驅動開發規範  
**內容**: 紅燈-綠燈-重構循環與測試標準。

---

### 2. 組件與整合 (Components & Integration)

#### [AGENT_STRUCTURE_RULE.md](AGENT_STRUCTURE_RULE.md)
**用途**: Agent 開發結構規範  
**內容**: 標準化 Agent 的目錄、配置與接口。

#### [WORKFLOW_INTEGRATION_RULE.md](WORKFLOW_INTEGRATION_RULE.md)
**用途**: Workflow 整合標準  
**內容**: 如何將 Skills 和 Agents 接入 Workflow 系統。

#### [TOOLING_USAGE_RULE.md](TOOLING_USAGE_RULE.md)
**用途**: 工具使用與依賴規範  
**內容**: 區分 Core Lib 與 Devtools，防止循環依賴。

---

### 3. 代碼質量與命名 (Code Quality & Naming)

#### [CODING_STYLE_RULE.md](CODING_STYLE_RULE.md)
**用途**: 程式碼風格規範  
**內容**: Clean Code、命名、型別提示等要求。

#### [FILE_NAMING_CONVENTION_RULE.md](FILE_NAMING_CONVENTION_RULE.md)
**用途**: 檔案命名規範  
**內容**: 統一各類檔案的命名格式。

#### [FILE_CLASSIFICATION_RULE.md](FILE_CLASSIFICATION_RULE.md)
**用途**: 檔案分類決策  
**內容**: 檔案應該放在哪裡的決策邏輯。

---

### 4. 系統內部管理 (Internal Management)

#### [INTERNAL_RULE.md](INTERNAL_RULE.md)
**用途**: `.internal/` 目錄管理  
**內容**: 任務追蹤、Token 監測與知識管理。

#### [TASK_SUMMARY_RULE.md](TASK_SUMMARY_RULE.md)
**用途**: 任務總結規範  
**內容**: 格式、更新頻率與內容要求。

#### [TODO_UPDATE_RULE.md](TODO_UPDATE_RULE.md)
**用途**: TODO 更新規範  
**內容**: 任務追蹤檔案的管理。

---

## 🎯 執行準則 (Guidelines)

1. **先讀規格**: 在開發前必須閱讀對應的規則。
2. **強制執行**: 所有開發規則均為 `MANDATORY`。
3. **持續更新**: 隨著系統演進，規則應定期審閱與更新。

---

**最後更新**: 2026-02-01  
**位置**: `rules/development/`  
**狀態**: Active
