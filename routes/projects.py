from fastapi import APIRouter,HTTPException
from bson.objectid import ObjectId
from schemas.projects import all_data
from models.projects import Projects
from config.database import projects_collection
project_router=APIRouter()

@project_router.get("/")
async def get_all_project():
    data=projects_collection.find( )
    return all_data(data)

@project_router.post("/")
async def create_project(new_project:Projects):
    try:
        project= projects_collection.insert_one(dict(new_project))
        return{"status code":200, "id":str(project.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occured : {e}")

@project_router.put("/{project_id}")
async def update_project(project_id:str,updated_project:Projects):
    try:
        id=ObjectId(project_id)
        find_project=projects_collection.find_one({"_id":id})
        if not find_project:
            raise HTTPException(status_code=500, detail=f"project doesnt exist")
        project=projects_collection.update_one({"_id":id},{"$set":dict(updated_project)})
        return{"status_code":200,"message":"project Updated"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occured : {e}")

@project_router.delete("/{project_id}")
async def delete_project(project_id:str):
    try:
        id=ObjectId(project_id)
        project = projects_collection.find_one({"_id": id})
        if not project:
            raise HTTPException(status_code=500, detail=f"project doesnt exist")
        projects_collection.delete_one({"_id": id})
        return{"status_code":200,"message":"project deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occured : {e}")
