---
title: "synthforge 全貌"
subtitle: "AI 驅動開發環境的實驗性專案"
document_type: overview
version: 1.0
language: zh-TW
related_concepts:
  - skills
  - agents
  - workflow_engine
  - rules_system
related_documents:
  - 01_PHILOSOPHY.md
  - 02_ARCHITECTURE.md
  - 07_STRENGTHS_AND_GAPS.md
tags: [overview, entry-point, synthforge]
---

# synthforge 全貌

> 這是 skills 概念剛出來時的試驗場。有些想法長成了骨架，有些停在 placeholder，有些在碰撞中改變了方向。這些文件記錄的不是成品，而是過程。

## 一句話定位

**synthforge** 是一個規則治理優先、工作流驅動的 AI 開發環境——嘗試用治理框架和工作流引擎，讓 AI 代理在開發流程中可預測、可追溯、可改進地運作。

## 為什麼存在

2026 年初，AI coding assistant 的 skills 概念剛浮出水面。所有人都興奮地想把 AI 塞進開發流程，但很少有人回答一個根本問題：

> **AI 代理在專案裡該守什麼規矩？**

synthforge 的回答是：先建規則，再寫代碼。先定治理，再做工具。先用工作流編排行為，再讓代理自主行動。

這個回答有對的部分，也有過度的部分。這些文件就是來拆解這一切的。

## 核心構成

| 模組 | 作用 | 狀態 |
|------|------|------|
| **rules/** | 22 條治理規則，分 core / development / management 三層 | ✅ 完備 |
| **skills/** | 5 個無狀態可重用能力（spec_parser, task_generator 等） | ✅ 大部分完成 |
| **agents/** | 4 個有狀態 AI 代理（Planner, Executor, Reviewer, Self-Improvement） | ⚠️ 骨架到位，實作為 placeholder |
| **workflows/** | YAML 宣告式工作流引擎（Parser + Validator + Executor + Context） | ⚠️ Engine v1 完成，Executor 為 placeholder |
| **core_lib/** | 共享基礎設施（utils, git 自動化） | ⚠️ utils 完成，git 模組引用但未見實作 |
| **devtools/** | CLI 入口 + 知識圖譜 + 結構優化器 | ✅ 大部分完成 |

## 讀法建議

```
你想了解什麼？          → 去哪裡
─────────────────────────────────────
整體設計思想           → 01_PHILOSOPHY.md
模組怎麼串             → 02_ARCHITECTURE.md
規則體系的邏輯         → 03_RULES_SYSTEM.md
技能 vs 代理的界線     → 04_SKILLS_AND_AGENTS.md
工作流引擎怎麼跑       → 05_WORKFLOW_ENGINE.md
工具有哪些             → 06_DEVTOOLS.md
這專案強在哪、弱在哪   → 07_STRENGTHS_AND_GAPS.md
怎麼走到今天的         → 08_BUILDING_JOURNEY.md
帶走什麼經驗           → 09_LESSONS.md
```

## 幾個關鍵數字

- **22** 條治理規則
- **4** 個 AI 代理
- **5** 個技能
- **4** 個內建工作流模板
- **7** 大 CLI 命令群
- **4** 個建構階段（Phase 1-3 完成，Phase 4 30%）
- **0** 個完整落地的代理實作

最後一個數字是最誠實的——骨架很漂亮，但 executor 是 placeholder，代理的核心方法裡寫著 `pass`。這不是缺點，這是這個實驗的真相：**設計走在了實作前面，而且走得很遠。**

## 授權

Dual License：AGPL-3.0（非商業免費）+ Commercial License（商業需授權）。详见 [LICENSE](../LICENSE)。