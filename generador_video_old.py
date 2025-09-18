import moviepy.editor as mp
import os
import webbrowser
from datetime import datetime

class GeneradorVideo:
    def __init__(self):
        self.output_dir = "outputs"
        self._crear_carpeta()
    
    def _crear_carpeta(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def generar(self, prompt):
        try:
            print("🎥 Generando video...")
            
            # Crear un video simple con texto
            txt_clip = mp.TextClip(
                prompt, 
                fontsize=24, 
                color='white', 
                size=(640, 480),
                bg_color='black'
            )
            txt_clip = txt_clip.set_duration(5)  # 5 segundos
            
            # Crear nombre único
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"video_{timestamp}.mp4"
            output_path = os.path.join(self.output_dir, filename)
            
            # Guardar video
            txt_clip.write_videofile(
                output_path, 
                fps=24,
                verbose=False,
                logger=None
            )
            
            print(f"✅ Video guardado: {output_path}")
            
            # Abrir automáticamente
            webbrowser.open(output_path)
            
            return output_path
            
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            print(error_msg)
            return error_msg