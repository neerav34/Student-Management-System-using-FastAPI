from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://admin:admin123@mycluster.v0ahc.mongodb.net/?retryWrites=true&w=majority&appName=MyCluster"

client = AsyncIOMotorClient(MONGO_URI)

database = client[
    "student_management"
] 

student_collection = database["students"]
