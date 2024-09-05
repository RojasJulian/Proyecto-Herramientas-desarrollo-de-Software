import pandas as pd
import streamlit as st
import plotly_express as px

st.header('Venta de vehiculos')
car_data = pd.read_csv('vehicles_us.csv')  # Leer el dataframe
# st.write(car_data.head())


hist_button = st.button('Crear histograma')  # Creacion de boton


if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button('Crear grafico de dispersion')


if scatter_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Grafico de dispersion para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    graf = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(graf)
