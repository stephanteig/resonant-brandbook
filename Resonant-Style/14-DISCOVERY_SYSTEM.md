# 14 — DISCOVERY SYSTEM

## Purpose

Discover helps a person find music that feels relevant without collapsing every recommendation into popularity or endless scrolling.

## Discovery levels

| Level | Meaning |
| --- | --- |
| Safe picks | Very likely to fit established listening patterns. |
| Explore | A little outside the normal pattern. |
| Wildcard | More unexpected, with a clear reason to try it. |

## Recommendation contract

Each recommendation should have a short explanation such as: “Recommended because you frequently listen to X and Y, but have not explored much Z.” It should reveal source context, allow dismissal, and avoid claiming certainty.

## Surfaces

For You is the initial Discover entry surface. New Music and Explore are planned navigation destinations. Artist, genre, mood, era, and playlist context may become discovery inputs as their underlying data exists.

## Principles

Personal relevance over popularity. Quality over quantity. Context before novelty. A clear next action. No recommendation without evidence.

## Empty and disconnected states

Before Spotify data and taste signals exist, Discover explains what connection will enable and shows no fabricated recommendations.

## Illustration Required

**Purpose:** show a recommendation with a reason.

**Description:** three recommendation cards or lanes for Safe picks, Explore, and Wildcard, each with rationale and a quiet save/play action.

**Suggested composition:** use increasing visual distance from the listener’s known taste while keeping the same card grammar.

**Priority:** P0. **Assets:** approved sample content or labelled fixture data only.

## Related pages

[Taste](13-ANALYTICS_SYSTEM.md) · [Player](11-MUSIC_PLAYER.md) · [AI](12-AI_SYSTEM.md) · [Search](16-SEARCH_SYSTEM.md)

## TODO

- Define recommendation inputs, ranking, feedback, and provider limits.
- Confirm whether Discover is server-generated, cached, or user-triggered.
