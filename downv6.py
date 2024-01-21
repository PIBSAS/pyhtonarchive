import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def obtener_nombres_archivos(enlace, extension='.zip', filtro_regex=None):
    respuesta = requests.get(enlace)

    if respuesta.status_code == 200:
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        
        if filtro_regex:
            # Si se proporciona un filtro_regex, usamos expresiones regulares para filtrar los enlaces
            enlaces_archivos = soup.find_all('a', href=lambda href: (href and re.match(filtro_regex, href)))
        else:
            # Si no hay filtro_regex, simplemente obtenemos todos los enlaces con la extensión dada
            enlaces_archivos = soup.find_all('a', href=lambda href: (href and href.endswith(extension)))
        
        nombres_archivos = [os.path.basename(urljoin(enlace, enlace_archivo['href'])).replace(extension, '').strip() for enlace_archivo in enlaces_archivos]

        return nombres_archivos
    else:
        print(f"Error al acceder al enlace. Código de estado: {respuesta.status_code}")
        return []

def guardar_nombres_archivos_en_archivo_como_codigo_python(nombres_archivos, nombre_archivo_salida):
    with open(nombre_archivo_salida, 'w') as archivo:
        archivo.write(f"archivos = {repr(nombres_archivos)}\n")

def descargar_archivos(archivos, path1, path2, extension='.zip'):
    for archivo in archivos:
        url = path1 + archivo + extension
        destino = os.path.join(path2, archivo + extension)

        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            total_size = int(response.headers.get('content-length', 0))
            barra_progreso = tqdm(total=total_size, unit='B', unit_scale=True, desc=f"Descargando {archivo}{extension}")

            with open(destino, 'wb') as archivo_descargado:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        archivo_descargado.write(chunk)
                        barra_progreso.update(len(chunk))

            barra_progreso.close()
            print(f"Archivo {archivo}{extension} descargado correctamente.")
        except requests.exceptions.RequestException as e:
            print(f"Error al descargar {archivo}{extension}: {e}")

# Ejemplo de uso
enlace = 'https://archive.org/download/MAME2003_Reference_Set_MAME0.78_ROMs_CHDs_Samples/roms/'
path_descarga = 'RetroPie/roms/mame-libretro/'
extension_archivo = '.zip'

# Filtro por expresión regular: solo archivos que empiecen con números o letras de A a F
filtro_regex = r'^[0-9A-Fa-f].*'  

nombres_archivos_filtrados = obtener_nombres_archivos(enlace, extension_archivo, filtro_regex)

if nombres_archivos_filtrados:
    print(f"Nombres de archivos con extensión '{extension_archivo}' y filtrados por expresión regular encontrados:")
    for nombre_archivo in nombres_archivos_filtrados:
        print(nombre_archivo)

    # Guardar los nombres como código de Python en un archivo
    archivo_salida_python = 'nombres_archivos_python_filtrados.py'
    guardar_nombres_archivos_en_archivo_como_codigo_python(nombres_archivos_filtrados, archivo_salida_python)
    print(f"Lista de nombres de archivos filtrada guardada como código de Python en '{archivo_salida_python}'.")

    # Descargar los archivos
    descargar_archivos(nombres_archivos_filtrados, enlace, path_descarga, extension_archivo)
else:
    print(f"No se encontraron archivos con extensión '{extension_archivo}' y filtrados por expresión regular en el enlace proporcionado.")
