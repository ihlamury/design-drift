# Discord UI Skills Design System

## Core Guidelines

**Colors:** The system uses `#4548ED` as the primary accent and page background, with a limited palette of 9 colors. Text must maintain a 4.5:1 contrast ratio for accessibility.

**Typography:** "MUST use `Inter` as primary font family" with weights limited to regular, medium, and bold. Headings use 52px/700 weight, while body text is 20px/400.

**Spacing & Layout:** "MUST use 4px grid for spacing" with a 1920px base viewport width. Designers should avoid arbitrary values and stick to the defined scale.

**Borders:** "SHOULD use 9px as default border-radius" consistently across components.

## Interaction Patterns

Focus states require a 2px outline in the accent color. "NEVER remove focus indicators" for accessibility. Disabled states use 50% opacity with a not-allowed cursor.

**Animation:** Changes should be minimal—"NEVER add animation unless it is explicitly requested" and never exceed 200ms for feedback interactions.

## Key Constraint

The system emphasizes semantic tokens and a light-mode aesthetic aligned with Discord's current design direction, ensuring consistency through strict adherence to predefined scales rather than arbitrary values.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/discord

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
