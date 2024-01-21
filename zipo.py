import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def obtener_nombres_archivos_zip(enlace):
    # Realizar la solicitud GET al enlace
    respuesta = requests.get(enlace)

    # Verificar si la solicitud fue exitosa (código 200)
    if respuesta.status_code == 200:
        # Utilizar BeautifulSoup para analizar el HTML
        soup = BeautifulSoup(respuesta.text, 'html.parser')

        # Encontrar todos los enlaces que terminan con '.zip'
        enlaces_zip = soup.find_all('a', href=lambda href: (href and href.endswith('.zip')))

        # Construir la lista de nombres de archivos ZIP completos
        nombres_archivos_zip = [urljoin(enlace, enlace_zip['href']) for enlace_zip in enlaces_zip]

        return nombres_archivos_zip
    else:
        print(f"Error al acceder al enlace. Código de estado: {respuesta.status_code}")
        return []

# Ejemplo de uso
enlace = 'https://archive.org/download/MAME2003_Reference_Set_MAME0.78_ROMs_CHDs_Samples/roms/'
nombres_archivos_zip = obtener_nombres_archivos_zip(enlace)

if nombres_archivos_zip:
    print("Nombres de archivos ZIP encontrados:")
    for nombre_archivo in nombres_archivos_zip:
        print(nombre_archivo)
else:
    print("No se encontraron archivos ZIP en el enlace proporcionado.")
