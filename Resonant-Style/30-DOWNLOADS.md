# 30 — DOWNLOADS & DISTRIBUTION

## Purpose

Explain how people enter Resonant, create an account, and connect Spotify without weakening trust.

## Verified distribution language

The current repository is a web application deployed through Vercel, with local, Preview, and Production environments. The public landing page must work without credentials. Account creation uses Google; Spotify connection uses a separate server-side OAuth flow with PKCE. No installer, downloadable desktop build, or signed binary is verified.

## Documentation rules

State the public URL, environment, account requirements, Spotify permissions, privacy boundary, and any Preview access method exactly as the target release states them. Never imply that a web Preview is Production or that connecting Spotify grants Resonant account access.

## TODO

- Confirm final domain, Vercel project, and public release URL.
- Document Spotify consent scopes and provider revocation guidance.
- Add final privacy, retention, export, and account deletion copy.
## Verification checklist

Before publishing a download page, verify filename, platform, version, checksum, signing state, licence, third-party notices, hardware requirements, network requirements, and rollback/retry guidance. Keep copy release-specific.
