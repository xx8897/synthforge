"""
.internal 檔案移動腳本
"""
import shutil
from pathlib import Path

base = Path('.internal')

# 定義移動規則
moves = [
    # 任務總結 → summaries/2026-01/
    ('任務總結_2026-01-29_1310.md', 'summaries/2026-01/任務總結_2026-01-29_1310.md'),
    ('任務總結_2026-01-29_1413.md', 'summaries/2026-01/任務總結_2026-01-29_1413.md'),
    ('任務總結_2026-01-29_1415.md', 'summaries/2026-01/任務總結_2026-01-29_1415.md'),
    ('任務總結_2026-01-29_1429.md', 'summaries/2026-01/任務總結_2026-01-29_1429.md'),
    
    # 確認文件 → confirmations/pending/
    ('rules_strategy_confirmation.md', 'confirmations/pending/rules_strategy_confirmation.md'),
    ('internal_restructure_confirmation.md', 'confirmations/pending/internal_restructure_confirmation.md'),
    
    # 分析文件 → analysis/
    ('internal_structure_planning.md', 'analysis/internal_structure_planning.md'),
    ('rules_naming_expert_analysis.md', 'analysis/rules_naming_expert_analysis.md'),
    ('ai_tools_readme_behavior.md', 'analysis/ai_tools_readme_behavior.md'),
    ('token_limits_industry_standards.md', 'analysis/token_limits_industry_standards.md'),
    ('bilingual_strategy_analysis.md', 'analysis/bilingual_strategy_analysis.md'),
    
    # 規劃 → planning/
    ('待辦.md', 'planning/待辦.md'),
    
    # 臨時 → temp/
    ('快速狀態.md', 'temp/快速狀態.md'),
    ('快速總結_2026-01-29.md', 'temp/快速總結_2026-01-29.md'),
]

# 執行移動
print('開始移動檔案...\n')
for source, dest in moves:
    source_path = base / source
    dest_path = base / dest
    
    if source_path.exists():
        shutil.move(str(source_path), str(dest_path))
        print(f'✅ {source} → {dest}')
    else:
        print(f'⚠️  找不到: {source}')

# 歸檔會話總結
會話總結 = base / '會話總結.md'
if 會話總結.exists():
    docs_sessions = Path('docs/sessions')
    docs_sessions.mkdir(parents=True, exist_ok=True)
    shutil.move(str(會話總結), 'docs/sessions/SESSION_2026-01-29_MORNING.md')
    print(f'\n✅ 會話總結.md → docs/sessions/SESSION_2026-01-29_MORNING.md')

print('\n🎉 檔案移動完成！')
