#! /usr/bin/python3 - shebang
import sys

print("Entrada de sys: ",sys.argv)
print("Argumentos de sys: ",sys.argv[1:])
if len(sys.argv) > 1:
    for i in range(1,len(sys.argv)):
        print(sys.argv[i], "--> tipo:",type(sys.argv[i]))
print("Fin")
