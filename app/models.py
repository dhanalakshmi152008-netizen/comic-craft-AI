from pydantic import BaseModel
from typing import Optional

class ComicRequest(BaseModel):
    prompt: str
    style: Optional[str] = "comic"