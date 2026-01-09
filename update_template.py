#!/usr/bin/env python3
"""
更新模板文件，将书籍数据替换为衣服数据
"""
from clothes_data import CLOTHES_DATA, SAMPLE_EXCHANGES

# 读取模板文件
with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 生成衣服数据的 JavaScript
clothes_js = "        // 衣服数据（15件衣服）\n        const books = [\n"
for i, item in enumerate(CLOTHES_DATA):
    # 转义单引号
    why_release = item['why_release'].replace("'", "\\'").replace("\n", " ")
    clothes_js += f"""            {{
                id: {item['id']},
                title: '{item['title']}',
                author: '{item.get('category', 'Clothing')}',
                cover: '{item['cover']}',
                why_release: '{why_release}',
                user: {{ name: '{item['user']['name']}', avatar: '{item['user']['avatar']}', trust_badge: '{item['user']['trust_badge']}' }}
            }}"""
    if i < len(CLOTHES_DATA) - 1:
        clothes_js += ",\n"
    else:
        clothes_js += "\n"
clothes_js += "        ];"

# 找到并替换书籍数据
import re
pattern = r'// 衣服数据（15件衣服）\s+const books = \[.*?\];'
content = re.sub(pattern, clothes_js, content, flags=re.DOTALL)

# 生成交换历史数据
exchanges_js = "        // 历史交换记录（最近一个月）\n        const exchanges = [\n"
for i, ex in enumerate(SAMPLE_EXCHANGES):
    exchanges_js += f"""            {{
                item1: {{ title: '{ex['item1']['title']}', cover: '{ex['item1']['cover']}', user: '{ex['item1']['user']}' }},
                item2: {{ title: '{ex['item2']['title']}', cover: '{ex['item2']['cover']}', user: '{ex['item2']['user']}' }},
                date: '{ex['date']}'
            }}"""
    if i < len(SAMPLE_EXCHANGES) - 1:
        exchanges_js += ",\n"
    else:
        exchanges_js += "\n"
exchanges_js += "        ];"

# 替换交换历史数据（找到旧的交换数据部分）
pattern2 = r'// 历史交换记录.*?const exchanges = \[.*?\];'
content = re.sub(pattern2, exchanges_js, content, flags=re.DOTALL)

# 更新其他文本
content = content.replace('book1', 'item1')
content = content.replace('book2', 'item2')
content = content.replace('exchange.book1', 'exchange.item1')
content = content.replace('exchange.book2', 'exchange.item2')

# 更新分享文本
old_share = '¿Tienes libros que ya leíste? En Trueque Digital los cambias por nuevas historias con lectores de Dubai, Abu Dhabi y de todo el Medio Oriente.'
new_share = 'Do you have clothes you no longer wear? Exchange them for new styles with fashion lovers in Dubai, Abu Dhabi, and across the Middle East.'
content = content.replace(old_share, new_share)

# 保存文件
with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ 模板文件已更新！")

