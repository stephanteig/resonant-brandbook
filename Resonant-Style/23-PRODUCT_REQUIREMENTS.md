# 23 — PRODUCT REQUIREMENTS

## Purpose

This page keeps the brand narrative aligned with the approved product direction and prevents visual documentation from inventing functionality.

## Product goals

- Listen with more context.
- Find and organize music without losing personal meaning.
- Understand taste as patterns, not a verdict.
- Discover relevant music with a reason behind it.
- Keep user corrections and decisions in control.
- Make Spotify integration, account state, privacy, and freshness visible.

## Current product foundation

The repository implements a Next.js web surface with shared shell and route boundaries for Home, Search, Library, Playlists, Discover, Taste, and Account. It includes responsive navigation, a global empty Player bar, static empty/connected states, Google authentication direction, Spotify OAuth with PKCE, server-side token handling, Supabase storage contracts, a deterministic Taste Engine, and an explainable Playlist Review Engine.

## Product direction

The product direction includes Spotify playback, richer Player controls, Library organization, playlist editing and review, a future Builder flow, Discover levels (Safe picks, Explore, Wildcard), Taste methodology and correction, and contextual Assistant support. Label each item by release status in the Brand Book; do not present direction as shipped behaviour.

## Data and trust requirements

Google authenticates the Resonant account. Spotify is a separate connection. Provider tokens stay server-side and are encrypted at rest. Local, Preview, and Production environments remain separate. User-owned tables require RLS and ownership predicates. No secret, token, or copied private listening data belongs in screenshots or docs.

## Feature documentation contract

Every feature page explains purpose, user problem, rationale, ideal workflow, data boundary, states, edge cases, accessibility, responsive behaviour, implementation notes, illustration brief, and TODOs.

## Non-requirements

Resonant is not a social network, a popularity scoreboard, a black-box recommender, or a giant chat interface. Automations, additional music providers, deeper Assistant work, and ChatGPT integration are later-stage direction.

## Related pages

[Project context](02-PROJECT_CONTEXT.md) · [AI](12-AI_SYSTEM.md) · [Taste](13-ANALYTICS_SYSTEM.md) · [Mockups](21-MOCKUPS.md)

## TODO

- Add a release-labelled feature matrix from the current `specs/` directory.
- Confirm the first full Spotify data-sync milestone and retention policy.
