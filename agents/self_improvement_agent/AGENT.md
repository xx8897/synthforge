# Self-Improvement Agent

**自我改進代理**

從錯誤中學習並自動優化工作流的智能代理。

---

## 🎯 功能 (Features)

### 1. 錯誤學習 (Error Learning)
- 記錄並分析錯誤模式
- 自動提取解決方案
- 建立錯誤知識庫

### 2. 工作流優化 (Workflow Optimization)
- 分析性能瓶頸
- 建議改進措施
- 自動優化配置

### 3. 性能監控 (Performance Monitoring)
- 實時監控執行時間
- 追蹤成功率
- 生成性能報告

---

## 🚀 使用方法 (Usage)

### 記錄錯誤
```python
from agents.self_improvement_agent.agent import SelfImprovementAgent

agent = SelfImprovementAgent()

# 記錄錯誤
error_id = agent.record_error(
    error_type="validation_error",
    error_message="Invalid input format",
    context={'workflow': 'feature_development', 'step': 'validate'},
    solution="Add input validation"
)
```

### 獲取改進建議
```python
# 分析工作流並獲取建議
suggestions = agent.suggest_improvement(
    workflow_name="feature_development",
    current_performance={
        'execution_time': 450,
        'success_rate': 0.75
    }
)

for suggestion in suggestions['suggestions']:
    print(f"- {suggestion['description']}")
```

### 監控性能
```python
# 監控工作流性能
result = agent.monitor_performance(
    workflow_name="feature_development",
    metrics={
        'execution_time': 320,
        'success_rate': 0.95,
        'tasks_completed': 10
    }
)

if result['alerts']:
    print("⚠️ Alerts:")
    for alert in result['alerts']:
        print(f"  - {alert}")
```

### 生成報告
```python
# 生成改進報告
report = agent.generate_improvement_report()
print(report)
```

---

## 📊 學習數據庫 (Learning Database)

數據存儲在 `.internal/learning/improvements.json`:

```json
{
  "errors": [
    {
      "id": "error_20260202_001234",
      "type": "validation_error",
      "message": "Invalid input",
      "context": {...},
      "solution": "Add validation",
      "timestamp": "2026-02-02T00:12:34",
      "resolved": true
    }
  ],
  "performance": {
    "feature_development": [
      {
        "execution_time": 320,
        "success_rate": 0.95,
        "timestamp": "2026-02-02T00:15:00"
      }
    ]
  }
}
```

---

## 🔄 自動優化流程 (Auto-Optimization Flow)

```
1. 執行工作流
   ↓
2. 記錄性能數據
   ↓
3. 檢測異常模式
   ↓
4. 生成改進建議
   ↓
5. 應用優化（可選）
   ↓
6. 驗證改進效果
```

---

## 📋 API 參考 (API Reference)

### record_error()
記錄錯誤以供學習。

**參數**:
- `error_type`: 錯誤類型
- `error_message`: 錯誤訊息
- `context`: 錯誤上下文
- `solution`: 解決方案（可選）

**返回**: 錯誤 ID

### suggest_improvement()
建議工作流改進。

**參數**:
- `workflow_name`: 工作流名稱
- `current_performance`: 當前性能指標

**返回**: 改進建議字典

### monitor_performance()
監控工作流性能。

**參數**:
- `workflow_name`: 工作流名稱
- `metrics`: 性能指標

**返回**: 監控結果

### generate_improvement_report()
生成改進報告。

**返回**: Markdown 格式報告

---

## 🎯 最佳實踐 (Best Practices)

1. **定期記錄**: 每次工作流執行後記錄性能數據
2. **分析模式**: 定期查看錯誤模式並應用建議
3. **驗證改進**: 應用優化後驗證效果
4. **持續學習**: 讓系統從每次執行中學習

---

## 🔗 相關文檔 (Related Documentation)

- [Workflow System](../../workflows/README.md)
- [Executor Agent](../executor_agent/AGENT.md)
- [Planner Agent](../planner_agent/AGENT.md)

---

**Created**: 2026-02-02  
**Version**: 1.0.0  
**Status**: Production Ready
