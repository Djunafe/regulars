"""Задание 3"""
"""Написать пример регулярного выражения, которое совпадает с 'd', 'dog', 'dogog', но не совпадает с 'dogogog'."""

import re

my_text = 'd  dogogog dog fgdhj edog dgo dogog dogogog dogogogog'
results = re.findall(r'd(?:og){,2}', my_text)
print(results)
