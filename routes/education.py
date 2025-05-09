from fastapi import APIRouter,HTTPException
from bson.objectid import ObjectId
from schemas.education import all_data
from models.education import Education
from config.database import education_collection
education_router=APIRouter()

@education_router.get("/")
async def get_all_education():
    data=education_collection.find( )
    return all_data(data)

@education_router.post("/")
async def create_education(new_education:Education):
    try:
        education= education_collection.insert_one(dict(new_education))
        return{"status code":200, "id":str(education.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured : {e}")

@education_router.put("/{education_id}")
async def update_education(education_id:str,updated_education:Education):
    try:
        id=ObjectId(education_id)
        find_education=education_collection.find_one({"_id":id})
        if not find_education:
            return HTTPException(status_code=500, detail=f"education doesnt exist")
        education=education_collection.update_one({"_id":id},{"$set":dict(updated_education)})
        return{"status_code":200,"message":"education Updated"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured : {e}")

@education_router.delete("/{education_id}")
async def delete_education(education_id:str):
    try:
        id=ObjectId(education_id)
        education = education_collection.find_one({"_id": id})
        if not education:
            return HTTPException(status_code=500, detail=f"education doesnt exist")
        education_collection.delete_one({"_id": id})
        return{"status_code":200,"message":"education deleted"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured : {e}")
