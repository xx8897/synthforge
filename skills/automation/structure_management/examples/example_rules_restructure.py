"""
創建 rules/ 目錄結構並移動規則檔案
"""
from pathlib import Path
import shutil

# 定義基礎路徑
base = Path('.')
rules_base = base / 'rules'

# 定義目錄結構
directories = [
    'rules/core',
    'rules/development',
]

# 創建目錄
print('創建 rules/ 目錄結構...\n')
for dir_path in directories:
    Path(dir_path).mkdir(parents=True, exist_ok=True)
    print(f'✅ 已創建: {dir_path}/')

# 定義移動規則
moves = [
    # Core rules
    ('DIRECTORY_README_RULE.md', 'rules/core/DIRECTORY_README_RULE.md'),
    ('VIBE_GUIDE_SYNC_RULE.md', 'rules/core/VIBE_GUIDE_SYNC_RULE.md'),
    ('BILINGUAL_OUTPUT_RULE.md', 'rules/core/BILINGUAL_OUTPUT_RULE.md'),
    ('DRY_RULE.md', 'rules/core/DRY_RULE.md'),
    
    # Development rules
    ('FILE_NAMING_CONVENTION_RULE.md', 'rules/development/FILE_NAMING_CONVENTION_RULE.md'),
    ('INTERNAL_RULE.md', 'rules/development/INTERNAL_RULE.md'),
]

# 移動檔案
print('\n移動規則檔案...\n')
for source, dest in moves:
    source_path = base / source
    dest_path = base / dest
    
    if source_path.exists():
        shutil.move(str(source_path), str(dest_path))
        print(f'✅ {source} → {dest}')
    else:
        print(f'⚠️  找不到: {source}')

print('\n🎉 rules/ 目錄創建完成！')
