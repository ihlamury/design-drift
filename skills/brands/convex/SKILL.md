# Convex UI Skills - Design System Guide

## Core Design Principles

**Color Foundation:** The system mandates very dark backgrounds with `#0F0F0F` as the base, using `#214AE8` as the primary accent for interactive elements. "MUST maintain text contrast ratio of at least 4.5:1 for accessibility."

**Typography:** All interfaces should employ the Inter font family exclusively. Primary headings use 40px semi-bold weight, while body text follows a 21px, 400-weight specification.

**Spacing & Grid:** Every design decision adheres to a 4px grid system. "NEVER use arbitrary spacing values (use design scale)" ensures consistency across components.

**Layout:** Designs target a 1920px viewport width as the baseline, with specific guidance to use `h-dvh` instead of `h-screen` for full-height elements.

## Interactive Standards

The system emphasizes accessibility and clarity in interactions:
- Focus states require a 2px outline in the accent color
- Disabled states use 50% opacity with a `not-allowed` cursor
- "MUST use an AlertDialog for destructive or irreversible actions"

## Animation Constraints

Restraint is key: "NEVER add animation unless it is explicitly requested." When animations are necessary, they should only affect compositor properties and respect user motion preferences.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/convex

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
