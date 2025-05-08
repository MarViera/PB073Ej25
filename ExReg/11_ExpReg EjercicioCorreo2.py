import re
#Tomaremos la opción simple nombre.apellidoletras

#Proponemos un patrón
# letras . letras
patron = r'(\w+[.]*\w*)@([a-z]+).edu[.]{0,1}([a-z]*)'
patCorreo = re.compile(patron)

#Capturamos un mensaje 
cadena = input()

#Buscamos e imprimimos
mo = patCorreo.search(cadena)
print("Correo: ",mo.group())
print("Usuario: ",mo.group(1))
print("Universidad: ",mo.group(2))
print("Pais: ",mo.group(3))

