# DRY_RULE.md - Don't Repeat Yourself Rule

**Status**: MANDATORY 強制  
**Priority**: HIGH 高  
**Scope**: All code and documentation in synthforge

---

## 🎯 Core Principle / 核心原則

Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

系統中的每一個知識點都必須有單一、明確、權威的表述。

**BUT**: Don't be too DRY. Balance DRY with readability and maintainability.

**但是**: 不要過度乾燥。在 DRY 和可讀性、可維護性之間取得平衡。

---

## 📋 Enforcement Scope / 執行範圍

### MUST (必須遵循) - 強制提取

**When duplication is NOT allowed**:

#### 1. 規則和文件中的重複內容
```markdown
❌ BAD: Token 限制在 3 個規則中重複定義
RULE_A.md: "Token limit: 10K warning, 20K critical"
RULE_B.md: "Token limit: 10K warning, 20K critical"
RULE_C.md: "Token limit: 10K warning, 20K critical"

✅ GOOD: 單一定義，其他引用
TOKEN_STANDARD.md: "Token limit: 10K warning, 20K critical"
RULE_A.md: "See [TOKEN_STANDARD.md](TOKEN_STANDARD.md)"
RULE_B.md: "See [TOKEN_STANDARD.md](TOKEN_STANDARD.md)"
```

#### 2. 配置和常數的重複定義
```python
❌ BAD: 魔術數字重複出現
def calculate_circle_area(radius):
    return 3.14159 * radius * radius

def calculate_circle_circumference(radius):
    return 2 * 3.14159 * radius

✅ GOOD: 單一定義
PI = 3.14159  # Single source of truth

def calculate_circle_area(radius):
    return PI * radius ** 2

def calculate_circle_circumference(radius):
    return 2 * PI * radius
```

#### 3. 相同邏輯重複 3 次以上
```python
❌ BAD: 相同驗證邏輯重複 3 次
def process_user(user):
    if not user or not user.email or '@' not in user.email:
        raise ValueError("Invalid user")
    # process...

def save_user(user):
    if not user or not user.email or '@' not in user.email:
        raise ValueError("Invalid user")
    # save...

def update_user(user):
    if not user or not user.email or '@' not in user.email:
        raise ValueError("Invalid user")
    # update...

✅ GOOD: 提取為函數
def validate_user(user):
    if not user or not user.email or '@' not in user.email:
        raise ValueError("Invalid user")

def process_user(user):
    validate_user(user)
    # process...

def save_user(user):
    validate_user(user)
    # save...
```

**Action**: 必須提取到單一位置，其他地方引用。

---

### SHOULD (應該遵循) - 建議提取

**When duplication should be avoided**:

#### 1. 相同邏輯重複 2 次
```python
⚠️ CONSIDER: 重複 2 次，評估是否提取
def format_user_name(user):
    return f"{user.first_name} {user.last_name}".strip()

def format_admin_name(admin):
    return f"{admin.first_name} {admin.last_name}".strip()

# 評估:
# - 未來會有更多類似的格式化嗎？ → 提取
# - User 和 Admin 的格式化可能不同？ → 保留
```

**Rule of Three**: 第 3 次重複時必須提取，第 2 次重複時評估。

#### 2. 相似的文件結構
```markdown
⚠️ CONSIDER: 多個文件有相同的 sections
File A:
## Purpose
## Usage
## Examples

File B:
## Purpose
## Usage
## Examples

# 評估:
# - 這是標準格式嗎？ → 創建模板
# - 內容差異大嗎？ → 保留
```

**Action**: 評估後決定是否提取。考慮：
- 未來是否會獨立演化？
- 提取後是否更易維護？
- 是否降低可讀性？

---

### MAY (可以保留重複) - 允許重複

**When duplication is acceptable**:

#### 1. 為了可讀性的重複
```python
✅ ACCEPTABLE: 簡單計算重複 2 次
def calculate_discount_price(price):
    return price * 0.9  # 10% discount

def calculate_tax_price(price):
    return price * 1.1  # 10% tax

# 理由:
# - 邏輯簡單，一行即可理解
# - 提取後反而降低可讀性
# - 未來可能獨立變化（折扣率 vs 稅率）
```

#### 2. 不同上下文的相似實作
```python
✅ ACCEPTABLE: 看起來相似但概念不同
class User:
    def validate(self):
        if not self.email:
            raise ValueError("Email required")
        if not self.name:
            raise ValueError("Name required")

class Product:
    def validate(self):
        if not self.name:
            raise ValueError("Name required")
        if not self.price:
            raise ValueError("Price required")

# 理由:
# - User 和 Product 是不同的領域概念
# - 驗證規則未來可能完全不同
# - 強行提取會造成不當耦合
```

#### 3. 解耦比 DRY 更重要
```python
✅ ACCEPTABLE: 不同模組的獨立實作
# module_a.py
def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')

# module_b.py
def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')

# 理由:
# - 兩個模組應該獨立
# - 避免共享依賴
# - 未來可能需要不同的日期格式
```

**Action**: 保持重複，但記錄原因（註解或文件）。

---

## ⚖️ Balance: Don't Be Too DRY / 不要過度乾燥

### 過度 DRY 的問題

#### 問題 1: 過度抽象
```python
❌ TOO DRY: 過度抽象導致難以理解
def process(entity, action, validator, transformer, saver, logger, config):
    """太多參數，完全不知道在做什麼"""
    if validator(entity, config):
        transformed = transformer(entity, config)
        result = saver(transformed, config)
        logger.log(action, result)
        return result

✅ BALANCED: 適度抽象
def save_user(user):
    """清楚明確的功能"""
    validate_user(user)
    user_data = transform_user_data(user)
    return database.save(user_data)
```

#### 問題 2: 錯誤的抽象
```python
❌ TOO DRY: 強行合併不相關的概念
def process_entity(entity):
    """User 和 Product 強行合併"""
    if entity.type == 'user':
        # user logic
    elif entity.type == 'product':
        # product logic

✅ BALANCED: 分離不同概念
def process_user(user):
    # user logic

def process_product(product):
    # product logic
```

#### 問題 3: 過早優化
```python
❌ TOO DRY: 第一次重複就提取
# 只出現 1 次，就創建複雜的抽象層
def create_abstract_factory_builder_pattern():
    ...

✅ BALANCED: 等到第 3 次重複
# 第 1 次: 寫程式碼
# 第 2 次: 注意到重複，但保持觀察
# 第 3 次: 確認模式，提取重複
```

---

## ✅ Checklist / 檢查清單

### 創建/修改程式碼時:

- [ ] 是否有重複的邏輯？
- [ ] 重複出現幾次？（1次/2次/3次以上）
- [ ] 是否屬於 MUST/SHOULD/MAY 範圍？
- [ ] 提取後是否更易理解？
- [ ] 提取後是否更易維護？
- [ ] 是否會造成不當耦合？
- [ ] 如果保留重複，原因是什麼？

### 創建/修改文件時:

- [ ] 是否有重複的內容？
- [ ] 是否可以用引用代替重複？
- [ ] 引用後是否仍然易於理解？
- [ ] 是否符合 DRY 原則？

---

## 🎯 Decision Tree / 決策樹

```
發現重複
    ↓
重複幾次？
    ├─ 1 次 → 保持，不處理
    ├─ 2 次 → 評估
    │   ├─ 未來會更多？ → 提取
    │   ├─ 可能獨立演化？ → 保留
    │   └─ 簡單邏輯？ → 保留
    └─ 3 次以上 → 必須提取
        ↓
提取後是否更易理解？
    ├─ 是 → 提取 ✅
    └─ 否 → 重新評估
        ↓
    是否不同概念？
        ├─ 是 → 保留重複 ✅
        └─ 否 → 簡化抽象後提取 ✅
```

---

## 📊 Examples in synthforge / synthforge 中的範例

### 範例 1: 規則整合（正確的 DRY）✅

**Before**: 4 個規則重複 .internal/ 結構說明
```
CONFIRMATION_DOCUMENTS_RULE.md: .internal/ 結構 (重複 1)
INTERNAL_MANAGEMENT_RULE.md: .internal/ 結構 (重複 2)
KNOWLEDGE_MANAGEMENT_RULE.md: .internal/ 結構 (重複 3)
TOKEN_CLEANUP_RULE.md: .internal/ 結構 (重複 4)
```

**After**: 整合為 INTERNAL_RULE.md
```
INTERNAL_RULE.md: .internal/ 結構 (單一來源)
```

**Result**: ✅ 節省 40% 行數，單一真相來源

---

### 範例 2: 語言策略（正確的應用，不是重複）✅

**BILINGUAL_OUTPUT_RULE.md**: 定義策略
```markdown
Layer 1 (雙語): 核心規則
Layer 2 (純中文): .internal/ 內容
```

**INTERNAL_RULE.md**: 應用策略
```markdown
任務總結模板: 純中文（遵循 BILINGUAL_OUTPUT_RULE）
```

**Result**: ✅ 不是重複，是正確的策略應用

---

### 範例 3: 檔案命名（正確的子集，不是重複）✅

**FILE_NAMING_CONVENTION_RULE.md**: 完整規範
```markdown
所有檔案類型的命名規範
```

**INTERNAL_RULE.md Part 1.3**: .internal/ 子集
```markdown
只提到 .internal/ 相關的命名
```

**Result**: ✅ 不是重複，一個是完整規範，一個是子集

---

## ⚠️ Common Pitfalls / 常見陷阱

### 陷阱 1: 過度 DRY
```python
❌ 不要這樣做
def do_everything(a, b, c, d, e, f, g, h, i, j):
    # 10 個參數，完全不知道在做什麼
    pass
```

### 陷阱 2: 錯誤的抽象
```python
❌ 不要這樣做
def process_user_and_product(item):
    # 強行合併不相關的概念
    pass
```

### 陷阱 3: 過早優化
```python
❌ 不要這樣做
# 只重複 1 次就創建複雜的抽象
```

### 陷阱 4: 忽略上下文
```python
❌ 不要這樣做
# 不同領域的概念強行共用程式碼
```

---

## 🔗 Related / 相關

**Detailed Explanation**:  
詳細說明和更多範例請參見: [DRY 原則知識點](.internal/knowledge/best_practices/dry_principle.md)

**Other Principles**:
- KISS Principle (Keep It Simple, Stupid)
- YAGNI Principle (You Aren't Gonna Need It)
- SOLID Principles

---

## 🎯 Summary / 總結

**Key Points**:

1. ✅ **MUST**: 重複 3 次以上 → 必須提取
2. ✅ **SHOULD**: 重複 2 次 → 評估後決定
3. ✅ **MAY**: 可讀性、不同概念、解耦 → 可以保留
4. ✅ **Rule of Three**: 第 3 次重複時才提取
5. ✅ **Balance**: 不要過度 DRY，保持可讀性

**Remember**:
- DRY is a principle, not a religion
- Balance DRY with readability
- Don't extract on first duplication
- Wrong abstraction is worse than duplication

**記住**:
- DRY 是原則，不是教條
- 在 DRY 和可讀性之間取得平衡
- 不要在第一次重複就提取
- 錯誤的抽象比重複更糟

**This rule ensures maintainability while avoiding over-abstraction.**  
**此規則確保可維護性，同時避免過度抽象。**

---

## 📚 相關規則 / Related Rules

### 強依賴 (Strong Dependencies)
- 無（DRY 是基礎原則）

### 相關 (Related)
- **FILE_NAMING_CONVENTION_RULE.md** - 命名應該清楚避免混淆
- [INTERNAL_RULE](../development/INTERNAL_RULE.md) - 知識點應該整合不重複
- [SINGLE_SOURCE_OF_TRUTH_RULE](SINGLE_SOURCE_OF_TRUTH_RULE.md) - DRY 的延伸原則

### 衝突 (Conflicts)
- ❌ 無已知衝突

---

**Created**: 2026-01-29  
**Last Updated**: 2026-02-01  
**Status**: ACTIVE  
**Priority**: HIGH  
**Enforcement**: MANDATORY
