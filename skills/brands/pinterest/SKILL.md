# Pinterest UI Skills - Design System Overview

This design system provides opinionated constraints for building Pinterest-style interfaces. Here are the key specifications:

## Core Principles

The system emphasizes a "light mode, Inter font, 4px grid" aesthetic. It applies when creating light-mode interfaces and Pinterest-inspired design systems.

## Color Palette

The system uses a reduced 11-color palette with a white page background (`#FFFFFF`). Key semantic tokens include:
- Primary text: `#3B3B3A`
- Accent/destructive: `#EB5B3E`
- Secondary text: `#ED93A1`

All text must maintain at least 4.5:1 contrast ratio for accessibility.

## Typography

"MUST use `Inter` as primary font family" with limited weight options (bold, semi-bold, regular). Primary headings use 49px/700 weight, while body text uses 19px/400.

## Spacing & Layout

The system mandates a 4px grid for spacing with predefined scales (3px, 4px, 5px, 51px, 71px). Border radius options are limited to 13px or 15px, and the base viewport width is 1920px.

## Interactive Guidelines

Focus states require 2px outlines, disabled states use 50% opacity, and destructive actions need AlertDialog confirmation. Importantly: "NEVER add animation unless it is explicitly requested."

## Key Constraint

"NEVER use arbitrary spacing values (use design scale)" ensures consistency throughout implementations.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/pinterest

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
