# Codeium UI Skills Design System

**Color Palette:**
The system mandates dark backgrounds with lightness under 20, using `#152443` as the base surface and `#32E5AD` as the accent color for actions and focus states. Text contrast must maintain at least 4.5:1 ratios.

**Typography:**
"MUST use `Inter` as primary font family" with limited weights (regular and bold only). Primary headings use 77px/700, while body text uses 20px/400. The system specifies exact semantic tokens for different text levels, from `heading-1` down to `caption` styles.

**Layout & Spacing:**
The design system enforces a 4px grid for all spacing, with a base viewport of 1920px. Arbitrary spacing values are prohibited; instead, designers must choose from: 5px, 6px, 16px, 29px, 42px.

**Interactive Elements:**
Focus states require a 2px outline in the accent color with 2px offset. Disabled states use 50% opacity. Animations are restricted to compositor properties only (`transform`, `opacity`), never layout properties, and must not exceed 200ms.

**Key Constraint:**
"NEVER add animation unless it is explicitly requested," reflecting a performance-conscious, accessibility-aware approach to interface design.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/codeium

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
