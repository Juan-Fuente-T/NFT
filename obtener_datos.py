import os
import json
import requests
from web3 import Web3
from dotenv import load_dotenv

# Carga las variables desde el archivo .env
load_dotenv()

# Obtiene las variables desde el archivo .env
web3_provider_url = os.getenv("WEB3_PROVIDER_URL")
contract_address = os.getenv("CONTRACT_ADDRESS")
contract_abi = json.loads(os.getenv("CONTRACT_ABI"))
ipfs_url = os.getenv("IPFS_URL")
your_address = os.getenv("YOUR_ADDRESS")
private_key = os.getenv("PRIVATE_KEY")

# Conecta a un nodo Ethereum
w3 = Web3(Web3.HTTPProvider(web3_provider_url))

# Crea una instancia del contrato
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Función para obtener los datos desde IPFS
def obtener_datos_desde_ipfs(url):
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        raise Exception("Error al obtener datos desde IPFS")

# Obtén los datos desde IPFS
datos_ipfs = obtener_datos_desde_ipfs(ipfs_url)

# Parámetros del NFT
nombre = datos_ipfs["name"]
descripcion = datos_ipfs["description"]
imagen = datos_ipfs["image"]

# Transacción para mintear un NFT con los datos
transaction = contract.functions.mintNFT(nombre, descripcion, imagen).buildTransaction({
    'chainId': 11155111,
    'gas': 2000000,
    'gasPrice': w3.toWei('5', 'gwei'),
    'nonce': w3.eth.getTransactionCount(your_address),
})

# Firma y envía la transacción
signed_transaction = w3.eth.account.signTransaction(transaction, private_key)
tx_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)

print(f"Transacción enviada. Hash de transacción: {tx_hash.hex()}")

print("datos IPFS", nombre, descripcion, imagen)