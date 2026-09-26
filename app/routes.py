from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()
BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

def generate_mock_panels(prompt, char, setting, tone, style):
    panels = []
    titles = ["The Forest's Edge","The Whispering Woods","A Brave Decision","The Guardian's Test","A New Legend"]
    for i in range(5):
        panels.append({
            "title": f"Panel {i+1}: {titles[i]}",
            "description": f"{char} explores {setting} in {tone} tone. Prompt: {prompt}",
            "dialog": f"{char}: 'I will protect this {setting}!'",
            "image_url": "https://images.unsplash.com/photo-1474511320723-9a56873867b5?w=800" if i==0 else f"https://picsum.photos/seed/comic{i}/800/500"
        })
    return panels

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/generate", response_class=HTMLResponse)
async def generate_comic(request: Request, story_prompt: str = Form(...), character_name: str = Form(...), setting: str = Form(...), tone: str = Form(...), art_style: str = Form(...)):
    panels = generate_mock_panels(story_prompt, character_name, setting, tone, art_style)
    info = {"prompt": story_prompt, "char": character_name, "setting": setting, "tone": tone, "style": art_style}
    return templates.TemplateResponse("comic_preview.html", {"request": request, "panels": panels, "info": info})

@router.get("/download-pdf", response_class=HTMLResponse)
async def download_pdf(request: Request):
    return templates.TemplateResponse("export_success.html", {"request": request})