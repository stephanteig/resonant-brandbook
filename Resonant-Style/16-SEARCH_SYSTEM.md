# 16 — SEARCH SYSTEM

## Purpose

One global search helps a person move directly to songs, artists, albums, and playlists without losing context.

## Scope

The current product surface is Search with a clear disconnected state. The implementation direction supports Spotify search through a typed server-side client, with a maximum search page size of 10 and explicit input validation.

## Result architecture

```text
Query → organized result page
       ├── Songs
       ├── Artists
       ├── Albums
       └── Playlists
```

One organized result page is preferable to separate opaque searches. Result groups should preserve artwork, title, artist/owner, type, and the action that follows.

## Principles

Fast, predictable, forgiving, and context-preserving. Trim whitespace, keep the query visible, make scope obvious, and provide a calm no-result state. A search such as `Daft Punk` should not require the user to understand provider terminology.

## Accessibility and responsive behaviour

Use a labelled search input, keyboard focus, visible result headings, semantic links, and no colour-only type cues. At 320 px, results stack and controls remain reachable without horizontal scrolling.

## Edge cases

Empty query, no result, ambiguous duplicate names, slow provider response, expired token, unavailable Spotify, explicit disconnect, and unsupported endpoint. Explain the next action without exposing provider errors or secrets.

## Illustration Required

**Purpose:** show search as a bridge through the catalogue.

**Description:** one query field, grouped results, selected artist/album context, and mobile stacked result groups.

**Suggested composition:** an oversized search field with thin result bands underneath.

**Priority:** P0. **Assets:** approved fixture data and mobile screen.

## Related pages

[Library](15-LIBRARY_SYSTEM.md) · [Writing](04-WRITING_GUIDE.md) · [Accessibility](18-ACCESSIBILITY.md)

## TODO

- Define result ranking, debounce, pagination, keyboard navigation, and provider error copy.
