#!/usr/bin/env python3
import sys, signal

def def_handler(sig,frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

#Para una salida limpia
signal.signal(signal.SIGINT, def_handler)

#Empezamos

welcome = "Bienvenido a un Script Basico para calcular la noche de Pizzas\n La receta va de mi parte :D "
print(f"Hola // {welcome}")

#receta representada en porcentajes

harina = 100
agua = 57
levadura = 2
sal = 2.4
aceite = 15

#Suma de todos los ingredientes para calcular el Factor Panadero(bf)
total_ingredients = harina + agua + aceite + levadura + sal

#Tambien necesitamos preguntar por el peso del paston
while True:
    print(f"[+]TIP--el peso una de Pizza pequeña promedio oscila entre 200 a 300 gramos\n")
    weight  = input("[+]¿Cuantos gramos quieres que pese el paston (masa total)?:  ")
    if weight.isnumeric() is True:
        weight = int(weight)    
        break
    else:
        print("[!] Ingrese el valor en gramos \n Ejemplo 1000 para un kilo | 1500  seria un Kilo y medio")



#Con el peso y la suma total de porcetajes de los ingredientes
bf = weight  / total_ingredients

#Por cortesia mostramos el Factor Panadero
print(f"\nTu factor panadero es de: {bf:.2f}")
#trasparemos la receta de 'porcentaje' a 'gramos'
f_grams = bf * harina
w_grams = bf * agua
y_grams = bf * levadura
s_grams = bf * sal  
o_grams = bf * aceite

#Mostramosla receta que varia en proporciones dependiendo del tamaño del paston

print(f"\nTu receta para hacer un paston de masa para pizza que pesara: {weight}gr ")
print(f"[+]Harina Panadera: {f_grams.__round__():.0f}gr")
print(f"[+]Agua: {w_grams.__round__():.0f}gr")
print(f"[+]Levadura: {y_grams.__round__():.0f}gr")
print(f"[+]Sal: {s_grams.__round__():.0f}gr")
print(f"[+]Aceite: {o_grams.__round__():.0f}gr")
print(f"\n[!]Despues del correcto amasado---> Deja la masa en reposo 30min (Cubierta)\nBuen Provecho-")


