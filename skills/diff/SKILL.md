---
name: diff
description: "Token-by-token diff of a file against the locked design system. Usage: /design-drift:diff [file]."
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
