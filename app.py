import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.booking_repository import BookingRepository
from lib.calendar import *

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

#------Home Page------
@app.route('/', methods=["GET"]) 
def home_page():
    connection = get_flask_database_connection(app)

    return render_template('home.html')


#------Login Page------
@app.route('/login', methods=["GET"]) 
def login_page():
    connection = get_flask_database_connection(app)

@app.route('/login', methods=["POST"]) 
def post_login_details():
    connection = get_flask_database_connection(app)

#------Signup Page------
@app.route('/signup', methods=["GET"]) 
def signup_page():
    connection = get_flask_database_connection(app)

#------Single Space Page------

from routes.single_space_routes import apply_single_space_routes
apply_single_space_routes(app)


#------Booking Confirmation Page------

from routes.confirm_booking_routes import apply_confirm_booking_routes
apply_confirm_booking_routes(app)


#------User Bookings Page------
@app.route('/users/<user_id>', methods=["GET"]) 
def view_user_bookings(user_id):
    connection = get_flask_database_connection(app)

    return render_template('users/user_bookings.html')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
