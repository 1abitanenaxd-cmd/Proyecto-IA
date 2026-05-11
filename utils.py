import re
import hashlib
from datetime import datetime

class UtilsManager:
    """
    Herramientas de limpieza, seguridad y organización para la librería IA.
    """
    def __init__(self):
        pass

    # 1. LIMPIEZA DE DATOS Y EXPRESIONES REGULARES (REGEX)
    def anonimizar_texto(self, texto):
        """
        Usa Regex para esconder datos sensibles antes de mandarlos a la IA.
        """
        if not isinstance(texto, str):
            return texto
            
        # Ocultar correos electrónicos
        texto_limpio = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '[CORREO OCULTO]', texto)
        
        # Ocultar números de teléfono o carnets (ej. 8 dígitos seguidos)
        texto_limpio = re.sub(r'\b\d{7,10}\b', '[NUMERO OCULTO]', texto_limpio)
        
        return texto_limpio

    def extraer_texto_relevante(self, texto_ia):
        """
        A veces la IA responde con basura extra como ```json ... ```. 
        Esto limpia la respuesta para sacar solo lo útil.
        """
        texto_limpio = texto_ia.replace("```json", "").replace("```", "").strip()
        return texto_limpio

    # 2. GESTIÓN DE ARCHIVOS (NOMBRES ÚNICOS)
    def generar_nombre_unico(self, prefijo="archivo", extension=".txt"):
        """
        Genera un nombre que NUNCA se va a repetir usando fecha, hora y un hash.
        Ideal para que audio.py no sobreescriba sus mp3.
        """
        # Saca la fecha y hora exacta (ej: 20260511_103015)
        ahora = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Crea un hash aleatorio cortito
        hash_random = hashlib.md5(str(datetime.now().microsecond).encode()).hexdigest()[:6]
        
        # Resultado: audio_20260511_103015_a1b2c3.mp3
        return f"{prefijo}_{ahora}_{hash_random}{extension}"

    # 3. VALIDACIÓN DE ARCHIVOS
    def es_archivo_seguro(self, nombre_archivo):
        """
        Una doble validación de seguridad por si acaso.
        """
        extensiones_prohibidas = ['.exe', '.bat', '.cmd', '.sh']
        for ext in extensiones_prohibidas:
            if nombre_archivo.lower().endswith(ext):
                return False
        return True
