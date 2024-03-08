#!/usr/bin/env python3
import sys, signal
import requests

#Script para definir comisiones del proyecto Labora

#Funcion de salida limpia

def def_handler(sig,frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)
#Asignamos la funcion a Ctrl+C
signal.signal(signal.SIGINT, def_handler)

#automatizar la introduccion de la data del Dolar Tarjeta y Dolar Cripto requests en https://app.dolarapi.com/

def Dolar_tarjeta():
    
    response = requests.get("https://dolarapi.com/v1/dolares/tarjeta")
    precio_tarjeta_api = int(response.json()["venta"])
    return precio_tarjeta_api

def Dolar_Cripto():
    response = requests.get("https://dolarapi.com/v1/dolares/cripto")
    precio_usdt = int(response.json()["venta"])
    return precio_usdt

#Definir el precio del curso pagado al dolar tarjeta  
precio_tarjeta_api = Dolar_tarjeta() 
total_en_dolares_del_curso = int(input("[+]Introduce el precio del curso en dolares: "))
monto_curso_pagado_tarjeta =  total_en_dolares_del_curso * precio_tarjeta_api

#Calculo de la compra en usdt
precio_usdt_api = Dolar_Cripto()
precio_del_curso_sin_comision =  precio_usdt_api * total_en_dolares_del_curso

#La comision se aplica a la diferencia entre los precios del curso

diferencia = monto_curso_pagado_tarjeta - precio_del_curso_sin_comision
comision = diferencia * 20 / 100

#Precios finales

TOTAL_FINAL =   precio_del_curso_sin_comision + comision
Ahorro_Final =  monto_curso_pagado_tarjeta - TOTAL_FINAL
cotizacion_real = TOTAL_FINAL / total_en_dolares_del_curso

print(f"\n[!]Total Del curso al ser pagado al Dolar Tarjeta: {monto_curso_pagado_tarjeta} Pesos Argentinos")
print(f"\n[+]El total Del curso Con descuento incluido mas la comision es de: {TOTAL_FINAL} Pesos  Argentinos")
print(f"\n[+]Ahorro Final: {Ahorro_Final:.2f} Pesos Argentinos\n")
print(f"\n[+]Pagas el dolar a: {cotizacion_real:.2f} Pesos Argentinos\n\n")
