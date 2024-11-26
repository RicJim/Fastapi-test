from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from mangum import Mangum
import os

from .audio_process import mel_spectrogram

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://bird-app-nextjs-pwa.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

handler = Mangum(app)

@app.get("/")
async def hello_fast_api():
    return {"message": "Hello! FastApi"}

@app.get("/favicon.ico")
async def favicon():
    return RedirectResponse(url="/static/favicon.ico")

@app.post("/mel_spectrogram")
def hello_nextjs(file: UploadFile = File(...)):
    try:
        segments = mel_spectrogram(file)

        serializable_segments = [segment.tolist() for segment in segments]

        return JSONResponse(
            content={
                "message": "Archivo procesado exitosamente.",
                "segments": serializable_segments,
            },
            status_code=200,
        )
    except Exception as e:
        return JSONResponse(
            content={"error": f"Error al procesar el archivo: {str(e)}"},
            status_code=500,
        )