# Rippling UI Skills - Design System Guidelines

This is an opinionated design system for building dark-mode interfaces with Rippling's aesthetic. Here are the key takeaways:

## Core Requirements

**Colors**: The system mandates `#000000` as the page background and `#FDF6FD` for primary actions. Dark surfaces with lightness below 20% are essential, maintaining at least 4.5:1 text contrast ratios.

**Typography**: Inter is the required font family, with `43px` extra-bold for primary headings and `16px` weight-400 for body text. The system recommends limiting font weights to reduce complexity.

**Spacing & Layout**: A 4px grid governs all spacing decisions, with 2px as the default gap between elements. The base viewport is 1920px wide, and full-height elements should use `h-dvh` rather than `h-screen`.

## Interaction Standards

The guidelines prohibit removing focus indicators and require `2px` outlines with accent color for focus states. Destructive actions demand an AlertDialog component, and disabled states must show `opacity: 0.5` with `cursor: not-allowed`.

## Animation Constraints

Animations are forbidden unless explicitly requested and must never exceed 200ms. Only compositor properties (`transform`, `opacity`) should animate—layout properties are off-limits. The system respects `prefers-reduced-motion` preferences.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/rippling

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
