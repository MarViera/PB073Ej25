import matplotlib.pyplot as plt

#Múltiples conjuntos de datos en la misma gráfica
nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3,
                 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0,
                 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0,
                 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]

#creamos una lista (meses) donde almacenamos los números
#1, 2, 3 y así sucesivamente hasta 12 usando la función range()
months = range(1, 13)
#A continuación, llamamos a la función plot() con tres pares
#de listas. 
#Cada par consta de una lista de meses a graficar en el
#eje x y una lista de temperaturas mensuales promedio
#(para 2000, 2006, y 2012, respectivamente) para ser
#graficados en el eje y. 
plt.plot(months, nyc_temp_2000, months, nyc_temp_2006,
     months, nyc_temp_2012,marker='o')
plt.legend([2000, 2006, 2012])
plt.title('Temperatura promedio en NYC')
plt.xlabel('Mes')
plt.ylabel('Temperatura (F)')
plt.axis(ymin=0, ymax=100, xmin=1, xmax=12)
plt.show()
plt.savefig("graf2.png")
