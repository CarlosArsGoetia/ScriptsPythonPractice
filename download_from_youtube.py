#!/usr/bin/env python3
import os
from pytube import YouTube
import sys, signal

def def_handler(sig,frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

#Ctrl+C
signal.signal(signal.SIGINT, def_handler)

#El usuario tiene tres opciones [1]Descargar Video con audio  [2]Descargar solo AUDIO [3]Las dos opciones a la vez

while True:
    options = input("\n[1]Descargar Video con audio  \n\n[2]Descargar solo AUDIO\n  \n\n[3] Descargar Video con audio + Audio por separado)\n\n[++]Introduce tu opcion (numero): ")
    if options.isdigit() and int(options) in [1, 2, 3]:
        break
    else:
        print("[!]Solo Hay tres opciones  \n[1] \n[2] \n[3]")
        exit(1)


if options == "1":
    try:
        pwd = os.getcwd()
        url = input("\n[+]Introduce el link del video: ")
        # la variable se llama  asi "yt" como en la documentacion 
        yt = YouTube(url)

        titulo_del_video = yt.title
        cantidad_de_visitas = yt.views
        video = yt.streams.get_highest_resolution()
        video.download(pwd)
        print(f"\n[+] Tituo del video: '{titulo_del_video}'  ")
        print(f"\n[+]Este video tiene {cantidad_de_visitas} visitas")
        print (f"\n[+]El video fue  guardado en {pwd}\n")

    except Exception as error:
    # Manejar errores
        print(f"\n[!]Ocurrió un error al descargar el video: {error}\n")
        exit(1)
    
if options == "2":
    try:
        pwd = os.getcwd()
        url = input("\n[+]Introduce el link del video: ")
        # la variable se llama  asi "yt" como en la documentacion 
        yt = YouTube(url)

        titulo_del_video = yt.title
        cantidad_de_visitas = yt.views
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_file_path = audio_stream.download(pwd, filename= titulo_del_video+'_Audio.mp3')
    
        print(f"\n[+] Tituo del video: '{titulo_del_video}'  ")
        print(f"\n[+]Este video tiene {cantidad_de_visitas} visitas")
        print (f"\n[+]El Audio fue  guardado en {pwd}\n")

    except Exception as error:
        # Manejar errores
        print(f"\n[!]Ocurrió un error al descargar el audio del video: {error}\n")
        exit(1)

else:
        try:

            pwd = os.getcwd()
            url = input("\n[!]Introduce el link del video: ")
            # la variable se llama  asi "yt" como en la documentacion 
            yt = YouTube(url)

            titulo_del_video = yt.title
            cantidad_de_visitas = yt.views
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_file_path = audio_stream.download(pwd, filename= titulo_del_video+'_Audio.mp3')
            video = yt.streams.get_highest_resolution()
            video.download(pwd)
    
            print(f"\n[+] Tituo del video: '{titulo_del_video}'  ")
            print(f"\n[+]Este video tiene {cantidad_de_visitas} visitas")
            print (f"\n[+]El Audio  y el Video fueron  guardados en {pwd}\n")
        
        except Exception as error:
            # Manejar errores
            print(f"\n[!]Ocurrió un error al descargar el audio del video: {error}\n")
            exit(1)


#Saludos 