# Resonant UI Kit / Design Reference

Static design-reference portal for Resonant. This folder is intentionally independent from the production application and does not import React, product routes, authentication, Spotify, Supabase, or application state.

## Source of truth

- Brand Book: Resonant Brand Book v0.5
- Typography roles: Inter Tight / Inter / Geist Mono
- Core verified palette: Canvas `#11100F`, Surface `#191816`, Accent `#D8B36A`, Mint Signal `#67F3C2`
- Spatial rhythm: 8px mental grid with rem-based implementation tokens

## Structure

- `index.html` — design portal and version information
- `foundations/index.html` — color, type, spacing, grid, surface, motion, icons, artwork
- `components/index.html` — controls, cards, navigation, music, review, taste, feedback, and state references
- `patterns/index.html` — search, playlist review, discovery, Spotify sync, AI explanation, onboarding, settings
- `examples/index.html` — composed workspace, player, taste, and playlist review surfaces
- `styles.css` — shared reference styling
- `assets/` — approved local brand and editorial assets

## Design rule

Every element must earn its place. If removing it makes the page stronger, it should be removed. If adding it does not make the story clearer, it should not exist.

## Usage

Open `index.html` directly in a browser or serve this folder as static files. The reference is safe to inspect and edit without affecting production code.
