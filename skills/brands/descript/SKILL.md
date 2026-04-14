# Descript UI Skills Design System

**Core Principles:**
- "MUST use dark backgrounds (lightness < 20) for primary surfaces"
- Primary background color is `#2C0814`
- "MUST use `Inter` as primary font family"
- "MUST use 4px grid for spacing"

**Color Palette:**
The system defines semantic tokens including `surface-base` (dark burgundy), `surface-raised` (light cream), destructive states in red (`#F2212E`), and maintains "text contrast ratio of at least 4.5:1 for accessibility"

**Typography:**
Primary headings use 79px at 700 weight, body text at 18px/400 weight. The system "MUST limit font weights to: regular, bold, medium"

**Spacing & Borders:**
Uses a 4px grid foundation with recommended gaps of 6px and border-radius options of 3px, 6px, 7px, 9px, or 13px.

**Layout:**
Designed for 1920px viewport width, requiring "h-dvh for full viewport height" and respecting safe-area insets.

**Interaction Standards:**
- Focus states require "2px outline with accent color (#5E6AD2)"
- Disabled elements use 0.5 opacity with `cursor: not-allowed`
- "NEVER add animation unless it is explicitly requested"
- Animations must respect `prefers-reduced-motion`

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/descript

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
