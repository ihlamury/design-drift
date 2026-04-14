---
name: fetch
description: Preview a DESIGN.md for any brand. Does not activate enforcement. Usage: /design-drift:fetch [brand].
---

# Design Drift — Fetch

The user has invoked `/design-drift:fetch $ARGUMENTS`.

## Steps

1. **Check bundled DESIGN.md** at `skills/designs/$ARGUMENTS.md` in the plugin directory.
   - Also try slug variants: `$ARGUMENTS.app.md`, `$ARGUMENTS.ai.md`, `runwayml.md` (for runway), `theverge.md` (for the-verge).

2. If found: display content, show quick summary (colors, fonts, description), offer to lock.

3. If not found:
   - Check if bundled SKILL.md exists at `skills/brands/$ARGUMENTS/SKILL.md`
   - If yes: "No DESIGN.md available for $ARGUMENTS, but constraint SKILL.md exists. Run /design-drift:lock $ARGUMENTS."
   - If no: "Not found in either source. Check brand name or run `/design-drift:lock` to see all 121 brands."

## Slug reference

| User types | File looked up |
|------------|---------------|
| linear | skills/designs/linear.app.md |
| mistral | skills/designs/mistral.ai.md |
| runway | skills/designs/runwayml.md |
| the-verge | skills/designs/theverge.md |

Attribution: "Design system from getdesign.md by VoltAgent (MIT License)"
