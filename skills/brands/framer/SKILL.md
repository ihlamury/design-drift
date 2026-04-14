# Framer UI Skills - Design System

**Core Design Principles:**
- Dark mode aesthetic with `#000000` base backgrounds
- Inter typeface exclusively
- 4px grid system for all spacing
- Minimal, curated color palette

**Typography Standards:**
Primary headings use 93px at weight 700, while body text should be 23px at weight 500. The system specifies `text-balance` for headings and `text-pretty` for body content.

**Color System:**
Surfaces range from pure black (#000000) to slightly elevated surfaces at #141415. Text contrast must maintain at least 4.5:1 ratio for accessibility compliance.

**Spacing & Borders:**
All spacing derives from a 4px base unit. Border radius options include: 1px, 2px, 3px, 4px, 7px, 8px, 15px, 17px. Default border-radius is 4px.

**Layout:**
Designed for 1920px viewport width. The system discourages `h-screen` in favor of `h-dvh` for viewport-relative heights.

**Interactive States:**
Focus states require 2px outlines with #5E6AD2 accent color. Disabled elements use 0.5 opacity. Animations limited to 200ms maximum with compositor properties only—never layout properties.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/framer

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
