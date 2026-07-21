# SETUP.md — Plug-and-play checklist (free-first)

Do these in order. Total cost to start: **~£0–5/month** (only the Claude API usage is paid, pennies per run).

## Step 1 — Already done ✅ (your connected Claude tools)

These are already connected in your Claude.ai account and need nothing:

- **Canva** → thumbnails & channel art (free tier)
- **WordPress.com** → the blog leg (free tier, upgrade later only if it earns)
- **Google Drive** → asset storage (scripts, audio, video files)
- **Google Calendar** → content calendar sync
- **Gmail** → approval notifications
- **Zapier** (free: 100 tasks/mo) → glue for notifications & cross-posting

## Step 2 — Accounts to create (all free, ~10 min)

| # | Account | Why | Cost |
|---|---|---|---|
| 1 | GitHub repo (private) | Home of the factory + free daily automation | Free |
| 2 | YouTube channel (new, on your Google account) | Primary long-term revenue | Free |
| 3 | TikTok account | Fast feedback loop, repurposed shorts | Free |
| 4 | Anthropic API key (console.anthropic.com) | Powers the agent team | ~£2–5/mo usage |
| 5 | Pexels + Pixabay accounts | Free stock video/images, free API keys | Free |

## Step 3 — Wire the automation (10 min)

1. Push this repo to GitHub (commands at the bottom).
2. Repo → Settings → Secrets and variables → Actions → **New repository secret**:
   - `ANTHROPIC_API_KEY` = your key
3. Actions tab → enable workflows. Done — the factory now runs daily.

## Step 4 — Approval notifications (pick ONE, 5 min)

- **Easiest:** GitHub mobile app → watch the repo → you get a push notification when new drafts land in `content/pending/`.
- **Zapier (free):** Zap = "New file in GitHub repo path content/pending" → "Send Gmail to me". Uses ~30 of your 100 free tasks/mo.

## Free production stack (no paid video tools)

| Job | Free tool | Paid alternative (only when earning) |
|---|---|---|
| Voiceover | **Edge-TTS** (Microsoft neural voices, free, script included) | ElevenLabs £5/mo |
| Video assembly | **CapCut desktop** (free) or FFmpeg script | Descript £12/mo |
| Stock footage | Pexels / Pixabay (free + API) | Storyblocks £15/mo |
| Music | YouTube Audio Library (free) | Epidemic Sound £9/mo |
| Thumbnails | Canva free (already connected) | Canva Pro £11/mo |
| Scheduling | YouTube/TikTok native schedulers (free) | Buffer £5/mo |

**Rule: nothing gets a paid upgrade until the free version is the proven bottleneck.**

## Push to GitHub (run on your machine, 2 min)

```bash
# 1. Create a new PRIVATE repo named content-factory on github.com (no README)
# 2. Then in the unzipped folder:
git init
git add -A
git commit -m "Content Factory v1"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/content-factory.git
git push -u origin main
```

That's it. First test run: `python orchestrator/run.py` (needs `pip install anthropic pyyaml` and `export ANTHROPIC_API_KEY=...`).
