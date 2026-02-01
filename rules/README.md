# Rules - synthforge 規則

**用途**: 集中管理所有 synthforge 規則  
**原則**: 明確、可執行、DRY

---

## 📁 目錄結構

| 目錄 | 用途 | 規則數 |
|------|------|---------|
| core/ | 核心規則（強制執行） | 7 |
| development/ | 開發規則 | 14 |
| management/ | 管理規則 | 1 |

**總計**: 22 個規則

---

## 📋 Core Rules / 核心規則

### 1. AGENT_WORKFLOW_RULE.md ⭐⭐⭐⭐⭐
**用途**: AI Agent 工作流規範  
**狀態**: MANDATORY  
**觸發**: 每次執行任務前

**核心要求**:
- 執行前必須檢查相關規則
- Rules 優先於 Skills
- 根據任務類型查表
- 違規立即修正

---

### 2. DIRECTORY_README_RULE.md ⭐⭐⭐⭐⭐
**用途**: 目錄 README 管理規則  
**狀態**: MANDATORY  
**觸發**: 查看/使用/修改目錄前

**核心要求**:
- 進入目錄前讀 README.md
- 修改後更新 README.md
- 結構變更時更新 ARCHITECTURE.md

---

### 2. VIBE_GUIDE_SYNC_RULE.md ⭐⭐⭐⭐⭐
**用途**: VIBE_GUIDE 同步策略  
**狀態**: MANDATORY  
**觸發**: 結構變更時

**核心要求**:
- 所有變更更新 ARCHITECTURE.md
- 只有頂層變更更新 VIBE_GUIDE.md
- Option B 策略（引用而非重複）

---

### 3. BILINGUAL_OUTPUT_RULE.md ⭐⭐⭐⭐
**用途**: 分層語言策略  
**狀態**: MANDATORY  
**觸發**: 創建文件時

**核心要求**:
- Layer 1 (雙語): 核心規則、AI 配置
- Layer 2 (純中文): .internal/、docs/
- Layer 3 (英文): 程式碼註解

---

### 4. DRY_RULE.md ⭐⭐⭐⭐⭐
**用途**: Don't Repeat Yourself 原則  
**狀態**: MANDATORY  
**觸發**: 創建/修改程式碼或文件時

**核心要求**:
- MUST: 重複 3 次以上必須提取
- SHOULD: 重複 2 次評估後決定
- MAY: 可讀性、不同概念、解耦優先可保留
- Balance: 不要過度 DRY

---

### 5. SERIES_TASK_WORKFLOW_RULE.md ⭐⭐⭐⭐⭐
**用途**: 系列任務工作流規則  
**狀態**: MANDATORY  
**觸發**: 系列任務完成後

**核心要求**:
- Step 1: 檢查並更新 TODO（當天有 → 更新；無 → 創建）
- Step 2: 檢查並創建/更新總結（當小時有 → 更新；無 → 創建）
- TODO = 任務追蹤器，總結 = 持續記錄

---

### 6. SINGLE_SOURCE_OF_TRUTH_RULE.md ⭐⭐⭐⭐⭐
**用途**: 單一真理來源原則  
**狀態**: MANDATORY  
**觸發**: 創建/修改任何知識、邏輯、配置時

**核心要求**:
- 每份知識只有單一權威來源
- 避免多處維護導致不一致
- 使用引用代替複製

---

## 🔧 Development Rules / 開發規則

### 6. FILE_NAMING_CONVENTION_RULE.md ⭐⭐⭐⭐
**用途**: 統一檔案命名規範  
**狀態**: MANDATORY  
**觸發**: 創建新檔案時

**核心要求**:
- 規則: `[TOPIC]_RULE.md` (大寫)
- 程式碼: `[module].py` (小寫)
- 總結: `summary_YYYY-MM-DD_HH.md`
- 知識: `[name].md` (小寫)

---

### 7. INTERNAL_RULE.md ⭐⭐⭐⭐⭐
**用途**: .internal 目錄管理  
**狀態**: MANDATORY  
**觸發**: 使用 .internal/ 時

**核心要求**:
- 6 個子目錄結構
- 任務完成前創建總結
- Token 監控和建議性清理
- 知識點管理

---

### 8. TASK_SUMMARY_RULE.md ⭐⭐⭐⭐⭐
**用途**: 任務總結規則  
**狀態**: MANDATORY  
**觸發**: 系列任務完成後

**核心要求**:
- 格式: `summary_YYYY-MM-DD_HH.md`
- 創建前必須查看當天最新總結
- 同一小時內更新現有總結

---

### 9. TODO_UPDATE_RULE.md ⭐⭐⭐⭐⭐
**用途**: TODO 更新規則  
**狀態**: MANDATORY  
**觸發**: 系列任務完成後

**核心要求**:
- 格式: `TODO_MM_DD.md`
- 系列性問答確認後必須更新
- 最多 5 個 TODO 檔案

---

### 10. CODING_STYLE_RULE.md ⭐⭐⭐⭐⭐
**用途**: 程式碼風格與 Clean Code 規範  
**狀態**: MANDATORY  
**觸發**: 編寫任何程式碼時

**核心要求**:
- 小函數（< 20 行）
- 單一職責原則 (SRP)
- 有意義的命名
- 型別提示必須
- 無佔位符（NO `pass`, `...`, `TODO`）

---

### 11. SPEC_DRIVEN_DEVELOPMENT_RULE.md ⭐⭐⭐⭐⭐
**用途**: 規格驅動開發工作流  
**狀態**: MANDATORY  
**觸發**: 開始任何功能或複雜任務時

**核心要求**:
- Step 1: Specify (創建 implementation_plan.md)
- Step 2: Clarify & Review (請求用戶審查)
- Step 3: Spec-as-Source (規格即源碼)
- Step 4: Tasks (分解為 task.md)
- Step 5: Implement (嚴格依照規格)
- Step 6: Verify (測試並創建 walkthrough.md)

---

### 12. FILE_CLASSIFICATION_RULE.md ⭐⭐⭐⭐
**用途**: 檔案分類與放置決策樹  
**狀態**: MANDATORY  
**觸發**: 創建新檔案時

**核心要求**:
- 程式碼 vs 文件決策樹
- 明確的檔案類型對應表
- 避免檔案放置混亂

---

### 13. TOOLING_USAGE_RULE.md ⭐⭐⭐⭐⭐
**用途**: Core Lib vs Devtools 使用規範  
**狀態**: MANDATORY  
**觸發**: 開發新工具或函數時

**核心要求**:
- 明確區分 Runtime 與 Development 依賴
- 依賴方向規則（Devtools 可引用 Core Lib，反之不可）
- 避免工具程式碼重複與依賴混亂

---

### 14. TDD_RULE.md ⭐⭐⭐⭐⭐
**用途**: 測試驅動開發規範  
**狀態**: MANDATORY  
**觸發**: 編寫代碼前
**位置**: [development/TDD_RULE.md](development/TDD_RULE.md)

**核心要求**:
- 紅燈 -> 綠燈 -> 重構循環
- 測試覆蓋率 80%+
- 無測試不代碼

---

### 15. AGENT_STRUCTURE_RULE.md ⭐⭐⭐⭐⭐
**用途**: Agent 開發結構規範  
**狀態**: MANDATORY  
**觸發**: 創建新 Agent 時
**位置**: [development/AGENT_STRUCTURE_RULE.md](development/AGENT_STRUCTURE_RULE.md)

**核心要求**:
- 標準目錄結構 (AGENT.md, config.yml)
- 標準接口與返回格式
- 強制異步執行

---

### 16. WORKFLOW_INTEGRATION_RULE.md ⭐⭐⭐⭐⭐
**用途**: Skills/Agents 整合規範  
**狀態**: MANDATORY  
**觸發**: 整合組件到 Workflow 時
**位置**: [development/WORKFLOW_INTEGRATION_RULE.md](development/WORKFLOW_INTEGRATION_RULE.md)

**核心要求**:
- 標準函數簽名
- 配置驅動整合
- 錯誤處理轉化為結構化輸出

---

### 17. KNOWLEDGE_BASE_RULE.md ⭐⭐⭐⭐⭐
**用途**: 知識庫提取與管理規則  
**狀態**: MANDATORY  
**觸發**: 對話中產生新概念或解決重要問題時
**位置**: [management/KNOWLEDGE_BASE_RULE.md](management/KNOWLEDGE_BASE_RULE.md)

---

### 18. WORKFLOW_RULE.md ⭐⭐⭐⭐⭐
**用途**: Workflow 創建與執行規則  
**狀態**: MANDATORY  
**觸發**: 創建或執行 workflow 時
**位置**: [../workflows/WORKFLOW_RULE.md](..//workflows/WORKFLOW_RULE.md)

---

## 📋 Management Rules / 管理規則

---

## 🎯 快速參考

### 創建新檔案時:
1. 檢查 [FILE_CLASSIFICATION_RULE](development/FILE_CLASSIFICATION_RULE.md)
2. 檢查 [FILE_NAMING_CONVENTION_RULE](development/FILE_NAMING_CONVENTION_RULE.md)
3. 檢查 [BILINGUAL_OUTPUT_RULE](core/BILINGUAL_OUTPUT_RULE.md)
4. 檢查 [DRY_RULE](core/DRY_RULE.md)

### 修改結構時:
1. 檢查 [DIRECTORY_README_RULE](core/DIRECTORY_README_RULE.md)
2. 檢查 [VIBE_GUIDE_SYNC_RULE](core/VIBE_GUIDE_SYNC_RULE.md)

### 開發新工具時:
1. 檢查 [TOOLING_USAGE_RULE](development/TOOLING_USAGE_RULE.md)
2. 檢查 [SINGLE_SOURCE_OF_TRUTH_RULE](core/SINGLE_SOURCE_OF_TRUTH_RULE.md)
3. 檢查 [CODING_STYLE_RULE](development/CODING_STYLE_RULE.md)

### 使用 .internal/ 時:
1. 檢查 [INTERNAL_RULE](development/INTERNAL_RULE.md)

### 系列任務完成後:
1. 檢查 [SERIES_TASK_WORKFLOW_RULE](core/SERIES_TASK_WORKFLOW_RULE.md)
2. 檢查 [TASK_SUMMARY_RULE](development/TASK_SUMMARY_RULE.md)
3. 檢查 [TODO_UPDATE_RULE](development/TODO_UPDATE_RULE.md)
4. 檢查 [KNOWLEDGE_BASE_RULE](management/KNOWLEDGE_BASE_RULE.md)

---

## 📊 規則優先級

| 優先級 | 規則 | 何時檢查 |
|--------|------|---------|
| ⭐⭐⭐⭐⭐ | DIRECTORY_README_RULE | 每次進入目錄 |
| ⭐⭐⭐⭐⭐ | VIBE_GUIDE_SYNC_RULE | 結構變更 |
| ⭐⭐⭐⭐⭐ | DRY_RULE | 創建/修改程式碼 |
| ⭐⭐⭐⭐⭐ | INTERNAL_RULE | 使用 .internal/ |
| ⭐⭐⭐⭐⭐ | SERIES_TASK_WORKFLOW_RULE | 系列任務完成 |
| ⭐⭐⭐⭐⭐ | TASK_SUMMARY_RULE | 系列任務完成 |
| ⭐⭐⭐⭐⭐ | TODO_UPDATE_RULE | 系列任務完成 |
| ⭐⭐⭐⭐ | BILINGUAL_OUTPUT_RULE | 創建文件 |
| ⭐⭐⭐⭐ | FILE_NAMING_CONVENTION_RULE | 創建檔案 |

---

## ✅ 規則檢查清單

創建新功能時:
- [ ] 檔案命名符合規範？
- [ ] 語言策略正確？
- [ ] 無重複內容（DRY）？
- [ ] 目錄 README 已更新？
- [ ] 結構變更已同步？

---

**最後更新**: 2026-02-01  
**規則數量**: 20  
**狀態**: ACTIVE
