# pyhtonarchive
Listado y descarga de archivos en una web con Python


# Requisitos:
- Python.
- pip.
- requests o wget
- beautifulsoup4
- tqdm.

      py o python -m pip install -upgrade pip

      pip install requests beautifulsoup4 tqdm

# Utilizando requerimientos.txt
    pip install -r requerimientos.txt

## Versión 1:
	Solo obtenemos un listado en el repl con la ruta y el nombre de todos los archivos con extensión zip


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
    enlace = 'https://ejemplo.com/carpeta_con_archivos_zip/'
    nombres_archivos_zip = obtener_nombres_archivos_zip(enlace)
    
    if nombres_archivos_zip:
        print("Nombres de archivos ZIP encontrados:")
        for nombre_archivo in nombres_archivos_zip:
            print(nombre_archivo)
    else:
        print("No se encontraron archivos ZIP en el enlace proporcionado.")


## Versión 2:
	Se guarda lo obtenido en un txt.


    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    
    def obtener_nombres_archivos_zip(enlace):
        respuesta = requests.get(enlace)
    
        if respuesta.status_code == 200:
            soup = BeautifulSoup(respuesta.text, 'html.parser')
            enlaces_zip = soup.find_all('a', href=lambda href: (href and href.endswith('.zip')))
            nombres_archivos_zip = [urljoin(enlace, enlace_zip['href']) for enlace_zip in enlaces_zip]
    
            return nombres_archivos_zip
        else:
            print(f"Error al acceder al enlace. Código de estado: {respuesta.status_code}")
            return []
    
    def guardar_nombres_archivos_en_archivo(nombres_archivos, nombre_archivo_salida):
        with open(nombre_archivo_salida, 'w') as archivo:
            for nombre_archivo in nombres_archivos:
                archivo.write(nombre_archivo + '\n')
    
    # Ejemplo de uso
    enlace = 'https://ejemplo.com/carpeta_con_archivos_zip/'
    nombres_archivos_zip = obtener_nombres_archivos_zip(enlace)
    
    if nombres_archivos_zip:
        print("Nombres de archivos ZIP encontrados:")
        for nombre_archivo in nombres_archivos_zip:
            print(nombre_archivo)
    
        # Guardar los nombres en un archivo
        archivo_salida = 'nombres_archivos_zip.txt'
        guardar_nombres_archivos_en_archivo(nombres_archivos_zip, archivo_salida)
        print(f"Listado de nombres de archivos guardado en '{archivo_salida}'.")
    else:
        print("No se encontraron archivos ZIP en el enlace proporcionado.")


## Versión 3:
	Solo un listado con los nombres, sin path, sin extensión.


    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    import os
    
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
    
    def guardar_nombres_archivos_en_archivo(nombres_archivos, nombre_archivo_salida):
        with open(nombre_archivo_salida, 'w') as archivo:
            for nombre_archivo in nombres_archivos:
                archivo.write(nombre_archivo + '\n')
    
    # Ejemplo de uso
    enlace = 'https://ejemplo.com/carpeta_con_archivos_zip/'
    nombres_archivos_zip = obtener_nombres_archivos_zip(enlace)
    
    if nombres_archivos_zip:
        print("Nombres de archivos ZIP encontrados:")
        for nombre_archivo in nombres_archivos_zip:
            print(nombre_archivo)
    
        # Guardar los nombres en un archivo
        archivo_salida = 'nombres_archivos.txt'
        guardar_nombres_archivos_en_archivo(nombres_archivos_zip, archivo_salida)
        print(f"Listado de nombres de archivos guardado en '{archivo_salida}'.")
    else:
        print("No se encontraron archivos ZIP en el enlace proporcionado.")


## Versión 4:
	Guardar dicha lista en otro archivo pero formando una lista de Python para ser reutilizada.


    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    import os
    
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
            archivo.write("archivos = " + repr(nombres_archivos))
    
    # Ejemplo de uso
    enlace = 'https://ejemplo.com/carpeta_con_archivos_zip/'
    nombres_archivos_zip = obtener_nombres_archivos_zip(enlace)
    
    if nombres_archivos_zip:
        print("Nombres de archivos ZIP encontrados:")
        for nombre_archivo in nombres_archivos_zip:
            print(nombre_archivo)
    
        # Guardar los nombres como código de Python en un archivo
        archivo_salida = 'nombres_archivos_python.py'
        guardar_nombres_archivos_en_archivo_como_codigo_python(nombres_archivos_zip, archivo_salida)
        print(f"Lista de nombres de archivos guardada como código de Python en '{archivo_salida}'.")
    else:
        print("No se encontraron archivos ZIP en el enlace proporcionado.")


## Versión 5 Descarga con wget:
    Reutilizando la lista obtenida, pero requiere que Wget esté instalado en el dispositivo.


    import subprocess
    
    archivos = ['armora', 'astrob', 'astrof', 'battles', 'berzerk', 'blockade', 'boothill', 'bosco', 'buckrog', 'carnival', 'circus', 'congo', 'cosmicg', 'depthch', 'dkong', 'dkongjr', 'elim2', 'galaga', 'gorf', 'gridlee', 'invaders', 'invinco', 'mario', 'monsterb', 'natodef', 'panic', 'polepos', 'pulsar', 'qbert', 'rallyx', 'reactor', 'ripoff', 'seawolf', 'sharkatt', 'solarq', 'spaceod', 'spacewar', 'spacfury', 'starcas', 'starcrus', 'startrek', 'subroc3d', 'sundance', 'tacscan', 'tankbatt', 'targ', 'thehand', 'thief', 'turbo', 'vanguard', 'warrior', 'wow', 'xevios', 'xevious', 'zaxxon', 'zektor']
    
    path1 = "https://ejemplo.com/carpeta_con_archivos_zip/"
    path2 = "micarpeta/misarchivos/bajados/"
    
    for archivo in archivos:
        url = path1 + archivo + ".zip"
        destino = path2 + archivo + ".zip"
        
        comando_wget = f"wget -c {url} -P {destino}"
        
        # Ejecutar el comando wget
        try:
            subprocess.run(comando_wget, shell=True, check=True)
            print(f"Archivo {archivo}.zip descargado correctamente.")
        except subprocess.CalledProcessError as e:
            print(f"Error al descargar {archivo}.zip: {e}")
    ´´´´
    
    
    ## Versión 6 Descarga con requests:
       Que ya viene en Python:
    
        import requests
        import os
        
        archivos = ['armora', 'astrob', 'astrof', 'battles', 'berzerk', 'blockade', 'boothill', 'bosco', 'buckrog', 'carnival', 'circus', 'congo', 'cosmicg', 'depthch', 'dkong', 'dkongjr', 'elim2', 'galaga', 'gorf', 'gridlee', 'invaders', 'invinco', 'mario', 'monsterb', 'natodef', 'panic', 'polepos', 'pulsar', 'qbert', 'rallyx', 'reactor', 'ripoff', 'seawolf', 'sharkatt', 'solarq', 'spaceod', 'spacewar', 'spacfury', 'starcas', 'starcrus', 'startrek', 'subroc3d', 'sundance', 'tacscan', 'tankbatt', 'targ', 'thehand', 'thief', 'turbo', 'vanguard', 'warrior', 'wow', 'xevios', 'xevious', 'zaxxon', 'zektor']
        
        path1 = "https://ejemplo.com/carpeta_con_archivos_zip/"
        path2 = "micarpeta/misarchivos/bajados/"
        
        for archivo in archivos:
            url = path1 + archivo + ".zip"
            destino = os.path.join(path2, archivo + ".zip")
            
            # Descargar el archivo con requests
            try:
                response = requests.get(url, stream=True)
                response.raise_for_status()
                
                with open(destino, 'wb') as archivo_descargado:
                    for chunk in response.iter_content(chunk_size=8192):
                        archivo_descargado.write(chunk)
                        
                print(f"Archivo {archivo}.zip descargado correctamente.")
            except requests.exceptions.RequestException as e:
                print(f"Error al descargar {archivo}.zip: {e}")


## Versión 7 Descarga con requests con tqdm:
   Agrega una barra de progreso.

    import requests
    import os
    from tqdm import tqdm
    
    archivos = ['armora', 'astrob', 'astrof', 'battles', 'berzerk', 'blockade', 'boothill', 'bosco', 'buckrog', 'carnival', 'circus', 'congo', 'cosmicg', 'depthch', 'dkong', 'dkongjr', 'elim2', 'galaga', 'gorf', 'gridlee', 'invaders', 'invinco', 'mario', 'monsterb', 'natodef', 'panic', 'polepos', 'pulsar', 'qbert', 'rallyx', 'reactor', 'ripoff', 'seawolf', 'sharkatt', 'solarq', 'spaceod', 'spacewar', 'spacfury', 'starcas', 'starcrus', 'startrek', 'subroc3d', 'sundance', 'tacscan', 'tankbatt', 'targ', 'thehand', 'thief', 'turbo', 'vanguard', 'warrior', 'wow', 'xevios', 'xevious', 'zaxxon', 'zektor']
    
    path1 = "https://ejemplo.com/carpeta_con_archivos_zip/"
    path2 = "micarpeta/misarchivos/bajados/"
    
    for archivo in archivos:
        url = path1 + archivo + ".zip"
        destino = os.path.join(path2, archivo + ".zip")
        
        # Descargar el archivo con requests y mostrar una barra de progreso
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            # Obtener el tamaño total del archivo
            total_size = int(response.headers.get('content-length', 0))
            
            # Configurar la barra de progreso
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


## Versión 8 Integrando obtención y descarga:
   De esta manera se colocan los Paths y el link.

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
    enlace = 'https://ejemplo.com/carpeta_con_archivos_zip/'
    path_descarga = 'micarpeta/misarchivos/bajados/'
    
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


## Versión 9 cualquier extensión:
	Por defecto se establece zip, pero con la variable extension_archivo se la puede cambiar.

    import requests
    import os
    from tqdm import tqdm
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    
    def obtener_nombres_archivos(enlace, extension='.zip'):
        respuesta = requests.get(enlace)
    
        if respuesta.status_code == 200:
            soup = BeautifulSoup(respuesta.text, 'html.parser')
            enlaces_archivos = soup.find_all('a', href=lambda href: (href and href.endswith(extension)))
            nombres_archivos = [os.path.basename(urljoin(enlace, enlace_archivo['href'])).replace(extension, '') for enlace_archivo in enlaces_archivos]
    
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
    enlace = 'https://archive.org/download/MAME2003_Reference_Set_MAME0.78_ROMs_CHDs_Samples/samples/'
    path_descarga = 'RetroPie/bios/mame-2003/samples'
    extension_archivo = '.jpg'
    
    nombres_archivos_zip = obtener_nombres_archivos(enlace, extension_archivo)
    
    if nombres_archivos_zip:
        print(f"Nombres de archivos con extensión '{extension_archivo}' encontrados:")
        for nombre_archivo in nombres_archivos_zip:
            print(nombre_archivo)
    
        # Guardar los nombres como código de Python en un archivo
        archivo_salida_python = 'nombres_archivos_python.py'
        guardar_nombres_archivos_en_archivo_como_codigo_python(nombres_archivos_zip, archivo_salida_python)
        print(f"Lista de nombres de archivos guardada como código de Python en '{archivo_salida_python}'.")
    
        # Descargar los archivos
        descargar_archivos(nombres_archivos_zip, enlace, path_descarga, extension_archivo)
    else:
        print(f"No se encontraron archivos con extensión '{extension_archivo}' en el enlace proporcionado.")


## Versión 10 con Regex:
	Para filtrar y solo descargar una parte los que empiezan con numeros y de la a a la F.

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
                enlaces_archivos = soup.find_all('a', href=lambda href: (href and re.match(filtro_regex, href)))
            else:
                enlaces_archivos = soup.find_all('a', href=lambda href: (href and href.endswith(extension)))
            
            nombres_archivos = [os.path.basename(urljoin(enlace, enlace_archivo['href'])).replace(extension, '').strip() for enlace_archivo in enlaces_archivos]
    
    	# Eliminar elementos vacíos de la lista
            nombres_archivos = list(filter(None, nombres_archivos))
    
            return nombres_archivos
        else:
            print(f"Error al acceder al enlace. Código de estado: {respuesta.status_code}")
            return []
    
    def guardar_nombres_archivos_en_archivo_como_codigo_python(nombres_archivos, nombre_archivo_salida):
        with open(nombre_archivo_salida, 'w') as archivo:
            archivo.write(f"archivos = {repr(nombres_archivos)}\n")
    
    def descargar_archivos(archivos, enlace, path2, extension='.zip'):
        for archivo in archivos:
            url = urljoin(enlace, archivo + extension)  # Corregir la construcción de la URL
            destino = os.path.join(path2, archivo + extension)
    
            print(f"Intentando descargar desde la URL: {url}")
    
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
    #De la G a la M es filtro_regex = re.compile('^[g-mG-M]')
    ##De la N a la Z es filtro_regex = re.compile('^[n-zN-Z]')
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


