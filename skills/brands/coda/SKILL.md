# Coda UI Skills Reference

## Core Requirements

**Color System:** Uses a light-mode palette with `#FEFEFE` as the base surface and `#DCEBF4` as the accent color for primary actions. The guidelines emphasize reducing the color palette while maintaining a 4.5:1 text contrast ratio.

**Typography:** "MUST use `Inter` as primary font family" with specific sizing rules—71px/700 weight for primary headings and 16px/500 for body text. The system restricts font weights to maintain consistency.

**Spacing & Layout:** Implements a strict 4px grid system. "MUST use 4px grid for spacing" with predefined scales (1px, 3px, 4px, 5px, 6px, 9px, 10px, 12px). Border-radius values are limited to: 3px, 4px, 5px, 6px, 7px, 15px.

**Interactive States:** Focus states require a 2px outline in the accent color with 2px offset. Disabled elements use 50% opacity with `cursor: not-allowed`.

**Animation Constraints:** "NEVER add animation unless it is explicitly requested" and interactions should not exceed 200ms. Only compositor properties (transform, opacity) should animate.

**Accessibility:** The guidelines mandate aria-labels for icon-only buttons and require respecting `prefers-reduced-motion` preferences.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/coda

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
