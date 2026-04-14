# Airbnb UI Skills - Design System Guidelines

This design system document provides comprehensive constraints for building Airbnb-inspired interfaces using a light mode aesthetic.

## Key Design Principles

The system emphasizes consistency through specific constraints: "MUST use `#FEFEFE` as page background" and implementation of an Inter-based typography hierarchy. The color palette consists of 13 carefully selected semantic tokens for surfaces, text, and interactive states.

## Core Requirements

**Spacing & Layout:** Designers must "use 4px grid for spacing" and should reference a defined scale rather than arbitrary values. The base viewport is 1920px wide.

**Typography:** Inter font is mandatory, with sizes including 15px for body text and 19px for primary headings. The system limits font weights to "light, regular, medium."

**Interactions:** The guidelines specify that focus states require "2px outline with accent color (`#5E6AD2`)" and that destructive actions must trigger an AlertDialog.

**Animation:** This is notably restricted—the document states "NEVER add animation unless it is explicitly requested" and prohibits animating layout properties, keeping interactions under 200ms.

## Notable Constraints

The system includes unusual specifications like "0px height for input fields" and emphasizes accessibility by "maintain[ing] text contrast ratio of at least 4.5:1."

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/airbnb

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
