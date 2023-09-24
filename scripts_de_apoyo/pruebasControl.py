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
my_contract_address = os.getenv("CONTRACT_ADDRESS") # direccion del contrato deployado en sepolia

#CAMBIAR CONTRACT ADDRESS  EN .ENV SI SE QUIERE OBTENER URI O SUPPLY DE OTRO CONTRATO(+ABI)

# Se construye la URL completa para obtener cada una dinamicamente
json_url = f"https://black-ashamed-dove-888.mypinata.cloud/ipfs/{json_cid}"

# Encabezados para la autenticación
headers = {
    "pinata_api_key": pinata_api_key,
    "pinata_secret_api_key": pinata_secret_api_key,
}

# Se realiza la solicitud GET para obtener el JSON con los metadatos
response = requests.get(json_url, headers=headers)

        
# Se verifica si la solicitud fue exitosa
current_token_id = 1
if response.status_code == 200:
    # Se verifica si la respuesta contiene datos antes de intentar analizarla como JSON
    if response.text:
        json_data = response.json()
        print("JSON descargado exitosamente.") #print de control para depuracion
        
        #Cambiar ABI si cambia la address contract        
        with open("ContractABI.json", "r") as abi_file:
            myContractABI = json.load(abi_file)
            

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
            
        name = "NFT_Tejeluz_6"    
        description = "NFT de las piezas de joyería de vidrio Tejeluz"
        image_url = "https://tejeluz.com/wp-content/uploads/Colgante-de-vidrio-reciclado-y-acero-hipoalergenico-Flor-de-Luna-Joyeria-sostenible-Tejeluz-600x600.jpg"
        Supply = get_total_supply()
        print("Supply:", Supply)
        
        #Zona de minteo de pruebas
        """for i, item in enumerate(json_data[1:], start=2):  # Empezamos desde el segundo elemento y asignamos nombres únicos
            image_url = f"https://black-ashamed-dove-888.mypinata.cloud/ipfs/{folder_cid}/{item['image']}"
            name = item.get("name", f"Nombre predeterminado {i}")  # Usamos un nombre único basado en el índice
            description = item.get("description", "Descripción predeterminada")
            #print(f"URL de la imagen: {image_url}") #print de control para depuracion
            #print("DATOS MINT:", name, description, image_url) #print de control para depuracion
            
            # Se procede a llamar a la función mintNFT del contrato NFTs
            
            gas_estimate = contract.functions.mintNFT(name, description, image_url).estimate_gas(
                {"from": wallet.address}
            )
    
            #tokenId = 2
            # Se procede a llamar a la función mintNFT del contrato NFTs
            
            nonce = w3.eth.get_transaction_count(wallet.address)    
            # Crea una transacción que llama al método mintNFT de tu contrato.
            transaction = contract.functions.mintNFT(name, description, image_url).build_transaction({
                'from': wallet.address,
                'gas': 45800,
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

            current_token_id += 1"""

        # Ejemplo de uso
        if __name__ == "__main__":
            #Comprobamos URIs o totalSupply si es necesario
            token_id_to_query = 3 # Se reemplaza con el ID del token que deseas consultar
            uri = get_token_uri(token_id_to_query)
            print(f"Token ID {token_id_to_query} URI: {uri}")
            
            total_supply = get_total_supply()
            print(f"Total de suministro de tokens: {total_supply}")
            
            