from fastapi import APIRouter,HTTPException
from bson.objectid import ObjectId
from schemas.skills import all_data
from models.skills import Skills
from config.database import skills_collection
skills_router=APIRouter()

@skills_router.get("/")
async def get_all_skills():
    data=skills_collection.find( )
    return all_data(data)

@skills_router.post("/")
async def create_skills(new_skill:Skills):
    try:
        skill= skills_collection.insert_one(dict(new_skill))
        return{"status code":200, "id":str(skill.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occured : {e}")

@skills_router.put("/{skills_id}")
async def update_skills(skills_id:str,updated_skill:Skills):
    try:
        id=ObjectId(skills_id)
        find_skill=skills_collection.find_one({"_id":id})
        if not find_skill:
            raise HTTPException(status_code=500, detail=f"Skill doesnt exist")
        skill=skills_collection.update_one({"_id":id},{"$set":dict(updated_skill)})
        return{"status_code":200,"message":"Skills Updated"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occured : {e}")

@skills_router.delete("/{skills_id}")
async def delete_skills(skills_id:str):
    try:
        id=ObjectId(skills_id)
        skill = skills_collection.find_one({"_id": id})
        if not skill:
            raise HTTPException(status_code=500, detail=f"Skills doesnt exist")
        skills_collection.delete_one({"_id": id})
        return{"status_code":200,"message":"Skills deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occured : {e}")
