"""
Git Automation Tools
====================

Automate common Git operations like commit and PR creation.
自動化常見的 Git 操作，如提交和 PR 創建。
"""

import subprocess
from typing import Dict, Any, List, Optional
from pathlib import Path


class GitAutomation:
    """Git automation utilities."""
    
    def __init__(self, repo_path: str = "."):
        """
        Initialize Git automation.
        
        Args:
            repo_path: Path to the Git repository
        """
        self.repo_path = Path(repo_path).resolve()
    
    def auto_commit(
        self,
        files: Optional[List[str]] = None,
        message: str = "",
        add_all: bool = False
    ) -> Dict[str, Any]:
        """
        Automatically commit changes.
        自動提交變更。
        
        Args:
            files: List of files to commit (None = use add_all)
            message: Commit message
            add_all: If True, add all changed files
            
        Returns:
            {
                'success': bool,
                'commit_hash': str,
                'files_committed': List[str],
                'errors': List[str]
            }
        """
        result = {
            'success': False,
            'commit_hash': '',
            'files_committed': [],
            'errors': []
        }
        
        try:
            # Stage files
            if add_all:
                subprocess.run(
                    ['git', 'add', '-A'],
                    cwd=self.repo_path,
                    check=True,
                    capture_output=True,
                    text=True
                )
                result['files_committed'] = self._get_staged_files()
            elif files:
                for file in files:
                    subprocess.run(
                        ['git', 'add', file],
                        cwd=self.repo_path,
                        check=True,
                        capture_output=True,
                        text=True
                    )
                result['files_committed'] = files
            else:
                result['errors'].append("No files specified and add_all=False")
                return result
            
            # Commit
            if not message:
                message = "Auto-commit: Update files"
            
            commit_result = subprocess.run(
                ['git', 'commit', '-m', message],
                cwd=self.repo_path,
                check=True,
                capture_output=True,
                text=True
            )
            
            # Get commit hash
            hash_result = subprocess.run(
                ['git', 'rev-parse', 'HEAD'],
                cwd=self.repo_path,
                check=True,
                capture_output=True,
                text=True
            )
            
            result['success'] = True
            result['commit_hash'] = hash_result.stdout.strip()
            
        except subprocess.CalledProcessError as e:
            result['errors'].append(f"Git command failed: {e.stderr}")
        except Exception as e:
            result['errors'].append(f"Unexpected error: {str(e)}")
        
        return result
    
    def create_pr(
        self,
        title: str,
        body: str = "",
        base_branch: str = "main",
        head_branch: str = "",
        draft: bool = False
    ) -> Dict[str, Any]:
        """
        Create a pull request using GitHub CLI.
        使用 GitHub CLI 創建 Pull Request。
        
        Args:
            title: PR title
            body: PR description
            base_branch: Target branch (default: main)
            head_branch: Source branch (default: current branch)
            draft: Create as draft PR
            
        Returns:
            {
                'success': bool,
                'pr_url': str,
                'pr_number': int,
                'errors': List[str]
            }
        """
        result = {
            'success': False,
            'pr_url': '',
            'pr_number': 0,
            'errors': []
        }
        
        try:
            # Get current branch if not specified
            if not head_branch:
                branch_result = subprocess.run(
                    ['git', 'branch', '--show-current'],
                    cwd=self.repo_path,
                    check=True,
                    capture_output=True,
                    text=True
                )
                head_branch = branch_result.stdout.strip()
            
            # Build gh pr create command
            cmd = [
                'gh', 'pr', 'create',
                '--title', title,
                '--base', base_branch,
                '--head', head_branch
            ]
            
            if body:
                cmd.extend(['--body', body])
            
            if draft:
                cmd.append('--draft')
            
            # Create PR
            pr_result = subprocess.run(
                cmd,
                cwd=self.repo_path,
                check=True,
                capture_output=True,
                text=True
            )
            
            # Parse PR URL from output
            pr_url = pr_result.stdout.strip()
            result['pr_url'] = pr_url
            
            # Extract PR number from URL
            if pr_url:
                pr_number = pr_url.split('/')[-1]
                result['pr_number'] = int(pr_number)
            
            result['success'] = True
            
        except subprocess.CalledProcessError as e:
            result['errors'].append(f"GitHub CLI command failed: {e.stderr}")
        except Exception as e:
            result['errors'].append(f"Unexpected error: {str(e)}")
        
        return result
    
    def push_branch(
        self,
        branch: str = "",
        force: bool = False,
        set_upstream: bool = True
    ) -> Dict[str, Any]:
        """
        Push branch to remote.
        推送分支到遠端。
        
        Args:
            branch: Branch name (default: current branch)
            force: Force push
            set_upstream: Set upstream tracking
            
        Returns:
            {
                'success': bool,
                'branch': str,
                'errors': List[str]
            }
        """
        result = {
            'success': False,
            'branch': '',
            'errors': []
        }
        
        try:
            # Get current branch if not specified
            if not branch:
                branch_result = subprocess.run(
                    ['git', 'branch', '--show-current'],
                    cwd=self.repo_path,
                    check=True,
                    capture_output=True,
                    text=True
                )
                branch = branch_result.stdout.strip()
            
            result['branch'] = branch
            
            # Build push command
            cmd = ['git', 'push']
            
            if set_upstream:
                cmd.extend(['--set-upstream', 'origin', branch])
            else:
                cmd.extend(['origin', branch])
            
            if force:
                cmd.append('--force')
            
            # Push
            subprocess.run(
                cmd,
                cwd=self.repo_path,
                check=True,
                capture_output=True,
                text=True
            )
            
            result['success'] = True
            
        except subprocess.CalledProcessError as e:
            result['errors'].append(f"Git push failed: {e.stderr}")
        except Exception as e:
            result['errors'].append(f"Unexpected error: {str(e)}")
        
        return result
    
    def _get_staged_files(self) -> List[str]:
        """Get list of staged files."""
        try:
            result = subprocess.run(
                ['git', 'diff', '--cached', '--name-only'],
                cwd=self.repo_path,
                check=True,
                capture_output=True,
                text=True
            )
            return result.stdout.strip().split('\n') if result.stdout.strip() else []
        except Exception:
            return []


# Convenience functions
def auto_commit_and_push(
    message: str,
    files: Optional[List[str]] = None,
    add_all: bool = False,
    repo_path: str = "."
) -> Dict[str, Any]:
    """
    Commit and push in one operation.
    一次操作完成提交和推送。
    
    Args:
        message: Commit message
        files: Files to commit
        add_all: Add all changed files
        repo_path: Repository path
        
    Returns:
        {
            'success': bool,
            'commit_hash': str,
            'push_success': bool,
            'errors': List[str]
        }
    """
    git = GitAutomation(repo_path)
    
    # Commit
    commit_result = git.auto_commit(files=files, message=message, add_all=add_all)
    
    if not commit_result['success']:
        return {
            'success': False,
            'commit_hash': '',
            'push_success': False,
            'errors': commit_result['errors']
        }
    
    # Push
    push_result = git.push_branch()
    
    return {
        'success': commit_result['success'] and push_result['success'],
        'commit_hash': commit_result['commit_hash'],
        'push_success': push_result['success'],
        'errors': commit_result['errors'] + push_result['errors']
    }


def create_feature_pr(
    feature_name: str,
    description: str = "",
    base_branch: str = "main",
    repo_path: str = "."
) -> Dict[str, Any]:
    """
    Create a feature PR with standard naming.
    創建標準命名的功能 PR。
    
    Args:
        feature_name: Feature name
        description: Feature description
        base_branch: Target branch
        repo_path: Repository path
        
    Returns:
        PR creation result
    """
    git = GitAutomation(repo_path)
    
    title = f"feat: {feature_name}"
    body = description or f"Implement {feature_name}"
    
    return git.create_pr(
        title=title,
        body=body,
        base_branch=base_branch
    )
