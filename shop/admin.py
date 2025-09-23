from flask_login import current_user
import flask

def is_admin(function: object):
    def delete_product(*args, **kwargs):
        if current_user.is_authenticated and current_user.is_admin:
            function(*args, **kwargs)
        return flask.redirect('/shop')
    return delete_product