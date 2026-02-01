"""
Security Auditor - 安全檢查員
掃描專案中的安全風險，防止敏感資訊外洩

Security Auditor - Scans projects for security risks and prevents sensitive information leaks
"""

import re
from pathlib import Path
from typing import List, Dict, Tuple
import yaml


class SecurityIssue:
    """安全問題 / Security Issue"""
    
    SEVERITY_CRITICAL = "🔴 CRITICAL"
    SEVERITY_HIGH = "🟠 HIGH"
    SEVERITY_MEDIUM = "🟡 MEDIUM"
    SEVERITY_LOW = "⚪ LOW"
    
    def __init__(self, severity: str, category: str, file_path: Path, 
                 line_number: int, description: str, snippet: str = ""):
        self.severity = severity
        self.category = category
        self.file_path = file_path
        self.line_number = line_number
        self.description = description
        self.snippet = snippet
    
    def __str__(self):
        return f"{self.severity} [{self.category}] {self.file_path}:{self.line_number}\n   {self.description}\n   > {self.snippet[:80]}..."


class SecurityAuditor:
    """安全審計器 / Security Auditor"""
    
    def __init__(self, project_path: Path):
        self.project_path = project_path
        self.issues: List[SecurityIssue] = []
        
        # 敏感模式定義 / Sensitive patterns
        self.patterns = {
            # API Keys
            'openai_key': (
                r'sk-[a-zA-Z0-9]{48}',
                SecurityIssue.SEVERITY_CRITICAL,
                "OpenAI API Key detected"
            ),
            'anthropic_key': (
                r'sk-ant-[a-zA-Z0-9\-]{95}',
                SecurityIssue.SEVERITY_CRITICAL,
                "Anthropic API Key detected"
            ),
            'aws_key': (
                r'AKIA[0-9A-Z]{16}',
                SecurityIssue.SEVERITY_CRITICAL,
                "AWS Access Key detected"
            ),
            'github_token': (
                r'ghp_[a-zA-Z0-9]{36}',
                SecurityIssue.SEVERITY_CRITICAL,
                "GitHub Personal Access Token detected"
            ),
            
            # Generic secrets
            'generic_api_key': (
                r'api[_-]?key[\s]*[=:]["\']\s*[a-zA-Z0-9]{20,}',
                SecurityIssue.SEVERITY_HIGH,
                "Potential API key in code"
            ),
            'password_hardcoded': (
                r'password[\s]*[=:]["\']\s*[^\s"\']{8,}',
                SecurityIssue.SEVERITY_HIGH,
                "Hardcoded password detected"
            ),
            
            # Absolute paths (Windows & Unix)
            'windows_absolute_path': (
                r'[C-Z]:\\Users\\[a-zA-Z0-9_]+',
                SecurityIssue.SEVERITY_MEDIUM,
                "Hardcoded Windows absolute path"
            ),
            'unix_absolute_path': (
                r'/home/[a-zA-Z0-9_]+/',
                SecurityIssue.SEVERITY_MEDIUM,
                "Hardcoded Unix absolute path"
            ),
            
            # Private IPs
            'private_ip': (
                r'192\.168\.\d{1,3}\.\d{1,3}',
                SecurityIssue.SEVERITY_LOW,
                "Private IP address in code"
            ),
            
            # Email addresses (可能是個人信箱)
            'email': (
                r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
                SecurityIssue.SEVERITY_LOW,
                "Email address found (check if personal)"
            ),
        }
    
    def scan(self) -> List[SecurityIssue]:
        """
        執行完整掃描 / Run full security scan
        
        Returns:
            List of security issues found
        """
        print(f"🔍 Scanning {self.project_path} for security issues...")
        print("   正在掃描安全風險...\n")
        
        # 掃描所有文字檔案
        for file_path in self.project_path.rglob('*'):
            if file_path.is_file() and self._is_text_file(file_path):
                self._scan_file(file_path)
        
        # 檢查特定檔案是否存在
        self._check_sensitive_files()
        
        # 檢查檔案權限（Unix-like 系統）
        self._check_file_permissions()
        
        return self.issues
    
    def _scan_file(self, file_path: Path):
        """掃描單一檔案 / Scan a single file"""
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            lines = content.split('\n')
            
            for line_num, line in enumerate(lines, 1):
                for pattern_name, (regex, severity, description) in self.patterns.items():
                    matches = re.finditer(regex, line, re.IGNORECASE)
                    for match in matches:
                        # 跳過註解中的範例（可能是文件說明）
                        if self._is_in_comment(line, match.start()):
                            continue
                        
                        issue = SecurityIssue(
                            severity=severity,
                            category=pattern_name,
                            file_path=file_path.relative_to(self.project_path),
                            line_number=line_num,
                            description=description,
                            snippet=line.strip()
                        )
                        self.issues.append(issue)
        
        except Exception as e:
            print(f"   ⚠️  無法掃描 {file_path}: {e}")
    
    def _is_text_file(self, file_path: Path) -> bool:
        """判斷是否為文字檔案 / Check if file is text"""
        text_extensions = {
            '.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.cpp', '.c', '.h',
            '.go', '.rs', '.rb', '.php', '.cs', '.swift', '.kt',
            '.html', '.css', '.scss', '.sass', '.less',
            '.json', '.yaml', '.yml', '.toml', '.xml', '.ini', '.cfg',
            '.md', '.txt', '.rst', '.sh', '.bash', '.zsh',
            '.env', '.gitignore', '.dockerignore'
        }
        return file_path.suffix.lower() in text_extensions
    
    def _is_in_comment(self, line: str, position: int) -> bool:
        """檢查是否在註解中 / Check if position is in a comment"""
        # 簡化版：檢查該行是否以 # 或 // 開頭
        stripped = line.strip()
        return stripped.startswith('#') or stripped.startswith('//')
    
    def _check_sensitive_files(self):
        """檢查是否存在敏感檔案 / Check for sensitive files"""
        sensitive_files = [
            '.env', '.env.local', '.env.production',
            'secrets.yaml', 'credentials.json',
            'id_rsa', 'id_ed25519', '*.pem', '*.key'
        ]
        
        for pattern in sensitive_files:
            matches = list(self.project_path.glob(f"**/{pattern}"))
            for file_path in matches:
                issue = SecurityIssue(
                    severity=SecurityIssue.SEVERITY_CRITICAL,
                    category="sensitive_file",
                    file_path=file_path.relative_to(self.project_path),
                    line_number=0,
                    description=f"Sensitive file should not be committed: {file_path.name}",
                    snippet=""
                )
                self.issues.append(issue)
    
    def _check_file_permissions(self):
        """檢查檔案權限 / Check file permissions (Unix-like only)"""
        import stat
        import os
        
        if os.name != 'posix':
            return  # Windows 不適用
        
        for file_path in self.project_path.rglob('*'):
            if file_path.is_file():
                mode = file_path.stat().st_mode
                # 檢查是否所有人可寫
                if mode & stat.S_IWOTH:
                    issue = SecurityIssue(
                        severity=SecurityIssue.SEVERITY_MEDIUM,
                        category="file_permission",
                        file_path=file_path.relative_to(self.project_path),
                        line_number=0,
                        description="File is world-writable (chmod 666 or 777)",
                        snippet=oct(stat.S_IMODE(mode))
                    )
                    self.issues.append(issue)
    
    def generate_report(self) -> str:
        """
        生成報告 / Generate security report
        
        Returns:
            Formatted report string
        """
        if not self.issues:
            return "✅ No security issues found!\n   未發現安全問題！"
        
        # 按嚴重程度分組
        by_severity = {
            SecurityIssue.SEVERITY_CRITICAL: [],
            SecurityIssue.SEVERITY_HIGH: [],
            SecurityIssue.SEVERITY_MEDIUM: [],
            SecurityIssue.SEVERITY_LOW: []
        }
        
        for issue in self.issues:
            by_severity[issue.severity].append(issue)
        
        report = []
        report.append("=" * 80)
        report.append("🛡️  SECURITY AUDIT REPORT / 安全審計報告")
        report.append("=" * 80)
        report.append(f"\nTotal Issues Found: {len(self.issues)}")
        report.append(f"總計發現問題: {len(self.issues)}\n")
        
        for severity in [SecurityIssue.SEVERITY_CRITICAL, SecurityIssue.SEVERITY_HIGH,
                        SecurityIssue.SEVERITY_MEDIUM, SecurityIssue.SEVERITY_LOW]:
            issues = by_severity[severity]
            if issues:
                report.append(f"\n{severity} ({len(issues)} issues):")
                report.append("-" * 80)
                for issue in issues:
                    report.append(str(issue))
                    report.append("")
        
        report.append("=" * 80)
        report.append("\n⚠️  RECOMMENDATIONS / 建議:")
        report.append("1. Remove all hardcoded secrets and use environment variables")
        report.append("   移除所有硬編碼的密鑰，改用環境變數")
        report.append("2. Add sensitive files to .gitignore")
        report.append("   將敏感檔案加入 .gitignore")
        report.append("3. Use relative paths instead of absolute paths")
        report.append("   使用相對路徑而非絕對路徑")
        report.append("=" * 80)
        
        return "\n".join(report)


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python security_auditor.py <project_path>")
        print("用法: python security_auditor.py <專案路徑>")
        sys.exit(1)
    
    project_path = Path(sys.argv[1])
    
    if not project_path.exists():
        print(f"❌ Project not found: {project_path}")
        print(f"❌ 專案不存在: {project_path}")
        sys.exit(1)
    
    auditor = SecurityAuditor(project_path)
    issues = auditor.scan()
    
    print(auditor.generate_report())
    
    # 如果有 CRITICAL 問題，返回錯誤碼
    has_critical = any(i.severity == SecurityIssue.SEVERITY_CRITICAL for i in issues)
    sys.exit(1 if has_critical else 0)
