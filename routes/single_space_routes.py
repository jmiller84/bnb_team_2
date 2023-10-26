import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.booking_repository import BookingRepository
from lib.calendar import *
from lib.space_repository import SpaceRepository


def apply_single_space_routes(app):

    @app.route('/spaces/<int:space_id>', methods=["GET"])
    def show_space_info_and_calendar(space_id):
        connection = get_flask_database_connection(app)
        booking_repository = BookingRepository(connection)
        space_repository = SpaceRepository(connection)

        space_info = space_repository.find_by_space_id(space_id)        
        unavailable_dates = booking_repository.show_unavailable_dates_for_space(space_id)

        return render_template('/spaces/single_space.html', cal=cal, str_month=str_month, current_month=current_month, current_year=current_year, unavailable_dates = unavailable_dates, space_info = space_info)

    @app.route('/spaces/<int:space_id>', methods=["POST"])
    def select_date_for_space(space_id):
        connection = get_flask_database_connection(app)

        if "select_date_button" in request.form:
            selected_day = request.form['select_date_button']
            selected_date = date(int(current_year), int(current_month), int(selected_day))

            session['selected_date'] = selected_date
 
            return redirect(f'/spaces/{space_id}/confirm')
        
        else:
            return "hello"
            return redirect('/')
        