# Resonant Design System
## 06 — LOGO SYSTEM

## Purpose

Protect the approved Resonant Version 1 identity across the web product, Brand Book, presentations, marketing material, and physical applications.

## Official working identity

The supplied Resonant logo sheet is the authoritative Version 1 visual reference. It defines the geometric symbol, the cut-out relationship between forms, the rounded optical language, and the approved colour treatments. Use the supplied artwork exactly as delivered; do not redraw, simplify, reinterpret, or substitute the mark.

The editable source is stored in [`Assets/Logo/Source/`](../Assets/Logo/Source/), with the approved vector variants in [`Assets/Logo/Color-Variations/`](../Assets/Logo/Color-Variations/). The PDF builder consumes the supplied PNG variants from [`Assets/Logo/Color-Variations/png/`](../Assets/Logo/Color-Variations/png/). Keep these paths replaceable so future optical refinements can be introduced without changing document structure.

## Approved forms

| Form | Background | Use |
| --- | --- | --- |
| Primary gradient | Graphite / near-black | Hero moments, cover pages, app icon, high-attention brand surfaces. |
| Single-colour Emerald | Dark or neutral surface | Product header, favicon, compact identity, UI-adjacent applications. |
| White | Black or deep graphite | Dark-mode product surfaces, monochrome print, photography with tested contrast. |
| Black | White or light neutral | Light-mode surfaces, documents, invoices, one-colour print. |
| Icon-only symbol | Any approved contrast-safe surface | App icon, desktop shortcut, favicon, avatar, sticker, merchandise. |

The approved asset package also supports dark, neutral, light, and green-tinted backgrounds; icon sizes at 180, 64, 32, and 16 px; close-up detail; construction grid; clear space; and embroidery.

## Construction

The symbol is treated as one geometric unit. Preserve the relative scale of the vertical stem, angled forms, interior cut-out, and rounded terminal ends. The diagonal cut-out is part of the identity, not a decorative gap.

For construction diagrams, use the supplied vector source package as the visual authority. Do not infer a new mathematical grid from a raster preview. Any vector construction must be checked optically against the approved artwork before entering production.

## Clear space

Use clear space on every side of the symbol. The minimum unit is `x`, defined as the visible width of the narrow interior cut-out at the mark’s current size. Keep at least `1x` clear space between the mark and any typography, edge, control, artwork, or competing identity. Increase to `2x` for hero and editorial use.

```text
┌──────────────────────────────┐
│                              │
│        ┌──────────┐          │
│        │  SYMBOL  │          │  1x minimum on all sides
│        └──────────┘          │
│                              │
└──────────────────────────────┘
```

Clear space is measured from the visual edge of the symbol, not from an invisible file canvas. Do not reclaim space by cropping into the mark.

## Minimum sizes

| Context | Recommended | Minimum working test |
| --- | ---: | ---: |
| Hero / cover | 180 px or larger | 120 px |
| Product header | 64 px | 48 px |
| Favicon / compact control | 32 px | 16 px only after raster testing |
| Embroidery | 25 mm wide or larger | Confirm stitch test before production |
| One-colour print | 18 mm wide or larger | Confirm legibility on final stock |

At 16 px, use the icon-only symbol and preserve the strongest silhouette. Never squeeze a full lockup into a size where its interior cut-out or terminal shapes collapse.

## Background and contrast

Place gradient and Emerald treatments on quiet dark surfaces. Place white on black or deep graphite. Place black on white or a light neutral. Avoid textured or high-frequency backgrounds unless a solid contrast field protects the mark.

The logo is not a substitute for text contrast. Test adjacent copy independently, and do not use glow, shadow, outline, or blur to rescue an invalid placement.

## Do / don’t

| Do | Don’t |
| --- | --- |
| Preserve proportions, cut-out geometry, colour stops, and rounded terminals. | Stretch, compress, rotate, skew, or mirror the mark. |
| Use the approved monochrome version when reproduction is limited. | Recolour the mark with arbitrary hues or gradients. |
| Give the icon room to breathe. | Crop into the silhouette or place type inside clear space. |
| Use a tested export at each target size. | Rely on a tiny preview to approve a 16 px or embroidery application. |
| Keep the source asset replaceable and versioned. | Reconstruct the mark from a font, screenshot, or unapproved redraw. |

## Application examples

| Context | Preferred treatment |
| --- | --- |
| Website hero | Primary gradient symbol with `2x` clear space and restrained glow in the environment, not baked into the mark. |
| Product header | Single-colour Emerald or white symbol, 48–64 px, linked to Home and labelled “Resonant”. |
| App icon / desktop icon | Icon-only symbol centred in a rounded square with tested optical padding. |
| Favicon | 16–32 px icon-only symbol on a contrast-safe solid field. |
| Social avatar | Icon-only symbol, generous padding, no additional text. |
| Sticker | Black or white one-colour symbol on matte stock; preserve the cut-out. |
| Apparel / embroidery | White or Emerald one-colour symbol; use a physical stitch sample before ordering. |
| Presentation / PDF | Primary gradient for opening pages, monochrome for dense reference pages. |

## Accessibility

When the logo is a link or Home control, provide the accessible name “Resonant”. When it is decorative beside an adjacent text heading, hide the duplicate from assistive technology. Do not communicate connection, selection, or system status through logo colour alone.

## Implementation notes

Keep the editable source in the asset repository and keep all placements linked to a replaceable asset slot. Use the approved SVG variants for product and print delivery, and the matching high-resolution PNG derivatives for raster contexts. Preserve the same geometry and approved treatments. Name future size exports by form and size, for example `resonant-symbol-emerald-64.png` and `resonant-symbol-white.svg`.

## Illustration Required

**Purpose:** make the identity operational at a glance.

**Description:** a visual reference sheet containing the approved vector artwork, colour treatments, icon sizes, construction grid, clear-space frame, misuse strip, and real-world applications.

**Suggested composition:** open with the exact logo sheet full-bleed; follow with a page of large variants; then a measured clear-space/construction spread; finish with favicon, app icon, sticker, apparel, embroidery, print, and website applications.

**Priority:** P0.

**Assets required:** `Assets/Logo/Source/`, `Assets/Logo/Color-Variations/`, `Assets/Logo/Color-Variations/png/`, tested size exports, print proof, embroidery sample, and application mockup board.

## Related pages

[Brand identity](05-BRAND_IDENTITY.md) · [Colour system](07-COLOR_SYSTEM.md) · [Imagery](19-IMAGERY.md) · [Mockups](21-MOCKUPS.md) · [Design tokens](26-DESIGN_TOKENS.md)

## TODO

- Confirm trademark, legal owner, and co-branding rules.
- Create measured vector exports that match the supplied reference exactly.
- Run physical minimum-size, embroidery, sticker, and one-colour print tests.
- Add the final export manifest without changing the approved geometry.
