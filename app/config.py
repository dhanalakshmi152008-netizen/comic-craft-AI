import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

class Settings:
    base_dir = Path(__file__).resolve().parent.parent
    static_path = base_dir / "static"
    templates_dir = base_dir / "templates"
    templates_path = base_dir / "templates"
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY","")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY","")
    app_name = "ComicCraftAI"
    def __getattr__(self, name):
        return os.getenv(name, "")

settings = Settings()
settings.static_path.mkdir(parents=True, exist_ok=True)
settings.templates_dir.mkdir(parents=True, exist_ok=True)