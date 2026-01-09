#!/usr/bin/env python3
"""
生成超高级UI模板 - 参考UI/UX Pro Max项目
采用最现代的设计：Neumorphism + Glassmorphism混合风格
更吸引人、更专业的衣服交换平台设计
"""
import json
from clothes_data import CLOTHES_DATA
from translations import AR_TRANSLATIONS, ZH_TRANSLATIONS, CLOTHES_DATA_ZH

def generate_template(lang='ar', translations=None, clothes_data=None):
    """生成超高级UI模板"""
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
            --primary: #6366f1;
            --primary-dark: #4f46e5;
            --primary-light: #818cf8;
            --secondary: #ec4899;
            --accent: #f59e0b;
            --success: #10b981;
            --text-primary: #111827;
            --text-secondary: #6b7280;
            --bg-primary: #0f172a;
            --bg-secondary: #1e293b;
            --glass-bg: rgba(255, 255, 255, 0.08);
            --glass-border: rgba(255, 255, 255, 0.18);
            --shadow-soft: 0 2px 8px rgba(0, 0, 0, 0.1);
            --shadow-medium: 0 4px 16px rgba(0, 0, 0, 0.15);
            --shadow-large: 0 8px 32px rgba(0, 0, 0, 0.2);
            --shadow-xl: 0 16px 64px rgba(0, 0, 0, 0.25);
        }}

        body {{
            font-family: 'Inter', 'Cairo', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
            min-height: 100vh;
            color: var(--text-primary);
            line-height: 1.6;
            padding-bottom: 120px;
            position: relative;
            overflow-x: hidden;
        }}

        @keyframes gradientShift {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}

        /* 动态背景装饰 */
        body::before {{
            content: '';
            position: fixed;
            top: -50%;
            {'right' if is_rtl else 'left'}: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.2) 0%, transparent 70%);
            animation: float 25s ease-in-out infinite;
            pointer-events: none;
            z-index: 0;
        }}

        body::after {{
            content: '';
            position: fixed;
            bottom: -50%;
            {'left' if is_rtl else 'right'}: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(236, 72, 153, 0.2) 0%, transparent 70%);
            animation: float 30s ease-in-out infinite reverse;
            pointer-events: none;
            z-index: 0;
        }}

        @keyframes float {{
            0%, 100% {{ transform: translate(0, 0) rotate(0deg); opacity: 0.5; }}
            50% {{ transform: translate(100px, -100px) rotate(180deg); opacity: 0.8; }}
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 40px 20px;
            position: relative;
            z-index: 1;
        }}

        /* 超现代语言切换器 */
        .lang-switcher {{
            position: fixed;
            top: 30px;
            {'right' if is_rtl else 'left'}: 30px;
            z-index: 1001;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(30px) saturate(180%);
            -webkit-backdrop-filter: blur(30px) saturate(180%);
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 14px 28px;
            border-radius: 50px;
            text-decoration: none;
            color: white;
            font-weight: 700;
            font-size: 15px;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        }}

        .lang-switcher:hover {{
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-4px) scale(1.05);
            box-shadow: 0 12px 48px rgba(0, 0, 0, 0.3);
        }}

        /* 超现代头部 */
        .header {{
            text-align: center;
            padding: 80px 50px;
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(40px) saturate(180%);
            -webkit-backdrop-filter: blur(40px) saturate(180%);
            border: 2px solid rgba(255, 255, 255, 0.25);
            border-radius: 40px;
            margin-bottom: 50px;
            box-shadow: 0 20px 80px rgba(0, 0, 0, 0.3),
                        inset 0 1px 0 rgba(255, 255, 255, 0.4);
            position: relative;
            overflow: hidden;
        }}

        .header::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 6px;
            background: linear-gradient(90deg, #6366f1, #ec4899, #f59e0b, #10b981, #6366f1);
            background-size: 200% 100%;
            animation: shimmer 3s linear infinite;
        }}

        @keyframes shimmer {{
            0% {{ background-position: 0% 0%; }}
            100% {{ background-position: 200% 0%; }}
        }}

        .header h1 {{
            font-size: 64px;
            font-weight: 900;
            color: white;
            margin-bottom: 20px;
            text-shadow: 0 4px 30px rgba(0, 0, 0, 0.3),
                         0 2px 10px rgba(255, 255, 255, 0.2);
            letter-spacing: -2px;
            line-height: 1.1;
        }}

        .header p {{
            color: rgba(255, 255, 255, 0.95);
            font-size: 22px;
            font-weight: 500;
            text-shadow: 0 2px 15px rgba(0, 0, 0, 0.2);
        }}

        /* 超现代导航 */
        .nav-controls {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 50px;
            padding: 0 20px;
        }}

        .nav-arrow {{
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(30px);
            -webkit-backdrop-filter: blur(30px);
            border: 2px solid rgba(255, 255, 255, 0.3);
            color: white;
            width: 72px;
            height: 72px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 36px;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            font-weight: 300;
        }}

        .nav-arrow:hover:not(:disabled) {{
            background: rgba(255, 255, 255, 0.3);
            transform: scale(1.15) translateY(-4px);
            box-shadow: 0 16px 64px rgba(0, 0, 0, 0.3);
        }}

        .item-counter {{
            font-size: 24px;
            color: white;
            font-weight: 800;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(30px);
            -webkit-backdrop-filter: blur(30px);
            border: 2px solid rgba(255, 255, 255, 0.3);
            padding: 20px 40px;
            border-radius: 50px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        }}

        /* 超现代卡片 - 混合Neumorphism和Glassmorphism */
        .clothes-card {{
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(40px) saturate(180%);
            -webkit-backdrop-filter: blur(40px) saturate(180%);
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 40px;
            padding: 0;
            margin-bottom: 50px;
            box-shadow: 0 20px 80px rgba(0, 0, 0, 0.25),
                        inset 0 1px 0 rgba(255, 255, 255, 0.5);
            overflow: hidden;
            position: relative;
            transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
        }}

        .clothes-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 8px;
            background: linear-gradient(90deg, #6366f1, #ec4899, #f59e0b, #10b981);
            background-size: 200% 100%;
            opacity: 0;
            transition: opacity 0.3s;
            animation: shimmer 3s linear infinite;
        }}

        .clothes-card:hover {{
            transform: translateY(-12px) scale(1.01);
            box-shadow: 0 32px 120px rgba(0, 0, 0, 0.35),
                        inset 0 1px 0 rgba(255, 255, 255, 0.6);
        }}

        .clothes-card:hover::before {{
            opacity: 1;
        }}

        .clothes-header {{
            display: grid;
            grid-template-columns: 400px 1fr;
            gap: 50px;
            padding: 50px;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.85) 100%);
        }}

        .clothes-image-wrapper {{
            position: relative;
            border-radius: 30px;
            overflow: hidden;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2),
                        inset 0 1px 0 rgba(255, 255, 255, 0.3);
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }}

        .clothes-cover {{
            width: 100%;
            height: 500px;
            object-fit: cover;
            transition: transform 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
            display: block;
        }}

        .clothes-card:hover .clothes-cover {{
            transform: scale(1.12);
        }}

        .clothes-info {{
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 20px 0;
        }}

        .clothes-title {{
            font-size: 48px;
            font-weight: 900;
            background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 16px;
            line-height: 1.2;
            letter-spacing: -1px;
        }}

        .clothes-category {{
            display: inline-block;
            padding: 10px 24px;
            background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
            color: white;
            border-radius: 50px;
            font-size: 15px;
            font-weight: 700;
            margin-bottom: 30px;
            width: fit-content;
            box-shadow: 0 8px 24px rgba(99, 102, 241, 0.4);
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .user-info {{
            display: flex;
            align-items: center;
            gap: 20px;
            margin-top: auto;
            padding-top: 30px;
            border-top: 2px solid rgba(0, 0, 0, 0.06);
        }}

        .user-avatar {{
            width: 64px;
            height: 64px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid;
            border-image: linear-gradient(135deg, #6366f1, #ec4899) 1;
            flex-shrink: 0;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
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
            font-size: 14px;
            padding: 8px 16px;
            border-radius: 50px;
            background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
            color: #92400e;
            font-weight: 700;
            display: inline-block;
            box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3);
        }}

        .whatsapp-icon {{
            width: 64px;
            height: 64px;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
            border-radius: 50%;
            padding: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 8px 24px rgba(37, 211, 102, 0.4);
        }}

        .whatsapp-icon:hover {{
            transform: scale(1.2) rotate(10deg);
            box-shadow: 0 16px 48px rgba(37, 211, 102, 0.6);
        }}

        .whatsapp-icon svg {{
            width: 32px;
            height: 32px;
            fill: white;
        }}

        .why-release {{
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.06) 0%, rgba(236, 72, 153, 0.06) 100%);
            padding: 50px;
            border-top: 2px solid rgba(0, 0, 0, 0.06);
        }}

        .why-release h4 {{
            font-size: 18px;
            background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
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

        /* 超现代分享按钮 */
        .share-btn {{
            position: absolute;
            top: 40px;
            {'left' if is_rtl else 'right'}: 40px;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(30px);
            -webkit-backdrop-filter: blur(30px);
            border: 2px solid rgba(255, 255, 255, 0.3);
            color: white;
            border-radius: 50px;
            padding: 16px 32px;
            font-size: 16px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 12px;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            z-index: 10;
            font-weight: 700;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        }}

        .share-btn:hover {{
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-4px) scale(1.05);
            box-shadow: 0 16px 64px rgba(0, 0, 0, 0.3);
        }}

        /* 超现代底部按钮 */
        .fixed-bottom-btn {{
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(40px) saturate(180%);
            -webkit-backdrop-filter: blur(40px) saturate(180%);
            border-top: 2px solid rgba(255, 255, 255, 0.25);
            padding: 30px;
            box-shadow: 0 -16px 64px rgba(0, 0, 0, 0.2);
            z-index: 1000;
        }}

        .request-btn {{
            width: 100%;
            max-width: 1400px;
            margin: 0 auto;
            padding: 24px;
            background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
            color: white;
            border: none;
            border-radius: 50px;
            font-size: 22px;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            display: block;
            box-shadow: 0 12px 48px rgba(99, 102, 241, 0.5);
            letter-spacing: 0.5px;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        }}

        .request-btn:hover {{
            transform: translateY(-6px) scale(1.02);
            box-shadow: 0 20px 80px rgba(99, 102, 241, 0.6);
        }}

        /* 超现代模态框 */
        .modal {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
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
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(40px) saturate(180%);
            -webkit-backdrop-filter: blur(40px) saturate(180%);
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 40px;
            max-width: 650px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
            position: relative;
            padding: 60px 50px;
            box-shadow: 0 32px 120px rgba(0, 0, 0, 0.4);
        }}

        .modal-close {{
            position: absolute;
            top: 30px;
            {'left' if is_rtl else 'right'}: 30px;
            background: rgba(0, 0, 0, 0.05);
            border: 2px solid rgba(0, 0, 0, 0.1);
            font-size: 36px;
            cursor: pointer;
            color: var(--text-secondary);
            width: 56px;
            height: 56px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            transition: all 0.3s;
        }}

        .modal-close:hover {{
            background: rgba(0, 0, 0, 0.1);
            transform: rotate(90deg) scale(1.1);
        }}

        .modal-title {{
            font-size: 36px;
            background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 40px;
            text-align: center;
            font-weight: 900;
            letter-spacing: -1px;
        }}

        .form-group {{
            margin-bottom: 32px;
        }}

        .form-group label {{
            display: block;
            margin-bottom: 14px;
            font-weight: 800;
            color: var(--text-primary);
            font-size: 17px;
        }}

        .form-group textarea {{
            width: 100%;
            min-height: 160px;
            padding: 20px;
            border: 2px solid rgba(0, 0, 0, 0.1);
            border-radius: 20px;
            font-family: inherit;
            font-size: 16px;
            resize: vertical;
            transition: all 0.3s;
            background: rgba(255, 255, 255, 0.9);
        }}

        .form-group textarea:focus {{
            outline: none;
            border-color: #6366f1;
            box-shadow: 0 0 0 6px rgba(99, 102, 241, 0.1);
            background: white;
        }}

        .image-upload-area {{
            border: 3px dashed rgba(99, 102, 241, 0.3);
            border-radius: 24px;
            padding: 50px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
            margin-bottom: 24px;
            background: rgba(99, 102, 241, 0.05);
        }}

        .image-upload-area:hover {{
            border-color: #6366f1;
            background: rgba(99, 102, 241, 0.1);
        }}

        .uploaded-image {{
            max-width: 100%;
            max-height: 350px;
            border-radius: 20px;
            margin-top: 24px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
        }}

        .upload-icon {{
            font-size: 64px;
            background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 20px;
        }}

        .submit-btn {{
            width: 100%;
            padding: 24px;
            background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
            color: white;
            border: none;
            border-radius: 50px;
            font-size: 20px;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            margin-top: 40px;
            box-shadow: 0 12px 48px rgba(99, 102, 241, 0.5);
            letter-spacing: 0.5px;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        }}

        .submit-btn:hover {{
            transform: translateY(-4px) scale(1.02);
            box-shadow: 0 20px 80px rgba(99, 102, 241, 0.6);
        }}

        /* 超现代历史交换区 */
        .history-section {{
            margin-top: 60px;
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(40px) saturate(180%);
            -webkit-backdrop-filter: blur(40px) saturate(180%);
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 40px;
            padding: 50px;
            box-shadow: 0 20px 80px rgba(0, 0, 0, 0.25),
                        inset 0 1px 0 rgba(255, 255, 255, 0.5);
        }}

        .history-section h2 {{
            font-size: 40px;
            background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 40px;
            text-align: center;
            font-weight: 900;
            letter-spacing: -1px;
        }}

        .exchange-list {{
            display: flex;
            gap: 30px;
            overflow-x: auto;
            padding: 24px 0;
            scroll-snap-type: x mandatory;
            -webkit-overflow-scrolling: touch;
        }}

        .exchange-item {{
            display: flex;
            align-items: center;
            gap: 24px;
            padding: 36px;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.08) 0%, rgba(236, 72, 153, 0.08) 100%);
            border-radius: 30px;
            min-width: 450px;
            flex-shrink: 0;
            scroll-snap-align: start;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            border: 2px solid rgba(99, 102, 241, 0.15);
        }}

        .exchange-clothes {{
            text-align: center;
            flex: 1;
        }}

        .exchange-clothes img {{
            width: 120px;
            height: 180px;
            object-fit: cover;
            border-radius: 20px;
            margin-bottom: 16px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
        }}

        .exchange-clothes p {{
            font-size: 15px;
            font-weight: 800;
            line-height: 1.4;
            color: var(--text-primary);
        }}

        .exchange-icon {{
            font-size: 48px;
            background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .exchange-date {{
            font-size: 14px;
            color: var(--text-secondary);
            text-align: center;
            margin-top: 16px;
            font-weight: 600;
        }}

        /* 响应式设计 */
        @media (max-width: 968px) {{
            .clothes-header {{
                grid-template-columns: 1fr;
                gap: 40px;
            }}

            .clothes-cover {{
                height: 400px;
            }}

            .header h1 {{
                font-size: 48px;
            }}

            .clothes-title {{
                font-size: 36px;
            }}
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 30px 15px;
            }}

            .header {{
                padding: 50px 30px;
            }}

            .header h1 {{
                font-size: 40px;
            }}

            .clothes-header {{
                padding: 40px 30px;
            }}

            .share-btn {{
                position: static;
                width: 100%;
                margin-top: 24px;
            }}

            .exchange-item {{
                flex-direction: column;
                min-width: 320px;
            }}

            .lang-switcher {{
                top: 20px;
                {'right' if is_rtl else 'left'}: 20px;
                padding: 12px 24px;
                font-size: 14px;
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
                    <p style="color: var(--text-secondary); font-size: 17px;">{translations['upload_photo']}</p>
                    <img id="uploadedImagePreview" class="uploaded-image" style="display: none;">
                </div>
                <input type="file" id="itemImageInput" accept="image/*" style="display: none;" onchange="handleImageUpload(event)">
            </div>
            
            <div class="whatsapp-display" id="whatsappDisplay" style="display: none; margin-top: 32px; padding: 32px; background: linear-gradient(135deg, rgba(37, 211, 102, 0.1) 0%, rgba(37, 211, 102, 0.05) 100%); border-radius: 24px; text-align: center;">
                <p style="color: #155724; font-weight: 800; margin-bottom: 16px; font-size: 20px;">{translations['request_sent']}</p>
                <p style="color: var(--text-secondary); font-size: 16px;">{translations['contact_owner']}:</p>
                <a href="https://wa.me/{translations['whatsapp_number'].replace('+', '').replace(' ', '')}" target="_blank" class="whatsapp-link" id="whatsappLink" onclick="openWhatsApp(items[currentItemIndex].id); return true;" style="display: inline-flex; align-items: center; gap: 14px; color: #25D366; text-decoration: none; font-weight: 800; font-size: 22px; margin-top: 20px; padding: 20px 40px; background: white; border-radius: 50px; transition: all 0.3s; box-shadow: 0 8px 32px rgba(37, 211, 102, 0.3);">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/>
                    </svg>
                    {translations['whatsapp_number']}
                </a>
            </div>

            <button class="submit-btn" onclick="submitExchange()" id="submitBtn">
                🤝 {translations['send_request']}
            </button>

            <div class="success-message" id="successMessage" style="display: none; margin-top: 32px; padding: 32px; background: linear-gradient(135deg, rgba(37, 211, 102, 0.1) 0%, rgba(37, 211, 102, 0.05) 100%); border-radius: 24px; color: #155724; text-align: center; font-size: 18px; font-weight: 700;">
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

            // 使用绝对URL确保图片能加载
            const imageUrl = item.cover.startsWith('http') ? item.cover : 
                           (item.cover.startsWith('/') ? window.location.origin + item.cover : 
                           window.location.origin + '/static/' + item.cover.replace('/static/', ''));

            itemDisplay.innerHTML = `
                <div class="clothes-card">
                    <div class="clothes-header">
                        <div class="clothes-image-wrapper">
                            <img src="${{encodeURI(imageUrl)}}" alt="${{item.title}}" class="clothes-cover" loading="lazy" onerror="this.onerror=null; this.style.display='none'; this.nextElementSibling.style.display='block';">
                            <div style="display: none; width: 100%; height: 500px; background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); border-radius: 30px; display: flex; align-items: center; justify-content: center; color: #6b7280; font-size: 24px; font-weight: 600;">图片加载中...</div>
                        </div>
                        <div class="clothes-info">
                            <div>
                                <div class="clothes-title">${{item.title}}</div>
                                <span class="clothes-category">${{item.category}}</span>
                            </div>
                            <div class="user-info">
                                <img src="${{item.user.avatar}}" alt="${{item.user.name}}" class="user-avatar" onerror="this.onerror=null; this.src='data:image/svg+xml,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\'%3E%3Crect width=\\'64\\' height=\\'64\\' fill=\\'%236366f1\\'/%3E%3Ctext x=\\'50%25\\' y=\\'50%25\\' fill=\\'white\\' text-anchor=\\'middle\\' dominant-baseline=\\'central\\' font-size=\\'28\\' font-weight=\\'bold\\'>${{item.user.name.charAt(0)}}</text%3E%3C/svg%3E';">
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
                <div style="min-width: 450px; flex-shrink: 0;">
                    <div class="exchange-item">
                        <div class="exchange-clothes">
                            <img src="${{encodeURI(img1Url)}}" alt="${{ex.item1.title}}" loading="lazy" onerror="this.onerror=null; this.style.display='none';">
                            <p>${{ex.item1.title}}</p>
                            <p style="font-size: 13px; color: var(--text-secondary); margin-top: 8px; font-weight: 600;">${{ex.item1.user}}</p>
                        </div>
                        <div class="exchange-icon">🤝</div>
                        <div class="exchange-clothes">
                            <img src="${{encodeURI(img2Url)}}" alt="${{ex.item2.title}}" loading="lazy" onerror="this.onerror=null; this.style.display='none';">
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
    print('✅ 已生成超高级UI模板（阿拉伯语）')
    
    zh_html = generate_template('zh', ZH_TRANSLATIONS, CLOTHES_DATA_ZH)
    with open('templates/index_zh.html', 'w', encoding='utf-8') as f:
        f.write(zh_html)
    print('✅ 已生成超高级UI模板（中文）')

