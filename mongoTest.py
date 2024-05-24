from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, request

app = Flask(__name__)
uri = "mongodb+srv://benmross:Rose7714!!@phsreservations.kzol6gh.mongodb.net/?retryWrites=true&w=majority&appName=PHSReservations"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
db = client['PHSReservations']
collection = db['Rooms']
reservations = db['Reservations']
documents = collection.find({'Number': {'$regex': f'.*{'HUB'}.*', '$options': 'i'}})
for doc in documents:
    print(doc)
reservations.insert_one({'Number': 'HUBS', 'Email': 'test@gmail.com', 'Period': 1})
@app.route('/python_function', methods=['POST'])
def python_function():
    # Call your desired function here
    result = reservationClick()
    return result
def reservationClick(roomNumber):
    reservations.insert_one({'Number': roomNumber, 'Email': 'test@gmail.com', 'Period': 1})