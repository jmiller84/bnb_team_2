import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection

def apply_login_routes(app):
    # Show login form page
    @app.route('/login', methods=["GET"]) 
    def get_login_form_page():
        connection = get_flask_database_connection(app)
        return "", 200

    # Process submitted login form
    @app.route('/login', methods=["POST"]) 
    def post_login_form_data():
        connection = get_flask_database_connection(app)
        return "", 400