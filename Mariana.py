import streamlit as st
import time
import os

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Para Mariana", page_icon="❤️", layout="centered")

# --- ESTILOS CSS (Fondo de cuaderno y botones rojos) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f6;
        background-image: linear-gradient(90deg, rgba(200,0,0,.05) 1px, transparent 1px),
                          linear-gradient(rgba(200,0,0,.05) 1px, transparent 1px);
        background-size: 20px 20px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border: none;
        height: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>💌 Pacto 2032</h1>", unsafe_allow_html=True)
st.write("Un mensaje especial para mi 'prima' favorita y mi 'primer todo'.")

# --- BOTÓN PARA ABRIR ---
if st.button("Abrir Carta"):
    with st.spinner('Cargando promesa...'):
        time.sleep(1.5)
    
    st.balloons() 

    # --- CARGAR LAS IMÁGENES ---
    # Aquí es donde fallaba antes. Verifica los nombres de archivo.
    imagenes = ["carta_parte1.png", "carta_parte2.png"]
    
    for nombre_img in imagenes:
        if os.path.exists(nombre_img):
            st.image(nombre_img, use_container_width=True) # Actualizado para quitar la alerta amarilla
            st.write("---") # Separador entre hojas
        else:
            st.error(f"⚠️ Error: No encuentro la imagen llamada '{nombre_img}'. Por favor guárdala en la misma carpeta que este archivo.")

    # --- MÚSICA FINAL ---
    st.markdown("### 🎶 Nuestra Canción")
    st.video("https://www.youtube.com/watch?v=R0y_m5P6XUw") 

    # --- CONFIRMACIÓN ---
    st.write("---")
    if st.checkbox("Acepto el pacto hasta el 31/12/2032 💍"):
        st.success("✅ Pacto sellado. Nos vemos en las próximas vacaciones. ❤️")