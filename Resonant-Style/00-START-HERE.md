# Resonant Design System
## 00 — START HERE

> Read this document before making a brand, product, or marketing decision.

## Purpose

This repository defines the shared language for Resonant: a context-first personal music control center. It is written for designers, developers, writers, marketers, partners, and anyone preparing the future Canva Brand Book.

## The product in one sentence

Resonant helps people listen with context: to find music, understand taste, shape playlists, and discover what belongs next.

## Verified Version 1 scope

The product source implements a public web foundation for **Home**, **Search**, **Library**, **Playlists**, **Discover**, **Taste**, **Account**, and a global **Player** surface. It also establishes Spotify OAuth with PKCE, server-side token handling, Supabase contracts, a deterministic Taste Engine, an explainable Playlist Review Engine, responsive navigation, and explicit loading/empty/error states. Assistant, deep playback, data sync, richer discovery, and automation remain phased product work.

## Governing idea

Music comes first. The interface should help a person listen, understand, organize, and discover; it should not turn listening into a generic dashboard. Artwork and visual energy support the music, while controls remain calm and legible.

## How to use the system

1. Verify behaviour in [the product repository](https://github.com/stephanteig/resonant).
2. Start with the relevant foundation chapter.
3. Explain the musical or user problem before specifying UI.
4. Cover states, keyboard access, responsive behaviour, and recovery.
5. Mark anything unverified as `TODO`.

## Scope boundary

The current product is not a social network, popularity scoreboard, black-box recommendation feed, or giant chatbot. Spotify is the first provider, but Resonant’s identity is context, taste, and user agency.

## Related pages

[Project context](02-PROJECT_CONTEXT.md) · [Design philosophy](03-DESIGN_PHILOSOPHY.md) · [Product requirements](23-PRODUCT_REQUIREMENTS.md) · [Brand Book structure](22-BRAND_BOOK_STRUCTURE.md)

## TODO

- Confirm the final public brand-owner name and trademark guidance.
- Add approved Figma library links when the library exists.
- Add final production screenshots after the current release is frozen.
