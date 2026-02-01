"""
Workflow Executor
=================

Execute workflow definitions.

This module provides:
- Workflow execution engine
- Phase and step execution
- Error handling and retry logic
- Skill and agent loading

Usage:
    from workflows.engine.executor import WorkflowExecutor
    from workflows.engine.parser import parse_workflow
    
    workflow = parse_workflow('workflows/templates/feature_development.yml')
    executor = WorkflowExecutor()
    result = await executor.execute(workflow)
"""

import asyncio
from pathlib import Path
from typing import Any, Optional
import importlib.util
import sys

from workflows.engine.parser import WorkflowDefinition, Phase, PhaseStep
from workflows.engine.context import ExecutionContext, StepResult
from workflows.engine.validators import WorkflowValidator


class ExecutionError(Exception):
    """Raised when workflow execution fails."""
    pass


class WorkflowExecutor:
    """
    Executes workflow definitions.
    
    Attributes:
        skills_dir: Directory containing skills
        agents_dir: Directory containing agents
        dry_run: If True, simulate execution without actually running
    """
    
    def __init__(
        self,
        skills_dir: str = 'skills',
        agents_dir: str = 'agents',
        dry_run: bool = False
    ):
        self.skills_dir = Path(skills_dir)
        self.agents_dir = Path(agents_dir)
        self.dry_run = dry_run
        self.validator = WorkflowValidator(str(self.skills_dir), str(self.agents_dir))
    
    async def execute(
        self,
        workflow: WorkflowDefinition,
        validate: bool = True
    ) -> ExecutionContext:
        """
        Execute a workflow.
        
        Args:
            workflow: WorkflowDefinition to execute
            validate: Whether to validate before execution
            
        Returns:
            ExecutionContext with execution results
            
        Raises:
            ExecutionError: If execution fails
        """
        # Validate workflow
        if validate:
            errors = self.validator.validate(workflow)
            critical_errors = [e for e in errors if e.severity == 'error']
            if critical_errors:
                error_msg = '\n'.join(str(e) for e in critical_errors)
                raise ExecutionError(f"Workflow validation failed:\n{error_msg}")
        
        # Create execution context
        context = ExecutionContext(
            workflow_name=workflow.name,
            workflow_version=workflow.version
        )
        
        print(f"\n🚀 Starting workflow: {workflow.name}")
        print(f"   Execution ID: {context.execution_id}")
        print(f"   Phases: {len(workflow.phases)}\n")
        
        try:
            # Execute phases sequentially
            for phase in workflow.phases:
                await self._execute_phase(phase, workflow, context)
            
            # Mark execution as successful
            context.end_execution('success')
            print(f"\n✅ Workflow completed successfully")
            print(f"   Duration: {context.duration:.2f}s")
            
        except Exception as e:
            context.end_execution('failure')
            print(f"\n❌ Workflow failed: {e}")
            raise ExecutionError(f"Workflow execution failed: {e}")
        
        return context
    
    async def _execute_phase(
        self,
        phase: Phase,
        workflow: WorkflowDefinition,
        context: ExecutionContext
    ):
        """Execute a single phase."""
        print(f"📋 Phase: {phase.name}")
        context.start_phase(phase.name)
        
        try:
            # Execute steps in phase
            for step in phase.steps:
                await self._execute_step(step, workflow, context)
            
            context.end_phase('success')
            print(f"   ✅ Phase '{phase.name}' completed\n")
            
        except Exception as e:
            context.end_phase('failure')
            raise ExecutionError(f"Phase '{phase.name}' failed: {e}")
    
    async def _execute_step(
        self,
        step: PhaseStep,
        workflow: WorkflowDefinition,
        context: ExecutionContext
    ):
        """Execute a single step."""
        print(f"   → {step.type}: {step.name}")
        if step.description:
            print(f"      {step.description}")
        
        context.start_step(step.name, step.type)
        
        try:
            if self.dry_run:
                # Simulate execution
                print(f"      [DRY RUN] Simulating execution")
                await asyncio.sleep(0.1)
                output = f"simulated_output_{step.name}"
            else:
                # Execute based on type
                if step.type == 'skill':
                    output = await self._execute_skill(step, context)
                elif step.type == 'agent':
                    output = await self._execute_agent(step, context)
                else:
                    raise ExecutionError(f"Unknown step type: {step.type}")
            
            context.end_step('success', output=output)
            print(f"      ✅ Completed")
            
        except Exception as e:
            context.end_step('failure', error=str(e))
            raise ExecutionError(f"Step '{step.name}' failed: {e}")
    
    async def _execute_skill(self, step: PhaseStep, context: ExecutionContext) -> Any:
        """Execute a skill."""
        skill_path = self._find_skill_path(step.name)
        
        if not skill_path:
            raise ExecutionError(f"Skill '{step.name}' not found")
        
        # For now, just return a placeholder
        # In the future, this will actually load and execute the skill
        print(f"      [PLACEHOLDER] Would execute skill at: {skill_path}")
        
        # Simulate skill execution
        await asyncio.sleep(0.1)
        
        return {"status": "success", "skill": step.name}
    
    async def _execute_agent(self, step: PhaseStep, context: ExecutionContext) -> Any:
        """Execute an agent."""
        agent_path = self._find_agent_path(step.name)
        
        if not agent_path:
            raise ExecutionError(f"Agent '{step.name}' not found")
        
        # For now, just return a placeholder
        # In the future, this will actually load and execute the agent
        print(f"      [PLACEHOLDER] Would execute agent at: {agent_path}")
        
        # Simulate agent execution
        await asyncio.sleep(0.1)
        
        return {"status": "success", "agent": step.name}
    
    def _find_skill_path(self, skill_name: str) -> Optional[Path]:
        """Find skill directory path."""
        # Check in skills/ directory
        skill_path = self.skills_dir / skill_name
        if skill_path.exists():
            return skill_path
        
        # Check in skills/workflow_skills/ directory
        workflow_skills_path = self.skills_dir / 'workflow_skills' / skill_name
        if workflow_skills_path.exists():
            return workflow_skills_path
        
        return None
    
    def _find_agent_path(self, agent_name: str) -> Optional[Path]:
        """Find agent directory path."""
        agent_path = self.agents_dir / agent_name
        if agent_path.exists():
            return agent_path
        
        return None


async def execute_workflow_file(workflow_path: str, dry_run: bool = False) -> ExecutionContext:
    """
    Execute a workflow from a file.
    
    Args:
        workflow_path: Path to workflow YAML file
        dry_run: If True, simulate execution
        
    Returns:
        ExecutionContext with results
    """
    from workflows.engine.parser import parse_workflow
    
    workflow = parse_workflow(workflow_path)
    executor = WorkflowExecutor(dry_run=dry_run)
    return await executor.execute(workflow)


if __name__ == '__main__':
    # Test executor
    import sys
    
    async def main():
        if len(sys.argv) > 1:
            workflow_path = sys.argv[1]
            dry_run = '--dry-run' in sys.argv
            
            try:
                context = await execute_workflow_file(workflow_path, dry_run=dry_run)
                
                print("\n" + "="*60)
                print("EXECUTION SUMMARY")
                print("="*60)
                
                summary = context.get_summary()
                for key, value in summary.items():
                    print(f"{key:20s}: {value}")
                
            except Exception as e:
                print(f"\n❌ Error: {e}")
                sys.exit(1)
        else:
            print("Usage: python executor.py <workflow.yml> [--dry-run]")
    
    asyncio.run(main())
