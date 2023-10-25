import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.booking_repository import BookingRepository
from lib.calendar import *

def apply_confirm_booking_routes(app):

    @app.route('/spaces/<space_id>/confirm', methods=["GET"]) 
    def show_booking_info_for_confirmation(space_id):
        connection = get_flask_database_connection(app)
        selected_date = session.get('selected_date', None)
  
        return render_template('spaces/confirm_booking.html')

    @app.route('/spaces/<space_id>/confirm', methods=["POST"]) 
    def confirm_booking(space_id):
        connection = get_flask_database_connection(app)

        if "confirm_button" in request.form:
            # user_id = session.get('user_id', None)
            user_id = 1
            return redirect(f'/users/{user_id}')
            
        if "cancel_button" in request.form:

            #space_id = session.get('space_id', None)
            space_id = 1
            return redirect(f'/spaces/{space_id}')