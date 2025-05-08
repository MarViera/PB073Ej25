import re

ast_regex = re.compile (r"(Ha)*") # * -> 0 o más veces
mo = ast_regex.search ("HaHaHaHaHaHaHaHaHaHaHaHa")
print (mo.group())
print (mo.group(1))
input()
mo = ast_regex.search ("Hola")#Permite el valor nulo
if mo != None:
    print (mo.group(),"no encontro nada")
else:
    print("No cumple")
