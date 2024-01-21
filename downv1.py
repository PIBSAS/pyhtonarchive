import subprocess

archivos = ['armora', 'astrob', 'astrof', 'battles', 'berzerk', 'blockade', 'boothill', 'bosco', 'buckrog', 'carnival', 'circus', 'congo', 'cosmicg', 'depthch', 'dkong', 'dkongjr', 'elim2', 'galaga', 'gorf', 'gridlee', 'invaders', 'invinco', 'mario', 'monsterb', 'natodef', 'panic', 'polepos', 'pulsar', 'qbert', 'rallyx', 'reactor', 'ripoff', 'seawolf', 'sharkatt', 'solarq', 'spaceod', 'spacewar', 'spacfury', 'starcas', 'starcrus', 'startrek', 'subroc3d', 'sundance', 'tacscan', 'tankbatt', 'targ', 'thehand', 'thief', 'turbo', 'vanguard', 'warrior', 'wow', 'xevios', 'xevious', 'zaxxon', 'zektor']

path1 = "https://archive.org/download/MAME2003_Reference_Set_MAME0.78_ROMs_CHDs_Samples/samples/"
path2 = "RetroPie/bios/mame-2003/samples"

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
