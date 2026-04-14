# Launchdarkly UI Skills - Complete Reference

## Overview
This is an opinionated design system for building interfaces inspired by Launchdarkly's aesthetic, emphasizing "dark mode, Inter font, 4px grid."

## Core Design Principles

**Color System:**
- Dark backgrounds with lightness below 20%
- Primary surface: pure black (#000000)
- Accent color: #AAB7F5 for interactions
- Minimum 4.5:1 contrast ratio for accessibility

**Typography:**
- Single font family: Inter
- Primary heading: 138px/700 weight
- Body text: 32px/700 weight
- Use `text-balance` for headings, `text-pretty` for body

**Spacing & Layout:**
- Mandatory 4px grid system
- Design viewport: 1920px width
- No arbitrary spacing or border-radius values
- Use `h-dvh` instead of `h-screen`

**Interactive Elements:**
- 2px accent-colored outlines for focus states
- No animation without explicit request
- Animations limited to compositor properties only
- Maximum 200ms for interaction feedback
- Always include `aria-label` on icon-only buttons

**Performance Rules:**
- Never animate large blur or backdrop-filter surfaces
- Avoid `will-change` outside active animations
- Use render logic instead of useEffect where possible

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/launchdarkly

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
