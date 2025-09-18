import tkinter as tk
from tkinter import ttk, messagebox
from controlador import Controlador
import os

class MultimediaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Generador Multimedia  ✨")
        self.root.geometry("600x500")
        self.root.configure(bg='#FFF0F5')  # Rosa claro de fondo
        
        # Configurar estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configurar colores
        self.colors = {
            'background': '#FFF0F5',
            'button1': '#FFB6C1',  # Rosa claro
            'button2': '#FFD700',  # Amarillo dorado
            'button3': '#87CEFA',  # Azul claro
            'button4': '#98FB98',  # Verde menta
            'button5': '#DDA0DD',  # Ciruela
            'text': '#8B4513',     # Marrón oscuro
            'entry_bg': '#FFFFFF'  # Blanco
        }
        
        self.ctrl = Controlador()
        
        self._crear_interfaz()
        
    def _crear_interfaz(self):
        # Frame principal 
        main_frame = ttk.Frame(self.root, padding="30")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar expansión 
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Título 
        title_label = tk.Label(main_frame, 
                              text="✨ Generador Multimedia  ✨", 
                              font=("Comic Sans MS", 18, "bold"),
                              fg=self.colors['text'],
                              bg=self.colors['background'])
        title_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Entrada de texto con estilo
        ttk.Label(main_frame, text="¿Qué dibujamos?:", 
                 font=("Arial", 12),
                 background=self.colors['background'],
                 foreground=self.colors['text']).grid(row=1, column=0, sticky=tk.W, pady=10)
        
        self.texto_entry = tk.Entry(main_frame, width=40, 
                                   font=("Arial", 11),
                                   bg=self.colors['entry_bg'],
                                   fg=self.colors['text'],
                                   relief="flat",
                                   highlightthickness=2,
                                   highlightcolor="#FF69B4")
        self.texto_entry.grid(row=1, column=1, pady=10, padx=10)
        self.texto_entry.insert(0, "Escribe algo bonito aquí...")
        
        # Botones con colores y estilo 
        botones = [
            ("🖼️ Generar Imagen", self.generar_imagen, self.colors['button1']),
            ("🎵 Generar Audio", self.generar_audio, self.colors['button2']),
            ("🎥 Generar Video", self.generar_video, self.colors['button3']),
            ("🔄 Generar GIF", self.generar_gif, self.colors['button4']),
            ("📂 Abrir Carpeta de Outputs", self.abrir_carpeta, self.colors['button5'])
        ]
        
        for i, (texto, comando, color) in enumerate(botones):
            btn = tk.Button(main_frame, text=texto, 
                           command=comando,
                           font=("Arial", 14, "bold"),
                           bg=color,
                           fg=self.colors['text'],
                           activebackground="#FFC0CB",
                           relief="raised",
                           padx=20,
                           pady=15,
                           borderwidth=3,
                           cursor="heart")
            btn.grid(row=2+i, column=0, columnspan=2, pady=8, sticky=(tk.W, tk.E))
            # Efecto hover
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg="#FFC0CB"))
            btn.bind("<Leave>", lambda e, b=btn, c=color: b.configure(bg=c))
        
        # Status 
        self.status_var = tk.StringVar()
        self.status_var.set("Lista para crear cosas bonitas... 💖")
        status_label = tk.Label(main_frame, textvariable=self.status_var, 
                               font=("Arial", 12, "italic"),
                               fg="#FF69B4",
                               bg=self.colors['background'])
        status_label.grid(row=7, column=0, columnspan=2, pady=20)
        
        # Footer 
        footer = tk.Label(main_frame, text="💕 Creado con amor 💕", 
                         font=("Arial", 10),
                         fg="#FF69B4",
                         bg=self.colors['background'])
        footer.grid(row=8, column=0, columnspan=2, pady=10)
    
    def abrir_carpeta(self):
        try:
            os.startfile("outputs")  # 
        except:
            try:
                os.system(f"open outputs")  # 
            except:
                os.system(f"xdg-open outputs")  #
    
    def generar_imagen(self):
        prompt = self.texto_entry.get()
        self.status_var.set("Creando una imagen bonita... 🌸")
        self.root.update()
        img = self.ctrl.imagen.generar(prompt)
        self.status_var.set("Imagen lista! 📂✨")
    
    def generar_audio(self):
        prompt = self.texto_entry.get()
        self.status_var.set("Generando melodía... 🎶")
        self.root.update()
        output = self.ctrl.audio.generar(prompt)
        self.status_var.set("Audio listo! 🔊💖")
    
    def generar_video(self):
        prompt = self.texto_entry.get()
        self.status_var.set("Produciendo video... 🎥")
        self.root.update()
        output = self.ctrl.video.generar(prompt)
        self.status_var.set("Video listo! 🎬✨")
    
    # En tu main.py, modifica el método generar_gif:
    def generar_gif(self):
        prompt = self.texto_entry.get()
        self.status_var.set("Creando GIF adorable... 🎡")
        self.root.update()
        output = self.ctrl.gif.generar(prompt)
        if output:
            self.status_var.set("GIF listo! 💫")
        else:
            self.status_var.set("Error al crear GIF 😢")

if __name__ == "__main__":
    root = tk.Tk()
    app = MultimediaApp(root)
    root.mainloop()