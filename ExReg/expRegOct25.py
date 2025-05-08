import re

patron = r"\d{5}\D"
cadena = input()
cadena += " "
objExpReg = re.compile(patron)
mo = objExpReg.search(cadena)
print("Tu C.P. es: ", mo.group())
