import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.booking_repository import BookingRepository
from lib.booking import Booking
from lib.space_repository import SpaceRepository
from lib.calendar import *
from datetime import datetime

def apply_confirm_booking_routes(app):

    @app.route('/spaces/<space_id>/confirm', methods=["GET"]) 
    def show_booking_info_for_confirmation(space_id):
        connection = get_flask_database_connection(app)
        space_repository = SpaceRepository(connection)
        space_info = space_repository.find_by_space_id(space_id)

        selected_date = session['selected_date']
        formatted_date = selected_date[:16]
  
        return render_template('spaces/confirm_booking.html', space_info=space_info, formatted_date=formatted_date)

    @app.route('/spaces/<space_id>/confirm', methods=["POST"]) 
    def confirm_booking(space_id):
        connection = get_flask_database_connection(app)

        if "confirm_button" in request.form:
            
            repository = BookingRepository(connection)

            date = session.get('selected_date', None)
            date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S %Z")

            repository.create(Booking(
                id = None,
                user_id = session.get('user_id', None),
                space_id = int(space_id),
                date = date
                ))
            
            user_id = session.get('user_id', None)
            return redirect(f'/users/{user_id}')
            
        if "cancel_button" in request.form:


            return redirect(f'/spaces/{space_id}')