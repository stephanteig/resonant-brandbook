# Resonant Design System
## 10 — COMPONENT SYSTEM

## Purpose

Components make the web product coherent without flattening the difference between a player, a taste summary, a playlist review, and a dialog.

## Inventory

| Group | Verified components |
| --- | --- |
| Shell | Brand header, primary navigation, account actions, persistent player. |
| Music | Player bar, artwork tile, track row, playlist row, artist/album card. |
| Controls | Buttons, icon buttons, text inputs, selects, sliders, checkbox, toggle, tabs. |
| Dialogs | Account connection, confirmation, review, and Assistant surfaces. |
| Feedback | Toast stack, recovery banner, loading/progress, error and empty states. |

## Component contract

Document purpose, anatomy, variants, default/hover/focus/pressed/disabled/loading/selected states, keyboard behaviour, pointer behaviour, responsive behaviour, tokens, and edge cases. A component must not require hover to reveal essential information.

## Interaction rules

Use a visible focus ring. Make destructive or data-affecting actions explicit. Keep disabled controls explanatory where the reason is not obvious. Preserve listening context when moving between Home, Search, Library, Playlists, Discover, Taste, and Account.

## Example: track row

The track row communicates title, artist, album, duration, selected state, play state, and availability. Playing changes the persistent Player; selecting exposes the appropriate destination or action. It must distinguish provider-unavailable data from a genuinely empty result.

## Related pages

[Interaction patterns](25-INTERACTION_PATTERNS.md) · [Tokens](26-DESIGN_TOKENS.md) · [Accessibility](18-ACCESSIBILITY.md)

## TODO

- Add component anatomy diagrams and final token references.
- Add the canonical Figma component and code component names.
## State documentation example

For a primary button, document label, icon use, hover, focus, pressed, disabled, loading, success feedback, and error recovery. For a track row, document selected, playing, unavailable, empty, and provider-error states.

## Do / don’t

Do compose screens from named components. Don’t create one-off variants that differ only by padding. Do expose a disabled reason. Don’t use a toast as the only record of a failed export.

## Implementation notes

The source uses React components and Lucide icons. Keep visual token names independent from CSS implementation and test component states in isolation.
