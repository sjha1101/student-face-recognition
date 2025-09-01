from pymongo import MongoClient

# MongoDB se connect ho raha hai
client = MongoClient("mongodb://localhost:27017/")

# attendance_system naam ka DB banayega (agar nahi hai to automatically create ho jayega)
db = client["attendance_system"]

# students collection banega (ya use karega agar pehle se hai)
students_col = db["students"]

# attendance collection banega
attendance_col = db["attendance"]

# attendance_col me attendance insert karega
# attendance_col.insert_one({"roll_no": "123", "name": "xyz", "status": "present"})