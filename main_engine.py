# main_engine.py

# Importas el trabajo de tus compañeros y el tuyo
from archivos import ArchivoProcesador
from audio import AudioProcesador
from utils import UtilsManager

class MotorLibreriaIA:
    def __init__(self):
        # Inicializas las herramientas de los 3
        self.procesador_archivos = ArchivoProcesador()
        self.procesador_audio = AudioProcesador()
        self.utils = UtilsManager()
        
    def procesar_solicitud_completa(self, ruta_archivo, idioma_audio="es"):
        """
        Esta es la función maestra que el usuario final llamará.
        """
        # 1. Tu compañero saca el texto del archivo
        datos_archivo = self.procesador_archivos.procesar_archivo_entrada(ruta_archivo)
        
        if datos_archivo["estado"] == "error":
            return datos_archivo["mensaje"]
            
        texto_crudo = datos_archivo["contenido"]
        
        # 2. TÚ limpias los datos (Seguridad Regex)
        texto_limpio = self.utils.anonimizar_texto(texto_crudo)
        
       # 3. LLAMADA REAL A LA API DE LA IA (El cerebro del proyecto)
        import requests 
        
        # OJO: Esta URL y formato dependen de si usan OpenAI, Gemini u otra. 
        # Este es el estándar más común (estilo OpenAI):
        url_api = "https://api.openai.com/v1/chat/completions"
        tu_api_key = "AQUI_PONES_EL_TOKEN_QUE_LES_DIO_EL_DOCENTE" # O lo sacas del .env
        
        headers = {
            "Authorization": f"Bearer {tu_api_key}",
            "Content-Type": "application/json"
        }
        
        datos_json = {
            "model": "gpt-3.5-turbo", # O el modelo que estén usando
            "messages": [{"role": "user", "content": texto_limpio}]
        }
        
        try:
            # Hacemos la petición POST (mandamos los datos)
            respuesta = requests.post(url_api, headers=headers, json=datos_json)
            respuesta.raise_for_status() # Verifica si hubo error de conexión
            
            # Sacamos el texto útil del JSON gigante que nos devuelve
            datos_ia = respuesta.json()
            respuesta_ia = datos_ia["choices"][0]["message"]["content"]
            
        except requests.exceptions.RequestException as e:
            return {"error": f"Falló la conexión con la IA: {e}"}
          
        # 4. TÚ limpias la respuesta de la IA
        texto_final = self.utils.extraer_texto_relevante(respuesta_ia)
        
        # 5. El otro compañero genera el MP3
        # Usas tu función para que no se sobreescriba el audio
        nombre_audio = self.utils.generar_nombre_unico("audio", ".mp3")
        resultado_audio = self.procesador_audio.generar_voz(texto_final, idioma_audio)
        
        # 6. Devuelves el resultado final
        return {
            "texto_procesado": texto_final,
            "ruta_audio": resultado_audio.get("ruta", "Error de audio")
        }
