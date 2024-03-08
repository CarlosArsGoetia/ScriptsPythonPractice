import urllib.request 
import os.path
import shutil

def get_html(url):
    req = urllib.request.urlopen(url)
    html = req.read().decode('utf-8')
    return html


def get_file(url):
    req = urllib.request.urlopen(url)
    html = req.read()
    return html


if __name__ == '__main__':
    url = input("Introduce URL: ")
    filename = "target"

    # Descargar archivo
    objetivo = open(f"{filename}.html", "w", encoding="utf-8")
    objetivo.write(get_html(url))
    objetivo.close()

 #Para guardar el archivo de una manera distinta si ya existe ese nombre en el directorio
    if os.path.exists(f"{filename}.html"):
        x = 1
        while os.path.exists(f"{filename}_{x}.html"):
            x += 1

        nuevo_nombre = f"{filename}_{x}.html"

        shutil.copyfile(f"{filename}.html", nuevo_nombre)

        print(f"[!] Script finalizado. Archivos guardados en: {os.getcwd()}\n Bajo el nombre de: {nuevo_nombre}")
