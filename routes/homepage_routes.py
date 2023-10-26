import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.booking_repository import BookingRepository
from lib.space_repository import SpaceRepository
from lib.user_repository import UserRepository
from datetime import datetime

def apply_home_page_routes(app):
    @app.route('/', methods=["GET"]) 
    def home_page():
        connection = get_flask_database_connection(app)
        repository = SpaceRepository(connection)
        spaces = repository.all()
        return render_template('home.html', spaces=spaces)
    
def apply_home_page_routes_POST(app):
    @app.route('/', methods=["POST"]) 
    def home_page_book_now_button():
        space_id = request.form['book_now_button']
        return redirect(f'/spaces/{space_id}')
