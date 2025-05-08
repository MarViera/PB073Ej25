from statistics import mean
#import statistics
from fractions import Fraction as F
from decimal import Decimal as D
import random

listaInt = list()
listaFloat = list()
listaDec = list()
listaFrac = list()
for i in range(5):
    listaInt.append(random.randint(1,100))
    listaFloat.append(random.random())
    var = str(random.random()+random.randint(0,10))
    var = var[:5]
    listaDec.append(D(var))
    listaFrac.append(F(random.randint(1,10),random.randint(1,10)))

#Imprimimos
print(listaInt, "Media: ", mean(listaInt))
print(listaFloat, "Media: ", mean(listaFloat))
print(listaDec, "Media: ", mean(listaDec))
print(listaFrac, "Media: ", mean(listaFrac))


    
    
