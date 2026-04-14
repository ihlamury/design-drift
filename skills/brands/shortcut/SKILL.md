# Shortcut UI Skills - Design System Overview

## Core Principles

This is an opinionated design system for building interfaces inspired by Shortcut's aesthetic. The framework emphasizes "light mode, Inter font, 4px grid" as its foundational constraints.

## Key Specifications

**Color Palette:**
The system defines semantic tokens including `surface-base` (#FFFFFF), `accent` (#3831BF for primary actions), and maintains "text contrast ratio of at least 4.5:1 for accessibility."

**Typography:**
Inter is the required typeface. Primary headings use "50px / 700" weight, while body text employs "21px / 400." The system discourages modifying letter-spacing without explicit requests.

**Spacing & Layout:**
All spacing must follow a 4px grid system. The design targets a "1920px base viewport width" and uses `h-dvh` instead of `h-screen` for full-height elements.

**Interactive Design:**
Focus states require "2px outline with accent color (#3831BF)" and a matching outline-offset. Disabled elements use "opacity: 0.5" with `cursor: not-allowed`. The system prohibits removing focus indicators.

**Animation:**
Animations should only occur when explicitly requested and must "respect `prefers-reduced-motion`." Only compositor properties (transform, opacity) should animate, never layout properties.

**Components:**
Input fields have 0px height, and destructive actions require AlertDialog implementations. Error messages should appear adjacent to their triggering actions.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/shortcut

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
