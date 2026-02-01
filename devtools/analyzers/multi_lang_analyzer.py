"""
Multi-Language Dependency Analyzer - 多語言依賴分析器
Analyzes dependencies for Python, JavaScript, TypeScript, and more

Supports:
- Python (.py) - import statements
- JavaScript (.js) - require() and import
- TypeScript (.ts, .tsx) - import statements
- Node.js (package.json)
"""

import ast
import json
import re
from pathlib import Path
from typing import Set, Dict, List, Tuple
from dataclasses import dataclass
from enum import Enum


class Language(Enum):
    """Supported languages"""
    PYTHON = "python"
    JAVASCRIPT = "javascript"
    TYPESCRIPT = "typescript"
    UNKNOWN = "unknown"


@dataclass
class DependencyInfo:
    """Dependency information"""
    name: str
    language: Language
    files: List[str]
    version: str = None
    
    def __hash__(self):
        return hash(self.name)


class MultiLanguageAnalyzer:
    """多語言依賴分析器 / Multi-Language Dependency Analyzer"""
    
    # Language file extensions
    EXTENSIONS = {
        Language.PYTHON: ['.py'],
        Language.JAVASCRIPT: ['.js', '.jsx', '.mjs', '.cjs'],
        Language.TYPESCRIPT: ['.ts', '.tsx'],
    }
    
    # Standard library modules (Python)
    PYTHON_STDLIB = set([
        'abc', 'ast', 'asyncio', 'base64', 'collections', 'copy', 'csv',
        'datetime', 'decimal', 'enum', 'functools', 'hashlib', 'io', 'itertools',
        'json', 'logging', 'math', 'os', 'pathlib', 'pickle', 're', 'shutil',
        'socket', 'sqlite3', 'string', 'subprocess', 'sys', 'tempfile', 'threading',
        'time', 'typing', 'unittest', 'urllib', 'uuid', 'warnings', 'weakref',
    ])
    
    # Node.js built-in modules
    NODE_BUILTINS = set([
        'assert', 'buffer', 'child_process', 'cluster', 'crypto', 'dgram',
        'dns', 'events', 'fs', 'http', 'https', 'net', 'os', 'path',
        'querystring', 'readline', 'stream', 'string_decoder', 'timers',
        'tls', 'tty', 'url', 'util', 'v8', 'vm', 'zlib',
    ])
    
    def __init__(self, project_path: Path):
        self.project_path = Path(project_path)
        self.dependencies: Dict[Language, Set[DependencyInfo]] = {
            Language.PYTHON: set(),
            Language.JAVASCRIPT: set(),
            Language.TYPESCRIPT: set(),
        }
        self.file_count: Dict[Language, int] = {
            Language.PYTHON: 0,
            Language.JAVASCRIPT: 0,
            Language.TYPESCRIPT: 0,
        }
    
    def analyze(self) -> Dict[str, any]:
        """
        分析專案的所有語言依賴 / Analyze all language dependencies
        
        Returns:
            Dictionary with analysis results
        """
        print(f"🔍 Analyzing multi-language dependencies in: {self.project_path}\n")
        
        # Detect languages
        languages = self._detect_languages()
        
        if not languages:
            print("❌ No supported language files found")
            return {}
        
        print(f"📋 Detected languages: {', '.join(lang.value for lang in languages)}\n")
        
        # Analyze each language
        for lang in languages:
            if lang == Language.PYTHON:
                self._analyze_python()
            elif lang in [Language.JAVASCRIPT, Language.TYPESCRIPT]:
                self._analyze_javascript_typescript()
        
        # Generate results
        return self._generate_results()
    
    def _detect_languages(self) -> Set[Language]:
        """檢測專案使用的語言 / Detect languages used in project"""
        languages = set()
        
        for lang, extensions in self.EXTENSIONS.items():
            for ext in extensions:
                if list(self.project_path.rglob(f'*{ext}')):
                    languages.add(lang)
                    break
        
        return languages
    
    def _analyze_python(self):
        """分析 Python 依賴 / Analyze Python dependencies"""
        print("🐍 Analyzing Python dependencies...")
        
        for py_file in self.project_path.rglob('*.py'):
            if self._should_skip(py_file):
                continue
            
            self.file_count[Language.PYTHON] += 1
            imports = self._extract_python_imports(py_file)
            
            for imp in imports:
                # Skip standard library
                if imp in self.PYTHON_STDLIB:
                    continue
                
                # Skip local modules
                if self._is_local_module(imp, Language.PYTHON):
                    continue
                
                dep = DependencyInfo(
                    name=imp,
                    language=Language.PYTHON,
                    files=[str(py_file.relative_to(self.project_path))]
                )
                
                # Add or update dependency
                existing = next((d for d in self.dependencies[Language.PYTHON] if d.name == imp), None)
                if existing:
                    existing.files.append(str(py_file.relative_to(self.project_path)))
                else:
                    self.dependencies[Language.PYTHON].add(dep)
        
        print(f"   ✅ Analyzed {self.file_count[Language.PYTHON]} Python files")
    
    def _analyze_javascript_typescript(self):
        """分析 JavaScript/TypeScript 依賴 / Analyze JS/TS dependencies"""
        print("📦 Analyzing JavaScript/TypeScript dependencies...")
        
        # Combine JS and TS extensions
        extensions = self.EXTENSIONS[Language.JAVASCRIPT] + self.EXTENSIONS[Language.TYPESCRIPT]
        
        for ext in extensions:
            for file in self.project_path.rglob(f'*{ext}'):
                if self._should_skip(file):
                    continue
                
                lang = Language.TYPESCRIPT if ext in self.EXTENSIONS[Language.TYPESCRIPT] else Language.JAVASCRIPT
                self.file_count[lang] += 1
                
                imports = self._extract_js_ts_imports(file)
                
                for imp in imports:
                    # Skip Node.js built-ins
                    if imp in self.NODE_BUILTINS:
                        continue
                    
                    # Skip relative imports
                    if imp.startswith('.') or imp.startswith('/'):
                        continue
                    
                    dep = DependencyInfo(
                        name=imp,
                        language=lang,
                        files=[str(file.relative_to(self.project_path))]
                    )
                    
                    # Add or update dependency
                    existing = next((d for d in self.dependencies[lang] if d.name == imp), None)
                    if existing:
                        existing.files.append(str(file.relative_to(self.project_path)))
                    else:
                        self.dependencies[lang].add(dep)
        
        js_count = self.file_count[Language.JAVASCRIPT]
        ts_count = self.file_count[Language.TYPESCRIPT]
        print(f"   ✅ Analyzed {js_count} JavaScript and {ts_count} TypeScript files")
    
    def _extract_python_imports(self, file_path: Path) -> Set[str]:
        """提取 Python import / Extract Python imports"""
        imports = set()
        
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.add(alias.name.split('.')[0])
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.add(node.module.split('.')[0])
        
        except Exception as e:
            print(f"   ⚠️  Error analyzing {file_path.name}: {e}")
        
        return imports
    
    def _extract_js_ts_imports(self, file_path: Path) -> Set[str]:
        """提取 JavaScript/TypeScript import / Extract JS/TS imports"""
        imports = set()
        
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Match: import ... from 'package'
            import_pattern = r"import\s+.*?\s+from\s+['\"]([^'\"]+)['\"]"
            for match in re.finditer(import_pattern, content):
                package = match.group(1)
                # Extract package name (before /)
                if '/' in package and not package.startswith('.'):
                    package = package.split('/')[0]
                if package.startswith('@'):
                    # Scoped package: @scope/package
                    parts = package.split('/')
                    if len(parts) >= 2:
                        package = f"{parts[0]}/{parts[1]}"
                imports.add(package)
            
            # Match: require('package')
            require_pattern = r"require\(['\"]([^'\"]+)['\"]\)"
            for match in re.finditer(require_pattern, content):
                package = match.group(1)
                if '/' in package and not package.startswith('.'):
                    package = package.split('/')[0]
                if package.startswith('@'):
                    parts = package.split('/')
                    if len(parts) >= 2:
                        package = f"{parts[0]}/{parts[1]}"
                imports.add(package)
        
        except Exception as e:
            print(f"   ⚠️  Error analyzing {file_path.name}: {e}")
        
        return imports
    
    def _should_skip(self, file_path: Path) -> bool:
        """檢查是否應跳過檔案 / Check if file should be skipped"""
        skip_patterns = [
            '__pycache__', '.venv', 'venv', 'node_modules',
            '.git', 'dist', 'build', '.next', '.nuxt'
        ]
        
        return any(pattern in str(file_path) for pattern in skip_patterns)
    
    def _is_local_module(self, module_name: str, language: Language) -> bool:
        """檢查是否為本地模組 / Check if module is local"""
        if language == Language.PYTHON:
            # Check if module file exists
            if (self.project_path / f"{module_name}.py").exists():
                return True
            if (self.project_path / module_name).is_dir():
                return True
        
        return False
    
    def _generate_results(self) -> Dict[str, any]:
        """生成分析結果 / Generate analysis results"""
        results = {}
        
        for lang, deps in self.dependencies.items():
            if not deps:
                continue
            
            results[lang.value] = {
                'file_count': self.file_count[lang],
                'dependency_count': len(deps),
                'dependencies': [
                    {
                        'name': dep.name,
                        'used_in': dep.files,
                        'usage_count': len(dep.files)
                    }
                    for dep in sorted(deps, key=lambda d: d.name)
                ]
            }
        
        return results
    
    def generate_report(self) -> str:
        """生成分析報告 / Generate analysis report"""
        results = self.analyze()
        
        if not results:
            return "No dependencies found"
        
        report = []
        report.append("=" * 80)
        report.append("🌍 MULTI-LANGUAGE DEPENDENCY ANALYSIS / 多語言依賴分析")
        report.append("=" * 80)
        report.append(f"\nProject: {self.project_path.name}\n")
        
        for lang_name, data in results.items():
            report.append(f"📋 {lang_name.upper()}")
            report.append(f"   Files analyzed: {data['file_count']}")
            report.append(f"   Dependencies found: {data['dependency_count']}\n")
            
            for dep in data['dependencies']:
                report.append(f"   • {dep['name']}")
                report.append(f"     Used in {dep['usage_count']} file(s)")
                if dep['usage_count'] <= 3:
                    for file in dep['used_in']:
                        report.append(f"       - {file}")
                report.append("")
        
        report.append("=" * 80)
        
        return '\n'.join(report)


if __name__ == '__main__':
    import click
    
    @click.command()
    @click.argument('project_path', type=click.Path(exists=True))
    def main(project_path):
        """Analyze multi-language project dependencies"""
        path = Path(project_path)
        analyzer = MultiLanguageAnalyzer(path)
        
        print(analyzer.generate_report())
    
    main()
