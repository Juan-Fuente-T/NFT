# Contrato NFT Solidity y Script Python para Mintear NFTs Automáticamente

Este proyecto combina un contrato inteligente en Solidity que permite la creación de NFTs (Tokens No Fungibles) basados en el estándar ERC721 con un script Python que automatiza el proceso de acuñación de NFTs y la gestión de metadatos asociados a cada uno.

Se ha utilizado para la emisión de una pequeña colección de 12 NFT de elaboración propia basados en algunas de mis fotografías, tratadas artísticamente y alojadas en Pinata IPFS.

El título de la colección es Future Garden.

## Contrato NFT en Solidity

El contrato NFT en Solidity es una implementación simple pero poderosa de ERC721 que ofrece las siguientes características:

### Características del Contrato
- Acuñación de NFTs: Se han acuñado una serie propia de NFTs de modo automático y restringuido solo al owner. Cada NFT acuñado obtiene un identificador único y metadatos asociados.

- Metadatos Automatizados: El contrato genera automáticamente metadatos para cada NFT acuñado. Estos metadatos incluyen un nombre, una descripción y una URL de imagen.

- Consulta de Metadatos: Los usuarios pueden acceder a los metadatos de un NFT específico utilizando la función tokenURI.

### Empezando con el Contrato
Para interactuar con el contrato NFT en Solidity, sigue estos pasos:

- Despliegue del Contrato: Despliega el contrato en una red blockchain compatible. Puedes utilizar herramientas como Truffle o Remix para realizar este paso.

- Acuñación de NFTs: Los usuarios no podrán acuñar NFTs ya que está limitado solo al duelo del contrato. Cada NFT generado obtiene un nombre, una descripción y una imagen única asociada.

- Consulta de Metadatos: Utiliza la función tokenURI para recuperar los metadatos de un NFT específico, incluyendo su nombre, descripción e imagen.

### Detalles del Contrato
- Nombre del Contrato: NFTFactory
- Símbolo del Token: NFC

## Script Python para Mintear NFTs Automáticamente
El script Python se encarga de automatizar el proceso de acuñación de NFTs y la gestión de los metadatos asociados a cada uno. Este script trabaja en conjunto con el contrato NFT en Solidity y ofrece las siguientes funcionalidades:

### Características del Script Python
- Acuñación Automatizada: El script interactúa con el contrato NFT en Solidity para acuñar NFTs automáticamente. Se define el nombre, la descripción y la URL de la imagen para cada NFT.

- Cálculo de Gas Automatizado: El script estima la cantidad de gas necesaria para realizar la acuñación de cada NFT, asegurando una ejecución eficiente.

- Seguimiento de Transacciones: El script realiza un seguimiento de las transacciones, espera a que se confirmen y proporciona información detallada sobre el proceso de acuñación, evitando además el agolpamiento.

- Control de Errores: El script maneja errores de manera adecuada, lo que garantiza que cualquier problema durante la acuñación se registre para su revisión.

### Uso del Script Python
Para utilizar el script Python y automatizar la acuñación de NFTs, se han seguido estos pasos:

- Configuración de Parámetros: Se han configurado correctamente los parámetros necesarios en el script, como las claves de API y las direcciones de contrato.

- Ejecución del Script: Se ha ejecutado el script Python, que se encargade acuñar NFTs automáticamente según los parámetros proporcionados.

- Seguimiento y Confirmación: El script rastra las transacciones y espera a que se confirmen. Proporciona información detallada sobre el estado de cada NFT acuñado.

### Contribución y Soporte
Este proyecto es de código abierto, por lo que puedes contribuir, realizar mejoras y personalizaciones según tus necesidades. Si tienes preguntas o necesitas ayuda, no dudes en crear un problema (issue) o solicitar asistencia en la sección de problemas del repositorio.

#### ¡Espero que este proyecto te resulte interesante, es un paso en el mundo de los NFTs y la automatización de procesos en blockchain!

### Licencia
Este proyecto se distribuye bajo la licencia INSERTA_LA_LICENCIA_ADECUADA. Consulta el archivo LICENSE para obtener más detalles sobre los términos de uso.
