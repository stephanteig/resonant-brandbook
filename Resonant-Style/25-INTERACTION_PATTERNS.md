# 25 — INTERACTION PATTERNS

## Purpose

Shared patterns reduce cognitive load across the web product.

## Core patterns

| Pattern | Guidance |
| --- | --- |
| Select then inspect | Selection keeps the song, artist, album, or playlist context visible. |
| Search then deepen | A result opens a related artist, album, playlist, or Player context. |
| Observe then explain | Taste and recommendation surfaces show source, freshness, and confidence. |
| Propose then review | Playlist findings and Builder suggestions remain reviewable before mutation. |
| Connect then use | Provider-dependent content remains unavailable until Spotify is connected. |
| Error then recover | OAuth, provider, loading, and route errors explain a safe next action. |

## Keyboard and pointer

Every pointer operation needs a keyboard path where the platform permits it. Reordering playlist tracks must have a precise alternative or documented limitation. Keep targets large enough and focus order predictable.

## Edge cases

Signed out, missing Spotify, expired provider token, empty library, no recommendations, unavailable route, failed OAuth, and stale or incomplete data are first-class states.

## Related pages

[Components](10-COMPONENT_SYSTEM.md) · [Loading/error states](27-LOADING_ERROR_STATES.md) · [Player](11-MUSIC_PLAYER.md)
## Pattern checklist

Before shipping an interaction, verify entry point, primary action, cancel path, undo/recovery path, keyboard path, focus return, status announcement, disabled reason, and narrow-desktop behaviour. The checklist applies to a playlist change and a Spotify connection.

## TODO

- Add interaction diagrams for Spotify connection, playlist review, and provider retry.
