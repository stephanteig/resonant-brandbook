# 28 — DESKTOP

## Purpose

Desktop is the verified Version 1 web context and gives Resonant room for simultaneous listening, discovery, playlist, and taste surfaces.

## Product anatomy

Header and primary navigation remain stable; route content occupies the main reading surface; the persistent Player preserves listening context; dialogs handle account and provider setup.

## Behaviour

Support pointer precision, keyboard navigation, dense result lists, artwork grids, playlist tables, and explanatory charts. Keep the current route and listening context visible when moving between surfaces. Do not hide connection state, loading status, or recovery actions at narrow desktop widths.

## Accessibility

Test Windows scaling, high-DPI displays, keyboard-only use, screen readers, and 200% zoom. Verify that dialogs do not open off-screen.

## TODO

- Add supported window dimensions and a breakpoint matrix from production testing.
- Add Windows 10/11 and installer/portable differences to the release-specific appendix.
## Recommended verification widths

Use the widest and narrowest supported production windows as test fixtures. Record actual values in the release appendix; do not invent breakpoint numbers in the Brand Book.

## Do / don’t

Do keep primary navigation, connection state, and the Player available. Don’t let a modal obscure the only indication that a provider is disconnected or an analysis is still running.
