import os 
from pathlib import Path

class AudioProcesador:
    
    def __init__(self, idioma_defecto='es'):
        self.idioma_defecto = idioma_defecto
        self.carpeta_salida = Path("audios_procesados")
        self.carpeta_salida.mkdir(parents=True, exist_ok=True)

    def generar_voz(self, texto, idioma=None):
        idioma_final = idioma or self.idioma_defecto
        nombre_archivo = f"respuesta_{idioma_final}.mp3"
        ruta_archivo = self.carpeta_salida / nombre_archivo

        try:
            from gtts import gTTS

            tts = gTTS(text=texto, lang=idioma_final, slow=False)
            tts.save(str(ruta_archivo))
            return {
                "estado": "exito",
                "ruta": str(ruta_archivo),
                "info": {"idioma": idioma_final, "tamaño_texto": len(texto)}   
            }
        except Exception as error:
            return {
                "estado": "error",
                "mensaje": f"Hubo un problema con gTTS: {error}"
            }
    def cargar_audio(self, ruta_archivo):
        try:
            archivo = Path(ruta_archivo)
            return {
                "estado": "exito",
                "contenido": "audio/mp4",
                "info": archivo.read_bytes()
                         
            }
        except FileNotFoundError:
            return {"estado": "error", "mensaje": "No se encontro el archivo de audio."}
        except Exception as error:
            return {"estado": "error", "mensaje": str(error)}
