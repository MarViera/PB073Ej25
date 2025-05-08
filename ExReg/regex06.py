#Agrupemos --> método group
import re

cadena1 = "El numero es (81)8329-4000 pero no me se la extensión"
cadena2 = "(81)8329-4000"
regex = r'\(\d{2}\)\d{4}-\d{4}'
patron = re.compile(regex)
mo = patron.search(cadena1)
print ("Número encontrado: " + mo.group())
mo = patron.search(cadena2)
print ("Número encontrado: " + mo.group())

input("Diferencia entre search y match")
mo = re.match(patron,cadena1)
if mo:
    print("Si hay coincidencia exacta:", mo.group())
else:
    print("No hay coincidencia")
mo = re.match(patron,cadena2)
if mo:
    print("Si hay coincidencia exacta:", mo.group())
else:
    print("No hay coincidencia")


