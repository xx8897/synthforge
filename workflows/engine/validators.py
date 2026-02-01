"""
Workflow Validators
===================

Validate workflow definitions for correctness and completeness.

This module provides:
- Workflow structure validation
- Dependency validation
- Skill/Agent existence validation
- Data flow validation

Usage:
    from workflows.engine.validators import WorkflowValidator
    
    validator = WorkflowValidator()
    errors = validator.validate(workflow)
"""

from pathlib import Path
from typing import List, Set, Dict, Any
from workflows.engine.parser import WorkflowDefinition, Phase, PhaseStep


class ValidationError:
    """Represents a validation error."""
    
    def __init__(self, message: str, severity: str = 'error', location: str = None):
        self.message = message
        self.severity = severity  # 'error', 'warning', 'info'
        self.location = location
    
    def __str__(self):
        prefix = {
            'error': '❌',
            'warning': '⚠️',
            'info': 'ℹ️'
        }.get(self.severity, '•')
        
        location_str = f" [{self.location}]" if self.location else ""
        return f"{prefix} {self.message}{location_str}"


class WorkflowValidator:
    """Validates workflow definitions."""
    
    def __init__(self, skills_dir: str = 'skills', agents_dir: str = 'agents'):
        self.skills_dir = Path(skills_dir)
        self.agents_dir = Path(agents_dir)
    
    def validate(self, workflow: WorkflowDefinition) -> List[ValidationError]:
        """
        Validate a workflow definition.
        
        Args:
            workflow: WorkflowDefinition to validate
            
        Returns:
            List of ValidationError objects
        """
        errors = []
        
        # Basic structure validation
        errors.extend(self._validate_structure(workflow))
        
        # Dependency validation
        errors.extend(self._validate_dependencies(workflow))
        
        # Skill/Agent existence validation
        errors.extend(self._validate_components(workflow))
        
        # Data flow validation
        errors.extend(self._validate_data_flow(workflow))
        
        # Configuration validation
        errors.extend(self._validate_config(workflow))
        
        return errors
    
    def _validate_structure(self, workflow: WorkflowDefinition) -> List[ValidationError]:
        """Validate basic workflow structure."""
        errors = []
        
        # Check required fields
        if not workflow.name:
            errors.append(ValidationError("Workflow name is required"))
        
        if not workflow.phases:
            errors.append(ValidationError("Workflow must have at least one phase"))
        
        # Check phase names are unique
        phase_names = [p.name for p in workflow.phases]
        if len(phase_names) != len(set(phase_names)):
            errors.append(ValidationError("Phase names must be unique"))
        
        # Check each phase
        for phase in workflow.phases:
            if not phase.steps:
                errors.append(ValidationError(
                    f"Phase must have at least one step",
                    location=f"Phase '{phase.name}'"
                ))
        
        return errors
    
    def _validate_dependencies(self, workflow: WorkflowDefinition) -> List[ValidationError]:
        """Validate workflow dependencies."""
        errors = []
        
        # Check for circular dependencies (future implementation)
        # For now, just warn if phases seem to have circular data flow
        
        return errors
    
    def _validate_components(self, workflow: WorkflowDefinition) -> List[ValidationError]:
        """Validate that referenced skills and agents exist."""
        errors = []
        
        for phase in workflow.phases:
            for step in phase.steps:
                location = f"Phase '{phase.name}', Step '{step.name}'"
                
                if step.type == 'skill':
                    if not self._skill_exists(step.name):
                        errors.append(ValidationError(
                            f"Skill '{step.name}' not found in {self.skills_dir}",
                            severity='warning',
                            location=location
                        ))
                
                elif step.type == 'agent':
                    if not self._agent_exists(step.name):
                        errors.append(ValidationError(
                            f"Agent '{step.name}' not found in {self.agents_dir}",
                            severity='warning',
                            location=location
                        ))
        
        return errors
    
    def _validate_data_flow(self, workflow: WorkflowDefinition) -> List[ValidationError]:
        """Validate data flow between phases."""
        errors = []
        
        # Track outputs from each phase
        available_outputs: Set[str] = set()
        
        for phase in workflow.phases:
            for step in phase.steps:
                location = f"Phase '{phase.name}', Step '{step.name}'"
                
                # Check if required input is available
                if step.input:
                    # Check if input file exists or was produced by previous step
                    if not self._is_input_available(step.input, available_outputs):
                        errors.append(ValidationError(
                            f"Input '{step.input}' not available (not produced by previous steps)",
                            severity='warning',
                            location=location
                        ))
                
                # Add output to available outputs
                if step.output:
                    available_outputs.add(step.output)
        
        return errors
    
    def _validate_config(self, workflow: WorkflowDefinition) -> List[ValidationError]:
        """Validate workflow configuration."""
        errors = []
        
        # Check timeout is reasonable
        if 'timeout' in workflow.config:
            timeout = workflow.config['timeout']
            if not isinstance(timeout, int) or timeout <= 0:
                errors.append(ValidationError(
                    "Timeout must be a positive integer",
                    location="config.timeout"
                ))
        
        # Check retry count is reasonable
        if 'retry' in workflow.config:
            retry = workflow.config['retry']
            if not isinstance(retry, int) or retry < 0:
                errors.append(ValidationError(
                    "Retry count must be a non-negative integer",
                    location="config.retry"
                ))
        
        return errors
    
    def _skill_exists(self, skill_name: str) -> bool:
        """Check if a skill exists."""
        # Check in skills/ directory
        skill_path = self.skills_dir / skill_name
        if skill_path.exists():
            return True
        
        # Check in skills/workflow_skills/ directory
        workflow_skills_path = self.skills_dir / 'workflow_skills' / skill_name
        if workflow_skills_path.exists():
            return True
        
        return False
    
    def _agent_exists(self, agent_name: str) -> bool:
        """Check if an agent exists."""
        agent_path = self.agents_dir / agent_name
        return agent_path.exists()
    
    def _is_input_available(self, input_file: str, available_outputs: Set[str]) -> bool:
        """Check if input file is available."""
        # Check if it's in available outputs
        if input_file in available_outputs:
            return True
        
        # Check if it's a file that exists
        if Path(input_file).exists():
            return True
        
        # Check common input files
        common_inputs = ['implementation_plan.md', 'task.md', 'issue.md']
        if input_file in common_inputs:
            return True
        
        return False


def validate_workflow_file(workflow_path: str) -> List[ValidationError]:
    """
    Validate a workflow file.
    
    Args:
        workflow_path: Path to workflow YAML file
        
    Returns:
        List of ValidationError objects
    """
    from workflows.engine.parser import parse_workflow
    
    try:
        workflow = parse_workflow(workflow_path)
        validator = WorkflowValidator()
        return validator.validate(workflow)
    except Exception as e:
        return [ValidationError(f"Failed to parse workflow: {e}")]


if __name__ == '__main__':
    # Test validation
    import sys
    
    if len(sys.argv) > 1:
        workflow_path = sys.argv[1]
        errors = validate_workflow_file(workflow_path)
        
        if not errors:
            print("✅ Workflow is valid")
        else:
            print(f"Found {len(errors)} validation issue(s):\n")
            for error in errors:
                print(f"  {error}")
            
            # Count by severity
            error_count = sum(1 for e in errors if e.severity == 'error')
            warning_count = sum(1 for e in errors if e.severity == 'warning')
            
            print(f"\nSummary: {error_count} errors, {warning_count} warnings")
            
            if error_count > 0:
                sys.exit(1)
    else:
        print("Usage: python validators.py <workflow.yml>")
