from fastapi import APIRouter,HTTPException
from bson.objectid import ObjectId
from schemas.achievements import all_data
from models.achievements import Achievements
from config.database import achievements_collection
achievements_router=APIRouter()

@achievements_router.get("/")
async def get_all_achievements():
    data=achievements_collection.find( )
    return all_data(data)

@achievements_router.post("/")
async def create_achievements(new_achievements:Achievements):
    try:
        achievements= achievements_collection.insert_one(dict(new_achievements))
        return{"status code":200, "id":str(achievements.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured : {e}")

@achievements_router.put("/{achievements_id}")
async def update_achievements(achievements_id:str,updated_achievements:Achievements):
    try:
        id=ObjectId(achievements_id)
        find_achievements=achievements_collection.find_one({"_id":id})
        if not find_achievements:
            return HTTPException(status_code=500, detail=f"achievements doesnt exist")
        achievements=achievements_collection.update_one({"_id":id},{"$set":dict(updated_achievements)})
        return{"status_code":200,"message":"achievements Updated"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured : {e}")

@achievements_router.delete("/{achievements_id}")
async def delete_achievements(achievements_id:str):
    try:
        id=ObjectId(achievements_id)
        achievements = achievements_collection.find_one({"_id": id})
        if not achievements:
            return HTTPException(status_code=500, detail=f"achievements doesnt exist")
        achievements_collection.delete_one({"_id": id})
        return{"status_code":200,"message":"achievements deleted"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured : {e}")
