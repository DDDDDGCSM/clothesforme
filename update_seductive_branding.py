#!/usr/bin/env python3
"""
更新品牌名称和所有文案，使其更具诱惑力，吸引男性用户
"""
import json
import re

# 新的品牌名称
NEW_BRAND_NAME_AR = "تبادل الإغراء - Exchange Desire"
NEW_BRAND_NAME_ZH = "欲望交换 - Desire Exchange"

# 新的诱惑性文案（英文）- 更直接、更有吸引力
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

# 新的诱惑性文案（中文）- 更直接、更有吸引力
SEDUCTIVE_COPY_ZH = {
    1: "我想要交换这件令人惊艳的泳装，因为我在寻找能让我在海滩上成为焦点的单品。这件衣服一直是我吸引眼球的秘密武器，现在我准备用它换取让我感觉更加不可抗拒的东西。非常适合想要看起来绝对迷人的你。",
    2: "我想要交换这套休闲装，因为我想要能瞬间抓住你眼球的东西。这件衣服一直是我展现魅力的首选，我准备用它换取让我感觉更加诱人的单品。适合想要看起来轻松性感的你。",
    3: "我想要交换这套职业装，因为我在寻找能让我感觉既强大又不可抗拒的单品。这套衣服一直是我的自信助推器，现在我想用它换取让我感觉更加迷人的东西。非常适合想要看起来既专业又绝对迷人的你。",
    4: "我想要交换这套时尚装，因为我想要让我感觉更加诱人的东西。这件衣服一直是我吸引眼球的最爱，我准备用它换取让我感觉更加不可抗拒的单品。适合想要看起来轻松火辣诱人的你。",
    5: "我想要交换这套舒适装，因为我在寻找能让我感觉更加迷人的东西。这件衣服一直是我的舒适选择，但现在我想要让我感觉更加吸引人和迷人的单品。非常适合想要看起来既舒适又绝对不可抗拒的你。",
    6: "我想要交换这件优雅礼服，因为我想要让我感觉更加不可抗拒的东西。这件衣服一直是我特殊场合的秘密武器，现在我想用它换取让我感觉更加迷人的单品。适合想要看起来惊艳绝对性感的你。",
    7: "我想要交换这件休闲上衣，因为我在寻找能让我感觉更加吸引人的东西。这件衣服一直是我看起来很棒的首选，现在我想用它换取让我感觉更加迷人的单品。非常适合想要看起来轻松性感诱人的你。",
    8: "我想要交换这套现代装，因为我想要让我感觉更加诱人的东西。这件衣服一直是我吸引注意力的最爱，我准备用它换取让我感觉更加不可抗拒的单品。适合想要看起来火辣绝对迷人的你。",
    9: "我想要交换这件经典单品，因为我在寻找能让我感觉更加迷人的东西。这件衣服一直是我的经典选择，但现在我想要让我感觉更加吸引人和诱人的单品。非常适合想要看起来既优雅又绝对不可抗拒的你。",
    10: "我想要交换这套个性装，因为我想要让我感觉更加不可抗拒的东西。这件衣服一直是我吸引眼球的大胆选择，现在我想用它换取让我感觉更加迷人的单品。适合想要看起来惊艳绝对性感的你。",
    11: "我想要交换这套百搭装，因为我在寻找能让我感觉更加吸引人的东西。这件衣服一直是我的可靠选择，现在我想用它换取让我感觉更加迷人的单品。非常适合想要看起来轻松性感诱人的你。",
    12: "我想要交换这套特殊场合装，因为我想要让我感觉更加诱人的东西。这件衣服一直是我庆祝活动的首选，我准备用它换取让我感觉更加不可抗拒的单品。适合想要看起来火辣绝对迷人的你。",
    13: "我想要交换这套睡衣，因为我在寻找能让我感觉更加迷人的东西。这件衣服一直是我的舒适选择，但现在我想要让我感觉更加吸引人和诱人的单品。非常适合想要看起来既舒适又绝对不可抗拒的你。",
    14: "我想要交换这套时尚杂志合集，因为我想要能激励我看起来更加不可抗拒的东西。这套合集一直是我的风格指南，现在我想用它换取让我感觉更加迷人的东西。适合想要跟上性感时尚潮流的你。",
    15: "我想要交换这本时尚交换杂志，因为我在寻找能让我感觉更加吸引人的东西。这本杂志一直是我的灵感来源，现在我想用它换取让我感觉更加迷人的东西。非常适合想要发现如何看起来绝对不可抗拒的你。"
}

# 更新 translations.py
with open('translations.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 更新品牌名称
content = re.sub(r"'site_title': 'Trueque Digital - تبادل الملابس'", f"'site_title': '{NEW_BRAND_NAME_AR}'", content)
content = re.sub(r"'site_title': 'Trueque Digital - 衣服交换'", f"'site_title': '{NEW_BRAND_NAME_ZH}'", content)

# 更新中文文案
for item_id, new_copy in SEDUCTIVE_COPY_ZH.items():
    pattern = f"(\\s+'id': {item_id},[\\s\\S]*?'why_release': ')[^']*(')"
    escaped_copy = new_copy.replace("'", "\\'")
    content = re.sub(pattern, f"\\g<1>{escaped_copy}\\g<2>", content)

with open('translations.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 已更新translations.py')

# 更新 clothes_data.py
with open('clothes_data.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 更新英文文案
for item_id, new_copy in SEDUCTIVE_COPY_EN.items():
    pattern = f"(\\s+'id': {item_id},[\\s\\S]*?'why_release': ')[^']*(')"
    escaped_copy = new_copy.replace("'", "\\'")
    content = re.sub(pattern, f"\\g<1>{escaped_copy}\\g<2>", content)

with open('clothes_data.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 已更新clothes_data.py')

print('✅ 所有文案已更新为更具诱惑力的版本！')

