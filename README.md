# image-resize-240

A [Manus](https://manus.im) skill that batch-resizes uploaded images to exactly **240×240 pixels**.

## Overview

`image-resize-240` is a modular Manus skill designed to standardize image dimensions in a single command. Whether you need thumbnails, uniform icon sets, or any fixed-size image output, this skill handles the conversion automatically — supporting multiple formats and preserving transparency where appropriate.

## Features

| Feature | Details |
|---|---|
| **Supported formats** | JPEG, PNG, GIF, BMP, WEBP, TIFF |
| **Output size** | Exactly 240×240 pixels |
| **Batch processing** | Multiple files in a single invocation |
| **Transparency (PNG)** | Preserved in output |
| **Transparency (JPEG)** | Composited onto a white background |
| **GIF handling** | First frame extracted and saved as a static image |
| **Output naming** | `<original_stem>_240x240.<ext>` alongside the source file, or in a custom `--output-dir` |

## File Structure

```
image-resize-240/
├── SKILL.md          # Skill metadata and workflow instructions for Manus
├── README.md         # This file
└── scripts/
    └── resize_to_240.py   # Core image resizing script (Pillow-based)
```

## Usage

### Via Manus

Once the skill is installed, simply upload your images and ask Manus to resize them to 240×240. Manus will invoke the skill automatically and return the converted files.

### Via Command Line

```bash
python3 scripts/resize_to_240.py <file1> [<file2> ...] [--output-dir <dir>]
```

**Examples:**

```bash
# Resize a single file (output saved next to original)
python3 scripts/resize_to_240.py photo.jpg

# Resize multiple files to a specific output directory
python3 scripts/resize_to_240.py icon.png banner.webp logo.tiff --output-dir ./resized
```

## Requirements

- Python 3.8+
- [Pillow](https://python-pillow.org/) (`pip install pillow`)

## How It Works

The script uses Pillow's `LANCZOS` resampling filter — the highest-quality downsampling algorithm available — to resize each image to 240×240 pixels. For images with transparency, the behavior differs by output format: PNG files retain their alpha channel, while JPEG files (which do not support transparency) have the transparent regions composited onto a white background before saving.

## License

This skill is provided as-is for use with the Manus agent platform.
