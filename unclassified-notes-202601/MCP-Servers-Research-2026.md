# Comprehensive Research: MCP (Model Context Protocol) Servers for Programmers (2026)

> **Last Updated:** February 15, 2026
> **Ecosystem Size:** 3,000+ MCP servers indexed on MCP.so; 1,200+ quality-verified on mcp-awesome.com; 8,230+ on PulseMCP
> **Official Repo Stars:** ~78,700 stars on [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

---

## Table of Contents

1. [What is MCP?](#what-is-mcp)
2. [Diagramming and Visual Tools MCPs](#1-diagramming-and-visual-tools-mcps)
3. [Browsing and Web MCPs](#2-browsing-and-web-mcps)
4. [Database and Data MCPs](#3-database-and-data-mcps)
5. [Git and Code MCPs](#4-git-and-code-mcps)
6. [File System and Editor MCPs](#5-file-system-and-editor-mcps)
7. [Cloud and Infrastructure MCPs](#6-cloud-and-infrastructure-mcps)
8. [Communication and Productivity MCPs](#7-communication-and-productivity-mcps)
9. [AI and ML MCPs](#8-ai-and-ml-mcps)
10. [API and Integration MCPs](#9-api-and-integration-mcps)
11. [Other Notable MCPs](#10-other-notable-mcps)
12. [Key Directories and Registries](#key-directories-and-registries)
13. [Security Best Practices](#security-best-practices)
14. [Sources](#sources)

---

## What is MCP?

The **Model Context Protocol (MCP)** is an open standard introduced by Anthropic in November 2024 that standardizes how AI systems (LLMs) integrate with external tools, data sources, and services. It provides a universal interface -- often described as "USB-C for AI" -- allowing any MCP-compliant client (Claude Desktop, Cursor, VS Code Copilot, Windsurf, OpenAI ChatGPT Desktop, etc.) to connect to any MCP-compliant server.

### Key Milestones

| Date | Event |
|---|---|
| Nov 2024 | Anthropic announces MCP as an open standard |
| Mar 2025 | OpenAI officially adopts MCP across its products (including ChatGPT Desktop) |
| Nov 2025 | Specification revision 2025-11-25 published |
| Dec 2025 | Anthropic donates MCP to the **Agentic AI Foundation (AAIF)** under the Linux Foundation, co-founded by Anthropic, Block, and OpenAI |
| Dec 2025 | Google launches managed MCP servers for Maps, BigQuery, GCE, GKE |
| Jan 2026 | GitHub launches official MCP server with 80+ tools |
| Feb 2026 | Miro launches MCP server; ecosystem surpasses 8,000+ indexed servers |

### Official SDKs

| Language | Maintainer | Notes |
|---|---|---|
| TypeScript | Anthropic | ~21k stars; primary reference SDK |
| Python | Anthropic | ~21k stars; `mcp` package on PyPI |
| C# | Microsoft | .NET ecosystem |
| Kotlin | JetBrains | JVM ecosystem |
| Java | Community | JVM alternative |
| Ruby | Shopify | Ruby ecosystem |
| PHP | The PHP Foundation | PHP ecosystem |
| Rust | Community | ~3k stars |

---

## 1. Diagramming and Visual Tools MCPs

### Overview Table

| MCP Server | Source | Description | Key Tools | Status |
|---|---|---|---|---|
| **Excalidraw MCP** | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | Create and manipulate Excalidraw diagrams via AI | 26 tools: `get_element`, `clear_canvas`, `export_scene`, `export_to_image`, `snapshot_scene`, `get_canvas_screenshot`, `export_to_excalidraw_url`, `set_viewport` | Released Nov 2025; actively maintained |
| **Excalidraw MCP (Scofieldfree)** | [Scofieldfree/excalidraw-mcp](https://github.com/Scofieldfree/excalidraw-mcp) | AI agents create/edit Excalidraw diagrams in conversation | Bridge between MCP clients and local Excalidraw instance | Active |
| **Mermaid-to-Excalidraw** | [yannick-cw/mermaid-to-excalidraw-mcp](https://github.com/yannick-cw/mermaid-to-excalidraw-mcp) | Convert Mermaid diagrams to styled Excalidraw files | Flowcharts, sequence diagrams, ER diagrams; outputs `.excalidraw.md` files openable in Obsidian | Active |
| **Miro MCP** | Official (Miro) | Bidirectional integration between Miro whiteboards and AI coding environments | Visual collaboration, whiteboard manipulation, sticky notes, shapes | Launched Feb 2, 2026 (with Anthropic, AWS, GitHub, Google) |
| **Mermaid MCP** | [hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid) | Generate Mermaid diagrams dynamically with AI | Mermaid chart generation, rendering to images | Active |
| **Mermaid Diagram Generator** | [reblabers](https://www.pulsemcp.com/servers/reblabers-mermaid-diagram-generator) | Render Mermaid diagrams as images | Image output (PNG/SVG) from Mermaid syntax | Released Dec 2025 |
| **Mermaid-MCP-Server** | [peng-shawn/mermaid-mcp-server](https://github.com/peng-shawn/mermaid-mcp-server) | Convert Mermaid diagrams to PNG images | PNG rendering of Mermaid code | Active |
| **Mermaid Project Analyzer** | [GittyBurstein/mermaid-mcp-server](https://github.com/mcp-research/GittyBurstein__mermaid-mcp-server) | Turn codebases (local/GitHub) into Mermaid diagrams | `list_files`, `read_file`, `generate_mermaid`, `render_mermaid` | Active |
| **Draw.io MCP (Official)** | [@drawio/mcp on npm](https://www.npmjs.com/package/@drawio/mcp) | Open diagrams in the draw.io editor from AI conversations | `npm i @drawio/mcp`; v1.1.2 | Official; maintained by draw.io team |
| **Draw.io MCP (Community)** | [lgazo/drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server) | Programmatic diagram control and intelligent analysis | Create, modify, analyze draw.io diagrams | Active |
| **Figma Dev Mode MCP** | [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) | Expose live Figma design data to AI coding tools | Layer hierarchy, auto-layout, variants, text styles, token references | Official Figma server; remote + desktop modes |
| **Framelink Figma MCP** | [GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) | Simplified Figma API access for AI coding agents | Layout and styling extraction, one-shot design-to-code | Popular community alternative |
| **tldraw MCP** | [dpunj/tldraw-mcp](https://glama.ai/mcp/servers/@dpunj/tldraw-mcp) | AI-driven canvas manipulation with tldraw | Create, update, manage shapes, flowcharts, frames | Active |
| **tldraw MCP (shahidhustles)** | [shahidhustles/tldraw-mcp](https://github.com/shahidhustles/tldraw-mcp) | Claude creates tldraw diagrams from natural language | Natural language to diagram conversion | Active |
| **UML-MCP** | [antoinebou12/uml-mcp](https://github.com/antoinebou12/uml-mcp) | Generate UML diagrams via PlantUML, Mermaid, Kroki | Class, Sequence, Activity, Use Case, State, Component, ER, BPMN, C4; SVG/PNG/PDF output | Comprehensive; uses Kroki fallback |
| **Diagram Bridge MCP** | [tohachan/diagram-bridge-mcp](https://github.com/tohachan/diagram-bridge-mcp) | Intelligent diagram format selection and rendering via Kroki | Mermaid, PlantUML, C4, D2, GraphViz, BPMN, Structurizr, Excalidraw, Vega-Lite; `help_choose_diagram` tool | Listed Jan 2026 |
| **C4 Diagrammer** | [jonverrier/C4Diagrammer](https://github.com/jonverrier/C4Diagrammer) | Generate C4 architecture diagrams from legacy codebases | Code summaries + C4 diagrams using Mermaid.js | Active |

### Notes on Diagramming MCPs

- **PlantUML** is supported primarily through the UML-MCP and Diagram Bridge servers, which use Kroki as a rendering backend supporting 30+ diagram types.
- **Whimsical** and **Lucidchart** do not have dedicated MCP servers as of Feb 2026. Teams needing these can use Mermaid/PlantUML-based MCP servers or the Miro MCP as alternatives for collaborative visual work.
- The **Diagram Bridge MCP** is the most versatile option, supporting 9+ diagram formats with a `help_choose_diagram` tool for guided format selection.
- The **yctimlin/mcp_excalidraw** server is the most feature-complete Excalidraw integration with 26 tools and canvas screenshot capability for AI visual feedback loops.

### Installation Example: Excalidraw MCP

```json
{
  "mcpServers": {
    "excalidraw": {
      "command": "npx",
      "args": ["-y", "mcp_excalidraw"]
    }
  }
}
```

Docker alternative:
```bash
docker run -d -p 3000:3000 --name mcp-excalidraw-canvas ghcr.io/yctimlin/mcp_excalidraw-canvas:latest
```

### Installation Example: Draw.io MCP

```json
{
  "mcpServers": {
    "drawio": {
      "command": "npx",
      "args": ["-y", "@drawio/mcp"]
    }
  }
}
```

---

## 2. Browsing and Web MCPs

### Overview Table

| MCP Server | Source | Description | Key Tools | Status |
|---|---|---|---|---|
| **Playwright MCP (Microsoft)** | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Official browser automation via accessibility tree snapshots | Chromium, Firefox, WebKit; deterministic control; fast structured output | Official Microsoft; production-ready |
| **MCP-Playwright (Community)** | [executeautomation/mcp-playwright](https://github.com/executeautomation/mcp-playwright) | Browser + API automation for Claude, Cursor, Cline | Browser automation + API testing combined | Active; popular |
| **Browserbase MCP** | [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) | Cloud-hosted browser automation with Stagehand | Multi-browser support, STDIO + SHTTP transport, `--experimental` flag | Production; Stagehand v3 |
| **Puppeteer MCP** | [twolven/puppeteer](https://www.pulsemcp.com/servers/twolven-puppeteer) | Puppeteer integration with Steel SDK | Browser automation, data extraction, screenshots | Active |
| **Brave Search MCP** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Privacy-first web search via Brave Search API | `brave_web_search`, `brave_local_search`; result filtering | Official reference server |
| **Tavily MCP** | [tavily-ai/tavily-mcp](https://github.com/tavily-ai/tavily-mcp) | Real-time search, extraction, crawling, site mapping | `search`, `extract`, `map`, `crawl`; 1,000 free monthly credits | Official; actively maintained |
| **Fetch MCP** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Web content fetching and conversion for LLMs | URL fetching, HTML-to-markdown conversion, robots.txt compliance | Official reference server |
| **Firecrawl MCP** | [mendableai/firecrawl-mcp-server](https://github.com/mendableai/firecrawl-mcp-server) | Web scraping, crawling, structured data extraction | Scrape, deep crawl, site map, AI-powered extraction; cloud + self-hosted | Active; 64.8% benchmark success rate |
| **Bright Data MCP** | [Bright Data](https://brightdata.com/) | Enterprise web data collection with anti-detection | Search + Web Unlocker + Scraping Browser + Web Scraper API | 76.8% benchmark success rate (highest) |
| **Perplexity MCP** | [perplexityai/modelcontextprotocol](https://github.com/perplexityai/modelcontextprotocol) | AI-powered search and reasoning | Sonar, Sonar Pro, Sonar Deep Research, Sonar Reasoning Pro models | Official; paid API ($1-15/M tokens) |
| **Exa MCP** | Via [MCP Omnisearch](https://github.com/spences10/mcp-omnisearch) | Semantic search and similar content discovery | `exa_contents`, `exa_similar`, `exa_answer` | Part of Omnisearch |
| **MCP Omnisearch** | [spences10/mcp-omnisearch](https://github.com/spences10/mcp-omnisearch) | Unified multi-provider search | Auto-detects API keys for Tavily, Brave, Kagi, Exa, Perplexity, Jina, Firecrawl | Active |
| **Context7 MCP** | [context7.com](https://context7.com/) | Fetch current library/API docs as context | Version-specific docs, code examples; replaces stale training data | Active; Node.js >= v18 |
| **Jina Reader MCP** | Jina AI | URL-to-markdown, web search, image search, embeddings | Clean markdown extraction, strips boilerplate/nav/ads | Active |
| **Brave Deep Research** | [suthio/brave-deep-research](https://www.pulsemcp.com/servers/suthio-brave-deep-research) | Deep research combining Brave Search + web scraping | Full content extraction, configurable link traversal depth | Active |

### Web Scraping Benchmark Results (2026)

| MCP Server | Success Rate | Avg. Completion Time | Best For |
|---|---|---|---|
| **Bright Data** | 76.8% | 48.7s | Anti-bot bypassing, enterprise scraping |
| **Firecrawl** | 64.8% | 77.6s | General-purpose scraping, structured extraction |
| **Tavily** | 45.0% | 41.3s | Quick factual lookups, research |

### Installation Example: Playwright MCP

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-playwright"]
    }
  }
}
```
Requires browser binaries: `npx playwright install`

### Installation Example: Brave Search MCP

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

### Installation Example: Tavily MCP

```json
{
  "mcpServers": {
    "tavily": {
      "command": "npx",
      "args": ["-y", "tavily-mcp"],
      "env": {
        "TAVILY_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

---

## 3. Database and Data MCPs

### Universal / Multi-Database Servers

| MCP Server | Source | Databases Supported | Key Features | Status |
|---|---|---|---|---|
| **AnyDB-MCP** | [officialalexeev/anydb-mcp](https://github.com/officialalexeev/anydb-mcp) | PostgreSQL, MySQL, SQLite, MongoDB, Redis | Zero-config via `npx`; auto-detects DB type from URI; stateless; single `db_query` tool | Active |
| **MCP-DBS** | [mcp-dbs](https://mcp.so/server/mcp-dbs) | SQLite, PostgreSQL, MSSQL, MongoDB | SSE + STDIO modes; `npm install -g mcp-dbs` | Active |
| **Multi-DB (neverinfamous)** | [neverinfamous/db](https://www.pulsemcp.com/servers/neverinfamous-db) | SQLite, PostgreSQL, MySQL, MongoDB, Redis, SQL Server | OAuth 2.0 auth; granular scope-based permissions | Enterprise-focused |
| **MCP-Datalink** | [pilat/mcp-datalink](https://github.com/pilat/mcp-datalink) | PostgreSQL, MySQL, SQLite | Parameterized queries; schema inspection | Active |

### Database-Specific Servers

| MCP Server | Source | Description | Key Features | Status |
|---|---|---|---|---|
| **PostgreSQL (Official)** | [modelcontextprotocol/server-postgres](https://github.com/modelcontextprotocol/servers) | PostgreSQL integration for AI | Schema inspection, query capabilities, read-only mode, connection pooling | Official reference server |
| **SQLite (Official)** | [modelcontextprotocol/server-sqlite](https://github.com/modelcontextprotocol/servers) | SQLite database operations | Built-in analysis features, business intelligence queries | Official reference server |
| **MongoDB (QuantGeekDev)** | [QuantGeekDev/mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp) | MongoDB integration | Direct LLM-to-database interaction, CRUD operations | Active |
| **MongoDB Lens** | [furey/mongodb-lens](https://github.com/furey/mongodb-lens) | Full-featured MongoDB MCP | Comprehensive MongoDB operations, aggregation pipelines | Active |
| **MySQL MCP** | Community | MySQL database access | Schema inspection, query execution, table management | Active |
| **Redis (Official)** | Redis Labs | Redis data management and search | Manage + search data in Redis instances | Official |
| **Redis Cloud API** | Redis Labs | Redis Cloud resource management | Natural language cloud resource management | Official |
| **Upstash Redis** | Upstash | Serverless Redis on Upstash | Manage databases, run commands via natural language | Active |
| **Supabase MCP** | [supabase.com/docs/guides/getting-started/mcp](https://supabase.com/docs/guides/getting-started/mcp) | Supabase (Postgres + Auth + Storage + Edge Functions) | Edge functions, Postgres streaming, serverless, real-time subscriptions | Official; production-ready |
| **Neon Postgres MCP** | Neon (official) | Serverless Postgres | Local (stdio) + remote (OAuth) modes; comprehensive toolset; branching support | Official; Neon acquired by Databricks |
| **GreptimeDB MCP** | GreptimeDB | Time-series database | Metrics, logging, time-series analytics; local + cloud setup | Active |
| **Chroma MCP** | Chroma | Vector/semantic document management | Vector search, scaling from dev to production, RAG-ready | Open-source; popular for RAG |
| **DuckDB MCP** | Community | Analytical queries | In-process OLAP, Parquet/CSV/JSON support | Active |
| **Turso MCP** | Turso | Edge SQLite (libSQL) | Distributed SQLite at the edge | Active |

### Installation Example: PostgreSQL MCP

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgresql://user:password@localhost:5432/mydb"
      ]
    }
  }
}
```

### Installation Example: SQLite MCP

```json
{
  "mcpServers": {
    "sqlite": {
      "command": "uvx",
      "args": ["mcp-server-sqlite", "--db-path", "/path/to/database.db"]
    }
  }
}
```

### Installation Example: AnyDB-MCP (Zero-Config)

```bash
# PostgreSQL
npx anydb-mcp postgresql://user:pass@host:5432/db

# MongoDB
npx anydb-mcp mongodb://user:pass@host:27017/db

# Redis
npx anydb-mcp redis://host:6379

# SQLite
npx anydb-mcp sqlite:///path/to/db.sqlite
```

---

## 4. Git and Code MCPs

### Overview Table

| MCP Server | Source | Description | Key Tools | Status |
|---|---|---|---|---|
| **GitHub MCP (Official)** | [github.com/github/github-mcp-server](https://github.com/github/github-mcp-server) | Official GitHub MCP server by GitHub | 80+ tools: commits, PRs, issues, branches, code search, Actions, security advisories | Released Jan 10, 2026; production |
| **GitHub MCP (Anthropic)** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Reference GitHub integration | Repository management, PR automation, file operations, issue tracking | Official reference server |
| **GitLab MCP** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | GitLab API integration | 44 tools across 18 entity types; CQRS architecture; OAuth 2.1 | Official; Premium/Ultimate users |
| **Bitbucket MCP (Atlassian)** | [aashari/mcp-server-atlassian-bitbucket](https://github.com/aashari/mcp-server-atlassian-bitbucket) | Bitbucket workspaces, repos, PRs | List, get, comment, search on PRs and repos | Active; App Passwords deprecated by Jun 2026 |
| **Bitbucket MCP (MatanYemini)** | [MatanYemini/bitbucket-mcp](https://github.com/MatanYemini/bitbucket-mcp) | Bitbucket Cloud + Server APIs | Cloud and Server API integration | Active |
| **Git MCP (Official)** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Core Git operations | Git commit, diff, log, branch, status, show operations | Official reference server |
| **GitMCP** | [gitmcp.io](https://gitmcp.io) | GitHub documentation access via remote MCP | URL-based setup; no installation required | Active |
| **Azure DevOps MCP** | Community | Azure DevOps Git integration | Repository workflows in Microsoft ecosystem, work items, pipelines | Active |
| **Unified Git Forge** | Community | Multi-platform Git management | GitHub, GitLab, Gitea, Bitbucket via CLI tools | Released Dec 17, 2025 |
| **Sentry MCP** | [Sentry](https://blog.sentry.io/introducing-mcp-server-monitoring/) | Error tracking + performance telemetry | Access Sentry data; monitors MCP servers themselves; 50M req/month | Production |
| **Gitingest** | Community | Repository analysis and ingestion | Code analysis, repo understanding, documentation extraction | Active |

### Installation Example: GitHub MCP (Official)

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_YOUR_TOKEN"
      }
    }
  }
}
```

### Installation Example: Git MCP

```json
{
  "mcpServers": {
    "git": {
      "command": "uvx",
      "args": ["mcp-server-git", "--repository", "/path/to/repo"]
    }
  }
}
```

### Installation Example: GitLab MCP

```json
{
  "mcpServers": {
    "gitlab": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gitlab"],
      "env": {
        "GITLAB_PERSONAL_ACCESS_TOKEN": "glpat-YOUR_TOKEN",
        "GITLAB_API_URL": "https://gitlab.com/api/v4"
      }
    }
  }
}
```

---

## 5. File System and Editor MCPs

### Overview Table

| MCP Server | Source | Description | Key Tools | Status |
|---|---|---|---|---|
| **Filesystem MCP (Official)** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | Secure filesystem operations with configurable access | Read, write, move, search files; directory listing; directory tree; configurable allowed paths | Official reference server |
| **Desktop Commander MCP** | [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | Terminal control + file system + diff editing | Execute commands, file ops, process management, in-memory code execution (Python/Node.js/R), Excel/PDF support | 5.3k stars; MIT; very popular |
| **VS Code MCP Server** | [juehang/vscode-mcp-server](https://github.com/juehang/vscode-mcp-server) | Expose VS Code editing features to MCP clients | Symbol search, document outlines, file ops, diagnostics, refactoring with import updates | VS Code Marketplace extension |
| **VS Code Native MCP** | [code.visualstudio.com/mcp](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) | Built-in MCP support in VS Code | MCP server gallery (`@mcp` in Extensions); GitHub Copilot agent mode integration | Native since late 2025 |
| **Visual Studio 2026 MCP** | Microsoft | Azure MCP Server built into Visual Studio 2026 | Azure resource management, IaC generation, AKS queries, Cosmos DB queries | GA with Visual Studio 2026 |
| **JetBrains MCP** | JetBrains | MCP support in IntelliJ-based IDEs | AI Assistant integration; Kotlin SDK co-maintained | Official |
| **MCP Shell Server** | [tumf/mcp-shell-server](https://github.com/tumf/mcp-shell-server) | Secure whitelisted shell command execution | Command whitelisting, stdin support, shell injection prevention | Active |
| **Everything Search MCP** | Community | Windows Everything search integration | Fast file search across entire drives on Windows | Active |

### Filesystem MCP Configuration

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/path/to/allowed/dir1",
        "/path/to/allowed/dir2"
      ]
    }
  }
}
```

Docker (with read-only mount):
```bash
docker run -v /path/to/dir:/projects/dir:ro \
  mcp/filesystem --allow-dir /projects
```

### Desktop Commander Configuration

```json
{
  "mcpServers": {
    "desktop-commander": {
      "command": "npx",
      "args": ["-y", "@wonderwhy-er/desktop-commander@latest"]
    }
  }
}
```

### Filesystem Security Best Practices

- Never grant filesystem access to your entire root drive (`/`) or home directory (`~`)
- Restrict access to specific project or scratch directories
- Use read-only mounts where possible
- VS Code shows permission dialogs before MCP tool execution
- The Desktop Commander MCP is powerful but should be scoped carefully in production

---

## 6. Cloud and Infrastructure MCPs

### Cloud Provider MCPs

| MCP Server | Source | Description | Key Features | Status |
|---|---|---|---|---|
| **AWS MCP Servers** | AWS (Official) | AWS service integration | Cost analysis, auto-scaling, resource management; Docker/ECS deployment; TLS + Cognito + WAF + IAM secured | Official; production |
| **Amazon Bedrock AgentCore** | AWS | Enterprise context manager for MCP orchestration | Query routing, multi-session memory, agent coordination, cross-agent delegation | Enterprise; integrated with Bedrock |
| **Azure MCP Server** | Microsoft (Official) | Azure cloud service integration | Azure SQL, Cosmos DB, Azure Functions, AKS; built into Visual Studio 2026 | Official; GA |
| **Google Cloud MCP** | [Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services) | Managed MCP for Google services | Maps, BigQuery, Compute Engine, GKE; expanding to Cloud Run, Cloud Storage, AlloyDB, Spanner, Looker | Official; launched Dec 2025 |
| **Cloudflare MCP** | Cloudflare (Official) | Edge orchestration for AI agents | Edge-first processing; Workers, KV, D1, R2 storage integration; one-click deployment | Official; production |

### Infrastructure as Code MCPs

| MCP Server | Source | Description | Key Features | Status |
|---|---|---|---|---|
| **Terraform MCP** | [hashicorp/terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server) | Terraform ecosystem integration | Registry APIs, TF Enterprise/HCP, workspace states, trigger runs with approval; AGENTS.md for AI guidance | Official HashiCorp; local only currently |
| **Pulumi MCP** | [pulumi.com/docs/iac/using-pulumi/mcp-server](https://www.pulumi.com/docs/iac/using-pulumi/mcp-server/) | AI-assisted IaC with Pulumi | CLI integration, registry queries, resource management; delegates to Pulumi Neo for complex tasks | Official; Docker available (`mcp/pulumi`) |
| **Pulumi Remote MCP** | [pulumi.com/blog/remote-mcp-server](https://www.pulumi.com/blog/remote-mcp-server/) | Hosted Pulumi MCP -- no local installation | Cloud infrastructure management, stack search, Neo delegation | Available now for all Pulumi users |
| **StackGen MCP** | [stackgen.com](https://stackgen.com/) | Infrastructure lifecycle management for platform teams | Pre-approved blueprints, security/compliance encoding, developer self-service provisioning | Enterprise; production |

### Container and Orchestration MCPs

| MCP Server | Source | Description | Key Features | Status |
|---|---|---|---|---|
| **Docker MCP** | Docker | Docker container management | Container lifecycle, image management, Compose support | Active |
| **Kubernetes MCP** | Community | Kubernetes cluster management | Pod management, deployment, service management, kubectl proxy | Community; active |
| **ArgoCD MCP** | Community | GitOps continuous delivery | ArgoCD workflow management, application sync | Community; active |
| **Pulumi K8s Operator 2.0** | Pulumi | Manage Pulumi stacks within K8s | Enhanced reconciliation, automatic retry, idempotent updates, fine-grained refresh | GA |

### DevOps Observability MCPs

| MCP Server | Source | Description | Key Features | Status |
|---|---|---|---|---|
| **Datadog MCP** | [docs.datadoghq.com/bits_ai/mcp_server](https://docs.datadoghq.com/bits_ai/mcp_server/) | Full observability integration | Logs, metrics, traces, APM; AWS DevOps Agent integration; correlates multiple signals | Official; Preview (free during preview) |
| **Datadog MCP (Community)** | [shelfio/datadog-mcp](https://github.com/shelfio/datadog-mcp) | Community Datadog MCP | Comprehensive monitoring and observability tools; ~39.8k downloads | Open-source; active |
| **Sentry MCP** | [Sentry](https://blog.sentry.io/introducing-mcp-server-monitoring/) | Error tracking + MCP server monitoring | MCP-specific telemetry; 50M requests/month across thousands of users | Production |
| **Prometheus MCP** | Community | Open-source monitoring | Natural language to PromQL; best for Prometheus + Grafana stacks | Community; active |
| **PagerDuty MCP** | Community | Incident management | Alert escalation, incident coordination, on-call management | Active |

### Installation Example: Terraform MCP

```json
{
  "mcpServers": {
    "terraform": {
      "command": "npx",
      "args": ["-y", "@hashicorp/terraform-mcp-server"]
    }
  }
}
```

### Installation Example: Pulumi MCP (Docker)

```json
{
  "mcpServers": {
    "pulumi": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "mcp/pulumi"],
      "env": {
        "PULUMI_ACCESS_TOKEN": "pul-YOUR_TOKEN"
      }
    }
  }
}
```

### Installation Example: Pulumi Remote MCP (No Install)

```json
{
  "mcpServers": {
    "pulumi-remote": {
      "url": "https://mcp.pulumi.com",
      "auth": "oauth"
    }
  }
}
```

---

## 7. Communication and Productivity MCPs

### Overview Table

| MCP Server | Source | Description | Key Tools | Status |
|---|---|---|---|---|
| **Slack MCP** | Official / Community | Slack channel interaction and automation | Read channels, summarize threads, post messages; chat history as knowledge base | Active; 40% productivity increase reported |
| **Notion MCP** | Official / Community | Notion workspace access for AI | Semantic search, page/database access, content generation/updates; 1,200 updates/min benchmark | Active |
| **Linear MCP** | Community | Linear project management integration | Issues, cycles, project updates, team workload | Ideal for high-velocity startups |
| **Jira MCP** | Community | Jira ticket management | Create/update tickets, project status queries, workflow management | Enterprise scale |
| **Atlassian MCP (Official)** | [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server) | Remote MCP for Jira + Confluence | Secure OAuth 2.1; respects existing Atlassian permissions | Official Atlassian |
| **Atlassian MCP (Community)** | [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) | Jira + Confluence (Cloud + Server/DC) | `confluence_search`, `confluence_get_page`, `confluence_create_page`, `jira_search`, `jira_create_issue` | Popular community server |
| **Google Workspace MCP** | [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | Full Google Workspace control -- most complete | Gmail, Calendar, Drive, Docs, Sheets, Slides, Forms, Tasks, Contacts, Chat (12/12 services) | v1.4.3; OAuth 2.1; multi-user |
| **Google Calendar MCP** | [nspady/google-calendar-mcp](https://github.com/nspady/google-calendar-mcp) | Google Calendar management | Multi-account, recurring events, free/busy queries, smart scheduling, image/PDF import | Active |
| **Google Drive MCP** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Google Drive file access | Search and access files/folders; read-only | Official reference server |
| **Google Maps MCP** | [Google Cloud (Official)](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services) | Geospatial data access | Places, weather, routing, distance/travel time; grounded real-world data | Official managed; launched Dec 2025 |
| **Salesforce MCP** | Salesforce (Official) | CRM and business data access | Close cases, pull customer data, update records via natural language | Official |
| **Asana MCP** | Community | Asana project management | Task management, project tracking, team coordination | Active |
| **Monday.com MCP** | Community | Monday.com integration | Board and item management, status updates | Active |
| **Todoist MCP** | Community | Todoist task management | Create/update tasks, project management | Active |

### Installation Example: Atlassian MCP (Community)

```bash
pip install mcp-atlassian
```

```json
{
  "mcpServers": {
    "atlassian": {
      "command": "python",
      "args": ["-m", "mcp_atlassian"],
      "env": {
        "JIRA_URL": "https://your-instance.atlassian.net",
        "JIRA_EMAIL": "your@email.com",
        "JIRA_API_TOKEN": "your-token",
        "CONFLUENCE_URL": "https://your-instance.atlassian.net/wiki",
        "CONFLUENCE_EMAIL": "your@email.com",
        "CONFLUENCE_API_TOKEN": "your-token"
      }
    }
  }
}
```

### Installation Example: Google Workspace MCP

```json
{
  "mcpServers": {
    "google-workspace": {
      "command": "npx",
      "args": ["-y", "google-workspace-mcp"],
      "env": {
        "GOOGLE_CLIENT_ID": "your-client-id",
        "GOOGLE_CLIENT_SECRET": "your-client-secret"
      }
    }
  }
}
```

---

## 8. AI and ML MCPs

### Vector Database MCPs

| MCP Server | Source | Description | Key Features | Status |
|---|---|---|---|---|
| **Pinecone MCP** | Pinecone (Official) | Managed vector similarity search | Fully managed; SOC 2, ISO 27001, GDPR, HIPAA; Pinecone Assistant wraps chunking + embedding + search + reranking | Enterprise; production |
| **Qdrant MCP** | Qdrant | High-performance vector search | Rust-based; best-in-class latency (8ms p50); sophisticated filtering; distributed; ACID transactions | Open-source; production |
| **Weaviate MCP** | Weaviate | Knowledge graph + vector search | GraphQL API; native generative module (v1.30); hybrid search; multi-modal; HIPAA on AWS | Enterprise; production |
| **Chroma MCP** | Chroma | Lightweight vector database for RAG | Developer-friendly; prototyping to production scaling; open-source | Active; popular for getting started |
| **Milvus MCP** | Milvus | Billion-scale vector search | GPU support; distributed architecture; strong open-source community | Active |
| **Vectara MCP** | Vectara | Semantic search and RAG | Real-time relevance-ranked context; custom domain-specific embeddings | Commercial |

### Vector DB Performance Benchmarks (2026)

| Database | p50 Latency | p99 Latency | Queries/Second | Best For |
|---|---|---|---|---|
| **Qdrant** | 8ms | 25ms | 1,500 | High performance, self-hosted |
| **Weaviate** | 15ms | 40ms | 800 | Hybrid search, knowledge graphs |
| **Pinecone** | 20ms | 50ms | 500 | Managed, zero-ops |

### When to Choose Which Vector DB

| Use Case | Recommendation |
|---|---|
| Managed, zero-ops | **Pinecone** -- minimal ops overhead, fastest to get started |
| Hybrid search | **Weaviate** -- vectors + structured data, GraphQL API, ML modules |
| High performance, self-hosted | **Qdrant** -- Rust-based performance, sophisticated filtering |
| Billion-scale | **Milvus** -- GPU support, distributed, strong community |
| Prototyping | **Chroma** -- developer-friendly, lightweight, excellent for small/medium apps |

### Memory and Knowledge Graph MCPs

| MCP Server | Source | Description | Key Features | Status |
|---|---|---|---|---|
| **Memory MCP (Official)** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Knowledge graph-based persistent memory | Entities with observations + typed relationships; cross-conversation persistence | Official reference server |
| **Zep Knowledge Graph** | [getzep.com](https://www.getzep.com/product/knowledge-graph-mcp/) | Persistent temporal knowledge graph | Local graph memory for any MCP client; persists across sessions; temporal awareness | Active |
| **Neo4j Knowledge Graph** | Community | Developer interactions to Neo4j graph | Uses Gemini for extraction of goals/constraints/relationships | Released Jan 2026 |

### AI Framework MCPs

| MCP Server | Source | Description | Key Features | Status |
|---|---|---|---|---|
| **LangChain MCP** | LangChain | Build MCP servers with LangChain | Dynamic knowledge base queries, adapters, out-of-the-box integrations | Active |
| **LlamaIndex MCP** | LlamaIndex | MCP-compatible context servers | Structured + unstructured data sources; fine-grained retrieval pipelines | Active |
| **Databricks MCP** | Databricks | Delta Lake + ML pipelines to LLMs | Mosaic framework; enterprise-grade data context for AI | Enterprise |
| **Context7 MCP** | [context7.com](https://context7.com/) | Live documentation fetching for AI | Version-specific docs + code examples as context; replaces stale training data | Rising star; highly recommended |

### Thinking and Reasoning MCPs

| MCP Server | Source | Description | Key Features | Status |
|---|---|---|---|---|
| **Sequential Thinking (Official)** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Structured step-by-step reasoning | Explicit thought sequences with reflection steps; problem decomposition; revision support | Official reference server |
| **Time MCP (Official)** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Timezone conversion and time operations | Reliable date/time math delegated to backend | Official reference server |

### Installation Example: Memory MCP

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

### Installation Example: Sequential Thinking MCP

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

---

## 9. API and Integration MCPs

### GraphQL MCPs

| MCP Server | Source | Description | Key Features | Status |
|---|---|---|---|---|
| **Apollo MCP Server** | [apollographql.com/docs/apollo-mcp-server](https://www.apollographql.com/docs/apollo-mcp-server) | Official Apollo GraphQL integration | Secure enterprise API access; schema introspection; supergraph support | Official Apollo; production |
| **mcp-graphql** | [blurrah/mcp-graphql](https://github.com/blurrah/mcp-graphql) | Generic GraphQL MCP server | Works with any GraphQL API; Python + TypeScript versions; also on PyPI | Active |
| **Microsoft Fabric GraphQL** | Microsoft | Fabric GraphQL API via MCP | `introspect-schema` tool; deep Fabric ecosystem integration | Official Microsoft |
| **Zuplo GraphQL MCP** | [zuplo.com](https://zuplo.com/blog/mcp-server-graphql) | Turn any GraphQL API into an MCP server | Auth, rate limiting, automatic AI agent querying | Active |

### REST and gRPC MCPs

| MCP Server | Source | Description | Key Features | Status |
|---|---|---|---|---|
| **REST API MCP** | Various community projects | JSON config to callable MCP tools | Dynamic API integration; rapid REST endpoint exposure | Multiple implementations |
| **gRPC MCP** | Community | Bridge AI to gRPC backends | Dynamic service method exposure via server reflection | Active |
| **OpenAPI MCP** | Community | Convert OpenAPI/Swagger specs to MCP tools | Auto-generates MCP tools from API specs | Active |

### Automation and Workflow MCPs

| MCP Server | Source | Description | Key Features | Status |
|---|---|---|---|---|
| **Zapier MCP** | Zapier (Official) | 8,000+ app integrations via MCP | RESTful endpoints; OAuth auth; audit logs; rate limiting; managed cloud | Official; Free tier: 100 tasks/month; Pro: $19.99/month |
| **n8n MCP** | [n8n.io](https://n8n.io/) | Open-source workflow automation + MCP | ~100 MCP tools; multi-agent systems; AI Agent Tool node; self-hostable; Python + Node.js execution | Active; very popular; open-source |
| **n8n Workflow Builder** | [makafeli/n8n-workflow-builder](https://github.com/makafeli/n8n-workflow-builder) | Connect AI assistants to n8n for workflow management | Natural language workflow creation, execution, management | Active |
| **Make (Integromat) MCP** | Make | Visual automation + MCP | AI orchestration "Grid"; workflow templates; similar to Zapier but more visual | Active |
| **Pipedream MCP** | [pipedream.com](https://pipedream.com/) | API integration platform | Thousands of pre-built integrations; code-level flexibility | Active |

### Payment and Communication MCPs

| MCP Server | Source | Description | Key Features | Status |
|---|---|---|---|---|
| **Stripe MCP** | [docs.stripe.com/mcp](https://docs.stripe.com/mcp) | Official Stripe payment integration | Create customers, PaymentIntents, invoices, subscriptions; remote (`mcp.stripe.com`) + local (`npx`) | Official; OAuth + API key auth |
| **Stripe Agent Toolkit** | [github.com/stripe/ai](https://github.com/stripe/ai) | Stripe for AI agent frameworks | OpenAI SDK, LangChain, CrewAI, Vercel AI SDK; Python + TypeScript | Official |
| **Twilio MCP** | [Twilio](https://www.twilio.com/en-us/blog/introducing-twilio-alpha-mcp-server) | Twilio communication APIs | Serverless Functions deployment; SMS, voice, messaging | Alpha; official |
| **SendGrid MCP** | [Garoth/sendgrid-mcp](https://github.com/Garoth/sendgrid-mcp) | Email automation via SendGrid | Contact lists, templates, single sends, statistics | Active |

### Installation Example: Stripe MCP (Remote -- No Install)

```json
{
  "mcpServers": {
    "stripe": {
      "url": "https://mcp.stripe.com",
      "auth": "oauth"
    }
  }
}
```

Stripe MCP (Local):
```bash
npx -y @stripe/mcp --api-key=sk_test_YOUR_KEY --tools=all
```

### Installation Example: n8n MCP

```json
{
  "mcpServers": {
    "n8n": {
      "command": "npx",
      "args": ["-y", "n8n-mcp-server"],
      "env": {
        "N8N_API_URL": "http://localhost:5678",
        "N8N_API_KEY": "your-api-key"
      }
    }
  }
}
```

---

## 10. Other Notable MCPs

### Developer Experience and Documentation

| MCP Server | Source | Description | Key Features | Status |
|---|---|---|---|---|
| **Everything MCP** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Reference/test server showcasing all MCP features | Prompts, resources, tools -- for testing MCP client implementations | Official reference |
| **MCP Inspector** | [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector) | Visual testing tool for MCP servers | ~8,700 stars; debug and inspect MCP server behavior; essential for development | Official; essential for MCP dev |
| **GPT Researcher MCP** | Community | Autonomous research agent | Browse, summarize, synthesize information independently | Active |
| **Markdownify MCP** | Community | Convert various file formats to Markdown | PDF, DOCX, HTML, images (via OCR), spreadsheets to Markdown | Active |

### Edge and Deployment MCPs

| MCP Server | Source | Description | Key Features | Status |
|---|---|---|---|---|
| **Cloudflare Workers MCP** | [Cloudflare](https://www.pulsemcp.com/servers/cloudflare-workers) | Deploy MCP servers at the edge | One-click deploy; <5 min setup; KV/D1/R2 storage | Official |
| **Vercel MCP** | Vercel | Next.js-native MCP deployment | `mcp-handler` package; Fluid Compute scaling; OAuth built-in | Active |
| **Netlify MCP** | [PulseMCP](https://www.pulsemcp.com/servers/dynamicendpoints-netlify) | Deploy to Netlify via MCP | Unified hosting provider interface | Active |

### Enterprise and Business Data

| MCP Server | Source | Description | Key Features | Status |
|---|---|---|---|---|
| **K2view MCP** | [k2view.com](https://www.k2view.com/) | Enterprise data access for GenAI | Patented Micro-Database tech; real-time data; unifies SQL + APIs + cloud | Enterprise leader in 2026 |
| **Salesforce MCP** | Salesforce | CRM data for AI agents | Natural language queries; case management; record updates | Official |
| **HubSpot MCP** | Community | Marketing + CRM integration | Contact, deal, and campaign management | Active |
| **Ahrefs MCP** | Ahrefs | SEO data for AI agents | Backlink analysis, keyword research, site audits | Active |
| **Skyvia MCP** | [Skyvia](https://blog.skyvia.com/best-mcp-servers/) | Cloud data integration platform | Data import/export, sync, replication across cloud apps and databases | Active |

### Red Hat MCP Servers (New in 2026)

| MCP Server | Source | Description | Key Features | Status |
|---|---|---|---|---|
| **Red Hat Enterprise Linux MCP** | Red Hat | System telemetry for AI | Root-cause analysis, proactive analytics, system health | New in 2026 |
| **Red Hat Lightspeed MCP** | Red Hat | AI-powered troubleshooting | Natural language system queries in IDE, diagnostics | New in 2026 |

### Design and Content

| MCP Server | Source | Description | Key Features | Status |
|---|---|---|---|---|
| **Canva MCP** | Canva (Official) | Design creation and editing via AI | Create designs, apply templates, generate images | Official |
| **WordPress MCP** | Community | WordPress site management | Post creation, media management, site config | Active |
| **Spotify MCP** | Community | Music integration for AI | Playlist management, track search, playback control | Active |

---

## Key Directories and Registries

| Directory | URL | Description |
|---|---|---|
| **Official MCP Servers Repo** | [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | ~78.7k stars; official reference + community servers |
| **MCP.so** | [mcp.so](https://mcp.so) | 3,000+ MCP servers indexed with quality ratings |
| **mcp-awesome.com** | [mcp-awesome.com](https://mcp-awesome.com/) | 1,200+ quality-verified servers; tutorials + guides |
| **PulseMCP** | [pulsemcp.com/servers](https://www.pulsemcp.com/servers) | 8,230+ servers; updated daily; server.json hosting |
| **MCP Market** | [mcpmarket.com/leaderboards](https://mcpmarket.com/leaderboards) | Top 100 leaderboard by GitHub stars |
| **Glama MCP** | [glama.ai/mcp/servers](https://glama.ai/mcp/servers) | Categorized MCP server directory |
| **Awesome MCP (wong2)** | [github.com/wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) | Curated list; one of the earliest |
| **Awesome MCP (punkpeye)** | [github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Large collection; synced web directory at mcpservers.org |
| **Awesome MCP (appcypher)** | [github.com/appcypher/awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) | Production-ready + experimental servers |
| **Awesome Remote MCP** | [github.com/jaw9c/awesome-remote-mcp-servers](https://github.com/jaw9c/awesome-remote-mcp-servers) | Curated remote/hosted MCP servers (no installation needed) |
| **VS Code MCP Gallery** | [code.visualstudio.com/mcp](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) | In-editor MCP server discovery |
| **MCP Official Spec** | [modelcontextprotocol.io](https://modelcontextprotocol.io) | Protocol specification + docs |
| **MCP Registry** | [github.com/modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry) | Community-driven server registry |
| **LobeHub MCP** | [lobehub.com/mcp](https://lobehub.com/mcp) | LobeChat MCP server marketplace |

---

## Quick Reference: MCP Configuration Patterns

Most MCP servers follow one of these configuration patterns in `claude_desktop_config.json` (or equivalent for Cursor, VS Code, Windsurf, etc.):

### Pattern 1: Node.js / npx (Most Common)

```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "@scope/package-name"],
      "env": {
        "API_KEY": "your-key-here"
      }
    }
  }
}
```

### Pattern 2: Python / uvx

```json
{
  "mcpServers": {
    "server-name": {
      "command": "uvx",
      "args": ["package-name", "--option", "value"]
    }
  }
}
```

### Pattern 3: Docker

```json
{
  "mcpServers": {
    "server-name": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "API_KEY=your-key", "mcp/image-name"]
    }
  }
}
```

### Pattern 4: Remote MCP Server (No Installation)

```json
{
  "mcpServers": {
    "server-name": {
      "url": "https://mcp.example.com",
      "auth": "oauth"
    }
  }
}
```

### Config File Locations

| Client | Config Location |
|---|---|
| **Claude Desktop (macOS)** | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| **Claude Desktop (Windows)** | `%APPDATA%\Claude\claude_desktop_config.json` |
| **Cursor** | `.cursor/mcp.json` in project root or `~/.cursor/mcp.json` |
| **VS Code** | `.vscode/mcp.json` in workspace or user settings |
| **Windsurf** | `~/.codeium/windsurf/mcp_config.json` |

---

## Security Best Practices

1. **Start read-only.** Begin with read-only servers (docs, search, observability) before adding write capabilities.
2. **Scope narrowly.** Use per-project API keys, limit directory access, use dev/test data only for initial setup.
3. **Audit everything.** Log who called what tool and when. Use Sentry or Datadog MCP monitoring.
4. **Validate inputs.** Guard against prompt injection -- a demonstrated real-world risk in 2025 incidents.
5. **Use restricted API keys.** For services like Stripe, create Restricted API Keys with only the permissions you need.
6. **Never expose root.** Never give filesystem MCP access to `/`, `~`, or directories containing secrets.
7. **Monitor MCP servers.** Use Sentry MCP monitoring (one line of instrumentation) or Datadog for observability into MCP server behavior.
8. **Review AGENTS.md files.** Some MCP servers (like Terraform) include `AGENTS.md` files that guide how AI agents should use their tools -- review these for security implications.
9. **Watch for credential leaks.** MCP servers may log API keys or sensitive data. Ensure logging is configured appropriately.
10. **Keep servers updated.** MCP is a fast-moving ecosystem. Pin versions in production but regularly check for security patches.

---

## Recommended Starter Set for Developers

If you are setting up MCP servers for the first time, here is a pragmatic starting point:

| Category | Server | Why |
|---|---|---|
| **Search** | Brave Search MCP | Free tier, privacy-first, no tracking |
| **Docs** | Context7 MCP | Current library docs instead of stale training data |
| **Files** | Filesystem MCP (Official) | Secure, scoped file access |
| **Git** | GitHub MCP (Official) | 80+ tools, official |
| **Memory** | Memory MCP (Official) | Cross-conversation knowledge persistence |
| **Thinking** | Sequential Thinking MCP | Better reasoning for complex problems |
| **Browser** | Playwright MCP (Microsoft) | Deterministic, fast, accessibility-tree based |
| **Database** | PostgreSQL MCP (Official) | Most common production DB |
| **Diagrams** | Mermaid MCP or Draw.io MCP | Quick visual output |

---

## Sources

- [Model Context Protocol Official Site](https://modelcontextprotocol.io)
- [modelcontextprotocol/servers on GitHub](https://github.com/modelcontextprotocol/servers)
- [MCP Specification 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25)
- [Wikipedia - Model Context Protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol)
- [Google Cloud MCP Announcement](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services)
- [Google Launches Managed MCP Servers (TechCrunch)](https://techcrunch.com/2025/12/10/google-is-going-all-in-on-mcp-servers-agent-ready-by-design/)
- [Stripe MCP Documentation](https://docs.stripe.com/mcp)
- [Datadog MCP Server Docs](https://docs.datadoghq.com/bits_ai/mcp_server/)
- [Datadog Remote MCP Server Blog](https://www.datadoghq.com/blog/datadog-remote-mcp-server/)
- [Sentry MCP Server Monitoring](https://blog.sentry.io/introducing-mcp-server-monitoring/)
- [HashiCorp Terraform MCP Server](https://github.com/hashicorp/terraform-mcp-server)
- [Pulumi MCP Server Docs](https://www.pulumi.com/docs/iac/using-pulumi/mcp-server/)
- [Pulumi Remote MCP Server](https://www.pulumi.com/blog/remote-mcp-server/)
- [Apollo GraphQL MCP Server](https://www.apollographql.com/docs/apollo-mcp-server)
- [Figma Dev Mode MCP Guide](https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Dev-Mode-MCP-Server)
- [Microsoft Playwright MCP](https://github.com/microsoft/playwright-mcp)
- [Browserbase MCP Server](https://github.com/browserbase/mcp-server-browserbase)
- [Builder.io - Best MCP Servers for Developers 2026](https://www.builder.io/blog/best-mcp-servers-2026)
- [StackGen - Best MCP Servers for Platform Engineers 2026](https://stackgen.com/blog/the-10-best-mcp-servers-for-platform-engineers-in-2025)
- [Obot AI - Top 15 MCP Servers](https://obot.ai/blog/top-15-mcp-servers/)
- [Skyvia - Top 12 MCP Servers Guide 2026](https://blog.skyvia.com/best-mcp-servers/)
- [K2view - Awesome MCP Servers Directory 2026](https://www.k2view.com/blog/awesome-mcp-servers)
- [InfoWorld - 10 MCP Servers for DevOps](https://www.infoworld.com/article/4096223/10-mcp-servers-for-devops.html)
- [The New Stack - 10 MCP Servers for Frontend Developers](https://thenewstack.io/10-mcp-servers-for-frontend-developers/)
- [Composio - 13 MCP Servers Every Developer Should Know](https://composio.dev/blog/13-mcp-servers-every-developer-should-know)
- [MCP Market Leaderboard](https://mcpmarket.com/leaderboards)
- [PulseMCP Directory](https://www.pulsemcp.com/servers)
- [MCP.so Server Index](https://mcp.so)
- [mcp-awesome.com](https://mcp-awesome.com/)
- [Perplexity MCP Server Docs](https://docs.perplexity.ai/guides/mcp-server)
- [Twilio MCP Server Blog](https://www.twilio.com/en-us/blog/introducing-twilio-alpha-mcp-server)
- [Supabase MCP Docs](https://supabase.com/docs/guides/getting-started/mcp)
- [VS Code MCP Servers Docs](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)
- [Desktop Commander MCP](https://github.com/wonderwhy-er/DesktopCommanderMCP)
- [Atlassian MCP Server](https://github.com/atlassian/atlassian-mcp-server)
- [Google Workspace MCP](https://github.com/taylorwilsdon/google_workspace_mcp)
- [n8n MCP Integration](https://n8n.io/integrations/mcp-client-tool/)
- [n8n MCP Guide for Beginners](https://generect.com/blog/n8n-mcp/)
- [Integrating MCP with Vector Databases (Markaicode)](https://markaicode.com/integrating-mcp-vector-databases/)
- [CyberPress - Top 10 MCP Servers 2025](https://cyberpress.org/best-mcp-servers/)
- [Intuz - Top 10 MCP Servers 2026](https://www.intuz.com/blog/best-mcp-servers)
- [CybersecurityNews - Top 10 MCP Servers 2026](https://cybersecuritynews.com/best-model-context-protocol-mcp-servers/)
- [Pomerium - Best MCP Servers 2025](https://www.pomerium.com/blog/best-model-context-protocol-mcp-servers-in-2025)
- [Desktop Commander Blog - 22 Best MCP Servers](https://desktopcommander.app/blog/2025/11/25/best-mcp-servers/)
- [Awesome MCP Servers (wong2)](https://github.com/wong2/awesome-mcp-servers)
- [Awesome MCP Servers (punkpeye)](https://github.com/punkpeye/awesome-mcp-servers)
- [Awesome MCP Servers (appcypher)](https://github.com/appcypher/awesome-mcp-servers)
