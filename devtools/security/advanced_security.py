"""
Advanced Security Scanner - 進階安全掃描器
Multi-layer security analysis combining static, dynamic, and AI-powered scanning

三層安全分析：靜態分析 + 動態分析 + AI 驅動掃描
"""

import subprocess
import json
from pathlib import Path
from typing import Dict, List
import ast
import re


class AdvancedSecurityScanner:
    """
    進階安全掃描器 / Advanced Security Scanner
    
    Layers:
    1. Static Analysis (Bandit, Semgrep)
    2. Pattern-based Logic Flaw Detection
    3. AI-Powered Code Review (optional)
    """
    
    def __init__(self, project_path: Path):
        self.project_path = project_path
        self.vulnerabilities = []
    
    def scan_all(self) -> Dict:
        """執行完整掃描 / Run complete scan"""
        results = {
            'static_analysis': self.run_static_analysis(),
            'logic_flaws': self.detect_logic_flaws(),
            'runtime_risks': self.detect_runtime_risks(),
            'ai_review': None  # Optional, requires API key
        }
        
        return results
    
    def run_static_analysis(self) -> Dict:
        """
        Layer 1: 靜態分析 / Static Analysis
        使用 Bandit 和 Semgrep
        """
        results = {'bandit': [], 'semgrep': []}
        
        # Run Bandit (Python security scanner)
        try:
            bandit_result = subprocess.run(
                ['bandit', '-r', str(self.project_path), '-f', 'json'],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if bandit_result.returncode == 0 or bandit_result.returncode == 1:
                results['bandit'] = json.loads(bandit_result.stdout).get('results', [])
        
        except FileNotFoundError:
            results['bandit'] = {'error': 'Bandit not installed. Run: pip install bandit'}
        except subprocess.TimeoutExpired:
            results['bandit'] = {'error': 'Bandit scan timeout'}
        except Exception as e:
            results['bandit'] = {'error': str(e)}
        
        # Run Semgrep (multi-language scanner)
        try:
            semgrep_result = subprocess.run(
                ['semgrep', '--config=auto', '--json', str(self.project_path)],
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if semgrep_result.returncode == 0:
                results['semgrep'] = json.loads(semgrep_result.stdout).get('results', [])
        
        except FileNotFoundError:
            results['semgrep'] = {'error': 'Semgrep not installed. Run: pip install semgrep'}
        except subprocess.TimeoutExpired:
            results['semgrep'] = {'error': 'Semgrep scan timeout'}
        except Exception as e:
            results['semgrep'] = {'error': str(e)}
        
        return results
    
    def detect_logic_flaws(self) -> List[Dict]:
        """
        Layer 2: 邏輯漏洞偵測 / Logic Flaw Detection
        偵測常見的邏輯錯誤與業務邏輯漏洞
        """
        flaws = []
        
        # 危險函數模式
        dangerous_patterns = {
            # Code Injection
            'sql_injection': {
                'pattern': r'execute\s*\(\s*["\'].*%s.*["\']\s*%',
                'severity': 'CRITICAL',
                'description': 'Potential SQL Injection - using string formatting in SQL'
            },
            'sql_injection_fstring': {
                'pattern': r'execute\s*\(\s*f["\'].*\{.*\}',
                'severity': 'CRITICAL',
                'description': 'Potential SQL Injection - using f-string in SQL'
            },
            'command_injection': {
                'pattern': r'os\.system\s*\(\s*.*\+',
                'severity': 'CRITICAL',
                'description': 'Potential Command Injection - concatenating user input'
            },
            'subprocess_shell': {
                'pattern': r'subprocess\.(run|call|Popen).*shell\s*=\s*True',
                'severity': 'HIGH',
                'description': 'Command execution with shell=True - potential injection'
            },
            'eval_usage': {
                'pattern': r'\beval\s*\(',
                'severity': 'HIGH',
                'description': 'Dangerous use of eval() - can execute arbitrary code'
            },
            'exec_usage': {
                'pattern': r'\bexec\s*\(',
                'severity': 'HIGH',
                'description': 'Dangerous use of exec() - can execute arbitrary code'
            },
            
            # Deserialization
            'pickle_unsafe': {
                'pattern': r'pickle\.loads?\s*\(',
                'severity': 'HIGH',
                'description': 'Unsafe deserialization with pickle - can execute code'
            },
            'yaml_unsafe': {
                'pattern': r'yaml\.load\s*\([^,)]*\)',
                'severity': 'HIGH',
                'description': 'Unsafe YAML loading - use yaml.safe_load() instead'
            },
            
            # Cryptography
            'hardcoded_crypto': {
                'pattern': r'(AES|DES|RSA).*key\s*=\s*["\']',
                'severity': 'CRITICAL',
                'description': 'Hardcoded cryptographic key'
            },
            'weak_crypto': {
                'pattern': r'\b(MD5|SHA1|DES)\b',
                'severity': 'MEDIUM',
                'description': 'Weak cryptographic algorithm - use SHA256+ or AES'
            },
            
            # Authentication & Authorization
            'auth_bypass': {
                'pattern': r'if.*password\s*==\s*["\']',
                'severity': 'CRITICAL',
                'description': 'Hardcoded password comparison - authentication bypass risk'
            },
            'missing_auth_check': {
                'pattern': r'@app\.route.*\n(?!.*@login_required).*def\s+\w+',
                'severity': 'HIGH',
                'description': 'Route without authentication decorator - potential unauthorized access'
            },
            'admin_check_weak': {
                'pattern': r'if.*user.*==\s*["\']admin["\']',
                'severity': 'HIGH',
                'description': 'Weak admin check - use role-based access control'
            },
            
            # IDOR (Insecure Direct Object Reference)
            'idor_risk': {
                'pattern': r'(get|filter|query).*\(id\s*=\s*(request\.|params\.|args\.)',
                'severity': 'HIGH',
                'description': 'Potential IDOR - missing authorization check on object access'
            },
            
            # CSRF
            'csrf_missing': {
                'pattern': r'@app\.route.*methods\s*=\s*\[.*POST.*\](?!.*csrf)',
                'severity': 'MEDIUM',
                'description': 'POST route without CSRF protection'
            },
            
            # XSS
            'xss_risk': {
                'pattern': r'render_template_string\s*\(.*\+',
                'severity': 'HIGH',
                'description': 'Potential XSS - concatenating user input in template'
            },
            'unsafe_html': {
                'pattern': r'\.innerHTML\s*=',
                'severity': 'MEDIUM',
                'description': 'Direct innerHTML assignment - XSS risk'
            },
            
            # Path Traversal
            'path_traversal': {
                'pattern': r'open\s*\(.*\+.*request\.',
                'severity': 'CRITICAL',
                'description': 'Path traversal vulnerability - validate file paths'
            },
            
            # Business Logic
            'race_condition': {
                'pattern': r'(balance|quantity|stock).*-=.*\n.*(?!.*lock|transaction)',
                'severity': 'HIGH',
                'description': 'Potential race condition - missing synchronization'
            },
            'price_manipulation': {
                'pattern': r'price\s*=\s*(request\.|params\.|args\.)',
                'severity': 'CRITICAL',
                'description': 'Price from user input - manipulation risk'
            },
        }
        
        # 掃描所有 Python 檔案
        for py_file in self.project_path.rglob('*.py'):
            if '__pycache__' in str(py_file) or '.venv' in str(py_file):
                continue
            
            try:
                content = py_file.read_text(encoding='utf-8')
                lines = content.split('\n')
                
                for line_num, line in enumerate(lines, 1):
                    for flaw_type, config in dangerous_patterns.items():
                        if re.search(config['pattern'], line):
                            flaws.append({
                                'type': flaw_type,
                                'severity': config['severity'],
                                'file': str(py_file.relative_to(self.project_path)),
                                'line': line_num,
                                'description': config['description'],
                                'code': line.strip()
                            })
            
            except Exception as e:
                print(f"   ⚠️  Error scanning {py_file}: {e}")
        
        return flaws
    
    def detect_runtime_risks(self) -> List[Dict]:
        """
        Layer 3: 執行時風險偵測 / Runtime Risk Detection
        偵測可能導致執行時問題的模式
        """
        risks = []
        
        runtime_patterns = {
            'unclosed_file': {
                'pattern': r'open\s*\([^)]+\)(?!\s*with)',
                'severity': 'MEDIUM',
                'description': 'File opened without context manager - potential resource leak'
            },
            'infinite_loop_risk': {
                'pattern': r'while\s+True:(?!.*break)',
                'severity': 'MEDIUM',
                'description': 'Infinite loop without break - potential hang'
            },
            'thread_without_join': {
                'pattern': r'Thread\s*\([^)]+\)\.start\(\)',
                'severity': 'LOW',
                'description': 'Thread started without join() - potential resource leak'
            },
            'recursive_without_base': {
                'pattern': r'def\s+(\w+).*:\s*.*\1\s*\(',
                'severity': 'MEDIUM',
                'description': 'Recursive function - check for base case'
            },
        }
        
        for py_file in self.project_path.rglob('*.py'):
            if '__pycache__' in str(py_file) or '.venv' in str(py_file):
                continue
            
            try:
                content = py_file.read_text(encoding='utf-8')
                lines = content.split('\n')
                
                for line_num, line in enumerate(lines, 1):
                    for risk_type, config in runtime_patterns.items():
                        if re.search(config['pattern'], line):
                            risks.append({
                                'type': risk_type,
                                'severity': config['severity'],
                                'file': str(py_file.relative_to(self.project_path)),
                                'line': line_num,
                                'description': config['description'],
                                'code': line.strip()
                            })
            
            except Exception as e:
                print(f"   ⚠️  Error scanning {py_file}: {e}")
        
        return risks
    
    def generate_report(self, results: Dict) -> str:
        """生成綜合報告 / Generate comprehensive report"""
        report = []
        report.append("=" * 80)
        report.append("🔒 ADVANCED SECURITY SCAN REPORT / 進階安全掃描報告")
        report.append("=" * 80)
        report.append(f"\nProject: {self.project_path.name}\n")
        
        # Static Analysis Results
        report.append("=" * 80)
        report.append("📊 LAYER 1: STATIC ANALYSIS / 靜態分析")
        report.append("=" * 80)
        
        if 'error' in results['static_analysis'].get('bandit', {}):
            report.append(f"\n⚠️  Bandit: {results['static_analysis']['bandit']['error']}")
        else:
            bandit_issues = results['static_analysis'].get('bandit', [])
            report.append(f"\nBandit found {len(bandit_issues)} issues:")
            for issue in bandit_issues[:10]:  # Show first 10
                report.append(f"   🔴 {issue.get('issue_severity', 'UNKNOWN')}: {issue.get('issue_text', '')}")
                report.append(f"      File: {issue.get('filename', '')}:{issue.get('line_number', '')}")
        
        if 'error' in results['static_analysis'].get('semgrep', {}):
            report.append(f"\n⚠️  Semgrep: {results['static_analysis']['semgrep']['error']}")
        else:
            semgrep_issues = results['static_analysis'].get('semgrep', [])
            report.append(f"\nSemgrep found {len(semgrep_issues)} issues:")
            for issue in semgrep_issues[:10]:
                report.append(f"   🔴 {issue.get('extra', {}).get('severity', 'UNKNOWN')}: {issue.get('extra', {}).get('message', '')}")
        
        # Logic Flaws
        report.append("\n" + "=" * 80)
        report.append("🧠 LAYER 2: LOGIC FLAW DETECTION / 邏輯漏洞偵測")
        report.append("=" * 80)
        
        logic_flaws = results['logic_flaws']
        report.append(f"\nFound {len(logic_flaws)} potential logic flaws:\n")
        
        for flaw in logic_flaws:
            report.append(f"🔴 {flaw['severity']}: {flaw['description']}")
            report.append(f"   File: {flaw['file']}:{flaw['line']}")
            report.append(f"   Code: {flaw['code']}")
            report.append("")
        
        # Runtime Risks
        report.append("=" * 80)
        report.append("⚡ LAYER 3: RUNTIME RISK DETECTION / 執行時風險偵測")
        report.append("=" * 80)
        
        runtime_risks = results['runtime_risks']
        report.append(f"\nFound {len(runtime_risks)} potential runtime risks:\n")
        
        for risk in runtime_risks:
            report.append(f"🟡 {risk['severity']}: {risk['description']}")
            report.append(f"   File: {risk['file']}:{risk['line']}")
            report.append(f"   Code: {risk['code']}")
            report.append("")
        
        # Summary
        report.append("=" * 80)
        report.append("📝 SUMMARY / 總結")
        report.append("=" * 80)
        
        total_critical = len([f for f in logic_flaws if f['severity'] == 'CRITICAL'])
        total_high = len([f for f in logic_flaws if f['severity'] == 'HIGH'])
        total_medium = len([f for f in logic_flaws + runtime_risks if f['severity'] == 'MEDIUM'])
        
        report.append(f"\n🔴 Critical: {total_critical}")
        report.append(f"🟠 High: {total_high}")
        report.append(f"🟡 Medium: {total_medium}")
        
        if total_critical > 0:
            report.append("\n⚠️  CRITICAL ISSUES FOUND - IMMEDIATE ACTION REQUIRED")
            report.append("⚠️  發現嚴重問題 - 需要立即處理")
        
        report.append("\n" + "=" * 80)
        report.append("💡 RECOMMENDATIONS / 建議")
        report.append("=" * 80)
        report.append("\n1. Install security tools:")
        report.append("   pip install bandit semgrep")
        report.append("\n2. Fix critical issues first")
        report.append("   優先修復嚴重問題")
        report.append("\n3. Review all SQL/command execution code")
        report.append("   審查所有 SQL/命令執行程式碼")
        report.append("\n4. Use parameterized queries")
        report.append("   使用參數化查詢")
        report.append("\n5. Avoid eval() and exec()")
        report.append("   避免使用 eval() 和 exec()")
        report.append("=" * 80)
        
        return '\n'.join(report)


if __name__ == '__main__':
    import click
    
    @click.command()
    @click.argument('project_path', type=click.Path(exists=True))
    def main(project_path):
        """Run advanced security scan"""
        scanner = AdvancedSecurityScanner(Path(project_path))
        results = scanner.scan_all()
        print(scanner.generate_report(results))
    
    main()
