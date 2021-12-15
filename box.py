import re

"""Задание 2"""
"""Записать пример регулярного выражения, которое совпадает сразу с тремя строками: 'dog', 'box', 'bog'."""

my_text = 'e ffedog nnsbox ms; bogwwd'
results = re.findall(r'[db]o[xg]', my_text)
print(results)

"""Написать пример регулярного выражения, которое не совпадает сразу с тремя строками: 
'dog', 'box, 'bog', но совпадает с 'cot'."""

my_text2 = 'e cot ffcotedog nnsbox cotms; bogwwcotdrot'
results2 = re.findall(r'(?:cot(?!dog)(?!box)(?!bog))', my_text2)     # or [c[^db]o[^gx](?<=t)
print(results2)
