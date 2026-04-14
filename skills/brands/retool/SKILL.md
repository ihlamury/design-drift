# Retool UI Skills - Design System Overview

This MIT-licensed design system provides opinionated constraints for building Retool-style interfaces with AI agents.

## Key Design Principles

**Color Palette:** The system emphasizes light backgrounds with a curated set of semantic tokens. The page background uses `#E3E6D7`, while `#80AEF2` serves as the primary accent for actions and focus states. All text must maintain at least 4.5:1 contrast ratios.

**Typography:** "MUST use `Inter` as primary font family" with specific sizing rules—54px at weight 700 for headings and 19px at weight 500 for body text. The guidance recommends applying `text-balance` to headings and `text-pretty` to body content.

**Spacing & Layout:** Developers should adhere to a 4px grid system and avoid arbitrary values. The framework targets 1920px viewport widths and specifies using `h-dvh` rather than `h-screen` for full-height elements.

**Interactive Patterns:** Focus states require `2px` outlines in the accent color with matching outline-offset. Disabled elements use 50% opacity with `cursor: not-allowed`. "NEVER remove focus indicators" emphasizes accessibility requirements.

**Animation:** Restraint is emphasized—animations should only use compositor properties like `transform` and `opacity`, never layout properties, and must stay under 200ms for interaction feedback.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/retool

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
