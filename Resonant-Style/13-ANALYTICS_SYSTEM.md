# 13 — TASTE & ANALYTICS SYSTEM

## Purpose

Taste turns authorised listening records and explicit corrections into understandable patterns, not a score that claims to define a person.

## Product areas

| Surface | Question answered |
| --- | --- |
| Overview | What is the shape of my listening right now? |
| Artists | Which artists recur, and how are they changing? |
| Genres | Which genre combinations show up in my history? |
| Eras | Which decades or release periods do I return to? |
| Moods | What emotional patterns appear in context? |
| Listening | How does taste change over time? |
| Taste Profile | What structured signals power Resonant’s explanations? |

## Taste Profile fields

Core artists, strong and secondary genres, preferred eras, energy preferences, familiarity preference, discovery tolerance, artist/album repetition tolerance, mood patterns, context patterns, known dislikes, playlist patterns, confidence, last updated, data sources, and calculation notes.

## Methodology rules

Every result includes provenance, freshness, confidence, and a human-readable calculation note. The Taste Engine is deterministic and side-effect-free. Findings are estimates, never identity claims. The empty profile must contain no invented artists, genres, eras, or counts.

## User correction

The future Edit My Taste flow lets a person mark a finding Correct, Sort of, or Wrong, and maintain “I love”, “I like”, “I don’t like”, and “Never recommend” lists. Observed data and explicit correction are separate sources.

## Visual language

Use editorial summaries, restrained charts, and clear comparison. A chart must answer a question. Provide numeric and textual alternatives. Avoid a generic dashboard wall.

## Illustration Required

**Purpose:** show data as a personal story.

**Description:** Taste overview with confidence, freshness, sources, calculation notes, and one restrained trend visual.

**Suggested composition:** large narrative headline, three quiet metrics, one chart, one methodology panel.

**Priority:** P0. **Assets:** verified empty Taste screen and future populated fixture with clearly labelled sample data.

## Related pages

[Color](07-COLOR_SYSTEM.md) · [AI](12-AI_SYSTEM.md) · [Accessibility](18-ACCESSIBILITY.md) · [Mockups](21-MOCKUPS.md)

## TODO

- Define authenticated Spotify ingestion and data freshness windows.
- Specify chart types, colour mapping, responsive behaviour, and user correction UI.
