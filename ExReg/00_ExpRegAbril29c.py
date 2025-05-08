import re
#Patrón para numeros teléfonicos
patron = r'\(?(\d\d)\)?(\d{4}-?\d{4})'
expresion_telefono = re.compile(patron)#Empiezan con r
cadena = '''El número de la UANL es (81)8329-4000.
Pero el número de FCFM es 8183294030 y el de Escolar y archivo es (81)83204001.'''

mo = expresion_telefono.findall(cadena)
print(mo)
print(type(mo))
for tel in mo:
    print("("+tel[0]+")",tel[1])
