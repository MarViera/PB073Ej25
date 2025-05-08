import os
try:
    from googlesearch import search
except ImportError:
    os.system('pip install google')
    print('Installing google... Ejecute de nuevo')
    exit()

# to search 
query = input("Búsqueda: ")
print("Buscando...")
for enlace in search(query, tld="com", num=15,
                     stop=15, pause=5):
    print(enlace)



