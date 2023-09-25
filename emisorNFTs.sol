// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.21;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol"; // Se importa el contrato ERC721
import "@openzeppelin/contracts/utils/Counters.sol"; // Se importa la biblioteca Counters

contract NFTs is ERC721 {
    using Counters for Counters.Counter; // Se utiliza la biblioteca Counters
    Counters.Counter private tokenIds; // Contador privado para generar identificadores únicos de tokens

    address public owner = 0xe67F18c5064f12470Efc943798236edF45CF3Afb; // Dirección del owner
    //Se utiliza un custom error para evitar usar require y ahorrar gas
    error NotOwner();
    //Se guardan los datos agrupados para cada NFT
    struct DatosNFTs {
        string nombre;
        string descripcion;
        string imagen;
    }

    mapping(uint256 => DatosNFTs) private datos; // Mapeo de identificadores de tokens a datos personalizados

    // Evento que se emite al crear un nuevo token NFT
    event NFTMinted(address indexed creator, uint256 indexed tokenId, string nombre, string descripcion, string imagen); 

    modifier onlyOwner() {
        //require(msg.sender == owner, "No eres el owner"); // Modificador que restringe ciertas funciones solo al owner
        if (msg.sender != owner) //el custom error ahorra gas con respeto al require
        revert NotOwner();
        _;
    }

    constructor() ERC721("NFTFactory", "NFC") {} // Constructor del contrato, establece el nombre y símbolo del contrato ERC721

    //Funcion para emitir los NFT, recibe por parametro los datos necesarios
    function mintNFT(string memory nombre, string memory descripcion, string memory imagen) public onlyOwner {
        tokenIds.increment(); // Incrementa el contador de tokens
        uint256 newTokenId = tokenIds.current(); // Obtiene el nuevo identificador de token

        datos[newTokenId] = DatosNFTs(nombre, descripcion, imagen); // Guarda los datos personalizados del nuevo token
        _safeMint(msg.sender, newTokenId); // Crea el nuevo token NFT y lo asigna al creador

        emit NFTMinted(msg.sender, newTokenId, nombre, descripcion, imagen); // Emite el evento de creación de NFT
    }

    //Funcion para entregar la URI con lo metadatpos del NFT
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "El token no existe"); // Verifica que el token exista

        // Obtiene los datos para construir la URI del token
        string memory name = datos[tokenId].nombre;
        string memory description = datos[tokenId].descripcion;
        string memory imageUrl = datos[tokenId].imagen;

        // Construye la URI del token en formato JSON
        string memory uri = string(
            abi.encodePacked(
                '{"name": "', name, '",',
                '"description": "', description, '",',
                '"image": "', imageUrl, '"',
                '}'
            )
        );

        return uri; // Retorna la URI del token
    }

    //Funcion para entregar la cantidad de tokens emitidos
    function totalSupply() public view returns (uint256) {
        return tokenIds.current(); // Retorna la cantidad total de tokens creados hasta el momento
    }
}   
    //variante para la funcion de entrega de URI
    /*
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "El token no existe");

        DatosNFTs memory data = datos[tokenId];

        string memory baseURI = _baseURI();
        return bytes(baseURI).length > 0 ? string(abi.encodePacked(baseURI, tokenId.toString())) : "";
    }*/