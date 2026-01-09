#!/usr/bin/env python3
"""
生成衣服数据的 JavaScript 代码
"""
from clothes_data import CLOTHES_DATA

js_code = "        // 衣服数据（15件衣服）\n        const books = [\n"

for i, item in enumerate(CLOTHES_DATA):
    js_code += f"""            {{
                id: {item['id']},
                title: '{item['title']}',
                author: '{item.get('category', 'Clothing')}',
                cover: '{item['cover']}',
                why_release: `{item['why_release']}`,
                user: {{ name: '{item['user']['name']}', avatar: '{item['user']['avatar']}', trust_badge: '{item['user']['trust_badge']}' }}
            }}"""
    if i < len(CLOTHES_DATA) - 1:
        js_code += ",\n"
    else:
        js_code += "\n"

js_code += "        ];"

print(js_code)

