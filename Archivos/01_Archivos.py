#Ejemplo 01 de Archivos
#Se crea el flujo (puente) hacia el archivo
fo = open("PB073EJ2025.txt","a")
#Modos de abrir un archivo
# r --> leer
# w --> escribir
# a --> appending (agregar)
# r+ --> lectura y escritura
print(fo)
#Nos dice que archivo abre y su codificación
#Usamos el método write
variable = """ Hola mensaje
grandote versión 2
Bye!\n"""
fo.write (variable)
fo.write ("\nAdios mundo!\n")
fo.write (str(51)) #Debemos convertir a string
fo.write ("LCC y LSTI rulz\n")

#Cerramos el flujo hacia el archivo
fo.close()

#Intentamos escribir más
fo.write("Adios mundo!")
