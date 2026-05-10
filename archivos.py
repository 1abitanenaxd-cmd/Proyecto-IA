import os
from pathlib import Path

class ArchivoProcesador:
    """
    Procesador universal: Extrae texto de documentos o prepara imágenes/PDFs para la IA.
    """
    def __init__(self):
        # Asegúrate de que estos nombres coincidan abajo
        self.formatos_texto = ['.txt', '.py', '.md', '.csv']
        self.formatos_word = ['.docx']
        self.formatos_visuales = ['.jpg', '.jpeg', '.png', '.pdf']
        
        self.carpeta_salida = Path("archivos_creados")
        self.carpeta_salida.mkdir(parents=True, exist_ok=True)

    def procesar_archivo_entrada(self, ruta_entrada):
        try:
            archivo = Path(ruta_entrada)
            ext = archivo.suffix.lower()

            # CORRECCIÓN: Usamos 'formatos_texto' en plural
            if ext in self.formatos_texto:
                return {"tipo": "texto", "contenido": archivo.read_text(encoding='utf-8')}

            elif ext in self.formatos_word:
                return {"tipo": "texto", "contenido": self._leer_word(archivo)}

            elif ext in self.formatos_visuales:
                mime = "application/pdf" if ext == ".pdf" else f"image/{ext[1:]}"
                return {
                    "tipo": "binario",
                    "tipo_mime": mime,
                    "datos": archivo.read_bytes()
                }
            else:
                return {"estado": "error", "mensaje": "Este formato no lo conozco."}

        except Exception as e:
            return {"estado": "error", "mensaje": f"Error al leer: {e}"}

    def crear_archivo_de_respuesta(self, texto_ia, nombre_final):
        try:
            ruta = self.carpeta_salida / nombre_final
            # CORRECCIÓN: 'encoding' sin la N extra
            ruta.write_text(texto_ia, encoding='utf-8')
            return {"estado": "exito", "ruta": str(ruta)}
        except Exception as e:
            return {"estado": "error", "mensaje": str(e)}

    def _leer_word(self, ruta):
        try:
            from docx import Document
            doc = Document(ruta)
            return "\n".join([p.text for p in doc.paragraphs])
        except Exception: return "Error en Word"
