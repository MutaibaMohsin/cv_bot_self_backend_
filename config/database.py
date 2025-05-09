
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://mutaibamohsin32:WrLRjaVqyNYcaKXX@cluster0.w6rzy4l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client["cv_database"]

skills_collection = db["skills"]
projects_collection = db["projects"]
user_collection=db["users"]
education_collection = db["education"]
experience_collection = db["experience"]
achievements_collection = db["achievements"]
