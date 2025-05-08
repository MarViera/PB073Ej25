a = 2 + 3j
b = complex(3,-4)

#Impresión
print('a = ',a)
print('b = ',b)

#Operaciones
print('Conjugado de a = ',a.conjugate())
print('Conjugado de b = ',b.conjugate())
input()
print('a + b = ', a + b)
print('a - b = ', a - b)
print('a * b = ', a * b)
print('a / b = ', a / b)

#Partes
print("Real de a = ", a.real)
print("Imaginario de a = ", a.imag)
print('Magnitud de a', abs(a))
print('Ojo es diferente para reales -5: ', abs(-5))
