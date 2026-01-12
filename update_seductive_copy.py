#!/usr/bin/env python3
"""
更新衣服文案，使其更有诱惑性，吸引男性用户
从"为什么分享"改为"我想要交换的原因"
"""
import json

# 新的诱惑性文案（英文）
SEDUCTIVE_COPY_EN = {
    1: "I want to exchange this stunning swimsuit because I'm looking for something that will make me feel irresistible at the beach. This piece has been my secret weapon for turning heads, and now I'm ready to trade it for something equally captivating. Perfect for someone who wants to stand out and feel confident.",
    2: "I'm exchanging this casual outfit because I want something that will catch your eye. This piece has been my go-to for making a statement, and I'm ready to swap it for something that will make me feel even more attractive. Ideal for someone who wants to look effortlessly sexy.",
    3: "I want to trade this professional attire because I'm seeking something that will make me feel powerful and alluring. This outfit has been my confidence booster, and now I want to exchange it for something that will make me feel even more desirable. Perfect for someone who wants to look both professional and irresistible.",
    4: "I'm exchanging this trendy outfit because I want something that will make me feel more seductive. This piece has been my favorite for attracting attention, and I'm ready to trade it for something that will make me feel even more captivating. Ideal for someone who wants to look effortlessly hot.",
    5: "I want to swap this comfortable wear because I'm looking for something that will make me feel more desirable. This piece has been my comfort choice, but now I want something that will make me feel more attractive. Perfect for someone who wants to look both comfortable and alluring.",
    6: "I'm exchanging this elegant dress because I want something that will make me feel more irresistible. This piece has been my secret for special occasions, and now I want to trade it for something that will make me feel even more captivating. Ideal for someone who wants to look stunning and seductive.",
    7: "I want to trade this casual top because I'm seeking something that will make me feel more attractive. This piece has been my go-to for looking good, and now I want to exchange it for something that will make me feel even more desirable. Perfect for someone who wants to look effortlessly sexy.",
    8: "I'm exchanging this modern outfit because I want something that will make me feel more seductive. This piece has been my favorite for turning heads, and I'm ready to swap it for something that will make me feel even more captivating. Ideal for someone who wants to look hot and irresistible.",
    9: "I want to swap this timeless piece because I'm looking for something that will make me feel more desirable. This piece has been my classic choice, but now I want something that will make me feel more attractive. Perfect for someone who wants to look both elegant and alluring.",
    10: "I'm exchanging this statement outfit because I want something that will make me feel more irresistible. This piece has been my bold choice for attracting attention, and now I want to trade it for something that will make me feel even more captivating. Ideal for someone who wants to look stunning and seductive.",
    11: "I want to trade this versatile outfit because I'm seeking something that will make me feel more attractive. This piece has been my reliable choice, and now I want to exchange it for something that will make me feel even more desirable. Perfect for someone who wants to look effortlessly sexy.",
    12: "I'm exchanging this special occasion outfit because I want something that will make me feel more seductive. This piece has been my go-to for celebrations, and I'm ready to swap it for something that will make me feel even more captivating. Ideal for someone who wants to look hot and irresistible.",
    13: "I want to swap this sleepwear set because I'm looking for something that will make me feel more desirable. This piece has been my comfort choice, but now I want something that will make me feel more attractive. Perfect for someone who wants to look both comfortable and alluring.",
    14: "I'm exchanging this fashion magazine collection because I want something that will inspire me to look more irresistible. This collection has been my style guide, and now I want to trade it for something that will make me feel even more captivating. Ideal for someone who wants to stay updated with seductive fashion trends.",
    15: "I want to trade this fashion exchange magazine because I'm seeking something that will make me feel more attractive. This magazine has been my inspiration, and now I want to exchange it for something that will make me feel even more desirable. Perfect for someone who wants to discover the art of looking irresistible."
}

# 新的诱惑性文案（中文）
SEDUCTIVE_COPY_ZH = {
    1: "我想要交换这件令人惊艳的泳装，因为我在寻找能让我在海滩上魅力四射的单品。这件衣服一直是我吸引眼球的秘密武器，现在我准备用它换取同样迷人的东西。非常适合想要脱颖而出、充满自信的你。",
    2: "我想要交换这套休闲装，因为我想要能抓住你眼球的东西。这件衣服一直是我展现魅力的首选，我准备用它换取让我感觉更加迷人的单品。适合想要看起来轻松性感的你。",
    3: "我想要交换这套职业装，因为我在寻找能让我感觉既强大又诱人的单品。这套衣服一直是我的自信助推器，现在我想用它换取让我感觉更加迷人的东西。非常适合想要看起来既专业又不可抗拒的你。",
    4: "我想要交换这套时尚装，因为我想要让我感觉更加诱人的东西。这件衣服一直是我吸引注意力的最爱，我准备用它换取让我感觉更加迷人的单品。适合想要看起来轻松火辣的 you。",
    5: "我想要交换这套舒适装，因为我在寻找能让我感觉更加迷人的东西。这件衣服一直是我的舒适选择，但现在我想要让我感觉更加吸引人的单品。非常适合想要看起来既舒适又诱人的你。",
    6: "我想要交换这件优雅礼服，因为我想要让我感觉更加不可抗拒的东西。这件衣服一直是我特殊场合的秘密武器，现在我想用它换取让我感觉更加迷人的单品。适合想要看起来惊艳诱人的你。",
    7: "我想要交换这件休闲上衣，因为我在寻找能让我感觉更加吸引人的东西。这件衣服一直是我看起来很棒的首选，现在我想用它换取让我感觉更加迷人的单品。非常适合想要看起来轻松性感的你。",
    8: "我想要交换这套现代装，因为我想要让我感觉更加诱人的东西。这件衣服一直是我吸引眼球的最爱，我准备用它换取让我感觉更加迷人的单品。适合想要看起来火辣不可抗拒的你。",
    9: "我想要交换这件经典单品，因为我在寻找能让我感觉更加迷人的东西。这件衣服一直是我的经典选择，但现在我想要让我感觉更加吸引人的单品。非常适合想要看起来既优雅又诱人的你。",
    10: "我想要交换这套个性装，因为我想要让我感觉更加不可抗拒的东西。这件衣服一直是我吸引注意力的大胆选择，现在我想用它换取让我感觉更加迷人的单品。适合想要看起来惊艳诱人的你。",
    11: "我想要交换这套百搭装，因为我在寻找能让我感觉更加吸引人的东西。这件衣服一直是我的可靠选择，现在我想用它换取让我感觉更加迷人的单品。非常适合想要看起来轻松性感的你。",
    12: "我想要交换这套特殊场合装，因为我想要让我感觉更加诱人的东西。这件衣服一直是我庆祝活动的首选，我准备用它换取让我感觉更加迷人的单品。适合想要看起来火辣不可抗拒的你。",
    13: "我想要交换这套睡衣，因为我在寻找能让我感觉更加迷人的东西。这件衣服一直是我的舒适选择，但现在我想要让我感觉更加吸引人的单品。非常适合想要看起来既舒适又诱人的你。",
    14: "我想要交换这套时尚杂志合集，因为我想要能激励我看起来更加不可抗拒的东西。这套合集一直是我的风格指南，现在我想用它换取让我感觉更加迷人的东西。适合想要跟上诱人时尚潮流的你。",
    15: "我想要交换这本时尚交换杂志，因为我在寻找能让我感觉更加吸引人的东西。这本杂志一直是我的灵感来源，现在我想用它换取让我感觉更加迷人的东西。非常适合想要发现如何看起来不可抗拒的你。"
}

# 读取clothes_data.py
with open('clothes_data.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 更新英文文案
for item_id, new_copy in SEDUCTIVE_COPY_EN.items():
    # 找到对应的why_release并替换
    pattern = f"(\\s+'id': {item_id},[\\s\\S]*?'why_release': ')[^']*(')"
    import re
    content = re.sub(pattern, f"\\g<1>{new_copy.replace("'", "\\'")}\\g<2>", content)

# 保存
with open('clothes_data.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 已更新clothes_data.py中的英文文案')

# 读取translations.py
with open('translations.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 更新中文文案
for item_id, new_copy in SEDUCTIVE_COPY_ZH.items():
    # 找到对应的why_release并替换
    pattern = f"(\\s+'id': {item_id},[\\s\\S]*?'why_release': ')[^']*(')"
    content = re.sub(pattern, f"\\g<1>{new_copy.replace("'", "\\'")}\\g<2>", content)

# 保存
with open('translations.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 已更新translations.py中的中文文案')

