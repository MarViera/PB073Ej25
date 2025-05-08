#Capturar numeros en otras bases

bina = input('binario: ')
octa = input('octal: ')
hexa = input('hexa: ')
deci = input('decimal: ')

#Convertimos
bina = int(bina,2)
octa = int(octa,8)
hexa = int(hexa,16)
deci = int(deci,10)

#Imprimimos en decimal
print("Impresión decimal")
print(bina)
print(octa)
print(hexa)
print(deci)

#Pasamos a la base correcta
bina = bin(bina)
octa = oct(octa)
hexa = hex(hexa)
#deci = dec(deci) - No existe dec

#Imprimimos
print("Imprimimos en su base")
print(bina)
print(octa)
print(hexa)
print(deci)
