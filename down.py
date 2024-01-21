archivos = ['armora', 'astrob', 'astrof', 'battles', 'berzerk', 'blockade', 'boothill', 'bosco', 'buckrog', 'carnival', 'circus', 'congo', 'cosmicg', 'depthch', 'dkong', 'dkongjr', 'elim2', 'galaga', 'gorf', 'gridlee', 'invaders', 'invinco', 'mario', 'monsterb', 'natodef', 'panic', 'polepos', 'pulsar', 'qbert', 'rallyx', 'reactor', 'ripoff', 'seawolf', 'sharkatt', 'solarq', 'spaceod', 'spacewar', 'spacfury', 'starcas', 'starcrus', 'startrek', 'subroc3d', 'sundance', 'tacscan', 'tankbatt', 'targ', 'thehand', 'thief', 'turbo', 'vanguard', 'warrior', 'wow', 'xevios', 'xevious', 'zaxxon', 'zektor']

path="https://ejemplo.com/carpeta_con_archivos_zip/"
path="micarpeta/misarchivos/bajados/"
for _ in len(archivos):
	wget -c {path}+_+.zip -P {path2}