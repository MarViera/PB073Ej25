import re
#Tomaremos la opción simple nombre.apellidoletras

#Proponemos un patrón
patCorreo = re.compile(r'([a-z]+)\.([a-z]+)@(uanl.edu.mx)') #Office 365


#Capturamos un mensaje
cadena = input()

#Buscamos e impromimos
mo = patCorreo.search(cadena)
print(mo.group(0)) #cuando no ponemos nada, es como si pusieramos 0
print("Tu nombre es: ",mo.group(1))
print("La info de tus apellidos es: ",mo.group(2))
print("El dominio de tu correo es: ",mo.group(3))

