import os, random
try:
    from googlesearch import search
except ImportError:
    os.system('pip install google')
    print('Installing google... Ejecute de nuevo')
    exit()

# to search 
query = input("Búsqueda: ")
print("Buscando...")
selec = random.randint(0,14)
valor = 0
for enlace in search(query, tld="com",
                     num=15, stop=15, pause=5):
    if valor == selec:
        print(selec,enlace)
        break
    valor += 1



