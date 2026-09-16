# 27 — LOADING, EMPTY, AND ERROR STATES

## Purpose

Listening and interpretation must remain understandable when a provider connects, a taste calculation runs, or a route fails.

## State model

```text
idle → working → success
             ↘ cancelled
             ↘ recoverable error → retry
```

## Rules

Name the operation, show determinate progress when available, preserve inputs, explain the next action, and never imply that a cancelled job completed. Errors must identify the object and constraint.

## Verified examples

The public landing page is static and should not depend on provider data. Account exposes signed-out, connected, unavailable, error, and disconnected states. Search, Library, Discover, Taste, and Player use honest empty/disconnected surfaces. Runtime errors offer retry; unknown routes use an accessible 404.

## Empty states

Empty states should teach the next useful action without inventing tracks, artists, counts, recommendations, or analysis.

## Accessibility

Use an `aria-live` status without repeated progress spam, keep focus near the failed action, and provide a static text alternative to spinners.

## Related pages

[Writing](04-WRITING_GUIDE.md) · [Interaction](25-INTERACTION_PATTERNS.md) · [Accessibility](18-ACCESSIBILITY.md)
## Copy examples

- Connect: “Connect Spotify to start searching.”
- Success: “Spotify is connected.”
- Retry: “Google sign-in could not be completed. Please try again.”
- Error: “That view could not load. Try again, or return to the Resonant home.”
- Empty: “Your taste will take shape here.”

## Implementation notes

Preserve operation inputs across retry where safe. Put errors near the affected surface and keep durable status for long-running work so a toast is not the only evidence.

## TODO

- Map every verified provider and file-dialog state to a final component and copy string.
