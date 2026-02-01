# Skills vs Rules - 架構決策分析
# Skills vs Rules - Architecture Decision Analysis

**Question**: 有了 skills 後還需要大量的 rules 並進行管理嗎？  
**Question**: With skills, do we still need extensive rules management?

**Answer**: 需要，但方式不同。Skills 和 Rules 是互補的，不是替代關係。

**Answer**: Yes, but differently. Skills and Rules are complementary, not替代.

---

## 🎯 Skills vs Rules 的本質區別

### Skills（技能）
**What**: Reusable capabilities / 可重用的能力  
**Purpose**: DO things / 做事情  
**Example**: Web scraping, data analysis, API calls

**Characteristics**:
- ✅ Executable code / 可執行程式碼
- ✅ Composable / 可組合
- ✅ Parameterized / 可參數化
- ✅ Testable / 可測試

**Example**:
```python
# skills/web_search/skill.py
class WebSearchSkill:
    def search(self, query: str) -> List[Result]:
        # Implementation
        pass
```

---

### Rules（規則）
**What**: Constraints and guidelines / 約束和指南  
**Purpose**: GOVERN how things are done / 管理如何做事  
**Example**: "Always read README.md before entering directory"

**Characteristics**:
- ✅ Declarative / 聲明式
- ✅ Enforceable / 可執行
- ✅ Auditable / 可審計
- ✅ Context-specific / 特定於上下文

**Example**:
```markdown
# DIRECTORY_README_RULE.md
MANDATORY: Before entering ANY subdirectory, MUST read its README.md first.
```

---

## 📊 對比表 / Comparison Table

| Aspect | Skills | Rules |
|--------|--------|-------|
| **Nature** | Code / 程式碼 | Guidelines / 指南 |
| **Purpose** | Execute tasks / 執行任務 | Govern behavior / 管理行為 |
| **When** | Runtime / 執行時 | Design time / 設計時 |
| **Example** | `web_search.search()` | "Read README first" |
| **Testable** | Unit tests / 單元測試 | Compliance checks / 合規檢查 |
| **Composable** | Yes / 是 | No / 否 |
| **Enforceable** | Via API / 透過 API | Via review / 透過審查 |

---

## 🤔 為什麼兩者都需要？/ Why Both Are Needed?

### Scenario 1: Web Scraping

**Without Skill**:
```python
# Every time you need to scrape, write this:
import requests
from bs4 import BeautifulSoup

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# ... 50 lines of parsing code
```

**With Skill**:
```python
# Reusable, tested, optimized
from skills.web_search import WebSearchSkill

skill = WebSearchSkill()
results = skill.search("AI tools")
```

**Benefit**: Don't repeat yourself / 不要重複自己

---

**Without Rule**:
```python
# Skill might scrape too aggressively
skill.search("query", rate_limit=None)  # ❌ Might get banned
```

**With Rule**:
```markdown
# SKILL_USAGE_RULES.md
- MUST respect rate limits (max 10 requests/second)
- MUST include User-Agent header
- MUST handle 429 (Too Many Requests) gracefully
```

**Benefit**: Ensures responsible usage / 確保負責任的使用

---

### Scenario 2: Code Modification

**Without Skill**:
```python
# Manually edit files every time
with open('file.py', 'r') as f:
    content = f.read()
# ... manual string manipulation
```

**With Skill**:
```python
# Automated, consistent
from skills.code_refactor import RefactorSkill

skill = RefactorSkill()
skill.rename_function('old_name', 'new_name')
```

---

**Without Rule**:
```python
# Modify file without updating README
skill.rename_function('old_name', 'new_name')
# ❌ README.md still shows old_name
```

**With Rule**:
```markdown
# DIRECTORY_README_RULE.md
After modifying ANY file, MUST update directory README.md
```

**Benefit**: Maintains consistency / 保持一致性

---

## 🎯 專家建議：分層管理 / Expert Recommendation: Layered Management

### Layer 1: Core Rules (Few, Critical)
**Count**: 5-10 rules  
**Scope**: Workspace-wide  
**Enforcement**: Mandatory

**Examples**:
1. Directory README Rule
2. Bilingual Documentation Rule
3. Security-First Rule
4. Git Commit Convention
5. Code Review Requirement

**Storage**: Root-level files
- `DIRECTORY_README_RULE.md`
- `AGENT_RULES.md`
- `DOC_GUIDE.md`

---

### Layer 2: Domain Rules (Moderate, Specific)
**Count**: 10-20 rules per domain  
**Scope**: Specific to devtools, agents, skills  
**Enforcement**: Recommended

**Examples**:
- `devtools/TOOL_DEVELOPMENT_RULES.md`
- `agents/AGENT_BEHAVIOR_RULES.md`
- `skills/SKILL_DESIGN_RULES.md`

---

### Layer 3: Skill-Specific Rules (Many, Contextual)
**Count**: 1-5 rules per skill  
**Scope**: Individual skill  
**Enforcement**: Optional but recommended

**Examples**:
- `skills/web_search/USAGE_RULES.md`
- `skills/data_analysis/BEST_PRACTICES.md`

---

## 📋 Rule Management Strategy / 規則管理策略

### ✅ DO: Keep Rules Minimal and Focused

**Bad** (Too many rules):
```
RULE_001.md
RULE_002.md
RULE_003.md
... (100 rules)
```

**Good** (Organized by domain):
```
DIRECTORY_README_RULE.md      ← Core
AGENT_RULES.md                ← Core
devtools/DEVELOPMENT_RULES.md ← Domain
skills/web_search/USAGE.md    ← Skill-specific
```

---

### ✅ DO: Make Rules Discoverable

**Bad**:
- Rules scattered everywhere
- No index

**Good**:
```markdown
# VIBE_GUIDE.md
## Core Principles
0. Directory README Rule (CRITICAL)
1. Separation of Concerns
2. Bilingual Everything
...
```

---

### ✅ DO: Automate Rule Enforcement

**Example**: Pre-commit hook
```bash
# .git/hooks/pre-commit
#!/bin/bash

# Check if README.md was updated when files changed
python devtools/check_readme_sync.py

# Check bilingual format
python devtools/check_bilingual.py
```

---

### ❌ DON'T: Create Rules for Everything

**Bad**:
```markdown
# VARIABLE_NAMING_RULE.md
Variables must be named in snake_case
Functions must be named in snake_case
Classes must be named in PascalCase
...
```

**Good**:
Use linter (automated) instead of manual rule:
```bash
# .pylintrc or pyproject.toml
[tool.pylint]
variable-naming-style = "snake_case"
```

---

## 🎯 Final Answer / 最終答案

### Question: 有了 skills 後還需要大量的 rules 嗎？

**Answer**: 需要，但不是「大量」。

**Strategy**:
1. **Core Rules**: 5-10 個（關鍵、強制）
2. **Domain Rules**: 每個領域 10-20 個（推薦）
3. **Skill-Specific Rules**: 每個技能 1-5 個（可選）

**Total**: ~30-50 rules across entire workspace

---

### Why This Works / 為什麼這樣有效:

1. **Skills handle "what"** / Skills 處理「做什麼」
   - Web scraping
   - Data analysis
   - Code refactoring

2. **Rules handle "how"** / Rules 處理「如何做」
   - Rate limiting
   - Error handling
   - Documentation updates

3. **Together**: Powerful + Responsible
   - Skills provide capability
   - Rules ensure quality

---

## 📊 Example: Web Search Skill + Rules

### Skill (Code):
```python
# skills/web_search/skill.py
class WebSearchSkill:
    def __init__(self, rate_limit=10):
        self.rate_limit = rate_limit
    
    def search(self, query: str) -> List[Result]:
        # Implementation with rate limiting
        pass
```

### Rules (Guidelines):
```markdown
# skills/web_search/USAGE_RULES.md

1. MUST set appropriate rate_limit (default: 10 req/s)
2. MUST handle network errors gracefully
3. MUST cache results when possible
4. MUST respect robots.txt
```

### Result:
- ✅ Skill provides reusable code
- ✅ Rules ensure responsible usage
- ✅ Both are necessary

---

## 🎯 Conclusion / 結論

**Skills 和 Rules 是互補的，不是替代的。**

**Skills and Rules are complementary, not替代.**

**Best Practice**:
- Keep core rules minimal (5-10)
- Organize domain rules by directory
- Embed skill-specific rules in skill README
- Automate enforcement where possible
- Review and update regularly

**最佳實踐**:
- 保持核心規則最少（5-10 個）
- 按目錄組織領域規則
- 在技能 README 中嵌入特定規則
- 盡可能自動化執行
- 定期審查和更新

---

**Created**: 2026-01-29  
**Status**: Active  
**Recommendation**: Implement layered rule management
