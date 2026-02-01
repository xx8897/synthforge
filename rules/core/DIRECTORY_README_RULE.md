# Directory README Rule - 目錄 README 規則
# The Most Important Rule for Maintaining Code Integrity

**Status**: MANDATORY 強制執行  
**Priority**: CRITICAL 關鍵  
**Applies to**: ALL subdirectories 所有子目錄

---

## 🎯 核心原則 / Core Principle

> **Every directory MUST have a README.md that serves as the entry point and manifest for that directory.**

> **每個目錄都必須有一個 README.md 作為該目錄的入口點和清單。**

---

## 📋 規則詳細說明 / Rule Details

### Rule 1: 進入前必讀 / Read Before Enter

**When**: Before **viewing**, **using**, OR **modifying** ANY file in a subdirectory  
**Action**: MUST read the directory's README.md first

**何時**: 在**查看**、**使用**或**修改**子目錄中的任何檔案之前  
**動作**: 必須先閱讀該目錄的 README.md

**Triggers / 觸發條件**:
- ✅ **Viewing** / 查看：Opening a file to read
- ✅ **Using** / 使用：Importing or calling functions from a file
- ✅ **Modifying** / 修改：Editing, adding, or deleting files

**Example**:
```
❌ WRONG:
1. Open devtools/security_auditor.py
2. Start coding

✅ CORRECT:
1. Read devtools/README.md
2. Understand the tool's purpose and API
3. Then open devtools/security_auditor.py
```

---

### Rule 2: README 必須包含的內容 / Required Content

Every directory README.md MUST contain:

每個目錄的 README.md 必須包含：

#### 1. **File Manifest / 檔案清單**
List ALL files in the directory with brief descriptions.

列出目錄中的所有檔案及簡短描述。

```markdown
## Files / 檔案

| File | Purpose | Status |
|------|---------|--------|
| cli.py | Unified CLI interface | ✅ Complete |
| security_auditor.py | Basic security scanning | ✅ Complete |
| advanced_security.py | Deep security analysis | ✅ Complete |
```

#### 2. **Functionality Overview / 功能概覽**
Explain what this directory does.

解釋這個目錄的作用。

```markdown
## Purpose / 目的

This directory contains all development tools for synthforge.
本目錄包含 synthforge 的所有開發工具。
```

#### 3. **Dependencies / 依賴關係**
List dependencies between files in this directory.

列出此目錄中檔案之間的依賴關係。

```markdown
## Dependencies / 依賴

- cli.py → imports all other tools
- advanced_security.py → extends security_auditor.py
```

#### 4. **Usage / 使用方式**
How to use the files in this directory.

如何使用此目錄中的檔案。

```markdown
## Usage / 使用

```bash
python devtools/cli.py [command]
```
```

#### 5. **Last Updated / 最後更新**
Timestamp of last modification.

最後修改的時間戳記。

```markdown
**Last Updated**: 2026-01-29  
**Files**: 8  
**Status**: Active
```

---

### Rule 4: ARCHITECTURE.md 同步更新 / Sync ARCHITECTURE.md

**CRITICAL**: When directory structure changes, MUST update ARCHITECTURE.md

**關鍵**: 當目錄結構變更時，必須更新 ARCHITECTURE.md

#### Triggers for ARCHITECTURE Update / 觸發 ARCHITECTURE 更新的情況:

1. ✅ **New directory added** / 新增目錄
   - Add to directory tree in ARCHITECTURE.md
   - Explain purpose of new directory
   - Update component diagram if applicable

2. ✅ **Directory deleted** / 刪除目錄
   - Remove from directory tree
   - Update affected diagrams
   - Document reason for removal

3. ✅ **Directory renamed** / 重新命名目錄
   - Update all references in ARCHITECTURE.md
   - Update navigation paths
   - Update examples

4. ✅ **Directory moved** / 移動目錄
   - Update directory tree structure
   - Update all path references
   - Update component relationships

5. ✅ **Major functionality change** / 主要功能變更
   - Update component descriptions
   - Update interaction diagrams
   - Update design decisions section

**Location**: `docs/architecture/ARCHITECTURE.md`

**Example**:
```markdown
# Before adding devtools/security/
synthforge/
├── devtools/
│   ├── cli.py
│   └── security_auditor.py

# After adding devtools/security/
synthforge/
├── devtools/
│   ├── cli.py
│   └── security/          ← NEW: Update ARCHITECTURE.md
│       ├── README.md
│       ├── auditor.py
│       └── advanced.py
```

---

### Rule 5: Projects 獨立架構 / Independent Project Architecture

**IMPORTANT**: Each project in `projects/` is its own root with the same rules.

**重要**: `projects/` 中的每個專案都是獨立的根目錄，遵循相同規則。

#### Project Structure / 專案結構:

```
projects/my_app/              ← Independent root
├── README.md                 ← Project overview
├── ARCHITECTURE.md           ← Project architecture
├── src/
│   └── README.md             ← Must have!
├── tests/
│   └── README.md             ← Must have!
├── docs/
│   └── README.md             ← Must have!
└── reports/
    └── README.md             ← Must have!
```

#### Rules Apply to Projects / 規則適用於專案:

1. ✅ **Directory README Rule** applies
   - Every subdirectory in project has README.md
   - Read before enter, update after modify

2. ✅ **ARCHITECTURE.md** applies
   - Each project has its own ARCHITECTURE.md
   - Update when project structure changes

3. ✅ **Independence** principle
   - Project does NOT depend on synthforge devtools at runtime
   - Project can be distributed independently
   - Project has its own git repo (optional)

**Example Project**:
```
projects/my_fastapi_app/
├── README.md                 ← "My FastAPI Application"
├── ARCHITECTURE.md           ← Project-specific architecture
├── src/
│   ├── README.md             ← "Source code directory"
│   ├── main.py
│   ├── api/
│   │   ├── README.md         ← "API endpoints"
│   │   └── routes.py
│   └── models/
│       ├── README.md         ← "Data models"
│       └── user.py
├── tests/
│   ├── README.md             ← "Test suite"
│   └── test_api.py
└── reports/                  ← Auto-generated by devtools
    ├── README.md             ← "Tool outputs"
    └── security_scan_2026-01-29.txt
```

---

### Rule 6: 修改時必須同步更新 / Sync on Modification

**CRITICAL**: When ANY file in a directory changes, the README.md MUST be updated.

**關鍵**: 當目錄中的任何檔案發生變化時，README.md 必須更新。

#### Triggers for README Update / 觸發 README 更新的情況:

1. ✅ **New file added** / 新增檔案
   - Add to file manifest
   - Update file count
   - Update last modified date

2. ✅ **File deleted** / 刪除檔案
   - Remove from manifest
   - Update file count
   - Update last modified date

3. ✅ **File renamed** / 重新命名檔案
   - Update manifest entry
   - Update dependencies if affected
   - Update last modified date

4. ✅ **Functionality changed** / 功能變更
   - Update file description
   - Update usage examples if affected
   - Update last modified date

5. ✅ **Dependencies changed** / 依賴變更
   - Update dependency graph
   - Update last modified date

---

### Rule 4: README 模板 / README Template

Use this template for all directory READMEs:

所有目錄 README 使用此模板：

```markdown
# [Directory Name] - [Purpose]

**Purpose**: [One-line description]  
**Files**: [Count]  
**Last Updated**: [Date]

---

## 📁 Files / 檔案

| File | Purpose | Status | Lines |
|------|---------|--------|-------|
| file1.py | Description | ✅ Complete | ~500 |
| file2.py | Description | ⏳ In Progress | ~300 |

---

## 🎯 Purpose / 目的

[Detailed explanation of what this directory does]

---

## 🔗 Dependencies / 依賴關係

### Internal Dependencies:
- file1.py → file2.py

### External Dependencies:
- Requires: package1, package2

---

## 📖 Usage / 使用方式

```bash
[Usage examples]
```

---

## 🏗️ Architecture / 架構

[Diagram or explanation of how files relate]

---

## 📝 Notes / 注意事項

[Any important notes or warnings]

---

**Created**: [Date]  
**Last Updated**: [Date]  
**Maintainer**: synthforge team
```

---

## 🔄 工作流程 / Workflow

### For AI Agents / 給 AI 代理:

```
1. User asks to work on file in subdirectory
   使用者要求處理子目錄中的檔案
   ↓
2. STOP! Read [subdirectory]/README.md FIRST
   停！先閱讀 [子目錄]/README.md
   ↓
3. Understand:
   理解：
   - What files exist / 存在哪些檔案
   - How they relate / 它們如何關聯
   - What dependencies exist / 存在哪些依賴
   ↓
4. NOW you can work on the file
   現在可以處理檔案
   ↓
5. After modification:
   修改後：
   - Update the file / 更新檔案
   - Update README.md / 更新 README.md
   - Update last modified date / 更新最後修改日期
```

---

## 📊 Example: devtools/ Directory

### Before (Bad) / 之前（不好）:
```
devtools/
├── cli.py
├── security_auditor.py
├── advanced_security.py
└── ... (8 files total)
```

**Problem**: No manifest, hard to know what exists  
**問題**: 沒有清單，難以知道存在什麼

### After (Good) / 之後（好）:
```
devtools/
├── README.md          ← ENTRY POINT (lists all 8 files)
├── cli.py
├── security_auditor.py
├── advanced_security.py
└── ... (8 files total)
```

**Benefit**: README.md tells you everything  
**好處**: README.md 告訴你一切

---

## ✅ Enforcement / 執行

### Checklist for Every Code Change / 每次程式碼變更的檢查清單:

- [ ] Did I read the directory README.md first?
      我是否先閱讀了目錄的 README.md？

- [ ] Did I modify any file?
      我是否修改了任何檔案？

- [ ] Did I update the README.md to reflect changes?
      我是否更新了 README.md 以反映變更？

- [ ] Did I update the "Last Updated" date?
      我是否更新了「最後更新」日期？

- [ ] Are all file descriptions accurate?
      所有檔案描述是否準確？

---

## 🎯 Why This Rule is CRITICAL / 為什麼此規則至關重要

### Problem Without This Rule / 沒有此規則的問題:

1. **Lost Context** / 失去上下文
   - Modify file A, forget it affects file B
   - 修改檔案 A，忘記它影響檔案 B

2. **Broken Dependencies** / 破壞依賴
   - Change function signature, don't update callers
   - 更改函數簽名，不更新呼叫者

3. **Orphaned Files** / 孤立檔案
   - Files exist but nobody knows their purpose
   - 檔案存在但沒人知道其目的

4. **Duplicate Work** / 重複工作
   - Create new file that already exists
   - 創建已存在的新檔案

### Solution With This Rule / 有此規則的解決方案:

1. **Strong Coupling** / 強耦合
   - README.md forces you to see the big picture
   - README.md 強制你看到全局

2. **Change Tracking** / 變更追蹤
   - Every change is documented
   - 每個變更都被記錄

3. **Discoverability** / 可發現性
   - Easy to find what you need
   - 容易找到你需要的

4. **Consistency** / 一致性
   - All directories follow same pattern
   - 所有目錄遵循相同模式

---

## 📝 Implementation Plan / 實施計劃

### Phase 1: Create READMEs for Existing Directories
為現有目錄創建 README

- [ ] devtools/README.md (update existing)
- [ ] devtools/analyzers/README.md (exists, verify compliance)
- [ ] docs/README.md (new)
- [ ] docs/guides/README.md (new)
- [ ] docs/architecture/README.md (new)
- [ ] docs/planning/README.md (new)
- [ ] docs/strategies/README.md (new)
- [ ] docs/sessions/README.md (new)

### Phase 2: Enforce Rule in VIBE_GUIDE.md
在 VIBE_GUIDE.md 中執行規則

- [ ] Add to "Core Principles"
- [ ] Add to "For AI Agents: Decision Tree"
- [ ] Make it prominent

### Phase 3: Create Automated Checker (Future)
創建自動檢查器（未來）

- [ ] Script to verify all directories have README.md
- [ ] Script to check if README.md is up to date
- [ ] CI/CD integration

---

## 🚨 Violation Examples / 違規範例

### ❌ BAD: Modify without updating README
```
1. Edit devtools/cli.py
2. Add new command
3. Commit
4. (README.md still shows old command list)
```

### ✅ GOOD: Update README with changes
```
1. Read devtools/README.md
2. Edit devtools/cli.py
3. Add new command
4. Update devtools/README.md:
   - Add command to list
   - Update usage examples
   - Update last modified date
5. Commit both files
```

---

## 🎓 Best Practices / 最佳實踐

1. **Keep README.md at top of directory listing**
   - Name it README.md (uppercase) so it appears first
   - 命名為 README.md（大寫）使其首先出現

2. **Use tables for file manifests**
   - Easy to scan visually
   - 易於視覺掃描

3. **Include file size/line count**
   - Helps understand complexity
   - 幫助理解複雜度

4. **Link to related docs**
   - Cross-reference where appropriate
   - 適當時交叉引用

5. **Keep it updated**
   - Stale README is worse than no README
   - 過時的 README 比沒有 README 更糟

---

## 📚 Related Rules / 相關規則

- **VIBE_GUIDE.md**: Overall navigation
- **AGENT_RULES.md**: Agent behavior
- **DOC_GUIDE.md**: Documentation format

---

**This rule is NON-NEGOTIABLE.**  
**此規則不可協商。**

**Violating this rule WILL lead to broken code and lost context.**  
**違反此規則將導致程式碼損壞和上下文丟失。**

**ALWAYS read README.md before entering a directory.**  
**進入目錄前始終閱讀 README.md。**

**ALWAYS update README.md after modifying files.**  
**修改檔案後始終更新 README.md。**

---

## 📚 相關規則 / Related Rules

### 強依賴 (Strong Dependencies)
- **VIBE_GUIDE_SYNC_RULE.md** - VIBE_GUIDE 引用目錄 README
- **FILE_NAMING_CONVENTION_RULE.md** - README 檔案命名規範

### 相關 (Related)
- **VIBE_GUIDE.md** - 強連結到所有目錄 README
- **ARCHITECTURE.md** - 目錄結構變更時必須同步更新

### 衝突 (Conflicts)
- ❌ 無已知衝突

---

**Created**: 2026-01-29  
**Last Updated**: 2026-02-01  
**Status**: ACTIVE  
**Priority**: CRITICAL  
**Enforcement**: MANDATORY
