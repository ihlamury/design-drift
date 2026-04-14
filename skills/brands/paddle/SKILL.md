# Paddle UI Skills - Design System Overview

Paddle UI Skills is an opinionated design system for building light-mode interfaces with a specific aesthetic. Here are the key constraints:

## Core Design Tokens

**Colors:** The system uses `#FDFDDF` as page background and `#3475F2` for primary actions. Text maintains accessibility through a minimum 4.5:1 contrast ratio.

**Typography:** All interfaces must employ Inter as the sole font family. Primary headings use 74px/700 weight, while body text relies on 32px/500 weight. The system restricts font weights to reduce cognitive load.

**Spacing & Borders:** A rigid 4px grid governs all spacing decisions, with border-radius values limited to: 0px, 1px, 2px, 3px, 4px, 6px, 7px, 9px, 13px.

## Implementation Rules

The guidelines emphasize that designers should "NEVER use arbitrary spacing values" and "NEVER use arbitrary border-radius values". Layouts target a 1920px viewport width as the baseline.

Interactive elements must follow strict patterns: focus states require a "2px outline with accent color", and disabled states mandate "opacity: 0.5" with "cursor: not-allowed".

**Animation Constraint:** The system explicitly states "NEVER add animation unless explicitly requested" and limits compositor animations to 200ms maximum.

This design system prioritizes consistency, accessibility, and performance over flexibility.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/paddle

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
