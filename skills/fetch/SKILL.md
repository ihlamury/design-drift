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
