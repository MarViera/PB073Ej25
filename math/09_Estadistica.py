from statistics import mean
import random

calificaciones = list()
for i in range(250):
    calificaciones.append(random.randint(0,100))

print(calificaciones)
print("La calificación que más se repite es: ",
      mean(calificaciones))
'''
lista = ["a", "a", "b", "c", "a"]
print("La letra que más se repite es: ",
      mode(lista))
'''
