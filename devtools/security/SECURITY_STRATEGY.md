# Security Scanning Strategy
# 安全掃描策略

## Scan Modes / 掃描模式

### 🚀 Quick Scan (快速掃描)
**Time**: ~5 seconds  
**Tools**: Basic Security Auditor only  
**Use Case**: Pre-commit checks, rapid feedback

**Detects**:
- API keys leakage
- Hardcoded passwords
- Absolute paths
- Sensitive files

**Command**:
```bash
python devtools/cli.py check projects/my_app --security
```

---

### 🔬 Deep Scan (深度掃描)
**Time**: ~30-60 seconds  
**Tools**: Advanced Security Scanner (Bandit + Semgrep + Custom Rules)  
**Use Case**: Pre-release, CI/CD pipeline

**Detects**:
- All Quick Scan items
- SQL Injection
- Command Injection
- XSS vulnerabilities
- CSRF issues
- Authentication bypass
- Authorization flaws
- IDOR
- Path traversal
- Business logic errors
- Race conditions

**Command**:
```bash
python devtools/cli.py check projects/my_app --security --deep
```

---

### 🤖 AI-Assisted Scan (AI 輔助掃描)
**Time**: ~2-5 minutes  
**Tools**: Deep Scan + LLM Analysis  
**Use Case**: Critical releases, security audit

**Additional Features**:
- Semantic code understanding
- Context-aware vulnerability detection
- Custom business logic analysis
- Remediation suggestions

**Command**:
```bash
python devtools/cli.py check projects/my_app --security --ai
```

**Requires**: OpenAI/Anthropic API key

---

## Implementation / 實作

### CLI Integration:
```python
@cli.command()
@click.option('--quick', is_flag=True, help='Quick scan (5s)')
@click.option('--deep', is_flag=True, help='Deep scan (30-60s)')
@click.option('--ai', is_flag=True, help='AI-assisted scan (2-5min)')
def security_scan(project_path, quick, deep, ai):
    if ai:
        # Run all layers including AI
        run_advanced_scan(project_path, use_ai=True)
    elif deep:
        # Run Bandit + Semgrep + Custom rules
        run_advanced_scan(project_path, use_ai=False)
    else:
        # Default: Quick scan
        run_basic_scan(project_path)
```

---

## Recommendation / 建議

**Daily Development**: Quick Scan  
**Before PR**: Deep Scan  
**Before Release**: AI-Assisted Scan (if available)

---

**Created**: 2026-01-29  
**Part of**: synthforge devtools
