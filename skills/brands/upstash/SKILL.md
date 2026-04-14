# Upstash UI Skills - Design System Guide

The Upstash UI Skills document provides comprehensive constraints for building interfaces aligned with Upstash's design aesthetic, emphasizing a light-mode approach with specific technical requirements.

## Key Design Principles

**Color System**: The system establishes a semantic token approach, with `#000000` as the page background and `#15B169` as the primary accent for actions and focus states. "MUST maintain text contrast ratio of at least 4.5:1 for accessibility."

**Typography**: Inter is the mandatory font family. The guidelines specify `100px / 700` weight for primary headings and `25px / 400` for body text, with directives to use `text-balance` for headings and `text-pretty` for body content.

**Spacing & Grid**: The system mandates a "4px grid for spacing" with specific increments (1px through 8px) and establishes `5px` as the default gap between elements.

**Layout Standards**: Design baseline is "1920px base viewport width" with consistent component patterns and a requirement to use `h-dvh` instead of `h-screen` for full viewport heights.

## Critical Constraints

Interactive elements require a "`2px` outline with accent color" for focus states. The guidelines strictly prohibit animation unless explicitly requested and restrict animations to compositor properties only (`transform`, `opacity`).

For destructive actions, "MUST use an AlertDialog for destructive or irreversible actions," and errors should display adjacent to their origin point rather than blocking workflows.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/upstash

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
