from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.routes import router

app = FastAPI(title="ComicCraft AI")
BASE_DIR = Path(__file__).resolve().parent.parent
app.include_router(router)