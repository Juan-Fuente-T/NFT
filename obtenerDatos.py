import requests
import json
from pinata import Pinata

pinata = Pinata('api_key', 'api_secret', 'secret_access_token')

# Filtrar para obtener los archivos con estado 'pinned' y límite de 10 archivos
filters = {
    'status': 'pinned',
    'pageLimit': 15
}

for archivo in archivos:
    # Acceder a la información del archivo
    id = archivo['id']
    ipfs_pin_hash = archivo['ipfs_pin_hash']
    size = archivo['size']

with open('metdatos.json') as json_file:
    data = json.load(json_file)

diccionario = data['diccionario']

# Número total de archivos JSON
total_archivos = 12  # Cambia esto al número total de archivos que tienes

# URL base de Piñata para los JSON y las imágenes
base_url_json = "https://black-ashamed-dove-888.mypinata.cloud/ipfs/QmbFMke1KXqnYyBBWxB74N4c5SBnJMVAiMNRcGu6x1AwQH"
base_url_imagen = "https://black-ashamed-dove-888.mypinata.cloud/ipfs/QmSz8cySmzuCc57j6LZRR3bVGGfiXaQY9XFnxKTkP2x981/FutureGarden_1.jpg"

print(base_url_json)

# Diccionario para almacenar los datos
datos_dict = {}

# Iterar sobre los nombres de archivos JSON y obtener los datos de Piñata
for i in range(1, total_archivos + 1):
    # Componer el nombre de archivo JSON
    nombre_json = f"json{i}"

    json_cid = "QmbFMke1KXqnYyBBWxB74N4c5SBnJMVAiMNRcGu6x1AwQH"  # Reemplaza "tu_cid_aqui" con tu CID real
    json_url = f"https://black-ashamed-dove-888.mypinata.cloud/{json_cid}"

    # Realizar una solicitud GET a la URL del JSON
    response_json = requests.get(json_url)

    # Verificar si la solicitud del JSON fue exitosa
    if response_json.status_code == 200:
        # Parsear el contenido JSON del JSON
        data_json = json.loads(response_json.text)

        # Componer la URL de la imagen basada en la estructura de nombres
        nombre_imagen = f"FutureGarden_{i}"
        imagen_url = base_url_imagen + nombre_imagen

        print("Datos IPFS:", nombre_imagen, imagen_url)

    else:
        print(f"Error al obtener datos desde {json_url}")

# Ahora, datos_dict contiene los datos de todos los archivos JSON y las URL de las imágenes

base_url = "https://black-ashamed-dove-888.mypinata.cloud/ipfs/QmSz8cySmzuCc57j6LZRR3bVGGfiXaQY9XFnxKTkP2x981/FutureGarden_"

"""for i in range(1, 13):
    url = f"{base_url}{i}.jpg"
    print(url)"""


