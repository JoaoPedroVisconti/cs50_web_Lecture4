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
    f = open("C:/Users/Joao/EngenhariaGoogleDrive/Development/Courses/CS50/WebDevelopment/cs50_web_Lecture3/flights.csv")
    reader = csv.reader(f)
    
    for origin, destination, duration in reader:
        flight = Flight(origin=origin, destination=destination, duration=duration)
        db.session.add(flight)
        
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes")
    
    db.session.commit()
    
if __name__ == "__main__":
    with app.app_context():
        main()       