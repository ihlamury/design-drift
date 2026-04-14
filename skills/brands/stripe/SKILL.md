# Stripe UI Skills Design System

This is an MIT-licensed design system for creating interfaces inspired by Stripe's aesthetic. Here are the key guidelines:

## Core Requirements

**Colors:** The system mandates `#F2F6F9` for page backgrounds and `#517BDF` for primary actions, while maintaining "text contrast ratio of at least 4.5:1 for accessibility."

**Typography:** All interfaces "MUST use `Inter` as primary font family" with specific sizing rules—53px/700 weight for primary headings and 28px for body text.

**Spacing & Grid:** "MUST use 4px grid for spacing" and avoid arbitrary values outside the defined scale (1px through 13px).

**Borders:** Border-radius must come from a specific scale (3px to 35px), with "22px as default border-radius."

## Layout & Interaction

The system targets "1920px base viewport width" and prohibits `h-screen` in favor of `h-dvh`. For interactive elements, focus states require "2px outline with accent color," and designers "NEVER remove focus indicators."

**Animation constraints** are strict: only compositor properties like `transform` and `opacity` should animate, never layout properties, and interactions shouldn't exceed 200ms.

The design philosophy emphasizes accessibility, performance, and semantic consistency throughout.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/stripe

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
