from generator_imagen import GeneradorImagen
from generator_audio import GeneradorAudio
from generator_video import GeneradorVideo
from generator_gif import GeneradorGIF


class Controlador:
    def __init__(self):
        self.imagen = GeneradorImagen()
        self.audio = GeneradorAudio()
        self.video = GeneradorVideo()
        self.gif = GeneradorGIF()