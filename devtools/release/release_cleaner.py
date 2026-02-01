"""
Release Cleaner - 發布清潔工
智能過濾專案雜訊，生成乾淨的發布包

Release Cleaner - Intelligently filters project noise and generates clean release packages
"""

import shutil
from pathlib import Path
from typing import List, Set, Dict
import yaml
import fnmatch
import os


class ReleaseCleaner:
    """發布清潔工 / Release Cleaner"""
    
    def __init__(self, project_path: Path, output_path: Path, 
                 filters_config: Path = None):
        self.project_path = project_path
        self.output_path = output_path
        self.filters_config = filters_config or Path(__file__).parent / 'filters.yaml'
        
        # 載入過濾規則
        self.filters = self._load_filters()
        
        # 統計資訊
        self.stats = {
            'total_files': 0,
            'copied_files': 0,
            'filtered_files': 0,
            'total_size': 0,
            'copied_size': 0,
            'large_files_warned': []
        }
    
    def _load_filters(self) -> Dict[str, List[str]]:
        """載入過濾規則 / Load filter rules"""
        if not self.filters_config.exists():
            print(f"⚠️  Filter config not found: {self.filters_config}")
            print("   Using default filters...")
            return self._get_default_filters()
        
        with open(self.filters_config, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        # 合併所有類別的規則
        all_filters = []
        for category, patterns in config.items():
            if isinstance(patterns, list):
                all_filters.extend(patterns)
        
        return {'patterns': all_filters}
    
    def _get_default_filters(self) -> Dict[str, List[str]]:
        """預設過濾規則 / Default filter rules"""
        return {
            'patterns': [
                '.venv/', 'node_modules/', '__pycache__/',
                '*.pyc', '*.log', '.env', '.DS_Store'
            ]
        }
    
    def should_filter(self, file_path: Path) -> tuple[bool, str]:
        """
        判斷檔案是否應該被過濾 / Check if file should be filtered
        
        Returns:
            (should_filter, reason)
        """
        rel_path = file_path.relative_to(self.project_path)
        rel_path_str = str(rel_path).replace('\\', '/')
        
        # 檢查每個過濾模式
        for pattern in self.filters.get('patterns', []):
            pattern = pattern.rstrip('/')
            
            # 目錄匹配
            if pattern.endswith('/'):
                if any(part == pattern[:-1] for part in rel_path.parts):
                    return True, f"Matched directory filter: {pattern}"
            
            # 檔案名匹配（支援萬用字元）
            elif fnmatch.fnmatch(file_path.name, pattern):
                return True, f"Matched file filter: {pattern}"
            
            # 路徑匹配
            elif fnmatch.fnmatch(rel_path_str, pattern):
                return True, f"Matched path filter: {pattern}"
        
        # 檢查專案級別的 .releaseignore
        releaseignore = self.project_path / '.releaseignore'
        if releaseignore.exists():
            with open(releaseignore, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        if fnmatch.fnmatch(rel_path_str, line):
                            return True, f"Matched .releaseignore: {line}"
        
        return False, ""
    
    def check_large_file(self, file_path: Path) -> bool:
        """
        檢查大檔案並詢問使用者 / Check large files and ask user
        
        Returns:
            True if file should be included
        """
        size_mb = file_path.stat().st_size / (1024 * 1024)
        
        if size_mb > 100:  # 超過 100MB
            print(f"\n⚠️  Large file detected / 發現大檔案:")
            print(f"   File: {file_path.relative_to(self.project_path)}")
            print(f"   Size: {size_mb:.1f} MB")
            print(f"\n   This file is very large. Options:")
            print(f"   此檔案非常大。選項：")
            print(f"   1. Include (keep in release) / 包含（保留在發布包中）")
            print(f"   2. Exclude (filter out) / 排除（過濾掉）")
            print(f"   3. Suggest download script / 建議改為下載腳本")
            
            while True:
                choice = input("   Choice [1/2/3]: ").strip()
                if choice == '1':
                    self.stats['large_files_warned'].append(str(file_path.relative_to(self.project_path)))
                    return True
                elif choice == '2':
                    return False
                elif choice == '3':
                    self._suggest_download_script(file_path)
                    return False
                else:
                    print("   Invalid choice. Please enter 1, 2, or 3.")
        
        return True
    
    def _suggest_download_script(self, file_path: Path):
        """建議下載腳本 / Suggest download script"""
        script_name = "download_assets.py"
        script_path = self.output_path / script_name
        
        file_name = file_path.name
        file_url = f"https://example.com/assets/{file_name}"  # 使用者需要替換
        
        script_content = f'''#!/usr/bin/env python3
"""
Asset Downloader - 自動下載大型資源檔案
Auto-download large asset files
"""

import requests
from pathlib import Path

def download_file(url: str, dest: Path):
    """Download file with progress / 下載檔案並顯示進度"""
    print(f"Downloading {{dest.name}}...")
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    total_size = int(response.headers.get('content-length', 0))
    downloaded = 0
    
    with open(dest, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
            downloaded += len(chunk)
            if total_size:
                percent = (downloaded / total_size) * 100
                print(f"\\rProgress: {{percent:.1f}}%", end='')
    
    print(f"\\n✅ Downloaded: {{dest}}")

if __name__ == '__main__':
    # TODO: Replace with actual download URL
    # 請替換為實際的下載網址
    assets = [
        ("{file_url}", "{file_name}"),
    ]
    
    for url, filename in assets:
        dest = Path(filename)
        if not dest.exists():
            download_file(url, dest)
        else:
            print(f"✓ Already exists: {{filename}}")
'''
        
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(script_content)
        
        print(f"\n   ✅ Created download script: {script_name}")
        print(f"   ✅ 已創建下載腳本: {script_name}")
        print(f"   📝 Remember to:")
        print(f"   📝 記得：")
        print(f"      1. Upload {file_name} to a hosting service")
        print(f"         將 {file_name} 上傳到檔案託管服務")
        print(f"      2. Update the URL in {script_name}")
        print(f"         更新 {script_name} 中的網址")
        print(f"      3. Add to README: 'Run python {script_name} before use'")
        print(f"         在 README 中註明：'使用前請執行 python {script_name}'")
    
    def clean(self, interactive: bool = True) -> Path:
        """
        執行清潔並複製檔案 / Execute cleaning and copy files
        
        Args:
            interactive: 是否在遇到大檔案時詢問使用者
        
        Returns:
            Path to cleaned output directory
        """
        print(f"🧹 Release Cleaner / 發布清潔工")
        print(f"   Source: {self.project_path}")
        print(f"   Output: {self.output_path}\n")
        
        # 創建輸出目錄
        self.output_path.mkdir(parents=True, exist_ok=True)
        
        # 遍歷所有檔案
        for item in self.project_path.rglob('*'):
            if item.is_file():
                self.stats['total_files'] += 1
                self.stats['total_size'] += item.stat().st_size
                
                # 檢查是否應該過濾
                should_filter, reason = self.should_filter(item)
                
                if should_filter:
                    self.stats['filtered_files'] += 1
                    print(f"   ⊗ Filtered: {item.relative_to(self.project_path)} ({reason})")
                    continue
                
                # 檢查大檔案
                if interactive and not self.check_large_file(item):
                    self.stats['filtered_files'] += 1
                    continue
                
                # 複製檔案
                rel_path = item.relative_to(self.project_path)
                dest = self.output_path / rel_path
                dest.parent.mkdir(parents=True, exist_ok=True)
                
                shutil.copy2(item, dest)
                self.stats['copied_files'] += 1
                self.stats['copied_size'] += item.stat().st_size
                
                print(f"   ✓ Copied: {rel_path}")
        
        # 生成報告
        self._generate_summary()
        
        return self.output_path
    
    def _generate_summary(self):
        """生成清潔摘要 / Generate cleaning summary"""
        print("\n" + "=" * 80)
        print("📊 CLEANING SUMMARY / 清潔摘要")
        print("=" * 80)
        print(f"Total files scanned: {self.stats['total_files']}")
        print(f"總計掃描檔案: {self.stats['total_files']}")
        print(f"\nCopied: {self.stats['copied_files']} files ({self._format_size(self.stats['copied_size'])})")
        print(f"已複製: {self.stats['copied_files']} 個檔案 ({self._format_size(self.stats['copied_size'])})")
        print(f"\nFiltered: {self.stats['filtered_files']} files")
        print(f"已過濾: {self.stats['filtered_files']} 個檔案")
        
        reduction = (1 - self.stats['copied_size'] / max(self.stats['total_size'], 1)) * 100
        print(f"\nSize reduction: {reduction:.1f}%")
        print(f"體積縮減: {reduction:.1f}%")
        
        if self.stats['large_files_warned']:
            print(f"\n⚠️  Large files included:")
            print(f"⚠️  包含的大檔案:")
            for f in self.stats['large_files_warned']:
                print(f"   - {f}")
        
        print("=" * 80)
    
    def _format_size(self, size_bytes: int) -> str:
        """格式化檔案大小 / Format file size"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.1f} TB"


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python release_cleaner.py <project_path> <output_path>")
        print("用法: python release_cleaner.py <專案路徑> <輸出路徑>")
        sys.exit(1)
    
    project_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    
    if not project_path.exists():
        print(f"❌ Project not found: {project_path}")
        sys.exit(1)
    
    cleaner = ReleaseCleaner(project_path, output_path)
    cleaner.clean(interactive=True)
    
    print(f"\n✅ Release package ready at: {output_path}")
    print(f"✅ 發布包已準備完成: {output_path}")
