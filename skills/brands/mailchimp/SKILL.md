# Mailchimp UI Skills Design System

**Color Foundation:**
The system uses a dark-light contrast approach with `#000000` for page backgrounds and `#2E114B` for primary actions. The palette includes semantic tokens for surfaces, text, borders, and state indicators (warning, success).

**Typography Standards:**
"MUST use `Inter` as primary font family" with specific scales ranging from 5px to 53px. Primary headings require 53px/extra_bold weight, while body text uses 31px/semi_bold.

**Spacing & Structure:**
"MUST use 4px grid for spacing" with defined scales: 1px, 2px, 3px, 4px, 5px, 6px, 11px, 13px. Border-radius follows a specific scale (0px through 25px) with "1px as default border-radius."

**Layout Requirements:**
Designs target 1920px viewport width with 607px main content height and 30px header height.

**Interactive Design:**
Focus states require `2px` outline in accent color with matching offset. Disabled elements use 0.5 opacity with `cursor: not-allowed`. Animations must respect `prefers-reduced-motion` and "NEVER exceed `200ms`" for interaction feedback.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/mailchimp

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
