# 🏭 Content Factory

This is the merged entry point for the ContentFactory project. It combines the original product overview with the local setup instructions and the new project-level layout.

An AI-orchestrated faceless content business. One Master agent manages a virtual team of specialist agents, produces content on a schedule, and asks you only for approvals.

**Target: £5,000/month — reached in milestones, not overnight.**

```
                        ┌─────────────────────┐
                        │   YOU (approvals)   │
                        └──────────▲──────────┘
                                   │ approve / reject / redirect
                        ┌──────────┴──────────┐
                        │   MASTER (CEO agent) │  ← agents/MASTER.md
                        └──────────┬──────────┘
        ┌────────────┬─────────────┼─────────────┬────────────┐
        ▼            ▼             ▼             ▼            ▼
   Researcher   Scriptwriter   Producer      Publisher     Analyst
   (trends &    (scripts &     (voiceover,   (YouTube,     (metrics,
    niches)      hooks)         visuals,      TikTok,       weekly
                                assembly)     blog)         report)
```

## What this environment does
- Coordinates a multi-agent workflow for research, scripting, production, publishing, and analysis
- Stores drafts in pending, approved, and published content folders
- Supports local execution and simple setup for development or experimentation

## How it runs without you

1. GitHub Actions (free) wakes the orchestrator on a schedule (default: daily 7am).
2. The orchestrator calls the Claude API with the Master + team prompts and generates finished script drafts into [content/pending/](content/pending/).
3. You get a notification (GitHub commit / email via Zapier). You review on your phone, move approved files to [content/approved/](content/approved/) (or just reply "approve #3").
4. Approved scripts get produced (voiceover + visuals) and published.
5. Every Sunday the Analyst writes a performance report to [data/](data/) and the Master proposes next week's plan — again, waiting only on your approval.

Nothing publishes without your explicit approval. That is the one human step by design.

## Requirements
See [requirements.md](requirements.md) for the full list of software, environment variables, and optional tools.

## Design overview
See [designs.md](designs.md) for the architecture, runtime flow, and deployment model.

## Installation

### 1. Prerequisites
Make sure you have:
- Python 3.10 or newer
- Git
- An Anthropic API key

### 2. Clone and enter the repository
```bash
git clone https://github.com/giriva/ContentFactory.git
cd ContentFactory
```

### 3. Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Set your environment variable
```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

## Step-by-step startup instructions
1. Open a terminal in the project root.
2. Activate the virtual environment.
3. Install the Python dependencies.
4. Export your Anthropic API key.
5. Start the environment with the one-command launcher below.

## One-command startup
Run the following command from the project root:

```bash
./start.sh
```

The launcher will:
- create the local virtual environment if needed
- install the Python dependencies from [requirements.txt](requirements.txt)
- verify that the API key is available
- start the orchestrator workflow

## Repo map

| Path | What it is |
|---|---|
| [agents/](agents/) | System prompts for the Master and each specialist |
| [orchestrator/run.py](orchestrator/run.py) | The engine: runs the team pipeline via Claude API |
| [orchestrator/config.yaml](orchestrator/config.yaml) | Your niche, cadence, targets, voice |
| [content/pending/](content/pending/) | Drafts awaiting YOUR approval |
| [content/approved/](content/approved/) | Approved → ready to produce |
| [content/published/](content/published/) | Live content archive |
| [templates/](templates/) | Script + calendar + tracker templates |
| [ROADMAP.md](ROADMAP.md) | Phased plan: content first, platform features only when needed |
| [orchestrator/assemble_video.py](orchestrator/assemble_video.py) | Free FFmpeg auto-assembly (clips + voice + captions → video) |
| [docs/ECONOMICS.md](docs/ECONOMICS.md) | Free vs paid stack, the honest maths to £5k |
| [docs/APPROVAL_WORKFLOW.md](docs/APPROVAL_WORKFLOW.md) | Exactly how approvals work |
| [SETUP.md](SETUP.md) | Plug-and-play setup checklist |

## Milestones (iterate slowly — this is the plan)

| Phase | Goal | Focus |
|---|---|---|
| 0 (wk 1–2) | Ship 10 pieces | Prove the pipeline works end-to-end |
| 1 (mo 1–2) | First £100 | Find what gets views; add affiliate links |
| 2 (mo 3–4) | £1,000/mo | Double down on winners, add digital product |
| 3 (mo 5+) | £5,000/mo | Scale winning format, multiple revenue streams |

## Honest disclaimer

The agents remove the labour bottleneck, not the market one. £5k/month requires content people actually watch and offers people actually buy. The Analyst's weekly reports exist to find that fit fast. Expect the first month to earn ~£0 — that's normal and budgeted for.
