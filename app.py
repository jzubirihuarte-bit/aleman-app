import streamlit as st
import pandas as pd
import random

# =====================================================
# CONFIGURACIÓN GENERAL
# =====================================================

st.set_page_config(
    page_title="Entrenador de Alemán",
    page_icon="🇩🇪",
    layout="centered"
)

st.title("🇩🇪 Entrenador de Alemán")

# =====================================================
# ESTADÍSTICAS GLOBALES
# =====================================================

if "aciertos" not in st.session_state:
    st.session_state.aciertos = 0

if "fallos" not in st.session_state:
    st.session_state.fallos = 0


total = st.session_state.aciertos + st.session_state.fallos

if total > 0:
    porcentaje = round(
        st.session_state.aciertos / total * 100,
        1
    )
else:
    porcentaje = 0

col1, col2, col3 = st.columns(3)

col1.metric(
    "✅ Aciertos",
    st.session_state.aciertos
)

col2.metric(
    "❌ Fallos",
    st.session_state.fallos
)

col3.metric(
    "% Éxito",
    porcentaje
)

st.divider()

# =====================================================
# PESTAÑAS
# =====================================================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📚 Vocabulario",
        "📝 Verbos",
        "💬 Frases",
        "🎯 Examen"
    ]
)

# =====================================================
# SUSTANTIVOS
# =====================================================

with tab1:

    st.header("📚 Vocabulario")

    @st.cache_data
    def cargar_vocabulario():
        return pd.read_excel(
            "datos/sustantivos_aleman_100_mas_sin_frases.xlsx"
        )

    df = cargar_vocabulario()

    # Inicializar palabra actual
    if "indice_vocabulario" not in st.session_state:
        st.session_state.indice_vocabulario = (
            df.sample().index[0]
        )

    fila = df.loc[
        st.session_state.indice_vocabulario
    ]

    palabra = fila["Palabra en alemán"]

    st.subheader(
        f"Palabra: {palabra}"
    )

    articulo_usuario = st.selectbox(
        "Selecciona el artículo",
        ["der", "die", "das"],
        key="articulo_vocabulario"
    )

    traduccion_usuario = st.text_input(
        "Escribe la traducción al español",
        key="traduccion_vocabulario"
    )

    if st.button(
        "✅ Comprobar",
        key="comprobar_vocabulario"
    ):

        articulo_correcto = (
            str(fila["Artículo"])
            .strip()
            .lower()
        )

        traduccion_correcta = (
            str(
                fila["Traducción al español"]
            )
            .strip()
            .lower()
        )

        articulo_ok = (
            articulo_usuario.lower()
            ==
            articulo_correcto
        )

        traduccion_ok = (
            traduccion_usuario.strip().lower()
            ==
            traduccion_correcta
        )

        if articulo_ok and traduccion_ok:

            st.success(
                "✅ Artículo y traducción correctos"
            )

            st.session_state.aciertos += 1

        else:

            st.session_state.fallos += 1

            if not articulo_ok:

                st.error(
                    f"Artículo correcto: "
                    f"{fila['Artículo']}"
                )

            if not traduccion_ok:

                st.error(
                    f"Traducción correcta: "
                    f"{fila['Traducción al español']}"
                )

    if st.button(
        "➡️ Siguiente palabra",
        key="siguiente_vocabulario"
    ):

        nuevo_indice = (
            df.sample().index[0]
        )

        while (
            nuevo_indice
            ==
            st.session_state.indice_vocabulario
        ):
            nuevo_indice = (
                df.sample().index[0]
            )

        st.session_state.indice_vocabulario = (
            nuevo_indice
        )

        st.rerun()

# =====================================================
# VERBOS
# =====================================================

with tab2:

    st.header("📝 Verbos")

    @st.cache_data
    def cargar_verbos():
        return pd.read_excel(
            "datos/verbos_aleman.xlsx"
        )

    verbos = cargar_verbos()

    personas = [
        "ich",
        "du",
        "er/sie/es",
        "wir",
        "ihr",
        "sie/Sie"
    ]

    if "indice_verbo" not in st.session_state:

        st.session_state.indice_verbo = (
            verbos.sample().index[0]
        )

        st.session_state.persona = (
            random.choice(personas)
        )

    fila = verbos.loc[
        st.session_state.indice_verbo
    ]

    infinitivo = fila["Infinitivo"]

    persona = (
        st.session_state.persona
    )

    st.subheader(
        f"Conjuga '{infinitivo}' "
        f"para '{persona}'"
    )

    conjugacion_usuario = (
        st.text_input(
            "Conjugación",
            key="conjugacion"
        )
    )

    significado_usuario = (
        st.text_input(
            "Significado en español",
            key="significado"
        )
    )

    if st.button(
        "Comprobar verbo"
    ):

        conjugacion_ok = (
            conjugacion_usuario
            .strip()
            .lower()
            ==
            str(fila[persona])
            .strip()
            .lower()
        )

        significado_ok = (
            significado_usuario
            .strip()
            .lower()
            ==
            str(fila["Español"])
            .strip()
            .lower()
        )

        if (
            conjugacion_ok
            and significado_ok
        ):

            st.success(
                "✅ Correcto"
            )

            st.session_state.aciertos += 1

        else:

            st.session_state.fallos += 1

            st.error(
                f"Conjugación correcta: "
                f"{fila[persona]}"
            )

            st.error(
                f"Significado correcto: "
                f"{fila['Español']}"
            )

    if st.button(
        "Siguiente verbo"
    ):

        st.session_state.indice_verbo = (
            verbos.sample().index[0]
        )

        st.session_state.persona = (
            random.choice(personas)
        )

        st.rerun()
        

# =====================================================
# FRASES
# =====================================================

with tab3:

    st.header("💬 Frases")

    @st.cache_data
    def cargar_frases():
        return pd.read_excel(
            "datos/frases_aleman_100.xlsx"
        )

    frases = cargar_frases()

    modo = st.radio(
        "Modo de práctica",
        [
            "🇩🇪 Alemán → Español",
            "🇪🇸 Español → Alemán"
        ]
    )

    if "indice_frase" not in st.session_state:
        st.session_state.indice_frase = (
            frases.sample().index[0]
        )

    fila = frases.loc[
        st.session_state.indice_frase
    ]

    frase_aleman = fila["Frase alemán"]
    frase_espanol = fila["Frase español"]

    # ===== ALEMÁN -> ESPAÑOL =====

    if modo == "🇩🇪 Alemán → Español":

        st.subheader("Traduce al español:")

        st.info(frase_aleman)

        respuesta = st.text_area(
            "Tu traducción",
            key="frase_es"
        )

        if st.button(
            "Comprobar frase ES"
        ):

            if (
                respuesta.strip().lower()
                ==
                frase_espanol.strip().lower()
            ):

                st.success(
                    "✅ Correcto"
                )

                st.session_state.aciertos += 1

            else:

                st.session_state.fallos += 1

                st.error(
                    f"Correcto: "
                    f"{frase_espanol}"
                )

    # ===== ESPAÑOL -> ALEMÁN =====

    else:

        st.subheader(
            "Escribe la frase en alemán:"
        )

        st.info(frase_espanol)

        respuesta = st.text_area(
            "Tu respuesta",
            key="frase_de"
        )

        if st.button(
            "Comprobar frase DE"
        ):

            if (
                respuesta.strip().lower()
                ==
                frase_aleman.strip().lower()
            ):

                st.success(
                    "✅ Correcto"
                )

                st.session_state.aciertos += 1

            else:

                st.session_state.fallos += 1

                st.error(
                    f"Correcto: "
                    f"{frase_aleman}"
                )

    st.write("")

    if st.button(
        "➡️ Siguiente frase"
    ):

        nuevo_indice = (
            frases.sample().index[0]
        )

        while (
            nuevo_indice
            ==
            st.session_state.indice_frase
        ):
            nuevo_indice = (
                frases.sample().index[0]
            )

        st.session_state.indice_frase = (
            nuevo_indice
        )

        st.rerun()

    if "Adjetivo/Concepto" in fila:

        st.caption(
            f"💡 Concepto principal: "
            f"{fila['Adjetivo/Concepto']}"
        )

# =====================================================
# EXAMEN (FUTURO)
# =====================================================

with tab4:

    st.header("🎯 Examen mixto")

    st.info(
        "Próximamente: mezclará "
        "sustantivos, verbos, "
        "adjetivos y preposiciones."
    )

# =====================================================
# REINICIAR
# =====================================================

st.divider()

if st.button(
    "🔄 Reiniciar estadísticas"
):
    st.session_state.aciertos = 0
    st.session_state.fallos = 0
    st.rerun()