"""Convierte guiones de estudio (.txt) en episodios MP3 con dos voces en español.

Formato del guion, una línea por intervención:
  A: texto de la presentadora
  B: texto del copresentador
  [PAUSA 6]   silencio de 6 segundos para responder en voz alta

Uso: python3 generar_audio.py <carpeta_guiones> <carpeta_salida> <carpeta_modelo>
"""
import re, subprocess, sys
from pathlib import Path

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

VOCES = {"A": "ef_dora", "B": "em_alex"}

guiones, salida, modelo = (Path(p) for p in sys.argv[1:4])
salida.mkdir(parents=True, exist_ok=True)
k = Kokoro(str(modelo / "kokoro-v1.0.onnx"), str(modelo / "voices-v1.0.bin"))

for guion in sorted(guiones.glob("*.txt")):
    partes, sr = [], 24000
    for linea in guion.read_text(encoding="utf-8").splitlines():
        linea = linea.strip()
        if m := re.fullmatch(r"\[PAUSA (\d+)\]", linea):
            partes.append(np.zeros(int(sr * int(m[1])), dtype=np.float32))
        elif m := re.fullmatch(r"([AB]):\s*(.+)", linea):
            audio, sr = k.create(m[2], voice=VOCES[m[1]], speed=1.0, lang="es")
            partes += [audio, np.zeros(int(sr * 0.45), dtype=np.float32)]
    wav = salida / (guion.stem + ".wav")
    sf.write(wav, np.concatenate(partes), sr)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-b:a", "96k",
                    "-metadata", f"title={guion.stem.replace('_', ' ')}", wav.with_suffix(".mp3")], check=True)
    wav.unlink()
    print("listo:", wav.with_suffix(".mp3"))
