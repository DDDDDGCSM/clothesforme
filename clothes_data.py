#!/usr/bin/env python3
"""
中东衣服交换平台 - 衣服数据
包含所有衣服的推销文案
"""

# 衣服数据（15件）
CLOTHES_DATA = [
    {
        'id': 1,
        'title': 'Stylish Swimsuit',
        'category': 'Swimwear',
        'cover': '/static/clothes-middle-east/item1.png',
        'condition': 'Like New',
        'size': 'M',
        'why_release': 'I want to exchange this stunning swimsuit because I\'m looking for something that will make me feel irresistible at the beach. This piece has been my secret weapon for turning heads, and now I\'m ready to trade it for something equally captivating. Perfect for someone who wants to stand out and feel confident.',
        'user': {
            'name': 'Fatima Al-Mansoori',
            'avatar': 'https://i.pravatar.cc/150?img=1',
            'trust_level': 'trusted',
            'trust_badge': '⭐ Trusted Member'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 2,
        'title': 'Casual Summer Outfit',
        'category': 'Casual',
        'cover': '/static/clothes-middle-east/item2.png',
        'condition': 'Excellent',
        'size': 'S',
        'why_release': 'I\'m exchanging this casual outfit because I want something that will catch your eye. This piece has been my go-to for making a statement, and I\'m ready to swap it for something that will make me feel even more attractive. Ideal for someone who wants to look effortlessly sexy.',
        'user': {
            'name': 'Layla Hassan',
            'avatar': 'https://i.pravatar.cc/150?img=5',
            'trust_level': 'new',
            'trust_badge': '🌙 New Member'
        },
        'has_story': True,
        'verified': False
    },
    {
        'id': 3,
        'title': 'Professional Business Attire',
        'category': 'Business',
        'cover': '/static/clothes-middle-east/item3.png',
        'condition': 'Like New',
        'size': 'L',
        'why_release': 'I want to trade this professional attire because I\'m seeking something that will make me feel powerful and alluring. This outfit has been my confidence booster, and now I want to exchange it for something that will make me feel even more desirable. Perfect for someone who wants to look both professional and irresistible.',
        'user': {
            'name': 'Noor Al-Zahra',
            'avatar': 'https://i.pravatar.cc/150?img=9',
            'trust_level': 'trusted',
            'trust_badge': '⭐ Trusted Member'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 4,
        'title': 'Trendy Street Style Outfit',
        'category': 'Casual',
        'cover': '/static/clothes-middle-east/item4.png',
        'condition': 'Good',
        'size': 'M',
        'why_release': 'I\'m exchanging this trendy outfit because I want something that will make me feel more seductive. This piece has been my favorite for attracting attention, and I\'m ready to trade it for something that will make me feel even more captivating. Ideal for someone who wants to look effortlessly hot.',
        'user': {
            'name': 'Aisha Mohammed',
            'avatar': 'https://i.pravatar.cc/150?img=12',
            'trust_level': 'trusted',
            'trust_badge': '⭐ Trusted Member'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 5,
        'title': 'Comfortable Home Wear',
        'category': 'Casual',
        'cover': '/static/clothes-middle-east/item5.png',
        'condition': 'Excellent',
        'size': 'S',
        'why_release': 'I want to swap this comfortable wear because I\'m looking for something that will make me feel more desirable. This piece has been my comfort choice, but now I want something that will make me feel more attractive. Perfect for someone who wants to look both comfortable and alluring.',
        'user': {
            'name': 'Mariam Al-Rashid',
            'avatar': 'https://i.pravatar.cc/150?img=15',
            'trust_level': 'new',
            'trust_badge': '🌙 New Member'
        },
        'has_story': True,
        'verified': False
    },
    {
        'id': 6,
        'title': 'Elegant Formal Dress',
        'category': 'Dress',
        'cover': '/static/clothes-middle-east/item6.png',
        'condition': 'Like New',
        'size': 'M',
        'why_release': 'I\'m exchanging this elegant dress because I want something that will make me feel more irresistible. This piece has been my secret for special occasions, and now I want to trade it for something that will make me feel even more captivating. Ideal for someone who wants to look stunning and seductive.',
        'user': {
            'name': 'Zainab Al-Khalifa',
            'avatar': 'https://i.pravatar.cc/150?img=20',
            'trust_level': 'trusted',
            'trust_badge': '⭐ Trusted Member'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 7,
        'title': 'Stylish Casual Top',
        'category': 'Casual',
        'cover': '/static/clothes-middle-east/item7.png',
        'condition': 'Good',
        'size': 'L',
        'why_release': 'I want to trade this casual top because I\'m seeking something that will make me feel more attractive. This piece has been my go-to for looking good, and now I want to exchange it for something that will make me feel even more desirable. Perfect for someone who wants to look effortlessly sexy.',
        'user': {
            'name': 'Sara Al-Mazrouei',
            'avatar': 'https://i.pravatar.cc/150?img=25',
            'trust_level': 'new',
            'trust_badge': '🌙 New Member'
        },
        'has_story': False,
        'verified': False
    },
    {
        'id': 8,
        'title': 'Chic Modern Outfit',
        'category': 'Casual',
        'cover': '/static/clothes-middle-east/item8.png',
        'condition': 'Excellent',
        'size': 'M',
        'why_release': 'I\'m exchanging this modern outfit because I want something that will make me feel more seductive. This piece has been my favorite for turning heads, and I\'m ready to swap it for something that will make me feel even more captivating. Ideal for someone who wants to look hot and irresistible.',
        'user': {
            'name': 'Hala Al-Dhaheri',
            'avatar': 'https://i.pravatar.cc/150?img=30',
            'trust_level': 'trusted',
            'trust_badge': '⭐ Trusted Member'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 9,
        'title': 'Classic Timeless Piece',
        'category': 'Casual',
        'cover': '/static/clothes-middle-east/item9.png',
        'condition': 'Like New',
        'size': 'S',
        'why_release': 'I want to swap this timeless piece because I\'m looking for something that will make me feel more desirable. This piece has been my classic choice, but now I want something that will make me feel more attractive. Perfect for someone who wants to look both elegant and alluring.',
        'user': {
            'name': 'Amira Al-Suwaidi',
            'avatar': 'https://i.pravatar.cc/150?img=35',
            'trust_level': 'trusted',
            'trust_badge': '⭐ Trusted Member'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 10,
        'title': 'Fashion-Forward Statement Outfit',
        'category': 'Casual',
        'cover': '/static/clothes-middle-east/item10.png',
        'condition': 'Excellent',
        'size': 'L',
        'why_release': 'I\'m exchanging this statement outfit because I want something that will make me feel more irresistible. This piece has been my bold choice for attracting attention, and now I want to trade it for something that will make me feel even more captivating. Ideal for someone who wants to look stunning and seductive.',
        'user': {
            'name': 'Yasmin Al-Qasimi',
            'avatar': 'https://i.pravatar.cc/150?img=40',
            'trust_level': 'new',
            'trust_badge': '🌙 New Member'
        },
        'has_story': True,
        'verified': False
    },
    {
        'id': 11,
        'title': 'Versatile Everyday Outfit',
        'category': 'Casual',
        'cover': '/static/clothes-middle-east/item11.png',
        'condition': 'Good',
        'size': 'M',
        'why_release': 'I want to trade this versatile outfit because I\'m seeking something that will make me feel more attractive. This piece has been my reliable choice, and now I want to exchange it for something that will make me feel even more desirable. Perfect for someone who wants to look effortlessly sexy.',
        'user': {
            'name': 'Rania Al-Nuaimi',
            'avatar': 'https://i.pravatar.cc/150?img=45',
            'trust_level': 'trusted',
            'trust_badge': '⭐ Trusted Member'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 12,
        'title': 'Elegant Special Occasion Outfit',
        'category': 'Dress',
        'cover': '/static/clothes-middle-east/item12.png',
        'condition': 'Like New',
        'size': 'S',
        'why_release': 'I\'m exchanging this special occasion outfit because I want something that will make me feel more seductive. This piece has been my go-to for celebrations, and I\'m ready to swap it for something that will make me feel even more captivating. Ideal for someone who wants to look hot and irresistible.',
        'user': {
            'name': 'Lina Al-Mazrouei',
            'avatar': 'https://i.pravatar.cc/150?img=50',
            'trust_level': 'trusted',
            'trust_badge': '⭐ Trusted Member'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 13,
        'title': 'Comfortable Sleepwear Set',
        'category': 'Sleepwear',
        'cover': '/static/clothes-middle-east/sleepwear.png',
        'condition': 'Excellent',
        'size': 'M',
        'why_release': 'I want to swap this sleepwear set because I\'m looking for something that will make me feel more desirable. This piece has been my comfort choice, but now I want something that will make me feel more attractive. Perfect for someone who wants to look both comfortable and alluring.',
        'user': {
            'name': 'Nadia Al-Hosani',
            'avatar': 'https://i.pravatar.cc/150?img=55',
            'trust_level': 'trusted',
            'trust_badge': '⭐ Trusted Member'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 14,
        'title': 'Fashion Magazine Collection',
        'category': 'Magazine',
        'cover': '/static/clothes-middle-east/magazine1.png',
        'condition': 'Like New',
        'size': 'N/A',
        'why_release': 'I\'m exchanging this fashion magazine collection because I want something that will inspire me to look more irresistible. This collection has been my style guide, and now I want to trade it for something that will make me feel even more captivating. Ideal for someone who wants to stay updated with seductive fashion trends.',
        'user': {
            'name': 'Dina Al-Kaabi',
            'avatar': 'https://i.pravatar.cc/150?img=60',
            'trust_level': 'trusted',
            'trust_badge': '⭐ Trusted Member'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 15,
        'title': 'Fashion Exchange Magazine',
        'category': 'Magazine',
        'cover': '/static/clothes-middle-east/magazine2.png',
        'condition': 'Excellent',
        'size': 'N/A',
        'why_release': 'I want to trade this fashion exchange magazine because I\'m seeking something that will make me feel more attractive. This magazine has been my inspiration, and now I want to exchange it for something that will make me feel even more desirable. Perfect for someone who wants to discover the art of looking irresistible.',
        'user': {
            'name': 'Salma Al-Mansoori',
            'avatar': 'https://i.pravatar.cc/150?img=65',
            'trust_level': 'trusted',
            'trust_badge': '⭐ Trusted Member'
        },
        'has_story': True,
        'verified': True
    }
]

# 交换历史示例数据
SAMPLE_EXCHANGES = [
    {
        'id': 1,
        'date': '2025-01-08',
        'item1': {
            'title': 'Elegant Evening Dress',
            'cover': '/static/clothes-middle-east/item1.png',
            'user': 'Fatima'
        },
        'item2': {
            'title': 'Professional Business Attire',
            'cover': '/static/clothes-middle-east/item3.png',
            'user': 'Noor'
        },
        'message1': 'Thank you for this beautiful exchange! The dress is perfect.',
        'message2': 'So happy you love it! Enjoy your new professional look!'
    },
    {
        'id': 2,
        'date': '2025-01-05',
        'item1': {
            'title': 'Casual Summer Outfit',
            'cover': '/static/clothes-middle-east/item2.png',
            'user': 'Layla'
        },
        'item2': {
            'title': 'Comfortable Home Wear',
            'cover': '/static/clothes-middle-east/item5.png',
            'user': 'Mariam'
        },
        'message1': 'Perfect for Dubai weather! Thank you so much!',
        'message2': 'Glad it works for you! Enjoy your new casual style!'
    }
]

