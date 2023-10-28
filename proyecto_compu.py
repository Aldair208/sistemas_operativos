

import time
import random

def generar_numeros_random(minimo, maximo):
    return random.randint(minimo, maximo)

def multiplicacion():
    primer_tiempo_multiplicacion = time.time()

    while time.time() - primer_tiempo_multiplicacion < 5:
        num1 = generar_numeros_random(1, 1000)
        num2 = generar_numeros_random(1, 1000)
        resultado = num1 * num2
        print("\033[0;34m" + f"Números utilizados para multiplicación: {num1} y {num2} = {resultado}" + "\033[0;m")
        time.sleep(1)

def suma():
    primer_tiempo_suma = time.time()

    while time.time() - primer_tiempo_suma < 5:
        num1 = generar_numeros_random(1, 1000)
        num2 = generar_numeros_random(1, 1000)
        resultado = num1 + num2
        print("\033[0;33m" + f"Números utilizados para suma: {num1} y {num2} = {resultado}" + "\033[0;m")
        time.sleep(1)

def resta():
    primer_tiempo_resta = time.time()

    while time.time() - primer_tiempo_resta < 4:
        num1 = generar_numeros_random(1, 1000)
        num2 = generar_numeros_random(1, 1000)
        resultado = num1 - num2
        print("\033[0;32m" + f"Números utilizados para resta: {num1} y {num2} = {resultado}" + "\033[0;m")
        time.sleep(1)

def division():
    primer_tiempo_division = time.time()

    while time.time() - primer_tiempo_division < 4:
        num1 = generar_numeros_random(1, 1000)
        num2 = generar_numeros_random(1, 1000)
        if num2 == 0:
            print("\033[0;31m" + "No se puede dividir por cero." + "\033[0;m")
        else:
            resultado = num1 / num2
            print("\033[0;31m" + f"Números utilizados para división: {num1} y {num2} = {resultado}" + "\033[0;m")
        time.sleep(1)


Proceso=[suma(),resta(), division(), multiplicacion(),division(),suma(),resta()]
print(Proceso)