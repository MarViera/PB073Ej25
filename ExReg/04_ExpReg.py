import re

br_regexp = re.compile (r"Batman|Robin") # | --> o
mo = br_regexp.search ("Batman y Robin") #Busca la primera coincidencia
print (mo.group()) #Batman 

mo = br_regexp.search ("Robin y Batman")
print (mo.group()) #Robin

