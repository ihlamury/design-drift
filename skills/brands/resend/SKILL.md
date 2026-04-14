# Resend UI Skills - Design System Guide

Resend UI Skills is an opinionated design system for building dark-mode interfaces with a specific aesthetic. Here are the key constraints:

## Core Principles

**Colors:** The system mandates `#060606` for page backgrounds and maintains a limited palette of 5 colors maximum. "MUST maintain text contrast ratio of at least 4.5:1 for accessibility."

**Typography:** Inter font is required exclusively. Primary headings use 88px at weight 700, while body text employs 18px at weight 400. The guidance specifies limiting font weights to "bold, regular, medium."

**Spacing & Layout:** All spacing follows a strict 4px grid system. The design targets a 1920px viewport width, and developers should "use `h-dvh` for full viewport height" rather than screen-based measurements.

**Borders:** Border radius is constrained to 15px, with widths limited to 2px or 3px options.

## Interactive Guidelines

Focus states require "2px outline with accent color (#5E6AD2)" and matching outline-offset. Disabled states apply 50% opacity with `cursor: not-allowed`.

Animation is restricted—"NEVER add animation unless it is explicitly requested"—and any animations must target only compositor properties like transform and opacity, never layout properties.

The system emphasizes accessibility and performance, prohibiting arbitrary spacing values and requiring structural skeletons for loading states.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/resend

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
