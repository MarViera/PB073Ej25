from fractions import Fraction
from decimal import Decimal

f1 = Fraction(1.5)
f2 = Fraction(1.1)
f3 = Fraction(Decimal('1.1'))
print(1.1)
if f2 == f3:
    print('Si son iguales')
else:
    print('No son iguales')

print(f1,'\n',f2,'\n',f3)
