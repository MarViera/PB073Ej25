import re

patron1 = re.compile(r'pika[a-zA-Z]+') # + -> Aparece una o más veces
patron2 = re.compile(r'pika([a-zA-Z]+)') # pikapalabra --> pikapalabra, group(1) -> palabra

cadena = input("Captura tu pikamensaje: ")
pikaPalabras = patron1.findall(cadena)
traduccion = patron2.findall(cadena)
print(pikaPalabras)
print(traduccion)
#pikaPalabras y traduccion son listas
if len(pikaPalabras) == len(traduccion):
    print("Ambas listas tienen la misma cantidad de elementos")

for i in range(len(pikaPalabras)):
    print(pikaPalabras[i],"=",traduccion[i])
