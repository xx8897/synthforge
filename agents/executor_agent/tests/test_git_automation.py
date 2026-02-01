"""
Tests for Git Automation Tools
"""

import pytest
from pathlib import Path
from agents.executor_agent.git_automation import (
    GitAutomation,
    auto_commit_and_push,
    create_feature_pr
)


class TestGitAutomation:
    """Test Git automation functionality."""
    
    def test_init(self):
        """Test GitAutomation initialization."""
        git = GitAutomation()
        assert git.repo_path.exists()
    
    def test_auto_commit_no_files(self):
        """Test auto_commit with no files specified."""
        git = GitAutomation()
        result = git.auto_commit(message="Test commit")
        
        assert 'success' in result
        assert 'errors' in result
        assert isinstance(result['errors'], list)
    
    def test_push_branch_structure(self):
        """Test push_branch return structure."""
        git = GitAutomation()
        result = git.push_branch()
        
        assert 'success' in result
        assert 'branch' in result
        assert 'errors' in result
    
    def test_create_pr_structure(self):
        """Test create_pr return structure."""
        git = GitAutomation()
        result = git.create_pr(title="Test PR")
        
        assert 'success' in result
        assert 'pr_url' in result
        assert 'pr_number' in result
        assert 'errors' in result


class TestConvenienceFunctions:
    """Test convenience functions."""
    
    def test_auto_commit_and_push_structure(self):
        """Test auto_commit_and_push return structure."""
        result = auto_commit_and_push(message="Test")
        
        assert 'success' in result
        assert 'commit_hash' in result
        assert 'push_success' in result
        assert 'errors' in result
    
    def test_create_feature_pr_structure(self):
        """Test create_feature_pr return structure."""
        result = create_feature_pr(feature_name="test-feature")
        
        assert 'success' in result
        assert 'pr_url' in result
        assert 'errors' in result


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
