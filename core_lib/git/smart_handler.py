"""
Smart Git Handler
=================

Advanced Git intelligence for automatic tagging and change analysis.
用於自動標籤和變更分析的高級 Git 智能。
"""

import subprocess
import re
from typing import Dict, Any, List, Optional
from pathlib import Path
from .automation import GitAutomation


class SmartGitHandler:
    """Intelligent Git operations handler."""
    
    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path).resolve()
        self.automation = GitAutomation(repo_path)
        
    def analyze_changes(self) -> Dict[str, Any]:
        """
        Analyze staged changes and suggest a commit type.
        分析暫存的變更並建議提交類型。
        """
        staged_files = self._get_staged_files()
        if not staged_files:
            return {'suggestion': 'chore', 'reason': 'No changes found'}
            
        extensions = {Path(f).suffix for f in staged_files}
        paths = {str(Path(f).parent) for f in staged_files}
        
        # Simple heuristic analysis
        if all(f.endswith('.md') for f in staged_files):
            return {'suggestion': 'docs', 'reason': 'Only documentation files changed'}
            
        if any('tests' in p for p in paths):
            return {'suggestion': 'test', 'reason': 'Test files involved'}
            
        if any(p.startswith('core_lib') or p.startswith('agents') for p in paths):
            return {'suggestion': 'feat', 'reason': 'Core implementation change'}
            
        return {'suggestion': 'chore', 'reason': 'General maintenance'}

    def suggest_next_tag(self) -> str:
        """
        Calculate the next version tag based on commit history since last tag.
        根據自上次標籤以來的提交歷史計算下一個版本標籤。
        """
        last_tag = self._get_last_tag()
        if not last_tag:
            return "v1.0.0"
            
        commits = self._get_commits_since_tag(last_tag)
        if not commits:
            return last_tag
            
        major, minor, patch = self._parse_tag(last_tag)
        
        increment = "patch"
        for commit in commits:
            # Strip hash if present (from --oneline)
            msg = re.sub(r'^[a-f0-9]+\s+', '', commit)
            
            if "BC:" in msg or "BREAKING CHANGE" in msg:
                increment = "major"
                break
            if msg.startswith("feat:") or msg.startswith("refactor:"):
                if increment != "major":
                    increment = "minor"
                    
        if increment == "major":
            return f"v{major + 1}.0.0"
        elif increment == "minor":
            return f"v{major}.{minor + 1}.0"
        else:
            return f"v{major}.{minor}.{patch + 1}"

    def apply_smart_tag(self, message: str = "") -> Dict[str, Any]:
        """Apply the suggested tag automatically."""
        next_tag = self.suggest_next_tag()
        last_tag = self._get_last_tag()
        
        if next_tag == last_tag:
            return {'success': False, 'error': 'No new changes to tag'}
            
        try:
            cmd = ['git', 'tag', '-a', next_tag, '-m', message or f"Automated Release {next_tag}"]
            subprocess.run(cmd, cwd=self.repo_path, check=True, capture_output=True, text=True)
            return {'success': True, 'tag': next_tag}
        except subprocess.CalledProcessError as e:
            return {'success': False, 'error': e.stderr}

    def _get_staged_files(self) -> List[str]:
        result = subprocess.run(
            ['git', 'diff', '--cached', '--name-only'],
            cwd=self.repo_path, capture_output=True, text=True
        )
        return result.stdout.strip().split('\n') if result.stdout.strip() else []

    def _get_last_tag(self) -> Optional[str]:
        try:
            result = subprocess.run(
                ['git', 'describe', '--tags', '--abbrev=0'],
                cwd=self.repo_path, capture_output=True, text=True
            )
            return result.stdout.strip()
        except:
            return None

    def _get_commits_since_tag(self, tag: str) -> List[str]:
        result = subprocess.run(
            ['git', 'log', f'{tag}..HEAD', '--oneline'],
            cwd=self.repo_path, capture_output=True, text=True
        )
        return result.stdout.strip().split('\n') if result.stdout.strip() else []

    def _parse_tag(self, tag: str) -> tuple:
        match = re.match(r'v(\d+)\.(\d+)\.(\d+)', tag)
        if match:
            return tuple(map(int, match.groups()))
        return (0, 0, 0)
