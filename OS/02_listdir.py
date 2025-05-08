import os

archivos = os.listdir()
print(archivos)
input()
for i in archivos:
    if ".txt" in i:
        with open (str(i),'r') as file:
            print('Contenido de archivo',str(i))
            for line in file:
               print(line,end='')
