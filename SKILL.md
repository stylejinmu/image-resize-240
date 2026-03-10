---
name: image-resize-240
description: 将用户上传的图片批量转换为 240×240 像素。适用场景：用户要求将图片缩放/调整为 240x240、生成缩略图、统一图片尺寸为 240 像素等。支持 JPEG、PNG、GIF、BMP、WEBP、TIFF 格式。
---

# Image Resize to 240×240

## Workflow

1. Collect all user-uploaded image file paths.
2. Run the resize script:

```bash
python3.11 /home/ubuntu/skills/image-resize-240/scripts/resize_to_240.py <file1> [<file2> ...] [--output-dir <dir>]
```

3. Deliver the output files to the user via `message` tool with `attachments`.

## Key Behaviors

- Output files are named `<original_stem>_240x240<ext>` and saved next to the originals unless `--output-dir` is specified.
- JPEG output: transparent layers are composited onto a **white background**.
- PNG output: transparency is **preserved**.
- GIF: only the **first frame** is resized and saved as a static image.
- Unsupported formats and missing files are reported as errors; other files continue processing.

## Example

```bash
python3.11 /home/ubuntu/skills/image-resize-240/scripts/resize_to_240.py \
    /home/ubuntu/Downloads/photo.jpg \
    /home/ubuntu/Downloads/icon.png \
    --output-dir /home/ubuntu/Downloads/resized
```
