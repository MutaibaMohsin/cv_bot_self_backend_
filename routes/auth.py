from fastapi import APIRouter, HTTPException, Depends
from models.user import User
from config.database import user_collection
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import jwt
user_router = APIRouter()
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_pwd_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def authenticate_user(username: str, password: str):
    try:
        user = user_collection.find_one({"username": username})
        if user and verify_password(password, user["password"]):
            return user
        return False
    except Exception:
        return False

@user_router.post("/signup")
async def signup(new_user: User):
    try:
        if user_collection.find_one({"username": new_user.username}):
            raise HTTPException(status_code=400, detail="Username already exists")
        user_data = {
            "username": new_user.username,
            "email": new_user.email,
            "password": get_pwd_hash(new_user.password)
        }

        newuser = user_collection.insert_one(user_data)
        return {"status code": 200, "id": str(newuser.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occurred: {e}")
    

@user_router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        username = form_data.username
        password = form_data.password

        user = authenticate_user(username, password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")

        access_token = create_access_token(data={"sub": username})
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occurred: {e}")
@user_router.get("/")
async def get_token(token: str = Depends(oauth2_scheme)):
    return {"message": "Token is valid!"}
