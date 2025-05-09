from pydantic import BaseModel
class Education(BaseModel):
    degree: str
    university: str