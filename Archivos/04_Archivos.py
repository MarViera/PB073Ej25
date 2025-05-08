import random

numeros = list()
for i in range(28):
    numeros.append(random.randint(0,100))

fo = open("1erParcialPB073.txt","w")
print(numeros)
#Como guardamos cada elemento de la lista en un archivo
for calificacion in numeros:
    fo.write(str(calificacion)+'\n')

#for i in range(len(numeros)): 
#    fo.write(str(numeros[i])+'\n')
fo.close()

