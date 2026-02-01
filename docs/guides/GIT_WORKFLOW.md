# Git Workflow Guide
# Git 工作流程指南

**Version**: 1.0  
**Last Updated**: 2026-02-02  
**Author**: xx8897

---

## 🎯 Overview / 概覽

synthforge uses a **Feature Branch Workflow** with **Git Worktrees** to maintain a clean, isolated development environment.

synthforge 使用**功能分支工作流程**和 **Git Worktrees** 來維護乾淨、隔離的開發環境。

---

## ⚡ Quick Start: Do I Need `git add`? / 快速開始：我需要 `git add` 嗎？

### Short Answer / 簡短回答

**NO, if you use `-a` parameter!** / **不需要，如果您使用 `-a` 參數！**

```bash
# This command does BOTH git add AND git commit
# 這個命令同時執行 git add 和 git commit
python devtools/cli.py git commit -m "your message" -a
```

### Detailed Explanation / 詳細說明

#### With `-a` Parameter (Recommended) / 使用 `-a` 參數（推薦）⭐

```bash
# One command does everything
# 一個命令完成所有操作
python devtools/cli.py git commit -m "feat: add new feature" -a

# Equivalent to / 等同於:
git add -A                              # Stage all changes
git commit -m "feat: add new feature"   # Commit
```

**What `-a` does / `-a` 的作用**:
- ✅ Automatically stages ALL modified files / 自動暫存所有已修改的文件
- ✅ Automatically stages ALL deleted files / 自動暫存所有已刪除的文件
- ✅ Then commits them / 然後提交它們
- ⚠️ Does NOT stage new untracked files / 不會暫存新的未追蹤文件

#### Without `-a` Parameter / 不使用 `-a` 參數

```bash
# You MUST manually add files first
# 您必須先手動添加文件
git add file1.py file2.md
python devtools/cli.py git commit -m "feat: specific changes"
```

### Comparison Table / 對比表

| Scenario | Need `git add`? | Command |
|----------|-----------------|---------|
| **Commit all changes** | ❌ NO | `python devtools/cli.py git commit -m "msg" -a` |
| **Commit specific files** | ✅ YES | `git add file.py` → `python devtools/cli.py git commit -m "msg"` |
| **Using native git** | ❌ NO | `git commit -am "msg"` |
| **Using native git** | ✅ YES | `git add .` → `git commit -m "msg"` |

### When to Use Each / 何時使用

#### Use `-a` (Most Common) / 使用 `-a`（最常見）⭐

```bash
# Daily development - commit everything
# 日常開發 - 提交所有變更
python devtools/cli.py git commit -m "feat: implement user login" -a
```

**Best for / 最適合**:
- Regular development / 日常開發
- When you want to commit all your changes / 想提交所有變更時
- Quick iterations / 快速迭代

#### Don't Use `-a` (Selective Commits) / 不使用 `-a`（選擇性提交）

```bash
# Only commit specific files
# 只提交特定文件
git add src/auth.py
git add tests/test_auth.py
python devtools/cli.py git commit -m "feat: add authentication"
```

**Best for / 最適合**:
- Committing only part of your changes / 只提交部分變更
- Separating concerns into multiple commits / 將關注點分成多個提交
- When you have unrelated changes / 有不相關的變更時

### Important Notes / 重要提示

⚠️ **New Files (Untracked)** / **新文件（未追蹤）**

```bash
# If you created a NEW file, -a won't add it
# 如果您創建了新文件，-a 不會添加它

# You must add new files manually first
# 您必須先手動添加新文件
git add new_file.py
python devtools/cli.py git commit -m "feat: add new module" -a
```

✅ **Modified Files** / **已修改的文件**

```bash
# -a automatically handles modified files
# -a 自動處理已修改的文件
python devtools/cli.py git commit -m "fix: update logic" -a
```

---

## 🤖 Smart Git Operations / 智慧 Git 操作 ⭐ New!

synthforge now includes intelligent Git analysis to automate your workflow. / synthforge 現在包含智慧 Git 分析以自動化您的工作流程。

### Smart Commit / 智慧提交

Automatically analyze your changes and suggest the correct commit type (feat, fix, docs, etc.). / 自動分析您的變更並建議正確的提交類型。

```bash
# Analyze and commit (with auto-staging)
# 分析並提交（包含自動暫存）
python devtools/cli.py git commit -s -a
```

**What it does / 它的作用**:
- 🔍 **Analyzes files**: Detects if you changed core logic, tests, or docs.
- 💡 **Suggests type**: Prepends `feat:`, `fix:`, `docs:`, etc. automatically.
- 🚀 **One-command**: Stages, generates message, and commits.

### Smart Tagging / 智慧標籤

Automatically calculate and apply the next version tag (SemVer) based on your commit history. / 根據您的提交歷史自動計算並應用下一個版本標籤（SemVer）。

```bash
# Automatically determine and apply next tag (v1.0.1, v1.1.0, etc.)
# 自動確定並應用下一個標籤
python devtools/cli.py git tag --auto
```

**Rules / 規則**:
- 🆕 **Minor (0.x.0)**: Automatic if new `feat:` commits are found.
- 🐞 **Patch (0.0.x)**: Automatic for `fix:`, `docs:`, or `chore:` commits.
- ⚠️ **Major (x.0.0)**: Triggered if `BREAKING CHANGE` or `BC:` is found in commit messages.

---

## 🌳 What are Git Worktrees? / 什麼是 Git Worktrees？

**Git Worktrees** allow you to have multiple working directories from the same repository simultaneously.

**Git Worktrees** 允許您同時從同一個儲存庫擁有多個工作目錄。

### Benefits / 優點

- ✅ **Isolation**: Each feature in its own directory / 每個功能都在自己的目錄中
- ✅ **Clean Main Branch**: Never pollute main with WIP / 永不污染主分支
- ✅ **Parallel Work**: Work on multiple features simultaneously / 同時處理多個功能
- ✅ **Easy Context Switching**: No stashing required / 無需暫存

### Example / 範例

```
synthforge/                    ← Main repository (master branch)
├── .worktrees/
│   ├── feature_user_auth/     ← Worktree for feature/user-auth
│   └── bugfix_login_error/    ← Worktree for bugfix/login-error
```

---

## 🚀 Daily Workflow / 日常工作流程

### Option 1: Automated Workflow (Recommended) / 選項 1：自動化工作流程（推薦）

```bash
# Start a new feature with full automation
# 使用完全自動化開始新功能
python devtools/cli.py workflow run workflows/templates/feature_development.yml

# This will:
# 1. Ask for feature name
# 2. Create feature branch
# 3. Set up Git worktree
# 4. Guide you through TDD implementation
# 5. Run tests automatically
# 6. Create PR when done
```

### Option 2: Manual Workflow / 選項 2：手動工作流程

#### Step 1: Create Feature Branch / 步驟 1：創建功能分支

```bash
# Create and checkout new branch
git checkout -b feature/user-authentication

# Or use CLI helper
python devtools/cli.py git branch feature/user-authentication
```

#### Step 2: Make Changes / 步驟 2：進行變更

```bash
# Edit files
# 編輯文件

# Check status
git status

# Or use CLI
python devtools/cli.py git status
```

#### Step 3: Commit Changes / 步驟 3：提交變更

```bash
# Stage and commit
git add .
git commit -m "feat: add user authentication"

# Or use CLI (recommended - follows commit conventions)
python devtools/cli.py git commit -m "feat: add user authentication" -a
```

#### Step 4: Push to Remote / 步驟 4：推送到遠端

```bash
# Push branch
git push -u origin feature/user-authentication

# Or use CLI
python devtools/cli.py git push
```

#### Step 5: Create Pull Request / 步驟 5：創建 Pull Request

```bash
# Using GitHub CLI (if installed)
gh pr create --title "Add User Authentication" --body "Implements login/logout"

# Or use synthforge CLI
python devtools/cli.py git pr --title "Add User Authentication" --body "Implements login/logout"

# Or manually on GitHub web interface
# 或在 GitHub 網頁介面手動操作
```

#### Step 6: After Merge / 步驟 6：合併後

```bash
# Switch back to main
git checkout master

# Pull latest changes
git pull origin master

# Delete feature branch
git branch -d feature/user-authentication

# Delete remote branch (if not auto-deleted)
git push origin --delete feature/user-authentication
```

---

## 🔧 Git Worktree Commands / Git Worktree 命令

### Create Worktree / 創建 Worktree

```bash
# Create worktree for new feature
git worktree add .worktrees/feature_name -b feature/feature-name

# Or use synthforge automation
python -c "from core_lib.git.worktree import GitWorktreeManager; \
           manager = GitWorktreeManager(); \
           result = manager.create_worktree('feature/feature-name'); \
           print(result)"
```

### List Worktrees / 列出 Worktrees

```bash
# List all worktrees
git worktree list

# Or use Python
python -c "from core_lib.git.worktree import GitWorktreeManager; \
           manager = GitWorktreeManager(); \
           result = manager.list_worktrees(); \
           print(result)"
```

### Remove Worktree / 移除 Worktree

```bash
# Remove worktree
git worktree remove .worktrees/feature_name

# Or use Python
python -c "from core_lib.git.worktree import GitWorktreeManager; \
           manager = GitWorktreeManager(); \
           result = manager.cleanup_worktree('.worktrees/feature_name'); \
           print(result)"
```

### Prune Stale Worktrees / 清理過期 Worktrees

```bash
# Clean up stale worktree references
git worktree prune

# Or use Python
python -c "from core_lib.git.worktree import GitWorktreeManager; \
           manager = GitWorktreeManager(); \
           result = manager.prune_worktrees(); \
           print(result)"
```

---

## 📝 Commit Message Conventions / 提交訊息規範

synthforge follows **Conventional Commits** specification.

synthforge 遵循 **Conventional Commits** 規範。

### Format / 格式

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types / 類型

- `feat`: New feature / 新功能
- `fix`: Bug fix / 錯誤修復
- `docs`: Documentation only / 僅文件
- `style`: Code style (formatting, etc.) / 代碼風格
- `refactor`: Code refactoring / 代碼重構
- `test`: Add or update tests / 添加或更新測試
- `chore`: Maintenance tasks / 維護任務

### Examples / 範例

```bash
# Good commits / 好的提交
git commit -m "feat: add user login functionality"
git commit -m "fix: resolve authentication token expiry issue"
git commit -m "docs: update API documentation"
git commit -m "refactor: simplify user service logic"

# Bad commits / 不好的提交
git commit -m "update"
git commit -m "fix bug"
git commit -m "changes"
```

---

## 🔄 Branch Strategy / 分支策略

### Branch Types / 分支類型

1. **master** (or **main**)
   - Production-ready code / 生產就緒代碼
   - Always stable / 始終穩定
   - Protected branch / 受保護分支

2. **feature/***
   - New features / 新功能
   - Branch from: `master`
   - Merge to: `master`
   - Example: `feature/user-authentication`

3. **bugfix/***
   - Bug fixes / 錯誤修復
   - Branch from: `master`
   - Merge to: `master`
   - Example: `bugfix/login-error`

4. **hotfix/***
   - Urgent production fixes / 緊急生產修復
   - Branch from: `master`
   - Merge to: `master`
   - Example: `hotfix/security-patch`

5. **refactor/***
   - Code refactoring / 代碼重構
   - Branch from: `master`
   - Merge to: `master`
   - Example: `refactor/user-service`

### Branch Naming / 分支命名

```bash
# Good names / 好的命名
feature/user-authentication
bugfix/login-timeout
hotfix/security-vulnerability
refactor/database-queries

# Bad names / 不好的命名
feature/new-stuff
fix
update
my-branch
```

---

## 🛡️ Best Practices / 最佳實踐

### 1. Commit Often / 經常提交

```bash
# Make small, atomic commits
# 進行小型、原子性的提交

# Good: Multiple small commits
git commit -m "feat: add login form"
git commit -m "feat: add login validation"
git commit -m "feat: add login API integration"

# Bad: One huge commit
git commit -m "feat: add entire login system"
```

### 2. Write Meaningful Messages / 撰寫有意義的訊息

```bash
# Good / 好
git commit -m "fix: resolve null pointer exception in user service"

# Bad / 不好
git commit -m "fix bug"
```

### 3. Pull Before Push / 推送前先拉取

```bash
# Always pull latest changes before pushing
# 推送前始終拉取最新變更
git pull origin master
git push origin feature/my-feature
```

### 4. Use Worktrees for Isolation / 使用 Worktrees 進行隔離

```bash
# Instead of switching branches
# 而不是切換分支
git checkout feature/new-feature

# Use worktrees
# 使用 worktrees
git worktree add .worktrees/new_feature -b feature/new-feature
cd .worktrees/new_feature
```

### 5. Clean Up After Merge / 合併後清理

```bash
# After PR is merged
# PR 合併後
git checkout master
git pull
git branch -d feature/my-feature
git worktree remove .worktrees/my_feature
```

---

## 🚨 Common Issues / 常見問題

### Issue 1: Merge Conflicts / 合併衝突

```bash
# Pull latest changes
git pull origin master

# Resolve conflicts in your editor
# 在編輯器中解決衝突

# Mark as resolved
git add .
git commit -m "fix: resolve merge conflicts"
```

### Issue 2: Forgot to Create Branch / 忘記創建分支

```bash
# If you made changes on master
# 如果您在 master 上進行了變更

# Create new branch with current changes
git checkout -b feature/my-feature

# Your changes are now on the new branch
# 您的變更現在在新分支上
```

### Issue 3: Need to Switch Context / 需要切換上下文

```bash
# Instead of stashing
# 而不是暫存

# Use worktrees for parallel work
git worktree add .worktrees/urgent_fix -b hotfix/urgent-fix
cd .worktrees/urgent_fix
# Work on urgent fix
# 處理緊急修復
```

---

## 📊 Git Status Check / Git 狀態檢查

```bash
# Check current status
git status

# Check commit history
git log --oneline -10

# Check branches
git branch -a

# Check worktrees
git worktree list

# Or use synthforge CLI for all-in-one
python devtools/cli.py git status
```

---

## 🔗 Useful Resources / 有用資源

- [Git Documentation](https://git-scm.com/doc)
- [Git Worktrees Guide](https://git-scm.com/docs/git-worktree)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

---

**Happy Coding! / 編碼愉快！** 🚀
