# Shopify UI Skills Design System

This document outlines Shopify's design constraints for AI agents building light-mode interfaces. Here are the key guidelines:

## Core Design Principles

**Colors**: The system uses a minimal palette anchored by `#FEFEFE` page backgrounds and dark text tokens like `#858A8E` for primary content. "MUST maintain text contrast ratio of at least 4.5:1 for accessibility."

**Typography**: All interfaces require the Inter typeface with specific sizes (88px for headings, 39px for body). The guidelines note that "SHOULD reduce font weights (currently 5 detected)" to improve consistency.

**Spacing & Layout**: Implementation demands adherence to "a 4px grid for spacing" with predetermined scales. Designs target a 1920px base viewport, and creators should "NEVER use arbitrary spacing values (use design scale)."

**Borders**: Radius values are restricted to three options—19px, 26px, or 28px—with "26px+ radius for pill-shaped elements."

## Interactive Behavior

Focus states require "2px outline with accent color (#5E6AD2)" and matching outline-offset. Disabled elements use 50% opacity with a not-allowed cursor. The system prohibits animation unless requested and restricts changes to compositor properties only, capping durations at 200ms.

**Accessibility**: Icon-only buttons must include aria-labels, destructive actions require AlertDialogs, and motion preferences must be respected.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/shopify

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
