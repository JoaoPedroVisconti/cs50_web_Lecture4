from flask import Flask, render_template, request
from models import *
from config import *
from flask.json import jsonify

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (DATABASE_URI)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    flights = Flight.query.all()
    return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    """Book a flight"""
    
    # Get form information
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number")
    
    # Make sure the flight exists
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="Nosuch flight with that id")
    
    # Add passenger
    flight.add_passenger(name)
    return render_template("success.html")

@app.route("/flights")
def flights():
    """List all flights"""
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """List detail about a single flight"""
    
    # Make sure the flight exists
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight")
    
    # Get all passengers
    passengers = Passengers.query.filter_by(flight_id=flight_id)
    return render_template("flight.html", flight=flight, passengers=passengers)

@app.route("/api/flights/<int:flight_id>")
def flight_api(flight_id):
    #! Build a API #
    
    # Make sure that the flight exists
    flight = Flight.query.get(flight_id)
    if flight is None:
        return jsonify({"error": "No such flight"}), 422
    
    # Get all passengers
    passengers = flight.passengers
    names = []
    
    for passenger in passengers:
        names.append(passenger.name)
    
    return jsonify({
        "origin": flight.origin,
        "destination": flight.destination,
        "duration": flight.duration,
        "passengers": names
    })
    