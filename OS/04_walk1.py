import os

#Pedir direccion al usuario
#Abrir los archivo txt en esa direccion
count = 0 #Contar archivos
ruta = "C:\\Users\\Mar\\Pictures\\Disney"
#ruta = "."
print(os.walk(ruta))
input()
for dirpath, dirnames, filenames in os.walk(ruta):
##    Listamos los nombres de archivos
    print(dirpath)
    print(dirnames)
    print(filenames)
    input()
    for name in filenames:
        print ("Archivo",count,":",
               os.path.join(dirpath,name))
        count +=1
        if name == "Renombre1.txt":
            os.rename ("Renombre1.txt","Renombradote2.txt")
            print ("Revisa la carpeta, el archivo cambio de nombre")    
