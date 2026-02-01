# Devtools - Development Toolkit

A comprehensive suite of development tools for AI-assisted coding environments.

用於 AI 輔助編程環境的綜合開發工具套件。

---

## 🛠️ Available Tools

### 1. **Project Scaffolder** (專案腳手架)
Quickly create new projects from templates.

**Templates:**
- `python-cli` - Python CLI Application
- `python-fastapi` - FastAPI Web Service
- `node-express` - Node.js Express Server
- `static-web` - Static HTML/CSS/JS Website

**Usage:**
```bash
python devtools/cli.py new --name=my_app --type=python-fastapi
```

---

### 2. **Security Auditor** (安全檢查員)
Scan projects for security vulnerabilities and sensitive information leaks.

**Detects:**
- API Keys (OpenAI, Anthropic, AWS, GitHub)
- Hardcoded passwords
- Absolute paths
- Sensitive files (.env, *.key)
- File permissions (Unix)

**Usage:**
```bash
python devtools/cli.py check projects/my_app --security
```

---

### 3. **Release Cleaner** (發布清潔工)
Prepare clean project releases by filtering out development noise.

**Filters:**
- AI tool artifacts (.cursor/, .continue/)
- IDE configurations (.vscode/, .idea/)
- Virtual environments (.venv/, node_modules/)
- Build artifacts (__pycache__/, dist/)
- Sensitive files (.env, *.key)
- Personal notes (TODO.md, scratch/)

**Usage:**
```bash
python devtools/cli.py release projects/my_app dist/my_app_clean --clean
```

---

### 4. **Dependency Analyzer** (依賴分析器)
Analyze project dependencies and generate minimal requirements.txt.

**Features:**
- Scan actual imports in code
- Detect unused dependencies
- Find missing dependencies
- Generate minimal requirements.txt

**Usage:**
```bash
python devtools/cli.py analyze projects/my_app --generate-req
```

---

### 5. **License Checker** (授權檢查器)
Check dependency licenses and assess legal risks.

**License Categories:**
- ✅ Permissive (MIT, Apache, BSD) - Low risk
- 🟡 Weak Copyleft (LGPL, MPL) - Medium risk
- 🟠 Strong Copyleft (GPL, AGPL) - High risk
- 🔴 Proprietary/Unknown - Critical risk

**Usage:**
```bash
python devtools/cli.py check projects/my_app --licenses
```

---

## 📋 Quick Start

### Installation

```bash
# Install required dependencies
pip install click pyyaml

# Optional: For license checking
pip install pip-licenses
```

### Basic Usage

```bash
# Create a new project
python devtools/cli.py new --name=my_awesome_app --type=python-fastapi

# Run all checks
python devtools/cli.py check projects/my_awesome_app --all

# Prepare for release
python devtools/cli.py release projects/my_awesome_app dist/my_awesome_app --clean --audit

# Show help
python devtools/cli.py --help
```

---

## 🎯 Use Cases

### Scenario 1: Starting a New Project
```bash
# Create project
python devtools/cli.py new --name=api_server --type=python-fastapi

# Navigate to project
cd projects/api_server

# Start development
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### Scenario 2: Pre-Release Security Check
```bash
# Run comprehensive check
python devtools/cli.py check projects/my_app --all

# Fix any issues found
# ...

# Prepare clean release
python devtools/cli.py release projects/my_app dist/my_app_v1.0 --clean --audit
```

### Scenario 3: Dependency Cleanup
```bash
# Analyze dependencies
python devtools/cli.py analyze projects/my_app

# Review unused packages
# Remove them from requirements.txt

# Regenerate minimal requirements
python devtools/cli.py analyze projects/my_app --generate-req
```

---

## 📁 File Structure

```
devtools/
├── __init__.py              # Package initialization
├── cli.py                   # Unified CLI interface
├── tests/                   # Unit and integration tests
├── scaffolder.py            # Project templates
├── security_auditor.py      # Security scanning
├── release_cleaner.py       # Release preparation
├── dep_analyzer.py          # Dependency analysis
├── license_checker.py       # License compliance
└── filters.yaml             # Global filter rules
```

---

## ⚙️ Configuration

### Global Filters (`filters.yaml`)
Customize what gets filtered during release cleaning.

```yaml
ai_tools:
  - .cursor/
  - .continue/
  # Add your custom AI tool directories

secrets:
  - .env
  - *.key
  # Add your custom secret patterns
```

### Project-Level Overrides (`.releaseignore`)
Create a `.releaseignore` file in your project root:

```
# Project-specific filters
my_local_config.yaml
experiments/
*.draft.*
```

---

## 🔧 Advanced Usage

### Using as Python Module

```python
from devtools import SecurityAuditor, ReleaseCleaner
from pathlib import Path

# Security audit
auditor = SecurityAuditor(Path('projects/my_app'))
issues = auditor.scan()
print(auditor.generate_report())

# Release cleaning
cleaner = ReleaseCleaner(
    Path('projects/my_app'),
    Path('dist/my_app_clean')
)
cleaner.clean(interactive=False)
```

### Batch Processing

```python
from pathlib import Path
from devtools import SecurityAuditor

# Scan all projects
workspace = Path('projects')
for project in workspace.iterdir():
    if project.is_dir():
        auditor = SecurityAuditor(project)
        issues = auditor.scan()
        if issues:
            print(f"⚠️  Issues found in {project.name}")
```

---

## 🚀 Roadmap

### Phase 1: Core Tools ✅
- [x] Project Scaffolder
- [x] Security Auditor
- [x] Release Cleaner
- [x] Dependency Analyzer
- [x] License Checker
- [x] Unified CLI

### Phase 2: Advanced Features (Planned)
- [ ] Environment Validator
- [ ] Changelog Generator
- [ ] Docker Builder
- [ ] Performance Profiler
- [ ] Code Quality Scanner

### Phase 3: AI Integration (Future)
- [ ] AI-powered code review
- [ ] Automated documentation generation
- [ ] Test generation
- [ ] Refactoring suggestions

---

## 📝 Contributing

### Adding a New Tool

1. Create `devtools/your_tool.py`
2. Implement with bilingual output (EN/ZH)
3. Add CLI command in `cli.py`
4. Update this README
5. Add tests

### Tool Template

```python
"""
Your Tool - 您的工具
Brief description

Brief description in Chinese
"""

class YourTool:
    def __init__(self, project_path):
        self.project_path = project_path
    
    def run(self):
        """Main logic"""
        pass
    
    def generate_report(self):
        """Generate bilingual report"""
        return "Report content"
```

---

## 📄 License

This toolkit is part of the AI Workspace project.

---

## 🤝 Support

For issues or questions:
1. Check `TASKS.md` for implementation status
2. Review `ARCHITECTURE.md` for design decisions
3. See examples in this README

---

**Version**: 1.0.0  
**Last Updated**: 2026-01-29
