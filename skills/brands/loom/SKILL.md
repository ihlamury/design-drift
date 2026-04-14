# Loom UI Skills Design System

## Core Design Principles

The system emphasizes **light-mode interfaces** with specific color constraints: page backgrounds use `#E4EDFE`, primary actions employ `#2256C7`, and text maintains a minimum 4.5:1 contrast ratio for accessibility.

## Technical Requirements

- **Typography**: Inter font exclusively, with sizes ranging from 11px to 54px
- **Spacing**: Strict 4px grid adherence; no arbitrary values permitted
- **Border Radius**: Limited scale (4px, 15px, 18px, 22px, 26px, 28px)
- **Viewport**: Designed for 1920px base width using `h-dvh` for full-height elements

## Interaction Guidelines

The document mandates focus states with "2px outline with accent color (#2256C7) and 2px outline-offset," while animation is restricted to compositor properties only, capped at 200ms for interaction feedback.

## Key Restrictions

The system explicitly prohibits arbitrary spacing values, focus indicator removal, arbitrary border-radius usage, and layout property animations. It also requires `AlertDialog` components for destructive actions and mandates `aria-label` attributes on icon-only buttons.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/loom

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
