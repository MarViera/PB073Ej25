from collections import Counter
import random

calificaciones = list()
for i in range(40): 
    calificaciones.append(random.randint(0,10))
print(calificaciones)
frec = Counter(calificaciones)
print(frec)
print("Frecuencia de aparición ", frec.most_common())
print("Dato con más apariciones ", frec.most_common(1))
print("Top 3 con más apariciones ", frec.most_common(3))
input()
#Imprimir bonito la tabla de frecuencias
print('{0}\t{1}'.format("Calificación","Apariciones"))
for calif in frec.most_common():
    print('{0}\t\t\t{1}'.format(calif[0],calif[1]))
print(frec.most_common()[0][0])
input()

#Imprimir bonito la tabla de frecuencias
print('{0}\t{1}'.format("Calificación","Apariciones"))
tuplaFrec = frec.most_common()
tuplaFrec.sort(reverse=True)
for calif in tuplaFrec:
    print('{0}\t\t\t{1}'.format(calif[0],calif[1]))
