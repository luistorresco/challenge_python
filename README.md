# Análisis de la Huella Ecológica Global 2023

Este proyecto analiza datos relacionados con la huella ecológica global del año 2023. Utilizando un conjunto de datos almacenado en un archivo CSV, el proyecto busca calcular estadísticas clave y crear un modelo de red neuronal para predecir la huella ecológica total de consumo.

## Descripción de los Archivos

- `Global Ecological Footprint 2023.csv`: Archivo CSV que contiene los datos de la huella ecológica global.
- `modelo.py`: Script de Python que contiene la lógica para entrenar el modelo de red neuronal.
- `nuevo.csv`: Archivo CSV que contiene dos columnas seleccionadas del conjunto de datos original: `Country` y `Region`.

## Procesamiento de Datos

El script de Python realiza las siguientes operaciones en el conjunto de datos:

- Lee los datos del archivo CSV.
- Convierte las columnas relevantes a valores numéricos, tratando los errores como valores `NaN`.
- Rellena los valores `NaN` con la media de las columnas numéricas.
- Separa los datos en características (`X`) y la etiqueta objetivo (`y`) para predecir la huella ecológica total de consumo.
- Divide los datos en conjuntos de entrenamiento y prueba.
- Escala las características para normalización.

## Modelo de Red Neuronal

El modelo de red neuronal se construye utilizando la API de Keras de TensorFlow y consiste en:

- Una capa de entrada con activación `relu`.
- Una capa oculta con 64 unidades y activación `relu`.
- Una capa oculta con 32 unidades y activación `relu`.
- Una capa de salida con una sola unidad para la predicción.

El modelo se compila con el optimizador `adam` y la función de pérdida `mean_squared_error`. Se entrena durante 1000 épocas con un `validation_split` del 20%.

## Evaluación y Predicción

Después de entrenar el modelo, este se evalúa con el conjunto de prueba. Luego, se realizan predicciones sobre este mismo conjunto. Las primeras 10 predicciones se imprimen en la consola junto con los valores reales correspondientes para comparar su rendimiento.

## Creación de un Nuevo CSV

El script también permite seleccionar dos columnas específicas del DataFrame (`Country` y `Region`) y guardarlas en un nuevo archivo CSV llamado `nuevo.csv`.

## Requisitos

Para ejecutar el script, es necesario tener instaladas las siguientes bibliotecas de Python:

- pandas
- scikit-learn
- TensorFlow

## Ejecución

Para ejecutar el script, navega al directorio donde se encuentra el archivo `modelo.py` y ejecuta el siguiente comando en la terminal:

```shell
python modelo.py
python main.py