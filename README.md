# Análisis de la Huella Ecológica Global 2023

Este proyecto analiza datos relacionados con la huella ecológica global del año 2023. Utilizando un conjunto de datos almacenado en un archivo CSV, el proyecto busca calcular estadísticas clave y crear un modelo de red neuronal para predecir la huella ecológica total de consumo.

## Descripción de los Archivos

- `Global Ecological Footprint 2023.csv`: Archivo CSV que contiene los datos de la huella ecológica global.
- `main.py`: Script de Python que contiene la lógica para analizar los datos y generar resultados.
- `nuevo.csv`: Archivo CSV que contiene dos columnas seleccionadas del conjunto de datos original: `Country` y `Region`.

## Procesamiento de Datos

El script `main.py` realiza las siguientes operaciones en el conjunto de datos:

- Lee los datos del archivo CSV utilizando la biblioteca pandas.
- Muestra las primeras 10 filas del DataFrame para visualizar los datos de muestra.
- Obtiene la lista de columnas del DataFrame para conocer los nombres de las columnas.
- Calcula el valor máximo de la columna "Number of Countries required".
- Calcula el valor mínimo de la columna "Number of Countries required".
- Muestra la fila que tiene el mayor valor en la columna "Number of Countries required".
- Muestra la fila que tiene el menor valor en la columna "Number of Countries required".
- Calcula el promedio de la columna "Number of Countries required".
- Selecciona solo dos columnas del DataFrame ("Country" y "Region") y guarda el resultado en un nuevo DataFrame llamado "nuevo".
- Guarda el nuevo DataFrame en un archivo CSV llamado "nuevo.csv".

## Requisitos

Para ejecutar el script `main.py`, es necesario tener instaladas las siguientes bibliotecas de Python:

- pandas
- scikit-learn
- TensorFlow

Asegúrate de tener estas bibliotecas instaladas en tu entorno de Python antes de ejecutar el código.

## Ejecución

Para ejecutar el script, debes proporcionar la ruta correcta del archivo CSV en la variable `archivo_csv`. 

Una vez que hayas configurado la ruta correcta, puedes ejecutar el script y ver los resultados en la consola. Los resultados incluirán las primeras 10 filas del DataFrame, la lista de columnas, el valor máximo y mínimo de la columna "Number of Countries required", la fila con el mayor y menor valor de esa columna, el promedio de la columna "Number of Countries required", el DataFrame "nuevo" con las columnas seleccionadas y el archivo CSV "nuevo.csv" guardado en la ubicación especificada.

Recuerda asegurarte de proporcionar la ruta correcta para el archivo CSV y el archivo CSV resultante. Además, asegúrate de tener instaladas las bibliotecas pandas, scikit-learn y TensorFlow en tu entorno de Python para que el código funcione correctamente.