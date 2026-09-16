# 11 — MUSIC PLAYER

## Purpose

The Player is Resonant’s persistent listening surface. It keeps music available while the person moves between Home, Search, Library, Playlists, Discover, and Taste.

## Product role

The Player is not a separate media dashboard. It is a quiet layer that preserves listening context and gives the person a way back to the current track.

## Current foundation

The verified implementation includes a global bottom player bar with album-art placeholder, “Now playing” label, track status, Previous, Play, Next, and device status. Before Spotify is connected, controls are disabled and the surface says “Connect Spotify to start listening.”

## Planned expanded view

The Masterplan calls for a larger Now Playing view, Spotify playback, seek, volume, device selection, queue, shuffle, repeat, artwork, and track/artist/album navigation. These are product direction, not all current implementation.

## Information hierarchy

1. Artwork and current track.
2. Playback status and primary control.
3. Secondary transport and device context.
4. Path to deeper Now Playing context.

## States

Disconnected, empty, connected/idle, playing, paused, loading, unavailable device, provider error, and mobile compact mode. Never fabricate a track, device, duration, or playback progress.

## Interaction and accessibility

Controls have accessible names and remain keyboard reachable. Focus is visible. Disabled controls explain the missing Spotify connection. The compact mobile player keeps the current listening context while the bottom navigation remains usable.

## Illustration Required

**Purpose:** make “persistent listening context” tangible.

**Description:** a desktop shell with bottom player, an expanded Now Playing concept, and a mobile mini-player.

**Suggested composition:** show one track moving from mini-player to full context; label current foundation vs planned view.

**Priority:** P0. **Assets:** verified current player component and approved future-state annotation.

## Related pages

[Layout](09-LAYOUT_GRID.md) · [Motion](24-MOTION.md) · [Accessibility](18-ACCESSIBILITY.md) · [Mockups](21-MOCKUPS.md)

## TODO

- Capture authenticated Spotify player states after playback is implemented.
- Confirm exact mobile player gestures, queue, seek, volume, and device controls.
