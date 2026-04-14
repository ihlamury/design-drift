# Airtable UI Skills - Design System Guidelines

**Color Foundation:**
- Background: `#FDF5EA` (warm cream tone)
- Primary text: `#B5B8BC` (light gray)
- Raised surfaces: `#13151D` (near-black)
- Strict 4.5:1 contrast ratio requirement

**Typography Standards:**
- "MUST use `Inter` as primary font family" with consistent weights
- Primary heading: 145px/700 weight
- Body text: 24px/400 weight
- Apply `text-balance` for headings, `text-pretty` for body

**Spacing & Layout:**
- Mandatory 4px grid system for all spacing
- 7px border-radius as default scale
- 1920px viewport baseline
- Use `h-dvh` instead of `h-screen`

**Interactive Principles:**
- Focus states require "2px outline with accent color (#5E6AD2)" and 2px offset
- Hover effects lighten primary buttons by 10%
- Disabled state: 0.5 opacity + not-allowed cursor
- Destructive actions demand AlertDialog confirmation

**Animation Constraints:**
- Only animate compositor properties (transform, opacity)
- Never exceed 200ms for feedback
- Respect `prefers-reduced-motion` preference
- No layout animations

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/airtable

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
