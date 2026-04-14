# Mixpanel UI Skills - Design System Guidelines

This is an opinionated design system for building Mixpanel-style interfaces with AI agents, licensed under MIT.

## Core Principles

The system emphasizes light-mode interfaces using a 4px grid, Inter typography, and a constrained color palette. Key mandatory requirements include using `#F4F3F4` for page backgrounds and `#201757` for primary actions, while maintaining at least 4.5:1 text contrast ratios.

## Essential Specifications

**Typography:** Inter font exclusively, with primary headings at 62px/700 weight and body text at 15px/400 weight.

**Spacing & Borders:** Strictly adhere to the 4px grid scale (1px, 2px, 3px, etc.). Border radius must follow the defined scale, with 3px as the default.

**Layout:** Design for 1920px viewport width, using `h-dvh` instead of `h-screen` and respecting safe-area-inset for fixed elements.

**Interactive States:** Focus states require 2px outline in accent color with 2px offset. Disabled states use 50% opacity and "not-allowed" cursor. Hover states vary by component type.

**Animation:** Only animate compositor properties (transform, opacity) within 200ms, respecting prefers-reduced-motion. Layout animations are prohibited.

**Accessibility:** Never remove focus indicators, add aria-labels to icon-only buttons, and never block paste functionality in inputs.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/mixpanel

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
