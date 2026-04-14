# Anthropic UI Skills Documentation

**Color Palette**: The system uses a light mode foundation with `#ECE9E0` as the primary surface background, supplemented by carefully selected semantic tokens maintaining a "4.5:1 contrast ratio for accessibility."

**Typography**: All interfaces "MUST use `Inter` as primary font family" with specific sizes ranging from 10px to 68px. The largest headings use "68px / 700" weight.

**Spacing & Layout**: Everything adheres to "a 4px grid for spacing" with a 1920px base viewport width. Border radius options are limited to "3px, 15px."

**Interactive Elements**: Focus states require "2px outline with accent color (#5E6AD2)" and a matching outline-offset. Disabled states use "opacity: 0.5" with `cursor: not-allowed`.

**Animation Philosophy**: The guidelines state "NEVER add animation unless it is explicitly requested" and restrict animations to compositor properties only, with a 200ms maximum for feedback animations.

**Accessibility**: The system emphasizes avoiding removal of focus indicators, using AlertDialogs for destructive actions, and respecting `prefers-reduced-motion` preferences.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/anthropic

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
