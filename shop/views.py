import flask, os
from flask_login import current_user

from .models import Product
from .admin import is_admin

from Project.db import DATABASE
from Project.config_page import config_page

@config_page(template_name= 'shop.html')
def render_shop() -> dict:
    
    message = ''
    # 
    type = flask.request.args.get('type')
    list_products = Product.query.all() 
    # 
    if flask.request.method == "POST":
        if type == 'add_product' and current_user.is_authenticated and current_user.is_admin:
            product_name_form = flask.request.form['product_name']
            product_name_model = Product.query.filter_by(product_name = product_name_form).first()
            
            if product_name_model is None:
                product = Product(
                    product_name = product_name_form,
                    price = flask.request.form['price'],
                    discount = flask.request.form['discount'],
                    count = flask.request.form['count'],
                    description = flask.request.form['description']
                )
                DATABASE.session.add(product)
                DATABASE.session.commit()
                #
                image = flask.request.files['image']
                image.save(dst= os.path.abspath(os.path.join(__file__, '..', 'static', 'images', 'products', f'{product_name_form}.png')))
                
                message = 'Продукт додано до магазину'
            else:
                message = 'Такий продукт вже існує'
    
    return {
        'message': message,
        'list_product': list_products,
        'type_products': Product.query.all()
    }

@is_admin
def delete_product():
    # 
    product_id = int(flask.request.args.get(key= 'id'))
    #
    get_model_product = Product.query.get(ident= product_id) # object | None
    if get_model_product is not None:
        DATABASE.session.delete(get_model_product)
        DATABASE.session.commit()
        #
        os.remove(path= os.path.abspath(os.path.join(__file__, '..', 'static', 'images', 'products', f'{get_model_product.product_name}.png')))
#
def add_product_cookies():
    list_id_products = flask.request.cookies.get(key= 'list_products')
    product_id = flask.request.args.get(key= "id")
    response = flask.make_response(flask.redirect('/shop'))

    if list_id_products is not None:
        list_id_products += " " + product_id
        response.set_cookie(key= "list_products", value= list_id_products)
    else:
        response.set_cookie(key= "list_products", value= product_id)
    return response

def create_json(list_products: list, list_filter: list):
    for product in list_products:
        dict_product = {
            'product_name': product.product_name,
            'type_product': product.type_product,
            'price': product.price,
            'discount': product.discount,
            'count': product.count,
            'description': product.description,
            'product_id': product.id
        }
        list_filter.append(dict_product)

def filter():
    data = flask.request.get_data(as_text = True)
    list_filter = []
    if data != 'all':
        list_products = Product.query.filter_by(type_product = data).all()
    else: 
        list_products = Product.query.all()
        
    create_json(list_products= list_products, list_filter= list_filter)
    return  {
        'products': list_filter,
        'is_admin': current_user.is_admin if current_user.is_authenticated else False
    }