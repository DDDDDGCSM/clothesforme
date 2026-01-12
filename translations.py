#!/usr/bin/env python3
"""
多语言翻译数据
支持阿拉伯语（默认）和中文
"""

# 阿拉伯语翻译（默认）
AR_TRANSLATIONS = {
    'site_title': 'Trueque Digital - تبادل الملابس',
    'site_subtitle': 'تبادل الملابس، شارك القصص، ابني المجتمع',
    'exchange_clothes': 'تبادل الملابس',
    'share_stories': 'شارك القصص',
    'build_community': 'ابني المجتمع',
    'request_exchange': 'طلب التبادل',
    'why_sharing': 'لماذا أشارك هذا',
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
    'site_subtitle': '交换衣服，分享故事，建立社区',
    'exchange_clothes': '交换衣服',
    'share_stories': '分享故事',
    'build_community': '建立社区',
    'request_exchange': '申请交换',
    'why_sharing': '为什么分享这件衣服',
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
        'why_release': '这件漂亮的泳装非常适合在迪拜的海滩日和泳池派对。时尚的设计和舒适的剪裁让我感到自信和优雅。我选择分享它是因为我找到了新的最爱风格，但我知道它会给其他人带来同样的快乐。非常适合海滩度假、泳池派对或任何水上活动。',
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
        'why_release': '这套舒适时尚的休闲装非常适合迪拜的温暖天气。轻质面料透气性好，非常适合购物或休闲早午餐。我选择传递它是因为我找到了新的最爱风格，但这件衣服值得被其他人穿着和喜爱。',
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
        'why_release': '这套专业装帮助我获得了梦想工作的面试机会。经典的设计和完美的剪裁给了我所需的自信。现在我已经建立了我的职业衣橱，我想把这件幸运的衣服传递给需要同样自信提升的人。非常适合面试、会议或任何专业场合。',
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
        'why_release': '这套时尚装是我周末外出的标志性单品。它总是获得赞美，让我感觉时尚。我分享它是因为时尚应该被分享，其他人也应该感受到我穿着它时的时尚感。',
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
        'why_release': '这套舒适的居家服一直是我懒散周末和在家工作日的舒适伴侣。柔软的面料感觉像拥抱，非常适合在家放松或跑腿。我选择分享它是因为我有太多类似的单品，但我知道它会给其他人带来舒适。',
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
        'why_release': '这件美丽的正式礼服陪伴我度过了许多庆祝活动。优雅的设计和讨人喜欢的剪裁让我在每次活动中都感觉像公主。我分享它是因为我相信每个女人都应该感到美丽，这件礼服有那种魔力。',
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
        'why_release': '这件多功能上衣一直是衣橱必备品。它与所有东西都很搭配，总是看起来很整洁。我选择传递它是因为我想为新单品腾出空间，但这件上衣值得继续成为某人的首选单品。',
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
        'why_release': '这套现代装代表了我进入当代时尚的旅程。它多功能、舒适，总是让我感到自信。我分享它是因为时尚是关于表达自己，我希望其他人也能体验到同样的感觉。',
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
        'why_release': '这件永恒的单品在我的衣橱里已经很多年了，因为它永远不会过时。经典的设计适用于任何场合。我选择分享它来腾出空间，但我知道它会为其他人服务得和我一样好。',
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
        'why_release': '这套大胆的装束帮助我走出舒适区，拥抱我独特的风格。它总是引人注目，让我感觉像在走时尚T台。我分享它是因为我希望其他人也能体验到那种自信提升。',
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
        'why_release': '这套多功能装一直是我无数天的可靠选择。它适用于工作、休闲外出以及介于两者之间的一切。我选择传递它是因为我相信可持续时尚，希望这件单品能继续与新的人一起继续它的旅程。',
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
        'why_release': '这套优雅的装束一直是我特殊庆祝活动的选择。美丽的设计和完美的合身让每个场合都令人难忘。我分享它是因为我希望其他人穿着这件单品创造他们自己美丽的回忆。',
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
        'why_release': '这套舒适的睡衣一直是我宁静夜晚的舒适伴侣。柔软、透气的面料感觉奢华。我分享它是因为我相信每个人都应该在舒适的服装中享受良好的睡眠，这套睡衣正是如此。',
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
        'why_release': '这套时尚杂志多年来一直是我的灵感来源。充满了风格提示、趋势和美丽的摄影。我分享它是因为知识和灵感应该被分享。非常适合任何希望了解中东时尚趋势的人。',
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
        'why_release': '这本特别版杂志全部关于可持续时尚和衣服交换。它让我看到了循环时尚的重要性。我分享它是因为我希望其他人发现交换衣服和建立可持续衣橱的快乐。',
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

