import pygame
from gtts import gTTS
import tkinter as tk
from tkinter import ttk, messagebox

# Diccionario de mapeo Braille (Unicode) a español
braille_to_spanish = {
    "⠁": "a", "⠃": "b", "⠉": "c", "⠙": "d", "⠑": "e",
    "⠋": "f", "⠛": "g", "⠓": "h", "⠊": "i", "⠚": "j",
    "⠅": "k", "⠇": "l", "⠍": "m", "⠝": "n", "⠻": "ñ",
    "⠕": "o", "⠏": "p", "⠟": "q", "⠗": "r", "⠎": "s",
    "⠞": "t", "⠥": "u", "⠧": "v", "⠺": "w", "⠭": "x",
    "⠽": "y", "⠵": "z",
    "⠀": " ",  # Espacio
    "?": "?",  # Caracter desconocido
    "⠈⠁": "á", "⠈⠑": "é", "⠈⠊": "í", "⠈⠕": "ó", "⠈⠥": "ú",  # Acentos
    "⠠": ",",  # Coma
    "⠨": ".",  # Punto
}

# Función para traducir Braille a español
def traducir_braille_a_espanol(braille_texto):
    return "".join(braille_to_spanish.get(c, "?") for c in braille_texto)

# Función para actualizar la traducción en tiempo real
def actualizar_traduccion(event=None):
    braille_texto = entrada_braille.get("1.0", tk.END).strip()
    texto_traducido = traducir_braille_a_espanol(braille_texto)
    salida_traduccion.config(state=tk.NORMAL)
    salida_traduccion.delete("1.0", tk.END)
    salida_traduccion.insert(tk.END, texto_traducido)
    salida_traduccion.config(state=tk.DISABLED)

# Función para convertir texto a audio y reproducirlo
def texto_a_audio():
    texto = salida_traduccion.get("1.0", tk.END).strip()
    if texto:
        try:
            tts = gTTS(text=texto, lang="es")
            tts.save("audio.mp3")

            # Reproducción con pygame
            pygame.mixer.init()
            pygame.mixer.music.load("audio.mp3")
            pygame.mixer.music.play()

            # Espera hasta que termine de reproducir
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el audio: {e}")
    else:
        messagebox.showwarning("Advertencia", "Por favor ingrese texto para reproducir.")

# Interfaz gráfica con tkinter y ttk
ventana = tk.Tk()
ventana.title("Traducción de Braille a Español")
ventana.geometry("500x450")
ventana.configure(bg="#D3D3D3")  # Fondo plomo claro

# Estilo ttk
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 18, 'bold'), foreground='white', background='#D3D3D3', padding=10)
style.map('TButton', background=[('active', '#b0b0b0')])

# Título
titulo = tk.Label(
    ventana, 
    text="Traducción de Braille a Español", 
    font=("Helvetica", 18, "bold"), 
    bg="#D3D3D3", 
    fg="#003B5C"
)
titulo.pack(pady=20)

# Entrada de texto en Braille
entrada_frame = tk.Frame(ventana, bg="#D3D3D3")  # Fondo igual al de la ventana
entrada_frame.pack(pady=10)

tk.Label(
    entrada_frame, 
    text="Ingrese texto en Braille:", 
    font=("Helvetica", 18), 
    bg="#D3D3D3", 
    fg="#003B5C"
).pack(pady=5)

entrada_braille = tk.Text(
    entrada_frame, 
    height=1, 
    width=15, 
    font=("Helvetica", 18), 
    bd=1, 
    relief="solid", 
    wrap="none", 
    # bg="#D3D3D3", 
    # fg="black"
)
entrada_braille.pack(ipadx=50, ipady=5)  # Ancho 100px y alto 25px
entrada_braille.bind("<KeyRelease>", actualizar_traduccion)  # Actualiza al escribir


# Salida de traducción
salida_frame = tk.Frame(ventana, bg="#D3D3D3")  # Fondo igual al de la ventana
salida_frame.pack(pady=10)

tk.Label(
    salida_frame, 
    text="Texto traducido:", 
    font=("Helvetica", 18), 
    bg="#D3D3D3", 
    fg="#003B5C"
).pack(pady=5)

salida_traduccion = tk.Text(
    salida_frame, 
    height=5, 
    width=40, 
    font=("Helvetica", 18), 
    bd=1, 
    relief="solid", 
    wrap="word", 
)
salida_traduccion.pack(pady=5)

# Botón para traducir y reproducir
boton_traducir = tk.Button(
    ventana, 
    text="Reproducir Traducción", 
    font=("Helvetica", 18, "bold"), 
    bg="#D3D3D3", 
    fg="#003B5C", 
    bd=1, 
    relief="solid", 
    command=texto_a_audio
)
boton_traducir.pack(pady=15)

# Ejecutar la aplicación
ventana.mainloop()
