# File Naming Convention Rule - 檔案命名規範規則
# Standardized Naming Across synthforge

**Status**: MANDATORY 強制  
**Priority**: HIGH 高  
**Scope**: All files in synthforge workspace

---

## 🎯 規則目的 / Rule Purpose

建立統一的檔案命名規範，確保：
1. 檔案類型一目了然
2. 易於搜尋和分類
3. 避免命名衝突
4. 符合業界最佳實踐

Establish unified file naming conventions to ensure:
1. File types are immediately clear
2. Easy to search and categorize
3. Avoid naming conflicts
4. Follow industry best practices

---

## 📋 核心命名規則

### Rule 1: 規則檔案 / Rule Files

**格式**: `[TOPIC]_RULE.md`

**特點**:
- 全大寫
- 底線分隔
- 必須有 `_RULE` 後綴

**範例**:
```
✅ DIRECTORY_README_RULE.md
✅ VIBE_GUIDE_SYNC_RULE.md
✅ BILINGUAL_OUTPUT_RULE.md
✅ CODING_STYLE_RULE.md
✅ COMMIT_CONVENTION_RULE.md
✅ KNOWLEDGE_MANAGEMENT_RULE.md

❌ directory-readme-rule.md (不是全大寫)
❌ DIRECTORY_README.md (缺少 _RULE)
❌ DirectoryReadmeRule.md (不是底線分隔)
```

**位置**: `rules/[category]/[TOPIC]_RULE.md`

---

### Rule 2: 確認文件 / Confirmation Documents

**格式**: `[topic]_confirmation.md`

**特點**:
- 全小寫
- 底線分隔
- 必須有 `_confirmation` 後綴

**範例**:
```
✅ rules_strategy_confirmation.md
✅ devtools_restructure_confirmation.md
✅ architecture_design_confirmation.md

❌ RulesStrategyConfirmation.md (不是小寫)
❌ rules-strategy-confirmation.md (不是底線)
❌ rules_strategy.md (缺少 _confirmation)
```

**位置**: `.internal/confirmations/pending/`

---

### Rule 3: 分析文件 / Analysis Documents

**格式**: `[topic]_analysis.md`

**特點**:
- 全小寫
- 底線分隔
- 必須有 `_analysis` 後綴

**範例**:
```
✅ rules_naming_expert_analysis.md
✅ token_limits_industry_standards.md
✅ performance_bottleneck_analysis.md

❌ RulesNamingAnalysis.md
❌ rules-naming-analysis.md
```

**位置**: `.internal/analysis/`

---

### Rule 4: 任務總結 / Task Summaries

**格式**: `summary_YYYY-MM-DD_HH.md`

**特點**:
- 英文名稱（便於搜尋和排序）
- 日期時間格式固定（使用小時，避免檔案過多）
- 底線分隔

**範例**:
```
✅ summary_2026-01-29_14.md
✅ summary_2026-02-01_09.md

❌ summary_2026-01-29_1415.md (不使用分鐘)
❌ 任務總結_2026-01-29.md (不使用中文)
❌ summary_20260129.md (日期格式錯誤)
❌ summary-2026-01-29.md (不是底線)
```

**位置**: `.internal/summaries/YYYY-MM/`

---

### Rule 5: 知識點文件 / Knowledge Documents

**格式**: `[descriptive_name].md`

**特點**:
- 全小寫
- 底線分隔
- 描述性名稱
- 不需要特殊後綴

**範例**:
```
✅ python_best_practices.md
✅ git_workflow_tips.md
✅ debugging_common_errors.md
✅ api_reference_fastapi.md

❌ PythonBestPractices.md (不是小寫)
❌ python-best-practices.md (不是底線)
❌ python.md (不夠描述性)
```

**位置**: `.internal/knowledge/[category]/`

---

### Rule 6: 架構文件 / Architecture Documents

**格式**: `[TOPIC].md`

**特點**:
- 全大寫
- 底線分隔（如需要）
- 不需要後綴

**範例**:
```
✅ ARCHITECTURE.md
✅ FEATURES.md
✅ ROADMAP.md
✅ IMPLEMENTATION_PLAN.md

❌ architecture.md (不是大寫)
❌ Architecture.md (不是全大寫)
```

**位置**: `docs/architecture/`

---

### Rule 7: 指南文件 / Guide Documents

**格式**: `[TOPIC].md` 或 `[TOPIC]_GUIDE.md`

**特點**:
- 全大寫
- 可選 `_GUIDE` 後綴

**範例**:
```
✅ QUICKSTART.md
✅ DOC_GUIDE.md
✅ AGENT_RULES.md
✅ CONTRIBUTING.md

❌ quickstart.md
❌ DocGuide.md
```

**位置**: `docs/guides/`

---

### Rule 8: 策略文件 / Strategy Documents

**格式**: `[TOPIC]_STRATEGY.md`

**特點**:
- 全大寫
- 必須有 `_STRATEGY` 後綴

**範例**:
```
✅ GITHUB_STRATEGY.md
✅ TESTING_STRATEGY.md
✅ DEPLOYMENT_STRATEGY.md

❌ GITHUB.md (缺少 _STRATEGY)
❌ github_strategy.md (不是大寫)
```

**位置**: `docs/strategies/`

---

### Rule 9: 程式碼檔案 / Code Files

**格式**: `[module_name].py` (Python)

**特點**:
- 全小寫
- 底線分隔
- 描述性名稱

**範例**:
```
✅ security_auditor.py
✅ dependency_analyzer.py
✅ release_cleaner.py

❌ SecurityAuditor.py (不是小寫)
❌ security-auditor.py (不是底線)
❌ sa.py (不夠描述性)
```

**位置**: `devtools/`, `core_lib/`

---

## 📊 命名規範總表

| File Type | Format | Case | Separator | Suffix | Example |
|-----------|--------|------|-----------|--------|---------|
| **Rules** | `[TOPIC]_RULE.md` | UPPER | `_` | `_RULE` | `DIRECTORY_README_RULE.md` |
| **Confirmations** | `[topic]_confirmation.md` | lower | `_` | `_confirmation` | `rules_strategy_confirmation.md` |
| **Analysis** | `[topic]_analysis.md` | lower | `_` | `_analysis` | `token_limits_analysis.md` |
| **Summaries** | `summary_YYYY-MM-DD_HH.md` | lower | `_` | - | `summary_2026-01-29_14.md` |
| **Knowledge** | `[name].md` | lower | `_` | - | `python_best_practices.md` |
| **Architecture** | `[TOPIC].md` | UPPER | `_` | - | `ARCHITECTURE.md` |
| **Guides** | `[TOPIC].md` | UPPER | `_` | optional `_GUIDE` | `QUICKSTART.md` |
| **Strategies** | `[TOPIC]_STRATEGY.md` | UPPER | `_` | `_STRATEGY` | `GITHUB_STRATEGY.md` |
| **Code** | `[module].py` | lower | `_` | `.py` | `security_auditor.py` |

---

## 🔍 搜尋模式 / Search Patterns

### 找到所有規則:
```bash
find . -name "*_RULE.md"
```

### 找到所有確認文件:
```bash
find .internal/confirmations/pending -name "*_confirmation.md"
```

### 找到所有分析:
```bash
find .internal/analysis -name "*_analysis.md"
```

### 找到所有知識點:
```bash
find .internal/knowledge -name "*.md"
```

---

## ✅ 檢查清單 / Checklist

創建新檔案時，確認：

- [ ] 檔案類型正確（規則/確認/分析/知識等）
- [ ] 命名格式符合規範
- [ ] 大小寫正確
- [ ] 分隔符正確（底線 `_`）
- [ ] 後綴正確（如需要）
- [ ] 位置正確（對應目錄）

---

## 🚨 常見錯誤 / Common Mistakes

### 錯誤 1: 大小寫混用
```
❌ DirectoryReadmeRule.md
✅ DIRECTORY_README_RULE.md (規則)
✅ directory_readme_rule.md (如果是程式碼)
```

### 錯誤 2: 使用連字號
```
❌ directory-readme-rule.md
✅ directory_readme_rule.md
```

### 錯誤 3: 缺少必要後綴
```
❌ DIRECTORY_README.md (在 rules/ 下)
✅ DIRECTORY_README_RULE.md
```

### 錯誤 4: 不夠描述性
```
❌ dr.md
❌ rule1.md
✅ DIRECTORY_README_RULE.md
```

---

## 🔄 重新命名指南 / Renaming Guide

如果發現檔案命名不符合規範：

### Step 1: 確認新名稱
```
Old: DirectoryReadmeRule.md
New: DIRECTORY_README_RULE.md
```

### Step 2: 使用 git mv
```bash
git mv DirectoryReadmeRule.md DIRECTORY_README_RULE.md
```

### Step 3: 更新所有引用
```bash
# 搜尋引用
grep -r "DirectoryReadmeRule.md" .

# 更新引用
# (手動或腳本)
```

### Step 4: 提交
```bash
git commit -m "refactor: rename to follow naming convention"
```

---

## 📝 例外情況 / Exceptions

### 1. 第三方工具配置檔案
```
✅ .cursorrules (工具要求)
✅ .gitignore (業界慣例)
✅ package.json (Node.js 慣例)
```

### 2. README 檔案
```
✅ README.md (業界慣例，全大寫)
```

### 3. 特殊文件
```
✅ LICENSE (業界慣例)
✅ CHANGELOG.md (業界慣例)
✅ CONTRIBUTING.md (業界慣例)
```

---

## 🎯 Summary / 總結

**Key Points**:

1. ✅ 規則檔案: `[TOPIC]_RULE.md` (大寫)
2. ✅ 確認文件: `[topic]_confirmation.md` (小寫)
3. ✅ 分析文件: `[topic]_analysis.md` (小寫)
4. ✅ 知識點: `[descriptive_name].md` (小寫)
5. ✅ 任務總結: `任務總結_YYYY-MM-DD_HHMM.md` (中文)
6. ✅ 一律使用底線 `_` 分隔

**This rule ensures consistent, searchable, and professional file naming.**  
**此規則確保一致、可搜尋和專業的檔案命名。**

---

---

## 📚 相關規則 / Related Rules

### 強依賴 (Strong Dependencies)
- **DIRECTORY_README_RULE.md** - 目錄必須有 README，本規則定義 README 的命名
- **INTERNAL_RULE.md** - 定義 .internal/ 的檔案命名和結構

### 相關 (Related)
- **DRY_RULE.md** - 避免重複，命名應該清楚避免混淆
- **VIBE_GUIDE_SYNC_RULE.md** - 頂層文件命名影響 VIBE_GUIDE 引用

### 衝突 (Conflicts)
- ❌ 無已知衝突

---

**Created**: 2026-01-29  
**Last Updated**: 2026-02-01  
**Status**: ACTIVE  
**Priority**: HIGH  
**Enforcement**: MANDATORY
