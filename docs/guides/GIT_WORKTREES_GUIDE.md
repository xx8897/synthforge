# Git Worktrees Guide

**Git Worktrees 使用指南**

---

## 📋 What are Git Worktrees?

**Git Worktrees** allow you to have multiple working directories attached to the same repository, enabling parallel development on different branches without switching contexts.

**Git Worktrees** 允許您在同一個倉庫中擁有多個工作目錄，實現在不同分支上並行開發而無需切換上下文。

---

## 🎯 Why Use Git Worktrees?

### Benefits

1. **Parallel Development**: Work on multiple features/fixes simultaneously
2. **Context Preservation**: Each worktree maintains its own state
3. **No Stashing**: No need to stash changes when switching tasks
4. **Isolated Testing**: Test different branches independently
5. **CI/CD Friendly**: Run tests on multiple branches concurrently

### Use Cases

- 🔧 **Feature Development**: Develop new feature while fixing urgent bugs
- 🐛 **Bug Fixes**: Fix bugs without interrupting current work
- 🧪 **Testing**: Test different versions simultaneously
- 📊 **Code Review**: Review PRs without affecting current branch

---

## 🚀 Quick Start

### Using synthforge's Git Worktree Manager

```python
from core_lib.git.worktree import GitWorktreeManager

# Initialize manager
manager = GitWorktreeManager()

# Create a new worktree
result = manager.create_worktree(
    branch_name='feature/new-feature',
    base_branch='main'
)

print(f"Worktree created at: {result['worktree_path']}")

# Work in the worktree...

# Cleanup when done
manager.cleanup_worktree(result['worktree_path'])
```

### Using Git CLI

```bash
# Create worktree
git worktree add ../feature-branch feature/new-feature

# List worktrees
git worktree list

# Remove worktree
git worktree remove ../feature-branch
```

---

## 📚 GitWorktreeManager API

### Creating Worktrees

```python
result = manager.create_worktree(
    branch_name='feature/my-feature',  # Required: New branch name
    base_branch='main',                # Optional: Base branch (default: 'main')
    worktree_dir='/custom/path'        # Optional: Custom directory
)

# Returns:
{
    'success': True,
    'worktree_path': '/path/to/worktree',
    'branch_name': 'feature/my-feature',
    'errors': []
}
```

### Listing Worktrees

```python
result = manager.list_worktrees()

# Returns:
{
    'success': True,
    'worktrees': [
        {
            'path': '/path/to/worktree1',
            'branch': 'refs/heads/feature/branch1',
            'head': 'abc123...'
        },
        {
            'path': '/path/to/worktree2',
            'branch': 'refs/heads/bugfix/issue-42',
            'head': 'def456...'
        }
    ],
    'errors': []
}
```

### Cleaning Up Worktrees

```python
result = manager.cleanup_worktree(
    worktree_path='/path/to/worktree',
    force=False  # Force removal even with uncommitted changes
)

# Returns:
{
    'success': True,
    'removed': True,
    'errors': []
}
```

### Pruning Stale Worktrees

```python
result = manager.prune_worktrees()

# Returns:
{
    'success': True,
    'pruned': 2,  # Number of pruned worktrees
    'errors': []
}
```

---

## 🔄 Integration with Executor Agent

The `executor_agent` automatically uses Git Worktrees when configured:

### Configuration

Edit `agents/executor_agent/config.yml`:

```yaml
git:
  use_worktrees: true
  worktree_base_dir: .worktrees
  auto_cleanup: true
```

### Workflow Usage

```yaml
# In workflow
phases:
  execute:
    - agent: executor_agent
      action: implement_tasks
      config:
        use_worktree: true
        branch_name: feature/auto-generated
```

**Behavior**:
1. Creates worktree in `.worktrees/feature_auto-generated/`
2. Implements tasks in isolated environment
3. Commits changes to worktree branch
4. Optionally cleans up worktree after completion

---

## 📋 Best Practices

### 1. Organize Worktrees

```bash
# Create worktrees in dedicated directory
.worktrees/
├── feature_new-ui/
├── bugfix_issue-123/
└── hotfix_critical-bug/
```

### 2. Naming Conventions

```python
# Good: Descriptive branch names
manager.create_worktree('feature/user-authentication')
manager.create_worktree('bugfix/login-error')
manager.create_worktree('hotfix/security-patch')

# Bad: Unclear names
manager.create_worktree('test')
manager.create_worktree('temp')
```

### 3. Clean Up Regularly

```python
# Prune stale worktrees weekly
manager.prune_worktrees()

# Remove completed worktrees
for worktree in completed_worktrees:
    manager.cleanup_worktree(worktree['path'])
```

### 4. Avoid Conflicts

```python
# Check if worktree exists before creating
result = manager.list_worktrees()
existing_branches = [w['branch'] for w in result['worktrees']]

if 'feature/my-feature' not in existing_branches:
    manager.create_worktree('feature/my-feature')
```

---

## 🚨 Common Issues

### Issue 1: Worktree Already Exists

**Problem**: Trying to create worktree that already exists

**Solution**:
```python
# Check first
result = manager.list_worktrees()
if worktree_path not in [w['path'] for w in result['worktrees']]:
    manager.create_worktree(branch_name)
```

### Issue 2: Branch Already Checked Out

**Problem**: Branch is already checked out in another worktree

**Solution**:
```bash
# Use different branch name or remove existing worktree
git worktree remove /path/to/existing
```

### Issue 3: Uncommitted Changes

**Problem**: Cannot remove worktree with uncommitted changes

**Solution**:
```python
# Force removal
manager.cleanup_worktree(worktree_path, force=True)

# Or commit changes first
# cd /path/to/worktree
# git add .
# git commit -m "Save changes"
```

---

## 🎯 Advanced Usage

### Parallel Testing

```python
# Create worktrees for different test scenarios
test_branches = ['test/scenario-1', 'test/scenario-2', 'test/scenario-3']

for branch in test_branches:
    result = manager.create_worktree(branch, base_branch='develop')
    # Run tests in each worktree concurrently
```

### Feature Comparison

```python
# Compare two feature implementations
manager.create_worktree('feature/approach-a', base_branch='main')
manager.create_worktree('feature/approach-b', base_branch='main')

# Implement different approaches in each worktree
# Compare results and choose best approach
```

### Hotfix Workflow

```python
# Create hotfix worktree from production
result = manager.create_worktree('hotfix/critical-bug', base_branch='production')

# Fix bug in worktree
# Test thoroughly
# Merge to production

# Cleanup
manager.cleanup_worktree(result['worktree_path'])
```

---

## 📊 Worktree Lifecycle

```
1. Create Worktree
   ↓
2. Switch to Worktree Directory
   ↓
3. Make Changes
   ↓
4. Commit Changes
   ↓
5. Push Branch (optional)
   ↓
6. Merge/PR
   ↓
7. Cleanup Worktree
   ↓
8. Prune (if needed)
```

---

## 🔗 Related Documentation

- [Git Worktree Official Docs](https://git-scm.com/docs/git-worktree)
- [Executor Agent Documentation](../agents/executor_agent/AGENT.md)
- [Workflow Integration](../workflows/README.md)

---

## ✅ Summary

Git Worktrees enable:
- ✅ Parallel development
- ✅ Context preservation
- ✅ Isolated testing
- ✅ Efficient workflows

**Use synthforge's `GitWorktreeManager` for easy worktree management!**

---

**Created**: 2026-02-01  
**Version**: 1.0.0  
**Status**: Production Ready
