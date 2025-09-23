import flask 
from Project.config_page import config_page

@config_page(template_name= 'cart.html' )
def render_cart() -> dict:
    return {}