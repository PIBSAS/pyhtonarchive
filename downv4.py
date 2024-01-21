import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def obtener_nombres_archivos_zip(enlace):
    respuesta = requests.get(enlace)

    if respuesta.status_code == 200:
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        enlaces_zip = soup.find_all('a', href=lambda href: (href and href.endswith('.zip')))
        nombres_archivos_zip = [os.path.basename(urljoin(enlace, enlace_zip['href'])).replace('.zip', '') for enlace_zip in enlaces_zip]

        return nombres_archivos_zip
    else:
        print(f"Error al acceder al enlace. Código de estado: {respuesta.status_code}")
        return []

def guardar_nombres_archivos_en_archivo_como_codigo_python(nombres_archivos, nombre_archivo_salida):
    with open(nombre_archivo_salida, 'w') as archivo:
        archivo.write(f"archivos = {repr(nombres_archivos)}\n")

def descargar_archivos(archivos, path1, path2):
    for archivo in archivos:
        url = path1 + archivo + ".zip"
        destino = os.path.join(path2, archivo + ".zip")

        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            total_size = int(response.headers.get('content-length', 0))
            barra_progreso = tqdm(total=total_size, unit='B', unit_scale=True, desc=f"Descargando {archivo}.zip")

            with open(destino, 'wb') as archivo_descargado:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        archivo_descargado.write(chunk)
                        barra_progreso.update(len(chunk))

            barra_progreso.close()
            print(f"Archivo {archivo}.zip descargado correctamente.")
        except requests.exceptions.RequestException as e:
            print(f"Error al descargar {archivo}.zip: {e}")

# Ejemplo de uso
enlace = 'https://archive.org/download/MAME2003_Reference_Set_MAME0.78_ROMs_CHDs_Samples/samples/'
path_descarga = 'RetroPie/bios/mame-2003/samples'

nombres_archivos_zip = obtener_nombres_archivos_zip(enlace)

if nombres_archivos_zip:
    print("Nombres de archivos ZIP encontrados:")
    for nombre_archivo in nombres_archivos_zip:
        print(nombre_archivo)

    # Guardar los nombres como código de Python en un archivo
    archivo_salida_python = 'nombres_archivos_python.py'
    guardar_nombres_archivos_en_archivo_como_codigo_python(nombres_archivos_zip, archivo_salida_python)
    print(f"Lista de nombres de archivos guardada como código de Python en '{archivo_salida_python}'.")

    # Descargar los archivos
    descargar_archivos(nombres_archivos_zip, enlace, path_descarga)
else:
    print("No se encontraron archivos ZIP en el enlace proporcionado.")
