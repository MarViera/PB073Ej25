#Gráfica de pastel
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15,15,2,39,4,15])
frutas = ["Apples", "Bananas", "Cherries","Dates","A","B","C","D","E"]

plt.pie(y, labels = frutas)
plt.show() 
