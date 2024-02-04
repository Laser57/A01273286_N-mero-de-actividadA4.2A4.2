'''
Codigo realizado para determinar el numero binario y hexadecimal de numeros positivos y negativos
usar txt en formato utf-8 como entrada
puede trabajar con numeros negativos y positivos
Se implementa una condicion para retirar letras y dejar solo numeros,
se notificara al usuario cuando no se tenga una palabra valida
Parametos: requiere unicamente usar el comando python nombre_archivo.py archivo_txt.txt
LUIS ALFONSO SABANERO ESQUIVEL A01273286
ENERO 2024
'''
import time
import sys
TIEMPO_INICIO = time.time()
MASTER = []
NUMEROS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '.', ',']
RESULTADO_ARCHIVO = "ConvertionResults.txt"
NOMBRE_ARCHIVO = sys.argv[1]
#LEEMOS ARCHIVO, NOS ASEGURAMOS QUE LOS VALORES NUMERICOS SEAN VALIDOS
#EN CASO QUE NO SE OMITE EL VALOR
with open(NOMBRE_ARCHIVO, 'r', encoding='UTF-8') as file:
    for linea in file:
        AUX = ""
        for i in linea.strip():
            if i in NUMEROS:
                AUX += i
            else:
                break
        if AUX != "":
            MASTER.append(int(AUX))
        else:
            print(f"Linea {linea} con valor invalido, se omite")
#PARTE BINARIA, SE GUARDA EL RESULTADO EN UNA LISTA
LISTA_BINARIA=[]
for NUMERO in MASTER:
    BINARIO=""
    NEGATIVO=False
#BANDERA NEGATIVA, EN CASO DE SER NEGATIVO PASAMOS VALOR ABSOLUTO
    if NUMERO<0:
        NEGATIVO=True
        NUMERO=abs(NUMERO)
#USAREMOS EL RESIDUO DE LA OPERACION MODULO % LA BASE NUMERICO
    while NUMERO > 0:
        RESIDUO = NUMERO % 2
        BINARIO = str(RESIDUO) + BINARIO
        NUMERO //= 2
#VALOR NEGATIVO SE USARA 8 BITS PARA REPRESENTAR EL NUMERO, SE USARA EL INVERSO DEL
#NUMERO POSITIVO Y SE LE SUMARA UN COMPLEMENTO + 1
    if NEGATIVO:
        BINARIO=BINARIO.zfill(8)
        BINARIO="".join('1' if BIT == '0' else '0' for BIT in str(BINARIO))
        COMPLEMENTO = "00000001"
        RESULTADO = ""
        ACARREO = 0
#USAMOS 8 BITS PARA EL CICLO, USAMOS UNA SUMA BINARIA PARA APLICAR EL +1
        for i in range(8 - 1, -1, -1):
            BIT1 = int(BINARIO[i])
            BIT2 = int(COMPLEMENTO[i])
            SUMA_BIT = BIT1 + BIT2 + ACARREO
            RESULTADO = str(SUMA_BIT % 2) + RESULTADO
            ACARREO = SUMA_BIT // 2
        if ACARREO:
            RESULTADO = "1" + RESULTADO
        LISTA_BINARIA.append(RESULTADO)
    else:
        LISTA_BINARIA.append(BINARIO)
#PARTE HEXADECIMAL USAMOS OPERACION MODULO %16
LISTA_HEXADECIMAL=[]
for NUMERO in MASTER:
    HEX=""
    if NUMERO < 0:
        NUMERO = 2**32 + NUMERO
    while NUMERO > 0:
        RESIDUO = NUMERO % 16
#APLICAMOS TRANSFORMACION DE NUMERO PARA VALORES MAYORES A 16 A,B,C,D,E,F
        if RESIDUO>=10:
            RESIDUO=chr(ord('A') + RESIDUO - 10)
        HEX = str(RESIDUO) + HEX
        NUMERO //= 16
    LISTA_HEXADECIMAL.append(HEX)
##CALCULAMOS TIEMPO FINAL
TIEMPO_FINAL = time.time() - TIEMPO_INICIO
#VACIAMOS EL LAS LISTAS HEXADECIMAL Y BINARIA PARA GUARDAR TXT
with open(RESULTADO_ARCHIVO, 'a',encoding='UTF-8') as ARCHIVO:
    ARCHIVO.write(f"Archivo: {sys.argv[1]}\n")
    for indice, numero in enumerate(MASTER):
        binario = LISTA_BINARIA[indice]
        hexadecimal = LISTA_HEXADECIMAL[indice]
        ARCHIVO.write(f"DECIMAL: {numero} BINARIO: {binario} HEXADECIMAL: {hexadecimal}\n")
        print(f"DECIMAL: {numero} BINARIO: {binario} HEXADECIMAL: {hexadecimal}")
    ARCHIVO.write(f"Tiempo de ejecución:{TIEMPO_FINAL}\n")
print(f"Tiempo de ejecución: {TIEMPO_FINAL} segundos")
