---
description: Step-by-step procedure for enriching a single ticker report. Quality rules are defined in CLAUDE.md (project root).
---

# Enrich Ticker — Procedure

> **All quality standards (wikilink rules, metadata requirements, formatting) are defined in `CLAUDE.md`.**
> This document is the step-by-step procedure only.

## Prerequisites
- Target file must exist in `Pilot_Reports/{Industry}/{Ticker}_{Name}.md`
- If missing, generate first: `python "f:\My TW Coverage\02_generate_base_reports.py" --ticker <TICKER> --name "<NAME>"`

## Steps

### 1. Read the Target File
- Note existing metadata: `板塊`, `產業`, `市值`, `企業價值`
- Note financial tables — these must be preserved exactly

### 2. Research the Company
Search deeply using multiple queries:
- `[Ticker] 法說會` — investor conference
- `[Ticker] 年報 主要客戶` — annual report customers
- `[Ticker] 供應商 供應鏈` — supply chain
- `[Company Name] supplier customer` — English sources
- Company IR pages, MOPS filings

**Find specific proper nouns** — company names, product names, technology names. Generic descriptions are only allowed as plain-text context labels, never as `[[wikilinks]]`. See `CLAUDE.md` Golden Rule #1.

### 3. Enrich the Report

**業務簡介**: Replace English with professional Traditional Chinese. Add `[[wikilinks]]` for every key entity and technology.

**供應鏈位置**: Segment by business line or category with 上游/中游/下游 structure. Use plain-text context labels before specific wikilinked names:
```
**上游 (原料):**
- **晶圓代工:** [[台積電]], [[聯電]]
```

**主要客戶及供應商**: Break down by segment. Use exact company names:
```
### 主要客戶
- **AI 伺服器:** [[NVIDIA]], [[Supermicro]]
### 主要供應商
- **封裝基板:** 基板廠如 [[欣興]], [[南亞電路板]]
```

**財務概況**: DO NOT TOUCH.

### 4. Verify
- Run audit: `python .agent/workflows/audit_batch.py <batch> -v`
- Confirm ticker shows CLEAN
- If not, fix flagged issues and re-audit

## Batch Mode
For batch enrichment, use the DATA dict in `fix_batch.py` instead of editing files one by one. See `workflow_documentation.md` for the batch procedure.
