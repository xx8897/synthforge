"""
Execution Context
=================

Manage workflow execution context and state.

This module provides:
- Execution context management
- State tracking
- Variable storage
- Execution history

Usage:
    from workflows.engine.context import ExecutionContext
    
    context = ExecutionContext(workflow_name="feature_development")
    context.set_variable("spec_file", "spec.json")
    spec_file = context.get_variable("spec_file")
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path
import json


@dataclass
class StepResult:
    """Result of a single workflow step execution."""
    step_name: str
    step_type: str  # 'skill' or 'agent'
    status: str  # 'success', 'failure', 'skipped'
    start_time: datetime
    end_time: Optional[datetime] = None
    output: Any = None
    error: Optional[str] = None
    
    @property
    def duration(self) -> float:
        """Get execution duration in seconds."""
        if self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        return 0.0


@dataclass
class PhaseResult:
    """Result of a workflow phase execution."""
    phase_name: str
    status: str  # 'success', 'failure', 'in_progress'
    start_time: datetime
    end_time: Optional[datetime] = None
    steps: List[StepResult] = field(default_factory=list)
    
    @property
    def duration(self) -> float:
        """Get execution duration in seconds."""
        if self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        return 0.0


class ExecutionContext:
    """
    Manages workflow execution context and state.
    
    Attributes:
        workflow_name: Name of the workflow being executed
        workflow_version: Version of the workflow
        execution_id: Unique execution identifier
        start_time: When execution started
        variables: Dictionary of execution variables
        phase_results: List of phase execution results
    """
    
    def __init__(self, workflow_name: str, workflow_version: str = None):
        self.workflow_name = workflow_name
        self.workflow_version = workflow_version
        self.execution_id = self._generate_execution_id()
        self.start_time = datetime.now()
        self.end_time: Optional[datetime] = None
        self.status = 'in_progress'  # 'in_progress', 'success', 'failure'
        
        # Execution state
        self.variables: Dict[str, Any] = {}
        self.phase_results: List[PhaseResult] = []
        self.current_phase: Optional[PhaseResult] = None
        
        # Working directory
        self.working_dir = Path.cwd()
    
    def _generate_execution_id(self) -> str:
        """Generate unique execution ID."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        return f"{self.workflow_name}_{timestamp}"
    
    def set_variable(self, name: str, value: Any):
        """Set an execution variable."""
        self.variables[name] = value
    
    def get_variable(self, name: str, default: Any = None) -> Any:
        """Get an execution variable."""
        return self.variables.get(name, default)
    
    def has_variable(self, name: str) -> bool:
        """Check if variable exists."""
        return name in self.variables
    
    def start_phase(self, phase_name: str) -> PhaseResult:
        """Start a new phase."""
        phase_result = PhaseResult(
            phase_name=phase_name,
            status='in_progress',
            start_time=datetime.now()
        )
        self.phase_results.append(phase_result)
        self.current_phase = phase_result
        return phase_result
    
    def end_phase(self, status: str = 'success'):
        """End the current phase."""
        if self.current_phase:
            self.current_phase.status = status
            self.current_phase.end_time = datetime.now()
            self.current_phase = None
    
    def start_step(self, step_name: str, step_type: str) -> StepResult:
        """Start a new step in the current phase."""
        if not self.current_phase:
            raise RuntimeError("No active phase to add step to")
        
        step_result = StepResult(
            step_name=step_name,
            step_type=step_type,
            status='in_progress',
            start_time=datetime.now()
        )
        self.current_phase.steps.append(step_result)
        return step_result
    
    def end_step(self, status: str = 'success', output: Any = None, error: str = None):
        """End the current step."""
        if not self.current_phase or not self.current_phase.steps:
            raise RuntimeError("No active step to end")
        
        current_step = self.current_phase.steps[-1]
        current_step.status = status
        current_step.end_time = datetime.now()
        current_step.output = output
        current_step.error = error
    
    def end_execution(self, status: str = 'success'):
        """End the workflow execution."""
        self.status = status
        self.end_time = datetime.now()
    
    @property
    def duration(self) -> float:
        """Get total execution duration in seconds."""
        if self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        return (datetime.now() - self.start_time).total_seconds()
    
    def get_summary(self) -> Dict[str, Any]:
        """Get execution summary."""
        return {
            'execution_id': self.execution_id,
            'workflow_name': self.workflow_name,
            'workflow_version': self.workflow_version,
            'status': self.status,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat() if self.end_time else None,
            'duration': self.duration,
            'phases': len(self.phase_results),
            'total_steps': sum(len(p.steps) for p in self.phase_results),
            'successful_steps': sum(
                1 for p in self.phase_results 
                for s in p.steps 
                if s.status == 'success'
            ),
            'failed_steps': sum(
                1 for p in self.phase_results 
                for s in p.steps 
                if s.status == 'failure'
            )
        }
    
    def save_to_file(self, filepath: str):
        """Save execution context to JSON file."""
        data = {
            'execution_id': self.execution_id,
            'workflow_name': self.workflow_name,
            'workflow_version': self.workflow_version,
            'status': self.status,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat() if self.end_time else None,
            'duration': self.duration,
            'variables': self.variables,
            'phase_results': [
                {
                    'phase_name': p.phase_name,
                    'status': p.status,
                    'start_time': p.start_time.isoformat(),
                    'end_time': p.end_time.isoformat() if p.end_time else None,
                    'duration': p.duration,
                    'steps': [
                        {
                            'step_name': s.step_name,
                            'step_type': s.step_type,
                            'status': s.status,
                            'start_time': s.start_time.isoformat(),
                            'end_time': s.end_time.isoformat() if s.end_time else None,
                            'duration': s.duration,
                            'error': s.error
                        }
                        for s in p.steps
                    ]
                }
                for p in self.phase_results
            ]
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    @classmethod
    def load_from_file(cls, filepath: str) -> 'ExecutionContext':
        """Load execution context from JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        context = cls(
            workflow_name=data['workflow_name'],
            workflow_version=data.get('workflow_version')
        )
        context.execution_id = data['execution_id']
        context.status = data['status']
        context.start_time = datetime.fromisoformat(data['start_time'])
        if data.get('end_time'):
            context.end_time = datetime.fromisoformat(data['end_time'])
        context.variables = data.get('variables', {})
        
        return context


if __name__ == '__main__':
    # Test execution context
    context = ExecutionContext("test_workflow", "1.0.0")
    
    # Simulate execution
    context.set_variable("input_file", "test.md")
    
    # Phase 1
    context.start_phase("parse")
    context.start_step("spec_parser", "skill")
    context.end_step("success", output="spec.json")
    context.end_phase("success")
    
    # Phase 2
    context.start_phase("execute")
    context.start_step("executor_agent", "agent")
    context.end_step("success")
    context.end_phase("success")
    
    context.end_execution("success")
    
    # Print summary
    summary = context.get_summary()
    print("Execution Summary:")
    for key, value in summary.items():
        print(f"  {key}: {value}")
