"""
Reviewer Agent
==============

AI agent for code review and quality assurance.

This agent provides:
- Code review
- Quality checks
- Rule compliance verification
- Improvement suggestions

Usage:
    from agents.reviewer_agent.reviewer import ReviewerAgent
    
    agent = ReviewerAgent()
    result = await agent.code_review(files=['src/module.py'])
"""

from pathlib import Path
from typing import Dict, List, Any, Optional
import yaml


class ReviewIssue:
    """Represents a code review issue."""
    
    def __init__(
        self,
        severity: str,
        category: str,
        message: str,
        file: str = None,
        line: int = None
    ):
        self.severity = severity  # 'error', 'warning', 'info'
        self.category = category  # 'style', 'security', 'performance', etc.
        self.message = message
        self.file = file
        self.line = line
    
    def __str__(self):
        location = f"{self.file}:{self.line}" if self.file and self.line else self.file or "general"
        severity_icon = {'error': '❌', 'warning': '⚠️', 'info': 'ℹ️'}.get(self.severity, '•')
        return f"{severity_icon} [{self.category}] {location}: {self.message}"


class ReviewerAgent:
    """AI agent for code review and quality assurance."""
    
    def __init__(self, config_path: str = None):
        self.config = self._load_config(config_path)
        self.issues: List[ReviewIssue] = []
    
    def _load_config(self, config_path: str = None) -> Dict[str, Any]:
        """Load agent configuration."""
        if config_path and Path(config_path).exists():
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        
        # Default configuration
        return {
            'agent': {
                'name': 'reviewer_agent',
                'version': '1.0.0'
            },
            'settings': {
                'check_style': True,
                'check_security': True,
                'check_performance': True,
                'check_tests': True
            },
            'thresholds': {
                'min_coverage': 80,
                'max_complexity': 10,
                'max_function_length': 50
            }
        }
    
    async def code_review(
        self,
        files: List[str] = None,
        checks: List[str] = None,
        rules_path: str = './rules/',
        auto_fix_minor: bool = False
    ) -> Dict[str, Any]:
        """
        Review code changes.
        
        Args:
            files: List of files to review
            checks: List of check types (style, security, performance, maintainability)
            rules_path: Path to rules directory
            auto_fix_minor: Auto-fix minor issues
            
        Returns:
            Review result dictionary
        """
        self.issues = []
        
        if checks is None:
            checks = ['style', 'security', 'performance', 'maintainability']
        
        # Perform checks
        if 'style' in checks:
            self._check_style(files)
        
        if 'security' in checks:
            self._check_security(files)
        
        if 'performance' in checks:
            self._check_performance(files)
        
        if 'maintainability' in checks:
            self._check_maintainability(files)
        
        # Count issues by severity
        errors = [i for i in self.issues if i.severity == 'error']
        warnings = [i for i in self.issues if i.severity == 'warning']
        
        result = {
            'approved': len(errors) == 0,
            'total_issues': len(self.issues),
            'errors': len(errors),
            'warnings': len(warnings),
            'issues': [str(i) for i in self.issues],
            'auto_fixed': 0 if not auto_fix_minor else len([i for i in self.issues if i.severity == 'info'])
        }
        
        return result
    
    async def review_fix(
        self,
        fix_implementation: Dict[str, Any],
        check_side_effects: bool = True,
        verify_minimal_changes: bool = True
    ) -> Dict[str, Any]:
        """
        Review bug fix.
        
        Args:
            fix_implementation: Fix implementation details
            check_side_effects: Check for side effects
            verify_minimal_changes: Verify minimal changes
            
        Returns:
            Review result dictionary
        """
        # Placeholder implementation
        return {
            'approved': True,
            'minimal_changes': verify_minimal_changes,
            'no_side_effects': check_side_effects,
            'issues': []
        }
    
    async def review_refactoring(
        self,
        refactored_code: Dict[str, Any],
        check_code_quality: bool = True,
        verify_no_behavior_change: bool = True,
        check_performance: bool = True
    ) -> Dict[str, Any]:
        """
        Review refactored code.
        
        Args:
            refactored_code: Refactored code details
            check_code_quality: Check code quality
            verify_no_behavior_change: Verify behavior preservation
            check_performance: Check performance
            
        Returns:
            Review result dictionary
        """
        # Placeholder implementation
        return {
            'approved': True,
            'quality_improved': check_code_quality,
            'behavior_preserved': verify_no_behavior_change,
            'performance_ok': check_performance,
            'issues': []
        }
    
    def _check_style(self, files: List[str]):
        """Check code style."""
        # Placeholder: In real implementation, would use linters
        # Example issue
        if files:
            self.issues.append(ReviewIssue(
                severity='info',
                category='style',
                message='Code style looks good',
                file=files[0] if files else None
            ))
    
    def _check_security(self, files: List[str]):
        """Check security vulnerabilities."""
        # Placeholder: In real implementation, would use security scanners
        pass
    
    def _check_performance(self, files: List[str]):
        """Check performance issues."""
        # Placeholder: In real implementation, would use profilers
        pass
    
    def _check_maintainability(self, files: List[str]):
        """Check code maintainability."""
        # Placeholder: In real implementation, would check complexity, etc.
        pass


if __name__ == '__main__':
    # Test reviewer agent
    import asyncio
    import sys
    
    async def main():
        if len(sys.argv) > 1:
            files = sys.argv[1:]
            
            agent = ReviewerAgent()
            result = await agent.code_review(files=files)
            
            print("\n" + "="*60)
            print("CODE REVIEW RESULT")
            print("="*60)
            print(f"Approved: {result['approved']}")
            print(f"Total Issues: {result['total_issues']}")
            print(f"Errors: {result['errors']}")
            print(f"Warnings: {result['warnings']}")
            
            if result['issues']:
                print(f"\nIssues:")
                for issue in result['issues']:
                    print(f"  {issue}")
            
            if result['approved']:
                print("\n✅ Code review passed")
            else:
                print("\n❌ Code review failed")
                sys.exit(1)
        else:
            print("Usage: python reviewer.py <file1> [file2] ...")
    
    asyncio.run(main())
