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
        rows = repository.find_bookings_by_user_id_with_space_info_as_dictionary(user_id)
        username = rows[0]['username']
        booking_details = [
            {'booking_id': row['booking_id'],
            'space_name': row['name'],
            'booking_date': (row['date']).strftime("%d %B %Y"),
            'price': row['price']} for row in rows]
        booking_repository = BookingRepository(connection)
        booking_requests = booking_repository.find_all_unconfirmed_booking_requests(user_id)

        return render_template('user_page.html', username=username, bookings=booking_details, booking_requests=booking_requests)