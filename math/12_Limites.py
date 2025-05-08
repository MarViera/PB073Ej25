from sympy import Limit, Symbol, S, sin

x = Symbol('x')
print('Infinito: ',S.Infinity)
input()
Limit(1/x, x, S.Infinity)
print(Limit(1/x, x, S.Infinity))
input()
l = Limit(1/x, x, S.Infinity)
print("R =",l.doit())
input()
#Otro límite
print("Calcular: ", Limit(sin(x)/x, x, 0))
print(Limit(sin(x)/x, x, 0).doit())

#Otro límite
n = Symbol('n')
print("Calcular: ", Limit((1+1/n)**n, n, S.Infinity))
print(Limit((1+1/n)**n, n, S.Infinity).doit())
