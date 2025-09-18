import imageio
from PIL import Image, ImageDraw, ImageFont
import os
import webbrowser
from datetime import datetime

class GeneradorGIF:
    def __init__(self):
        self.output_dir = "outputs"
        self._crear_carpeta()
    
    def _crear_carpeta(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def generar(self, prompt):
        try:
            print("🔄 Generando GIF...")
            
            # Crear frames para el GIF
            frames = []
            colors = ['red', 'blue', 'green', 'yellow', 'purple']
            
            for i in range(5):  # 5 frames
                img = Image.new('RGB', (400, 200), color='black')
                d = ImageDraw.Draw(img)
                
                # Texto animado con colores cambiantes
                d.text((50, 80), prompt, fill=colors[i % len(colors)])
                d.text((150, 150), f"Frame {i+1}", fill='white')
                
                frames.append(img)
            
            # Crear nombre único
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"gif_{timestamp}.gif"
            output_path = os.path.join(self.output_dir, filename)
            
            # Guardar GIF
            frames[0].save(
                output_path,
                save_all=True,
                append_images=frames[1:],
                duration=500,  # 500ms entre frames
                loop=0,        # loop infinito
                optimize=True
            )
            
            print(f"✅ GIF guardado: {output_path}")
            
            # Abrir automáticamente
            webbrowser.open(output_path)
            
            return output_path
            
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            print(error_msg)
            return error_msg