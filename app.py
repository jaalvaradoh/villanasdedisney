import streamlit as st
import random

st.set_page_config(page_title="Trivia Villanas Disney", page_icon="👑")

st.title("👑 Trivia: Villanas de Disney")

# Preguntas
preguntas = [
    {
        "pregunta": "¿Cómo se llama la villana de La Sirenita?",
        "opciones": ["Úrsula", "Maléfica", "Cruella", "Reina Malvada"],
        "respuesta": "Úrsula"
    },
    {
        "pregunta": "¿Qué villana odia a los dálmatas?",
        "opciones": ["Cruella de Vil", "Gothel", "Maléfica", "Yzma"],
        "respuesta": "Cruella de Vil"
    },
    {
        "pregunta": "¿Quién es la villana de Enredados?",
        "opciones": ["Madre Gothel", "Úrsula", "Reina Malvada", "Lady Tremaine"],
        "respuesta": "Madre Gothel"
    },
    {
        "pregunta": "¿Qué villana se convierte en dragón?",
        "opciones": ["Maléfica", "Cruella", "Úrsula", "Yzma"],
        "respuesta": "Maléfica"
    },
    {
        "pregunta": "¿Quién es la villana principal de Blancanieves?",
        "opciones": ["Reina Malvada", "Maléfica", "Gothel", "Cruella"],
        "respuesta": "Reina Malvada"
    }
]

# Inicializar estado
if "preguntas_mezcladas" not in st.session_state:
    st.session_state.preguntas_mezcladas = []
    for p in preguntas:
        opciones = p["opciones"].copy()
        random.shuffle(opciones)
        st.session_state.preguntas_mezcladas.append({
            "pregunta": p["pregunta"],
            "opciones": opciones,
            "respuesta": p["respuesta"]
        })

if "respuestas" not in st.session_state:
    st.session_state.respuestas = {}

# Mostrar preguntas
st.subheader("Responde las 5 preguntas:")

for i, p in enumerate(st.session_state.preguntas_mezcladas):
    st.session_state.respuestas[i] = st.radio(
        p["pregunta"],
        p["opciones"],
        key=f"pregunta_{i}"
    )

# Botón para verificar
if st.button("Verificar respuestas"):
    correctas = 0

    for i, p in enumerate(st.session_state.preguntas_mezcladas):
        if st.session_state.respuestas.get(i) == p["respuesta"]:
            correctas += 1

    st.write(f"✅ Respuestas correctas: {correctas}/5")

    if correctas == 5:
        st.balloons()
        st.success("🎉 ¡Perfecto! ¡Acertaste todas!")
    else:
        st.warning("😅 ¡Sigue intentando!")

# Botón para reiniciar
if st.button("Reiniciar juego"):
    st.session_state.clear()
    st.rerun()
