from fastapi import FastAPI, HTTPException, Query

from app.jokes import ALL_JOKES, CATEGORIES, select_joke

app = FastAPI(title="AISD Teaching Example")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/categories")
def categories() -> dict[str, list[str]]:
    return {"categories": list(CATEGORIES)}


@app.get("/joke")
def joke(category: str | None = Query(default=None)) -> dict[str, str]:
    try:
        selected_category, selected_joke = select_joke(category)
    except KeyError as error:
        raise HTTPException(status_code=404, detail="Unknown category") from error

    return {"category": selected_category, "joke": selected_joke}