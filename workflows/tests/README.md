# Workflow Tests

**Purpose**: Integration tests for workflow system  
**用途**: 工作流系統整合測試

---

## 🧪 Test Coverage

### Integration Tests (`test_integration.py`)

**Workflow Tests**:
- ✅ Parse all workflow templates
- ✅ Validate all workflow templates
- ✅ Execute workflows in dry-run mode

**Skill Tests**:
- ✅ Verify skill existence
- ✅ Check skill structure

**Agent Tests**:
- ✅ Verify agent existence
- ✅ Check agent structure
- ✅ Test agent functionality

---

## 🚀 Running Tests

### Run all tests
```bash
pytest workflows/tests/ -v
```

### Run specific test file
```bash
pytest workflows/tests/test_integration.py -v
```

### Run with coverage
```bash
pytest workflows/tests/ --cov=workflows --cov=skills --cov=agents
```

---

## 📋 Test Requirements

Install test dependencies:
```bash
pip install pytest pytest-asyncio pytest-cov
```

---

**Created**: 2026-02-01  
**Status**: Active
