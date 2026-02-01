"""
devtools 重組腳本
"""
from pathlib import Path
import shutil

base = Path('devtools')

# 創建新目錄
directories = [
    'security',
    'release',
    'project'
]

print('創建 devtools/ 子目錄...\n')
for dir_name in directories:
    (base / dir_name).mkdir(exist_ok=True)
    # 創建 __init__.py
    (base / dir_name / '__init__.py').write_text(f'"""{ dir_name.capitalize()} tools for synthforge"""\n')
    print(f'✅ 已創建: devtools/{dir_name}/')

# 移動檔案
moves = [
    # 安全工具 → security/
    ('security_auditor.py', 'security/security_auditor.py'),
    ('advanced_security.py', 'security/advanced_security.py'),
    ('filters.yaml', 'security/filters.yaml'),
    ('SECURITY_STRATEGY.md', 'security/SECURITY_STRATEGY.md'),
    
    # 分析工具 → analyzers/ (已存在)
    ('dep_analyzer.py', 'analyzers/dep_analyzer.py'),
    ('license_checker.py', 'analyzers/license_checker.py'),
    
    # 發布工具 → release/
    ('release_cleaner.py', 'release/release_cleaner.py'),
    
    # 專案工具 → project/
    ('scaffolder.py', 'project/scaffolder.py'),
]

print('\n移動檔案...\n')
for source, dest in moves:
    source_path = base / source
    dest_path = base / dest
    
    if source_path.exists():
        # 確保目標目錄存在
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(source_path), str(dest_path))
        print(f'✅ {source} → {dest}')
    else:
        print(f'⚠️  找不到: {source}')

# 創建 analyzers/__init__.py (如果不存在)
analyzers_init = base / 'analyzers' / '__init__.py'
if not analyzers_init.exists():
    analyzers_init.write_text('"""Analysis tools for synthforge"""\n')
    print(f'\n✅ 已創建: devtools/analyzers/__init__.py')

print('\n🎉 devtools/ 重組完成！')
