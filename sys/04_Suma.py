#! /usr/bin/python3 - shebang
import sys

suma = 0.0
print(type(suma))
print("Entrada de sys: ",sys.argv)
print("Argumentos de sys: ",sys.argv[1:])
if len(sys.argv) > 1:
    for i in range(1,len(sys.argv)):
        num = float(sys.argv[i])
        suma += num
print(suma)
print(type(suma))

