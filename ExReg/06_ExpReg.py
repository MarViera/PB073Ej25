import re

##Expresión regular con prefijo
bat_regex = re.compile (r"Bat(man|imovil|arang)")
mo = bat_regex.search("Batman subio a su Batimovil olvidó su Batarang.")
print ('1',mo.group())
print ('2',mo.group(1))
input()
mo = bat_regex.findall("Batman subio a su Batimovil olvidó su Batarang. Batman, Batman")
print ('3',mo)

