# 24 — MOTION

## Purpose

Motion makes transport, progress, selection, and change understandable. It should feel like musical timing, not visual noise.

## Rules

Use immediate feedback for play/record state, short easing for selection and panel changes, and determinate progress for installs, generation, conversion, and rendering. Never animate essential information only once or hide a state behind a transition.

## Timing guidance

Use the shortest duration that preserves orientation. Transport feedback should feel immediate; modal and panel transitions may be slightly slower. Exact durations require product testing and are TODO, not tokens.

## Reduced motion

When reduced motion is requested, remove decorative glows, parallax, and non-essential movement. Keep a static playhead, visible progress values, and state changes.

## Do / don’t

Do let the playhead communicate time. Don’t make the whole interface pulse with the beat or use animation to imply audio quality.

## Related pages

[Interaction patterns](25-INTERACTION_PATTERNS.md) · [Visual language](VISUAL_LANGUAGE.md) · [Accessibility](18-ACCESSIBILITY.md) · [Tokens](26-DESIGN_TOKENS.md)

## TODO

- Define production motion tokens and record reduced-motion behaviour from the app.
## Motion inventory

Transport motion: playhead and active state. Process motion: installation, generation, conversion, and rendering progress. Spatial motion: dialog and panel entry. Feedback motion: success/error acknowledgement. Each has a purpose, stopping condition, and reduced-motion fallback.

## Edge cases

Do not let progress run after cancellation, restart completed animation on every render, or move focus while a dialog changes. Keep audio timing independent from decorative UI timing.
