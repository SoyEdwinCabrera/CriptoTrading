# CryptoTrading: Tu Puerta al Mundo de los Datos Cripto

## Introducción

Imagina un mundo donde los datos de las criptomonedas están al alcance de tu mano, listos para ser analizados, estudiados y utilizados para tomar decisiones informadas. **CryptoTrading** es un proyecto diseñado para facilitar la extracción de datos históricos y actuales de las principales criptomonedas, utilizando la API de Binance. Con este proyecto, puedes obtener precios, volúmenes y tendencias de activos como Bitcoin, Ethereum, Binance Coin, XRP y Litecoin, todo con unos pocos pasos.

## Historia del Proyecto

Todo comenzó con una idea: ¿cómo podemos simplificar el acceso a los datos de criptomonedas para analistas, traders y entusiastas? La respuesta fue clara: automatizar el proceso de extracción de datos utilizando Python y la API de Binance. Así nació **CryptoTrading**, un proyecto que combina la potencia de las bibliotecas modernas con la simplicidad de un script que hace todo el trabajo pesado por ti.

## Dependencias Instaladas

Para que este proyecto funcione, utilizamos las siguientes herramientas y bibliotecas:

1. **Python**: El lenguaje principal del proyecto.
2. **Binance API**: Para acceder a los datos de criptomonedas.
3. **Pandas**: Para manipular y estructurar los datos extraídos.
4. **dotenv**: Para manejar las claves API de forma segura.
5. **os**: Para interactuar con las variables de entorno.
6. **datetime**: Para manejar fechas y rangos temporales.

## Paso a Paso: Cómo Creamos el Proyecto

### 1. Configuración Inicial
Primero, instalamos las dependencias necesarias. Si aún no las tienes, puedes instalarlas ejecutando los siguientes comandos:

```bash
pip install python-binance pandas python-dotenv
```

### 2. Creación del Archivo `.env`
Para proteger nuestras claves API, creamos un archivo `.env` en el directorio raíz del proyecto. Este archivo contiene las siguientes variables:

```
api_key1=TU_API_KEY
api_secret1=TU_API_SECRET
```

### 3. Desarrollo del Script Principal
El corazón del proyecto es el archivo `criptos.py`. Aquí es donde ocurre la magia:

- **Carga de Variables de Entorno**: Utilizamos `dotenv` para cargar las claves API de forma segura.
- **Conexión con Binance**: Usamos la biblioteca `binance` para conectarnos a la API y extraer datos.
- **Extracción de Datos**: Creamos la función `criptodata`, que toma como entrada el ticker de una criptomoneda y extrae datos históricos y actuales.
- **Estructuración de Datos**: Utilizamos `pandas` para organizar los datos en un DataFrame, facilitando su análisis.
- **Exportación a CSV**: Guardamos los datos extraídos en archivos CSV para su uso posterior.

### 4. Ejecución del Script
Finalmente, ejecutamos el script para extraer datos de las criptomonedas seleccionadas. La lista de activos incluye:

- Bitcoin (BTCUSDT)
- Ethereum (ETHUSDT)
- Binance Coin (BNBUSDT)
- XRP (XRPUSDT)
- Litecoin (LTCUSDT)

El script guarda los datos en archivos CSV con el nombre del ticker correspondiente.

### 5. Validación y Optimización
Probamos el script con diferentes activos y rangos de tiempo para asegurarnos de que funciona correctamente. Ajustamos detalles como el formato de las fechas y la estructura de los datos para garantizar la máxima utilidad.

## Cómo Usar Este Proyecto

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias ejecutando:

```bash
pip install python-binance pandas python-dotenv
```

3. Crea un archivo `.env` en el directorio raíz y agrega tus claves API.
4. Ejecuta el script `criptos.py`:

```bash
python criptos.py
```

5. Encuentra los datos extraídos en archivos CSV en el mismo directorio.

## Conclusión

**CryptoTrading** es más que un proyecto; es una herramienta poderosa para explorar el mundo de las criptomonedas. Ya seas un analista buscando tendencias o un trader buscando datos históricos, este proyecto está diseñado para simplificar tu trabajo y ayudarte a tomar decisiones informadas. ¡Únete a nosotros en esta aventura cripto y descubre el poder de los datos!