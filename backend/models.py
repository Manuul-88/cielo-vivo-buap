from pydantic import BaseModel
from typing import Optional

class Planeta(BaseModel):
    name: str
    color1: str
    color2: str
    size: int
    moons: int
    rings: bool
    message: Optional[str] = None