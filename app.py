import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.booking_repository import BookingRepository
from lib.space_repository import SpaceRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

#------Home Page------
@app.route('/', methods=["GET"]) 
def home_page():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    return render_template('home.html', spaces=spaces)


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
@app.route('/spaces/<space_id>', methods=["GET"]) 
def show_space_info_and_calendar():
    connection = get_flask_database_connection(app)

@app.route('/spaces/<space_id>', methods=["POST"]) 
def select_date_for_space():
    connection = get_flask_database_connection(app)

#------Booking Confirmation Page------
@app.route('/spaces/<space_id>/confirm', methods=["GET"]) 
def show_booking_info_for_confirmation():
    connection = get_flask_database_connection(app)

@app.route('/spaces/<space_id>/confirm', methods=["POST"]) 
def confirm_booking():
    connection = get_flask_database_connection(app)

    return redirect('users/<user_id>')

#------User Bookings Page------
@app.route('/users/<user_id>', methods=["GET"]) 
def view_user_bookings():
    connection = get_flask_database_connection(app)




# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
