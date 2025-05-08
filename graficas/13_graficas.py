# Fuerza de atracción gravitacional

import matplotlib.pyplot as plt
# Draw the graph
def draw_graph(x, y1,y2):
    plt.plot(x, y1, x, y2, marker='o')
    plt.xlabel('Distancia [m x 10 ** -12]')
    plt.ylabel('Fuerza gravitacional y Eléctrica [N]')
    plt.legend(['F gravitacional','F eléctrica'])
    plt.yscale('log', base=10)
    plt.title('Relación entre la fuerza gravitacional y la distancia')
    plt.show()

#Datos
# Constante gravitacional, G
G = 6.674e-11
# Constante eléctrica (de Coulomb), k
k = 8.99e9
# Masas
#Electrón
m1 = 9.11e-31
#Protón
m2 = 1.67e-27
# Cargar
#Electrón
q1 = 1.6e-19
#Protón
q2 = +1.6e-19

#Creamos la lista de valores sobre los que se variará la distancia
#La distancia entre el electrón y el protón es aprox 5.3e-11
r = range(1, 101,2)
#Creamos la lista de valores de la fuerza
Fg = list()
Fe = list()
for dist in r:  #obs: Calculamos la fuerza en cada uno de los valores de la lista de distancias (r). usamos un etiqueta (force) para referirse a la fuerza calculada y agregarla a la lista (F).
    force = G*(m1*m2)/((dist*1e-12)**2)
    Fg.append(force)
    force = k*(q1*q2)/((dist*1e-12)**2)
    Fe.append(force)

draw_graph(r, Fg,Fe)
