# Notion UI Skills - Design System Guidelines

This MIT-licensed design system provides constraints for building Notion-inspired interfaces with these core principles:

## Key Design Tokens

The system establishes a restrained color palette anchored by `#F6F6F6` for page backgrounds and `#97CAEE` for interactive elements. All text must maintain "at least 4.5:1" contrast ratios for accessibility.

## Typography Standards

Inter is the exclusive font family. Heading styles range from 66px at weight 700 down to 8px, with the directive to "use `text-balance` for headings and `text-pretty` for body text."

## Structural Rules

Layouts should respect a 4px grid system with defined spacing increments: 1px, 2px, 4px, 5px, 6px, 11px, 14px, 18px. Border-radius values are restricted to 3px, 4px, 6px, or 15px—"NEVER use arbitrary border-radius values."

## Interaction Patterns

Focus states require "2px outline with accent color" and matching outline-offset. Animations are prohibited unless explicitly requested and must "NEVER exceed 200ms for interaction feedback." Disabled states mandate "opacity: 0.5" with `cursor: not-allowed`.

## Performance Constraints

The system forbids animating layout properties, applying `will-change` outside active animations, or animating large `blur()` surfaces—prioritizing both visual consistency and performance.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/notion

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
