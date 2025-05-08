import re
#Patrón para numeros teléfonicos
#patron = r'[0-9]{5}\D'
patron = r'\w*'
expresion_cp= re.compile(patron)#Empiezan con r
cadena = '''66455, 66620 y 36670.'''

mo = expresion_cp.findall(cadena)
print(mo)
print(type(mo))
for cp in mo:
    print(cp)
