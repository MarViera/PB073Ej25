#Leemos
fo = open("PB073EJ2025.txt","r") #nombre del archivo puede ser una variable
#fo tendrá una línea por cada línea del archivo
print(fo)
for perrito in fo:
    print(type(perrito),perrito,end='')
fo.close()
