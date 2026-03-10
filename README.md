# image-resize-240

一个 [Manus](https://manus.im) Skill，可将上传的图片批量转换为精确的 **240×240 像素**。

## 功能简介

`image-resize-240` 是一个模块化的 Manus Skill，用于一键统一图片尺寸。无论是生成缩略图、制作统一规格的图标集，还是其他固定尺寸的图片输出需求，该 Skill 均可自动完成转换，支持多种格式，并在适当情况下保留图片透明度。

## 特性

| 特性 | 说明 |
|---|---|
| **支持格式** | JPEG、PNG、GIF、BMP、WEBP、TIFF |
| **输出尺寸** | 精确 240×240 像素 |
| **批量处理** | 单次命令处理多个文件 |
| **透明通道（PNG）** | 保留透明度 |
| **透明通道（JPEG）** | 自动合成白色背景 |
| **GIF 处理** | 提取第一帧并保存为静态图 |
| **输出命名** | `原文件名_240x240.扩展名`，默认保存在原文件同目录，可通过 `--output-dir` 指定输出目录 |

## 文件结构

```
image-resize-240/
├── SKILL.md                   # Skill 元数据与 Manus 工作流指令
├── README.md                  # 本文件
└── scripts/
    └── resize_to_240.py       # 核心图片转换脚本（基于 Pillow）
```

## 使用方式

### 通过 Manus 使用

安装 Skill 后，只需上传图片并告知 Manus 将其转换为 240×240，Manus 将自动调用该 Skill 并返回转换后的文件。

### 通过命令行使用

```bash
python3 scripts/resize_to_240.py <文件1> [<文件2> ...] [--output-dir <目录>]
```

**示例：**

```bash
# 转换单个文件（输出保存在原文件同目录）
python3 scripts/resize_to_240.py photo.jpg

# 批量转换多个文件并指定输出目录
python3 scripts/resize_to_240.py icon.png banner.webp logo.tiff --output-dir ./resized
```

## 环境依赖

- Python 3.8+
- [Pillow](https://python-pillow.org/)（`pip install pillow`）

## 实现原理

脚本使用 Pillow 的 `LANCZOS` 重采样滤镜（最高质量的降采样算法）将每张图片缩放至 240×240 像素。对于含透明通道的图片，输出格式决定处理方式：PNG 文件保留 Alpha 通道；JPEG 文件（不支持透明度）则将透明区域合成到白色背景后再保存。

## 许可证

本 Skill 按原样提供，供 Manus 智能体平台使用。
