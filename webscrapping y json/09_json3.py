import json
##Como el contenido de la cadena tiene comilla doble, es importante colocar la cadena en comilla simple
cadena = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
print ("Mi cadena es de tipo:",type(cadena))
CadenaJson = json.loads(cadena)
print ("CadenaJson es de tipo:", type(CadenaJson))

print ("loads signfica loadString, debe recibir una cadena (string)")

for key in CadenaJson:
    print (key)

print("Proceso inverso diccionario")
diccionario = {
    "name": "Zophie",
    "isCat": True,  #Cambia este valor
    "miceCaught": 0,
    "felineIQ": None    #Cambia este valor
    }
print ("diccionario es de tipo:",type(diccionario))

cadenaNueva = json.dumps(diccionario)
print ("cadenaNueva es de tipo:",type(cadenaNueva))  
