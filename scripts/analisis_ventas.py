# =============================================================================
# Script: analisis_ventas.py
# Descripción: Análisis de ventas a partir de un dataset CSV.
#              Calcula indicadores clave y genera un gráfico de evolución temporal.
# Autor: P2 - Paco (desarrollo inicial), P3 - Luis (revisión y documentación)
# =============================================================================

import pandas as pd          # Manipulación y análisis de datos tabulares
import matplotlib.pyplot as plt  # Generación de gráficos y visualizaciones

# -----------------------------------------------------------------------------
# Carga de datos
# Se lee el archivo CSV desde la carpeta /datos y se almacena en un DataFrame.
# Un DataFrame es una tabla similar a una planilla de cálculo.
# -----------------------------------------------------------------------------

df = pd.read_csv('datos/dataset.csv')

# -----------------------------------------------------------------------------
# Indicadores generales de ventas
# Se calculan métricas de resumen sobre la columna 'sales_amount',
# que representa el monto de cada venta registrada.
# -----------------------------------------------------------------------------

print("=" * 40 + " ANÁLISIS DE VENTAS " + "=" * 40 + "\n")
print(f"Ventas totales:          ${df['sales_amount'].sum():,.2f}")
print(f"Venta promedio:          ${df['sales_amount'].mean():,.2f}")
print(f"Venta máxima registrada: ${df['sales_amount'].max():,.2f}")
print(f"Venta mínima registrada: ${df['sales_amount'].min():,.2f}")

# -----------------------------------------------------------------------------
# Análisis de ventas por mes
# Se convierte la columna 'sales_date' al tipo datetime para poder extraer
# componentes de fecha (año, mes, día) de forma precisa.
# Luego se agrupa por número de mes y se suman los montos de cada grupo.
# -----------------------------------------------------------------------------

df['sales_date'] = pd.to_datetime(df['sales_date'])  # Conversión a tipo datetime
df['mes'] = df['sales_date'].dt.month                # Extracción del número de mes (1-12)
ventas_por_mes = df.groupby('mes')['sales_amount'].sum()  # Sumatoria de ventas agrupadas por mes

print("\n" + "=" * 42 + " VENTAS POR MES " + "=" * 42 + "\n")
print(ventas_por_mes)

# -----------------------------------------------------------------------------
# Generación del gráfico de evolución temporal
# Se grafica el monto de cada venta en función de su fecha, permitiendo
# visualizar tendencias y variaciones a lo largo del tiempo.
# -----------------------------------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    df['sales_date'],
    df['sales_amount'],
    marker='o',    # Marca cada punto de dato con un círculo
    color='blue',
    linewidth=1.5  # Grosor de la línea de conexión entre puntos
)

plt.title('Evolución de Ventas')
plt.xlabel('Fecha')
plt.ylabel('Monto de Ventas ($)')     # Se agrega la unidad monetaria al eje Y
plt.xticks(rotation=45)               # Rotación de 45° para evitar superposición de fechas
plt.tight_layout()                    # Ajuste automático de márgenes para evitar recortes
plt.savefig('resultados/grafico_ventas.png')     # Se guarda el gráfico como imagen PNG en /resultados

print("\nGráfico guardado correctamente en: resultados/grafico_ventas.png")
