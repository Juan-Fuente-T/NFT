from web3 import Web3

alchemy_url = "https://polygon-mumbai.g.alchemy.com/v2/v2kQ9jNXew4AilZT7fHDS0ijN1nM5tLN"  # Reemplaza con la URL de tu nodo Alchemy
w3 = Web3(Web3.HTTPProvider(alchemy_url))

if w3.is_connected():
    print("Conexión exitosa a Alchemy")
else:
    print("No se pudo conectar a Alchemy")
    
"""
#Este escrpt permite conectarse a una direccion y llamar al balance

from web3 import Web3

alchemy_url = ""  # Reemplaza con la URL de tu nodo Alchemy
w3 = Web3(Web3.HTTPProvider("https://eth-sepolia.g.alchemy.com/v2/QF_rlvr4V0ZORimK7ysBA4mJvl0Bk47c"))

address = "0xe67F18c5064f12470Efc943798236edF45CF3Afb"  # Reemplaza con la dirección que deseas consultar

balance_wei = w3.eth.get_balance(address)
balance_eth = w3.from_wei(balance_wei, "ether")

print(f"Saldo de {address}: {balance_eth} ETH")"""

