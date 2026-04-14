# Slack UI Skills - Design System Documentation

The Slack UI Skills is a design system framework (MIT licensed) created by design-skills for building interfaces with Slack's aesthetic principles.

## Core Principles

The system establishes "opinionated constraints for building Slack-style interfaces with AI agents," emphasizing light-mode design, the Inter typeface, and a 4-pixel grid foundation.

## Key Design Rules

**Color System:** The palette uses `#FFFFFF` for page backgrounds and `#481652` as the accent color for primary actions. The framework specifies "text contrast ratio of at least 4.5:1 for accessibility."

**Typography:** Inter is the mandatory font family, with primary headings at 61px/700 weight and body text at 22px/500 weight. The guidance includes using `text-balance` for headings and `text-pretty` for body content.

**Spacing & Borders:** All spacing must follow a 4px grid with predefined values (1px, 2px, 4px, etc.), and border-radius options are limited to: 1px, 3px, 4px, 8px, 9px, or 16px.

**Layout:** The base viewport is 1920px width, and developers should use `h-dvh` instead of `h-screen` for full-height elements.

## Interactive & Animation Guidelines

- Focus states require a 2px outline in the accent color with 2px offset
- "Never add animation unless it is explicitly requested"
- Animations are limited to compositor properties (transform, opacity) with maximum 200ms duration
- Disabled states use 0.5 opacity and `cursor: not-allowed`

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/slack

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
