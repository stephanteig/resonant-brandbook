# Resonant Brand Book — Codex Handoff

This repository is the source package for implementing the Resonant rebrand across the product, website, marketing surfaces, presentations, and future developer documentation.

## Read first

1. [`README.md`](README.md)
2. [`PROJECT_STATUS.md`](PROJECT_STATUS.md)
3. [`Resonant-Style/00-START-HERE.md`](Resonant-Style/00-START-HERE.md)
4. [`Resonant-Style/02-PROJECT_CONTEXT.md`](Resonant-Style/02-PROJECT_CONTEXT.md)
5. [`Resonant-Style/03-DESIGN_PHILOSOPHY.md`](Resonant-Style/03-DESIGN_PHILOSOPHY.md)
6. [`Resonant-Style/06-LOGO_SYSTEM.md`](Resonant-Style/06-LOGO_SYSTEM.md)
7. [`Resonant-Style/07-COLOR_SYSTEM.md`](Resonant-Style/07-COLOR_SYSTEM.md)
8. [`Resonant-Style/08-TYPOGRAPHY.md`](Resonant-Style/08-TYPOGRAPHY.md)
9. [`Resonant-Style/26-DESIGN_TOKENS.md`](Resonant-Style/26-DESIGN_TOKENS.md)
10. [`Resonant-Style/VISUAL_LANGUAGE.md`](Resonant-Style/VISUAL_LANGUAGE.md)
11. [`Resonant-Style/ART_DIRECTION.md`](Resonant-Style/ART_DIRECTION.md)
12. [`Resonant-Style/PRODUCT_ART_DIRECTION.md`](Resonant-Style/PRODUCT_ART_DIRECTION.md)
13. [`Design-Reference/index.html`](Design-Reference/index.html)

Read the full `Resonant-Style/` directory before making a substantial implementation decision.

## Design Reference authority

[`Design-Reference/`](Design-Reference/index.html) is the implementation reference for:

- Components and component states
- Patterns and user flows
- Layout and responsive composition
- Spacing, grid, radius, elevation, and surface treatment
- Interaction and motion principles
- Loading, empty, error, disconnected, and recovery examples
- Product screenshot and marketing-mockup composition

Future development must reference both `Resonant-Style/` and `Design-Reference/`. `Resonant-Style/` remains the authority for brand intent, product language, visual language, art direction, and design tokens. `Design-Reference/` shows how those rules are assembled into reusable visual surfaces. The product repository remains authoritative for implemented behaviour and technical constraints.

## Authority order

1. The implementation repository: [stephanteig/resonant](https://github.com/stephanteig/resonant)
2. Verified product behaviour and tests
3. This repository’s design-system documentation
4. Explicitly labelled `TODO` and future direction

If a design document conflicts with implemented product behaviour, the product repository wins. Do not convert planned behaviour into a shipped feature.

## Rebrand rules

- Preserve the approved Resonant logo geometry exactly.
- Use the supplied logo assets in `Assets/Logo/Source/`, `Assets/Logo/Color-Variations/`, and `Assets/Logo/Color-Variations/png/`.
- Preserve the approved colour palette and typography roles.
- Keep music ahead of artwork, artwork ahead of interface, and analytics/AI in an explanatory role.
- Maintain explicit Spotify connection, account, loading, empty, error, accessibility, and recovery states.
- Do not invent mobile, native, social, streaming, or AI functionality that the product repository does not implement.
- Use the Visual Language, Art Direction, and Product Art Direction chapters to keep product proof, marketing, and mockups recognisable without relying on the logo.
- Treat `Design-Reference/` as the shared visual implementation reference: do not create new one-off UI pages before checking the documented components, states, patterns, and token mappings.

## Asset map

| Asset | Use |
| --- | --- |
| `Assets/Logo/Source/` | Editable Affinity and SVG source files. |
| `Assets/Logo/Color-Variations/` | Approved vector logo variants. |
| `Assets/Logo/Color-Variations/png/` | Supplied raster logo variants used for product and presentation work. |
| `Assets/Editorial/` | Approved editorial image fixtures. |
| `Assets/Mockups/` | Concept application boards and mockup references. |
| `Resonant-Brandbook-v0.5.pdf` | Current visual publication output. |

## PDF build

From the repository root:

```bash
python3 build_brandbook_pdf.py
```

The builder writes the current PDF to the repository root. Keep historical PDFs intact when creating a new version, and update the output filename and status record for each release.

## Implementation handoff checklist

- [ ] Read the full product repository before changing product UI.
- [ ] Map design tokens before styling individual components.
- [ ] Replace one-off colours and spacing with semantic tokens.
- [ ] Implement the shell and persistent Player before feature-specific surfaces.
- [ ] Verify all current, loading, empty, disconnected, error, and recovery states.
- [ ] Test keyboard navigation, focus visibility, contrast, 200% zoom, reduced motion, and narrow widths.
- [ ] Record unverified decisions as `TODO` instead of guessing.
- [ ] Keep implementation changes in the product repository; keep this repository as the brand source.
