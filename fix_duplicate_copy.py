#!/usr/bin/env python3
"""
修复重复拼接的文案，只保留新的诱惑性文案
"""
import re

# 新的诱惑性文案（英文）
SEDUCTIVE_COPY_EN = {
    1: "I'm trading this stunning swimsuit because I want something that will make every head turn at the beach. This piece has been my secret weapon for attracting attention, and I'm ready to exchange it for something that will make me feel even more irresistible. Perfect for someone who wants to look absolutely captivating.",
    2: "I want to exchange this casual outfit because I'm looking for something that will catch your eye instantly. This piece has been my go-to for making a bold statement, and I'm ready to swap it for something that will make me feel even more alluring. Ideal for someone who wants to look effortlessly seductive.",
    3: "I'm trading this professional attire because I want something that will make me feel powerful and irresistible. This outfit has been my confidence booster, and now I want to exchange it for something that will make me feel even more desirable. Perfect for someone who wants to look both professional and absolutely captivating.",
    4: "I want to exchange this trendy outfit because I'm seeking something that will make me feel more seductive. This piece has been my favorite for turning heads, and I'm ready to trade it for something that will make me feel even more irresistible. Ideal for someone who wants to look effortlessly hot and alluring.",
    5: "I'm trading this comfortable wear because I want something that will make me feel more desirable. This piece has been my comfort choice, but now I want something that will make me feel more attractive and captivating. Perfect for someone who wants to look both comfortable and absolutely irresistible.",
    6: "I want to exchange this elegant dress because I'm looking for something that will make me feel more irresistible. This piece has been my secret weapon for special occasions, and now I want to trade it for something that will make me feel even more captivating. Ideal for someone who wants to look stunning and absolutely seductive.",
    7: "I'm trading this casual top because I want something that will make me feel more attractive. This piece has been my go-to for looking amazing, and now I want to exchange it for something that will make me feel even more desirable. Perfect for someone who wants to look effortlessly sexy and alluring.",
    8: "I want to exchange this modern outfit because I'm seeking something that will make me feel more seductive. This piece has been my favorite for attracting attention, and I'm ready to swap it for something that will make me feel even more irresistible. Ideal for someone who wants to look hot and absolutely captivating.",
    9: "I'm trading this timeless piece because I want something that will make me feel more desirable. This piece has been my classic choice, but now I want something that will make me feel more attractive and alluring. Perfect for someone who wants to look both elegant and absolutely irresistible.",
    10: "I want to exchange this statement outfit because I'm looking for something that will make me feel more irresistible. This piece has been my bold choice for turning heads, and now I want to trade it for something that will make me feel even more captivating. Ideal for someone who wants to look stunning and absolutely seductive.",
    11: "I'm trading this versatile outfit because I want something that will make me feel more attractive. This piece has been my reliable choice, and now I want to exchange it for something that will make me feel even more desirable. Perfect for someone who wants to look effortlessly sexy and alluring.",
    12: "I want to exchange this special occasion outfit because I'm seeking something that will make me feel more seductive. This piece has been my go-to for celebrations, and I'm ready to swap it for something that will make me feel even more irresistible. Ideal for someone who wants to look hot and absolutely captivating.",
    13: "I'm trading this sleepwear set because I want something that will make me feel more desirable. This piece has been my comfort choice, but now I want something that will make me feel more attractive and alluring. Perfect for someone who wants to look both comfortable and absolutely irresistible.",
    14: "I want to exchange this fashion magazine collection because I'm looking for something that will inspire me to look more irresistible. This collection has been my style guide, and now I want to trade it for something that will make me feel even more captivating. Ideal for someone who wants to stay updated with seductive fashion trends.",
    15: "I'm trading this fashion exchange magazine because I want something that will make me feel more attractive. This magazine has been my inspiration, and now I want to exchange it for something that will make me feel even more desirable. Perfect for someone who wants to discover the art of looking absolutely irresistible."
}

# 读取clothes_data.py
with open('clothes_data.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 修复所有重复的文案
for item_id, new_copy in SEDUCTIVE_COPY_EN.items():
    # 找到包含重复内容的why_release行
    pattern = f"(\\s+'id': {item_id},[\\s\\S]*?'why_release': ')[^']*(')"
    # 匹配到第一个单引号结束的位置，然后替换
    escaped_copy = new_copy.replace("'", "\\'")
    # 使用更精确的模式，匹配到第一个完整的why_release值
    pattern2 = f"(\\s+'id': {item_id},[\\s\\S]*?'why_release': ')[^']*'[^']*(')"
    content = re.sub(pattern2, f"\\g<1>{escaped_copy}\\g<2>", content)
    # 如果还有重复，再替换一次
    pattern3 = f"(\\s+'id': {item_id},[\\s\\S]*?'why_release': ')[^']*'[^']*(')"
    content = re.sub(pattern3, f"\\g<1>{escaped_copy}\\g<2>", content)

# 手动修复每个项目（更可靠的方法）
for item_id in range(1, 16):
    new_copy = SEDUCTIVE_COPY_EN[item_id]
    escaped_copy = new_copy.replace("'", "\\'")
    # 找到id对应的整个字典块
    pattern = f"(\\s+'id': {item_id},[\\s\\S]*?'why_release': ')[^']*'[^']*(')"
    matches = re.findall(pattern, content)
    if matches:
        # 替换第一个匹配
        content = re.sub(pattern, f"\\g<1>{escaped_copy}\\g<2>", content, count=1)

with open('clothes_data.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 已修复clothes_data.py中的重复文案')

# 验证语法
import py_compile
try:
    py_compile.compile('clothes_data.py', doraise=True)
    print('✅ 语法检查通过')
except py_compile.PyCompileError as e:
    print(f'❌ 语法错误: {e}')

