# Jasper UI Skills Design System

**Color Palette:**
The system defines semantic tokens including `surface-base` (#F5261E for page backgrounds), `accent` (#6899D0 for primary actions), and `destructive` (#F5261E for errors). "MUST maintain text contrast ratio of at least 4.5:1 for accessibility."

**Typography:**
"MUST use `Inter` as primary font family" with constrained weights (regular, medium, bold). Heading sizes range from 91px down to 10px, with specific guidance like using `text-balance` for headings.

**Spacing & Layout:**
The system enforces a 4px grid system with "SHOULD use spacing from scale: 1px, 2px, 3px, 4px, 5px, 6px, 8px, 9px." Base viewport width is 1920px.

**Interactive Elements:**
Focus states require "2px outline with accent color (#6899D0)" and 2px offset. Disabled states use 0.5 opacity. Animations are restricted—"NEVER add animation unless it is explicitly requested" and should not exceed 200ms.

**Key Constraints:**
Borders use 4px radius consistently, input fields have 0px height, and the system prohibits blocking paste functions or removing focus indicators.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/jasper

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
