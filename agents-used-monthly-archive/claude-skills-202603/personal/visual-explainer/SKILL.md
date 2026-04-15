---
name: visual-explainer
description: Use when someone asks to understand, explain, or document how a part of the codebase works and wants a visual or ELI5 output - generates an interactive scrollable HTML explainer with metaphors, diagrams, and progressive disclosure
---

# Visual Explainer

Generate an elegant, interactive HTML page that explains how a part of the codebase works — using progressive disclosure, metaphors, and visual storytelling inspired by [How LLMs Work](https://paraschopra.github.io/how-llms-work/).

## When to Use

- User asks "explain how X works" or "help me understand Y"
- User asks for an ELI5 or visual explainer of codebase concepts
- User wants to onboard someone on a subsystem
- User asks for documentation that's "not boring"

## Process

### 1. Deep Exploration

Launch Explore agents to thoroughly understand the target code:
- Key structs, traits, functions, and their relationships
- Data flow (input → processing → output)
- Configuration options
- Error handling patterns
- File paths and line numbers for all critical code

**You must understand the code deeply before writing a single word of explanation.**

### 2. Narrative Architecture

Structure as **5-8 Acts** that build progressively:

| Act Position | Purpose | Example |
|---|---|---|
| Act I | The Mystery — what problem does this solve? | "You have data at rest. You need it in motion." |
| Act II-III | Core mechanics — one concept per act | Polling loop, CDC, query building |
| Mid acts | Comparisons — side-by-side when 2+ things | PostgreSQL vs MongoDB approaches |
| Later acts | Safety/resilience — error handling, retries | Commit/discard protocol |
| Final act | Architecture — how it all fits together | Plugin system, traits, big picture table |

### 3. Pedagogical Techniques

Apply ALL of these:

**Metaphors first, code second.** Every technical concept gets a relatable metaphor before any code appears:
- Polling → "postal worker checking the mailbox"
- CDC → "microphone in the database room vs checking the mailbox"
- Plugin system → "USB devices: plug in, recognized, ready"
- Retry logic → "bank transaction: money only moves if both sides agree"

**One concept per section.** Never introduce two new ideas simultaneously.

**Concrete → Abstract.** Start with `SELECT * FROM users WHERE id > 42` before explaining the generic tracking offset pattern.

**Visual variety.** Alternate between:
- Metaphor cards (icon + title + explanation)
- Step-by-step flows (numbered with connecting lines)
- Side-by-side comparison cards (color-coded)
- ASCII diagrams in monospace blocks
- Syntax-highlighted code blocks
- Insight callout boxes for key takeaways
- Comparison tables for the big picture
- Animated flow diagrams (CSS-only pulsing arrows)

### 4. Generate HTML

Use the template at `~/.claude/skills/visual-explainer/template.html` as the CSS/JS foundation. The template provides:
- Dark theme with accent color variables (customize per topic)
- All component styles (hero, acts, metaphors, flows, code blocks, diagrams, comparisons, tables, insights)
- Scroll-reveal animations
- Side navigation dots
- Responsive layout

**Adapt the template — don't start from scratch.** Change:
- CSS color variables to match the topic (e.g., blue for database, green for networking)
- Hero title and subtitle
- Act content
- Navigation dot labels

### 5. Output Location

Write to `.prd/ELI5/` directory in the project root (create if needed). Use `index.html` for single topics or `{topic-name}.html` for multiple.

Open in browser after creation for immediate preview.

## Component Reference

### Hero Section
Full-viewport centered title with subtle radial gradient glow and scroll-down hint arrow.

### Metaphor Card
```html
<div class="metaphor">
  <div class="metaphor-icon">EMOJI</div>
  <div class="metaphor-body">
    <h4>Metaphor Title</h4>
    <p>One-sentence explanation connecting familiar concept to technical one.</p>
  </div>
</div>
```

### Step Flow (numbered vertical timeline)
```html
<div class="flow">
  <div class="flow-step">
    <div class="flow-num">1</div>
    <div class="flow-content">
      <h4>Step Title</h4>
      <p>What happens and why, with inline <code>code</code> references.</p>
    </div>
  </div>
  <!-- more steps... -->
</div>
```

### Side-by-Side Comparison
```html
<div class="vs-grid">
  <div class="vs-card pg">  <!-- color class -->
    <h4>Option A</h4>
    <ul><li>Detail</li></ul>
  </div>
  <div class="vs-card mongo">
    <h4>Option B</h4>
    <ul><li>Detail</li></ul>
  </div>
</div>
```

### Insight Callout
```html
<div class="insight">
  <div class="insight-label">Key Insight</div>
  <p>The most important takeaway from this section.</p>
</div>
```

### ASCII Diagram
```html
<div class="diagram"><!-- monospace art with span classes: .node .arrow .str .dim .fn --></div>
```

### Code Block
```html
<div class="code-block">
  <div class="code-header"><span class="code-dot pg"></span> Language/Context</div>
  <pre><!-- syntax highlighted with span classes: .kw .fn .str .cmt .type .num --></pre>
</div>
```

### Comparison Table
```html
<table class="comparison-table"><!-- .tag-yes and .tag-no for feature support --></table>
```

## Quality Checklist

- [ ] Opens with a mystery/question, not a definition
- [ ] Every technical concept has a metaphor introduced BEFORE the code
- [ ] One concept per act (never two new ideas at once)
- [ ] At least 3 different visual component types used
- [ ] Side-by-side comparisons when 2+ approaches exist
- [ ] Code blocks have language labels and syntax highlighting
- [ ] Ends with a big-picture summary table + one-line takeaway
- [ ] Navigation dots match act structure
- [ ] Scroll-reveal animations work
- [ ] Opens in browser after creation
