# CLI 測試腳本
# Test all CLI commands

$env:PYTHONIOENCODING="utf-8"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "=== synthforge CLI 測試 ===" -ForegroundColor Cyan
Write-Host ""

# Test 1: Version
Write-Host "1️⃣ 測試版本命令..." -ForegroundColor Yellow
python devtools/cli.py --version
Write-Host ""

# Test 2: Help
Write-Host "2️⃣ 測試幫助命令..." -ForegroundColor Yellow
python devtools/cli.py --help | Select-Object -First 15
Write-Host ""

# Test 3: Workflow list
Write-Host "3️⃣ 測試 workflow list..." -ForegroundColor Yellow
python devtools/cli.py workflow list
Write-Host ""

# Test 4: Info
Write-Host "4️⃣ 測試 info 命令..." -ForegroundColor Yellow
python devtools/cli.py info
Write-Host ""

# Test 5: Git help
Write-Host "5️⃣ 測試 git 命令..." -ForegroundColor Yellow
python devtools/cli.py git --help
Write-Host ""

Write-Host "=== 測試完成 ===" -ForegroundColor Green
