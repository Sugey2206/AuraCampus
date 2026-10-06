import streamlit as st

# 1. Configuración de página (debe ir antes de cualquier otro comando de Streamlit)
st.set_page_config(
    page_title="Aura Campus",
    page_icon="logo.jpg",
    layout="wide",
    initial_sidebar_state="expanded"
)

from config import setup_page
from modules import (
    run_gemini, run_book_writing_assistant, run_media_script_builder, 
    run_web_builder, run_wellness_support, generate_image
)

# Ejecución opcional de estilos extra si setup_page los incluye
setup_page()

st.markdown("""
    <div class="main-header">
        🌿 Aura Campus
        <div style="font-size: 1rem; font-weight: 400; color: #556b2f; margin-top: 5px;">
            Tu espacio de aprendizaje, bienestar, creatividad y conexión estudiantil
        </div>
    </div>
""", unsafe_allow_html=True)

# 2. Barra Lateral
st.sidebar.header("🎛️ Panel de Control")
selected_tone = st.sidebar.selectbox(
    "Selecciona el Tono del Asistente:",
    ["Cálido y Motivador 🌸", "Socrático & Reflexivo 💡", "Tesis & Riguroso 🎓"]
)

st.sidebar.markdown("---")
st.sidebar.header("🔑 Claves de Acceso")
gemini_key = st.sidebar.text_input("Google Gemini API Key", type="password")

# 3. Pestañas Principales Integradas
(
    tab_gemini, tab_writing, tab_media, 
    tab_thesis, tab_web, tab_visual, 
    tab_wellness, tab_profile
) = st.tabs([
    "⚡ Análisis & PDFs", 
    "✍️ Taller de Libros", 
    "🎬 Canva & Guiones", 
    "📜 Tesis", 
    "🌐 Creador Web", 
    "🎨 Portadas", 
    "💚 Bienestar", 
    "📊 Mi Espacio"
])

# --- TAB 1: GEMINI & PDFS ---
with tab_gemini:
    st.header("⚡ Análisis de Documentos & Resúmenes")
    uploaded_pdf = st.file_uploader("Carga tu guía o PDF de clase:", type=["pdf"])
    prompt_gemini = st.text_area("¿Qué deseas hacer?", placeholder="Ej: Hazme un resumen en tabla comparativa de los conceptos principales.")
    
    if st.button("Procesar Consulta", type="primary"):
        if not gemini_key:
            st.error("Ingresa tu API Key de Gemini en la barra lateral.")
        else:
            with st.spinner("Procesando..."):
                try:
                    res = run_gemini(gemini_key, prompt_gemini, uploaded_pdf, tone=selected_tone)
                    st.markdown("### 📋 Respuesta:")
                    st.markdown(res)
                except Exception as e:
                    st.error(f"Error: {e}")

# --- TAB 2: TALLER DE LIBROS Y ESCRITURA ---
with tab_writing:
    st.header("✍️ Taller Literario & Bloqueo Escritor")
    st.write("Un asistente creativo para ayudarte a escribir libros, historias, personajes y superar el bloqueo del lienzo en blanco.")
    story_input = st.text_area("Cuéntame tu idea, capítulo actual o en qué parte te quedaste estancado:", placeholder="Ej: Mi personaje principal acaba de descubrir un secreto en el capítulo 3 pero no sé cómo continuar la conversación...")
    
    if st.button("Desbloquear & Continuar Libro"):
        if not gemini_key:
            st.error("Ingresa tu API Key de Gemini.")
        else:
            with st.spinner("Generando inspiración literaria..."):
                try:
                    book_res = run_book_writing_assistant(gemini_key, story_input)
                    st.markdown("### 📖 Sugerencia Narrativa:")
                    st.markdown(book_res)
                except Exception as e:
                    st.error(f"Error: {e}")

# --- TAB 3: CANVA & GUIONES PARA VIDEOS ---
with tab_media:
    st.header("🎬 Creador de Guiones para Canva & Videos")
    st.write("Genera la estructura, el guión de voz y las ideas visuales para tus presentaciones o videos académicos.")
    media_type = st.selectbox("Tipo de contenido:", ["Presentación en Canva / Diapositivas", "Video de Exposición / Video Presentación", "Pitch / Discurso Corto"])
    topic_media = st.text_area("Tema o proyecto a presentar:", placeholder="Ej: Presentación para la materia de Comunicación sobre habilidades de expresión oral.")
    
    if st.button("Generar Guión & Prompts para Canva"):
        if not gemini_key:
            st.error("Ingresa tu API Key de Gemini.")
        else:
            with st.spinner("Diseñando guión y diapositivas..."):
                try:
                    media_res = run_media_script_builder(gemini_key, media_type, topic_media)
                    st.markdown("### 📽️ Guión y Estructura:")
                    st.markdown(media_res)
                except Exception as e:
                    st.error(f"Error: {e}")

# --- TAB 4: TESIS ---
with tab_thesis:
    st.header("📜 Asistente Metodológico de Tesis")
    thesis_input = st.text_area("Plantea la sección de tu tesis a revisar:", placeholder="Ej: Redacción del Marco Teórico sobre investigación cualitativa.")
    
    if st.button("Revisar Tesis"):
        if not gemini_key:
            st.error("Ingresa tu API Key de Gemini.")
        else:
            with st.spinner("Revisando metodología..."):
                try:
                    res = run_gemini(gemini_key, f"Tesis: {thesis_input}", tone="Tesis & Riguroso 🎓")
                    st.markdown("### 🎓 Sugerencia:")
                    st.markdown(res)
                except Exception as e:
                    st.error(f"Error: {e}")

# --- TAB 5: CREADOR WEB ---
with tab_web:
    st.header("🌐 Creador Web")
    web_prompt = st.text_area("Describe el sitio web que deseas:", placeholder="Ej: Sitio web para un proyecto sobre paradigmas de investigación.")
    
    if st.button("Generar Código Web"):
        if not gemini_key:
            st.error("Ingresa tu API Key de Gemini.")
        else:
            with st.spinner("Generando código..."):
                try:
                    code_res = run_web_builder(gemini_key, web_prompt)
                    st.code(code_res, language="html")
                except Exception as e:
                    st.error(f"Error: {e}")

# --- TAB 6: PORTADAS ---
with tab_visual:
    st.header("🎨 Creador de Portadas Relajantes")
    prompt_img = st.text_area("Descripción visual:", placeholder="Ej: Aesthetic minimal cover, mint green leaves, soft light pastel background")
    
    if st.button("Generar Diseño"):
        if not prompt_img.strip():
            st.warning("Escribe una descripción.")
        else:
            with st.spinner("Creando ilustración..."):
                try:
                    img_pil, img_bytes = generate_image(prompt_img)
                    st.image(img_pil, caption="Resultado", use_container_width=True)
                    st.download_button("📥 Descargar", data=img_bytes, file_name="portada_aura.png", mime="image/png")
                except Exception as e:
                    st.error(f"Error: {e}")

# --- TAB 7: BIENESTAR ---
with tab_wellness:
    st.header("💚 Bienestar Emocional")
    feeling_input = st.text_area("¿Cómo te sientes hoy?", placeholder="Ej: Mañana expongo y siento mucha ansiedad.")
    
    if st.button("Recibir Apoyo"):
        if not gemini_key:
            st.error("Ingresa tu API Key de Gemini.")
        else:
            with st.spinner("Cargando apoyo..."):
                try:
                    wellness_res = run_wellness_support(gemini_key, feeling_input)
                    st.markdown(wellness_res)
                except Exception as e:
                    st.error(f"Error: {e}")

# --- TAB 8: MI ESPACIO ---
with tab_profile:
    st.header("📊 Mi Espacio & Cursos")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📌 Mis Objetivos")
        st.checkbox("Avanzar 2 páginas de mi libro / tesis")
        st.checkbox("Practicar guión de exposición")
        st.checkbox("Pausa activa y respiración")
    with col2:
        st.subheader("📚 Cursos Recomendados")
        st.info("💡 **Redacción Literaria Creativa**")
        st.info("💡 **Diseño Visual en Canva para Exposiciones**")
        st.image("logo.jpg", use_container_width=True)

