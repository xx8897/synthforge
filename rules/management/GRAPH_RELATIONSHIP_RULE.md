# GRAPH_RELATIONSHIP_RULE - Documentation of Knowledge Links
# GRAPH_RELATIONSHIP_RULE - 知識鏈結文件化庫

**Status**: STABLE  
**Priority**: MEDIUM (6/10)  
**Version**: 1.0  

---

## 🎯 Purpose / 目的

Ensure all rules, components, and task documents contain machine-readable metadata that allows the `KnowledgeGraph` engine to build a complete relationship tree/graph.

確保所有規則、組件和任務文檔都包含機器可讀的元數據，使 `KnowledgeGraph` 引擎能夠構建完整的關係樹/圖。

---

## 📋 Relationship Standards / 關係標準

### 1. Metadata Keys / 元數據鍵
Every significant document SHOULD include a `Relationships` or `Meta` section (or YAML frontmatter) with the following keys:

- `depends_on`: List of documents or components required for this item to function.
- `related_to`: List of relevant items that provide context.
- `implements`: (For code) Which rules or requirements this code satisfies.

### 2. Formatting / 格式設定

#### In Markdown Headers (Preferred) / 在 Markdown 標題中（首選）
```markdown
---
relationships:
  - depends_on: rule_core_standard
  - related_to: docs_architecture
---
```

#### In Markdown Sections / 在 Markdown 節點中
```markdown
### 🔗 Relationships
- **Depends on**: [CORE_RULE](rules/core/CORE_RULE.md)
- **Related to**: [ARCHITECTURE](docs/architecture/ARCHITECTURE.md)
```

---

## 🧭 Graph Visualization / 圖譜視覺化

The `KnowledgeGraph` engine analyzes these links to generate:

1.  **Tree View**: Hierarchical dependency (Primary for Rules).
2.  **Network Graph**: Lateral relationships (Primary for Features/Agents).

---

## 🛠️ Usage / 使用方式

To update the map after adding relationships:
```bash
python devtools/cli.py graph build
```

---

**Last Updated**: 2026-02-02  
**Maintainer**: xx8897
