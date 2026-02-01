# Git Automation Tools

**Git 自動化工具**

自動化常見的 Git 操作，包括提交、推送和 PR 創建。

---

## 📚 功能 (Features)

### 1. 自動提交 (Auto Commit)
```python
from agents.executor_agent.git_automation import GitAutomation

git = GitAutomation()

# 提交特定文件
result = git.auto_commit(
    files=['file1.py', 'file2.py'],
    message="feat: Add new feature"
)

# 提交所有變更
result = git.auto_commit(
    add_all=True,
    message="chore: Update documentation"
)
```

### 2. 推送分支 (Push Branch)
```python
# 推送當前分支
result = git.push_branch()

# 推送指定分支
result = git.push_branch(branch="feature/new-feature")

# 強制推送
result = git.push_branch(force=True)
```

### 3. 創建 PR (Create Pull Request)
```python
# 創建 PR (需要 GitHub CLI)
result = git.create_pr(
    title="feat: Add new feature",
    body="This PR adds...",
    base_branch="main"
)

# 創建草稿 PR
result = git.create_pr(
    title="WIP: Work in progress",
    draft=True
)
```

---

## 🚀 便捷函數 (Convenience Functions)

### 一鍵提交並推送
```python
from agents.executor_agent.git_automation import auto_commit_and_push

result = auto_commit_and_push(
    message="feat: Complete feature",
    add_all=True
)
```

### 創建功能 PR
```python
from agents.executor_agent.git_automation import create_feature_pr

result = create_feature_pr(
    feature_name="user authentication",
    description="Implement user login and registration"
)
```

---

## 📋 返回格式 (Return Format)

所有函數返回統一的字典格式：

```python
{
    'success': bool,      # 操作是否成功
    'errors': List[str],  # 錯誤訊息列表
    # ... 其他特定字段
}
```

### auto_commit 返回
```python
{
    'success': bool,
    'commit_hash': str,
    'files_committed': List[str],
    'errors': List[str]
}
```

### create_pr 返回
```python
{
    'success': bool,
    'pr_url': str,
    'pr_number': int,
    'errors': List[str]
}
```

---

## ⚙️ 前置需求 (Prerequisites)

### GitHub CLI (用於 PR 創建)
```bash
# Windows (使用 winget)
winget install --id GitHub.cli

# 驗證安裝
gh --version

# 登入 GitHub
gh auth login
```

---

## 🧪 測試 (Testing)

```bash
# 運行測試
python agents/executor_agent/tests/test_git_automation.py

# 或使用 pytest
pytest agents/executor_agent/tests/test_git_automation.py -v
```

---

## 📝 使用範例 (Examples)

### 範例 1: 完整的功能開發流程
```python
from agents.executor_agent.git_automation import GitAutomation

git = GitAutomation()

# 1. 提交變更
commit_result = git.auto_commit(
    add_all=True,
    message="feat: Implement user authentication"
)

if commit_result['success']:
    # 2. 推送到遠端
    push_result = git.push_branch()
    
    if push_result['success']:
        # 3. 創建 PR
        pr_result = git.create_pr(
            title="feat: User Authentication",
            body="Implements login and registration features"
        )
        
        if pr_result['success']:
            print(f"PR created: {pr_result['pr_url']}")
```

### 範例 2: 快速提交並推送
```python
from agents.executor_agent.git_automation import auto_commit_and_push

result = auto_commit_and_push(
    message="docs: Update README",
    add_all=True
)

if result['success']:
    print(f"Committed and pushed: {result['commit_hash']}")
else:
    print(f"Errors: {result['errors']}")
```

---

## 🔗 相關文檔 (Related Documentation)

- [Git Worktrees Guide](../../../docs/guides/GIT_WORKTREES_GUIDE.md)
- [Executor Agent](AGENT.md)
- [Workflow Integration](../../../rules/development/WORKFLOW_INTEGRATION_RULE.md)

---

**Created**: 2026-02-02  
**Version**: 1.0.0  
**Status**: Production Ready
