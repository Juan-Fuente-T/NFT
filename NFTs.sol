// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.19;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol";
//import "../../Codigos_ejemplo/ERC20-ERC721/ERC721.sol"
contract NFTs is ERC721 {
    address owner = 0xAa147de37b4a356807812BDB0De01e7284E7694b; //MI direccion
    //constante que guarda el precio del NFT
    uint256 PRICE = 0.1 ether;
    //variable que guarda la cantidad de token que van saliendo
    uint256 totalSupply;
    string memory baseIPFS = "https://carpetaipfsJuan/json";
    
    //las variables struct tipo DatosNFT guardan las caracteristicas de nuestro NFT
    struct DatosNFTs {
        string nombre;
        string descripcion;
        string imagen;
        
    }
{
    "name": "FutureGarden. NFT8",
    "description": "La naturaleza se transforma y muta bajo la influencia de la Web 3.0. El futuro surge desde el centro de la tierra. FutureGarden es una Serie Limitada de 12 fotografías de Juan Fuente tratadas artísticamente",
    "image": "/FutureGarden_8.jpg"
    }
    

    //hacemos un mapping para guardar los datos del nft en variables tipo datos
    mapping(uint256 => DatosNFTs) datos;


    //el contructor del ERC721 necesita name y symbol
    constructor() ERC721("NFTFactory", "NFC") {
        //creator = owner;
    }

    // Aquí debes implementar la lógica para obtener y parsear el contenido JSON desde IPFS
        // y extraer el nombre y la descripción para el NFT
        // ...

    function mintNFTFromIPFS(
    string[] memory name,
    string[] memory description,
    uint256 tokenNumber
) public {
    require (msg.sender == owner, "No eres el owner");
        uint256 tokenId = totalSupply() + 1;
    
        _mint(owner, tokenId);
    }
    string memory imageUrl = string(abi.encodePacked(baseIPFS, uint2str(tokenNumber), ".json"));

    //string memory baseIPFS = "https://carpetaipfsJuan/json";
    //string memory imageIPFS = string(abi.encodePacked(baseIPFS, uint2str(tokenNumber), ".json"));
    datos[tokenId] = DatosNFTs({
        nombre: name,
        descripcion: description,
        imagen: imageUrl
    });


     // Función para obtener la URI de un token
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(tokenId > 0, "El token no existe");
        
        string memory name = datos[tokenId].nombre;
        string memory description = datos[tokenId].descripcion;
        string memory imageUrl = datos(tokenId).imagen; // Convierte el tokenId en cadena
        
        string memory uri = string(
            abi.encodePacked(
                '{',
                '"name": "', name, '",',
                '"description": "', description, '",',
                '"image": " ', imageUrl'"',
                '}'
        )
    );

    return uri;
}
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