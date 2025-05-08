import json, requests
for i in range (1,2): #Pongan un número pequeño, puede tardar mucho
    url = "http://swapi.dev/api/people/"+str(i)+'/'
    response = requests.get(url)#200
    if response.status_code != 200: #Si consultaramos alguna que no existe, es mejor terminar
        break
    infoPersonaje = json.loads(response.text)
    #print(infoPersonaje)
    for x,y in infoPersonaje.items():
        if "http" in y and x != "url":
            response2 = requests.get(y)
            infoExtra = json.loads(response2.text)
            y = infoExtra['name']
        if x == 'films':
            pelis = list()
            for i in y:
                response2 = requests.get(i)
                infoExtra = json.loads(response2.text)
                pelis.append(infoExtra["title"])
            y = pelis
        if x == 'starships' or x == 'vehicles':
            if len(y) < 1:
                continue
            naves = list()
            for i in y:
                response2 = requests.get(i)
                infoExtra = json.loads(response2.text)
                naves.append(infoExtra["name"])
            y = naves
        if x == 'species':
            if len(y) < 1:
                y = 'human'
            else:
                response2 = requests.get(y[0]) #y es una lista de un solo elemento
                infoExtra = json.loads(response2.text)
                y = infoExtra["name"] 
        if x != "created" and x != "edited" and x != "url":
            print(x+":",y)
    print("* * * * * * * * * * * * * * * * * * *\n")
