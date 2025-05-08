from googlesearch import search
import webbrowser

# to search 
query = input("Búsqueda: ")
print("Buscando...")
cant = 3
for enlace in search(query, tld="com",
                     num=cant, stop=cant, pause=5):
    webbrowser.open(enlace)



