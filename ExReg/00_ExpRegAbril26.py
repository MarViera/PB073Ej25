import re
#Patrón para numeros teléfonicos
patron = r'\(?(\d\d)\)?(\d{4}-?\d{4})'
#patron = r'(\d{2})(\d{8})'
expresion_telefono = re.compile(patron)#Empiezan con r
cadena = 'Mi numero es (81)8329-4000.'
#cadena = 'Mi numero es 8183294000.'
#cadena = 'Mi numero es (81)83294000.'
#cadena = 'Mi numero es 818329-4000.'
#cadena = input("Ingresa texto: ")
mo = expresion_telefono.search(cadena)
#print(mo)
#print(type(mo))
#input()
if mo != None:
    print("Teléfono completo", mo.group())
    print("Lada local", mo.group(1))
    print("Número telefónico", mo.group(2))
    #print(type(mo.group()))
else:
    print("No se encontraron números telefónicos")
