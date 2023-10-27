import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.booking_repository import BookingRepository
from lib.space_repository import SpaceRepository
from lib.user_repository import UserRepository
from datetime import datetime

def apply_user_page_routes(app):
    @app.route('/users/<int:user_id>', methods=["GET"]) 
    def view_user_bookings(user_id):
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)

        try:
            user = repository.find_user_by_user_id(user_id)
        except IndexError:
            # => No user with the given id exists.
            return render_template('error_user_not_found.html', user_id=user_id), 404
        username = user.username

        rows = repository.find_bookings_by_user_id_with_space_info_as_dictionary(user_id)
        booking_details = [
            {'booking_id': row['booking_id'],
            'space_name': row['name'],
            'booking_date': (row['date']).strftime("%d %B %Y"),
            'price': row['price'],
            'confirmed': row['confirmed']} for row in rows]
        booking_repository = BookingRepository(connection)
        booking_requests = booking_repository.find_all_unconfirmed_booking_requests(user_id)

        return render_template('user_page.html', username=username, user_id=user_id, bookings=booking_details, booking_requests=booking_requests)
    
    @app.route('/users/<int:user_id>', methods=["POST"]) 
    def set_status_of_request(user_id):
        connection = get_flask_database_connection(app)
        repository = BookingRepository(connection)

        if "reject-booking" in request.form:
            booking_id = request.form['reject-booking']
            repository.delete(booking_id)

            return redirect(f'/users/{user_id}')
        
        elif "confirm-booking" in request.form:
            booking_id = request.form['confirm-booking']
            repository.update_booking_to_confirmed(booking_id)
        
            return redirect(f'/users/{user_id}')