import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generar datos aleatorios
np.random.seed(0)

n = 50  # Número de observaciones
temperatura = np.random.normal(25, 5, n)  # Temperatura en grados Celsius
precipitacion = np.random.uniform(0, 20, n)  # Precipitación en mm
luz_solar = np.random.uniform(4, 12, n)  # Luz solar en horas
num_hojas = 5 + 2 * temperatura + 0.5 * precipitacion + 1.5 * luz_solar + np.random.normal(0, 3, n)  # Número de hojas

# Crear un DataFrame con los datos
data = pd.DataFrame({'Temperatura (°C)': temperatura,
                     'Precipitación (mm)': precipitacion,
                     'Luz Solar (horas)': luz_solar,
                     'Número de Hojas': num_hojas})

# Crear el modelo de regresión lineal
model = LinearRegression()

# Dividir los datos en variables independientes (X) y variable dependiente (Y)
X = data[['Temperatura (°C)', 'Precipitación (mm)', 'Luz Solar (horas)']]
Y = data['Número de Hojas']

# Ajustar el modelo a los datos
model.fit(X, Y)

# Obtener los coeficientes de regresión
coeficientes = model.coef_
intercepcion = model.intercept_

# Imprimir los coeficientes
print('Coeficiente de Temperatura:', coeficientes[0])
print('Coeficiente de Precipitación:', coeficientes[1])
print('Coeficiente de Luz Solar:', coeficientes[2])
print('Intercepción:', intercepcion)

# Realizar predicciones
nueva_temperatura = 30
nueva_precipitacion = 10
nueva_luz_solar = 8
prediccion = model.predict([[nueva_temperatura, nueva_precipitacion, nueva_luz_solar]])

# Imprimir la predicción
print(f'Número de Hojas estimado para T={nueva_temperatura}°C, P={nueva_precipitacion}mm, L={nueva_luz_solar} horas: {prediccion[0]:.2f}')

# Crear un gráfico de dispersión para visualizar los resultados
plt.figure(figsize=(10, 6))
plt.scatter(Y, model.predict(X), color='blue', alpha=0.7)
plt.xlabel('Número de Hojas Real')
plt.ylabel('Número de Hojas Predicho')
plt.title('Regresión Lineal para el Crecimiento de Plantas de Maíz')
plt.grid(True)
plt.show()
