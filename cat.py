import re

"""Написать пример регулярного выражения, которое совпадает сразу с тремя строками: 'cat', 'cbt', 'ctt'."""

my_text = 'docat dmcbts ttctttt dcatdcaat '
results = re.findall(r'c(?:at|bt|tt)}', my_text)    # or  'c[abt][t]'   or 'c[ab]?[t]{1,2}'
print(results)

"""Написать пример регулярного выражения, которое не совпадает сразу с тремя строками: 'cat', 'cbt', 'ctt'. """

my_text2 = 'docatdmcbtsttcttttdcatdcaat'
results2 = re.findall(r'.(?:(?!cat)(?!cbt)(?!ctt)).', my_text2)
print(results2)

"""Написать пример регулярного выражения, которое совпадает с 'c', 'cat', 'catat' или 'catatatatat"""

my_text3 = 'cdocat dmcatatbts ttctttt dcatdcaatee ddcatatatatatatatat ycatatata'
results3 = re.findall(r'c(?:at){5}|c(?:at){,2}', my_text3)
print(results3)

"""Написать пример регулярного выражения, которое совпадает с 'c', 'cat', но не будет совпадать целиком с 'catat'
 или 'catatatatat, а будет совпадать с 'cat' в них"""

my_text4 = 'cdocat dcmcbcatts ttctttt dcatdcaatcatc'
results4 = re.findall(r'cat|c', my_text4)   # or 'c(?:at|)'     or c(?:at)?
print(results4)
