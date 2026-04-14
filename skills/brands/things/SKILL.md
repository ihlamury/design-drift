# Things UI Skills - Design System

This is an MIT-licensed design system for creating interfaces matching Things's aesthetic. Here are the key constraints:

**Color Palette:**
- Background: `#EEF2F5` (light blue-gray)
- Primary accent: `#729AE0` (blue)
- Text colors range from `#2F343B` (dark) to `#9499A1` (light gray)
- "SHOULD limit color palette to 5 distinct colors"

**Typography:**
- Font: Inter only
- Heading: 49px, weight 700
- Body: 23px, weight 400
- "MUST use `text-balance` for headings and `text-pretty` for body text"

**Layout & Spacing:**
- 8px grid system required
- 1920px base viewport width
- 72px default gap between elements
- "NEVER use arbitrary spacing values (use design scale)"

**Interactive Elements:**
- Focus states: 2px outline in accent color with 2px offset
- Disabled: 50% opacity + `cursor: not-allowed`
- Hover: lighten buttons by 10% or use raised surface background

**Animation Rules:**
- "NEVER exceed `200ms` for interaction feedback"
- Compositor properties only (transform, opacity)
- Respect `prefers-reduced-motion`

**Critical Constraints:**
- No arbitrary border-radius values
- 1px subtle borders for separation
- Use `h-dvh` instead of `h-screen`
- Require `aria-label` on icon-only buttons

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/things

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
