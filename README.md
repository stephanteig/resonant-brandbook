# Resonant Brand Book source

Version 1 of the Resonant brand and product design system. This repository is the source for the future Canva Brand Book, printable PDF, internal design guidance, marketing material, and developer-facing references.

## Product truth

Resonant is a personal control center for music. It brings listening, taste, playlists, discovery, and music-aware assistance into one web application. Spotify is the first music source; the product’s identity is the context it adds around listening, not the provider itself. The current foundation includes Home, Search, Library, Playlists, Discover, Taste, Account, a global Player surface, responsive navigation, Spotify OAuth with PKCE, Supabase contracts, a deterministic Taste Engine, and an explainable Playlist Review Engine.

The product repository is the authority for implemented behaviour. The current reference is [github.com/stephanteig/resonant](https://github.com/stephanteig/resonant). This brandbook never replaces the application source, product contract, or implementation specs.

## Read in order

1. [00 — Start here](Resonant-Style/00-START-HERE.md)
2. [02 — Project context](Resonant-Style/02-PROJECT_CONTEXT.md)
3. [03 — Design philosophy](Resonant-Style/03-DESIGN_PHILOSOPHY.md)
4. [05 — Brand identity](Resonant-Style/05-BRAND_IDENTITY.md)
5. [07 — Color system](Resonant-Style/07-COLOR_SYSTEM.md)
6. [09 — Layout and grid](Resonant-Style/09-LAYOUT_GRID.md)
7. [10 — Component system](Resonant-Style/10-COMPONENT_SYSTEM.md)
8. [11 — Music player](Resonant-Style/11-MUSIC_PLAYER.md)
9. [12 — Local AI system](Resonant-Style/12-AI_SYSTEM.md)
10. [21 — Mockups](Resonant-Style/21-MOCKUPS.md)
11. [Visual language](Resonant-Style/VISUAL_LANGUAGE.md)
12. [Art direction](Resonant-Style/ART_DIRECTION.md)
13. [Product art direction](Resonant-Style/PRODUCT_ART_DIRECTION.md)

## Repository map

| Chapter | Scope |
| --- | --- |
| 00–04 | Orientation, product context, philosophy, and writing |
| 05–10 | Brand identity and visual foundations |
| 11–16 | Player, AI, taste, discovery, library, and search |
| 17–20 | Iconography, accessibility, imagery, website, and visual language guidance |
| 21–23 | Screen specifications, Brand Book assembly, and product requirements |
| 24–30 | Motion, interaction patterns, tokens, states, desktop, mobile, and downloads |
| 31–34 | Account, playlist workflows, taste profile, sound identity, and product art direction |

The visual-language layer is documented in `VISUAL_LANGUAGE.md`, `ART_DIRECTION.md`, and `PRODUCT_ART_DIRECTION.md`. Together they define how Resonant remains recognisable beyond its logo, type, colour, and spacing systems.

## Design Reference

[`Design-Reference/`](Design-Reference/index.html) is the official static UI Kit and design-reference portal for this repository. It translates the Brand Book into inspectable foundations, reusable component states, interaction patterns, and composed product examples.

Its purpose is to keep the visual language operational across the website, desktop app, future mobile surfaces, marketing mockups, and product screenshots. It does not replace the Brand Book or the product repository: the Brand Book defines the identity and rules, the Design Reference demonstrates how those rules compose, and the application repository remains authoritative for implemented behaviour.

Future implementation work should reference both [`Resonant-Style/`](Resonant-Style/00-START-HERE.md) and [`Design-Reference/`](Design-Reference/index.html). The Design Reference is static by design and is not a production component library.

`PROJECT_STATUS.md` records the verified scope, open TODOs, and the recommended Canva production path.

For implementation handoff, start with [`CODEX_HANDOFF.md`](CODEX_HANDOFF.md). The current publication output is [`Resonant-Brandbook-v0.5.pdf`](Resonant-Brandbook-v0.5.pdf).

## Documentation rules

- Explain the reason before the rule.
- Document implemented behaviour as fact; label proposals and gaps as `TODO`.
- Keep “Resonant”, “track”, “artist”, “album”, “playlist”, “taste”, “discovery”, “connection”, and “player” consistent.
- Do not document streaming-service features, social features, hosted analytics, or a mobile application unless the product repository implements them.
- Do not modify application code from this repository.
