# Resonant Design System
## 02 — PROJECT CONTEXT

## Purpose

This is the product context for every brand, UX, marketing, and visual decision in Resonant.

## Product definition

Resonant is a personal control center for music. It brings listening, taste, playlists, discovery, and music-aware assistance into one web application while keeping product areas explicit and understandable.

Spotify is the first music source. It is an integration, not Resonant’s identity. Google creates the Resonant account; Spotify is connected separately and provides the music context.

## Product promise

Resonant helps a person listen with context: to find music, understand patterns, shape playlists, and discover something new without losing the thread that made the music matter.

## Product areas

| Area | Role | Current route/surface |
| --- | --- | --- |
| Home | Orient the person and explain the product. | `/` |
| Search | Find songs, artists, albums, and playlists in one place. | `/search` |
| Library | Organise Liked Songs, saved albums, artists, playlists, and recently played. | `/library` |
| Playlists | Edit, review, and eventually build listening collections. | `/playlists` |
| Player | Persistent listening surface and playback context. | Global player bar; expanded view planned. |
| Discover | Personal discovery with explanations and risk levels. | `/discover`; deeper surfaces planned. |
| Taste | Listening patterns, history, trends, and taste profile. | `/taste`; deeper surfaces planned. |
| Assistant | Context-aware AI support where it helps. | Planned product area. |

## Core journey

```text
Open Resonant → connect account → connect Spotify → listen or search
      ↓
save / organize → see taste patterns → review a playlist → discover with context
```

The current implementation deliberately uses honest disconnected states and does not fabricate tracks, artists, counts, recommendations, or identity.

## Audience

People who care about music as a personal archive: curious listeners, playlist makers, collectors, and anyone who wants more context than a standard streaming interface provides.

## Product boundaries

Resonant is not a social feed, a generic data dashboard, or a single giant chatbot. AI supports specific jobs such as playlist improvement, taste explanation, discovery, and building; the core product must remain useful without AI.

## Architecture as a brand constraint

The repository is a single Next.js web surface with explicit route ownership and shared packages. Local, Preview, and Production are separate contexts. The interface must make environment markers and connection state visible outside Production.

## Related pages

[Design philosophy](03-DESIGN_PHILOSOPHY.md) · [Player](11-MUSIC_PLAYER.md) · [Taste](13-ANALYTICS_SYSTEM.md) · [Discovery](14-DISCOVERY_SYSTEM.md) · [Desktop and mobile](28-DESKTOP.md)

## TODO

- Confirm the final product-area release matrix and which planned routes are active in the next release.
- Document the first authenticated data-sync flow once implemented.
