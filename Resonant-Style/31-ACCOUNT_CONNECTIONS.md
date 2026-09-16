# 31 — ACCOUNT & CONNECTIONS

## Purpose

Account is where identity and music-provider access meet without being confused with each other.

## Model

```text
Google identity → Resonant account → separate Spotify connection
```

Google authenticates the Resonant account. Spotify is a connected service that supplies music data. Disconnecting Spotify must not delete the Resonant account.

## States

Signed out, sign-in unavailable, signed in without Spotify, Spotify connected, connection unavailable, OAuth cancelled/error, and disconnected confirmation. The UI must not reveal tokens, provider secrets, or private implementation errors.

## Interaction rules

Use explicit “Continue with Google”, “Connect Spotify”, “Disconnect Spotify”, “Sign out”, and “Back to home” actions. Disconnect is authenticated POST behaviour, never a destructive GET. Explain what the connection enables before asking for permission.

## Responsive and accessibility

The account surface must remain legible at 320 px, use semantic status text, preserve focus after an action, and expose alerts with a role appropriate to their urgency.

## Illustration Required

**Purpose:** show trust through separation.

**Description:** identity card and Spotify connection card with signed-out, connected, and error states.

**Suggested composition:** two cards connected by a quiet relationship line; tokens and secrets never appear.

**Priority:** P0. **Assets:** approved account fixture screenshots and privacy copy.

## Related pages

[Privacy and security](23-PRODUCT_REQUIREMENTS.md) · [Writing](04-WRITING_GUIDE.md) · [Loading/error states](27-LOADING_ERROR_STATES.md)

## TODO

- Confirm account deletion, data export, token revocation, and retention flows.
