# Git & GitHub Strategy - 版本控制與協作策略

**Version**: 2.0
**Status**: MANDATORY 強制
**Scope**: All repositories in synthforge workspace

---

## 🎯 Core Strategy / 核心策略

**Hybrid Model**:
1.  **Workplace Root (`synthforge/`)**: **Private Repo** (Tools & Configs)
2.  **Projects (`projects/`)**: **Independent Repos** (Apps)
3.  **Common Assets**: **Submodule or Package** (Skills & Agents)

**混合模式**:
1.  **工作區根目錄 (`synthforge/`)**: **私有儲存庫** (工具與配置)
2.  **專案 (`projects/`)**: **獨立儲存庫** (應用程式)
3.  **共用資源**: **子模組或套件** (技能與代理)

---

## 📦 Repository Structure / 儲存庫結構

### 1. Main Repo: `synthforge` (Private)
**URL**: `https://github.com/xx8897/synthforge` (private)

**Contains**:
- ✅ `devtools/` - All development tools
- ✅ `agents/` - AI assistants
- ✅ `skills/` - Reusable capabilities
- ✅ `templates/` - Project templates
- ✅ `rules/` - All rules
- ✅ `docs/` - All documentation
- ✅ `.gitignore` (excludes `projects/`)
- ❌ `projects/` - **EXCLUDED** (each is separate repo)

### 2. Project Repos: Individual Repositories
**Example**: `https://github.com/xx8897/my-awesome-app`

**Contains**:
- ✅ Project source code
- ✅ Project-specific `README.md`
- ✅ Project-specific `.gitignore`
- ✅ `requirements.txt` or `package.json`
- ❌ No synthforge devtools (independent)

---

## 🚀 Workflow / 工作流程

### Initial Setup (Workspace)

```bash
cd C:\Users\xx8897\synthforge

# Initialize git
git init

# Add remote
git remote add origin https://github.com/xx8897/synthforge.git

# Check ignores (projects/ must be ignored)
git status

# Initial commit
git add .
git commit -m "feat: initialize synthforge workspace v2.0"
git push -u origin main
```

### New Project Setup

```bash
cd C:\Users\xx8897\synthforge\projects\my_app

# Initialize separate repo
git init

# Add remote
git remote add origin https://github.com/xx8897/my_app.git

# Initial commit
git add .
git commit -m "init: my_app structure"
git push -u origin main
```

### Daily Workflow

**Updating synthforge (Tools & Docs)**:
```bash
cd C:\Users\xx8897\synthforge
# Edit rules or tools
git add rules/ devtools/
git commit -m "feat(rules): update coding style"
git push
```

**Updating a Project**:
```bash
cd C:\Users\xx8897\synthforge\projects\my_app
# Edit app code
git add .
git commit -m "feat(auth): add login page"
git push
```

---

## 📝 Commit Convention / 提交規範

**Format**: `<type>(<scope>): <subject>`

**Types**:
- `feat`: New feature (新功能)
- `fix`: Bug fix (修復)
- `docs`: Documentation (文件)
- `style`: Formatting (格式)
- `refactor`: Restructuring (重構)
- `test`: Adding tests (測試)
- `chore`: Maintenance (雜項)

**Examples**:
```bash
git commit -m "feat(devtools): add security auditor"
git commit -m "fix(cli): handle unicode paths"
git commit -m "docs(arch): merge git strategies"
```

---

## 🔒 Security & Best Practices / 安全與最佳實踐

### Before Pushing:
1.  **Run Security Scan**:
    ```bash
    python devtools/cli.py check . --security
    ```
2.  **Check Secrets**: Ensure no `.env` or `*.key` files.
3.  **Check Ignores**: Ensure `projects/` is ignored in root repo.

### .gitignore Strategy

**Root (`synthforge/.gitignore`)**:
```gitignore
# Exclude all projects
projects/
!projects/.gitkeep

# Secrets
.env
*.key
secrets.yaml

# AI Artifacts
.cursor/
.continue/
.internal/temp/
```

**Project (`projects/app/.gitignore`)**:
```gitignore
# Runtime
__pycache__/
.venv/
node_modules/

# Secrets
.env

# Build
dist/
build/
```

---

## 🤖 GitHub Integration (GitHub 特性)

### Repository Settings
- **Main Branch Protection**: Require PR reviews, status checks.
- **Secrets**: `OPENAI_API_KEY` (for CI/CD scans).

### Future CI/CD
- **Test Tools**: Run `pytest tests/` on push to `synthforge`.
- **Lint Projects**: Run linters on push to project repos.

---

## 🎯 Summary / 總結

| Aspect | synthforge | Projects |
|--------|-----------|----------|
| **Repo** | Private | Public/Private |
| **Content** | Tools, Rules, Docs | App Code |
| **Updates** | Tooling improvements | Feature development |
| **Relationship**| Tool Provider | Tool Consumer |

**Key Rule**: Workspace root manages tools; Projects manage apps. completely separate git histories.

---

**Created**: 2026-01-29
**Updated**: 2026-02-01 (Merged GITHUB_STRATEGY)
**Status**: ACTIVE
