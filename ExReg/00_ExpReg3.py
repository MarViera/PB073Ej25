import re
patron = r'\((\d{2})\)(\d{4})-(\d{4})'
cad = 'Mi numero es (81)8329-4000 y el (81)8329-4030'
print("Agrupando datos")
expresion_telefono = re.compile(patron)
mo = expresion_telefono.findall(cad)
print(mo)
print("Sin agrupar datos")
patron = r'\(\d{2}\)\d{4}-\d{4}'
expresion_telefono = re.compile(patron)
cad = 'Mi numero es (81)8329-4000 y el (81)8329-4030'
mo = expresion_telefono.findall(cad)
print(mo)

