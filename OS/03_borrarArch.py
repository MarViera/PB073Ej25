import os

##Creamos un el archivo y colocamos contenido
fo = open ("Renombre1.txt","w")
fo.write("Hola mundo!!!")
fo.close()
input()
#os.remove("Renombre.txt")
try:
    os.remove("Renombre1.txt")
    ## En windows lanza la excepcion
    ## FileNotFoundError: si no existe el archivo
except OSError:
    print("No se encontro el archivo")
    archivos = os.listdir()
    print(archivos)
#Aqui sigue el programa
print("Aqui")
