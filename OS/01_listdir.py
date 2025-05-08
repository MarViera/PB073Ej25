import os
#La dirección de la carpeta
# lista el contenido de un directorio
# default "."
cosa = "C:\\Users\\Mar\\Pictures\\Disney"
archivos = os.listdir(cosa) #dir, ls, Get-ChildItem
#print(archivos,"\t",len(archivos))#Lista
#input()
for i in archivos:
    if ".pdf" in i:
        print(i)
