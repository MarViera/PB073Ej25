import requests
# https://swapi.dev/api/people/4/
url = input("Ingresa un sitio web (incluye el http): ")
r = requests.get(url)
if r.status_code == 200:
    personaje = r.json() #dict
    print(type(personaje))
    print("llaves del dict ",personaje.keys())
    print('valores del dict',personaje.values())
    print('todo el dict', personaje)
    for x,y in personaje.items():
        print(x,"-",y)
else:
    print("La pagina no existe, bye!")
    exit()
