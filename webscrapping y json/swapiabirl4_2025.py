import requests

def obtener_personajes(n1, n2):
    personajes = [] 
    for i in range(n1, n2 + 1):
        url = f"https://swapi.dev/api/people/{i}/"
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            # Obtener el nombre del planeta
            planeta_respuesta = requests.get(datos["homeworld"])
            planeta = planeta_respuesta.json()
            planeta_nombre = planeta["name"]
            peliculas = []
            for film_url in datos["films"]:
                pelis_respuesta = requests.get(film_url)
                peli = pelis_respuesta.json()
                peli_nombre = peli["title"]
                peliculas.append(peli_nombre)
            
            personaje = {
                "name": datos["name"],
                "height": datos["height"],
                "mass": datos["mass"],
                "hair_color": datos["hair_color"],
                "birth_year": datos["birth_year"],
                "homeworld": planeta_nombre,
                "films": peliculas
            }
            personajes.append(personaje)
    return personajes

# Solicitar al usuario los números de inicio y fin
n1 = int(input("Ingrese el número de personaje inicial: "))
n2 = int(input("Ingrese el número de personaje final: "))

# Obtener la información de los personajes
personajes_consultados = obtener_personajes(n1, n2)

# Mostrar los resultados
arch = open("arch_test.txt","w")
for personaje in personajes_consultados:
    arch.write(str(personaje))
    for x,y in personaje.items():
        print(f"{x} -> {y}")

arch.close()
