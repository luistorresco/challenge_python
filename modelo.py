import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

# Ruta del archivo CSV
archivo_csv = r"C:\Users\lf.torres\Desktop\reto python\Global Ecological Footprint 2023.csv"

# Leer el archivo CSV
df = pd.read_csv(archivo_csv, encoding="latin-1")

# Convertir todas las columnas relevantes a numéricas, forzando los errores a N
for col in ['SDGi', 'Life Exectancy', 'HDI', 'Per Capita GDP',
            'Population (millions)', 'Cropland Footprint', 'Grazing Footprint',
            'Forest Product Footprint', 'Carbon Footprint', 'Fish Footprint',
            'Built up land']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Calcular la media solo para las columnas numéricas y rellenar los valores NaN
mean_values = df.select_dtypes(include=[np.number]).mean()
df.fillna(mean_values, inplace=True)

# Separar las características (X) y la etiqueta (y) que deseas predecir
X = df[['SDGi', 'Life Exectancy', 'HDI', 'Per Capita GDP',
        'Population (millions)', 
        'Cropland Footprint', 'Grazing Footprint', 'Forest Product Footprint', 
        'Carbon Footprint', 'Fish Footprint', 'Built up land']]
y = df['Total Ecological Footprint (Consumption)']

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
                                                    random_state=42)

# Escalar las características para la normalización
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Crear el modelo
model = keras.Sequential([
    layers.Dense(units=64, activation='relu', 
                 input_shape=(X_train_scaled.shape[1],)),
    layers.Dense(units=32, activation='relu'),
    layers.Dense(units=1)
])

# Compilar el modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# Entrenar el modelo
history = model.fit(X_train_scaled, y_train, epochs=5000, validation_split=0.2)

# Evaluar el modelo
model.evaluate(X_test_scaled, y_test)

# Hacer predicciones con el conjunto de prueba
predictions = model.predict(X_test_scaled)

# Imprimir algunas de las predicciones
for i in range(1):  # Imprimir las primeras 10 predicciones
    print(f"Predicción: {predictions[i][0]}, Valor real: {y_test.iloc[i]}")