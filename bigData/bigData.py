import pandas as pd

data = pd.read_csv('datos.csv')  

print("Número total de registros:", len(data))
print("Columnas disponibles:", list(data.columns))

# Ejemplo de procesamiento y análisis de datos
# Supongamos que queremos encontrar el promedio de una columna 'ventas' en función de la columna 'mes'
promedio_ventas_mes = data.groupby('mes')['ventas'].mean()


print("\nPromedio de ventas por mes:")
print(promedio_ventas_mes)

