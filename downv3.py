import requests
import os
from tqdm import tqdm

archivos = ['armora', 'astrob', 'astrof', 'battles', 'berzerk', 'blockade', 'boothill', 'bosco', 'buckrog', 'carnival', 'circus', 'congo', 'cosmicg', 'depthch', 'dkong', 'dkongjr', 'elim2', 'galaga', 'gorf', 'gridlee', 'invaders', 'invinco', 'mario', 'monsterb', 'natodef', 'panic', 'polepos', 'pulsar', 'qbert', 'rallyx', 'reactor', 'ripoff', 'seawolf', 'sharkatt', 'solarq', 'spaceod', 'spacewar', 'spacfury', 'starcas', 'starcrus', 'startrek', 'subroc3d', 'sundance', 'tacscan', 'tankbatt', 'targ', 'thehand', 'thief', 'turbo', 'vanguard', 'warrior', 'wow', 'xevios', 'xevious', 'zaxxon', 'zektor']

path1 = "https://archive.org/download/MAME2003_Reference_Set_MAME0.78_ROMs_CHDs_Samples/samples/"
path2 = "RetroPie/bios/mame-2003/samples/"

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
