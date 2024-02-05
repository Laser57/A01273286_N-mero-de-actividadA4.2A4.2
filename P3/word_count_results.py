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
tiempo_inicio = time.time()
dic_contador = {}
NOMBRE_ARCHIVO = sys.argv[1]
RESULTADO_ARCHIVO = "WordCountResults.txt"
with open(NOMBRE_ARCHIVO, 'r', encoding='UTF-8') as file:
    master = file.read()
#CREAMOS UNA VARIABLE MAESTROA PARA PODER ALMACENAR PALABRA Y COINCIDENCIA POSTERIORMENTE
for palabra in master.split():
#EN CASO QUE EXISTA LA PALABRA AGREGAMOS UNA COINCIDENCIA
    if palabra in dic_contador:
        dic_contador[palabra] += 1
    else:
        dic_contador[palabra] = 1
#CALCULAMOS TIEMPO FINAL
tiempo_final = time.time() - tiempo_inicio
#OPERACION DE ESCRITURA, PUEDE CONCATENAR EL ARCHIVO,
#GUARDA EL VALOR ITEM Y VALOR DEL DICCIONARIO CREADO
with open(RESULTADO_ARCHIVO, 'a', encoding='UTF-8') as archivo:
    archivo.write(f"Archivo: {sys.argv[1]}\n")
    for item, valor in dic_contador.items():
        print(f"{item}: {valor}")
        linea = f"{item}: {valor}\n"
        archivo.write(linea)
    archivo.write(f"Tiempo de ejecución: {tiempo_final}")
print(f"Tiempo de ejecución: {tiempo_final} segundos")
