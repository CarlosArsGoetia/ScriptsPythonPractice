#!/usr/bin/env python3
import qrcode
import argparse

# el url se lo pasaremos con un Argumento al ejecutar el script
#Ejemplo python3 /ruta/al/archivo/generando_qr.py -u https://www.chess.com

def get_arguments():
    parser = argparse.ArgumentParser(description="[!]Generador QR (Agrega una URL): ")
    parser.add_argument("-u", "--url", required=True, dest="url", help="Usa -u  o --url  https://xxxxxxx.com")
    return parser.parse_args()


def main():
    
    args = get_arguments()
    url = args.url  
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=8, border=3)
    data_uri = f"{url}"
    qr.add_data(data_uri)  
    qr.make(fit=True)
    image = qr.make_image(fill_color="black", back_color="white")  
    image.save('qrcode.png')
    print(f"[+]----->Proceso finalizado<----------")
    
   
if __name__ == "__main__":
    main()