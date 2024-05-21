import pandas as pd



# Ruta del archivo CSV
archivo_csv = (
    r"C:\\Users\\lf.torres\\Desktop\\reto python\\Global Ecological Footprint 2023.csv"
)

# Leer el archivo CSV
df = pd.read_csv(archivo_csv, encoding="latin-1")

# Mostrar las primeras 10 filas del DataFrame
print(df.head(10))

# Mostrar las columnas del DataFrame
columnas = df.columns
print(columnas)


# Mostrar el número maximo de la columna 'Number of Countries requered'
print(df["Number of Countries required"].max())

# Mostrar el número minimo de la columna 'Number of Countries requered'
print(df["Number of Countries required"].min())

# Mostrar la cidudad con el mayor 'Number of Countries requered'
print(
    df[df["Number of Countries required"] == 
       df["Number of Countries required"].max()]
)

# Mostrar la cidudad con el menor 'Number of Countries requered'
print(
    df[df["Number of Countries required"] == 
       df["Number of Countries required"].min()]
)

# mostrar el promedio de la columna 'Number of Countries requered'
print(df["Number of Countries required"].mean())

# mostrar solo dos columnas del DataFrame y guadarlo en un nuevo DataFrame
nuevo = df[["Country", "Region"]]
print(nuevo)

# Mostrar solo dos columnas del DataFrame y guardarlo en un nuevo CSV
nuevo_csv = r"C:\\Users\\lf.torres\\Desktop\\reto python\\nuevo.csv"
df[["Country", "Region"]].to_csv(nuevo_csv, index=False)
