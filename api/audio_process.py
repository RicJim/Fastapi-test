import os
from io import BytesIO

def mel_spectrogram(file):
    try:
        audio_data = file.file.read()
        audio_file = BytesIO(audio_data)

        print("Entró en mel_spectrogram y procesó el archivo")
        return "Tarea mel_spectrogram completada"
    except Exception as e:
        print(f"Error en mel_spectrogram: {str(e)}")
        raise