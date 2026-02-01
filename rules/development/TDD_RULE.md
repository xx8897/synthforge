---
name: TDD_RULE
category: development
priority: high
version: 1.0.0
related_rules:
  - SPEC_DRIVEN_DEVELOPMENT_RULE
  - CODING_STYLE_RULE
  - AGENT_WORKFLOW_RULE
---

# TDD_RULE - Test-Driven Development Rule

**測試驅動開發規則**

---

## 📋 Purpose

Define Test-Driven Development (TDD) workflow and automation standards for synthforge.

定義 synthforge 的測試驅動開發（TDD）工作流程和自動化標準。

---

## 🎯 Core Principles

### 1. Red-Green-Refactor Cycle

**The TDD Mantra**:
1. **Red**: Write a failing test
2. **Green**: Write minimal code to pass the test
3. **Refactor**: Improve code while keeping tests green

**TDD 口訣**：
1. **紅燈**：寫一個失敗的測試
2. **綠燈**：寫最少的代碼讓測試通過
3. **重構**：改進代碼，保持測試通過

### 2. Test First, Always

- ✅ Write test before implementation
- ✅ No production code without a failing test
- ✅ Tests define the specification

### 3. Small Steps

- ✅ One test at a time
- ✅ Minimal code to pass
- ✅ Frequent commits

---

## 🔄 TDD Workflow

### Standard TDD Cycle

```
1. Read Task
   ↓
2. Write Test (Red)
   - Test fails (expected)
   ↓
3. Write Code (Green)
   - Minimal implementation
   - Test passes
   ↓
4. Refactor (Clean)
   - Improve code quality
   - Tests still pass
   ↓
5. Commit
   ↓
6. Next Task → Repeat
```

### Integration with SPEC_DRIVEN_DEVELOPMENT

```
Spec (implementation_plan.md)
   ↓
Tasks (task.md)
   ↓
For each task:
   ├─ Write Test (Red)
   ├─ Implement (Green)
   ├─ Refactor (Clean)
   └─ Commit
   ↓
All tasks complete
```

---

## 📝 Testing Standards

### Test Structure

Use **AAA Pattern** (Arrange-Act-Assert):

```python
def test_example():
    # Arrange - Setup
    input_data = create_test_data()
    expected_output = "expected result"
    
    # Act - Execute
    actual_output = function_under_test(input_data)
    
    # Assert - Verify
    assert actual_output == expected_output
```

### Test Naming Convention

**Format**: `test_<function>_<scenario>_<expected_result>`

**Examples**:
```python
def test_parse_workflow_valid_yaml_returns_workflow_object()
def test_parse_workflow_invalid_yaml_raises_error()
def test_execute_workflow_empty_phases_completes_successfully()
```

### Test Organization

```
project/
├── src/
│   └── module.py
└── tests/
    ├── unit/
    │   └── test_module.py
    ├── integration/
    │   └── test_integration.py
    └── e2e/
        └── test_end_to_end.py
```

---

## 🎯 Coverage Requirements

### Minimum Coverage

- **Unit Tests**: 80% coverage minimum
- **Integration Tests**: Critical paths covered
- **E2E Tests**: Main workflows covered

### What to Test

**✅ Must Test**:
- Public APIs
- Business logic
- Edge cases
- Error handling

**❌ Don't Test**:
- Third-party libraries
- Simple getters/setters
- Configuration files

---

## 🤖 TDD Automation

### Automated Test Running

**Using pytest**:
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/unit/test_module.py

# Run tests matching pattern
pytest -k "test_parse"

# Watch mode (requires pytest-watch)
ptw
```

### Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: pytest
        language: system
        pass_filenames: false
        always_run: true
```

### CI/CD Integration

```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: |
          pip install -r requirements.txt
          pytest --cov=src --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v2
```

---

## 🛠️ TDD with Workflow System

### Executor Agent Integration

The `executor_agent` implements TDD automatically:

```yaml
# In workflow
- agent: executor_agent
  action: implement_tasks
  mode: TDD
  config:
    test_first: true
    coverage_threshold: 80
```

**Agent Behavior**:
1. Read task from task.md
2. Write test (Red)
3. Implement code (Green)
4. Refactor (Clean)
5. Run tests
6. Verify coverage
7. Commit changes

### Test Runner Skill

```yaml
# In workflow
- skill: test_runner
  config:
    test_path: tests/
    coverage_threshold: 80
    generate_report: true
```

---

## 📋 TDD Checklist

### Before Writing Code

- [ ] Read and understand the task
- [ ] Identify what needs to be tested
- [ ] Write test cases (at least one)
- [ ] Verify test fails (Red)

### While Writing Code

- [ ] Write minimal code to pass test
- [ ] Run tests frequently
- [ ] Keep tests green
- [ ] Refactor when needed

### After Writing Code

- [ ] All tests pass (Green)
- [ ] Coverage meets threshold (≥80%)
- [ ] Code is clean and readable
- [ ] Commit with meaningful message

---

## 🎓 TDD Best Practices

### 1. Write Simple Tests

**Good**:
```python
def test_add_two_numbers():
    assert add(2, 3) == 5
```

**Bad** (too complex):
```python
def test_calculator():
    # Tests too many things at once
    assert add(2, 3) == 5
    assert subtract(5, 3) == 2
    assert multiply(2, 3) == 6
```

### 2. Test One Thing at a Time

Each test should verify **one behavior**.

### 3. Use Descriptive Names

Test names should describe **what** is being tested and **what** is expected.

### 4. Keep Tests Independent

Tests should not depend on each other.

### 5. Use Fixtures for Setup

```python
import pytest

@pytest.fixture
def sample_data():
    return {"key": "value"}

def test_with_fixture(sample_data):
    assert sample_data["key"] == "value"
```

---

## 🚨 Common TDD Mistakes

### ❌ Writing Tests After Code

**Wrong**: Code first, tests later  
**Right**: Tests first, code second

### ❌ Testing Implementation Details

**Wrong**: Testing private methods  
**Right**: Testing public APIs

### ❌ Large Test Functions

**Wrong**: One test testing everything  
**Right**: Multiple small, focused tests

### ❌ Ignoring Failing Tests

**Wrong**: Commenting out failing tests  
**Right**: Fix the code or fix the test

---

## 🔧 Tools

### Testing Frameworks

- **Python**: pytest, unittest
- **JavaScript**: Jest, Mocha
- **Go**: testing package

### Coverage Tools

- **Python**: pytest-cov, coverage.py
- **JavaScript**: Istanbul, nyc

### Mocking Tools

- **Python**: unittest.mock, pytest-mock
- **JavaScript**: sinon, jest.mock

---

## 📊 TDD Metrics

### Track These Metrics

1. **Test Coverage**: % of code covered by tests
2. **Test Count**: Number of tests
3. **Test Execution Time**: How long tests take
4. **Test Failure Rate**: % of tests failing

### Target Metrics

- Coverage: ≥80%
- Execution Time: <5 minutes for unit tests
- Failure Rate: <1% (in main branch)

---

## 🔄 Integration with Other Rules

### SPEC_DRIVEN_DEVELOPMENT_RULE

TDD is the **implementation phase** of SDD:
- Spec defines **what** to build
- TDD defines **how** to build it

### CODING_STYLE_RULE

- Tests follow same coding style
- Clean, readable test code
- Consistent naming

### AGENT_WORKFLOW_RULE

- TDD is mandatory in workflows
- Executor agent enforces TDD
- Test runner validates coverage

---

## 📝 Examples

### Example 1: Simple Function

**Task**: Implement `add(a, b)` function

**Step 1 - Write Test (Red)**:
```python
def test_add_two_positive_numbers():
    assert add(2, 3) == 5
```

**Step 2 - Implement (Green)**:
```python
def add(a, b):
    return a + b
```

**Step 3 - Refactor (Clean)**:
```python
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b
```

### Example 2: Workflow Parser

**Task**: Parse YAML workflow file

**Step 1 - Write Test (Red)**:
```python
def test_parse_workflow_valid_yaml_returns_workflow_object():
    yaml_content = """
    name: Test Workflow
    phases:
      - name: test_phase
    """
    workflow = parse_workflow(yaml_content)
    assert workflow.name == "Test Workflow"
    assert len(workflow.phases) == 1
```

**Step 2 - Implement (Green)**:
```python
def parse_workflow(yaml_content: str) -> Workflow:
    data = yaml.safe_load(yaml_content)
    return Workflow(
        name=data['name'],
        phases=data['phases']
    )
```

**Step 3 - Refactor (Clean)**:
```python
def parse_workflow(yaml_content: str) -> Workflow:
    """Parse YAML workflow definition."""
    try:
        data = yaml.safe_load(yaml_content)
        return Workflow(
            name=data.get('name', 'Unnamed'),
            phases=data.get('phases', [])
        )
    except yaml.YAMLError as e:
        raise WorkflowParseError(f"Invalid YAML: {e}")
```

---

## ✅ Summary

TDD ensures:
- ✅ Code works as expected
- ✅ Bugs are caught early
- ✅ Refactoring is safe
- ✅ Documentation through tests
- ✅ Better design

**Remember**: **Red → Green → Refactor** 🔴 → 🟢 → 🔵

---

**Version**: 1.0.0  
**Created**: 2026-02-01  
**Status**: Active  
**Enforcement**: Mandatory in workflows
