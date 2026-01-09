#!/usr/bin/env python3
"""
生成惊艳的UI模板 - 参考现代时尚电商网站
采用最吸引人的设计：大图展示、现代配色、流畅动画
"""
import json
from clothes_data import CLOTHES_DATA
from translations import AR_TRANSLATIONS, ZH_TRANSLATIONS, CLOTHES_DATA_ZH

def generate_template(lang='ar', translations=None, clothes_data=None):
    """生成惊艳的UI模板"""
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
    
    js_data = json.dumps(clothes_data, ensure_ascii=False, indent=16)
    
    html = f'''<!DOCTYPE html>
<html lang="{lang_attr}" dir="{dir_attr}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{translations['site_title']}</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>👗</text></svg>">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Cairo:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        :root {{
            --primary: #ff6b9d;
            --primary-dark: #ff4d7a;
            --primary-light: #ff8fb3;
            --secondary: #c44569;
            --accent: #f8b500;
            --success: #10b981;
            --text-primary: #1a1a1a;
            --text-secondary: #666;
            --bg-light: #fafafa;
            --white: #ffffff;
            --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.08);
            --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.12);
            --shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.16);
            --shadow-xl: 0 16px 64px rgba(0, 0, 0, 0.2);
        }}

        body {{
            font-family: 'Inter', 'Cairo', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #ffeef7 0%, #fff5f8 50%, #ffeef7 100%);
            min-height: 100vh;
            color: var(--text-primary);
            line-height: 1.6;
            padding-bottom: 100px;
            position: relative;
            overflow-x: hidden;
        }}

        /* 优雅的背景装饰 */
        body::before {{
            content: '';
            position: fixed;
            top: -200px;
            {'right' if is_rtl else 'left'}: -200px;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(255, 107, 157, 0.1) 0%, transparent 70%);
            border-radius: 50%;
            pointer-events: none;
            z-index: 0;
            animation: float 20s ease-in-out infinite;
        }}

        body::after {{
            content: '';
            position: fixed;
            bottom: -200px;
            {'left' if is_rtl else 'right'}: -200px;
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, rgba(196, 69, 105, 0.08) 0%, transparent 70%);
            border-radius: 50%;
            pointer-events: none;
            z-index: 0;
            animation: float 25s ease-in-out infinite reverse;
        }}

        @keyframes float {{
            0%, 100% {{ transform: translate(0, 0) scale(1); }}
            50% {{ transform: translate(50px, -50px) scale(1.1); }}
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 30px 20px;
            position: relative;
            z-index: 1;
        }}

        /* 优雅的语言切换器 */
        .lang-switcher {{
            position: fixed;
            top: 25px;
            {'right' if is_rtl else 'left'}: 25px;
            z-index: 1001;
            background: var(--white);
            padding: 12px 24px;
            border-radius: 30px;
            text-decoration: none;
            color: var(--primary);
            font-weight: 700;
            font-size: 14px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: var(--shadow-md);
            border: 2px solid transparent;
        }}

        .lang-switcher:hover {{
            background: var(--primary);
            color: var(--white);
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }}

        /* 精美的头部 */
        .header {{
            text-align: center;
            padding: 60px 40px;
            background: var(--white);
            border-radius: 30px;
            margin-bottom: 40px;
            box-shadow: var(--shadow-lg);
            position: relative;
            overflow: hidden;
        }}

        .header::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 5px;
            background: linear-gradient(90deg, var(--primary), var(--secondary), var(--accent), var(--primary));
            background-size: 200% 100%;
            animation: shimmer 3s linear infinite;
        }}

        @keyframes shimmer {{
            0% {{ background-position: 0% 0%; }}
            100% {{ background-position: 200% 0%; }}
        }}

        .header h1 {{
            font-size: 56px;
            font-weight: 900;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 16px;
            letter-spacing: -1.5px;
            line-height: 1.1;
        }}

        .header p {{
            color: var(--text-secondary);
            font-size: 20px;
            font-weight: 500;
        }}

        /* 导航控制 */
        .nav-controls {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 40px;
            padding: 0 20px;
        }}

        .nav-arrow {{
            background: var(--white);
            color: var(--primary);
            border: 2px solid var(--primary);
            width: 60px;
            height: 60px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 28px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: var(--shadow-md);
            font-weight: 300;
        }}

        .nav-arrow:hover:not(:disabled) {{
            background: var(--primary);
            color: var(--white);
            transform: scale(1.1) translateY(-2px);
            box-shadow: var(--shadow-lg);
        }}

        .item-counter {{
            font-size: 20px;
            color: var(--text-primary);
            font-weight: 800;
            background: var(--white);
            padding: 14px 28px;
            border-radius: 30px;
            box-shadow: var(--shadow-md);
        }}

        /* 惊艳的卡片设计 - 大图展示 */
        .clothes-card {{
            background: var(--white);
            border-radius: 30px;
            padding: 0;
            margin-bottom: 40px;
            box-shadow: var(--shadow-xl);
            overflow: hidden;
            position: relative;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        .clothes-card:hover {{
            transform: translateY(-8px);
            box-shadow: 0 24px 80px rgba(255, 107, 157, 0.25);
        }}

        .clothes-header {{
            display: grid;
            grid-template-columns: 500px 1fr;
            gap: 50px;
            padding: 50px;
            background: linear-gradient(135deg, #fff 0%, #fafafa 100%);
        }}

        .clothes-image-wrapper {{
            position: relative;
            border-radius: 25px;
            overflow: hidden;
            box-shadow: var(--shadow-lg);
            background: linear-gradient(135deg, #f5f5f5 0%, #e8e8e8 100%);
        }}

        .clothes-cover {{
            width: 100%;
            height: 600px;
            object-fit: cover;
            transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
            display: block;
        }}

        .clothes-card:hover .clothes-cover {{
            transform: scale(1.05);
        }}

        .clothes-info {{
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 20px 0;
        }}

        .clothes-title {{
            font-size: 52px;
            font-weight: 900;
            color: var(--text-primary);
            margin-bottom: 16px;
            line-height: 1.2;
            letter-spacing: -2px;
        }}

        .clothes-category {{
            display: inline-block;
            padding: 10px 24px;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: var(--white);
            border-radius: 50px;
            font-size: 14px;
            font-weight: 700;
            margin-bottom: 30px;
            width: fit-content;
            box-shadow: var(--shadow-md);
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .user-info {{
            display: flex;
            align-items: center;
            gap: 16px;
            margin-top: auto;
            padding-top: 30px;
            border-top: 2px solid #f0f0f0;
        }}

        .user-avatar {{
            width: 60px;
            height: 60px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid var(--primary);
            flex-shrink: 0;
            box-shadow: var(--shadow-md);
        }}

        .user-details {{
            flex: 1;
        }}

        .user-name {{
            font-size: 20px;
            font-weight: 800;
            color: var(--text-primary);
            margin-bottom: 8px;
        }}

        .trust-badge {{
            font-size: 13px;
            padding: 6px 14px;
            border-radius: 50px;
            background: linear-gradient(135deg, #fff3cd 0%, #ffe69c 100%);
            color: #856404;
            font-weight: 700;
            display: inline-block;
            box-shadow: var(--shadow-sm);
        }}

        .whatsapp-icon {{
            width: 60px;
            height: 60px;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
            border-radius: 50%;
            padding: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: var(--shadow-md);
        }}

        .whatsapp-icon:hover {{
            transform: scale(1.15) rotate(5deg);
            box-shadow: 0 12px 32px rgba(37, 211, 102, 0.4);
        }}

        .whatsapp-icon svg {{
            width: 28px;
            height: 28px;
            fill: var(--white);
        }}

        .why-release {{
            background: linear-gradient(135deg, #fff5f8 0%, #ffeef7 100%);
            padding: 50px;
            border-top: 2px solid #f0f0f0;
        }}

        .why-release h4 {{
            font-size: 18px;
            color: var(--primary);
            margin-bottom: 20px;
            text-transform: uppercase;
            font-weight: 800;
            letter-spacing: 2px;
        }}

        .why-release p {{
            font-size: 18px;
            line-height: 2;
            color: var(--text-secondary);
            font-weight: 400;
        }}

        /* 分享按钮 */
        .share-btn {{
            position: absolute;
            top: 40px;
            {'left' if is_rtl else 'right'}: 40px;
            background: var(--white);
            color: var(--primary);
            border: 2px solid var(--primary);
            border-radius: 50px;
            padding: 14px 28px;
            font-size: 15px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 10px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            z-index: 10;
            font-weight: 700;
            box-shadow: var(--shadow-md);
        }}

        .share-btn:hover {{
            background: var(--primary);
            color: var(--white);
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }}

        /* 底部按钮 */
        .fixed-bottom-btn {{
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: var(--white);
            border-top: 2px solid #f0f0f0;
            padding: 25px;
            box-shadow: 0 -8px 32px rgba(0, 0, 0, 0.1);
            z-index: 1000;
        }}

        .request-btn {{
            width: 100%;
            max-width: 1400px;
            margin: 0 auto;
            padding: 22px;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: var(--white);
            border: none;
            border-radius: 50px;
            font-size: 20px;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            display: block;
            box-shadow: var(--shadow-lg);
            letter-spacing: 0.5px;
        }}

        .request-btn:hover {{
            transform: translateY(-4px);
            box-shadow: 0 16px 48px rgba(255, 107, 157, 0.4);
        }}

        /* 模态框 */
        .modal {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
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
            background: var(--white);
            border-radius: 30px;
            max-width: 600px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
            position: relative;
            padding: 50px 40px;
            box-shadow: var(--shadow-xl);
        }}

        .modal-close {{
            position: absolute;
            top: 25px;
            {'left' if is_rtl else 'right'}: 25px;
            background: #f5f5f5;
            border: none;
            font-size: 32px;
            cursor: pointer;
            color: var(--text-secondary);
            width: 50px;
            height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            transition: all 0.3s;
        }}

        .modal-close:hover {{
            background: var(--primary);
            color: var(--white);
            transform: rotate(90deg) scale(1.1);
        }}

        .modal-title {{
            font-size: 32px;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 35px;
            text-align: center;
            font-weight: 900;
            letter-spacing: -1px;
        }}

        .form-group {{
            margin-bottom: 28px;
        }}

        .form-group label {{
            display: block;
            margin-bottom: 12px;
            font-weight: 800;
            color: var(--text-primary);
            font-size: 16px;
        }}

        .form-group textarea {{
            width: 100%;
            min-height: 150px;
            padding: 18px;
            border: 2px solid #e0e0e0;
            border-radius: 16px;
            font-family: inherit;
            font-size: 16px;
            resize: vertical;
            transition: all 0.3s;
            background: var(--bg-light);
        }}

        .form-group textarea:focus {{
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 4px rgba(255, 107, 157, 0.1);
            background: var(--white);
        }}

        .image-upload-area {{
            border: 3px dashed #e0e0e0;
            border-radius: 20px;
            padding: 45px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
            margin-bottom: 20px;
            background: var(--bg-light);
        }}

        .image-upload-area:hover {{
            border-color: var(--primary);
            background: #fff5f8;
        }}

        .uploaded-image {{
            max-width: 100%;
            max-height: 320px;
            border-radius: 16px;
            margin-top: 20px;
            box-shadow: var(--shadow-md);
        }}

        .upload-icon {{
            font-size: 60px;
            color: var(--primary);
            margin-bottom: 16px;
        }}

        .submit-btn {{
            width: 100%;
            padding: 20px;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: var(--white);
            border: none;
            border-radius: 50px;
            font-size: 18px;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            margin-top: 32px;
            box-shadow: var(--shadow-lg);
            letter-spacing: 0.5px;
        }}

        .submit-btn:hover {{
            transform: translateY(-3px);
            box-shadow: 0 16px 48px rgba(255, 107, 157, 0.4);
        }}

        /* 历史交换区 */
        .history-section {{
            margin-top: 50px;
            background: var(--white);
            border-radius: 30px;
            padding: 45px;
            box-shadow: var(--shadow-xl);
        }}

        .history-section h2 {{
            font-size: 36px;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 35px;
            text-align: center;
            font-weight: 900;
            letter-spacing: -1px;
        }}

        .exchange-list {{
            display: flex;
            gap: 28px;
            overflow-x: auto;
            padding: 20px 0;
            scroll-snap-type: x mandatory;
            -webkit-overflow-scrolling: touch;
        }}

        .exchange-item {{
            display: flex;
            align-items: center;
            gap: 24px;
            padding: 32px;
            background: linear-gradient(135deg, #fff5f8 0%, #ffeef7 100%);
            border-radius: 25px;
            min-width: 420px;
            flex-shrink: 0;
            scroll-snap-align: start;
            box-shadow: var(--shadow-md);
            border: 2px solid #ffe0e8;
        }}

        .exchange-clothes {{
            text-align: center;
            flex: 1;
        }}

        .exchange-clothes img {{
            width: 110px;
            height: 165px;
            object-fit: cover;
            border-radius: 18px;
            margin-bottom: 14px;
            box-shadow: var(--shadow-md);
        }}

        .exchange-clothes p {{
            font-size: 15px;
            font-weight: 800;
            line-height: 1.4;
            color: var(--text-primary);
        }}

        .exchange-icon {{
            font-size: 44px;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .exchange-date {{
            font-size: 13px;
            color: var(--text-secondary);
            text-align: center;
            margin-top: 14px;
            font-weight: 600;
        }}

        /* 响应式设计 */
        @media (max-width: 968px) {{
            .clothes-header {{
                grid-template-columns: 1fr;
                gap: 40px;
            }}

            .clothes-cover {{
                height: 450px;
            }}

            .header h1 {{
                font-size: 42px;
            }}

            .clothes-title {{
                font-size: 38px;
            }}
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 20px 15px;
            }}

            .header {{
                padding: 40px 25px;
            }}

            .header h1 {{
                font-size: 36px;
            }}

            .clothes-header {{
                padding: 35px 25px;
            }}

            .share-btn {{
                position: static;
                width: 100%;
                margin-top: 20px;
            }}

            .exchange-item {{
                flex-direction: column;
                min-width: 300px;
            }}

            .lang-switcher {{
                top: 15px;
                {'right' if is_rtl else 'left'}: 15px;
                padding: 10px 20px;
                font-size: 13px;
            }}
        }}
    </style>
</head>
<body>
    <a href="{translations['language_switcher_url']}" class="lang-switcher">
        {translations['language_switcher']}
    </a>

    <div class="container">
        <div class="header">
            <h1>👗 {translations['site_title']}</h1>
            <p>{translations['site_subtitle']}</p>
        </div>

        <div class="nav-controls">
            <button class="nav-arrow" onclick="prevItem()" id="prevBtn">‹</button>
            <div class="item-counter">
                <span id="currentIndex">1</span> / <span id="totalItems">15</span>
            </div>
            <button class="nav-arrow" onclick="nextItem()" id="nextBtn">›</button>
        </div>

        <div style="position: relative;">
            <div id="itemDisplay"></div>
            <button class="share-btn" onclick="shareItem()">
                📤 {translations['share']}
            </button>
        </div>

        <div class="history-section">
            <h2>🤝 {translations['completed_exchanges']}</h2>
            <div class="exchange-list" id="exchangeList"></div>
        </div>
    </div>

    <div class="fixed-bottom-btn">
        <button class="request-btn" onclick="openModal()">
            👗 {translations['request_exchange']}
        </button>
    </div>

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
                    <p style="color: var(--text-secondary); font-size: 16px;">{translations['upload_photo']}</p>
                    <img id="uploadedImagePreview" class="uploaded-image" style="display: none;">
                </div>
                <input type="file" id="itemImageInput" accept="image/*" style="display: none;" onchange="handleImageUpload(event)">
            </div>
            
            <div class="whatsapp-display" id="whatsappDisplay" style="display: none; margin-top: 28px; padding: 28px; background: linear-gradient(135deg, rgba(37, 211, 102, 0.1) 0%, rgba(37, 211, 102, 0.05) 100%); border-radius: 20px; text-align: center;">
                <p style="color: #155724; font-weight: 800; margin-bottom: 14px; font-size: 18px;">{translations['request_sent']}</p>
                <p style="color: var(--text-secondary); font-size: 15px;">{translations['contact_owner']}:</p>
                <a href="https://wa.me/{translations['whatsapp_number'].replace('+', '').replace(' ', '')}" target="_blank" class="whatsapp-link" id="whatsappLink" onclick="openWhatsApp(items[currentItemIndex].id); return true;" style="display: inline-flex; align-items: center; gap: 12px; color: #25D366; text-decoration: none; font-weight: 800; font-size: 20px; margin-top: 18px; padding: 18px 36px; background: var(--white); border-radius: 50px; transition: all 0.3s; box-shadow: var(--shadow-md);">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/>
                    </svg>
                    {translations['whatsapp_number']}
                </a>
            </div>

            <button class="submit-btn" onclick="submitExchange()" id="submitBtn">
                🤝 {translations['send_request']}
            </button>

            <div class="success-message" id="successMessage" style="display: none; margin-top: 28px; padding: 28px; background: linear-gradient(135deg, rgba(37, 211, 102, 0.1) 0%, rgba(37, 211, 102, 0.05) 100%); border-radius: 20px; color: #155724; text-align: center; font-size: 17px; font-weight: 700;">
                ✅ {translations['request_sent_success']}
            </div>
        </div>
    </div>

    <script>
        const items = {js_data};
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
        let viewedItemsInSession = new Set();

        function init() {{
            displayItem(0);
            displayExchanges();
            updateCounter();
        }}

        function displayItem(index) {{
            if (index < 0 || index >= items.length) return;
            currentItemIndex = index;
            const item = items[index];
            const itemDisplay = document.getElementById('itemDisplay');
            
            if (item && item.id && !viewedItemsInSession.has(item.id)) {{
                viewedItemsInSession.add(item.id);
            }}

            // 确保使用正确的图片路径
            const imageUrl = item.cover.startsWith('http') ? item.cover : 
                           (item.cover.startsWith('/') ? window.location.origin + item.cover : 
                           window.location.origin + '/static/' + item.cover.replace('/static/', ''));

            itemDisplay.innerHTML = `
                <div class="clothes-card">
                    <div class="clothes-header">
                        <div class="clothes-image-wrapper">
                            <img src="${{imageUrl}}" alt="${{item.title}}" class="clothes-cover" loading="lazy" onerror="handleImageError(this, '${{imageUrl}}')">
                        </div>
                        <div class="clothes-info">
                            <div>
                                <div class="clothes-title">${{item.title}}</div>
                                <span class="clothes-category">${{item.category}}</span>
                            </div>
                            <div class="user-info">
                                <img src="${{item.user.avatar}}" alt="${{item.user.name}}" class="user-avatar" onerror="this.onerror=null; this.src='data:image/svg+xml,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\'%3E%3Crect width=\\'60\\' height=\\'60\\' fill=\\'%23ff6b9d\\'/%3E%3Ctext x=\\'50%25\\' y=\\'50%25\\' fill=\\'white\\' text-anchor=\\'middle\\' dominant-baseline=\\'central\\' font-size=\\'28\\' font-weight=\\'bold\\'>${{item.user.name.charAt(0)}}</text%3E%3C/svg%3E';">
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
        }}

        function handleImageError(img, url) {{
            console.error('Image load failed:', url);
            img.style.display = 'none';
            const wrapper = img.parentElement;
            if (wrapper && !wrapper.querySelector('.error-placeholder')) {{
                const placeholder = document.createElement('div');
                placeholder.className = 'error-placeholder';
                placeholder.style.cssText = 'width: 100%; height: 600px; background: linear-gradient(135deg, #f5f5f5 0%, #e8e8e8 100%); border-radius: 25px; display: flex; align-items: center; justify-content: center; color: #999; font-size: 20px; font-weight: 600;';
                placeholder.textContent = '图片加载失败';
                wrapper.appendChild(placeholder);
            }}
        }}

        function updateCounter() {{
            document.getElementById('currentIndex').textContent = currentItemIndex + 1;
            document.getElementById('totalItems').textContent = items.length;
        }}

        function prevItem() {{
            displayItem(currentItemIndex > 0 ? currentItemIndex - 1 : items.length - 1);
        }}

        function nextItem() {{
            displayItem(currentItemIndex < items.length - 1 ? currentItemIndex + 1 : 0);
        }}

        function displayExchanges() {{
            const exchangeList = document.getElementById('exchangeList');
            exchangeList.innerHTML = exchanges.map(ex => {{
                const img1Url = ex.item1.cover.startsWith('http') ? ex.item1.cover : 
                              (ex.item1.cover.startsWith('/') ? window.location.origin + ex.item1.cover : 
                              window.location.origin + '/static/' + ex.item1.cover.replace('/static/', ''));
                const img2Url = ex.item2.cover.startsWith('http') ? ex.item2.cover : 
                              (ex.item2.cover.startsWith('/') ? window.location.origin + ex.item2.cover : 
                              window.location.origin + '/static/' + ex.item2.cover.replace('/static/', ''));
                return `
                <div style="min-width: 420px; flex-shrink: 0;">
                    <div class="exchange-item">
                        <div class="exchange-clothes">
                            <img src="${{img1Url}}" alt="${{ex.item1.title}}" loading="lazy" onerror="this.style.display='none';">
                            <p>${{ex.item1.title}}</p>
                            <p style="font-size: 13px; color: var(--text-secondary); margin-top: 8px; font-weight: 600;">${{ex.item1.user}}</p>
                        </div>
                        <div class="exchange-icon">🤝</div>
                        <div class="exchange-clothes">
                            <img src="${{img2Url}}" alt="${{ex.item2.title}}" loading="lazy" onerror="this.style.display='none';">
                            <p>${{ex.item2.title}}</p>
                            <p style="font-size: 13px; color: var(--text-secondary); margin-top: 8px; font-weight: 600;">${{ex.item2.user}}</p>
                        </div>
                    </div>
                    <div class="exchange-date">${{ex.date}}</div>
                </div>
            `;
            }}).join('');
        }}

        function openModal() {{
            document.getElementById('exchangeModal').classList.add('active');
            document.body.style.overflow = 'hidden';
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
                    document.getElementById('uploadedImagePreview').src = uploadedImage;
                    document.getElementById('uploadedImagePreview').style.display = 'block';
                    document.getElementById('imageUploadArea').classList.add('has-image');
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
            document.getElementById('whatsappDisplay').style.display = 'block';
            document.getElementById('submitBtn').style.display = 'none';
        }}

        function openWhatsApp(itemId) {{
            const currentItem = items[currentItemIndex];
            const message = encodeURIComponent(`Hello, I'm interested in exchanging this item: "${{currentItem ? currentItem.title : ''}}"`);
            window.open(`https://wa.me/{translations['whatsapp_number'].replace('+', '').replace(' ', '')}?text=${{message}}`, '_blank');
        }}

        function shareItem() {{
            const item = items[currentItemIndex];
            const shareText = `👗 ${{item.title}} – ${{item.category}}\\n\\n"${{item.why_release.substring(0, 110)}}..."\\n\\n🔥 Exchange clothes, share stories!`;
            if (navigator.share) {{
                navigator.share({{ title: `👗 ${{item.title}}`, text: shareText, url: window.location.href }});
            }} else {{
                navigator.clipboard.writeText(shareText);
                alert('Text copied!');
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

if __name__ == '__main__':
    ar_html = generate_template('ar', AR_TRANSLATIONS, CLOTHES_DATA)
    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write(ar_html)
    print('✅ 已生成惊艳UI模板（阿拉伯语）')
    
    zh_html = generate_template('zh', ZH_TRANSLATIONS, CLOTHES_DATA_ZH)
    with open('templates/index_zh.html', 'w', encoding='utf-8') as f:
        f.write(zh_html)
    print('✅ 已生成惊艳UI模板（中文）')

