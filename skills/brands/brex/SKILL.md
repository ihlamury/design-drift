# Brex UI Skills - Design System Guide

MIT-licensed design system providing "opinionated constraints for building Brex-style interfaces with AI agents."

## Key Design Principles

**Color Foundation:**
The system establishes a refined palette anchored on "#D9D1CF" for page backgrounds and "#00070D" for primary actions, maintaining "text contrast ratio of at least 4.5:1 for accessibility."

**Typography Standards:**
All interfaces must use Inter font exclusively, with specific sizing rules: "68px / 700" for main headings and "24px / 400" for body content.

**Spacing & Grid:**
The framework mandates "4px grid for spacing" with "5px as default gap between elements," avoiding arbitrary values entirely.

**Layout Constraints:**
Designs target "1920px base viewport width" and require `h-dvh` instead of `h-screen` for full-height elements.

**Interactive Requirements:**
Focus states need "2px outline with accent color," disabled states use "opacity: 0.5," and destructive actions must trigger an AlertDialog. Importantly, the guidelines state "NEVER remove focus indicators."

**Animation Guidance:**
Animations should only animate "compositor props (transform, opacity)" and must "not exceed 200ms for interaction feedback," while respecting motion preferences.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/brex

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
