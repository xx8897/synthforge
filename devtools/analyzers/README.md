# Multi-Language Dependency Analyzers
# 多語言依賴分析器

This directory contains dependency analyzers for different programming languages.

本目錄包含不同程式語言的依賴分析器。

---

## Supported Languages / 支援的語言

| Language | Analyzer | Package File | Status |
|----------|----------|--------------|--------|
| **Python** | `python_analyzer.py` | `requirements.txt`, `pyproject.toml` | ✅ Complete |
| **Node.js** | `nodejs_analyzer.py` | `package.json`, `package-lock.json` | ✅ Complete |
| **Go** | `go_analyzer.py` | `go.mod`, `go.sum` | ✅ Complete |
| **Rust** | `rust_analyzer.py` | `Cargo.toml`, `Cargo.lock` | ✅ Complete |
| **C++** | `cpp_analyzer.py` | `CMakeLists.txt`, `conanfile.txt` | 📝 Planned |

---

## Features / 功能

### Core Features (All Languages):
- ✅ Direct dependency detection
- ✅ Indirect (transitive) dependency detection
- ✅ Unused dependency detection
- ✅ Missing dependency detection
- ✅ Dependency tree visualization
- ✅ Version conflict detection
- ✅ Security vulnerability checking

### Language-Specific:
- **Python**: Integration with `pip-audit`, `safety`
- **Node.js**: Integration with `npm audit`, `yarn audit`
- **Go**: Integration with `go list`, `govulncheck`
- **Rust**: Integration with `cargo audit`

---

## Usage / 使用方式

### Via CLI:
```bash
# Auto-detect language
python devtools/cli.py analyze projects/my_app

# Specify language
python devtools/cli.py analyze projects/my_app --lang=python
python devtools/cli.py analyze projects/my_app --lang=nodejs
python devtools/cli.py analyze projects/my_app --lang=go
python devtools/cli.py analyze projects/my_app --lang=rust
```

### As Python Module:
```python
from devtools.analyzers import PythonAnalyzer, NodeJSAnalyzer

# Python project
analyzer = PythonAnalyzer(Path('projects/my_app'))
result = analyzer.analyze()
print(analyzer.generate_report())

# Node.js project
analyzer = NodeJSAnalyzer(Path('projects/my_app'))
result = analyzer.analyze()
```

---

## Architecture / 架構

### Base Class:
All analyzers inherit from `BaseAnalyzer`:

```python
class BaseAnalyzer:
    def analyze(self) -> Dict
    def detect_direct_deps(self) -> Set[str]
    def detect_indirect_deps(self) -> Set[str]
    def find_unused(self) -> List[str]
    def find_missing(self) -> List[str]
    def check_vulnerabilities(self) -> List[Dict]
    def visualize_tree(self) -> str
    def generate_report(self) -> str
```

### Dependency Tree Format:
```
my-app
├── requests==2.28.0
│   ├── urllib3==1.26.0
│   ├── certifi==2022.12.7
│   └── charset-normalizer==3.0.1
├── fastapi==0.95.0
│   ├── pydantic==1.10.0
│   └── starlette==0.26.0
└── numpy==1.24.0
```

---

## Indirect Dependency Detection / 間接依賴偵測

### Why It's Important:
Indirect dependencies (dependencies of your dependencies) can:
- Introduce security vulnerabilities
- Cause version conflicts
- Increase bundle size
- Break unexpectedly when updated

### How We Detect Them:

#### Python:
```bash
# Use pip show to get dependencies
pip show package_name

# Use pipdeptree for full tree
pipdeptree -p package_name
```

#### Node.js:
```bash
# package-lock.json contains full dependency tree
npm list --all

# Or use npm-check
npm-check
```

#### Go:
```bash
# go.mod only shows direct deps
# go.sum shows all (direct + indirect)
go list -m all
```

#### Rust:
```bash
# Cargo.lock contains full dependency tree
cargo tree
```

---

## Security Vulnerability Checking / 安全漏洞檢查

### Integration with Security Tools:

| Language | Tool | Command |
|----------|------|---------|
| Python | pip-audit | `pip-audit` |
| Python | safety | `safety check` |
| Node.js | npm audit | `npm audit` |
| Node.js | yarn audit | `yarn audit` |
| Go | govulncheck | `govulncheck ./...` |
| Rust | cargo-audit | `cargo audit` |

### Vulnerability Report Format:
```json
{
  "package": "requests",
  "version": "2.25.0",
  "vulnerability": "CVE-2021-33503",
  "severity": "HIGH",
  "description": "...",
  "fixed_in": "2.26.0"
}
```

---

## Version Conflict Detection / 版本衝突偵測

### Example Conflict:
```
Package A requires: requests>=2.28.0
Package B requires: requests<2.27.0
❌ CONFLICT: No version satisfies both constraints
```

### Resolution Strategies:
1. **Upgrade**: Update Package B to support newer requests
2. **Downgrade**: Use older Package A version
3. **Fork**: Create custom version of one package
4. **Alternative**: Find replacement for one package

---

## Performance / 效能

| Language | Project Size | Analysis Time |
|----------|--------------|---------------|
| Python | 100 deps | ~5s |
| Node.js | 500 deps | ~10s |
| Go | 50 deps | ~3s |
| Rust | 100 deps | ~8s |

---

## Troubleshooting / 疑難排解

### Python:
**Issue**: "pip-audit not found"  
**Solution**: `pip install pip-audit`

### Node.js:
**Issue**: "package-lock.json missing"  
**Solution**: `npm install` to generate it

### Go:
**Issue**: "go.sum out of date"  
**Solution**: `go mod tidy`

### Rust:
**Issue**: "Cargo.lock missing"  
**Solution**: `cargo build` to generate it

---

## Future Enhancements / 未來改進

- [ ] C++ support (CMake, Conan)
- [ ] Java support (Maven, Gradle)
- [ ] PHP support (Composer)
- [ ] Ruby support (Bundler)
- [ ] Interactive dependency resolution
- [ ] Automated dependency updates
- [ ] License compatibility checking per dependency

---

**Created**: 2026-01-29  
**Part of**: synthforge devtools  
**Maintainer**: synthforge team
