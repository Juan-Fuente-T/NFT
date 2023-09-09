// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.19;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol";
//import "../../Codigos_ejemplo/ERC20-ERC721/ERC721.sol"
contract NFTs is ERC721 {
    address owner = 0xchachacha; //MI direccion
    //constante que guarda el precio del NFT
    uint256 PRICE = 0.1 ether;
    //variable que guarda la cantidad de token que van saliendo
    uint256 totalSupply = 0;

    //las variables struct tipo DatosNFT guardan las caracteristicas de nuestro NFT
    struct DatosNFTs {
        string nombre;
        string descripcion;
        string imageURL;
        
    }
    //hacemos un mapping para guardar los datos del nft en variables tipo datos
    mapping(uint256 => DatosNFT) datos;

    //mapping(uint256 => string) private _tokenURIs;

    //el contructor del ERC721 necesita name y symbol
    constructor() ERC721("NFTFactory", "NFC") {
        creator = owner;
    }

    function batchMintNFTs(
    string[] memory names,
    string[] memory descriptions,
    string[] memory imageUrls
) public {
    require (msg.sender == owner, "No eres el owner")
    require(names.length == descriptions.length && descriptions.length == imageUrls.length, "Los arrays de entrada deben ser de la misma longitud");
    
    for (uint256 i = 0; i < names.length; i++) {
        uint256 tokenId = totalSupply() + 1;
        _mint(msg.sender, tokenId);
        datos[tokenId] = Datos(names[i], descriptions[i]);
    }
}


    //funcion para mintear los nft, evalua que el valor que envia msg.sender sea mayor que el precio del nft
    /*function mint() public payable {
        require(msg.value >= PRICE, "No has pagado el NFT");
        //se actualiza el numero de tokens minteados 
        totalSupply++;
        //funcion que emite los tokens, toma por parametro a quien los envia y el numero id del token
        _mint(msg.sender, tokenId);
    }*/
     // Función para obtener la URI de un token
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "El token no existe");
        
        string memory name = datos[tokenId].nombre;
        string memory description = datos[tokenId].descripcion;
        string memory imageNumber = uint2str(tokenId); // Convierte el tokenId en cadena
        
        string memory uri = string(
            abi.encodePacked(
                '{',
                '"name": "', name, '",',
                '"description": "', description, '",',
                '"image": "https://www.pxfuel.com/en/desktop-wallpaper/', imageNumber, '"',
                '}'
        )
    );

    return uri;
}



    //funcion que pasa los metadatos al token y devuelve un string con los datos)sobreescribe la funcion del ERC721
   /* function tokenURI(uint256 tokenId) public override view returns (string memory) {
        /* Estructura estandar URI
        {
            "name": "PAISAJE",
            "description": "Un paisaje bonito",
            "image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8fA%3D%3D&w=1000&q=80"
        }
        */
        //devuelve todos los metadatos empaquetados y codificados
        /*return string(
            abi.encodePacked(
                '{',
                    '"name": "Beholder",',
                    '"description": "Una imagen sugerida de Ironman en la sombra",',
                    '"image": "https://www.pxfuel.com/en/desktop-wallpaper-pizjc",',
                '}'
            )
        );
    }*/

}