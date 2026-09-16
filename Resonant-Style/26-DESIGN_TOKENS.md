# 26 — DESIGN TOKENS

## Purpose

Tokens keep brand decisions portable across Figma, CSS, and future native surfaces.

## Verified seed tokens

| Token | Value |
| --- | --- |
| `color.brand.emerald` | `#30DDA1` |
| `color.brand.mint` | `#67F3C2` |
| `color.surface.graphite` | `#0B0F0D` |
| `color.surface.charcoal` | `#171C1A` |
| `color.content.primary` | `#F7F8F8` |
| `space.base` | `8px` |
| `font.display` | Inter Tight |
| `font.interface` | Inter |
| `font.data` | Geist Mono |

## Naming

Prefer semantic names (`color.action.primary`) over literal names. A token should describe purpose, not the current colour. Record source, contrast, state, and platform mapping.

## TODO

- Define neutral, semantic, spacing, radius, elevation, blur, opacity, typography, and motion scales.
- Publish CSS, Figma, and native mappings after the values are approved.
## Token lifecycle

1. Propose a semantic name and rationale.
2. Test contrast and state combinations.
3. Map to Figma and code.
4. Use in one component before broad adoption.
5. Deprecate by reference, never by silently changing meaning.

Do not create tokens for one-off screenshot decoration or unverified platforms.
