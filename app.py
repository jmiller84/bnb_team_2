import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.booking_repository import BookingRepository
from lib.calendar import *
from lib.space_repository import SpaceRepository
from lib.user_repository import UserRepository
from datetime import datetime

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

#------Home Page------
from routes.homepage_routes import apply_home_page_routes
apply_home_page_routes(app)

from routes.homepage_routes import apply_home_page_routes_POST
apply_home_page_routes_POST(app)

#------Login Page------

from login_routes import apply_login_routes
apply_login_routes(app)

#------Signup Page------

from signup_routes import apply_signup_routes
apply_signup_routes(app)

#------Single Space Page------

from routes.single_space_routes import apply_single_space_routes
apply_single_space_routes(app)


#------Booking Confirmation Page------

from routes.confirm_booking_routes import apply_confirm_booking_routes
apply_confirm_booking_routes(app)


#------User Bookings Page------

from routes.user_page_routes import apply_user_page_routes
apply_user_page_routes(app)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
