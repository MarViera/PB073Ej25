Alumno = {
    "Nombre" : "Nombre completo",
    "Matricula" : 0,
    "Semestre" : 0,
    "Carrera" : "NA"
}

listaAlum = list()
with open ("ListaAlumnos.txt","r") as file:
    for line in file:
        #Dividimos la línea leída con la coma
        info = line.split(',')#line es str, split separo por un caracter
        #info es una lista de str
        Alumno["Matricula"] = int(info[0])
        Alumno["Semestre"] = int(info[1])
        Alumno["Carrera"] = info[2]
        #Eliminamos el salto de línea
        info[3] = info[3].replace('\n','')
        Alumno["Nombre"] = info[3]
        temp = Alumno.copy()
        listaAlum.append(temp)
print(listaAlum)
for alu in listaAlum:
    for x,y in alu.items():
        print(x,y)
    print("****")
