"""
.internal 目錄結構創建腳本
"""
import os
from pathlib import Path

# 定義基礎路徑
base_path = Path('.internal')

# 定義要創建的目錄結構
directories = [
    'summaries/2026-01',
    'confirmations/pending',
    'confirmations/archived',
    'analysis',
    'planning',
    'knowledge/best_practices',
    'knowledge/patterns',
    'knowledge/troubleshooting',
    'knowledge/references',
    'knowledge/tools',
    'knowledge/lessons_learned',
    'temp'
]

# 創建目錄
for dir_path in directories:
    full_path = base_path / dir_path
    full_path.mkdir(parents=True, exist_ok=True)
    print(f'✅ 已創建: {full_path}')

print('\n🎉 .internal 目錄結構創建完成！')

# 列出結構
print('\n📁 目錄結構:')
for root, dirs, files in os.walk(base_path):
    level = root.replace(str(base_path), '').count(os.sep)
    indent = ' ' * 2 * level
    print(f'{indent}{os.path.basename(root)}/')
    sub_indent = ' ' * 2 * (level + 1)
    for file in files:
        if file != 'create_structure.py':  # 不顯示這個腳本本身
            print(f'{sub_indent}{file}')
