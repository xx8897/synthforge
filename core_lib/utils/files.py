"""
File and Directory Utilities
檔案和目錄工具函數

Extracted from skills/examples/structure_management/
從 skills/examples/structure_management/ 提取
"""
from pathlib import Path
import shutil
import os
from typing import List, Tuple

def ensure_dir_exists(path: Path) -> None:
    """
    Ensure directory exists, create if not
    確保目錄存在，不存在則創建
    
    Args:
        path: Directory path to ensure exists
    """
    path.mkdir(parents=True, exist_ok=True)

def batch_create_dirs(directories: List[str], base: Path) -> None:
    """
    Batch create directories
    批量創建目錄
    
    Args:
        directories: List of directory paths (relative to base)
        base: Base path
        
    Example:
        batch_create_dirs(['dir1', 'dir2/subdir'], Path('.'))
    """
    print('Creating directories...\n')
    for dir_path in directories:
        full_path = base / dir_path
        ensure_dir_exists(full_path)
        print(f'✅ Created: {full_path}')
    print('\n🎉 Directory creation complete!')

def batch_move_files(moves: List[Tuple[str, str]], base: Path) -> None:
    """
    Batch move files
    批量移動檔案
    
    Args:
        moves: List of (source, dest) tuples (relative to base)
        base: Base path
        
    Example:
        moves = [('old.txt', 'new/old.txt')]
        batch_move_files(moves, Path('.'))
    """
    print('Moving files...\n')
    for source, dest in moves:
        source_path = base / source
        dest_path = base / dest
        
        if source_path.exists():
            # Ensure destination directory exists
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source_path), str(dest_path))
            print(f'✅ {source} → {dest}')
        else:
            print(f'⚠️  Not found: {source}')
    print('\n🎉 File moving complete!')

def list_directory_tree(path: Path, max_depth: int = 3) -> str:
    """
    List directory tree structure
    列出目錄樹結構
    
    Args:
        path: Directory path
        max_depth: Maximum depth to display
        
    Returns:
        Tree structure as string
        
    Example:
        tree = list_directory_tree(Path('.'))
        print(tree)
    """
    lines = []
    lines.append(f'\n📁 Directory structure:\n')
    
    for root, dirs, files in os.walk(path):
        level = root.replace(str(path), '').count(os.sep)
        if level > max_depth:
            continue
        indent = ' ' * 2 * level
        lines.append(f'{indent}{os.path.basename(root)}/')
        sub_indent = ' ' * 2 * (level + 1)
        for file in files:
            lines.append(f'{sub_indent}{file}')
    
    return '\n'.join(lines)
