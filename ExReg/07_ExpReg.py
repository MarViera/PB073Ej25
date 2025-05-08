import re
sup_regex = re.compile (r'www(.\w+)?.uanl.mx') #dominios y subdominios
# www.uanl.mx           
cadena = input("Dime las paginas")
mo = sup_regex.findall(cadena)
for encontrado in mo:
    encontrado = 'www'+encontrado+'.uanl.mx'
    print(encontrado)
