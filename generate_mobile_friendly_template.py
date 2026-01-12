#!/usr/bin/env python3
"""
生成移动端友好的UI模板 - 深色主题+金色，移动端优化
确保在手机上清晰可见，文字大小合适，布局合理
"""
import json
from clothes_data import CLOTHES_DATA
from translations import AR_TRANSLATIONS, ZH_TRANSLATIONS, CLOTHES_DATA_ZH

def generate_template(lang='ar', translations=None, clothes_data=None):
    """生成移动端友好的UI模板"""
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
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>{translations['site_title']}</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>👗</text></svg>">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700;800;900&family=Cairo:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }}

        :root {{
            --primary: #d4af37;
            --primary-dark: #b8941f;
            --primary-light: #e8c547;
            --secondary: #8b4513;
            --accent: #ff6b9d;
            --dark: #1a1a1a;
            --darker: #0f0f0f;
            --text-primary: #ffffff;
            --text-secondary: #d4d4d4;
            --text-gold: #d4af37;
            --bg-gradient: linear-gradient(135deg, #1a1a1a 0%, #2d1b1b 50%, #1a1a1a 100%);
            --gold-gradient: linear-gradient(135deg, #d4af37 0%, #f4d03f 50%, #d4af37 100%);
            --shadow-gold: 0 8px 32px rgba(212, 175, 55, 0.3);
            --shadow-dark: 0 16px 64px rgba(0, 0, 0, 0.5);
        }}

        body {{
            font-family: 'Inter', 'Cairo', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: var(--bg-gradient);
            background-attachment: fixed;
            min-height: 100vh;
            color: var(--text-primary);
            line-height: 1.6;
            padding-bottom: 100px;
            position: relative;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }}

        /* 背景装饰 - 移动端减少 */
        body::before {{
            content: '';
            position: fixed;
            top: -300px;
            {'right' if is_rtl else 'left'}: -300px;
            width: 800px;
            height: 800px;
            background: radial-gradient(circle, rgba(212, 175, 55, 0.15) 0%, transparent 70%);
            border-radius: 50%;
            pointer-events: none;
            z-index: 0;
            animation: pulse 8s ease-in-out infinite;
        }}

        body::after {{
            content: '';
            position: fixed;
            bottom: -300px;
            {'left' if is_rtl else 'right'}: -300px;
            width: 700px;
            height: 700px;
            background: radial-gradient(circle, rgba(255, 107, 157, 0.12) 0%, transparent 70%);
            border-radius: 50%;
            pointer-events: none;
            z-index: 0;
            animation: pulse 10s ease-in-out infinite reverse;
        }}

        @keyframes pulse {{
            0%, 100% {{ transform: scale(1); opacity: 0.5; }}
            50% {{ transform: scale(1.2); opacity: 0.8; }}
        }}

        .container {{
            max-width: 1600px;
            margin: 0 auto;
            padding: 20px 15px;
            position: relative;
            z-index: 1;
        }}

        /* 语言切换器 - 移动端优化 */
        .lang-switcher {{
            position: fixed;
            top: 15px;
            {'right' if is_rtl else 'left'}: 15px;
            z-index: 1001;
            background: rgba(26, 26, 26, 0.95);
            backdrop-filter: blur(20px);
            border: 2px solid var(--primary);
            padding: 10px 18px;
            border-radius: 50px;
            text-decoration: none;
            color: var(--primary);
            font-weight: 800;
            font-size: 13px;
            transition: all 0.3s;
            box-shadow: var(--shadow-gold);
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .lang-switcher:hover {{
            background: var(--gold-gradient);
            color: var(--dark);
            transform: translateY(-2px);
        }}

        /* 头部 - 移动端优化 */
        .header {{
            text-align: center;
            padding: 40px 25px;
            background: rgba(26, 26, 26, 0.9);
            backdrop-filter: blur(30px);
            border: 2px solid var(--primary);
            border-radius: 25px;
            margin-bottom: 30px;
            box-shadow: var(--shadow-dark), var(--shadow-gold);
            position: relative;
            overflow: hidden;
        }}

        .header::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: var(--gold-gradient);
            background-size: 200% 100%;
            animation: shimmer 2s linear infinite;
        }}

        @keyframes shimmer {{
            0% {{ background-position: 0% 0%; }}
            100% {{ background-position: 200% 0%; }}
        }}

        .header h1 {{
            font-family: 'Playfair Display', serif;
            font-size: 36px;
            font-weight: 900;
            background: var(--gold-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 12px;
            letter-spacing: -1px;
            line-height: 1.2;
        }}

        .header p {{
            color: var(--text-secondary);
            font-size: 16px;
            font-weight: 500;
            letter-spacing: 0.3px;
        }}

        /* 导航控制 - 移动端优化 */
        .nav-controls {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
            padding: 0 10px;
            gap: 15px;
        }}

        .nav-arrow {{
            background: rgba(26, 26, 26, 0.9);
            backdrop-filter: blur(20px);
            color: var(--primary);
            border: 2px solid var(--primary);
            width: 50px;
            height: 50px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 24px;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: var(--shadow-gold);
            font-weight: 300;
            flex-shrink: 0;
        }}

        .nav-arrow:active {{
            transform: scale(0.95);
        }}

        .nav-arrow:hover:not(:disabled) {{
            background: var(--gold-gradient);
            color: var(--dark);
            transform: scale(1.1);
        }}

        .item-counter {{
            font-size: 18px;
            color: var(--primary);
            font-weight: 900;
            background: rgba(26, 26, 26, 0.9);
            backdrop-filter: blur(20px);
            border: 2px solid var(--primary);
            padding: 12px 24px;
            border-radius: 50px;
            box-shadow: var(--shadow-gold);
            text-transform: uppercase;
            letter-spacing: 1.5px;
            flex: 1;
            text-align: center;
        }}

        /* 卡片设计 - 移动端优化 */
        .clothes-card {{
            background: rgba(26, 26, 26, 0.9);
            backdrop-filter: blur(30px);
            border: 2px solid var(--primary);
            border-radius: 25px;
            padding: 0;
            margin-bottom: 30px;
            box-shadow: var(--shadow-dark), var(--shadow-gold);
            overflow: hidden;
            position: relative;
            transition: all 0.3s;
        }}

        .clothes-card:active {{
            transform: scale(0.98);
        }}

        .clothes-header {{
            display: flex;
            flex-direction: column;
            gap: 25px;
            padding: 25px;
            background: linear-gradient(135deg, rgba(26, 26, 26, 0.95) 0%, rgba(45, 27, 27, 0.95) 100%);
        }}

        .clothes-image-wrapper {{
            position: relative;
            width: 100%;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: var(--shadow-dark), 0 0 40px rgba(212, 175, 55, 0.2);
            background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
            border: 2px solid var(--primary);
        }}

        .clothes-cover {{
            width: 100%;
            height: auto;
            min-height: 400px;
            max-height: 500px;
            object-fit: cover;
            display: block;
            filter: brightness(1.05) contrast(1.1);
        }}

        .clothes-info {{
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}

        .clothes-title {{
            font-family: 'Playfair Display', serif;
            font-size: 32px;
            font-weight: 900;
            background: var(--gold-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1.3;
            letter-spacing: -1px;
        }}

        .clothes-category {{
            display: inline-block;
            padding: 8px 20px;
            background: var(--gold-gradient);
            color: var(--dark);
            border-radius: 50px;
            font-size: 13px;
            font-weight: 900;
            width: fit-content;
            box-shadow: var(--shadow-gold);
            text-transform: uppercase;
            letter-spacing: 1.5px;
            border: 2px solid var(--primary-dark);
        }}

        .user-info {{
            display: flex;
            align-items: center;
            gap: 15px;
            padding-top: 20px;
            border-top: 2px solid rgba(212, 175, 55, 0.3);
        }}

        .user-avatar {{
            width: 55px;
            height: 55px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid var(--primary);
            flex-shrink: 0;
            box-shadow: var(--shadow-gold);
        }}

        .user-details {{
            flex: 1;
            min-width: 0;
        }}

        .user-name {{
            font-size: 18px;
            font-weight: 900;
            color: var(--text-primary);
            margin-bottom: 6px;
            letter-spacing: 0.3px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        .trust-badge {{
            font-size: 12px;
            padding: 6px 14px;
            border-radius: 50px;
            background: var(--gold-gradient);
            color: var(--dark);
            font-weight: 900;
            display: inline-block;
            box-shadow: var(--shadow-gold);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .whatsapp-icon {{
            width: 55px;
            height: 55px;
            cursor: pointer;
            transition: all 0.3s;
            background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
            border-radius: 50%;
            padding: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 8px 24px rgba(37, 211, 102, 0.5);
            border: 3px solid var(--primary);
            flex-shrink: 0;
        }}

        .whatsapp-icon:active {{
            transform: scale(0.9);
        }}

        .whatsapp-icon:hover {{
            transform: scale(1.1);
            box-shadow: 0 12px 40px rgba(37, 211, 102, 0.7);
        }}

        .whatsapp-icon svg {{
            width: 28px;
            height: 28px;
            fill: var(--white);
        }}

        .why-release {{
            background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(255, 107, 157, 0.05) 100%);
            padding: 25px;
            border-top: 2px solid rgba(212, 175, 55, 0.3);
            position: relative;
        }}

        .why-release::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: var(--gold-gradient);
            background-size: 200% 100%;
            animation: shimmer 2s linear infinite;
        }}

        .why-release h4 {{
            font-size: 16px;
            color: var(--primary);
            margin-bottom: 15px;
            text-transform: uppercase;
            font-weight: 900;
            letter-spacing: 2px;
            font-family: 'Playfair Display', serif;
        }}

        .why-release p {{
            font-size: 16px;
            line-height: 1.8;
            color: var(--text-secondary);
            font-weight: 400;
            letter-spacing: 0.2px;
        }}

        /* 分享按钮 - 移动端优化 */
        .share-btn {{
            position: static;
            width: 100%;
            margin-top: 20px;
            background: rgba(26, 26, 26, 0.9);
            backdrop-filter: blur(20px);
            color: var(--primary);
            border: 2px solid var(--primary);
            border-radius: 50px;
            padding: 14px 24px;
            font-size: 15px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            transition: all 0.3s;
            font-weight: 900;
            box-shadow: var(--shadow-gold);
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .share-btn:active {{
            transform: scale(0.98);
        }}

        .share-btn:hover {{
            background: var(--gold-gradient);
            color: var(--dark);
            transform: translateY(-2px);
        }}

        /* 底部按钮 - 移动端优化 */
        .fixed-bottom-btn {{
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(26, 26, 26, 0.98);
            backdrop-filter: blur(30px);
            border-top: 3px solid var(--primary);
            padding: 20px 15px;
            box-shadow: 0 -16px 64px rgba(0, 0, 0, 0.5);
            z-index: 1000;
        }}

        .request-btn {{
            width: 100%;
            padding: 18px;
            background: var(--gold-gradient);
            color: var(--dark);
            border: 3px solid var(--primary-dark);
            border-radius: 50px;
            font-size: 18px;
            font-weight: 900;
            cursor: pointer;
            transition: all 0.3s;
            display: block;
            box-shadow: var(--shadow-gold);
            letter-spacing: 1.5px;
            text-transform: uppercase;
            font-family: 'Playfair Display', serif;
        }}

        .request-btn:active {{
            transform: scale(0.98);
        }}

        .request-btn:hover {{
            transform: translateY(-3px);
            box-shadow: 0 16px 64px rgba(212, 175, 55, 0.6);
        }}

        /* 模态框 - 移动端优化 */
        .modal {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.95);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            z-index: 2000;
            overflow-y: auto;
            padding: 15px;
        }}

        .modal.active {{
            display: flex;
            align-items: flex-start;
            justify-content: center;
            padding-top: 20px;
        }}

        .modal-content {{
            background: rgba(26, 26, 26, 0.98);
            backdrop-filter: blur(40px);
            border: 3px solid var(--primary);
            border-radius: 30px;
            max-width: 100%;
            width: 100%;
            max-height: 95vh;
            overflow-y: auto;
            position: relative;
            padding: 40px 25px;
            box-shadow: var(--shadow-dark), var(--shadow-gold);
        }}

        .modal-close {{
            position: absolute;
            top: 20px;
            {'left' if is_rtl else 'right'}: 20px;
            background: rgba(212, 175, 55, 0.2);
            border: 2px solid var(--primary);
            font-size: 28px;
            cursor: pointer;
            color: var(--primary);
            width: 50px;
            height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            transition: all 0.3s;
        }}

        .modal-close:active {{
            transform: scale(0.9);
        }}

        .modal-close:hover {{
            background: var(--gold-gradient);
            color: var(--dark);
            transform: rotate(90deg) scale(1.1);
        }}

        .modal-title {{
            font-family: 'Playfair Display', serif;
            font-size: 28px;
            background: var(--gold-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 30px;
            text-align: center;
            font-weight: 900;
            letter-spacing: -0.5px;
        }}

        .form-group {{
            margin-bottom: 25px;
        }}

        .form-group label {{
            display: block;
            margin-bottom: 12px;
            font-weight: 900;
            color: var(--primary);
            font-size: 16px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .form-group textarea {{
            width: 100%;
            min-height: 140px;
            padding: 18px;
            border: 2px solid rgba(212, 175, 55, 0.3);
            border-radius: 18px;
            font-family: inherit;
            font-size: 16px;
            resize: vertical;
            transition: all 0.3s;
            background: rgba(26, 26, 26, 0.8);
            color: var(--text-primary);
        }}

        .form-group textarea:focus {{
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 4px rgba(212, 175, 55, 0.2);
            background: rgba(26, 26, 26, 0.95);
        }}

        .image-upload-area {{
            border: 3px dashed rgba(212, 175, 55, 0.4);
            border-radius: 20px;
            padding: 35px 20px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
            margin-bottom: 20px;
            background: rgba(212, 175, 55, 0.05);
        }}

        .image-upload-area:active {{
            transform: scale(0.98);
        }}

        .image-upload-area:hover {{
            border-color: var(--primary);
            background: rgba(212, 175, 55, 0.1);
        }}

        .uploaded-image {{
            max-width: 100%;
            max-height: 300px;
            border-radius: 18px;
            margin-top: 20px;
            box-shadow: var(--shadow-dark);
            border: 2px solid var(--primary);
        }}

        .upload-icon {{
            font-size: 56px;
            background: var(--gold-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 16px;
        }}

        .submit-btn {{
            width: 100%;
            padding: 20px;
            background: var(--gold-gradient);
            color: var(--dark);
            border: 3px solid var(--primary-dark);
            border-radius: 50px;
            font-size: 18px;
            font-weight: 900;
            cursor: pointer;
            transition: all 0.3s;
            margin-top: 30px;
            box-shadow: var(--shadow-gold);
            letter-spacing: 1.5px;
            text-transform: uppercase;
            font-family: 'Playfair Display', serif;
        }}

        .submit-btn:active {{
            transform: scale(0.98);
        }}

        .submit-btn:hover {{
            transform: translateY(-3px);
            box-shadow: 0 16px 64px rgba(212, 175, 55, 0.6);
        }}

        /* 历史交换区 - 移动端优化 */
        .history-section {{
            margin-top: 40px;
            background: rgba(26, 26, 26, 0.9);
            backdrop-filter: blur(30px);
            border: 2px solid var(--primary);
            border-radius: 25px;
            padding: 30px 20px;
            box-shadow: var(--shadow-dark), var(--shadow-gold);
        }}

        .history-section h2 {{
            font-family: 'Playfair Display', serif;
            font-size: 32px;
            background: var(--gold-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 30px;
            text-align: center;
            font-weight: 900;
            letter-spacing: -0.5px;
        }}

        .exchange-list {{
            display: flex;
            gap: 20px;
            overflow-x: auto;
            padding: 15px 0;
            scroll-snap-type: x mandatory;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: thin;
            scrollbar-color: var(--primary) rgba(26, 26, 26, 0.5);
        }}

        .exchange-list::-webkit-scrollbar {{
            height: 6px;
        }}

        .exchange-list::-webkit-scrollbar-track {{
            background: rgba(26, 26, 26, 0.5);
            border-radius: 3px;
        }}

        .exchange-list::-webkit-scrollbar-thumb {{
            background: var(--primary);
            border-radius: 3px;
        }}

        .exchange-item {{
            display: flex;
            align-items: center;
            gap: 20px;
            padding: 25px;
            background: linear-gradient(135deg, rgba(212, 175, 55, 0.15) 0%, rgba(255, 107, 157, 0.1) 100%);
            border-radius: 20px;
            min-width: 320px;
            flex-shrink: 0;
            scroll-snap-align: start;
            box-shadow: var(--shadow-dark);
            border: 2px solid rgba(212, 175, 55, 0.4);
        }}

        .exchange-clothes {{
            text-align: center;
            flex: 1;
        }}

        .exchange-clothes img {{
            width: 90px;
            height: 135px;
            object-fit: cover;
            border-radius: 15px;
            margin-bottom: 12px;
            box-shadow: var(--shadow-dark);
            border: 2px solid var(--primary);
        }}

        .exchange-clothes p {{
            font-size: 14px;
            font-weight: 900;
            line-height: 1.4;
            color: var(--text-primary);
            letter-spacing: 0.3px;
        }}

        .exchange-icon {{
            font-size: 36px;
            background: var(--gold-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .exchange-date {{
            font-size: 12px;
            color: var(--text-secondary);
            text-align: center;
            margin-top: 12px;
            font-weight: 700;
            letter-spacing: 0.5px;
        }}

        /* 桌面端样式 */
        @media (min-width: 769px) {{
            .container {{
                padding: 40px 20px;
            }}

            .header {{
                padding: 80px 50px;
                border-radius: 40px;
            }}

            .header h1 {{
                font-size: 72px;
            }}

            .header p {{
                font-size: 22px;
            }}

            .nav-controls {{
                margin-bottom: 50px;
                padding: 0 20px;
            }}

            .nav-arrow {{
                width: 70px;
                height: 70px;
                font-size: 32px;
            }}

            .item-counter {{
                font-size: 24px;
                padding: 18px 36px;
            }}

            .clothes-card {{
                border-radius: 40px;
                margin-bottom: 50px;
            }}

            .clothes-header {{
                display: grid;
                grid-template-columns: 600px 1fr;
                gap: 60px;
                padding: 60px;
            }}

            .clothes-image-wrapper {{
                border-radius: 30px;
            }}

            .clothes-cover {{
                height: 700px;
                min-height: 700px;
                max-height: 700px;
            }}

            .clothes-title {{
                font-size: 64px;
            }}

            .clothes-category {{
                padding: 12px 28px;
                font-size: 16px;
            }}

            .user-info {{
                gap: 20px;
                padding-top: 35px;
            }}

            .user-avatar {{
                width: 70px;
                height: 70px;
            }}

            .user-name {{
                font-size: 22px;
            }}

            .trust-badge {{
                font-size: 14px;
                padding: 8px 18px;
            }}

            .whatsapp-icon {{
                width: 70px;
                height: 70px;
                padding: 18px;
            }}

            .whatsapp-icon svg {{
                width: 34px;
                height: 34px;
            }}

            .why-release {{
                padding: 60px;
            }}

            .why-release h4 {{
                font-size: 20px;
            }}

            .why-release p {{
                font-size: 20px;
                line-height: 2.2;
            }}

            .share-btn {{
                position: absolute;
                top: 50px;
                {'left' if is_rtl else 'right'}: 50px;
                width: auto;
                margin-top: 0;
            }}

            .fixed-bottom-btn {{
                padding: 30px;
            }}

            .request-btn {{
                padding: 26px;
                font-size: 24px;
            }}

            .modal-content {{
                max-width: 700px;
                padding: 60px 50px;
                border-radius: 40px;
            }}

            .modal-title {{
                font-size: 40px;
            }}

            .history-section {{
                padding: 60px;
                border-radius: 40px;
            }}

            .history-section h2 {{
                font-size: 48px;
            }}

            .exchange-item {{
                min-width: 480px;
                padding: 40px;
                border-radius: 30px;
            }}

            .exchange-clothes img {{
                width: 130px;
                height: 195px;
            }}

            .exchange-clothes p {{
                font-size: 16px;
            }}

            .exchange-icon {{
                font-size: 52px;
            }}
        }}

        /* 平板端样式 */
        @media (min-width: 481px) and (max-width: 768px) {{
            .header h1 {{
                font-size: 42px;
            }}

            .clothes-title {{
                font-size: 36px;
            }}

            .clothes-cover {{
                min-height: 450px;
                max-height: 550px;
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
                    <p style="color: var(--text-secondary); font-size: 15px;">{translations['upload_photo']}</p>
                    <img id="uploadedImagePreview" class="uploaded-image" style="display: none;">
                </div>
                <input type="file" id="itemImageInput" accept="image/*" style="display: none;" onchange="handleImageUpload(event)">
            </div>
            
            <div class="whatsapp-display" id="whatsappDisplay" style="display: none; margin-top: 28px; padding: 28px; background: linear-gradient(135deg, rgba(37, 211, 102, 0.15) 0%, rgba(37, 211, 102, 0.08) 100%); border-radius: 20px; text-align: center; border: 2px solid rgba(37, 211, 102, 0.3);">
                <p style="color: #25D366; font-weight: 900; margin-bottom: 14px; font-size: 18px; text-transform: uppercase; letter-spacing: 1px;">{translations['request_sent']}</p>
                <p style="color: var(--text-secondary); font-size: 15px;">{translations['contact_owner']}:</p>
                <a href="https://wa.me/{translations['whatsapp_number'].replace('+', '').replace(' ', '')}" target="_blank" class="whatsapp-link" id="whatsappLink" onclick="openWhatsApp(items[currentItemIndex].id); return true;" style="display: inline-flex; align-items: center; gap: 12px; color: #25D366; text-decoration: none; font-weight: 900; font-size: 20px; margin-top: 18px; padding: 18px 32px; background: rgba(26, 26, 26, 0.9); border-radius: 50px; transition: all 0.3s; box-shadow: 0 8px 32px rgba(37, 211, 102, 0.4); border: 2px solid #25D366;">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/>
                    </svg>
                    {translations['whatsapp_number']}
                </a>
            </div>

            <button class="submit-btn" onclick="submitExchange()" id="submitBtn">
                🤝 {translations['send_request']}
            </button>

            <div class="success-message" id="successMessage" style="display: none; margin-top: 28px; padding: 28px; background: linear-gradient(135deg, rgba(37, 211, 102, 0.15) 0%, rgba(37, 211, 102, 0.08) 100%); border-radius: 20px; color: #25D366; text-align: center; font-size: 17px; font-weight: 900; border: 2px solid rgba(37, 211, 102, 0.3); text-transform: uppercase; letter-spacing: 1px;">
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
                                <img src="${{item.user.avatar}}" alt="${{item.user.name}}" class="user-avatar" onerror="this.onerror=null; this.src='data:image/svg+xml,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\'%3E%3Crect width=\\'55\\' height=\\'55\\' fill=\\'%23d4af37\\'/%3E%3Ctext x=\\'50%25\\' y=\\'50%25\\' fill=\\'%231a1a1a\\' text-anchor=\\'middle\\' dominant-baseline=\\'central\\' font-size=\\'26\\' font-weight=\\'bold\\'>${{item.user.name.charAt(0)}}</text%3E%3C/svg%3E';">
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
                placeholder.style.cssText = 'width: 100%; min-height: 400px; background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%); border-radius: 20px; display: flex; align-items: center; justify-content: center; color: #d4af37; font-size: 20px; font-weight: 700; border: 2px solid #d4af37;';
                placeholder.textContent = '图片加载中...';
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
                <div style="min-width: 320px; flex-shrink: 0;">
                    <div class="exchange-item">
                        <div class="exchange-clothes">
                            <img src="${{img1Url}}" alt="${{ex.item1.title}}" loading="lazy" onerror="this.style.display='none';">
                            <p>${{ex.item1.title}}</p>
                            <p style="font-size: 12px; color: var(--text-secondary); margin-top: 8px; font-weight: 700;">${{ex.item1.user}}</p>
                        </div>
                        <div class="exchange-icon">🤝</div>
                        <div class="exchange-clothes">
                            <img src="${{img2Url}}" alt="${{ex.item2.title}}" loading="lazy" onerror="this.style.display='none';">
                            <p>${{ex.item2.title}}</p>
                            <p style="font-size: 12px; color: var(--text-secondary); margin-top: 8px; font-weight: 700;">${{ex.item2.user}}</p>
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
    print('✅ 已生成移动端友好UI模板（阿拉伯语）')
    
    zh_html = generate_template('zh', ZH_TRANSLATIONS, CLOTHES_DATA_ZH)
    with open('templates/index_zh.html', 'w', encoding='utf-8') as f:
        f.write(zh_html)
    print('✅ 已生成移动端友好UI模板（中文）')

