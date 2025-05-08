import re

bat_regex = re.compile (r"Bat(man|imovil|arang)")
cadena1 = "Batman subio a su Batimovil pero olvidó su Batarang."
mo = bat_regex.search(cadena1)
print("Cadena original: ",cadena1)
print (mo.group())  
print (mo.group(0,1))
input("...")
cadena2 = "Batman subio a su Batimovil olvidó su Batarang. Batman, Batman"
mo = bat_regex.findall(cadena2)
print("Cadena original: ",cadena2)
print (mo)
