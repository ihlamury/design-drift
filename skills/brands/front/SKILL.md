# Front UI Skills Design System

**Core Principles:**
- "Light-mode interfaces" with white backgrounds (#FFFFFF)
- Inter font exclusively with a 4px grid system
- Reduced color palette emphasizing the accent color #C8CC51

**Color System:**
The semantic tokens establish a light base with darker raised surfaces (#240733) and an accent for primary actions. Text contrast must maintain "at least 4.5:1 for accessibility."

**Typography:**
"Inter" serves as the required font family with specific sizes: 58px for primary headings and 26px for body text, both at 700 weight. Text should use `text-balance` for headings and `text-pretty` for body copy.

**Spacing & Borders:**
The design system mandates "4px grid for spacing" with defined scales. Border radius follows specific increments (1px, 2px, 3px, 5px, 6px, 18px, 20px) rather than arbitrary values.

**Interactive Design:**
Focus states require "2px outline with accent color (#C8CC51)" and 2px offset. Disabled states use 50% opacity. The system explicitly states to "Never remove focus indicators."

**Performance:**
"Never animate layout properties (width, height, top, left, margin, padding)" — only compositor properties like transform and opacity. Animations must stay under 200ms and respect motion preferences.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/front

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
