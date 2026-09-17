# Resonant Design System
## PRODUCT ART DIRECTION

## Purpose

This chapter defines how Resonant’s product surfaces should be photographed, rendered, cropped, annotated, and presented so every mockup feels like the same product.

It does not define new product functionality. It defines the visual treatment of verified surfaces, clearly labelled concepts, fixture data, and future screens.

Use this chapter with [Visual language](VISUAL_LANGUAGE.md), [Art direction](ART_DIRECTION.md), [Mockups](21-MOCKUPS.md), [Layout & grid](09-LAYOUT_GRID.md), and [Accessibility](18-ACCESSIBILITY.md).

## Product presentation principle

Show the question before the interface.

```text
user question → musical object → context → decision → next action
```

The render should make the first two steps visible before it asks the viewer to inspect components.

## Shared product render rules

- Use one dominant surface per frame.
- Keep the Player available as a quiet listening thread when the surface includes it.
- Show artwork, title, artist, and listening context before secondary analytics.
- Use the real product shell when the surface is verified.
- Label future or illustrative UI as **Concept** or **Fixture**.
- Never fabricate tracks, artists, counts, recommendations, playback progress, or account data.
- Keep connection state and data freshness visible where they affect the meaning of the surface.
- Use callouts to explain hierarchy, not to label every element.
- Use the approved logo asset without redrawing or modifying it.
- Prefer one large proof over a wall of miniature screens.

## Surface direction

### Home

**Question:** What can I listen to or understand now?

**Art direction:** orient the viewer with one current listening or context statement, then show the supporting areas as a considered sequence. The composition should not feel like a dashboard of equal destinations.

- Lead with the current listening thread or product orientation.
- Keep product areas secondary and grouped by intent.
- Use artwork as a quiet anchor, not as a card background for every section.
- Preserve visible connection and empty states in disconnected examples.

**Avoid:** dense card grids, fake activity counts, and a homepage that looks like a popularity feed.

### Player

**Question:** How does Resonant keep the listening thread present?

**Art direction:** artwork is the visual anchor. Controls sit around it with generous quiet space, and the state is more important than the number of controls shown.

- Crop close enough to read album artwork and track identity.
- Keep transport controls visually subordinate to the current track.
- Show disconnected, idle, playing, paused, loading, and unavailable states only when verified or explicitly labelled.
- For future expanded views, show the concept boundary and do not imply that planned controls are shipped.

**Avoid:** DJ-console density, oversized control clusters, decorative waveforms, or a player that competes with the page it belongs to.

### Search

**Question:** How does a person move from intention to the right music object?

**Art direction:** make the query the first visual event, then organise results into calm bands for songs, artists, albums, and playlists.

- Use a large, readable search field.
- Preserve the query in the composition.
- Show one selected or relevant result context when using a concept fixture.
- Keep result type labels textual, not colour-only.

**Avoid:** an undifferentiated result wall, provider branding as the primary identity, or a search field floating without result structure.

### Library

**Question:** How does saved music become a personal archive?

**Art direction:** use repeated artwork as an archive rhythm, then break the rhythm with one selected object and its context.

- Let artwork lead, but keep titles and artists easy to scan.
- Show meaningful sorting or filtering only when the behaviour is known.
- Use empty and disconnected states as honest compositions, not blank placeholders.
- Allow the archive to feel accumulated without becoming cluttered.

**Avoid:** a generic masonry gallery, popularity-first ordering, or artwork without collection context.

### Playlists

**Question:** What is this collection trying to do?

**Art direction:** establish the playlist identity first, then give the track table enough structure to support listening and editing.

- Use a clear title, artwork anchor, and collection context.
- Keep the table readable and calm.
- Show actions near the collection, not scattered across every row.
- Treat review and builder concepts as explicit proposal states.

**Avoid:** chaotic tables, tiny rows, unexplained badges, and a playlist surface that looks like a spreadsheet.

### Playlist Review

**Question:** What feels out of place, and what can I decide about it?

**Art direction:** tell a before/after story. The visual should show the collection, the finding, the affected tracks, and the Keep / Remove / Unsure decision boundary.

- Use one finding as the lead example.
- Keep analysis separate from mutation.
- Make the reason readable without opening another surface.
- Use restrained comparison: before, finding, decision.

**Avoid:** red-flag walls, algorithmic certainty, irreversible arrows, or a “clean up” button with no review state.

### Discover

**Question:** Why might this be worth hearing next?

**Art direction:** present discovery as curation with distance, not as an endless feed. The three levels are Safe picks, Explore, and Wildcard; each should have a reason.

- Use three lanes or a clear progressive sequence only when the data is available.
- Give the artwork enough room to invite listening.
- Keep explanation and save/play action adjacent.
- Show uncertainty as context, not as a warning colour alone.

**Avoid:** TikTok-style feed motion, popularity rankings without context, or a “surprise” card with no relationship to taste.

### Taste

**Question:** What patterns are present in my listening right now?

**Art direction:** make taste feel like a personal story supported by evidence, not a dashboard score.

- Lead with a plain-language summary.
- Support it with a small number of observations.
- Show confidence, freshness, data sources, and calculation notes as context.
- Use charts only when they answer a visible question.
- Provide a numeric or textual alternative for every visual pattern.

**Avoid:** Excel-like grids, a single taste score, false precision, dense chart walls, or a visual that claims to define the listener.

### Account and connections

**Question:** Who is signed in, what is connected, and what does that enable?

**Art direction:** use separation as the visual idea. Google identity and Spotify connection should read as related but distinct.

- Use two clear cards or stages.
- Make connection status visible in words.
- Show cancellation, unavailable, error, and disconnected states with the same calm hierarchy.
- Never show tokens, secrets, or private data in a render.

**Avoid:** one blended “account” card, provider confusion, or a decorative lock that replaces real privacy explanation.

### Loading, empty, error, and 404

**Question:** What is happening, and what can I do next?

**Art direction:** preserve the affected object and show a clear next action. A quiet field is often stronger than a large illustration.

- Name the operation.
- Use determinate progress when available.
- Keep inputs and context visible across retry.
- Use a static textual alternative to animation.

**Avoid:** generic spinners, fake content, blameful copy, or an error page that erases the listening thread.

## Product photography and render framing

### Camera and crop

- Use a low, calm perspective for physical product and screen studies.
- Keep the primary subject close enough to inspect but not so close that context disappears.
- Use a stable horizon unless a diagonal is communicating direction or transition.
- Frame the Player, artwork, or current signal before surrounding chrome.
- Use whitespace as a deliberate part of the shot.

### Light and surface

- Prefer soft directional light with one controlled highlight.
- Let graphite and charcoal surfaces provide quiet depth.
- Use the approved accent only where it marks a meaningful signal.
- Avoid reflective surfaces that turn the screen into visual noise.
- Keep glass, haze, and bloom subordinate to hierarchy.

### Device frames

- Use a device or browser frame only when it explains scale, context, or responsive behaviour.
- Do not use device frames as decoration around every screenshot.
- Keep the frame’s materials quiet and unbranded.
- Show the same surface at one or two useful sizes, not a catalogue of devices.

## Mockup annotations

Annotations should make the product’s reasoning visible.

### Annotation vocabulary

Prefer:

- **Anchor** — the music object or current signal.
- **Context** — the evidence that explains relevance.
- **Decision** — the action the person can take.
- **Boundary** — a connection, privacy, or product-scope distinction.
- **State** — current, loading, empty, error, disconnected, or planned.
- **Recovery** — the safe next action.

Avoid vague callouts such as “beautiful UI”, “smart AI”, “seamless experience”, or “powerful dashboard”.

### Annotation density

- One hero render: up to three callouts.
- One component: up to five anatomy labels.
- One workflow: three to five numbered steps.
- One comparison: one shared caption and one difference note.

## Responsive art direction

The visual story should survive a change in width.

| Context | Preserve | Simplify |
| --- | --- | --- |
| Desktop | Shell, Player, primary artwork, relationship context. | Secondary detail can move below the main surface. |
| Narrow desktop | Current route, connection state, recovery, and primary action. | Reduce simultaneous panels before shrinking type. |
| Mobile concept | Current listening thread, focused task, and touch-safe action. | Collapse networks into a sequence; do not compress a desktop dashboard. |

Mobile remains future product scope unless verified by the implementation repository. Label all mobile art direction as Concept until then.

## Cross-surface consistency test

Place Home, Player, Taste, Playlist Review, Discover, and Account renders beside one another with their logos removed. They should share:

- the same relationship between music and explanation;
- the same calm density;
- the same approach to artwork and cropping;
- the same treatment of status and uncertainty;
- the same restraint around depth and motion;
- the same respect for connection and privacy boundaries.

If they do not, fix the art direction before changing the component.

## Handoff template

```text
Surface:
Product status: Current / Planned / Concept
User question:
Primary music object:
Context shown:
Primary decision:
State shown:
Artwork source and rights:
Frame / crop:
Annotation count:
Responsive treatment:
Accessibility alternative:
Reviewer:
Approval status:
```

## Related pages

[Visual language](VISUAL_LANGUAGE.md) · [Art direction](ART_DIRECTION.md) · [Mockups](21-MOCKUPS.md) · [Player](11-MUSIC_PLAYER.md) · [Taste](13-ANALYTICS_SYSTEM.md) · [Discovery](14-DISCOVERY_SYSTEM.md) · [Playlist workflows](32-PLAYLIST_WORKFLOWS.md) · [Account & connections](31-ACCOUNT_CONNECTIONS.md) · [Accessibility](18-ACCESSIBILITY.md)

## TODO

- Replace concept descriptions with verified screenshots after the relevant product surfaces are stable.
- Create one approved render template for each current product area.
- Record the final camera, crop, export, and annotation presets in the Canva and Figma libraries.
- Create a visual review checklist for every future marketing and product render.
