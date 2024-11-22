import os
from io import BytesIO
import librosa
import numpy as np

def mel_spectrogram(file):
    try:
        sample_length = 16000
        num_mfcc = 13

        audio_data = file.file.read()
        audio_file = BytesIO(audio_data)

        audio, sr = librosa.load(audio_file, sr=16000)
        segments = []
        for start in range(0, len(audio), sample_length):
            segment = audio[start:start + sample_length]
            if len(segment) < sample_length:
                segment = np.pad(segment, (0, sample_length - len(segment)))
            mfcc = librosa.feature.mfcc(y=segment, sr=sr, n_mfcc=num_mfcc)
            segments.append(mfcc.T)

        print("Entró en mel_spectrogram y procesó el archivo")
        return segments
    except Exception as e:
        print(f"Error en mel_spectrogram: {str(e)}")
        raise