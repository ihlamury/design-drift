# Plaid UI Skills - Design System Guide

Plaid UI Skills is an MIT-licensed design system framework for building dark-mode interfaces with specific aesthetic constraints. Here are the key guidelines:

## Core Design Principles

**Color Palette:** The system mandates `#1B1B1B` as the page background and `#7FB4D5` for primary actions. "MUST use dark backgrounds (lightness < 20) for primary surfaces" and maintain a 4.5:1 text contrast ratio minimum.

**Typography:** Inter is the required font family. Specifications include `72px` weight `700` for primary headings and `23px` weight `400` for body text, with text-balance applied to headings.

**Spacing & Grid:** Implementation requires adherence to a 4px grid system with spacing values limited to: 3px, 4px, 5px, 6px, 11px, and 41px.

## Technical Requirements

**Borders:** Border-radius must use the defined scale (18px, 19px, 26px, 32px), with 26px as the default value for rounded elements.

**Layout:** "MUST design for 1920px base viewport width" and use `h-dvh` instead of `h-screen` for full-height layouts.

**Interactions:** Focus states require `2px` outlines in the accent color with matching offset. Disabled elements use `opacity: 0.5` and `cursor: not-allowed`.

**Animation:** "NEVER add animation unless it is explicitly requested" and limit animations to compositor properties only, respecting reduced-motion preferences.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/plaid

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
