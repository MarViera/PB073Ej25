from statistics import median, mean, mode
import random

calificaciones = list()
for i in range(2500): #Cambiar a número par para ver la diferencia
    calificaciones.append(random.randint(0,100))

print(calificaciones)
print("La promedio de las calificaciones es: ",
      mean(calificaciones))
print("La mediana de las calificaciones es: ",
      median(calificaciones))
print("La moda de las calificaciones es: ",
      mode(calificaciones))




#Verificación
#calificaciones.sort()
#print(calificaciones)
#print(calificaciones[12])
