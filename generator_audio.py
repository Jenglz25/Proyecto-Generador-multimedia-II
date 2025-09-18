from gtts import gTTS
import os
import webbrowser
from datetime import datetime
import pygame
import time

class GeneradorAudio:
    def __init__(self):
        self.output_dir = "outputs"
        self._crear_carpeta()
        pygame.mixer.init()
    
    def _crear_carpeta(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def generar(self, prompt):
        try:
            print("🎵 Generando audio...")
            
            # Generar audio con Google TTS (gratuito)
            tts = gTTS(text=prompt, lang='es', slow=False)
            
            # Crear nombre único
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"audio_{timestamp}.mp3"
            output_path = os.path.join(self.output_dir, filename)
            
            # Guardar archivo
            tts.save(output_path)
            
            print(f"✅ Audio guardado: {output_path}")
            
            # Reproducir automáticamente
            self._reproducir_audio(output_path)
            
            return output_path
            
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            print(error_msg)
            return error_msg
    
    def _reproducir_audio(self, path):
        try:
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
            print("🔊 Reproduciendo audio...")
        except Exception as e:
            print(f"❌ Error reproduciendo audio: {e}")