"""
Spec Parser Skill
=================

Parse implementation_plan.md into structured JSON format.

This skill extracts:
- Goal and background
- Proposed changes (by component and file)
- Verification plan
- User review requirements

Usage:
    from skills.workflow_skills.spec_parser.parser import parse_spec
    
    spec = parse_spec('implementation_plan.md')
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field, asdict


@dataclass
class FileChange:
    """Represents a file change."""
    action: str  # MODIFY, NEW, DELETE
    path: str
    basename: str
    description: str = ""


@dataclass
class Component:
    """Represents a component with file changes."""
    name: str
    summary: str = ""
    files: List[FileChange] = field(default_factory=list)


@dataclass
class VerificationPlan:
    """Represents verification plan."""
    automated_tests: List[str] = field(default_factory=list)
    manual_verification: List[str] = field(default_factory=list)


@dataclass
class SpecificationData:
    """Represents parsed specification."""
    goal: str = ""
    background: str = ""
    user_review_required: List[str] = field(default_factory=list)
    components: List[Component] = field(default_factory=list)
    verification_plan: VerificationPlan = field(default_factory=VerificationPlan)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return asdict(self)
    
    def to_json(self, filepath: str = None) -> str:
        """Convert to JSON string or save to file."""
        json_str = json.dumps(self.to_dict(), indent=2, ensure_ascii=False)
        
        if filepath:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(json_str)
        
        return json_str


class SpecParser:
    """Parser for implementation_plan.md files."""
    
    def __init__(self):
        self.current_section = None
        self.current_component = None
    
    def parse(self, filepath: str) -> SpecificationData:
        """
        Parse implementation_plan.md file.
        
        Args:
            filepath: Path to implementation_plan.md
            
        Returns:
            SpecificationData object
        """
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
        
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        spec = SpecificationData()
        
        # Parse sections
        spec.goal = self._extract_goal(content)
        spec.background = self._extract_background(content)
        spec.user_review_required = self._extract_user_review(content)
        spec.components = self._extract_components(content)
        spec.verification_plan = self._extract_verification_plan(content)
        
        return spec
    
    def _extract_goal(self, content: str) -> str:
        """Extract goal description."""
        # Look for # [Goal Description] section
        match = re.search(r'#\s+(.+?)\n\n(.+?)(?=\n##|\Z)', content, re.DOTALL)
        if match:
            return match.group(2).strip()
        return ""
    
    def _extract_background(self, content: str) -> str:
        """Extract background context."""
        # Look for background or context section
        match = re.search(r'##\s+(?:Background|Context).*?\n\n(.+?)(?=\n##|\Z)', content, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return ""
    
    def _extract_user_review(self, content: str) -> List[str]:
        """Extract user review requirements."""
        items = []
        
        # Look for User Review Required section
        match = re.search(r'##\s+User Review Required.*?\n\n(.+?)(?=\n##|\Z)', content, re.DOTALL)
        if match:
            section = match.group(1)
            # Extract bullet points or numbered items
            items = re.findall(r'[-*]\s+(.+?)(?=\n[-*]|\n\n|\Z)', section, re.DOTALL)
            items = [item.strip() for item in items]
        
        return items
    
    def _extract_components(self, content: str) -> List[Component]:
        """Extract proposed changes by component."""
        components = []
        
        # Look for Proposed Changes section
        match = re.search(r'##\s+Proposed Changes.*?\n\n(.+?)(?=\n##\s+(?!#)|\Z)', content, re.DOTALL)
        if not match:
            return components
        
        changes_section = match.group(1)
        
        # Split by ### Component sections
        component_sections = re.split(r'\n###\s+(?!#)', changes_section)
        
        for section in component_sections[1:]:  # Skip first empty split
            component = self._parse_component_section(section)
            if component:
                components.append(component)
        
        return components
    
    def _parse_component_section(self, section: str) -> Optional[Component]:
        """Parse a component section."""
        lines = section.split('\n')
        if not lines:
            return None
        
        # First line is component name
        component_name = lines[0].strip()
        component = Component(name=component_name)
        
        # Look for summary (text before first ####)
        summary_match = re.search(r'^(.+?)(?=\n####|\Z)', section, re.DOTALL)
        if summary_match:
            summary = summary_match.group(1).replace(component_name, '').strip()
            component.summary = summary
        
        # Extract file changes (#### [MODIFY] [filename](path))
        file_pattern = r'####\s+\[(MODIFY|NEW|DELETE)\]\s+\[([^\]]+)\]\(([^)]+)\)'
        file_matches = re.finditer(file_pattern, section)
        
        for match in file_matches:
            action = match.group(1)
            basename = match.group(2)
            path = match.group(3).replace('file:///', '')
            
            # Extract description (text after file header until next #### or ###)
            desc_start = match.end()
            desc_match = re.search(r'\n(.+?)(?=\n####|\n###|\Z)', section[desc_start:], re.DOTALL)
            description = desc_match.group(1).strip() if desc_match else ""
            
            file_change = FileChange(
                action=action,
                path=path,
                basename=basename,
                description=description
            )
            component.files.append(file_change)
        
        return component
    
    def _extract_verification_plan(self, content: str) -> VerificationPlan:
        """Extract verification plan."""
        plan = VerificationPlan()
        
        # Look for Verification Plan section
        match = re.search(r'##\s+Verification Plan.*?\n\n(.+?)(?=\n##\s+(?!#)|\Z)', content, re.DOTALL)
        if not match:
            return plan
        
        verification_section = match.group(1)
        
        # Extract automated tests
        auto_match = re.search(r'###\s+Automated Tests.*?\n\n(.+?)(?=\n###|\Z)', verification_section, re.DOTALL)
        if auto_match:
            tests = re.findall(r'[-*]\s+(.+?)(?=\n[-*]|\n\n|\Z)', auto_match.group(1), re.DOTALL)
            plan.automated_tests = [t.strip() for t in tests]
        
        # Extract manual verification
        manual_match = re.search(r'###\s+Manual Verification.*?\n\n(.+?)(?=\n###|\Z)', verification_section, re.DOTALL)
        if manual_match:
            items = re.findall(r'[-*]\s+(.+?)(?=\n[-*]|\n\n|\Z)', manual_match.group(1), re.DOTALL)
            plan.manual_verification = [i.strip() for i in items]
        
        return plan


def parse_spec(filepath: str, output_path: str = None) -> SpecificationData:
    """
    Parse implementation_plan.md file.
    
    Args:
        filepath: Path to implementation_plan.md
        output_path: Optional path to save JSON output
        
    Returns:
        SpecificationData object
    """
    parser = SpecParser()
    spec = parser.parse(filepath)
    
    if output_path:
        spec.to_json(output_path)
    
    return spec


if __name__ == '__main__':
    # Test parser
    import sys
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else 'spec.json'
        
        try:
            spec = parse_spec(input_file, output_file)
            print(f"✅ Successfully parsed specification")
            print(f"   Goal: {spec.goal[:100]}...")
            print(f"   Components: {len(spec.components)}")
            print(f"   Output: {output_file}")
        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)
    else:
        print("Usage: python parser.py <implementation_plan.md> [output.json]")
