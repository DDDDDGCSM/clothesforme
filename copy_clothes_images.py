#!/usr/bin/env python3
"""
复制衣服图片到 static 目录
"""
import os
import shutil
from pathlib import Path

# 源目录和目标目录
source_dir = Path("/Users/a58/cursor/归档/OK 调研/bookforME/中东衣服")
target_dir = Path("/Users/a58/cursor/归档/OK 调研/bookforME/static/clothes-middle-east")

# 创建目标目录
target_dir.mkdir(parents=True, exist_ok=True)

# 复制所有 PNG 文件
png_files = list(source_dir.glob("*.png"))
print(f"找到 {len(png_files)} 个 PNG 文件")

for png_file in png_files:
    target_file = target_dir / png_file.name
    shutil.copy2(png_file, target_file)
    print(f"已复制: {png_file.name}")

print(f"\n✅ 所有图片已复制到: {target_dir}")

