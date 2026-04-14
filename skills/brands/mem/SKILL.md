# Mem UI Skills Design System

**Color Palette:**
The system uses a light mode foundation with `#F9F5ED` as the base background and `#95A3DC` as the accent color for primary actions. "MUST maintain text contrast ratio of at least 4.5:1 for accessibility."

**Typography:**
All interfaces should use Inter as the sole font family. The hierarchy includes an 86px bold heading, 20px regular body text, and several secondary text styles. Headings use `text-balance` while body text uses `text-pretty`.

**Spacing & Layout:**
"MUST use 4px grid for spacing" with predefined scale values (1px through 28px). The base viewport is 1920px wide, and designers should "use `h-dvh` for full viewport height" rather than `h-screen`.

**Components:**
Ghost buttons feature transparent backgrounds with dark text. Focus states require "2px outline with accent color (#95A3DC)" and matching outline-offset.

**Animation:**
"NEVER add animation unless it is explicitly requested" and animations must stay under 200ms, affecting only compositor properties like transform and opacity.

**Accessibility:**
All icon-only buttons need aria-labels, and focus indicators are mandatory—never removable.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/mem

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
