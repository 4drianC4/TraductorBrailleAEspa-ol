import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
from playsound import playsound

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
            tts.save("traduccion.mp3")
            playsound("traduccion.mp3")
        except Exception as e:
            tk.messagebox.showerror("Error", f"No se pudo generar el audio: {e}")
    else:
        tk.messagebox.showwarning("Advertencia", "No hay texto para reproducir.")

# Interfaz gráfica con tkinter
ventana = tk.Tk()
ventana.title("Traductor de Braille a Español en Tiempo Real")

# Entrada de texto en Braille
tk.Label(ventana, text="Ingrese texto en Braille:").pack(pady=5)
entrada_braille = tk.Text(ventana, height=5, width=40)
entrada_braille.pack(pady=5)
entrada_braille.bind("<KeyRelease>", actualizar_traduccion)  # Actualiza al escribir

# Salida de traducción
tk.Label(ventana, text="Texto traducido:").pack(pady=5)
salida_traduccion = tk.Text(ventana, height=5, width=40, state=tk.DISABLED)
salida_traduccion.pack(pady=5)

# Botón para reproducir la traducción
boton_reproducir = tk.Button(ventana, text="Reproducir Traducción", command=texto_a_audio)
boton_reproducir.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
