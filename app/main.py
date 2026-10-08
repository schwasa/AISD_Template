from fastapi import FastAPI

from app.jokes import select_joke

app = FastAPI(title="AISD Teaching Example")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/joke")
def joke() -> dict[str, str]:
    return {"joke": select_joke()}