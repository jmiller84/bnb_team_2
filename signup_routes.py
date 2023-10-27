import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User

def apply_signup_routes(app):
    # Show signup form page
    @app.route('/signup', methods=["GET"]) 
    def get_signup_form_page():
        # Check if the user is logged in
        user_is_logged_in = (session.get('user_id', None) is not None)
        connection = get_flask_database_connection(app)
        return render_template(
            'signup.html',
            errors=None,
            user_is_logged_in=user_is_logged_in
        )

    # Process submitted signup form
    @app.route('/signup', methods=["POST"])
    def post_signup_form_data():
        connection = get_flask_database_connection(app)
        error_messages = []
        if session.get('user_id', None) is not None:
            # User is already logged in
            return render_template(
                'signup.html',
                erorrs=[
                    "You are already logged in. If you are trying to "\
                    "create a new account, please log out first."
                ]
            ), 400
        try:
            desired_username = request.form["username"]
            desired_password = request.form["password"]
        except:
            return redirect("/signup")
        user_repository = UserRepository(connection)
        if len(desired_username) > 255:
            msg = "That username is too long (over 255 characters)."
            error_messages.append(msg)
        if len(desired_password) > 255:
            msg = "That password is too long (over 255 characters)."
            error_messages.append(msg)
        if len(desired_password) < 8:
            msg = "Please choose a more secure password "\
                "(at least 8 characters long)."
            error_messages.append(msg)
        all_existing_usernames = [
            user.username for user in user_repository.all()
        ]
        if desired_username in all_existing_usernames:
            msg = f"The username {desired_username} is already in use; "\
                "please choose a different username."
            error_messages.append(msg)
        if len(error_messages) == 0:
            new_user = User(None, desired_username, desired_password)
            # As a side effect, user_repository.create will set new_user.id
            user_repository.create(new_user)
            # Auto-login to the newly created account
            session['user_id'] = new_user.id
            session['username'] = new_user.username
            return redirect(f"/users/{session['user_id']}")
        return render_template(
            'login.html',
            errors=error_messages
        ), 400