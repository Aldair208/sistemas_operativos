import time
import random

def generar_numeros_random(minimo, maximo):
    return random.randint(minimo, maximo)

ja =  random.randint(5, 10)
la =  random.randint(5, 10)
ka =  random.randint(5, 10)

for i in range (1,1000):
    if i == 10 :
        for j in range (1,ja):
            if j==5:
                for k in range(1,ka):
                    num1 = generar_numeros_random(1, 1000)
                    num2 = generar_numeros_random(1, 1000)
                    resultado = num1 - num2
                    print("\033[0;32m" + f"Sg {k} Números utilizados para resta: {num1} y {num2} = {resultado}" + "\033[0;m")
                    time.sleep(1)

                for l in range(1,la):
                    num1 = generar_numeros_random(1, 1000)
                    num2 = generar_numeros_random(1, 1000)
                    resultado = num1 + num2
                    print("\033[0;33m" + f"Sg {l}Números utilizados para suma: {num1} y {num2} = {resultado}" + "\033[0;m")
                    time.sleep(1)

            num1 = generar_numeros_random(1, 1000)
            num2 = generar_numeros_random(1, 1000)
            if num2 == 0:
                print("\033[0;31m" + "No se puede dividir por cero." + "\033[0;m")
            else:
                resultado = num1 / num2
                print("\033[0;31m" + f"Sg {j} Números utilizados para división: {num1} y {num2} = {resultado}" + "\033[0;m")
            time.sleep(1)

    num1 = generar_numeros_random(1, 1000)
    num2 = generar_numeros_random(1, 1000)
    resultado = num1 * num2
    print("\033[0;34m" + f"Sg {i} Números utilizados para multiplicación: {num1} y {num2} = {resultado}" + "\033[0;m")
    time.sleep(1)
    








