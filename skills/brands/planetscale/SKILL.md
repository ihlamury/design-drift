# Planetscale UI Skills - Design System

This is an opinionated design system for building dark-mode interfaces inspired by Planetscale's aesthetic. Here are the key principles:

## Core Constraints

**Color Palette:** The system mandates `#000000` for page backgrounds and `#7967D3` for primary actions. "MUST maintain text contrast ratio of at least 4.5:1 for accessibility."

**Typography:** All text uses Inter font exclusively. Primary headings require `51px` at weight `700`, while body text uses `17px` at weight `400`.

**Spacing & Grid:** "MUST use 4px grid for spacing" with a default gap of `38px` between elements. Arbitrary spacing values are prohibited.

**Layout:** Designs target a `1920px` viewport width base, using `h-dvh` instead of `h-screen` for full-height elements.

## Interactive Guidelines

Focus states require a `2px` outline in the accent color with matching offset. Hover states typically shift backgrounds to `#F8F8F9`, while disabled states use `opacity: 0.5` and `cursor: not-allowed`.

**Animation Policy:** "NEVER add animation unless it is explicitly requested" and limit interactions to compositor properties only (`transform`, `opacity`). Animations must not exceed `200ms`.

**Accessibility:** Icon-only buttons must include `aria-label` attributes, and focus indicators should never be removed.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/planetscale

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
