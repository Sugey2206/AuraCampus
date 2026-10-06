from google import genai
from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO
import pypdf

def extract_pdf_text(uploaded_file):
    pdf_reader = pypdf.PdfReader(BytesIO(uploaded_file.read()))
    text = ""
    for page in pdf_reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text

def get_system_prompt_by_tone(tone):
    if "Cálido" in tone:
        return "Eres Aura, una mentora muy cálida, paciente, cercana y motivadora. Explicas sin abrumar y das aliento al estudiante o escritor."
    elif "Socrático" in tone:
        return "Eres un tutor socrático. Guías mediante preguntas clave para estimular el pensamiento crítico y la creatividad."
    else:
        return "Eres un consultor riguroso, formal y preciso experto en metodología académica y literatura."

def run_gemini(api_key, prompt, pdf_file=None, tone="Cálido y Motivador 🌸"):
    client = genai.Client(api_key=api_key)
    context = ""
    if pdf_file is not None:
        pdf_text = extract_pdf_text(pdf_file)
        context = f"\n\n[CONTENIDO DEL PDF]:\n{pdf_text[:10000]}\n\n"
    
    system_instruction = get_system_prompt_by_tone(tone)
    full_prompt = f"{system_instruction}\n{context}\nConsulta: {prompt}"
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )
    return response.text

def run_book_writing_assistant(api_key, story_input):
    """Módulo especializado para la creación de libros y bloqueo escritor."""
    client = genai.Client(api_key=api_key)
    prompt = (
        "Eres un mentor literario empático de Aura Campus. Ayuda al usuario a continuar su libro u obra. "
        f"Idea/Texto actual: '{story_input}'. Proporciona: 1) Sugerencias para desbloquear la trama, "
        "2) Ideas para el desarrollo de personajes o giros narrativos, 3) Un borrador con la continuidad de la escena."
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def run_media_script_builder(api_key, media_type, topic):
    """Generador de guiones para Videos, Canva, Pitch e Exposiciones."""
    client = genai.Client(api_key=api_key)
    prompt = (
        f"Crea una estructura completa y guión profesional para {media_type} sobre el tema: '{topic}'. "
        "Incluye: 1) Estructura paso a paso por diapositivas o escenas, 2) Texto exacto a decir (guión de voz), "
        "3) Sugerencias visuales/prompts para diseñar las diapositivas o plantillas en Canva."
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def run_web_builder(api_key, topic_description):
    client = genai.Client(api_key=api_key)
    prompt = (
        f"Crea el código completo de una página web en HTML y CSS integrado (con un diseño limpio, colores pastel y responsive) "
        f"para el siguiente proyecto universitario: {topic_description}. Entrega solo el código funcional dentro de un bloque HTML."
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def run_wellness_support(api_key, user_feeling):
    client = genai.Client(api_key=api_key)
    prompt = (
        "Eres el espacio de Bienestar Emocional de Aura Campus. Un estudiante te comparte lo que siente: "
        f"'{user_feeling}'. Ofrece palabras de validación emocional, un consejo práctico y empático para el entorno universitario "
        "y una técnica breve de relajación o manejo del estrés/ansiedad."
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def generate_image(prompt, width=1024, height=1024, seed=42):
    prompt_encoded = requests.utils.quote(prompt)
    url = f"https://pollinations.ai/p/{prompt_encoded}?width={width}&height={height}&seed={seed}"
    response = requests.get(url, timeout=30)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content)), response.content
    else:
        raise Exception("Error al generar la imagen.")
