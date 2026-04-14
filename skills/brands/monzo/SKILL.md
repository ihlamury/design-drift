# Monzo UI Skills - Design System Guidelines

This is an opinionated design system for creating interfaces aligned with Monzo's aesthetic. Here are the key constraints:

## Core Principles

**Colors**: The system uses a light mode with `#FFFFFF` backgrounds and maintains a "light backgrounds for primary surfaces" approach. Text contrast must meet 4.5:1 accessibility standards.

**Typography**: "MUST use `Inter` as primary font family" with specific sizing rules—48px/700 weight for primary headings and 21px/extra_bold for body text.

**Spacing & Layout**: All spacing follows a 4px grid system. The design targets a 1920px viewport with consistent element widths. Border radius values come from a defined scale: 3px, 4px, 6px, 16px, or 25px.

## Critical Rules

- Never use arbitrary spacing or border-radius values
- Always include focus indicators (2px outline with #5E6AD2)
- Only animate compositor properties (transform, opacity)—never layout properties
- Use AlertDialog for destructive actions
- Never block paste functionality in inputs
- Respect `prefers-reduced-motion` in animations

The system includes semantic color tokens, predefined text styles, and interaction state specifications to maintain consistency across Monzo-inspired interfaces.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/monzo

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
