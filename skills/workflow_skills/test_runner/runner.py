"""
Test Runner Skill
==================

Run automated tests and generate coverage reports.

This skill provides:
- Test execution using pytest
- Coverage reporting
- Threshold enforcement
- Result aggregation

Usage:
    from skills.workflow_skills.test_runner.runner import run_tests
    
    result = run_tests(test_dir='tests/', coverage_threshold=80)
"""

import subprocess
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict


@dataclass
class TestResult:
    """Test execution result."""
    all_passed: bool
    total_tests: int
    passed_tests: int
    failed_tests: int
    skipped_tests: int
    coverage: float
    duration: float
    failed_test_names: List[str]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return asdict(self)


class TestRunner:
    """Runs automated tests using pytest."""
    
    def __init__(
        self,
        test_dir: str = 'tests',
        coverage_threshold: float = 80.0,
        fail_on_low_coverage: bool = True
    ):
        self.test_dir = Path(test_dir)
        self.coverage_threshold = coverage_threshold
        self.fail_on_low_coverage = fail_on_low_coverage
    
    def run_tests(
        self,
        generate_report: bool = True,
        report_path: str = 'coverage.html'
    ) -> TestResult:
        """
        Run tests and generate coverage report.
        
        Args:
            generate_report: Whether to generate HTML report
            report_path: Path for HTML report
            
        Returns:
            TestResult object
        """
        if not self.test_dir.exists():
            raise FileNotFoundError(f"Test directory not found: {self.test_dir}")
        
        # Build pytest command
        cmd = [
            'pytest',
            str(self.test_dir),
            '-v',
            '--tb=short',
            f'--cov={self.test_dir.parent}',
            '--cov-report=term',
            '--cov-report=json:coverage.json'
        ]
        
        if generate_report:
            cmd.append(f'--cov-report=html:{report_path}')
        
        # Run tests
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300  # 5 minutes timeout
            )
            
            # Parse results
            test_result = self._parse_results(result)
            
            # Check coverage threshold
            if self.fail_on_low_coverage and test_result.coverage < self.coverage_threshold:
                print(f"⚠️  Coverage ({test_result.coverage}%) below threshold ({self.coverage_threshold}%)")
                test_result.all_passed = False
            
            return test_result
            
        except subprocess.TimeoutExpired:
            raise RuntimeError("Test execution timed out (5 minutes)")
        except FileNotFoundError:
            raise RuntimeError("pytest not found. Install with: pip install pytest pytest-cov")
    
    def _parse_results(self, result: subprocess.CompletedProcess) -> TestResult:
        """Parse pytest results."""
        output = result.stdout + result.stderr
        
        # Parse test counts from output
        total_tests = 0
        passed_tests = 0
        failed_tests = 0
        skipped_tests = 0
        failed_test_names = []
        
        # Look for summary line: "X passed, Y failed, Z skipped"
        import re
        summary_match = re.search(r'(\d+) passed', output)
        if summary_match:
            passed_tests = int(summary_match.group(1))
        
        failed_match = re.search(r'(\d+) failed', output)
        if failed_match:
            failed_tests = int(failed_match.group(1))
        
        skipped_match = re.search(r'(\d+) skipped', output)
        if skipped_match:
            skipped_tests = int(skipped_match.group(1))
        
        total_tests = passed_tests + failed_tests + skipped_tests
        
        # Parse coverage from JSON
        coverage = 0.0
        coverage_file = Path('coverage.json')
        if coverage_file.exists():
            try:
                with open(coverage_file, 'r') as f:
                    coverage_data = json.load(f)
                    coverage = coverage_data.get('totals', {}).get('percent_covered', 0.0)
            except Exception:
                pass
        
        # Parse duration
        duration_match = re.search(r'in ([\d.]+)s', output)
        duration = float(duration_match.group(1)) if duration_match else 0.0
        
        # Extract failed test names
        failed_pattern = r'FAILED (.+?) -'
        failed_test_names = re.findall(failed_pattern, output)
        
        return TestResult(
            all_passed=(failed_tests == 0 and result.returncode == 0),
            total_tests=total_tests,
            passed_tests=passed_tests,
            failed_tests=failed_tests,
            skipped_tests=skipped_tests,
            coverage=coverage,
            duration=duration,
            failed_test_names=failed_test_names
        )


def run_tests(
    test_dir: str = 'tests',
    coverage_threshold: float = 80.0,
    fail_on_low_coverage: bool = True,
    generate_report: bool = True,
    report_path: str = 'coverage.html'
) -> Dict[str, Any]:
    """
    Run tests and generate coverage report.
    
    Args:
        test_dir: Directory containing tests
        coverage_threshold: Minimum coverage percentage
        fail_on_low_coverage: Fail if coverage below threshold
        generate_report: Generate HTML report
        report_path: Path for HTML report
        
    Returns:
        Dictionary with test results
    """
    runner = TestRunner(
        test_dir=test_dir,
        coverage_threshold=coverage_threshold,
        fail_on_low_coverage=fail_on_low_coverage
    )
    
    result = runner.run_tests(
        generate_report=generate_report,
        report_path=report_path
    )
    
    return result.to_dict()


if __name__ == '__main__':
    # Test runner
    import sys
    
    test_dir = sys.argv[1] if len(sys.argv) > 1 else 'tests'
    
    try:
        result = run_tests(test_dir=test_dir)
        
        print("\n" + "="*60)
        print("TEST RESULTS")
        print("="*60)
        print(f"Total Tests:    {result['total_tests']}")
        print(f"Passed:         {result['passed_tests']}")
        print(f"Failed:         {result['failed_tests']}")
        print(f"Skipped:        {result['skipped_tests']}")
        print(f"Coverage:       {result['coverage']:.1f}%")
        print(f"Duration:       {result['duration']:.2f}s")
        
        if result['failed_test_names']:
            print(f"\nFailed Tests:")
            for test_name in result['failed_test_names']:
                print(f"  - {test_name}")
        
        if result['all_passed']:
            print("\n✅ All tests passed!")
            sys.exit(0)
        else:
            print("\n❌ Some tests failed")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
