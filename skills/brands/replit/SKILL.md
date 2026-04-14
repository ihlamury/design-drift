# Replit UI Skills - Design System Overview

The Replit UI Skills document provides a comprehensive design system for creating light-mode interfaces with a specific aesthetic. Here are the key constraints:

## Core Principles

The system mandates using `#F8F8F8` as the page background and `#9266E6` for primary interactive elements. "MUST use `Inter` as primary font family" for all typography, with body text set at 13px/400 weight.

## Grid & Spacing

All spacing adheres to a 4px grid system. The guidelines state: "NEVER use arbitrary spacing values (use design scale)" and recommend 2px as the default gap between elements.

## Borders & Radius

Border radius must come from a predefined scale (0px through 45px). The document specifies "MUST use 1px border width consistently" and "SHOULD use 3px as default border-radius."

## Interactive Design

Focus states require "2px outline with accent color (#9266E6)" and a 2px outline-offset. Disabled elements must use 50% opacity with a `not-allowed` cursor.

## Animation Constraints

The system restricts animation heavily: "NEVER add animation unless it is explicitly requested" and limits interactions to compositor properties only (transform, opacity), capping duration at 200ms.

## Accessibility

Text contrast must maintain at least 4.5:1 ratio, and "MUST add an `aria-label` to icon-only buttons."

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/replit

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
