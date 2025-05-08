import re
# @uanl.edu.mx
# @uanl.mx
# @fcfm.uanl.mx
#\w+\.\w+ ==> perla.vieragn @edu
#pviera uanl.mx
#pviera fcfm.uanl.mx
#\w+
sup_regex = re.compile (r"\w+@(fcfm.)?uanl.mx") #dominios y subdominios
sup_regex2 = re.compile (r"\w+\.\w+@uanl(.edu)?.mx") #dominios y subdominios

mo = sup_regex.search ("El dominio de mi correo es pviera@fcfm.uanl.mx por que si")
if mo == None:
    print("No cumple con el patrón")
else:
    print (mo.group())
input()
mo = sup_regex.search ("Mi correo es pviera@uanl.mx por que si")
if mo == None:
    print("No cumple con el patrón")
else:
    print (mo.group())
input()
mo = sup_regex.search ("Mi correo es perla.vieragn@uanl.edu.mx por que si")
if mo == None:
    print("No cumple con el patrón")
else:
    print (mo.group())
input()
mo = sup_regex2.search ("Mi correo es pviera@uanl.mx por que si")
if mo == None:
    print("No cumple con el patrón")
else:
    print (mo.group())
input()
mo = sup_regex2.search ("Mi correo es perla.vieragn@uanl.edu.mx por que si")
if mo == None:
    print("No cumple con el patrón")
else:
    print (mo.group())
