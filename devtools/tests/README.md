# 開發工具測試 - devtools/tests

**用途**: 存放 `core_lib` 與 `devtools` 的單元測試與集成測試
**原則**: 確保核心功能的穩定性與正確性

---

## 📁 檔案清單 / File Manifest

| 檔案 | 用途 | 狀態 |
|------|------|---------|
| [test_core_utils.py](test_core_utils.py) | 測試 `core_lib.utils.files` 的功能 | ✅ Active |

---

## 🚀 執行測試 / Running Tests

在專案根目錄執行：

```bash
python devtools/tests/test_core_utils.py
```

或使用 pytest：

```bash
pytest devtools/tests/
```

---

## 📝 注意事項 / Notes

- 測試應在臨時目錄中執行，避免破壞實際的工作區結構。
- 遵循 `CODING_STYLE_RULE.md` 中的 Clean Code 原則。

---

**最後更新**: 2026-02-01
**維護者**: synthforge team
