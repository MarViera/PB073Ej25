from fractions import Fraction
import re

while True:
    fraccion = input("Ingresa una fracción [d/d]: ")
    exp_reg = re.compile(r'\d+/\d+')
    frac = exp_reg.search(fraccion)
    if frac != None:
        break
    else:
        print('Error de ingreso de datos!')
frac = frac.group()
print(frac)
f1 = Fraction(frac)
print(f1)
