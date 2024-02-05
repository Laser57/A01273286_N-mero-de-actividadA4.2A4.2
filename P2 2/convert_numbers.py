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
tiempo_inicio = time.time()
master = []
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '.', ',']
RESULTADO_ARCHIVO = "ConvertionResults.txt"
NOMBRE_ARCHIVO = sys.argv[1]
#LEEMOS ARCHIVO, NOS ASEGURAMOS QUE LOS VALORES NUMERICOS SEAN VALIDOS
#EN CASO QUE NO SE OMITE EL VALOR
with open(NOMBRE_ARCHIVO, 'r', encoding='UTF-8') as file:
    for linea in file:
        AUX = ""
        for i in linea.strip():
            if i in numeros:
                AUX += i
            else:
                break
        if AUX != "":
            master.append(int(AUX))
        else:
            print(f"Linea {linea} con valor invalido, se omite")
#PARTE BINARIA, SE GUARDA EL RESULTADO EN UNA LISTA
lista_binaria=[]
for numero in master:
    BINARIO=""
    NEGATIVO=False
#BANDERA NEGATIVA, EN CASO DE SER NEGATIVO PASAMOS VALOR ABSOLUTO
    if numero<0:
        NEGATIVO=True
        numero=abs(numero)
#USAREMOS EL RESIDUO DE LA OPERACION MODULO % LA BASE NUMERICO
    while numero > 0:
        residuo = numero % 2
        BINARIO = str(residuo) + BINARIO
        numero //= 2
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
            bit1 = int(BINARIO[i])
            bit2 = int(COMPLEMENTO[i])
            suma_bit = bit1 + bit2 + ACARREO
            RESULTADO = str(suma_bit % 2) + RESULTADO
            ACARREO = suma_bit // 2
        if ACARREO:
            RESULTADO = "1" + RESULTADO
        lista_binaria.append(RESULTADO)
    else:
        lista_binaria.append(BINARIO)
#PARTE HEXADECIMAL USAMOS OPERACION MODULO %16
lista_hexadecimal=[]
for numero in master:
    HEX=""
    if numero < 0:
        numero = 2**32 + numero
    while numero > 0:
        residuo = numero % 16
#APLICAMOS TRANSFORMACION DE NUMERO PARA VALORES MAYORES A 16 A,B,C,D,E,F
        if residuo>=10:
            residuo=chr(ord('A') + residuo - 10)
        HEX = str(residuo) + HEX
        numero //= 16
    lista_hexadecimal.append(HEX)
##CALCULAMOS TIEMPO FINAL
tiempo_final = time.time() - tiempo_inicio
#VACIAMOS EL LAS LISTAS HEXADECIMAL Y BINARIA PARA GUARDAR TXT
with open(RESULTADO_ARCHIVO, 'a',encoding='UTF-8') as ARCHIVO:
    ARCHIVO.write(f"Archivo: {sys.argv[1]}\n")
    for indice, numero in enumerate(master):
        binario = lista_binaria[indice]
        hexadecimal = lista_hexadecimal[indice]
        ARCHIVO.write(f"DECIMAL: {numero} BINARIO: {binario} HEXADECIMAL: {hexadecimal}\n")
        print(f"DECIMAL: {numero} BINARIO: {binario} HEXADECIMAL: {hexadecimal}")
    ARCHIVO.write(f"Tiempo de ejecución:{tiempo_final}\n")
print(f"Tiempo de ejecución: {tiempo_final} segundos")
