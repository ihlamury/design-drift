# Cal UI Skills - Design System Guidelines

**Color Foundation**
The palette centers on light mode with `#FDFDFD` as the primary page background. The system maintains "text contrast ratio of at least 4.5:1 for accessibility" and includes semantic tokens for surfaces, text hierarchy, and states.

**Typography**
Inter is the exclusive font family, with `70px` / `700` weight for primary headings and `16px` / `400` for body text. The guidelines specify using `text-balance` for headings and `text-pretty` for body content.

**Spacing & Layout**
A strict 4px grid governs all spacing, with `5px` as the default gap between elements. The base viewport is designed for 1920px width, and developers must "use `h-dvh` for full viewport height" rather than `h-screen`.

**Interaction Standards**
Focus states require a `2px` outline with `#5E6AD2`, while disabled elements use `opacity: 0.5` with `cursor: not-allowed`. Destructive actions must trigger an AlertDialog component.

**Animation Constraints**
The system prohibits animation unless explicitly requested and restricts movement to compositor properties only, keeping interactions under 200ms while respecting `prefers-reduced-motion` preferences.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/cal

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
