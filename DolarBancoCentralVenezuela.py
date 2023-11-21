import telebot
import json
import pyBCV
import sys, signal, requests, threading, time

# Funcion para una salida limpia  se la copie a s4vitar :D

def def_handler(sig,frame):
    print("\n\n[!] Apango Bot...\n")
    sys.exit(1)

#Ctrl+C
signal.signal(signal.SIGINT, def_handler) 

# api token bot
API_TOKEN = 'AQui iria tu token del godfatherbot de telegram '
bot = telebot.TeleBot(API_TOKEN)

# Funcion que consulta el dolar y mas adelante se llamara esta funcion con un comando del bot
def get_dolar_price():
    try:
        dolar_price = pyBCV.Currency().get_rate(currency_code='USD')
        return dolar_price
    except Exception as e:
        bot.send_message(message.chat.id, f'Error al obtener la tasa de cambio: {e}')

#Funcion Euro y mas adelante se llamara esta funcion con un comando del bot

def get_euro_price():
    try:
        euro_precio_actual = pyBCV.Currency().get_rate(currency_code='EUR')
        return euro_precio_actual
    except Exception as e:
        bot.send_message(message.chat.id, f'Error al obtener la tasa de cambio: {e}')

# Comando Start + introduccion

@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.reply_to(message, """
Hola soy el bot creado por @CriptoResuelve 
Usame para saber el Precio Del Dolar/Bolivar
Estos son los comandos disponibles:
/Precio_BCV
/Ayuda
/DonacionesUSDT
""")

@bot.message_handler(func=lambda message: message.text not in ['/start', '/Precio_BCV', '/Ayuda', '/DonacionesUSDT'])
def cmd_invalid_command(message):
    bot.send_message(message.chat.id, 'Ese comando no es valido.\n Comando Validos\n /start \n/Precio_BCV \n/Ayuda \n/DonacionesUSDT')




#comando DonacionesUSDT comando  para que envie las billeteras  cripto en este caso estan las mias
@bot.message_handler(commands=['DonacionesUSDT'])
def cmd_DonacionesUSDT(message):
    bot.reply_to(message, "Wallet USDT por la RED TRC:\n TPEXBHP3cFEnM7zf4Kh6cLsVPfYMgbeHgW  ")
    bot.reply_to(message, "Wallet USDT por la RED BEP20(BSC): \n0x7488d00AB9ceE205343C28c94D93fD7A2F8fDa48")
    
#Comando "Ayuda"  Help
@bot.message_handler(commands=['Ayuda'])
def cmd_Ayuda(message):
    bot.reply_to(message, "Presiona o escribe  /Precio_BCV  el bot te dara respuesta  sobre el precio del Dolar y el Euro en Bolivares")

#Comando "Precio BCV"  trae las funciones   que fueron creadas arriba
@bot.message_handler(commands=['Precio_BCV'])
def cmd_Precio_BCV(message):
    # Obtener la tasa de cambio del dólar
    dolar_price = get_dolar_price()
    euro_precio_actual = get_euro_price()

    # Enviar la tasa de cambio al usuario
    bot.send_message(message.chat.id, f'El precio del $DOLAR es de\n {dolar_price}  segun el BCV.')
    bot.send_message(message.chat.id, f'El precio del $EURO es:\n {euro_precio_actual} segun el BCV')
    bot.send_message(message.chat.id, f'Fecha Valor: \nEl  {pyBCV.Currency().get_rate(currency_code="Fecha")}.')


if __name__ == '__main__':
    print('--iniciando el BOT-- ')
    bot.infinity_polling()
   
