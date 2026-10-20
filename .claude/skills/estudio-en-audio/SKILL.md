---
name: estudio-en-audio
description: Convierte un PDF (tesis, proyecto, apuntes) en una serie de episodios MP3 de estudio en español, con dos voces, preguntas de repaso con pausas y un simulacro de sustentación. Usar cuando alguien quiera estudiar un documento escuchándolo, en formato pódcast o audiolibro.
---

# Estudio en audio

Método: no leer el PDF en voz alta, sino reescribirlo como pódcast de estudio con recuerdo activo.

1. Extraer el texto: `pdftotext archivo.pdf texto.txt` y leerlo completo.
2. Escribir un guion `.txt` por episodio (4–6 min cada uno), en una carpeta aparte:
   - Ep. 1: todo el documento en 5 minutos (título, problema, objetivo, hipótesis, método, muestra).
   - Un episodio por capítulo, con siglas y trucos de memoria para los datos clave.
   - Cada episodio termina con 4–5 preguntas, cada una seguida de `[PAUSA n]` y su respuesta.
   - Último episodio: simulacro de examen o sustentación, más los puntos débiles del documento.
   - Formato: `A: ...` (voz femenina), `B: ...` (voz masculina), `[PAUSA 6]`.
   - Escribir números, siglas y decimales como se pronuncian ("cero coma cero cinco", "ese pe ese ese").
3. Instalar el motor de voz (sin conexión):
   ```bash
   pip install kokoro-onnx soundfile
   curl -sSLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
   curl -sSLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
   ```
4. Generar los MP3 (necesita ffmpeg):
   `python3 scripts/generar_audio.py <carpeta_guiones> <carpeta_salida> <carpeta_modelo>`
