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
with open('TC3.txt', 'r', encoding='UTF-8') as file:
    for linea in file:
        AUX = ""
        for i in linea.strip():
            if i in NUMEROS:
                AUX += i
            else:
                break
        MASTER.append(int(AUX))
LISTA_BINARIA=[]
for NUMERO in MASTER:
    BINARIO=""
    NEGATIVO=False
    if NUMERO<0:
        NEGATIVO=True
        NUMERO=abs(NUMERO)
    while NUMERO > 0:
        RESIDUO = NUMERO % 2
        BINARIO = str(RESIDUO) + BINARIO
        NUMERO //= 2
    if NEGATIVO:
        BINARIO=BINARIO.zfill(8)
        BINARIO="".join('1' if BIT == '0' else '0' for BIT in str(BINARIO))
        COMPLEMENTO = "00000001"
        RESULTADO = ""
        ACARREO = 0
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
LISTA_HEXADECIMAL=[]
for NUMERO in MASTER:
    HEX=""
    if NUMERO < 0:
        NUMERO = 2**32 + NUMERO
    while NUMERO > 0:
        RESIDUO = NUMERO % 16
        if RESIDUO>=10:
            RESIDUO=chr(ord('A') + RESIDUO - 10)
        HEX = str(RESIDUO) + HEX
        NUMERO //= 16
    LISTA_HEXADECIMAL.append(HEX)
for indice, numero in enumerate(MASTER):
    binario = LISTA_BINARIA[indice]
    hexadecimal = LISTA_HEXADECIMAL[indice]
    print(f"DECIMAL: {numero} BINARIO: {binario} HEXADECIMAL: {hexadecimal}")
TIEMPO_FINAL = time.time() - TIEMPO_INICIO
print(f"Tiempo de ejecución: {TIEMPO_FINAL} segundos")
