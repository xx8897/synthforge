"""
Tests for SmartGitHandler
=========================
"""

import pytest
from core_lib.git.smart_handler import SmartGitHandler
from core_lib.git.automation import GitAutomation
import subprocess
import os
import shutil

@pytest.fixture
def temp_repo(tmp_path):
    repo_dir = tmp_path / "test_repo"
    repo_dir.mkdir()
    subprocess.run(['git', 'init'], cwd=repo_dir, check=True)
    subprocess.run(['git', 'config', 'user.email', 'test@example.com'], cwd=repo_dir, check=True)
    subprocess.run(['git', 'config', 'user.name', 'test'], cwd=repo_dir, check=True)
    return repo_dir

def test_analyze_changes_docs(temp_repo):
    handler = SmartGitHandler(str(temp_repo))
    doc_file = temp_repo / "README.md"
    doc_file.write_text("test docs")
    subprocess.run(['git', 'add', 'README.md'], cwd=temp_repo, check=True)
    
    analysis = handler.analyze_changes()
    assert analysis['suggestion'] == 'docs'

def test_analyze_changes_feat(temp_repo):
    handler = SmartGitHandler(str(temp_repo))
    core_dir = temp_repo / "core_lib"
    core_dir.mkdir()
    code_file = core_dir / "app.py"
    code_file.write_text("def app(): pass")
    subprocess.run(['git', 'add', 'core_lib/app.py'], cwd=temp_repo, check=True)
    
    analysis = handler.analyze_changes()
    assert analysis['suggestion'] == 'feat'

def test_suggest_next_tag_patch(temp_repo):
    handler = SmartGitHandler(str(temp_repo))
    # Create initial tag
    (temp_repo / "initial.txt").write_text("init")
    subprocess.run(['git', 'add', '.'], cwd=temp_repo, check=True)
    subprocess.run(['git', 'commit', '-m', 'chore: initial'], cwd=temp_repo, check=True)
    subprocess.run(['git', 'tag', 'v1.0.0'], cwd=temp_repo, check=True)
    
    # Create fix commit
    (temp_repo / "fix.txt").write_text("fix")
    subprocess.run(['git', 'add', '.'], cwd=temp_repo, check=True)
    subprocess.run(['git', 'commit', '-m', 'fix: bug fix'], cwd=temp_repo, check=True)
    
    next_tag = handler.suggest_next_tag()
    assert next_tag == 'v1.0.1'

def test_suggest_next_tag_minor(temp_repo):
    handler = SmartGitHandler(str(temp_repo))
    # Create initial tag
    (temp_repo / "initial.txt").write_text("init")
    subprocess.run(['git', 'add', '.'], cwd=temp_repo, check=True)
    subprocess.run(['git', 'commit', '-m', 'chore: initial'], cwd=temp_repo, check=True)
    subprocess.run(['git', 'tag', 'v1.0.0'], cwd=temp_repo, check=True)
    
    # Create feat commit
    (temp_repo / "feat.txt").write_text("feat")
    subprocess.run(['git', 'add', '.'], cwd=temp_repo, check=True)
    subprocess.run(['git', 'commit', '-m', 'feat: new feature'], cwd=temp_repo, check=True)
    
    next_tag = handler.suggest_next_tag()
    assert next_tag == 'v1.1.0'

def test_suggest_next_tag_major(temp_repo):
    handler = SmartGitHandler(str(temp_repo))
    # Create initial tag
    (temp_repo / "initial.txt").write_text("init")
    subprocess.run(['git', 'add', '.'], cwd=temp_repo, check=True)
    subprocess.run(['git', 'commit', '-m', 'chore: initial'], cwd=temp_repo, check=True)
    subprocess.run(['git', 'tag', 'v1.0.0'], cwd=temp_repo, check=True)
    
    # Create major commit
    (temp_repo / "break.txt").write_text("break")
    subprocess.run(['git', 'add', '.'], cwd=temp_repo, check=True)
    subprocess.run(['git', 'commit', '-m', 'feat: break BC: change'], cwd=temp_repo, check=True)
    
    next_tag = handler.suggest_next_tag()
    assert next_tag == 'v2.0.0'
