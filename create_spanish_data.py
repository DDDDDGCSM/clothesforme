#!/usr/bin/env python3
"""
创建西班牙语衣服数据
基于CLOTHES_DATA_AR翻译成西班牙语
"""
from translations import CLOTHES_DATA_AR

# 西语翻译映射
SPANISH_TRANSLATIONS = {
    'مايوه أنيق': 'Traje de baño elegante',
    'ملابس السباحة': 'Traje de baño',
    'كالجديد': 'Como nuevo',
    'طقم صيفي كاجوال': 'Conjunto casual de verano',
    'كاجوال': 'Casual',
    'ممتاز': 'Excelente',
    'زي عمل احترافي': 'Atuendo profesional',
    'عمل': 'Profesional',
    'أزياء الشارع العصرية': 'Moda callejera moderna',
    'جيد': 'Bueno',
    'فستان أنيق': 'Vestido elegante',
    'فستان': 'Vestido',
    'قميص كاجوال': 'Camisa casual',
    'قميص': 'Camisa',
    'زي عصري': 'Atuendo moderno',
    'عصري': 'Moderno',
    'قطعة كلاسيكية': 'Pieza clásica',
    'كلاسيكي': 'Clásico',
    'زي جريء': 'Atuendo llamativo',
    'جريء': 'Llamativo',
    'زي متعدد الاستخدامات': 'Atuendo versátil',
    'متعدد الاستخدامات': 'Versátil',
    'فستان مناسبة خاصة أنيق': 'Vestido elegante para ocasión especial',
    'بيجامة مريحة': 'Pijama cómodo',
    'ملابس النوم': 'Ropa de dormir',
    'مجموعة مجلات أزياء': 'Colección de revistas de moda',
    'مجلة': 'Revista',
    'مجلة أزياء للتبادل': 'Revista de moda para intercambio',
    '⭐ عضو موثوق': '⭐ Miembro de confianza',
    '🌙 عضو جديد': '🌙 Nuevo miembro',
}

# 西语描述模板
SPANISH_DESCRIPTIONS = [
    "Quiero intercambiar este traje de baño impresionante porque busco algo que haga que todas las miradas se vuelvan hacia mí en la playa. Esta pieza ha sido mi arma secreta para atraer atención, y estoy lista para intercambiarla por algo que me haga sentir aún más irresistible. Perfecto para alguien que quiere verse absolutamente cautivador.",
    "Quiero intercambiar este conjunto casual porque busco algo que capture tu atención instantáneamente. Esta pieza ha sido mi favorita para hacer una declaración audaz, y estoy lista para cambiarla por algo que me haga sentir aún más seductora. Ideal para alguien que quiere verse con un estilo relajado y seductor.",
    "Quiero intercambiar este atuendo profesional porque busco algo que me haga sentir poderosa e irresistible. Este conjunto ha sido mi impulsor de confianza, y ahora quiero intercambiarlo por algo que me haga sentir aún más deseable. Perfecto para alguien que quiere verse tanto profesional como absolutamente cautivador.",
    "Quiero intercambiar este conjunto de moda porque busco algo que me haga sentir más seductora. Esta pieza ha sido mi favorita para llamar la atención, y estoy lista para cambiarla por algo que me haga sentir aún más irresistible. Ideal para alguien que quiere verse con un estilo relajado, sexy y seductor.",
    "Quiero intercambiar este conjunto cómodo porque busco algo que me haga sentir más atractiva. Esta pieza ha sido mi elección cómoda, pero ahora quiero algo que me haga sentir aún más atractiva y seductora. Perfecto para alguien que quiere verse cómodo y absolutamente irresistible.",
    "Quiero intercambiar este vestido elegante porque busco algo que me haga sentir más irresistible. Esta pieza ha sido mi arma secreta para ocasiones especiales, y ahora quiero cambiarla por algo que me haga sentir aún más cautivadora. Ideal para alguien que quiere verse impresionante y absolutamente seductor.",
    "Quiero intercambiar esta camisa casual porque busco algo que me haga sentir más atractiva. Esta pieza ha sido mi favorita para lucir increíble, y ahora quiero intercambiarla por algo que me haga sentir aún más deseable. Perfecto para alguien que quiere verse con un estilo relajado, sexy y seductor.",
    "Quiero intercambiar este atuendo moderno porque busco algo que me haga sentir más seductora. Esta pieza ha sido mi favorita para atraer atención, y estoy lista para cambiarla por algo que me haga sentir aún más irresistible. Ideal para alguien que quiere verse con un estilo moderno y absolutamente cautivador.",
    "Quiero intercambiar esta pieza clásica porque busco algo que me haga sentir más atractiva. Esta pieza ha sido mi elección clásica, pero ahora quiero algo que me haga sentir aún más atractiva y seductora. Perfecto para alguien que quiere verse elegante y absolutamente irresistible.",
    "Quiero intercambiar este atuendo llamativo porque busco algo que me haga sentir más irresistible. Esta pieza ha sido mi elección audaz para llamar la atención, y ahora quiero cambiarla por algo que me haga sentir aún más cautivadora. Ideal para alguien que quiere verse impresionante y absolutamente seductor.",
    "Quiero intercambiar este atuendo versátil porque busco algo que me haga sentir más atractiva. Esta pieza ha sido mi elección confiable, y ahora quiero intercambiarla por algo que me haga sentir aún más deseable. Perfecto para alguien que quiere verse con un estilo relajado, sexy y seductor.",
    "Quiero intercambiar este atuendo para ocasión especial porque busco algo que me haga sentir más seductora. Esta pieza ha sido mi favorita para celebraciones, y estoy lista para cambiarla por algo que me haga sentir aún más irresistible. Ideal para alguien que quiere verse con un estilo moderno y absolutamente cautivador.",
    "Quiero intercambiar este pijama cómodo porque busco algo que me haga sentir más atractiva. Esta pieza ha sido mi elección cómoda, pero ahora quiero algo que me haga sentir aún más atractiva y seductora. Perfecto para alguien que quiere verse cómodo y absolutamente irresistible.",
    "Quiero intercambiar esta colección de revistas de moda porque busco algo que me inspire a lucir más irresistible. Esta colección ha sido mi guía de estilo, y ahora quiero cambiarla por algo que me haga sentir aún más cautivadora. Ideal para alguien que quiere mantenerse actualizado con las tendencias de moda seductoras.",
    "Quiero intercambiar esta revista de moda porque busco algo que me haga sentir más atractiva. Esta revista ha sido mi fuente de inspiración, y ahora quiero intercambiarla por algo que me haga sentir aún más deseable. Perfecto para alguien que quiere descubrir cómo verse absolutamente irresistible.",
]

CLOTHES_DATA_ES = []
for i, item_ar in enumerate(CLOTHES_DATA_AR):
    item_es = item_ar.copy()
    # 翻译标题
    item_es['title'] = SPANISH_TRANSLATIONS.get(item_ar['title'], item_ar['title'])
    # 翻译类别
    item_es['category'] = SPANISH_TRANSLATIONS.get(item_ar['category'], item_ar['category'])
    # 翻译状态
    item_es['condition'] = SPANISH_TRANSLATIONS.get(item_ar['condition'], item_ar['condition'])
    # 使用西语描述
    if i < len(SPANISH_DESCRIPTIONS):
        item_es['why_release'] = SPANISH_DESCRIPTIONS[i]
    # 翻译用户徽章
    item_es['user']['trust_badge'] = SPANISH_TRANSLATIONS.get(item_ar['user']['trust_badge'], item_ar['user']['trust_badge'])
    CLOTHES_DATA_ES.append(item_es)

if __name__ == '__main__':
    # 将CLOTHES_DATA_ES添加到translations.py
    import re
    with open('translations.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已存在CLOTHES_DATA_ES
    if 'CLOTHES_DATA_ES = [' not in content:
        # 找到CLOTHES_DATA_AR的结束位置
        pattern = r'(CLOTHES_DATA_AR = \[.*?\n\])'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            # 在CLOTHES_DATA_AR后添加CLOTHES_DATA_ES
            es_data_str = '\n\n# 衣服数据的西班牙语翻译\nCLOTHES_DATA_ES = ' + repr(CLOTHES_DATA_ES).replace("'", '"').replace('True', 'true').replace('False', 'false')
            content = content[:match.end()] + es_data_str + '\n'
            with open('translations.py', 'w', encoding='utf-8') as f:
                f.write(content)
            print('✅ 已创建CLOTHES_DATA_ES并添加到translations.py')
        else:
            print('❌ 未找到CLOTHES_DATA_AR，无法添加CLOTHES_DATA_ES')
    else:
        print('✅ CLOTHES_DATA_ES已存在')
    
    print(f'✅ 已创建{len(CLOTHES_DATA_ES)}个西语衣服数据项')

