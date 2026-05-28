import pandas as pd  # Librería para leer CSV
import matplotlib.pyplot as plt  # Librería para crear gráficos

# Leer archivo CSV
df = pd.read_csv('datos/dataset.csv')  # Guardar en "df"

# Indicadores básicos
print("="*40 + " ANÁLISIS DE VENTAS " + "="*40 + "\n")
print(f"Ventas totales: ${df['sales_amount'].sum():,.2f}")
print(f"Venta promedio diaria: ${df['sales_amount'].mean():,.2f}")
print(f"Venta máxima: ${df['sales_amount'].max():,.2f}")
print(f"Venta mínima: ${df['sales_amount'].min():,.2f}")

# Ventas por mes
df['sales_date'] = pd.to_datetime(df['sales_date'])  # Convertir la columna de fecha a formate datetime
df['mes'] = df['sales_date'].dt.month  # Extraer número del mes en nueva columna
ventas_por_mes = df.groupby('mes')['sales_amount'].sum() # Agrupar ventas por mes y calcular la suma total

print("\n" + "="*42 + " VENTAS POR MES " + "="*42 + "\n")
print(ventas_por_mes)

# Gráfico de evolución de ventas
plt.figure(figsize=(10, 5))  # Crear figura del gráfico
plt.plot(df['sales_date'], df['sales_amount'], marker='o', color='blue')  # Graficar evolución temporal de las ventas
plt.title('Evolución de Ventas')  # Título
plt.xlabel('Fecha')  # "Fecha" en posición horizontal del gráfico
plt.ylabel('Monto de Ventas')  # "Monto de ventas" en posición vertical del gráfico
plt.xticks(rotation=45)  # Rotar las fechas del eje X 45° para mejor legibilidad
plt.tight_layout()  # Ajustar los márgenes del gráfico
plt.savefig('resultados/grafico_ventas.png')  # Guardar el gráfico como imagen en la carpeta de resultados

print("\nGráfico guardado en /resultados")
