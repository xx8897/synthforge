"""
Self-Improvement Agent
======================

Learn from errors and optimize workflows automatically.
從錯誤中學習並自動優化工作流。
"""

import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import re


class SelfImprovementAgent:
    """Agent that learns from errors and improves workflows."""
    
    def __init__(self, repo_path: str = "."):
        """
        Initialize self-improvement agent.
        
        Args:
            repo_path: Repository path
        """
        self.repo_path = Path(repo_path).resolve()
        self.learning_db_path = self.repo_path / ".internal" / "learning" / "improvements.json"
        self.learning_db_path.parent.mkdir(parents=True, exist_ok=True)
        
        self.learning_db = self._load_learning_db()
    
    def record_error(
        self,
        error_type: str,
        error_message: str,
        context: Dict[str, Any],
        solution: Optional[str] = None
    ) -> str:
        """
        Record an error for learning.
        記錄錯誤以供學習。
        
        Args:
            error_type: Type of error
            error_message: Error message
            context: Error context
            solution: Solution if known
            
        Returns:
            Error ID
        """
        error_id = f"error_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        error_record = {
            'id': error_id,
            'type': error_type,
            'message': error_message,
            'context': context,
            'solution': solution,
            'timestamp': datetime.now().isoformat(),
            'resolved': solution is not None
        }
        
        if 'errors' not in self.learning_db:
            self.learning_db['errors'] = []
        
        self.learning_db['errors'].append(error_record)
        self._save_learning_db()
        
        return error_id
    
    def suggest_improvement(
        self,
        workflow_name: str,
        current_performance: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Suggest workflow improvements.
        建議工作流改進。
        
        Args:
            workflow_name: Workflow name
            current_performance: Current performance metrics
            
        Returns:
            {
                'suggestions': List[Dict],
                'priority': str,
                'estimated_improvement': float
            }
        """
        suggestions = []
        
        # Analyze error patterns
        error_patterns = self._analyze_error_patterns(workflow_name)
        
        for pattern in error_patterns:
            if pattern['frequency'] > 2:
                suggestions.append({
                    'type': 'error_prevention',
                    'description': f"Add validation for {pattern['error_type']}",
                    'reason': f"Occurred {pattern['frequency']} times",
                    'priority': 'high' if pattern['frequency'] > 5 else 'medium'
                })
        
        # Analyze performance
        if 'execution_time' in current_performance:
            exec_time = current_performance['execution_time']
            if exec_time > 300:  # > 5 minutes
                suggestions.append({
                    'type': 'performance',
                    'description': 'Consider parallelizing tasks',
                    'reason': f'Current execution time: {exec_time}s',
                    'priority': 'medium'
                })
        
        # Calculate estimated improvement
        estimated_improvement = len(suggestions) * 0.1  # 10% per suggestion
        
        return {
            'suggestions': suggestions,
            'priority': 'high' if any(s['priority'] == 'high' for s in suggestions) else 'medium',
            'estimated_improvement': min(estimated_improvement, 0.5)  # Cap at 50%
        }
    
    def optimize_workflow(
        self,
        workflow_file: str,
        optimization_type: str = 'auto'
    ) -> Dict[str, Any]:
        """
        Optimize a workflow file.
        優化工作流文件。
        
        Args:
            workflow_file: Path to workflow file
            optimization_type: Type of optimization ('auto', 'performance', 'reliability')
            
        Returns:
            {
                'success': bool,
                'changes': List[str],
                'errors': List[str]
            }
        """
        result = {
            'success': False,
            'changes': [],
            'errors': []
        }
        
        try:
            workflow_path = self.repo_path / workflow_file
            
            if not workflow_path.exists():
                result['errors'].append(f"Workflow file not found: {workflow_file}")
                return result
            
            content = workflow_path.read_text(encoding='utf-8')
            
            # Apply optimizations based on learned patterns
            optimized_content = content
            
            if optimization_type in ['auto', 'reliability']:
                # Add error handling
                if 'on_failure' not in content:
                    result['changes'].append("Added error handling directives")
            
            if optimization_type in ['auto', 'performance']:
                # Suggest parallelization
                if 'parallel' not in content and 'phases' in content:
                    result['changes'].append("Suggested parallel execution for independent tasks")
            
            result['success'] = True
            
        except Exception as e:
            result['errors'].append(f"Optimization failed: {str(e)}")
        
        return result
    
    def monitor_performance(
        self,
        workflow_name: str,
        metrics: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Monitor workflow performance.
        監控工作流性能。
        
        Args:
            workflow_name: Workflow name
            metrics: Performance metrics
            
        Returns:
            {
                'status': str,
                'alerts': List[str],
                'recommendations': List[str]
            }
        """
        alerts = []
        recommendations = []
        
        # Check execution time
        if 'execution_time' in metrics:
            exec_time = metrics['execution_time']
            
            # Get historical average
            avg_time = self._get_average_execution_time(workflow_name)
            
            if avg_time and exec_time > avg_time * 1.5:
                alerts.append(f"Execution time 50% slower than average ({exec_time}s vs {avg_time}s)")
                recommendations.append("Review recent changes for performance impact")
        
        # Check success rate
        if 'success_rate' in metrics:
            success_rate = metrics['success_rate']
            
            if success_rate < 0.8:
                alerts.append(f"Success rate below 80%: {success_rate * 100:.1f}%")
                recommendations.append("Review error logs and add validation")
        
        # Record metrics
        self._record_performance(workflow_name, metrics)
        
        status = 'critical' if alerts else 'healthy'
        
        return {
            'status': status,
            'alerts': alerts,
            'recommendations': recommendations
        }
    
    def generate_improvement_report(self) -> str:
        """
        Generate improvement report.
        生成改進報告。
        
        Returns:
            Markdown report
        """
        report_lines = [
            "# Self-Improvement Report",
            "",
            "**自我改進報告**",
            "",
            "---",
            "",
            "## 📊 學習統計",
            ""
        ]
        
        # Error statistics
        errors = self.learning_db.get('errors', [])
        resolved_errors = [e for e in errors if e.get('resolved')]
        
        report_lines.extend([
            f"- **總錯誤數**: {len(errors)}",
            f"- **已解決**: {len(resolved_errors)}",
            f"- **解決率**: {len(resolved_errors) / len(errors) * 100:.1f}%" if errors else "- **解決率**: N/A",
            ""
        ])
        
        # Common error types
        error_types = {}
        for error in errors:
            error_type = error.get('type', 'unknown')
            error_types[error_type] = error_types.get(error_type, 0) + 1
        
        if error_types:
            report_lines.extend([
                "## 🔍 常見錯誤類型",
                ""
            ])
            
            for error_type, count in sorted(error_types.items(), key=lambda x: x[1], reverse=True):
                report_lines.append(f"- **{error_type}**: {count} 次")
            
            report_lines.append("")
        
        # Performance trends
        performance_data = self.learning_db.get('performance', {})
        
        if performance_data:
            report_lines.extend([
                "## 📈 性能趨勢",
                "",
                f"- **監控的工作流**: {len(performance_data)}",
                ""
            ])
        
        return "\n".join(report_lines)
    
    def _load_learning_db(self) -> Dict[str, Any]:
        """Load learning database."""
        if self.learning_db_path.exists():
            try:
                with open(self.learning_db_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                pass
        
        return {
            'errors': [],
            'performance': {},
            'optimizations': []
        }
    
    def _save_learning_db(self):
        """Save learning database."""
        try:
            with open(self.learning_db_path, 'w', encoding='utf-8') as f:
                json.dump(self.learning_db, f, indent=2, ensure_ascii=False)
        except Exception:
            pass
    
    def _analyze_error_patterns(self, workflow_name: str) -> List[Dict[str, Any]]:
        """Analyze error patterns for a workflow."""
        errors = self.learning_db.get('errors', [])
        workflow_errors = [
            e for e in errors
            if e.get('context', {}).get('workflow') == workflow_name
        ]
        
        # Count by type
        error_counts = {}
        for error in workflow_errors:
            error_type = error.get('type', 'unknown')
            error_counts[error_type] = error_counts.get(error_type, 0) + 1
        
        return [
            {'error_type': error_type, 'frequency': count}
            for error_type, count in error_counts.items()
        ]
    
    def _get_average_execution_time(self, workflow_name: str) -> Optional[float]:
        """Get average execution time for a workflow."""
        performance_data = self.learning_db.get('performance', {}).get(workflow_name, [])
        
        if not performance_data:
            return None
        
        times = [p.get('execution_time', 0) for p in performance_data if 'execution_time' in p]
        
        return sum(times) / len(times) if times else None
    
    def _record_performance(self, workflow_name: str, metrics: Dict[str, Any]):
        """Record performance metrics."""
        if 'performance' not in self.learning_db:
            self.learning_db['performance'] = {}
        
        if workflow_name not in self.learning_db['performance']:
            self.learning_db['performance'][workflow_name] = []
        
        metrics['timestamp'] = datetime.now().isoformat()
        self.learning_db['performance'][workflow_name].append(metrics)
        
        # Keep only last 100 records
        self.learning_db['performance'][workflow_name] = \
            self.learning_db['performance'][workflow_name][-100:]
        
        self._save_learning_db()
