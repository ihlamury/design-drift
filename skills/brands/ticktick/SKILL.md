# Ticktick UI Skills - Design System Guidelines

## Overview
This is an opinionated design system for building Ticktick-style interfaces with AI agents, using light mode, Inter font, and a 4px grid system.

## Key Design Principles

**Colors:** The system uses a refined palette with `#FEFEFE` for page backgrounds and `#6E85D9` as the primary accent. "MUST maintain text contrast ratio of at least 4.5:1 for accessibility."

**Typography:** Inter is the exclusive font family. Primary headings use 51px/700 weight, while body text defaults to 13px/400. "MUST use `text-balance` for headings and `text-pretty` for body text."

**Spacing & Structure:** All spacing adheres to a 4px grid. "SHOULD use 5px as default gap between elements." Border radius options are limited to 3px, 16px, 22px, 23px, and 25px.

**Interactive Behavior:** Focus states require "2px outline with accent color (#6E85D9)" and a 2px offset. Hover states typically apply the `#D8EDF7` background color. "MUST use opacity: 0.5" for disabled states.

**Animation:** "NEVER add animation unless it is explicitly requested" and interactions should not exceed 200ms. Only compositor properties like transform and opacity should animate.

## When to Reference
Use these guidelines when creating light-mode interfaces, designing Ticktick-inspired systems, or implementing UIs with Inter font and 4px grid specifications.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/ticktick

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
