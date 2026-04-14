# GitHub UI Skills Design System

**Color Foundation:**
The system uses dark backgrounds with `#10131A` as the primary surface and `#030036` for accents. It maintains "text contrast ratio of at least 4.5:1 for accessibility."

**Typography:**
Inter is the required font family with weights limited to regular, bold, and light. Primary headings use 53px/700 weight, while body text uses 29px/400.

**Spacing & Layout:**
All spacing follows a 4px grid system. The design targets a 1920px viewport width with a 64px header height. Border radius options include 3px, 4px, 5px, 9px, 15px, 22px, and 29px.

**Interactive Patterns:**
Focus states require a 2px outline in the accent color with 2px offset. Animations are restricted to compositor properties only and must not exceed 200ms. The system explicitly states: "NEVER remove focus indicators."

**Key Constraint:**
"NEVER use arbitrary spacing values (use design scale)" emphasizes adherence to predefined measurements throughout the system.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/github

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
