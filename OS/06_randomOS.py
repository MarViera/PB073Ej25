#Cosas random con os
import os

print("SO: ",os.name)
print("Directorio actual: ",os.getcwd())
print("Archivos\n",os.listdir())
#C:\Users\marle\Desktop
directorio = input("Moverse al directorio: ")
os.chdir(directorio)
input()
print("**Nuevo directorio actual: ",os.getcwd())
print("Archivos\n",os.listdir())

carpeta = input("Carpeta nueva: ")
os.mkdir(carpeta)
print("Archivos\n",os.listdir())
input()
os.rmdir(carpeta)
