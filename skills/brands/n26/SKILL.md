# N26 UI Skills Design System

This is an opinionated design system for building N26-styled interfaces with dark mode aesthetics. Here are the key guidelines:

## Core Design Principles

**Color Palette:** The system mandates dark backgrounds with lightness below 20%, using pure black (`#000000`) as the base. "MUST use `#116F64` for primary actions and focus states (`accent`)" to maintain brand consistency.

**Typography:** "MUST use `Inter` as primary font family" with specific sizing rules—46px for headings and 27px for body text at weight 500.

**Spacing & Grid:** All spacing must follow "a 4px grid" with predefined increments (2px, 3px, 5px, 6px, 7px, 8px, 25px, 35px). Arbitrary values are prohibited.

**Accessibility:** Text contrast must maintain "at least 4.5:1" ratio, and focus indicators cannot be removed—they require a 2px outline in the accent color.

## Interactive Standards

Buttons use subtle ghost variants, hover states apply the raised surface color, and disabled elements drop to 50% opacity. Destructive actions require AlertDialog confirmation, while errors display contextually near the triggering element.

Animation is restricted: only compositor properties (`transform`, `opacity`) animate, interactions must complete within 200ms, and `prefers-reduced-motion` must be respected.

The base viewport is 1920px wide with a header fixed at 72px height.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/n26

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
