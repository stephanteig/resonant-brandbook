# 18 — ACCESSIBILITY

## Purpose

This chapter turns inclusive access into a product and release requirement.

## Goal

Make listening, discovery, playlist work, and taste interpretation usable across vision, hearing, mobility, cognition, and technology differences.

## Baseline

Target WCAG 2.2 AA for applicable UI. Use 16 px minimum body text, visible focus, keyboard operation, 44×44 px pointer targets where practical, semantic names, reduced motion, and non-colour state cues.

## Web product requirements

- Player controls have visible labels and do not trap focus.
- Current page, connection, loading, empty, and error state are announced in text.
- Taste metrics and charts have numeric or textual alternatives.
- Dialogs and OAuth states return focus correctly and explain cancellation.
- Zoom to 200% does not hide essential transport or recovery actions.
- Audio-dependent instructions always have a visual alternative.

## Testing checklist

Keyboard-only pass; screen-reader names; focus visibility; contrast; 200% zoom; reduced-motion mode; long labels; error recovery; high-DPI rendering; and Windows accessibility settings.

## TODO

- Record assistive-technology test matrix and known issues.
- Confirm whether captions/transcripts are needed for future tutorial media.

## Related pages

[Components](10-COMPONENT_SYSTEM.md) · [Motion](24-MOTION.md) · [Writing](04-WRITING_GUIDE.md)
## Do / don’t

Do pair charts and taste signals with plain-language summaries. Do keep Spotify connection consent adjacent to the action. Don’t rely on a red border alone, trap focus in a background surface, or make artwork the only way to identify a track.

## Implementation notes

Accessibility is a release gate, not a polish pass. Capture test evidence with the product release and link limitations to the affected component or screen.
