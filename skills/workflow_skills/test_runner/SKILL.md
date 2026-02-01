---
name: test_runner
description: Run automated tests and generate coverage reports
version: 1.0.0
tags: [workflow, testing, automation, tdd]
---

# Test Runner Skill

## Description

Runs automated tests and generates coverage reports for workflow automation.

執行自動化測試並生成覆蓋率報告，用於工作流自動化。

## When to Use

Use this skill when you need to:
- Run automated test suites
- Generate coverage reports
- Verify test results
- Enforce coverage thresholds

## Input

- **Configuration**: Test configuration
- **Test Directory**: Directory containing tests

## Output

- **Test Results**: Pass/fail status
- **Coverage Report**: Coverage percentage and details
- **Report File**: Optional JSON/HTML report

## Configuration

```yaml
- skill: test_runner
  action: run_all_tests
  config:
    test_dir: tests/              # Test directory
    coverage_threshold: 80        # Minimum coverage %
    fail_on_low_coverage: true    # Fail if below threshold
    generate_report: true         # Generate HTML report
    report_path: coverage.html    # Report output path
```

## Example

```python
from skills.workflow_skills.test_runner import run_tests

result = run_tests(
    test_dir='tests/',
    coverage_threshold=80
)

if result['all_passed']:
    print(f"✅ All tests passed ({result['coverage']}% coverage)")
else:
    print(f"❌ {result['failed_count']} tests failed")
```

## Dependencies

- Python 3.10+
- pytest
- pytest-cov

## Related Skills

- `executor_agent` - Uses test_runner for TDD
- `reviewer_agent` - Checks test coverage

---

**Version**: 1.0.0  
**Status**: Active Development  
**Maintainer**: synthforge team
