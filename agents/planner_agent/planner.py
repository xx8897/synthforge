"""
Planner Agent
=============

AI agent for task planning, validation, and optimization.

This agent provides:
- Task validation
- Dependency analysis
- Effort estimation
- Plan optimization

Usage:
    from agents.planner_agent.planner import PlannerAgent
    
    agent = PlannerAgent()
    result = await agent.validate_tasks('task.md')
"""

import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
import yaml


@dataclass
class Task:
    """Represents a single task."""
    description: str
    completed: bool = False
    dependencies: List[str] = field(default_factory=list)
    estimated_hours: float = 0.0
    complexity: int = 1  # 1-10


@dataclass
class ValidationResult:
    """Task validation result."""
    valid: bool
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    estimated_hours: float = 0.0
    task_count: int = 0


class PlannerAgent:
    """AI agent for task planning and validation."""
    
    def __init__(self, config_path: str = None):
        self.config = self._load_config(config_path)
        self.tasks: List[Task] = []
    
    def _load_config(self, config_path: str = None) -> Dict[str, Any]:
        """Load agent configuration."""
        if config_path and Path(config_path).exists():
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        
        # Default configuration
        return {
            'agent': {
                'name': 'planner_agent',
                'version': '1.0.0'
            },
            'settings': {
                'max_task_depth': 5,
                'dependency_check': True,
                'effort_estimation': True
            },
            'thresholds': {
                'max_complexity': 10,
                'max_dependencies': 5
            }
        }
    
    async def validate_tasks(
        self,
        task_file: str,
        check_dependencies: bool = True,
        estimate_effort: bool = True
    ) -> Dict[str, Any]:
        """
        Validate task plan.
        
        Args:
            task_file: Path to task.md
            check_dependencies: Check task dependencies
            estimate_effort: Estimate effort
            
        Returns:
            Validation result dictionary
        """
        result = ValidationResult(valid=True)
        
        # Parse task file
        try:
            self.tasks = self._parse_task_file(task_file)
            result.task_count = len(self.tasks)
        except Exception as e:
            result.valid = False
            result.errors.append(f"Failed to parse task file: {e}")
            return self._result_to_dict(result)
        
        # Validate structure
        if not self.tasks:
            result.valid = False
            result.errors.append("No tasks found in task file")
            return self._result_to_dict(result)
        
        # Check dependencies
        if check_dependencies:
            dep_errors = self._check_dependencies()
            result.errors.extend(dep_errors)
            if dep_errors:
                result.valid = False
        
        # Estimate effort
        if estimate_effort:
            result.estimated_hours = self._estimate_total_effort()
        
        # Check complexity
        for i, task in enumerate(self.tasks):
            if task.complexity > self.config['thresholds']['max_complexity']:
                result.warnings.append(
                    f"Task {i+1} has high complexity ({task.complexity})"
                )
        
        return self._result_to_dict(result)
    
    async def create_fix_plan(
        self,
        issue_file: str,
        minimal_changes: bool = True
    ) -> Dict[str, Any]:
        """
        Create bug fix plan.
        
        Args:
            issue_file: Path to issue.md
            minimal_changes: Prefer minimal changes
            
        Returns:
            Fix plan dictionary
        """
        # Placeholder implementation
        return {
            'plan': 'Bug fix plan',
            'steps': [
                'Diagnose issue',
                'Implement fix',
                'Add regression test',
                'Verify fix'
            ],
            'estimated_hours': 2.0
        }
    
    async def create_refactoring_plan(
        self,
        ensure_backward_compatibility: bool = True,
        plan_incremental_steps: bool = True
    ) -> Dict[str, Any]:
        """
        Create refactoring plan.
        
        Args:
            ensure_backward_compatibility: Ensure compatibility
            plan_incremental_steps: Plan incremental steps
            
        Returns:
            Refactoring plan dictionary
        """
        # Placeholder implementation
        return {
            'plan': 'Refactoring plan',
            'steps': [
                'Analyze code',
                'Identify refactoring opportunities',
                'Plan incremental changes',
                'Execute refactoring'
            ],
            'estimated_hours': 4.0
        }
    
    def _parse_task_file(self, task_file: str) -> List[Task]:
        """Parse task.md file."""
        tasks = []
        
        with open(task_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract tasks (lines starting with - [ ] or - [x])
        task_pattern = r'^- \[([ x/])\] (.+)$'
        matches = re.finditer(task_pattern, content, re.MULTILINE)
        
        for match in matches:
            status = match.group(1)
            description = match.group(2).strip()
            
            task = Task(
                description=description,
                completed=(status == 'x'),
                complexity=self._estimate_complexity(description)
            )
            tasks.append(task)
        
        return tasks
    
    def _estimate_complexity(self, description: str) -> int:
        """Estimate task complexity (1-10)."""
        # Simple heuristic based on keywords
        complexity = 1
        
        high_complexity_keywords = ['refactor', 'redesign', 'migrate', 'optimize']
        medium_complexity_keywords = ['implement', 'create', 'add', 'update']
        
        desc_lower = description.lower()
        
        if any(kw in desc_lower for kw in high_complexity_keywords):
            complexity = 7
        elif any(kw in desc_lower for kw in medium_complexity_keywords):
            complexity = 4
        
        return complexity
    
    def _check_dependencies(self) -> List[str]:
        """Check task dependencies."""
        errors = []
        
        # Check for circular dependencies (simplified)
        # In a real implementation, this would use graph analysis
        
        return errors
    
    def _estimate_total_effort(self) -> float:
        """Estimate total effort in hours."""
        total_hours = 0.0
        
        for task in self.tasks:
            # Simple estimation: complexity * 0.5 hours
            task.estimated_hours = task.complexity * 0.5
            total_hours += task.estimated_hours
        
        return total_hours
    
    def _result_to_dict(self, result: ValidationResult) -> Dict[str, Any]:
        """Convert validation result to dictionary."""
        return {
            'valid': result.valid,
            'errors': result.errors,
            'warnings': result.warnings,
            'estimated_hours': result.estimated_hours,
            'task_count': result.task_count
        }


if __name__ == '__main__':
    # Test planner agent
    import asyncio
    import sys
    
    async def main():
        if len(sys.argv) > 1:
            task_file = sys.argv[1]
            
            agent = PlannerAgent()
            result = await agent.validate_tasks(task_file)
            
            print("\n" + "="*60)
            print("TASK VALIDATION RESULT")
            print("="*60)
            print(f"Valid: {result['valid']}")
            print(f"Tasks: {result['task_count']}")
            print(f"Estimated Hours: {result['estimated_hours']:.1f}")
            
            if result['errors']:
                print(f"\nErrors:")
                for error in result['errors']:
                    print(f"  ❌ {error}")
            
            if result['warnings']:
                print(f"\nWarnings:")
                for warning in result['warnings']:
                    print(f"  ⚠️  {warning}")
            
            if result['valid']:
                print("\n✅ Task plan is valid")
            else:
                print("\n❌ Task plan has errors")
                sys.exit(1)
        else:
            print("Usage: python planner.py <task.md>")
    
    asyncio.run(main())
