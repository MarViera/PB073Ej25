import os
#La dirección de la carpeta
# lista el contenido de un directorio
# default "."
archivos = os.listdir("C:/Users/marle/Pictures/Screenshots") #dir, ls, Get-ChildItem
print(archivos)#Lista
for i in archivos:
    print(i)
