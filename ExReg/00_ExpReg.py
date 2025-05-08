import re
#Patrón para numeros teléfonicos
patron = r'\(\d{2}\)\d{4}-\d{4}'
expresion_telefono = re.compile(patron)#Empiezan con r
cadena = 'Mi numero es (81)83294000.'
#cadena = input("Ingresa texto: ")
mo = expresion_telefono.search(cadena)
print(mo)
print(type(mo))
input()
if mo != None:
    print(mo.group())
    print(type(mo.group()))
else:
    print("No se encontraron números telefónicos")
