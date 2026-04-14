# Wise UI Skills - Design System Guidelines

The Wise UI Skills is an opinionated design system for building interfaces with Wise's aesthetic. Here are the key constraints:

## Core Design Principles

**Colors:** The system mandates a `#91E75E` green background for primary surfaces, with `#FEFEFE` for raised elements. A strict 4.5:1 text contrast ratio is required for accessibility.

**Typography:** "MUST use `Inter` as primary font family" with specific sizing rules—70px for headings, 41px for body text, both at 700 weight. Text should use `text-balance` for headings.

**Spacing & Grids:** "MUST use 4px grid for spacing" with predefined scales (1px, 3px, 4px, 5px, 6px, 7px, 19px, 33px). Arbitrary spacing values are prohibited.

**Borders:** Border radius must come from a defined scale (4px, 15px, 18px, 19px, 20px, 21px, 22px, 37px). Default is 20px for standard elements.

## Interaction & Accessibility

Focus states require a `2px` outline in accent color with `2px` offset—"NEVER remove focus indicators." Disabled states use 50% opacity with `cursor: not-allowed`.

Animation is heavily restricted: "NEVER add animation unless it is explicitly requested" and limited to compositor properties only, with a 200ms maximum for feedback.

## Layout

Design targets a 1920px viewport. The guideline specifies using `h-dvh` instead of `h-screen` and maintaining `safe-area-inset` for fixed elements.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/wise

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
