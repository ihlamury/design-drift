# Readwise UI Skills - Design System Reference

This is an opinionated design system for building interfaces inspired by Readwise's aesthetic. Here are the key constraints:

## Core Guidelines

**Colors:** Light mode with `#FFFFFF` backgrounds and `#3C78C1` accent color. "MUST maintain text contrast ratio of at least 4.5:1 for accessibility."

**Typography:** Inter font exclusively, with sizes ranging from 5px to 48px. "MUST use `text-balance` for headings and `text-pretty` for body text."

**Spacing & Layout:** "MUST use 4px grid for spacing" and design for 1920px base viewport width. Use `h-dvh` instead of `h-screen` for full viewport heights.

**Borders:** Apply border-radius only from the defined scale (2px, 5px, 7px, 9px). "SHOULD use subtle borders (1px) for element separation."

## Interactive Elements

- Focus states require "2px outline with accent color (#3C78C1)" and matching outline-offset
- Disabled elements use 50% opacity with `cursor: not-allowed`
- Destructive actions must trigger AlertDialog confirmations

## Animation & Performance

"NEVER add animation unless it is explicitly requested" and "MUST animate only compositor props (transform, opacity)." Never exceed 200ms for interaction feedback, and always respect `prefers-reduced-motion`.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/readwise

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
