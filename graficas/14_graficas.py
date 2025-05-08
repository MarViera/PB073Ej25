import matplotlib.pyplot as plt

def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Distancia [m x 10 ** -12]')
    plt.ylabel('Fuerza eléctrica [N]')
    plt.show()

r = range(1, 101,2)
Fe = list()
for dist in r: 
    force = (8.99e9)*((1.6e-19)*(+1.6e-19))/((dist*1e-12)**2)
    Fe.append(force)
draw_graph(r, Fe)

