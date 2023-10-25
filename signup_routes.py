import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection

def apply_signup_routes(app):
    # Show signup form page
    @app.route('/signup', methods=["GET"]) 
    def get_signup_form_page():
        connection = get_flask_database_connection(app)
        return "", 200

    # Process submitted signup form
    @app.route('/signup', methods=["POST"])
    def post_signup_form_data():
        connection = get_flask_database_connection(app)
        return "", 400