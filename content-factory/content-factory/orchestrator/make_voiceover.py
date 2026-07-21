#!/usr/bin/env python3
"""Free voiceover + captions via Microsoft Edge neural TTS.
Usage: pip install edge-tts
       python orchestrator/make_voiceover.py script.txt out.mp3 [voice]
Writes out.mp3 AND out.srt (subtitles) — upload the SRT to YouTube/TikTok
or burn it in with assemble_video.py.
"""
import asyncio, pathlib, sys
import yaml
import edge_tts

ROOT = pathlib.Path(__file__).resolve().parent.parent

async def main():
    text = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
    out = pathlib.Path(sys.argv[2])
    cfg = yaml.safe_load((ROOT / "orchestrator" / "config.yaml").read_text())
    voice = sys.argv[3] if len(sys.argv) > 3 else cfg.get("voice", "en-GB-RyanNeural")

    communicate = edge_tts.Communicate(text, voice)
    submaker = edge_tts.SubMaker()
    with open(out, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] in ("WordBoundary", "SentenceBoundary"):
                submaker.feed(chunk)
    srt = out.with_suffix(".srt")
    srt.write_text(submaker.get_srt(), encoding="utf-8")
    print(f"Saved {out} + {srt} ({voice})")

asyncio.run(main())
