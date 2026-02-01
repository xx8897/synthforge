"""
Summary Skill
=============

Extract context from task.md and session summaries to inform automation.
從 task.md 和會話摘要中提取上下文，以為自動化提供資訊。
"""

import re
from pathlib import Path
from typing import List, Dict, Optional, Any


class SummarySkill:
    """Skill to parse tasks and summaries for contextual awareness."""
    
    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path).resolve()
        
    def get_latest_completed_task(self) -> Optional[str]:
        """
        Find the last completed task [x] in task.md or active task artifacts.
        在 task.md 或活動任務工件中查找最後一個完成的任務 [x]。
        """
        # 1. Try to find the local task.md from the agent's brain directory
        # (This is the most current source of truth for the active task)
        # Note: In a real environment, we'd look for the specific conversation ID.
        # Here we'll look for a generic task.md if possible, or common locations.
        
        task_paths = [
            self.repo_path / "task.md",
            # Add other potential internal task paths
        ]
        
        # Also check the hidden internal planning folder
        internal_planning = self.repo_path / ".internal" / "planning"
        if internal_planning.exists():
            recent_todos = sorted(internal_planning.glob("TODO_*.md"), reverse=True)
            if recent_todos:
                task_paths.append(recent_todos[0])

        for path in task_paths:
            if path.exists():
                content = path.read_text(encoding='utf-8')
                # Find the last [x] or [/] item
                # Match: - [x] Task Description
                matches = re.findall(r'-\s+\[[xX/]\]\s+(.+)', content)
                if matches:
                    # Return the most recent one (last one found)
                    return matches[-1].strip()
        
        return None

    def get_all_active_tasks(self) -> List[str]:
        """Get all items marked as in-progress [/]."""
        active_tasks = []
        task_file = self.repo_path / "task.md"
        if task_file.exists():
            content = task_file.read_text(encoding='utf-8')
            matches = re.findall(r'-\s+\[/\]\s+(.+)', content)
            active_tasks = [m.strip() for m in matches]
        return active_tasks

    def get_summary_hints(self) -> str:
        """
        Extract hints from the latest summary file.
        從最新的摘要文件中提取提示。
        """
        summary_dir = self.repo_path / ".internal" / "summaries"
        if not summary_dir.exists():
            return ""
            
        # Get the most recent summary file
        summary_files = sorted(summary_dir.rglob("summary_*.md"), reverse=True)
        if not summary_files:
            return ""
            
        latest_summary = summary_files[0]
        content = latest_summary.read_text(encoding='utf-8')
        
        # Extract the objective or high-level goals
        match = re.search(r'# USER Objective:\s*\n(.+)', content)
        if match:
            return match.group(1).strip()
            
        return ""
