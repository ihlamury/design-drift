# Mobbin UI Skills Design System

This is a comprehensive design system document for creating Mobbin-inspired interfaces. Here are the key takeaways:

## Core Principles

The system emphasizes "light mode, Inter font, 4px grid" as foundational constraints. It mandates using `#FFFFFF` backgrounds and maintains a deliberately reduced color palette of 11 colors for consistency.

## Typography Standards

All text must use Inter as the exclusive font family. Primary headings require `75px` at weight 700, while body text uses `18px` at weight 400. The system limits font weights to bold, regular, and medium only.

## Spacing & Layout

The design enforces a strict 4px grid system with permitted spacing values of 2px, 3px, 4px, 5px, and 18px. Border radius choices are limited to 8px, 21px, 22px, and 28px. Layouts should target 1920px viewport width.

## Interactive Behaviors

Focus states require "2px outline with accent color (#5E6AD2)" and matching outline-offset. Disabled states apply 50% opacity with a `not-allowed` cursor. Animations must respect `prefers-reduced-motion` and never exceed 200ms.

## Accessibility Requirements

Text contrast must maintain at least 4.5:1 ratios. Icon-only buttons require `aria-label` attributes, and destructive actions demand AlertDialog confirmation.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/mobbin

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
