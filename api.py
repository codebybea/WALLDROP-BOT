from fastapi import FastAPI # type: ignore
import json
from typing import List, Dict

app = FastAPI()

def load_wallpapers() -> List[Dict]:
    try:
        with open("wallpapers.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.get("/wallpapers")
async def get_wallpapers():
    wallpapers = load_wallpapers()
    return {"wallpapers": wallpapers}

if __name__ == "__main__":
    import uvicorn # type: ignore
    uvicorn.run(app, host="0.0.0.0", port=8000)