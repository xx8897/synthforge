"""
Knowledge Graph System
======================

Build and visualize relationships between rules, knowledge, and components.
構建並視覺化規則、知識和組件之間的關係。
"""

import json
from pathlib import Path
from typing import Dict, List, Set, Any, Optional
import re


class KnowledgeGraph:
    """Knowledge graph for rules and knowledge base."""
    
    def __init__(self, repo_path: str = "."):
        """
        Initialize knowledge graph.
        
        Args:
            repo_path: Path to repository
        """
        self.repo_path = Path(repo_path).resolve()
        self.nodes: Dict[str, Dict[str, Any]] = {}
        self.edges: List[Dict[str, str]] = []
    
    def build_from_rules(self) -> Dict[str, Any]:
        """
        Build graph from rules directory.
        從 rules 目錄構建圖譜。
        
        Returns:
            {
                'nodes': Dict[str, Dict],
                'edges': List[Dict],
                'stats': Dict
            }
        """
        rules_dir = self.repo_path / "rules"
        
        if not rules_dir.exists():
            return {'nodes': {}, 'edges': [], 'stats': {}}
        
        # Scan all rule files
        for rule_file in rules_dir.rglob("*.md"):
            if rule_file.name == "README.md":
                continue
            
            self._process_rule_file(rule_file)
        
        # Build statistics
        stats = {
            'total_nodes': len(self.nodes),
            'total_edges': len(self.edges),
            'categories': self._count_categories(),
            'most_connected': self._find_most_connected()
        }
        
        return {
            'nodes': self.nodes,
            'edges': self.edges,
            'stats': stats
        }
    
    def build_from_knowledge(self) -> Dict[str, Any]:
        """
        Build graph from knowledge base.
        從知識庫構建圖譜。
        
        Returns:
            Knowledge graph data
        """
        knowledge_dir = self.repo_path / ".internal" / "knowledge"
        
        if not knowledge_dir.exists():
            return {'nodes': {}, 'edges': [], 'stats': {}}
        
        # Scan knowledge files
        for knowledge_file in knowledge_dir.rglob("*.md"):
            if knowledge_file.name == "README.md":
                continue
            
            self._process_knowledge_file(knowledge_file)
        
        stats = {
            'total_nodes': len(self.nodes),
            'total_edges': len(self.edges),
            'categories': self._count_categories()
        }
        
        return {
            'nodes': self.nodes,
            'edges': self.edges,
            'stats': stats
        }
    
    def visualize_mermaid(self) -> str:
        """
        Generate Mermaid diagram.
        生成 Mermaid 圖表。
        
        Returns:
            Mermaid diagram string
        """
        lines = ["graph TD"]
        
        # Add nodes
        for node_id, node_data in self.nodes.items():
            label = node_data.get('name', node_id)
            category = node_data.get('category', 'other')
            
            # Style based on category
            if category == 'core':
                lines.append(f'    {node_id}["{label}"]:::core')
            elif category == 'development':
                lines.append(f'    {node_id}["{label}"]:::dev')
            elif category == 'management':
                lines.append(f'    {node_id}["{label}"]:::mgmt')
            else:
                lines.append(f'    {node_id}["{label}"]')
        
        # Add edges
        for edge in self.edges:
            source = edge['source']
            target = edge['target']
            relation = edge.get('type', 'relates_to')
            
            if relation == 'depends_on':
                lines.append(f'    {source} -->|depends on| {target}')
            elif relation == 'related_to':
                lines.append(f'    {source} -.->|related| {target}')
            else:
                lines.append(f'    {source} --> {target}')
        
        # Add styles
        lines.append("")
        lines.append("    classDef core fill:#f96,stroke:#333,stroke-width:2px")
        lines.append("    classDef dev fill:#9cf,stroke:#333,stroke-width:2px")
        lines.append("    classDef mgmt fill:#9f9,stroke:#333,stroke-width:2px")
        
        return "\n".join(lines)
    
    def export_json(self, output_file: str) -> bool:
        """
        Export graph to JSON.
        導出圖譜為 JSON。
        
        Args:
            output_file: Output file path
            
        Returns:
            Success status
        """
        try:
            data = {
                'nodes': self.nodes,
                'edges': self.edges,
                'stats': {
                    'total_nodes': len(self.nodes),
                    'total_edges': len(self.edges)
                }
            }
            
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            return True
        except Exception:
            return False
    
    def _process_rule_file(self, file_path: Path):
        """Process a rule file and extract relationships."""
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Extract rule name
            rule_name = file_path.stem
            
            # Determine category
            category = 'other'
            if 'core' in str(file_path):
                category = 'core'
            elif 'development' in str(file_path):
                category = 'development'
            elif 'management' in str(file_path):
                category = 'management'
            
            # Add node
            node_id = f"rule_{rule_name}"
            self.nodes[node_id] = {
                'id': node_id,
                'name': rule_name,
                'type': 'rule',
                'category': category,
                'path': str(file_path.relative_to(self.repo_path))
            }
            
            # Extract related rules
            related_pattern = r'related_rules:\s*\n((?:\s+-\s+.+\n?)+)'
            related_match = re.search(related_pattern, content)
            
            if related_match:
                related_text = related_match.group(1)
                related_rules = re.findall(r'-\s+(.+)', related_text)
                
                for related in related_rules:
                    related = related.strip()
                    if related and not related.startswith('('):
                        target_id = f"rule_{related}"
                        self.edges.append({
                            'source': node_id,
                            'target': target_id,
                            'type': 'related_to'
                        })
        
        except Exception:
            pass
    
    def _process_knowledge_file(self, file_path: Path):
        """Process a knowledge file."""
        try:
            rule_name = file_path.stem
            
            # Determine category
            category = 'concepts'
            if 'tools' in str(file_path):
                category = 'tools'
            elif 'references' in str(file_path):
                category = 'references'
            
            # Add node
            node_id = f"knowledge_{rule_name}"
            self.nodes[node_id] = {
                'id': node_id,
                'name': rule_name,
                'type': 'knowledge',
                'category': category,
                'path': str(file_path.relative_to(self.repo_path))
            }
        
        except Exception:
            pass
    
    def _count_categories(self) -> Dict[str, int]:
        """Count nodes by category."""
        categories: Dict[str, int] = {}
        for node in self.nodes.values():
            category = node.get('category', 'other')
            categories[category] = categories.get(category, 0) + 1
        return categories
    
    def _find_most_connected(self, top_n: int = 5) -> List[Dict[str, Any]]:
        """Find most connected nodes."""
        connections: Dict[str, int] = {}
        
        for edge in self.edges:
            source = edge['source']
            target = edge['target']
            connections[source] = connections.get(source, 0) + 1
            connections[target] = connections.get(target, 0) + 1
        
        # Sort by connection count
        sorted_nodes = sorted(
            connections.items(),
            key=lambda x: x[1],
            reverse=True
        )[:top_n]
        
        return [
            {
                'node_id': node_id,
                'connections': count,
                'name': self.nodes.get(node_id, {}).get('name', node_id)
            }
            for node_id, count in sorted_nodes
        ]


def analyze_knowledge_relationships(repo_path: str = ".") -> Dict[str, Any]:
    """
    Analyze relationships in knowledge base.
    分析知識庫中的關係。
    
    Args:
        repo_path: Repository path
        
    Returns:
        Analysis results
    """
    graph = KnowledgeGraph(repo_path)
    
    # Build from both rules and knowledge
    rules_data = graph.build_from_rules()
    knowledge_data = graph.build_from_knowledge()
    
    return {
        'rules': rules_data,
        'knowledge': knowledge_data,
        'combined_stats': {
            'total_nodes': len(graph.nodes),
            'total_edges': len(graph.edges)
        }
    }


def generate_knowledge_map(
    repo_path: str = ".",
    output_file: str = ".internal/knowledge/knowledge_map.md"
) -> bool:
    """
    Generate knowledge map document.
    生成知識地圖文檔。
    
    Args:
        repo_path: Repository path
        output_file: Output file path
        
    Returns:
        Success status
    """
    graph = KnowledgeGraph(repo_path)
    graph.build_from_rules()
    graph.build_from_knowledge()
    
    # Generate Mermaid diagram
    mermaid = graph.visualize_mermaid()
    
    # Create markdown document
    content = f"""# Knowledge Map

**知識地圖**

自動生成的規則與知識關聯圖譜。

---

## 📊 統計

- **總節點數**: {len(graph.nodes)}
- **總連接數**: {len(graph.edges)}

---

## 🗺️ 關聯圖

```mermaid
{mermaid}
```

---

**生成時間**: {Path(output_file).stat().st_mtime if Path(output_file).exists() else 'N/A'}
"""
    
    try:
        output_path = Path(repo_path) / output_file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding='utf-8')
        return True
    except Exception:
        return False
