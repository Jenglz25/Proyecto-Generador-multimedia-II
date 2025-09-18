
import os
from dotenv import load_dotenv
import torch
from diffusers import StableDiffusionPipeline, EulerAncestralDiscreteScheduler
from datetime import datetime
import subprocess

class GeneradorImagen:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv("HF_TOKEN")
        self.output_dir = "outputs"
        self._crear_carpeta()
        self.pipeline = None
        self._cargar_modelo()
    
    def _crear_carpeta(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def _cargar_modelo(self):
        """Carga el modelo con configuración optimizada"""
        try:
            print("🔄 Cargando modelo optimizado...")

            if not self.token:
                print("❌ Token no encontrado en .env")
                return
            
            model_id = "stabilityai/stable-diffusion-2-1"

            scheduler = EulerAncestralDiscreteScheduler.from_pretrained(
                model_id, 
                subfolder="scheduler",
                use_auth_token=self.token
            )

            self.pipeline = StableDiffusionPipeline.from_pretrained(
                model_id,
                scheduler=scheduler,
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                use_auth_token=self.token,
                safety_checker=None,
                requires_safety_checker=False
            )

            if torch.cuda.is_available():
                self.pipeline = self.pipeline.to("cuda")
                self.pipeline.enable_attention_slicing()
                print("✅ Modelo optimizado en GPU")
            else:
                print("✅ Modelo en CPU")

        except Exception as e:
            print(f"❌ Error: {str(e)}")
            self.pipeline = None

    def _optimizar_prompt(self, prompt):
        """Agrega detalles para mejorar la calidad del render"""
        positivo = f"masterpiece, best quality, highly detailed, {prompt}, vibrant colors, ultra sharp, 4k render"
        negativo = ("text, words, letters, signature, blurry, low quality, bad anatomy, "
                    "distorted, deformed, extra limbs, watermark, ugly")
        return positivo, negativo

    def generar(self, prompt, width=768, height=512, steps=50, guidance=9.0, seed=None):
        """Genera imagen con prompts positivo y negativo"""
        try:
            if self.pipeline is None:
                return None

            positivo, negativo = self._optimizar_prompt(prompt)

            generator = torch.manual_seed(seed if seed is not None else torch.seed())

            print(f"🎨 Generando: '{prompt}'")

            with torch.no_grad():
                image = self.pipeline(
                    prompt=positivo,
                    negative_prompt=negativo,
                    num_inference_steps=steps,
                    guidance_scale=guidance,
                    width=width,
                    height=height,
                    generator=generator
                ).images[0]

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"imagen_{timestamp}.png"
            image_path = os.path.join(self.output_dir, filename)
            image.save(image_path)

            print(f"💾 Imagen guardada en: {image_path}")

            # Abrir carpeta automáticamente
            try:
                if os.name == 'nt':
                    os.startfile(os.path.dirname(image_path))
                elif os.name == 'posix':
                    subprocess.Popen(['open', os.path.dirname(image_path)])
            except:
                print("📂 Abre manualmente la carpeta 'outputs'")

            return image_path

        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return None


# Ejemplo de uso
if __name__ == "__main__":
    generador = GeneradorImagen()

    resultado = generador.generar(
        "una vaca con vestido azul estilo caricatura, en un campo verde con flores, día soleado, tierna y graciosa"
    )

    if resultado:
        print("🎉 ¡Proceso completado! Revisa la carpeta 'outputs'")
    else:
        print("😞 No se pudo generar la imagen")
