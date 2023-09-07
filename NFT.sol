// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.19;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol";

contract NFT is ERC721 {
    //constante que guarda el precio del NFT
    uint256 PRICE = 0.1 ether;
    //variable que gurda la cantidad de token que van saliendo
    uint256 totalSupply = 0;

    //las variables struct tipo DatosNFT guardan las caracteristicas de nuestro NFT
    struct DatosNFT {
        string nombre;
        string descripcion;
    }
   