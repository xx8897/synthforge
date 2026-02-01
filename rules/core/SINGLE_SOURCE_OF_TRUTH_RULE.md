# 單一真理來源規則 - SINGLE_SOURCE_OF_TRUTH_RULE.md
# SSOT Principle

**狀態**: MANDATORY
**優先級**: MEDIUM
**範圍**: 所有知識、狀態、邏輯與配置

---

## 🎯 規則目的 / Rule Purpose

確保系統中的每一份知識（資料、邏輯、配置）都只有單一且明確的權威性來源，避免因多處維護導致的不一致性。

Ensure every piece of knowledge (data, logic, configuration) has a single, unambiguous, authoritative representation.

---

## 🏗️ SSOT Implementation / 實作 SSOT

### 1. 知識 SSOT (Knowledge)
- **規則**: `VIBE_GUIDE.md` 是導航的 SSOT。
- **規則**: `ARCHITECTURE.md` 是結構的 SSOT。
- **規則**: 避免在多個文件中重複描述同一概念，應使用「引用 (Link)」。

### 2. 程式碼 SSOT (Code)
- **規則**: 通用邏輯必須提取至 `core_lib`。
- **規則**: 不要複製貼上 (Copy-Paste) 函數，應引用導入。
- **規則**: 常數 (Constants) 應定義在單一配置檔或類別中。

### 3. 狀態 SSOT (State)
- **規則**: 避免在不同組件間同步狀態，應由一個組件持有並傳遞。
- **規則**: 資料庫或持久化存儲是最終的真理來源。

---

## 🚫 常見反模式 / Anti-Patterns

### 1. 幽靈配置 (Ghost Configs)
- **錯誤**: 在多個檔案中硬編碼相同的設定值（如 API URL）。
- **修正**: 提取至 `core_lib.config` 或單一環境變數。

### 2. 文檔分歧 (Documentation Divergence)
- **錯誤**: 在 `README.md` 和 `DOCS.md` 中分別描述同一功能，卻未同步。
- **修正**: 其中一個做為 SSOT，另一個僅包含連結。

---

## ✅ 檢查清單 / Checklist

- [ ] 這個資訊是否已經在其他地方定義過？
- [ ] 如果我修改這裡，是否需要同時修改其他地方？（如果是，則違反 SSOT）
- [ ] 是否可以透過引用代替複製？

---

**創建時間**: 2026-02-01
**狀態**: ACTIVE
**優先級**: HIGH

---

## 🔗 相關規則 / Related Rules
- [DRY_RULE](DRY_RULE.md): SSOT 是 DRY 原則的延伸
- [VIBE_GUIDE_SYNC_RULE](VIBE_GUIDE_SYNC_RULE.md): 文檔的 SSOT 實踐
- [TOOLING_USAGE_RULE](../development/TOOLING_USAGE_RULE.md): 工具程式碼的 SSOT
