# Obsidian UI Skills - Design System Reference

## Overview
This is an MIT-licensed design system for creating dark-mode interfaces inspired by Obsidian's aesthetic, emphasizing a "4px grid" and "Inter font" throughout.

## Key Design Principles

**Color Foundation:**
The system mandates "dark backgrounds (lightness < 20)" with black (`#000000`) as the base and purple (`#6930C7`) as the accent color. Text contrast must maintain at least 4.5:1 ratio for accessibility compliance.

**Typography Constraints:**
"Inter as primary font family" with defined scales: body text at 14px/400 weight, headings at 78px/700 weight. The system discourages arbitrary font choices, using `text-balance` for headings and `text-pretty` for body content.

**Spacing & Grid:**
"Use 4px grid for spacing" exclusively. The system prohibits arbitrary spacing, instead providing a defined scale (1-8px) with 2px as the default gap between elements.

**Border Radius:**
"Use design scale" of 3px, 4px, 5px, 6px, 8px, 11px, and 23px radius values. Pills and rounded elements use 23px+, while standard components default to 4px.

## Interaction & Accessibility

Focus states require "2px outline with accent color" and matching offset. The system mandates `aria-label` attributes on icon-only buttons and prohibits removing focus indicators. Disabled states use 50% opacity with `cursor: not-allowed`.

**Animation Guidance:**
"Never add animation unless explicitly requested" and animations must stay under 200ms, respecting `prefers-reduced-motion` preferences. Only compositor properties (transform, opacity) should animate.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/obsidian

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
