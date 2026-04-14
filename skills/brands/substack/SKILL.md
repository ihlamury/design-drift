# Substack UI Skills - Design System Overview

This MIT-licensed design system provides constraints for building interfaces aligned with Substack's aesthetic, emphasizing light mode, Inter typography, and a 4px grid foundation.

## Core Principles

**Color Strategy:** "MUST use `#FFFFFF` as page background (`surface-base`)" with a deliberately constrained palette of approximately 15 colors. The system prioritizes accessibility, requiring text contrast ratios of at least 4.5:1.

**Typography:** The design system standardizes on Inter font exclusively, with "MUST use `36px` / `semi_bold` for primary headings" and `17px` weight 500 for body text. Text rendering uses `text-balance` for headings and `text-pretty` for body content.

**Spacing & Rhythm:** All spacing adheres strictly to a 4px grid. "SHOULD use 4px as default gap between elements" with predefined scales preventing arbitrary values.

**Interactive Design:** Focus states require "2px outline with accent color (`#5E6AD2`)" and matching outline-offset. The system explicitly states "NEVER remove focus indicators," emphasizing accessibility.

**Animation Constraints:** "NEVER add animation unless it is explicitly requested" and animations must respect `prefers-reduced-motion`. Only compositor properties (transform, opacity) animate, never layout properties.

**Viewport Baseline:** The system designs for 1920px width, using `h-dvh` instead of `h-screen` for proper viewport height calculation on modern devices.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/substack

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
