import os
import pandas as pd
import requests

# ============================================================
# 1. EXTRACCIÓN — Fetch the data
# ============================================================

url_datos = "https://ourworldindata.org/grapher/global-temperature-anomalies-by-month.csv?v=1&csvType=full&useColumnShortNames=true"

df = pd.read_csv(
    url_datos,
    storage_options={
        "User-Agent": "Our World In Data data fetch/1.0"
    }
)

# ============================================================
# 2. EXTRACCIÓN — Fetch the metadata
# ============================================================

url_metadata = "https://ourworldindata.org/grapher/global-temperature-anomalies-by-month.metadata.json?v=1&csvType=full&useColumnShortNames=true"

metadata = requests.get(url_metadata).json()

# ============================================================
# 3. EXPLORACIÓN INICIAL
# ============================================================

print("Dimensiones del DataFrame:")
print(df.shape)

print("\nColumnas:")
print(df.columns.tolist())

print("\nTipos de datos:")
print(df.dtypes)

print("\nValores nulos:")
print(df.isnull().sum())

# ============================================================
# 4. LIMPIEZA
# ============================================================

# Eliminar registros que no tengan cambio de temperatura
df = df.dropna(subset=["temperature_anomaly"])

# ============================================================
# 5. TRANSFORMACIÓN
# ============================================================

# Convertir el año a entero
df["Year"] = df["year"].astype(int)

# Crear una nueva columna con la anomalía de temperatura
# redondeada a dos decimales
df["temperature_anomaly_round"] = df["temperature_anomaly"].round(2)

# ============================================================
# 6. FILTRADO
# ============================================================

# Trabajaremos únicamente con datos a partir del año 2000
df = df[df["year"] >= 2000]

# ============================================================
# 7. ANÁLISIS
# ============================================================

# Promedio de anomalía de temperatura por mes
promedio_mes = (
    df.groupby("entity")["temperature_anomaly_round"]
      .mean()
      .round(2)
      .sort_values(ascending=False)
)

print("\nPromedio de anomalía de temperatura por mes:")
print(promedio_mes.head(10))

# ============================================================
# 8. RESULTADO
# ============================================================
# Obtener la ruta absoluta del archivo de salida, relativa a la ubicación de este script
script_dir = os.path.dirname(os.path.abspath(__file__))
archivo_salida = os.path.join(os.path.dirname(script_dir), "data", "processed", "promedio_anomalia_temperatura_por_mes.csv")

# Crear directorio si no existe
os.makedirs(os.path.dirname(archivo_salida), exist_ok=True)

promedio_mes.to_csv(
    archivo_salida,
    header=["Average temperature anomaly"]
)

print("\nPipeline ejecutado correctamente.")
print(f"Archivo generado: {archivo_salida}")