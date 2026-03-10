#!/usr/bin/env python3
"""
Resize one or more images to exactly 240x240 pixels.

Usage:
    python resize_to_240.py <input_path> [<input_path2> ...] [--output-dir <dir>]

- Supports: JPEG, PNG, GIF (first frame), BMP, WEBP, TIFF
- Output files are saved alongside originals by default, with suffix `_240x240`
- If --output-dir is specified, all outputs go to that directory
- Transparent images (RGBA/P) are composited on a white background before saving as JPEG;
  PNG output preserves transparency
"""

import argparse
import sys
from pathlib import Path
from PIL import Image


SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".tif"}
TARGET_SIZE = (240, 240)


def resize_image(input_path: Path, output_dir: Path | None = None) -> Path:
    """Resize a single image to 240x240 and save it. Returns the output path."""
    with Image.open(input_path) as img:
        # For animated GIFs, use only the first frame
        if hasattr(img, "n_frames") and img.n_frames > 1:
            img.seek(0)

        # Convert palette images to RGBA to preserve transparency
        if img.mode == "P":
            img = img.convert("RGBA")

        resized = img.resize(TARGET_SIZE, Image.LANCZOS)

        # Determine output path
        suffix = input_path.suffix.lower()
        stem = input_path.stem + "_240x240"
        out_name = stem + suffix

        if output_dir:
            output_dir.mkdir(parents=True, exist_ok=True)
            out_path = output_dir / out_name
        else:
            out_path = input_path.parent / out_name

        # Save — for JPEG, flatten transparency onto white background
        if suffix in {".jpg", ".jpeg"}:
            if resized.mode in ("RGBA", "LA"):
                background = Image.new("RGB", TARGET_SIZE, (255, 255, 255))
                background.paste(resized, mask=resized.split()[-1])
                resized = background
            elif resized.mode != "RGB":
                resized = resized.convert("RGB")
            resized.save(out_path, quality=95)
        else:
            resized.save(out_path)

        return out_path


def main():
    parser = argparse.ArgumentParser(description="Resize images to 240x240 pixels.")
    parser.add_argument("inputs", nargs="+", help="Input image file paths")
    parser.add_argument("--output-dir", "-o", type=str, default=None,
                        help="Directory to save resized images (default: same as input)")
    args = parser.parse_args()

    output_dir = Path(args.output_dir) if args.output_dir else None
    errors = []

    for raw_path in args.inputs:
        p = Path(raw_path)
        if not p.exists():
            errors.append(f"File not found: {p}")
            continue
        if p.suffix.lower() not in SUPPORTED_EXTENSIONS:
            errors.append(f"Unsupported format: {p.suffix} ({p})")
            continue
        try:
            out = resize_image(p, output_dir)
            print(f"✅  {p.name}  →  {out}")
        except Exception as e:
            errors.append(f"Failed to process {p}: {e}")

    if errors:
        print("\nErrors:", file=sys.stderr)
        for err in errors:
            print(f"  ✗ {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
