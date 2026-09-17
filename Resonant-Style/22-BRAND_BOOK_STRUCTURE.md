# 22 — BRAND BOOK STRUCTURE

## Purpose

This chapter turns the design-system source into an editorial, visual Brand Book suitable for Canva, PDF, internal design review, and marketing handoff.

## Recommended 100–120 page structure

| Part | Pages | Visual emphasis |
| --- | ---: | --- |
| Opening | 4–6 | Cover, manifesto, product signal, full-bleed mood. |
| Brand | 10–14 | Mission, values, personality, voice, messaging. |
| Identity | 12–16 | Logo grid, clear space, marks, colour, type, imagery. |
| Product language | 12–16 | Philosophy, hierarchy, layout, components, states. |
| Product surfaces | 30–40 | Home, Player, Search, Library, Playlists, Taste, Discover, Account. |
| Intelligence and trust | 8–12 | Assistant, methodology, freshness, privacy, connection states. |
| Responsive system | 6–8 | Desktop, tablet, iPhone-width compositions, navigation changes. |
| Visual language | 8–12 | Signal, wave, memory, pattern, artwork, photography, depth, motion, and recognition. |
| Art direction | 10–16 | Hero compositions, product renders, photography, album-art treatment, UI crops, scale, rhythm, and concrete briefs. |
| Product art direction | 8–12 | Consistent presentation of Home, Player, Search, Library, Taste, Playlist Review, Discover, Account, and product states. |
| Handoff | 8–10 | Tokens, accessibility, motion, website, downloads, TODOs. |

## Spread rhythm

Every chapter begins with a full-page hero. Alternate visual spreads, principle spreads, annotated UI spreads, and concise reference spreads. Use asymmetry, generous margins, large type, and editorial pacing. Do not reproduce the density of the source Markdown inside Canva.

## Version 0.5 editorial page language

The Brand Book should create pauses between specification chapters. Use these page types deliberately:

| Page type | Job | Typical content |
| --- | --- | --- |
| Hero image | Establish atmosphere before explanation. | Nocturnal listening photograph with one sentence. |
| Statement page | Give a principle room to resonate. | “Music comes first.” or “Listen with context.” |
| Type specimen | Make hierarchy visible rather than describing it. | Display, interface, data, and numeric examples. |
| Material spread | Show colour, spacing, radius, blur, and elevation as a visual system. | Swatches, spacing rhythm, surface stack. |
| Product proof | Show how philosophy becomes a product surface. | Home, Player, Taste, Playlist Review, Discover. |
| Trust diagram | Explain data and reasoning without a paragraph wall. | Spotify → history → Taste Engine → review → discovery. |
| Reference page | Preserve operational detail. | Tables, rules, accessibility, implementation, TODO. |

The target rhythm is visual interruption every two to four reference pages. A reference page can be dense when it is useful; it should not be the only page type in a chapter.

The Visual Language chapter is the bridge between rules and art direction. `ART_DIRECTION.md` turns those principles into a reviewed library of concrete examples, while `PRODUCT_ART_DIRECTION.md` keeps product surfaces consistent across screenshots, mockups, presentations, and marketing. Neither chapter replaces product evidence.

After these chapters are reviewed, freeze the Version 1 Brand Book and move implementation into a Resonant UI Kit. New product pages should use the shared component library rather than introducing one-off visual solutions.

## Visual ratio

Aim for 65–75% visual material in the presentation PDF: product screens, logo sheets, colour fields, grids, type specimens, component states, diagrams, artwork, photography, and responsive comparisons. Text explains the decision; it should not be the primary image. The Markdown source may remain more detailed than the presentation.

## Production checklist

- Pin the product commit/version represented.
- Use only verified screens and clearly labelled concepts.
- Include logo assets, colour swatches, type specimens, UI crops, and mockup compositions.
- Test contrast, reading order, alt text, and PDF export.
- Keep unverified roadmap surfaces visibly marked.
- Use editorial pages to create pacing; never fill a hero spread with a table merely because the source contains one.

## Illustration Required

**Purpose:** define the visual pacing of the finished book.

**Description:** contact sheet showing hero, principle, UI, system, and appendix spread types.

**Suggested composition:** five miniature page pairs with visual/text ratios.

**Priority:** P0. **Assets:** final Canva master template and approved image set.

## Related pages

[Mockups](21-MOCKUPS.md) · [Imagery](19-IMAGERY.md) · [Visual language](VISUAL_LANGUAGE.md) · [Art direction](ART_DIRECTION.md) · [Product art direction](PRODUCT_ART_DIRECTION.md) · [Tokens](26-DESIGN_TOKENS.md)

## TODO

- Confirm final page count, page size, Canva owner, and review milestones.
