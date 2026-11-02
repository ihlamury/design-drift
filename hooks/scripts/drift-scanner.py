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

def find_lock(filepath: str) -> tuple:
    """Walk up from the written file, then CWD, to find .design-lock. Returns (project_root, config)."""
    start = Path(filepath).parent
    cwd = Path(os.getcwd())
    for parent in [start] + list(start.parents) + [cwd] + list(cwd.parents):
        lock = parent / ".design-lock"
        if lock.exists():
            config = {}
            for line in lock.read_text().splitlines():
                if "=" in line:
                    k, v = line.split("=", 1)
                    config[k.strip()] = v.strip()
            return parent, config
    return None, {}


# ── Slug normalization ────────────────────────────────────────────────────────

# Maps user-facing brand slugs to getdesign.md template filenames (without .md)
SLUG_MAP = {
    "linear": "linear.app",
    "mistral": "mistral.ai",
    "runway": "runwayml",
    "the-verge": "theverge",
    "theverge": "theverge",
    "x": "x.ai",
    "together": "together.ai",
    "opencode": "opencode.ai",
    "mistral.ai": "mistral.ai",
    "linear.app": "linear.app",
    "runwayml": "runwayml",
}

def resolve_design_slug(brand: str) -> list:
    """Return candidate design slugs to try for a given brand."""
    candidates = [brand]
    if brand in SLUG_MAP:
        candidates.append(SLUG_MAP[brand])
    # Also try common dot-suffixed variants
    for suffix in (".app", ".ai", ".md"):
        candidates.append(brand + suffix)
    return list(dict.fromkeys(candidates))  # deduplicate, preserve order


# ── Design system loading ─────────────────────────────────────────────────────

def load_design_system(brand: str, project_root: Path, plugin_dir: str) -> str:
    """
    Load full design system text for the active brand.

    Three sources, all optional, additive when combined:
      1. SKILL.md      — constraint layer (MUST/SHOULD/NEVER + token tables)
      2. DESIGN.md     — bundled atmosphere layer from getdesign.md (skills/designs/)
      3. cached DESIGN — written to .design-cache/ at lock time (same content)

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

    # Check bundled designs (skills/designs/[slug].md) with slug normalization
    designs_dir = Path(plugin_dir) / "skills" / "designs"
    for slug in resolve_design_slug(brand):
        design_path = designs_dir / f"{slug}.md"
        if design_path.exists():
            parts.append(design_path.read_text())
            break

    # Also check project-local cache (written at /design-drift:lock time)
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

    project_root, config = find_lock(filepath)
    if not config:
        sys.exit(0)

    brand = config.get("BRAND", "").lower().strip()
    if not brand:
        sys.exit(0)

    plugin_dir = os.environ.get(
        "CLAUDE_PLUGIN_ROOT",
        os.environ.get(
            "PLUGIN_DIR",
            str(Path(os.path.abspath(__file__)).parent.parent.parent)
        )
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
        # stderr on exit 0 never reaches the agent; additionalContext does.
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": _format_output(violations, filepath, brand),
            }
        }))

    sys.exit(0)


if __name__ == "__main__":
    main()
