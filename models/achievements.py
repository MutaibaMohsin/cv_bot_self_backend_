from pydantic import BaseModel, Field

class Achievements(BaseModel):
    name: str
    organization:str
    description: str
