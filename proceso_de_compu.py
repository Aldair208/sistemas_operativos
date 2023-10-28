import time
import random

def generar_numeros_random(minimo, maximo):
    return random.randint(minimo, maximo)


def multiplicacion():
    primer_tiempo_multiplicacion = time.time()
    limite_multiplicacion = 5
    while time.time() - primer_tiempo_multiplicacion < limite_multiplicacion:
        num1 = generar_numeros_random(1,1000)
        num2 = generar_numeros_random(1,1000)
        resultado = None
        resultado = num1 * num2
        print("\033[0;34m"f"Números utilizados para multiplicacion: {num1} y {num2} = {resultado}"+"\033[0;m")

def suma():
    primer_tiempo_suma = time.time()
    limite_suma = 5
    while time.time() - primer_tiempo_suma < limite_suma:
        num1 = generar_numeros_random(1,1000)
        num2 = generar_numeros_random(1,1000)
        resultado = None
        resultado = num1 * num2
        print("\033[0;33m"+f"Números utilizados para suma: {num1} y {num2} = {resultado}"+"\033[0;m")


def resta():
    primer_tiempo_resta = time.time()
    limite_resta = 4
    while time.time() - primer_tiempo_resta < limite_resta:
        num1 = generar_numeros_random(1,1000)
        num2 = generar_numeros_random(1,1000)
        resultado = None
        resultado = num1 * num2
        print("\033[0;32m"+f"Números utilizados para resta: {num1} y {num2} = {resultado}"+"\033[0;m")


def division():
    primer_tiempo_division = time.time()
    limite_division = 4
    while time.time() - primer_tiempo_division < limite_division:
        num1 = generar_numeros_random(1,1000)
        num2 = generar_numeros_random(1,1000)
        resultado = None
        resultado = num1 * num2
        print("\033[0;31m"+f"Números utilizados para division: {num1} y {num2} = {resultado}"+"\033[0;m")


multiplicacion()
suma()
division()
resta()


