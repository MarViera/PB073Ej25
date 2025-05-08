#Agrupemos --> método group
import re

cadena = "El numero es (81)8329-4000 pero no me se la extensión"
patron1 = re.compile(r'(\(\d{2}\))(\d{4})-(\d{4})')
mo = patron1.search(cadena)
print ("Número encontrado: " + mo.group())
print ("Lada", mo.group(1)) #(81)
print ("Numero",mo.group(2),mo.group(3))

#Creamos un patrón con grupos, ponemos entre paréntesis
# todos los grupos que querramos armar
# los paréntesis no deben tener \ previo
patron2 = re.compile(r'\((\d{2})\)(\d{4})-(\d{4})')
mo = patron2.search(cadena)
print ("Número encontrado: " + mo.group())
print ("Lada", mo.group(1)) #81
print ("Numero",mo.group(2),mo.group(3))
