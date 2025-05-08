import requests
import json
from datetime import datetime

##Hacemos un request para obtener el reporte actual
## Ver documentacion para su uso https://openweathermap.org/api/one-call-api
#Definimos las variables para hacer la petición
lat = "25.725536" #agrega inputs para este dato
lon = "-100.315157" #agrega inputs para este dato
appid = "28865615a26534ce0cf21d489694e587" #sustituir por tu API id
page = requests.get ("https://api.openweathermap.org/data/2.5/onecall?lat="
                     +lat+"&lon="+lon+"&exclude=minutely,hourly,daily&units=metric&appid="
                     +appid)    #Internamente es un método HTTP GET
print (page.status_code)                                #Status code 200 significa "Ok", 
print ("Page es de tipo:",type(page))
print ("Page content es de tipo:",type(page.content))

#El contenido de la página nos devuelve el json como texto sin formato
#print (page.content)  #descomentar para llerlo

#Convertimos el json a diccionario
weatherData = json.loads(page.content)

input("Vamos a imprimir el diccionario del clima: ")
for x,y in weatherData.items():
    print("\t",x+":",y)

input("Desplegamos ahora el diccionario con el tipo de dato de su valor")
for key in weatherData:
    print (key,":",type(weatherData[key]))
#Observamos que current es un diccionario

#Reimprimimos el diccionario tomando el nuevo descubrimiento
input("Enter para ver el clima")
for x,y in weatherData.items():
    if type(y) == dict: #imprimir datos de dict interno
        print("\t",x+":")
        for a,b in y.items():
            print("\t\t",a+":",b)
    else: #imprimir claves y valores no dict
        print("\t",x+":",y)

print ("También se puede imprmir current directamente: ")
for elem in weatherData["current"]: #weatherData["current"] --> dict()
    print (elem,":\t",weatherData["current"][elem])

#Revisemos los datos de hora
print("dt",weatherData["current"]["dt"]) #horario en UNIX -> 1/Enero/1970 en UTC
dt = int(weatherData["current"]["dt"])
print ("dt",datetime.utcfromtimestamp(dt).strftime("%d-%m-%Y %H:%M:%S")) #Convertir
sunrise = int(weatherData["current"]["sunrise"])
sunset = int(weatherData["current"]["sunset"])
print ("sunrise", datetime.utcfromtimestamp(sunrise).strftime("%d-%m-%Y %H:%M:%S"))
print ("sunset",datetime.utcfromtimestamp(sunset).strftime("%d-%m-%Y %H:%M:%S"))
