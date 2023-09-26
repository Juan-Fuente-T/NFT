import os
import json
import requests
from dotenv import load_dotenv
from web3 import Web3
import time
from web3.middleware import geth_poa_middleware

# Se cargan las variables de entorno desde el archivo .env
load_dotenv()

# SE recuperan las credenciales desde las variables de entorno
pinata_api_key = os.getenv("API_KEY") #api kei IPFS Pinata
pinata_secret_api_key = os.getenv("API_SECRET") # api secret IPFS Pinata
json_cid = os.getenv("CID_DEL_JSON") #metadatos subidos a IPFS Pinata
folder_cid =os.getenv("CID_DE_IMAGENES") # imagenes subidas IPFS Pinata
wallet_private_key = os.getenv("WALLET_PRIVATE_KEY")  # clave privada wallet
eth_rpc_url = os.getenv("WEB3_PROVIDER_URL")  # URL del nodo sepolia
my_contract_address = os.getenv("CONTRACT_ADDRESS") # direccion del contrato deployado en sepolia


# Se construye la URL completa para obtener cada url dinamicamente
json_url = f"https://black-ashamed-dove-888.mypinata.cloud/ipfs/{json_cid}"

# Encabezados para la autenticación
headers = {
    "pinata_api_key": pinata_api_key,
    "pinata_secret_api_key": pinata_secret_api_key,
}

# Se realiza la solicitud GET para obtener el JSON con los matadatos
response = requests.get(json_url, headers=headers)

# Se verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Se verifica si la respuesta contiene datos antes de intentar analizarla como JSON
    if response.text:
        json_data = response.json()
        print("JSON descargado exitosamente.") #print de control para depuracion
        
        # Se leen el archivo ABI del contrato
        with open("ContractABI.json", "r") as abi_file:
            myContractABI = json.load(abi_file)
        
        # Se conecta con el nodo Sepolia. Crea una instancia de Web3
        w3 = Web3(Web3.HTTPProvider(eth_rpc_url))
    
        # Se agrega el middleware de PoA
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)

        # Se asegura que la dirección sea correcta
        contract_address = w3.to_checksum_address(my_contract_address)

        # Se despliega el contrato NFTs
        nfts_contract = w3.eth.contract(
            address= contract_address, abi= myContractABI
        )  
        # Se importa la billetera utilizando la clave privada
        wallet = w3.eth.account.from_key(wallet_private_key)

        #funcion que devuelve el total de tokens minteados
        total_supply = nfts_contract.functions.totalSupply().call()
        print(f"Total de tokens NFT minteados: {total_supply}")
        
        #se aumenta el numero de id para evitar repeticiones
        current_token_id = total_supply + 1
        # Se itera a través de los elementos en el JSON, comenzando desde el segundo elemento (índice 1)
        for i, item in enumerate(json_data):  # Empezamos desde el segundo elemento y asignamos nombres únicos
            image_url = f"https://black-ashamed-dove-888.mypinata.cloud/ipfs/{folder_cid}/{item['image']}"
            name = item.get("name", f"Nombre predeterminado {i}")  # Usamos un nombre único basado en el índice
            description = item.get("description", "Descripción predeterminada")
            #print(f"URL de la imagen: {image_url}") #print de control para depuracion
            #print("DATOS MINT:", name, description, image_url) #print de control para depuracion
            
            # Se hace una llamada para estimar la cantidad de gas necesaria para el minteo
            gas_estimate = nfts_contract.functions.mintNFT(name, description, image_url).estimate_gas(
                {"from": wallet.address}
            )
            print(f"Estimación de gas: {gas_estimate}") #impresion de control
            #se hace una llamada para estimar el precio del gas
            gas_price = w3.eth.gas_price
            
            try:
                # Se procede a llamar a la función mintNFT del contrato NFTs

                # Se obtiene el ultimo nonce para asegurarse de que no se repita
                nonce = w3.eth.get_transaction_count(wallet.address, 'latest')  # Obtiene el nonce actual
                # Se crea una transacción que llama al método mintNFT del contrato.
                transaction = nfts_contract.functions.mintNFT(name, description, image_url).build_transaction({
                    'from': wallet.address,
                    'gas': gas_estimate,
                    #'gasPrice': w3.to_wei('59', 'gwei'),#pruebas con precio de gas fijo
                    'gasPrice':gas_price,
                    'nonce': nonce,
                })
                                
                # Se firma la transacción con la clave privada.
                signed_txn = w3.eth.account.sign_transaction(transaction, wallet_private_key)

                # Se envia la transacción firmada.
                tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
                
                #se espera a que se termine la transaccion y se obtengan los datos
                tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
                print(f"NFT minteado: {name}, Tx Hash: {tx_hash.hex()}")#impresion de control
                
                while tx_receipt is None: #si aun no se ha confirmadpo la trasaccion
                    time.sleep(10)  # se esperan 10 segundos antes de hacer la siguiente cpomprobacion
                    #se obtiene un recibo con datos d ela transaccon
                    tx_receipt = w3.eth.get_transaction_receipt(tx_hash)
                #impresiones de control e informativas    
                print(f"Block Number: {tx_receipt['blockNumber']}")
                print(f"Gas Used: {tx_receipt['gasUsed']}")
                #se llama al total de ntf minteados y se imprime a modo informativo
                total_supply = nfts_contract.functions.totalSupply().call()
                print(f"Total de tokens NFT minteados: {total_supply}")
                
                current_token_id += 1 #se aumenta el nuimero de Id
            except Exception as e:
                print(f"Error al mintear el NFT: {str(e)}")  #print de control por si falla el minteo
            
        else: #prints de control para depuracion de errores en la obtencion de datos
            print("La respuesta está vacía, no se pudo analizar como JSON.")

else:
    print(f"No se pudo descargar el JSON. Código de estado: {response.status_code}")
    

    #Este script descarga las imagenes a local
"""
    # Descarga la imagen y la guarda localmente
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                with open(image_filename, 'wb') as image_file:
                    image_file.write(image_response.content)
                print(f"Imagen descargada: {image_filename}")
            else:
                print(f"No se pudo descargar la imagen. Código de estado: {image_response.status_code}")

    """