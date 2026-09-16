# Resonant Design System
## 01 — MASTER PROMPT

## Objective

Create precise Markdown documentation for the Resonant brand and product system. The output must be sufficient for a designer to assemble the Canva Brand Book and for a developer to understand intent without inventing behaviour.

## Purpose

This prompt is the editorial contract for future contributors and generated documentation.

## Authority order

1. Implemented product source and tests in [stephanteig/resonant](https://github.com/stephanteig/resonant).
2. Product documentation and release notes.
3. This brandbook’s principles and visual rules.
4. Explicitly labelled future considerations.

When sources conflict, use the higher source and add a TODO describing the conflict. Never silently convert a roadmap idea into a shipped feature.

## Required page anatomy

Every substantial page should answer: purpose, problem, rationale, rules, usage, states and edge cases, accessibility, responsive behaviour, implementation notes, examples, related pages, and TODOs.

## Writing rules

- Explain why before how.
- Prefer concrete nouns and active verbs.
- Keep “Resonant”, “track”, “artist”, “album”, “playlist”, “taste”, “discovery”, “connection”, and “player” consistent.
- Say “Spotify connection” when referring to provider access; do not imply that Resonant owns or replaces Spotify’s catalogue.
- Distinguish verified product behaviour from future direction with explicit labels such as **Current**, **Planned**, and **TODO**.

## Screen rule

Any screen reference must include purpose, audience, hierarchy, components, interactions, responsive behaviour, accessibility, future improvements, and an `Illustration Required` brief when a visual is needed. See [Mockups](21-MOCKUPS.md).

## Non-goals

Do not modify application code, prescribe an alternate architecture, document unimplemented mobile or native products as fact, or present a concept mockup as a verified screenshot.

## Quality gate

Before publishing a chapter, check product truth, terminology, cross-references, keyboard behaviour, contrast, reduced motion, loading, empty, error, and recovery states.

## TODO

- Add the final release/version pin used for each future documentation pass.
