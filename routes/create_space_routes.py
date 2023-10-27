import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.booking_repository import BookingRepository
from lib.space_repository import SpaceRepository
from lib.user_repository import UserRepository
from datetime import datetime, timedelta
from flask import Flask, render_template, redirect, request, session

def apply_create_space_routes(app):
    @app.route('/users/<int:user_id>/create_space', methods=["GET"]) 
    def get_create_space_form(user_id):

        
        return render_template('spaces/create_space.html')
    

    @app.route('/users/<int:user_id>/create_space', methods=["POST"]) 
    def post_create_space_form(user_id):

        connection = get_flask_database_connection(app)
        space_repository = SpaceRepository(connection)
        space_title = request.form['name']
        space_description = request.form['description']
        space_price = request.form['price']
        new_space_id = space_repository.create(
                id = None, 
                title = space_title,
                description = space_description,
                price = float(space_price)
                )

        booking_repository = BookingRepository(connection)
        unavailable_start_date = request.form['unavailable_start_date']
        unavailable_end_date = request.form['unavailable_end_date']
        
        unavailable_start_date = datetime(2023,10,20)
        unavailable_end_date = datetime(2023,10,25)

        unavailable_dates_list = []

        while unavailable_start_date <= unavailable_end_date:
            unavailable_dates_list.append(unavailable_start_date)
            unavailable_start_date += timedelta(days=1)

        for date in unavailable_dates_list:
            booking_repository.create(
                id = None,
                user_id = session.get('user_id', None),
                space_id = new_space_id,
                date = date,
                confirmed = True
                )
 
        return render_template('/')
    

