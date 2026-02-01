# GitHub Actions Workflows

**AI-Powered Automation for synthforge**

---

## 📋 Available Workflows

### 1. AI PR Review (`ai_pr_review.yml`)

**Trigger**: Pull requests (opened, synchronized, reopened)

**Purpose**: Automated AI code review for pull requests

**Features**:
- Reviews changed files using `reviewer_agent`
- Posts review comments on PR
- Runs tests
- Provides actionable feedback

**Usage**: Automatically runs on every PR

---

### 2. AI Issue Triage (`ai_issue_triage.yml`)

**Trigger**: Issues (opened, reopened)

**Purpose**: Automated issue classification and labeling

**Features**:
- Detects issue type (bug, feature, documentation)
- Assigns priority labels
- Suggests relevant workflows
- Provides triage recommendations

**Usage**: Automatically runs when issues are created

---

### 3. AI Code Analysis (`ai_code_analysis.yml`)

**Trigger**: 
- Push to main/develop
- Pull requests to main/develop
- Weekly schedule (Monday 00:00 UTC)

**Purpose**: Comprehensive code quality analysis

**Features**:
- Cyclomatic complexity analysis
- Maintainability index
- Linting (pylint)
- Test coverage
- Workflow validation
- Creates issues for critical findings (weekly)

**Usage**: Automatically runs on push/PR and weekly

---

## 🚀 Setup

### Prerequisites

1. **GitHub Repository**: Push synthforge to GitHub
2. **Permissions**: Ensure workflows have required permissions
3. **Dependencies**: Install required Python packages

### Installation

1. Push to GitHub:
```bash
git init
git add .
git commit -m "Initial commit with AI workflows"
git remote add origin <your-repo-url>
git push -u origin main
```

2. Enable GitHub Actions:
   - Go to repository Settings → Actions → General
   - Enable "Allow all actions and reusable workflows"

3. Configure Permissions:
   - Settings → Actions → General → Workflow permissions
   - Select "Read and write permissions"
   - Check "Allow GitHub Actions to create and approve pull requests"

---

## 📊 Workflow Details

### AI PR Review

**Steps**:
1. Checkout code
2. Set up Python
3. Install dependencies
4. Run AI code review on changed files
5. Comment PR with results
6. Run tests
7. Check review status

**Output**: PR comment with review results

---

### AI Issue Triage

**Steps**:
1. Checkout code
2. Set up Python
3. Analyze issue title and body
4. Determine type and priority
5. Add labels
6. Comment with triage results and suggestions

**Labels Added**:
- `bug`, `enhancement`, `documentation`
- `workflow`, `agent`, `skill`
- `priority: low/medium/high/critical`

---

### AI Code Analysis

**Steps**:
1. Checkout code
2. Set up Python
3. Run complexity analysis (radon)
4. Run linting (pylint)
5. Run tests with coverage
6. Validate workflows
7. Generate summary report
8. Upload artifacts
9. Comment on PR (if PR)
10. Create issue for critical findings (if scheduled)

**Artifacts**: 
- `code-analysis-report` (markdown + HTML coverage)

---

## 🔧 Customization

### Modify Review Criteria

Edit `.github/workflows/ai_pr_review.yml`:
```yaml
- name: Run AI Code Review
  run: |
    python agents/reviewer_agent/reviewer.py \
      --checks style,security,performance \
      $(cat changed_files.txt)
```

### Adjust Triage Logic

Edit `.github/workflows/ai_issue_triage.yml`:
```javascript
// Add custom label logic
if (title.includes('your-keyword')) {
  labels.push('your-label');
}
```

### Change Analysis Schedule

Edit `.github/workflows/ai_code_analysis.yml`:
```yaml
schedule:
  # Run daily at 02:00 UTC
  - cron: '0 2 * * *'
```

---

## 📝 Best Practices

### 1. Review Workflow Runs

Check Actions tab regularly:
- Monitor workflow success/failure
- Review analysis reports
- Address critical findings

### 2. Customize for Your Needs

Adjust workflows based on:
- Team size
- Project complexity
- Review requirements

### 3. Keep Dependencies Updated

Update Python packages:
```bash
pip install --upgrade pytest pytest-cov pylint radon
```

### 4. Monitor Costs

GitHub Actions has usage limits:
- Free tier: 2,000 minutes/month
- Monitor usage in Settings → Billing

---

## 🐛 Troubleshooting

### Workflow Fails

**Problem**: Workflow fails with "No module named 'xyz'"  
**Solution**: Add missing package to `requirements.txt` or install step

**Problem**: Permission denied  
**Solution**: Check workflow permissions in repository settings

### No Comments on PR

**Problem**: Workflow runs but doesn't comment  
**Solution**: Ensure "Read and write permissions" are enabled

### Analysis Report Too Long

**Problem**: Comment exceeds GitHub limit  
**Solution**: Report is automatically truncated; check artifacts for full report

---

## 📚 Related Documentation

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [synthforge Workflow System](../workflows/README.md)
- [Agent Documentation](../agents/README.md)

---

## ✅ Summary

These GitHub Actions workflows provide:
- ✅ Automated code review
- ✅ Intelligent issue triage
- ✅ Comprehensive code analysis
- ✅ Continuous quality monitoring

**All powered by synthforge AI agents!** 🤖

---

**Created**: 2026-02-01  
**Version**: 1.0.0  
**Status**: Production Ready
