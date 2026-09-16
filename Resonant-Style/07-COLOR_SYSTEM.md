# Resonant Design System
## 07 — COLOR SYSTEM

## Purpose

Colour gives Resonant its warm, nocturnal, editorial character while keeping hierarchy and accessibility clear.

## Verified product palette

| Token | Hex | Role |
| --- | --- | --- |
| Canvas | `#11100F` | Primary dark background. |
| Ink | `#F4F0E8` | Primary text and key content. |
| Muted | `#BDB7AD` | Secondary text and descriptions. |
| Line | `#38342F` | Dividers, borders, and quiet structure. |
| Accent | `#D8B36A` | Warm gold for emphasis, status, and primary actions. |
| Accent ink | `#201A10` | Text on accent surfaces. |
| Surface | `#191816` | Cards, player bar, and elevated areas. |
| Selected surface | `#24211C` | Active navigation and selected surfaces. |

These values are verified in `apps/web/app/globals.css` and should replace the earlier emerald palette in future Brand Book exports.

## Colour philosophy

Warm gold provides the signal; the near-black canvas provides room for artwork and typography. Colour is sparse by design. A page should not feel colourful until the music or artwork earns that attention.

## Semantic use

| State | Treatment |
| --- | --- |
| Active/current | Accent plus background or underline change. |
| Focus | Accent outline with visible offset. |
| Disconnected | Quiet text and a clear explanatory status, not an alarm. |
| Error | Accent/error text plus a specific recovery action. |
| Planned | Muted label plus “Soon”; never a misleading disabled button. |

## Gradient, glow, and artwork

The current product is flat and restrained. Do not invent a glow system or artwork-derived gradients as current UI. Future visual exploration may use warm atmospheric fields, but content contrast must survive their brightest and darkest areas.

## Accessibility

Test every text/background and control combination against WCAG AA. Never use colour alone for current page, connection state, confidence, or recommendation risk. Include text labels and `aria-current`/semantic states.

## Illustration Required

**Purpose:** make the palette feel like a brand system, not a hex table.

**Description:** full-width canvas, ink and muted type samples, warm accent blocks, selected navigation, player bar, and a contrast-tested recommendation card.

**Suggested composition:** large colour fields on the left; real UI fragments and contrast notes on the right.

**Priority:** P0.

**Assets required:** approved swatches, contrast results, and one authenticated screenshot when available.

## Related pages

[Tokens](26-DESIGN_TOKENS.md) · [Typography](08-TYPOGRAPHY.md) · [Imagery](19-IMAGERY.md)

## TODO

- Add semantic success/warning/error colours and contrast ratios.
- Define light theme policy; current product is dark-first.
