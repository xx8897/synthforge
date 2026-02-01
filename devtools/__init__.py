"""
Devtools - synthforge Development Toolkit
開發工具集 - synthforge 開發工具包

A comprehensive suite of development tools organized by function.
按功能組織的綜合開發工具套件。

Tools organized by category:
- security/: Security scanning and auditing
- analyzers/: Dependency and license analysis
- release/: Release preparation and cleaning
- project/: Project scaffolding and setup

Usage:
    python -m devtools.cli [COMMAND] [OPTIONS]
    
    Or import as a module:
    from devtools.security import security_auditor
    from devtools.analyzers import dep_analyzer
"""

__version__ = '1.0.0'
__author__ = 'synthforge Team'

# Import main modules for direct usage
from .security import security_auditor
from .analyzers import dep_analyzer, license_checker
from .release import release_cleaner
from .project import scaffolder

__all__ = [
    'security_auditor',
    'dep_analyzer',
    'license_checker',
    'release_cleaner',
    'scaffolder',
]
