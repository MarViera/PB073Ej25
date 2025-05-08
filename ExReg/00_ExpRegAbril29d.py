import re

#Encontrar todos los correos @uanl.edu.mx 
patron = r"@uanl\.edu\.mx"
regex = re.compile(patron)
cadena = '''Los correos son perla.vieragn@uanl.edu.mx, ayuda@uanl.edu.mx'''
correos = regex.findall(cadena)
print(correos)
for mail in correos:
    print(mail)
