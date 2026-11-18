# Práctica U5.1 — Preparación de PySpark y exploración de NYC Taxi

## Descripción

Preparación del entorno local con PySpark y PyArrow para consultar de forma remota (HTTP `Range`) un archivo Parquet de NYC Yellow Taxi (enero de 2025) sin descargarlo completo en disco.

## Estructura

- `U5_1_preparation_pyspark_NYC_taxi.ipynb`: Notebook principal de la práctica.
- `notebooks/`: Carpeta para notebooks adicionales de la unidad.
- `data/raw/` y `data/processed/`: Estructura estándar de datos (en esta práctica no se almacenan datasets locales).
- `requirements.txt`: Dependencias de Python necesarias para ejecutar el proyecto.

## Requisitos previos

- Python 3 (entorno virtual `.venv` en `U5_1/.venv`)
- Java (JDK 17+ disponible en el sistema)

## Ejecución

1. Activa el entorno virtual `U5_1/.venv` o selecciona su kernel en VS Code / Jupyter.
2. Si necesitas reinstalar dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta todas las celdas de `U5_1_preparation_pyspark_NYC_taxi.ipynb`.
