"""
Workflow Engine Package
=======================

This package provides the core workflow execution engine for synthforge.

Components:
- parser.py: Parse YAML workflow definitions
- executor.py: Execute workflows
- context.py: Execution context management
- validators.py: Workflow validation

Usage:
    from workflows.engine import parse_workflow, execute_workflow
    
    workflow = parse_workflow('workflows/templates/feature_development.yml')
    result = await execute_workflow(workflow)
"""

__version__ = '1.0.0'
__author__ = 'synthforge team'

# Placeholder for future imports
# from .parser import parse_workflow, validate_workflow
# from .executor import execute_workflow
# from .context import ExecutionContext
# from .validators import WorkflowValidator

__all__ = [
    # 'parse_workflow',
    # 'validate_workflow',
    # 'execute_workflow',
    # 'ExecutionContext',
    # 'WorkflowValidator',
]
