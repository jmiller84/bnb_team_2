import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User

def apply_login_routes(app):
    # Show login form page
    @app.route('/login', methods=["GET"]) 
    def get_login_form_page():
        if session.get('user_id', None) is not None:
            # The user is already logged in
            return redirect(f"/user/{session['user_id']}")
        connection = get_flask_database_connection(app)
        return render_template(
            'login.html',
            errors=None
        )

    # Process submitted login form
    @app.route('/login', methods=["POST"]) 
    def post_login_form_data():
        connection = get_flask_database_connection(app)
        error_messages = []
        if session.get('username', None) is not None:
            # User is already logged in
            return render_template(
                'login.html',
                errors=[
                    "You are already logged in. If you are trying to "\
                    "switch accounts, please log out first."
                ]
            ), 400
        try:
            submitted_username = request.form["username"]
            submitted_password = request.form["password"]
        except:
            return redirect("/login")
        if len(submitted_username) > 255:
            error_messages.append(
                "The submitted username was too long (over 255 characters)."
            )
        if len(submitted_password) > 255:
            error_messages.append(
                "The submitted password was too long (over 255 characters)."
            )
        user_repository = UserRepository(connection)
        users_with_correct_username = [
            user for user in user_repository.all()
            if user.username == request.form["username"]
        ]
        if len(users_with_correct_username) == 0:
            error_messages.append(
                "No account exists with the given "\
                "combination of username and password."
            )
        else:
            correct_user = users_with_correct_username[0]
            if submitted_password != correct_user.password:
                error_messages.append(
                    "No account exists with the given "\
                    "combination of username and password."
                )
        if len(error_messages) == 0:
            session['user_id'] = correct_user.id
            session['username'] = correct_user.username
            return redirect(f"/users/{session['user_id']}")

        return render_template(
            'login.html',
            errors=error_messages
        ), 400

    # Log out of account (if logged in)
    # then redirect to homepage
    @app.route('/logout', methods=["GET"])
    def get_do_logout():
        session.pop('user_id', None)
        session.pop('username', None)
    return redirect('/')