# synthforge Documentation

**Purpose**: Comprehensive documentation for synthforge  
**Last Updated**: 2026-02-01

---

## 📁 Structure / 結構

```
docs/
├── README.md (this file)
├── architecture/        → System design and decisions
├── guides/              → User guides and tutorials
```

---

## 🎯 Documentation Categories / 文件類別

### 1. Architecture Documentation (architecture/)
**Purpose**: Technical design, system architecture, and design decisions  
**用途**: 技術設計、系統架構和設計決策

**Key Files**:
- [ARCHITECTURE.md](architecture/ARCHITECTURE.md) - Complete system architecture
- [DESIGN_DECISIONS.md](architecture/DESIGN_DECISIONS.md) - Design decision records
- [ROADMAP.md](architecture/ROADMAP.md) - Feature roadmap
- [GIT_STRATEGY.md](architecture/GIT_STRATEGY.md) - Git and GitHub strategy

---

### 2. User Guides (guides/)
**Purpose**: How-to guides, tutorials, and reference documentation  
**用途**: 操作指南、教學和參考文件

**Key Files**:
- [QUICKSTART.md](guides/QUICKSTART.md) - Quick start guide
- [AGENT_RULES.md](guides/AGENT_RULES.md) - AI agent behavior rules
- [DOC_GUIDE.md](guides/DOC_GUIDE.md) - Documentation standards
- [SKILLS_VS_RULES.md](guides/SKILLS_VS_RULES.md) - Skills vs Rules concepts

---

## 🔗 Navigation / 導航

**From VIBE_GUIDE**:
```
VIBE_GUIDE.md
    ↓ [STRONG]
docs/architecture/ARCHITECTURE.md  ← System design
docs/guides/AGENT_RULES.md         ← AI behavior
```

**Within docs/**:
```
docs/README.md (you are here)
    ↓ [WEAK]
architecture/README.md → All architecture docs
guides/README.md       → All guide docs
```

---

## 📝 Document Types / 文件類型

| Type | Location | Naming | Example |
|------|----------|--------|---------|
| Architecture | `architecture/` | `[TOPIC].md` | `ARCHITECTURE.md` |
| Guides | `guides/` | `[TOPIC].md` or `[TOPIC]_GUIDE.md` | `QUICKSTART.md` |

---

## ✅ Documentation Principles / 文件原則

1. **SSOT (Single Source of Truth)**
   - Each piece of information exists in ONE place
   - Other documents reference, not duplicate

2. **Bilingual**
   - All documentation in English and Traditional Chinese
   - Follow BILINGUAL_OUTPUT_RULE.md

3. **Up-to-date**
   - Update documentation with code changes
   - Mark last updated date

4. **Discoverable**
   - Clear hierarchy from VIBE_GUIDE
   - README in every directory

---

**Created**: 2026-02-01  
**Last Updated**: 2026-02-01  
**Maintainer**: synthforge team
