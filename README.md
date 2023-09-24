# Solidity NFT Contract and Python Script for Minting NFTs Automatically
This project combines a Solidity smart contract that enables the creation of NFTs (Non-Fungible Tokens) based on the ERC721 standard with a Python script that automates the NFT minting process and manages associated metadata.

It has been used to mint a small collection of 12 NFTs based on some of my personally crafted photographs, artistically treated and hosted on Pinata IPFS. 
The collection is titled "Future Garden."

## Solidity NFT Contract
The Solidity NFT contract is a simple yet powerful implementation of ERC721 that offers the following features:

### Contract Features
- NFT Minting: A series of NFTs has been minted automatically and restricted only to the contract owner. Each minted NFT receives a unique identifier and associated metadata.

- Automated Metadata: The contract automatically generates metadata for each minted NFT, including a name, description, and image URL.

- Metadata Query: Users can access the metadata of a specific NFT using the tokenURI function.

- Getting Started with the Contract
To interact with the Solidity NFT contract, follow these steps:

### Deploy the Contract: Deploy the contract on a compatible blockchain network. Tools like Truffle or Remix can be used for this step.

- NFT Minting: Users cannot mint NFTs as it is restricted only to the contract owner. Each generated NFT receives a name, description, and unique associated image.

- Metadata Query: Use the tokenURI function to retrieve the metadata of a specific NFT, including its name, description, and image.

- Contract Details
Contract Name: NFTFactory
Token Symbol: NFC

## Python Script for Automated NFT Minting
The Python script automates the NFT minting process and manages associated metadata. This script works in conjunction with the Solidity NFT contract and offers the following functionalities:

### Script Features
- Automated Minting: The script interacts with the Solidity NFT contract to automatically mint NFTs. The name, description, and image URL for each NFT are defined.

- Automated Gas Calculation: The script estimates the amount of gas required to mint each NFT, ensuring efficient execution.

- Transaction Tracking: The script tracks transactions, waits for confirmations, and provides detailed information about the minting process, avoiding congestion.

- Error Handling: The script handles errors appropriately, ensuring that any issues during minting are logged for review.

### Using the Python Script
To use the Python script and automate the NFT minting process, the following steps were followed:

- Parameter Configuration: The necessary parameters in the script, such as API keys and contract addresses, were correctly configured.

- Script Execution: The Python script was executed, automating the minting of NFTs according to the provided parameters.

- Tracking and Confirmation: The script tracks transactions and waits for confirmations. It provides detailed information about the status of each minted NFT.

## Contribution and Support
This project is open-source, so you can contribute, make improvements, and customize it according to your needs. If you have questions or need assistance, feel free to create an issue or request support in the repository's issues section.

#### We hope this project proves to be interesting, representing a step into the world of NFTs and process automation on the blockchain!
## License
This project is distributed under the INSERT_APPROPRIATE_LICENSE. Refer to the LICENSE file for more details on the terms of use.











