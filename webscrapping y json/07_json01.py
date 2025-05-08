import json, requests
#Modifica los valores númericos para ver otros personajes
for i in range (1,2): 
    url = "http://swapi.dev/api/people/"+str(i)+'/'
    response = requests.get(url)
    #Si consultaramos alguna que no existe, es mejor terminar
    if response.status_code != 200: 
        break
    infoPersonaje = json.loads(response.text)
    print(infoPersonaje)
    print(type(infoPersonaje))
    for x,y in infoPersonaje.items():
        print(x,y)
