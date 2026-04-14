# design-drift — Claude Code Build Spec

> Hand this document to Claude Code and say: "Build this project exactly as specified."

---

## What we're building

A Claude Code plugin called **design-drift** that:
1. Covers **121 unique brands** by combining ihlamury/design-skills (87 brands) with VoltAgent/awesome-design-md (59 brands, MIT licensed)
2. When both sources exist for a brand → full enrichment (constraint rules + visual tokens together)
3. When only SKILL.md exists → constraint-only enforcement (MUST/SHOULD/NEVER)
4. When only DESIGN.md exists → token-only enforcement (colors, fonts, spacing extracted at runtime)
5. Uses a `PostToolUse` hook with a **fully dynamic scanner** — no hardcoded brand data anywhere
6. Is installable as a Claude Code plugin from a single GitHub repo

**The positioning:** awesome-design-md gives you inspiration. design-drift gives you enforcement. Together they cover 121 brands — more than either alone.

---

## Brand coverage matrix

### Full enrichment — 25 brands (SKILL.md + DESIGN.md)
Both sources loaded, tokens enriched from both constraint rules and visual atmosphere.

airbnb, airtable, anthropic, apple, cal, discord, figma, framer, github, intercom, linear, miro, monzo, notion, openai, pinterest, posthog, raycast, resend, shopify, slack, spotify, stripe, supabase, vercel

### Constraint-only — 62 brands (SKILL.md only)
MUST/SHOULD/NEVER rules enforced. No DESIGN.md available from awesome-design-md.

amplitude, arc, ashby, awwwards, bear, beehiiv, brex, clerk, coda, codeium, convertkit, convex, copy-ai, craft, deel, descript, dribbble, front, ghost, gumroad, gusto, hugging-face, jasper, lattice, launchdarkly, lemonsqueezy, liveblocks, loom, loops, mailchimp, matter, mem, mercury, mixpanel, mobbin, n26, neon, obsidian, paddle, pitch, plaid, planetscale, railway, ramp, readwise, replit, retool, rippling, robinhood, segment, shortcut, substack, superhuman, things, ticktick, tldraw, todoist, upstash, warp, webflow, weights-biases, wise

### Token-only — 34 brands (DESIGN.md only)
Colors, fonts, spacing extracted dynamically. No bundled SKILL.md.

binance, bmw, bugatti, clay, clickhouse, cohere, coinbase, composio, cursor, elevenlabs, expo, ferrari, ibm, lamborghini, lovable, meta, minimax, mintlify, mistral, mongodb, nike, renault, replicate, revolut, runway, sanity, sentry, spacex, tesla, the-verge, uber, voltagent, wired, zapier

---

## Repo to create

`ihlamury/design-drift` (new GitHub repo, public, MIT license)

---

## Complete directory structure

```
design-drift/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── lock/
│   │   └── SKILL.md
│   ├── check/
│   │   └── SKILL.md
│   ├── diff/
│   │   └── SKILL.md
│   ├── fetch/
│   │   └── SKILL.md
│   └── brands/
│       └── [87 brand directories, each with SKILL.md]
├── hooks/
│   ├── hooks.json
│   └── scripts/
│       └── drift-scanner.py
├── agents/
│   └── drift-guard.md
├── README.md
└── .gitignore
```

---

## File contents

### `.claude-plugin/plugin.json`

```json
{
  "name": "design-drift",
  "description": "Lock your design system, prevent drift. 121 brands. Enforces constraints on every UI write via PostToolUse hooks. Powered by ihlamury/design-skills + VoltAgent/awesome-design-md.",
  "version": "1.0.0",
  "author": {
    "name": "Yagiz Ihlamur",
    "url": "https://github.com/ihlamury"
  },
  "homepage": "https://github.com/ihlamury/design-drift",
  "repository": "https://github.com/ihlamury/design-drift",
  "license": "MIT",
  "keywords": ["design-system", "ui", "vibe-coding", "design-drift", "claude-code"]
}
```

---

### `skills/lock/SKILL.md`

```markdown
---
name: lock
description: Lock a brand design system for the session. Activates drift enforcement on all subsequent UI writes. Supports 121 brands. Usage: /design-drift:lock [brand].
---

# Design Drift — Lock

The user has invoked `/design-drift:lock $ARGUMENTS`.

## Source resolution logic

design-drift pulls from two sources. Use both when available, fall back gracefully.

| Sources available | Behavior |
|-------------------|----------|
| SKILL.md ✓ + DESIGN.md ✓ | Full enrichment: MUST/SHOULD/NEVER constraints + visual tokens from both |
| SKILL.md ✓ + DESIGN.md ✗ | Constraint-only: MUST/SHOULD/NEVER rules, tokens extracted from SKILL.md |
| SKILL.md ✗ + DESIGN.md ✓ | Token-only: colors, fonts, spacing extracted from DESIGN.md |
| SKILL.md ✗ + DESIGN.md ✗ | Fail with helpful message |

## Steps

1. **Attempt to fetch DESIGN.md** from awesome-design-md:
   ```
   https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/design-md/$ARGUMENTS/DESIGN.md
   ```
   - If successful: create `.design-cache/` directory in project root, write content to `.design-cache/$ARGUMENTS.md`
   - If failed: continue silently, note in the lock summary

2. **Check for bundled SKILL.md** at `skills/brands/$ARGUMENTS/SKILL.md` in the plugin directory.

3. **If both fail**: tell the user "$ARGUMENTS not found in design-skills (87 brands) or awesome-design-md (59 brands). Check the brand name." Stop.

4. **Determine coverage tier**:
   - Both sources: "Full enrichment"
   - SKILL.md only: "Constraint-only"
   - DESIGN.md only: "Token-only"

5. **Write `.design-lock`** to the project root:
   ```
   BRAND=$ARGUMENTS
   LOCKED_AT=<current ISO timestamp>
   SOURCE=design-drift
   HAS_SKILL=<true|false>
   HAS_DESIGN_MD=<true|false>
   ```

6. **Display lock summary**:
   - Brand + coverage tier
   - Top colors extracted (up to 8 hex values)
   - Font family names found
   - Spacing grid if found
   - Top 5 MUST rules (from SKILL.md if available)
   - Top 3 NEVER rules (from SKILL.md if available)
   - 1-line atmosphere description (from DESIGN.md if available)

7. **Confirm**:
   ```
   ✓ Design lock active: [brand] ([tier])
   Drift scanner enforcing on every UI write.
   Run /design-drift:check to audit existing files.
   ```

## Notes
- `.design-lock` and `.design-cache/` are session-local — both in `.gitignore`
- The scanner reads tokens dynamically from these files at runtime. No hardcoded data.
- awesome-design-md brand slugs may differ from design-skills slugs. Try common variations if first fetch fails (e.g. "cal.com" vs "cal", "linear.app" vs "linear").
```

---

### `skills/check/SKILL.md`

```markdown
---
name: check
description: Audit existing UI files against the locked design system. Returns compliance report with violations and fixes. Supports all 121 brands.
---

# Design Drift — Check

The user has invoked `/design-drift:check $ARGUMENTS`.

## Steps

1. **Read `.design-lock`**. If missing, tell user to run `/design-drift:lock [brand]` first.

2. **Determine scope**:
   - $ARGUMENTS specifies file/dir → scan that only
   - No arguments → scan `**/*.css`, `**/*.scss`, `**/*.tsx`, `**/*.jsx`, `**/*.html`, `**/*.vue`, `**/*.svelte`
   - Always exclude: `node_modules/`, `dist/`, `build/`, `.next/`, `.nuxt/`, `coverage/`

3. **Load design system** from available sources:
   - `skills/brands/[brand]/SKILL.md` (if exists)
   - `.design-cache/[brand].md` (if exists)
   If neither exists, prompt re-run of `/design-drift:lock [brand]`.

4. **Check each file** for:
   - **Color violations** — hardcoded hex/rgb not in design system
   - **Typography violations** — font-family not matching design system fonts
   - **Spacing violations** — values not on the detected grid
   - **Border radius violations** — values not in the detected scale
   - **NEVER rule violations** — patterns explicitly prohibited in SKILL.md

5. **Output compliance report**:
   ```
   Design Drift Report — [brand] ([tier])
   ──────────────────────────────────────
   Scanned: [N] files
   Compliant: [N] files
   Violations: [N] total

   VIOLATIONS
   ──────────
   src/components/Button.tsx:14
     ✗ color: #333333 — not in [brand] design system
       → Closest: #0A2540 | or use a CSS variable

   src/styles/global.css:8
     ✗ font-family: 'Arial' — [brand] uses [extracted fonts]
       → Use: [font stack]
   ```

6. Offer auto-fix: "Fix all violations? Or select specific files."
```

---

### `skills/diff/SKILL.md`

```markdown
---
name: diff
description: Token-by-token diff of a file against the locked design system. Usage: /design-drift:diff [file].
---

# Design Drift — Diff

The user has invoked `/design-drift:diff $ARGUMENTS`.

## Steps

1. Read `.design-lock`. If missing, ask user to lock first.
2. Load file from $ARGUMENTS. If none specified, ask.
3. Extract all tokens: colors, font-family, font-size, font-weight, spacing, border-radius, transitions.
4. Load design system from `.design-cache/[brand].md` + `skills/brands/[brand]/SKILL.md`.
5. Classify each token:
   - ✓ COMPLIANT — found in design system
   - ~ CLOSE — right property, slightly off value
   - ✗ DRIFT — not found, show correct alternative
6. Output diff table:
   ```
   Token Diff — [filename] vs [brand]
   ───────────────────────────────────────────────
   Property       | Found      | Expected   | Status
   ───────────────────────────────────────────────
   background     | #ffffff    | in palette | ✓ OK
   color          | #1a1a1a    | #0A2540    | ✗ DRIFT
   font-family    | 'Arial'    | [brand]    | ✗ DRIFT
   border-radius  | 12px       | 8px        | ✗ DRIFT
   padding        | 24px       | 24px       | ✓ OK
   ```
7. Summary: "[N] compliant, [N] close, [N] drifted."
```

---

### `skills/fetch/SKILL.md`

```markdown
---
name: fetch
description: Preview a DESIGN.md from awesome-design-md for any brand. Does not activate enforcement. Usage: /design-drift:fetch [brand].
---

# Design Drift — Fetch

The user has invoked `/design-drift:fetch $ARGUMENTS`.

## Steps

1. Fetch from: `https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/design-md/$ARGUMENTS/DESIGN.md`

2. If found: display content, show quick summary (colors, fonts, description), offer to lock.

3. If not found:
   - Check if bundled SKILL.md exists locally
   - If yes: "No DESIGN.md in awesome-design-md, but constraint SKILL.md exists. Run /design-drift:lock $ARGUMENTS."
   - If no: "Not found in either source. Check brand name."

Attribution: "Design system from VoltAgent/awesome-design-md (MIT License)"
```

---

### `hooks/hooks.json`

```json
{
  "hooks": [
    {
      "event": "PostToolUse",
      "tools": ["Write", "Edit", "MultiEdit"],
      "command": "python3 $PLUGIN_DIR/hooks/scripts/drift-scanner.py"
    }
  ]
}
```

---

### `hooks/scripts/drift-scanner.py`

```python
#!/usr/bin/env python3
"""
design-drift PostToolUse hook — dynamic scanner.

Reads .design-lock, loads SKILL.md and/or cached DESIGN.md for the active brand,
extracts tokens at runtime, checks written content for violations.

No hardcoded brand data. Works with all 121 brands.
"""

import json
import sys
import os
import re
from pathlib import Path


# ── File targeting ────────────────────────────────────────────────────────────

UI_EXTENSIONS = {".css", ".scss", ".sass", ".tsx", ".jsx", ".html", ".vue", ".svelte"}
SKIP_DIRS = {"node_modules", "dist", "build", ".next", ".nuxt", "coverage", ".git"}

def is_ui_file(filepath: str) -> bool:
    p = Path(filepath)
    if any(part in SKIP_DIRS for part in p.parts):
        return False
    return p.suffix in UI_EXTENSIONS


# ── Lock file ─────────────────────────────────────────────────────────────────

def find_lock() -> tuple:
    """Walk up from CWD to find .design-lock. Returns (project_root, config)."""
    cwd = Path(os.getcwd())
    for parent in [cwd] + list(cwd.parents):
        lock = parent / ".design-lock"
        if lock.exists():
            config = {}
            for line in lock.read_text().splitlines():
                if "=" in line:
                    k, v = line.split("=", 1)
                    config[k.strip()] = v.strip()
            return parent, config
    return None, {}


# ── Design system loading ─────────────────────────────────────────────────────

def load_design_system(brand: str, project_root: Path, plugin_dir: str) -> str:
    """
    Load full design system text for the active brand.

    Two sources, both optional, additive when combined:
      1. SKILL.md  — constraint layer (MUST/SHOULD/NEVER + token tables)
      2. DESIGN.md — atmosphere layer (visual tokens from awesome-design-md, cached at lock time)

    Token extraction runs against the combined text regardless of which sources are present.
    This means:
      - Full enrichment brands (both): richest token set, full constraint enforcement
      - Constraint-only brands (SKILL.md only): tokens from SKILL.md tables
      - Token-only brands (DESIGN.md only): tokens from DESIGN.md CSS values
    """
    parts = []

    skill_path = Path(plugin_dir) / "skills" / "brands" / brand / "SKILL.md"
    if skill_path.exists():
        parts.append(skill_path.read_text())

    cached = project_root / ".design-cache" / f"{brand}.md"
    if cached.exists():
        parts.append(cached.read_text())

    return "\n\n".join(parts)


# ── Token extraction ──────────────────────────────────────────────────────────

def extract_tokens(design_text: str) -> dict:
    """
    Parse DESIGN.md / SKILL.md text and extract tokens dynamically.
    Works against both formats — no brand-specific logic anywhere.
    """
    tokens = {
        "colors": set(),
        "fonts": set(),
        "spacing_grid": None,
        "border_radius": set(),
        "never_rules": [],
        "must_rules": [],
    }

    if not design_text:
        return tokens

    lines = design_text.splitlines()

    # Hex colors — scan entire document
    hex_pat = re.compile(r'#([0-9a-fA-F]{3,8})\b')
    for line in lines:
        for h in hex_pat.findall(line):
            full = "#" + "".join(c * 2 for c in h.upper()) if len(h) == 3 else f"#{h.upper()}"
            tokens["colors"].add(full)

    # rgb() colors → hex
    rgb_pat = re.compile(r'rgb\(\s*(\d+),\s*(\d+),\s*(\d+)\s*\)')
    for line in lines:
        for m in rgb_pat.finditer(line):
            r, g, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
            tokens["colors"].add(f"#{r:02X}{g:02X}{b:02X}")

    # Font families — patterns present in both SKILL.md tables and DESIGN.md CSS blocks
    font_pats = [
        re.compile(r"font.family\s*[:\|]\s*[`'\"]?([A-Za-z][\w\s\-]+)", re.IGNORECASE),
        re.compile(r"MUST use [`'\"]([A-Za-z][\w\s\-]+)[`'\"] as primary font", re.IGNORECASE),
        re.compile(r"Font Famil(?:y|ies)[^\n]*[`'\"]([A-Za-z][\w\s\-]+)[`'\"]", re.IGNORECASE),
        re.compile(r"\|\s*`([A-Za-z][\w\s\-]+)`\s*\|.*[Ff]ont"),
    ]
    for line in lines:
        for pat in font_pats:
            for m in pat.finditer(line):
                font = m.group(1).strip().strip("'\"` ")
                if 2 <= len(font) <= 40 and not font.lower().startswith("var("):
                    tokens["fonts"].add(font)

    # Spacing grid
    grid_pats = [
        re.compile(r'MUST use (\d+)px grid', re.IGNORECASE),
        re.compile(r'(\d+)px grid for spacing', re.IGNORECASE),
        re.compile(r'spacing.*?grid.*?(\d+)px', re.IGNORECASE),
        re.compile(r'Grid[^\n]*:\s*(\d+)px', re.IGNORECASE),
    ]
    for line in lines:
        for pat in grid_pats:
            m = pat.search(line)
            if m and tokens["spacing_grid"] is None:
                val = int(m.group(1))
                if val in (2, 4, 8, 10, 16):
                    tokens["spacing_grid"] = val
                    break

    # Border-radius — only from lines mentioning border-radius
    radius_px = re.compile(r'\b(\d+)px\b')
    in_radius = False
    for line in lines:
        lower = line.lower()
        if "border" in lower and "radius" in lower:
            in_radius = True
        elif in_radius and line.strip().startswith("#"):
            in_radius = False
        if in_radius:
            for m in radius_px.finditer(line):
                val = int(m.group(1))
                if 0 <= val <= 64:
                    tokens["border_radius"].add(val)

    # NEVER and MUST rules
    never_re = re.compile(r'^[-*]?\s*NEVER\s+(.+)$', re.IGNORECASE)
    must_re = re.compile(r'^[-*]?\s*MUST\s+(.+)$', re.IGNORECASE)
    for line in lines:
        m = never_re.match(line.strip())
        if m:
            tokens["never_rules"].append(m.group(1).strip())
        m = must_re.match(line.strip())
        if m:
            tokens["must_rules"].append(m.group(1).strip())

    return tokens


# ── Content scanning ──────────────────────────────────────────────────────────

def scan(content: str, tokens: dict, filepath: str, brand: str) -> list:
    violations = []
    lines = content.splitlines()

    if not tokens["colors"] and not tokens["fonts"] and not tokens["border_radius"]:
        return []

    colors_lower = {c.lower() for c in tokens["colors"]}
    hex_pat = re.compile(r'#([0-9a-fA-F]{3,8})\b')

    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped or stripped.startswith(("//", "*", "/*", "<!--", "#")):
            continue
        if re.match(r'--[\w-]+\s*:', stripped):
            continue

        # Color check
        for h in hex_pat.findall(line):
            full = "#" + "".join(c * 2 for c in h.upper()) if len(h) == 3 else f"#{h.upper()}"
            if full.lower() not in colors_lower:
                hint = _closest_color(full, tokens["colors"])
                violations.append({
                    "line": i, "type": "color", "severity": "error",
                    "message": f"Color {full} not in {brand} design system",
                    "hint": f"Use {hint} or a CSS variable",
                })

        # Font check
        if tokens["fonts"] and "font-family" in stripped.lower():
            if not any(f.lower() in stripped.lower() for f in tokens["fonts"]) and "var(--" not in stripped:
                violations.append({
                    "line": i, "type": "font", "severity": "warning",
                    "message": f"font-family may not match {brand} spec",
                    "hint": f"{brand} uses: {', '.join(list(tokens['fonts'])[:3])}",
                })

        # Spacing grid check
        if tokens["spacing_grid"]:
            grid = tokens["spacing_grid"]
            if any(p in stripped.lower() for p in ("padding", "margin", "gap", "top:", "left:", "right:", "bottom:")):
                for val_str in re.findall(r'\b(\d+)px\b', stripped):
                    val = int(val_str)
                    if val > 0 and val % grid != 0:
                        violations.append({
                            "line": i, "type": "spacing", "severity": "warning",
                            "message": f"{val}px breaks {brand} {grid}px grid",
                            "hint": f"Use {_snap_to_grid(val, grid)}px",
                        })

        # Border-radius check
        if tokens["border_radius"] and "border-radius" in stripped.lower():
            for val_str in re.findall(r'\b(\d+)px\b', stripped):
                val = int(val_str)
                if val != 0 and val not in tokens["border_radius"]:
                    closest = min(tokens["border_radius"], key=lambda x: abs(x - val))
                    violations.append({
                        "line": i, "type": "border-radius", "severity": "warning",
                        "message": f"border-radius {val}px not in {brand} scale {sorted(tokens['border_radius'])}",
                        "hint": f"Use {closest}px",
                    })

    errors = [v for v in violations if v["severity"] == "error"]
    warnings = [v for v in violations if v["severity"] == "warning"]
    return errors[:5] + warnings[:3]


# ── Helpers ───────────────────────────────────────────────────────────────────

def _hex_to_rgb(h: str) -> tuple:
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)

def _color_distance(a: str, b: str) -> float:
    try:
        r1, g1, b1 = _hex_to_rgb(a)
        r2, g2, b2 = _hex_to_rgb(b)
        return ((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2) ** 0.5
    except Exception:
        return 999.0

def _closest_color(target: str, palette: set) -> str:
    return min(palette, key=lambda c: _color_distance(target, c)) if palette else target

def _snap_to_grid(val: int, grid: int) -> int:
    lower = (val // grid) * grid
    upper = lower + grid
    return lower if (val - lower) <= (upper - val) else upper

def _format_output(violations: list, filepath: str, brand: str) -> str:
    if not violations:
        return ""
    lines = [f"\n⚠️  design-drift [{brand}] — {len(violations)} violation(s) in {Path(filepath).name}"]
    for v in violations:
        icon = "✗" if v["severity"] == "error" else "~"
        lines.append(f"   {icon} Line {v['line']} ({v['type']}): {v['message']}")
        lines.append(f"     → {v['hint']}")
    lines.append(f"\n   Run /design-drift:check for full audit.")
    return "\n".join(lines)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    try:
        raw = sys.stdin.read()
        tool_result = json.loads(raw) if raw.strip() else {}
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)

    if tool_result.get("tool_name", "") not in ("Write", "Edit", "MultiEdit"):
        sys.exit(0)

    tool_input = tool_result.get("tool_input", {})
    filepath = tool_input.get("file_path") or tool_input.get("path", "")
    if not filepath or not is_ui_file(filepath):
        sys.exit(0)

    project_root, config = find_lock()
    if not config:
        sys.exit(0)

    brand = config.get("BRAND", "").lower().strip()
    if not brand:
        sys.exit(0)

    plugin_dir = os.environ.get(
        "PLUGIN_DIR",
        str(Path(os.path.abspath(__file__)).parent.parent.parent)
    )

    design_text = load_design_system(brand, project_root, plugin_dir)
    tokens = extract_tokens(design_text)

    content = (
        tool_input.get("content")
        or tool_input.get("new_content")
        or tool_input.get("new_string")
        or ""
    )
    if not content:
        sys.exit(0)

    violations = scan(content, tokens, filepath, brand)
    if violations:
        print(_format_output(violations, filepath, brand), file=sys.stderr)

    sys.exit(0)


if __name__ == "__main__":
    main()
```

---

### `agents/drift-guard.md`

```markdown
---
name: drift-guard
description: Autonomous design enforcement agent. Activates when .design-lock is present. Silently watches UI writes and surfaces only real violations.
model: claude-sonnet-4-20250514
---

You are drift-guard, a specialized design consistency agent.

When activated:
1. Check for `.design-lock` in the project root
2. If found, load constraints from `skills/brands/[brand]/SKILL.md` (if exists) and `.design-cache/[brand].md` (if exists)
3. Monitor all UI file changes during the session
4. After any write to a UI file, silently verify compliance
5. Surface only violations that would be user-visible (wrong color, wrong font, broken spacing)

Operating principles:
- Silent when compliant. Only speak when there is a real violation.
- Always provide the correct value, never just flag the problem.
- Batch violations — wait for a logical chunk before interrupting.
- Reference the brand: "This breaks the Linear constraint on border-radius. Linear uses 6px or 8px only."

Tools: Read, Write, Edit.
```

---

### `skills/brands/` — all 87 brands

**Instructions for Claude Code:**

For each brand in the list below, fetch the SKILL.md from `ihlamury/design-skills` and save to `skills/brands/[brand]/SKILL.md`. Append the note block at the end of each file.

Fetch URL pattern: `https://raw.githubusercontent.com/ihlamury/design-skills/main/skills/[brand]/SKILL.md`

**All 87 brands to fetch:**

airbnb, airtable, amplitude, anthropic, apple, arc, ashby, awwwards, bear, beehiiv, brex, cal, clerk, coda, codeium, convertkit, convex, copy-ai, craft, deel, descript, discord, dribbble, figma, framer, front, ghost, github, gumroad, gusto, hugging-face, intercom, jasper, lattice, launchdarkly, lemonsqueezy, linear, liveblocks, loom, loops, mailchimp, matter, mem, mercury, miro, mixpanel, mobbin, monzo, n26, neon, notion, obsidian, openai, paddle, pinterest, pitch, plaid, planetscale, posthog, railway, ramp, raycast, readwise, replit, resend, retool, rippling, robinhood, segment, shopify, shortcut, slack, spotify, stripe, substack, supabase, superhuman, things, ticktick, tldraw, todoist, upstash, vercel, warp, webflow, weights-biases, wise

**Append to end of every fetched file:**

```markdown
## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/[brand]

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
```

---

### `README.md`

````markdown
# design-drift

> Lock your design system. Enforce it automatically. Stop AI drift.

**design-drift** is a Claude Code plugin that prevents AI agents from drifting
away from your design system — in real time, on every write.

```
ihlamury/design-skills   →   87 brands, MUST/SHOULD/NEVER constraint layer
VoltAgent/awesome-design-md  →   59 brands, visual atmosphere + token layer
design-drift             →   121 brands total, enforcement on every UI write
```

## Install

```bash
claude --plugin-dir https://github.com/ihlamury/design-drift
# or
/plugin install design-drift@ihlamury
```

## Usage

```bash
/design-drift:lock linear      # lock a brand
/design-drift:check            # audit all UI files
/design-drift:diff src/Button.tsx  # token diff on one file
/design-drift:fetch cursor     # preview any brand's DESIGN.md
```

Once locked, the drift scanner fires automatically on every Write/Edit. No prompting needed.

## Brand coverage — 121 brands

### Full enrichment (25) — SKILL.md + DESIGN.md
airbnb · airtable · anthropic · apple · cal · discord · figma · framer · github · intercom · linear · miro · monzo · notion · openai · pinterest · posthog · raycast · resend · shopify · slack · spotify · stripe · supabase · vercel

### Constraint-only (62) — SKILL.md
amplitude · arc · ashby · awwwards · bear · beehiiv · brex · clerk · coda · codeium · convertkit · convex · copy-ai · craft · deel · descript · dribbble · front · ghost · gumroad · gusto · hugging-face · jasper · lattice · launchdarkly · lemonsqueezy · liveblocks · loom · loops · mailchimp · matter · mem · mercury · mixpanel · mobbin · n26 · neon · obsidian · paddle · pitch · plaid · planetscale · railway · ramp · readwise · replit · retool · rippling · robinhood · segment · shortcut · substack · superhuman · things · ticktick · tldraw · todoist · upstash · warp · webflow · weights-biases · wise

### Token-only (34) — DESIGN.md via awesome-design-md
binance · bmw · bugatti · clay · clickhouse · cohere · coinbase · composio · cursor · elevenlabs · expo · ferrari · ibm · lamborghini · lovable · meta · minimax · mintlify · mistral · mongodb · nike · renault · replicate · revolut · runway · sanity · sentry · spacex · tesla · the-verge · uber · voltagent · wired · zapier

## How it works

**1. Lock** — `/design-drift:lock stripe`
Fetches DESIGN.md from awesome-design-md → cached to `.design-cache/stripe.md`
Loads bundled SKILL.md constraint layer → `skills/brands/stripe/SKILL.md`
Writes `.design-lock` with brand + coverage tier

**2. Enforce** — automatic on every write
`PostToolUse` hook fires after every Write/Edit to a UI file
Scanner reads `.design-lock`, loads available sources (SKILL.md + cached DESIGN.md)
Tokens extracted dynamically — colors, fonts, spacing grid, border-radius
Violations surface inline with line numbers and exact fix hints

**3. Audit** — `/design-drift:check`
Scans all UI files, returns structured violation report, offers auto-fix

## Why dynamic extraction

The scanner has zero hardcoded brand data. It parses whatever SKILL.md and DESIGN.md
text is available and extracts tokens at runtime. Adding a new brand requires only
adding a SKILL.md — no scanner changes needed.

## Powered by

- [ihlamury/design-skills](https://github.com/ihlamury/design-skills) — 87 brands, constraint enforcement layer
- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) — 59 brands, DESIGN.md layer (MIT)

## License

MIT
````

---

### `.gitignore`

```
.design-lock
.design-cache/
__pycache__/
*.pyc
.DS_Store
```

---
```

---

## After the build — launch sequence

| Step | Action |
|------|--------|
| 1 | Push `ihlamury/design-drift` to GitHub (public, MIT) |
| 2 | End-to-end test: lock linear → write wrong hex → confirm hook fires |
| 3 | Record 30s screen recording: lock → write → violation caught inline |
| 4 | Post on X: "Built a Claude Code plugin that catches design drift in real time. 121 brands. DESIGN.md gives inspiration. design-drift enforces the rules." + recording |
| 5 | Open issue on VoltAgent/awesome-design-md: "Built constraint enforcement on top of your token layer — cross-reference?" |
| 6 | LinkedIn message to VoltAgent Turkish co-founder |
| 7 | Submit to anthropics/claude-plugins-official via platform.claude.com/plugins/submit |
| 8 | PR to VoltAgent/awesome-agent-skills under Design & UI |

---

## Attribution

- `ihlamury/design-skills` (MIT) — 87 brand SKILL.md files, constraint enforcement layer
- `VoltAgent/awesome-design-md` (MIT) — 59 brand DESIGN.md files, fetched on-demand and cached at lock time
```