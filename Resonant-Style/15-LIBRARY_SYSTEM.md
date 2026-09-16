# 15 — LIBRARY SYSTEM

## Purpose

Library is the considered home for the music a person has saved and played through Spotify.

## Areas

Liked Songs, saved albums, artists, playlists, and recently played. The current route is an honest empty surface until Spotify is connected; no fake content is shown.

## Information hierarchy

1. What collection is being viewed.
2. Artwork, title, artist, and save/listen context.
3. Search, sort, filter, and play actions.
4. Secondary metadata and relationship signals.

## Principles

Fast, searchable, visual, and personal. Sorting and filtering should be meaningful improvements over a plain list. Artwork leads, but text remains primary for access and scanning.

## Edge cases

Handle an empty library, revoked Spotify permission, deleted item, duplicate saved item, unavailable artwork, long artist names, and recently played history with no records. Never substitute popularity data for missing user data.

## Illustration Required

**Purpose:** show Library as an archive rather than a grid of generic cards.

**Description:** saved albums, artists, and playlists with sort/filter controls and one selected item.

**Suggested composition:** one editorial hero row followed by a dense but calm list; show artwork, titles, and context together.

**Priority:** P0. **Assets:** cleared Spotify artwork fixture and responsive screen capture.

## Related pages

[Search](16-SEARCH_SYSTEM.md) · [Player](11-MUSIC_PLAYER.md) · [Typography](08-TYPOGRAPHY.md)

## TODO

- Define sorting/filtering options and list/grid behaviour.
- Confirm Spotify scopes, pagination, artwork fallback, and caching.
