# Raycast UI Skills - Design System Overview

The Raycast UI Skills document is a design system specification for building interfaces with Raycast's aesthetic. Here are the key guidelines:

## Core Constraints

**Color Palette**: The system specifies a light-mode palette with `#DFDFDF` as the page background and includes semantic tokens like `surface-raised` (#08090B) for cards and `text-primary` (#636162) for main content.

**Typography**: "MUST use `Inter` as primary font family" with specific sizes ranging from 9px to 64px. The system limits weights to regular, bold, and light only.

**Spacing & Layout**: The design uses a 4px grid system with a base viewport of 1920px. "NEVER use arbitrary spacing values (use design scale)" is a strict requirement.

## Key Rules

- Border-radius must follow the scale: 4px, 6px, 10px, 13px, 18px
- Focus states require a 2px outline with `#5E6AD2` accent color
- Animations must not exceed 200ms and should only affect compositor properties
- "NEVER remove focus indicators" emphasizes accessibility priorities

The document provides detailed tables for colors, typography styles, and component specifications to maintain consistency across Raycast-inspired interfaces.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/raycast

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
