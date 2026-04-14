# Bear UI Skills Design System

## Key Design Principles

**Color & Contrast:**
The system uses a light-mode palette anchored on `#FFFFFF` backgrounds with semantic tokens for surfaces and text. It requires "at least 4.5:1" contrast ratios for accessibility.

**Typography:**
Inter font is mandatory, with specific rules: "MUST use `50px` / `700` for primary headings" and "MUST use `14px` / `400` for body text." The system discourages excessive font weight variations.

**Layout Grid:**
Spacing strictly follows a 4px grid system. The design targets 1920px viewport width and prohibits arbitrary spacing values.

**Borders & Radius:**
Only three border-radius values are permitted: 7px, 11px, and 18px. Default is 11px.

**Interactive States:**
Focus states require "2px outline with accent color (`#5E6AD2`)" and matching outline-offset. Hover states use `#DDDDDE`, while disabled states apply 50% opacity.

**Animation Constraints:**
The guidelines are restrictive: "NEVER add animation unless it is explicitly requested" and animations limited to compositor properties only, maximum 200ms duration.

**Performance:**
Prohibits large blur animations, unnecessary `will-change` properties, and encourages render-logic over `useEffect` hooks.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/bear

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
