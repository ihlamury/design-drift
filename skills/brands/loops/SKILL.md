# Loops UI Skills - Design System Guidelines

**Color Foundation:**
"MUST use `#FFFFFF` as page background" and maintain semantic tokens like surface-raised (#ECECEC) and text-primary (#CCCCCE). Contrast ratios must meet accessibility standards.

**Typography Requirements:**
"MUST use `Inter` as primary font family" with specified sizes: 39px for primary headings and 22px for body text, all at 700 weight. The system emphasizes single font family consistency.

**Spatial Grid:**
"MUST use 4px grid for spacing" with predefined scales (1px through 9px), establishing "5px as default gap between elements."

**Border & Radius:**
"MUST use 1px border width consistently" with approved radius values ranging from 0px to 26px for pill-shaped components.

**Layout Standards:**
Design should reference a 1920px viewport width base, using `h-dvh` instead of `h-screen` for full-height elements.

**Interaction Principles:**
Focus states require "2px outline with accent color (#5E6AD2)" and destructive actions demand AlertDialog confirmation. Animation is prohibited unless explicitly requested, with compositor properties limited to 200ms maximum.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/loops

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
