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
    "⠀": " "  # Espacio
}

# Función para traducir Braille a español
def traducir_braille_a_espanol(braille_texto):
    return "".join(braille_to_spanish.get(c, "?") for c in braille_texto)

# Función para convertir texto a audio y reproducirlo
def texto_a_audio(texto, nombre_archivo="audio.mp3", idioma="es"):
    try:
        tts = gTTS(text=texto, lang=idioma)
        tts.save(nombre_archivo)
        playsound(nombre_archivo)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo generar el audio: {e}")

# Función para manejar la traducción y el audio
def procesar_texto():
    braille_texto = entrada_braille.get("1.0", tk.END).strip()  # Obtener texto del cuadro
    if not braille_texto:
        messagebox.showwarning("Advertencia", "Por favor ingrese texto en braille.")
        return
    texto_traducido = traducir_braille_a_espanol(braille_texto)
    salida_traduccion.config(state=tk.NORMAL)
    salida_traduccion.delete("1.0", tk.END)
    salida_traduccion.insert(tk.END, texto_traducido)
    salida_traduccion.config(state=tk.DISABLED)
    texto_a_audio(texto_traducido)

# Interfaz gráfica con tkinter
ventana = tk.Tk()
ventana.title("Traductor de Braille a Español")

# Entrada de texto en Braille
tk.Label(ventana, text="Ingrese texto en Braille:").pack(pady=5)
entrada_braille = tk.Text(ventana, height=5, width=40)
entrada_braille.pack(pady=5)

# Botón para traducir y reproducir
boton_traducir = tk.Button(ventana, text="Traducir y Reproducir", command=procesar_texto)
boton_traducir.pack(pady=10)

# Salida de traducción
tk.Label(ventana, text="Texto traducido:").pack(pady=5)
salida_traduccion = tk.Text(ventana, height=5, width=40, state=tk.DISABLED)
salida_traduccion.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
