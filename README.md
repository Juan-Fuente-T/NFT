# Solidity NFT Contract

This contract represents a simple ERC721-based NFT (Non-Fungible Token) that allows users to mint NFTs by paying a specific price. Each minted NFT has associated metadata, including a name, description, and image URL.

## Features

- Mint NFTs by sending the required payment.
- Automatically generate metadata for each minted NFT.
- View NFT metadata using the tokenURI function.

## Getting Started

To interact with this contract, you can follow these steps:

1. Deploy the contract to a supported blockchain network.

2. Mint NFTs by sending the required payment to the contract.

3. Use the `tokenURI` function to retrieve the metadata for a specific NFT.

## Contract Details

- Contract Name: Beholder_IronMan (BIM)
- Token Symbol: BIM

## Minting NFTs

To mint an NFT, use the `mint` function by sending the required payment in Ether. The price per NFT is 0.1 Ether.

Example of minting an NFT:

`
function mint() public payable {
    require(msg.value >= 0.1 ether, "Payment insufficient to mint NFT");
    _mint(msg.sender, totalSupply);
    totalSupply++;
} '


## Viewing NFT Metadata

You can retrieve the metadata for a specific NFT by using the `tokenURI` function, which overrides the ERC721 standard function. The metadata includes the name, description, and an image URL.

Example of retrieving NFT metadata:

`solidity
function tokenURI(uint256 tokenId) public override view returns (string memory) {
    return string(
        abi.encodePacked(
            '{',
                '"name": "Beholder",',
                '"description": "A suggested image of Ironman in the shadow",',
                '"image": "https://www.pxfuel.com/en/desktop-wallpaper-pizjc",',
            '}'
        )
    );
} 
`






