---
name: reviewer_agent
role: Code Review and Quality Assurance
goal: Review code changes and ensure quality standards
version: 1.0.0
---

# Reviewer Agent

## Role & Responsibilities

The **Reviewer Agent** is responsible for code review and quality assurance.

**審查代理**負責代碼審查和質量保證。

### Primary Responsibilities

1. **Code Review**
   - Review code changes
   - Check coding standards
   - Identify potential issues

2. **Quality Checks**
   - Verify test coverage
   - Check security vulnerabilities
   - Assess performance

3. **Rule Compliance**
   - Verify adherence to rules
   - Check documentation
   - Validate naming conventions

4. **Improvement Suggestions**
   - Suggest optimizations
   - Recommend refactoring
   - Provide feedback

---

## Available Actions

### 1. code_review

**Purpose**: Review code changes

**Input**: Code changes (diff or files)

**Example**:
```yaml
- agent: reviewer_agent
  action: code_review
  config:
    checks: [style, security, performance, maintainability]
    rules_path: ./rules/
    auto_fix_minor: false
```

---

### 2. review_fix

**Purpose**: Review bug fix

**Input**: Fix implementation

**Example**:
```yaml
- agent: reviewer_agent
  action: review_fix
  config:
    check_side_effects: true
    verify_minimal_changes: true
```

---

### 3. review_refactoring

**Purpose**: Review refactored code

**Input**: Refactored code

**Example**:
```yaml
- agent: reviewer_agent
  action: review_refactoring
  config:
    check_code_quality: true
    verify_no_behavior_change: true
    check_performance: true
```

---

## Configuration

Default configuration in `config.yml`:

```yaml
agent:
  name: reviewer_agent
  version: 1.0.0
  
settings:
  check_style: true
  check_security: true
  check_performance: true
  check_tests: true
  
thresholds:
  min_coverage: 80
  max_complexity: 10
  max_function_length: 50
```

---

## Review Checklist

### Code Style
- [ ] Follows coding standards
- [ ] Consistent naming
- [ ] Proper formatting

### Security
- [ ] No security vulnerabilities
- [ ] Input validation
- [ ] Proper error handling

### Performance
- [ ] No obvious bottlenecks
- [ ] Efficient algorithms
- [ ] Proper resource management

### Tests
- [ ] Adequate test coverage
- [ ] Tests are meaningful
- [ ] Edge cases covered

### Documentation
- [ ] Code is documented
- [ ] README updated
- [ ] Examples provided

---

## Tools Available

The reviewer agent can use:
- Static analysis tools
- Security scanners
- Performance profilers
- Test coverage tools

---

## Example Usage

```python
from agents.reviewer_agent.reviewer import ReviewerAgent

agent = ReviewerAgent()
result = await agent.code_review(
    files=['src/module.py'],
    checks=['style', 'security', 'performance']
)

if result['approved']:
    print(f"✅ Code review passed")
else:
    print(f"❌ Issues found:")
    for issue in result['issues']:
        print(f"   - {issue}")
```

---

**Version**: 1.0.0  
**Status**: Active Development  
**Maintainer**: synthforge team
