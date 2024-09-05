import pandas as pd
import streamlit as st
import plotly_express as px

st.header('Venta de vehiculos')
car_data = pd.read_csv('vehicles_us.csv')  # Leer el dataframe
st.write(car_data.head())


# Botón para el histograma
hist_button = st.button('Crear histograma')

if hist_button:  # al hacer clic en el botón
    # Escribir un mensaje
    st.write('Histograma para el conjunto de datos de anuncios de venta de coches')

    fig = px.histogram(car_data,
                       x="odometer",
                       nbins=20,  # Número de divisiones
                       title="Distribución de kilometraje",
                       labels={"odometer": "Kilometraje (millas)", }
                       )

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# Botón para el gráfico de dispersión
scatter_button = st.button('Crear gráfico de dispersión')

if scatter_button:  # al hacer clic en el botón
    # Escribir un mensaje
    st.write(
        'Gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión con mejoras
    graf = px.scatter(car_data,
                      x="odometer",
                      y="price",
                      labels={
                          "odometer": "Kilometraje (millas)", "price": "Precio (USD)"},
                      title="Relación entre Kilometraje y Precio",)

    # Mostrar el gráfico de dispersión
    st.plotly_chart(graf, use_container_width=True)
