import pandas as pd

# Cargando los datos de nuestra big data de prueba
data = pd.read_csv('datos.csv')  

# Análisis básico de los datos 
print("Número total de registros:", len(data))
print("Columnas disponibles:", list(data.columns))

# Ejemplo de procesamiento y análisis de datos
# Supongamos que queremos encontrar el promedio de una columna 'ventas' en función de la columna 'mes'
promedio_ventas_mes = data.groupby('mes')['ventas'].mean()

# Visualización de resultados
print("\nPromedio de ventas por mes:")
print(promedio_ventas_mes)

