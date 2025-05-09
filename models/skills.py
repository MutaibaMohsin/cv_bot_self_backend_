from pydantic import BaseModel
from typing import List
class Skills(BaseModel):
    category: str
    items: List[str] 
