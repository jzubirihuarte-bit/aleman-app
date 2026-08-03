import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Entrenador de Alemán",
    page_icon="🇩🇪",
    layout="centered"
)

# Cargar Excel
@st.cache_data
def cargar_datos():
    return pd.read_excel("sustantivos_aleman_100_mas_sin_frases.xlsx")

df = cargar_datos()

# Inicialización de variables de sesión
if "indice" not in st.session_state:
    st.session_state.indice = df.sample().index[0]

if "aciertos" not in st.session_state:
    st.session_state.aciertos = 0

if "fallos" not in st.session_state:
    st.session_state.fallos = 0

fila = df.loc[st.session_state.indice]

st.title("🇩🇪 Practica Alemán")

# Estadísticas
total = st.session_state.aciertos + st.session_state.fallos

if total > 0:
    porcentaje = round(st.session_state.aciertos / total * 100, 1)
else:
    porcentaje = 0

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("✅ Aciertos", st.session_state.aciertos)

with col2:
    st.metric("❌ Fallos", st.session_state.fallos)

with col3:
    st.metric("% Éxito", porcentaje)

st.divider()

palabra = fila["Palabra en alemán"]

st.subheader(f"Palabra: {palabra}")

articulo_usuario = st.selectbox(
    "Selecciona el artículo",
    ["der", "die", "das"]
)

traduccion_usuario = st.text_input(
    "Escribe la traducción al español"
)

# Comprobar
if st.button("Comprobar"):

    articulo_correcto = str(fila["Artículo"]).strip().lower()
    traduccion_correcta = str(fila["Traducción al español"]).strip().lower()

    articulo_ok = articulo_usuario.lower() == articulo_correcto
    traduccion_ok = (
        traduccion_usuario.strip().lower()
        == traduccion_correcta
    )

    if articulo_ok and traduccion_ok:
        st.success("✅ Todo correcto")
        st.session_state.aciertos += 1

    else:
        st.session_state.fallos += 1

        if not articulo_ok:
            st.error(
                f"Artículo incorrecto. Correcto: {articulo_correcto}"
            )

        if not traduccion_ok:
            st.error(
                f"Traducción incorrecta. Correcta: {traduccion_correcta}"
            )

# Siguiente palabra
if st.button("Siguiente palabra"):

    nuevo_indice = df.sample().index[0]

    while nuevo_indice == st.session_state.indice:
        nuevo_indice = df.sample().index[0]

    st.session_state.indice = nuevo_indice
    st.rerun()

# Reiniciar estadísticas
if st.button("Reiniciar estadísticas"):
    st.session_state.aciertos = 0
    st.session_state.fallos = 0
    st.rerun()