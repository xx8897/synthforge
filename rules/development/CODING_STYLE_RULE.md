# CODING_STYLE_RULE.md - Coding Style Guidelines
# Clean Code & Best Practices

**Status**: MANDATORY 強制
**Priority**: HIGH 高
**Scope**: All code in synthforge

---

## 🎯 規則目的 / Rule Purpose

建立統一的高標準程式碼風格，確保程式碼的可讀性、可維護性和擴展性。

Establish unified, high-standard coding style to ensure code readability, maintainability, and scalability.

**Core Philosophy**: Code is read much more often than it is written.
**核心哲學**: 程式碼被閱讀的次數遠多於被撰寫的次數。

---

## 📋 1. Clean Code Principles / Clean Code 原則

### 1.1 Small Functions (小函數)
- **Rule**: Functions should be small (ideally < 20 lines).
- **Rule**: A function should do ONE thing only (SRP).
- **原則**: 函數應該很小（理想情況 < 20 行）。
- **原則**: 一個函數應該只做一件事（單一職責原則）。

```python
# ❌ BAD: Doing too much
def process_user_data(data):
    # Validate
    if not data.get('id'): raise ...
    # Transform
    user = User(data)
    user.name = data['name'].upper()
    # Save
    db.save(user)
    # Email
    email.send(user)

# ✅ GOOD: Composed functions
def process_user_data(data):
    validate_data(data)
    user = create_user_from_data(data)
    save_to_db(user)
    send_welcome_email(user)
```

### 1.2 Meaningful Names (有意義的命名)
- **Rule**: Names should reveal intent.
- **Rule**: Avoid abbreviations (unless standard like `id`, `url`).
- **Rule**: Use `verb_noun` for functions/methods.
- **原則**: 命名應該揭示意圖。
- **原則**: 避免縮寫（除非是標準的如 `id`, `url`）。
- **原則**: 函數/方法使用 `動詞_名詞`。

```python
# ❌ BAD
d = 10  # days
def get_it(): ...

# ✅ GOOD
days_since_creation = 10
def get_active_accounts(): ...
```

### 1.3 Minimal Comments (最小化註解)
- **Rule**: Code should be self-documenting. Use descriptive names instead of comments.
- **Rule**: Comments should explain "Why", not "What".
- **Rule**: Public APIs MUST have docstrings.
- **原則**: 程式碼應該自我文檔化。使用描述性命名代替註解。
- **原則**: 註解應該解釋「為什麼」，而不是「做什麼」。
- **原則**: 公共 API 必須有文件字串。

```python
# ❌ BAD
# Check if user is active
if user.status == 1:
    ...

# ✅ GOOD
if user.is_active():
    ...
```

---

## 🐍 2. Python Conventions / Python 規範

### 2.1 Naming (命名)
- **Classes**: `PascalCase` (e.g., `UserAccount`)
- **Functions/Variables**: `snake_case` (e.g., `calculate_total`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRY_COUNT`)
- **Private**: `_leading_underscore` (e.g., `_internal_method`)

### 2.2 Type Hinting (型別提示)
- **MANDATORY**: All function signatures MUST have type hints.
- **強制**: 所有函數簽名必須有型別提示。

```python
def calculate_score(points: list[int], bonus: float = 0.0) -> float:
    return sum(points) + bonus
```

### 2.3 Docstrings (文件字串)
- **MANDATORY**: All public modules, classes, and functions.
- **Format**: Google Style or Sphinx Style.
- **Language**: English (Bilingual preferred for complex logic).

---

## 🌟 3. Anti-Patterns to Avoid / 應避免的反模式

### 3.1 Magic Numbers (魔術數字)
- **Avoid**: Hardcoded numbers in logic.
- **Use**: Named constants.

```python
# ❌ BAD
if points > 100: ...

# ✅ GOOD
WINNING_SCORE = 100
if points > WINNING_SCORE: ...
```

### 3.2 Deep Nesting (深層嵌套)
- **Avoid**: `if` inside `if` inside `for`...
- **Use**: Guard clauses (early returns) or extract functions.

```python
# ❌ BAD
if valid:
    if active:
        do_work()

# ✅ GOOD
if not valid: return
if not active: return
do_work()
```

---

## ⚠️ 4. AI-Specific Rules / AI 特別規則

### 4.1 NO Placeholders (無佔位符)
- **Rule**: Never leave `pass`, `...`, or `# TODO: implement this` in final code.
- **Rule**: If implementation is pending, raise `NotImplementedError` with a clear message.
- **原則**: 絕不在最終程式碼中留下佔位符。
- **原則**: 如果實作待定，拋出 `NotImplementedError` 並附帶清楚訊息。

### 4.2 Explicit Imports (明確導入)
- **Rule**: Avoid `from module import *`.
- **Rule**: Import only what is used.

---

## ✅ Checklist / 檢查清單

Before marking a task as complete:
- [ ] Are functions small and focused?
- [ ] Are naming conventions followed?
- [ ] Are type hints present?
- [ ] Is logic explained via code structure, not comments?
- [ ] Are magic numbers extracted to constants?

---

**Created**: 2026-02-01
**Status**: ACTIVE
**Enforcement**: MANDATORY
