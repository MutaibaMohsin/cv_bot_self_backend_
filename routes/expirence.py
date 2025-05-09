from fastapi import APIRouter,HTTPException
from bson.objectid import ObjectId
from schemas.expirence import all_data
from models.expeirence import Experience
from config.database import experience_collection
experience_router=APIRouter()

@experience_router.get("/")
async def get_all_experience():
    data=experience_collection.find( )
    return all_data(data)

@experience_router.post("/")
async def create_experience(new_experience:Experience):
    try:
        experience= experience_collection.insert_one(dict(new_experience))
        return{"status code":200, "id":str(experience.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured : {e}")

@experience_router.put("/{experience_id}")
async def update_experience(experience_id:str,updated_experience:Experience):
    try:
        id=ObjectId(experience_id)
        find_experience=experience_collection.find_one({"_id":id})
        if not find_experience:
            return HTTPException(status_code=500, detail=f"experience doesnt exist")
        experience=experience_collection.update_one({"_id":id},{"$set":dict(updated_experience)})
        return{"status_code":200,"message":"experience Updated"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured : {e}")

@experience_router.delete("/{experience_id}")
async def delete_experience(experience_id:str):
    try:
        id=ObjectId(experience_id)
        experience = experience_collection.find_one({"_id": id})
        if not experience:
            return HTTPException(status_code=500, detail=f"experience doesnt exist")
        experience_collection.delete_one({"_id": id})
        return{"status_code":200,"message":"experience deleted"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured : {e}")
