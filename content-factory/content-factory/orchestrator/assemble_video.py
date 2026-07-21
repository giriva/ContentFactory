#!/usr/bin/env python3
"""Free automatic video assembly with FFmpeg (their 'Remotion', for £0).
Takes a folder of stock clips (from Pexels/Pixabay), a voiceover mp3, and an
optional .srt — outputs a 1080x1920 vertical video with captions burned in.

Usage:
  python orchestrator/assemble_video.py clips_folder/ voiceover.mp3 out.mp4
Requires ffmpeg + ffprobe installed (free: https://ffmpeg.org).
"""
import pathlib, subprocess, sys, tempfile

def dur(path):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)]).strip())

def main():
    clips_dir, voice, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), sys.argv[3]
    clips = sorted(p for p in clips_dir.iterdir() if p.suffix.lower() in {".mp4", ".mov"})
    if not clips:
        sys.exit("No clips found.")
    total = dur(voice)
    per_clip = total / len(clips)
    srt = voice.with_suffix(".srt")

    with tempfile.TemporaryDirectory() as td:
        parts = []
        for i, c in enumerate(clips):
            p = pathlib.Path(td) / f"part{i}.mp4"
            subprocess.run([
                "ffmpeg", "-y", "-v", "error", "-i", str(c), "-t", f"{per_clip:.2f}",
                "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,"
                       "crop=1080:1920,fps=30", "-an", str(p)], check=True)
            parts.append(p)
        concat = pathlib.Path(td) / "list.txt"
        concat.write_text("".join(f"file '{p}'\n" for p in parts))
        vf = (f"subtitles={srt}:force_style='FontSize=16,Bold=1,Outline=2,"
              f"Alignment=2,MarginV=60'") if srt.exists() else "null"
        subprocess.run([
            "ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(concat),
            "-i", str(voice), "-vf", vf, "-c:v", "libx264", "-preset", "fast",
            "-c:a", "aac", "-shortest", out], check=True)
    print(f"Done: {out} ({total:.0f}s, {len(clips)} clips)")

if __name__ == "__main__":
    main()
