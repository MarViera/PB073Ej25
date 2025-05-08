import re
expresion_telefono = re.compile(r'\((\d{2})\)(\d{4})-(\d{4})')
mo = expresion_telefono.search('Mi numero es (81)8329-4000.')
print(mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group(2),mo.group(3))

