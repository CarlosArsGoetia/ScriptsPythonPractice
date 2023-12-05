#!/usr/bin/python3
import sys, signal

#un script que hice para ahorrar tiempo mientras arbitro usdt

def def_handler(sig,frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

#Ctrl+C
signal.signal(signal.SIGINT, def_handler)

###Script para calcular comision(tu decides la comision)  sobre el precio  del usdt


try:
  usdt = float(input("Introduce el precio de compra del USDT: "))
except ValueError:
  print("El valor introducido no es un número válido.")
  exit()
#si no introduce un valor valido se ejecuta una salida limpia

porcentaje = float(input("Introduce el porcentaje de la comisión: "))

comision = usdt * porcentaje / 100
comision = round(comision)

precio_final = usdt + comision

print(f"el precio del usdt:\n {usdt:.2f}")
print(f"comision detallada:\n {comision}")
print(f"El precio final seria de:\n {precio_final}")
