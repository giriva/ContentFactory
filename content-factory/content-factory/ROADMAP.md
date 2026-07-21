# ROADMAP.md — Content first, platform later

This merges the "AI Factory" feature vision with a lean, revenue-first sequence.
Rule: **a feature gets built only when its absence is the measured bottleneck.**

## Phase 0 — Ship (weeks 1–2)  ← YOU ARE HERE
- Repo live, GitHub Actions running daily batches
- 10 pieces published across YT Shorts + TikTok + blog
- Covers from ChatGPT plan: trend research, idea gen, script gen, voice gen (Edge-TTS),
  captions (auto-SRT), SEO basics, content calendar, publishing checklist, human review

## Phase 1 — First £100 (months 1–2)
- A/B testing: 2 title/hook variants per piece, tracked in data/tracker.csv
- Affiliate layer live on every relevant piece
- Asset library: structured Google Drive folders (footage, audio, thumbnails, brand kit)
- Auto video assembly (FFmpeg script) once manual CapCut flow is proven

## Phase 2 — £1k/mo (months 3–4)
- Own digital product (£15–30) sold via Gumroad/Ko-fi
- Email capture (free tier: MailerLite/Beehiiv) linked from blog + descriptions
- Zapier automations: pending-draft alerts, cross-posting, tracker updates
- Analytics upgrade: weekly report reads YouTube Studio CSV exports

## Phase 3 — £5k/mo (months 5+)
- Second brand/niche IF brand #1 is profitable (multi-brand = a second config.yaml, not a platform)
- Consider paid upgrades only where free tier is the proven bottleneck
- Optional: simple dashboard page generated from tracker.csv (static HTML, free on GitHub Pages)

## Explicitly deferred from the "AI Factory" plan (and why)
| Their feature | Our answer | Build it when… |
|---|---|---|
| Next.js dashboard + auth | Analyst weekly report + GitHub | you have >3 people using it |
| FastAPI backend | run.py + Actions | scheduled runs stop being enough |
| PostgreSQL + Redis | tracker.csv → Google Sheet | tracker exceeds ~5k rows |
| S3 storage | Google Drive (connected, free) | Drive 15GB is full |
| Self-hosted n8n + Docker | Zapier free tier (connected) | you exceed 100 tasks/mo AND Zapier paid < value |
| Remotion rendering | CapCut → FFmpeg script | rendering >1 video/day manually |
| "Enterprise features" | never, probably | someone pays you for them |
