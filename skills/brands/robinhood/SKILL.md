# Robinhood UI Skills - Design System Overview

This MIT-licensed design system provides guidelines for creating Robinhood-inspired interfaces with dark mode aesthetics.

## Key Design Principles

**Color Palette:** The system mandates pure black (#000000) backgrounds with a signature lime accent (#B7DF2F) for interactive elements. The constraint states: "MUST use `#000000` as page background (`surface-base`)" and reserves the bright accent specifically for "primary actions and focus states."

**Typography:** Inter is the exclusively required typeface. Heading sizes reach 85px at weight 700, while body text sits at 14px/400. The guidelines emphasize reducing font weight variation and applying `text-balance` to headings.

**Spacing & Layout:** Everything aligns to a 4px grid system. Border radius is limited to two values (19px, 21px), with 21px recommended as the default. The base viewport is 1920px wide.

**Interactive Behavior:** Focus states require a 2px outline in the accent color with 2px offset. Animations are restricted to compositor properties (transform, opacity) and must not exceed 200ms. The system explicitly states: "NEVER remove focus indicators."

**Accessibility:** Minimum contrast ratio required is 4.5:1. Destructive actions demand AlertDialog confirmation, and paste functionality in inputs cannot be blocked.

This opinionated framework prioritizes consistency and accessibility while maintaining Robinhood's distinctive visual identity.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/robinhood

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
