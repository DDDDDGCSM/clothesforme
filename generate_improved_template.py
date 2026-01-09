#!/usr/bin/env python3
"""
生成改进的模板文件，支持多语言和更好的UI设计
"""
import json
from clothes_data import CLOTHES_DATA
from translations import AR_TRANSLATIONS, ZH_TRANSLATIONS, CLOTHES_DATA_ZH

def generate_template(lang='ar', translations=None, clothes_data=None):
    """生成模板HTML"""
    if lang == 'zh':
        dir_attr = 'ltr'
        lang_attr = 'zh-CN'
        is_rtl = False
    else:
        dir_attr = 'rtl'
        lang_attr = 'ar'
        is_rtl = True
    
    if translations is None:
        translations = AR_TRANSLATIONS
    if clothes_data is None:
        clothes_data = CLOTHES_DATA
    
    # 生成JavaScript数据
    js_data = json.dumps(clothes_data, ensure_ascii=False, indent=16)
    
    html = f'''<!DOCTYPE html>
<html lang="{lang_attr}" dir="{dir_attr}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{translations['site_title']}</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>👗</text></svg>">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans Arabic', 'PingFang SC', 'Microsoft YaHei', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #2C3E50;
            line-height: 1.6;
            padding-bottom: 100px;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px 15px;
        }}

        /* 语言切换器 */
        .lang-switcher {{
            position: fixed;
            top: 20px;
            {'right' if is_rtl else 'left'}: 20px;
            z-index: 1001;
            background: white;
            padding: 10px 15px;
            border-radius: 25px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            text-decoration: none;
            color: #667eea;
            font-weight: 600;
            font-size: 14px;
            transition: all 0.3s;
        }}

        .lang-switcher:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(0,0,0,0.2);
        }}

        /* 头部 */
        .header {{
            text-align: center;
            padding: 40px 20px;
            background: white;
            border-radius: 20px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        }}

        .header h1 {{
            font-size: 42px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 10px;
            font-weight: 700;
        }}

        .header p {{
            color: #6c757d;
            font-size: 18px;
            font-weight: 300;
        }}

        /* 衣服卡片 - 更吸引人的设计 */
        .clothes-card {{
            background: white;
            border-radius: 25px;
            padding: 0;
            margin-bottom: 30px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            overflow: hidden;
            position: relative;
            transition: transform 0.3s, box-shadow 0.3s;
        }}

        .clothes-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        }}

        .clothes-header {{
            display: flex;
            gap: 20px;
            padding: 25px;
            background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        }}

        .clothes-image-wrapper {{
            position: relative;
            flex-shrink: 0;
        }}

        .clothes-cover {{
            width: 150px;
            height: 200px;
            object-fit: cover;
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            transition: transform 0.3s;
        }}

        .clothes-card:hover .clothes-cover {{
            transform: scale(1.05);
        }}

        .clothes-info {{
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        .clothes-title {{
            font-size: 24px;
            font-weight: 700;
            color: #2C3E50;
            margin-bottom: 8px;
            line-height: 1.3;
        }}

        .clothes-category {{
            display: inline-block;
            padding: 6px 12px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            margin-bottom: 15px;
            width: fit-content;
        }}

        .user-info {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-top: auto;
            padding-top: 15px;
            border-top: 1px solid #e9ecef;
        }}

        .user-avatar {{
            width: 45px;
            height: 45px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid #667eea;
            flex-shrink: 0;
        }}

        .user-details {{
            flex: 1;
        }}

        .user-name {{
            font-size: 15px;
            font-weight: 600;
            color: #2C3E50;
            margin-bottom: 4px;
        }}

        .trust-badge {{
            font-size: 12px;
            padding: 4px 10px;
            border-radius: 15px;
            background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%);
            color: #2d3436;
            font-weight: 600;
            display: inline-block;
        }}

        .whatsapp-icon {{
            width: 40px;
            height: 40px;
            cursor: pointer;
            transition: all 0.3s;
            background: #25D366;
            border-radius: 50%;
            padding: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .whatsapp-icon:hover {{
            transform: scale(1.15);
            box-shadow: 0 4px 12px rgba(37, 211, 102, 0.4);
        }}

        .whatsapp-icon svg {{
            width: 24px;
            height: 24px;
            fill: white;
        }}

        .why-release {{
            background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
            padding: 25px;
            border-top: 3px solid #667eea;
            margin: 0;
        }}

        .why-release h4 {{
            font-size: 14px;
            color: #667eea;
            margin-bottom: 12px;
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 1px;
        }}

        .why-release p {{
            font-size: 15px;
            line-height: 1.8;
            color: #495057;
        }}

        /* 导航控制 */
        .nav-controls {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
            padding: 0 10px;
        }}

        .nav-arrow {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            width: 55px;
            height: 55px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 28px;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        }}

        .nav-arrow:hover:not(:disabled) {{
            transform: scale(1.1);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
        }}

        .nav-arrow:disabled {{
            background: #95a5a6;
            cursor: not-allowed;
            opacity: 0.5;
            box-shadow: none;
        }}

        .item-counter {{
            font-size: 18px;
            color: white;
            font-weight: 700;
            background: rgba(255,255,255,0.2);
            padding: 10px 20px;
            border-radius: 25px;
            backdrop-filter: blur(10px);
        }}

        /* 底部固定按钮 */
        .fixed-bottom-btn {{
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(10px);
            padding: 20px;
            box-shadow: 0 -4px 20px rgba(0,0,0,0.1);
            z-index: 1000;
        }}

        .request-btn {{
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 18px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 30px;
            font-size: 18px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s;
            display: block;
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        }}

        .request-btn:hover {{
            transform: translateY(-3px);
            box-shadow: 0 12px 35px rgba(102, 126, 234, 0.6);
        }}

        .share-btn {{
            position: absolute;
            top: 25px;
            {'left' if is_rtl else 'right'}: 25px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 25px;
            padding: 12px 20px;
            font-size: 14px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.3s;
            z-index: 10;
            font-weight: 600;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }}

        .share-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5);
        }}

        /* 模态框 */
        .modal {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(5px);
            z-index: 2000;
            overflow-y: auto;
            padding: 20px;
        }}

        .modal.active {{
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .modal-content {{
            background: white;
            border-radius: 25px;
            max-width: 550px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
            position: relative;
            padding: 35px 25px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }}

        .modal-close {{
            position: absolute;
            top: 20px;
            {'left' if is_rtl else 'right'}: 20px;
            background: #f8f9fa;
            border: none;
            font-size: 28px;
            cursor: pointer;
            color: #6c757d;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            transition: all 0.3s;
        }}

        .modal-close:hover {{
            background: #e9ecef;
            transform: rotate(90deg);
        }}

        .modal-title {{
            font-size: 28px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 25px;
            text-align: center;
            font-weight: 700;
        }}

        .form-group {{
            margin-bottom: 25px;
        }}

        .form-group label {{
            display: block;
            margin-bottom: 10px;
            font-weight: 600;
            color: #2C3E50;
            font-size: 15px;
        }}

        .form-group textarea {{
            width: 100%;
            min-height: 130px;
            padding: 15px;
            border: 2px solid #e9ecef;
            border-radius: 12px;
            font-family: inherit;
            font-size: 15px;
            resize: vertical;
            transition: all 0.3s;
        }}

        .form-group textarea:focus {{
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }}

        .image-upload-area {{
            border: 3px dashed #e9ecef;
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
            margin-bottom: 15px;
            background: #f8f9fa;
        }}

        .image-upload-area:hover {{
            border-color: #667eea;
            background: #f0f4ff;
        }}

        .image-upload-area.has-image {{
            border-style: solid;
            padding: 15px;
            background: white;
        }}

        .uploaded-image {{
            max-width: 100%;
            max-height: 250px;
            border-radius: 12px;
            margin-top: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}

        .upload-icon {{
            font-size: 48px;
            color: #667eea;
            margin-bottom: 15px;
        }}

        .whatsapp-display {{
            display: none;
            margin-top: 25px;
            padding: 20px;
            background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
            border-radius: 15px;
            text-align: center;
        }}

        .whatsapp-display.active {{
            display: block;
        }}

        .whatsapp-link {{
            display: inline-flex;
            align-items: center;
            gap: 10px;
            color: #25D366;
            text-decoration: none;
            font-weight: 700;
            font-size: 18px;
            margin-top: 15px;
            padding: 15px 25px;
            background: white;
            border-radius: 30px;
            transition: all 0.3s;
            box-shadow: 0 4px 15px rgba(37, 211, 102, 0.3);
        }}

        .whatsapp-link:hover {{
            background: #25D366;
            color: white;
            transform: scale(1.05);
            box-shadow: 0 6px 20px rgba(37, 211, 102, 0.5);
        }}

        .submit-btn {{
            width: 100%;
            padding: 18px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 30px;
            font-size: 18px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s;
            margin-top: 25px;
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        }}

        .submit-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 12px 35px rgba(102, 126, 234, 0.6);
        }}

        .submit-btn:disabled {{
            background: #95a5a6;
            cursor: not-allowed;
            box-shadow: none;
        }}

        .success-message {{
            display: none;
            margin-top: 25px;
            padding: 20px;
            background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
            border-radius: 15px;
            color: #155724;
            text-align: center;
            font-size: 15px;
            font-weight: 600;
        }}

        /* 历史交换区 */
        .history-section {{
            margin-top: 40px;
            background: white;
            border-radius: 25px;
            padding: 30px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        }}

        .history-section h2 {{
            font-size: 26px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 20px;
            text-align: center;
            font-weight: 700;
        }}

        .exchange-list {{
            display: flex;
            gap: 20px;
            overflow-x: auto;
            padding: 15px 0;
            scroll-snap-type: x mandatory;
            -webkit-overflow-scrolling: touch;
        }}

        .exchange-item {{
            display: flex;
            align-items: center;
            gap: 15px;
            padding: 20px;
            background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
            border-radius: 15px;
            min-width: 320px;
            flex-shrink: 0;
            scroll-snap-align: start;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        }}

        .exchange-clothes {{
            text-align: center;
            flex: 1;
        }}

        .exchange-clothes img {{
            width: 80px;
            height: 120px;
            object-fit: cover;
            border-radius: 10px;
            margin-bottom: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}

        .exchange-clothes p {{
            font-size: 12px;
            font-weight: 600;
            line-height: 1.3;
            color: #2C3E50;
        }}

        .exchange-icon {{
            font-size: 32px;
            color: #667eea;
        }}

        .exchange-date {{
            font-size: 12px;
            color: #6c757d;
            text-align: center;
            margin-top: 10px;
            font-weight: 500;
        }}

        /* 响应式设计 */
        @media (max-width: 768px) {{
            .container {{
                padding: 15px 10px;
            }}

            .header h1 {{
                font-size: 32px;
            }}

            .clothes-header {{
                flex-direction: column;
                align-items: center;
                text-align: center;
            }}

            .clothes-cover {{
                width: 180px;
                height: 240px;
            }}

            .share-btn {{
                position: static;
                width: 100%;
                margin-top: 15px;
            }}

            .exchange-item {{
                flex-direction: column;
                min-width: 280px;
            }}

            .lang-switcher {{
                top: 10px;
                {'right' if is_rtl else 'left'}: 10px;
                padding: 8px 12px;
                font-size: 12px;
            }}
        }}
    </style>
</head>
<body>
    <a href="{translations['language_switcher_url']}" class="lang-switcher">
        {translations['language_switcher']}
    </a>

    <div class="container">
        <!-- 头部 -->
        <div class="header">
            <h1>👗 {translations['site_title']}</h1>
            <p>{translations['site_subtitle']}</p>
        </div>

        <!-- 导航控制 -->
        <div class="nav-controls">
            <button class="nav-arrow" onclick="prevItem()" id="prevBtn">‹</button>
            <div class="item-counter">
                <span id="currentIndex">1</span> / <span id="totalItems">15</span>
            </div>
            <button class="nav-arrow" onclick="nextItem()" id="nextBtn">›</button>
        </div>

        <!-- 衣服展示 -->
        <div style="position: relative;">
            <div id="itemDisplay">
                <!-- 衣服卡片将在这里动态加载 -->
            </div>
            <!-- 分享按钮 -->
            <button class="share-btn" onclick="shareItem()">
                📤 {translations['share']}
            </button>
        </div>

        <!-- 历史交换区 -->
        <div class="history-section">
            <h2>🤝 {translations['completed_exchanges']}</h2>
            <div class="exchange-list" id="exchangeList">
                <!-- 交换记录将在这里动态加载 -->
            </div>
        </div>
    </div>

    <!-- 底部固定按钮 -->
    <div class="fixed-bottom-btn">
        <button class="request-btn" onclick="openModal()">
            👗 {translations['request_exchange']}
        </button>
    </div>

    <!-- 申请交换模态框 -->
    <div class="modal" id="exchangeModal">
        <div class="modal-content">
            <button class="modal-close" onclick="closeModal()">&times;</button>
            <h2 class="modal-title">{translations['request_exchange']}</h2>
            
            <div class="form-group">
                <label>{translations['why_sharing']}:</label>
                <textarea id="userStory" placeholder="{translations['write_story']}"></textarea>
            </div>

            <div class="form-group">
                <label>{translations['upload_photo']}:</label>
                <div class="image-upload-area" id="imageUploadArea" onclick="document.getElementById('itemImageInput').click()">
                    <div class="upload-icon">📷</div>
                    <p style="color: #6c757d; font-size: 15px;">{translations['upload_photo']}</p>
                    <img id="uploadedImagePreview" class="uploaded-image" style="display: none;">
                </div>
                <input type="file" id="itemImageInput" accept="image/*" style="display: none;" onchange="handleImageUpload(event)">
            </div>
            
            <div class="whatsapp-display" id="whatsappDisplay">
                <p style="color: #155724; font-weight: 700; margin-bottom: 10px; font-size: 16px;">{translations['request_sent']}</p>
                <p style="color: #6c757d; font-size: 14px;">{translations['contact_owner']}:</p>
                <a href="https://wa.me/{translations['whatsapp_number'].replace('+', '').replace(' ', '')}" target="_blank" class="whatsapp-link" id="whatsappLink" onclick="openWhatsApp(items[currentItemIndex].id); return true;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/>
                    </svg>
                    {translations['whatsapp_number']}
                </a>
            </div>

            <button class="submit-btn" onclick="submitExchange()" id="submitBtn">
                🤝 {translations['send_request']}
            </button>

            <div class="success-message" id="successMessage">
                ✅ {translations['request_sent_success']}
            </div>
        </div>
    </div>

    <script>
        // 衣服数据
        const items = {js_data};

        // 交换历史
        const exchanges = [
            {{
                item1: {{ title: items[0].title, cover: items[0].cover, user: items[0].user.name.split(' ')[0] }},
                item2: {{ title: items[2].title, cover: items[2].cover, user: items[2].user.name.split(' ')[0] }},
                date: '2025-01-08'
            }},
            {{
                item1: {{ title: items[1].title, cover: items[1].cover, user: items[1].user.name.split(' ')[0] }},
                item2: {{ title: items[4].title, cover: items[4].cover, user: items[4].user.name.split(' ')[0] }},
                date: '2025-01-05'
            }}
        ];

        let currentItemIndex = 0;
        let uploadedImage = null;
        let hasSubmittedExchange = false;
        let viewedItemsInSession = new Set();

        // 初始化
        function init() {{
            displayItem(0);
            displayExchanges();
            updateCounter();
            trackEvent('page_view', {{}});
        }}

        // 显示当前衣服
        function displayItem(index) {{
            if (index < 0 || index >= items.length) return;
            currentItemIndex = index;
            
            const item = items[index];
            const itemDisplay = document.getElementById('itemDisplay');
            
            if (item && item.id && !viewedItemsInSession.has(item.id)) {{
                trackEvent('item_view', {{ itemId: item.id }});
                viewedItemsInSession.add(item.id);
            }}

            itemDisplay.innerHTML = `
                <div class="clothes-card">
                    <div class="clothes-header">
                        <div class="clothes-image-wrapper">
                            <img src="${{encodeURI(item.cover)}}" alt="${{item.title}}" class="clothes-cover" loading="lazy" onerror="this.onerror=null; this.style.display='none';">
                        </div>
                        <div class="clothes-info">
                            <div>
                                <div class="clothes-title">${{item.title}}</div>
                                <span class="clothes-category">${{item.category}}</span>
                            </div>
                            <div class="user-info">
                                <img src="${{item.user.avatar}}" alt="${{item.user.name}}" class="user-avatar" onerror="this.onerror=null; this.src='data:image/svg+xml,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\'%3E%3Crect width=\\'45\\' height=\\'45\\' fill=\\'%23667eea\\'/%3E%3Ctext x=\\'50%25\\' y=\\'50%25\\' fill=\\'white\\' text-anchor=\\'middle\\' dominant-baseline=\\'central\\' font-size=\\'18\\' font-weight=\\'bold\\'>${{item.user.name.charAt(0)}}</text%3E%3C/svg%3E';">
                                <div class="user-details">
                                    <div class="user-name">${{item.user.name}}</div>
                                    <span class="trust-badge">${{item.user.trust_badge}}</span>
                                </div>
                                <div class="whatsapp-icon" onclick="openWhatsApp(${{item.id}})" title="Contact via WhatsApp">
                                    <svg viewBox="0 0 24 24" fill="currentColor">
                                        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/>
                                    </svg>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="why-release">
                        <h4>{translations['why_sharing']}</h4>
                        <p>${{item.why_release}}</p>
                    </div>
                </div>
            `;

            updateCounter();
            updateNavButtons();
        }}

        function updateCounter() {{
            document.getElementById('currentIndex').textContent = currentItemIndex + 1;
            document.getElementById('totalItems').textContent = items.length;
        }}

        function updateNavButtons() {{
            document.getElementById('prevBtn').disabled = false;
            document.getElementById('nextBtn').disabled = false;
        }}

        function prevItem() {{
            if (currentItemIndex > 0) {{
                displayItem(currentItemIndex - 1);
            }} else {{
                displayItem(items.length - 1);
            }}
        }}

        function nextItem() {{
            if (currentItemIndex < items.length - 1) {{
                displayItem(currentItemIndex + 1);
            }} else {{
                displayItem(0);
            }}
        }}

        function displayExchanges() {{
            const exchangeList = document.getElementById('exchangeList');
            exchangeList.innerHTML = exchanges.map(exchange => `
                <div style="min-width: 320px; flex-shrink: 0; scroll-snap-align: start;">
                    <div class="exchange-item">
                        <div class="exchange-clothes">
                            <img src="${{encodeURI(exchange.item1.cover)}}" alt="${{exchange.item1.title}}" loading="lazy" onerror="this.onerror=null; this.style.display='none';">
                            <p>${{exchange.item1.title}}</p>
                            <p style="font-size: 11px; color: #6c757d; margin-top: 5px;">${{exchange.item1.user}}</p>
                        </div>
                        <div class="exchange-icon">🤝</div>
                        <div class="exchange-clothes">
                            <img src="${{encodeURI(exchange.item2.cover)}}" alt="${{exchange.item2.title}}" loading="lazy" onerror="this.onerror=null; this.style.display='none';">
                            <p>${{exchange.item2.title}}</p>
                            <p style="font-size: 11px; color: #6c757d; margin-top: 5px;">${{exchange.item2.user}}</p>
                        </div>
                    </div>
                    <div class="exchange-date">${{exchange.date}}</div>
                </div>
            `).join('');
        }}

        function openModal() {{
            document.getElementById('exchangeModal').classList.add('active');
            document.body.style.overflow = 'hidden';
            document.getElementById('userStory').value = '';
            uploadedImage = null;
            document.getElementById('uploadedImagePreview').style.display = 'none';
            document.getElementById('imageUploadArea').classList.remove('has-image');
            document.getElementById('whatsappDisplay').classList.remove('active');
            document.getElementById('submitBtn').style.display = 'block';
        }}

        function closeModal() {{
            document.getElementById('exchangeModal').classList.remove('active');
            document.body.style.overflow = 'auto';
        }}

        function handleImageUpload(event) {{
            const file = event.target.files[0];
            if (file) {{
                const reader = new FileReader();
                reader.onload = function(e) {{
                    uploadedImage = e.target.result;
                    const preview = document.getElementById('uploadedImagePreview');
                    const uploadArea = document.getElementById('imageUploadArea');
                    preview.src = uploadedImage;
                    preview.style.display = 'block';
                    uploadArea.classList.add('has-image');
                    uploadArea.querySelector('.upload-icon').style.display = 'none';
                }};
                reader.readAsDataURL(file);
            }}
        }}

        function submitExchange() {{
            const story = document.getElementById('userStory').value.trim();
            if (!story || story.length < 20) {{
                alert('{translations["write_story"]}');
                return;
            }}
            if (!uploadedImage) {{
                alert('{translations["upload_photo"]}');
                return;
            }}
            hasSubmittedExchange = true;
            document.getElementById('whatsappDisplay').classList.add('active');
            document.getElementById('submitBtn').style.display = 'none';
            trackEvent('exchange_request', {{ itemId: items[currentItemIndex].id }});
        }}

        function openWhatsApp(itemId) {{
            const currentItem = items[currentItemIndex];
            trackEvent('whatsapp_click', {{ itemId: currentItem ? currentItem.id : itemId }});
            const message = encodeURIComponent(`Hello, I'm interested in exchanging this item: "${{currentItem ? currentItem.title : ''}}"`);
            window.open(`https://wa.me/{translations['whatsapp_number'].replace('+', '').replace(' ', '')}?text=${{message}}`, '_blank');
        }}

        function shareItem() {{
            const item = items[currentItemIndex];
            const shareText = `👗 ${{item.title}} – ${{item.category}}\\n\\n"${{item.why_release.substring(0, 110)}}..."\\n\\n🔥 Exchange clothes, share stories, build community!`;
            if (navigator.share) {{
                navigator.share({{ title: `👗 ${{item.title}}`, text: shareText, url: window.location.href }});
            }} else {{
                navigator.clipboard.writeText(shareText);
                alert('Text copied!');
            }}
            trackEvent('share', {{ itemId: item.id }});
        }}

        function trackEvent(eventType, payload) {{
            try {{
                const body = {{
                    event_type: eventType,
                    anon_id: localStorage.getItem('td_anon_id') || 'td_' + Math.random().toString(36).substring(2) + Date.now().toString(36),
                    book_id: payload.itemId || null,
                    extra: payload.extra || {{}}
                }};
                if (navigator.sendBeacon) {{
                    navigator.sendBeacon('/api/track', new Blob([JSON.stringify(body)], {{ type: 'application/json' }}));
                }} else {{
                    fetch('/api/track', {{ method: 'POST', headers: {{ 'Content-Type': 'application/json' }}, body: JSON.stringify(body), keepalive: true }});
                }}
            }} catch (e) {{
                console.warn('Tracking failed:', e);
            }}
        }}

        document.getElementById('exchangeModal').addEventListener('click', function(e) {{
            if (e.target === this) closeModal();
        }});

        document.addEventListener('keydown', function(e) {{
            if (e.key === 'Escape') closeModal();
        }});

        init();
    </script>
</body>
</html>'''
    
    return html

# 生成两个版本的模板
if __name__ == '__main__':
    # 阿拉伯语版本（默认）
    ar_html = generate_template('ar', AR_TRANSLATIONS, CLOTHES_DATA)
    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write(ar_html)
    print('✅ 已生成阿拉伯语版本模板')
    
    # 中文版本
    zh_html = generate_template('zh', ZH_TRANSLATIONS, CLOTHES_DATA_ZH)
    with open('templates/index_zh.html', 'w', encoding='utf-8') as f:
        f.write(zh_html)
    print('✅ 已生成中文版本模板')

