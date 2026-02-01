"""
License Checker - 授權檢查器
掃描專案依賴的授權，警告潛在的法律風險

License Checker - Scans dependency licenses and warns about potential legal risks
"""

import subprocess
import sys
import json
from pathlib import Path
from typing import Dict, List
import re


# 授權分類
LICENSE_CATEGORIES = {
    'permissive': {
        'licenses': ['MIT', 'Apache-2.0', 'BSD-2-Clause', 'BSD-3-Clause', 'ISC', 'Python-2.0'],
        'risk': 'LOW',
        'description': 'Permissive licenses - safe for commercial use'
    },
    'copyleft_weak': {
        'licenses': ['LGPL-2.1', 'LGPL-3.0', 'MPL-2.0', 'EPL-1.0'],
        'risk': 'MEDIUM',
        'description': 'Weak copyleft - safe if used as library'
    },
    'copyleft_strong': {
        'licenses': ['GPL-2.0', 'GPL-3.0', 'AGPL-3.0'],
        'risk': 'HIGH',
        'description': 'Strong copyleft - requires source code disclosure'
    },
    'proprietary': {
        'licenses': ['Commercial', 'Proprietary'],
        'risk': 'CRITICAL',
        'description': 'Proprietary licenses - check terms carefully'
    },
    'unknown': {
        'licenses': ['UNKNOWN', 'UNLICENSED'],
        'risk': 'HIGH',
        'description': 'Unknown license - legal risk'
    }
}


class LicenseChecker:
    """授權檢查器 / License Checker"""
    
    def __init__(self, project_path: Path):
        self.project_path = project_path
        self.packages: Dict[str, Dict] = {}
    
    def scan(self) -> Dict[str, any]:
        """
        掃描所有依賴的授權 / Scan all dependency licenses
        
        Returns:
            Dictionary with scan results
        """
        print(f"📜 Scanning licenses in: {self.project_path}\n")
        
        # 獲取已安裝的套件
        self._get_package_licenses()
        
        # 分類授權
        categorized = self._categorize_licenses()
        
        # 檢查風險
        risks = self._assess_risks(categorized)
        
        return {
            'total_packages': len(self.packages),
            'packages': self.packages,
            'categorized': categorized,
            'risks': risks
        }
    
    def _get_package_licenses(self):
        """獲取套件授權資訊 / Get package license information"""
        try:
            # 使用 pip-licenses (需要安裝: pip install pip-licenses)
            result = subprocess.run(
                [sys.executable, '-m', 'pip_licenses', '--format=json'],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                packages = json.loads(result.stdout)
                for pkg in packages:
                    self.packages[pkg['Name']] = {
                        'version': pkg['Version'],
                        'license': pkg['License'],
                        'author': pkg.get('Author', 'Unknown')
                    }
            else:
                # Fallback: 使用 pip show
                self._get_licenses_via_pip_show()
        
        except FileNotFoundError:
            print("   ⚠️  pip-licenses not found. Install: pip install pip-licenses")
            print("   ⚠️  未找到 pip-licenses。安裝: pip install pip-licenses")
            self._get_licenses_via_pip_show()
    
    def _get_licenses_via_pip_show(self):
        """透過 pip show 獲取授權 (Fallback) / Get licenses via pip show"""
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'list', '--format=json'],
            capture_output=True,
            text=True,
            check=True
        )
        
        packages = json.loads(result.stdout)
        
        for pkg in packages[:20]:  # 限制數量避免太慢
            pkg_info = subprocess.run(
                [sys.executable, '-m', 'pip', 'show', pkg['name']],
                capture_output=True,
                text=True
            )
            
            license_match = re.search(r'License: (.+)', pkg_info.stdout)
            license_name = license_match.group(1) if license_match else 'UNKNOWN'
            
            self.packages[pkg['name']] = {
                'version': pkg['version'],
                'license': license_name,
                'author': 'Unknown'
            }
    
    def _categorize_licenses(self) -> Dict[str, List[str]]:
        """分類授權 / Categorize licenses"""
        categorized = {cat: [] for cat in LICENSE_CATEGORIES.keys()}
        
        for pkg_name, pkg_info in self.packages.items():
            license_name = pkg_info['license']
            
            # 找到對應的類別
            found = False
            for category, info in LICENSE_CATEGORIES.items():
                if any(lic in license_name for lic in info['licenses']):
                    categorized[category].append(pkg_name)
                    found = True
                    break
            
            if not found:
                categorized['unknown'].append(pkg_name)
        
        return categorized
    
    def _assess_risks(self, categorized: Dict[str, List[str]]) -> Dict[str, any]:
        """評估風險 / Assess risks"""
        risks = {
            'critical': [],
            'high': [],
            'medium': [],
            'low': []
        }
        
        for category, packages in categorized.items():
            risk_level = LICENSE_CATEGORIES[category]['risk']
            
            if risk_level == 'CRITICAL':
                risks['critical'].extend(packages)
            elif risk_level == 'HIGH':
                risks['high'].extend(packages)
            elif risk_level == 'MEDIUM':
                risks['medium'].extend(packages)
            else:
                risks['low'].extend(packages)
        
        return risks
    
    def generate_report(self) -> str:
        """生成授權報告 / Generate license report"""
        result = self.scan()
        
        report = []
        report.append("=" * 80)
        report.append("📜 LICENSE COMPLIANCE REPORT / 授權合規報告")
        report.append("=" * 80)
        report.append(f"\nTotal packages: {result['total_packages']}")
        report.append(f"總計套件數: {result['total_packages']}\n")
        
        # 按類別顯示
        for category, packages in result['categorized'].items():
            if not packages:
                continue
            
            info = LICENSE_CATEGORIES[category]
            risk_icon = {
                'LOW': '✅',
                'MEDIUM': '🟡',
                'HIGH': '🟠',
                'CRITICAL': '🔴'
            }.get(info['risk'], '⚪')
            
            report.append(f"\n{risk_icon} {category.upper().replace('_', ' ')} ({len(packages)} packages)")
            report.append(f"   Risk: {info['risk']}")
            report.append(f"   {info['description']}")
            report.append("   Packages:")
            
            for pkg in sorted(packages):
                pkg_info = result['packages'][pkg]
                report.append(f"      • {pkg} ({pkg_info['version']}) - {pkg_info['license']}")
        
        # 風險總結
        report.append("\n" + "=" * 80)
        report.append("⚠️  RISK SUMMARY / 風險總結")
        report.append("=" * 80)
        
        if result['risks']['critical']:
            report.append(f"\n🔴 CRITICAL ({len(result['risks']['critical'])}):")
            for pkg in result['risks']['critical']:
                report.append(f"   • {pkg} - Review license terms immediately")
        
        if result['risks']['high']:
            report.append(f"\n🟠 HIGH ({len(result['risks']['high'])}):")
            for pkg in result['risks']['high']:
                pkg_info = result['packages'][pkg]
                report.append(f"   • {pkg} ({pkg_info['license']}) - May require source disclosure")
        
        if result['risks']['medium']:
            report.append(f"\n🟡 MEDIUM ({len(result['risks']['medium'])}):")
            report.append(f"   {len(result['risks']['medium'])} packages - Safe if used as libraries")
        
        report.append("\n" + "=" * 80)
        report.append("📝 RECOMMENDATIONS / 建議:")
        
        if result['risks']['critical'] or result['risks']['high']:
            report.append("   ⚠️  High-risk licenses detected!")
            report.append("   ⚠️  偵測到高風險授權！")
            report.append("   • Consult legal team before distribution")
            report.append("     發布前請諮詢法務團隊")
            report.append("   • Consider replacing GPL packages with MIT alternatives")
            report.append("     考慮將 GPL 套件替換為 MIT 替代品")
        else:
            report.append("   ✅ No high-risk licenses found")
            report.append("   ✅ 未發現高風險授權")
        
        report.append("=" * 80)
        
        return '\n'.join(report)
    
    def generate_licenses_file(self, output_path: Path = None):
        """生成 LICENSES.txt / Generate LICENSES.txt"""
        if output_path is None:
            output_path = self.project_path / 'LICENSES.txt'
        
        result = self.scan()
        
        lines = []
        lines.append("=" * 80)
        lines.append("THIRD-PARTY SOFTWARE LICENSES")
        lines.append("第三方軟體授權")
        lines.append("=" * 80)
        lines.append("")
        
        for pkg_name in sorted(result['packages'].keys()):
            pkg_info = result['packages'][pkg_name]
            lines.append(f"\n{pkg_name} ({pkg_info['version']})")
            lines.append(f"License: {pkg_info['license']}")
            lines.append(f"Author: {pkg_info['author']}")
            lines.append("-" * 80)
        
        content = '\n'.join(lines)
        output_path.write_text(content, encoding='utf-8')
        
        print(f"\n✅ Generated: {output_path}")


if __name__ == '__main__':
    import click
    
    @click.command()
    @click.argument('project_path', type=click.Path(exists=True))
    @click.option('--generate-file', is_flag=True, help='Generate LICENSES.txt')
    def main(project_path, generate_file):
        """Check dependency licenses"""
        path = Path(project_path)
        checker = LicenseChecker(path)
        
        print(checker.generate_report())
        
        if generate_file:
            checker.generate_licenses_file()
    
    main()
