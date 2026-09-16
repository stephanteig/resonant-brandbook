# Resonant Design System
## 09 — LAYOUT & GRID SYSTEM

## Purpose

The layout system creates a stable home for music, context, and decisions across desktop and narrow mobile screens.

## Spatial tokens

The verified application uses a rem-based scale: `0.5rem`, `1rem`, `1.5rem`, `2rem`, and `3rem`, with clamp-based responsive padding. Use an 8 px mental grid for composition, but preserve the product’s rem tokens in implementation.

## Desktop anatomy

```text
Persistent sidebar                 Main content
RESONANT + environment             Page header
Home / Search                      Primary surface
Your music                         Contextual detail
Discover                           Global player
Taste
Account
```

The desktop sidebar is 15 rem wide. The main content is deliberately constrained rather than stretched across an ultra-wide display. The current player bar anchors the bottom of the shell.

## Mobile anatomy

```text
Mobile header: wordmark + environment
Page header and primary content
Global player bar
Sticky four-item primary navigation
```

At 720 px and below, the sidebar becomes a mobile header and bottom navigation. The player hides device text while retaining the track and controls. Cards stack and content padding increases below the sticky navigation.

## Page templates

- **Landing:** header, hero, signal statement, principles, product areas, footer.
- **Workspace:** eyebrow, title, description, empty or populated surface, supporting cards.
- **Account:** status, authentication, provider connection, sign-out/disconnect actions.
- **Taste:** metrics, profile narrative, methodology, sources.
- **Player:** mini-player everywhere; full Now Playing view planned.

## Alignment rules

Use left alignment for text and lists. Let the accent rule or index create rhythm. Center only compact authentication states or short empty-state actions. Do not center dense data.

## Accessibility

Support 320 px mobile width without horizontal overflow, 200% zoom, keyboard focus, logical heading order, sticky navigation that does not obscure content, and touch targets that remain comfortable.

## Illustration Required

**Purpose:** show the system across breakpoints.

**Description:** paired desktop and iPhone-width frames with sidebar-to-bottom-nav transformation.

**Suggested composition:** one large desktop shell, one narrow crop, annotated arrows for the responsive changes.

**Priority:** P0. **Assets:** verified shell screenshot and mobile smoke capture.

## Related pages

[Desktop](28-DESKTOP.md) · [Mobile](29-MOBILE.md) · [Components](10-COMPONENT_SYSTEM.md)
