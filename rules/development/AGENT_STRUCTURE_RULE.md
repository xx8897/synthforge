---
name: AGENT_STRUCTURE_RULE
category: development
priority: high
version: 1.0.0
related_rules:
  - AGENT_WORKFLOW_RULE
  - FILE_NAMING_CONVENTION_RULE
  - CODING_STYLE_RULE
---

# AGENT_STRUCTURE_RULE - Agent Development Standards

**Agent 開發標準規則**

---

## 📋 Purpose

Standardize the structure, development, and testing of AI agents in synthforge.

標準化 synthforge 中 AI agents 的結構、開發和測試。

---

## 🏗️ Agent Directory Structure

### Standard Agent Structure

```
agents/
├── README.md                          # Agents overview
├── <agent_name>/
│   ├── AGENT.md                       # Agent documentation
│   ├── <agent_name>.py                # Agent implementation
│   ├── config.yml                     # Agent configuration
│   ├── __init__.py                    # Package initialization
│   └── tests/                         # Agent tests (optional)
│       ├── test_<agent_name>.py
│       └── fixtures/
└── <another_agent>/
    └── ...
```

### Example: planner_agent

```
agents/planner_agent/
├── AGENT.md                           # Documentation
├── planner.py                         # Implementation
├── config.yml                         # Configuration
├── __init__.py                        # Package init
└── tests/                             # Tests
    ├── test_planner.py
    └── fixtures/
        └── sample_task.md
```

---

## 📄 Required Files

### 1. AGENT.md (Required)

**Purpose**: Agent documentation

**Template**:
```markdown
---
name: <agent_name>
role: <agent_role>
goal: <agent_goal>
version: 1.0.0
---

# <Agent Name> Agent

## Role & Responsibilities

<Description of what this agent does>

### Primary Responsibilities

1. **<Responsibility 1>**
   - <Details>

2. **<Responsibility 2>**
   - <Details>

---

## Available Actions

### 1. <action_name>

**Purpose**: <What this action does>

**Input**: <Input format>

**Output**: <Output format>

**Example**:
\`\`\`yaml
- agent: <agent_name>
  action: <action_name>
  config:
    param1: value1
\`\`\`

---

## Configuration

Default configuration in \`config.yml\`:

\`\`\`yaml
agent:
  name: <agent_name>
  version: 1.0.0
  
settings:
  setting1: value1
\`\`\`

---

## Example Usage

\`\`\`python
from agents.<agent_name>.<agent_name> import <AgentClass>

agent = <AgentClass>()
result = await agent.<action_name>(params)
\`\`\`
```

---

### 2. Implementation File (Required)

**Naming**: `<agent_name>.py`

**Template**:
```python
"""
<Agent Name> Agent
==================

<Brief description>

This agent provides:
- <Feature 1>
- <Feature 2>

Usage:
    from agents.<agent_name>.<agent_name> import <AgentClass>
    
    agent = <AgentClass>()
    result = await agent.<action>(params)
"""

from pathlib import Path
from typing import Dict, List, Any, Optional
import yaml


class <AgentClass>:
    """<Agent description>."""
    
    def __init__(self, config_path: str = None):
        """Initialize agent with configuration."""
        self.config = self._load_config(config_path)
    
    def _load_config(self, config_path: str = None) -> Dict[str, Any]:
        """Load agent configuration."""
        if config_path and Path(config_path).exists():
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        
        # Default configuration
        return {
            'agent': {
                'name': '<agent_name>',
                'version': '1.0.0'
            },
            'settings': {}
        }
    
    async def <action_name>(
        self,
        param1: str,
        param2: int = 0
    ) -> Dict[str, Any]:
        """
        <Action description>.
        
        Args:
            param1: <Description>
            param2: <Description>
            
        Returns:
            Result dictionary
        """
        # Implementation
        result = {
            'success': True,
            'data': {}
        }
        
        return result


if __name__ == '__main__':
    # Standalone testing
    import asyncio
    import sys
    
    async def main():
        if len(sys.argv) > 1:
            # CLI usage
            agent = <AgentClass>()
            result = await agent.<action_name>(sys.argv[1])
            print(result)
        else:
            print("Usage: python <agent_name>.py <params>")
    
    asyncio.run(main())
```

---

### 3. config.yml (Required)

**Purpose**: Agent configuration

**Template**:
```yaml
agent:
  name: <agent_name>
  version: 1.0.0
  role: <agent_role>
  
settings:
  # Agent-specific settings
  setting1: value1
  setting2: value2
  
# Optional sections
thresholds:
  threshold1: 10
  
features:
  feature1: true
  feature2: false
```

---

### 4. __init__.py (Optional)

**Purpose**: Package initialization

**Content**:
```python
"""<Agent Name> Agent package."""

from .<agent_name> import <AgentClass>

__all__ = ['<AgentClass>']
__version__ = '1.0.0'
```

---

## 🎯 Agent Development Standards

### 1. Agent Class Structure

```python
class AgentName:
    """Agent description."""
    
    def __init__(self, config_path: str = None):
        """Initialize agent."""
        self.config = self._load_config(config_path)
        self.state = {}  # Agent state (if needed)
    
    def _load_config(self, config_path: str = None) -> Dict:
        """Load configuration."""
        pass
    
    async def action_name(self, **kwargs) -> Dict[str, Any]:
        """Public action method."""
        pass
    
    def _helper_method(self):
        """Private helper method."""
        pass
```

### 2. Naming Conventions

**Agent Names**:
- Format: `<purpose>_agent`
- Examples: `planner_agent`, `executor_agent`, `reviewer_agent`
- Lowercase with underscores

**Class Names**:
- Format: `<Purpose>Agent`
- Examples: `PlannerAgent`, `ExecutorAgent`, `ReviewerAgent`
- PascalCase

**Action Methods**:
- Format: `<verb>_<noun>`
- Examples: `validate_tasks`, `implement_fix`, `review_code`
- Lowercase with underscores

### 3. Return Format

All agent actions should return a dictionary:

```python
{
    'success': bool,           # Required: True/False
    'data': Any,              # Optional: Result data
    'errors': List[str],      # Optional: Error messages
    'metadata': Dict          # Optional: Additional info
}
```

### 4. Error Handling

```python
async def action_name(self, param: str) -> Dict[str, Any]:
    """Action with error handling."""
    result = {
        'success': True,
        'errors': []
    }
    
    try:
        # Action logic
        data = self._process(param)
        result['data'] = data
        
    except ValueError as e:
        result['success'] = False
        result['errors'].append(f"Invalid input: {e}")
    
    except Exception as e:
        result['success'] = False
        result['errors'].append(f"Unexpected error: {e}")
    
    return result
```

---

## 🧪 Testing Standards

### Test Structure

```
agents/<agent_name>/tests/
├── test_<agent_name>.py       # Main tests
├── test_actions.py            # Action tests
├── test_config.py             # Config tests
└── fixtures/                  # Test data
    ├── sample_input.json
    └── expected_output.json
```

### Test Template

```python
"""
Tests for <Agent Name> Agent
"""

import pytest
from agents.<agent_name>.<agent_name> import <AgentClass>


class Test<AgentClass>:
    """Test suite for <AgentClass>."""
    
    @pytest.fixture
    def agent(self):
        """Create agent instance."""
        return <AgentClass>()
    
    @pytest.mark.asyncio
    async def test_<action>_success(self, agent):
        """Test successful action execution."""
        result = await agent.<action>(valid_input)
        
        assert result['success'] is True
        assert 'data' in result
    
    @pytest.mark.asyncio
    async def test_<action>_error_handling(self, agent):
        """Test error handling."""
        result = await agent.<action>(invalid_input)
        
        assert result['success'] is False
        assert len(result['errors']) > 0
```

### Coverage Requirements

- **Minimum**: 80% code coverage
- **Actions**: All public actions tested
- **Error Paths**: Error handling tested
- **Edge Cases**: Edge cases covered

---

## 🔄 Workflow Integration

### Agent Invocation in Workflows

```yaml
# In workflow YAML
phases:
  - name: planning
    steps:
      - agent: planner_agent
        action: validate_tasks
        input: task.md
        config:
          max_depth: 5
          check_dependencies: true
```

### Agent Interface

All agents must implement:

```python
class AgentInterface:
    """Base interface for all agents."""
    
    def __init__(self, config_path: str = None):
        """Initialize agent."""
        pass
    
    async def execute_action(
        self,
        action: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Execute agent action.
        
        Args:
            action: Action name
            **kwargs: Action parameters
            
        Returns:
            Result dictionary
        """
        pass
```

---

## 📋 Agent Development Checklist

### Before Creating Agent

- [ ] Define agent purpose and responsibilities
- [ ] Identify required actions
- [ ] Design configuration schema
- [ ] Plan integration with workflows

### During Development

- [ ] Create agent directory structure
- [ ] Write AGENT.md documentation
- [ ] Implement agent class
- [ ] Create config.yml
- [ ] Write tests (TDD)
- [ ] Ensure 80%+ coverage

### After Development

- [ ] All tests pass
- [ ] Documentation complete
- [ ] Standalone testing works
- [ ] Workflow integration tested
- [ ] Code review completed

---

## 🎓 Best Practices

### 1. Keep Agents Focused

Each agent should have a **single, clear responsibility**.

**Good**: `reviewer_agent` - Code review only  
**Bad**: `super_agent` - Does everything

### 2. Use Configuration

Make agents configurable via `config.yml`:

```yaml
agent:
  name: reviewer_agent
  
settings:
  check_style: true
  check_security: true
  
thresholds:
  min_coverage: 80
```

### 3. Provide Standalone Testing

Agents should be testable standalone:

```bash
python agents/planner_agent/planner.py task.md
```

### 4. Document Actions

Each action should be well-documented:

```python
async def validate_tasks(
    self,
    task_file: str,
    max_depth: int = 5
) -> Dict[str, Any]:
    """
    Validate tasks from task.md.
    
    Args:
        task_file: Path to task.md
        max_depth: Maximum task nesting depth
        
    Returns:
        {
            'success': bool,
            'valid': bool,
            'task_count': int,
            'errors': List[str]
        }
    """
```

### 5. Use Async/Await

All agent actions should be async:

```python
async def action_name(self, param: str) -> Dict[str, Any]:
    """Async action."""
    result = await some_async_operation(param)
    return {'success': True, 'data': result}
```

---

## 🚨 Common Mistakes

### ❌ Too Many Responsibilities

**Wrong**: Agent does too many things  
**Right**: One agent, one responsibility

### ❌ No Configuration

**Wrong**: Hardcoded values  
**Right**: Configurable via config.yml

### ❌ Poor Error Handling

**Wrong**: Exceptions crash agent  
**Right**: Graceful error handling with error messages

### ❌ No Tests

**Wrong**: No tests  
**Right**: Comprehensive test coverage

---

## 📊 Agent Quality Metrics

### Track These Metrics

1. **Test Coverage**: ≥80%
2. **Action Count**: Number of actions
3. **Configuration Complexity**: Number of config options
4. **Documentation Quality**: AGENT.md completeness

---

## ✅ Summary

Good agents are:
- ✅ Focused (single responsibility)
- ✅ Configurable (via config.yml)
- ✅ Documented (AGENT.md)
- ✅ Tested (≥80% coverage)
- ✅ Async (async/await)
- ✅ Error-handled (graceful failures)

---

**Version**: 1.0.0  
**Created**: 2026-02-01  
**Status**: Active  
**Enforcement**: Mandatory for all agents
