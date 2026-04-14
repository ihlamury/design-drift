# Lattice UI Skills Design System

## Key Design Principles

**Color Foundation:** The system uses "#FEFDFC" as the base background with "#26B177" as the primary accent for actions and focus states. "text contrast ratio of at least 4.5:1 for accessibility" must be maintained throughout.

**Typography:** All interfaces must employ Inter font exclusively. Primary headings use 71px at weight 700, while body text follows at 40px weight 700. The guidelines emphasize using "text-balance for headings and text-pretty for body text."

**Grid & Spacing:** A strict 4px grid governs all spacing decisions. The system restricts spacing to predefined scales (1-8px) and forbids arbitrary values to ensure consistency.

**Interactive Patterns:** Focus states require "2px outline with accent color" and matching outline-offset. Disabled states use 50% opacity with cursor indication. "AlertDialog for destructive or irreversible actions" is mandatory.

**Performance:** Animation is discouraged unless explicitly requested and must animate only compositor properties (transform, opacity), never layout properties. The system respects prefers-reduced-motion preferences.

The design system targets a 1920px viewport base with systematic constraints across borders (4px default radius), components, and interaction states to maintain visual coherence.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/lattice

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
