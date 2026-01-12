#!/usr/bin/env python3
"""
多语言翻译数据
支持阿拉伯语（默认）和中文
"""

# 阿拉伯语翻译（默认）
AR_TRANSLATIONS = {
    'site_title': 'Trueque Digital - تبادل الملابس',
    'site_subtitle': 'هنا يمكنك تبادل أي شيء تريده',
    'exchange_clothes': 'تبادل الملابس',
    'share_stories': 'شارك القصص',
    'build_community': 'ابني المجتمع',
    'request_exchange': 'طلب التبادل',
    'why_sharing': 'لماذا أريد تبادل هذا',
    'completed_exchanges': 'التبادلات المكتملة',
    'send_request': 'إرسال الطلب',
    'request_sent': 'تم إرسال الطلب بنجاح!',
    'contact_owner': 'اتصل بصاحب العنصر',
    'share': 'مشاركة',
    'items': 'عناصر',
    'item': 'عنصر',
    'by': 'بواسطة',
    'trusted_member': 'عضو موثوق',
    'new_member': 'عضو جديد',
    'request_sent_success': 'تم إرسال الطلب! سنخطرك عندما يرد المستخدم.',
    'write_story': 'اكتب هنا لماذا تريد هذا العنصر وما العنصر الذي تريد تبادله...',
    'upload_photo': 'اضغط لرفع صورة',
    'whatsapp_number': '+971 50 921 6685',
    'language_switcher': 'English',
    'language_switcher_url': '/en'
}

# 中文翻译
ZH_TRANSLATIONS = {
    'site_title': 'Trueque Digital - 衣服交换',
    'site_subtitle': '你在这里可以换你想换的任何东西',
    'exchange_clothes': '交换衣服',
    'share_stories': '分享故事',
    'build_community': '建立社区',
    'request_exchange': '申请交换',
    'why_sharing': '我想要交换的原因',
    'completed_exchanges': '已完成的交换',
    'send_request': '发送申请',
    'request_sent': '申请已成功发送！',
    'contact_owner': '联系物品主人',
    'share': '分享',
    'items': '件',
    'item': '件',
    'by': '来自',
    'trusted_member': '⭐ 可信成员',
    'new_member': '🌙 新成员',
    'request_sent_success': '✅ 申请已发送！用户回复时我们会通知您。',
    'write_story': '请写下您为什么想要这件物品，以及您想交换的物品...',
    'upload_photo': '点击上传照片',
    'whatsapp_number': '+971 50 921 6685',
    'language_switcher': 'العربية',
    'language_switcher_url': '/'
}

# 衣服数据的中文翻译
CLOTHES_DATA_ZH = [
    {
        'id': 1,
        'title': '时尚泳装',
        'category': '泳装',
        'cover': '/static/clothes-middle-east/item1.png',
        'condition': '几乎全新',
        'size': 'M',
        'why_release': '我想要交换这件令人惊艳的泳装，因为我在寻找能让我在海滩上魅力四射的单品。这件衣服一直是我吸引眼球的秘密武器，现在我准备用它换取同样迷人的东西。非常适合想要脱颖而出、充满自信的你。',
        'user': {
            'name': 'Fatima Al-Mansoori',
            'avatar': 'https://i.pravatar.cc/150?img=1',
            'trust_level': 'trusted',
            'trust_badge': '⭐ 可信成员'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 2,
        'title': '休闲夏季套装',
        'category': '休闲',
        'cover': '/static/clothes-middle-east/item2.png',
        'condition': '优秀',
        'size': 'S',
        'why_release': '我想要交换这套休闲装，因为我想要能抓住你眼球的东西。这件衣服一直是我展现魅力的首选，我准备用它换取让我感觉更加迷人的单品。适合想要看起来轻松性感的你。',
        'user': {
            'name': 'Layla Hassan',
            'avatar': 'https://i.pravatar.cc/150?img=5',
            'trust_level': 'new',
            'trust_badge': '🌙 新成员'
        },
        'has_story': True,
        'verified': False
    },
    {
        'id': 3,
        'title': '专业商务装',
        'category': '商务',
        'cover': '/static/clothes-middle-east/item3.png',
        'condition': '几乎全新',
        'size': 'L',
        'why_release': '我想要交换这套职业装，因为我在寻找能让我感觉既强大又诱人的单品。这套衣服一直是我的自信助推器，现在我想用它换取让我感觉更加迷人的东西。非常适合想要看起来既专业又不可抗拒的你。',
        'user': {
            'name': 'Noor Al-Zahra',
            'avatar': 'https://i.pravatar.cc/150?img=9',
            'trust_level': 'trusted',
            'trust_badge': '⭐ 可信成员'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 4,
        'title': '时尚街头风格',
        'category': '休闲',
        'cover': '/static/clothes-middle-east/item4.png',
        'condition': '良好',
        'size': 'M',
        'why_release': '我想要交换这套时尚装，因为我想要让我感觉更加诱人的东西。这件衣服一直是我吸引注意力的最爱，我准备用它换取让我感觉更加迷人的单品。适合想要看起来轻松火辣的 you。',
        'user': {
            'name': 'Aisha Mohammed',
            'avatar': 'https://i.pravatar.cc/150?img=12',
            'trust_level': 'trusted',
            'trust_badge': '⭐ 可信成员'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 5,
        'title': '舒适居家服',
        'category': '休闲',
        'cover': '/static/clothes-middle-east/item5.png',
        'condition': '优秀',
        'size': 'S',
        'why_release': '我想要交换这套舒适装，因为我在寻找能让我感觉更加迷人的东西。这件衣服一直是我的舒适选择，但现在我想要让我感觉更加吸引人的单品。非常适合想要看起来既舒适又诱人的你。',
        'user': {
            'name': 'Mariam Al-Rashid',
            'avatar': 'https://i.pravatar.cc/150?img=15',
            'trust_level': 'new',
            'trust_badge': '🌙 新成员'
        },
        'has_story': True,
        'verified': False
    },
    {
        'id': 6,
        'title': '优雅正式礼服',
        'category': '礼服',
        'cover': '/static/clothes-middle-east/item6.png',
        'condition': '几乎全新',
        'size': 'M',
        'why_release': '我想要交换这件优雅礼服，因为我想要让我感觉更加不可抗拒的东西。这件衣服一直是我特殊场合的秘密武器，现在我想用它换取让我感觉更加迷人的单品。适合想要看起来惊艳诱人的你。',
        'user': {
            'name': 'Zainab Al-Khalifa',
            'avatar': 'https://i.pravatar.cc/150?img=20',
            'trust_level': 'trusted',
            'trust_badge': '⭐ 可信成员'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 7,
        'title': '时尚休闲上衣',
        'category': '休闲',
        'cover': '/static/clothes-middle-east/item7.png',
        'condition': '良好',
        'size': 'L',
        'why_release': '我想要交换这件休闲上衣，因为我在寻找能让我感觉更加吸引人的东西。这件衣服一直是我看起来很棒的首选，现在我想用它换取让我感觉更加迷人的单品。非常适合想要看起来轻松性感的你。',
        'user': {
            'name': 'Sara Al-Mazrouei',
            'avatar': 'https://i.pravatar.cc/150?img=25',
            'trust_level': 'new',
            'trust_badge': '🌙 新成员'
        },
        'has_story': False,
        'verified': False
    },
    {
        'id': 8,
        'title': '时尚现代套装',
        'category': '休闲',
        'cover': '/static/clothes-middle-east/item8.png',
        'condition': '优秀',
        'size': 'M',
        'why_release': '我想要交换这套现代装，因为我想要让我感觉更加诱人的东西。这件衣服一直是我吸引眼球的最爱，我准备用它换取让我感觉更加迷人的单品。适合想要看起来火辣不可抗拒的你。',
        'user': {
            'name': 'Hala Al-Dhaheri',
            'avatar': 'https://i.pravatar.cc/150?img=30',
            'trust_level': 'trusted',
            'trust_badge': '⭐ 可信成员'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 9,
        'title': '经典永恒单品',
        'category': '休闲',
        'cover': '/static/clothes-middle-east/item9.png',
        'condition': '几乎全新',
        'size': 'S',
        'why_release': '我想要交换这件经典单品，因为我在寻找能让我感觉更加迷人的东西。这件衣服一直是我的经典选择，但现在我想要让我感觉更加吸引人的单品。非常适合想要看起来既优雅又诱人的你。',
        'user': {
            'name': 'Amira Al-Suwaidi',
            'avatar': 'https://i.pravatar.cc/150?img=35',
            'trust_level': 'trusted',
            'trust_badge': '⭐ 可信成员'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 10,
        'title': '时尚前卫宣言装',
        'category': '休闲',
        'cover': '/static/clothes-middle-east/item10.png',
        'condition': '优秀',
        'size': 'L',
        'why_release': '我想要交换这套个性装，因为我想要让我感觉更加不可抗拒的东西。这件衣服一直是我吸引注意力的大胆选择，现在我想用它换取让我感觉更加迷人的单品。适合想要看起来惊艳诱人的你。',
        'user': {
            'name': 'Yasmin Al-Qasimi',
            'avatar': 'https://i.pravatar.cc/150?img=40',
            'trust_level': 'new',
            'trust_badge': '🌙 新成员'
        },
        'has_story': True,
        'verified': False
    },
    {
        'id': 11,
        'title': '多功能日常装',
        'category': '休闲',
        'cover': '/static/clothes-middle-east/item11.png',
        'condition': '良好',
        'size': 'M',
        'why_release': '我想要交换这套百搭装，因为我在寻找能让我感觉更加吸引人的东西。这件衣服一直是我的可靠选择，现在我想用它换取让我感觉更加迷人的单品。非常适合想要看起来轻松性感的你。',
        'user': {
            'name': 'Rania Al-Nuaimi',
            'avatar': 'https://i.pravatar.cc/150?img=45',
            'trust_level': 'trusted',
            'trust_badge': '⭐ 可信成员'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 12,
        'title': '优雅特殊场合装',
        'category': '礼服',
        'cover': '/static/clothes-middle-east/item12.png',
        'condition': '几乎全新',
        'size': 'S',
        'why_release': '我想要交换这套特殊场合装，因为我想要让我感觉更加诱人的东西。这件衣服一直是我庆祝活动的首选，我准备用它换取让我感觉更加迷人的单品。适合想要看起来火辣不可抗拒的你。',
        'user': {
            'name': 'Lina Al-Mazrouei',
            'avatar': 'https://i.pravatar.cc/150?img=50',
            'trust_level': 'trusted',
            'trust_badge': '⭐ 可信成员'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 13,
        'title': '舒适睡衣套装',
        'category': '睡衣',
        'cover': '/static/clothes-middle-east/sleepwear.png',
        'condition': '优秀',
        'size': 'M',
        'why_release': '我想要交换这套睡衣，因为我在寻找能让我感觉更加迷人的东西。这件衣服一直是我的舒适选择，但现在我想要让我感觉更加吸引人的单品。非常适合想要看起来既舒适又诱人的你。',
        'user': {
            'name': 'Nadia Al-Hosani',
            'avatar': 'https://i.pravatar.cc/150?img=55',
            'trust_level': 'trusted',
            'trust_badge': '⭐ 可信成员'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 14,
        'title': '时尚杂志合集',
        'category': '杂志',
        'cover': '/static/clothes-middle-east/magazine1.png',
        'condition': '几乎全新',
        'size': 'N/A',
        'why_release': '我想要交换这套时尚杂志合集，因为我想要能激励我看起来更加不可抗拒的东西。这套合集一直是我的风格指南，现在我想用它换取让我感觉更加迷人的东西。适合想要跟上诱人时尚潮流的你。',
        'user': {
            'name': 'Dina Al-Kaabi',
            'avatar': 'https://i.pravatar.cc/150?img=60',
            'trust_level': 'trusted',
            'trust_badge': '⭐ 可信成员'
        },
        'has_story': True,
        'verified': True
    },
    {
        'id': 15,
        'title': '时尚交换杂志',
        'category': '杂志',
        'cover': '/static/clothes-middle-east/magazine2.png',
        'condition': '优秀',
        'size': 'N/A',
        'why_release': '我想要交换这本时尚交换杂志，因为我在寻找能让我感觉更加吸引人的东西。这本杂志一直是我的灵感来源，现在我想用它换取让我感觉更加迷人的东西。非常适合想要发现如何看起来不可抗拒的你。',
        'user': {
            'name': 'Salma Al-Mansoori',
            'avatar': 'https://i.pravatar.cc/150?img=65',
            'trust_level': 'trusted',
            'trust_badge': '⭐ 可信成员'
        },
        'has_story': True,
        'verified': True
    }
]

