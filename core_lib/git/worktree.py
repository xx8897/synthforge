"""
Git Worktree Manager
====================

Manage Git worktrees for isolated development.

This module provides:
- Worktree creation
- Worktree cleanup
- Branch management
- Isolation for parallel development

Usage:
    from core_lib.git.worktree import GitWorktreeManager
    
    manager = GitWorktreeManager()
    worktree_path = manager.create_worktree('feature/new-feature')
    # ... do work in worktree ...
    manager.cleanup_worktree(worktree_path)
"""

import subprocess
from pathlib import Path
from typing import Dict, Any, Optional
import tempfile
import shutil


class GitWorktreeError(Exception):
    """Git worktree operation error."""
    pass


class GitWorktreeManager:
    """Manage Git worktrees for isolated development."""
    
    def __init__(self, repo_path: str = '.'):
        """
        Initialize Git worktree manager.
        
        Args:
            repo_path: Path to Git repository
        """
        self.repo_path = Path(repo_path).resolve()
        self._verify_git_repo()
    
    def _verify_git_repo(self):
        """Verify that repo_path is a Git repository."""
        git_dir = self.repo_path / '.git'
        if not git_dir.exists():
            raise GitWorktreeError(f"Not a Git repository: {self.repo_path}")
    
    def create_worktree(
        self,
        branch_name: str,
        base_branch: str = 'main',
        worktree_dir: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a new Git worktree.
        
        Args:
            branch_name: Name of the new branch
            base_branch: Base branch to branch from
            worktree_dir: Optional custom worktree directory
            
        Returns:
            {
                'success': bool,
                'worktree_path': str,
                'branch_name': str,
                'errors': List[str]
            }
        """
        result = {
            'success': True,
            'worktree_path': '',
            'branch_name': branch_name,
            'errors': []
        }
        
        try:
            # Determine worktree path
            if worktree_dir:
                worktree_path = Path(worktree_dir)
            else:
                # Create in .worktrees/ directory
                worktrees_dir = self.repo_path / '.worktrees'
                worktrees_dir.mkdir(exist_ok=True)
                worktree_path = worktrees_dir / branch_name.replace('/', '_')
            
            # Check if worktree already exists
            if worktree_path.exists():
                result['success'] = False
                result['errors'].append(f"Worktree already exists: {worktree_path}")
                return result
            
            # Create worktree
            cmd = [
                'git', 'worktree', 'add',
                '-b', branch_name,
                str(worktree_path),
                base_branch
            ]
            
            process = subprocess.run(
                cmd,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            result['worktree_path'] = str(worktree_path)
            
        except subprocess.CalledProcessError as e:
            result['success'] = False
            result['errors'].append(f"Git worktree creation failed: {e.stderr}")
        
        except Exception as e:
            result['success'] = False
            result['errors'].append(f"Unexpected error: {e}")
        
        return result
    
    def cleanup_worktree(
        self,
        worktree_path: str,
        force: bool = False
    ) -> Dict[str, Any]:
        """
        Remove a Git worktree.
        
        Args:
            worktree_path: Path to worktree to remove
            force: Force removal even with uncommitted changes
            
        Returns:
            {
                'success': bool,
                'removed': bool,
                'errors': List[str]
            }
        """
        result = {
            'success': True,
            'removed': False,
            'errors': []
        }
        
        try:
            worktree_path = Path(worktree_path)
            
            if not worktree_path.exists():
                result['errors'].append(f"Worktree does not exist: {worktree_path}")
                return result
            
            # Remove worktree
            cmd = ['git', 'worktree', 'remove', str(worktree_path)]
            if force:
                cmd.append('--force')
            
            process = subprocess.run(
                cmd,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            result['removed'] = True
            
        except subprocess.CalledProcessError as e:
            result['success'] = False
            result['errors'].append(f"Git worktree removal failed: {e.stderr}")
        
        except Exception as e:
            result['success'] = False
            result['errors'].append(f"Unexpected error: {e}")
        
        return result
    
    def list_worktrees(self) -> Dict[str, Any]:
        """
        List all Git worktrees.
        
        Returns:
            {
                'success': bool,
                'worktrees': List[Dict],
                'errors': List[str]
            }
        """
        result = {
            'success': True,
            'worktrees': [],
            'errors': []
        }
        
        try:
            cmd = ['git', 'worktree', 'list', '--porcelain']
            
            process = subprocess.run(
                cmd,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            # Parse output
            worktrees = []
            current_worktree = {}
            
            for line in process.stdout.strip().split('\n'):
                if line.startswith('worktree '):
                    if current_worktree:
                        worktrees.append(current_worktree)
                    current_worktree = {'path': line.split(' ', 1)[1]}
                elif line.startswith('branch '):
                    current_worktree['branch'] = line.split(' ', 1)[1]
                elif line.startswith('HEAD '):
                    current_worktree['head'] = line.split(' ', 1)[1]
            
            if current_worktree:
                worktrees.append(current_worktree)
            
            result['worktrees'] = worktrees
            
        except subprocess.CalledProcessError as e:
            result['success'] = False
            result['errors'].append(f"Failed to list worktrees: {e.stderr}")
        
        except Exception as e:
            result['success'] = False
            result['errors'].append(f"Unexpected error: {e}")
        
        return result
    
    def prune_worktrees(self) -> Dict[str, Any]:
        """
        Prune stale worktree information.
        
        Returns:
            {
                'success': bool,
                'pruned': int,
                'errors': List[str]
            }
        """
        result = {
            'success': True,
            'pruned': 0,
            'errors': []
        }
        
        try:
            cmd = ['git', 'worktree', 'prune', '-v']
            
            process = subprocess.run(
                cmd,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            # Count pruned worktrees
            result['pruned'] = len([
                line for line in process.stdout.split('\n')
                if 'Removing worktrees' in line
            ])
            
        except subprocess.CalledProcessError as e:
            result['success'] = False
            result['errors'].append(f"Failed to prune worktrees: {e.stderr}")
        
        except Exception as e:
            result['success'] = False
            result['errors'].append(f"Unexpected error: {e}")
        
        return result


if __name__ == '__main__':
    # Standalone testing
    import sys
    import json
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python git_worktree.py create <branch_name> [base_branch]")
        print("  python git_worktree.py cleanup <worktree_path>")
        print("  python git_worktree.py list")
        print("  python git_worktree.py prune")
        sys.exit(1)
    
    manager = GitWorktreeManager()
    command = sys.argv[1]
    
    if command == 'create':
        branch_name = sys.argv[2]
        base_branch = sys.argv[3] if len(sys.argv) > 3 else 'main'
        result = manager.create_worktree(branch_name, base_branch)
        print(json.dumps(result, indent=2))
    
    elif command == 'cleanup':
        worktree_path = sys.argv[2]
        result = manager.cleanup_worktree(worktree_path)
        print(json.dumps(result, indent=2))
    
    elif command == 'list':
        result = manager.list_worktrees()
        print(json.dumps(result, indent=2))
    
    elif command == 'prune':
        result = manager.prune_worktrees()
        print(json.dumps(result, indent=2))
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
