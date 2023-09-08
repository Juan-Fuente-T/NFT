# Contrato NFT Solidity

Este contrato representa un NFT (Token No Fungible) sencillo basado en ERC721 que permite a los usuarios acuñar NFTs pagando un precio específico. Cada NFT acuñado tiene metadatos asociados, incluyendo un nombre, descripción y URL de la imagen.

## Características
- Acuña NFTs enviando el pago requerido.
- Genera automáticamente metadatos para cada NFT acuñado.
- Visualiza los metadatos de los NFTs usando la función tokenURI.

## Empezando
Para interactuar con este contrato, puedes seguir estos pasos:

1. Despliega el contrato en una red blockchain compatible.
2. Acuña NFTs enviando el pago requerido al contrato.
3. Usa la función tokenURI para recuperar los metadatos para un NFT específico.

## Detalles del Contrato
- Nombre del Contrato: Beholder_IronMan (BIM)
- Símbolo del Token: BIM

### Acuñando NFTs
Para acuñar un NFT, usa la función mint enviando el pago requerido en Ether. El precio por NFT es 0.1 Ether.

Ejemplo de cómo acuñar un NFT:

``` javascript
function mint() public payable {
    require(msg.value >= 0.1 ether, "Payment insufficient to mint NFT");
    _mint(msg.sender, totalSupply);
    totalSupply++;
}
```
## Visualizando Metadatos de NFTs
Puedes recuperar los metadatos para un NFT específico usando la función tokenURI, que sobrescribe la función estándar de ERC721. Los metadatos incluyen el nombre, descripción, y una URL de la imagen.

Ejemplo de cómo recuperar metadatos de NFTs:

``` javascript
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
```



