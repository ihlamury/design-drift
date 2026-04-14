# Ramp UI Skills - Design System Guidelines

Ramp UI Skills is an MIT-licensed design system for building light-mode interfaces with a distinctive aesthetic. Here are the key principles:

## Core Design Tokens

The system uses a minimal color palette anchored by `#FFFFFF` for page backgrounds and `#EBF123` for primary actions. Typography relies exclusively on the Inter font family, with primary headings at 61px/700 weight and body text at 19px/500 weight.

## Structural Constraints

All spacing follows a 4px grid system, with "spacing from scale: 3px, 4px, 5px, 8px, 38px, 65px." Border radius is limited to 4px or 5px values only. The base viewport is designed for 1920px width.

## Interactive Patterns

Focus states require "2px outline with accent color (#EBF123)" and a matching outline-offset. Destructive actions must use AlertDialog components, and all icon-only buttons need aria-labels for accessibility.

## Performance Priorities

The guidelines explicitly state: "NEVER add animation unless it is explicitly requested" and animations must not exceed 200ms. Layout animations are prohibited—only compositor properties like transform and opacity should move.

This system prioritizes consistency, accessibility (4.5:1 contrast minimum), and performance over decorative flourishes.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/ramp

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
