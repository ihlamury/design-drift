---
name: lock
description: Lock a brand design system for the session. Activates drift enforcement on all subsequent UI writes. Supports 121 brands. Usage: /design-drift:lock [brand].
---

# Design Drift — Lock

The user has invoked `/design-drift:lock $ARGUMENTS`.

## Source resolution logic

design-drift pulls from two bundled sources. Use both when available, fall back gracefully.

| Sources available | Behavior |
|-------------------|----------|
| SKILL.md ✓ + DESIGN.md ✓ | Full enrichment: MUST/SHOULD/NEVER constraints + visual tokens from both |
| SKILL.md ✓ + DESIGN.md ✗ | Constraint-only: MUST/SHOULD/NEVER rules, tokens extracted from SKILL.md |
| SKILL.md ✗ + DESIGN.md ✓ | Token-only: colors, fonts, spacing extracted from DESIGN.md |
| SKILL.md ✗ + DESIGN.md ✗ | Fail with helpful message |

## Slug normalization

Some brands have alternate filenames in the bundled designs. Try these mappings if the
first lookup fails:

| User types | Design file |
|------------|-------------|
| linear | linear.app.md |
| mistral | mistral.ai.md |
| runway | runwayml.md |
| the-verge | theverge.md |

## Steps

1. **Check for bundled DESIGN.md** in `skills/designs/` in the plugin directory:
   - Try `skills/designs/$ARGUMENTS.md` first
   - If not found, try slug variants: `$ARGUMENTS.app.md`, `$ARGUMENTS.ai.md`, etc.
   - If found: create `.design-cache/` in project root, copy content to `.design-cache/$ARGUMENTS.md`

2. **Check for bundled SKILL.md** at `skills/brands/$ARGUMENTS/SKILL.md` in the plugin directory.

3. **If both fail**: tell the user "$ARGUMENTS not found in design-skills (87 brands) or getdesign.md (66 brands). Check the brand name." Stop.

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
- The scanner reads tokens dynamically from bundled files at runtime. No hardcoded data.
- DESIGN.md files are sourced from getdesign.md (via `npx getdesign`) and bundled in `skills/designs/`.
- 66 brands have bundled DESIGN.md. 87 brands have bundled SKILL.md. 121 brands total across both.
