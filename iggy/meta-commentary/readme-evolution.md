# README Evolution: From AI-Generated to Engineer-Approved

The sink README went through 5 versions in one session. This documents
what changed and why at each step — the actual feedback loop.

---

## v1: The Kitchen Sink (284 lines)

Sections: Overview, Quick Start, Configuration, Payload Formats, Metadata
Fields, Error Handling & Retries, Offset Tracking, Testing, Verify It Works.

**What was wrong:** Every AI tell was present. Exhaustive documentation of
features nobody asked about. "Payload Formats" section explaining JSON vs
BSON vs string with examples. "Offset Tracking" section explaining
`tracking_field` with diagrams. The README was trying to be a user manual
for a connector that doesn't have users yet.

**The tell:** No other connector README in the repo had more than 3 sections.
We had 9.

---

## v2: Trimmed but Still Too Much (106 lines)

Removed Offset Tracking and Error Handling sections. Kept Payload Formats
and Verify It Works.

**What was wrong:** "Verify It Works" was fake — it told you to build the
project, then run a separate command. The testcontainers E2E tests spin up
their OWN MongoDB, so pointing users at a manual `docker run` was
meaningless theater. Payload Formats section duplicated information already
in the config table.

---

## v3: Over-Corrected (20 lines)

Tried to match the repo's minimalist convention. Stdout sink is 13 lines.
Random source is 19 lines.

**What was wrong:** "Think more what is our context." Those connectors have
zero configuration. MongoDB has 13 config options (sink) and 17 (source).
Without the config table, the README is useless. There's no external docs
site to link to.

**The lesson:** Convention matching without context is cargo-culting. Match
the WHY, not the WHAT. Stdout doesn't need a config table because it has
no config. We do.

---

## v4: Right-Sized (60+70 lines)

Three sections: Quick Start, Configuration, Testing.

**What changed:**

- Config table preserved (it's the documentation)
- Testing section lists E2E test names (reviewer sees coverage at a glance)
- No "Features" section (the config table IS the feature list)
- No "Verify It Works" section (the E2E tests ARE the verification)

**External validation:** Kafka MongoDB Connector's README is 84 lines with
zero config docs. But they have <https://docs.confluent.io> with 50+ pages
of documentation. We don't. The README must be self-sufficient.

---

## v5: Added "Try It" (131+137 lines)

New first section: "Try It" — full interactive test with copy-paste commands.

**Why this was added last:** It wasn't obvious that we needed it. The E2E
tests already prove correctness. But the Elasticsearch PR saga showed what
happens when a reviewer can't quickly verify: 5 months of "I'll fix it
this week." The interactive test lets a reviewer see the data flow in 60
seconds without reading the implementation.

**Design of the Try It section:**

- Self-contained: creates its own config via heredocs (no editing tracked files)
- Shows expected output: reviewer knows what success looks like before running
- Includes cleanup command: no leftover Docker containers or temp files
- Sink shows: Iggy CLI message -> connector -> MongoDB document
- Source shows: MongoDB document -> connector -> Iggy message

---

## The Reference Points

| Reference | Lines | What it taught us |
|-----------|-------|-------------------|
| stdout_sink README | 13 | Minimal is fine when there's nothing to configure |
| postgres_source README | 375 | Long is fine when there's complexity to document |
| elasticsearch_source README | 276 | Config tables are the core value |
| Kafka MongoDB Connector | 84 | External docs site changes everything |
| Debezium MongoDB docs | 2000+ | Separate docs site, README is just a pointer |

**The meta-lesson:** README length is not a style choice. It's a function of
(config complexity) * (1 / external docs availability). We have high config
complexity and zero external docs. The README must carry the full weight.

---

## What "Best Engineers" Actually Do

The user kept asking "what would the best engineers say?" Here's what we
learned by studying real examples:

1. **They don't write feature lists.** The config table IS the feature list.
   If a feature isn't in the config, it doesn't need documenting.

2. **They show, don't tell.** "Try It" with expected output > "Features"
   section with bullet points.

3. **They name their tests well.** `given_io_timeout_error_should_be_transient`
   is documentation. Listing test names in the README is free docs.

4. **They match the codebase convention, then add ONE thing.** Our ONE thing
   is the interactive test section. Everything else matches the repo pattern.
