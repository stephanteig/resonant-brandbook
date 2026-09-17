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

## Version 2 expansion: presentation and visual-language tokens

The following categories are a proposed expansion for the next token review. They do not replace the approved Version 1 seeds above, and they must not be implemented as production values until they are mapped to the product repository, Figma, and accessibility tests.

The purpose of this expansion is to document meaning before numbers. A token should explain what a value is for, not merely make a surface look polished.

### Radius

Radius should describe the relationship between a surface and its contents. Do not round every object by default.

| Candidate token | Candidate value | Meaning | Typical use |
| --- | ---: | --- | --- |
| `radius-tight` | 8 px | Precise, compact, close to content. | Inputs, small controls, compact states. |
| `radius-control` | 12 px | A comfortable interactive boundary. | Buttons, selects, small cards. |
| `radius-card` | 16 px | A calm content container. | Player, context, review, and taste cards. |
| `radius-panel` | 24 px | A surface with room for hierarchy. | Large panels and editorial UI crops. |
| `radius-feature` | 36 px | A presentation object with visible atmosphere. | Hero product render or large artwork frame. |
| `radius-field` | 64 px | A broad visual field, not a default component radius. | Atmospheric crop or future editorial composition. |

**Rule:** radius is subordinate to hierarchy. A larger radius must not be used to make an unimportant object feel more important.

**Status:** Proposed. Validate against the current codebase and approved typography/spacing before adoption.

### Elevation and shadows

Resonant should use depth to separate layers, not to create a floating-card aesthetic.

| Candidate role | Shadow behaviour | Meaning |
| --- | --- | --- |
| `elevation-flat` | None or a 1 px line. | Same plane; reference, table, or quiet field. |
| `elevation-raised` | Short, soft, low-opacity shadow. | A control or panel needs separation. |
| `elevation-overlay` | Broader, softer separation with a clear boundary. | Dialog, menu, or temporary layer. |
| `elevation-hero` | Atmospheric separation only; never a heavy drop shadow. | Large artwork or product presentation. |

Do not use shadows to rescue insufficient contrast. Do not stack more than two elevation cues on one surface. Confirm the final values in light and dark contexts and in print.

### Blur

Blur is a relationship tool: it can separate foreground from background or indicate a temporary layer. It is not a brand effect.

| Candidate role | Candidate range | Use |
| --- | ---: | --- |
| `blur-none` | 0 px | Tables, controls, type specimens, accessibility surfaces. |
| `blur-soft` | 8 px | A quiet background separation. |
| `blur-medium` | 16 px | A distinct image or overlay relationship. |
| `blur-atmosphere` | 24 px | Editorial field or controlled hero atmosphere. |
| `blur-max` | 32 px or more | Rare; requires a clear reason and contrast test. |

Blur must never remove the information needed to identify a track, state, control, or recovery action. Reduced-transparency or reduced-motion settings should have a legible non-blurred fallback.

### Transparency

Transparency should explain layering, not make the entire product look like glass.

| Candidate role | Candidate opacity | Meaning |
| --- | ---: | --- |
| `opacity-solid` | 100% | Primary reading surface and critical control. |
| `opacity-support` | 96% | A surface that remains fully readable but sits behind another layer. |
| `opacity-atmosphere` | 88% | Artwork or field support where contrast has been tested. |
| `opacity-trace` | 72% or lower | Decorative trace or inactive background element only. |

**Rule:** critical text, focus rings, Player controls, connection status, and error recovery do not depend on transparency.

### Motion curves

Motion curves should describe intent:

| Candidate role | Curve character | Why |
| --- | --- | --- |
| `motion-immediate` | Near-linear, minimal travel. | A play, pause, focus, or status response should not feel delayed. |
| `motion-enter` | Soft ease-out. | A new context arrives and settles into place. |
| `motion-exit` | Short ease-in. | A temporary surface yields quickly to the next state. |
| `motion-context` | Smooth, continuous curve. | A relationship or panel preserves orientation while changing. |
| `motion-reduced` | No decorative travel. | The state changes directly and remains understandable. |

Do not tune motion to the beat, use bounce as personality, or make a transition longer because it looks impressive. See [Motion](24-MOTION.md) for the current philosophy.

### Timing

These are candidate review points, not approved production tokens:

| Candidate timing | Candidate use | Review question |
| ---: | --- | --- |
| 120 ms | Immediate state acknowledgement. | Does the response feel instant? |
| 180 ms | Small control or selection change. | Does the person retain focus? |
| 240 ms | Panel, card, or context transition. | Is the relationship understandable? |
| 320 ms | Larger editorial or spatial movement. | Does the extra time improve orientation? |
| 480 ms+ | Rare hero or atmosphere transition. | Is the movement necessary, or is it performance? |

Every timing needs a stopping condition, a reduced-motion fallback, and a focus policy. Do not add a timing merely because it exists in a token table.

### Visual-language roles

These semantic roles connect the token system to [Visual language](VISUAL_LANGUAGE.md) without turning the art direction into CSS decoration.

| Role | Meaning | Test |
| --- | --- | --- |
| `visual.signal` | The current thing that deserves attention. | Can the viewer name what is current? |
| `visual.relationship` | A known connection between objects or states. | Can the viewer explain the line or overlap? |
| `visual.memory` | A previous state, return, archive, or trace. | Is the past specific rather than nostalgic? |
| `visual.distance` | Familiarity, uncertainty, or discovery range. | Is the distance explained rather than implied by colour alone? |
| `visual.quiet-field` | Space that protects hierarchy and listening. | Would adding detail make the message weaker? |

### Governance

Before promoting a proposed token to an approved token:

1. Document its semantic job.
2. Test it with the current product shell and Player.
3. Test it in empty, loading, error, disconnected, and focused states.
4. Test contrast, 200% zoom, reduced motion, and reduced transparency.
5. Map it to Figma and code using the same semantic name.
6. Record deprecation and migration behaviour.

## Related pages

[Visual language](VISUAL_LANGUAGE.md) · [Art direction](ART_DIRECTION.md) · [Product art direction](PRODUCT_ART_DIRECTION.md) · [Color system](07-COLOR_SYSTEM.md) · [Typography](08-TYPOGRAPHY.md) · [Motion](24-MOTION.md) · [Accessibility](18-ACCESSIBILITY.md)
