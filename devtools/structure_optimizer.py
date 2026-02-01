"""
Structure Optimization Automation Script
結構優化自動化腳本

This script handles file operations for structure optimization:
- Delete directories/files
- Move files
- Rename files
- Restructure directories

Usage:
    python structure_optimizer.py --confirm
"""

from pathlib import Path
import shutil
from typing import List, Tuple
import sys
import os

# Ensure project root is in python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core_lib.utils.files import batch_move_files, list_directory_tree

class StructureOptimizer:
    """Handle structure optimization operations"""
    
    def __init__(self, base_path: Path, dry_run: bool = True):
        self.base = base_path
        self.dry_run = dry_run
        self.operations = []
    
    def delete_directory(self, dir_path: str) -> None:
        """Delete a directory and all its contents"""
        full_path = self.base / dir_path
        self.operations.append(('DELETE_DIR', dir_path))
        
        if not self.dry_run:
            if full_path.exists():
                shutil.rmtree(full_path)
                print(f'✅ Deleted directory: {dir_path}')
            else:
                print(f'⚠️  Directory not found: {dir_path}')
        else:
            print(f'[DRY RUN] Would delete directory: {dir_path}')
    
    def delete_file(self, file_path: str) -> None:
        """Delete a single file"""
        full_path = self.base / file_path
        self.operations.append(('DELETE_FILE', file_path))
        
        if not self.dry_run:
            if full_path.exists():
                full_path.unlink()
                print(f'✅ Deleted file: {file_path}')
            else:
                print(f'⚠️  File not found: {file_path}')
        else:
            print(f'[DRY RUN] Would delete file: {file_path}')
    
    def move_files(self, moves: List[Tuple[str, str]]) -> None:
        """Move multiple files"""
        self.operations.append(('MOVE_FILES', moves))
        
        if not self.dry_run:
            batch_move_files(moves, self.base)
        else:
            print(f'[DRY RUN] Would move {len(moves)} files:')
            for src, dst in moves:
                print(f'  {src} → {dst}')
    
    def rename_file(self, old_path: str, new_path: str) -> None:
        """Rename a file"""
        old_full = self.base / old_path
        new_full = self.base / new_path
        self.operations.append(('RENAME', old_path, new_path))
        
        if not self.dry_run:
            if old_full.exists():
                old_full.rename(new_full)
                print(f'✅ Renamed: {old_path} → {new_path}')
            else:
                print(f'⚠️  File not found: {old_path}')
        else:
            print(f'[DRY RUN] Would rename: {old_path} → {new_path}')
    
    def show_summary(self) -> None:
        """Show summary of all operations"""
        print('\n' + '='*60)
        print('OPERATION SUMMARY')
        print('='*60)
        for op in self.operations:
            print(f'  {op[0]}: {op[1] if len(op) > 1 else ""}')
        print('='*60 + '\n')

def main():
    """Main execution"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Structure Optimization Script')
    parser.add_argument('--confirm', action='store_true', help='Execute operations (default is dry run)')
    parser.add_argument('--base', type=str, default='.', help='Base directory')
    args = parser.parse_args()
    
    base_path = Path(args.base).resolve()
    optimizer = StructureOptimizer(base_path, dry_run=not args.confirm)
    
    print('🚀 Structure Optimization Script')
    print(f'📁 Base: {base_path}')
    print(f'🔧 Mode: {"EXECUTE" if args.confirm else "DRY RUN"}\n')
    
    # Task 1: Delete skills/examples/
    print('Task 1: Delete skills/examples/')
    optimizer.delete_directory('skills/examples')
    
    # Task 2: Move docs/sessions/ files
    print('\nTask 2: Move docs/sessions/ files')
    sessions_files = [
        ('docs/sessions/DEVTOOLS_STRUCTURE_IMPROVEMENT.md', '.internal/summaries/2026-01/devtools_structure_improvement.md'),
        ('docs/sessions/FINAL_SUMMARY.md', '.internal/summaries/2026-01/final_summary.md'),
        ('docs/sessions/RULES_MANAGEMENT_STRATEGY.md', '.internal/summaries/2026-01/rules_management_strategy.md'),
        ('docs/sessions/SESSION_2026-01-29_MORNING.md', '.internal/summaries/2026-01/session_2026-01-29_morning.md'),
        ('docs/sessions/SESSION_SUMMARY.md', '.internal/summaries/2026-01/session_summary.md'),
        ('docs/sessions/STRUCTURE_IMPROVEMENT.md', '.internal/summaries/2026-01/structure_improvement.md'),
        ('docs/sessions/SUMMARY.md', '.internal/summaries/2026-01/summary.md'),
        ('docs/sessions/VIBE_GUIDE_OPTIMIZATION.md', '.internal/summaries/2026-01/vibe_guide_optimization.md'),
    ]
    optimizer.move_files(sessions_files)
    optimizer.delete_directory('docs/sessions')
    
    # Task 3: Merge GIT files (manual - just delete GITHUB_STRATEGY.md)
    print('\nTask 3: Delete GITHUB_STRATEGY.md (already merged)')
    # Note: Merging should be done manually first
    # optimizer.delete_file('docs/architecture/GITHUB_STRATEGY.md')
    print('⚠️  Manual task: Merge GITHUB_STRATEGY.md + GIT_STRATEGY.md first')
    
    # Task 4: Rename FEATURES.md
    print('\nTask 4: Rename FEATURES.md → ROADMAP.md')
    # optimizer.rename_file('docs/architecture/FEATURES.md', 'docs/architecture/ROADMAP.md')
    print('⚠️  Manual task: Check if FEATURES.md exists first')
    
    # Show summary
    optimizer.show_summary()
    
    if not args.confirm:
        print('💡 This was a DRY RUN. Use --confirm to execute.')
    else:
        print('✅ Operations completed!')

if __name__ == '__main__':
    main()
