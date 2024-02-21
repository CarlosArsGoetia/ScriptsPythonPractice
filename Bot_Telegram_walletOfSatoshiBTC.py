import telebot
import requests
import cryptocompare

import sys, signal, threading

def def_handler(sig,frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

#Ctrl+C
signal.signal(signal.SIGINT, def_handler)



# Define la comisión.
comision = 0.003

url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
response = requests.get(url)
precio_bitcoin = int(float(response.json()["data"]["amount"]))


API_TOKEN = 'AQUI VA TU TOKEN DEL BOT'  
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.reply_to(message, """
Hola fui creado por CriptoResuelve @WHYYOUFOLLOWTHEHYPE 
para facilitar el rulo (no renieges con la conversion)
Dime cuantos satoshis tienes y te dire  de cuanto es la orden para sacarlos
por la  red Lightning (menos la comision de Wallet Of Satoshis)

ejemplo  ""/convertir 10500""


/help
/donate
/convertir

Este bot esta en linea en una pagina gratuita por ahora  
Dona  para poder mantenerlo 24/7

""")

@bot.message_handler(commands=['help'])
def cmd_help(message):
    bot.reply_to(message, "usa el comando /convertir +  tu cantidad de satoshis  \nusa el comando /donate y te paso la wallet")



@bot.message_handler(commands=['donate'])
def cmd_donate(message):
    bot.reply_to(message, "Donaciones RED BEP20: \n0x83f78501F39cA95843f6d2ADE76cb58D5dB9Cb0d \n  Donaciones RED Polygon:  \n0x305bE3B153Ce7525dBbB00ffcB8d80ddf345CFE9 ")





# Define el comando /convertir.
@bot.message_handler(commands=["convertir"])
def convertir(message):
    # Obtiene los satoshis del mensaje.
    satoshis = message.text.split(" ")[1]
    
    # Comprueba si la cantidad de satoshis es válida.
    try:
        satoshis = int(satoshis)
    except ValueError:
        bot.send_message(message.chat.id, "La cantidad de satoshis debe ser un número entero.")
        return
    if satoshis < 10500:
        bot.send_message(message.chat.id,"La cantidad de satoshis debe ser mayor o igual a 10500.")
        return
    

    
    # Calcula la comisión en satoshis.
    comision_satoshis = satoshis * comision

    # Calcula el valor final de los satoshis, teniendo en cuenta la comisión.
    valor_final_dolares = (satoshis - comision_satoshis) * precio_bitcoin / 100000000

    # Calcula la orden, redondeando a 8 decimales.
    orden = round(valor_final_dolares / precio_bitcoin, 8)

    # Envia dos mensajes al usuario.
    bot.send_message(message.chat.id, "Tus satoshis valen $" + str(valor_final_dolares))
    bot.send_message(message.chat.id, "Haz una orden de " + str(orden) + " BTC")


if __name__ == '__main__':
    print('--iniciando el BOT-- ')
    bot.infinity_polling()
