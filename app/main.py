from fastapi import FastAPI
from app.routers import user, audio

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello in audio service"}


app.include_router(user.router)
app.include_router(audio.router)
