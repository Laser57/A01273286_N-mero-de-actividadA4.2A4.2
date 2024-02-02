'''
Codigo realizado para determinas media, moda, mediana, varianza, desv. standard
usar txt en formato utf-8 como entrada
puede trabajar con nuemeros en formato flotante.
Se implementa una condicion para retirar letras y dejar solo numeros
LUIS ALFONSO SABANERO ESQUIVEL A01273286
ENERO 2024
'''
import time

TIEMPO_INICIO = time.time()
MASTER = []
NUMEROS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '.', ',']

with open('TC1.txt', 'r', encoding='UTF-8') as file:
    for linea in file:
        AUX = ""
        for i in linea.strip():
            if i in NUMEROS:
                AUX += i
            else:
                break
        MASTER.append(float(AUX))

MEAN = 0
VARIANZA = 0
DESV_STD = 0
MODA = 0
SUMA_CUADRADOS_DIFERENCIAS = 0

for i in MASTER:
    MEAN += i
MEAN = MEAN/len(MASTER)
print(f"Count: {len(MASTER)}")
print(f"MEAN: {MEAN}")

for x in MASTER:
    SUMA_CUADRADOS_DIFERENCIAS += (x - MEAN) ** 2
VARIANZA = SUMA_CUADRADOS_DIFERENCIAS / (len(MASTER) - 1)
DESV_STD = VARIANZA ** (1 / 2)
print(f"VARIANZA: {VARIANZA}")
print(f"Desv Std: {DESV_STD}")

DATOS_ORDENADO = sorted(MASTER)
CANTIDAD_ELEMENTOS = len(DATOS_ORDENADO)

if CANTIDAD_ELEMENTOS % 2 == 1:
    MEDIANA = DATOS_ORDENADO[CANTIDAD_ELEMENTOS // 2]
else:
    INDICE1 = CANTIDAD_ELEMENTOS // 2 - 1
    INDICE2 = CANTIDAD_ELEMENTOS // 2
    MEDIANA = (DATOS_ORDENADO[INDICE1] + DATOS_ORDENADO[INDICE2]) / 2
print(f"MEDIANA: {MEDIANA}")

FRECUENCIAS = {}
for elemento in MASTER:
    if elemento in FRECUENCIAS:
        FRECUENCIAS[elemento] += 1
    else:
        FRECUENCIAS[elemento] = 1

MAX_FRECUENCIA = 0
for elemento, frecuencia in FRECUENCIAS.items():
    if frecuencia > MAX_FRECUENCIA:
        MAX_FRECUENCIA = frecuencia
        MODA = elemento
print(f"MODA: {MODA}")

TIEMPO_FINAL = time.time() - TIEMPO_INICIO
print(f"Tiempo de ejecución: {TIEMPO_FINAL} segundos")
