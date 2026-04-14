# Neon UI Skills Design System

The Neon UI Skills document is a comprehensive design system guide for building dark-mode interfaces with specific constraints and patterns.

## Key Specifications

**Color Foundation:** The system mandates `#000000` as the page background with carefully selected semantic tokens. "MUST use dark backgrounds (lightness < 20) for primary surfaces" and maintain "text contrast ratio of at least 4.5:1 for accessibility."

**Typography Requirements:** Inter is the required font family. Primary headings must be 54px at weight 700, while body text should be 16px at weight 500. The guide specifies "MUST use `text-balance` for headings and `text-pretty` for body text."

**Spacing & Layout:** All spacing follows "a 4px grid" system with default gaps of 5px. The base viewport width is 1920px. Border radius options are limited to: 16px, 17px, 19px, or 21px.

**Interactive States:** Focus indicators require a "2px outline with accent color (#5E6AD2)" and matching outline-offset. Disabled states use "opacity: 0.5" with "cursor: not-allowed."

**Animation Constraints:** The system explicitly states "NEVER add animation unless it is explicitly requested" and "NEVER animate layout properties (`width`, `height`, `top`, `left`, `margin`, `padding`)."

**Accessibility:** Icon-only buttons must include `aria-label` attributes, and destructive actions require AlertDialog confirmation. The system emphasizes respecting `prefers-reduced-motion`.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/neon

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
