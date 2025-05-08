#Leemos de una forma más "sencilla"
with open ("PB073EJ2025.txt","r") as file: #file = fo
    for line in file:
        print(line,end='') #file.close()
print("Se acabo")
print(file)

