# Phase 1 Quick Start Guide: Bundle Reconnaissance

**Phase:** 1 of 8
**Timeline:** Days 1-2 (2026-02-02 to 2026-02-03)
**Estimated Duration:** 4-6 hours
**Status:** READY TO BEGIN

---

## Objectives

1. Identify the bundler type used to create cli.js
2. Extract module map from the bundled code
3. Document import/export patterns
4. Generate human-readable version of cli.js
5. Create dependency visualization

---

## Prerequisites

### Required Tools (Not Yet Installed)
```bash
npm install -g prettier       # Code beautification
npm install -g restringer     # Deobfuscation (40+ transforms)
npm install -g wakaru         # Bundle unpacking
npm install -g madge          # Dependency visualization
npm install -g @ast-grep/cli  # AST-based code search
```

### Verification Commands
```bash
prettier --version
restringer --version
wakaru --version
madge --version
ast-grep --version
```

---

## Step-by-Step Execution Plan

### Step 1: Install Toolchain (5 minutes)
```bash
cd /Users/amuldotexe/Desktop/A01_20260131/agent-room-of-requirements/referenceRepo

# Install all required tools
npm install -g prettier restringer wakaru madge @ast-grep/cli

# Verify installations
prettier --version && echo "✓ Prettier installed"
restringer --version && echo "✓ REstringer installed"
wakaru --version && echo "✓ Wakaru installed"
madge --version && echo "✓ Madge installed"
ast-grep --version && echo "✓ ast-grep installed"
```

**Expected Output:**
- Each tool should report its version number
- No errors about missing packages

---

### Step 2: Beautify cli.js (10-15 minutes)
```bash
# Beautify the main bundle (WARNING: This will take time due to 11.1MB file size)
prettier package/cli.js > analysis/cli-beautified.js

# Verify output
ls -lh analysis/cli-beautified.js
wc -l analysis/cli-beautified.js

# Extract first 500 lines for quick inspection
head -n 500 analysis/cli-beautified.js > analysis/cli-first-500-lines.js
```

**Expected Output:**
- `cli-beautified.js` should be larger than original (formatting adds whitespace)
- File should have 100,000+ lines (estimate)
- First 500 lines should show readable JavaScript

**What to Look For:**
- Bundler signature in first 100 lines
- Module wrapper patterns
- Copyright/license comments
- Build tool identifiers

---

### Step 3: Identify Bundler Type (15-20 minutes)

#### A. Check for Webpack Signature
```bash
# Search for webpack-specific patterns
grep -n "webpackBootstrap" analysis/cli-beautified.js | head -n 5
grep -n "__webpack_require__" analysis/cli-beautified.js | head -n 5
grep -n "webpackJsonp" analysis/cli-beautified.js | head -n 5
```

**Webpack Indicators:**
- `__webpack_require__` function
- Module ID numeric keys: `{ "123": function(module, exports) {} }`
- `webpackBootstrap` comment
- `installedModules` cache object

#### B. Check for Rollup Signature
```bash
# Search for rollup-specific patterns
grep -n "rollup" analysis/cli-beautified.js | head -n 5
grep -n "createCommonjsModule" analysis/cli-beautified.js | head -n 5
```

**Rollup Indicators:**
- Flatter structure (less nesting)
- `createCommonjsModule` wrappers
- ES6 module syntax preserved in places

#### C. Check for esbuild Signature
```bash
# Search for esbuild-specific patterns
grep -n "esbuild" analysis/cli-beautified.js | head -n 5
grep -n "__commonJS" analysis/cli-beautified.js | head -n 5
grep -n "__toESM" analysis/cli-beautified.js | head -n 5
```

**esbuild Indicators:**
- `__commonJS()` wrapper function
- `__toESM()` for module conversion
- More compact than webpack

#### D. Manual Inspection
```bash
# View first 100 lines for bundler signature
head -n 100 analysis/cli-beautified.js > analysis/bundler-signature.js
```

**Document findings in:** `/analysis/01-bundler-detection.md`

---

### Step 4: Extract Module Map (20-30 minutes)

#### For Webpack Bundles:
```bash
# Extract module definitions (numeric keys)
grep -E "^\s*\"?[0-9]+\"?:\s*function\(" analysis/cli-beautified.js | wc -l

# Extract module IDs and save to file
grep -oE "\"?[0-9]+\"?:\s*function" analysis/cli-beautified.js | \
  sed -E 's/:\s*function//' | \
  sort -n | \
  uniq > analysis/module-ids-webpack.txt

# Count total modules
wc -l analysis/module-ids-webpack.txt
```

#### For All Bundle Types:
```bash
# Search for string literals that might be module paths
ast-grep --pattern 'require("$PATH")' analysis/cli-beautified.js > analysis/require-calls.txt

# Search for import statements
ast-grep --pattern 'import $X from "$PATH"' analysis/cli-beautified.js > analysis/import-statements.txt

# Extract all string literals (may contain file paths)
grep -oE '"[^"]{10,}"' analysis/cli-beautified.js | \
  sort | \
  uniq | \
  head -n 1000 > analysis/string-literals-sample.txt
```

**Create:** `/analysis/module-map.json` with structure:
```json
{
  "bundler": "webpack|rollup|esbuild|unknown",
  "moduleCount": 0,
  "modules": [
    {
      "id": "123",
      "path": "path/to/module",
      "type": "internal|external|core"
    }
  ]
}
```

---

### Step 5: Identify Import/Export Patterns (15 minutes)
```bash
# Find all export patterns
grep -n "exports\." analysis/cli-beautified.js | head -n 50 > analysis/export-patterns.txt
grep -n "module.exports" analysis/cli-beautified.js | head -n 50 >> analysis/export-patterns.txt

# Find require() patterns
grep -n "require(" analysis/cli-beautified.js | head -n 50 > analysis/require-patterns.txt

# Find import patterns (if any ES6)
grep -n "import " analysis/cli-beautified.js | head -n 50 > analysis/import-patterns.txt
```

**Document findings in:** `/analysis/01-import-export-patterns.md`

---

### Step 6: Generate Dependency Graph (10-15 minutes)
```bash
# Attempt dependency visualization (may fail on minified code)
madge analysis/cli-beautified.js --image analysis/dependency-graph.svg

# If fails, try with specific format
madge analysis/cli-beautified.js --format amd --image analysis/dependency-graph-amd.svg
madge analysis/cli-beautified.js --format cjs --image analysis/dependency-graph-cjs.svg

# Generate JSON output
madge analysis/cli-beautified.js --json > analysis/dependency-graph.json

# Generate text summary
madge analysis/cli-beautified.js --summary > analysis/dependency-summary.txt
```

**Expected Output:**
- SVG file with visual dependency graph (if successful)
- JSON file with dependency tree
- Summary with circular dependency warnings (if any)

**Note:** Madge may struggle with heavily bundled code. If it fails, document why and move on.

---

### Step 7: Search for Tool References (20 minutes)

Search for the 20 tools identified in sdk-tools.d.ts:

```bash
# Create search script
cat > analysis/search-tools.sh << 'EOF'
#!/bin/bash
TOOLS=(
  "AgentInput"
  "BashInput"
  "TaskOutputInput"
  "ExitPlanModeInput"
  "FileEditInput"
  "FileReadInput"
  "FileWriteInput"
  "GlobInput"
  "GrepInput"
  "TaskStopInput"
  "ListMcpResourcesInput"
  "McpInput"
  "NotebookEditInput"
  "ReadMcpResourceInput"
  "TodoWriteInput"
  "WebFetchInput"
  "WebSearchInput"
  "AskUserQuestionInput"
  "ConfigInput"
)

for tool in "${TOOLS[@]}"; do
  count=$(grep -c "$tool" analysis/cli-beautified.js)
  echo "$tool: $count occurrences"
done
EOF

chmod +x analysis/search-tools.sh
./analysis/search-tools.sh > analysis/tool-references.txt
```

**Document findings in:** `/analysis/01-tool-reference-locations.md`

---

### Step 8: Extract Entry Point (10 minutes)
```bash
# Find main entry point
tail -n 100 analysis/cli-beautified.js > analysis/entry-point-last-100.js

# Look for shebang
head -n 5 package/cli.js

# Search for process.argv usage (CLI entry point)
grep -n "process.argv" analysis/cli-beautified.js | head -n 20 > analysis/argv-usage.txt

# Search for commander/yargs (common CLI libraries)
grep -in "commander\|yargs\|minimist" analysis/cli-beautified.js | head -n 10
```

**Document findings in:** `/analysis/01-entry-point-analysis.md`

---

## Deliverables Checklist

After completing all steps, you should have:

- [ ] `/analysis/cli-beautified.js` - Formatted source (~15-20MB estimated)
- [ ] `/analysis/cli-first-500-lines.js` - Quick reference snippet
- [ ] `/analysis/01-bundler-detection.md` - Bundler identification report
- [ ] `/analysis/01-bundle-structure.md` - Complete bundle analysis
- [ ] `/analysis/module-map.json` - Extracted module metadata
- [ ] `/analysis/module-ids-webpack.txt` - Module ID list (if webpack)
- [ ] `/analysis/dependency-graph.svg` - Visual dependency map (if successful)
- [ ] `/analysis/dependency-graph.json` - Dependency data
- [ ] `/analysis/01-import-export-patterns.md` - Module pattern documentation
- [ ] `/analysis/tool-references.txt` - Tool occurrence counts
- [ ] `/analysis/01-tool-reference-locations.md` - Tool location mapping
- [ ] `/analysis/01-entry-point-analysis.md` - Entry point documentation

---

## Success Criteria

Phase 1 is complete when:

1. ✅ Bundler type identified with >80% confidence
2. ✅ Module structure documented (even if partially)
3. ✅ Entry point identified
4. ✅ At least 10/20 tools located in code
5. ✅ Human-readable version of cli.js created
6. ✅ All deliverables created

---

## Expected Challenges & Solutions

### Challenge 1: Prettier Fails on Large File
**Symptom:** Out of memory error or timeout
**Solution:**
```bash
# Increase Node memory limit
NODE_OPTIONS="--max-old-space-size=8192" prettier package/cli.js > analysis/cli-beautified.js
```

### Challenge 2: Heavy Obfuscation
**Symptom:** Variable names like `a`, `b`, `c` everywhere
**Solution:**
```bash
# Use REstringer for deobfuscation
restringer package/cli.js -o analysis/cli-deobfuscated.js

# Then beautify the deobfuscated version
prettier analysis/cli-deobfuscated.js > analysis/cli-beautified-deobf.js
```

### Challenge 3: Madge Fails
**Symptom:** "Cannot parse file" error
**Solution:**
- Document that madge failed
- Manually trace dependencies from require/import statements
- Use ast-grep for targeted searches instead

### Challenge 4: Can't Identify Bundler
**Symptom:** No clear webpack/rollup/esbuild signatures
**Solution:**
- Check package.json build scripts
- Look for build tool in devDependencies
- Document as "custom bundler" and proceed with manual analysis

---

## Time Estimates

| Task | Estimated Time |
|------|----------------|
| Install toolchain | 5 minutes |
| Beautify cli.js | 10-15 minutes |
| Identify bundler | 15-20 minutes |
| Extract module map | 20-30 minutes |
| Import/export patterns | 15 minutes |
| Dependency graph | 10-15 minutes |
| Search tool references | 20 minutes |
| Extract entry point | 10 minutes |
| **Total** | **~2-2.5 hours** |

Add 1-2 hours for documentation and unexpected issues.

**Total Phase 1 Duration:** 3-4 hours

---

## Next Phase Preview

After Phase 1 completion, Phase 2 will:
- Use module map to locate tool implementations
- Trace execution flow from CLI entry to tool execution
- Document ripgrep and WASM integration patterns
- Create detailed flow diagrams for each of 20 tools

**Phase 2 Prerequisites:**
- Beautified, readable code (from Phase 1)
- Module map (from Phase 1)
- Entry point identified (from Phase 1)
- Tool reference locations (from Phase 1)

---

**Created:** 2026-02-01
**Status:** Ready to Execute
**Estimated Completion:** 2026-02-03 (if started 2026-02-02)
