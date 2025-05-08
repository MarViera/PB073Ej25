import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
pasteles = ['chocolate','frutas',
            'tres leches',
            'red velvet']
#Var la gráfica de pastel
plt.pie(y, labels = pasteles)
plt.ylabel("Pasteles")
plt.show()




#Ver la gráfica en barras horizontales
x = np.array(pasteles)
plt.barh(x,y)
plt.show()

    
        
    
