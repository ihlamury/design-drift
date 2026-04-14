# Pitch UI Skills - Design System Guide

## Overview

This is an opinionated design system for building interfaces aligned with Pitch's aesthetic. It emphasizes light mode design, the Inter typeface, and a strict 4px grid system.

## Key Design Principles

**Color Strategy**
The system uses `#000000` for page backgrounds and `#5836F6` as the primary accent for actions and focus states. Text contrast must maintain at least 4.5:1 ratio for accessibility compliance.

**Typography**
"MUST use `Inter` as primary font family" and maintain consistency with specific sizing: 68px for primary headings and 26px for body text. The system recommends reducing the current five font weights to streamline the palette.

**Spacing & Grid**
All spacing must follow a 4px grid increment scale (1px, 2px, 3px, 4px, 5px, 7px, 8px, 9px). The guidance explicitly states: "NEVER use arbitrary spacing values (use design scale)."

**Borders**
Border radius should only use values from the defined scale: 3px, 4px, 6px, 7px, 8px. Default is 6px for most elements.

## Interactive Guidelines

Focus states require a 2px outline in the accent color with matching outline-offset. The system forbids removing focus indicators entirely.

For animations, "NEVER add animation unless it is explicitly requested" and interactions should not exceed 200ms. Motion should respect `prefers-reduced-motion` preferences.

## Layout Baseline

Design for 1920px viewport width. Use `h-dvh` instead of `h-screen` for full-height elements and respect safe-area insets for fixed positioning.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/pitch

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
