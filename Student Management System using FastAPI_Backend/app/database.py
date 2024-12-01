# from motor.motor_asyncio import AsyncIOMotorClient

# MONGO_DETAILS = "mongodb+srv://admin:admin123@mycluster.v0ahc.mongodb.net/?retryWrites=true&w=majority&appName=MyCluster"

# client = AsyncIOMotorClient(MONGO_DETAILS)
# database = client.studentDB
# student_collection = database.get_collection("students")

from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://admin:admin123@mycluster.v0ahc.mongodb.net/?retryWrites=true&w=majority&appName=MyCluster"

# Create the MongoDB client
client = AsyncIOMotorClient(MONGO_URI)

# Get the database
database = client[
    "student_management"
]  # You can name the database "student_management" or whatever you prefer.

# Get the collection
student_collection = database["students"]
