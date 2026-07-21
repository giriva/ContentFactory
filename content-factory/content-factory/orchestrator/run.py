#!/usr/bin/env python3
"""
Content Factory orchestrator.
Runs the Master + team pipeline via the Claude API and writes finished
draft packages into content/pending/ for owner approval.

Usage:
  export ANTHROPIC_API_KEY=sk-ant-...
  python orchestrator/run.py            # daily content run
  python orchestrator/run.py --weekly   # weekly analyst report
"""

import argparse
import datetime as dt
import os
import pathlib
import sys

import yaml

try:
    import anthropic
except ImportError:
    sys.exit("Run: pip install anthropic pyyaml")

ROOT = pathlib.Path(__file__).resolve().parent.parent
AGENTS = ROOT / "agents"
PENDING = ROOT / "content" / "pending"
DATA = ROOT / "data"

MODEL = "claude-sonnet-4-6"  # good quality/cost balance; use haiku to cut cost further


def load(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def load_config() -> dict:
    return yaml.safe_load(load(ROOT / "orchestrator" / "config.yaml"))


def call(client, system: str, user: str, max_tokens: int = 4000) -> str:
    msg = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return "".join(b.text for b in msg.content if b.type == "text")


def daily_run(client, cfg: dict) -> None:
    today = dt.date.today().isoformat()
    master = load(AGENTS / "MASTER.md")
    team = {
        name: load(AGENTS / f"{name}.md")
        for name in ["researcher", "scriptwriter", "producer"]
    }
    niche_brief = (
        f"Niche: {cfg['niche']}\nAudience: {cfg['audience']}\n"
        f"Tone: {cfg['tone']}\nFormats: {cfg['formats']}\n"
        f"Pieces per run: {cfg['pieces_per_run']}\nDate: {today}\n"
        f"Recent topics already used (avoid repeats): {recent_topics()}"
    )

    # 1. Researcher proposes topics
    topics = call(client, master + "\n\n" + team["researcher"],
                  f"{niche_brief}\n\nPropose today's ranked topic candidates.")

    # 2. Scriptwriter drafts the top picks
    scripts = call(client, master + "\n\n" + team["scriptwriter"],
                   f"{niche_brief}\n\nTopic candidates from Researcher:\n{topics}\n\n"
                   f"Write complete script packages for the top {cfg['pieces_per_run']} topics.",
                   max_tokens=8000)

    # 3. Producer attaches production plans
    plans = call(client, master + "\n\n" + team["producer"],
                 f"Scripts:\n{scripts}\n\nAttach a production plan to each script.",
                 max_tokens=4000)

    # 4. Master summarises for the owner
    summary = call(client, master,
                   f"Today's drafts:\n{scripts}\n\nProduction plans:\n{plans}\n\n"
                   "Write the owner-facing approval request block for this batch.")

    out = PENDING / f"{today}-batch.md"
    out.write_text(
        f"# Batch {today} — AWAITING APPROVAL\n\n{summary}\n\n---\n\n"
        f"## Topic research\n{topics}\n\n---\n\n"
        f"## Scripts\n{scripts}\n\n---\n\n"
        f"## Production plans\n{plans}\n",
        encoding="utf-8",
    )
    print(f"Wrote {out.relative_to(ROOT)} — review and move to content/approved/ to proceed.")


def weekly_run(client, cfg: dict) -> None:
    master = load(AGENTS / "MASTER.md")
    analyst = load(AGENTS / "analyst.md")
    tracker = DATA / "tracker.csv"
    stats = tracker.read_text() if tracker.exists() else "No tracker data yet."
    report = call(client, master + "\n\n" + analyst,
                  f"Weekly review. Milestone target: {cfg['milestone']}.\n"
                  f"Tracker data:\n{stats}\n\nWrite the weekly report and next-week proposal.")
    out = DATA / f"report-{dt.date.today().isoformat()}.md"
    out.write_text(report, encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)}")


def recent_topics() -> str:
    files = sorted(PENDING.glob("*-batch.md"))[-5:]
    titles = []
    for f in files:
        for line in f.read_text(encoding="utf-8").splitlines():
            if line.startswith("## ") or line.startswith("### "):
                titles.append(line.strip("# ").strip())
    return "; ".join(titles[-15:]) or "none yet"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--weekly", action="store_true", help="run the weekly analyst report")
    args = ap.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("Set ANTHROPIC_API_KEY first.")
    client = anthropic.Anthropic()
    cfg = load_config()

    if args.weekly:
        weekly_run(client, cfg)
    else:
        daily_run(client, cfg)


if __name__ == "__main__":
    main()
