from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from .audio_process import mel_spectrogram

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar "*" por los dominios específicos en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def hello_fast_api():
    return "Hello!"

@app.get("/favicon.ico")
async def favicon():
    return RedirectResponse(url="/static/favicon.ico")

@app.post("/mel_spectrogram")
def hello_nextjs(file: UploadFile = File(...)):
    try:
        mel_message = mel_spectrogram(file)

        return JSONResponse(
            content={
                "message": "Tareas completadas exitosamente.",
                "details": [mel_message],
            },
            status_code=200,
        )
    except Exception as e:
        return JSONResponse(
            content={"error": f"Error al procesar el archivo: {str(e)}"},
            status_code=500,
        )