from Project.db import DATABASE

class Product(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    # 
    product_name = DATABASE.Column(DATABASE.String(50), default = "product_name")
    price = DATABASE.Column(DATABASE.Float, default = 0,)
    discount = DATABASE.Column(DATABASE.Float, default = 0)
    count = DATABASE.Column(DATABASE.Integer, default = 0)
    description = DATABASE.Column(DATABASE.String(500), default = "description")
    # 
    type_product = DATABASE.Column(DATABASE.String(50), default = "product_type")
    #
    