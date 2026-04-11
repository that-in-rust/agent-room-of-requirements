#!/usr/bin/env python3
"""
Bootstrap a single-file explainer HTML page from the bundled template.
"""

from __future__ import annotations

import argparse
from html import escape
from pathlib import Path
from textwrap import dedent

SKILL_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = SKILL_DIR / "assets" / "elegant-explainer-template.html"

SECTION_SPECS = [
    {
        "id": "act1",
        "label": "Act I",
        "nav": "The Problem",
        "title": "The Problem",
        "body": """
        <p>Replace this opening with the real problem the system solves. Name the actors, the data, and why the behavior matters.</p>

        <div class="metaphor">
          <div class="metaphor-mark">01</div>
          <div class="metaphor-body">
            <h4>Choose One Helpful Metaphor</h4>
            <p>Use a short analogy only if it lowers the barrier to understanding. Tie it back to the real mechanics in the next paragraph.</p>
          </div>
        </div>

        <p>End this act with a plain-language thesis sentence that previews the rest of the page.</p>
        """,
    },
    {
        "id": "act2",
        "label": "Act II",
        "nav": "Core Loop",
        "title": "The Core Loop",
        "body": """
        <p>Explain the system's heartbeat here. Prefer the exact verbs used in the implementation or docs.</p>

        <div class="flow">
          <div class="flow-step">
            <div class="flow-num">1</div>
            <div class="flow-content">
              <h4>Initialize</h4>
              <p>Explain what must be ready before work begins.</p>
            </div>
          </div>
          <div class="flow-step">
            <div class="flow-num">2</div>
            <div class="flow-content">
              <h4>Read Or Poll</h4>
              <p>Describe how the system discovers new work or new data.</p>
            </div>
          </div>
          <div class="flow-step">
            <div class="flow-num">3</div>
            <div class="flow-content">
              <h4>Transform</h4>
              <p>Show how raw inputs become the payload or state the rest of the system needs.</p>
            </div>
          </div>
          <div class="flow-step">
            <div class="flow-num">4</div>
            <div class="flow-content">
              <h4>Apply Or Deliver</h4>
              <p>Show where the real effect happens: write, emit, send, store, or publish.</p>
            </div>
          </div>
          <div class="flow-step">
            <div class="flow-num">5</div>
            <div class="flow-content">
              <h4>Persist Progress</h4>
              <p>Explain what gets committed or remembered before the next cycle begins.</p>
            </div>
          </div>
        </div>

        <div class="insight">
          <div class="insight-label">Key Insight</div>
          <p>Summarize the one detail that makes this loop reliable, fast, or easy to misunderstand.</p>
        </div>
        """,
    },
    {
        "id": "act3",
        "label": "Act III",
        "nav": "Variants",
        "title": "Key Variants Or Modes",
        "body": """
        <p>Compare two important modes, components, or implementations. Delete one side if the system does not need a comparison.</p>

        <div class="vs-grid">
          <div class="vs-card">
            <h4>Path A</h4>
            <ul>
              <li>Explain what it talks to or depends on</li>
              <li>Explain how it tracks progress</li>
              <li>Explain its main strength</li>
              <li>Explain one limitation or caveat</li>
            </ul>
          </div>
          <div class="vs-card">
            <h4>Path B</h4>
            <ul>
              <li>Explain what differs from Path A</li>
              <li>Explain how it changes the lifecycle</li>
              <li>Explain what it is better at</li>
              <li>Explain what it cannot do</li>
            </ul>
          </div>
        </div>

        <div class="code-block">
          <div class="code-header">Representative snippet</div>
          <pre>// Replace this with one short code or query example
// that reveals how the system really behaves.</pre>
        </div>
        """,
    },
    {
        "id": "act4",
        "label": "Act IV",
        "nav": "State And Safety",
        "title": "State, Safety, And Recovery",
        "body": """
        <p>Slow down here. Explain what gets remembered, when it becomes durable, and how the system resumes after failure.</p>

        <div class="diagram">read()
  |
  v
tentative state
  |
  +--> success -> commit durable progress
  |
  +--> failure -> discard or retry from last safe point</div>

        <div class="options-grid">
          <div class="option-card">
            <code>state</code>
            <h4>What Is Persisted</h4>
            <p>Name the fields, offsets, checkpoints, or markers that let the system resume safely.</p>
          </div>
          <div class="option-card">
            <code>success</code>
            <h4>What Happens On Success</h4>
            <p>Explain when progress becomes committed and what future work skips because of that commit.</p>
          </div>
          <div class="option-card">
            <code>failure</code>
            <h4>What Happens On Failure</h4>
            <p>Explain the rollback, retry, or replay behavior in concrete terms.</p>
          </div>
        </div>

        <div class="insight">
          <div class="insight-label">Reliability Note</div>
          <p>Use this callout to state the delivery or recovery guarantee precisely.</p>
        </div>
        """,
    },
    {
        "id": "act5",
        "label": "Act V",
        "nav": "Architecture",
        "title": "Architecture And Boundaries",
        "body": """
        <p>Show what the author implements directly and what the surrounding runtime, framework, or host provides.</p>

        <div class="diagram">host runtime
  |
  +--> container / framework wrapper
         |
         +--> your component or plugin
                |
                +--> external system</div>

        <div class="vs-grid">
          <div class="vs-card">
            <h4>What The Component Owns</h4>
            <ul>
              <li>List the direct responsibilities</li>
              <li>List the inputs it receives</li>
              <li>List the outputs it emits</li>
            </ul>
          </div>
          <div class="vs-card">
            <h4>What The Runtime Owns</h4>
            <ul>
              <li>List lifecycle management responsibilities</li>
              <li>List serialization or orchestration duties</li>
              <li>List extension points or plugin hooks</li>
            </ul>
          </div>
        </div>
        """,
    },
    {
        "id": "act6",
        "label": "Act VI",
        "nav": "Failures",
        "title": "Failure Modes And Tradeoffs",
        "body": """
        <p>Group failures into meaningful buckets. Use real examples from the code or docs.</p>

        <div class="vs-grid">
          <div class="vs-card">
            <h4>Retryable</h4>
            <ul>
              <li>Network instability</li>
              <li>Temporary resource exhaustion</li>
              <li>Short-lived dependency failures</li>
            </ul>
          </div>
          <div class="vs-card">
            <h4>Fatal</h4>
            <ul>
              <li>Bad configuration</li>
              <li>Protocol or schema mismatch</li>
              <li>Permanent correctness violations</li>
            </ul>
          </div>
        </div>

        <div class="options-grid">
          <div class="option-card">
            <code>tradeoff</code>
            <h4>Correctness</h4>
            <p>State what the system optimizes for and what it refuses to compromise.</p>
          </div>
          <div class="option-card">
            <code>tradeoff</code>
            <h4>Performance</h4>
            <p>State the batching, latency, or throughput choice that shapes behavior.</p>
          </div>
          <div class="option-card">
            <code>tradeoff</code>
            <h4>Operability</h4>
            <p>State the logging, redaction, monitoring, or debugging behavior that matters in practice.</p>
          </div>
        </div>
        """,
    },
    {
        "id": "act7",
        "label": "Act VII",
        "nav": "Takeaway",
        "title": "The Big Picture",
        "body": """
        <p>Use the final section to compress the whole system into a clear mental model.</p>

        <table class="comparison-table">
          <thead>
            <tr>
              <th>Dimension</th>
              <th>Path A</th>
              <th>Path B</th>
              <th>Why It Matters</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Input</td>
              <td>Replace</td>
              <td>Replace</td>
              <td>Explain the user-visible consequence</td>
            </tr>
            <tr>
              <td>State</td>
              <td>Replace</td>
              <td>Replace</td>
              <td>Explain the recovery consequence</td>
            </tr>
            <tr>
              <td>Failure Handling</td>
              <td>Replace</td>
              <td>Replace</td>
              <td>Explain the reliability consequence</td>
            </tr>
          </tbody>
        </table>

        <div class="insight">
          <div class="insight-label">One Line Summary</div>
          <p>End with the shortest accurate sentence that captures the system's rhythm.</p>
        </div>
        """,
    },
]


def parse_command_arguments_now() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a new explainer HTML file from the elegant explainer template.",
    )
    parser.add_argument("--output", required=True, help="Output HTML path")
    parser.add_argument("--hero-title", required=True, help="Main page title")
    parser.add_argument(
        "--hero-subtitle",
        required=True,
        help="Subtitle shown under the page title",
    )
    parser.add_argument(
        "--hero-label",
        default="Technical Explainer",
        help="Small all-caps label shown above the title",
    )
    parser.add_argument(
        "--page-title",
        default="",
        help="Optional browser tab title. Defaults to the hero title.",
    )
    parser.add_argument(
        "--footer-label",
        default="Built from source",
        help="Footer heading shown above the source list",
    )
    parser.add_argument(
        "--source",
        action="append",
        default=[],
        help="Source file or note path to include in the footer. Repeat as needed.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite the output file if it already exists.",
    )
    return parser.parse_args()


def load_template_text_now() -> str:
    return TEMPLATE_PATH.read_text()


def render_nav_markup_now() -> str:
    nav_lines = [
        '  <div class="nav-dot" data-target="hero"><span class="nav-tooltip">Start</span></div>'
    ]
    for spec in SECTION_SPECS:
        nav_lines.append(
            f'  <div class="nav-dot" data-target="{spec["id"]}"><span class="nav-tooltip">{escape(spec["nav"])}</span></div>'
        )
    return "\n".join(nav_lines)


def render_section_markup_now() -> str:
    section_blocks = []
    for index, spec in enumerate(SECTION_SPECS):
        body_html = dedent(spec["body"]).strip()
        section_blocks.append(
            dedent(
                f"""
                <section class="act" id="{spec["id"]}">
                  <div class="reveal">
                    <div class="act-label">{escape(spec["label"])}</div>
                    <h2>{escape(spec["title"])}</h2>
                    {body_html}
                  </div>
                </section>
                """
            ).strip()
        )
        if index != len(SECTION_SPECS) - 1:
            section_blocks.append('<div class="divider"><hr></div>')
    return "\n\n".join(section_blocks)


def render_footer_sources_now(source_paths: list[str]) -> str:
    if not source_paths:
        source_paths = [
            "Replace this line with the main implementation file.",
            "Add supporting specs, notes, or interfaces below it.",
        ]
    escaped_lines = [escape(path) for path in source_paths]
    return "    " + "<br>\n    ".join(escaped_lines)


def build_placeholder_map_now(arguments: argparse.Namespace) -> dict[str, str]:
    page_title = arguments.page_title or arguments.hero_title
    return {
        "__PAGE_TITLE__": escape(page_title),
        "__HERO_LABEL__": escape(arguments.hero_label),
        "__HERO_TITLE__": escape(arguments.hero_title),
        "__HERO_SUBTITLE__": escape(arguments.hero_subtitle),
        "__NAV_ITEMS__": render_nav_markup_now(),
        "__SECTION_ITEMS__": render_section_markup_now(),
        "__FOOTER_LABEL__": escape(arguments.footer_label),
        "__FOOTER_SOURCES__": render_footer_sources_now(arguments.source),
    }


def write_output_file_now(arguments: argparse.Namespace) -> Path:
    output_path = Path(arguments.output).expanduser().resolve()
    if output_path.exists() and not arguments.force:
        raise SystemExit(
            f"Refusing to overwrite existing file: {output_path}. Use --force to replace it."
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    page_html = load_template_text_now()
    for placeholder, value in build_placeholder_map_now(arguments).items():
        page_html = page_html.replace(placeholder, value)

    output_path.write_text(page_html)
    return output_path


def main() -> None:
    arguments = parse_command_arguments_now()
    output_path = write_output_file_now(arguments)
    print(f"[OK] Created explainer scaffold: {output_path}")


if __name__ == "__main__":
    main()
