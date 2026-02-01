"""
Task Generator Skill
====================

Generate task.md from parsed specification JSON.

This skill creates:
- Structured task checklists
- Task grouping by component/phase
- Dependency analysis
- Priority ordering

Usage:
    from skills.workflow_skills.task_generator.generator import generate_tasks
    
    generate_tasks('spec.json', 'task.md')
"""

import json
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime


class TaskGenerator:
    """Generates task.md from specification JSON."""
    
    def __init__(self, group_by_component: bool = True, analyze_dependencies: bool = True):
        self.group_by_component = group_by_component
        self.analyze_dependencies = analyze_dependencies
    
    def generate(self, spec_path: str, output_path: str = 'task.md') -> str:
        """
        Generate task.md from specification JSON.
        
        Args:
            spec_path: Path to spec.json
            output_path: Path to output task.md
            
        Returns:
            Generated task markdown content
        """
        # Load specification
        with open(spec_path, 'r', encoding='utf-8') as f:
            spec = json.load(f)
        
        # Generate task content
        content = self._generate_content(spec)
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return content
    
    def _generate_content(self, spec: Dict[str, Any]) -> str:
        """Generate task markdown content."""
        lines = []
        
        # Header
        goal = spec.get('goal', 'Implementation Task')
        lines.append(f"# Task: {goal[:100]}")
        lines.append("")
        lines.append(f"**Created**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        lines.append("**Status**: 🔄 In Progress")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        # Checklist
        lines.append("## ✅ Checklist")
        lines.append("")
        
        # Generate tasks by component
        if self.group_by_component:
            components = spec.get('components', [])
            for i, component in enumerate(components, 1):
                lines.extend(self._generate_component_tasks(component, i))
        
        # Verification tasks
        verification = spec.get('verification_plan', {})
        if verification:
            lines.extend(self._generate_verification_tasks(verification))
        
        # Footer
        lines.append("---")
        lines.append("")
        lines.append("**Status**: Tasks generated from specification")
        
        return '\n'.join(lines)
    
    def _generate_component_tasks(self, component: Dict[str, Any], index: int) -> List[str]:
        """Generate tasks for a component."""
        lines = []
        
        component_name = component.get('name', f'Component {index}')
        lines.append(f"### {index}. {component_name}")
        lines.append("")
        
        # Summary
        summary = component.get('summary', '')
        if summary:
            lines.append(f"**Summary**: {summary}")
            lines.append("")
        
        # File tasks
        files = component.get('files', [])
        for file_change in files:
            action = file_change.get('action', 'MODIFY')
            basename = file_change.get('basename', 'file')
            path = file_change.get('path', '')
            
            task_desc = f"[{action}] `{basename}`"
            lines.append(f"- [ ] {task_desc}")
            
            # Add description as sub-item if exists
            description = file_change.get('description', '')
            if description:
                # Take first line of description
                first_line = description.split('\n')[0].strip()
                if first_line:
                    lines.append(f"  - {first_line}")
        
        lines.append("")
        return lines
    
    def _generate_verification_tasks(self, verification: Dict[str, Any]) -> List[str]:
        """Generate verification tasks."""
        lines = []
        
        lines.append("### Verification")
        lines.append("")
        
        # Automated tests
        auto_tests = verification.get('automated_tests', [])
        if auto_tests:
            lines.append("**Automated Tests**:")
            for test in auto_tests:
                # Extract test name from description
                test_name = test.split('\n')[0].strip() if test else "Run tests"
                lines.append(f"- [ ] {test_name}")
            lines.append("")
        
        # Manual verification
        manual = verification.get('manual_verification', [])
        if manual:
            lines.append("**Manual Verification**:")
            for item in manual:
                item_name = item.split('\n')[0].strip() if item else "Verify manually"
                lines.append(f"- [ ] {item_name}")
            lines.append("")
        
        return lines


def generate_tasks(
    spec_path: str,
    output_path: str = 'task.md',
    group_by_component: bool = True,
    analyze_dependencies: bool = True
) -> str:
    """
    Generate task.md from specification JSON.
    
    Args:
        spec_path: Path to spec.json
        output_path: Path to output task.md
        group_by_component: Group tasks by component
        analyze_dependencies: Analyze task dependencies
        
    Returns:
        Generated task markdown content
    """
    generator = TaskGenerator(
        group_by_component=group_by_component,
        analyze_dependencies=analyze_dependencies
    )
    return generator.generate(spec_path, output_path)


if __name__ == '__main__':
    # Test generator
    import sys
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else 'task.md'
        
        try:
            content = generate_tasks(input_file, output_file)
            print(f"✅ Successfully generated tasks")
            print(f"   Input: {input_file}")
            print(f"   Output: {output_file}")
            print(f"   Lines: {len(content.splitlines())}")
        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)
    else:
        print("Usage: python generator.py <spec.json> [task.md]")
