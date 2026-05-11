from google import genai
from PIL import Image
from gtts import gTTS

API_KEY = "TU_API_KEY_AQUI"

client = genai.Client(api_key=API_KEY)

def preguntar_ia(texto):

    respuesta = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=texto
    )

    return respuesta.text

def analizar_imagen(ruta_imagen, pregunta="Describe esta imagen"):

    imagen = Image.open(ruta_imagen)

    respuesta = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            pregunta,
            imagen
        ]
    )

    return respuesta.text

def analizar_archivo(ruta_archivo):

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    prompt = f"""
    Analiza este archivo:

    {contenido}
    """

    respuesta = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return respuesta.text

def generar_audio(texto, nombre_audio="respuesta.mp3"):

    tts = gTTS(text=texto, lang="es")

    tts.save(nombre_audio)

    print(f"Audio guardado en: {nombre_audio}")

def chat():
#centr
    print("===================================")
    print("CHAT GEMINI IA")
    print("Escribe 'salir' para terminar")
    print("===================================")

    chat = client.chats.create(
        model="gemini-2.0-flash"
    )

    while True:

        mensaje = input("\nTú: ")

        if mensaje.lower() == "salir":
            break

        respuesta = chat.send_message(mensaje)

        texto_respuesta = respuesta.text

        print("\nGemini:", texto_respuesta)

        opcion_audio = input("\n¿Generar audio? (s/n): ")

        if opcion_audio.lower() == "s":
            generar_audio(texto_respuesta)

def menu():

    while True:

        print("\n==============================")
        print("1. Preguntar a Gemini")
        print("2. Analizar Imagen")
        print("3. Analizar Archivo")
        print("4. Chat Continuo")
        print("5. Salir")
        print("==============================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            pregunta = input("\nEscribe tu pregunta: ")

            respuesta = preguntar_ia(pregunta)

            print("\nRespuesta:\n")
            print(respuesta)

            guardar_audio = input("\n¿Guardar audio? (s/n): ")

            if guardar_audio.lower() == "s":
                generar_audio(respuesta)

        elif opcion == "2":

            ruta = input("\nRuta de la imagen: ")

            pregunta = input(
                "Pregunta sobre la imagen (vacío = describir): "
            )

            if pregunta.strip() == "":
                pregunta = "Describe esta imagen"

            respuesta = analizar_imagen(ruta, pregunta)

            print("\nRespuesta:\n")
            print(respuesta)

        elif opcion == "3":

            ruta = input("\nRuta del archivo: ")

            respuesta = analizar_archivo(ruta)

            print("\nRespuesta:\n")
            print(respuesta)

        elif opcion == "4":

            chat()

        elif opcion == "5":

            print("\nPrograma finalizado")
            break

        else:

            print("\nOpción inválida")

if _name_ == "_main_":
    menu()