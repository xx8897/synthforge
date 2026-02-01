# Bilingual Output Rule - 雙語輸出規則
# Layered Language Strategy

**Status**: MANDATORY 強制  
**Priority**: HIGH 高  
**Scope**: All synthforge outputs

---

## 🎯 規則目的 / Rule Purpose

採用分層語言策略，在保持核心規則精確性的同時，大幅節省 token 消耗。

Adopt layered language strategy to maintain core rule precision while significantly reducing token consumption.

---

## 📋 分層策略 / Layered Strategy

### Layer 1: 雙語（英文 + 中文）

**適用範圍**:
- 核心規則檔案（*_RULE.md）
- AI 配置檔案（.cursorrules, .github/copilot-instructions.md）
- VIBE_GUIDE.md
- README.md（根目錄）
- ARCHITECTURE.md

**理由**:
- AI 理解更精確（英文訓練數據更多）
- 可能需要國際協作
- 技術術語英文更精確
- 專業性更強

**格式**:
```markdown
[English content]

---

[中文內容]
```

---

### Layer 2: 純中文

**適用範圍**:
- .internal/ 所有內容
  - 任務總結
  - 確認文件
  - 分析文件
  - 知識庫
- docs/ 下的文件和指南
- 子目錄的 README.md

**理由**:
- 個人使用為主
- 節省 50-65% token
- 閱讀和撰寫更快
- 母語更自然

**格式**:
```markdown
[純中文內容]
```

---

### Layer 3: 純英文

**適用範圍**:
- 程式碼註解
- Git commit messages
- 變數和函數命名

**理由**:
- 業界慣例
- AI 輔助更好
- 可能開源

---

## 📊 Token 節省效果

### 改變前（全部雙語）:
```
核心規則: ~15K tokens
文件指南: ~30K tokens
.internal/: ~20K tokens
Total: ~65K tokens
```

### 改變後（分層策略）:
```
核心規則: ~15K tokens（雙語，保持）
文件指南: ~10K tokens（純中文，節省 66%）
.internal/: ~7K tokens（純中文，節省 65%）
Total: ~32K tokens

節省: ~33K tokens (50%)
```

---

## 🎯 AI 輸出格式規範

### 規則相關輸出 → 雙語
```markdown
When: 創建或修改 *_RULE.md
Format: 英文 + 中文（雙語）
```

### 任務總結 → 純中文
```markdown
When: 創建任務總結
Format: 純中文
File: .internal/summaries/YYYY-MM/任務總結_YYYY-MM-DD_HHMM.md
```

### 分析文件 → 純中文
```markdown
When: 創建分析文件
Format: 純中文
File: .internal/analysis/[topic]_analysis.md
```

### 確認文件 → 純中文
```markdown
When: 創建確認文件
Format: 純中文
File: .internal/confirmations/pending/[topic]_confirmation.md
```

### 知識點 → 純中文
```markdown
When: 創建知識點
Format: 純中文
File: .internal/knowledge/[category]/[name].md
```

### 文件和指南 → 純中文
```markdown
When: 創建 docs/ 下的文件
Format: 純中文
```

---

## ✅ 檢查清單

創建新文件時，確認語言策略：

- [ ] 是核心規則？→ 雙語
- [ ] 是 AI 配置？→ 英文或雙語
- [ ] 是 .internal/ 內容？→ 純中文
- [ ] 是 docs/ 文件？→ 純中文
- [ ] 是程式碼？→ 英文註解

---

## 🔄 現有文件處理

### 逐步遷移（推薦）:
- 新文件按新規則
- 舊文件保持不變
- 需要更新時改為新格式

### 優先遷移:
1. .internal/ 所有內容
2. docs/ 文件
3. 子目錄 README.md

### 保持雙語:
- 核心規則
- VIBE_GUIDE.md
- 根目錄 README.md
- ARCHITECTURE.md

---

## 📝 範例

### 範例 1: 任務總結（純中文）

```markdown
# 任務總結 - 2026-01-29 15:00

## ✅ 已完成的任務

| # | 任務 | 狀態 | 成果 |
|---|------|------|------|
| 1 | 創建新結構 | ✅ 完成 | .internal 分層結構 |

## 📋 創建/修改的文件

1. ✅ `.internal/README.md` - 索引檔案
2. ✅ `.internal/knowledge/README.md` - 知識庫索引

## 🎯 關鍵決策

- 採用分層語言策略
- .internal 全部改為純中文

---

**時間**: 2026-01-29 15:00  
**狀態**: 完成
```

---

### 範例 2: 核心規則（雙語）

```markdown
# Example Rule - 範例規則

**Status**: MANDATORY  
**狀態**: 強制

---

## Rule Content

This is the English content.

---

## 規則內容

這是中文內容。
```

---

### 範例 3: 知識點（純中文）

```markdown
# Python 最佳實踐

**類別**: best_practices  
**建立**: 2026-01-29  
**標籤**: #python #coding

---

## 摘要

Python 編碼的基本最佳實踐。

---

## 內容

### 1. 使用型別提示

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
```

### 2. 使用上下文管理器

```python
with open('file.txt', 'r') as f:
    content = f.read()
```
```

---

## 🎯 Summary

**Key Points**:

1. ✅ 核心規則 → 雙語（保持精確性）
2. ✅ .internal/ → 純中文（節省 token）
3. ✅ docs/ → 純中文（個人使用）
4. ✅ 程式碼 → 英文（業界慣例）

**Token 節省**: ~50%

**This rule balances precision and efficiency through layered language strategy.**  
**此規則通過分層語言策略平衡精確性和效率。**

---

**Created**: 2026-01-29  
**Status**: ACTIVE  
**Priority**: HIGH  
**Enforcement**: MANDATORY

---

## 🔗 相關規則 / Related Rules
- [DIRECTORY_README_RULE](DIRECTORY_README_RULE.md): 目錄層級的說明規則
- [FILE_NAMING_CONVENTION_RULE](../development/FILE_NAMING_CONVENTION_RULE.md): 檔案命名規範
- [INTERNAL_RULE](../development/INTERNAL_RULE.md): 內部目錄語言規範
