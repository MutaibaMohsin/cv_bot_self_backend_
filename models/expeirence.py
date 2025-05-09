from pydantic import BaseModel
from typing import Optional,List

class Experience(BaseModel):
    position: str
    company: str
    location: str
    description: Optional[List[str]] = None