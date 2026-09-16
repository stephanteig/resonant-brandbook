# 33 — TASTE PROFILE

## Purpose

Taste Profile is the transparent layer that helps Resonant understand a listener without reducing them to one score.

## Profile anatomy

Core artists, strong genres, secondary genres, preferred eras, energy preferences, familiarity preference, discovery tolerance, artist repetition tolerance, album repetition tolerance, mood patterns, context patterns, known dislikes, playlist patterns, confidence, last updated, sources, and calculation notes.

## Narrative pattern

Start with an understandable sentence, support it with a small number of observations, and show how fresh and reliable the data is. Keep methodology available but secondary to the human-readable summary.

## Correction model

Observed data and explicit user corrections are separate. A person can mark an observation Correct, Sort of, or Wrong and maintain positive, negative, and never-recommend preferences.

## Empty state

Before Spotify history exists, show confidence 0%, “Not yet” for update, no sources, and a clear explanation that no artists, genres, or eras are assumed.

## Illustration Required

**Purpose:** make methodology feel humane.

**Description:** profile header, three metadata metrics, one narrative insight, one chart, and correction controls.

**Suggested composition:** large editorial statement on the left, evidence and methodology on the right.

**Priority:** P0. **Assets:** labelled fixture data, not private user history.

## Related pages

[Taste and analytics](13-ANALYTICS_SYSTEM.md) · [AI](12-AI_SYSTEM.md) · [Accessibility](18-ACCESSIBILITY.md)

## TODO

- Define profile visualizations, confidence language, update triggers, and correction persistence.
