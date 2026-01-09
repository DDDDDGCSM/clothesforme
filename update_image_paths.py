#!/usr/bin/env python3
"""
更新图片路径为英文文件名
"""
import re

# 更新clothes_data.py
with open('clothes_data.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 替换图片路径
replacements = {
    '/static/clothes-middle-east/衣服1.png': '/static/clothes-middle-east/item1.png',
    '/static/clothes-middle-east/衣服2.png': '/static/clothes-middle-east/item2.png',
    '/static/clothes-middle-east/衣服3.png': '/static/clothes-middle-east/item3.png',
    '/static/clothes-middle-east/衣服4.png': '/static/clothes-middle-east/item4.png',
    '/static/clothes-middle-east/衣服5.png': '/static/clothes-middle-east/item5.png',
    '/static/clothes-middle-east/衣服6.png': '/static/clothes-middle-east/item6.png',
    '/static/clothes-middle-east/衣服7.png': '/static/clothes-middle-east/item7.png',
    '/static/clothes-middle-east/衣服8.png': '/static/clothes-middle-east/item8.png',
    '/static/clothes-middle-east/衣服9.png': '/static/clothes-middle-east/item9.png',
    '/static/clothes-middle-east/衣服10.png': '/static/clothes-middle-east/item10.png',
    '/static/clothes-middle-east/衣服11.png': '/static/clothes-middle-east/item11.png',
    '/static/clothes-middle-east/衣服12.png': '/static/clothes-middle-east/item12.png',
    '/static/clothes-middle-east/睡衣.png': '/static/clothes-middle-east/sleepwear.png',
    '/static/clothes-middle-east/杂志.png': '/static/clothes-middle-east/magazine1.png',
    '/static/clothes-middle-east/杂志交换.png': '/static/clothes-middle-east/magazine2.png',
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open('clothes_data.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 已更新clothes_data.py中的图片路径')

# 更新translations.py中的中文数据
with open('translations.py', 'r', encoding='utf-8') as f:
    content = f.read()

for old, new in replacements.items():
    content = content.replace(old, new)

with open('translations.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 已更新translations.py中的图片路径')

