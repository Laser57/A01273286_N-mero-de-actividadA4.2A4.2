'''
Codigo realizado para determinar la cantidad de veces que
una palabra aparece en el archivo txt
usar txt en formato utf-8 como entrada
Parametos: requiere unicamente usar el comando
python nombre_archivo.py archivo_txt.txt
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
#CREAMOS UNA VARIABLE MAESTROA PARA PODER ALMACENAR PALABRA Y COINCIDENCIA POSTERIORMENTE
for I in MASTER.split():
#EN CASO QUE EXISTA LA PALABRA AGREGAMOS UNA COINCIDENCIA
    if I in DIC_CONTADOR:
        DIC_CONTADOR[I]=DIC_CONTADOR[I]+1
    else:
#EN CASO QUE NO AGREGAMOS UN 1
        DIC_CONTADOR[I]=1
#CALCULAMOS TIEMPO FINAL
TIEMPO_FINAL = time.time() - TIEMPO_INICIO
#OPERACION DE ESCRITURA, PUEDE CONCATENAR EL ARCHIVO,
#GUARDA EL VALOR ITEM Y VALOR DEL DICCIONARIO CREADO
with open(RESULTADO_ARCHIVO, 'a',encoding='UTF-8') as ARCHIVO:
    ARCHIVO.write(f"Archivo: {sys.argv[1]}\n")
    for ITEM,VALOR in DIC_CONTADOR.items():
        print(f"{ITEM}: {VALOR}")
        LINEA = f"{ITEM}: {VALOR}\n"
        ARCHIVO.write(LINEA)
    ARCHIVO.write(f"Tiempo de ejecución:{TIEMPO_FINAL}")
print(f"Tiempo de ejecución: {TIEMPO_FINAL} segundos")
