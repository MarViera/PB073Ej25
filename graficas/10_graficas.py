import matplotlib.pyplot as plt

def draw_graph(x, y):
    plt.plot(x, y, marker='*')
    plt.xlabel('Distancia [m]')
    plt.ylabel('Fuerza gravitacional [N]')
    plt.title('Relación entre la fuerza gravitacional y la distancia')
    plt.show()

G = 6.674e-11
m1 = 0.5
m2 = 1.5
r = range(100, 1001, 50)
F = list()
for dist in r:
    force = G*(m1*m2)/(dist**2)
    F.append(force)

draw_graph(r, F)
