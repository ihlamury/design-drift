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
