#!/usr/bin/env python3
"""Build a cursors_scalable/ tree (KDE Breeze SVG cursor format, read by GNOME Shell 51+)."""
import json
import os
import shutil
import sys
from pathlib import Path

source_dir = Path(__file__).parent / "src"
output_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "dist/cursors_scalable")
shutil.rmtree(output_dir, ignore_errors=True)
output_dir.mkdir(parents=True)

for config_file in sorted((source_dir / "config").glob("*.cursor")):
    cursor_name = config_file.stem
    cursor_dir = output_dir / cursor_name
    cursor_dir.mkdir()
    frames = []
    for line in config_file.read_text().split("\n"):
        fields = line.split()
        if len(fields) < 4 or not fields[3].startswith("x1/"):
            continue
        nominal_size, hotspot_x, hotspot_y = (int(value) for value in fields[:3])
        svg_name = Path(fields[3]).with_suffix(".svg").name
        shutil.copy(source_dir / "svg" / svg_name, cursor_dir / svg_name)
        frame = {
            "filename": svg_name,
            "nominal_size": nominal_size,
            "hotspot_x": hotspot_x,
            "hotspot_y": hotspot_y,
        }
        if len(fields) >= 5:
            frame["delay"] = int(fields[4])
        frames.append(frame)
    (cursor_dir / "metadata.json").write_text(json.dumps(frames, indent=2) + "\n")

# CSS names GNOME requests that the upstream cursorList does not cover.
extra_aliases = [
    ("ns-resize", "size_ver"),
    ("ew-resize", "size_hor"),
    ("all-resize", "all-scroll"),
    ("dnd-ask", "copy"),
]
alias_lines = (source_dir / "cursorList").read_text().split("\n")
for alias_name, target_name in [line.split() for line in alias_lines if line.strip()] + extra_aliases:
    alias_path = output_dir / alias_name
    if not alias_path.exists():
        os.symlink(target_name, alias_path)

print(f"{len(list(output_dir.iterdir()))} entries in {output_dir}")
