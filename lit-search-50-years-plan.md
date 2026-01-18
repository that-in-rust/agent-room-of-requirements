# Project LIT-SEARCH: 50 Years of CS/Math → Rust Library PMF Analysis

> *"A systematic plan to mine academic research for high-PMF Rust library opportunities"*

**Date:** January 18, 2026
**Scale:** ~14.5 million papers (1975-2025)
**Method:** Claude Code Agent Workforce
**Objective:** Identify high-PMF Rust libraries from academic research

---

## Executive Summary

This plan outlines how to systematically analyze 50 years of Computer Science and Mathematics research papers to identify opportunities for Rust libraries with high Product-Market Fit (PMF).

**The Challenge:** 14.5 million papers is too many to analyze manually.

**The Solution:** A multi-stage filtering pipeline that reduces the corpus to ~25,000 high-potential papers, then uses Claude Code agents for PMF evaluation.

---

## Part I: Data Sources (How to Get the Papers)

### Recommended Sources (Ranked)

| Source | Coverage | Cost | Rate Limit | Best For |
|--------|----------|------|------------|----------|
| **OpenAlex** | 474M papers | FREE | 50 req/sec | **Primary choice** |
| **Semantic Scholar** | 228M papers | FREE | 100 req/sec | Citation data |
| **DBLP** | 8.4M CS papers | FREE | N/A (bulk) | Historical CS |
| **arXiv** | 2.4M papers | FREE | 1 req/sec | Recent CS |
| **CORE** | OA full-texts | FREE | Varies | Full-text access |

### Quick Start Commands

```bash
# OpenAlex API (free, no auth required)
curl "https://api.openalex.org/works?filter=publication_year:2020-2025,concepts.id:C154945302"

# Semantic Scholar API (free with key)
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=rotary+positional+embedding"

# DBLP dump (historical CS)
wget https://dblp.org/rdf/dblp.rdf.gz
```

### Estimated Corpus Size

| Era | Papers | Notes |
|-----|---------|-------|
| 1975-1990 | ~500K | Pre-arXiv, digitized archives |
| 1991-2000 | ~1M | arXiv founded (1991) |
| 2001-2010 | ~3M | Dot-com era, ML boom |
| 2011-2020 | ~6M | Deep learning revolution |
| 2021-2025 | ~4M | Accelerated publishing |
| **TOTAL** | **~14.5M** | CS + Math |

---

## Part II: The Filtering Pipeline (Reducing 14.5M → 25K)

```
14.5M Raw Papers
    ↓ Stage 1: Language + Field Filter
5M CS/Math English Papers
    ↓ Stage 2: Citation Count Filter
500K Well-Cited Papers (>10 citations)
    ↓ Stage 3: Recency + Impact Filter
100K High-Potential Papers
    ↓ Stage 4: Keyword/Topic Filter
25K Relevant Papers
    ↓ Stage 5: Claude Code Agent Analysis
5-10K PMF-Scored Opportunities
```

### Filter Stage Details

**Stage 1: Language + Field**
- Keep: CS, Math, Engineering
- Exclude: Non-English, duplicates
- Result: 14.5M → 5M

**Stage 2: Citation Thresholds**
```
1975-1985: >50 citations
1986-1995: >30 citations
1996-2005: >20 citations
2006-2015: >10 citations
2016-2020: >5 citations
2021-2025: >1 citation
```
- Result: 5M → 500K

**Stage 3: Impact Score**
```
Score = log10(citations) × 0.3 + recency × 0.7
Keep: Score > 0.5
```
- Result: 500K → 100K

**Stage 4: Keywords**
```
Primary: algorithm, data structure, distributed, cryptography,
         compiler, database, neural, inference, optimization
Negative: psychology, sociology (using CS methods)
```
- Result: 100K → 25K

---

## Part III: Agent Processing Strategy

### Agent Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                  Orchestration Service (Rust)                 │
│         - Rate limiting, job queue, result aggregation       │
└──────────────────────┬──────────────────────────────────────┘
                       │
       ┌───────────────┼───────────────┐
       │               │               │
       ▼               ▼               ▼
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ Filter Agent│ │Analysis Agent│ │ PMF Agent   │
│  (Haiku)    │ │  (Sonnet)    │ │  (Opus)     │
│  Fast triage│ │  Deep read   │ │  Scoring    │
└─────────────┘ └─────────────┘ └─────────────┘
```

### Processing Costs (Estimated)

| Stage | Papers | Agent | Tokens/Paper | Total Tokens | Cost |
|-------|--------|-------|--------------|--------------|------|
| Filter | 25K | Haiku | 500 | 12.5M | ~$3 |
| Analysis | 5K | Sonnet | 3,000 | 15M | ~$45 |
| PMF Score | 5K | Opus | 1,000 | 5M | ~$75 |
| **TOTAL** | - | - | - | **32.5M** | **~$123** |

### Agent Output Format

```json
{
  "paper_id": "openalex:W123456789",
  "title": "Novel Algorithm for X",
  "year": 2023,
  "citations": 127,
  "pmf_score": 87,
  "breakdown": {
    "feasibility": 9,
    "demand": 8,
    "rust_advantage": 9,
    "competition": 2
  },
  "recommendation": "build",
  "suggested_crate": "algo-x",
  "mvp_features": ["core algorithm", "benchmarks", "Python bindings"],
  "competing_crates": [],
  "estimated_weeks": 4
}
```

---

## Part IV: PMF Scoring Rubric

### The Formula

```
PMF = (Feasibility × Demand × Rust_Advantage) / (Competition + 1)

All inputs 1-10, except Competition (1-5 divisor)
Final score: 1-100
```

### Scoring Guide

#### Feasibility (1-10)
- **10:** Pure Rust, well-defined algorithm
- **8:** Rust + FFI bindings
- **6:** Some research needed
- **4:** Significant unknowns
- **1-2:** Requires breakthrough

#### Demand (1-10)
- **10:** Universal algorithm (sorting, hashing)
- **8:** Important niche
- **6:** Growing field
- **4:** Small stable market
- **1-3:** Very niche

#### Rust Advantage (1-10)
- **10:** Critical for systems/crypto (safety + performance)
- **8:** Significant benefits
- **6:** Competitive
- **4:** Same as others
- **1-3:** Rust disadvantaged

#### Competition Penalty (1-5)
- **5:** No competition (best)
- **4:** Green field
- **3:** Non-Rust exists
- **2:** One Rust crate
- **1:** Crowded Rust market

### Score Interpretation

| PMF Range | Meaning | Action |
|-----------|---------|--------|
| 90-100 | Must Build | Start immediately |
| 75-89 | High Priority | Plan for next sprint |
| 60-74 | Consider | Backlog for later |
| < 60 | Pass | Skip |

---

## Part V: Implementation Roadmap

### Phase 1: Proof of Concept (Week 1)

**Goal:** Validate approach on 1,000 papers

- [ ] Set up OpenAlex API access
- [ ] Create PostgreSQL schema
- [ ] Implement filter logic
- [ ] Test agent analysis on 100 papers
- [ ] Validate scores against human expert

**Go/No-Go:** Agent-human agreement > 70%

### Phase 2: Pipeline Build (Week 2)

- [ ] Build orchestration service (Rust)
- [ ] Implement multi-stage filtering
- [ ] Create agent prompt templates
- [ ] Set up parallel processing
- [ ] Build result aggregation

### Phase 3: Full Processing (Week 3-4)

- [ ] Download full corpus metadata
- [ ] Run filtering pipeline
- [ ] Process ~25K papers through agents
- [ ] Generate opportunity database

### Phase 4: Output & Validation (Week 5-6)

- [ ] Human review of top 100
- [ ] Create ranked report
- [ ] Build dashboard
- [ ] Publish findings

---

## Part VI: Infrastructure Requirements

### Storage Costs

| Data | Size | Monthly Cost |
|------|------|--------------|
| Metadata only | ~50 GB | ~$1 |
| + Citation graph | ~200 GB | ~$5 |
| + Full-text (selective) | ~500 GB | ~$12 |

### Compute Requirements

```
Recommended:
- 4 vCPU orchestration server
- 16 GB RAM
- 100 GB SSD
- 1 TB S3 storage

Estimated cost: ~$50/month (AWS/Lightsail equivalent)
```

### Timeline (Parallel Processing)

| Phase | Duration |
|-------|----------|
| Data download | 1-2 days |
| Filtering | 1-2 hours |
| Agent analysis | 4-8 hours |
| Total | **~1 week** |

---

## Part VII: Key APIs and Tools

### OpenAlex (Primary)

```bash
# Base URL
https://api.openalex.org

# Example: Get recent CS papers
https://api.openalex.org/works?filter=publication_year:2020-2025,concepts.id:C154945302&per-page=200

# Example: Search by keyword
https://api.openalex.org/works?search=search+algorithm

# No API key required (polite pool: 50 req/sec)
```

### Semantic Scholar (Citations)

```bash
# Base URL
https://api.semanticscholar.org

# Get paper details with citations
https://api.semanticscholar.org/paper/ARXIV:2301.10140

# API key recommended (free)
```

### DBLP (Historical CS)

```bash
# RDF dump (one-time download)
wget https://dblp.org/rdf/dblp.rdf.gz
gunzip dblp.rdf

# Or query API
https://dblp.org/search?q=author%3ATuring
```

---

## Part VIII: Risk Mitigation

### Risk 1: API Rate Limits

**Mitigation:**
- Use OpenAlex (50 req/sec, free)
- Batch requests where possible
- Implement exponential backoff
- Cache all responses

### Risk 2: High API Costs

**Mitigation:**
- Aggressive filtering before agents
- Use Haiku for initial triage (cheapest)
- Set budget caps per stage
- Monitor token usage in real-time

### Risk 3: False Positives

**Mitigation:**
- Multi-agent voting (3 agents per paper)
- Human validation of top 100
- Confidence scoring by agents
- Calibration against known examples

### Risk 4: Copyright Issues

**Mitigation:**
- Use metadata-only (abstracts are fair use)
- Prioritize open access sources
- Don't redistribute full text
- Transformative analysis (legal)

---

## Part IX: Success Metrics

| Metric | Target |
|--------|--------|
| Papers analyzed | > 100K fully scored |
| High-PMF opportunities | > 100 (PMF > 75) |
| Cost per paper | < $0.05 |
| Processing time | < 1 week |
| Agent-human agreement | > 70% |

### Ultimate Success

**Libraries Built:** Number of high-PMF opportunities that result in published Rust crates within 6-12 months.

---

## Part X: Quick Start Commands

```bash
# 1. Clone the project template
git clone https://github.com/your-org/lit-search
cd lit-search

# 2. Set up environment
cp .env.example .env
# Edit .env with your API keys

# 3. Run database migrations
psql $DATABASE_URL < schema.sql

# 4. Start ingestion
cargo run --bin ingest -- --years 1975-2025 --fields cs,math

# 5. Run filtering
cargo run --bin filter -- --citations 10 --keywords algorithm,database

# 6. Run agents
cargo run --bin agents -- --parallel 50 --budget 200

# 7. Generate report
cargo run --bin report -- --format markdown --output rust-opportunities.md
```

---

## References

### Data Sources
- [OpenAlex](https://openalex.org/) - Free open scholarly catalog
- [OpenAlex API Docs](https://docs.openalex.org/) - Technical documentation
- [Semantic Scholar API](https://www.semanticscholar.org/product/api) - Citation data
- [DBLP](https://dblp.org/) - Computer science bibliography
- [DBLP Download](https://dblp.org/faq/How+can+I+download+the+whole+dblp+dataset) - Bulk data access

### Tools
- [Anthropic Claude API](https://platform.claude.com/docs/en/api/rate-limits) - Rate limits
- [GROBID](https://grobid.readthedocs.io/) - PDF parsing
- [PostgreSQL](https://www.postgresql.org/) - Metadata storage
- [Qdrant](https://qdrant.tech/) - Vector embeddings

### Cost References
- [AWS S3 Pricing](https://aws.amazon.com/s3/pricing/) - Storage costs
- [Claude Pricing](https://www.anthropic.com/pricing) - API costs

---

**Status:** PLANNING COMPLETE - Ready for implementation

**Next Step:** Run 1,000 paper proof-of-concept to validate approach
