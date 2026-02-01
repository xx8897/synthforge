"""
Workflow Parser
===============

Parse YAML workflow definitions into structured WorkflowDefinition objects.

This module provides functionality to:
- Parse YAML workflow files
- Validate workflow structure
- Resolve dependencies
- Extract metadata

Usage:
    from workflows.engine.parser import parse_workflow, validate_workflow
    
    workflow = parse_workflow('workflows/templates/feature_development.yml')
    errors = validate_workflow(workflow)
"""

import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field


@dataclass
class PhaseStep:
    """Represents a single step in a workflow phase."""
    type: str  # 'skill' or 'agent'
    name: str
    description: Optional[str] = None
    input: Optional[str] = None
    output: Optional[str] = None
    action: Optional[str] = None
    mode: Optional[str] = None
    config: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Phase:
    """Represents a workflow phase."""
    name: str
    steps: List[PhaseStep] = field(default_factory=list)


@dataclass
class WorkflowDefinition:
    """Represents a complete workflow definition."""
    name: str
    phases: List[Phase] = field(default_factory=list)
    description: Optional[str] = None
    version: Optional[str] = None
    author: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    config: Dict[str, Any] = field(default_factory=dict)
    outputs: List[str] = field(default_factory=list)
    success_criteria: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def filepath(self) -> Optional[Path]:
        """Get the filepath if set."""
        return getattr(self, '_filepath', None)
    
    @filepath.setter
    def filepath(self, value: Path):
        """Set the filepath."""
        self._filepath = value


class WorkflowParseError(Exception):
    """Raised when workflow parsing fails."""
    pass


def parse_workflow(workflow_path: str) -> WorkflowDefinition:
    """
    Parse a YAML workflow file into a WorkflowDefinition object.
    
    Args:
        workflow_path: Path to the workflow YAML file
        
    Returns:
        WorkflowDefinition object
        
    Raises:
        WorkflowParseError: If parsing fails
        FileNotFoundError: If workflow file doesn't exist
    """
    path = Path(workflow_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Workflow file not found: {workflow_path}")
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise WorkflowParseError(f"Invalid YAML syntax: {e}")
    
    if not isinstance(data, dict):
        raise WorkflowParseError("Workflow file must contain a YAML dictionary")
    
    # Parse required fields
    if 'name' not in data:
        raise WorkflowParseError("Workflow must have a 'name' field")
    
    if 'phases' not in data:
        raise WorkflowParseError("Workflow must have a 'phases' field")
    
    # Create WorkflowDefinition
    workflow = WorkflowDefinition(
        name=data['name'],
        description=data.get('description'),
        version=data.get('version'),
        author=data.get('author'),
        tags=data.get('tags', []),
        config=data.get('config', {}),
        outputs=data.get('outputs', []),
        success_criteria=data.get('success_criteria', {})
    )
    
    # Store filepath
    workflow.filepath = path
    
    # Parse phases
    phases_data = data['phases']
    if not isinstance(phases_data, dict):
        raise WorkflowParseError("'phases' must be a dictionary")
    
    for phase_name, steps_data in phases_data.items():
        phase = Phase(name=phase_name)
        
        if not isinstance(steps_data, list):
            raise WorkflowParseError(f"Phase '{phase_name}' must contain a list of steps")
        
        for step_data in steps_data:
            if not isinstance(step_data, dict):
                raise WorkflowParseError(f"Each step in phase '{phase_name}' must be a dictionary")
            
            # Determine step type
            if 'skill' in step_data:
                step_type = 'skill'
                step_name = step_data['skill']
            elif 'agent' in step_data:
                step_type = 'agent'
                step_name = step_data['agent']
            else:
                raise WorkflowParseError(f"Step in phase '{phase_name}' must have either 'skill' or 'agent' field")
            
            step = PhaseStep(
                type=step_type,
                name=step_name,
                description=step_data.get('description'),
                input=step_data.get('input'),
                output=step_data.get('output'),
                action=step_data.get('action'),
                mode=step_data.get('mode'),
                config=step_data.get('config', {})
            )
            
            phase.steps.append(step)
        
        workflow.phases.append(phase)
    
    return workflow


def validate_workflow(workflow: WorkflowDefinition) -> List[str]:
    """
    Validate a workflow definition.
    
    Args:
        workflow: WorkflowDefinition to validate
        
    Returns:
        List of validation error messages (empty if valid)
    """
    errors = []
    
    # Check required fields
    if not workflow.name:
        errors.append("Workflow name is required")
    
    if not workflow.phases:
        errors.append("Workflow must have at least one phase")
    
    # Check phases
    for phase in workflow.phases:
        if not phase.name:
            errors.append("Phase name is required")
        
        if not phase.steps:
            errors.append(f"Phase '{phase.name}' must have at least one step")
        
        # Check steps
        for i, step in enumerate(phase.steps):
            step_id = f"Phase '{phase.name}', Step {i+1}"
            
            if not step.name:
                errors.append(f"{step_id}: Step name is required")
            
            if step.type not in ['skill', 'agent']:
                errors.append(f"{step_id}: Step type must be 'skill' or 'agent'")
    
    return errors


def get_workflow_metadata(workflow_path: str) -> Dict[str, Any]:
    """
    Get workflow metadata without full parsing.
    
    Args:
        workflow_path: Path to workflow file
        
    Returns:
        Dictionary with metadata (name, description, version, tags)
    """
    path = Path(workflow_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Workflow file not found: {workflow_path}")
    
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    return {
        'name': data.get('name'),
        'description': data.get('description'),
        'version': data.get('version'),
        'author': data.get('author'),
        'tags': data.get('tags', []),
        'filepath': str(path)
    }


def list_workflows(directory: str = 'workflows/templates') -> List[Dict[str, Any]]:
    """
    List all workflows in a directory.
    
    Args:
        directory: Directory to search for workflows
        
    Returns:
        List of workflow metadata dictionaries
    """
    path = Path(directory)
    
    if not path.exists():
        return []
    
    workflows = []
    for yml_file in path.glob('*.yml'):
        try:
            metadata = get_workflow_metadata(str(yml_file))
            workflows.append(metadata)
        except Exception:
            # Skip invalid workflows
            continue
    
    return workflows


if __name__ == '__main__':
    # Test parsing
    import sys
    
    if len(sys.argv) > 1:
        workflow_path = sys.argv[1]
        try:
            workflow = parse_workflow(workflow_path)
            print(f"✅ Successfully parsed workflow: {workflow.name}")
            print(f"   Phases: {len(workflow.phases)}")
            print(f"   Version: {workflow.version}")
            
            errors = validate_workflow(workflow)
            if errors:
                print("\n⚠️ Validation errors:")
                for error in errors:
                    print(f"   - {error}")
            else:
                print("\n✅ Workflow is valid")
        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)
    else:
        print("Usage: python parser.py <workflow.yml>")
