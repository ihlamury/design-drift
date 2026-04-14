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
