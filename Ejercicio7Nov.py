#from datetime import datetime
import time
from statistics import median, mean
import matplotlib.pyplot as plt
from collections import Counter


datosClima = {'lat': 28.5421,
               'lon': -81.379,
               'timezone': 'America/New_York',
               'timezone_offset': -18000,
               'current': {'dt': 1699457053,
                           'sunrise': 1699443748,
                           'sunset': 1699482964,
                           'temp': 25.17,
                           'feels_like': 25.57,
                           'pressure': 1020,
                           'humidity': 70,
                           'dew_point': 19.31,
                           'uvi': 2.86,
                           'clouds': 0,
                           'visibility': 10000,
                           'wind_speed': 2.06,
                           'wind_deg': 40,
                           'weather': [{'id': 800,
                                        'main': 'Clear',
                                        'description': 'clear sky',
                                        'icon': '01d'}]},
               'daily': [{'dt': 1699462800,
                          'sunrise': 1699443748,
                          'sunset': 1699482964,
                          'moonrise': 1699427940,
                          'moonset': 1699474020,
                          'moon_phase': 0.85,
                          'temp': {'day': 26.33,
                                   'min': 18.78,
                                   'max': 29.34,
                                   'night': 21.13,
                                   'eve': 24.35,
                                   'morn': 19.87},
                          'feels_like': {'day': 26.33,
                                         'night': 21.34,
                                         'eve': 24.46,
                                         'morn': 20.13},
                          'pressure': 1020,
                          'humidity': 58,
                          'dew_point': 17.41,
                          'wind_speed': 3.5,
                          'wind_deg': 114,
                          'wind_gust': 6.25,
                          'weather': [{'id': 800,
                                       'main': 'Clear',
                                       'description': 'clear sky',
                                       'icon': '01d'}],
                          'clouds': 0,
                          'pop': 0.02,
                          'uvi': 5.52},
                         {'dt': 1699549200,
                          'sunrise': 1699530195,
                          'sunset': 1699569329,
                          'moonrise': 1699517580,
                          'moonset': 1699562040,
                          'moon_phase': 0.88,
                          'temp': {'day': 28.03,
                                   'min': 19.25,
                                   'max': 29.37,
                                   'night': 21.93,
                                   'eve': 25.17,
                                   'morn': 19.25},
                          'feels_like': {'day': 28.22,
                                         'night': 22.22,
                                         'eve': 25.18,
                                         'morn': 19.53},
                          'pressure': 1018,
                          'humidity': 47,
                          'dew_point': 15.66,
                          'wind_speed': 3.69,
                          'wind_deg': 119,
                          'wind_gust': 7.57,
                          'weather': [{'id': 803,
                                       'main': 'Clouds',
                                       'description': 'broken clouds',
                                       'icon': '04d'}],
                          'clouds': 55,
                          'pop': 0,
                          'uvi': 5.35},
                         {'dt': 1699635600,
                          'sunrise': 1699616641,
                          'sunset': 1699655694,
                          'moonrise': 1699607160,
                          'moonset': 1699650060,
                          'moon_phase': 0.91,
                          'temp': {'day': 28.93,
                                   'min': 20.44,
                                   'max': 30.81,
                                   'night': 24.27,
                                   'eve': 27.42,
                                   'morn': 20.87},
                          'feels_like': {'day': 30.34,
                                         'night': 24.71,
                                         'eve': 27.9,
                                         'morn': 21.36},
                          'pressure': 1018,
                          'humidity': 56,
                          'dew_point': 19.35,
                          'wind_speed': 3.23,
                          'wind_deg': 198,
                          'wind_gust': 7.37,
                          'weather': [{'id': 500,
                                       'main':'Rain',
                                       'description':
                                       'light rain',
                                       'icon': '10d'}],
                          'clouds': 48,
                          'pop': 0.4,
                          'rain': 0.24,
                          'uvi': 5.64},
                         {'dt': 1699722000,
                          'sunrise': 1699703088,
                          'sunset': 1699742061,
                          'moonrise': 1699696860,
                          'moonset': 1699738200,
                          'moon_phase': 0.94,
                          'temp': {'day': 30.8,
                                   'min': 21.76,
                                   'max': 30.8,
                                   'night': 23.46,
                                   'eve': 25.13,
                                   'morn': 21.76},
                          'feels_like': {'day': 31.58,
                                         'night': 23.98,
                                         'eve': 25.6,
                                         'morn': 22.26},
                          'pressure': 1018,
                          'humidity': 46,
                          'dew_point': 17.97,
                          'wind_speed': 3.32,
                          'wind_deg': 101,
                          'wind_gust': 6.05,
                          'weather': [{'id': 500,
                                       'main':
                                       'Rain', 'description':
                                       'light rain',
                                       'icon': '10d'}],
                          'clouds': 38,
                          'pop': 0.3,
                          'rain': 0.35,
                          'uvi': 5.67},
                         {'dt': 1699808400,
                          'sunrise': 1699789536,
                          'sunset': 1699828430,
                          'moonrise': 1699786740,
                          'moonset': 1699826580,
                          'moon_phase': 0.98,
                          'temp': {'day': 27.17,
                                   'min': 19.81,
                                   'max': 27.17,
                                   'night': 19.81,
                                   'eve': 20.53,
                                   'morn': 20.92},
                          'feels_like': {'day': 28.38,
                                         'night': 20.07,
                                         'eve': 20.73,
                                         'morn': 21.47},
                          'pressure': 1019,
                          'humidity': 61,
                          'dew_point': 18.93,
                          'wind_speed': 6.4,
                          'wind_deg': 15,
                          'wind_gust': 11.49,
                          'weather': [{'id': 500,
                                       'main': 'Rain',
                                       'description': 'light rain',
                                       'icon': '10d'}],
                          'clouds': 85,
                          'pop': 0.3,
                          'rain': 0.11,
                          'uvi': 6},
                         {'dt': 1699894800,
                          'sunrise': 1699875983,
                          'sunset': 1699914800,
                          'moonrise': 1699876800,
                          'moonset': 1699915320,
                          'moon_phase': 0,
                          'temp': {'day': 24.02,
                                   'min': 20.06,
                                   'max': 24.25,
                                   'night': 20.84,
                                   'eve': 21.01,
                                   'morn': 20.59},
                          'feels_like': {'day': 24.23,
                                         'night': 20.68,
                                         'eve': 21.02,
                                         'morn': 20.9},
                          'pressure': 1020,
                          'humidity': 67,
                          'dew_point': 17.6,
                          'wind_speed': 7.18,
                          'wind_deg': 37,
                          'wind_gust': 12.25,
                          'weather': [{'id': 500,
                                       'main': 'Rain',
                                       'description': 'light rain',
                                       'icon': '10d'}],
                          'clouds': 88,
                          'pop': 0.53,
                          'rain': 0.95,
                          'uvi': 6}, {'dt': 1699981200,
                                      'sunrise': 1699962431,
                                      'sunset': 1700001171,
                                      'moonrise': 1699967040,
                                      'moonset': 1700004360,
                                      'moon_phase': 0.04,
                                      'temp': {'day': 23.73,
                                               'min': 18.78,
                                               'max': 23.73,
                                               'night': 18.78,
                                               'eve': 19.28,
                                               'morn': 19.11},
                                      'feels_like': {'day': 23.2,
                                                     'night': 18.18,
                                                     'eve': 18.67,
                                                     'morn': 18.56},
                                      'pressure': 1023,
                                      'humidity': 40,
                                      'dew_point': 9.21,
                                      'wind_speed': 7.96,
                                      'wind_deg': 54,
                                      'wind_gust': 11,
                                      'weather': [{'id': 801,
                                                   'main': 'Clouds',
                                                   'description': 'few clouds',
                                                   'icon': '02d'}],
                                      'clouds': 19,
                                      'pop': 0.04,
                                      'uvi': 6},
                         {'dt': 1700067600,
                          'sunrise': 1700048879,
                          'sunset': 1700087544,
                          'moonrise': 1700057340,
                          'moonset': 1700094000,
                          'moon_phase': 0.08,
                          'temp': {'day': 24.7,
                                   'min': 18.45,
                                   'max': 24.7,
                                   'night': 21.33,
                                   'eve': 20.87,
                                   'morn': 18.45},
                          'feels_like': {'day': 24.24,
                                         'night': 20.77,
                                         'eve': 20.32,
                                         'morn': 17.89},
                          'pressure': 1024,
                          'humidity': 39,
                          'dew_point': 10.05,
                          'wind_speed': 7.94,
                          'wind_deg': 62,
                          'wind_gust': 11.64,
                          'weather': [{'id': 803,
                                       'main': 'Clouds',
                                       'description':'broken clouds',
                                       'icon': '04d'}],
                          'clouds': 58,
                          'pop': 0,
                          'uvi': 6}]}

for k,v in datosClima.items():
    print(k, "->", type(v))
fecha = list()
tmin = list()
tmax = []
tmor = []
teve = []
tnight = []
presion = []
humedad = []
tipoclima = []
#print(datosClima['daily'])
for dia in datosClima['daily']:
    #print(dia['dt'])
    temp = time.strftime("%d/%m",
                    time.localtime(dia['dt']))
    fecha.append(temp)
    tmin.append(dia['temp']['min'])
    tmax.append(dia['temp']['max'])
    tmor.append(dia['temp']['morn'])
    teve.append(dia['temp']['eve'])
    tnight.append(dia['temp']['night'])
    presion.append(dia['pressure'])
    humedad.append(dia['humidity'])
    tipoclima.append(dia['weather'][0]['main'])
tprom = []
#print(presion)
#print(humedad)
#print(tipoclima)
for i in range(len(tmin)):
    #print(fecha[i], tmin[i], tmax[i], tmor[i], teve[i],tnight[i])
    tprom.append((tmin[i]+tmax[i])/2)
tpmin = mean(tmin)
tpmax = mean(tmax)
tpmor = mean(tmor)
tpeve = mean(teve)
tpnig = mean(tnight)

tmmin = median(tmin)
tmmax = median(tmax)
tmmor = median(tmor)
tmeve = median(teve)
tmnig = median(tnight)

#Impriman bonito los datos!!
plt.plot(fecha, tmin, fecha, tmax, marker='*')
plt.legend(["Mínimas","Máximas"])
plt.title('Temperaturas máximas y mínimas en Monterrey')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (C)')
plt.axis(ymin=0, ymax=40, xmin=1, xmax=7)
plt.show()

plt.plot(fecha, tmor, fecha, teve,
         fecha, tnight, marker='o')
plt.legend(["Matutinas","Vespertinas", "Nocturnas"])
plt.title('Temperaturas en Monterrey')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (C)')
plt.axis(ymin=0, ymax=40, xmin=1, xmax=7)
plt.show()
# 8.Graficar presión atmosférica:
#Extrae y grafica la presión atmosférica del campo daily.
plt.plot(fecha, presion, marker='+')
plt.title('Presión atmosférica en Monterrey')
plt.xlabel('Fecha')
plt.ylabel('Presión (mB)')
plt.axis(ymin=950, ymax=1050, xmin=1, xmax=7)
plt.show()
# 9.Graficar humedad relativa:
#Extrae y grafica la humedad relativa del campo daily.
plt.plot(fecha, humedad, marker='x')
plt.title('Humedad relativa en Monterrey')
plt.xlabel('Fecha')
plt.ylabel('Humedad relativa (%)')
plt.axis(ymin=0, ymax=100, xmin=1, xmax=7)
plt.show()

#10.Generar tabla de frecuencia:
#Del campo weather en cada registro del campo daily,
#extrae el campo main.
#Genera una tabla de frecuencia para clasificar y
#contabilizar los tipos de clima.
frec = Counter(tipoclima)
climas = []
repe = []
for clima,repeticiones in frec.most_common():
    print('{0}\t\t\t{1}'.format(clima,repeticiones))
    climas.append(clima)
    repe.append(repeticiones)
    
#11.Graficar tabla de frecuencia:
#A partir de la tabla de frecuencia, crea una gráfica de pastel.
#Hasta aquí se hace y entrega hoy!
plt.pie(repe, labels = climas)
plt.show()



    
