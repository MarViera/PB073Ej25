from sympy.plotting import plot
from sympy import Symbol
x = Symbol('x')
p = plot(2*x+3,
         3*x+1,
         legend=True,
         xlabel = 'x',
         show=False)
p[0].line_color = 'b' #p[0], se refiere a la primera línea, 2x + 3, b de blue o azul
p[1].line_color = 'r'
p[0].label = 'F1'
p[1].label = 'F2'
p.show()
p = plot(2*x**2 + 3, (x, -5, 5),
     title='Función lineal',
     xlabel='x',
     ylabel='2x**2+3',
     show=True)
