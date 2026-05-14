import re
import hashlib
from datetime import datetime

class UtilsManager:
    """
    Herramientas de limpieza, seguridad, organización y control de IA.
    """
    def __init__(self):
        pass

    # 1. LIMPIEZA DE DATOS Y PRIVACIDAD
    def anonimizar_texto(self, texto):
        if not isinstance(texto, str):
            return texto
            
        texto_limpio = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '[CORREO OCULTO]', texto)
        texto_limpio = re.sub(r'\b\d{7,10}\b', '[NUMERO OCULTO]', texto_limpio)
        return texto_limpio

    def extraer_texto_relevante(self, texto_ia):
        texto_limpio = texto_ia.replace("```json", "").replace("```", "").strip()
        return texto_limpio

    # 2. GESTIÓN DE ARCHIVOS (Evita que se borren los mp3)
    def generar_nombre_unico(self, prefijo="archivo", extension=".txt"):
        ahora = datetime.now().strftime("%Y%m%d_%H%M%S")
        hash_random = hashlib.md5(str(datetime.now().microsecond).encode()).hexdigest()[:6]
        return f"{prefijo}_{ahora}_{hash_random}{extension}"

    # 3. SEGURIDAD DE ARCHIVOS
    def es_archivo_seguro(self, nombre_archivo):
        extensiones_prohibidas = ['.exe', '.bat', '.cmd', '.sh']
        for ext in extensiones_prohibidas:
            if nombre_archivo.lower().endswith(ext):
                return False
        return True

    # 4. TRADUCCIÓN
    def preparar_prompt_traduccion(self, texto, idioma_destino):
        texto_limpio = self.anonimizar_texto(texto)
        prompt = f"Traduce el siguiente texto al {idioma_destino}. Solo devuelve la traducción, nada más:\n\n{texto_limpio}"
        return prompt

    # 5. INGENIERÍA DE PROMPTS (¡LA NUEVA HERRAMIENTA QUE AGREGASTE!)
    def preparar_prompt_estricto(self, texto_usuario):
        instruccion_oculta = (
            "Instrucción estricta: Responde de forma extremadamente concreta, "
            "directa y concisa. No des saludos, no te despidas, y no des "
            "explicaciones innecesarias. Ve directo a la respuesta útil.\n\n"
        )
        prompt_final = instruccion_oculta + "Consulta del usuario: " + texto_usuario
        return prompt_final
