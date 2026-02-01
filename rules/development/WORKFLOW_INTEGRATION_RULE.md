---
name: WORKFLOW_INTEGRATION_RULE
category: development
priority: high
version: 1.0.0
related_rules:
  - WORKFLOW_RULE
  - AGENT_STRUCTURE_RULE
  - SKILL_STRUCTURE_RULE (planned)
  - AGENT_WORKFLOW_RULE
---

# WORKFLOW_INTEGRATION_RULE - Workflow Integration Standards

**工作流整合標準規則**

---

## 📋 Purpose

Define standards for integrating skills and agents with the workflow system.

定義 skills 和 agents 與工作流系統整合的標準。

---

## 🎯 Integration Principles

### 1. Workflow-Compatible Components

Components (skills/agents) must be **workflow-compatible** to be used in workflows.

### 2. Standard Interfaces

All components follow standard input/output interfaces.

### 3. Configuration-Driven

Components are configured via YAML in workflows.

### 4. Error Handling

Components handle errors gracefully and return structured results.

---

## 🔧 Making Skills Workflow-Compatible

### Skill Interface Requirements

#### 1. Standard Function Signature

```python
def skill_function(
    input_data: Any,
    config: Dict[str, Any] = None
) -> Dict[str, Any]:
    """
    Skill function.
    
    Args:
        input_data: Input data (file path, data object, etc.)
        config: Configuration dictionary from workflow
        
    Returns:
        {
            'success': bool,
            'output': Any,
            'errors': List[str]
        }
    """
    pass
```

#### 2. Return Format

```python
{
    'success': True/False,     # Required
    'output': Any,             # Required: Skill output
    'errors': [],              # Optional: Error messages
    'metadata': {}             # Optional: Additional info
}
```

### Example: Workflow-Compatible Skill

```python
"""
Spec Parser Skill
=================

Parse implementation_plan.md into structured JSON.
"""

from pathlib import Path
from typing import Dict, Any
import json


def parse_spec(
    spec_file: str,
    config: Dict[str, Any] = None
) -> Dict[str, Any]:
    """
    Parse specification file.
    
    Args:
        spec_file: Path to implementation_plan.md
        config: Configuration options
            - output_file: Optional output file path
            - format: Output format (json/yaml)
            
    Returns:
        {
            'success': bool,
            'output': Dict,  # Parsed spec
            'errors': List[str]
        }
    """
    result = {
        'success': True,
        'output': {},
        'errors': []
    }
    
    try:
        # Parse spec
        spec_data = _parse_file(spec_file)
        result['output'] = spec_data
        
        # Save if output_file specified
        if config and config.get('output_file'):
            _save_output(spec_data, config['output_file'])
        
    except FileNotFoundError:
        result['success'] = False
        result['errors'].append(f"File not found: {spec_file}")
    
    except Exception as e:
        result['success'] = False
        result['errors'].append(f"Parse error: {e}")
    
    return result


# Standalone execution
if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        result = parse_spec(sys.argv[1])
        print(json.dumps(result, indent=2))
    else:
        print("Usage: python parser.py <spec_file>")
```

### Workflow Usage

```yaml
# In workflow
phases:
  - name: specify
    steps:
      - skill: spec_parser
        input: implementation_plan.md
        config:
          output_file: spec.json
          format: json
```

---

## 🤖 Making Agents Workflow-Compatible

### Agent Interface Requirements

#### 1. Standard Action Method

```python
class AgentName:
    """Agent class."""
    
    async def action_name(
        self,
        input_data: Any,
        config: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """
        Agent action.
        
        Args:
            input_data: Input data
            config: Configuration from workflow
            
        Returns:
            {
                'success': bool,
                'data': Any,
                'errors': List[str]
            }
        """
        pass
```

#### 2. Return Format

```python
{
    'success': True/False,     # Required
    'data': Any,              # Required: Action result
    'errors': [],             # Optional: Error messages
    'metadata': {}            # Optional: Additional info
}
```

### Example: Workflow-Compatible Agent

```python
"""
Planner Agent
=============

Validate and plan tasks.
"""

from typing import Dict, Any, List


class PlannerAgent:
    """Task planning agent."""
    
    def __init__(self, config_path: str = None):
        """Initialize agent."""
        self.config = self._load_config(config_path)
    
    async def validate_tasks(
        self,
        task_file: str,
        config: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """
        Validate tasks from task.md.
        
        Args:
            task_file: Path to task.md
            config: Configuration options
                - max_depth: Maximum task nesting
                - check_dependencies: Check task dependencies
                
        Returns:
            {
                'success': bool,
                'data': {
                    'valid': bool,
                    'task_count': int,
                    'issues': List[str]
                },
                'errors': List[str]
            }
        """
        result = {
            'success': True,
            'data': {
                'valid': True,
                'task_count': 0,
                'issues': []
            },
            'errors': []
        }
        
        try:
            # Validate tasks
            tasks = self._parse_tasks(task_file)
            result['data']['task_count'] = len(tasks)
            
            # Check depth if configured
            if config and config.get('max_depth'):
                depth_issues = self._check_depth(tasks, config['max_depth'])
                result['data']['issues'].extend(depth_issues)
            
            # Check dependencies if configured
            if config and config.get('check_dependencies'):
                dep_issues = self._check_dependencies(tasks)
                result['data']['issues'].extend(dep_issues)
            
            # Set valid flag
            result['data']['valid'] = len(result['data']['issues']) == 0
            
        except Exception as e:
            result['success'] = False
            result['errors'].append(f"Validation error: {e}")
        
        return result
```

### Workflow Usage

```yaml
# In workflow
phases:
  - name: plan
    steps:
      - agent: planner_agent
        action: validate_tasks
        input: task.md
        config:
          max_depth: 5
          check_dependencies: true
```

---

## 📋 Integration Checklist

### For Skills

- [ ] **Standard Signature**: `skill_function(input_data, config=None)`
- [ ] **Return Format**: `{'success': bool, 'output': Any, 'errors': []}`
- [ ] **Error Handling**: Graceful error handling
- [ ] **Standalone Testing**: Can run standalone
- [ ] **Documentation**: SKILL.md complete
- [ ] **Configuration**: Supports config parameter

### For Agents

- [ ] **Standard Method**: `async def action(input_data, config=None)`
- [ ] **Return Format**: `{'success': bool, 'data': Any, 'errors': []}`
- [ ] **Error Handling**: Graceful error handling
- [ ] **Standalone Testing**: Can run standalone
- [ ] **Documentation**: AGENT.md complete
- [ ] **Configuration**: Supports config parameter

---

## 🔄 Workflow Execution Flow

### How Components Are Invoked

```
Workflow Executor
    ↓
Read workflow YAML
    ↓
For each step:
    ├─ Load component (skill/agent)
    ├─ Prepare input
    ├─ Prepare config
    ├─ Execute component
    ├─ Capture result
    ├─ Check success
    └─ Continue or abort
    ↓
Complete workflow
```

### Component Loading

**Skills**:
```python
# Workflow executor loads skill
from skills.workflow_skills.spec_parser.parser import parse_spec

result = parse_spec(input_data, config)
```

**Agents**:
```python
# Workflow executor loads agent
from agents.planner_agent.planner import PlannerAgent

agent = PlannerAgent()
result = await agent.validate_tasks(input_data, config)
```

---

## 🎯 Configuration Standards

### Workflow Configuration

```yaml
# In workflow YAML
- skill: spec_parser
  input: implementation_plan.md
  config:
    output_file: spec.json
    format: json
    validate: true
```

### Component Configuration

```python
def skill_function(input_data, config=None):
    """Skill function."""
    # Use config with defaults
    output_file = config.get('output_file') if config else None
    format = config.get('format', 'json') if config else 'json'
    validate = config.get('validate', True) if config else True
```

---

## 🧪 Testing Integration

### Test Workflow Invocation

```python
"""Test skill/agent in workflow context."""

import pytest
from workflows.engine.executor import WorkflowExecutor
from workflows.engine.parser import parse_workflow


@pytest.mark.asyncio
async def test_skill_in_workflow():
    """Test skill execution in workflow."""
    workflow_yaml = """
    name: Test Workflow
    phases:
      - name: test
        steps:
          - skill: spec_parser
            input: test_spec.md
            config:
              format: json
    """
    
    workflow = parse_workflow(workflow_yaml)
    executor = WorkflowExecutor()
    context = await executor.execute(workflow)
    
    assert context.status == 'success'
    assert len(context.phase_results) == 1
```

### Test Standalone Execution

```python
"""Test skill/agent standalone."""

def test_skill_standalone():
    """Test skill without workflow."""
    from skills.workflow_skills.spec_parser.parser import parse_spec
    
    result = parse_spec('test_spec.md', {'format': 'json'})
    
    assert result['success'] is True
    assert 'output' in result
```

---

## 📊 Integration Patterns

### Pattern 1: Sequential Skills

```yaml
phases:
  - name: process
    steps:
      - skill: spec_parser
        input: spec.md
        output: spec.json
      
      - skill: task_generator
        input: spec.json
        output: task.md
```

### Pattern 2: Agent + Skill

```yaml
phases:
  - name: plan
    steps:
      - skill: task_generator
        input: spec.json
        output: task.md
      
      - agent: planner_agent
        action: validate_tasks
        input: task.md
```

### Pattern 3: Conditional Execution

```yaml
phases:
  - name: validate
    steps:
      - agent: planner_agent
        action: validate_tasks
        input: task.md
        on_failure: abort
      
      - skill: task_generator
        input: spec.json
        condition: previous_success
```

---

## 🚨 Common Integration Issues

### Issue 1: Wrong Return Format

**Problem**: Component returns wrong format  
**Solution**: Follow standard return format

```python
# Wrong
def skill():
    return "result"

# Right
def skill():
    return {'success': True, 'output': "result", 'errors': []}
```

### Issue 2: No Error Handling

**Problem**: Exceptions crash workflow  
**Solution**: Handle errors gracefully

```python
# Wrong
def skill(input_data):
    data = parse_file(input_data)  # May raise exception
    return {'success': True, 'output': data}

# Right
def skill(input_data):
    try:
        data = parse_file(input_data)
        return {'success': True, 'output': data, 'errors': []}
    except Exception as e:
        return {'success': False, 'output': None, 'errors': [str(e)]}
```

### Issue 3: Ignoring Configuration

**Problem**: Component ignores config parameter  
**Solution**: Use config parameter

```python
# Wrong
def skill(input_data, config=None):
    # Ignores config
    return process(input_data)

# Right
def skill(input_data, config=None):
    options = config or {}
    return process(input_data, **options)
```

---

## 📝 Documentation Requirements

### SKILL.md Requirements

```markdown
## Workflow Integration

### Input Format
<Describe expected input>

### Configuration Options
- `option1`: <Description>
- `option2`: <Description>

### Output Format
<Describe output structure>

### Example Usage in Workflow
\`\`\`yaml
- skill: skill_name
  input: input_file
  config:
    option1: value1
\`\`\`
```

### AGENT.md Requirements

```markdown
## Workflow Integration

### Actions
1. **action_name**
   - Input: <Format>
   - Config: <Options>
   - Output: <Format>

### Example Usage in Workflow
\`\`\`yaml
- agent: agent_name
  action: action_name
  input: input_data
  config:
    option1: value1
\`\`\`
```

---

## ✅ Summary

Workflow-compatible components must:
- ✅ Follow standard interfaces
- ✅ Return structured results
- ✅ Handle errors gracefully
- ✅ Support configuration
- ✅ Be testable standalone
- ✅ Be documented

---

**Version**: 1.0.0  
**Created**: 2026-02-01  
**Status**: Active  
**Enforcement**: Mandatory for workflow integration
