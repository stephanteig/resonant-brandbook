# Resonant Design System
## 08 — TYPOGRAPHY

## Purpose

Typography gives production information a calm, editorial hierarchy while keeping controls fast to scan.

## Typeface roles

| Role | Typeface | Use |
| --- | --- | --- |
| Display | Inter Tight | Brand headlines, covers, marketing statements. |
| Interface | Inter | Navigation, labels, dialogs, settings, body copy. |
| Data | Geist Mono | Measurements, timestamps, IDs, and aligned values. |

These roles originate in the existing brandbook; confirm that the licenses and final font files are included before distribution.

## Hierarchy

Use one display style, four heading levels, body, caption, overline, and button styles. A stable hierarchy is more important than a large scale. Use semibold for active labels sparingly; do not use weight as the only state cue.

## Responsive and accessibility rules

Body copy starts at 16 px. Keep interface labels readable at 100–200% zoom, avoid long all-caps strings, use comfortable line height, and keep prose measure near 45–85 characters. Numbers that must align use tabular figures.

## Do / don’t

Do use space and size to establish hierarchy. Don’t add decorative typefaces, justify prose, compress explanatory text, or mix several families within one screen.

## TODO

- Confirm exact font files and licensing.
- Define pixel/rem styles, weight mapping, line heights, and desktop breakpoints.
- Add Figma text-style names and a type specimen illustration.
## Content examples

- Product headline: “Listen with context.”
- Page label: “TASTE” with the supporting hint “Your listening, explained”.
- Measurement: “72%” in Geist Mono when alignment matters.
- Progress: “Updating your taste profile…” rather than an unexplained spinner.

## Edge cases

Long project names must wrap or truncate with a discoverable full value. Localized lyrics must support Unicode and native scripts. Numeric values must not jump width as they update.

## Implementation notes

Define text styles centrally and keep the same semantic name across Figma and code. Use tabular numerals for meters and tables.
