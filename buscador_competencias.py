import pandas as pd
import streamlit as st

# Cargar los datos desde el archivo Excel
file_path = "renec.xlsx"  # Asegúrate de que este archivo esté en la misma carpeta
data = pd.read_excel(file_path, sheet_name="datos")

# Renombrar las columnas para simplificar su uso
data.columns = ['Código', 'Nivel', 'Título', 'Comité', 'Sector Productivo']

# Título de la aplicación
st.title("Buscador de Estándares de Competencia - RENEC")

# Filtros interactivos
sector = st.selectbox("Filtrar por Sector Productivo:", ["Todos"] + data['Sector Productivo'].unique().tolist())
nivel = st.selectbox("Filtrar por Nivel de Competencia:", ["Todos"] + sorted(data['Nivel'].unique()))
keyword = st.text_input("Buscar por Palabra Clave en el Título:")

# Aplicar filtros
filtered_data = data.copy()
if sector != "Todos":
    filtered_data = filtered_data[filtered_data['Sector Productivo'] == sector]
if nivel != "Todos":
    filtered_data = filtered_data[filtered_data['Nivel'] == nivel]
if keyword:
    filtered_data = filtered_data[filtered_data['Título'].str.contains(keyword, case=False, na=False)]

# Mostrar resultados
st.subheader("Resultados de la Búsqueda")
st.write(f"Se encontraron {len(filtered_data)} estándares.")
st.dataframe(filtered_data)
