import csv
import os

from flask import Flask, render_template, request
from models import *
from config import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (DATABASE_URI)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    flights = Flight.query.all()
    
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes")
    
    flight1 = Flight.query.get(2)
    
    print(f"Flight id=2 {flight1.origin} to {flight1.destination}, {flight1.duration} minutes")
        
if __name__ == "__main__":
    with app.app_context():
        main()