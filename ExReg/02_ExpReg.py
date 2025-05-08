#Agrupemos --> método group
import re

cadena = "El numero es (81)8329-4000 pero no me se la extensión"
patron1 = re.compile(r'\(\d{2}\)\d{4}-\d{4}') #(agrupar)
mo = patron1.search(cadena)
if mo != None:
    print('Número encontrado: ' + mo.group())
input("Aquí")
#La siguiente línea no funciona porque no hay
# agrupaciones en el patrón (no hay paréntesis)
#print('Grupo encontrado: ' + mo.group(1))
#Quita comentario para probar que falla

#Creamos un patrón con grupos, ponemos entre paréntesis
# todos los grupos que querramos armar
# los paréntesis no deben tener \ previo
patron2 = re.compile(r'\((\d{2})\)(\d{4})-(\d{4})')
# al leer el patrón tenemos:
#    2 dígitos entre paréntesis
#    4 dígitos
#    4 dígitos
mo = patron2.search(cadena)
print ("Número encontrado: " + mo.group())#por default enviaramos un 0
print ("Lada", mo.group(1))
print ("Numero",mo.group(2),mo.group(3))
# Cómo saber la cantidad de grupos??
print("Cantidad de grupos: ",len(mo.groups()))

# Resumen
# mo.group() --> Nos da la cadena encontrada que corresponde al patrón
# mo.group(i) --> Nos da el grupo específico, en este caso el índice comienza en 1
# ya que en mo.group(), es como si enviáramos mo.group(0), observa:
print ("Grupo 0: " + mo.group(0))


