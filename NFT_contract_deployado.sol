// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract NFTs is ERC721 {
    address public owner = 0xe67F18c5064f12470Efc943798236edF45CF3Afb; //direccion del owner
    
    event NFTMinted(address indexed creator, uint256 tokenId); //evento que se emite al ser minteado un nft

    constructor() ERC721("NFTFactory", "NFC") { //el contrctor da nombre y simbolo al nft
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "No eres el owner"); //el modifier olo permite al owner mintear
        _;
    }

//en el estruct se guardan los datos de nft
    struct DatosNFTs {
        string nombre;
        string descripcion;
        string imagen;
    }
//el mapping va creando structs y dandoles un numero
    mapping(uint256 => DatosNFTs) datos;

//Funcion que emite nft
    function mintNFT( //toma por parametro estos tres valores
        string memory name,
        string memory description,
        string memory imageUrl
    ) public onlyOwner { //solo puede ejecutarla el owner
        uint256 tokenId = totalSupply ++; //aumenta el numero de tokens emitidos

        _mint(msg.sender, tokenId); //se envie el nft al que lo ha emitido, que en este caso es el dueño

        datos[tokenId] = DatosNFTs({
            nombre: name,
            descripcion: description,
            imagen: imageUrl
        });

        emit NFTMinted(msg.sender, tokenId); //se emite evento d etoken emitido
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(tokenId > 0, "El token no existe"); //da error en caso de no haya token emitidos

        //estos son los valores que devuelve la URI
        string memory name = datos[tokenId].nombre;
        string memory description = datos[tokenId].descripcion;
        string memory imageUrl = datos[tokenId].imagen;

        string memory uri = string(
            abi.encodePacked(
                '{"name": "', name, '",',
                '"description": "', description, '",',
                '"image": "', imageUrl, '"',
                '}'
            )
        );

        return uri;
    }
}