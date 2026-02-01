"""
Devtools CLI - 統一命令列介面
Unified command-line interface for all development tools

Usage:
    python devtools/cli.py [COMMAND] [OPTIONS]

Commands:
    new         Create new project from template
    check       Run security and quality checks
    release     Prepare project for release
    analyze     Analyze dependencies and licenses
    workflow    Workflow automation commands
    git         Git automation commands
    interactive Interactive mode
    help        Show detailed help
"""

import sys
import os
from pathlib import Path

# Fix encoding for Windows console
if sys.platform == 'win32':
    # Set UTF-8 encoding for stdout/stderr
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    if sys.stderr.encoding != 'utf-8':
        sys.stderr.reconfigure(encoding='utf-8')
    # Set environment variable for Python I/O
    os.environ['PYTHONIOENCODING'] = 'utf-8'

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import click


@click.group()
@click.version_option(version='1.0.0', prog_name='Devtools')
def cli():
    """
    🛠️  Devtools - AI Workspace Development Tools
    
    統一的開發工具集，提供專案腳手架、安全檢查、發布管理等功能
    """
    pass


@cli.command()
@click.option('--name', required=True, help='Project name / 專案名稱')
@click.option('--type', 'project_type',
              type=click.Choice(['python-cli', 'python-fastapi', 'node-express', 'static-web']),
              default='python-cli',
              help='Project type / 專案類型')
@click.option('--path', default=None, help='Custom output path / 自訂輸出路徑')
def new(name, project_type, path):
    """
    Create a new project from template
    從模板創建新專案
    """
    from .project.scaffolder import new_project as scaffolder_new
    
    # 調用 scaffolder
    ctx = click.Context(scaffolder_new)
    ctx.invoke(scaffolder_new, name=name, project_type=project_type, path=path)


@cli.command()
@click.argument('project_path', type=click.Path(exists=True))
@click.option('--security', is_flag=True, help='Run security audit / 執行安全檢查')
@click.option('--licenses', is_flag=True, help='Check licenses / 檢查授權')
@click.option('--deps', is_flag=True, help='Analyze dependencies / 分析依賴')
@click.option('--all', 'check_all', is_flag=True, help='Run all checks / 執行所有檢查')
def check(project_path, security, licenses, deps, check_all):
    """
    Run various checks on the project
    對專案執行各種檢查
    """
    path = Path(project_path)
    
    if check_all:
        security = licenses = deps = True
    
    if not (security or licenses or deps):
        click.echo("❌ Please specify at least one check type")
        click.echo("❌ 請至少指定一種檢查類型")
        click.echo("\nOptions: --security, --licenses, --deps, --all")
        return
    
    # Security Audit
    if security:
        click.echo("\n" + "=" * 80)
        click.echo("🛡️  Running Security Audit...")
        click.echo("=" * 80)
        
        from .security.security_auditor import SecurityAuditor
        auditor = SecurityAuditor(path)
        auditor.scan()
        click.echo(auditor.generate_report())
    
    # License Check
    if licenses:
        click.echo("\n" + "=" * 80)
        click.echo("📜 Checking Licenses...")
        click.echo("=" * 80)
        
        from .analyzers.license_checker import LicenseChecker
        checker = LicenseChecker(path)
        click.echo(checker.generate_report())
    
    # Dependency Analysis
    if deps:
        click.echo("\n" + "=" * 80)
        click.echo("📦 Analyzing Dependencies...")
        click.echo("=" * 80)
        
        from .analyzers.dep_analyzer import DependencyAnalyzer
        analyzer = DependencyAnalyzer(path)
        click.echo(analyzer.generate_report())


@cli.command()
@click.argument('project_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
@click.option('--clean', is_flag=True, help='Clean project files / 清理專案檔案')
@click.option('--audit', is_flag=True, help='Run security audit first / 先執行安全檢查')
@click.option('--interactive/--no-interactive', default=True, 
              help='Interactive mode for large files / 大檔案互動模式')
def release(project_path, output_path, clean, audit, interactive):
    """
    Prepare project for release
    準備專案發布
    """
    project = Path(project_path)
    output = Path(output_path)
    
    # Security audit first
    if audit:
        click.echo("🛡️  Running pre-release security audit...")
        click.echo("🛡️  執行發布前安全檢查...\n")
        
        from .security.security_auditor import SecurityAuditor
        auditor = SecurityAuditor(project)
        issues = auditor.scan()
        
        if issues:
            click.echo(auditor.generate_report())
            
            # Check for critical issues
            has_critical = any(i.severity == auditor.SecurityIssue.SEVERITY_CRITICAL 
                             for i in issues)
            
            if has_critical:
                click.echo("\n❌ Critical security issues found!")
                click.echo("❌ 發現嚴重安全問題！")
                
                if not click.confirm("Continue anyway? / 仍要繼續？"):
                    return
    
    # Clean release
    if clean:
        click.echo("\n🧹 Cleaning project for release...")
        click.echo("🧹 清理專案準備發布...\n")
        
        from .release.release_cleaner import ReleaseCleaner
        cleaner = ReleaseCleaner(project, output)
        cleaner.clean(interactive=interactive)
    else:
        # Simple copy
        import shutil
        shutil.copytree(project, output, dirs_exist_ok=True)
        click.echo(f"✅ Copied to: {output}")


@cli.command()
@click.argument('project_path', type=click.Path(exists=True))
@click.option('--generate-req', is_flag=True, help='Generate requirements.txt / 生成 requirements.txt')
@click.option('--generate-licenses', is_flag=True, help='Generate LICENSES.txt / 生成 LICENSES.txt')
def analyze(project_path, generate_req, generate_licenses):
    """
    Analyze project dependencies and licenses
    分析專案依賴與授權
    """
    path = Path(project_path)
    
    # Dependency analysis
    click.echo("📦 Analyzing dependencies...")
    from .analyzers.dep_analyzer import DependencyAnalyzer
    dep_analyzer = DependencyAnalyzer(path)
    click.echo(dep_analyzer.generate_report())
    
    if generate_req:
        dep_analyzer.generate_requirements()
    
    # License analysis
    click.echo("\n📜 Analyzing licenses...")
    from .analyzers.license_checker import LicenseChecker
    lic_checker = LicenseChecker(path)
    click.echo(lic_checker.generate_report())
    
    if generate_licenses:
        lic_checker.generate_licenses_file()


@cli.group()
def workflow():
    """
    Workflow automation commands
    工作流自動化命令
    """
    pass


@workflow.command('run')
@click.argument('workflow_file', type=click.Path(exists=True))
@click.option('--dry-run', is_flag=True, help='Simulate execution without running / 模擬執行')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output / 詳細輸出')
def workflow_run(workflow_file, dry_run, verbose):
    """
    Run a workflow
    執行工作流
    """
    import asyncio
    from workflows.engine.executor import execute_workflow_file
    
    click.echo(f"\n🚀 Running workflow: {workflow_file}")
    if dry_run:
        click.echo("   (Dry run mode - no actual execution)")
    click.echo("")
    
    try:
        context = asyncio.run(execute_workflow_file(workflow_file, dry_run=dry_run))
        
        # Show summary
        summary = context.get_summary()
        click.echo("\n" + "="*80)
        click.echo("WORKFLOW EXECUTION SUMMARY")
        click.echo("="*80)
        click.echo(f"Status:          {summary['status']}")
        click.echo(f"Duration:        {summary['duration']:.2f}s")
        click.echo(f"Phases:          {summary['phases']}")
        click.echo(f"Total Steps:     {summary['total_steps']}")
        click.echo(f"Successful:      {summary['successful_steps']}")
        click.echo(f"Failed:          {summary['failed_steps']}")
        
        if summary['status'] == 'success':
            click.echo("\n✅ Workflow completed successfully")
        else:
            click.echo("\n❌ Workflow failed")
            raise click.Abort()
            
    except Exception as e:
        click.echo(f"\n❌ Error: {e}")
        raise click.Abort()


@workflow.command('validate')
@click.argument('workflow_file', type=click.Path(exists=True))
@click.option('--verbose', '-v', is_flag=True, help='Verbose output / 詳細輸出')
def workflow_validate(workflow_file, verbose):
    """
    Validate a workflow
    驗證工作流
    """
    from workflows.engine.validators import validate_workflow_file
    
    click.echo(f"\n🔍 Validating workflow: {workflow_file}\n")
    
    errors = validate_workflow_file(workflow_file)
    
    if not errors:
        click.echo("✅ Workflow is valid")
    else:
        click.echo(f"Found {len(errors)} validation issue(s):\n")
        for error in errors:
            click.echo(f"  {error}")
        
        # Count by severity
        error_count = sum(1 for e in errors if e.severity == 'error')
        warning_count = sum(1 for e in errors if e.severity == 'warning')
        
        click.echo(f"\nSummary: {error_count} errors, {warning_count} warnings")
        
        if error_count > 0:
            click.echo("\n❌ Workflow validation failed")
            raise click.Abort()
        else:
            click.echo("\n⚠️  Workflow has warnings but is valid")


@workflow.command('list')
@click.option('--directory', '-d', default='workflows/templates', 
              help='Directory to search / 搜尋目錄')
def workflow_list(directory):
    """
    List available workflows
    列出可用的工作流
    """
    from workflows.engine.parser import list_workflows
    
    click.echo(f"\n📋 Available workflows in {directory}:\n")
    
    workflows = list_workflows(directory)
    
    if not workflows:
        click.echo("No workflows found")
        return
    
    for wf in workflows:
        click.echo(f"  • {wf['name']}")
        if wf.get('description'):
            click.echo(f"    {wf['description']}")
        if wf.get('version'):
            click.echo(f"    Version: {wf['version']}")
        if wf.get('tags'):
            click.echo(f"    Tags: {', '.join(wf['tags'])}")
        click.echo(f"    File: {wf['filepath']}")
        click.echo("")
    
    click.echo(f"Total: {len(workflows)} workflow(s)")


@cli.command()
def info():
    """
    Show devtools information
    顯示開發工具資訊
    """
    click.echo("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                      🛠️  DEVTOOLS - Development Toolkit                     ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

Available Tools / 可用工具:

  🏗️  Project Scaffolder      - Create new projects from templates
                               從模板創建新專案

  🛡️  Security Auditor        - Scan for security vulnerabilities
                               掃描安全漏洞

  🧹 Release Cleaner         - Clean project for distribution
                               清理專案準備發布

  📦 Dependency Analyzer     - Analyze and optimize dependencies
                               分析與優化依賴

  📜 License Checker         - Check dependency licenses
                               檢查依賴授權

Usage Examples / 使用範例:

  # Create new project / 創建新專案
  python devtools/cli.py new --name=my_app --type=python-fastapi

  # Run all checks / 執行所有檢查
  python devtools/cli.py check projects/my_app --all

  # Prepare release / 準備發布
  python devtools/cli.py release projects/my_app dist/my_app --clean --audit

  # Analyze project / 分析專案
  python devtools/cli.py analyze projects/my_app --generate-req

For detailed help on any command:
  python devtools/cli.py [COMMAND] --help

Version: 1.0.0
""")


# Git Automation Commands
@cli.group()
def git():
    """
    Git automation commands
    Git 自動化命令
    """
    pass


@git.command('commit')
@click.option('--message', '-m', help='Commit message (optional if using smart)')
@click.option('--all', '-a', is_flag=True, help='Add all changed files')
@click.option('--files', '-f', multiple=True, help='Specific files to commit')
@click.option('--smart', '-s', is_flag=True, help='Analyze changes and suggest commit type')
def git_commit(message, all, files, smart):
    """
    Auto-commit changes
    自動提交變更
    """
    from core_lib.git.automation import GitAutomation
    from core_lib.git.smart_handler import SmartGitHandler
    
    git_auto = GitAutomation()
    smart_handler = SmartGitHandler()
    
    if smart:
        analysis = smart_handler.analyze_changes()
        click.echo(click.style(f"🤖 Smart Analysis: {analysis['reason']}", fg='cyan'))
        if not message:
            message = analysis['message']
            click.echo(f"Suggested message: {click.style(message, fg='yellow')}")
    
    if not message:
        click.echo(click.style("❌ Commit message required (use -m or -s)", fg='red'))
        return

    result = git_auto.auto_commit(
        files=list(files) if files else None,
        message=message,
        add_all=all
    )
    
    if result['success']:
        click.echo(click.style(f"✅ Committed: {result['commit_hash'][:8]}", fg='green'))
        click.echo(f"Files: {', '.join(result['files_committed'])}")
    else:
        click.echo(click.style(f"❌ Commit failed", fg='red'))
        for error in result['errors']:
            click.echo(f"  {error}")


@git.command('push')
@click.option('--branch', '-b', help='Branch to push')
@click.option('--force', '-f', is_flag=True, help='Force push')
def git_push(branch, force):
    """
    Push branch to remote
    推送分支到遠端
    """
    from core_lib.git.automation import GitAutomation
    
    git_auto = GitAutomation()
    result = git_auto.push_branch(branch=branch or "", force=force)
    
    if result['success']:
        click.echo(click.style(f"✅ Pushed branch: {result['branch']}", fg='green'))
    else:
        click.echo(click.style(f"❌ Push failed", fg='red'))
        for error in result['errors']:
            click.echo(f"  {error}")


@git.command('tag')
@click.option('--name', '-n', help='Tag name (e.g., v1.0.0)')
@click.option('--message', '-m', help='Tag message')
@click.option('--auto', '-a', is_flag=True, help='Automatically determine next version')
def git_tag(name, message, auto):
    """
    Manage Git tags
    管理 Git 標籤
    """
    from core_lib.git.smart_handler import SmartGitHandler
    
    handler = SmartGitHandler()
    
    if auto:
        next_tag = handler.suggest_next_tag()
        click.echo(click.style(f"🤖 Suggested next tag: {next_tag}", fg='cyan'))
        result = handler.apply_smart_tag(message=message)
        if result['success']:
            click.echo(click.style(f"✅ Applied tag: {result['tag']}", fg='green'))
        else:
            click.echo(click.style(f"❌ Tagging failed: {result['error']}", fg='red'))
    elif name:
        import subprocess
        try:
            cmd = ['git', 'tag', '-a', name, '-m', message or f"Release {name}"]
            subprocess.run(cmd, check=True)
            click.echo(click.style(f"✅ Applied tag: {name}", fg='green'))
        except Exception as e:
            click.echo(click.style(f"❌ Tagging failed: {str(e)}", fg='red'))
    else:
        click.echo(click.style("❌ Tag name required or use --auto", fg='red'))
@git.command('pr')
@click.option('--title', '-t', required=True, help='PR title')
@click.option('--body', '-b', help='PR description')
@click.option('--base', default='main', help='Base branch')
@click.option('--draft', is_flag=True, help='Create as draft')
def git_pr(title, body, base, draft):
    """
    Create pull request
    創建 Pull Request
    """
    from core_lib.git.automation import GitAutomation
    
    git_auto = GitAutomation()
    result = git_auto.create_pr(
        title=title,
        body=body or "",
        base_branch=base,
        draft=draft
    )
    
    if result['success']:
        click.echo(click.style(f"✅ PR created: #{result['pr_number']}", fg='green'))
        click.echo(f"URL: {result['pr_url']}")
    else:
        click.echo(click.style(f"❌ PR creation failed", fg='red'))
        for error in result['errors']:
            click.echo(f"  {error}")


# Knowledge Graph Commands
@cli.group()
def graph():
    """
    Knowledge graph visualization
    知識圖譜視覺化
    """
    pass


@graph.command('build')
def graph_build():
    """
    Build/Update knowledge map
    構建/更新知識地圖
    """
    from devtools.knowledge_graph import generate_knowledge_map
    
    success = generate_knowledge_map()
    if success:
        click.echo(click.style("✅ Knowledge map updated: .internal/knowledge/knowledge_map.md", fg='green'))
    else:
        click.echo(click.style("❌ Failed to update knowledge map", fg='red'))


@graph.command('show')
def graph_show():
    """
    Show knowledge statistics
    顯示知識統計信息
    """
    from devtools.knowledge_graph import analyze_knowledge_relationships
    
    results = analyze_knowledge_relationships()
    click.echo(click.style("\n📊 Knowledge Statistics", fg='cyan', bold=True))
    click.echo(f"Rules: {results['rules']['stats']['total_nodes']}")
    click.echo(f"Knowledge: {results['knowledge']['stats']['total_nodes']}")
    click.echo(f"Total Edges: {results['combined_stats']['total_edges']}")
    
    if results['rules']['stats']['most_connected']:
        click.echo(click.style("\n🔗 Most Connected Rules:", fg='yellow'))
        for node in results['rules']['stats']['most_connected']:
            click.echo(f"  - {node['name']} ({node['connections']} connections)")


# Interactive Mode
@cli.command()
def interactive():
    """
    Start interactive mode
    啟動互動模式
    """
    click.echo(click.style("\n🛠️  Devtools Interactive Mode", fg='cyan', bold=True))
    click.echo("Type 'help' for available commands, 'exit' to quit\n")
    
    while True:
        try:
            command = click.prompt(click.style('devtools', fg='green') + ' > ', type=str)
            
            if command.lower() in ['exit', 'quit', 'q']:
                click.echo("Goodbye! 👋")
                break
            
            if command.lower() == 'help':
                click.echo("""
Available commands:
  new       - Create new project
  check     - Run security checks
  release   - Prepare release
  analyze   - Analyze dependencies
  workflow  - Workflow commands
  git       - Git automation
  help      - Show this help
  exit      - Exit interactive mode
                """)
                continue
            
            # Execute command
            import shlex
            try:
                cli.main(shlex.split(command), standalone_mode=False)
            except SystemExit:
                pass
            except Exception as e:
                click.echo(click.style(f"Error: {e}", fg='red'))
        
        except KeyboardInterrupt:
            click.echo("\nGoodbye! 👋")
            break
        except EOFError:
            click.echo("\nGoodbye! 👋")
            break


if __name__ == '__main__':
    cli()
