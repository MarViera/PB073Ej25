numeros = list()
#Leemos el archivo
with open("1erParcialPB073.txt","r") as file:
    for line in file:
        numeros.append(line)
#Qué tipo de dato es cada elemento de la lista?
for i in range(len(numeros)):
    print("Tipo:",type(numeros[i]),numeros[i])
    numeros[i] = int(numeros[i])
    if (numeros[i] > 65) & (numeros[i] < 96):
        numeros[i]+=5
    elif (numeros[i] >= 96):
        numeros[i] = 100
print(numeros)
fo = open("1erParcialPB.txt","w")
#Como guardamos cada elemento de la lista en un archivo
for calificacion in numeros:
    fo.write(str(calificacion)+'\n')
fo.close()
