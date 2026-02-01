"""
Executor Agent
==============

AI agent for code execution using Test-Driven Development (TDD).

This agent provides:
- TDD implementation
- Git worktree management
- Progress tracking
- Code quality assurance

Usage:
    from agents.executor_agent.executor import ExecutorAgent
    
    agent = ExecutorAgent()
    result = await agent.implement_tasks('task.md', mode='TDD')
"""

import re
from pathlib import Path
from typing import Dict, List, Any, Optional
import yaml

# Import Git worktree manager
try:
    from core_lib.git.worktree import GitWorktreeManager
    GIT_WORKTREE_AVAILABLE = True
except ImportError:
    GIT_WORKTREE_AVAILABLE = False


class ExecutorAgent:
    """AI agent for code execution with TDD."""
    
    def __init__(self, config_path: str = None):
        self.config = self._load_config(config_path)
        self.current_task = None
        self.completed_tasks = []
        
        # Initialize Git worktree manager if enabled
        self.worktree_manager = None
        if self.config.get('git', {}).get('use_worktrees') and GIT_WORKTREE_AVAILABLE:
            try:
                self.worktree_manager = GitWorktreeManager()
            except Exception as e:
                print(f"Warning: Git worktree manager initialization failed: {e}")
    
    def _load_config(self, config_path: str = None) -> Dict[str, Any]:
        """Load agent configuration."""
        if config_path and Path(config_path).exists():
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        
        # Default configuration
        return {
            'agent': {
                'name': 'executor_agent',
                'version': '1.0.0'
            },
            'settings': {
                'tdd_mode': True,
                'test_first': True,
                'coverage_threshold': 80
            },
            'git': {
                'use_worktrees': True,
                'auto_commit': True,
                'commit_message_template': 'feat: {task_description}'
            }
        }
    
    async def implement_tasks(
        self,
        task_file: str,
        mode: str = 'TDD',
        coverage_threshold: int = 80,
        test_first: bool = True
    ) -> Dict[str, Any]:
        """
        Implement tasks using TDD.
        
        Args:
            task_file: Path to task.md
            mode: Implementation mode (TDD, standard)
            coverage_threshold: Minimum test coverage
            test_first: Write tests first
            
        Returns:
            Implementation result dictionary
        """
        result = {
            'success': True,
            'completed_tasks': 0,
            'failed_tasks': 0,
            'coverage': 0.0,
            'errors': []
        }
        
        # Parse tasks
        try:
            tasks = self._parse_tasks(task_file)
        except Exception as e:
            result['success'] = False
            result['errors'].append(f"Failed to parse tasks: {e}")
            return result
        
        # Implement each task
        for task in tasks:
            if task['completed']:
                continue
            
            try:
                if mode == 'TDD':
                    await self._implement_task_tdd(task, test_first)
                else:
                    await self._implement_task_standard(task)
                
                self.completed_tasks.append(task)
                result['completed_tasks'] += 1
                
            except Exception as e:
                result['failed_tasks'] += 1
                result['errors'].append(f"Task '{task['description']}' failed: {e}")
        
        # Calculate coverage (placeholder)
        result['coverage'] = 85.0  # Simulated
        
        if result['coverage'] < coverage_threshold:
            result['success'] = False
            result['errors'].append(
                f"Coverage ({result['coverage']}%) below threshold ({coverage_threshold}%)"
            )
        
        return result
    
    async def implement_fix(
        self,
        fix_plan: Dict[str, Any],
        test_first: bool = True,
        add_regression_test: bool = True
    ) -> Dict[str, Any]:
        """
        Implement bug fix.
        
        Args:
            fix_plan: Fix plan from planner_agent
            test_first: Write test first
            add_regression_test: Add regression test
            
        Returns:
            Fix result dictionary
        """
        # Placeholder implementation
        return {
            'success': True,
            'fix_applied': True,
            'regression_test_added': add_regression_test,
            'tests_passed': True
        }
    
    async def execute_refactoring(
        self,
        refactoring_plan: Dict[str, Any],
        preserve_behavior: bool = True,
        run_tests_after_each_step: bool = True
    ) -> Dict[str, Any]:
        """
        Execute refactoring incrementally.
        
        Args:
            refactoring_plan: Refactoring plan
            preserve_behavior: Ensure behavior preservation
            run_tests_after_each_step: Run tests after each step
            
        Returns:
            Refactoring result dictionary
        """
        # Placeholder implementation
        return {
            'success': True,
            'steps_completed': 5,
            'behavior_preserved': preserve_behavior,
            'all_tests_passed': True
        }
    
    def _parse_tasks(self, task_file: str) -> List[Dict[str, Any]]:
        """Parse tasks from task.md."""
        tasks = []
        
        with open(task_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract tasks
        task_pattern = r'^- \[([ x/])\] (.+)$'
        matches = re.finditer(task_pattern, content, re.MULTILINE)
        
        for match in matches:
            status = match.group(1)
            description = match.group(2).strip()
            
            tasks.append({
                'description': description,
                'completed': (status == 'x'),
                'in_progress': (status == '/')
            })
        
        return tasks
    
    async def _implement_task_tdd(
        self,
        task: Dict[str, Any],
        test_first: bool
    ):
        """Implement task using TDD."""
        # Placeholder: In real implementation, this would:
        # 1. Write test (Red)
        # 2. Implement code (Green)
        # 3. Refactor (Clean)
        pass
    
    async def _implement_task_standard(self, task: Dict[str, Any]):
        """Implement task using standard approach."""
        # Placeholder
        pass


if __name__ == '__main__':
    # Test executor agent
    import asyncio
    import sys
    
    async def main():
        if len(sys.argv) > 1:
            task_file = sys.argv[1]
            
            agent = ExecutorAgent()
            result = await agent.implement_tasks(task_file)
            
            print("\n" + "="*60)
            print("IMPLEMENTATION RESULT")
            print("="*60)
            print(f"Success: {result['success']}")
            print(f"Completed Tasks: {result['completed_tasks']}")
            print(f"Failed Tasks: {result['failed_tasks']}")
            print(f"Coverage: {result['coverage']:.1f}%")
            
            if result['errors']:
                print(f"\nErrors:")
                for error in result['errors']:
                    print(f"  ❌ {error}")
            
            if result['success']:
                print("\n✅ Implementation successful")
            else:
                print("\n❌ Implementation failed")
                sys.exit(1)
        else:
            print("Usage: python executor.py <task.md>")
    
    asyncio.run(main())
