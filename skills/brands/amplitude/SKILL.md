# Amplitude UI Skills - Design System Guidelines

## Core Principles

The system enforces a "light mode, Inter font, 4px grid" philosophy. It uses `#000000` for page backgrounds and `#3151E1` as the primary accent color for interactive elements.

## Typography Standards

"Inter" is mandated as the sole font family across all text styles. Heading sizes range from 56px to 58px at weight 700, while body text uses 23px at weight 500. The system specifies distinct sizes for different text hierarchy levels (13px through 58px).

## Spacing & Layout

The design system requires adherence to a 4px grid with specific spacing increments (1px, 2px, 3px, 4px, 5px, 6px, 7px, 11px). Border-radius values must come from a defined scale, with 25px designated for pill-shaped elements.

## Interactive Design

Focus states require a 2px outline in the accent color with matching outline-offset. Disabled elements use 50% opacity. The guidelines explicitly prohibit removing focus indicators and blocking paste functionality in inputs.

## Performance Constraints

Animations must be limited to compositor properties only (transform, opacity) and never exceed 200ms for feedback. The system discourages motion unless explicitly requested and requires respecting `prefers-reduced-motion` preferences.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/amplitude

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
