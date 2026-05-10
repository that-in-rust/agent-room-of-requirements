---
name: local-vision-ollama
description: Analyze images using local Ollama vision model (qwen3.5:4b) with automatic pre-resizing and filename sanitization for reliable processing.
version: 1.0.0
author: hermes
model: qwen3.5:4b
---

# Local Vision via Ollama (qwen3.5:4b)

Analyze images locally using the qwen3.5:4b model running on Ollama. Handles the key pitfalls: oversized images causing timeouts, Unicode filenames breaking file paths, and batch processing.

## Architecture

- **Model**: qwen3.5:4b (Q4_K_M, ~3.4 GB)
- **Runtime**: Ollama at `http://localhost:11434`
- **Hardware**: M4 mini 24GB, GPU-accelerated
- **Config**: `~/.hermes/config.yaml` auxiliary.vision section
- **Env vars**: `~/.hermes/.env` AUXILIARY_VISION_* (takes precedence over config.yaml)

## Critical Rules

### 1. ALWAYS Pre-Resize Images Before Analysis

Full-resolution Retina screenshots (10+ MB, 2880x1800+) generate ~6,500+ vision tokens. The ViT prefill is O(n^2) on patch count and WILL timeout at 120s.

Target: **max 800px longest edge**. This produces ~600 tokens, processes in 10-20s instead of 90-120s+.

```bash
# Single image
sips -Z 800 /path/to/input.png --out /tmp/vision_input.png

# Batch - copy and resize all images in a folder
python3 -c "
import os, shutil
src = '/path/to/source/folder'
files = sorted(os.listdir(src), key=lambda f: os.path.getmtime(os.path.join(src, f)))
pngs = [f for f in files if f.lower().endswith(('.png','.jpg','.jpeg','.webp'))]
for i, f in enumerate(pngs):
    src_path = os.path.join(src, f)
    dst = f'/tmp/vision_{i}.png'
    shutil.copy2(src_path, dst)
    os.system(f'sips -Z 800 {dst} --out {dst}')
    print(f'{i}: {f} -> {dst}')
"
```

### 2. Sanitize Unicode Filenames

macOS Finder and screenshot tools use U+202F (narrow no-break space) instead of regular ASCII space in filenames like `Screenshot 2026-04-14 at 4.05.08 PM.png`. This breaks both `cp` and `vision_analyze` file path matching.

**Always use Python's `os.listdir()` + `os.path.join()` to handle these.** Never type or paste filenames from `ls` output.

```python
import os, shutil
files = os.listdir('/path/to/folder')
for f in files:
    if f.endswith('.png'):
        # Use os.path.join - NOT string concatenation with typed names
        full = os.path.join('/path/to/folder', f)
        shutil.copy2(full, f'/tmp/clean_{i}.png')
```

### 3. Use /tmp for Staging

Copy images to `/tmp/` with clean ASCII names before calling `vision_analyze`. This avoids both the Unicode filename issue and gives the vision pipeline a simple path.

### 4. Timeout Awareness

- Default vision timeout: 120s (from config.yaml `auxiliary.vision.timeout`)
- Full-res 10 MB image: ~90-120s (often times out)
- Resized 800px image: ~10-20s (reliable)
- If a single image times out, resize it smaller (try 600px) and retry
- Config can be bumped to 180-240s if needed: `auxiliary.vision.timeout: 240`

## Workflow: Analyze Images from a Folder

1. **Discover files** using Python `os.listdir()` (handles Unicode names)
2. **Sort by preference** (mtime for chronological, name for alphabetical)
3. **Copy to /tmp** with clean names: `/tmp/vision_0.png`, `/tmp/vision_1.png`, etc.
4. **Resize** all to 800px max edge with `sips -Z 800`
5. **Analyze** with `vision_analyze` tool, passing `/tmp/vision_N.png` paths
6. **Process in parallel** when possible (max 2-3 concurrent to avoid GPU contention)

### Example: Analyze 3 Oldest Images

```bash
# Step 1-3: Copy oldest 3 with clean names
python3 -c "
import os, shutil
src = '/path/to/folder'
files = sorted(
    [f for f in os.listdir(src) if f.lower().endswith(('.png','.jpg','.jpeg'))],
    key=lambda f: os.path.getmtime(os.path.join(src, f))
)
for i, f in enumerate(files[:3]):
    shutil.copy2(os.path.join(src, f), f'/tmp/vision_{i}.png')
    print(f'{i}: {repr(f)}')
"

# Step 4: Resize all
sips -Z 800 /tmp/vision_0.png --out /tmp/vision_0.png
sips -Z 800 /tmp/vision_1.png --out /tmp/vision_1.png
sips -Z 800 /tmp/vision_2.png --out /tmp/vision_2.png
```

Then call `vision_analyze` on each `/tmp/vision_N.png`.

## Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Image too large | Timeout (>120s) | Pre-resize to 800px with sips |
| Unicode spaces in filename | "No such file or directory" or "Invalid image source" | Copy to /tmp via Python os.listdir() |
| Too many concurrent requests | GPU OOM or extreme slowdown | Process max 2 at a time |
| PNG not recognized | vision_analyze fails | Ensure file has .png extension in /tmp path |
| vision_analyze uses wrong model | Slow or bad results | Check .env AUXILIARY_VISION_* matches config.yaml |

## Why qwen3.5:4b

- Fits in 24GB M4 with headroom (only 3.4 GB model)
- Full GPU acceleration (~35 tok/s text generation)
- Dynamic resolution ViT -- handles any image aspect ratio
- Good OCR and scene description capability
- Window Attention in ViT reduces compute vs full attention
- Never froze macOS (tested and stable at this size)

## Config Reference

```yaml
# ~/.hermes/config.yaml
auxiliary:
  vision:
    provider: custom
    model: qwen3.5:4b
    base_url: http://localhost:11434/v1
    api_key: no-key-required
    timeout: 120
```

```bash
# ~/.hermes/.env (takes precedence over config.yaml)
AUXILIARY_VISION_PROVIDER=custom
AUXILIARY_VISION_MODEL=qwen3.5:4b
AUXILIARY_VISION_BASE_URL=http://localhost:11434/v1
AUXILIARY_VISION_API_KEY=***
```

Both must agree. If vision routing is wrong, check .env first -- it overrides config.yaml.
