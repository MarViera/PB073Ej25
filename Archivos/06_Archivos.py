numeros = list()

#Leemos el archivo
with open("Evaluaciones.txt","r") as file:
    for line in file:
        numeros.append(int(line))#Convierto a int

#Qué tipo de dato es cada elemento de la lista?
print("Calificaciones sin puntos extra: ")
for i in range(len(numeros)):
    print(numeros[i])
    numeros[i]+=10

print("Calificaciones con puntos extra: ")
fo = open("Evaluaciones.txt","w")
for i in range(len(numeros)):
    print(numeros[i])
    fo.write(str(numeros[i])+'\n')

fo.close()




