# Webflow UI Skills Design System

This is an opinionated design system for building dark-mode interfaces with Webflow's aesthetic principles. Here are the key constraints:

## Core Requirements

**Colors:** The system mandates `#151515` for page backgrounds and `#8DB8F2` for primary actions. "MUST use dark backgrounds (lightness < 20) for primary surfaces" and maintain "text contrast ratio of at least 4.5:1 for accessibility."

**Typography:** "MUST use `Inter` as primary font family" with `62px` / `700` weight for primary headings and `28px` / semi-bold for body text.

**Spacing & Grid:** Follow a strict 4px grid system. "SHOULD use spacing from scale: 1px, 2px, 3px, 4px, 5px, 7px, 9px, 13px" and avoid arbitrary values.

**Borders:** "SHOULD use 2px as default border-radius" with scale options limited to 1px, 2px, 3px, and 18px.

## Key Constraints

- Design for 1920px viewport width
- Use `h-dvh` instead of `h-screen`
- Never animate layout properties; only transform and opacity
- Respect `prefers-reduced-motion`
- Include 2px focus outlines with accent color for accessibility
- Use AlertDialog for destructive actions

The system is MIT-licensed and authored by design-skills (v1.0.0).

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/webflow

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
