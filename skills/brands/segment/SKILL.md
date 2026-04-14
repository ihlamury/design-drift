# Segment UI Skills Design System

This is an opinionated design system for building interfaces with Segment's aesthetic. Here are the key constraints:

## Core Design Principles

**Color Palette:** The system uses a curated set of semantic tokens including `#0748D8` for page backgrounds and `#94C2F0` for primary actions. "MUST maintain text contrast ratio of at least 4.5:1 for accessibility."

**Typography:** Inter is the mandatory font family. The sizing scale ranges from 5px to 50px, with "heading-1" using 50px/700 weight and body text at 31px/500 weight. The guidelines specify using `text-balance` for headings and `text-pretty` for body text.

**Spacing & Layout:** A strict 4px grid system governs all spacing decisions. "NEVER use arbitrary spacing values (use design scale)." The base viewport width is 1920px, and designers should use `h-dvh` rather than `h-screen` for full-height elements.

**Borders:** A minimal border approach with 1px width and 6px or 7px radius values only.

## Interaction & Behavior

Focus states require "2px outline with accent color (#94C2F0)" and matching outline-offset. Destructive actions must use AlertDialog components, and error messages should appear contextually near the triggering action.

**Animation:** Animations are discouraged unless explicitly requested. When used, they're limited to compositor properties (transform, opacity) with a 200ms maximum duration, respecting `prefers-reduced-motion`.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/segment

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
