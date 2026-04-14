# Supabase UI Skills - Design System Guide

This document outlines an opinionated design system for creating Supabase-style interfaces, emphasizing dark mode aesthetics, consistency, and accessibility.

## Core Design Principles

The system mandates several foundational constraints:

**Color Foundation:** "MUST use dark backgrounds (lightness < 20) for primary surfaces" with `#121212` as the base page background. The palette includes semantic tokens like `surface-raised` (#000000) for cards and `success` (#3DB576) for confirmations, maintaining a minimum contrast ratio of 4.5:1.

**Typography:** "MUST use `Inter` as primary font family" exclusively. Primary headings require 56px/700 weight, while body text uses 15px/400 weight. Text rendering preferences include `text-balance` for headings and `text-pretty` for body content.

**Spacing & Layout:** The system enforces a 4px grid with predefined scales (3px, 4px, 5px, 6px, 16px, 40px, 61px). Border-radius values must come from a specific scale: 3px through 16px in increments. The base viewport width is 1920px.

## Interaction & Performance

Interactive components require careful attention: "MUST use `2px` outline with accent color (`#5E6AD2`)" for focus states, and animations must respect reduced motion preferences while never exceeding 200ms for feedback. Destructive actions require AlertDialog confirmation.

The system explicitly prohibits layout animations and `will-change` outside active contexts, prioritizing performance on compositor properties only.

## Complementary DESIGN.md

This skill pairs with the corresponding DESIGN.md from awesome-design-md where available:
https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/supabase

The DESIGN.md (fetched at lock time) provides visual atmosphere and additional color tokens.
This SKILL.md provides MUST/SHOULD/NEVER enforcement rules.
The drift scanner reads both files to extract tokens dynamically — no hardcoded values.
