# Document Processing Guide / 文件處理指南

**synthforge** 現在支援透過 LangChain 生態系處理外部文件。這讓 AI 能夠理解 PDF、網頁或其他格式的需求規格。

## 🚀 快速開始

### 載入 PDF
```bash
python devtools/cli.py doc load path/to/spec.pdf --type pdf
```

### 載入網頁並自動切割
```bash
python devtools/cli.py doc load https://python.org --type url --split
```

## 🛠️ 技術規格

### DocumentSkill (`skills/integration/document_skill.py`)
核心能力組件，整合了：
- `PyPDFLoader`: 處理 PDF 文件。
- `WebBaseLoader`: 抓取網頁內容。
- `RecursiveCharacterTextSplitter`: 智慧分段，支援語義化切割。

### CLI 指令
- `doc load <source>`: 載入文件或網址。
  - `--type [pdf|url]`: 指定來源類型。
  - `--split`: 是否自動進行文本切割。

## 📂 目錄結構
- `skills/integration/`: 整合外部框架的技能。
- `skills/integration/tests/`: 相關單元與整合測試。
