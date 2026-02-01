# Quick Start Guide

Get your AI Workspace up and running in 5 minutes!

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git (optional, for version control)

## Step 1: Set Up Python Environment

```bash
# Navigate to workspace
cd C:\Users\xx8897\ai_workspace

# Create virtual environment
python -m venv .venv

# Activate it
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# Upgrade pip
python -m pip install --upgrade pip
```

## Step 2: Install Dependencies

```bash
# Create requirements file first (if not exists)
mkdir requirements
echo openai anthropic requests pyyaml > requirements\base.txt

# Install
pip install -r requirements\base.txt
```

## Step 3: Set Up Environment Variables

Create a `.env` file in the workspace root:

```bash
# .env
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
WORKSPACE_ROOT=C:\Users\xx8897\ai_workspace
```

## Step 4: Create Basic Structure

```bash
# Create core directories
mkdir agents skills projects core_lib templates playground

# Create a simple skill
mkdir skills\hello_world
```

## Step 5: Create Your First Skill

Create `skills/hello_world/handler.py`:

```python
def execute(context, **kwargs):
    """A simple hello world skill."""
    name = kwargs.get('name', 'World')
    return f"Hello, {name}!"
```

Create `skills/hello_world/skill.yaml`:

```yaml
name: hello_world
version: 1.0.0
description: A simple greeting skill
inputs:
  name:
    type: string
    required: false
    default: World
```

## Step 6: Create Your First Agent

Create `agents/greeter/agent.yaml`:

```yaml
name: greeter
role: Friendly greeting assistant
model: gpt-4o-mini
temperature: 0.7
skills:
  - hello_world:1.0.0
```

Create `agents/greeter/system_prompt.md`:

```markdown
You are a friendly greeting assistant. 
When asked to greet someone, use the hello_world skill.
Be warm and welcoming!
```

## Step 7: Create Your First Project

```bash
# Create project directory
mkdir projects\my_first_project
cd projects\my_first_project

# Create main file
```

Create `projects/my_first_project/main.py`:

```python
import sys
sys.path.append('C:\\Users\\xx8897\\ai_workspace')

from core_lib.loader import load_skill

# Use the hello_world skill
hello_skill = load_skill('hello_world')
result = hello_skill.execute(name="AI Developer")
print(result)  # Output: Hello, AI Developer!
```

## Step 8: Run Your Project

```bash
python main.py
```

You should see: `Hello, AI Developer!`

## What's Next?

### Learn More
- Read [ARCHITECTURE.md](./ARCHITECTURE.md) to understand the system
- Check [ROADMAP.md](../architecture/ROADMAP.md) for all available features
- Review [ROADMAP.md](./ROADMAP.md) for implementation phases

### Add More Features
1. **Create more skills** - Add web search, file operations, etc.
2. **Build complex agents** - Combine multiple skills
3. **Start real projects** - Build something useful!

### Recommended Next Steps

1. **Add Templates** - Make project creation instant
2. **Set up Testing** - Ensure quality
3. **Add Observability** - Track what's happening

## Common Issues

### Import Errors
If you get import errors, make sure:
- Virtual environment is activated
- `PYTHONPATH` includes workspace root
- All dependencies are installed

### API Key Errors
- Check `.env` file exists
- Verify API keys are valid
- Ensure `.env` is loaded (use `python-dotenv`)

### Path Issues
- Use absolute paths in development
- Set `WORKSPACE_ROOT` environment variable
- Check `core_lib/paths.py` configuration

## Tips

- **Use the playground** - Test ideas quickly in `playground/`
- **Version your skills** - Prevents breaking changes
- **Document everything** - Future you will thank you
- **Start simple** - Add complexity as needed

## Getting Help

- Review the documentation in this workspace
- Check example skills and agents
- Experiment in the playground

---

# 快速上手指南

在 5 分鐘內啟動並執行您的 AI 工作區！

## 先決條件

- Python 3.10 或更高版本
- pip (Python 包管理器)
- Git (可選，用於版本控制)

## 第 1 步：設置 Python 環境

```bash
# 進入工作區
cd C:\Users\xx8897\ai_workspace

# 創建虛擬環境
python -m venv .venv

# 激活虛擬環境
.venv\Scripts\activate  # Windows 系統
# source .venv/bin/activate  # macOS/Linux 系統

# 升級 pip
python -m pip install --upgrade pip
```

## 第 2 步：安裝依賴項

```bash
# 首先創建 requirements 文件（如果不存在）
mkdir requirements
echo openai anthropic requests pyyaml > requirements\base.txt

# 安裝
pip install -r requirements\base.txt
```

## 第 3 步：設置環境變量

在工作區根目錄創建一個 `.env` 文件：

```bash
# .env
OPENAI_API_KEY=您的_openai_key
ANTHROPIC_API_KEY=您的_anthropic_key
WORKSPACE_ROOT=C:\Users\xx8897\ai_workspace
```

## 第 4 步：創建基本結構

```bash
# 創建核心目錄
mkdir agents skills projects core_lib templates playground

# 創建一個簡單的技能
mkdir skills\hello_world
```

## 第 5 步：創建您的第一個技能

創建 `skills/hello_world/handler.py`：

```python
def execute(context, **kwargs):
    """一個簡單的 hello world 技能。"""
    name = kwargs.get('name', 'World')
    return f"Hello, {name}!"
```

創建 `skills/hello_world/skill.yaml`：

```yaml
name: hello_world
version: 1.0.0
description: 一個簡單的問候技能
inputs:
  name:
    type: string
    required: false
    default: World
```

## 第 6 步：創建您的第一個代理

創建 `agents/greeter/agent.yaml`：

```yaml
name: greeter
role: 友好的問候助手
model: gpt-4o-mini
temperature: 0.7
skills:
  - hello_world:1.0.0
```

創建 `agents/greeter/system_prompt.md`：

```markdown
您是一位友好的問候助手。
當被要求向某人問候時，請使用 hello_world 技能。
請保持熱情和歡迎的態度！
```

## 第 7 步：創建您的第一個專案

```bash
# 創建專案目錄
mkdir projects\my_first_project
cd projects\my_first_project

# 創建主文件
```

創建 `projects/my_first_project/main.py`：

```python
import sys
sys.path.append('C:\\Users\\xx8897\\ai_workspace')

from core_lib.loader import load_skill

# 使用 hello_world 技能
hello_skill = load_skill('hello_world')
result = hello_skill.execute(name="AI 開發者")
print(result)  # 輸出：Hello, AI 開發者!
```

## 第 8 步：運行您的專案

```bash
python main.py
```

您應該會看到：`Hello, AI 開發者!`

## 下一步行動

### 了解更多
- 閱讀 [ARCHITECTURE.md](./ARCHITECTURE.md) 以了解系統架構
- 查看 [ROADMAP.md](../architecture/ROADMAP.md) 以獲取所有可用功能列表
- 查看 [ROADMAP.md](./ROADMAP.md) 以了解實施階段

### 添加更多功能
1. **創建更多技能** - 添加網頁搜尋、文件操作等。
2. **構建複雜代理** - 組合多個技能。
3. **開始實際專案** - 構建有用的東西！

### 推薦的後續步驟

1. **添加模板** - 讓專案創建變得瞬間完成
2. **設置測試** - 確保品質
3. **添加可觀測性** - 追踪發生的情況

## 常見問題

### 導入錯誤 (Import Errors)
如果您遇到導入錯誤，請確保：
- 虛擬環境已激活
- `PYTHONPATH` 包含工作區根目錄
- 所有依賴項都已安裝

### API Key 錯誤
- 檢查 `.env` 文件是否存在
- 驗證 API Key 是否有效
- 確保 `.env` 已加載（使用 `python-dotenv`）

### 路徑問題
- 在開發中使用絕對路徑
- 設置 `WORKSPACE_ROOT` 環境變量
- 檢查 `core_lib/paths.py` 配置

## 提示

- **使用實驗場 (Playground)** - 在 `playground/` 中快速測試想法
- **技能版本化** - 防止破壞性變更
- **文檔化一切** - 未來的您會感謝現在的自己
- **從簡單開始** - 根據需要逐步增加複雜度

## 獲取協助

- 查閱此工作區中的文檔
- 查看示例技能和代理
- 在實驗場進行實驗

---

**恭喜您！** 🎉 您現在擁有一個可以運作的 AI 工作區！
