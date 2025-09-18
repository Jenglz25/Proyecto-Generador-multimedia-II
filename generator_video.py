import moviepy.editor as mp
import os
import webbrowser
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import numpy as np

class GeneradorVideo:
    def __init__(self):
        self.output_dir = "outputs"
        self._crear_carpeta()
    
    def _crear_carpeta(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def _crear_frame(self, texto, size=(640,480), bg_color="black", text_color="white"):
        # Crear una imagen con fondo
        img = Image.new("RGB", size, bg_color)
        draw = ImageDraw.Draw(img)
        
        try:
            font = ImageFont.truetype("arial.ttf", 32)
        except:
            font = ImageFont.load_default()
        
        # Calcular tamaño del texto usando textbbox
        bbox = draw.textbbox((0,0), texto, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        
        # Dibujar el texto centrado
        draw.text(((size[0]-w)/2, (size[1]-h)/2), texto, font=font, fill=text_color)
        
        return np.array(img)

    def generar(self, prompt):
        try:
            print("🎥 Generando video...")

            # Crear un clip con el texto
            frame = self._crear_frame(prompt)
            clip = mp.ImageClip(frame).set_duration(5)  # duración 5s
            
            # Crear nombre único
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"video_{timestamp}.mp4"
            output_path = os.path.join(self.output_dir, filename)
            
            # Guardar el video
            clip.write_videofile(
                output_path, 
                fps=24,
                codec="libx264",
                audio=False,
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
