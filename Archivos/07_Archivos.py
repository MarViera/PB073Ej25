Alumno = {
    "Nombre" : "Nombre completo",
    "Matricula" : 0,
    "Semestre" : 0,
    "Carrera" : "NA" }

cant = 2 #int(input("Cant de alumnos a registrar: "))
listaAlum = list()
for i in range(cant):
    print("Captura de datos personales de alumno ",i+1)
    nombre = input("Nombre: ")
    mat = int(input("Matrícula: "))
    sem = int(input("Semestre: "))
    carr = input("Carrera: ")
    #Pasamos al diciconario
    Alumno["Nombre"] = nombre
    Alumno["Matricula"] = mat
    Alumno["Semestre"] = sem
    Alumno["Carrera"] = carr
    #Pasamos a una copia
    temp = Alumno.copy()
    listaAlum.append(temp)
print(listaAlum)
#input()
#Decidimos como almacenarlo en el archivo
# Matricula,Semestre,Carrera,Nombre
fo = open("ListaAlumnos.txt","a")
for i in range(cant):
    fo.write(str(listaAlum[i]["Matricula"])+',')
    fo.write(str(listaAlum[i]["Semestre"])+',')
    fo.write(listaAlum[i]["Carrera"]+
             ','+listaAlum[i]["Nombre"]+'\n')
fo.close()
