from fastapi import FastAPI
from routes.skills import skills_router
from routes.auth import user_router
from routes.projects import project_router
from routes.expirence import experience_router
from routes.education import education_router
from routes.achievements import achievements_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(skills_router, prefix="/skills", tags=["Skills"])
app.include_router(user_router, prefix="/users", tags=["user"])
app.include_router(project_router, prefix="/projects", tags=["Project"])
app.include_router(experience_router, prefix="/experience", tags=["Experience"])
app.include_router(education_router, prefix="/education", tags=["Education"])
app.include_router(achievements_router, prefix="/achievements", tags=["Achievement"])


# @app.get("/")
# async def Entry():
#     return {"message": "The app is working"}

