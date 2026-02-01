"""
Project Scaffolder - 專案腳手架
快速生成各種類型的專案結構

Project Scaffolder - Quickly generate project structures for various types
"""

import click
from pathlib import Path
import shutil
from datetime import datetime


TEMPLATES = {
    'python-cli': {
        'description': 'Python CLI Application',
        'files': {
            'main.py': '''#!/usr/bin/env python3
"""
{project_name} - CLI Application
"""

import click

@click.command()
@click.option('--name', default='World', help='Name to greet')
def main(name):
    """Simple CLI application"""
    click.echo(f'Hello {{name}}!')

if __name__ == '__main__':
    main()
''',
            'requirements.txt': '''click>=8.0.0
''',
            'README.md': '''# {project_name}

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py --name=YourName
```
''',
            '.gitignore': '''__pycache__/
*.pyc
.venv/
.env
dist/
build/
*.egg-info/
''',
        }
    },
    
    'python-fastapi': {
        'description': 'Python FastAPI Web Service',
        'files': {
            'main.py': '''from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="{project_name}")

class Item(BaseModel):
    name: str
    description: str = None

@app.get("/")
async def root():
    return {{"message": "Welcome to {project_name}"}}

@app.post("/items/")
async def create_item(item: Item):
    return {{"item": item, "status": "created"}}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
''',
            'requirements.txt': '''fastapi>=0.100.0
uvicorn[standard]>=0.23.0
pydantic>=2.0.0
''',
            'README.md': '''# {project_name}

FastAPI Web Service

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Visit: http://localhost:8000/docs
''',
            '.gitignore': '''__pycache__/
*.pyc
.venv/
.env
''',
        }
    },
    
    'node-express': {
        'description': 'Node.js Express Server',
        'files': {
            'index.js': '''const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

app.get('/', (req, res) => {{
  res.json({{ message: 'Welcome to {project_name}' }});
}});

app.listen(port, () => {{
  console.log(`Server running on port ${{port}}`);
}});
''',
            'package.json': '''{
  "name": "{project_name}",
  "version": "1.0.0",
  "description": "Express server",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js"
  },
  "dependencies": {
    "express": "^4.18.0"
  },
  "devDependencies": {
    "nodemon": "^3.0.0"
  }
}
''',
            'README.md': '''# {project_name}

Node.js Express Server

## Installation

```bash
npm install
```

## Run

```bash
npm start
```
''',
            '.gitignore': '''node_modules/
.env
dist/
''',
        }
    },
    
    'static-web': {
        'description': 'Static Website (HTML/CSS/JS)',
        'files': {
            'index.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project_name}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Welcome to {project_name}</h1>
        <p>Edit index.html to get started.</p>
    </div>
    <script src="script.js"></script>
</body>
</html>
''',
            'style.css': '''* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}}

.container {{
    background: white;
    padding: 3rem;
    border-radius: 1rem;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    text-align: center;
}}

h1 {{
    color: #333;
    margin-bottom: 1rem;
}}

p {{
    color: #666;
}}
''',
            'script.js': '''console.log('Welcome to {project_name}');

// Add your JavaScript here
''',
            'README.md': '''# {project_name}

Static Website

## Usage

Open `index.html` in your browser.
''',
        }
    },
}


@click.command()
@click.option('--name', required=True, help='Project name')
@click.option('--type', 'project_type', 
              type=click.Choice(list(TEMPLATES.keys())),
              default='python-cli',
              help='Project type')
@click.option('--path', default=None, help='Custom output path (default: projects/<name>)')
def new_project(name, project_type, path):
    """
    Create a new project from template
    從模板創建新專案
    """
    # 確定輸出路徑
    if path:
        output_path = Path(path)
    else:
        workspace_root = Path(__file__).parent.parent
        output_path = workspace_root / 'projects' / name
    
    if output_path.exists():
        click.echo(f"❌ Project already exists: {output_path}")
        click.echo(f"❌ 專案已存在: {output_path}")
        return
    
    # 獲取模板
    template = TEMPLATES[project_type]
    
    click.echo(f"\n🚀 Creating new project: {name}")
    click.echo(f"   Type: {template['description']}")
    click.echo(f"   Path: {output_path}\n")
    
    # 創建目錄
    output_path.mkdir(parents=True, exist_ok=True)
    
    # 生成檔案
    for filename, content in template['files'].items():
        file_path = output_path / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 替換模板變數
        content = content.format(
            project_name=name,
            date=datetime.now().strftime('%Y-%m-%d')
        )
        
        file_path.write_text(content, encoding='utf-8')
        click.echo(f"   ✓ Created: {filename}")
    
    click.echo(f"\n✅ Project created successfully!")
    click.echo(f"✅ 專案創建成功！\n")
    click.echo(f"📝 Next steps:")
    click.echo(f"   cd {output_path}")
    
    if project_type.startswith('python'):
        click.echo(f"   python -m venv .venv")
        click.echo(f"   .venv\\Scripts\\activate  # Windows")
        click.echo(f"   source .venv/bin/activate  # Unix")
        click.echo(f"   pip install -r requirements.txt")
    elif project_type.startswith('node'):
        click.echo(f"   npm install")
        click.echo(f"   npm start")


if __name__ == '__main__':
    new_project()
