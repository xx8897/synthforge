# VIBE_GUIDE_SYNC_RULE.md - VIBE_GUIDE 同步規則

**Status**: MANDATORY 強制  
**Priority**: CRITICAL 關鍵  
**Scope**: All structure changes

---

## 🎯 Core Strategy / 核心策略

**Option B**: VIBE_GUIDE 保持高階概覽，引用 ARCHITECTURE.md

VIBE_GUIDE maintains high-level overview, references ARCHITECTURE.md

---

## 📋 The Rule / 規則

### When to Update VIBE_GUIDE.md / 何時更新 VIBE_GUIDE

**ONLY update VIBE_GUIDE.md when**:
- New top-level directory added
- Major conceptual shift in workspace organization
- High-level categories change

**只在以下情況更新 VIBE_GUIDE.md**:
- 新增頂層目錄
- 工作區組織的重大概念轉變
- 高階分類變更

---

### When to Update ARCHITECTURE.md / 何時更新 ARCHITECTURE

**ALWAYS update ARCHITECTURE.md when**:
- Any directory added/removed/renamed
- Any file added/removed/renamed
- Any structural change

**始終更新 ARCHITECTURE.md 當**:
- 任何目錄新增/刪除/重新命名
- 任何檔案新增/刪除/重新命名
- 任何結構變更

---

## 🔄 Workflow / 工作流程

### Scenario 1: Add file in existing directory / 在現有目錄中新增檔案

**Example**: Add `devtools/security/auditor.py`

```
✅ Update: ARCHITECTURE.md (add file details)
❌ No need: VIBE_GUIDE.md (still shows devtools/)
```

---

### Scenario 2: Add subdirectory / 新增子目錄

**Example**: Add `devtools/security/`

```
✅ Update: ARCHITECTURE.md (complete structure)
❌ No need: VIBE_GUIDE.md (still shows devtools/)
```

---

### Scenario 3: Add top-level directory / 新增頂層目錄

**Example**: Add `rules/`

```
✅ Update: ARCHITECTURE.md (complete structure)
✅ Update: VIBE_GUIDE.md (add rules/ to high-level overview)
```

---

## 📊 What Each File Contains / 各檔案包含內容

### VIBE_GUIDE.md

**Content** / 內容:
- High-level overview (top-level directories only)
- Brief one-line descriptions
- Link to ARCHITECTURE.md for details

**高階概覽**:
- 只顯示頂層目錄
- 簡短的一行描述
- 連結到 ARCHITECTURE.md 查看詳情

**Example**:
```markdown
## 📊 Workspace Structure

**For detailed structure**: [ARCHITECTURE.md](docs/architecture/ARCHITECTURE.md)

### High-Level Overview:

```
synthforge/
├── 📄 Core Files (README, VIBE_GUIDE, Rules)
├── 📁 docs/          Documentation
├── 📁 devtools/      Development toolkit
├── 📁 rules/         All rules
└── 📁 projects/      User projects
```

**Complete directory tree**: See [ARCHITECTURE.md](docs/architecture/ARCHITECTURE.md)
```

---

### ARCHITECTURE.md

**Content** / 內容:
- Complete directory tree (all files)
- Detailed purpose of each component
- Dependencies
- Design decisions

**完整內容**:
- 完整目錄樹（所有檔案）
- 每個組件的詳細用途
- 依賴關係
- 設計決策

**Example**:
```markdown
## Directory Structure

### devtools/security/

**Purpose**: Security scanning tools with two levels

**Files**:
- `auditor.py`: Basic security checks (~300 lines)
- `advanced.py`: Deep vulnerability analysis (~500 lines)

**Dependencies**: bandit, semgrep

**Used by**: cli.py, release/cleaner.py

**Design Decision**: Separated basic and advanced to allow
quick scans without heavy dependencies.
```

---

## ✅ Checklist / 檢查清單

### When making structure changes / 進行結構變更時:

- [ ] Created/modified directory or file
- [ ] Added/updated README.md in directory (if new directory)
- [ ] Updated ARCHITECTURE.md with complete details
- [ ] Updated VIBE_GUIDE.md (only if top-level change)
- [ ] Verified structure tree is accurate
- [ ] Committed all changes together

---

## 🎯 Why Option B? / 為什麼選擇 Option B？

### 1. Maintainability / 可維護性

```
Most changes: Update 1 file (ARCHITECTURE.md)
Top-level changes: Update 2 files (both)

大部分變更：更新 1 個檔案
頂層變更：更新 2 個檔案
```

### 2. Consistency / 一致性

```
Single source of truth: ARCHITECTURE.md
VIBE_GUIDE references it

單一真相來源：ARCHITECTURE.md
VIBE_GUIDE 引用它
```

### 3. Scalability / 可擴展性

```
As project grows:
- VIBE_GUIDE stays concise
- ARCHITECTURE.md can expand

專案成長時：
- VIBE_GUIDE 保持簡潔
- ARCHITECTURE.md 可以擴展
```

### 4. Professionalism / 專業性

```
Follows best practices of large projects:
- Kubernetes
- Linux Kernel
- Rust

遵循大型專案最佳實踐
```

---

## 📝 Commit Message Template / 提交訊息模板

### For top-level changes:
```
feat(scope): add/remove/rename [directory]

- Created/Removed/Renamed [directory]
- Updated VIBE_GUIDE.md high-level overview
- Updated ARCHITECTURE.md with complete details
- Added README.md to [directory]
```

### For sub-level changes:
```
feat(scope): add/remove/rename [file/subdirectory]

- Created/Removed/Renamed [file/subdirectory]
- Updated ARCHITECTURE.md with details
- Added/Updated README.md in [directory]
```

---

## 🚨 Common Mistakes / 常見錯誤

### ❌ Mistake 1: Update VIBE_GUIDE for every change

```
Wrong: Add devtools/security/auditor.py
       → Update both VIBE_GUIDE and ARCHITECTURE

Correct: Add devtools/security/auditor.py
         → Update only ARCHITECTURE
```

### ❌ Mistake 2: Forget to update ARCHITECTURE

```
Wrong: Add rules/ directory
       → Only update VIBE_GUIDE

Correct: Add rules/ directory
         → Update both VIBE_GUIDE and ARCHITECTURE
```

### ❌ Mistake 3: Update in separate commits

```
Wrong:
  Commit 1: Add devtools/security/
  Commit 2: Update ARCHITECTURE.md (next day)

Correct:
  Commit 1: Add devtools/security/ + Update ARCHITECTURE.md
```

---

## 🎯 Summary / 總結

**Key Points**:

1. ✅ VIBE_GUIDE = High-level overview (top-level only)
2. ✅ ARCHITECTURE = Complete details (all files)
3. ✅ Most changes = Update ARCHITECTURE only
4. ✅ Top-level changes = Update both
5. ✅ Always commit together

**This rule ensures maintainability and consistency.**  
**此規則確保可維護性和一致性。**

---

**Created**: 2026-01-29  
**Status**: ACTIVE  
**Priority**: CRITICAL  
**Enforcement**: MANDATORY

---

## 🔗 相關規則 / Related Rules
- [DIRECTORY_README_RULE](DIRECTORY_README_RULE.md): 同樣需要同步架構變更
- [FILE_NAMING_CONVENTION_RULE](../development/FILE_NAMING_CONVENTION_RULE.md): 檔案命名影響架構
