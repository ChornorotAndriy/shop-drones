from flask_login import current_user
import flask


def config_page(template_name: str):
    def render_page(function: object):
        def execute(*args, **kwargs):
            context = function(*args, **kwargs)
            return flask.render_template(
                template_name_or_list = template_name, 
                current_user = current_user,
                **context
            )
        return execute
    return render_page
