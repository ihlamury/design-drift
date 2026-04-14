# Posthog UI Skills - Design System Guidelines

## Overview
This is an opinionated design system for building dark-mode interfaces inspired by PostHog's aesthetic, emphasizing a 4px grid, Inter typography, and specific color tokens.

## Key Design Principles

**Color Strategy:**
The system mandates "dark backgrounds (lightness < 20) for primary surfaces" with black (#000000) as the base. A limited palette of 5 colors ensures cohesion, while maintaining WCAG accessibility through minimum 4.5:1 text contrast ratios.

**Typography:**
Inter is the exclusive font family across all text styles (sizes ranging 10-14px). The guidelines restrict weights to regular and light only, with specific guidance: use `text-balance` for headings and `text-pretty` for body content.

**Spacing & Layout:**
A 4px grid system governs all spacing decisions. The viewport baseline is 1920px wide, with consistent element dimensions (41px, 24px, 857px, etc.). The system explicitly forbids arbitrary spacing values.

**Interactive Design:**
Focus states require "2px outline with accent color (#5E6AD2)" and matching outline-offset. Disabled states use 0.5 opacity with `cursor: not-allowed`. Animations are compositor-only (transform/opacity), never exceeding 200ms.

## Notable Constraints
- Never remove focus indicators
- Respect `prefers-reduced-motion`
- Use AlertDialog for destructive actions
- Avoid animating layout properties or large blur effects

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/posthog

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
