'''
Codigo realizado para determinas media, moda, mediana, varianza, desv. standard
usar txt en formato utf-8 como entrada
puede trabajar con nuemeros en formato flotante.
Se implementa una condicion para retirar letras y dejar solo numeros
LUIS ALFONSO SABANERO ESQUIVEL A01273286
ENERO 2024
'''
import time
import sys
TIEMPO_INICIO = time.time()
MASTER =""
DIC_CONTADOR={}
NOMBRE_ARCHIVO = sys.argv[1]
RESULTADO_ARCHIVO = "WordCountResults.txt"
with open(NOMBRE_ARCHIVO, 'r', encoding='UTF-8') as file:
    MASTER = file.read()
for I in MASTER.split():
    if I in DIC_CONTADOR:
        DIC_CONTADOR[I]=DIC_CONTADOR[I]+1
    else:
        DIC_CONTADOR[I]=1
TIEMPO_FINAL = time.time() - TIEMPO_INICIO
with open(RESULTADO_ARCHIVO, 'w',encoding='UTF-8') as ARCHIVO:
    for ITEM,VALOR in DIC_CONTADOR.items():
        print(f"{ITEM}: {VALOR}")
        LINEA = f"{ITEM}: {VALOR}\n"
        ARCHIVO.write(LINEA)
    ARCHIVO.write(f"Tiempo de ejecución:{TIEMPO_FINAL}")
print(f"Tiempo de ejecución: {TIEMPO_FINAL} segundos")
