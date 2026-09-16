# 32 — PLAYLIST WORKFLOWS

## Purpose

Playlists are where Resonant’s ordinary listening utility and explainable intelligence meet.

## Playlist workspace

The target surface includes playlist title, duration, track count, Play, Analyze, overflow actions, and a table with Track, Artist, Album, and Duration. People can search within a playlist, sort, reorder, add/remove, multi-select, move/copy, inspect, and open related artists or albums.

## Review flow

```text
Analyze playlist → findings → inspect affected tracks → Keep / Remove / Unsure
```

The review engine identifies duplicates, artist/album concentration, total length, genre and era patterns, and tracks that stand out. Findings are deterministic, explainable, side-effect-free, and do not mutate Spotify.

## Builder flow

```text
Prompt + Taste Profile + library + existing playlists + listening patterns
     → proposal → review → keep/remove/replace/reorder → Create in Spotify
```

Creation happens only after review. The interface must distinguish a proposal from a changed playlist.

## Accessibility and edge cases

Use table headers, row actions, keyboard selection, clear multi-select state, and non-colour finding labels. Handle empty playlists, duplicates, long titles, provider errors, stale data, and a cancelled proposal.

## Illustration Required

**Purpose:** show the difference between analysis and mutation.

**Description:** playlist table, review finding card, and Builder proposal with explicit review controls.

**Suggested composition:** three sequential spreads with a visible “nothing changes until you decide” rule.

**Priority:** P0. **Assets:** cleared playlist fixture and final review component.

## Related pages

[Library](15-LIBRARY_SYSTEM.md) · [AI](12-AI_SYSTEM.md) · [Writing](04-WRITING_GUIDE.md)

## TODO

- Define playlist table density, drag/reorder accessibility, mutation confirmation, and rollback.
