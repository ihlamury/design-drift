# Figma UI Skills - Design System Guidelines

**Color System:**
The palette uses eight semantic tokens, with `#FFFFFF` for page backgrounds and `#BEBAF6` as the primary accent. "Text contrast ratio of at least 4.5:1 for accessibility" is maintained throughout.

**Typography:**
Inter is the exclusive font family. Primary headings use 57px in extra-bold weight, while body text is set at 36px/700. The system includes ten defined text styles ranging from 13px to 57px.

**Spacing & Layout:**
A strict 4px grid governs all spacing decisions. "Use spacing from scale: 2px, 4px, 5px, 9px, 10px, 11px, 37px, 67px" with 5px as the default gap. The base viewport width is 1920px.

**Borders:**
Border radius options are limited to 3px or 4px, with consistent 1px border widths throughout.

**Interaction States:**
Focus states require a "2px outline with accent color (#BEBAF6)" and matching outline-offset. Disabled states use 50% opacity with a not-allowed cursor.

**Animation:**
Animations should only use compositor properties (transform, opacity) and never exceed 200ms, while respecting reduced-motion preferences.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/figma

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
