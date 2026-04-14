# OpenAI UI Skills - Design System

This is an opinionated design system for building interfaces with OpenAI's aesthetic. Key specifications include:

**Color Palette:**
The system uses a light mode foundation with `#FFFFFF` as the page background and maintains "text contrast ratio of at least 4.5:1 for accessibility."

**Typography:**
Inter is the required font family. Primary headings use `24px` / `semi_bold`, while body text is `14px` / `400`. The system limits fonts to regular, semi-bold, and light weights only.

**Spacing & Layout:**
All spacing follows a 4px grid system. The design targets a 1920px viewport with a 202px sidebar width. "NEVER use arbitrary spacing values (use design scale)."

**Components & States:**
Buttons include ghost variants with transparent backgrounds. Focus states require a `2px` outline with `#5E6AD2` accent color. The system mandates `AlertDialog` for destructive actions and prohibits paste blocking in input fields.

**Animation:**
"NEVER add animation unless it is explicitly requested." Animations are limited to compositor properties (`transform`, `opacity`) and must not exceed 200ms, with respect for `prefers-reduced-motion`.

The design system enforces consistency through constrained values across borders (16px-22px radius), interactive states, and performance guidelines that avoid expensive operations like large blur filters.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/openai

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
