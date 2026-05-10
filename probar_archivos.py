from archivos import ArchivoProcesador

def prueba_real():
    procesador = ArchivoProcesador()
    print("--- 📂 PROBANDO CON ARCHIVOS MANUALES ---")

    # Intenta leer el archivo que ya creaste (en la misma carpeta)
    archivo_usuario = "locura.txt"
    
    resultado = procesador.procesar_archivo_entrada(archivo_usuario)
    print(f"Resultado: {resultado}")

    if "tipo" in resultado:
        print(f"✅ Lectura exitosa")
        print(f"   Tipo detectado: {resultado['tipo']}")
        print(f"   Lo que dice el archivo: {resultado['contenido']}")
    else:
        print(f"❌ El motor no pudo leerlo: {resultado.get('mensaje')}")

if __name__ == "__main__":
    prueba_real()