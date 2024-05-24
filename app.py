from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://benmross:Rose7714!!@phsreservations.kzol6gh.mongodb.net/?retryWrites=true&w=majority&appName=PHSReservations"
client = MongoClient('mongodb+srv://benmross:Rose7714!!@phsreservations.kzol6gh.mongodb.net/?retryWrites=true&w=majority&appName=PHSReservations')
mongo = PyMongo(app)

# Connect to the MongoDB database
def get_db_connection():
    db = client.get_database('PHSReservations')
    return db

@app.route('/')
def index():
    db = get_db_connection()
    rooms = db['Rooms'].find()
    return render_template("index.html", rooms=rooms)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    db = get_db_connection()
    collection = db['Reservations']

    # Retrieve form data
    name = request.form['name']
    email = request.form['email']
    date = request.form['date']
    period = request.form['period']
    room = request.form['room']

    # Create a reservation document
    reservation = {
        "name": name,
        "email": email,
        "date": date,
        "period": period,
        "room": room
    }

    # Insert the reservation into the database
    collection.insert_one(reservation)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)