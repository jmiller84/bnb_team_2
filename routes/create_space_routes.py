import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.booking_repository import BookingRepository
from lib.booking import Booking
from lib.space_repository import SpaceRepository
from lib.space import Space
from lib.user_repository import UserRepository
from datetime import datetime, timedelta
from flask import Flask, render_template, redirect, request, session

def apply_create_space_routes(app):
    @app.route('/users/<int:user_id>/create_space', methods=["GET"]) 
    def get_create_space_form(user_id):

        return render_template('spaces/create_space.html', user_is_logged_in = True, errors = None, user_id=user_id, current_date = str(datetime.today()))
    

    @app.route('/users/<int:user_id>/create_space', methods=["POST"]) 
    def post_create_space_form(user_id):

        connection = get_flask_database_connection(app)
        space_repository = SpaceRepository(connection)
        logged_in_id = session.get('user_id', None)
        if logged_in_id != user_id:
            return render_template('error_must_log_in_first.html'), 401
        space_title = request.form['name']
        space_description = request.form['description']
        print(space_description)
        space_price = request.form['price_per_night']
        print(space_price)
        new_space_id = space_repository.create(Space(
                id = None, 
                name = space_title,
                description = space_description,
                price = float(space_price),
                host_id = user_id
                ))

        booking_repository = BookingRepository(connection)
        unavailable_start_date = request.form['first_available_night']
        unavailable_end_date = request.form['last_available_night']

        print(unavailable_start_date)
        print(unavailable_end_date)
        
        unavailable_start_date = datetime(2023,10,20)
        unavailable_end_date = datetime(2023,10,25)

        unavailable_dates_list = []

        while unavailable_start_date <= unavailable_end_date:
            unavailable_dates_list.append(unavailable_start_date)
            unavailable_start_date += timedelta(days=1)

        for date in unavailable_dates_list:
            booking_repository.create(Booking(
                id = None,
                user_id = session.get('user_id', None),
                space_id = new_space_id,
                date = date,
                confirmed = True
                ))
 
        return redirect(f'/users/{user_id}')
    

