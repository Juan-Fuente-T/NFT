// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.19;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol";
//import "../../Codigos_ejemplo/ERC20-ERC721/ERC721.sol"
contract NFT is ERC721 {
    //constante que guarda el precio del NFT
    uint256 PRICE = 0.1 ether;
    //variable que guarda la cantidad de token que van saliendo
    uint256 totalSupply = 0;

    //las variables struct tipo DatosNFT guardan las caracteristicas de nuestro NFT
    struct DatosNFT {
        string nombre;
        string descripcion;
    }
    //hacemos un mapping para guardar los datos del nft en variables tipo datos
    mapping(uint256 => DatosNFT) datos;
    //el contructor del ERC721 necesita name y symbol
    constructor() ERC721("Beholder_IronMan", "BIM") {

    }
    //funcion para mintear los nft, evalua que el valor que envia msg.sender sea mayor que el precio del nft
    function mint() public payable {
        require(msg.value >= PRICE, "No has pagado el NFT");
        //funcion que emite los tokens, toma por parametro a quien los envia y el numero id del token
        _mint(msg.sender, totalSupply);
        //se actualiza el numero de tokens minteados 
        totalSupply++;
    }
    //funcion que pasa los metadatos al token y devuelve un string con los datos)sobreescribe la funcion del ERC721
    function tokenURI(uint256 tokenId) public override view returns (string memory) {
        /* Estructura estandar URI
        {
            "name": "PAISAJE",
            "description": "Un paisaje bonito",
            "image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8fA%3D%3D&w=1000&q=80"
        }
        */
        //devuelve todos los metadatos empaquetados y codificados
        return string(
            abi.encodePacked(
                '{',
                    '"name": "Beholder",',
                    '"description": "Una imagen sugerida de Ironman en la sombra",',
                    '"image": "https://www.pxfuel.com/en/desktop-wallpaper-pizjc",',
                '}'
            )
        );
    }

}