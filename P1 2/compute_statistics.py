'''
Codigo realizado para determinar media, moda, mediana, varianza, desv. standard
usar txt en formato utf-8 como entrada
puede trabajar con nuemeros en formato flotante.
Se implementa una condicion para retirar letras y dejar solo numeros
Parametos: requiere unicamente usar el comando python nombre_archivo.py archivo_txt.txt
LUIS ALFONSO SABANERO ESQUIVEL A01273286
ENERO 2024
'''
import time
import sys
tiempo_inicio = time.time()
master = []
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '.', ',']
NOMBRE_ARCHIVO = sys.argv[1]
#LEEMOS EL ARCHIVO PASADO COMO PARAMETRO EN LA FUNCION
with open(NOMBRE_ARCHIVO, 'r', encoding='UTF-8') as file:
    for linea in file:
        AUX = ""
        for i in linea.strip():
            if i in numeros:
                if i in [',',';']:
                    i='.'
                AUX += i
            else:
                break
        if AUX != "":
            master.append(float(AUX))
        else:
            print(f"Linea {linea} con valor invalido, se omite")
MEAN = 0
VARIANZA = 0
DESV_STD = 0
MODA = 0
SUMA_CUADRADOS_DIFERENCIAS = 0
RESULTADO_ARCHIVO = "StatisticsResults.txt"
#CALCULO PARA DETERMINAR LA MEDIA SUMATORIA DE LOS VALORES / CANTIDAD DE VALRES
for i in master:
    MEAN += i
MEAN = MEAN/len(master)
print(f"Count: {len(master)}")
print(f"MEAN: {MEAN}")
#CALCULO VARIANZA VALOR X - MEDIA AL CUADRADO/LONGITUD -1
#DESVIACION ESTANDARD = RAIZ CUADARADA DE VARIANZA
for x in master:
    SUMA_CUADRADOS_DIFERENCIAS += (x - MEAN) ** 2
VARIANZA = SUMA_CUADRADOS_DIFERENCIAS / (len(master) - 1)
DESV_STD = VARIANZA ** (1 / 2)
print(f"VARIANZA: {VARIANZA}")
print(f"Desv Std: {DESV_STD}")

datos_ordenado = sorted(master)
cantidad_elementos = len(datos_ordenado)

#MEDIANA ES UN VALOR QUE REQUIERE LA LISTA ORDENADA DETERMINAMOS SEGUN EL CASO
#SI SON NUMEROS IMPARES O PARES
if cantidad_elementos % 2 == 1:
    mediana = datos_ordenado[cantidad_elementos // 2]
else:
    indice1 = cantidad_elementos // 2 - 1
    indice2 = cantidad_elementos // 2
    mediana = (datos_ordenado[indice1] + datos_ordenado[indice2]) / 2
print(f"MEDIANA: {mediana}")
frecuencias = {}
#CALCULO PARA LA MODA, DERTEMINAMOS CUAL ELEMENTO SE REPITE MAS
for elemento in master:
    if elemento in frecuencias:
        frecuencias[elemento] += 1
    else:
        frecuencias[elemento] = 1
MAX_FRECUENCIA = 0
for elemento, frecuencia in frecuencias.items():
    if frecuencia > MAX_FRECUENCIA:
        MAX_FRECUENCIA = frecuencia
        MODA = elemento
print(f"MODA: {MODA}")
tiempo_final = time.time() - tiempo_inicio
with open(RESULTADO_ARCHIVO, 'a',encoding='UTF-8') as ARCHIVO:
    ARCHIVO.write(f"Archivo: {sys.argv[1]}\n")
    ARCHIVO.write(f"Count: {len(master)}\n")
    ARCHIVO.write(f"MEAN: {MEAN}\n")
    ARCHIVO.write(f"VARIANZA: {VARIANZA}\n")
    ARCHIVO.write(f"Desv Std: {DESV_STD}\n")
    ARCHIVO.write(f"MEDIANA: {mediana}\n")
    ARCHIVO.write(f"MODA: {MODA}\n")
    ARCHIVO.write(f"Tiempo de ejecución:{tiempo_final}\n")
print(f"Tiempo de ejecución: {tiempo_final} segundos")
