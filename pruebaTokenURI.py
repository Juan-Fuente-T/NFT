import os
import json
import requests
from dotenv import load_dotenv
from web3 import Web3
from web3.middleware import geth_poa_middleware

load_dotenv()

pinata_api_key = os.getenv("API_KEY") #api kei IPFS Pinata
pinata_secret_api_key = os.getenv("API_SECRET") # api secret IPFS Pinata
json_cid = os.getenv("CID_DEL_JSON") #metadatos subidos a IPFS Pinata
folder_cid =os.getenv("CID_DE_IMAGENES") # imagenes subidas IPFS Pinata
wallet_private_key = os.getenv("WALLET_PRIVATE_KEY")  # clave privada wallet



eth_rpc_url = os.getenv("WEB3_PROVIDER_URL")  # URL del nodo sepolia
# Establece la URL del proveedor de Web3 (puede ser un nodo Ethereum o una red de prueba)


# Dirección del contrato ERC721 que deseas interactuar
my_contract_address = "0xa698FDD162Fe08925391B844780d48DcB0ed48C0"  # Dirección del contrato ERC721
#contract_address = "0x91112e722878AF0e48bF8Ea66994F15c4d5347C6"  # Reemplaza con la dirección de tu contrato ERC721
with open("myContractABI.json", "r") as abi_file:
    myContractABI = json.load(abi_file)
    
#print("myContractABI", myContractABI)

# Crea una instancia de Web3 y agrega el middleware PoA (si es necesario)
w3 = Web3(Web3.HTTPProvider(eth_rpc_url))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)


contract_address = w3.to_checksum_address(my_contract_address)
# Crea una instancia del contrato ERC721
contract = w3.eth.contract(address=contract_address, abi=myContractABI)

wallet = w3.eth.account.from_key(wallet_private_key)

# Función para obtener el URI del token por su ID
def get_token_uri(token_id):
    try:
        token_uri = contract.functions.tokenURI(token_id).call()
        return token_uri
    except Exception as e:
        return str(e)

# Función para obtener el total de suministro de tokens
def get_total_supply():
    try:
        total_supply = contract.functions.totalSupply().call()
        return total_supply
    except Exception as e:
        return str(e)
    
name = "NFT_Tejeluz_5"    
description = "NFT de las piezas de joyería de vidrio Tejeluz"
image_url = "https://tejeluz.com/wp-content/uploads/Colgante-de-vidrio-reciclado-y-acero-hipoalergenico-Flor-de-Luna-Joyeria-sostenible-Tejeluz-600x600.jpg"
#tokenId = 2
# Se procede a llamar a la función mintNFT del contrato NFTs
    
nonce = w3.eth.get_transaction_count(wallet.address)    
# Crea una transacción que llama al método mintNFT de tu contrato.
transaction = contract.functions.mintNFT(name, description, image_url).build_transaction({
    'from': wallet.address,
    'gas': 77000,
    'gasPrice': w3.to_wei('1.2', 'gwei'),
    'nonce': nonce,
})

# Firmar la transacción con tu clave privada.
signed_txn = w3.eth.account.sign_transaction(transaction, wallet_private_key)

# Enviar la transacción firmada.
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

# Esperar a que la transacción esté minada para obtener el recibo de la transacción.
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

hash_hex = tx_hash.hex()
print(f"NFT minteado: {name}, Tx Hash: {hash_hex}")


#hash_bytes = b'\x1e\'~\x9f9\x9a\xf5"\x1a\x17(Q\xae\xdc\xb7V\xbez=i\xdf"\x051.\x06\xc5\x8b\xb2\xec\x07\xbc'
#hash_bytes = b'h(d\xd2Ol\x16J\xbe\xadSM\xad\'-|"\xc8\x1e\x95\xe0\xc2\x02\xe2\xe9\xc9\xaa\xc6\x8c<U\x1b'

   
# Ejemplo de uso
if __name__ == "__main__":
    token_id_to_query = 4  # Reemplaza con el ID del token que deseas consultar
    uri = get_token_uri(token_id_to_query)
    print(f"Token ID {token_id_to_query} URI: {uri}")
    
    total_supply = get_total_supply()
    print(f"Total de suministro de tokens: {total_supply}")
    