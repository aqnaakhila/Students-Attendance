import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://student-attendance-2e281-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('Students')

data = {
    "141212":
        {
            "name": "Aqna Akhila",
            "major": "Student",
            "attendance": 4,
            "standing": "G",
            "year": 4,
            "starting_year": "2020",
            "last_attendance_time": "2024-05-18 00:00:53"
        },
    
    "852741":
        {
            "name": "Marry Gloss",
            "major": "Teacher",
            "attendance": 8,
            "standing": "B",
            "year": 6,
            "starting_year": "2018",
            "last_attendance_time": "2024-05-19 10:25:03"
        },
        
    "963852":
        {
            "name": "Elon Musk",
            "major": "Principal",
            "attendance": 2,
            "standing": "F",
            "year": 10,
            "starting_year": "2014",
            "last_attendance_time": "2024-02-19 12:05:38"
        }
}

for key, value in data.items():
    ref.child(key).set(value)