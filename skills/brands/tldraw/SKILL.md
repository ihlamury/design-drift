# Tldraw UI Skills - Design System Overview

Tldraw UI Skills is an MIT-licensed design system for building interfaces aligned with Tldraw's aesthetic. Here are the key guidelines:

## Core Principles

**Colors & Contrast:** The system uses a light-mode palette with `#E7EBEE` as page background and `#0E54F0` for primary actions. All text must maintain at least 4.5:1 contrast ratio for accessibility.

**Typography:** "MUST use `Inter` as primary font family" with limited weights (regular and medium). Font sizes range from 7px to 14px, with specific styles for headings, body text, and captions.

**Spacing & Layout:** The design follows "a 4px grid for spacing" and specific border-radius values (0px, 3px, 4px, 6px, 7px, 9px). The base viewport is 1920px wide.

## Implementation Rules

- Never use arbitrary spacing or border-radius values outside the defined scales
- Always use `h-dvh` instead of `h-screen` for full-height elements
- Apply `2px outline with accent color` for focus states
- Only animate compositor properties (transform, opacity), never layout properties
- Respect `prefers-reduced-motion` and keep animations under 200ms
- Use `AlertDialog` for destructive actions

The system emphasizes consistency, accessibility, and performance while maintaining Tldraw's distinctive minimal aesthetic.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/tldraw

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
