# Batch Enrichment — Operational Procedure

> **All quality rules live in `CLAUDE.md`** (project root). This document covers only the operational procedure.

---

## 1. Audit — Identify Work

```bash
python .agent/workflows/audit_batch.py <batch_num> -v
```

Output categories:
- **CLEAN** — passes all quality checks
- **NEEDS ENRICHMENT** — unenriched base file (English text, placeholders, or too short)
- **NEEDS QUALITY FIX** — enriched but fails quality checks (generic wikilinks, thin sections, etc.)
- **MISSING** — no file found

To audit all previously completed batches:
```bash
python .agent/workflows/audit_batch.py --all -v
```

---

## 2. Research — Deep Search Per Ticker

For each ticker needing work, search using:
- `[Ticker] 法說會` — investor conference transcripts
- `[Ticker] 年報 主要客戶` — annual report customer disclosures
- `[Ticker] 供應商 供應鏈` — supply chain information
- `[Company Name] supplier customer` — English-language sources
- Company IR pages, MOPS filings, industry reports

**Quality bar**: every wikilink must be a specific proper noun. See `CLAUDE.md` Golden Rule #1.

---

## 3. Prepare — Format DATA Dictionary

Format research into the `DATA` dict in `.agent/workflows/fix_batch.py`:

```python
DATA = {
    "XXXX": {
        "desc": "Traditional Chinese business description with [[specific wikilinks]]...",
        "up": "原料供應商如 [[Company A]], [[Company B]].",
        "mid": "**公司名** (core business description).",
        "down": "終端客戶如 [[Customer X]], [[Customer Y]].",
        "cust": "**業務分類:** [[Customer 1]], [[Customer 2]].",
        "supp": "**業務分類:** [[Supplier 1]], [[Supplier 2]]."
    },
}
```

---

## 4. Execute & Verify

```bash
# Apply enrichment
python .agent/workflows/fix_batch.py

# Verify — all tickers should show CLEAN
python .agent/workflows/audit_batch.py <batch_num> -v
```

---

## 5. Mark Complete

Update `task.md`: change `[ ]` to `[x]` for the batch.

---

## Execution Rules

- Process in groups of **10 tickers** per research-inject-verify cycle
- **7-command pattern** per 30-ticker batch: 1 audit + 3 loops of (inject DATA + run script)
- All data injection via `fix_batch.py` DATA dict — **no temporary scripts**
- After entire batch is verified CLEAN, notify user
- Only ask for user input when a major blocker is found
