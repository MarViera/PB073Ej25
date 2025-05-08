from sympy import Symbol, Derivative, sin

t = Symbol('t')
St = 5*t**2 + 2*t + 8 + sin(t)

d = Derivative(St, t)
print("Derivada de ",St)
print(d.doit())
input()
x = Symbol('x')
f = (x**3 + x**2 + x)*(x**2+x)
print("Derivada de ",f)
print(Derivative(f, x).doit())
