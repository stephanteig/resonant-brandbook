# 17 — ICONOGRAPHY

## Purpose

Icons make listening, navigation, and account controls recognizable without adding visual noise.

## System

The current interface uses Lucide React icons. Preserve their outlined, rounded character and consistent optical weight. The inherited 24×24, 2 px, rounded-cap guidance remains the working basis, subject to final library validation.

## Categories

Navigation, transport, search, library, playlists, discovery, taste, account, AI, audio, settings, help, warnings, and status.

## Rules

Use one icon per action, pair unfamiliar icons with labels, and provide an accessible name. Do not use colour alone, mix arbitrary filled and outlined families, rotate icons for decoration, or use a waveform as a generic loading spinner.

## States

Default, hover, focus, pressed, active, disabled, loading, and error must be legible at 16–24 px. A state change should be understandable in text or shape as well as colour.

## TODO

- Audit the current icon inventory and publish canonical Figma/code names.
- Add optical alignment and small-size tests to the Brand Book.
## Accessibility checklist

Every icon-only control needs an accessible name, visible focus, and a tooltip or adjacent label where meaning is not obvious. Decorative icons should be hidden from the accessibility tree.

## Related pages

[Visual language](VISUAL_LANGUAGE.md) · [Accessibility](18-ACCESSIBILITY.md) · [Components](10-COMPONENT_SYSTEM.md)

## Implementation notes

Use Lucide React where possible. A custom icon requires its 24×24 grid, stroke, caps, joins, optical bounds, and 16 px fallback documented before library adoption.
