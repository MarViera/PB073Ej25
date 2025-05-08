from sympy import Symbol, Derivative
from sympy.plotting import plot

t = Symbol('t')
St = 5*t**2 + 2*t + 8
print("Derivada de ",St)
dSt = Derivative(St, t).doit()
print("dSt = ",dSt)

p = plot(St, dSt,(t, -5, 5),
     title='Función y derivada',
     xlabel='t',
     ylabel='St y su derivada',
     show=True,
     legend=True)
