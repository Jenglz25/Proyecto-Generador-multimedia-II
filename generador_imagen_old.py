import requests
import os
from PIL import Image
import io
import webbrowser
from datetime import datetime

class GeneradorImagen:
    def __init__(self):
        self.output_dir = "outputs"
        self._crear_carpeta()
    
    def _crear_carpeta(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def generar(self, prompt):
        try:
            print("🖼️ Generando imagen...")
            
            # API gratuita de Stable Diffusion
            API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
            headers = {"Authorization": "Bearer hf_tu_token_opcional"}  # Puedes dejar vacío
            
            response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
            
            if response.status_code == 200:
                # Crear nombre único con timestamp
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"imagen_{timestamp}.png"
                image_path = os.path.join(self.output_dir, filename)
                
                # Guardar imagen
                image = Image.open(io.BytesIO(response.content))
                image.save(image_path)
                
                print(f"✅ Imagen guardada: {image_path}")
                
                # Abrir automáticamente
                webbrowser.open(image_path)
                
                return image_path
            else:
                error_msg = f"❌ Error API: {response.status_code}"
                print(error_msg)
                return error_msg
                
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            print(error_msg)
            return error_msg