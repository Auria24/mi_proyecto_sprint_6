import pandas as pd
import streamlit as st
import plotly_express as px

datos = pd.read_csv('vehicles_us.csv')

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            # crear un histograma
            fig = px.histogram(datos, x="odometer")
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)


build_histograma = st.checkbox('Construir un histograma')

if build_histograma: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    

scatter_button = st.button('Construir grafia de dispercion') # crear un botón   
if scatter_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un grafica de dispercion para el conjunto de datos de anuncios de venta de coches')   
            # crear un histograma
            fig = px.scatter(datos, x="odometer", y="price") # crear un gráfico de dispersión
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)
