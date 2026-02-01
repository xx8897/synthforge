"""
Dependency Analyzer - 依賴分析器
掃描專案實際使用的套件，生成最小化依賴清單

Dependency Analyzer - Scans actual package usage and generates minimal dependency lists
"""

import ast
import sys
from pathlib import Path
from typing import Set, Dict, List
import subprocess
import json


class DependencyAnalyzer:
    """依賴分析器 / Dependency Analyzer"""
    
    def __init__(self, project_path: Path):
        self.project_path = project_path
        self.imports: Set[str] = set()
        self.stdlib_modules = set(sys.stdlib_module_names)
        
    def analyze(self) -> Dict[str, any]:
        """
        分析專案依賴 / Analyze project dependencies
        
        Returns:
            Dictionary with analysis results
        """
        print(f"🔍 Analyzing dependencies in: {self.project_path}\n")
        
        # 掃描所有 Python 檔案
        for py_file in self.project_path.rglob('*.py'):
            if '__pycache__' in str(py_file) or '.venv' in str(py_file):
                continue
            self._analyze_file(py_file)
        
        # 分類依賴
        third_party = self._filter_third_party()
        
        # 檢查已安裝的套件
        installed = self._get_installed_packages()
        
        # 找出未使用的依賴
        unused = self._find_unused_dependencies(third_party, installed)
        
        # 找出缺少的依賴
        missing = self._find_missing_dependencies(third_party, installed)
        
        return {
            'total_imports': len(self.imports),
            'third_party': sorted(third_party),
            'installed': installed,
            'unused': unused,
            'missing': missing
        }
    
    def _analyze_file(self, file_path: Path):
        """分析單一檔案的 import / Analyze imports in a single file"""
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        self.imports.add(alias.name.split('.')[0])
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        self.imports.add(node.module.split('.')[0])
        
        except SyntaxError as e:
            print(f"   ⚠️  Syntax error in {file_path}: {e}")
        except Exception as e:
            print(f"   ⚠️  Error analyzing {file_path}: {e}")
    
    def _filter_third_party(self) -> Set[str]:
        """過濾出第三方套件 / Filter third-party packages"""
        third_party = set()
        
        for module in self.imports:
            # 跳過標準庫
            if module in self.stdlib_modules:
                continue
            
            # 跳過本地模組（假設專案內的模組）
            if (self.project_path / f"{module}.py").exists():
                continue
            if (self.project_path / module).is_dir():
                continue
            
            third_party.add(module)
        
        return third_party
    
    def _get_installed_packages(self) -> Dict[str, str]:
        """獲取已安裝的套件 / Get installed packages"""
        try:
            result = subprocess.run(
                [sys.executable, '-m', 'pip', 'list', '--format=json'],
                capture_output=True,
                text=True,
                check=True
            )
            packages = json.loads(result.stdout)
            return {pkg['name'].lower().replace('-', '_'): pkg['version'] 
                   for pkg in packages}
        except Exception as e:
            print(f"   ⚠️  Could not get installed packages: {e}")
            return {}
    
    def _find_unused_dependencies(self, used: Set[str], installed: Dict[str, str]) -> List[str]:
        """找出未使用的依賴 / Find unused dependencies"""
        # 讀取 requirements.txt
        req_file = self.project_path / 'requirements.txt'
        if not req_file.exists():
            return []
        
        required = set()
        for line in req_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#'):
                # 提取套件名稱（去除版本號）
                pkg = line.split('==')[0].split('>=')[0].split('<=')[0].strip()
                required.add(pkg.lower().replace('-', '_'))
        
        # 找出在 requirements.txt 但未被使用的
        unused = required - used
        return sorted(unused)
    
    def _find_missing_dependencies(self, used: Set[str], installed: Dict[str, str]) -> List[str]:
        """找出缺少的依賴 / Find missing dependencies"""
        missing = []
        for module in used:
            if module.lower() not in installed:
                missing.append(module)
        return sorted(missing)
    
    def generate_requirements(self, output_path: Path = None) -> str:
        """
        生成最小化的 requirements.txt / Generate minimal requirements.txt
        
        Args:
            output_path: Output file path (default: project_path/requirements.txt)
        
        Returns:
            Generated requirements content
        """
        result = self.analyze()
        
        if output_path is None:
            output_path = self.project_path / 'requirements.txt'
        
        lines = []
        lines.append("# Auto-generated by Dependency Analyzer")
        lines.append(f"# Generated: {Path(__file__).parent.parent.name}")
        lines.append("")
        
        installed = result['installed']
        
        for pkg in result['third_party']:
            pkg_lower = pkg.lower().replace('_', '-')
            
            if pkg_lower in installed:
                version = installed[pkg_lower]
                lines.append(f"{pkg_lower}>={version}")
            else:
                lines.append(f"{pkg_lower}")
        
        content = '\n'.join(lines)
        
        if output_path:
            output_path.write_text(content, encoding='utf-8')
            print(f"\n✅ Generated: {output_path}")
        
        return content
    
    def generate_report(self) -> str:
        """生成分析報告 / Generate analysis report"""
        result = self.analyze()
        
        report = []
        report.append("=" * 80)
        report.append("📦 DEPENDENCY ANALYSIS REPORT / 依賴分析報告")
        report.append("=" * 80)
        report.append(f"\nProject: {self.project_path.name}")
        report.append(f"Total imports found: {result['total_imports']}")
        report.append(f"總計發現 import: {result['total_imports']}\n")
        
        # Third-party packages
        report.append(f"Third-party packages used ({len(result['third_party'])}):")
        report.append(f"使用的第三方套件 ({len(result['third_party'])}):")
        for pkg in result['third_party']:
            installed_version = result['installed'].get(pkg.lower().replace('_', '-'), 'NOT INSTALLED')
            report.append(f"   • {pkg} ({installed_version})")
        
        # Unused dependencies
        if result['unused']:
            report.append(f"\n⚠️  Unused dependencies in requirements.txt ({len(result['unused'])}):")
            report.append(f"⚠️  requirements.txt 中未使用的依賴 ({len(result['unused'])}):")
            for pkg in result['unused']:
                report.append(f"   • {pkg}")
        
        # Missing dependencies
        if result['missing']:
            report.append(f"\n❌ Missing dependencies (used but not installed) ({len(result['missing'])}):")
            report.append(f"❌ 缺少的依賴（使用但未安裝） ({len(result['missing'])}):")
            for pkg in result['missing']:
                report.append(f"   • {pkg}")
        
        report.append("\n" + "=" * 80)
        
        if not result['unused'] and not result['missing']:
            report.append("✅ All dependencies are correctly configured!")
            report.append("✅ 所有依賴配置正確！")
        else:
            report.append("📝 Recommendations / 建議:")
            if result['unused']:
                report.append("   • Remove unused packages from requirements.txt")
                report.append("     從 requirements.txt 移除未使用的套件")
            if result['missing']:
                report.append("   • Install missing packages or add to requirements.txt")
                report.append("     安裝缺少的套件或加入 requirements.txt")
        
        report.append("=" * 80)
        
        return '\n'.join(report)


if __name__ == '__main__':
    import click
    
    @click.command()
    @click.argument('project_path', type=click.Path(exists=True))
    @click.option('--generate', is_flag=True, help='Generate requirements.txt')
    def main(project_path, generate):
        """Analyze project dependencies"""
        path = Path(project_path)
        analyzer = DependencyAnalyzer(path)
        
        print(analyzer.generate_report())
        
        if generate:
            analyzer.generate_requirements()
    
    main()
