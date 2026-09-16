# 12 — AI SYSTEM

## Purpose

Assistant features should help where context matters, while Resonant remains useful without a chatbot.

## Product position

AI appears at the point of need: improve a playlist, explain taste, find a different listen, or build a collection. It should not dominate the shell or become a single blank conversation screen.

## Verified direction

The Masterplan defines an Assistant area and context-aware AI features. Current repository work keeps Assistant as a future product area while the core shell and data contracts are established.

## Contextual entry points

| Surface | Useful action |
| --- | --- |
| Playlist | Improve this playlist; explain balance; propose changes. |
| Artist | Find similar artists. |
| Taste | Explain my music taste. |
| Discover | Find something different. |
| Builder | Create a playlist from a brief and taste context. |

## Principles

AI must show its context, explain its reasoning, preserve user agency, and distinguish observation from invention. Suggestions are reviewable. Playlist changes require Keep, Remove, Unsure, or an equivalent explicit decision before mutation.

## Safety and privacy

User-owned music data is authorized before use. Secrets remain server-side. AI must not expose Spotify tokens, private account information, or unreviewed third-party content. The assistant must not claim to know a person’s taste perfectly.

## States

Unavailable, awaiting Spotify context, thinking, suggestion ready, user reviewing, applied, rejected, failed, and stale context. Errors should preserve the request and explain retry.

## Illustration Required

**Purpose:** show AI as a quiet layer inside the product.

**Description:** playlist review card, taste explanation card, and discovery explanation—not a chatbot hero.

**Suggested composition:** place each action beside the source context and an explicit review action.

**Priority:** P0. **Assets:** approved product copy and future Assistant component direction.

## Related pages

[Taste](13-ANALYTICS_SYSTEM.md) · [Playlists](15-LIBRARY_SYSTEM.md) · [Discovery](14-DISCOVERY_SYSTEM.md) · [Writing](04-WRITING_GUIDE.md)

## TODO

- Define the Assistant UI and model/provider boundary.
- Specify data retention, AI disclosure, feedback, and review-before-write interaction.
