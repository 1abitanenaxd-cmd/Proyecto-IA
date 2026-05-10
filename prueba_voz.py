from audio import AudioProcesador  # Asegúrate que el archivo se llame motor_voz.py

def test_motor():
    # 1. Inicializamos el motor
    mi_voz = AudioProcesador(idioma_defecto="es")
    print("--- Iniciando prueba de MotorVoz ---")

    # 2. Probamos generar un audio en español
    resultado_es = mi_voz.generar_voz("Hola, esto es una prueba de mi motor de voz en español.")
    
    if resultado_es["estado"] == "exito":
        print(f"✅ ¡Éxito! Audio guardado en: {resultado_es['ruta']}")
        print(f"   Detalles: {resultado_es['info']}")
    else:
        print(f"❌ Error: {resultado_es['mensaje']}")

    # 3. Probamos la capacidad multilingüe (Inglés)
    print("\n--- Probando cambio de idioma ---")
    resultado_en = mi_voz.generar_voz("Hello, I can also speak English very well.", idioma="en")
    
    if resultado_en["estado"] == "exito":
        print(f"✅ ¡Éxito! Audio en inglés guardado: {resultado_en['ruta']}")
    
    # 4. Probamos el manejo de errores (Simulando un idioma que no existe)
    print("\n--- Probando manejo de excepciones ---")
    resultado_error = mi_voz.generar_voz("Prueba error", idioma="idioma-falso")
    print(f"Nota: El motor respondió: {resultado_error['mensaje']}")

if __name__ == "__main__":
    test_motor()