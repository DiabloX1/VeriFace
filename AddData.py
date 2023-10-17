import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecoattendance-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    'BRS1382':
        {
            "name": "Donel",
            "major": "Robotics",
            "starting_year": 2021,
            "total_attendance": 16,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2023-06-20 00:54:34"
        },
    'BRS1143':
        {
            "name": "Raina",
            "major": "AI",
            "starting_year": 2021,
            "total_attendance": 9,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-06-20 00:54:34"
        },
    '963852':
        {
            "name": "Elon",
            "major": "Phy",
            "starting_year": 2021,
            "total_attendance": 10,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-06-20 00:54:34"
        }
}

for key, value in data.items():     #sending to db
    ref.child(key).set(value)