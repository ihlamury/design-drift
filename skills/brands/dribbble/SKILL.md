# Dribbble UI Skills Design System

**Core Aesthetic:** Light mode interfaces using Inter font on a 4px grid system with a dark page background (#000000) and raised light surfaces (#FEFEFD).

**Color Foundation:** The system emphasizes a restrained palette with "#F2B5D7" serving as the primary accent for actions and focus states, while maintaining WCAG contrast ratios of at least 4.5:1.

**Typography:** Inter is the sole font family, with headings at 42px/700 weight and body text at 14px/300 weight. The guidelines specify using `text-balance` for headings and applying `tabular-nums` for numeric content.

**Spacing & Grids:** All spacing must follow a 4px scale (1px through 8px), with 4px as the default gap between elements. Border radius options range from 1px to 23px, with 14px as the standard and 22px+ for pill-shaped components.

**Interactive Patterns:** Focus states require a 2px outline in the accent color with 2px offset. Disabled states use 50% opacity. Destructive actions must trigger an AlertDialog, and all icon-only buttons need `aria-label` attributes.

**Animation Constraints:** Animations are prohibited unless explicitly requested and limited to compositor properties (transform, opacity) with maximum 200ms duration, respecting motion preferences.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/dribbble

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
