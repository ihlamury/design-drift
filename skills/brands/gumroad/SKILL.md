# Gumroad UI Skills - Design System Guidelines

## Core Design Principles

**Color Strategy:** The system mandates "dark backgrounds (lightness < 20) for primary surfaces" with pure black (#000000) as the base. Text contrast must meet WCAG standards of at least 4.5:1.

**Typography:** Inter is the exclusive font family. Heading sizes range from 92px down to 8px, with the guideline stating "use `text-balance` for headings and `text-pretty` for body text."

**Spacing & Grids:** All spacing adheres to a 4px grid system. The guidance specifies "never use arbitrary spacing values (use design scale)."

## Layout & Components

Designs target a 1920px viewport width. Input fields have a specific height of 0px. The system provides a Ghost button variant using transparent backgrounds with #C7C7C7 text.

## Interactive & Animation Guidelines

Focus states require "2px outline with accent color (#5E6AD2)" and matching outline-offset. Critically, the system states "never add animation unless it is explicitly requested" and animations must respect reduced-motion preferences, not exceeding 200ms.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/gumroad

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
