import random
import string

def generar_cadena_aleatoria(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    cadena_aleatoria = ''.join(random.choices(caracteres, k=longitud))
    return cadena_aleatoria

# Ejemplo de uso
longitud = int(input("Introduce la longitud de la cadena aleatoria: "))
cadena = generar_cadena_aleatoria(longitud)
print(f"Cadena aleatoria generada: {cadena}")
