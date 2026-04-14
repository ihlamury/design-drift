# Miro UI Skills Design System

This is an opinionated design system for building interfaces that match Miro's aesthetic, utilizing a light-mode color palette, Inter typography, and a 4px spacing grid.

## Key Design Constraints

**Colors:** The system establishes semantic tokens including `#FEFEFE` for page backgrounds and `#C2BBFE` for primary actions. Text must maintain "at least 4.5:1" contrast ratios for accessibility.

**Typography:** All interfaces should use Inter exclusively, with primary headings set at 47px/700 weight and body text at 7px/400 weight. The system discourages modifying letter-spacing arbitrarily.

**Spacing & Borders:** Adhere strictly to the 4px grid, using only predefined spacing values (1px through 8px). Border radius options are similarly constrained to a specific scale: 1px, 3px, 4px, 5px, 6px, 7px, 9px, 15px, 16px, 17px, 18px.

**Layout:** Design for a 1920px viewport width. Use `h-dvh` instead of `h-screen` for full-height elements, and respect safe-area insets for fixed positioning.

**Interaction:** Focus states require a 2px outline in the accent color with 2px offset. Animations should never be added without explicit request, remain under 200ms, and respect user motion preferences.

## When to Use

Reference these guidelines when creating light-mode interfaces or implementing Miro-inspired design systems with AI agents.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/miro

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
