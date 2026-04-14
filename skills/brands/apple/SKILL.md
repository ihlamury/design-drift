# Apple UI Skills Design System

**Core Principles:**
- Light mode aesthetic with `#FFFFFF` backgrounds
- Inter font family exclusively
- 4px grid system for all spacing
- 21px border-radius standard
- 1920px viewport width baseline

**Color Palette:**
The system defines seven semantic tokens including surfaces, text hierarchy, borders, and a primary accent color (`#155BD0`) for interactive elements.

**Typography:**
Ten text styles ranging from 51px headings to 10px labels, all using Inter. The guidelines mandate "text-balance for headings and text-pretty for body text."

**Spacing & Layout:**
"MUST use 4px grid for spacing" with restricted scale values (2px, 4px, 13px, 34px). Layout patterns show standardized header heights (43px) and content dimensions.

**Interaction & Animation:**
Focus states require 2px outlines with 2px offset. The system strictly prohibits animations unless explicitly requested and limits interaction feedback to 200ms maximum. Importantly, "NEVER animate layout properties (width, height, top, left, margin, padding)."

**Accessibility:**
Text contrast must maintain at least 4.5:1 ratio, focus indicators are mandatory, and the system respects `prefers-reduced-motion` preferences.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/apple

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
