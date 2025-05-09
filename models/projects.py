from pydantic import BaseModel
from typing import List,Optional
class Projects(BaseModel):
    name: str  
    description: str  
    technologies: Optional[List[str]] = []
