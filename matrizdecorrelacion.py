# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 09:49:34 2024

@author: jperezr
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar automáticamente el archivo Excel
file_path = 'Matriz de correlacion.xlsx'
data = pd.read_excel(file_path)

# Mostrar los datos en la aplicación
st.title('Matriz general de Correlación')
st.write("Los datos del archivo Excel son:")
st.dataframe(data)



# Datos de los atributos y sus pesos
data = {
    'Atributo': [
        'Sobre trabajo', 'Puesto', 'Estado marital', 'Años trabajados', 
        'Nivel en la empresa', 'Años en el rol actual', 'Salario mensual', 
        'Edad', 'Años con actual jefe', 'Nivel de opción de acciones', 
        'Años en la compañía', 'Compromiso con el trabajo', 
        'Satisfacción con el trabajo', 'Campo de estudios', 'Satisfacción', 
        'Departamento', 'Distancia desde casa', 'Trabajo Vida relación', 
        'Entrenamiento año anterior', 'Salario diario', 
        'Satisfacción en la relación', 'Trabajos totales', 
        'Años desde última promoción', 'Educación', 'Sexo', 
        'Tarifa mensual', 'Porcentaje de aumento salarial', 
        'Salario por horas', 'Desempeño'
    ],
    'Peso': [
        0.246, 0.242, 0.177, 0.171, 0.169, 0.161, 0.160, 
        0.159, 0.156, 0.137, 0.134, 0.130, 0.103, 0.103, 
        0.103, 0.086, 0.078, 0.064, 0.059, 0.057, 
        0.046, 0.043, 0.033, 0.031, 0.029, 0.015, 
        0.013, 0.007, 0.003
    ]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Configuración de Streamlit
st.title('Gráfico de Barras: pesos por correlación')

# Crear gráfico de barras
plt.figure(figsize=(12, 8))
plt.barh(df['Atributo'], df['Peso'], color='skyblue')
plt.xlabel('Peso')
plt.ylabel('Atributo')
plt.title('Peso de Atributos')
plt.xlim(0, 0.25)  # Ajustar el límite del eje x si es necesario
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Mostrar el gráfico en Streamlit
st.pyplot(plt)