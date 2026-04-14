# Railway UI Skills - Design System Guidelines

Railway's UI design system provides opinionated constraints for building dark-mode interfaces with a consistent aesthetic. Here are the key specifications:

## Core Design Principles

**Color Palette:**
The system mandates "dark backgrounds (lightness < 20) for primary surfaces" with `#0F0E14` as the base and `#0B1025` for accents. It requires maintaining "text contrast ratio of at least 4.5:1 for accessibility."

**Typography:**
"Inter" is the required font family, with `54px` / `extra_bold` for primary headings and `11px` / `300` for body text. The guidelines specify using `text-balance` for headings and `text-pretty` for body text.

**Spacing & Layout:**
All spacing must follow "a 4px grid" system with predefined scales (1px, 2px, 3px, 4px, 5px, 8px, 12px, 14px). The base viewport is 1920px, and developers should "use `h-dvh` for full viewport height" rather than `h-screen`.

**Borders:**
Border radius must come from the scale "0px, 2px, 3px, 4px, 5px, 6px, 8px, 10px" with 3px as the default.

## Interactive Standards

Focus states require "a `2px` outline with accent color" and matching outline-offset. Animation is prohibited unless explicitly requested, and when permitted, must be limited to compositor properties with "200ms" maximum duration while respecting `prefers-reduced-motion`.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/railway

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
