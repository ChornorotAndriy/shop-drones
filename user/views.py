import flask, flask_login

from flask_login import current_user

from .models import User
from Project.db import DATABASE
from Project.config_page import config_page

def logout():
    flask.session.clear()
    return flask.redirect('/')

@config_page(template_name= 'registration.html')
def render_registration() -> dict:
    message = ""
    
    if flask.request.method == "POST":
        password_form = flask.request.form["password"]
        confirm_password_form = flask.request.form["confirm_password"]
        email_form = flask.request.form["email"]
        
        user = User.query.filter_by(email = email_form).first()
        
        if user is None:
            if password_form == confirm_password_form:
                user = User(
                    username = flask.request.form["username"],
                    email = email_form,
                    password = password_form
                )
                DATABASE.session.add(user)
                DATABASE.session.commit()
                message = "Successful registration"
                
            else:
                message = "Passwords don't match"
        else:
            message = "User with this email already exists"

    return {'message': message}


def render_authorization():
    if flask.request.method == "POST":
        username_form = flask.request.form["username"]
        password_form = flask.request.form["password"]
        list_users = User.query.all()

        for user in list_users:
            if user.username == username_form and user.password == password_form:
                flask_login.login_user(user)
                
    if not flask_login.current_user.is_authenticated:
        return flask.render_template(template_name_or_list= "authorization.html")
    else:
        return flask.redirect(location= "/")
    