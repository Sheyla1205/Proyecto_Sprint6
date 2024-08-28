import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón
disp_button = st. button('Grafico de dispersión')


st.header('Creacion de Histograma')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disp_button:
    st.write(
        'Creación de un grafico de dispersión para el conjunto de datos de año de moledo de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un grafico de dispersión')


if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    fig = px.scatter(car_data, x='odometer', y='days_listed')
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Construir un grafico de dispersion comparando el valor de odometro con el numero de días en venta')
    fig = px.scatter(car_data, x='odometer', y='days_listed')
    st.plotly_chart(fig, use_container_width=True)
