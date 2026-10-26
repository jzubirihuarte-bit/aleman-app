import streamlit as st
import sqlite3
import pandas as pd
from rapidfuzz import fuzz
import plotly.express as px
import random

# =====================================================
# CONFIGURACIÓN
# =====================================================

st.set_page_config(
    page_title="🇩🇪 Deutsch Trainer",
    page_icon="🇩🇪",
    layout="wide"
)

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.card {
    border-radius:15px;
    padding:20px;
    border:1px solid #ddd;
    margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# CARGAR DATOS
# =====================================================

def cargar_vocabulario():

    conn = sqlite3.connect("datos/aleman.db")

    try:

        df = pd.read_sql(
            "SELECT * FROM vocabulario",
            conn
        )

        return df

    except Exception as e:

        st.error(str(e))
        raise

    finally:

        conn.close()
       
df_total = cargar_vocabulario()

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("⚙️ Configuración")

nivel = st.sidebar.selectbox(
    "Nivel",
    ["A1", "A2", "B1", "B2"]
)


categorias = sorted(
    df_total["categoria"]
    .dropna()
    .unique()
    .tolist()
)

categoria = st.sidebar.selectbox(
    "Categoría",
    ["Todas"] + categorias
)

if "tipo_palabra" in df_total.columns:

    tipos = sorted(
        df_total["tipo_palabra"]
        .dropna()
        .unique()
        .tolist()
    )

    tipo = st.sidebar.selectbox(
        "Tipo",
        ["Todas"] + tipos
    )
    
    modo_estudio = st.sidebar.selectbox(
    "Modo de estudio",
    [
        "Todo el vocabulario",
        "Solo falladas",
        "Solo dominadas",
        "Solo pendientes",
        "Solo favoritas"
    ]
)   

else:
    tipo = "Todas"

# =====================================================
# FILTROS
# =====================================================

df = df_total.copy()

df = df[
    df["nivel"] == nivel
]

if categoria != "Todas":

    df = df[
        df["categoria"] == categoria
    ]

if (
    "tipo_palabra" in df.columns
    and tipo != "Todas"
):

    df = df[
        df["tipo_palabra"] == tipo
    ]

# =====================================
# FILTRO MODO ESTUDIO
# =====================================

if modo_estudio == "Solo falladas":

    df = df[
        df["fallos"] > 0
    ]

elif modo_estudio == "Solo dominadas":

    if "dominada" in df.columns:

        df = df[
            df["dominada"] == 1
        ]

elif modo_estudio == "Solo pendientes":

    if "dominada" in df.columns:

        df = df[
            df["dominada"] == 0
        ]

elif modo_estudio == "Solo favoritas":

    if "favorita" in df.columns:

        df = df[
            df["favorita"] == 1
        ]

    else:

        st.warning(
            "La columna favorita todavía no existe."
        )

if len(df) == 0:

    st.warning(
        "No hay palabras para los filtros seleccionados."
    )

    st.stop()
    
# =====================================================
# REINICIAR ELEMENTOS AL CAMBIAR FILTROS
# =====================================================

estado_filtros = (
    f"{nivel}|"
    f"{categoria}|"
    f"{tipo}|"
    f"{modo_estudio}"
)

if "filtro_anterior" not in st.session_state:

    st.session_state.filtro_anterior = (
        estado_filtros
    )

if (
    st.session_state.filtro_anterior
    != estado_filtros
):

    for key in [

        "flashcard_actual",
        "flashcard_feedback",

        "articulo_actual",
        "articulo_feedback",

        "traduccion_actual",
        "traduccion_feedback",

        "contexto_actual",

        "frase_actual",
        "frase_feedback"

    ]:

        if key in st.session_state:
            del st.session_state[key]

    st.session_state.filtro_anterior = (
        estado_filtros
    )


# =====================================================
# KPIs
# =====================================================

total_palabras = len(df)

if "dominada" in df.columns:

    dominadas = len(
        df[df["dominada"] == 1]
    )

else:

    dominadas = 0

if "aciertos" in df.columns:

    aciertos = (
        df["aciertos"]
        .fillna(0)
        .sum()
    )

else:

    aciertos = 0

if "fallos" in df.columns:

    fallos = (
        df["fallos"]
        .fillna(0)
        .sum()
    )

else:

    fallos = 0

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "📚 Palabras",
    total_palabras
)

c2.metric(
    "✅ Dominadas",
    dominadas
)

c3.metric(
    "🎯 Aciertos",
    int(aciertos)
)

c4.metric(
    "❌ Fallos",
    int(fallos)
)

# ==========================================
# PROGRESO DEL NIVEL
# ==========================================

if total_palabras > 0:

    progreso = (
        dominadas / total_palabras
    )

    st.write(
        f"Progreso del nivel {nivel}"
    )

    st.progress(progreso)

    st.write(
        f"{dominadas} / {total_palabras} palabras dominadas"
    )

# =====================================================
# PESTAÑAS
# =====================================================

tabs = st.tabs([
    "📖 Estudiar",
    "🎯 Artículos",
    "✍️ Traducción",
    "🧠 Flashcards",
    "💡 Contexto",
    "🧩 Frases",
    "📈 Estadísticas"
])




# =====================================================
# TAB 1 - ESTUDIAR
# =====================================================

with tabs[0]:

    st.header("📖 Estudiar")

    falladas_df = df[
        df["fallos"] > 0
    ].sort_values(
        "fallos",
        ascending=False
    ).head(20)
    
    muestra = pd.concat(
    [
        falladas_df,
        df.sample(
            min(
                20,
                len(df)
            )
        )
    ]
    ).drop_duplicates(
    subset="id"
    )

    colores = {
        "der": "#2196F3",
        "die": "#E91E63",
        "das": "#4CAF50"
    }

    for _, row in muestra.iterrows():
        
        errores = row.get("fallos", 0)

        if errores > 0:
            aviso = f"🔥 {errores} fallos"
        else:
            aviso = ""

        st.markdown(
            f"""
            <div style="
            background-color:white;
            border-radius:15px;
            padding:20px;
            margin-bottom:10px;
            box-shadow:0px 2px 10px rgba(0,0,0,0.1);
            border-left:8px solid {colores.get(row.get('articulo',''),'#999')};
            ">

            <h3 style="color:{colores.get(row.get('articulo',''),'black')}">

            {row.get('articulo','')}
            {row['palabra']}

            </h3>

            <p>{row['espanol']}</p>

            <p style="color:red;">
            {aviso}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# =====================================================
# TAB 2 - ARTÍCULOS
# =====================================================

with tabs[1]:

    st.header("🎯 Artículos")

    sust = df[
        df["articulo"]
        .isin(["der", "die", "das"])
    ]

    if len(sust) > 0:

        # -------------------------------------
        # Inicialización
        # -------------------------------------

        if "articulo_actual" not in st.session_state:

            st.session_state.articulo_actual = (
                sust.sample().iloc[0]
            )

        if "articulo_feedback" not in st.session_state:

            st.session_state.articulo_feedback = None

        fila = st.session_state.articulo_actual

        st.subheader(
            fila["palabra"]
        )

        st.write(
            f"🇪🇸 {fila['espanol']}"
        )

        # Mostrar resultado anterior
        if st.session_state.articulo_feedback:

            tipo, mensaje = (
                st.session_state.articulo_feedback
            )

            if tipo == "success":
                st.success(mensaje)
            else:
                st.error(mensaje)

        respuesta = st.radio(
            "Selecciona el artículo",
            ["der", "die", "das"],
            key="articulo_quiz"
        )

        # -------------------------------------
        # COMPROBAR
        # -------------------------------------

        if st.button(
            "Comprobar",
            key="btn_articulo"
        ):

            conn = sqlite3.connect(
                "datos/aleman.db"
            )

            cursor = conn.cursor()

            if respuesta == fila["articulo"]:

                cursor.execute("""
                UPDATE vocabulario
                SET aciertos = aciertos + 1
                WHERE id = ?
                """, (int(fila["id"]),))

                cursor.execute("""
                UPDATE vocabulario
                SET dominada = 1
                WHERE id = ?
                AND aciertos >= 4
                """, (int(fila["id"]),))

                st.session_state.articulo_feedback = (
                    "success",
                    "✅ Correcto"
                )

            else:

                cursor.execute("""
                UPDATE vocabulario
                SET fallos = fallos + 1
                WHERE id = ?
                """, (int(fila["id"]),))

                st.session_state.articulo_feedback = (
                    "error",
                    f"❌ Correcto: {fila['articulo']}"
                )

            conn.commit()
            conn.close()

            st.cache_data.clear()

            st.rerun()

        # -------------------------------------
        # SIGUIENTE PALABRA
        # -------------------------------------

        if st.button(
            "➡️ Siguiente palabra",
            key="btn_articulo_next"
        ):

            st.session_state.articulo_actual = (
                sust.sample().iloc[0]
            )

            st.session_state.articulo_feedback = None

            st.rerun()

    else:

        st.info(
            "No hay sustantivos en este filtro."
        )

# =====================================================
# TAB 3 - TRADUCCIÓN
# =====================================================

with tabs[2]:

    st.header("✍️ Traducción")

    modo = st.radio(
        "Modo",
        ["DE → ES", "ES → DE"]
    )

    if "traduccion_actual" not in st.session_state:

        st.session_state.traduccion_actual = (
            df.sample().iloc[0]
        )

    if "traduccion_feedback" not in st.session_state:

        st.session_state.traduccion_feedback = None

    fila = st.session_state.traduccion_actual

    # -------------------------------------
    # MODO DE -> ES
    # -------------------------------------

    if modo == "DE → ES":

        correcto = fila["espanol"]

        st.subheader(
            fila["palabra"]
        )

    # -------------------------------------
    # MODO ES -> DE
    # -------------------------------------

    else:

        st.subheader(
            fila["espanol"]
        )

        exigir_articulo = st.checkbox(
            "Exigir artículo en alemán",
            value=True
        )

        articulo = (
            str(fila["articulo"]).strip()
            if pd.notna(fila["articulo"])
            else ""
        )

        if (
            exigir_articulo
            and articulo in ["der", "die", "das"]
        ):

            correcto = (
                f"{articulo} "
                f"{fila['palabra']}"
            )

        else:

            correcto = fila["palabra"]

    # -------------------------------------
    # FEEDBACK
    # -------------------------------------

    if st.session_state.traduccion_feedback:

        tipo, mensaje = (
            st.session_state.traduccion_feedback
        )

        if tipo == "success":

            st.success(
                mensaje
            )

        else:

            st.error(
                mensaje
            )

    # -------------------------------------
    # INPUT
    # -------------------------------------

    respuesta = st.text_input(
        "Respuesta",
        key="traduccion_input"
    )

    # -------------------------------------
    # COMPROBAR
    # -------------------------------------

    if st.button(
        "Comprobar traducción"
    ):

        similitud = fuzz.ratio(
            respuesta.lower().strip(),
            correcto.lower().strip()
        )

        conn = sqlite3.connect(
            "datos/aleman.db"
        )

        cursor = conn.cursor()

        if similitud >= 90:

            cursor.execute("""
            UPDATE vocabulario
            SET aciertos = aciertos + 1
            WHERE id = ?
            """, (int(fila["id"]),))

            cursor.execute("""
            UPDATE vocabulario
            SET dominada = 1
            WHERE id = ?
            AND aciertos >= 4
            """, (int(fila["id"]),))

            st.session_state.traduccion_feedback = (
                "success",
                "✅ Correcto"
            )

        else:

            cursor.execute("""
            UPDATE vocabulario
            SET fallos = fallos + 1
            WHERE id = ?
            """, (int(fila["id"]),))

            st.session_state.traduccion_feedback = (
                "error",
                f"❌ Correcto: {correcto}"
            )

        conn.commit()
        conn.close()

        st.rerun()
    
        # -------------------------------------
    # SIGUIENTE PALABRA
    # -------------------------------------

    if st.button(
        "➡️ Siguiente palabra",
        key="traduccion_next"
    ):

        nueva = df.sample().iloc[0]

        while (
            nueva["id"] == fila["id"]
            and len(df) > 1
        ):

            nueva = df.sample().iloc[0]

        st.session_state.traduccion_actual = nueva

        st.session_state.traduccion_feedback = None

        if "traduccion_input" in st.session_state:
            del st.session_state["traduccion_input"]

        st.rerun()

# =====================================================
# TAB 4 - FLASHCARDS
# =====================================================

with tabs[3]:

    st.header("🧠 Flashcards")

    # Inicialización
    if "flashcard_actual" not in st.session_state:

        st.session_state.flashcard_actual = (
            df.sort_values(
                "fallos",
                ascending=False
            )
            .sample(
                1,
                weights=df["fallos"] + 1
            )
            .iloc[0]
        )

    if "flashcard_counter" not in st.session_state:
        st.session_state.flashcard_counter = 0

    if "flashcard_feedback" not in st.session_state:
        st.session_state.flashcard_feedback = None

    fila = st.session_state.flashcard_actual

    st.subheader(
        f"{fila.get('articulo', '')} {fila['palabra']}"
    )

    # Mostrar feedback anterior
    if st.session_state.flashcard_feedback:

        tipo, mensaje = (
            st.session_state.flashcard_feedback
        )

        if tipo == "success":
            st.success(mensaje)

        elif tipo == "error":
            st.error(mensaje)

    respuesta = st.text_input(
        "Escribe la traducción:",
        key=f"flashcard_input_{st.session_state.flashcard_counter}"
    )

    # -------------------------------------------------
    # COMPROBAR
    # -------------------------------------------------

    if st.button(
        "Comprobar",
        key="flashcard_comprobar"
    ):

        correcto = fila["espanol"]

        similitud = fuzz.ratio(
            respuesta.lower().strip(),
            correcto.lower().strip()
        )

        conn = sqlite3.connect(
            "datos/aleman.db"
        )

        cursor = conn.cursor()

        if similitud >= 90:

            cursor.execute("""
            UPDATE vocabulario
            SET aciertos = aciertos + 1
            WHERE id = ?
            """, (int(fila["id"]),))

            cursor.execute("""
            UPDATE vocabulario
            SET dominada = 1
            WHERE id = ?
            AND aciertos >= 4
            """, (int(fila["id"]),))

            st.session_state.flashcard_feedback = (
                "success",
                "✅ Correcto"
            )

        else:

            cursor.execute("""
            UPDATE vocabulario
            SET fallos = fallos + 1
            WHERE id = ?
            """, (int(fila["id"]),))

            st.session_state.flashcard_feedback = (
                "error",
                f"❌ Correcto: {correcto}"
            )

        conn.commit()
        conn.close()

        st.cache_data.clear()

        st.rerun()

    # -------------------------------------------------
    # SIGUIENTE PALABRA
    # -------------------------------------------------

    if st.button(
        "➡️ Siguiente palabra",
        key="flashcard_next"
    ):

        st.session_state.flashcard_actual = (
            df.sort_values(
                "fallos",
                ascending=False
            )
            .sample(
                1,
                weights=df["fallos"] + 1
            )
            .iloc[0]
        )

        # Nueva key para limpiar el input
        st.session_state.flashcard_counter += 1

        # Limpiar mensajes
        st.session_state.flashcard_feedback = None

        st.rerun()
        
        
        
with tabs[4]:

    st.header("💡 Aprender en contexto")

    ejemplos = df[
        df["ejemplo_de"].notna()
    ]

    ejemplos = ejemplos[
        ejemplos["ejemplo_de"] != ""
    ]

    if len(ejemplos) == 0:

        st.info(
            "Todavía no hay ejemplos disponibles."
        )

    else:

        if "contexto_actual" not in st.session_state:

            st.session_state.contexto_actual = (
                ejemplos.sample().iloc[0]
            )

        fila = st.session_state.contexto_actual

        articulo = (
            str(fila["articulo"])
            if pd.notna(fila["articulo"])
            else ""
        )

        if articulo:

            st.subheader(
                f"{articulo} {fila['palabra']}"
            )

        else:

            st.subheader(
                fila["palabra"]
            )

        st.write(
            f"🇪🇸 {fila['espanol']}"
        )

        st.divider()

        st.markdown(
            f"**🇩🇪 {fila['ejemplo_de']}**"
        )

        if st.checkbox(
            "Mostrar traducción",
            value=True
        ):

            st.markdown(
                f"🇪🇸 {fila['ejemplo_es']}"
            )

        if st.button(
            "➡️ Siguiente ejemplo",
            key="contexto_next"
        ):

            nuevo = (
                ejemplos.sample().iloc[0]
            )

            while (
                nuevo["id"] == fila["id"]
                and len(ejemplos) > 1
            ):

                nuevo = (
                    ejemplos.sample().iloc[0]
                )

            st.session_state.contexto_actual = nuevo

            st.rerun()
        
# =====================================================
# TAB 6 - FRASES
# =====================================================

with tabs[5]:

    st.header("🧩 Completa la frase")

    ejemplos = df[
        df["ejemplo_de"].notna()
    ]

    ejemplos = ejemplos[
        ejemplos["ejemplo_de"] != ""
    ]

    if len(ejemplos) < 3:

        st.info(
            "No hay suficientes ejemplos."
        )

    else:

        # -------------------------------------
        # Inicialización
        # -------------------------------------

        if "frase_actual" not in st.session_state:

            st.session_state.frase_actual = (
                ejemplos.sample().iloc[0]
            )

        if "frase_feedback" not in st.session_state:

            st.session_state.frase_feedback = None

        fila = st.session_state.frase_actual

        palabra_correcta = str(
            fila["palabra"]
        ).strip()

        articulo = (
            str(fila["articulo"]).strip()
            if pd.notna(fila["articulo"])
            else ""
        )

        frase_original = fila["ejemplo_de"]

        # -------------------------------------
        # Mostrar feedback anterior
        # -------------------------------------

        if st.session_state.frase_feedback:

            tipo, mensaje = (
                st.session_state.frase_feedback
            )

            if tipo == "success":

                st.success(mensaje)

            else:

                st.error(mensaje)

            st.info(
                fila["ejemplo_es"]
            )

        # -------------------------------------
        # DIFICULTAD
        # -------------------------------------

        dificultad = st.selectbox(
            "Dificultad",
            [
                "Fácil",
                "Media",
                "Difícil"
            ]
        )

        # =================================================
        # FÁCIL
        # =================================================

        if dificultad == "Fácil":

            # Intentar buscar distractores similares
            if (
                "tipo_palabra" in ejemplos.columns
                and pd.notna(
                    fila["tipo_palabra"]
                )
            ):

                candidatos = ejemplos[
                    (
                        ejemplos["tipo_palabra"]
                        == fila["tipo_palabra"]
                    )
                    &
                    (
                        ejemplos["palabra"]
                        != palabra_correcta
                    )
                ]

            else:

                candidatos = ejemplos[
                    ejemplos["palabra"]
                    != palabra_correcta
                ]

            if len(candidatos) >= 2:

                distractores = (
                    candidatos["palabra"]
                    .sample(2)
                    .tolist()
                )

            else:

                distractores = (
                    ejemplos[
                        ejemplos["palabra"]
                        != palabra_correcta
                    ]["palabra"]
                    .sample(2)
                    .tolist()
                )

            opciones = (
                [palabra_correcta]
                + distractores
            )

            random.shuffle(opciones)

            frase_hueco = frase_original.replace(
                palabra_correcta,
                "__________",
                1
            )

            st.markdown(
                f"### {frase_hueco}"
            )

            respuesta = st.radio(
                "Selecciona la palabra",
                opciones,
                key="frase_facil"
            )

            if st.button(
                "Comprobar",
                key="frase_facil_btn"
            ):

                conn = sqlite3.connect(
                    "datos/aleman.db"
                )

                cursor = conn.cursor()

                if respuesta == palabra_correcta:

                    cursor.execute("""
                    UPDATE vocabulario
                    SET aciertos = aciertos + 1
                    WHERE id = ?
                    """, (
                        int(fila["id"]),
                    ))

                    cursor.execute("""
                    UPDATE vocabulario
                    SET dominada = 1
                    WHERE id = ?
                    AND aciertos >= 4
                    """, (
                        int(fila["id"]),
                    ))

                    st.session_state.frase_feedback = (
                        "success",
                        "✅ Correcto"
                    )

                else:

                    cursor.execute("""
                    UPDATE vocabulario
                    SET fallos = fallos + 1
                    WHERE id = ?
                    """, (
                        int(fila["id"]),
                    ))

                    st.session_state.frase_feedback = (
                        "error",
                        f"❌ Correcto: {palabra_correcta}"
                    )

                conn.commit()
                conn.close()

                st.cache_data.clear()

                st.rerun()

        # =================================================
        # MEDIA
        # =================================================

        elif dificultad == "Media":

            frase_hueco = frase_original.replace(
                palabra_correcta,
                "__________",
                1
            )

            st.markdown(
                f"### {frase_hueco}"
            )

            respuesta = st.text_input(
                "Escribe la palabra",
                key="frase_media"
            )

            if st.button(
                "Comprobar",
                key="frase_media_btn"
            ):

                similitud = fuzz.ratio(
                    respuesta.lower().strip(),
                    palabra_correcta.lower().strip()
                )

                conn = sqlite3.connect(
                    "datos/aleman.db"
                )

                cursor = conn.cursor()

                if similitud >= 90:

                    cursor.execute("""
                    UPDATE vocabulario
                    SET aciertos = aciertos + 1
                    WHERE id = ?
                    """, (
                        int(fila["id"]),
                    ))

                    cursor.execute("""
                    UPDATE vocabulario
                    SET dominada = 1
                    WHERE id = ?
                    AND aciertos >= 4
                    """, (
                        int(fila["id"]),
                    ))

                    st.session_state.frase_feedback = (
                        "success",
                        "✅ Correcto"
                    )

                else:

                    cursor.execute("""
                    UPDATE vocabulario
                    SET fallos = fallos + 1
                    WHERE id = ?
                    """, (
                        int(fila["id"]),
                    ))

                    st.session_state.frase_feedback = (
                        "error",
                        f"❌ Correcto: {palabra_correcta}"
                    )

                conn.commit()
                conn.close()

                st.cache_data.clear()

                st.rerun()

        # =================================================
        # DIFÍCIL
        # =================================================

        else:

            respuesta_correcta = (
                f"{articulo} {palabra_correcta}"
                if articulo in ["der", "die", "das"]
                else palabra_correcta
            )

            frase_hueco = frase_original

            if articulo in ["der", "die", "das"]:

                frase_hueco = frase_hueco.replace(
                    f"{articulo} {palabra_correcta}",
                    "______________",
                    1
                )

            frase_hueco = frase_hueco.replace(
                palabra_correcta,
                "______________",
                1
            )

            st.markdown(
                f"### {frase_hueco}"
            )

            respuesta = st.text_input(
                "Escribe artículo + palabra (ej: das Haus)",
                key="frase_dificil"
            )

            if st.button(
                "Comprobar",
                key="frase_dificil_btn"
            ):

                similitud = fuzz.ratio(
                    respuesta.lower().strip(),
                    respuesta_correcta.lower().strip()
                )

                conn = sqlite3.connect(
                    "datos/aleman.db"
                )

                cursor = conn.cursor()

                if similitud >= 90:

                    cursor.execute("""
                    UPDATE vocabulario
                    SET aciertos = aciertos + 1
                    WHERE id = ?
                    """, (
                        int(fila["id"]),
                    ))

                    cursor.execute("""
                    UPDATE vocabulario
                    SET dominada = 1
                    WHERE id = ?
                    AND aciertos >= 4
                    """, (
                        int(fila["id"]),
                    ))

                    st.session_state.frase_feedback = (
                        "success",
                        "✅ Correcto"
                    )

                else:

                    cursor.execute("""
                    UPDATE vocabulario
                    SET fallos = fallos + 1
                    WHERE id = ?
                    """, (
                        int(fila["id"]),
                    ))

                    st.session_state.frase_feedback = (
                        "error",
                        f"❌ Correcto: {respuesta_correcta}"
                    )

                conn.commit()
                conn.close()

                st.cache_data.clear()

                st.rerun()

        # =================================================
        # SIGUIENTE FRASE
        # =================================================

        if st.button(
            "➡️ Siguiente frase",
            key="next_frase"
        ):

            nuevo = (
                ejemplos.sample().iloc[0]
            )

            while (
                nuevo["id"] == fila["id"]
                and len(ejemplos) > 1
            ):

                nuevo = (
                    ejemplos.sample().iloc[0]
                )

            st.session_state.frase_actual = nuevo

            st.session_state.frase_feedback = None

            for key in [
                "frase_media",
                "frase_dificil"
            ]:

                if key in st.session_state:
                    del st.session_state[key]

            st.rerun()
      
        
# =====================================================
# TAB 7 - ESTADÍSTICAS
# =====================================================

with tabs[6]:

    st.header("📈 Estadísticas")

    # Resumen
    total_palabras = len(df)

    dominadas = len(
        df[df["dominada"] == 1]
    )

    pendientes = len(
        df[df["dominada"] == 0]
    )

    aciertos = int(
        df["aciertos"]
        .fillna(0)
        .sum()
    )

    fallos = int(
        df["fallos"]
        .fillna(0)
        .sum()
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "📚 Palabras",
        total_palabras
    )

    c2.metric(
        "✅ Dominadas",
        dominadas
    )

    c3.metric(
        "🎯 Aciertos",
        aciertos
    )

    c4.metric(
        "❌ Fallos",
        fallos
    )

    # Barra progreso

    if total_palabras > 0:

        progreso = dominadas / total_palabras

        st.subheader(
            f"Progreso {nivel}"
        )

        st.progress(progreso)

        st.write(
            f"{dominadas}/{total_palabras} palabras dominadas"
        )

    st.divider()

    # Gráfico dominadas vs pendientes

    estado_df = pd.DataFrame({

        "Estado": [
            "Dominadas",
            "Pendientes"
        ],

        "Cantidad": [
            dominadas,
            pendientes
        ]

    })

    fig = px.pie(
        estado_df,
        names="Estado",
        values="Cantidad",
        title="Progreso de aprendizaje"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # Top palabras más falladas

    top_fallos = (
        df.sort_values(
            "fallos",
            ascending=False
        )
        .head(10)
    )

    if len(top_fallos) > 0:

        fig2 = px.bar(
            top_fallos,
            x="palabra",
            y="fallos",
            title="Top 10 palabras más falladas"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )
