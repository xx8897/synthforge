"""
Workflow Integration Tests
===========================

Test workflow execution end-to-end.

Usage:
    pytest workflows/tests/test_integration.py -v
"""

import pytest
import asyncio
from pathlib import Path
from workflows.engine.parser import parse_workflow
from workflows.engine.executor import WorkflowExecutor
from workflows.engine.validators import WorkflowValidator


class TestWorkflowIntegration:
    """Integration tests for workflow system."""
    
    @pytest.fixture
    def workflow_dir(self):
        """Get workflows directory."""
        return Path('workflows/templates')
    
    @pytest.fixture
    def executor(self):
        """Create workflow executor."""
        return WorkflowExecutor(dry_run=True)
    
    def test_parse_feature_development_workflow(self, workflow_dir):
        """Test parsing feature_development.yml."""
        workflow_file = workflow_dir / 'feature_development.yml'
        
        workflow = parse_workflow(str(workflow_file))
        
        assert workflow.name == 'Feature Development'
        assert len(workflow.phases) > 0
        assert workflow.version is not None
    
    def test_validate_feature_development_workflow(self, workflow_dir):
        """Test validating feature_development.yml."""
        workflow_file = workflow_dir / 'feature_development.yml'
        
        workflow = parse_workflow(str(workflow_file))
        validator = WorkflowValidator()
        errors = validator.validate(workflow)
        
        # Should have no critical errors
        critical_errors = [e for e in errors if e.severity == 'error']
        assert len(critical_errors) == 0
    
    @pytest.mark.asyncio
    async def test_execute_feature_development_workflow_dry_run(self, workflow_dir, executor):
        """Test executing feature_development.yml in dry-run mode."""
        workflow_file = workflow_dir / 'feature_development.yml'
        
        workflow = parse_workflow(str(workflow_file))
        context = await executor.execute(workflow)
        
        assert context.status == 'success'
        assert len(context.phase_results) > 0
    
    def test_parse_bug_fix_workflow(self, workflow_dir):
        """Test parsing bug_fix.yml."""
        workflow_file = workflow_dir / 'bug_fix.yml'
        
        workflow = parse_workflow(str(workflow_file))
        
        assert workflow.name == 'Bug Fix'
        assert len(workflow.phases) > 0
    
    def test_parse_refactoring_workflow(self, workflow_dir):
        """Test parsing refactoring.yml."""
        workflow_file = workflow_dir / 'refactoring.yml'
        
        workflow = parse_workflow(str(workflow_file))
        
        assert workflow.name == 'Refactoring'
        assert len(workflow.phases) > 0
    
    def test_parse_rule_creation_workflow(self, workflow_dir):
        """Test parsing rule_creation.yml."""
        workflow_file = workflow_dir / 'rule_creation.yml'
        
        workflow = parse_workflow(str(workflow_file))
        
        assert workflow.name == 'Rule Creation'
        assert len(workflow.phases) > 0
    
    def test_all_workflows_are_valid(self, workflow_dir):
        """Test that all workflow templates are valid."""
        validator = WorkflowValidator()
        
        for workflow_file in workflow_dir.glob('*.yml'):
            workflow = parse_workflow(str(workflow_file))
            errors = validator.validate(workflow)
            
            critical_errors = [e for e in errors if e.severity == 'error']
            assert len(critical_errors) == 0, \
                f"Workflow {workflow_file.name} has critical errors: {critical_errors}"


class TestSkillIntegration:
    """Integration tests for skills."""
    
    def test_spec_parser_skill_exists(self):
        """Test that spec_parser skill exists."""
        skill_path = Path('skills/workflow_skills/spec_parser')
        assert skill_path.exists()
        assert (skill_path / 'SKILL.md').exists()
        assert (skill_path / 'parser.py').exists()
    
    def test_task_generator_skill_exists(self):
        """Test that task_generator skill exists."""
        skill_path = Path('skills/workflow_skills/task_generator')
        assert skill_path.exists()
        assert (skill_path / 'SKILL.md').exists()
        assert (skill_path / 'generator.py').exists()
    
    def test_test_runner_skill_exists(self):
        """Test that test_runner skill exists."""
        skill_path = Path('skills/workflow_skills/test_runner')
        assert skill_path.exists()
        assert (skill_path / 'SKILL.md').exists()
        assert (skill_path / 'runner.py').exists()


class TestAgentIntegration:
    """Integration tests for agents."""
    
    def test_planner_agent_exists(self):
        """Test that planner_agent exists."""
        agent_path = Path('agents/planner_agent')
        assert agent_path.exists()
        assert (agent_path / 'AGENT.md').exists()
        assert (agent_path / 'planner.py').exists()
        assert (agent_path / 'config.yml').exists()
    
    def test_executor_agent_exists(self):
        """Test that executor_agent exists."""
        agent_path = Path('agents/executor_agent')
        assert agent_path.exists()
        assert (agent_path / 'AGENT.md').exists()
        assert (agent_path / 'executor.py').exists()
        assert (agent_path / 'config.yml').exists()
    
    def test_reviewer_agent_exists(self):
        """Test that reviewer_agent exists."""
        agent_path = Path('agents/reviewer_agent')
        assert agent_path.exists()
        assert (agent_path / 'AGENT.md').exists()
        assert (agent_path / 'reviewer.py').exists()
        assert (agent_path / 'config.yml').exists()
    
    @pytest.mark.asyncio
    async def test_planner_agent_can_validate_tasks(self):
        """Test that planner_agent can validate tasks."""
        from agents.planner_agent.planner import PlannerAgent
        
        # Create a simple task file for testing
        task_file = Path('.internal/planning/TODO_02_01.md')
        if not task_file.exists():
            pytest.skip("Task file not found")
        
        agent = PlannerAgent()
        result = await agent.validate_tasks(str(task_file))
        
        assert 'valid' in result
        assert 'task_count' in result


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
